# L2 to L3 RCS ticket management: conocimiento contrastado

Consulta: 13 octubre 2026, America/Bogota. Análisis completado con el alcance y límites indicados abajo.

Fuente principal: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/474627801097 . Versión 26, publicada 2026-10-13 13:50:47 UTC, 08:50:47 Bogotá.

Correcciones confirmadas en la fuente: Solutions Experts ahora corresponde a Peter Just. El comentario 478276452363 del 5 octubre propuso Peter Just o Nicole Myers; la respuesta 478295130123 del 13 octubre 07:51:03 UTC pidió Peter Just. El cuerpo actual adopta Peter Just. La guía 478006902856 versión 5 del 27 agosto conserva James DeJohn y necesita reconciliación documental.

Ryan Barlow escribió el comentario 478296801281 el 13 octubre 13:44:55 UTC: no hace falta mensaje adicional de Teams para su cola de Delivery. Explica que vigilan la cola durante la jornada laboral. No extender esta excepción a Engage Engineering ni CSM.

La captura textual completa de la página sigue abajo. La transcripción visual del diagrama aparece después de esta captura.

This section describes the process used by the L2 Support team for issue resolution once ticket has been assigned to them. 

L2 Support will triage ticket and if/when needed will move ticket to appropriate L3 team as shown in the chart below.

Definitions and Responsibility of each team:

***Delivery ***is responsible for implementation and any configuration updates from what was originally implemented. 

*\*Note that this is not change requests or new feature requests; these would be CSM or Customer Feedback Portal*

Items such as:

- Set-up of initial feeds
    - Issues w/ feeds after implementation go to Infrastructure (Incident/Audit)
- Incorrect values
- Updates to value reason
- Changes to views on receipts
- Permissions
- Bulk removing/adding of information
- Links going to incorrect pages

***Engineering ***is responsible for anything code related in applications.

Delivery teams are as follows:

| **Product** | **Under Delivery Review Notification** |
| --- | --- |
| [Secure Incident & Audit (LPMS/CAMS)](https://trebuco.atlassian.net/wiki/spaces/RTS/pages/474627735563/AALPS+team) | @Matthew Kamminga |
| [Engage](https://trebuco.atlassian.net/wiki/spaces/RTS/pages/474627899400/Engage+team) | @Ian Williams@Kenny C Vu |
| Secure Store  - [Legacy Secure team - Retail Tenant Support - Confluence](https://trebuco.atlassian.net/wiki/spaces/RTS/pages/474627866642/Legacy+Secure+team) - [Secure 5 team](https://trebuco.atlassian.net/wiki/spaces/RTS/pages/474627605114/Secure+5+team) | @Carl Costelow |

Please note the following status and/or assignee processes when moving RCS tickets to different L3 departments.

- **Secure/Incident Engineering** – change status to “Under Engineering Review” and assign to @Shandana Khan
- **Engage Engineering** – change status to “Under Engineering Review” and assign to @Ian Williams
- **RTI/RTIaaS - **change status to “Under Engineering Review” and leave unassigned; the Engineers will pick this up from their queue
- **Infrastructure** – change status to “Under Infrastructure Review”; keep assigned to yourself
- **Security (InfoSec)** – change status to “Under Security Review”; keep assigned to yourself
- **Delivery - **
    - **Secure 5 **- change status to “Under Delivery Review”, assign to Peyman Motlagh, add “RCS Support Team” to Sprint field
    - **Incident **– change status to “Under Delivery Review”, assign to @Ryan Barlow
- **Solutions Experts **– change status to “Under Solutions Experts Review” and assign to @Peter Just
- **CSM **– change status to “Under CSM Review” and assign to responsible CSM

## Diagrama: transcripción completa y traducción operativa

Adjunto mostrado por la versión 26: image-20260415-174353.png, att477693706246, versión 1, 29700 bytes. Copia: adjuntos/confluence-474627801097/image-20260415-174353.png. Lectura visual directa el 13 octubre. Las otras 14 imágenes adjuntas no aparecen en el cuerpo vigente; no constituyen reglas actuales por estar almacenadas.

| Intermediate category | Ticket type | Escalation target | Notes |
| --- | --- | --- | --- |
| Possible bug or code-related issue | Incident | Engineering | L2 identifies a likely defect and escalates to Engineering for investigation and fix. |
| Issue with implemented data / config | Incident | Delivery | Problems with data or configuration that was already deployed are routed to the Delivery team for remediation. |
| Changes or updates to data / config or other billable items | Change Request | CSM | Any work involving configuration changes/items that may incur a charge is passed to the Customer Success Manager. |
| New feature request | Feature Request | Customer Feedback Portal | Customer-initiated requests for new functionality are referred to the Customer Feedback Portal. |

Interpretación: clasificar por naturaleza del trabajo. Un defecto probable de código va a Engineering como Incident. La remediación de datos/configuración ya implementados va a Delivery como Incident. Cambios potencialmente facturables van al CSM como Change Request. Funcionalidad nueva va al Customer Feedback Portal como Feature Request. La página no aporta la URL del portal ni criterios para decidir facturabilidad en casos disputados.

Delivery cubre implementación y actualizaciones de configuración original: feeds iniciales, valores incorrectos, value reason, vistas de recibos, permisos, altas/bajas masivas y enlaces que apuntan a páginas equivocadas. Excepción explícita: problemas de feeds posteriores a implementación en Incident/Audit corresponden a Infrastructure. No generalizar esa excepción a todos los productos.

## Matriz operativa vigente en la página principal

| Destino | Estado | Asignación y campos |
| --- | --- | --- |
| Secure/Incident Engineering | Under Engineering Review | Shandana Khan |
| Engage Engineering | Under Engineering Review | Ian Williams |
| RTI/RTIaaS | Under Engineering Review | Sin asignar; Engineering toma desde su cola |
| Infrastructure | Under Infrastructure Review | El analista conserva la asignación |
| Security / InfoSec | Under Security Review | El analista conserva la asignación |
| Delivery Secure 5 | Under Delivery Review | Peyman Motlagh; Sprint = RCS Support Team |
| Delivery Incident | Under Delivery Review | Ryan Barlow |
| Solutions Experts | Under Solutions Experts Review | Peter Just |
| CSM | Under CSM Review | CSM responsable |

La tabla “Under Delivery Review Notification” identifica Matthew Kamminga para Secure Incident & Audit, Ian Williams y Kenny C Vu para Engage, Carl Costelow para Secure Store. Es una tabla de notificación. No sustituye el campo Assignee de la matriz explícita. La página no explica el mecanismo de esas notificaciones ni resuelve toda diferencia entre ambas tablas.

## Comentarios: evidencia de las correcciones

Consulta completa: 3 comentarios principales y 1 respuesta; el conector no devolvió cursor adicional.

Comentario 477582852097, creado 2026-04-03 18:06:45 UTC, resuelto: “Aimee update graph - flow diagram”. No demuestra por sí mismo qué cambios hicieron al diagrama.

Comentario inline 478276452363, creado 2026-10-05 14:38:41 UTC, resuelto: “This needs to go to @Peter Just or @Nicole Myers now.”
Respuesta 478295130123 de Peter Just, creada 2026-10-13 07:51:03 UTC: “Please change to Peter Just”.
El cuerpo versión 26 confirma Peter Just. Nicole Myers aparece como alternativa propuesta en el comentario anterior; no presentarla como coasignación vigente.

Comentario 478296801281 de Ryan Barlow, creado 2026-10-13 13:44:55 UTC, abierto:
“@Viraj Kansara It is not necessary to also send a teams message. We have a queue that we work from… if the ticket is assigned to myself or Katy Scheldberg, or if the product type is in ("CAMS / Secure Audit (CAMS)", Izenda, "LPMS / Secure Incident (LPMS)", "Incident (f.k.a. LPMS)","Audit (f.k.a. CAMS)") AND the status is in Under Delivery Review AND Unassigned the ticket appears in our queue. We monitor the queue throughout the business day.”

Lectura operativa: Ryan indica que basta la cola y elimina el aviso extra de Teams para su ámbito. Describe entrada por asignación a Ryan o Katy, o por productos enumerados con Under Delivery Review y sin asignar. El comentario no publica el JQL; conservar su redacción y no inventar agrupaciones lógicas más precisas. La matriz de la página sigue indicando asignar Incident a Ryan. No convertir la posibilidad de entrada sin asignar en obligación de dejar sin asignar.

Enlaces directos a comentarios:
https://trebuco.atlassian.net/wiki/spaces/RTS/pages/474627801097?focusedCommentId=478276452363
https://trebuco.atlassian.net/wiki/spaces/RTS/pages/474627801097?focusedCommentId=478295130123
https://trebuco.atlassian.net/wiki/spaces/RTS/pages/474627801097?focusedCommentId=478296801281

## Contraste con el procedimiento complementario

Fuente leída en vivo: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478006902856
Título: Escalating Tickets to L3 Departments: Procedures and Responsibilities.
Versión 5, 27 agosto 2026 17:16:46 UTC.

Antes de escalar, L2 reproduce y documenta hallazgos como comentario interno. Debe incluir entorno Test/QA/Prod, reproducción completa con capturas, notas completas de Claude/IA usadas y conversaciones externas con otros ingenieros. Debe avisar al cliente del traslado al equipo investigador.

Esta guía dice que L2 hace triage de todas las aplicaciones excepto Engage. Conservar esa excepción al leer la introducción general de la página principal.

La guía describe creación automática de ENG para Under Engineering Review, RTAILIT para Under Infrastructure Review e INFOSEC para Under Security Review, con copia de comentarios en ambos sentidos. Son comportamientos documentados. No se probaron automatizaciones sobre tickets en esta tarea; una nota histórica ya advierte que no todos los comentarios de ENG se reflejan siempre.

La guía exige Teams a Ian para Engage Engineering y al CSM responsable. Esas instrucciones no quedan derogadas por el comentario de Ryan. Para Delivery Incident, el comentario directo de Ryan del 13 octubre corrige la exigencia anterior de Teams. Para Solutions Experts, el cuerpo actual y la respuesta de Peter corrigen James DeJohn.

Engage: informar al cliente, contactar a Ian como lead; respaldos Shruti Golwalker o Kenny Vu. Kevin Woo y Shruti manejan cambios POS; Kevin también trickle transactions. Para Critical/High, L1 publica en Engage Issues bajo Retail Ops. RTI/RTIaaS: L1 o L2 avisa al cliente; L1 publica Critical/High en Real Time Solutions.

Nomenclatura: AALPS comprende Incident, Audit, Aspect legacy y Apis; Secure 5 comprende Secure EBR y Secure 5; Legacy Secure Issues comprende Secure 3 y 4.

## Reconciliación con Cerebro y límites

Fuentes locales leídas: db:knowledge_chunks/245, db:knowledge_chunks/1620 y brain/memoria/reference_escalacion_l3_procedimiento.md. La consulta “474627801097 L2 L3” no recuperó una copia específica; la búsqueda técnica “L2 L3 RCS ticket management escalation” sí recuperó antecedentes.

1. La pregunta histórica sobre transcribir el gráfico queda resuelta mediante la tabla completa anterior.
2. Sustituir James DeJohn por Peter Just al usar este procedimiento. Las notas antiguas conservan valor histórico.
3. Eliminar el Teams obligatorio para la cola Delivery descrita por Ryan. No extenderlo a Engage, CSM o todas las colas.
4. La guía histórica db:knowledge_chunks/1620 mezclaba “Unassign” con asignaciones nominativas y añadía Database Services y Product Management. Ninguna de las dos páginas consultadas hoy contiene filas para Database Services o Product Management. No extraer esas rutas de esta página.
5. La memoria local registra corrección de Jon Morgan del 8 septiembre: Blue Team debe ir por Engineering, no por Waiting for Database Services. Este antecedente procede de una nota local; esta tarea no releyó el Teams original. No elevar esa nota a verificación en vivo.
6. Permanecen sin respuesta en esta página: mecanismo de pedir ayuda a Engineering sin transferir, pausa de SLA, árbitro para facturabilidad, plazos de aceptación y cobertura fuera de jornada. La publicación reciente no prueba que haya cambiado todo el proceso.
7. No convertir estados mencionados en páginas antiguas de equipos en transiciones actualmente disponibles de Jira. Consultar el ticket concreto cuando Juan vaya a ejecutar.

Alcance de captura: cuerpo vigente completo, diagrama vigente completo, comentarios y respuestas devueltos, cuatro páginas enlazadas de equipos, contraste textual con la guía complementaria. No incluye historial completo de versiones ni transcripción de adjuntos antiguos que la página vigente no muestra. No se comprobaron los diagramas de la guía complementaria; el análisis de esa fuente se limita a su texto.

## Uso y almacenamiento

Esta nota es conocimiento interno, no borrador de comentario ni prueba de envío. No corresponde a un ticket individual. Jira y Confluence se consultaron en solo lectura. brain/sessions.db no recibió escrituras. Juan incorpora la nota a esa base desde su terminal con cerrar. El índice derivado de Cerebro puede recuperar inbox en la siguiente búsqueda.

## Anexo: páginas de equipos enlazadas, texto completo

Los cargos y procedimientos siguientes reflejan lo publicado en cada versión, no una verificación independiente del roster actual. Las páginas Engage y Legacy conservan vocabulario histórico como Waiting For Engineering y Waiting For Customer; usar la matriz principal y validar Jira antes de actuar.

### AALPS team

Fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/474627735563
Versión 13; fecha 2026-04-06T19:43:46.989Z.

| **Name** | **Role** |
| --- | --- |
| Ryan Barlow | Implementation lead |
| Matt Kamminga | Product Owner |
| Chris Rippingale | VP Engineering |


### Engage team

Fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/474627899400
Versión 3; fecha 2026-03-31T19:52:16.323Z.

| **Name** | **Role** |
| --- | --- |
| Mike Tasch | Verify Infrastructure |
| Kenny Vu | VP Engineering, Product Owner |
| <retail-verifyengineering@apprissretail.com> | Email group |

**Process:**

A. Assignment and notification

L1 or L2 team assigns the RCS ticket to engineering team if there is a bug or a deeper investigation is required. Ticket can also be moved to engineering by other teams such as CSM or DataOps. This is done by changing the ticket transition to ‘Waiting For Engineering’. This moves the ticket to the ‘Verify Engineering Tickets’ queue in JIRA. If a Critical or High ticket is raised, Verify Management gets a notification email. In many instances, L1 team reaches out via the TEAMS channels to highlight Critical and HIGH issues. As needed, OPSGENIE may be used by L1 team to inform the engineering team when there is no response via TEAMS.

B. Working the ticket

The Jira queue is monitored by Kenny Vu who assigns the ticket to a engineer by updating the ‘Assignee’ field in the ticket. The assignee receives an email notifying them of the assignment.

The engineer works on the ticket until resolved or may assign it to a different team by changing the ticket workflow transition. While working the ticket, an engineer may chose to leave the ticket in ‘Waiting For Engineering’ status or change it to ‘Work in Progress’. If further information is needed from the customer, ticket status can be set to ' Waiting For Customer'. If the issue requires development work, a ticket is created in the Jira TREVERI project, which is the Verify development ticketing system. 

C. Updating the ticket

The engineer is expected to update the ticket atleast once a week even if there are no changes in status. The update can range from a specific update to simply, ‘testing in progress’. Comments can be made internal only or customer facing. 

D. Closing the ticket

Once work is complete on the ticket, the engineer will set the ticket status to ‘Complete’. This signifies that issue has been resolved. However, this does not imply that ticket is closed. Customer can verify the resolution before ticket can be set to ‘Closed’. If issue is not resolved, ticket can be moved to other statuses as needed. 

When setting the status to ‘Complete’, Resolution details will need to be provided from the dropdown options. After customer has verified the resolution, Support or Engineering team will set the ticket to ‘Closed’. 

E. Handling ‘SOW Estimation’ ticket types.

‘SOW estimation’ is used typically by CSMs to develop a work estimate or an SOW for a customer. In this case, Support (L1 or L2) is usually not involved and ticket may move back and forth between the CSM and engineering teams. SOW estimation workflow can be viewed on the main page of this section: [L2 to L3 RCS ticket management](https://trebuco.atlassian.net/wiki/spaces/RTS/pages/474627801097/L2+to+L3+RCS+ticket+management)

Note: Verify change requests are typically Modeling changes and require SOW.


### Legacy Secure team

Fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/474627866642
Versión 6; fecha 2026-04-06T19:57:56.929Z.

| **Name** | **Role** |
| --- | --- |
| Tomasz Mikunda | Product Owner |
| Chris Rippingale | VP Engineering |
| Securedevops | Email group |

**Process:**

A. Assignment and notification

L1 or L2 team assigns the RCS ticket to engineering team if there is a bug or a deeper investigation is required. Ticket can also be moved to engineering by other teams such as CSM or Solution Experts. This is done by changing the ticket transition to ‘Under Engineering Review’. This moves the ticket to the ‘Secure 3/4 Engineering Tickets’ queue in JIRA. If a Critical or High ticket is raised, Secure 3/4 Management gets a notification email. In many instances, L1 team reaches out via the TEAMS channels to highlight Critical and HIGH issues. As needed, OPSGENIE may be used by L1 team to inform the engineering team when there is no response via TEAMS.

Note: DataOps does not manage the Legacy secure DataLoads.  

Note: Legacy Secure team is based in Poland.

Note: Not all Secure 3 and Secure 4 customers are hosted by Appriss. Some servers are on-prem and customer is responsible for the environments. For these clients access to application and servers is restricted and usually requires tenant IT department involvement.

B. Working the ticket

The Jira queue is monitored by Tomasz Mikunda/ Maciej Pokorski who assign the ticket to an engineer by updating the ‘Assignee’ field in the ticket. The assignee receives an email notifying them of the assignment.

The engineer works on the ticket until resolved or may assign it to a different team by changing the ticket workflow transition. While working the ticket, an engineer may chose to leave the ticket in ‘Under Engineering Review’ status or change it to ‘Work in Progress’. If further information is needed from the customer, ticket status can be set to ' Waiting For Customer'. 

Note: Only minor development work and bug fixes are being done for Legacy secure.

C. Updating the ticket

The engineer is expected to update the ticket atleast once a week even if there are no changes in status. The update can range from a specific update to simply, ‘testing in progress’. Comments can be made internal only or customer facing. 

D. Closing the ticket

Once work is complete on the ticket, the engineer will set the ticket status to ‘Complete’. This signifies that issue has been resolved. However, this does not imply that ticket is closed. Customer can verify the resolution before ticket can be set to ‘Closed’. If issue is not resolved, ticket can be moved to other statuses as needed. 

When setting the status to ‘Complete’, Resolution details will need to be provided from the dropdown options. After customer has verified the resolution, Support or Engineering team will set the ticket to ‘Closed’. 

E. Handling ‘SOW Estimation’ ticket types.

‘SOW estimation’ is used typically by CSMs to develop a work estimate or an SOW for a customer. In this case, Support (L1 or L2) is usually not involved and ticket may move back and forth between the CSM and engineering teams. SOW estimation workflow can be viewed on the main page of this section: [L2 to L3 RCS ticket management](https://trebuco.atlassian.net/wiki/spaces/RTS/pages/474627801097/L2+to+L3+RCS+ticket+management)


### Secure 5 team

Fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/474627605114
Versión 12; fecha 2026-04-06T20:00:04.880Z.

| **Name** | **Role** |
| --- | --- |
| Shandana Khan | PM |
| Chris Rippingale | VP Engineering |
| Securedevops | Email group |
| Kenny Vu | VP Engineering |



