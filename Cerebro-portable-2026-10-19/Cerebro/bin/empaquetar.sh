#!/bin/bash
# Empaqueta Cerebro para otro PC. Corre DESPUES de cerrar.
#   source cerebro.sh && cerrar && bin/empaquetar.sh
# Opciones: --forzar (omite el chequeo de inbox pendiente), --sin-indice (no copia .cerebro/retrieval.sqlite)
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STAMP=$(date +%Y-%m-%d)
OUT="$ROOT/../Cerebro-portable-$STAMP"
FORZAR=0; SININDICE=0
for a in "$@"; do case "$a" in --forzar) FORZAR=1;; --sin-indice) SININDICE=1;; esac; done

DB="$ROOT/brain/sessions.db"
[ -f "$DB" ] || { echo "No encuentro $DB"; exit 1; }
[ -f "$DB-journal" ] && { echo "Hay journal junto a la base. Corre cerrar de nuevo."; exit 1; }

echo "==> Integridad de la base"
python3 - "$DB" <<'PY'
import sqlite3, sys
c = sqlite3.connect("file:%s?mode=ro" % sys.argv[1], uri=True)
r = c.execute("pragma integrity_check").fetchone()[0]
print("integridad", r)
sys.exit(0 if r == "ok" else 1)
PY

echo "==> Chequeo de inbox pendiente de cerrar"
PEND=$(find "$ROOT/inbox" -maxdepth 1 -name '*.md' -newer "$DB" ! -name '_to_delete_*' | wc -l | tr -d ' ')
if [ "$PEND" != "0" ] && [ "$FORZAR" = "0" ]; then
  echo "Hay $PEND notas en inbox mas nuevas que la base. Corre cerrar primero, o usa --forzar."
  exit 1
fi

echo "==> Copiando a $OUT/Cerebro"
rm -rf "$OUT"; mkdir -p "$OUT/Cerebro"
EXC=(--exclude='.venv-cerebro' --exclude='.DS_Store' --exclude='__pycache__' --exclude='.tmp.*'
     --exclude='brain/sessions.db.bak-*' --exclude='inbox/_to_delete_*' --exclude='inbox/x.tmp'
     --exclude='/tmp' --exclude='/handoff-antigravity' --exclude='/.impeccable')
[ "$SININDICE" = "1" ] && EXC+=(--exclude='.cerebro/retrieval.sqlite')
rsync -a "${EXC[@]}" "$ROOT/" "$OUT/Cerebro/"

cat > "$OUT/PC-NUEVO.md" <<MD
# Cerebro en otro PC. Paquete del $STAMP

1. Copia la carpeta Cerebro a la ruta que quieras, por ejemplo ~/Cerebro.
2. Instala Python 3.10 o superior y crea el entorno:
   cd ~/Cerebro
   python3 -m venv .venv-cerebro
   .venv-cerebro/bin/pip install -r bin/requirements-cerebro.txt
3. Carga los atajos: source ~/Cerebro/cerebro.sh
4. Verifica: estado (integridad ok, chunks, inbox). Luego: buscar "izenda export"
5. La primera busqueda descarga el modelo E5 y el reranker a la cache de Hugging Face. Necesita internet una vez.
   Si .cerebro/retrieval.sqlite no viajo, o la busqueda reclama indice: python3 bin/cerebro index
6. Registra el MCP en Claude Code, con las rutas del PC nuevo:
   claude mcp add cerebro -- ~/Cerebro/.venv-cerebro/bin/python ~/Cerebro/bin/cerebro_mcp.py
   En Claude Desktop, agrega el mismo comando en claude_desktop_config.json, seccion mcpServers.
7. Abre la carpeta en Claude (Code o Desktop). Lee AGENTS.md, CLAUDE.md y ESTADO.md.
   .claude/settings.json ya viaja con las denegaciones de guardar, ingerir y cerrar.
8. Fuera de la carpeta, reconecta: Jira/Atlassian, Teams y los skills cerebro-* de la cuenta Claude.
   skills/ viaja como copia de respaldo.

No viajan: .venv-cerebro, copias de seguridad de sessions.db, tmp/, handoff-antigravity/, inbox/_to_delete_*.
MD

echo "==> Verificando copia"
python3 - "$OUT/Cerebro/brain/sessions.db" <<'PY'
import sqlite3, sys
c = sqlite3.connect("file:%s?mode=ro" % sys.argv[1], uri=True)
print("copia integridad", c.execute("pragma integrity_check").fetchone()[0],
      "chunks", c.execute("select count(*) from knowledge_chunks").fetchone()[0])
PY

echo "==> Zip"
cd "$OUT/.."
rm -f "Cerebro-portable-$STAMP.zip"
zip -qr "Cerebro-portable-$STAMP.zip" "Cerebro-portable-$STAMP"
echo "Listo: $(cd "$OUT" && pwd)  y  $(pwd)/Cerebro-portable-$STAMP.zip ($(du -h "Cerebro-portable-$STAMP.zip" | cut -f1))"
