Facteus, estado después de las respuestas de Chris del 7 de octubre

Fecha 2026-10-07. Viraj mandó sus propias preguntas directo por chat a Chris y Sadam, distintas en redacción a las seis que armamos, pero se cruzan. Esto es lo que quedó resuelto y lo que sigue abierto.

Lo que se resolvió

Canal y escalación. Chris confirmó que usan el canal Data Issues, el mismo de todos los demás problemas de datos en Appriss. La vía es OpsGenie primero, levantando la alerta a Data Engineering Escalation, que es un escalation schedule. Si eso falla, los nombres de respaldo son Chris Howard, Nicholas Turner y Saddam Hussain como manager.

Alertas urgentes reportadas por el cliente. Chris confirmó que todo External Alert, cualquier correo directo de Facteus, se asigna a Data Engineering, sin distinguir si el cliente lo marcó urgente o no. Eso contesta la pregunta de escalar a L2 o no, no hay paso intermedio, va directo.

Cobertura de fin de semana. No hay un nombre fijo, está resuelto por el mismo escalation schedule de OpsGenie, Chris dice que ya está configurado y confirmado que funciona.

Go-live. Para External Alerts, el correo directo de Facteus al support desk, Chris dice que arranca en cuanto Support apruebe asumirlo, es decir que el bloqueo ahora es nuestro, no de ellos. Para Internal Alerts siguen esperando aprobaciones finales de Facteus, estimado para el 14 de octubre, y dice que avisan a Support apenas pase.

Product Type en Jira. Chris confirmó que hay que levantar un ticket de helpdesk para crear el Product Type de Facteus, todavía no existe. El campo de tipo de problema sí se puede reusar de los que ya existen en el portal RTS, ese no necesita ticket nuevo.

Chris se ofreció a documentar todas estas respuestas en una página de FAQ en el Wiki y actualizar la documentación central donde aplique.

Lo que sigue sin resolver

Si un cliente deja de enviar su propia data por un problema de su lado, ¿la alerta de Facteus se dispara igual? Viraj sí preguntó esto, Chris no lo contestó todavía.

Si se dispara, al notificar, ¿se dice qué cliente es o se mantiene genérico? Esto no se preguntó, es la segunda mitad de la pregunta que trajo L1 en la llamada.

El umbral exacto de drop_ratio y cuántas horas de staleness disparan la alerta de Missing Clients. Este sigue pendiente desde el 22 de septiembre, nunca se volvió a preguntar.

El artículo por tipo de alerta que pidió Shreyas, cómo confirmar que es real, qué herramienta revisar, si L1 puede resolverlo, a quién escalar, con qué frecuencia de seguimiento. No se preguntó todavía, y es justo el tipo de contenido que calza con la página de FAQ que Chris ofreció armar.

Dos decisiones que son nuestras, no de Chris

Si Support ya está listo para decir que sí a que Facteus empiece a escribir directo al support desk, eso depende de ustedes, no hay nada más que esperar del lado de ellos para External.

Quién levanta el ticket de helpdesk para el Product Type de Facteus, si lo hace Camila como se había hablado antes o lo hace Support directamente ahora que ya se sabe que hace falta.

Qué sigue

Vale la pena aceptar la oferta de Chris de la página de FAQ y mandarle ahí las cuatro preguntas que siguen abiertas, en vez de otro correo suelto. Si quieres, te armo esa respuesta.
