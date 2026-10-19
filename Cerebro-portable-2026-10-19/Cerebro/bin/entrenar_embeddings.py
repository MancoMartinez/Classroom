#!/usr/bin/env python3
"""Fine-tuning contrastivo del modelo de embeddings con pares ticket -> evidencia de Cerebro.

Pares positivos (consulta, pasaje):
  1. título de Jira del ticket -> fragmentos de documentos de sus precedentes (golden set)
  2. título de Jira del ticket -> fragmentos de sus propias notas de investigación
Negativo duro por par: fragmento de otro ticket del mismo cliente (prefijo del título),
para que el modelo aprenda causa, no nombre de cliente.
Pérdida: MultipleNegativesRankingLoss con el negativo duro explícito, prefijos E5.

Los sujetos de la partición test de eval_cerebro quedan fuera del entrenamiento, para que
la comparación posterior no tenga fuga. No se entrena con menos de --minimo consultas
distintas (150 por defecto). El guardián real es la partición test de eval_cerebro: el modelo
nuevo solo se adopta si supera al base ahí.

    python3 bin/entrenar_embeddings.py contar
    python3 bin/entrenar_embeddings.py entrenar [--minimo 150] [--epocas 1] [--max-seq 256]
        guarda .cerebro/modelos/e5-cerebro-AAAAMMDD; no cambia la configuración

Para probarlo: .cerebro/config.json {"embedding_model": ".cerebro/modelos/e5-cerebro-AAAAMMDD"},
luego python3 bin/cerebro_motor.py index --vectors y python3 bin/eval_cerebro.py ... --particion test.
Si no supera al modelo base en test, borra la clave y vuelve el modelo original; los vectores
de ambos modelos conviven en el índice porque la tabla vectors está indexada por modelo.
"""
import argparse, os, collections, contextlib, datetime, json, random, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import cerebro_motor as b
import eval_cerebro as ev

GENERICO = re.compile(r'^\s*\[(grafana|snowtime)\]', re.I)  # títulos de alertas automáticas: no describen un síntoma
CONSOLIDA = re.compile(r'(informe|instructivo|causa|analisis|hallazgo|investigacion|diagnostico|rca|verificacion|bitacora)', re.I)


def titulos():
    p = b.ROOT / 'cola/titulos-jira.json'
    return json.loads(p.read_text()) if p.exists() else {}


def cliente(titulo):
    return re.split(r'\s*[-–:]\s*', titulo.strip(), 1)[0].lower() if titulo else ''


def construir():
    tit = titulos()
    excluidos = {c['sujeto'] for c in ev.casos() if c['set'] == 'precedentes' and c['particion'] == 'test'}
    golden = json.loads((b.ROOT / 'cola/EVAL-precedentes.json').read_text())['casos'] if (b.ROOT / 'cola/EVAL-precedentes.json').exists() else []
    pares = []
    with contextlib.closing(b.connection()) as c:
        por_ticket = collections.defaultdict(list)
        for r in c.execute('SELECT e.ticket, ch.path, ch.title, ch.body FROM entities e JOIN chunks ch ON ch.id=e.chunk_id'):
            if r['ticket'] in (r['path'] + ' ' + r['title']).upper():
                por_ticket[r['ticket']].append(r['title'] + '\n' + r['body'])
        for caso in golden:
            if caso['sujeto'] in excluidos: continue
            for prec in caso['precedentes']:
                for texto in por_ticket.get(prec, [])[:3]:
                    pares.append((caso['sujeto'], caso['q'], texto))
        for t, q in tit.items():
            if t in excluidos or GENERICO.match(q): continue
            for texto in por_ticket.get(t, [])[:4]:
                if CONSOLIDA.search(texto[:200]) or len(por_ticket[t]) <= 4:
                    pares.append((t, q, texto))
        por_cliente = collections.defaultdict(list)
        for t, q in tit.items():
            por_cliente[cliente(q)].append(t)
    rnd = random.Random(13); filas = []
    for t, q, pos in pares:
        otros = [o for o in por_cliente[cliente(tit.get(t, ''))] if o != t and por_ticket.get(o)]
        neg = rnd.choice(por_ticket[rnd.choice(otros)]) if otros else None
        filas.append({'ticket': t, 'q': 'query: ' + q, 'pos': 'passage: ' + pos, 'neg': ('passage: ' + neg) if neg else None})
    return filas, excluidos


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    s = p.add_subparsers(dest='cmd', required=True)
    s.add_parser('contar')
    e = s.add_parser('entrenar'); e.add_argument('--minimo', type=int, default=150); e.add_argument('--epocas', type=int, default=1); e.add_argument('--max-seq', type=int, default=256); e.add_argument('--lote', type=int, default=16)
    a = p.parse_args()
    filas, excl = construir()
    consultas = len({f['q'] for f in filas})
    info = {'pares': len(filas), 'consultas_distintas': consultas, 'con_negativo_duro': sum(bool(f['neg']) for f in filas),
            'sujetos_test_excluidos': len(excl), 'titulos_disponibles': len(titulos())}
    print(json.dumps(info, ensure_ascii=False))
    if a.cmd == 'contar':
        return
    if consultas < a.minimo:
        sys.exit(f'Datos insuficientes: {consultas} consultas distintas, se exigen {a.minimo}. '
                 'Amplía cola/titulos-jira.json con títulos de Jira de tickets cerrados que tengan notas en Cerebro.')
    from datasets import Dataset
    from sentence_transformers import SentenceTransformer, SentenceTransformerTrainer, SentenceTransformerTrainingArguments
    try:
        from sentence_transformers.sentence_transformer import losses
    except ImportError:
        from sentence_transformers import losses
    modelo = SentenceTransformer(b.MODEL, revision=b.REVISION)
    modelo.max_seq_length = a.max_seq
    # La matriz de vocabulario (250k tokens, ~96M parámetros) queda congelada: con pocos
    # cientos de pares solo se ajusta el encoder, y el optimizador cabe en 3 GB de RAM.
    for p_ in modelo[0].auto_model.embeddings.word_embeddings.parameters():
        p_.requires_grad = False
    datos = [f for f in filas if f['neg']]
    ds = Dataset.from_dict({'anchor': [f['q'] for f in datos], 'positive': [f['pos'] for f in datos], 'negative': [f['neg'] for f in datos]})
    destino = b.CACHE / 'modelos' / ('e5-cerebro-' + datetime.date.today().strftime('%Y%m%d'))
    args = SentenceTransformerTrainingArguments(output_dir=str(destino) + '-tmp', num_train_epochs=a.epocas, per_device_train_batch_size=a.lote, dataloader_pin_memory=False,
                                                learning_rate=2e-5, warmup_steps=0.1, save_strategy='no', logging_steps=20, seed=13)
    SentenceTransformerTrainer(model=modelo, args=args, train_dataset=ds, loss=losses.MultipleNegativesRankingLoss(modelo)).train()
    modelo.save(str(destino))
    (destino / 'entrenamiento.json').write_text(json.dumps({**info, 'base': b.MODEL, 'revision_base': b.REVISION, 'epocas': a.epocas}, indent=1))
    print('Modelo guardado en', destino, '. La configuración no cambió.')


if __name__ == '__main__':
    _py = Path(__file__).resolve().parent.parent / '.venv-cerebro/bin/python'
    if _py.exists() and Path(sys.prefix).resolve() != _py.parent.parent.resolve():
        os.execv(str(_py), [str(_py), __file__, *sys.argv[1:]])
    main()
