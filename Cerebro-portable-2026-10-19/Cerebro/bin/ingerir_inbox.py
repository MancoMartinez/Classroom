#!/usr/bin/env python3
"""Consolida inbox/ dentro de la base. Un chunk por caso, no un chunk por archivo.

    python3 bin/ingerir_inbox.py                  ensayo, no escribe
    python3 bin/ingerir_inbox.py --aplicar        escribe en la base
    python3 bin/ingerir_inbox.py --desde 2026-08-25 --aplicar
    python3 bin/ingerir_inbox.py --archivar       mueve lo ingerido a inbox/archivo/

Por que existe. Entre el 25 ago y el 8 sep 2026 se escribieron 289 notas en inbox y entro
exactamente un chunk a la base. El cerebro dejo de aprender y se volvio una pila de markdown.

Que ingiere y que descarta:

    informe, instructivo, causa, analisis, verificacion   se consolidan por ticket
    cosecha                                                entran enteras, ya vienen destiladas
    comentario, respuesta, teams, correo, pegar            no entran, ese texto vive en Jira
    cola, reparto, refresco                                no entran, son foto de un momento
    plan, pasos, prompt, borrador                          no entran, son andamio de trabajo

En la base no se guarda la cronica. Se guarda la conclusion, la causa y lo que quedo pendiente.
El rastro completo queda en la lista de archivos al pie del chunk, y en tickets/.
"""
import argparse
import os
import re
import sqlite3
import sys
import time
from collections import defaultdict
from datetime import datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
DB = os.environ.get("CEREBRO_DB") or os.path.join(ROOT, "brain", "sessions.db")
INBOX = os.path.join(ROOT, "inbox")

TECHO_CUERPO = 7000  # un chunk mas largo no se lee, se busca dentro de el

TICKET = re.compile(r"(RCS|ENG|RTS|OUTM|DATASCI)-(\d{3,6})", re.I)
FECHA = re.compile(r"^(20\d{2}-\d{2}-\d{2})")

PEGABLE = ("comentario", "respuesta", "teams", "correo", "pegar", "email", "mensaje")
EFIMERO = ("cola-", "cola_", "reparto", "refresco", "asignacion-", "unassigned")
ANDAMIO = ("plan", "pasos", "prompt", "borrador", "draft", "checklist")
DESTILADO = ("cosecha",)
CONSOLIDA = ("informe", "instructivo", "causa", "analisis", "verificacion", "fix",
             "rca", "investigacion", "hallazgo", "diagnostico")

# Seccion del informe -> etiqueta en el chunk. El orden manda en la salida.
SECCIONES = [
    (("resumen", "tres frases", "que pasa"), "Que pasa"),
    (("causa raiz", "causa ra", "root cause", "hipotesis"), "Causa"),
    (("que se verifico", "verificado", "evidencia"), "Evidencia"),
    (("riesgo", "impacto"), "Impacto"),
    (("que sigue", "siguiente paso", "accion", "pendiente", "decision"), "Que sigue"),
    (("precedente", "relacionado"), "Precedentes"),
]

# Router de carpeta. El orden manda: la primera que engancha se queda con el chunk.
RUTAS = [
    (26, ("adusa", "ahold", "delhaize", "hannaford", "food lion", "stop & shop",
          "stop and shop", "giant food", "gsc", "martins")),
    (27, ("cerebro", "moscu", "segundo cerebro", "sessions.db", "bin/buscar", "fts5")),
    (17, ("reunion", "reuni", "guion de preguntas", "meeting", "llamada con", "standup",
          "agenda de la")),
    (16, ("causa raiz", "root cause", "confirmada.", "solucion", "workaround", "el fix",
          "resuelto", "reproduccion")),
]


def normal(s):
    s = s.lower()
    for a, b in (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"), ("ñ", "n")):
        s = s.replace(a, b)
    return s


def clasificar(nombre):
    n = normal(nombre)
    if any(k in n for k in DESTILADO):
        return "destilado"
    if any(k in n for k in EFIMERO):
        return "efimero"
    if any(k in n for k in PEGABLE):
        return "pegable"
    if any(k in n for k in CONSOLIDA):
        return "consolida"
    if any(k in n for k in ANDAMIO):
        return "andamio"
    return "consolida"


def fecha_de(nombre, ruta):
    m = FECHA.match(nombre)
    if m:
        try:
            return m.group(1), int(datetime.strptime(m.group(1), "%Y-%m-%d").timestamp())
        except ValueError:
            pass
    ts = int(os.path.getmtime(ruta))
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d"), ts


def ticket_de(nombre, texto):
    m = TICKET.search(nombre)
    if m:
        return f"{m.group(1).upper()}-{m.group(2)}"
    m = TICKET.search(texto[:1500])
    if m:
        return f"{m.group(1).upper()}-{m.group(2)}"
    return None


def secciones(texto):
    """Corta el markdown por encabezados y devuelve {etiqueta: texto} solo de lo que sirve."""
    bloques = re.split(r"^\s{0,3}#{1,4}\s+(.+?)\s*$", texto, flags=re.M)
    salida = {}
    if len(bloques) < 3:
        return salida
    for i in range(1, len(bloques) - 1, 2):
        titulo, cuerpo = normal(bloques[i]), bloques[i + 1].strip()
        if not cuerpo:
            continue
        for claves, etiqueta in SECCIONES:
            if any(k in titulo for k in claves):
                if etiqueta not in salida:
                    salida[etiqueta] = re.sub(r"\n{3,}", "\n\n", cuerpo)[:1200]
                break
    return salida


def primeras_frases(texto, n=3):
    cuerpo = re.sub(r"^---.*?---", "", texto, flags=re.S).strip()
    cuerpo = re.sub(r"^\s{0,3}#{1,6}.*$", "", cuerpo, flags=re.M)
    cuerpo = re.sub(r"```.*?```", "", cuerpo, flags=re.S)
    cuerpo = re.sub(r"\s+", " ", cuerpo).strip()
    frases = [f for f in re.split(r"(?<=[.:])\s+", cuerpo) if not es_etiqueta(f)]
    return " ".join(frases[:n])[:600]


def es_etiqueta(frase):
    """Descarta rotulos de formulario. 'Fecha:' o 'Entregable:' no describen nada."""
    f = frase.strip()
    return len(f) < 26 and (f.endswith(":") or f.endswith("."))


def titular(notas):
    """El titulo sale de la conclusion, no del primer renglon que aparezca."""
    for n in reversed(notas):
        qp = n["secciones"].get("Que pasa") or n["secciones"].get("Causa")
        if qp:
            t = re.sub(r"\s+", " ", re.sub(r"^[-*\d.\s]+", "", qp)).strip()
            if len(t) > 25:
                return t[:110]
    for n in reversed(notas):
        for m in re.finditer(r"^\s{0,3}#{1,3}\s+(.+)$", n["texto"], flags=re.M):
            t = m.group(1).strip(" #*")
            t = re.sub(r"^(informe|instructivo|analisis|an.lisis)\s*[.:-]\s*", "", t, flags=re.I)
            if len(t) > 18 and not es_etiqueta(t):
                return t[:110]
    return primeras_frases(notas[-1]["texto"], 2)[:110]


def carpeta_de(texto, ticket):
    """La carpeta 27 es del sistema Cerebro. Una nota de ticket nunca cae ahi aunque
    mencione la palabra cerebro, porque la escribio una sesion de cerebro-ticket."""
    plano = normal(texto[:4000])
    for fid, claves in RUTAS:
        if fid == 27 and ticket:
            continue
        if any(k in plano for k in claves):
            return fid
    return 19


def leer(ruta):
    try:
        return open(ruta, encoding="utf-8", errors="replace").read()
    except OSError:
        return ""


def construir(ticket, notas):
    """Un chunk por ticket. Conclusion arriba, rastro abajo, cronica en ninguna parte."""
    notas.sort(key=lambda x: x["fecha"])
    fechas = [n["fecha"] for n in notas]
    rango = fechas[0] if fechas[0] == fechas[-1] else f"{fechas[0]} a {fechas[-1]}"

    acumulado, vistos = {}, set()
    for n in notas:
        for etiqueta, cuerpo in n["secciones"].items():
            firma = normal(cuerpo)[:180]
            if firma in vistos:
                continue
            vistos.add(firma)
            acumulado.setdefault(etiqueta, []).append((n["fecha"], cuerpo))

    lineas = [f"Ticket {ticket}. Trabajado el {rango}. {len(notas)} notas en inbox."]

    if not acumulado:
        lineas.append("")
        lineas.append("Sin secciones reconocibles. Extracto de la nota mas reciente:")
        lineas.append(primeras_frases(notas[-1]["texto"], 4))
    else:
        for _, etiqueta in SECCIONES:
            if etiqueta not in acumulado:
                continue
            lineas.append("")
            lineas.append(f"## {etiqueta}")
            for fecha, cuerpo in acumulado[etiqueta][-2:]:
                marca = f"[{fecha}] " if len(acumulado[etiqueta]) > 1 else ""
                lineas.append(marca + cuerpo)

    lineas.append("")
    lineas.append("## Rastro")
    for n in notas:
        lineas.append(f"{n['fecha']} inbox/{n['archivo']}")

    cuerpo = "\n".join(lineas)
    if len(cuerpo) > TECHO_CUERPO:
        cuerpo = cuerpo[:TECHO_CUERPO] + "\n\n[cortado en el techo, el detalle esta en el rastro]"

    titulo = f"{ticket}. {titular(notas)}".strip().rstrip(".") + f" — {fechas[-1]}"
    return titulo, cuerpo, notas[-1]["ts"], carpeta_de(cuerpo, ticket)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--aplicar", action="store_true", help="escribe en la base")
    ap.add_argument("--desde", default="2026-08-25", help="fecha minima del archivo")
    ap.add_argument("--archivar", action="store_true", help="mueve lo ingerido a inbox/archivo/")
    ap.add_argument("--db", default=DB)
    a = ap.parse_args()

    if not os.path.isdir(INBOX):
        sys.exit(f"no encuentro {INBOX}")

    grupos, sueltas, descartes = defaultdict(list), [], defaultdict(list)

    for archivo in sorted(os.listdir(INBOX)):
        if not archivo.lower().endswith(".md"):
            continue
        ruta = os.path.join(INBOX, archivo)
        if not os.path.isfile(ruta):
            continue
        fecha, ts = fecha_de(archivo, ruta)
        if fecha < a.desde:
            descartes["antes del corte"].append(archivo)
            continue
        clase = clasificar(archivo)
        if clase in ("pegable", "efimero", "andamio"):
            descartes[clase].append(archivo)
            continue
        texto = leer(ruta)
        if len(texto.strip()) < 120:
            descartes["vacio"].append(archivo)
            continue
        nota = {"archivo": archivo, "fecha": fecha, "ts": ts, "texto": texto,
                "secciones": secciones(texto)}
        if clase == "destilado":
            sueltas.append(nota)
            continue
        t = ticket_de(archivo, texto)
        if t:
            grupos[t].append(nota)
        else:
            sueltas.append(nota)

    planes = []
    for ticket, notas in sorted(grupos.items()):
        titulo, cuerpo, ts, fid = construir(ticket, notas)
        planes.append({"titulo": titulo, "cuerpo": cuerpo, "ts": ts, "carpeta": fid,
                       "fuentes": [n["archivo"] for n in notas]})
    for n in sueltas:
        texto = n["texto"]
        titulo = None
        m = re.search(r"^\s{0,3}#\s+(.+)$", texto, flags=re.M)
        if m:
            titulo = m.group(1).strip()[:110]
        if not titulo:
            titulo = re.sub(r"^20\d{2}-\d{2}-\d{2}-|\.md$", "", n["archivo"]).replace("-", " ")
        cuerpo = texto[:TECHO_CUERPO]
        cuerpo += f"\n\n## Rastro\n{n['fecha']} inbox/{n['archivo']}"
        planes.append({"titulo": f"{titulo} — {n['fecha']}", "cuerpo": cuerpo, "ts": n["ts"],
                       "carpeta": carpeta_de(texto, None),
                       "fuentes": [n["archivo"]]})

    con = sqlite3.connect(a.db)
    existentes = {t for (t,) in con.execute("SELECT title FROM knowledge_chunks")}
    nombres = {i: n for i, n in con.execute("SELECT id,name FROM knowledge_folders")}

    nuevos = [p for p in planes if p["titulo"] not in existentes]
    repetidos = len(planes) - len(nuevos)

    print(f"inbox: {len(os.listdir(INBOX))} entradas, corte desde {a.desde}")
    for clase, lista in sorted(descartes.items()):
        print(f"  descarta {clase}: {len(lista)}")
    print(f"  tickets consolidados: {len(grupos)}")
    print(f"  notas sueltas y cosechas: {len(sueltas)}")
    print(f"  chunks a escribir: {len(nuevos)}  (repetidos que se saltan: {repetidos})")
    print()
    por_carpeta = defaultdict(int)
    for p in nuevos:
        por_carpeta[p["carpeta"]] += 1
    for fid, n in sorted(por_carpeta.items()):
        print(f"  carpeta {fid} {nombres.get(fid, '?')}: {n}")
    print()
    for p in nuevos[:12]:
        print(f"  [{p['carpeta']}] {p['titulo'][:96]}  ({len(p['cuerpo'])}B, "
              f"{len(p['fuentes'])} fuentes)")
    if len(nuevos) > 12:
        print(f"  ... y {len(nuevos) - 12} mas")

    if not a.aplicar:
        print("\nensayo. nada escrito. corre con --aplicar para escribir.")
        con.close()
        return

    cur = con.cursor()
    escritos = 0
    for p in nuevos:
        ordv = cur.execute("SELECT COALESCE(MAX(ord),0)+1 FROM knowledge_chunks WHERE folder_id=?",
                           (p["carpeta"],)).fetchone()[0]
        cur.execute("""INSERT INTO knowledge_chunks
            (folder_id,title,body,source_path,ord,created_at,contextualized_body,
             embedding_model,embedding_dim)
            VALUES(?,?,?,?,?,?,'','',0)""",
                    (p["carpeta"], p["titulo"], p["cuerpo"],
                     "inbox/" + ";".join(p["fuentes"])[:400], ordv, p["ts"]))
        escritos += 1
    con.commit()
    print(f"\nescritos {escritos} chunks. total ahora "
          f"{con.execute('SELECT COUNT(*) FROM knowledge_chunks').fetchone()[0]}.")
    print("integridad:", con.execute("PRAGMA integrity_check").fetchone()[0])
    con.close()

    if a.archivar:
        destino = os.path.join(INBOX, "archivo")
        os.makedirs(destino, exist_ok=True)
        movidos = 0
        for p in nuevos:
            for f in p["fuentes"]:
                o = os.path.join(INBOX, f)
                if os.path.isfile(o):
                    os.replace(o, os.path.join(destino, f))
                    movidos += 1
        print(f"archivados {movidos} archivos en inbox/archivo/")


if __name__ == "__main__":
    main()
