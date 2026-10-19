#!/usr/bin/env python3
"""Guarda una nota en la base. Version portable de bin/guardar, corre en Windows y en Mac.

    python bin/guardar.py --carpetas
    python bin/guardar.py 26 "Titulo"  --texto "cuerpo de la nota"
    python bin/guardar.py 26 "Titulo"  --archivo inbox/2026-09-08-tema.md
    type nota.md | python bin/guardar.py 26 "Titulo"          Windows
    cat nota.md  | python bin/guardar.py 26 "Titulo"          Mac

El bash `bin/guardar` sigue existiendo y hace lo mismo. Este archivo existe porque PowerShell no
ejecuta bash. Misma base, mismo backup, misma rotacion de dos copias.
"""
import argparse
import glob
import os
import shutil
import sqlite3
import sys
import time

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
DB = os.environ.get("CEREBRO_DB") or os.path.join(ROOT, "brain", "sessions.db")
COPIAS = 2


def carpetas(con):
    q = """SELECT f.id, f.name, COUNT(k.id) FROM knowledge_folders f
           LEFT JOIN knowledge_chunks k ON k.folder_id = f.id
           GROUP BY f.id ORDER BY f.id"""
    for fid, nombre, n in con.execute(q):
        print(f"  {fid:>3}  {nombre}  ({n})")


def moscu_abierta():
    """En macOS, Moscu abierta bloquea la escritura. En Windows no hay como verificarlo."""
    if sys.platform != "darwin":
        return False
    return os.system("pgrep -f 'Moscu.app/Contents/MacOS/Moscu' >/dev/null 2>&1") == 0


def respaldar(db):
    dest = f"{db}.bak-{time.strftime('%Y%m%d-%H%M%S')}"
    shutil.copy2(db, dest)
    viejos = sorted(glob.glob(f"{db}.bak-*"), key=os.path.getmtime, reverse=True)[COPIAS:]
    for v in viejos:
        try:
            os.remove(v)
        except OSError:
            pass
    return dest, len(viejos)


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("carpeta", nargs="?")
    ap.add_argument("titulo", nargs="?")
    ap.add_argument("--carpetas", action="store_true", help="lista las carpetas con sus IDs")
    ap.add_argument("--texto", help="cuerpo de la nota en la linea de comandos")
    ap.add_argument("--archivo", help="lee el cuerpo de un archivo")
    ap.add_argument("--db", default=DB)
    a = ap.parse_args()

    if not os.path.exists(a.db):
        sys.exit(f"no encuentro la base en {a.db}")

    if a.carpetas:
        con = sqlite3.connect(f"file:{a.db}?mode=ro", uri=True)
        carpetas(con)
        con.close()
        return

    if not a.carpeta or not a.titulo:
        sys.exit('uso: python bin/guardar.py 26 "Titulo" --texto "cuerpo"\n'
                 "     python bin/guardar.py --carpetas")

    if a.archivo:
        cuerpo = open(a.archivo, encoding="utf-8", errors="replace").read()
    elif a.texto:
        cuerpo = a.texto
    else:
        cuerpo = sys.stdin.read() if not sys.stdin.isatty() else ""
    if not cuerpo.strip():
        sys.exit("no llego cuerpo. usa --texto, --archivo, o mandalo por stdin")

    if moscu_abierta():
        sys.exit("Moscu esta abierta. Cierrala antes de escribir.")

    fid = int(a.carpeta)
    con = sqlite3.connect(a.db)
    if not con.execute("SELECT 1 FROM knowledge_folders WHERE id=?", (fid,)).fetchone():
        sys.exit(f"la carpeta {fid} no existe. corre: python bin/guardar.py --carpetas")

    bak, borrados = respaldar(a.db)
    print(f"backup en {os.path.basename(bak)}" + (f", {borrados} copias viejas borradas"
                                                  if borrados else ""))

    ordv = con.execute("SELECT COALESCE(MAX(ord),0)+1 FROM knowledge_chunks WHERE folder_id=?",
                       (fid,)).fetchone()[0]
    cur = con.cursor()
    cur.execute("""INSERT INTO knowledge_chunks
        (folder_id,title,body,source_path,ord,created_at,contextualized_body,
         embedding_model,embedding_dim)
        VALUES(?,?,?,?,?,?,'','',0)""",
                (fid, a.titulo, cuerpo, a.archivo or "terminal", ordv, int(time.time())))
    con.commit()
    print(f"guardado, chunk {cur.lastrowid}. total "
          f"{con.execute('SELECT COUNT(*) FROM knowledge_chunks').fetchone()[0]}.")
    con.close()


if __name__ == "__main__":
    main()
