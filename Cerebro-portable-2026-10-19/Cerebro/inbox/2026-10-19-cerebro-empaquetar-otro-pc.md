# Cerebro portable para otro PC

Se agrego bin/empaquetar.sh. Corre despues de cerrar, valida integridad de brain/sessions.db, se detiene si hay notas de inbox mas nuevas que la base, copia Cerebro sin .venv-cerebro, copias bak de la base, tmp, handoff-antigravity e inbox/_to_delete_*, genera PC-NUEVO.md con los pasos de instalacion y deja una carpeta mas un zip junto a Cerebro.

Al 19 oct 2026 hay 185 notas en inbox mas nuevas que sessions.db (ultima escritura 15 oct 15:16). cerrar queda pendiente y lo ejecuta Juan desde la terminal del Mac.

Orden: source cerebro.sh, cerrar, bin/empaquetar.sh
