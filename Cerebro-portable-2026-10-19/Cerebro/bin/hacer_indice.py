#!/usr/bin/env python3
"""Genera README.md: el punto de entrada que lee cualquier Claude al abrir el bundle."""
import sqlite3, sys, os, datetime, glob
root, stamp = sys.argv[1], sys.argv[2]
db = os.path.join(root, "brain", "sessions.db")
con = sqlite3.connect(db)

folders = con.execute("""
    SELECT f.id,f.name,COUNT(c.id) n FROM knowledge_folders f
    LEFT JOIN knowledge_chunks c ON c.folder_id=f.id
    GROUP BY f.id HAVING n>0 ORDER BY n DESC""").fetchall()
total = con.execute("SELECT COUNT(*) FROM knowledge_chunks").fetchone()[0]
try: items = con.execute("SELECT COUNT(*) FROM items").fetchone()[0]
except Exception: items = 0
mems = sorted(glob.glob(os.path.join(root, "brain", "memoria", "*.md")))
con.close()

L = [f"# Segundo cerebro — Juan Martínez", "",
     f"Exportado el {stamp}. {total} fragmentos de conocimiento, {items} items de la mesa de trabajo, {len(mems)} memorias.",
     "",
     "## Si eres Claude y acabas de abrir esto",
     "",
     "Lee `MAPA.md` primero, elige la ruta y salta. Si quieres el orden largo:",
     "",
     "1. `CLAUDE.md` — el contrato: reglas que no se negocian y por dónde entrar.",
     "2. `brain/memoria/MEMORY.md` — el índice de memorias. Cada línea apunta a un hecho verificado.",
     "3. `tickets/INDICE.md`, `flujos/INDICE.md`, `investigaciones/INDICE.md` — las tres vistas de trabajo.",
     "4. `brain/markdown/` — la base de conocimiento entera en texto plano, un archivo por carpeta.",
     "5. `brain/sessions.db` — la misma información en SQLite con FTS5.",
     "",
     "Para buscar rápido sin abrir nada:",
     "",
     "```bash",
     "bin/buscar \"lo que busques\"",
     "bin/buscar RCS-28535",
     "grep -ril \"lo que busques\" brain/markdown/ tickets/",
     "```",
     "",
     "## Qué hay en la base", "",
     "| # | Carpeta | Fragmentos |", "|---|---|---|"]
for fid, name, n in folders:
    L.append(f"| {fid} | {name} | {n} |")
L += ["", "## Memorias", ""]
for m in mems:
    b = os.path.basename(m)
    if b == "MEMORY.md": continue
    desc = ""
    for line in open(m).read().split("\n")[:8]:
        if line.startswith("description:"):
            desc = line.split(":", 1)[1].strip().strip('"'); break
    L.append(f"- `{b}` — {desc}")
L += ["", "## Cómo se regenera", "",
      "```bash", "./bin/exportar.sh", "```", "",
      "Cierra Moscú, copia la base con VACUUM, vuelca todo a markdown, reindexa los tickets, "
      "copia las memorias y comprime el bundle.",
      "", "## Estructura", "",
      "```", "Cerebro/",
      "├── MAPA.md            punto de entrada, elige la ruta según lo que vas a hacer",
      "├── CLAUDE.md          el contrato para cualquier sesión de Claude",
      "├── README.md          este archivo, generado",
      "├── inbox/             todo lo nuevo cae aquí sin pensarlo",
      "├── tickets/           una ficha por ticket, más INDICE.md (generado)",
      "├── flujos/            procesos y cómo se hace cada cosa (curado a mano)",
      "├── investigaciones/   causas raíz y mapas de sistema (curado a mano)",
      "├── brain/",
      "│   ├── sessions.db    la base de Moscú",
      "│   ├── markdown/      la base en texto plano",
      "│   └── memoria/       las memorias de Claude Code",
      "├── bin/               los scripts",
      "└── archivo/           lo viejo, guardado no borrado",
      "```"]
open(os.path.join(root, "README.md"), "w").write("\n".join(L))
print(f"   README.md ({len(folders)} carpetas, {len(mems)} memorias)")
