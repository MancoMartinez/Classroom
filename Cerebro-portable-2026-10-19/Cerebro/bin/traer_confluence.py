#!/usr/bin/env python3
"""Trae una carpeta de Confluence a markdown local y rehace su indice.

Dos modos, independientes:

  indice   Lee los .md que ya estan en el destino y reescribe INDICE.md.
           No toca la red. Sirve despues de que Claude baje fichas nuevas.

  bajar    Baja o refresca las paginas desde Confluence con la API REST.
           Necesita credenciales en el entorno:
               CONFLUENCE_BASE   https://trebuco.atlassian.net
               CONFLUENCE_USER   tu correo de Atlassian
               CONFLUENCE_TOKEN  token de API de https://id.atlassian.com/manage/tokens
           Solo reescribe la ficha si la version en Confluence subio.

Uso:
    python3 bin/traer_confluence.py indice
    python3 bin/traer_confluence.py indice --destino confluence/RTS-triage
    python3 bin/traer_confluence.py bajar --carpeta 478142038021
    python3 bin/traer_confluence.py bajar --carpeta 478142038021 --ensayo

La carpeta 478142038021 es "Triage" del espacio RTS, la de Diego Buelvas.
"""
import argparse, base64, json, os, re, sys, urllib.request, urllib.parse, datetime

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
DESTINO_DEFECTO = os.path.join(RAIZ, "confluence", "RTS-triage")
CARPETA_DEFECTO = "478142038021"


# ---------- frontmatter ----------

def leer_frontmatter(ruta):
    """Devuelve el dict del frontmatter YAML plano. Solo pares clave: valor."""
    datos, cuerpo_empieza = {}, False
    with open(ruta, encoding="utf-8") as fh:
        lineas = fh.readlines()
    if not lineas or lineas[0].strip() != "---":
        return datos
    for linea in lineas[1:]:
        if linea.strip() == "---":
            cuerpo_empieza = True
            break
        m = re.match(r"^([a-z_]+):\s*(.*)$", linea.rstrip("\n"))
        if m:
            datos[m.group(1)] = m.group(2).strip()
    return datos if cuerpo_empieza else {}


def escapar_pipe(texto):
    return texto.replace("|", "\\|")


# ---------- modo indice ----------

def hacer_indice(destino):
    fichas = []
    for nombre in sorted(os.listdir(destino)):
        if not nombre.endswith(".md") or nombre == "INDICE.md":
            continue
        ruta = os.path.join(destino, nombre)
        fm = leer_frontmatter(ruta)
        fm["_archivo"] = nombre
        fm["_bytes"] = os.path.getsize(ruta)
        fichas.append(fm)

    fichas.sort(key=lambda f: f.get("modificado", ""), reverse=True)

    hoy = datetime.date.today().isoformat()
    out = []
    out.append("# Fichas de triage de Confluence, espacio RTS")
    out.append("")
    out.append(f"{len(fichas)} fichas bajadas de la carpeta Triage que mantiene Diego Buelvas.")
    out.append("Formato fijo de 10 secciones: detalles del ticket, problema, perfil del cliente,")
    out.append("investigacion paso a paso con PASS y POINT OF FAILURE, causa raiz, hallazgos")
    out.append("adicionales, fix recomendado con opciones, preguntas abiertas, queries corridas, extras.")
    out.append("")
    out.append("Esto es material de precedente. Antes de investigar un sintoma parecido, busca aqui.")
    out.append("")
    out.append(f"Indice regenerado el {hoy} con `python3 bin/traer_confluence.py indice`.")
    out.append("No lo edites a mano, se reescribe completo.")
    out.append("")
    out.append("## Por que buscar aqui")
    out.append("")
    out.append("```bash")
    out.append('grep -ril "listagg" confluence/RTS-triage/')
    out.append('grep -l "tendertypegroup" confluence/RTS-triage/*.md')
    out.append("```")
    out.append("")
    out.append("## Fichas")
    out.append("")
    out.append("| Ticket | Cliente | Sintoma | Causa | Estado | Archivo |")
    out.append("|---|---|---|---|---|---|")
    for f in fichas:
        out.append("| {} | {} | {} | {} | {} | `{}` |".format(
            escapar_pipe(f.get("ticket", "?")),
            escapar_pipe(f.get("cliente", "")),
            escapar_pipe(f.get("sintoma", "")),
            escapar_pipe(f.get("causa", "")),
            escapar_pipe(f.get("estado_ficha", "")),
            f["_archivo"],
        ))
    out.append("")

    familias = {}
    for f in fichas:
        fam = f.get("familia")
        if fam:
            familias.setdefault(fam, []).append(f.get("ticket", "?"))
    if familias:
        out.append("## Familias de falla que se repiten")
        out.append("")
        for fam, tickets in sorted(familias.items()):
            out.append(f"- {fam}: {', '.join(tickets)}")
        out.append("")

    notas = [(f.get("ticket", "?"), f["nota_reutilizable"]) for f in fichas if f.get("nota_reutilizable")]
    if notas:
        out.append("## Notas que sirven para cualquier ticket")
        out.append("")
        for ticket, nota in notas:
            out.append(f"- {nota} ({ticket})")
        out.append("")

    ruta_indice = os.path.join(destino, "INDICE.md")
    with open(ruta_indice, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    print(f"INDICE.md reescrito con {len(fichas)} fichas: {ruta_indice}")


# ---------- modo bajar ----------

def credenciales():
    base = os.environ.get("CONFLUENCE_BASE", "https://trebuco.atlassian.net").rstrip("/")
    user = os.environ.get("CONFLUENCE_USER")
    token = os.environ.get("CONFLUENCE_TOKEN")
    if not user or not token:
        sys.exit("Faltan CONFLUENCE_USER y CONFLUENCE_TOKEN en el entorno. "
                 "Saca el token en https://id.atlassian.com/manage/tokens")
    auth = base64.b64encode(f"{user}:{token}".encode()).decode()
    return base, {"Authorization": f"Basic {auth}", "Accept": "application/json"}


def pedir(url, cabeceras):
    req = urllib.request.Request(url, headers=cabeceras)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def listar_paginas(base, cabeceras, carpeta):
    """Todas las paginas bajo la carpeta, con id, titulo y version."""
    paginas, inicio = [], 0
    while True:
        cql = urllib.parse.quote(f"ancestor={carpeta} and type=page")
        url = f"{base}/wiki/rest/api/content/search?cql={cql}&limit=50&start={inicio}&expand=version"
        data = pedir(url, cabeceras)
        for r in data.get("results", []):
            paginas.append({
                "id": r["id"],
                "titulo": r["title"],
                "version": r.get("version", {}).get("number", 0),
                "modificado": (r.get("version", {}).get("when") or "")[:10],
            })
        if len(data.get("results", [])) < data.get("limit", 0) or not data.get("_links", {}).get("next"):
            break
        inicio += data.get("limit", 50)
    return paginas


def bajar_cuerpo(base, cabeceras, page_id):
    url = f"{base}/wiki/rest/api/content/{page_id}?expand=body.storage,version"
    data = pedir(url, cabeceras)
    return data["body"]["storage"]["value"], data.get("version", {}).get("number", 0)


def a_texto(html):
    """Convierte el storage format a markdown. Usa html2text si esta, si no limpia a mano."""
    try:
        import html2text
        h = html2text.HTML2Text()
        h.body_width = 0
        h.ignore_images = True
        return h.handle(html)
    except ImportError:
        import html as _html
        texto = re.sub(r"<br\s*/?>", "\n", html)
        texto = re.sub(r"</(p|div|h[1-6]|tr|li)>", "\n", texto)
        texto = re.sub(r"<[^>]+>", "", texto)
        return _html.unescape(texto)


def slug(texto):
    texto = texto.lower()
    texto = re.sub(r"\[triage\]", "", texto)
    texto = re.sub(r"[^a-z0-9]+", "-", texto)
    return texto.strip("-")[:80]


def bajar(destino, carpeta, ensayo):
    base, cabeceras = credenciales()
    os.makedirs(destino, exist_ok=True)

    versiones = {}
    for nombre in os.listdir(destino):
        if nombre.endswith(".md") and nombre != "INDICE.md":
            fm = leer_frontmatter(os.path.join(destino, nombre))
            if fm.get("confluence_id"):
                versiones[fm["confluence_id"]] = (nombre, fm.get("version_confluence", ""))

    paginas = listar_paginas(base, cabeceras, carpeta)
    print(f"{len(paginas)} paginas en la carpeta {carpeta}")

    nuevas, actualizadas, iguales = 0, 0, 0
    for p in paginas:
        conocida = versiones.get(p["id"])
        if conocida and conocida[1] == str(p["version"]):
            iguales += 1
            continue
        if ensayo:
            print(("ACTUALIZA " if conocida else "NUEVA     ") + f'{p["id"]} {p["titulo"]}')
            nuevas += 0 if conocida else 1
            actualizadas += 1 if conocida else 0
            continue

        html, version = bajar_cuerpo(base, cabeceras, p["id"])
        cuerpo = a_texto(html)
        nombre = conocida[0] if conocida else slug(p["titulo"]) + ".md"
        ruta = os.path.join(destino, nombre)
        with open(ruta, "w", encoding="utf-8") as fh:
            fh.write("---\n")
            fh.write(f'titulo: {p["titulo"]}\n')
            fh.write(f'confluence_id: {p["id"]}\n')
            fh.write(f"version_confluence: {version}\n")
            fh.write(f'modificado: {p["modificado"]}\n')
            fh.write(f'fuente: {base}/wiki/spaces/RTS/pages/{p["id"]}\n')
            fh.write("---\n\n")
            fh.write(cuerpo)
        print(("actualizada " if conocida else "nueva       ") + nombre)
        if conocida:
            actualizadas += 1
        else:
            nuevas += 1

    print(f"\nnuevas {nuevas}, actualizadas {actualizadas}, sin cambio {iguales}")
    if not ensayo:
        hacer_indice(destino)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="modo", required=True)

    a = sub.add_parser("indice", help="rehacer INDICE.md desde los .md locales")
    a.add_argument("--destino", default=DESTINO_DEFECTO)

    b = sub.add_parser("bajar", help="bajar o refrescar desde Confluence")
    b.add_argument("--destino", default=DESTINO_DEFECTO)
    b.add_argument("--carpeta", default=CARPETA_DEFECTO)
    b.add_argument("--ensayo", action="store_true", help="solo dice que haria")

    args = ap.parse_args()
    destino = os.path.abspath(args.destino) if os.path.isabs(args.destino) else os.path.join(RAIZ, args.destino)

    if args.modo == "indice":
        hacer_indice(destino)
    else:
        bajar(destino, args.carpeta, args.ensayo)


if __name__ == "__main__":
    main()
