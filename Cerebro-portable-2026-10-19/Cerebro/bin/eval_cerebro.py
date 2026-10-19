#!/usr/bin/env python3
"""Evaluacion reproducible de la recuperacion de Cerebro.

Dos conjuntos:
  anclas       cola/EVAL-recuperacion.json, relevante = fragmento que cumple la regex ancla
  precedentes  cola/EVAL-precedentes.json, consulta = titulo de Jira del ticket sujeto,
               relevante = fragmento de un precedente que no menciona al sujeto

Metricas por modo: hit@1, hit@5, MRR@10, nDCG@10 (ganancia binaria, ideal con los
relevantes que existen en el indice) y recall@10. Particion fija dev/test por hash de la
consulta (70/30). Intervalo de confianza del 95 % por bootstrap pareado de la diferencia
contra el modo de referencia.

    python3 bin/eval_cerebro.py correr --modos bm25,hybrid,rerank [--presupuesto 150]
        reanudable: guarda cada caso en .cerebro/eval-runs/<firma>.jsonl y continua donde quedo
    python3 bin/eval_cerebro.py resumen [--referencia hybrid] [--particion test]

Modos: bm25, hybrid, rerank, y con sufijo +v (hybrid+v, rerank+v) para usar las variantes
de cola/EVAL-variantes.json. Para comparar otro reranker:
    python3 bin/eval_cerebro.py correr --modos hybrid+v,rerank+v --reranker BAAI/bge-reranker-v2-m3
    python3 bin/eval_cerebro.py resumen --modos hybrid+v,rerank+v --referencia hybrid+v --reranker BAAI/bge-reranker-v2-m3

Las anclas son proxies, no juicio humano. Ninguna cifra mide exactitud de respuestas.
"""
import argparse, os, contextlib, datetime, hashlib, json, math, random, re, sys, time
from pathlib import Path
import cerebro_motor as b

RUNS = b.CACHE / 'eval-runs'
K = 10
TICKET = b.TICKET


def particion(q):
    return 'dev' if int(hashlib.sha1(q.encode()).hexdigest(), 16) % 10 < 7 else 'test'


def casos():
    out = []
    p = b.ROOT / 'cola/EVAL-recuperacion.json'
    if p.exists():
        for c in json.loads(p.read_text())['casos']:
            out.append({'set': 'anclas', 'q': c['q'], 'ancla': c['ancla']})
    p = b.ROOT / 'cola/EVAL-precedentes.json'
    if p.exists():
        for c in json.loads(p.read_text())['casos']:
            out.append({'set': 'precedentes', 'q': c['q'], 'sujeto': c['sujeto'], 'precedentes': c['precedentes']})
    pv = b.ROOT / 'cola/EVAL-variantes.json'
    var = json.loads(pv.read_text()) if pv.exists() else {'anclas': {}, 'precedentes': {}}
    i = 0
    for c in out:
        if c['set'] == 'anclas':
            c['variantes'] = var['anclas'].get(str(i), []); i += 1
        else:
            c['variantes'] = var['precedentes'].get(c['sujeto'], [])
    for c in out:
        c['particion'] = particion(c['q'])
        c['id'] = hashlib.sha1((c['set'] + c['q']).encode()).hexdigest()[:12]
    return out


def relevante(caso, path, title, body):
    if caso['set'] == 'anclas':
        return bool(re.search(caso['ancla'], title + '\n' + body, re.I | re.S))
    texto = (path + ' ' + body).upper()
    if caso['sujeto'] in texto:
        return False
    return any(t in texto for t in caso['precedentes'])


def total_relevantes(c, caso):
    n = 0
    if caso['set'] == 'anclas':
        rx = re.compile(caso['ancla'], re.I | re.S)
        for title, body in c.execute('SELECT title, body FROM chunks'):
            n += bool(rx.search(title + '\n' + body))
    else:
        for path, title, body in c.execute('SELECT path, title, body FROM chunks'):
            n += relevante(caso, path, title, body)
    return n


def metricas(rels, n_rel):
    first = next((i for i, r in enumerate(rels, 1) if r), None)
    dcg = sum(1 / math.log2(i + 1) for i, r in enumerate(rels[:K], 1) if r)
    ideal = sum(1 / math.log2(i + 1) for i in range(1, min(K, n_rel) + 1))
    return {'hit1': int(first == 1), 'hit5': int(first is not None and first <= 5),
            'mrr': 1 / first if first and first <= K else 0.0,
            'ndcg': dcg / ideal if ideal else 0.0,
            'recall': sum(rels[:K]) / min(K, n_rel) if n_rel else 0.0}


def firma(modo):
    with contextlib.closing(b.connection()) as c:
        corpus = tuple(c.execute('SELECT count(*), max(id) FROM chunks').fetchone())
    cfg = json.dumps(b.config(), sort_keys=True)
    qs = ''.join(sorted(x['id'] for x in casos()))
    return modo + '-' + hashlib.sha1(f'{corpus}{cfg}{qs}'.encode()).hexdigest()[:10]


def correr(modos, presupuesto):
    RUNS.mkdir(parents=True, exist_ok=True)
    todos = casos(); inicio = time.perf_counter(); pendientes = 0
    with contextlib.closing(b.connection()) as c:
        for modo in modos:
            out = RUNS / (firma(modo) + '.jsonl')
            hechos = {json.loads(l)['id'] for l in out.read_text().splitlines()} if out.exists() else set()
            for caso in todos:
                if caso['id'] in hechos:
                    continue
                if time.perf_counter() - inicio > presupuesto:
                    pendientes += 1; continue
                t = time.perf_counter()
                base, _, sufijo = modo.partition('+')
                r = b.search(caso['q'], K, mode=base, refresh=False, variantes=caso['variantes'] if sufijo == 'v' else None)
                dt = time.perf_counter() - t
                rels = [relevante(caso, x['path'], x['title'], x['body']) for x in r['results']]
                fila = {**caso, 'modo': modo, 'segundos': round(dt, 4), 'n_rel': total_relevantes(c, caso),
                        'fuentes': [x['path'] + ':' + str(x['line']) for x in r['results']], 'rels': rels}
                fila.update(metricas(rels, fila['n_rel']))
                with out.open('a') as f:
                    f.write(json.dumps(fila, ensure_ascii=False) + '\n')
    print(json.dumps({'pendientes': pendientes, 'segundos': round(time.perf_counter() - inicio, 1)}))
    return pendientes


def cargar(modo):
    p = RUNS / (firma(modo) + '.jsonl')
    return {json.loads(l)['id']: json.loads(l) for l in p.read_text().splitlines()} if p.exists() else {}


def bootstrap(a, b_, n=2000, seed=7):
    rnd = random.Random(seed); d = [x - y for x, y in zip(a, b_)]
    if not d:
        return (0, 0)
    medias = sorted(sum(rnd.choice(d) for _ in d) / len(d) for _ in range(n))
    return round(medias[int(0.025 * n)], 4), round(medias[int(0.975 * n)], 4)


def resumen(modos, referencia, part):
    datos = {m: cargar(m) for m in modos}
    salida = {'fecha': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'particion': part,
              'referencia': referencia, 'config': b.config(), 'indice': {k: v for k, v in b.status().items() if k in ('sources', 'chunks', 'vector_chunks', 'model')},
              'conjuntos': {}}
    for conjunto in ('anclas', 'precedentes', 'todos'):
        bloque = {}
        ids = None
        for m in modos:
            filas = [f for f in datos[m].values() if (conjunto == 'todos' or f['set'] == conjunto)
                     and (part == 'todo' or f['particion'] == part) and f['n_rel'] > 0]
            ids = {f['id'] for f in filas} if ids is None else ids & {f['id'] for f in filas}
        if not ids:
            continue
        for m in modos:
            filas = [datos[m][i] for i in sorted(ids)]
            res = {'n': len(filas)}
            for k in ('hit1', 'hit5', 'mrr', 'ndcg', 'recall'):
                res[k] = round(sum(f[k] for f in filas) / len(filas), 4)
            tiempos = sorted(f['segundos'] for f in filas)
            res['p50_s'] = tiempos[len(tiempos) // 2]; res['p95_s'] = tiempos[int(0.95 * (len(tiempos) - 1))]
            if referencia in datos and m != referencia:
                ref = [datos[referencia][i] for i in sorted(ids)]
                res['delta_hit5_ic95'] = bootstrap([f['hit5'] for f in filas], [f['hit5'] for f in ref])
                res['delta_mrr_ic95'] = bootstrap([f['mrr'] for f in filas], [f['mrr'] for f in ref])
                res['delta_ndcg_ic95'] = bootstrap([f['ndcg'] for f in filas], [f['ndcg'] for f in ref])
            bloque[m] = res
        salida['conjuntos'][conjunto] = bloque
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S')
    (b.CACHE / f'evaluacion-{stamp}.json').write_text(json.dumps(salida, ensure_ascii=False, indent=2))
    print(json.dumps(salida, ensure_ascii=False, indent=1))
    return salida


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    s = p.add_subparsers(dest='cmd', required=True)
    c = s.add_parser('correr'); c.add_argument('--modos', default='bm25,hybrid'); c.add_argument('--presupuesto', type=float, default=1e9)
    c.add_argument('--reranker', help='prueba otro cross-encoder, p. ej. BAAI/bge-reranker-v2-m3, sin cambiar la configuración')
    r = s.add_parser('resumen'); r.add_argument('--modos', default='bm25,hybrid'); r.add_argument('--referencia', default='hybrid')
    r.add_argument('--reranker')
    r.add_argument('--particion', default='todo', choices=['dev', 'test', 'todo'])
    a = p.parse_args()
    if a.reranker:
        os.environ['CEREBRO_RERANKER_MODEL'] = a.reranker
        os.environ.setdefault('CEREBRO_DOWNLOAD', '1')
    b.build_vectors(download=False)
    if a.cmd == 'correr':
        sys.exit(2 if correr(a.modos.split(','), a.presupuesto) else 0)
    resumen(a.modos.split(','), a.referencia, a.particion)


if __name__ == '__main__':
    _py = Path(__file__).resolve().parent.parent / '.venv-cerebro/bin/python'
    if _py.exists() and Path(sys.prefix).resolve() != _py.parent.parent.resolve():
        os.execv(str(_py), [str(_py), __file__, *sys.argv[1:]])
    main()
