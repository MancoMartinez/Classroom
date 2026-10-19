# ADUSA · verificación en vivo, D4 y correo para Jim · 20 ago 2026

Verifiqué en Jira los ocho tickets que quedaron abiertos ayer. Confirmo lo que sí se hizo, marco lo que falta y corrijo tres columnas de estado que ya no coincidían con Jira por cambios de otros ingenieros de Appriss, ajenos a este ciclo de seguimiento.

## Lo que se ejecutó correctamente

RCS-28342 quedó bien hecho. El comentario sobre la cuenta de Janai está pegado tal cual se redactó ayer y el ticket ya transicionó a Work in progress. El D4 mueve la categoría de Awaiting Ahold input a Active with Appriss, porque el trabajo pendiente es de Appriss, actualizar el mapeo de Janai y después el de Stacie y Melanie.

RCS-28353 quedó bien hecho. El comentario a Leigh Ann sobre el fix en producción está pegado tal cual y el ticket ya transicionó a Under Customer Review. Esto adelanta el plan de ayer, que esperaba la confirmación de ella antes de transicionar. No hay problema en dejarlo así, el fix ya está confirmado en producción. El D4 mueve la categoría a Pending Ahold verification.

## Lo que falta

RCS-28378 tiene el comentario de cierre pegado tal cual, "Thank you for confirming. Closing this out." La transición a Completed nunca se ejecutó. Sigue en Under Customer Review en Jira, y el D4 lo refleja así. Falta hacer la transición Resolve, con Resolution en Resolved y Resolution Details en Engineer Resolved, segundo nivel Bug - Resolved w/ Release. No lo mandes directo a Closed, ese fue el error de RCS-28177.

RCS-28177 sigue con la bandera de la automatización sin atender. El comentario "Needs Attention - Add Resolution" quedó publicado el 19 de agosto a las 12:11pm y ningún comentario posterior lo resuelve. El ticket de cara al cliente está Closed y Jim ya confirmó que funciona, esto no bloquea nada hacia Ahold. Alguien con permiso de transición, Viraj, debe entrar, pasar el ticket a Completed y llenar el segundo nivel de Resolution Details para que la bandera desaparezca.

## Tres correcciones de estado que no vienen de este ciclo

Al revisar RCS-28304, RCS-28124 y RCS-28407 encontré que su estado real en Jira ya no era el que tenía el D3, sin relación con las acciones de ayer o hoy sobre el tracker de Chris. El D4 corrige las tres.

RCS-28304 pasó a Under Engineering Review. El D3 tenía Work in progress. El último comentario, del 19 de agosto a las 16:22, es interno, de Matthew Kamminga, y solo adjunta una captura de la vista previa a la unificación. No hay nada nuevo que comunicar a Leigh Ann.

RCS-28124 pasó a Under Customer Review. El D3 tenía Work in progress. Viraj comentó hoy a las 10:19am, repitiendo la pregunta de si el video ya sube bien y si .txt es un formato que usan los equipos de Ahold. Todavía no hay respuesta.

RCS-28407 pasó a Under Engineering Review. El D3 tenía Work in progress. Sigue en manos de Edwin Garzon, el mismo hueco de información de ayer, sin síntoma nuevo confirmado.

RCS-28123, RCS-28196 y RCS-28281 quedaron exactamente como se recomendó ayer, sin comentario nuevo y sin transición. Verificado.

## D4 generado

Archivo: Appriss ADUSA-Support-Tracker - 08202026 D4.xlsx, construido sobre el D3. Cambios reales, todos verificados en vivo hoy: RCS-28342 a Work in progress, categoría Active with Appriss. RCS-28353 a Under Customer Review, categoría Pending Ahold verification. RCS-28304, RCS-28124 y RCS-28407 con el estado corregido para que coincida con Jira real, sin cambio de categoría.

Tabla resumen recalculada. Total sigue en 35 tickets. Resolved 21, Pending Ahold verification 4, Awaiting Ahold input 0, Active with Appriss 10.

Ningún ticket quedó sin dueño ni sin respuesta por más de 24 horas. El más próximo a vencer ese plazo es RCS-28124, con la pregunta de Viraj de esta mañana a las 10:19am sin respuesta todavía.

## Correo para Jim

Revisé memoria contra el formato que usó J.R. el primer día y contra el D2 y el D3. Su correo mezcla dos cosas, un cierre de lo que ya se resolvió con el tracker adjunto, y una lista de preguntas reales, cada una con el contexto puntual y la pregunta directa al final del párrafo, dirigidas a Jim aunque el tema sea de Leigh Ann o de otro contacto. RCS-28378 y RCS-28342 no entran en esa lista porque Jim ya conoce el estado de los dos y no hay pregunta pendiente de su lado. Repasé los 35 tickets buscando otras preguntas reales todavía sin respuesta, no solo las tres del correo original de Jim, y encontré dos más aparte de RCS-28196: RCS-28124, con la pregunta que Viraj repitió esta mañana sobre la subida de video y el formato .txt, y RCS-28353, con la pregunta que se le hizo hoy a Leigh Ann sobre la reprueba del error 502 en el perfil de tienda. Las tres siguen sin respuesta.

```
Hi Jim,

Thanks for the call this morning and for confirming those three items by phone yesterday. I've updated the tracker with everything from both and it's attached.

Additional pages, RCS-28196. You mentioned you'd scan the other incident entry pages today for the same null default Leigh Ann found. We're still waiting on that whenever your team gets to it.

Attachments, RCS-28124. The Forbidden error came back once after the fix went in, so we followed up again this morning asking for a retest and whether .txt is a format your teams actually use. Still waiting on that test result from your side.

Store profile 502, RCS-28353. The fix reached production and we asked Leigh Ann today to retry the update that was failing. We're waiting on her confirmation as well.

Thanks,
```
