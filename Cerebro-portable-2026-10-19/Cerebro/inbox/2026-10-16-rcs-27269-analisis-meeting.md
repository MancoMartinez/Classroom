Qué pasa
Jira en vivo: Closed, Peyman Motlagh. Construyó derivación del nivel desde teams y replicación SSO+.
Causa
Recorrido histórico incompleto de tabla, mapeo y replicación, documentado también en resolución de RCS-26519. No prueba una causa común para todos los fallos posteriores.
Evidencia
Descripción del RCS y comentarios de Ryan del 23 jun, Shelley del 21 jul y cierre del 27 jul. https://trebuco.atlassian.net/browse/RCS-27269
Los MSG adjuntos incluyen correo del 23 jun: ubicaciones, grupos, equipos y roles automáticos; advertencia de excepciones persistentes. Shelley registró que TBI decidió conservar excepciones porque algunos usuarios no llegan por SailPoint.
Qué hago hoy
Llevar la expectativa de automatización como contexto de negocio y pedir responsable de la ruta actual SnowTime. No recomendar retirar excepciones masivamente.
Precedentes
RCS-26519 y RCS-27325; historia por bin/buscar. Análisis y correos extraídos en investigaciones/2026-10-16-tailored-incident-id-analisis.md y carpeta 2026-10-16-tailored-msg.
Compromisos
Appriss comunicó automatización y monitoreo. No se encontró autorización actual de eliminar excepciones. Esta sesión no ejecutó ninguna escritura externa.
