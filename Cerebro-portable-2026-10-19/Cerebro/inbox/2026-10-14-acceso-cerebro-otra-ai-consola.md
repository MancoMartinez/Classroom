# Acceso a Cerebro desde otra AI por consola

Raíz local: /Users/MancoMenStudio/Cerebro

Dar a la AI acceso de lectura a toda esta carpeta. Leer primero AGENTS.md, MAPA.md y ESTADO.md.

Comandos:

```sh
cd /Users/MancoMenStudio/Cerebro
python3 bin/cerebro status
python3 bin/buscar "síntoma o tema concreto"
python3 bin/buscar RCS-28671
python3 bin/cerebro read inbox/2026-09-28-cerebro-guia-uso.md --start 1 --count 100
```

La búsqueda reúne registros de brain/sessions.db y notas de inbox, bitácora, memorias, investigaciones, flujos y triage. Las fichas y el espejo están disponibles para lectura. La base sola no contiene todo el conocimiento reciente. Adjuntos binarios, PDF, Excel e imágenes requieren lectura específica. Jira en vivo determina estado actual.

brain/sessions.db es de solo lectura. No ejecutar bin/guardar, bin/ingerir_inbox.py ni cerrar. Guardar nuevos entregables en inbox. El índice .cerebro/retrieval.sqlite es derivado y reconstruible.

Para otra máquina se necesita acceso autorizado o copia de la carpeta completa y preparar su entorno; las rutas y dependencias locales no se transfieren automáticamente.

Fuentes: ESTADO.md e inbox/2026-09-28-cerebro-guia-uso.md, consultados el 14 de octubre de 2026. Búsqueda MCP sobre acceso y cobertura confirmó estas fuentes.
