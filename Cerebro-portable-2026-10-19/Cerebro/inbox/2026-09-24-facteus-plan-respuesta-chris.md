# Facteus, paso a paso desde hoy para responder a Chris

Fecha 2026-09-24. Plazo real, mañana 25 de septiembre.

## Por qué cambió el plazo

Camila mandó tres mensajes distintos, cada uno más corto que el anterior. El primero pedía revisar la documentación y dar feedback para el fin de la próxima semana. El segundo lo adelantó al fin de esta semana. El tercero dice que ya habló con cada uno individualmente y pide responder el hilo de correo con Chris mañana, con comentarios y feedback.

Ese mismo día, dentro de ENG-6450, Chris escribió que ya chasó a JR por el acceso pendiente. La fecha límite de mañana no es arbitraria, coincide con la escalación de Chris. Detalle completo de ese ticket en inbox/2026-09-24-facteus-complemento-viraj.md.

## Qué ya está resuelto y no hay que volver a investigar

El análisis del 22 de septiembre cubrió los ocho puntos del correo uno por uno, con veredicto y cita, en inbox/2026-09-22-facteus-documentacion-review.md. Los puntos 1, 4, 5, 7 y 8 del correo original ya aparecen marcados como listos por el propio Chris en su comentario del 15 de septiembre dentro de ENG-6450. Los puntos 2 y 3 quedaron con ajustes menores, umbral numérico sin definir en Missing Clients y árbol de decisión sin ninguna salida propia para Support. Ninguno de los dos bloquea una respuesta mañana, se pueden mencionar como sugerencia.

El punto que sí bloquea es el 6, accesos de Support antes del handover. Ese es el mismo punto que Chris tiene sin marcar y el mismo que escaló hoy con JR.

## Pasos de hoy, 24 de septiembre

Habla con Viraj hoy si alcanzas, o a primera hora mañana antes de escribir la respuesta. La guía completa con las preguntas concretas está en inbox/2026-09-24-facteus-complemento-viraj.md.

Pide a Viraj que confirme si tiene acceso al portal de IT Help Desk para revisar ITHD-9247, el ticket que Chris dice haber abierto el 16 de septiembre. Esta cuenta no pudo abrirlo.

Con lo que Viraj confirme, decide con él quién de los dos toma RETAILDB-2972 como propio esta semana, según la responsabilidad conjunta que Camila les asignó en junio.

## Pasos de mañana, 25 de septiembre

Confirma con Viraj el resultado de la conversación de hoy antes de escribir una sola palabra en el hilo de Chris.

Usa el borrador de abajo como base, ajusta el estado real de los accesos según lo que confirmen con Viraj, y pégalo tú mismo. Nadie más que tú escribe en el hilo, esto es solo el texto.

Copia a Camila si el hilo lo permite, para que vea que la respuesta salió a tiempo.

## Borrador para el hilo con Chris

Nota de tono: redactado como pregunta abierta, no como corrección, por si alguna pieza ya cambió de estado del lado de ellos sin que se haya visto reflejado en Jira.

```
Hi Chris,

Thanks for putting this together, the documents are clear and the team found them genuinely useful to
work from. A few notes from our side.

The triage steps, the missing data ticket detail, the decision tree, the internal/external
definitions, and the Facteus contacts all look ready to use as they are.

Two small things that might be worth a look, in case we're missing context on your side.

The Missing Clients page mentions a 26 hour staleness window. Would it help to spell out the exact
threshold that triggers the alert, so Support can tell at a glance if a ticket already carries
enough evidence or needs to escalate right away?

The decision tree routes every ticket, internal or external, to Data Engineering. Is there any
category of Facteus alert where Support is expected to resolve and close on its own, or is the
expectation that Support always hands off after triage? Either answer works, we just want to
document it correctly.

On the access side, RETAILDB-2972 still shows Open with no assignee on our end. We're checking
today whether ITHD-9247 is the same request or a separate one, and we'll follow up directly so this
doesn't sit blocked on our side any longer.

Happy to jump on a call if that's faster than going back and forth here.

Thanks,
Juan
```

## Si el acceso sigue sin resolverse cuando llegue la hora de responder

Envía la respuesta igual, con el resto del feedback, y deja el punto de acceso como lo último que falta por confirmar. No tiene sentido retener todo el feedback bueno por una sola pieza bloqueada que además Chris ya sabe que está bloqueada, la escaló él mismo hoy con JR.
