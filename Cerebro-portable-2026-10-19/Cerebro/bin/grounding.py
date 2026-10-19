#!/usr/bin/env python3
"""Verificador de grounding: cada oración de un borrador contra la evidencia de Cerebro.

    python3 bin/grounding.py borrador.md [--destino cliente|interno] [--excluir ruta ...]

Por oración calcula:
  soporte     coseno E5 máximo entre la oración (query:) y los pasajes candidatos (passage:)
  cobertura   fracción de entidades verificables (tickets, cifras, horas, identificadores
              técnicos) presentes en los mejores pasajes
  veredicto   respaldada, parcial o sin_respaldo, con umbrales calibrados en
              .cerebro/grounding-calibracion.json cuando existe
Alertas:
  hipotesis_al_cliente  la mejor evidencia es una HIPÓTESIS o DESCARTADA y el destino es el cliente
  estado_volatil        la oración afirma estado, fase o assignee: se verifica en Jira en vivo
  fecha_futura          compromiso o fecha futura en texto al cliente
  entidad_inexistente   una cifra, ticket o identificador que no aparece en ningún lugar del índice
Los borradores pegables (comentario, respuesta, teams, correo, mensaje) no cuentan como
evidencia: son texto escrito para Jira, no prueba. Tampoco el propio archivo verificado.
"""
import argparse, os, contextlib, datetime, json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cerebro_motor as b
import afirmaciones as af

PEGABLE = re.compile(r'(comentario|respuesta|teams|correo|pegar|email|mensaje|reply|draft|borrador)', re.I)
UMBRALES = {'soporte_alto': 0.90, 'soporte_bajo': 0.875, 'ce_alto': 4.0, 'ce_bajo': 1.0, 'cobertura': 0.67}
CORTESIA = re.compile(r'^(hi|hello|dear|thanks|thank you|best|regards|kind regards|hola|gracias|saludos|cheers)\b', re.I)
FUTURO = re.compile(r'\b(will be (fixed|resolved|deployed|released|available|completed)|eta|by (end of|next|monday|tuesday|wednesday|thursday|friday)|next (week|release|sprint)|tomorrow|we expect|should be (fixed|resolved|ready))\b', re.I)
ORACION = re.compile(r'(?<=[.!?])\s+(?=[A-Z0-9ÁÉÍÓÚÑ¿"(])|\n+')
NUM = re.compile(r'(?<![\w.])\d{1,3}(?:,\d{3})+(?![\w])|(?<![\w.:/])\d+(?:[.:/]\d+)*(?![\w])')
IDENT = re.compile(r'\b(?:[A-Za-z]+[._][A-Za-z0-9_.]+|[a-z]+[A-Z][A-Za-z0-9]+|[A-Z][a-z]+[A-Z][A-Za-z0-9]+|[A-Z]{2,}[0-9]+[A-Z0-9]*)\b')


def umbrales():
    p = b.CACHE / 'grounding-calibracion.json'
    if p.exists():
        try:
            return {**UMBRALES, **json.loads(p.read_text()).get('umbrales', {})}
        except ValueError:
            pass
    return UMBRALES


def oraciones(texto):
    for linea in ORACION.split(texto):
        o = linea.strip(' -*>#\t')
        if len(o) >= 20 and not CORTESIA.match(o) and not o.startswith('http'):
            yield o


def entidades(o):
    """Entidades de alta información: tickets, cantidades de 4 o más dígitos e identificadores
    técnicos. Horas, fechas m/d y versiones cortas se escriben de muchas formas y no se exigen."""
    ents = {t.upper() for t in b.TICKET.findall(o)}
    for n in NUM.findall(o):
        limpio = n.replace(',', '')
        if re.fullmatch(r'\d{4,}', limpio) and not re.fullmatch(r'20[0-3]\d', limpio):
            ents.add(limpio)
    for i in IDENT.findall(o):
        if not b.TICKET.fullmatch(i) and not re.fullmatch(r'[\d./:]+', i) and '.' not in i.strip('.')[-4:-3]:
            ents.add(i)
    return sorted(ents)


def _formas(e):
    e = b.norm(e)
    formas = {e}
    if e.isdigit():
        formas.add(f'{int(e):,}')
    return formas


def _en(texto_norm, e):
    return any(f in texto_norm for f in _formas(e))


def existe_en_indice(c, e):
    for f in _formas(e):
        q = '"' + ' '.join(re.findall(r'\w+', f)) + '"'
        try:
            if c.execute('SELECT 1 FROM search WHERE search MATCH ? LIMIT 1', (q,)).fetchone():
                return True
        except Exception:
            return True  # sintaxis FTS rara: no se acusa lo que no se pudo comprobar
    return False


def verificar(texto, destino='interno', excluir=(), k=20, excluir_ticket=None, usar_ce=True):
    import numpy as np
    u = umbrales(); hoy = datetime.date.today()
    excluir = {str(x) for x in excluir}
    salida = []
    with contextlib.closing(b.connection()) as c:
        ids, matrix = b.dense_matrix(c)
        pos = {cid: i for i, cid in enumerate(ids)}
        for o in oraciones(texto):
            lex = b.lexical(c, o, 60)
            den, scores = b.dense(c, o, 60)
            puntos = {}
            for canal in (lex, den):
                for r, cid in enumerate(canal, 1):
                    puntos[cid] = puntos.get(cid, 0) + 1 / (60 + r)
            cand = []
            for cid, _ in sorted(puntos.items(), key=lambda x: -x[1]):
                row = c.execute('SELECT id,path,line,end_line,title,body FROM chunks WHERE id=?', (cid,)).fetchone()
                if not row or row['path'] in excluir or (PEGABLE.search(row['path']) and row['path'].startswith('inbox/')):
                    continue
                if excluir_ticket and excluir_ticket in (row['path'] + ' ' + row['body']).upper():
                    continue
                cos = float(scores[pos[cid]]) if scores is not None and cid in pos else 0.0
                cand.append((cos, dict(row)))
                if len(cand) >= k:
                    break
            cand.sort(key=lambda x: -x[0])
            ce = None
            if usar_ce and cand:
                try:
                    pares = [(o, r['title'] + '\n' + r['body'][:2000]) for _, r in cand[:10]]
                    sc = b.reranker().predict(pares, batch_size=10, show_progress_bar=False)
                    orden = sorted(zip([float(x) for x in sc], cand[:10]), key=lambda x: -x[0])
                    ce = round(orden[0][0], 4)
                    cand = [x for _, x in orden] + cand[10:]
                except (ImportError, OSError, RuntimeError, ValueError):
                    usar_ce = False
            top = cand[:3]
            soporte = round(top[0][0], 4) if top else 0.0
            texto_top = b.norm(' '.join(r['title'] + ' ' + r['body'] for _, r in cand[:8]))
            ents = entidades(o)
            faltan = [e for e in ents if not _en(texto_top, e)]
            cobertura = round(1 - len(faltan) / len(ents), 3) if ents else None
            alertas = []
            inexist = [e for e in faltan if not existe_en_indice(c, e)]
            if inexist:
                alertas.append({'tipo': 'entidad_inexistente', 'detalle': inexist})
            if top:
                resumen = b.claim_summary(c, [top[0][1]['id']]).get(top[0][1]['id'])
                if destino == 'cliente' and resumen and b.solo_especulativo(resumen):
                    alertas.append({'tipo': 'hipotesis_al_cliente', 'detalle': f"{top[0][1]['path']}:{top[0][1]['line']}"})
            if af.VOLATIL.search(af._norm(o)):
                alertas.append({'tipo': 'estado_volatil', 'detalle': 'confirmar en Jira en vivo antes de enviar'})
            if destino == 'cliente':
                fechas = [d for d in re.findall(r'\b(20\d\d-\d\d-\d\d)\b', o) if d > hoy.isoformat()]
                if FUTURO.search(o) or fechas:
                    alertas.append({'tipo': 'fecha_futura', 'detalle': 'el cliente no recibe fechas ni promesas futuras'})
            cubre = cobertura is None or cobertura >= u['cobertura']
            # El cross-encoder separa mejor que el coseno (AUC medido en la calibración); el
            # coseno queda como respaldo cuando el reranker no está descargado.
            fuerte = ce >= u['ce_alto'] if ce is not None else soporte >= u['soporte_alto']
            medio = ce >= u['ce_bajo'] if ce is not None else soporte >= u['soporte_bajo']
            if fuerte and cubre and not inexist:
                veredicto = 'respaldada'
            elif medio or (cobertura or 0) >= 0.5:
                veredicto = 'parcial'
            else:
                veredicto = 'sin_respaldo'
            salida.append({'oracion': o, 'veredicto': veredicto, 'soporte': soporte, 'soporte_ce': ce, 'cobertura': cobertura,
                           'entidades_sin_respaldo': faltan, 'alertas': alertas,
                           'evidencia': [f"{r['path']}:{r['line']}-{r['end_line']}" for _, r in top[:2]]})
    bloquea = {'hipotesis_al_cliente', 'fecha_futura', 'entidad_inexistente'} if destino == 'cliente' else {'entidad_inexistente'}
    resumen = {v: sum(x['veredicto'] == v for x in salida) for v in ('respaldada', 'parcial', 'sin_respaldo')}
    return {'destino': destino, 'resumen': resumen,
            'bloqueantes': [x['oracion'] for x in salida if any(a['tipo'] in bloquea for a in x['alertas'])],
            'verificar_en_jira': [x['oracion'] for x in salida if any(a['tipo'] == 'estado_volatil' for a in x['alertas'])],
            'umbrales': u, 'oraciones': salida,
            'instruction': 'Corrige o elimina lo bloqueante. Para sin_respaldo, cita evidencia o reformula como pregunta. Lo volátil se confirma en Jira, nunca en Cerebro.'}


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('archivo'); p.add_argument('--destino', default='interno', choices=['interno', 'cliente'])
    p.add_argument('--excluir', nargs='*', default=[])
    a = p.parse_args()
    ruta = Path(a.archivo)
    texto = ruta.read_text(encoding='utf-8') if ruta.exists() else a.archivo
    excl = list(a.excluir)
    try:
        excl.append(ruta.resolve().relative_to(b.ROOT).as_posix())
    except ValueError:
        pass
    b.sync()
    print(json.dumps(verificar(texto, a.destino, excl), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    _py = Path(__file__).resolve().parent.parent / '.venv-cerebro/bin/python'
    if _py.exists() and Path(sys.prefix).resolve() != _py.parent.parent.resolve():
        os.execv(str(_py), [str(_py), __file__, *sys.argv[1:]])
    main()
