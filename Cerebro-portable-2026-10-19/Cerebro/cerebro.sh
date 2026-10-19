# Atajos de Cerebro para Mac y Linux. Equivalente de cerebro.ps1.
# Cargalo una vez por sesion, desde cualquier sitio:
#
#     source ~/Cerebro/cerebro.sh
#
# Despues los comandos son cortos:
#
#     buscar "izenda export"
#     buscar RCS-28535
#     carpetas
#     guardar 16 "Titulo del hallazgo" "cuerpo de la nota"
#     guardar-archivo 16 "Titulo" inbox/2026-09-08-tema.md
#     anotar RCS-28482 "pegue el comentario, quedo en Work in progress"
#     ingerir            ensayo, muestra que va a entrar a la base
#     ingerir-aplicar    escribe en la base
#     indexar            regenera tickets/
#     espejo             regenera brain/markdown desde la base
#     evaluar            mide el clasificador de la cola
#     refrescar          dice que etiquetas del eval vencieron
#     estado             cifras de la base y chequeo de integridad
#     cerrar             ingerir-aplicar mas indexar, la rutina de cierre del dia
#     compuerta          revisa inbox/*.md por credenciales; ingerir-aplicar y cerrar la corren solos
#     secretos [rutas]   informe de credenciales sin imprimir valores
#     verificar archivo [--destino cliente]   grounding de un borrador contra Cerebro
#     evaluar-busqueda   hit@5, MRR y nDCG de bm25, hibrido y reranker
#     cerebro            te para en la raiz de la carpeta

# Resuelve la raiz sin depender del directorio actual. zsh y bash.
if [ -n "${ZSH_VERSION:-}" ]; then
  CEREBRO_ROOT="$(cd "$(dirname "${(%):-%N}")" && pwd)"
else
  CEREBRO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
fi
export CEREBRO_ROOT

if command -v python3 >/dev/null 2>&1; then
  export CEREBRO_PY=python3
elif command -v python >/dev/null 2>&1; then
  export CEREBRO_PY=python
else
  echo "No encuentro Python. Instalalo con 'brew install python3'"
  return 1 2>/dev/null || exit 1
fi

_cerebro_py() { ( cd "$CEREBRO_ROOT" && "$CEREBRO_PY" "bin/$1" "${@:2}" ); }

cerebro()         { cd "$CEREBRO_ROOT"; }
buscar()          { _cerebro_py buscar "$@"; }
anotar()          { ( cd "$CEREBRO_ROOT" && ./bin/anotar "$@" ); }
indexar()         { _cerebro_py indexar_tickets.py "$@"; }
evaluar()         { _cerebro_py eval_cola.py "$@"; }
refrescar()       { _cerebro_py refrescar_eval.py "$@"; }
ingerir()         { _cerebro_py ingerir_inbox.py "$@"; }
secretos()        { ( cd "$CEREBRO_ROOT" && "$CEREBRO_PY" bin/secretos.py "$@" ); }
compuerta()       { ( cd "$CEREBRO_ROOT" && "$CEREBRO_PY" bin/secretos.py --compuerta inbox/*.md ); }
verificar()       { ( cd "$CEREBRO_ROOT" && "$CEREBRO_PY" bin/grounding.py "$@" ); }
evaluar-busqueda() { ( cd "$CEREBRO_ROOT" && "$CEREBRO_PY" bin/eval_cerebro.py correr --modos bm25,hybrid,rerank && "$CEREBRO_PY" bin/eval_cerebro.py resumen --modos bm25,hybrid,rerank ); }
ingerir-aplicar() { compuerta || return 1; _cerebro_py ingerir_inbox.py --aplicar "$@"; }
cola()            { _cerebro_py cola.py cola/jira-dump.json "$@"; }
carpetas()        { ( cd "$CEREBRO_ROOT" && ./bin/guardar --carpetas ); }

guardar() {
  if [ $# -lt 3 ]; then
    echo 'uso: guardar <carpeta> "titulo" "cuerpo"'; return 1
  fi
  printf '%s' "$3" | ( cd "$CEREBRO_ROOT" && ./bin/guardar "$1" "$2" )
}

guardar-archivo() {
  if [ $# -lt 3 ]; then
    echo 'uso: guardar-archivo <carpeta> "titulo" ruta/al/archivo.md'; return 1
  fi
  if [ ! -f "$3" ]; then echo "no encuentro el archivo $3"; return 1; fi
  ( cd "$CEREBRO_ROOT" && ./bin/guardar "$1" "$2" ) < "$3"
}

espejo()          { ( cd "$CEREBRO_ROOT" && "$CEREBRO_PY" bin/db_a_markdown.py brain/sessions.db brain/markdown >/dev/null && echo "brain/markdown regenerado" ); }

cerrar() {
  echo "== ingerir-aplicar =="; ingerir-aplicar || return 1
  echo; echo "== indexar =="; indexar || return 1
  echo; echo "== espejo =="; espejo || return 1
  echo; echo "== estado =="; estado
}

estado() {
  ( cd "$CEREBRO_ROOT" && "$CEREBRO_PY" - <<'PY'
import sqlite3, os, glob
db = os.path.join('brain', 'sessions.db')
c = sqlite3.connect(db)
q = lambda s: c.execute(s).fetchone()[0]
print('chunks     ', q('select count(*) from knowledge_chunks'))
print('fts        ', q('select count(*) from chunks_fts'))
print('carpetas   ', q('select count(*) from knowledge_folders'))
print('items      ', q('select count(*) from items'))
print('integridad ', q('pragma integrity_check'))
print('ultimo     ', c.execute("select date(max(created_at),'unixepoch') from knowledge_chunks").fetchone()[0])
print('backups    ', len(glob.glob(db + '.bak-*')))
print('journal    ', 'SI, cuidado' if os.path.exists(db + '-journal') else 'no')
print('tickets    ', len(glob.glob(os.path.join('tickets', '*.md'))))
print('inbox      ', len(glob.glob(os.path.join('inbox', '*.md'))))
PY
  )
}

printf '\033[32mCerebro cargado. Python: %s. Raiz: %s\033[0m\n' "$CEREBRO_PY" "$CEREBRO_ROOT"
printf '\033[90mComandos: buscar, carpetas, guardar, guardar-archivo, anotar, ingerir, ingerir-aplicar, indexar, espejo, evaluar, refrescar, cola, estado, cerrar, cerebro, compuerta, secretos, verificar, evaluar-busqueda\033[0m\n'
