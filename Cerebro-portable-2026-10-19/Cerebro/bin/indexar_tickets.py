#!/usr/bin/env python3
"""Genera tickets/INDICE.md y una ficha por ticket a partir de todo el cerebro.

Escanea brain/markdown, brain/memoria, inbox y adusa-envio-hoy. Extrae cada
identificador de ticket, junta el parrafo donde aparece y arma una ficha por
ticket con la evidencia ordenada de mas reciente a mas antigua.

Uso:  python3 bin/indexar_tickets.py [raiz]
"""
import os, re, sys, collections, datetime

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else
                       os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
OUT = os.path.join(ROOT, "tickets")
FUENTES = ["brain/markdown", "brain/memoria", "inbox", "adusa-envio-hoy", "bitacora", "adjuntos"]
EXT = (".md", ".txt")

TICKET = re.compile(r"\b(?:RCS|ENG|RTS|OUTM|DATASCI)-\d{3,6}\b")
FECHA_NOMBRE = re.compile(r"(20\d{2})-(\d{2})-(\d{2})")
META_CHUNK = re.compile(r"^_chunk (\d+)(?: · (\d{4}-\d{2}-\d{2}))?(?: · fuente: (.+?))?_\s*$")
JIRA = "https://trebuco.atlassian.net/browse/"

CLIENTES = [
    "Ahold", "ADUSA", "Delhaize", "Food Lion", "Stop & Shop", "Hannaford", "Giant",
    "Nordstrom", "Torrid", "Tailored Brands", "United Supermarkets", "Albertsons",
    "Stater Bros", "Vitamin Shoppe", "AutoZone", "Walmart", "Nike", "TJX", "CWH",
    "Camping World", "Sephora", "Lowe", "Dollar General", "Burlington", "Ulta",
]
ESTADOS = [
    "Under Customer Review", "Under Support Review", "Under Engineering Review",
    "Accepted into Development", "Waiting for Software Release", "Work in progress",
    "Needs Attention", "Completed", "Closed", "Resolved", "Open", "Triage",
]


def leer(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def fecha_de(path, texto_bloque):
    m = META_CHUNK.search(texto_bloque or "")
    if m and m.group(2):
        return m.group(2)
    m = FECHA_NOMBRE.search(os.path.basename(path))
    if m:
        return "-".join(m.groups())
    m = FECHA_NOMBRE.search(texto_bloque or "")
    if m:
        return "-".join(m.groups())
    try:
        return datetime.date.fromtimestamp(os.path.getmtime(path)).isoformat()
    except OSError:
        return ""


def bloques(path):
    """Devuelve (titulo_seccion, texto) por seccion de nivel 2, o el archivo entero."""
    texto = leer(path)
    if "\n## " not in texto:
        return [(os.path.basename(path), texto)]
    partes = re.split(r"\n(?=## )", texto)
    out = []
    for p in partes:
        titulo = p.splitlines()[0].lstrip("# ").strip() if p.strip() else ""
        out.append((titulo or os.path.basename(path), p))
    return out


def parrafos_con(texto, tid):
    out = []
    for par in re.split(r"\n\s*\n", texto):
        if tid in par:
            par = par.strip()
            if len(par) > 1400:
                i = par.find(tid)
                par = "…" + par[max(0, i - 500):i + 900] + "…"
            out.append(par)
    return out[:6]


def detectar(lista, texto):
    """Busca cada termino con frontera de palabra para no cazar 'Ulta' dentro de 'consulta'."""
    bajo = texto.lower()
    vistos = []
    for x in lista:
        if re.search(r"(?<![\wáéíóúñ])" + re.escape(x.lower()) + r"(?![\wáéíóúñ])", bajo):
            if x not in vistos:
                vistos.append(x)
    return vistos


def normalizar(p):
    return re.sub(r"\s+", " ", p).strip().lower()


def main():
    docs = []
    for base in FUENTES:
        d = os.path.join(ROOT, base)
        for dp, _, fs in os.walk(d):
            for f in fs:
                if f.lower().endswith(EXT) and f.upper() not in ("LEEME.MD", "README.MD"):
                    docs.append(os.path.join(dp, f))

    ev = collections.defaultdict(list)   # tid -> [(fecha, ruta, seccion, [parrafos])]
    for path in sorted(docs):
        rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
        for titulo, texto in bloques(path):
            for tid in sorted(set(TICKET.findall(texto))):
                pars = parrafos_con(texto, tid)
                if pars:
                    ev[tid].append((fecha_de(path, texto), rel, titulo, pars))

    os.makedirs(OUT, exist_ok=True)
    filas = []
    for tid, apar in sorted(ev.items()):
        # inbox y adusa-envio-hoy primero: son el original, brain/markdown es la copia ingerida
        apar.sort(key=lambda x: (x[0], not x[1].startswith(("inbox/", "adusa"))), reverse=True)

        # dedupe: el mismo parrafo aparece en el archivo de inbox y en el chunk exportado
        vistos = set()
        limpio = []
        for fecha, rel, titulo, pars in apar:
            nuevos = [p for p in pars if normalizar(p) not in vistos]
            vistos.update(normalizar(p) for p in nuevos)
            if nuevos:
                limpio.append((fecha, rel, titulo, nuevos))
        apar = limpio
        if not apar:
            continue

        todo = "\n".join(p for a in apar for p in a[3])
        clientes = detectar(CLIENTES, todo)
        if not clientes and any("adusa" in a[1].lower() for a in apar):
            clientes = ["ADUSA"]
        estados = detectar(ESTADOS, "\n".join(apar[0][3]))
        ultima = apar[0][0]
        docs_n = len({a[1] for a in apar})

        L = [f"# {tid}", "", f"{JIRA}{tid}", ""]
        L.append(f"Cliente: {', '.join(clientes[:3]) if clientes else 'sin identificar'}  ")
        L.append(f"Ultima actividad registrada en el cerebro: {ultima}  ")
        L.append(f"Aparece en {docs_n} documentos, {len(apar)} secciones")
        L += ["", "> El estado real vive en Jira. Esto es lo que quedo escrito, no la fuente de verdad.", ""]

        bit = os.path.join(ROOT, "bitacora", f"{tid}.md")
        if os.path.exists(bit):
            entradas = re.findall(r"^##\s*(\d{4}-\d{2}-\d{2})\s*\n+(.+?)(?=\n##\s|\Z)",
                                  leer(bit), flags=re.M | re.S)
            if entradas:
                L += ["## Bitacora, lo que Juan reporto haber trabajado", ""]
                for fecha, cuerpo in sorted(entradas, reverse=True)[:8]:
                    L.append(f"- **{fecha}** {re.sub(chr(10) + '+', ' ', cuerpo).strip()[:400]}")
                L.append("")

        adj = os.path.join(ROOT, "adjuntos", tid)
        if os.path.isdir(adj):
            archivos = sorted(os.listdir(adj))
            if archivos:
                L += ["## Adjuntos", "",
                      *[f"- `adjuntos/{tid}/{a}`" for a in archivos[:30]], ""]
        if estados:
            L += ["## Estado mencionado en lo mas reciente", "", ", ".join(estados[:4]), ""]
        L += ["## Donde aparece", ""]
        for fecha, rel, titulo, _ in apar[:40]:
            L.append(f"- {fecha} · `{rel}` › {titulo[:90]}")
        L += ["", "## Evidencia", ""]
        for fecha, rel, titulo, pars in apar[:14]:
            L.append(f"### {fecha} · {titulo[:90]}")
            L.append(f"_{rel}_")
            L.append("")
            for p in pars:
                L.append(p)
                L.append("")
        with open(os.path.join(OUT, f"{tid}.md"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(L).rstrip() + "\n")

        filas.append((tid, clientes[0] if clientes else "", estados[0] if estados else "",
                      ultima, docs_n))

    def clave(f):
        pref, num = f[0].split("-")
        return (pref, -int(num))

    filas.sort(key=clave)
    hoy = datetime.date.today().isoformat()
    I = [
        "# Indice de tickets",
        "",
        f"Generado el {hoy} por `bin/indexar_tickets.py`. {len(filas)} tickets con rastro en el cerebro.",
        "",
        "El estado real siempre esta en Jira. Esta tabla dice que se escribio y cuando, "
        "para saber si ya hay material antes de investigar de cero.",
        "",
        "Un identificador escrito en el cerebro no garantiza que el ticket exista. "
        "Los desmentidos estan en [DUDOSOS.md](./DUDOSOS.md), que este script no pisa.",
        "",
        "| Ticket | Cliente | Ultimo estado escrito | Ultima actividad | Docs | Ficha |",
        "|---|---|---|---|---|---|",
    ]
    for tid, cli, est, ult, n in filas:
        I.append(f"| [{tid}]({JIRA}{tid}) | {cli} | {est} | {ult} | {n} | [ficha](./{tid}.md) |")
    I += ["", "## Los mas trabajados", ""]
    for tid, cli, est, ult, n in sorted(filas, key=lambda f: -f[4])[:20]:
        I.append(f"- {tid} · {cli or 'sin cliente'} · {n} documentos · ultima {ult}")
    with open(os.path.join(OUT, "INDICE.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(I) + "\n")

    print(f"{len(filas)} fichas escritas en {OUT}")


if __name__ == "__main__":
    main()
