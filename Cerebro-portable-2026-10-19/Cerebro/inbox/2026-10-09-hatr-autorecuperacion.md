# HATR NotificationEmail: no hay autorecuperacion documentada ni observada

Pregunta de Juan, 9 oct 2026: los jobs HATR se recuperan solos.

Documentado, brain/markdown/14-appriss-ingeniería-docs-fuente.md chunk 461:
1. Checkpoint de Durable Functions: si un worker muere, otro retoma desde el ultimo await.
2. Lock por cliente TaskClientLock {ClientID}x{TaskName}. El documento no menciona expiracion ni TTL del lock.
3. Reintento de actividades: 3 reintentos, base 10 s, backoff 2x. Cubre fallas transitorias de una actividad, no una orquestacion detenida.

Observado:
1. RCS-29021 Claire's 439: waitingOnLock true desde 2026-09-10T14:50:14Z hasta el reinicio manual de Vlad el 9/22. Doce dias sin recuperarse.
2. RCS-29350 Wild Fork 354: cero intentos de envio de 10/8 17:50 UTC a 10/9 15:59 UTC. Volvio con el Run Now de Diego. Sleeping Until vencido.
3. Ninguno de los dos lo detecto un monitor. Claire's lo reporto el CSM, Wild Fork el cliente.
4. El Control Panel tiene herramientas manuales: Cleaning Scheduled Tasks Locks, Hatr Lock Diagnostics, Run Now.

Conclusion: HIPOTESIS con evidencia. Un job detenido no vuelve solo. Falta confirmar con Eng si existe TTL del lock.
Pendiente: inicio real de la caida de Wild Fork.
SELECT MIN(DateCreated) FROM notify.NotificationUser WHERE ID BETWEEN 274 AND 329;
Supone que la instancia programada envio las filas 274 a 329.
