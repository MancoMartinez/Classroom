# Backlog 82: orden por facilidad, 25 septiembre 2026

Cola verificada directamente en Chrome: Support Backlog Unassigned, tres tickets, todos Under Support Review, sin asignar y Medium. Fuente: https://trebuco.atlassian.net/jira/servicedesk/projects/RCS/queues/custom/82

Recomendación: empezar por RCS-29129 y continuar con RCS-29127 aprovechando el mismo reporte base. RCS-29128 queda tercero por incertidumbre técnica. Facilidad no equivale a prioridad operativa: Albertsons reporta una división completa sin datos de pago.

1. RCS-29129, PacSun MERCH CARD Refund Ranking. Dificultad estimada baja, confianza media. Existe el reporte CASH y el cliente adjunta ubicación, parámetros y columnas. Falta verificar en Composer cómo calcula monto, conteo y ranking y cuáles códigos representan devolución a merchandise card. Talos propone cambiar un filtro, sin evidencia independiente de la definición. No mezclar issue, reload y redeem automáticamente.
2. RCS-29127, PacSun Credit Card Refund Ranking. Dificultad estimada baja a media, confianza media. Misma base. Resolver alcance de crédito frente a débito y revisar los campos monetarios y de conteo. Reutilizar la validación del anterior.
3. RCS-29128, Albertsons Jewel división 32, pagos del 24 sep. Dificultad indeterminada. Robin descartó su hipótesis de operaciones de 23:59 en comentario del 25 sep 16:22:55 -0400. Revisar headers y tenders por tienda y día, archivos recibidos y carga antes de proponer recuperación.

Ambos PDF de PacSun muestran Quick Links > 8 - LP Investigative Reports > CASH REFUNDS w Ranking Dollars Count. Mantener Sale Date, Region Number y Store No, agrupación por región, distrito, tienda y cajero, monto, conteo y ranking. Copiar la versión actual que PacSun modificó, no una plantilla antigua. La captura CASH define estructura, no totales esperados de MERCH/CREDIT.

Historial: RCS-26883 documenta reportes y referencias personalizados por Nicole Myers y Vlad, confirmación de funcionamiento y cambio permanente el 22 jun. RCS-29039: Roseanne confirmó el 23 sep que reaparecieron sus reportes; estado actual UCR, pese al anuncio de cierre. RCS-24233: cambios de tender exigieron mapeo y PR, por lo que no asumir equivalencia por etiqueta. RCS-29104, bitácora local, enseña a distinguir archivo recibido de fila cargada; no demuestra causa común con Jewel.

Método: bin/buscar, fichas e índices locales, Rovo Search, JQL dirigido, descripciones y comentarios en Jira y revisión visual completa de los dos PDF. No se inspeccionó Composer ni datos productivos. No existe causa técnica confirmada para los tres tickets. No se ejecutaron cambios ni se enviaron mensajes. Las búsquedas semánticas avisaron cobertura parcial; la cola se verificó directamente.

Fichas de acción: 2026-09-25-rcs-29129-evaluacion.md, 2026-09-25-rcs-29127-evaluacion.md y 2026-09-25-rcs-29128-evaluacion.md en inbox. Juan puede ingerir las notas desde su terminal con cerrar.
