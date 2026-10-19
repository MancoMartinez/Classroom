# RCS-28294 · Por qué Shandana lo devolvió, y qué falta para re-escalar

27 ago 2026. Verificado contra el changelog de Jira y contra el checklist de Aimee.
Corrige lo que escribí hace una hora. Dije que no habías hecho la transición. La hiciste.

## La secuencia real, del changelog

| Cuándo | Quién | Qué |
|---|---|---|
| 25 ago 12:25 | J.R. Teagle | Quita el link `relates to ENG-6612` |
| 25 ago 13:11 | Juan | Reasigna de David Vargas a Luis Hernandez |
| 25 ago 19:53 | Juan | Pega el comentario interno de escalación |
| 25 ago 19:54 | Juan | Se quita el assignee |
| 25 ago 20:02 | Juan | Pega la respuesta al cliente. **Work in progress a Under Engineering Review, assignee Shandana Khan** |
| 26 ago 08:02 | **Shandana Khan** | **Under Engineering Review a Under Support Review, reasigna a Juan.** Comenta *"please can you provide exact steps to recreate?"* |
| 26 ago 14:06 | Juan | Pega los pasos de reproducción |
| Desde entonces | | Nada. Shandana lleva 29 horas sin volver |

Escalaste bien. Ella lo rebotó en 12 horas. La transición y la pregunta ocurrieron en el mismo minuto,
así que devolver el ticket fue la manera de pedir el dato, no una segunda decisión.

Es el mismo patrón que te hizo en RCS-27991 el 27 de agosto a las 03:53. Devuelve y pregunta en un
solo acto.

## Por qué lo devolvió. El comentario del 25 no tenía pasos de reproducción

El checklist de Aimee exige cinco cosas antes de escalar, de
`brain/memoria/reference_escalacion_l3_procedimiento.md`:

| Requisito | Comentario del 25 ago 19:53 |
|---|---|
| Entorno declarado, Test, QA o Prod | Parcial. Dice "read in production 25 August" dentro de encabezados de sección. No hay una línea que declare el entorno |
| **Pasos completos de reproducción con capturas** | **No.** Cero pasos |
| Notas de IA usadas en el troubleshooting | No |
| Conversaciones con otros ingenieros fuera del ticket | No |
| Avisar al cliente que el ticket se mueve | Sí, a las 20:02 |

Uno de cinco.

El comentario del 25 es un informe de investigación, y como informe es sólido: las 19 Smart Alerts
leídas en producción, la tabla de filtros, los 3 Success de `SmartAlertProcess` para el caso 48575,
el cero de HR1 en blanco sobre 405 y 39 casos, las tres hipótesis descartadas, y la distinción entre
`RunStatus = Success` y correo entregado.

Nada de eso es un procedimiento que un ingeniero pueda ejecutar. Shandana no necesitaba tus
conclusiones. Necesitaba poder reproducirlo.

Aimee hace cumplir esto de verdad. El 13 de agosto comentó el mismo texto en cuatro tickets de
Vedant Shirude parados en Under Support Review: *"before this ticket can be moved to Engineering they
need you to add your notes regarding what you did to triage/troubleshoot and explaining what we need
from them"*. El caso extremo fue RCS-28007, que tenía la investigación completa de Tyrone Whitney y
aun así no pasaba.

## Lo que ya está bien, y lo que todavía falta

El comentario del 26 a las 14:06 sí cumple. Preconditions con tenant, módulo, formulario, alerta y
filtro efectivo. Ocho pasos numerados. Consulta de verificación. La tabla que compara 48575 contra
48786 y el punto de arranque, *"Diff the execution path between ShopliftingID 48575 and ShopliftingID
48786"*. Eso es lo que ella pidió.

Siguen faltando tres requisitos del checklist:

1. **Capturas.** Tienes `adjuntos/RCS-28294/2026-ADUP-40-96.pdf` y
   `image-20260812-181001.png`. Ninguna está referenciada en los pasos. Aimee pide "pasos completos
   de reproducción **con capturas**".
2. **Notas de IA declaradas.** En RCS-27991 sí las declaraste. Aquí no.
3. **Constancia de conversaciones fuera del ticket.** Basta una línea diciendo que no hubo, o
   listando las que hubo.

En RCS-27991 hiciste el comentario interno completo con los tres. La bitácora del 26 ago lo registra.
Copia ese patrón aquí.

## El ENG nunca se creó. Verificado

Aimee dice que la transición a Under Engineering Review auto crea el ENG. Barrí el proyecto ENG con
JQL por `smart alert`, `smartalert` y `Vallarta`. **No hay ningún ENG creado el 25 ni el 26 de
agosto para este ticket.** El más nuevo es ENG-7808, del 25, y pertenece a ENG-7192, otro tema.

Hoy RCS-28294 no tiene ningún issuelink. J.R. quitó el de ENG-6612 el 25 a las 12:25, y tú explicaste
por qué en tu comentario: *"ENG-6612 is not related to this ticket. It covers attachment handling in
Cohesion mode, reached Done, and deployed to production on 4 August, one week before this was
reported."*

Consecuencia: lo que le dijiste a Tatiana el 25 a las 20:02, *"This is now with our Engineering team
as a tracked defect"*, fue cierto durante 12 horas. Dejó de serlo el 26 a las 08:02 y sigue sin
serlo. Eso no es negligencia tuya. Es que nadie le dijo al cliente que el ticket volvió.

## Dos ENG que conviene mirar antes de re-escalar

El barrido devolvió dos candidatos que no están enlazados a tu ticket.

**ENG-7359, "Smart Alert not working with Quick Entry"**, Backlog, Matthew Kamminga, creado el 17 de
agosto. Este es el que más pesa. Tu caso sin alerta, el 48786, tiene stage `Pending Summary-HR
Investigation Specialist`, distinto del 48575. Si se creó por una ruta de entrada distinta, encaja
con el título de ese ENG. Y tú mismo le preguntaste a Tatiana el 25 si su equipo entra normal o
llega al formulario por un enlace directo o un acceso guardado. Estás persiguiendo exactamente esa
hipótesis sin saber que ya existe el ticket.

**ENG-2819, "Smart Alert failing to run in Incident/Audit"**, Done, Kiran Vadday, creado el 3 de
abril de 2026. Precedente del mismo síntoma: la alerta no corre. Vale leer su causa raíz antes de
escalar, igual que el 66220 sirvió en RCS-27991.

Y el paraguas que ya conocías: **ENG-6541, "Harden smartalerts functionality"**, Backlog, Kamminga.

## Qué hacer, en orden

1. Lee ENG-7359 y ENG-2819. Si ENG-7359 describe tu caso, el ticket puede colgarse de ahí y te
   ahorras la escalación entera.
2. Completa el comentario interno con los tres requisitos que faltan: capturas referenciadas en los
   pasos, notas de IA declaradas, y constancia de conversaciones externas.
3. Enlaza ENG-6541 y RCS-28131 de Sportman, que ya está en Under Engineering Review con el mismo
   síntoma.
4. Vuelve a transicionar a Under Engineering Review con Shandana, y mándale Teams. Está en
   Europe/Madrid, escríbele temprano.
5. Escríbele a Tatiana. Le dijiste que estaba con ingeniería y hace dos días que no lo está.

## Bloque para el comentario interno que falta

```
Escalation checklist, completing what was missing from the 25 August comment.

Environment. Production. Vallarta tenant, /vallarta/nettrack/. All findings below were read in production on 25 August with read only access.

Reproduction steps. See my comment of 26 August. Preconditions, eight numbered steps, verification query and the two cases to diff.

Screenshots. Case report for 2026-ADUP-40-96 is attached to this ticket, showing Case Stage Pending Report to be Completed, HR Case Status Open, every interview field Pending, and the Investigation, Recommendation and Resolution sections empty. That is the case that generated three Success rows in incident.SmartAlertProcess.

AI assisted troubleshooting. Analysis of the alert configuration, the SmartAlertProcess rows and the HR1 population counts was carried out with AI assistance against read only production queries. Every figure quoted is from a query result, not inferred.

Conversations outside this ticket. None.

Related work items for triage. ENG-7359 Smart Alert not working with Quick Entry may describe this directly, given case 48786 sits at a different stage from 48575. ENG-2819 Smart Alert failing to run in Incident/Audit is a closed precedent for the same symptom. ENG-6541 Harden smartalerts functionality is the umbrella. RCS-28131 for Sportman carries the same symptom and is already in Under Engineering Review.

What we need from Engineering. Diff the execution path between ShopliftingID 48575 and ShopliftingID 48786. Zero rows in SmartAlertProcess for 48786 means the engine was never invoked, which is a different failure from the engine running and the filter evaluating false. Support holds read access to data only, not to code or application logs.
```

## Y el mensaje de Teams para Shandana

```
Hi Shandana, RCS-28294 Vallarta. I posted the exact reproduction steps you asked for on 26 August, plus the escalation checklist items that were missing. Two cases to diff, 48575 generated three SmartAlertProcess rows and 48786 generated none on the same filter. I have moved it back to Under Engineering Review. One thing worth checking first, ENG-7359 Smart Alert not working with Quick Entry may already cover this. Thanks.
```

## Y la corrección a Tatiana

```
Hi Tatiana,

A correction on the status I gave you on the 25th.

I told you this was with our Engineering team. It came back to Support the following morning for further detail, which I have since provided. It is going back to Engineering now.

I need nothing further from you at this point. The two questions I asked on the 25th still help if you have them.

Thank you.
```
