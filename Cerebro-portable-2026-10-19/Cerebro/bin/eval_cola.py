#!/usr/bin/env python3
"""Mide el clasificador de urgencia contra las etiquetas fijadas a mano.

Cada vez que se toque el lexico de bin/cola.py, corre esto. Si la exactitud baja, el cambio
esta mal. Las etiquetas viven en cola/EVAL-clasificador.json y se fijaron leyendo los
comentarios reales, no adivinando.

Uso:  python3 bin/eval_cola.py [cola/jira-dump.json]
"""
import json, os, sys, datetime, importlib.util

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
spec = importlib.util.spec_from_file_location("cola", os.path.join(ROOT, "bin", "cola.py"))
cola = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cola)

dump = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "cola", "jira-dump.json")
gold = json.load(open(os.path.join(ROOT, "cola", "EVAL-clasificador.json"), encoding="utf-8"))
esperado = {c["ticket"]: c for c in gold["casos"]}

d = json.load(open(dump, encoding="utf-8"))
ahora = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-4)))

ok = fallos = ausentes = 0
detalle = []
for i in d["issues"]["nodes"]:
    tid = i["key"]
    if tid not in esperado:
        ausentes += 1
        continue
    got = cola.clasificar_final(i, ahora)[0]["nivel"]
    want = esperado[tid]["nivel"]
    if got == want:
        ok += 1
    else:
        fallos += 1
        detalle.append((tid, want, got, esperado[tid]["evidencia"]))

# Antes de reportar nada, mira el calendario. Una etiqueta fijada antes del ultimo comentario
# de su ticket describe un momento que ya paso, y cuenta como fallo del lexico sin serlo.
# El 8 sep 2026 los cuatro fallos que marcaban 73% eran cuatro etiquetas vencidas.
fijado = gold.get("fijado", "")
vencidas = []
for i in d["issues"]["nodes"]:
    tid = i["key"]
    if tid not in esperado:
        continue
    cs = [c for c in i["fields"].get("comment", {}).get("comments", [])
          if not c["author"]["accountId"].startswith(cola.BOTS)]
    if cs and cs[-1]["created"][:10] > fijado:
        vencidas.append(tid)

evaluados = ok + fallos
print(f"evaluados {evaluados} de {len(esperado)} etiquetados")
if ausentes:
    print(f"{ausentes} tickets del volcado no estan etiquetados, no cuentan")
print(f"exactitud {ok}/{evaluados} = {ok / evaluados:.0%}" if evaluados else "sin casos")
for tid, want, got, ev in detalle:
    aviso = "  ETIQUETA VENCIDA, no es fallo del lexico" if tid in vencidas else ""
    print(f"  FALLA {tid}: esperaba nivel {want}, dio {got}{aviso}")
    print(f"        evidencia: {ev}")

if vencidas:
    print(f"\nAVISO: {len(vencidas)} etiquetas fijadas el {fijado} tienen comentarios posteriores.")
    print("Refrescalas antes de tocar el lexico:  python3 bin/refrescar_eval.py")
    print("Tickets: " + ", ".join(sorted(vencidas)))

sys.exit(1 if fallos else 0)
