#!/usr/bin/env python3
"""Detecta y redacta credenciales antes de que entren al indice o a la base.

    python3 bin/secretos.py [rutas...]          informe; nunca imprime el valor
    python3 bin/secretos.py --compuerta inbox   sale con 1 si hay hallazgos de severidad alta

Alta: patrones con formato propio (token de Atlassian, PAT de Azure DevOps, GitHub, AWS,
Slack, llaves privadas, JWT, cadenas de conexion con contrasena, asignaciones explicitas
password=, Bearer, credenciales en URL). Media: cadenas largas de entropia de Shannon
>= 4.3 bits por caracter con mezcla de clases, sin formato conocido.
El motor indexa siempre la version redactada; la fuente original no se modifica.
"""
import math, re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSION = 1
MARCA = '[SECRETO-REDACTADO:{}]'

# (nombre, regex, grupo con el valor o 0)
PATRONES = [
    ('atlassian_api_token', re.compile(r'ATATT3[A-Za-z0-9_\-=]{30,}'), 0),
    ('azure_devops_pat', re.compile(r'(?<![A-Za-z0-9])[A-Za-z0-9]{52,80}AZDO[A-Za-z0-9]{4}(?![A-Za-z0-9])'), 0),
    ('azure_devops_pat_clasico', re.compile(r'(?<![A-Za-z0-9])[a-z2-7]{52}(?![A-Za-z0-9])'), 0),
    ('github_token', re.compile(r'\b(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{60,})\b'), 0),
    ('aws_access_key', re.compile(r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b'), 0),
    ('slack_token', re.compile(r'\bxox[abposr]-[A-Za-z0-9-]{10,}\b'), 0),
    ('api_key_llm', re.compile(r'\bsk-(?:ant-|proj-)?[A-Za-z0-9_\-]{24,}\b'), 0),
    ('llave_privada', re.compile(r'-----BEGIN (?:[A-Z]+ )*PRIVATE KEY-----[\s\S]*?(?:-----END (?:[A-Z]+ )*PRIVATE KEY-----|$)'), 0),
    ('jwt', re.compile(r'\beyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}'), 0),
    ('azure_storage_key', re.compile(r'(?i)AccountKey=([A-Za-z0-9+/=]{40,})'), 1),
    ('cadena_conexion', re.compile(r'(?i)\b(?:password|pwd)\s*=\s*([^;\s"\']{6,})\s*;'), 1),
    ('credencial_en_url', re.compile(r'\b[a-z][a-z0-9+.-]*://[^/\s:@]+:([^/\s:@]{6,})@'), 1),
    ('bearer', re.compile(r'(?i)\bbearer\s+([A-Za-z0-9\-._~+/]{24,}=*)'), 1),
    ('asignacion', re.compile(r'(?i)\b(?:password|passwd|contrase(?:n|ñ)a|secret|client[_-]?secret|api[_-]?key|access[_-]?token|token|pat)\b\s*[:=]\s*["\'`]?([^\s"\'`<>,;]{8,})'), 1),
]
GENERICO = re.compile(r'(?<![A-Za-z0-9+/_=\-])[A-Za-z0-9+/_\-]{32,}={0,2}(?![A-Za-z0-9+/_=\-])')
MARCADORES = re.compile(r'(?i)^(x+|\*+|<[^>]*>|\.{3,}|redact|changeme|example|placeholder|your[_-]|tu[_-]|\$\{|%\w+%|null|none|true|false)')


def entropia(s):
    n = len(s); c = Counter(s)
    return -sum(v / n * math.log2(v / n) for v in c.values())


def _clases(s):
    return sum(bool(re.search(p, s)) for p in ('[a-z]', '[A-Z]', '[0-9]', '[+/_\\-=]'))


def _plausible(valor, nombre):
    if MARCADORES.match(valor) or '[SECRETO-REDACTADO' in valor:
        return False
    if nombre == 'asignacion':
        # "token: expired" o "password: reset" no son secretos.
        return len(valor) >= 8 and _clases(valor) >= 2 and entropia(valor) >= 3.0
    if nombre == 'azure_devops_pat_clasico':
        return _clases(valor) >= 2 and entropia(valor) >= 4.0
    return True


def hallazgos(texto):
    """Lista de (inicio, fin, nombre, severidad). Nunca devuelve el valor."""
    out = []
    for nombre, rx, g in PATRONES:
        for m in rx.finditer(texto):
            valor = m.group(g)
            if _plausible(valor, nombre):
                out.append((m.start(g), m.end(g), nombre, 'alta'))
    ocupado = [(a, b) for a, b, _, _ in out]
    for m in GENERICO.finditer(texto):
        v = m.group()
        if any(a < m.end() and m.start() < b for a, b in ocupado):
            continue
        if re.fullmatch(r'[0-9a-fA-F\-]+', v) or '/' in v or re.search(r'[A-Za-z]{4,}[-_][A-Za-z]{3,}', v):
            continue  # hashes, GUIDs, rutas y slugs de nombres de archivo
        if _clases(v) >= 3 and entropia(v) >= 4.3:
            out.append((m.start(), m.end(), 'alta_entropia', 'media'))
    out.sort()
    fusion = []
    for h in out:
        if fusion and h[0] < fusion[-1][1]:
            continue
        fusion.append(h)
    return fusion


def redactar(texto):
    """Reemplaza solo severidad alta; la entropia generica se informa, no se borra."""
    hs = [h for h in hallazgos(texto) if h[3] == 'alta']
    if not hs:
        return texto
    partes, pos = [], 0
    for a, b, nombre, _ in hs:
        partes += [texto[pos:a], MARCA.format(nombre)]; pos = b
    partes.append(texto[pos:])
    return ''.join(partes)


def escanear(rutas):
    filas = []
    for base in rutas:
        base = Path(base)
        archivos = [base] if base.is_file() else [p for p in base.rglob('*') if p.is_file() and p.suffix.lower() in ('.md', '.txt', '.json', '.csv', '.log')]
        for p in sorted(archivos):
            texto = p.read_text(encoding='utf-8', errors='replace')
            for a, b, nombre, sev in hallazgos(texto):
                linea = texto.count('\n', 0, a) + 1
                filas.append({'ruta': str(p), 'linea': linea, 'tipo': nombre, 'severidad': sev, 'largo': b - a})
    return filas


def main():
    args = sys.argv[1:]
    compuerta = '--compuerta' in args
    rutas = [a for a in args if a != '--compuerta'] or [ROOT / 'inbox']
    filas = escanear(rutas)
    for f in filas:
        print(f"{f['severidad']:5} {f['tipo']:26} {f['ruta']}:{f['linea']} ({f['largo']} caracteres)")
    altas = sum(f['severidad'] == 'alta' for f in filas)
    print(f'{len(filas)} hallazgos, {altas} de severidad alta.', file=sys.stderr)
    if compuerta and altas:
        print('Compuerta cerrada: retira o reemplaza el secreto en esos archivos antes de ingerir.', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
