#!/usr/bin/env python3
"""Mapa de relaciones de Cerebro: ticket, cliente, sistema, familia de causa y persona.

Cada arista guarda su procedencia y su confianza:
  documentada   lista explícita en investigaciones/, confluence/RTS-triage/INDICE.md o título de Jira
  mencion       el documento del ticket nombra la entidad (cuenta de menciones como peso)
  inferida      clasificación cero-disparo con E5: título de Jira y causas confirmadas del ticket
                contra la descripción de cada familia; trae su coseno y se valida contra las
                familias documentadas (ver validar)

    python3 bin/relaciones.py construir          reconstruye el grafo en .cerebro/retrieval.sqlite
    python3 bin/relaciones.py consultar "archivo malo que tumbó la carga" --hacia cliente
    python3 bin/relaciones.py vecinos "ADUSA"
    python3 bin/relaciones.py validar            precisión de la familia inferida contra la documentada

El grafo es una ayuda para encontrar precedentes. Una arista no prueba causa común; se lee la evidencia.
"""
import argparse, collections, contextlib, json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cerebro_motor as b

VERSION = 1
TICKET = b.TICKET

CLIENTES = {  # alias -> nombre canónico. Ampliable a mano; lo no listado queda con su prefijo de título.
    'ADUSA': ['adusa', 'ahold delhaize', 'ahold-delhaize', 'ahold', 'ahl', 'delhaize', 'dhz', 'food lion', 'stop & shop', 'stop and shop', 'hannaford', 'giant food', 'giant'],
    'Stater Bros': ['stater bros', 'staterbros', 'stater bro'],
    'Vitamin Shoppe': ['vitamin shoppe'],
    'Nordstrom': ['nordstrom'], 'TJX': ['tjx', 'tjxeu', 'tjxc', 'tjx eu'], 'The Home Depot': ['the home depot', 'home depot', 'thd'],
    'Urban Outfitters': ['urban outfitters', 'urban'], 'Starbucks': ['starbucks', 'sbux', 'sbx', 'sbx na'], "Kohl's": ["kohl's", 'kohls'],
    'Guess': ['guess'], 'Nike': ['nike'], 'Tailored Brands': ['tailored brands'], 'Alo Yoga': ['alo yoga', 'alo'],
    'Vallarta': ['vallarta'], 'Boot Barn': ['boot barn'], 'Myer': ['myer'], 'ICA': ['ica'], 'Sainsbury': ["sainsbury's", 'sainsbury'],
    'SpartanNash': ['spartannash', 'spartan nash'], 'Walmart': ['wal-mart', 'walmart', 'wmt'], 'Claire\'s': ["claire's", 'claires'],
    'GPC': ['gpc', 'genuine parts', 'gen parts'], 'PacSun': ['pacsun', 'pseb', 'pac sun'], 'Chanel': ['chanel'], '3Sixty': ['3sixty'],
    'Advance Auto Parts': ['advance auto parts', 'aap'], 'Goodwill': ['goodwill sacramento', 'goodwillsc', 'goodwill cc', 'goodwill'],
    'VF Corp': ['vf corp', 'vfc'], 'Wakefern': ['wakefern'], 'Big Y': ['big y', 'big y foods', 'byf'], 'Mattress Firm': ['mattress firm'],
    'Santikos': ['santikos'], 'Blain\'s': ["blain's"], 'NEXCOM': ['nexcom'], 'Wild Fork': ['wild fork'], 'CWH': ['cwh', 'chemist warehouse'],
    'Lululemon': ['lululemon', 'llu'], 'Winn-Dixie': ['winn-dixie'], 'WinCo': ['winco'], 'Kinney Drugs': ['kinney'], 'Estee Lauder': ['estee lauder'],
    'PPG': ['ppg'], 'Bunnings': ['bunnings'], 'Prada': ['prada'], 'Skechers': ['skechers'], 'Torrid': ['torrid'], 'PVH': ['pvh'],
}
SISTEMAS = {
    'LPMS': r'\blpms\b', 'Incident': r'\bincident\b', 'Secure': r'\bsecure\s*(5|store|incident|ebr)?\b', 'EBR': r'\bebr\b',
    'Izenda': r'\bizenda\b', 'Smart Alerts': r'smart\s*alerts?|smartalert', 'SSO/SAML': r'\bsso\b|\bsaml\b|\bidp\b',
    'Cloudflare/WAF': r'cloudflare|\bwaf\b|ray id|you have been blocked', 'Snowflake': r'snowflake', 'Greenplum/ARDM': r'greenplum|\bgp\d+\b|\bardm',
    'pyardm': r'pyardm', 'SnowTime': r'snowtime', 'Work Items/WISC': r'work ?items?|workview|\bwisc\b', 'Control Panel': r'control panel',
    'Ingestion API': r'ingestion api|event hub', 'Engage': r'\bengage\b', 'APIS': r'\bapis\b', 'Screen Designer': r'screen designer',
    'HATR/NotificationEmail': r'hatr|notificationemail', 'Key Vault': r'key ?vault', 'Zscaler': r'zscaler', 'Talos': r'\btalos\b', 'Grafana': r'grafana',
    'Azure DevOps': r'azure devops|\bado\b|pipeline', 'netTrack': r'nettrack',
}
PERSONAS = ['Juan Martinez', 'Viraj Kansara', 'Diego Buelvas', 'Sebastian Rueda', 'Edwin Garzon', 'Luis Hernandez', 'Sebastian Garces',
            'Enrique Jimenez', 'Nikita Rathore', 'Vedant Shirude', 'Bikash Kumar', 'Gulshan Kumar', 'Megha Rathi', 'Camila Cortes',
            'Shandana Khan', 'Matthew Kamminga', 'Kiran Vadday', 'Peyman Motlagh', 'Ryan Barlow', 'Vlad Bogus', 'Jon Morgan',
            'Chris Rippingale', 'Joe Austin', 'Aimee Wadsworth', 'Mohammed Mutahhar', 'Colton Neal', 'Carl Costelow', 'Matthew Everett',
            'Tatiana Barcenas', 'Thomas Walker', 'Paul Marderosian', 'Tyrone Whitney', 'Paula Dotson', 'Chris Orth', 'Ian Williams',
            'Jim Cosseboom', 'Leigh Ann', 'Anil P']
ALIAS_PERSONA = {'Matt Kamminga': 'Matthew Kamminga'}

# Familias de causa. Las que tienen 'tickets' están documentadas en investigaciones/ o en el índice de Confluence.
FAMILIAS = {
    'smart-alerts-filtros': {'desc': 'Smart Alert no dispara tras editar tipos de auditoría: ManageSmartAlerts no regenera FiltersSQL. Smart alert not triggering after editing audit types.', 'tickets': ['RCS-27407']},
    'smart-alerts-envio': {'desc': 'Smart Alerts no salen, no se generan o llegan tarde: SendSmartAlert timeout, SmartAlertProcess, frontera UTC, alerta de reasignación borrada, TempArea. Smart alerts not sending, not generating, emails not received.', 'tickets': ['RCS-28452', 'RCS-28294', 'RCS-28795', 'RCS-28106', 'RCS-29123', 'RCS-29026', 'RCS-29145', 'RCS-29103', 'RCS-29195', 'RCS-28915', 'RCS-28465', 'RCS-28534', 'ENG-9486']},
    'notificaciones-hatr': {'desc': 'Job HATR NotificationEmail_Scheduled detenido por tenant: la notificación queda en la app y no sale el correo. Notification emails not sent, email forwarding not working.', 'tickets': ['RCS-29021', 'RCS-29350']},
    'sso-login': {'desc': 'Usuarios no pueden entrar: SSO, SAML, claims, IdP del cliente, login error, no access, sign on error, usuario no aprovisionado. Users cannot log in.', 'tickets': ['RCS-28779', 'RCS-28631', 'RCS-28240', 'RCS-28693', 'RCS-28984', 'RCS-28442']},
    'waf-bloqueo': {'desc': 'Pantalla Sorry you have been blocked: Cloudflare WAF bloquea al usuario o al egress del proxy Zscaler; Ray ID. Users blocked by Cloudflare.', 'tickets': ['RCS-28556', 'RCS-28059', 'RCS-28289', 'RCS-29023', 'RCS-28057']},
    'carga-datos': {'desc': 'Carga de transacciones incompleta o fallida: archivos que llegaron y no cargaron, huecos por hora, feed detenido, zip o XML malo, filas de tender faltantes, pocas tiendas cargadas. Transaction data load incomplete, files sent but not loaded, data feed stopped.', 'tickets': ['RCS-28281', 'RCS-28547', 'RCS-29130', 'RCS-28756', 'RCS-29179', 'RCS-29135', 'RCS-29104']},
    'mapeo-campos': {'desc': 'Campo mal mapeado o vacío en el recibo o la búsqueda: mapping ARDM, flat receipt, campo faltante desde una fecha, regresión de mapeo. Field mapping missing or incorrect on receipt.', 'tickets': ['RCS-28638', 'RCS-28612', 'RCS-28581', 'RCS-27389', 'RCS-28718', 'RCS-28747', 'RCS-28725', 'RCS-28838']},
    'catalogo-campos-secure': {'desc': 'Rename de columnas ARDM v1 a v2 sin resync del catálogo de campos de Secure: búsquedas con error Sorry but we could not process your search. Search error after column rename.', 'tickets': ['RCS-28606', 'RTS-206610', 'RTS-206268', 'RTS-206667', 'RCS-28873']},
    'binding-obsoleto': {'desc': 'Binding de campo por posición o por etiqueta que queda obsoleto al editar display fields: chart o gráfico roto. Chart breaks after editing display fields.', 'tickets': ['RCS-28843', 'RCS-28841', 'RTS-206261']},
    'synopsis-display-fields': {'desc': 'Campo usado en el Synopsis que falta en los Display Fields de la búsqueda. Synopsis field missing from display fields.', 'tickets': ['RTS-205361', 'RTS-205224']},
    'duplicados-join': {'desc': 'Duplicados por join a una tabla de referencia sin dedup aguas arriba: filas duplicadas, montos inflados. Duplicate rows from join without dedup.', 'tickets': ['RCS-28077', 'RCS-28751', 'RCS-28746']},
    'excel-export-vacio': {'desc': 'Exportación a Excel con campos vacíos o cero filas: tipos Double en campos de texto. Excel export not populating fields.', 'tickets': ['RCS-26238', 'RCS-23141', 'RCS-28339']},
    'izenda-reportes': {'desc': 'Izenda: reportes que no exportan o descargan, 502, campos deshabilitados, visor y entrega leen fuentes distintas. Izenda report export fails.', 'tickets': ['RCS-28482', 'RCS-28872', 'RCS-27598', 'ENG-5649', 'RCS-28021', 'RCS-28413']},
    'permisos-jerarquia': {'desc': 'Usuario sin tiendas o con permisos incorrectos: jerarquía de ubicaciones, LHUA, distrito, security level, división. User cannot see stores, permissions issue.', 'tickets': ['RCS-28519', 'RCS-28852', 'RCS-28023', 'RCS-28093', 'ENG-7312']},
    'identidad-migracion': {'desc': 'Unificación de julio 2026: usuarios migrados ausentes de membership.Users, casos viejos invisibles, owner o creator en blanco. Migrated users missing after platform unification.', 'tickets': ['RCS-28364', 'RCS-28379', 'RCS-28177', 'ENG-7319', 'ENG-7366']},
    'adjuntos': {'desc': 'Adjuntos que no suben o no abren: archivos grandes, video, Forbidden, bucket de adjuntos. Attachment upload or download fails.', 'tickets': ['RCS-28535', 'ENG-7181', 'RCS-28167', 'RCS-28305', 'RCS-28331', 'RCS-28351', 'RCS-28710', 'ENG-9699']},
    'work-items': {'desc': 'Work items que no se generan, salen en cero o no se regeneran: ventana de sub-búsqueda anclada a la fecha de ejecución, cutover a SnowTime. Work items not producing results.', 'tickets': ['RCS-28671', 'RCS-29205', 'RCS-29206', 'RCS-29207', 'RCS-28170', 'RCS-28352', 'RCS-28632']},
    'rendimiento': {'desc': 'Lentitud y timeouts: regresión de plan SQL, sesión de ASP clásico bloqueada, 502 intermitente, tiempos de carga. Slowness, timeouts, degraded performance.', 'tickets': ['RCS-28256', 'RCS-27549', 'RCS-28881', 'RCS-28407', 'RCS-28072', 'RCS-28075', 'RCS-28084']},
    'pantallas-rotas': {'desc': 'Pantallas rotas o 404 tras la migración: rebuild por Screen Designer. Screen not rendering correctly.', 'tickets': ['RCS-28533', 'RCS-28334']},
}


def norm(s):
    return b.norm(s).strip()


def _alias():
    out = []
    for canon, aliases in CLIENTES.items():
        for a in aliases:
            out.append((norm(a), canon))
    return sorted(out, key=lambda x: -len(x[0]))


def cliente_de_titulo(titulo, tabla):
    t = norm(titulo)
    for a, canon in tabla:
        if re.match(r'^[\[(]?' + re.escape(a) + r'\b', t):
            return canon
    pref = re.split(r'\s*[-–:|]\s*', titulo.strip(), 1)[0].strip(' [()')
    return pref if 2 <= len(pref) <= 40 and not re.search(r'grafana|snowtime|appriss internal', pref, re.I) else None


def construir():
    import numpy as np
    tit = json.loads((b.ROOT / 'cola/titulos-jira.json').read_text()) if (b.ROOT / 'cola/titulos-jira.json').exists() else {}
    tabla = _alias()
    aristas = collections.defaultdict(lambda: {'peso': 0, 'evidencia': [], 'confianza': 'mencion', 'score': None})

    def add(t, tipo, valor, conf, ev, peso=1, score=None):
        a = aristas[(t, tipo, valor)]
        a['peso'] += peso
        if len(a['evidencia']) < 5 and ev not in a['evidencia']:
            a['evidencia'].append(ev)
        orden = {'documentada': 0, 'inferida': 1, 'mencion': 2}
        if orden[conf] < orden[a['confianza']]:
            a['confianza'] = conf
        if score is not None:
            a['score'] = score

    for t, titulo in tit.items():
        c = cliente_de_titulo(titulo, tabla)
        if c:
            add(t, 'cliente', c, 'documentada', 'titulo Jira: ' + titulo[:120])
    indice = b.ROOT / 'confluence/RTS-triage/INDICE.md'
    if indice.exists():
        for linea in indice.read_text(encoding='utf-8').splitlines():
            m = re.match(r'\|\s*((?:RCS|RTS)-\d+)\s*\|\s*([^|]+)\|', linea)
            if m:
                nombre = m.group(2).split('/')[0].strip()
                canon = next((cn for a, cn in tabla if norm(nombre).startswith(a)), nombre)
                add(m.group(1), 'cliente', canon, 'documentada', 'confluence/RTS-triage/INDICE.md')
    for fam, d in FAMILIAS.items():
        for t in d['tickets']:
            add(t, 'familia', fam, 'documentada', 'taxonomía de investigaciones/ y Confluence')

    sis_rx = {k: re.compile(v, re.I) for k, v in SISTEMAS.items()}
    per_rx = {p: re.compile(r'\b' + re.escape(p) + r'\b') for p in PERSONAS + list(ALIAS_PERSONA)}
    with contextlib.closing(b.connection()) as c:
        filas = c.execute('SELECT e.ticket, ch.path, ch.line, ch.title, ch.body FROM entities e JOIN chunks ch ON ch.id=e.chunk_id').fetchall()
        for r in filas:
            t = r['ticket']
            if t not in (r['path'] + ' ' + r['title']).upper():
                continue  # solo documentos del propio ticket; una mención suelta no basta
            texto = r['title'] + '\n' + r['body']
            ev = f"{r['path']}:{r['line']}"
            for k, rx in sis_rx.items():
                n = len(rx.findall(texto))
                if n: add(t, 'sistema', k, 'mencion', ev, n)
            for p, rx in per_rx.items():
                n = len(rx.findall(texto))
                if n: add(t, 'persona', ALIAS_PERSONA.get(p, p), 'mencion', ev, n)
            nt = norm(texto)
            for a, canon in tabla:
                if len(a) >= 4 and re.search(r'\b' + re.escape(a) + r'\b', nt):
                    add(t, 'cliente', canon, 'mencion', ev, 1)
        # Familia inferida: título + causas confirmadas del ticket contra la descripción de cada familia.
        causas = collections.defaultdict(list)
        for r in c.execute("SELECT ticket, text FROM claims WHERE kind IN ('confirmada','correccion') AND strength!='texto' AND ticket!=''"):
            if len(causas[r['ticket']]) < 4:
                causas[r['ticket']].append(r['text'][:300])
        tickets = sorted(set(tit) | set(causas))
        textos = [(t, (tit.get(t, '') + '. ' + ' '.join(causas.get(t, []))).strip()) for t in tickets if not re.match(r'^\s*\[(grafana|snowtime)\]', tit.get(t, ''), re.I)]
        textos = [(t, x) for t, x in textos if len(x) > 15]
        enc = b.encoder()
        fam = list(FAMILIAS)
        P = enc.encode(['passage: ' + FAMILIAS[f]['desc'] for f in fam], normalize_embeddings=True, show_progress_bar=False)
        Q = enc.encode(['query: ' + x for _, x in textos], normalize_embeddings=True, show_progress_bar=False, batch_size=32)
        S = Q @ P.T
        umbral = umbral_inferencia()
        for (t, _), fila in zip(textos, S):
            i = int(np.argmax(fila)); orden = np.sort(fila)
            if fila[i] >= umbral['coseno'] and fila[i] - orden[-2] >= umbral['margen']:
                add(t, 'familia', fam[i], 'inferida', 'clasificación E5 cero-disparo', 1, round(float(fila[i]), 4))
        with c:
            c.execute('DROP TABLE IF EXISTS relaciones')
            c.execute('CREATE TABLE relaciones(ticket TEXT, tipo TEXT, valor TEXT, peso INTEGER, confianza TEXT, score REAL, evidencia TEXT)')
            c.execute('CREATE INDEX rel_ticket ON relaciones(ticket)'); c.execute('CREATE INDEX rel_valor ON relaciones(tipo, valor)')
            c.executemany('INSERT INTO relaciones VALUES(?,?,?,?,?,?,?)', [(t, tp, v, a['peso'], a['confianza'], a['score'], json.dumps(a['evidencia'], ensure_ascii=False)) for (t, tp, v), a in aristas.items()])
            rev = dict(c.execute('SELECT key,value FROM metadata')).get('revision')
            c.execute('INSERT OR REPLACE INTO metadata VALUES(?,?)', ('relaciones_rev', f'{VERSION}:{rev}'))
        return {'aristas': len(aristas), 'por_tipo': dict(collections.Counter(tp for (_, tp, _) in aristas))}


def umbral_inferencia():
    p = b.CACHE / 'relaciones-validacion.json'
    if p.exists():
        return json.loads(p.read_text()).get('umbral', {'coseno': 0.80, 'margen': 0.01})
    return {'coseno': 0.80, 'margen': 0.01}


def asegurar():
    with contextlib.closing(b.connection()) as c:
        meta = dict(c.execute('SELECT key,value FROM metadata'))
        existe = c.execute("SELECT 1 FROM sqlite_master WHERE name='relaciones'").fetchone()
    if not existe or meta.get('relaciones_rev') != f"{VERSION}:{meta.get('revision')}":
        construir()


def resolver(texto):
    """Texto libre -> lista de (tipo, valor, score). Coincidencia exacta o por alias primero; si no, familia por E5."""
    t = norm(texto)
    m = TICKET.fullmatch(texto.strip().upper())
    if m:
        return [('ticket', m.group(), 1.0)]
    for a, canon in _alias():
        if t == a or t == norm(canon):
            return [('cliente', canon, 1.0)]
    for k in SISTEMAS:
        if t == norm(k) or re.fullmatch(SISTEMAS[k], t, re.I):
            return [('sistema', k, 1.0)]
    for p in PERSONAS:
        if t == norm(p):
            return [('persona', p, 1.0)]
    if t in FAMILIAS:
        return [('familia', t, 1.0)]
    enc = b.encoder()
    fam = list(FAMILIAS)
    P = enc.encode(['passage: ' + FAMILIAS[f]['desc'] for f in fam], normalize_embeddings=True, show_progress_bar=False)
    q = enc.encode(['query: ' + texto], normalize_embeddings=True, show_progress_bar=False)[0]
    s = P @ q
    orden = sorted(zip(s, fam), reverse=True)[:3]
    return [('familia', f, round(float(x), 4)) for x, f in orden if x >= orden[0][0] - 0.02]


def tickets_de(c, tipo, valor, confianzas=('documentada', 'inferida', 'mencion'), peso_min=1):
    if tipo == 'ticket':
        return {valor: {'confianza': 'documentada', 'evidencia': []}}
    out = {}
    for r in c.execute(f"SELECT ticket, confianza, peso, evidencia, score FROM relaciones WHERE tipo=? AND valor=? AND confianza IN ({','.join('?' * len(confianzas))}) AND peso>=?", (tipo, valor, *confianzas, peso_min)):
        out[r['ticket']] = {'confianza': r['confianza'], 'peso': r['peso'], 'score': r['score'], 'evidencia': json.loads(r['evidencia'])}
    return out


def consultar(texto, hacia=None, incluir_menciones=False):
    asegurar()
    origenes = resolver(texto)
    conf = ('documentada', 'inferida', 'mencion') if incluir_menciones else ('documentada', 'inferida')
    with contextlib.closing(b.connection()) as c:
        tickets = {}
        for tipo, valor, score in origenes:
            # Para clientes, sistemas y personas la mención es la relación; para familias se exige documentada o inferida.
            usar = ('documentada', 'inferida', 'mencion') if tipo in ('cliente', 'sistema', 'persona') else conf
            peso_min = 2 if tipo in ('sistema', 'persona') else 1
            for t, info in tickets_de(c, tipo, valor, usar, peso_min).items():
                tickets.setdefault(t, {**info, 'via': f'{tipo}:{valor}'})
        resultado = {'consulta': texto, 'resuelto_como': [{'tipo': t, 'valor': v, 'score': s} for t, v, s in origenes],
                     'tickets': len(tickets)}
        if not hacia or hacia == 'ticket':
            resultado['detalle'] = [{'ticket': t, **i} for t, i in sorted(tickets.items())][:60]
        else:
            agg = collections.defaultdict(lambda: {'tickets': [], 'peso': 0})
            for t in tickets:
                for r in c.execute("SELECT valor, peso, confianza, evidencia FROM relaciones WHERE ticket=? AND tipo=?", (t, hacia)):
                    if hacia in ('sistema', 'persona') and r['peso'] < 2: continue
                    if hacia == 'cliente' and r['confianza'] == 'mencion':
                        # Un cliente mencionado en la nota de otro ticket no es el cliente del ticket.
                        if any(x['confianza'] != 'mencion' for x in [dict(y) for y in c.execute("SELECT confianza FROM relaciones WHERE ticket=? AND tipo='cliente'", (t,))]):
                            continue
                    a = agg[r['valor']]; a['tickets'].append(t); a['peso'] += r['peso']
            resultado[hacia] = [{'valor': v, 'tickets': sorted(set(a['tickets'])), 'n_tickets': len(set(a['tickets']))} for v, a in sorted(agg.items(), key=lambda x: (-len(set(x[1]['tickets'])), x[0]))][:40]
        resultado['instruction'] = 'Cada relación trae confianza (documentada, inferida, mencion). Lee la evidencia de los tickets antes de afirmar un patrón común; una familia inferida es una hipótesis de agrupación.'
        return resultado


def vecinos(texto):
    asegurar()
    origen = resolver(texto)[0]
    with contextlib.closing(b.connection()) as c:
        if origen[0] == 'ticket':
            filas = c.execute('SELECT tipo, valor, peso, confianza, score, evidencia FROM relaciones WHERE ticket=? ORDER BY tipo, peso DESC', (origen[1],)).fetchall()
            return {'ticket': origen[1], 'relaciones': [dict(r, evidencia=json.loads(r['evidencia'])) for r in filas if not (r['tipo'] in ('sistema', 'persona') and r['peso'] < 2)]}
        ts = tickets_de(c, origen[0], origen[1])
        out = {'entidad': {'tipo': origen[0], 'valor': origen[1]}, 'tickets': sorted(ts), 'relacionados': {}}
        for tipo in ('cliente', 'sistema', 'familia', 'persona'):
            if tipo == origen[0]: continue
            cnt = collections.Counter()
            for t in ts:
                for r in c.execute('SELECT valor, peso FROM relaciones WHERE ticket=? AND tipo=?', (t, tipo)):
                    if tipo in ('sistema', 'persona') and r['peso'] < 2: continue
                    cnt[r['valor']] += 1
            out['relacionados'][tipo] = cnt.most_common(12)
        return out


def validar():
    """Precisión de la familia inferida contra las familias documentadas.

    Cada ticket documentado se clasifica como si fuera nuevo, con su título y sus causas
    confirmadas. Se barre el umbral de coseno y margen y se guarda el que da precisión >= 0.7
    con la mayor cobertura. Las descripciones de familia se escribieron mirando esos mismos
    casos, así que la cifra es optimista frente a tickets nuevos.
    """
    import numpy as np
    tit = json.loads((b.ROOT / 'cola/titulos-jira.json').read_text())
    fam = list(FAMILIAS)
    enc = b.encoder()
    P = enc.encode(['passage: ' + FAMILIAS[f]['desc'] for f in fam], normalize_embeddings=True, show_progress_bar=False)
    with contextlib.closing(b.connection()) as c:
        causas = collections.defaultdict(list)
        for r in c.execute("SELECT ticket, text FROM claims WHERE kind IN ('confirmada','correccion') AND strength!='texto' AND ticket!=''"):
            if len(causas[r['ticket']]) < 4: causas[r['ticket']].append(r['text'][:300])
    gold = [(t, f) for f in fam for t in FAMILIAS[f]['tickets'] if t in tit]
    Q = enc.encode(['query: ' + (tit[t] + '. ' + ' '.join(causas.get(t, []))) for t, _ in gold], normalize_embeddings=True, show_progress_bar=False)
    S = Q @ P.T
    filas = []
    for (t, f), s in zip(gold, S):
        i = int(np.argmax(s)); o = np.sort(s)
        filas.append((float(s[i]), float(s[i] - o[-2]), fam[i] == f))
    curva = []
    mejor = None
    for cos in [x / 100 for x in range(76, 92)]:
        for mg in (0.0, 0.01, 0.02, 0.03):
            sel = [ok for sc, m, ok in filas if sc >= cos and m >= mg]
            if not sel: continue
            prec = sum(sel) / len(sel); cob = len(sel) / len(filas)
            curva.append({'coseno': cos, 'margen': mg, 'precision': round(prec, 3), 'cobertura': round(cob, 3)})
            if prec >= 0.7 and (mejor is None or cob > mejor['cobertura']):
                mejor = curva[-1]
    top1 = sum(ok for _, _, ok in filas) / len(filas)
    res = {'tickets_documentados': len(filas), 'precision_top1_sin_umbral': round(top1, 3),
           'umbral': {'coseno': mejor['coseno'], 'margen': mejor['margen']} if mejor else {'coseno': 0.85, 'margen': 0.02},
           'elegido': mejor, 'nota': 'Los títulos documentados pueden parecerse a las descripciones escritas a partir de ellos; la cifra es optimista.',
           'curva': curva}
    (b.CACHE / 'relaciones-validacion.json').write_text(json.dumps(res, ensure_ascii=False, indent=1))
    return {k: v for k, v in res.items() if k != 'curva'}


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    s = p.add_subparsers(dest='cmd', required=True)
    s.add_parser('construir'); s.add_parser('validar')
    q = s.add_parser('consultar'); q.add_argument('texto'); q.add_argument('--hacia', choices=['ticket', 'cliente', 'sistema', 'familia', 'persona']); q.add_argument('--menciones', action='store_true')
    v = s.add_parser('vecinos'); v.add_argument('texto')
    a = p.parse_args()
    if a.cmd == 'construir': r = construir()
    elif a.cmd == 'validar': r = validar()
    elif a.cmd == 'consultar': r = consultar(a.texto, a.hacia, a.menciones)
    else: r = vecinos(a.texto)
    print(json.dumps(r, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    import os
    _py = Path(__file__).resolve().parent.parent / '.venv-cerebro/bin/python'
    if _py.exists() and Path(sys.prefix).resolve() != _py.parent.parent.resolve():
        os.execv(str(_py), [str(_py), __file__, *sys.argv[1:]])
    main()
