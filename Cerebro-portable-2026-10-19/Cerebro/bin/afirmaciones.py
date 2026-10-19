#!/usr/bin/env python3
"""Capa epistemica de Cerebro: afirmaciones con tipo, vigencia y versiones reemplazadas.

La unidad es la oracion, no el fragmento: un mismo parrafo mezcla CONFIRMADA e HIPOTESIS.
Tipos: confirmada, hipotesis, descartada, correccion, compromiso, estado.
Fuerza: etiqueta (palabra en mayusculas o al inicio con dos puntos), heredada (oracion sin
marca dentro de un parrafo etiquetado) o texto (marca en prosa).
Volatil: la oracion habla de estado, assignee o fase de Jira. Vence a los N dias de la
fecha del documento, porque esa fecha es cuando se observo, no cuando dejo de ser cierto.

Modelo bitemporal: observed_at es el tiempo valido (fecha del documento), recorded_at el
tiempo de registro en el indice, valid_until el fin de vigencia estimado para volatiles.
"""
import datetime, re, unicodedata

VERSION = 2
TICKET = re.compile(r'\b(?:RCS|RTS|ENG|OUTM|DATASCI|RETAILIT|RETAILDB)-\d+\b', re.I)


def _norm(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')


TIPOS = [
    ('descartada', re.compile(r'\b(descartad[oa]s?|refutad[oa]s?|no era la causa|ruled out|disproven|refuted)\b')),
    ('correccion', re.compile(r'\b(correccion|corregid[oa]s?|errata|fe de erratas|correction|corrected|me equivoque|estaba mal)\b')),
    ('hipotesis', re.compile(r'\b(hipotesis|sin verificar|no verificad[oa]|no confirmad[oa]|sin confirmar|por confirmar|falta confirmar|pendiente de confirmar|hypothesis|unconfirmed|not (yet )?confirmed|probablemente|posible causa|sospech[oa]|suspected)\b')),
    ('confirmada', re.compile(r'\b(confirmad[oa]s?|verificad[oa]s?|comprobad[oa]s?|confirmed|verified)\b')),
    ('compromiso', re.compile(r'\b(me comprometo|compromiso|prometi|quedamos en|nos comprometimos|will (send|provide|share|follow up|update)|eta)\b')),
]
NEGACION = re.compile(r'\b(no|sin|antes de|falta|por|not|un|aun no|todavia no|pendiente de)\s+(\w+\s+){0,2}$')
ETIQUETA = re.compile(r'\b(CONFIRMAD[AO]S?|VERIFICAD[AO]S?|HIP[OÓ]TESIS|SIN VERIFICAR|NO CONFIRMAD[AO]|DESCARTAD[AO]S?|REFUTAD[AO]S?|CORRECCI[OÓ]N|CORREGID[AO]|COMPROMISO)\b|^\s*[-*]?\s*(Confirmad[oa]|Hip[oó]tesis|Descartad[oa]|Correcci[oó]n|Compromiso)\s*:')
VOLATIL = re.compile(r'\b(under (customer|engineering) review|accepted into development|waiting for (customer|support|engineering)|work in progress|in progress|support resolved|resolved|closed|reopened|escalated|asignad[oa] a|reasignad[oa]|assignee|assigned to|estado actual|estado del ticket|status (is|:)|queda en|quedo en|sigue en|esta en (under|waiting|work)|sin asignar|unassigned)\b')
ORACION = re.compile(r'(?<=[.!?:])\s+(?=[A-ZÁÉÍÓÚÑ¿"`(])')


def clasificar(oracion):
    n = _norm(oracion)
    for tipo, rx in TIPOS:
        m = rx.search(n)
        if not m:
            continue
        if tipo == 'confirmada' and NEGACION.search(n[:m.start()]):
            return 'hipotesis'
        return tipo
    return None


def extraer(texto, primera_linea=1):
    """Devuelve [(linea, tipo, fuerza, volatil, oracion)] solo para oraciones con marca o estado.

    Una etiqueta suelta ("HIPOTESIS." al inicio) gobierna las oraciones siguientes del parrafo;
    al final de la linea ("... faltan 3. DESCARTADO.") marca las oraciones previas sin tipo.
    """
    out = []
    for i, linea in enumerate(texto.splitlines()):
        actual, previas = None, []
        oraciones = [o.strip(' -*>|#') for o in ORACION.split(linea.strip())]
        for j, o in enumerate(oraciones):
            if not o:
                continue
            tipo = clasificar(o)
            fuerza = 'etiqueta' if ETIQUETA.search(o) else 'texto'
            if len(o) < 12:
                if tipo and fuerza == 'etiqueta':
                    if j == len(oraciones) - 1 and previas:
                        for k in previas:
                            ln, _, _, vol, txt = out[k]
                            out[k] = (ln, tipo, 'etiqueta', vol, txt)
                    actual = tipo
                continue
            if tipo and fuerza == 'etiqueta':
                actual = tipo
            elif not tipo and actual in ('hipotesis', 'confirmada', 'descartada', 'correccion'):
                tipo, fuerza = actual, 'heredada'
            volatil = bool(VOLATIL.search(_norm(o)))
            if tipo is None and volatil:
                tipo = 'estado'
            if tipo:
                out.append((primera_linea + i, tipo, fuerza, int(volatil), o[:400]))
            if tipo in (None, 'estado'):
                if tipo is None:
                    out.append((primera_linea + i, 'sin_tipo', 'texto', 0, o[:400]))
                previas.append(len(out) - 1)
    return [x for x in out if x[1] != 'sin_tipo']


def vencimiento(observado, dias):
    if not observado:
        return ''
    try:
        return (datetime.date.fromisoformat(observado[:10]) + datetime.timedelta(days=dias)).isoformat()
    except ValueError:
        return ''


def vigente(valid_until, hoy=None):
    hoy = hoy or datetime.date.today().isoformat()
    return bool(valid_until) and valid_until >= hoy


SUFIJO = re.compile(r'[-_ ](v\d+|version[-_ ]?\d+|final|corregid[oa]|bis)$', re.I)
FECHA = re.compile(r'^20\d{2}-\d{2}-\d{2}[-_ ]?')


def _clave(path):
    carpeta, _, nombre = path.rpartition('/')
    stem = nombre.rsplit('.', 1)[0]
    base = FECHA.sub('', stem); marcas = []
    while True:
        m = SUFIJO.search(base)
        if not m:
            break
        marcas.append(m.group(1).lower()); base = base[:m.start()]
    return (carpeta, base.lower()), marcas


def _orden(path, marcas, fecha):
    num = max([int(re.sub(r'\D', '', m) or 0) for m in marcas] + [1 if marcas else 0])
    return (fecha or '', num, path)


def _dia(fecha):
    try:
        return datetime.date.fromisoformat(fecha[:10]).toordinal()
    except (ValueError, TypeError):
        return None


def versiones(fuentes, ventana=2):
    """fuentes: [(path, fecha)] -> {path_reemplazado: path_vigente}.

    Un documento queda reemplazado solo por otro del mismo nombre base, con marca explicita
    de version (v2, v3, final, corregido) y fechado entre 0 y `ventana` dias despues.
    Notas del mismo ticket en fechas distintas sin marca no se tocan: son comentarios
    distintos, no versiones.
    """
    grupos = {}
    for path, fecha in fuentes:
        if path.startswith('db:'):
            continue
        clave, marcas = _clave(path)
        grupos.setdefault(clave, []).append((path, marcas, fecha or ''))
    out = {}
    for miembros in grupos.values():
        if len(miembros) < 2 or not any(m for _, m, _ in miembros):
            continue
        for a in miembros:
            da = _dia(a[2]); oa = _orden(*a)
            mejor = None
            for b in miembros:
                if b is a or not b[1]:
                    continue
                db_ = _dia(b[2])
                if da is not None and db_ is not None and not (0 <= db_ - da <= ventana):
                    continue
                ob = _orden(*b)
                if ob > oa and (mejor is None or ob > _orden(*mejor)):
                    mejor = b
            if mejor:
                out[a[0]] = mejor[0]
    return out
