#!/usr/bin/env python3
"""Construye el golden set ticket->precedente desde las secciones de precedentes ya escritas.

Cada archivo con un encabezado que contenga "precedente" o "relacionad" aporta pares
(ticket del archivo, ticket citado en esa seccion). La consulta es el titulo de Jira del
ticket sujeto; un fragmento es relevante si pertenece a un documento del precedente y no
menciona al sujeto, para que la nota que lista los precedentes no cuente como acierto.

    python3 bin/golden_precedentes.py pares            lista sujetos y precedentes
    python3 bin/golden_precedentes.py construir titulos.json
        titulos.json = {"RCS-28281": "titulo de Jira", ...}, leido en vivo de Jira
        escribe cola/EVAL-precedentes.json
"""
import collections, datetime, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TICKET = re.compile(r'\b(?:RCS|RTS|ENG|OUTM|DATASCI)-\d{3,6}\b', re.I)
HEAD = re.compile(r'^(#{1,6})\s+(.*)')
FOLDERS = ('inbox', 'bitacora', 'investigaciones', 'Claude outputs')


def secciones_precedentes(text):
    level, buf = None, []
    for line in text.splitlines():
        h = HEAD.match(line)
        if h:
            if level is not None and len(h.group(1)) <= level:
                yield '\n'.join(buf); level, buf = None, []
            if re.search(r'precedente|relacionad', h.group(2), re.I):
                level, buf = len(h.group(1)), []
                continue
        if level is not None:
            buf.append(line)
    if level is not None:
        yield '\n'.join(buf)


def pares():
    out = collections.defaultdict(lambda: collections.defaultdict(set))
    for folder in FOLDERS:
        for p in (ROOT / folder).rglob('*.md'):
            sujetos = {t.upper() for t in TICKET.findall(p.name)}
            if len(sujetos) != 1:
                continue
            s = sujetos.pop()
            text = p.read_text(encoding='utf-8', errors='replace')
            for sec in secciones_precedentes(text):
                for t in TICKET.findall(sec):
                    t = t.upper()
                    if t != s and t.startswith('RCS-'):
                        out[s][t].add(p.relative_to(ROOT).as_posix())
    return out


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'pares'
    data = pares()
    if cmd == 'pares':
        print(json.dumps({s: sorted(v) for s, v in sorted(data.items())}, indent=1))
        print(len(data), 'sujetos,', sum(len(v) for v in data.values()), 'pares', file=sys.stderr)
        return
    titulos = json.loads(Path(sys.argv[2]).read_text())
    casos = []
    for s, precs in sorted(data.items()):
        if s not in titulos or not titulos[s].strip():
            continue
        casos.append({'q': titulos[s], 'sujeto': s, 'precedentes': sorted(precs),
                      'fuentes': sorted({f for fs in precs.values() for f in fs})})
    doc = {'descripcion': __doc__.strip().splitlines()[0],
           'fijado': datetime.date.today().isoformat(),
           'relevancia': 'fragmento de un documento cuyo nombre o cuerpo cita un precedente y que no menciona al sujeto',
           'casos': casos}
    (ROOT / 'cola/EVAL-precedentes.json').write_text(json.dumps(doc, ensure_ascii=False, indent=1))
    print(len(casos), 'casos escritos en cola/EVAL-precedentes.json')


if __name__ == '__main__':
    main()
