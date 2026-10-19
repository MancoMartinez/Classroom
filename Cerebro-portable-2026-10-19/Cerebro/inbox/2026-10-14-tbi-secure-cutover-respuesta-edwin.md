TBI 209. Respuesta a Edwin. Revisión 14 octubre 2026.

Qué pasa
Edwin pide fecha de cambio de fuente de Secure a SnowTime.

Causa y límite
ENG-7326 figura Live. El estado no acredita fecha, hora ni ejecución del cambio de fuente de Secure. Cerebro documenta SnowflakeTargetArdmDatabase y SetTargetArdmDatabase como mecanismo.

Evidencia
Jira ENG-7326, leído hoy. 24/24 comentarios consultados. Último comentario: Anushka, 7 octubre, 16:21 EDT, ajustes de tablas y producción pendiente de reconstrucción en esa nota.
Jira ENG-9899: Development Complete; corresponde a Engage, no acredita cambio de Secure.
Cerebro db:knowledge_chunks/551, líneas 28 a 39. inbox/2026-10-07-snowtime-migration-lista-despliegue-8oct.md: TBI en lista para confirmación por EOD; planificación, no prueba de ejecución.

Qué hago hoy
Pedir a Rae o DataOps fecha efectiva, zona horaria y enlace al run para TBI 209 en producción. Verificar destino efectivo y validación de Secure.

Precedentes
brain/markdown/14-appriss-ingeniería-docs-fuente.md, Snowflake, Database and schemas. No hallé confirmación exacta del flip de Secure en las fuentes consultadas.

Compromisos
Borrador no enviado. Ninguna fecha prometida.

Respuesta pegable
Hola Edwin, encontré que TBI 209 ya figura como Live en ENG-7326. La nota de migración del 7 de octubre lo incluía en la ola del 8 de octubre, pendiente de confirmación. Ninguna de esas fuentes confirma cuándo Secure cambió su fuente de datos.

Falta que Rae o DataOps confirmen si ya ejecutaron el cambio en producción, la fecha y hora con su zona horaria y el enlace al run, antes de darle al cliente una fecha de cutover de Secure.

Fuentes
https://trebuco.atlassian.net/browse/ENG-7326
https://trebuco.atlassian.net/browse/ENG-9899

