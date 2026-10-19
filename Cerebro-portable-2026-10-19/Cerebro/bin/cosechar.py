#!/usr/bin/env python3
"""
Registro de cosecha de transcripciones de chats de Cowork.

Las transcripciones NO se pueden leer por archivo desde el sandbox. Solo la sesion actual
deja su jsonl visible. Las demas se leen con la herramienta mcp__session_info__read_transcript.
Este script no lee nada. Lleva la cuenta de que sesion ya se coseho, para no repetir trabajo
ni volver a meter el mismo hallazgo a la base.

Uso:
    bin/cosechar.py pendientes  < lista.json   # que sesiones faltan, lee JSON de list_sessions
    bin/cosechar.py marcar <session_id> <titulo> <archivo_inbox>
    bin/cosechar.py estado                     # que se cosecho y cuando
"""

import json
import sys
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
REGISTRO = RAIZ / "cosecha" / "registro.json"


def cargar():
    if REGISTRO.exists():
        return json.loads(REGISTRO.read_text(encoding="utf-8"))
    return {"sesiones": {}}


def guardar(d):
    REGISTRO.parent.mkdir(exist_ok=True)
    REGISTRO.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")


def pendientes():
    """Recibe por stdin el JSON de sesiones. Imprime las que faltan."""
    reg = cargar()
    try:
        entrada = json.load(sys.stdin)
    except json.JSONDecodeError:
        print("Pasa por stdin un JSON con [{\"session_id\":..., \"title\":...}]")
        sys.exit(1)
    if isinstance(entrada, dict):
        entrada = entrada.get("sessions", [])
    faltan = [s for s in entrada if s.get("session_id") not in reg["sesiones"]]
    print(f"{len(faltan)} sesiones sin cosechar de {len(entrada)}")
    for s in faltan:
        print(f"  {s.get('session_id')}  {s.get('title', 'sin titulo')}")
    return faltan


def marcar(sid, titulo, archivo):
    reg = cargar()
    reg["sesiones"][sid] = {
        "titulo": titulo,
        "cosechado": datetime.now().isoformat(timespec="seconds"),
        "inbox": archivo,
    }
    guardar(reg)
    print(f"Marcada {sid} -> {archivo}")


def estado():
    reg = cargar()
    s = reg["sesiones"]
    print(f"{len(s)} sesiones cosechadas")
    for sid, d in sorted(s.items(), key=lambda x: x[1]["cosechado"], reverse=True):
        print(f"  {d['cosechado']}  {d['titulo'][:40]:40s}  {d['inbox']}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "pendientes":
        pendientes()
    elif cmd == "marcar":
        marcar(sys.argv[2], sys.argv[3], sys.argv[4])
    elif cmd == "estado":
        estado()
    else:
        print(__doc__)
        sys.exit(1)
