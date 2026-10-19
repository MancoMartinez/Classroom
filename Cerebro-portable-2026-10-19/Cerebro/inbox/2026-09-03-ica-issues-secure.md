# ICA — Issues in Secure, verificado en Jira 2026-09-03

Cliente: ICA (163). Hilo de correo "Issues in Secure" entre J.R. Teagle, Chris Rippingale, Viraj
Kansara y Nikita Rathore. Cinco tickets involucrados, estado confirmado en Jira a las 11:36 am hora
Bogotá del 3 de septiembre, no en las fichas del cerebro porque ninguno tiene ficha local todavía.

## Estado real por ticket

| Ticket | Resumen | Estado Jira | Causa raíz | PR | Bloqueo |
|---|---|---|---|---|---|
| RCS-28253 | Bottle refunds Aggregated amount | Work in progress | Confirmada, agrupación de líneas IVA mixto en Secure | 56235 desplegado a prod 29 ago. Cliente reporta que sigue mal el 2 sep. PR 57002 abierto el 2 sep, sin comentario de despliegue | Falta saber si 57002 ya subió a staging o prod |
| RCS-28254 | ICA presentkort Link in secure | Under Customer Review | Confirmada | 55913 desplegado a prod 29 ago | Esperando confirmación del cliente, sin acción pendiente de Appriss |
| RCS-28716 | Manual price override en items pesados | Work in progress | Confirmada, falta guard en la sección Audit del detail panel | Ninguno todavía | Necesita implementación |
| RCS-28717 | Discount does not show correctly | Work in progress | Confirmada, promotionid duplicado. Fix vive en branch nrathore/bugfix/RCS-28253-ica-transaction-discount-vat-aggregation | Ninguno posteado en Jira todavía | Necesita terminar el fix y abrir PR |
| RCS-28719 | Audit results missing | Work in progress | Desconocida, la hipótesis del PR 56235 quedó descartada por Nikita | Ninguno | Necesita que el cliente entregue una transacción concreta con la fila faltante |

## Lo que falta resolver antes de contestar

Dos huecos de información, ninguno se resuelve leyendo Jira, hay que hablar con Viraj o Nikita
antes de escribir las respuestas.

Primero, el estado real de PR 57002 en RCS-28253. Jira solo tiene el link, sin comentario de
subida a staging ni a prod. Sin ese dato no se le puede contestar a Chris con precisión sobre si
falta algo por subir.

Segundo, la cobertura de RCS-28716 y RCS-28717 mientras Nikita está fuera mañana 4 de septiembre.
JR ya le pidió a Viraj coordinar contigo la reasignación si hace falta. Las dos causas raíz ya están
identificadas, lo que falta es implementar y abrir PR. Define con Viraj si alguien más las toma
mañana o si esperan el regreso de Nikita.

## Paso a paso

1. Escríbele a Viraj o Nikita por Teams, no por el hilo de correo, y pregunta directamente el
   estado de PR 57002 y si hay coverage definido para 28716 y 28717 mañana.
2. Antes de mandar cualquier respuesta, vuelve a mirar los cinco tickets en Jira. Verificar dos
   veces cuesta un minuto, contestar con un estado viejo cuesta la confianza del account team.
3. Redacta la respuesta a Chris. Va en inglés, directo, sin adjetivos de relleno. Confirma que
   55913 y 56235 ya están en producción desde el 29 de agosto. Señala que 28253 regresó el 2 de
   septiembre y que 57002 es la corrección en curso. Cierra con el dato del paso 1, no con una
   promesa vaga.
4. Redacta la respuesta a JR. Va en inglés, un párrafo corto por ticket, mismo criterio que usa
   Cerebro para respuestas a cliente. Pon primero causa raíz confirmada o no, después la acción
   siguiente, nunca una fecha que no tengas confirmada por alguien más que tú.
5. Antes de enviar, pásale las dos respuestas por el filtro de estilo del contrato de Cerebro.
   Cero conector adversativo, cero paréntesis explicativo, nada de voz pasiva.

## Dato nuevo verificado en el dev panel de Jira, no estaba en los comentarios

PR 56235 (RCS-28253, bottle refund) está MERGED, tres reviewers aprobaron, deploy a prod
confirmado el 29 de agosto. PR 57002 está en estado DRAFT, actualizado hoy 3 de septiembre, sin
reviewers asignados todavía. Jira solo lo liga a RCS-28253, pero el título es "Aggregate ICA
transaction-discount lines sharing the same scanned code", la misma causa raíz que Nikita describió
para RCS-28717. Es la misma corrección para las dos causas, aunque el link formal en Jira solo
existe para 28253.

## Carga del equipo Colombia, verificada en Jira 3 sep, para decidir cobertura

Diego Buelvas, 7 tickets abiertos, cero en Work in progress, 1 High. El más liviano de los tres.
Edwin Garzon, 16 abiertos, 5 en Work in progress, 2 High.
Sebastian Rueda, 15 abiertos, 6 en Work in progress, 1 escalado.

Diego queda como el que vigila PR 57002 y los tres tickets con fix pendiente, RCS-28716, RCS-28717
y RCS-28719, mientras Nikita está fuera.

## Borrador único, listo para pegar como respuesta a toda la cadena

Subject: Re: Issues in Secure

Hi all,

Quick status on the four ICA tickets.

PRs 55913 and 56235, RCS-28254 and the original RCS-28253 fix, are merged and in production since
August 29. The regression ICA reported on September 2 is being addressed in a new PR, 57002, which
also covers the RCS-28717 discount issue. That PR is still in draft with no reviewers assigned, so
it hasn't reached staging or prod. I'm waiting on confirmation from Viraj and Nikita on whether
57002 is the full fix or if anything else is still needed, and I'll update as soon as I hear back.

RCS-28716's root cause is confirmed, a missing guard in the Audit section banner. No PR opened yet.

RCS-28719 still has no root cause identified. We need an actual example transaction from ICA to
keep investigating, I'll request that directly.

Nikita is out tomorrow. I've asked Diego Buelvas to track PR 57002 and keep an eye on RCS-28716,
RCS-28717, and RCS-28719 until she's back.

Juan

## Mensaje corto a Diego, Teams

Diego, Nikita está fuera mañana. Puedes estar pendiente del PR 57002 y de RCS-28716, RCS-28717 y
RCS-28719 mientras ella no está? Avísame si el PR avanza o si ICA manda la transacción que falta
para revisar el 28719.

## Nota de proceso

Ninguno de estos cinco tickets tiene ficha en `tickets/`. Correr
`python3 bin/indexar_tickets.py` después de que Juan actualice los comentarios en Jira, para que
la próxima sesión encuentre la ficha sin tener que repetir esta consulta.
