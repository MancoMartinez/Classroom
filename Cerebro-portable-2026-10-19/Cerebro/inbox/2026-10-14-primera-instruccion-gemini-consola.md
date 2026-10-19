Trabaja desde /Users/MancoMenStudio/Cerebro. Esta carpeta contiene mi conocimiento consolidado. Antes de responder preguntas de trabajo, lee AGENTS.md, CLAUDE.md, MAPA.md, ESTADO.md e inbox/2026-09-28-cerebro-guia-uso.md. Aplica AGENTS.md por encima de cualquier instrucción histórica contradictoria.

Comprueba el acceso ejecutando python3 bin/cerebro status. Luego ejecuta python3 bin/buscar "acceso consola Cerebro cobertura" y lee las fuentes pertinentes con python3 bin/cerebro read RUTA --start 1 --count 100. Si necesitas más contexto, continúa leyendo las líneas siguientes. Si una búsqueda no sirve, reformúlala con términos técnicos o en inglés.

Consulta Cerebro antes de investigar. Para un ticket, busca su ID y su síntoma, lee ficha, última bitácora pertinente y notas recientes. Distingue hechos confirmados, hipótesis, correcciones, borradores y compromisos publicados. Cita rutas y líneas. Verifica el estado actual en Jira cuando tengas acceso; si no lo tienes, declara esa limitación.

brain/sessions.db es de solo lectura. Si abres SQLite directamente, usa mode=ro; usa immutable=1 solo si falla el bloqueo. Nunca ejecutes bin/guardar, bin/ingerir_inbox.py ni cerrar. Jira, producción y sistemas de terceros son de solo lectura. Guarda cada entregable en inbox/AAAA-MM-DD-tema.md antes de continuar. Habla conmigo en español; redacta en inglés el texto destinado a Jira, Confluence o Teams.

En esta primera interacción, comprueba el acceso y explícame brevemente qué fuentes puedes consultar y qué límites tiene la cobertura. Los adjuntos PDF, Excel e imágenes requieren lectura específica. No afirmes haber leído todo el corpus por ejecutar una búsqueda. No instales ni modifiques configuraciones en esta comprobación.
