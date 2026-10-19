# Cerebro en otro PC. Paquete del 2026-10-19

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
