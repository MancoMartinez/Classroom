#!/usr/bin/env python3
"""Registra en la bitacora de un ticket lo que Juan ya trabajo. Append only, nunca pisa.

    python bin/anotar.py RCS-28482 "pegue el comentario del MISC tab, quedo en Work in progress"
    python bin/anotar.py RCS-28482 --ver

Version portable de bin/anotar, corre en Windows y en Mac. Baja el ticket a
TRABAJADO SIN PEGAR EN JIRA y recalcula la cola si hay volcado de Jira.
"""
import os
import re
import subprocess
import sys
import time

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
CABECERA = ("# {tid} — bitacora\n\n"
            "Lo que Juan reporto haber trabajado. Jira sigue siendo la fuente de verdad del "
            "estado.\nAdjuntos de este ticket en `adjuntos/{tid}/`.\n")


def main():
    if len(sys.argv) < 2:
        sys.exit('uso: python bin/anotar.py RCS-28482 "lo que hiciste"')
    tid = sys.argv[1].upper()
    if not re.match(r"^(RCS|ENG|RTS|OUTM|DATASCI)-\d+$", tid):
        sys.exit(f"'{tid}' no parece un ticket. formato RCS-28482")

    d = os.path.join(ROOT, "bitacora")
    os.makedirs(d, exist_ok=True)
    os.makedirs(os.path.join(ROOT, "adjuntos", tid), exist_ok=True)
    f = os.path.join(d, f"{tid}.md")

    if len(sys.argv) > 2 and sys.argv[2] == "--ver":
        if os.path.exists(f):
            print(open(f, encoding="utf-8").read())
        else:
            print(f"sin bitacora para {tid}")
        return

    nota = " ".join(sys.argv[2:]).strip()
    if not nota and not sys.stdin.isatty():
        nota = sys.stdin.read().strip()
    if not nota:
        sys.exit("no llego nota")

    if not os.path.exists(f):
        open(f, "w", encoding="utf-8").write(CABECERA.format(tid=tid))
    with open(f, "a", encoding="utf-8") as fh:
        fh.write(f"\n## {time.strftime('%Y-%m-%d')}\n\n{nota} ({time.strftime('%H:%M')})\n")
    print(f"anotado en bitacora/{tid}.md")

    dump = os.path.join(ROOT, "cola", "jira-dump.json")
    if os.path.exists(dump):
        r = subprocess.run([sys.executable, os.path.join(ROOT, "bin", "cola.py"), dump],
                           capture_output=True)
        print("cola recalculada" if r.returncode == 0 else "la cola no se pudo recalcular")


if __name__ == "__main__":
    main()
