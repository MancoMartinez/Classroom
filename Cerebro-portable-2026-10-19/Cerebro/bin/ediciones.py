#!/usr/bin/env python3
"""Bucle de aprendizaje por ediciones: lo que Claude redactó contra lo que Juan pegó.

    python3 bin/ediciones.py registrar --skill cerebro-comentario --ticket RCS-28281 \\
        --borrador inbox/2026-09-24-rcs-28281-comentario-interno.md --final final.txt
    python3 bin/ediciones.py emparejar jira-comentarios.json [--autor "Juan Martinez"]
        empareja borradores pegables de inbox con comentarios de Jira del autor, por ticket
        y similitud >= 0.35; el JSON es la respuesta de Jira (issues.nodes o lista de issues)
    python3 bin/ediciones.py versiones
        registra cada v1 de inbox contra su versión vigente (v2, v3, final)
    python3 bin/ediciones.py ejemplos --skill cerebro-comentario [--n 4]
        escribe inbox/AAAA-MM-DD-ejemplos-<skill>.md con pares few-shot y las ediciones sistemáticas
    python3 bin/ediciones.py resumen

Solo escribe .cerebro/ediciones.jsonl y el archivo de ejemplos en inbox. Jira se lee, nunca se escribe.
"""
import argparse, collections, datetime, difflib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / '.cerebro/ediciones.jsonl'
TICKET = re.compile(r'\b(?:RCS|RTS|ENG|OUTM|DATASCI)-\d+\b', re.I)
PEGABLE = re.compile(r'(comentario|respuesta|teams|correo|mensaje|email)', re.I)
SKILL_POR_NOMBRE = [('respuesta', 'cerebro-respuesta-cliente'), ('correo', 'cerebro-respuesta-cliente'),
                    ('comentario', 'cerebro-comentario'), ('teams', 'cerebro-comentario'), ('mensaje', 'cerebro-comentario')]


def leer(x):
    """Ruta de archivo o texto literal."""
    if '\n' in x or len(x) > 400:
        return x
    for p in (Path(x), ROOT / x):
        try:
            if p.is_file():
                return p.read_text(encoding='utf-8')
        except OSError:
            pass
    return x


def palabras(t):
    return re.findall(r"[\wÀ-ÿ'’-]+|[—–;:()]", t)


def comparar(borrador, final):
    a, f = palabras(borrador), palabras(final)
    sm = difflib.SequenceMatcher(a=[w.lower() for w in a], b=[w.lower() for w in f], autojunk=False)
    quitadas, agregadas = collections.Counter(), collections.Counter()
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op in ('delete', 'replace'):
            quitadas[' '.join(a[i1:i2])[:80]] += 1
        if op in ('insert', 'replace'):
            agregadas[' '.join(f[j1:j2])[:80]] += 1
    return {'similitud': round(sm.ratio(), 4), 'largo_borrador': len(borrador), 'largo_final': len(final),
            'quitado': quitadas.most_common(12), 'agregado': agregadas.most_common(12)}


def registrar(skill, ticket, borrador, final, origen='manual', ruta=None):
    b, f = leer(borrador), leer(final)
    fila = {'fecha': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'), 'skill': skill,
            'ticket': (ticket or '').upper(), 'origen': origen, 'ruta_borrador': ruta or (borrador if leer(borrador) != borrador else None),
            'borrador': b, 'final': f, **comparar(b, f)}
    LOG.parent.mkdir(exist_ok=True)
    with LOG.open('a', encoding='utf-8') as out:
        out.write(json.dumps(fila, ensure_ascii=False) + '\n')
    return fila


def cargar():
    return [json.loads(l) for l in LOG.read_text(encoding='utf-8').splitlines()] if LOG.exists() else []


def _texto_adf(nodo):
    if isinstance(nodo, str):
        return nodo
    if isinstance(nodo, dict):
        if nodo.get('type') == 'text':
            return nodo.get('text', '')
        sep = '\n' if nodo.get('type') in ('paragraph', 'heading', 'listItem') else ''
        return ''.join(_texto_adf(x) for x in nodo.get('content', [])) + sep
    if isinstance(nodo, list):
        return ''.join(_texto_adf(x) for x in nodo)
    return ''


def emparejar(json_path, autor, umbral=0.35):
    data = json.loads(Path(json_path).read_text())
    issues = data.get('issues', data) if isinstance(data, dict) else data
    if isinstance(issues, dict):
        issues = issues.get('nodes', [])
    vistos = {(r.get('ticket'), r.get('final', '')[:200]) for r in cargar()}
    nuevos = 0
    for it in issues:
        key = it.get('key', '').upper()
        comentarios = ((it.get('fields') or {}).get('comment') or {}).get('comments', [])
        propios = [_texto_adf(c.get('body')) for c in comentarios if autor.lower() in ((c.get('author') or {}).get('displayName') or '').lower()]
        if not propios:
            continue
        borradores = [p for p in (ROOT / 'inbox').glob(f'*{key.lower()}*') if PEGABLE.search(p.name)] + \
                     [p for p in (ROOT / 'inbox').glob(f'*{key}*') if PEGABLE.search(p.name)]
        for final in propios:
            mejor = max(((difflib.SequenceMatcher(a=p.read_text(encoding='utf-8')[:6000], b=final[:6000], autojunk=False).ratio(), p) for p in set(borradores)), default=(0, None))
            if mejor[1] is None or mejor[0] < umbral or (key, final[:200]) in vistos:
                continue
            skill = next((s for k, s in SKILL_POR_NOMBRE if k in mejor[1].name.lower()), 'cerebro-comentario')
            registrar(skill, key, str(mejor[1]), final, origen='jira', ruta=mejor[1].relative_to(ROOT).as_posix())
            nuevos += 1
    return nuevos


def versiones():
    """Registra cada cadena de versiones de inbox (v1 contra la versión vigente) como par de edición.

    Medido el 14 oct: 12 de 13 textos pegados en Jira coinciden en 98 % o más con su borrador
    final de inbox. La corrección de Juan ocurre antes, entre versiones del borrador.
    """
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import afirmaciones as af
    fuentes = []
    for p in (ROOT / 'inbox').glob('*.md'):
        m = re.match(r'(20\d\d-\d\d-\d\d)', p.name)
        fuentes.append((p.relative_to(ROOT).as_posix(), m.group(1) if m else ''))
    mapa = af.versiones(fuentes)
    vistos = {(r.get('ruta_borrador'), r.get('ruta_final')) for r in cargar()}
    nuevos = 0
    for viejo, nuevo in sorted(mapa.items()):
        if nuevo in mapa or (viejo, nuevo) in vistos:
            continue  # solo la versión vigente es final
        if not PEGABLE.search(viejo):
            continue
        skill = next((s for k, s in SKILL_POR_NOMBRE if k in viejo.lower()), 'cerebro-comentario')
        t = TICKET.search(viejo.upper())
        fila = registrar(skill, t.group() if t else '', viejo, nuevo, origen='versiones', ruta=viejo)
        fila['ruta_final'] = nuevo
        lineas = LOG.read_text(encoding='utf-8').splitlines()
        lineas[-1] = json.dumps(fila, ensure_ascii=False)
        LOG.write_text('\n'.join(lineas) + '\n', encoding='utf-8')
        nuevos += 1
    return nuevos


def ejemplos(skill, n):
    filas = [r for r in cargar() if r['skill'] == skill and r['similitud'] < 0.98]
    if not filas:
        sys.exit(f'Sin pares registrados para {skill}.')
    filas.sort(key=lambda r: (r['fecha'], 1 - r['similitud']), reverse=True)
    quitado, agregado = collections.Counter(), collections.Counter()
    for r in filas:
        quitado.update(dict(r['quitado'])); agregado.update(dict(r['agregado']))
    hoy = datetime.date.today().isoformat()
    out = ROOT / f'inbox/{hoy}-ejemplos-{skill}.md'
    partes = [f'# Ejemplos few-shot para {skill}', '',
              f'{len(filas)} pares borrador contra texto final. Similitud media {sum(r["similitud"] for r in filas) / len(filas):.2f}.', '',
              '## Lo que Juan quita con más frecuencia', ''] + [f'{v} veces: {k}' for k, v in quitado.most_common(15)] + \
             ['', '## Lo que Juan agrega con más frecuencia', ''] + [f'{v} veces: {k}' for k, v in agregado.most_common(15)] + ['']
    for i, r in enumerate(filas[:n], 1):
        partes += [f'## Par {i}: {r["ticket"]} ({r["fecha"][:10]}, similitud {r["similitud"]})', '', 'Borrador:', '', r['borrador'][:2500], '', 'Final pegado:', '', r['final'][:2500], '']
    out.write_text('\n'.join(partes), encoding='utf-8')
    return out


def resumen():
    por = collections.defaultdict(list)
    for r in cargar():
        por[r['skill']].append(r['similitud'])
    return {k: {'pares': len(v), 'similitud_media': round(sum(v) / len(v), 3), 'sin_cambios': sum(x >= 0.98 for x in v)} for k, v in por.items()}


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    s = p.add_subparsers(dest='cmd', required=True)
    r = s.add_parser('registrar'); r.add_argument('--skill', required=True); r.add_argument('--ticket', default=''); r.add_argument('--borrador', required=True); r.add_argument('--final', required=True)
    e = s.add_parser('emparejar'); e.add_argument('json'); e.add_argument('--autor', default='Juan Martinez')
    s.add_parser('versiones')
    x = s.add_parser('ejemplos'); x.add_argument('--skill', required=True); x.add_argument('--n', type=int, default=4)
    s.add_parser('resumen')
    a = p.parse_args()
    if a.cmd == 'registrar':
        f = registrar(a.skill, a.ticket, a.borrador, a.final)
        print(json.dumps({k: f[k] for k in ('skill', 'ticket', 'similitud', 'quitado', 'agregado')}, ensure_ascii=False, indent=1))
    elif a.cmd == 'emparejar':
        print(emparejar(a.json, a.autor), 'pares nuevos')
    elif a.cmd == 'versiones':
        print(versiones(), 'pares nuevos desde cadenas de versiones')
    elif a.cmd == 'ejemplos':
        print(ejemplos(a.skill, a.n))
    else:
        print(json.dumps(resumen(), ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
