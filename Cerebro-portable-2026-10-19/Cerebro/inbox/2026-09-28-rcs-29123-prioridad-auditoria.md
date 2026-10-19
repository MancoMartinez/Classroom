RCS-29123. Revisión integral, 28 septiembre 2026. Corte Jira 17:35 Bogotá.

Qué pasa
ADUSA Smart Alerts volvió a enviar; Jim confirmó recepción el 28 sep alrededor de 14:30 EDT. Estado: Under Customer Review. Orden: Recuperado; vigilar confirmación.

Causa
Deadlock de ProcessSmartAlert por paralelismo; fix para esperar ejecución previa, PR 58273, desplegado a US el 28 sep.

Evidencia
https://trebuco.atlassian.net/browse/RCS-29123?focusedCommentId=3370890
Snapshot local: cola/jira-2026-09-28-auditoria.json. Fechas de comentarios, no updated.

Qué hago hoy
Comprobar continuidad y cerrar según proceso. No priorizarlo como interrupción activa si no llega evidencia nueva.

Precedentes
Nota interna 3370892, validación staging 27 sep y producción 28 sep. RCS-29145 ya Completed, fuera de los 19.

Compromisos
Se comunicó recuperación hoy. Por petición de Jim, las alertas omitidas no se reenvían.
