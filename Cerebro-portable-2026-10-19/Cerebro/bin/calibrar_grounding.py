#!/usr/bin/env python3
"""Calibra los umbrales del verificador con un experimento controlado.

Para cada borrador pegable de un ticket, la misma oración se verifica dos veces: con el
índice completo (la evidencia del ticket existe) y excluyendo todo fragmento que nombre al
ticket (la evidencia no existe). Las oraciones que no obtienen soporte ni con evidencia se
descartan del análisis. Se elige el umbral que maximiza el índice de Youden (TPR - FPR) y se
escribe .cerebro/grounding-calibracion.json con las curvas resumidas.

    python3 bin/calibrar_grounding.py [--max-borradores 12] [--presupuesto 150]
"""
import argparse, os, json, re, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import cerebro_motor as b
import grounding as g


def main():
    p = argparse.ArgumentParser(); p.add_argument('--max-borradores', type=int, default=12); p.add_argument('--presupuesto', type=float, default=150)
    a = p.parse_args()
    parcial = b.CACHE / 'grounding-calibracion-parcial.jsonl'
    hechos = {json.loads(l)['archivo'] for l in parcial.read_text().splitlines()} if parcial.exists() else set()
    borradores = sorted(b.ROOT.glob('inbox/*-rcs-*-comentario-interno*.md'), reverse=True)[:a.max_borradores]
    inicio = time.perf_counter()
    for f in borradores:
        rel = f.relative_to(b.ROOT).as_posix()
        if rel in hechos: continue
        if time.perf_counter() - inicio > a.presupuesto:
            print('pendiente', rel); continue
        t = b.TICKET.search(f.name.upper())
        if not t: continue
        texto = '\n'.join(list(g.oraciones(f.read_text(encoding='utf-8')))[:40])
        con = g.verificar(texto, excluir=[rel])['oraciones']
        sin = g.verificar(texto, excluir=[rel], excluir_ticket=t.group())['oraciones']
        with parcial.open('a') as out:
            out.write(json.dumps({'archivo': rel, 'con': [x['soporte'] for x in con], 'sin': [x['soporte'] for x in sin],
                                  'cob_con': [x['cobertura'] for x in con], 'cob_sin': [x['cobertura'] for x in sin],
                                  'ce_con': [x['soporte_ce'] for x in con], 'ce_sin': [x['soporte_ce'] for x in sin]}) + '\n')
    filas = [json.loads(l) for l in parcial.read_text().splitlines()]
    res = {'borradores': len(filas), 'criterio': 'bajo maximiza Youden (TPR-FPR); alto es el menor umbral con FPR <= 10 %'}
    for senal, kc, ks, rango in (('coseno', 'con', 'sin', [x / 1000 for x in range(780, 961, 5)]),
                                 ('cross_encoder', 'ce_con', 'ce_sin', [x / 4 for x in range(-24, 41)])):
        pos = [x for r in filas for x in r[kc] if x is not None]
        neg = [x for r in filas for x in r[ks] if x is not None]
        if not pos or not neg:
            continue
        auc = sum((a > b) + 0.5 * (a == b) for a in pos for b in neg) / (len(pos) * len(neg))
        curva, mejor = [], (-1, None)
        for t in rango:
            tpr = sum(x >= t for x in pos) / len(pos); fpr = sum(x >= t for x in neg) / len(neg)
            curva.append((t, round(tpr, 3), round(fpr, 3)))
            if tpr - fpr > mejor[0]: mejor = (tpr - fpr, t)
        alto = next((t for t, _, f in curva if f <= 0.10), mejor[1])
        res[senal] = {'n': len(pos), 'auc': round(auc, 3), 'youden': round(mejor[0], 3), 'bajo': mejor[1], 'alto': max(alto, mejor[1]),
                      'media_con': round(sum(pos) / len(pos), 4), 'media_sin': round(sum(neg) / len(neg), 4), 'curva': curva}
    pc = [c for r in filas for c in r['cob_con'] if c is not None]; ps = [c for r in filas for c in r['cob_sin'] if c is not None]
    if pc and ps:
        res['cobertura'] = {'n': len(pc), 'auc': round(sum((a > b) + 0.5 * (a == b) for a in pc for b in ps) / (len(pc) * len(ps)), 3)}
    u = {'cobertura': 0.67}
    if 'coseno' in res: u.update(soporte_bajo=res['coseno']['bajo'], soporte_alto=res['coseno']['alto'])
    if 'cross_encoder' in res: u.update(ce_bajo=res['cross_encoder']['bajo'], ce_alto=res['cross_encoder']['alto'])
    res['umbrales'] = u
    (b.CACHE / 'grounding-calibracion.json').write_text(json.dumps(res, indent=1))
    print(json.dumps({k: ({kk: vv for kk, vv in v.items() if kk != 'curva'} if isinstance(v, dict) else v) for k, v in res.items()}, indent=1))


if __name__ == '__main__':
    _py = Path(__file__).resolve().parent.parent / '.venv-cerebro/bin/python'
    if _py.exists() and Path(sys.prefix).resolve() != _py.parent.parent.resolve():
        os.execv(str(_py), [str(_py), __file__, *sys.argv[1:]])
    main()
