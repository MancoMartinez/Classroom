# RCS-29417: hallazgos reportados por Edwin

Fuente: Juan pegó la nota literal de Edwin el 15 octubre 2026. Resultados de producción reportados por Edwin; el agente no repitió las consultas.

Qué pasa
Edwin comparó RAW_DATA y headers tipo 5 en ARDM_PRODUCTION.C166_SBX por día del 12 al 31 agosto. Reporta cobertura completa del 19 al 25 y hueco desde el 26 agosto, cubierto por el rebuild de hoy hacia 13:29 UTC. Reporta duplicación de los headers reconstruidos y ausencia de sus filas en ARDM_JSON. La tarea horaria de hoy genera filas únicas.

Causa
Edwin atribuye el faltante al flat/mapping cubierto por PR 58962. Esto refuerza la relación con el alcance Paid-In/Paid-Out investigado en RCS-29205; no demuestra identidad con el defecto de tokens de refunds. Causa del duplicado y ejecutor del rebuild desconocidos. Tienda 910647 sin eventos RAW_DATA según Edwin, pendiente de aclarar con cliente.

Evidencia
9375: 26/08 16:53, reg 01, check 0001, out $2.80; 27/08 14:30, out $104.76; 30/08 07:41.
10111: 04/09 12:23, reg 01, check 0001, out $64.43; 12:25, reg 03, check 0001, $73.40.
Semana 7 a 13 septiembre: 23.144 headers, 11.572 TRANSACTIONID y 11.573 eventos raw. Pares idénticos, creación separada 2,6 s. No inferir qué explica la diferencia de un evento raw. Fuente: nota literal de Edwin transmitida por Juan.

Qué hago hoy
Contrastar tipo 5 reportado con tipos 50/51 de la documentación previa. Antes de avanzar con tender, proponer a Anushka y al operador revisar duplicados, cobertura de ARDM_JSON y validación de la recarga. No ejecutar escrituras ni deduplicación.

Precedentes
RCS-29205, comentario interno 3384023 del 7 octubre y 3386643 del 9 octubre. inbox/2026-10-14-rcs-29205-verificacion-resultado.md registraba recarga pendiente; ese pendiente ya no describe la ejecución reportada hoy. No prueba seed o rebuild de tender completados.

Compromisos
Sin compromiso nuevo ni cierre verificado. La nota no identifica ejecutor ni prueba causa de duplicación.

Borrador invalidado
inbox/2026-10-15-rcs-29417-mensaje-edwin.md queda obsoleto: Edwin ya aportó ejemplos y aclaró el inicio del hueco. Ningún mensaje nuevo redactado.
