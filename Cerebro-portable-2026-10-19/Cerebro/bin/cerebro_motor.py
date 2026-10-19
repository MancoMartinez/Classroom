#!/usr/bin/env python3
"""Recuperación local compartida. Solo escribe el índice derivado .cerebro/.

Canales: BM25 de FTS5 y embeddings E5 locales, fusionados con RRF (k=60). Opcional: un
cross-encoder reordena los primeros N candidatos (modo rerank, activado por config solo si
la evaluación lo justifica). Capa epistémica: afirmaciones por oración con tipo, vigencia y
versiones reemplazadas (afirmaciones.py). El texto se indexa redactado (secretos.py).
"""
import argparse, collections, contextlib, datetime, hashlib, json, os, re, sqlite3, sys, unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import afirmaciones as af
import adjuntos
import secretos

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / '.cerebro'
DEFAULT_MODEL = 'intfloat/multilingual-e5-small'
DEFAULT_REVISION = '614241f622f53c4eeff9890bdc4f31cfecc418b3'
DEFAULTS = {
    'embedding_model': DEFAULT_MODEL,
    'embedding_revision': DEFAULT_REVISION,
    'reranker': {'enabled': False, 'model': 'cross-encoder/mmarco-mMiniLMv2-L12-H384-v1',
                 'revision': None, 'top_n': 30, 'max_length': 512, 'fusion': 'rrf'},
    'penalizacion_reemplazado': 0.5,
    'vigencia_volatil_dias': 3,
}
TICKET = re.compile(r'\b(?:RCS|RTS|ENG|OUTM|DATASCI|RETAILIT|RETAILDB)-\d+\b', re.I)
FOLDERS = ('inbox', 'bitacora', 'brain/memoria', 'investigaciones', 'flujos',
           'confluence/RTS-triage', 'Claude outputs')
STOP = set('a al algo como con de del donde el ella en es esta este esto la las lo los me mi no o para pero por que se si sin su sus te tiene un una y ya the a an and are as at be by for from how i in is it of on or that the this to was we what when with you'.split())
_model = None
_reranker = {}
_dense = {}
_qcache = collections.OrderedDict()


def config():
    cfg = json.loads(json.dumps(DEFAULTS))
    p = CACHE / 'config.json'
    if p.exists():
        try:
            user = json.loads(p.read_text())
            if 'embedding_model' in user and 'embedding_revision' not in user:
                user['embedding_revision'] = None  # modelo propio o local: sin revisión fija de Hugging Face
            for k, v in user.items():
                if isinstance(v, dict) and isinstance(cfg.get(k), dict):
                    cfg[k].update(v)
                else:
                    cfg[k] = v
        except (ValueError, OSError) as e:
            print('AVISO: .cerebro/config.json ilegible, uso valores por defecto: ' + str(e)[:120], file=sys.stderr)
    if os.environ.get('CEREBRO_RERANKER_MODEL'):
        # Prueba de otro cross-encoder sin tocar la configuración (eval_cerebro.py --reranker).
        cfg['reranker'].update(model=os.environ['CEREBRO_RERANKER_MODEL'], revision=None, enabled=True)
    return cfg


MODEL = config()['embedding_model']
REVISION = config()['embedding_revision']


def _adjuntos():
    """Apunta el extractor a la raíz activa (las pruebas la cambian) o lo apaga por entorno."""
    if os.environ.get('CEREBRO_SIN_ADJUNTOS'):
        return None
    adjuntos.ROOT = ROOT; adjuntos.SALIDA = CACHE / 'adjuntos'; adjuntos.INDICE = adjuntos.SALIDA / 'indice.json'
    return adjuntos


def norm(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')


def digest(s):
    return hashlib.sha256(s.encode()).hexdigest()


def source_db():
    p = Path(os.environ.get('CEREBRO_DB', ROOT / 'brain/sessions.db')).resolve()
    for flags in ('mode=ro', 'mode=ro&immutable=1'):
        con = None
        try:
            con = sqlite3.connect(p.as_uri() + '?' + flags, uri=True)
            con.execute('SELECT id FROM knowledge_chunks LIMIT 1').fetchone()
            if 'immutable' in flags:
                print('AVISO: SQLite leído con immutable; verificar journal antes de ingerir.', file=sys.stderr)
            return con
        except sqlite3.Error:
            if con: con.close()
    raise RuntimeError('No se pudo leer sessions.db; no se reemplaza un índice completo por uno parcial.')


def connection():
    CACHE.mkdir(exist_ok=True)
    c = sqlite3.connect(CACHE / 'retrieval.sqlite', timeout=60)
    c.row_factory = sqlite3.Row
    c.executescript('''
    CREATE TABLE IF NOT EXISTS sources(path TEXT PRIMARY KEY, signature TEXT, date TEXT);
    CREATE TABLE IF NOT EXISTS chunks(id INTEGER PRIMARY KEY, path TEXT, line INTEGER,
      end_line INTEGER, title TEXT, body TEXT, date TEXT, hash TEXT);
    CREATE INDEX IF NOT EXISTS chunk_path ON chunks(path);
    CREATE VIRTUAL TABLE IF NOT EXISTS search USING fts5(title,body,tokenize='unicode61 remove_diacritics 2');
    CREATE TABLE IF NOT EXISTS entities(ticket TEXT, chunk_id INTEGER, PRIMARY KEY(ticket,chunk_id));
    CREATE INDEX IF NOT EXISTS entity_chunk ON entities(chunk_id);
    CREATE TABLE IF NOT EXISTS vectors(hash TEXT, model TEXT, vector BLOB, PRIMARY KEY(hash,model));
    CREATE TABLE IF NOT EXISTS metadata(key TEXT PRIMARY KEY,value TEXT);
    CREATE TABLE IF NOT EXISTS claims(id INTEGER PRIMARY KEY, chunk_id INTEGER, path TEXT, line INTEGER,
      ticket TEXT, kind TEXT, strength TEXT, volatile INTEGER, text TEXT, hash TEXT,
      observed_at TEXT, recorded_at TEXT, valid_until TEXT);
    CREATE INDEX IF NOT EXISTS claim_chunk ON claims(chunk_id);
    CREATE INDEX IF NOT EXISTS claim_ticket ON claims(ticket);
    CREATE INDEX IF NOT EXISTS claim_path ON claims(path);
    CREATE TABLE IF NOT EXISTS superseded(path TEXT PRIMARY KEY, by TEXT);
    CREATE TABLE IF NOT EXISTS claims_done(path TEXT PRIMARY KEY, signature TEXT);
    ''')
    return c


def chunks(text, size=1100):
    """Segmentos con encabezado y líneas; cada línea larga se divide sin perder texto."""
    title, buf, start, length = '', [], 1, 0
    for line, value in enumerate(text.splitlines(), 1):
        heading = re.match(r'^#{1,6}\s+(.+)', value)
        if buf and (heading or length + len(value) > size):
            yield start, line - 1, title, '\n'.join(buf)
            buf, length = [], 0
        if heading: title = heading.group(1)
        for off in range(0, max(1, len(value)), size):
            piece = value[off:off+size]
            if not buf: start = line
            buf.append(piece); length += len(piece) + 1
            if length >= size:
                yield start, line, title, '\n'.join(buf)
                buf, length = [], 0
    if buf: yield start, len(text.splitlines()), title, '\n'.join(buf)


def database_documents():
    with contextlib.closing(source_db()) as c:
        tables = {r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        for row in c.execute('SELECT id,title,body,created_at FROM knowledge_chunks ORDER BY id'):
            yield f'db:knowledge_chunks/{row[0]}', row[1], row[2], datetime.datetime.fromtimestamp(row[3], datetime.timezone.utc).date().isoformat()
        links = collections.defaultdict(list)
        if 'item_links' in tables:
            for frm, to, chunk, kind in c.execute('SELECT from_item_id,to_item_id,to_chunk_id,link_type FROM item_links'):
                target = f'db:knowledge_chunks/{chunk}' if chunk else f'db:items/{to}'
                links[frm].append(f'Relación registrada ({kind}): {target}. Validar vigencia.')
        for row in c.execute('SELECT id,title,body,status FROM items'):
            yield f'db:items/{row[0]}', row[1], f'Estado histórico: {row[3]}\n{row[2] or ""}\n' + "\n".join(links[row[0]]), ''
        if 'meetings' in tables:
            for r in c.execute('SELECT id,title,created_at,summary,transcript,key_topics_json,action_items_json,decisions_json FROM meetings'):
                body = '\n\n'.join(f'{h}\n{v}' for h, v in zip(('Resumen', 'Transcripción', 'Temas', 'Acciones históricas', 'Decisiones'), r[3:]) if v)
                yield f'db:meetings/{r[0]}', r[1], body, datetime.datetime.fromtimestamp(r[2], datetime.timezone.utc).date().isoformat()
        if 'chat_conversations' in tables and 'chat_messages' in tables:
            for r in c.execute('SELECT id,title,summary,created_at FROM chat_conversations'):
                messages = c.execute('SELECT role,content FROM chat_messages WHERE conversation_id=? ORDER BY created_at,id', (r[0],)).fetchall()
                body = r[2] + '\n\n' + '\n\n'.join(role + ': ' + content for role, content in messages)
                yield f'db:chat_conversations/{r[0]}', r[1], body, datetime.datetime.fromtimestamp(r[3], datetime.timezone.utc).date().isoformat()
        if 'sessions' in tables:
            for r in c.execute('SELECT id,started_at,resume_text,jd_text,transcript FROM sessions'):
                yield f'db:sessions/{r[0]}', f'Sesión histórica {r[0]}', '\n\n'.join(r[2:]), datetime.datetime.fromtimestamp(r[1], datetime.timezone.utc).date().isoformat()
        if 'qa_pairs' in tables:
            for r in c.execute('SELECT id,created_at,detected_question,response FROM qa_pairs'):
                yield f'db:qa_pairs/{r[0]}', r[2], r[3], datetime.datetime.fromtimestamp(r[1], datetime.timezone.utc).date().isoformat()


def documents():
    """Fuentes con el cuerpo ya redactado: ningún secreto entra al índice ni sale por MCP."""
    for path, title, body, date in database_documents():
        yield path, title, secretos.redactar(body or ''), date
    paths = [p for folder in FOLDERS for p in (ROOT/folder).rglob('*') if p.is_file() and p.suffix.lower() in ('.md', '.txt')]
    paths += [ROOT/p for p in ('AGENTS.md', 'CLAUDE.md', 'MAPA.md', 'ESTADO.md', 'PASOS.md', 'tickets/DUDOSOS.md') if (ROOT/p).exists()]
    for p in sorted(paths):
        if not p.resolve().is_relative_to(ROOT) or p.is_symlink(): continue
        text = p.read_text(encoding='utf-8', errors='replace')
        date = re.search(r'20\d{2}-\d{2}-\d{2}', p.name)
        yield p.relative_to(ROOT).as_posix(), p.stem, secretos.redactar(text), date.group() if date else ''
    # Adjuntos: texto extraído (ya redactado) bajo la ruta original del archivo.
    if _adjuntos():
        for path, title, text, date in adjuntos.documentos():
            yield path, title, text, date


def _delete_path(c, path):
    c.execute('DELETE FROM search WHERE rowid IN (SELECT id FROM chunks WHERE path=?)', (path,))
    c.execute('DELETE FROM entities WHERE chunk_id IN (SELECT id FROM chunks WHERE path=?)', (path,))
    c.execute('DELETE FROM claims WHERE path=?', (path,))
    c.execute('DELETE FROM chunks WHERE path=?', (path,))


def _claims_for_chunk(c, cid, path, first, body, date, recorded, previous, dias):
    path_tickets = {t.upper() for t in TICKET.findall(path)}
    rows = []
    for line, kind, strength, volatile, text in af.extraer(body, first):
        own = {t.upper() for t in TICKET.findall(text)}
        tickets = own or path_tickets or {''}
        h = digest(path + '\n' + text)
        for t in tickets:
            rows.append((cid, path, line, t, kind, strength, volatile, text, h, date,
                         previous.get(h, recorded), af.vencimiento(date, dias) if volatile else ''))
    c.executemany('INSERT INTO claims(chunk_id,path,line,ticket,kind,strength,volatile,text,hash,observed_at,recorded_at,valid_until) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', rows)


def _bump(c):
    rev = int(dict(c.execute('SELECT key,value FROM metadata')).get('revision') or 0) + 1
    c.execute('INSERT OR REPLACE INTO metadata VALUES(?,?)', ('revision', str(rev)))


def sync():
    """Actualiza solo documentos cambiados, en una transacción; no modifica las fuentes."""
    try:
        if _adjuntos(): adjuntos.extraer(quiet=True, ocr=False)  # adjuntos nuevos sin OCR; las imágenes van por bin/adjuntos.py
    except Exception as e:
        print('AVISO: extracción de adjuntos omitida: ' + str(e)[:160], file=sys.stderr)
    dias = config()['vigencia_volatil_dias']
    now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
    with contextlib.closing(connection()) as c, c:
        previous = dict(c.execute('SELECT path,signature FROM sources'))
        meta = dict(c.execute('SELECT key,value FROM metadata'))
        seen, changed = set(), 0
        for path, title, body, date in documents():
            seen.add(path); signature = digest(title + '\n' + body)
            if previous.get(path) == signature: continue
            changed += 1
            prev_rec = dict(c.execute('SELECT hash,min(recorded_at) FROM claims WHERE path=? GROUP BY hash', (path,)))
            _delete_path(c, path)
            c.execute('INSERT OR REPLACE INTO sources VALUES(?,?,?)', (path, signature, date))
            for first, last, heading, part in chunks(body):
                if not part.strip(): continue
                label = title + (' | ' + heading if heading else '')
                h = digest(label + '\n' + part)
                cid = c.execute('INSERT INTO chunks(path,line,end_line,title,body,date,hash) VALUES(?,?,?,?,?,?,?)',
                                (path, first, last, label, part, date, h)).lastrowid
                c.execute('INSERT INTO search(rowid,title,body) VALUES(?,?,?)', (cid, label, part))
                for ticket in set(TICKET.findall(path + ' ' + part)):
                    c.execute('INSERT OR IGNORE INTO entities VALUES(?,?)', (ticket.upper(), cid))
                _claims_for_chunk(c, cid, path, first, part, date, now, prev_rec, dias)
            c.execute('INSERT OR REPLACE INTO claims_done VALUES(?,?)', (path, signature))
        removed = previous.keys() - seen
        for path in removed:
            _delete_path(c, path)
            c.execute('DELETE FROM sources WHERE path=?', (path,))
            c.execute('DELETE FROM claims_done WHERE path=?', (path,))
        if meta.get('claims_version') != str(af.VERSION):
            c.execute('DELETE FROM claims_done')
            c.execute('INSERT OR REPLACE INTO metadata VALUES(?,?)', ('claims_version', str(af.VERSION)))
        # Afirmaciones al día con cada fuente, aunque otra versión del motor haya reindexado
        # el documento: se reconstruyen desde chunks, sin releer las fuentes.
        pendientes = c.execute('SELECT s.path, s.signature FROM sources s LEFT JOIN claims_done d ON d.path=s.path WHERE d.signature IS NOT s.signature').fetchall()
        if pendientes:
            prev_rec = dict(c.execute('SELECT hash,min(recorded_at) FROM claims GROUP BY hash'))
            for p_ in pendientes:
                c.execute('DELETE FROM claims WHERE path=?', (p_['path'],))
                for r in c.execute('SELECT id,path,line,body,date FROM chunks WHERE path=?', (p_['path'],)).fetchall():
                    _claims_for_chunk(c, r['id'], r['path'], r['line'], r['body'], r['date'], now, prev_rec, dias)
                c.execute('INSERT OR REPLACE INTO claims_done VALUES(?,?)', (p_['path'], p_['signature']))
            changed += 1
        c.execute('DELETE FROM claims WHERE chunk_id NOT IN (SELECT id FROM chunks)')
        c.execute('DELETE FROM claims_done WHERE path NOT IN (SELECT path FROM sources)')
        if changed or removed or 'superseded_version' not in meta:
            c.execute('DELETE FROM superseded')
            fuentes = c.execute('SELECT path,date FROM sources').fetchall()
            c.executemany('INSERT INTO superseded VALUES(?,?)', af.versiones([tuple(r) for r in fuentes]).items())
            c.execute('INSERT OR REPLACE INTO metadata VALUES(?,?)', ('superseded_version', '1'))
            _bump(c)
        c.execute('INSERT OR REPLACE INTO metadata VALUES(?,?)', ('synced', datetime.datetime.now(datetime.timezone.utc).isoformat()))
    return changed


def encoder(download=False):
    global _model
    if _model is None:
        os.environ.setdefault('TOKENIZERS_PARALLELISM', 'false')
        from sentence_transformers import SentenceTransformer
        _model = SentenceTransformer(MODEL, revision=REVISION, trust_remote_code=False,
                                     local_files_only=not (download or os.environ.get('CEREBRO_DOWNLOAD')))
        _model.max_seq_length = 512
    return _model


def reranker(download=False):
    cfg = config()['reranker']
    key = (cfg['model'], cfg.get('revision'), cfg.get('dtype'))
    if key not in _reranker:
        os.environ.setdefault('TOKENIZERS_PARALLELISM', 'false')
        from sentence_transformers import CrossEncoder
        kwargs = {}
        if cfg.get('dtype'):
            import torch
            kwargs['model_kwargs'] = {'torch_dtype': getattr(torch, cfg['dtype'])}
        _reranker[key] = CrossEncoder(cfg['model'], revision=cfg.get('revision'), max_length=cfg.get('max_length', 512),
                                      trust_remote_code=False, **kwargs,
                                      local_files_only=not (download or os.environ.get('CEREBRO_DOWNLOAD')))
    return _reranker[key]


def build_vectors(download=True, refresh=True):
    import numpy as np
    if refresh: sync()
    with contextlib.closing(connection()) as c:
        rows = c.execute('SELECT hash,min(title) title,min(body) body FROM chunks WHERE hash NOT IN (SELECT hash FROM vectors WHERE model=?) GROUP BY hash', (MODEL,)).fetchall()
        if not rows: return status()
        model = encoder(download=download)
        for start in range(0, len(rows), 128):
            batch = rows[start:start+128]
            vecs = model.encode(['passage: ' + r['title'] + '\n' + r['body'] for r in batch], normalize_embeddings=True, batch_size=32, show_progress_bar=False)
            with c:
                c.executemany('INSERT OR REPLACE INTO vectors VALUES(?,?,?)', [(r['hash'], MODEL, np.asarray(v, dtype=np.float32).tobytes()) for r, v in zip(batch, vecs)])
                _bump(c)
            print(f'Vectores {min(start+128, len(rows))}/{len(rows)}', file=sys.stderr, flush=True)
    return status()


def status():
    cfg = config()
    with contextlib.closing(connection()) as c:
        kinds = dict(c.execute('SELECT kind,count(*) FROM claims GROUP BY kind'))
        hoy = datetime.date.today().isoformat()
        return {'sources': c.execute('SELECT count(*) FROM sources').fetchone()[0],
                'chunks': c.execute('SELECT count(*) FROM chunks').fetchone()[0],
                'vector_chunks': c.execute('SELECT count(*) FROM chunks WHERE hash IN (SELECT hash FROM vectors WHERE model=?)', (MODEL,)).fetchone()[0],
                'model': MODEL, 'revision': REVISION, 'synced': dict(c.execute('SELECT key,value FROM metadata')).get('synced'),
                'reranker': cfg['reranker'] if cfg['reranker']['enabled'] else 'desactivado',
                'afirmaciones': kinds,
                'estados_volatiles_vencidos': c.execute("SELECT count(*) FROM claims WHERE volatile=1 AND (valid_until='' OR valid_until<?)", (hoy,)).fetchone()[0],
                'documentos_reemplazados': c.execute('SELECT count(*) FROM superseded').fetchone()[0],
                'fragmentos_con_secreto_redactado': c.execute("SELECT count(*) FROM chunks WHERE body LIKE '%[SECRETO-REDACTADO:%'").fetchone()[0],
                'adjuntos': adjuntos.estado() if _adjuntos() else 'desactivados',
                'coverage': 'SQLite knowledge_chunks/items, reuniones, conversaciones, sesiones, Q&A y relaciones registradas; texto completo de inbox, bitácora, memorias, investigaciones, flujos, triage y Claude outputs; adjuntos xlsx, csv, pdf, docx, har y texto, e imágenes con OCR cuando se corre bin/adjuntos.py extraer. Fichas y espejo son vistas duplicadas; se leen por ticket.',
                'warning': 'Fechas son de documentos, no prueba de vigencia. Estado de tickets requiere Jira. Coaparición no demuestra causa común.'}


def lexical(c, query, limit=80):
    words = list(dict.fromkeys(w for w in re.findall(r'\w+', norm(query)) if len(w) > 1 and w not in STOP))
    if not words: return []
    expr = ' OR '.join('"' + w + '"' for w in words[:40])
    return [r[0] for r in c.execute('SELECT rowid FROM search WHERE search MATCH ? ORDER BY bm25(search,3.0,1.0) LIMIT ?', (expr, limit))]


def dense_matrix(c):
    """Matriz de vectores en memoria del proceso; se recarga solo si el índice cambió."""
    import numpy as np
    meta = dict(c.execute('SELECT key,value FROM metadata'))
    key = (meta.get('revision'), c.execute('SELECT count(*) FROM vectors WHERE model=?', (MODEL,)).fetchone()[0])
    if _dense.get('key') != key:
        rows = c.execute('SELECT ch.id,v.vector FROM chunks ch JOIN vectors v ON v.hash=ch.hash AND v.model=?', (MODEL,)).fetchall()
        _dense.clear()
        _dense['key'] = key
        _dense['ids'] = [r['id'] for r in rows]
        _dense['matrix'] = np.stack([np.frombuffer(r['vector'], dtype=np.float32) for r in rows]) if rows else None
    return _dense['ids'], _dense['matrix']


def embed_query(text):
    if text in _qcache:
        _qcache.move_to_end(text); return _qcache[text]
    v = encoder().encode(['query: ' + text], normalize_embeddings=True, show_progress_bar=False)[0]
    _qcache[text] = v
    if len(_qcache) > 512: _qcache.popitem(last=False)
    return v


def dense(c, query, limit=80):
    import numpy as np
    ids, matrix = dense_matrix(c)
    if matrix is None: return [], None
    scores = matrix @ embed_query(query)
    return [ids[int(i)] for i in np.argsort(-scores)[:limit]], scores


def claim_summary(c, ids):
    """{chunk_id: {'tipos': Counter, 'afirmaciones': [...], 'volatil': (observado, vigente)}}"""
    out = {}
    if not ids: return out
    hoy = datetime.date.today().isoformat()
    marks = ','.join('?' * len(ids))
    for r in c.execute(f'SELECT chunk_id,line,kind,strength,volatile,text,observed_at,valid_until FROM claims WHERE chunk_id IN ({marks}) GROUP BY chunk_id,line,kind,text', list(ids)):
        d = out.setdefault(r['chunk_id'], {'tipos': collections.Counter(), 'afirmaciones': [], 'volatil': None})
        d['tipos'][r['kind']] += 1
        d['afirmaciones'].append({'linea': r['line'], 'tipo': r['kind'], 'fuerza': r['strength'], 'texto': r['text'][:220]})
        if r['volatile']:
            vig = af.vigente(r['valid_until'], hoy)
            if d['volatil'] is None or (r['observed_at'] or '') > (d['volatil']['observado'] or ''):
                d['volatil'] = {'observado': r['observed_at'], 'vigente': vig}
    rank = {'descartada': 0, 'correccion': 1, 'hipotesis': 2, 'confirmada': 3, 'compromiso': 4, 'estado': 5}
    fz = {'etiqueta': 0, 'heredada': 1, 'texto': 2}
    for d in out.values():
        d['afirmaciones'].sort(key=lambda a: (fz[a['fuerza']], rank.get(a['tipo'], 9)))
        d['afirmaciones'] = d['afirmaciones'][:3]
    return out


def solo_especulativo(s):
    """Fragmento cuyas afirmaciones no volátiles son todas hipótesis o descartadas."""
    if not s: return False
    t = s['tipos']
    firmes = t['confirmada'] + t['correccion']
    return firmes == 0 and (t['hipotesis'] + t['descartada']) > 0


def search(query, limit=8, mode=None, refresh=True, hechos=False, variantes=None):
    if not query.strip(): raise ValueError('Consulta vacía')
    cfg = config()
    mode = mode or ('rerank' if cfg['reranker']['enabled'] else 'hybrid')
    if mode not in ('bm25', 'hybrid', 'rerank'): raise ValueError('Modo inválido: ' + mode)
    if refresh: sync()
    if TICKET.fullmatch(query.strip()): return ticket_packet(query.strip())
    warnings = []
    if mode != 'bm25':
        # Tras la instalación inicial, las notas nuevas reciben vector sin otra ingestión.
        try: build_vectors(download=False, refresh=False)
        except (ImportError, OSError, RuntimeError) as e:
            warnings.append('No se actualizaron vectores: ' + str(e)[:180])
    # Multi-consulta: la consulta original más reformulaciones (otro idioma, término técnico).
    # Cada variante aporta sus dos canales y RRF los fusiona; el reranker juzga con la original.
    consultas = [query] + [v for v in dict.fromkeys(x.strip() for x in (variantes or [])) if v and v != query][:4]
    with contextlib.closing(connection()) as c:
        channels = [lexical(c, q) for q in consultas]
        if mode != 'bm25':
            try:
                for q in consultas:
                    ranked, _ = dense(c, q)
                    if ranked: channels.append(ranked)
                if len(channels) == len(consultas): warnings.append('Sin vectores; ejecuta cerebro_motor.py index --vectors. Resultado solo BM25.')
                missing = c.execute('SELECT count(*) FROM chunks WHERE hash NOT IN (SELECT hash FROM vectors WHERE model=?)', (MODEL,)).fetchone()[0]
                if missing: warnings.append(f'{missing} fragmentos nuevos sin vector, disponibles por BM25.')
            except (ImportError, OSError, RuntimeError) as e:
                warnings.append('Canal vectorial no disponible: ' + str(e)[:180])
        points = collections.Counter()
        for channel in channels:
            for rank, cid in enumerate(channel, 1): points[cid] += 1 / (60 + rank)
        if not points:
            return {'query': query, 'mode': mode, 'warnings': warnings, 'results': [], 'instruction': 'Sin resultados. Reformula con el término técnico o en inglés.'}
        rows = {r['id']: dict(r) for r in c.execute(f'SELECT * FROM chunks WHERE id IN ({",".join("?" * len(points))})', list(points))}
        reemplazos = dict(c.execute(f'SELECT path,by FROM superseded WHERE path IN ({",".join("?" * len(rows))})', [r['path'] for r in rows.values()]))
        resumen = claim_summary(c, list(points))
        pen = cfg['penalizacion_reemplazado']
        for cid in points:
            if rows[cid]['path'] in reemplazos: points[cid] *= pen
        order = [cid for cid, _ in points.most_common()]
        if hechos:
            order = [cid for cid in order if not solo_especulativo(resumen.get(cid))
                     and not (resumen.get(cid, {}).get('volatil') and not resumen[cid]['volatil']['vigente'] and sum(resumen[cid]['tipos'].values()) == resumen[cid]['tipos']['estado'])]
        if mode == 'rerank':
            n = max(limit, int(cfg['reranker']['top_n']))
            head, tail = order[:n], order[n:]
            try:
                scores = reranker().predict([(query, rows[i]['title'] + '\n' + rows[i]['body'][:2000]) for i in head], batch_size=int(cfg['reranker'].get('batch_size', 16)), show_progress_bar=False)
                ce_order = [cid for _, cid in sorted(zip(scores, head), key=lambda x: -float(x[0]))]
                if cfg['reranker'].get('fusion', 'rrf') == 'rrf':
                    # El cross-encoder vota como un canal más contra el orden fusionado: con
                    # variantes, reemplazar el orden descartaba lo que hallaron las reformulaciones.
                    voto = collections.Counter()
                    for canal in (head, ce_order):
                        for rank, cid in enumerate(canal, 1): voto[cid] += 1 / (60 + rank)
                    ce_order = [cid for cid, _ in voto.most_common()]
                order = ce_order + tail
            except (ImportError, OSError, RuntimeError, ValueError) as e:
                warnings.append('Reranker no disponible, orden híbrido. Descárgalo una vez con: bin/cerebro index --reranker. Detalle: ' + str(e)[:120])
        out = []; seen = set(); per_path = collections.Counter(); vencidos = 0
        for cid in order:
            r = dict(rows[cid])
            content_hash = digest(norm(re.sub(r'\s+', ' ', r['body'])))
            if content_hash in seen or per_path[r['path']] >= 2: continue
            seen.add(content_hash); per_path[r['path']] += 1
            r['score'] = round(points[cid], 5); r.pop('hash')
            s = resumen.get(cid)
            if s:
                r['epistemico'] = dict(s['tipos'])
                r['afirmaciones'] = s['afirmaciones']
                if s['volatil']:
                    r['estado_volatil'] = s['volatil']
                    vencidos += not s['volatil']['vigente']
            if r['path'] in reemplazos: r['reemplazado_por'] = reemplazos[r['path']]
            out.append(r)
            if len(out) >= max(1, min(limit, 30)): break
    if vencidos:
        warnings.append(f'{vencidos} resultados citan estado, fase o assignee de Jira con vigencia vencida. Consulta Jira antes de repetirlo.')
    if any('reemplazado_por' in r for r in out):
        warnings.append('Hay versiones reemplazadas en los resultados; lee la versión indicada en reemplazado_por.')
    return {'query': query, 'variantes': consultas[1:], 'mode': mode, 'hechos': hechos, 'warnings': warnings, 'results': out,
            'instruction': 'Lee las fuentes antes de concluir. Distingue hipótesis, correcciones y confirmaciones. Ningún resultado semántico prueba causalidad.'}


def ticket_claims(c, ticket, limit=8):
    hoy = datetime.date.today().isoformat()
    rows = c.execute('SELECT path,line,kind,strength,volatile,text,observed_at,valid_until FROM claims WHERE ticket=? GROUP BY path,line,kind,text ORDER BY observed_at DESC, path DESC, line DESC', (ticket,)).fetchall()
    grupos = collections.defaultdict(list)
    ultimo_firme = ''
    for r in rows:
        if r['kind'] in ('descartada', 'correccion', 'confirmada') and r['strength'] != 'texto':
            ultimo_firme = max(ultimo_firme, r['observed_at'] or '')
    for r in rows:
        item = {'fuente': f"{r['path']}:{r['line']}", 'observado': r['observed_at'], 'fuerza': r['strength'], 'texto': r['text'][:260]}
        if r['volatile']:
            item['vigente'] = af.vigente(r['valid_until'], hoy)
            grupos['estados_jira'].append(item)
            if r['kind'] == 'estado': continue
        if r['kind'] == 'hipotesis' and ultimo_firme and (r['observed_at'] or '') < ultimo_firme:
            item['posiblemente_superada'] = f'hay una confirmación, corrección o descarte posterior ({ultimo_firme})'
        grupos[r['kind']].append(item)
    fz = {'etiqueta': 0, 'heredada': 1, 'texto': 2}
    return {k: sorted(v, key=lambda x: (-(int(re.sub(r'\D', '', x['observado'] or '0') or 0)), fz[x['fuerza']]))[:limit] for k, v in grupos.items()}


def ticket_packet(ticket):
    ticket = ticket.upper()
    if not TICKET.fullmatch(ticket): raise ValueError('ID de ticket inválido')
    with contextlib.closing(connection()) as c:
        rows = c.execute('SELECT DISTINCT ch.* FROM chunks ch JOIN entities e ON e.chunk_id=ch.id WHERE e.ticket=? ORDER BY ch.date DESC,ch.path,ch.line DESC', (ticket,)).fetchall()
        reemplazos = dict(c.execute('SELECT path,by FROM superseded'))
        direct = []; references = []; related = collections.defaultdict(set)
        for row in rows:
            r = dict(row); r.pop('hash')
            target = direct if ticket in {t.upper() for t in TICKET.findall(r['path'])} else references
            target.append(r)
            for other in TICKET.findall(r['body']):
                if other.upper() != ticket: related[other.upper()].add(r['path'])
        # ponytail: coaparición documental, no grafo causal; validar cada relación al leer la fuente.
        bypath = collections.defaultdict(list)
        for r in direct:
            if r['path'] not in reemplazos: bypath[r['path']].append(r)
        selected = []
        for path, parts in sorted(bypath.items(), key=lambda x: (not x[0].startswith("bitacora/"), -int(re.sub(r"\D", "", x[1][0]["date"]) or 0))):
            for part in parts[:2]:
                part['source_kind'] = 'borrador o nota local, envío no verificado' if path.startswith('inbox/') else 'historia local, contrastar vigencia'
                selected.append(part)
            if len(selected) >= 12: break
        paths = list(dict.fromkeys(r['path'] for r in direct + references))
        claims = ticket_claims(c, ticket)
    ficha = ROOT/'tickets'/f'{ticket}.md'
    return {'ticket': ticket, 'found': bool(rows or ficha.exists()), 'direct_evidence': selected,
            'afirmaciones': claims,
            'source_paths': paths[:80], 'sources_total': len(paths), 'reference_evidence': references[:3],
            'versiones_reemplazadas': {p: reemplazos[p] for p in paths if p in reemplazos},
            'related_mentions': [{'ticket': t, 'sources': sorted(p)[:3], 'kind': 'coaparición, verificar relación'} for t, p in sorted(related.items(), key=lambda x: -len(x[1]))[:15]],
            'ficha': str(ficha) if ficha.exists() else None,
            'instruction': 'Prioriza la bitácora completa y notas recientes. La ficha puede estar atrasada. Estado, assignee y fase salen de Jira en vivo, nunca de estados_jira. Una hipótesis marcada posiblemente_superada exige leer la fuente posterior antes de repetirla.'}


def read_source(path, start=1, count=80):
    start = max(1, int(start)); count = max(1, min(int(count), 250))
    m = re.fullmatch(r'db:(knowledge_chunks|items|meetings|chat_conversations|sessions|qa_pairs)/(\d+)', path)
    if m:
        doc = next((r for r in database_documents() if r[0] == path), None)
        if not doc: raise ValueError('Fuente inexistente')
        text = doc[2] or ''
    else:
        p = (ROOT/path).resolve()
        _adjuntos()
        extraido = (adjuntos.SALIDA / (path + '.txt')).resolve()
        if p.is_relative_to(ROOT) and extraido.is_relative_to(adjuntos.SALIDA.resolve()) and extraido.is_file() and any(p.is_relative_to((ROOT/f).resolve()) for f in adjuntos.CARPETAS):
            text = extraido.read_text(encoding='utf-8')
        else:
            allowed = any(p.is_relative_to((ROOT/f).resolve()) for f in FOLDERS + ('tickets', 'brain/markdown')) or p in [ROOT/f for f in ('AGENTS.md', 'CLAUDE.md', 'MAPA.md', 'ESTADO.md', 'PASOS.md')]
            if not p.is_relative_to(ROOT) or not allowed or p.suffix.lower() not in ('.md', '.txt'): raise ValueError('Ruta fuera del corpus permitido')
            text = p.read_text(encoding='utf-8')
    lines = secretos.redactar(text).splitlines()
    return {'path': path, 'start': start, 'total_lines': len(lines), 'text': '\n'.join(f'{i}: {v}' for i, v in enumerate(lines[start-1:start-1+count], start))}


def main():
    p = argparse.ArgumentParser(description=__doc__); s = p.add_subparsers(dest='cmd', required=True)
    b = s.add_parser('index'); b.add_argument('--vectors', action='store_true'); b.add_argument('--reranker', action='store_true', help='descarga y prueba el cross-encoder configurado')
    q = s.add_parser('search'); q.add_argument('query'); q.add_argument('--mode', choices=['bm25', 'hybrid', 'rerank']); q.add_argument('--limit', type=int, default=8); q.add_argument('--hechos', action='store_true')
    t = s.add_parser('ticket'); t.add_argument('key')
    r = s.add_parser('read'); r.add_argument('path'); r.add_argument('--start', type=int, default=1); r.add_argument('--count', type=int, default=80)
    s.add_parser('status'); a = p.parse_args()
    if a.cmd == 'index':
        if a.reranker:
            reranker(download=True).predict([('prueba', 'prueba')]); result = {'reranker': config()['reranker'], 'descargado': True}
        else:
            result = build_vectors() if a.vectors else {'changed': sync(), **status()}
    elif a.cmd == 'search': result = search(a.query, a.limit, a.mode, hechos=a.hechos)
    elif a.cmd == 'ticket': sync(); result = ticket_packet(a.key)
    elif a.cmd == 'read': result = read_source(a.path, a.start, a.count)
    else: result = status()
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__': main()
