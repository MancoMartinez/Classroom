# ADUSA. El plan de tickets de ingeniería que buscabas, reconstruido y verificado contra Jira en vivo

Fecha: 3 de septiembre de 2026. Fuentes cruzadas: los tres transcripts de hoy, `Appriss ADUSA-Support-Tracker (7).xlsx` que subiste, el cerebro completo, y Jira consultado en vivo ticket por ticket, incluidos comentarios y changelog. Confluence revisado, sin documento adicional que aporte al plan.

## El chat que no encontrabas

No es un chat aparte. Es el cerebro del 1 de septiembre. Dos documentos:

- `inbox/2026-09-01-adusa-dos-reuniones-y-el-encargo-de-jr.md`
- `inbox/2026-09-01-adusa-plan-escalacion-filas-61-69.md`

Ahí quedó el criterio completo de J.R. Teagle para escalar a ingeniería. Defecto confirmado más pasos de reproducción escritos en el ticket, las dos cosas juntas, o no se crea ENG. Verbatim suyo, dentro de RCS-28683: *"once you're able to get steps to reproduce in here, let's please get an ENG ticket created for this and linked."* La reunión de hoy es la continuación exacta de esa lista. Los ocho tickets que tratan J.R., Matt, Jim y Leigh Ann en el audio de hoy son los mismos nueve que se repartieron el 1 de septiembre, menos RCS-28281 que es de Secure.

## Estado de cada ticket, confirmado en Jira ahora mismo

| Ticket | Tema | Status en Jira, live | Assignee | ENG vinculado | Qué falta hoy |
|---|---|---|---|---|---|
| RCS-28535 | Adjuntos, sospecha Cloudflare | Work in progress | Edwin Garzon | ENG-7181, In Development | Nada nuevo escrito en Jira sobre Cloudflare. El único comentario de hoy es un mensaje enlatado de Edwin a Jim, "haven't heard back from you yet". La pista de Cloudflare que Matt dio en el audio de hoy no está en el ticket |
| RCS-28482 | Izenda, pestaña MISC en gris | Work in progress | Juan Martinez | Ninguno | Juan se comprometió en la reunión a crear el ENG hoy. A la hora de esta verificación no existe. Último movimiento en Jira sigue siendo el 26 de agosto |
| RCS-28667 | Nuevos usuarios sin jerarquía | Under Engineering Review | Matthew Kamminga | Ninguno | Megha pidió revisión de ingeniería el 2 de septiembre y escribió su sospecha de causa raíz, la unificación Delhaize deja al usuario sin jerarquía por defecto. Nadie ha clonado el ENG todavía |
| RCS-28123 | Asignación de casos | Work in progress | Juan Martinez | ENG-7192, Done, no cubre el síntoma abierto | Juan ya corrigió al cliente esta madrugada, la ausencia de popup de confirmación no es defecto, viene de una ruta de código comentada a propósito hace 3.5 años. Hoy a las 8:38 am Leigh Ann reportó un síntoma nuevo y distinto, el correo de notificación al reasignar dejó de llegar desde el lunes. J.R. pidió partirlo en un ticket aparte y Juan aceptó. Ese ticket todavía no existe |
| RCS-28693 | Login SSO, Harrison Xu y Paula Dotson | Under Customer Review | Vlad Bogus | Ninguno | Esperando que Leigh Ann confirme con Harrison si el problema sigue. Matthew Kamminga entró hoy a las 10:31 con Ryan a mapear tiendas de Delhaize como solución provisional. La decisión de ruta para el caso Paula Dotson, revisión de ingeniería o revisión de seguridad, sigue sin registrarse en Jira |
| RCS-28683 | 404 al agregar asociado | Work in progress | Megha Rathi | Ninguno | Sigue faltando lo que J.R. exigió por escrito el 1 de septiembre, pasos de reproducción completos. Sin eso no se crea el ENG |
| RCS-28596 | Empleados duplicados | Accepted into Development | Shandana Khan | ENG-7904, Development Complete | Desarrollo terminado, en QA. Acuerdo de hoy en la llamada, no liberar en viernes, apuntar a martes por el fin de semana largo |
| RCS-28589 | Apóstrofes en el archivo de tiendas | Under Engineering Review | Matthew Kamminga | Ninguno | Ryan Barlow ya dejó escrito el 1 de septiembre que el defecto está en la función de exportación, no en la base. Shandana lo asignó a Matthew como SRE inicial. Nadie ha clonado el ENG. J.R. lo señaló hoy mismo en la llamada |

## Lo que la reunión de hoy confirma y lo que todavía no está en Jira

Los ocho tickets discutidos hoy están en uno de tres estados reales, verificados contra Jira y no contra lo que se dijo en la llamada.

Dos ya tienen ingeniería trabajando con ticket propio. RCS-28535 con ENG-7181 en desarrollo, y RCS-28596 con ENG-7904 en QA con objetivo de esta semana.

Uno quedó resuelto como cambio de producto y no como defecto. RCS-28123 en su síntoma original. El correo de reasignación que dejó de llegar es un hallazgo de hoy, distinto, y necesita ticket propio que aún no existe.

Cinco siguen exactamente donde J.R. los dejó el 1 de septiembre, sin ENG creado: RCS-28482, RCS-28667, RCS-28683, RCS-28693 y RCS-28589. En los tres primeros falta material de reproducción o una respuesta pendiente. En RCS-28589 el material ya está completo desde el 1 de septiembre, verbatim de Ryan Barlow, *"This ticket needs to go to engineering to review the export to file functionality"*, y aun así no hay ENG dos días después. Ninguno de estos cinco se mueve solo. La transición a Under Engineering Review no dispara ninguna automatización, eso ya se verificó contra el changelog el 1 de septiembre y sigue siendo cierto hoy.

## Tres cosas para hacer hoy, en orden

Escribir el comentario que crea o pide el ENG en RCS-28482. Es tu compromiso de esta mañana con J.R. y con Jim.

Abrir el ticket nuevo para el correo de notificación de RCS-28123 y enlazarlo. Se lo prometiste a J.R. en la llamada de hoy.

Perseguir el ENG de RCS-28589. Tiene causa raíz escrita desde el 1 de septiembre y ningún ticket de ingeniería abierto todavía. Es el que peor se ve si Jim vuelve a preguntar.

El tracker interno que subiste, `Appriss ADUSA-Support-Tracker (7).xlsx`, ya trae las notas del 3 de septiembre pegadas fila por fila y coincide con todo lo anterior. Su cabecera sigue diciendo *"Status as of Wednesday, August 19, 2026"*, desactualizada desde hace dos semanas. Corrígela antes de mandar el próximo tracker a Jim.
