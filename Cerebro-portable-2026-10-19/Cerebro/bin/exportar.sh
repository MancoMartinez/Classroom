#!/bin/bash
# Regenera el bundle portable completo del segundo cerebro.
# Portable: si no encuentra la app Moscú, trabaja con la base que ya está en el bundle.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STAMP=$(date +%Y-%m-%d)

APP_DB="$HOME/Library/Application Support/InterviewApp/sessions.db"
APP_MEM="$HOME/.claude/projects/-Users-MancoMenStudio-Desktop-InterviewApp/memory"
BUNDLE_DB="$ROOT/brain/sessions.db"

if [ -f "$APP_DB" ]; then
  echo "==> Cerrando Moscú si está abierta"
  pkill -f "Moscu.app/Contents/MacOS/Moscu" 2>/dev/null || true
  sleep 1
  echo "==> Copiando la base de la app al bundle (VACUUM)"
  cp "$BUNDLE_DB" "$BUNDLE_DB.bak-$(date +%Y%m%d-%H%M%S)" 2>/dev/null || true
  rm -f "$BUNDLE_DB"
  sqlite3 "$APP_DB" "VACUUM INTO '$BUNDLE_DB';"
else
  echo "==> Sin app Moscú a la vista, uso la base del bundle tal cual"
fi

if [ -d "$APP_MEM" ]; then
  echo "==> Copiando memorias de Claude"
  mkdir -p "$ROOT/brain/memoria"
  cp "$APP_MEM"/*.md "$ROOT/brain/memoria/" 2>/dev/null || true
fi

echo "==> Exportando la base a markdown"
mkdir -p "$ROOT/brain/markdown"
python3 "$ROOT/bin/db_a_markdown.py" "$BUNDLE_DB" "$ROOT/brain/markdown"

echo "==> Reindexando tickets"
python3 "$ROOT/bin/indexar_tickets.py" "$ROOT"

echo "==> Escribiendo el índice"
python3 "$ROOT/bin/hacer_indice.py" "$ROOT" "$STAMP"

if command -v zip >/dev/null 2>&1; then
  echo "==> Empaquetando"
  cd "$ROOT"
  rm -f "$ROOT/../Cerebro-$STAMP.zip"
  zip -qr "$ROOT/../Cerebro-$STAMP.zip" README.md CLAUDE.md MAPA.md bin brain inbox tickets \
      flujos investigaciones adusa-envio-hoy \
      -x "*.DS_Store" "*/node_modules/*" "*sessions.db.bak-*"
  echo "Listo: $ROOT/../Cerebro-$STAMP.zip  ($(du -h "$ROOT/../Cerebro-$STAMP.zip" | cut -f1))"
fi
