#!/usr/bin/env python3
"""Extrae texto y estructura de los adjuntos para que Cerebro los busque y los cite.

    python3 bin/adjuntos.py extraer [--forzar]   procesa adjuntos nuevos o cambiados
    python3 bin/adjuntos.py estado               cobertura por tipo y pendientes

Formatos:
  xlsx/xlsm   lector propio sobre el ZIP (sin dependencias): por hoja, dimensiones,
              encabezado, primeras filas y estadísticas por columna numérica (n, ceros,
              mínimo, máximo, suma). Detecta matrices de conteo como minuto x hora.
  csv/tsv     igual que una hoja
  pdf         pypdf si está instalado, o pdftotext
  docx        lector propio sobre el ZIP
  har         resumen de red: peticiones más lentas con wait y receive
  txt sql srt md html json log py   texto
  png jpg     OCR con Vision de macOS (bin/ocr_vision.swift) o tesseract si existen
  mp4         solo metadatos

El texto queda en .cerebro/adjuntos/<ruta>.txt, redactado por secretos.py. El motor lo
indexa con la ruta original del adjunto, así la entidad del ticket sale de la carpeta.
"""
import argparse, csv, datetime, hashlib, io, json, math, os, re, shutil, subprocess, sys, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parent))
import secretos

ROOT = Path(__file__).resolve().parent.parent
CARPETAS = ('adjuntos', 'investigaciones')
SALIDA = ROOT / '.cerebro/adjuntos'
INDICE = SALIDA / 'indice.json'
TEXTO = {'.txt', '.sql', '.srt', '.log', '.py', '.html', '.htm', '.xml', '.json', '.md'}
BINARIOS = {'.xlsx', '.xlsm', '.csv', '.tsv', '.pdf', '.docx', '.har', '.png', '.jpg', '.jpeg', '.mp4'}
MAX_FILAS = 40
MAX_CHARS = 60000
NS = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main',
      'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
VERSION = 1


def candidatos():
    out = []
    for carpeta in CARPETAS:
        base = ROOT / carpeta
        if not base.exists():
            continue
        for p in base.rglob('*'):
            if not p.is_file() or p.is_symlink():
                continue
            suf = p.suffix.lower()
            if carpeta == 'adjuntos' and (suf in BINARIOS or suf in TEXTO):
                out.append(p)
            elif carpeta != 'adjuntos' and suf in BINARIOS:
                out.append(p)  # evidencia binaria dentro de investigaciones; el .md ya se indexa
    return sorted(out)


def firma(p):
    st = p.stat()
    return f'{VERSION}:{st.st_size}:{int(st.st_mtime)}'


def _num(v):
    try:
        f = float(str(v).replace(',', ''))
        return f if math.isfinite(f) else None
    except (TypeError, ValueError):
        return None


def tabla(nombre, filas):
    """Resumen de una tabla: dimensiones, primeras filas y estadística por columna numérica."""
    filas = [list(f) for f in filas if any(str(c).strip() for c in f)]
    if not filas:
        return f'## Hoja {nombre}\nVacía.\n'
    ancho = max(len(f) for f in filas)
    filas = [f + [''] * (ancho - len(f)) for f in filas]
    enc = filas[0]
    partes = [f'## Hoja {nombre}', f'{len(filas)} filas x {ancho} columnas.', '',
              'Primeras filas (tabuladas):']
    partes += ['\t'.join(str(c) for c in f) for f in filas[:MAX_FILAS]]
    if len(filas) > MAX_FILAS:
        partes.append(f'... {len(filas) - MAX_FILAS} filas más.')
    stats = []
    for j in range(ancho):
        col = [_num(f[j]) for f in filas[1:]]
        nums = [x for x in col if x is not None]
        if len(nums) >= max(3, 0.6 * (len(filas) - 1)):
            ceros = sum(x == 0 for x in nums)
            stats.append(f'{enc[j] or "col" + str(j + 1)}: n={len(nums)} ceros={ceros} min={min(nums):g} max={max(nums):g} suma={sum(nums):g}')
    if stats:
        partes += ['', 'Columnas numéricas:'] + stats
    # Celdas en cero dentro de una matriz numérica: el patrón de huecos que suele decidir un caso.
    if len(stats) >= 6:
        huecos = [f'fila {f[0]} col {enc[j]}' for f in filas[1:] for j in range(1, ancho) if _num(f[j]) == 0][:120]
        if huecos:
            partes += ['', f'Celdas en cero ({len(huecos)} primeras): ' + '; '.join(huecos)]
    return '\n'.join(partes) + '\n'


def _xlsx(p):
    with zipfile.ZipFile(p) as z:
        compartidas = []
        if 'xl/sharedStrings.xml' in z.namelist():
            for si in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si', NS):
                compartidas.append(''.join(t.text or '' for t in si.iter('{%s}t' % NS['m'])))
        libro = ET.fromstring(z.read('xl/workbook.xml'))
        rels = ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
        destino = {r.get('Id'): r.get('Target') for r in rels}
        partes = []
        for hoja in libro.find('m:sheets', NS):
            rid = hoja.get('{%s}id' % NS['r'])
            ruta = 'xl/' + destino[rid].lstrip('/').replace('xl/', '', 1)
            filas = []
            for row in ET.fromstring(z.read(ruta)).iter('{%s}row' % NS['m']):
                fila = {}
                for c in row.findall('m:c', NS):
                    ref = re.match(r'([A-Z]+)', c.get('r', 'A'))
                    col = 0
                    for ch in ref.group(1):
                        col = col * 26 + ord(ch) - 64
                    v = c.find('m:v', NS)
                    t = c.get('t')
                    if t == 's' and v is not None:
                        val = compartidas[int(v.text)]
                    elif t == 'inlineStr':
                        val = ''.join(x.text or '' for x in c.iter('{%s}t' % NS['m']))
                    else:
                        val = v.text if v is not None else ''
                    fila[col] = val
                if fila:
                    filas.append([fila.get(i, '') for i in range(1, max(fila) + 1)])
            partes.append(tabla(hoja.get('name'), filas))
        return '\n'.join(partes)


def _csv(p):
    texto = p.read_text(encoding='utf-8', errors='replace')
    try:
        dialecto = csv.Sniffer().sniff(texto[:4000])
    except csv.Error:
        dialecto = csv.excel_tab if p.suffix.lower() == '.tsv' else csv.excel
    return tabla(p.name, csv.reader(io.StringIO(texto), dialecto))


def _docx(p):
    with zipfile.ZipFile(p) as z:
        xml = z.read('word/document.xml').decode('utf-8', 'replace')
    parrafos = re.split(r'</w:p>', xml)
    return '\n'.join(re.sub(r'<[^>]+>', '', ' '.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', x))) for x in parrafos if '<w:t' in x)


def _pdf(p):
    try:
        from pypdf import PdfReader
        r = PdfReader(str(p))
        return '\n\n'.join(f'## Página {i}\n' + (pg.extract_text() or '') for i, pg in enumerate(r.pages, 1))
    except ImportError:
        if shutil.which('pdftotext'):
            return subprocess.run(['pdftotext', '-layout', str(p), '-'], capture_output=True, text=True, timeout=120).stdout
        raise RuntimeError('PDF sin extractor: instala pypdf en .venv-cerebro')


def _har(p):
    data = json.loads(p.read_text(encoding='utf-8', errors='replace'))
    entradas = data.get('log', {}).get('entries', [])
    filas = []
    for e in entradas:
        t = e.get('timings', {})
        filas.append((e.get('time', 0) or 0, e['request'].get('method'), e['request'].get('url', '')[:160],
                      e.get('response', {}).get('status'), t.get('wait'), t.get('receive'), e.get('startedDateTime', '')))
    filas.sort(key=lambda x: -x[0])
    partes = [f'HAR con {len(filas)} peticiones. Las 30 más lentas, en ms:', 'total\tmétodo\testado\twait\treceive\tinicio\turl']
    partes += [f'{f[0]:.0f}\t{f[1]}\t{f[3]}\t{f[4]}\t{f[5]}\t{f[6]}\t{f[2]}' for f in filas[:30]]
    estados = {}
    for f in filas:
        estados[f[3]] = estados.get(f[3], 0) + 1
    partes.append('Estados: ' + ', '.join(f'{k}={v}' for k, v in sorted(estados.items(), key=lambda x: str(x[0]))))
    return '\n'.join(partes)


def _ocr(p):
    swift = ROOT / 'bin/ocr_vision.swift'
    binario = ROOT / '.cerebro/ocr_vision'
    if sys.platform == 'darwin' and swift.exists():
        if not binario.exists() and shutil.which('swiftc'):
            subprocess.run(['swiftc', '-O', str(swift), '-o', str(binario)], capture_output=True, timeout=300)
        if binario.exists():
            r = subprocess.run([str(binario), str(p)], capture_output=True, text=True, timeout=120)
            if r.returncode == 0:
                return r.stdout
    if shutil.which('tesseract'):
        return subprocess.run(['tesseract', str(p), '-', '-l', 'eng+spa'], capture_output=True, text=True, timeout=120).stdout
    raise RuntimeError('Imagen sin OCR disponible: compila bin/ocr_vision.swift en el Mac o instala tesseract')


def extraer_uno(p):
    suf = p.suffix.lower()
    if suf in ('.xlsx', '.xlsm'):
        cuerpo = _xlsx(p)
    elif suf in ('.csv', '.tsv'):
        cuerpo = _csv(p)
    elif suf == '.docx':
        cuerpo = _docx(p)
    elif suf == '.pdf':
        cuerpo = _pdf(p)
    elif suf == '.har':
        cuerpo = _har(p)
    elif suf in ('.png', '.jpg', '.jpeg'):
        cuerpo = 'Texto reconocido por OCR:\n' + _ocr(p)
    elif suf == '.mp4':
        cuerpo = f'Video de {p.stat().st_size / 1e6:.1f} MB. Sin transcripción.'
    else:
        cuerpo = p.read_text(encoding='utf-8', errors='replace')
    rel = p.relative_to(ROOT).as_posix()
    ticket = re.search(r'\b(?:RCS|RTS|ENG|OUTM|DATASCI)-\d+\b', rel, re.I)
    fecha = datetime.datetime.fromtimestamp(p.stat().st_mtime).date().isoformat()
    cabecera = f'# Adjunto {p.name}\nRuta: {rel}\nTipo: {suf.lstrip(".")}\nTicket: {ticket.group().upper() if ticket else "sin ticket en la ruta"}\nModificado: {fecha}\n\n'
    return secretos.redactar(cabecera + cuerpo[:MAX_CHARS])


def destino(p):
    return SALIDA / (p.relative_to(ROOT).as_posix() + '.txt')


def extraer(forzar=False, quiet=False, ocr=True):
    SALIDA.mkdir(parents=True, exist_ok=True)
    indice = json.loads(INDICE.read_text()) if INDICE.exists() else {}
    vivos, hechos, errores = set(), 0, {}
    for p in candidatos():
        rel = p.relative_to(ROOT).as_posix(); vivos.add(rel)
        f = firma(p)
        if not forzar and indice.get(rel, {}).get('firma') == f and (destino(p).exists() or not indice[rel].get('ok')):
            continue
        if not ocr and p.suffix.lower() in ('.png', '.jpg', '.jpeg'):
            continue  # el OCR corre en la extracción explícita, no dentro de una búsqueda
        try:
            texto = extraer_uno(p)
            d = destino(p); d.parent.mkdir(parents=True, exist_ok=True); d.write_text(texto, encoding='utf-8')
            indice[rel] = {'firma': f, 'ok': True, 'chars': len(texto)}
            hechos += 1
        except Exception as e:  # un adjunto ilegible no frena a los demás
            indice[rel] = {'firma': f, 'ok': False, 'error': str(e)[:200]}
            errores[rel] = str(e)[:120]
    for rel in list(indice):
        if rel not in vivos:
            d = SALIDA / (rel + '.txt')
            if d.exists(): d.unlink()
            del indice[rel]
    INDICE.write_text(json.dumps(indice, ensure_ascii=False, indent=1))
    if not quiet and (hechos or errores):
        print(f'Adjuntos extraídos: {hechos}. Con error: {len(errores)}.', file=sys.stderr)
    return {'extraidos': hechos, 'errores': errores}


def documentos():
    """[(ruta_original, titulo, texto, fecha)] de los adjuntos ya extraídos."""
    if not INDICE.exists():
        return []
    out = []
    for rel, info in json.loads(INDICE.read_text()).items():
        d = SALIDA / (rel + '.txt')
        if info.get('ok') and d.exists():
            m = re.search(r'Modificado: (\d{4}-\d{2}-\d{2})', d.read_text(encoding='utf-8')[:400])
            out.append((rel, 'Adjunto ' + Path(rel).name, d.read_text(encoding='utf-8'), m.group(1) if m else ''))
    return out


def estado():
    indice = json.loads(INDICE.read_text()) if INDICE.exists() else {}
    por = {}
    for rel, info in indice.items():
        suf = Path(rel).suffix.lower()
        d = por.setdefault(suf, {'ok': 0, 'error': 0})
        d['ok' if info.get('ok') else 'error'] += 1
    pend = [p.relative_to(ROOT).as_posix() for p in candidatos() if p.relative_to(ROOT).as_posix() not in indice]
    errores = {r: i['error'] for r, i in indice.items() if not i.get('ok')}
    motivos = {}
    for e in errores.values():
        motivos[e[:70]] = motivos.get(e[:70], 0) + 1
    return {'por_tipo': por, 'pendientes': len(pend), 'motivos_de_error': motivos}


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    s = p.add_subparsers(dest='cmd', required=True)
    e = s.add_parser('extraer'); e.add_argument('--forzar', action='store_true'); e.add_argument('--sin-ocr', action='store_true')
    s.add_parser('estado')
    a = p.parse_args()
    print(json.dumps(extraer(a.forzar, ocr=not a.sin_ocr) if a.cmd == 'extraer' else estado(), ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
