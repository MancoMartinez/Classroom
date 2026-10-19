# KT Kristin — Sign-off & Procesos RTS

Carpeta 21 de la base de Moscú. 55 fragmentos.

## help@appriss inbox — manejo de clientes FUERA del portal
_chunk 1183 · 2026-07-14 · fuente: kt-kristin-2026-07-14_

Responsabilidad heredada de Kristin (sesión 2026-07-14). El inbox help@appriss lo ve también L1; ahí escriben clientes que NO están en el portal. Reglas:
- NO se abre ticket automáticamente: las organizaciones controlan quién abre tickets. Walmart exige UN contacto único (el application administrator canaliza todo); ASDA pidió un email dedicado para sus stores (los associates ven "help at Appriss" en la app y escriben ahí en vez de ir por su admin — casi siempre es tema de acceso/promoción).
- Cómo leer el inbox: subject con "RCS-####" = ya se está comunicando por ticket, no tocar. Sin RCS = alguien necesita ayuda → verificar si está en el portal (si estuviera, se le vería); si no está, responder redirigiéndolo a su application administrator o al canal del cliente.
- Kristin responde DESDE SU CORREO personal (no el de soporte) para que el cliente tenga un contacto de vuelta — si respondes desde el genérico y no está en el portal, no puede seguir el hilo con nadie.
- Cheat sheet de canned responses por cliente (ICA, Ahold —sus mensajes de "Zeus"—, ASDA...) + contactos de escalación del cliente (ej. Carl Reasoner en ASDA: se le agrega al hilo si el cliente dice que no recibió feedback). Kristin la comparte actualizada.
- Truco para encontrar el admin correcto de una org: sección Customers del portal → ver quién abrió tickets recientes y de qué tipo (quien abre tickets de incident reports es admin de aplicación; quien abre data tickets no te sirve para accesos).
- Inbox legacy "Retail Client Services": ya no existe como servicio, tiene auto-reply; solo llega junk y correos legales — para esos, canned response que dio Legal (Kristin la reenvía) y borrar. Correos raros → forward a Legal y que ellos decidan.
[Fuente: KT Kristin 2026-07-14, transcript oficial — meeting 65]

## KT Kristin 14-jul (tarde) — Statuses de ticket y escalación entre departamentos
_chunk 1221 · 2026-07-14 · fuente: kt-kristin-2026-07-14-tarde_

Sesión KT con Kristin, 14-jul-2026 por la tarde (~26 min, con Aimee, J.R. y Camila presentes). Tema: statuses de ticket y cómo escalar a cada departamento. Nombres corregidos de ASR: "EMG/NNG/NFT" = ticket ENG; "Stage Engineering" = Engage Engineering; "Shannon" = Shan (Shandana Khan); "Spotify" = Shopify.

PRIMER TOQUE (obligatorio): al tomar un ticket, cambiarlo a Work in Progress y enviar al cliente la canned response "New Ticket Assignment First Response" (confirma ownership). Luego triage con notas internas, nota al cliente, y pasar a Under Customer Review.

UNDER CUSTOMER REVIEW: es el ÚNICO status que pausa los timers de SLA. Cuando el cliente responde, el ticket vuelve SOLO a Work in Progress (así se detecta la respuesta). Solo desde Work in Progress se puede completar/cerrar un ticket.

ESCALACIÓN A ENGINEERING:
- Secure / Incident → status Under Engineering Review + asignar a Shan (Shandana Khan). Al mover, se AUTO-CREA un ticket ENG; Shan mira el ENG correspondiente y lo asigna al ingeniero que trabajará el issue. No se clona a mano.
- Engage → Under Engineering Review + asignar a Ian Williams (el ingeniero de Engage) + mensaje de Teams OBLIGATORIO (no ve las asignaciones solo). Engage Engineering es entidad separada; Shan tomó Incident apenas el año pasado; pasaron bajo Chris (Rippingale) recientemente.
- Soporte tiene visibilidad LIMITADA a los tickets ENG; los comentarios/estados de engineering no siempre reflejan en el RCS.

INFRAESTRUCTURA: Under Infrastructure Review (Retail IT). OJO: este status NO vuelve solo a Work in Progress cuando infra actualiza — hay que vigilarlo manualmente. Action item abierto: hablar con Austin para automatizar el retorno a Work in Progress.

SECURITY: al escalar se auto-crea un ticket propio (INFOSEC), status Under Security Review, el OWNERSHIP se queda en soporte. La conversación sincroniza ambos lados y llegan emails cuando security comenta.

DELIVERY / PAYMENTS: status Under Delivery Review. Peyman Motlagh (Delivery Secure 5; 'Peyman Motlagh' era error de ASR) revisa que no sea algo que soporte pueda resolver y lo asigna al equipo de delivery — hoy Tom Walker (p.ej. issues de Shopify). Professional Services = cliente pide cambiar el producto → lo toma el equipo de payments/delivery.

REGLA DE ESFUERZO: soporte se queda con todo lo que sea ≤4 horas de trabajo; lo demás se escala. El umbral VA A BAJAR a ≤2 horas (comentario en la reunión: "four hours is crazy").

TRAINING / HOW-TO (Engage): se asignan a James DeJohn, que reparte a su equipo. En teoría deberían ser SOW facturables, pero en 3 años nunca se ha cobrado un training.

OWNERSHIP (pregunta de Camila/J.R.): mientras sean tickets RCS/RTS, dejar el proceso como está hasta que el "support project" (tickets SUP) esté andando; la transición será por piezas. Tras la salida de Kristin (31-jul), Shan podría reasignar los RCS de vuelta al equipo, pero la recomendación explícita fue NO cambiar nada aún.

PRÁCTICA RECOMENDADA: al asignar a delivery/CSMs, siempre email + mensaje de Teams (Ian y Ryan suelen no ver los tickets asignados).

DOCS: todo esto existe en Confluence pero disperso; Kristin no encontró el doc en vivo y empezó uno nuevo consolidado ("departmental ticket process"). Sesión extra de 30 min agendada para mañana 15-jul para revisar ese doc y el resto de statuses. Ese doc va a la lista de migración antes del 31-jul.

## KT Kristin 15-jul — Playbook help inbox en vivo: ticket por cliente sin portal (LULU) + Samsung Infra Readiness
_chunk 1251 · 2026-07-15 · fuente: kt-kristin-2026-07-15-oficial_

Sesión KT con Kristin (15-jul, ~36 min): dos casos reales trabajados en vivo, ambos entrados por el buzón help@appriss (correo que también ve L1). Nombres verificados en Jira: Bryant McAnnally (CSM de Lululemon), James DeJohn (Sr. Solution Expert, el "Jim" de sesiones previas), Alyssa Garrison (contacto de Lulu CON acceso al portal), Shandana Khan.

CASO 1 — LULU, upload roto (RCS-27843). Una persona de Lululemon SIN acceso al portal escribió al buzón (su grupo interno debía abrir ticket en el portal y no pudo). Playbook de Kristin: (1) buscó si ya existía ticket — no; (2) validó con el CSM Bryant McAnnally: no es high priority (internamente lo tienen como medium) y según él era tema de training → Solution Expert; (3) creó el ticket manualmente copiando el texto LITERAL del correo, puso a Alyssa Garrison como reporter (sí tiene portal, recibirá las comunicaciones), product type EBR validado con el CSM, problem type "feature functionality question", prioridad Medium; (4) APAGÓ la notificación automática al cliente porque el CSM lleva la comunicación; (5) nota interna "per request of Bryant" explicando el enrutamiento; (6) lo movió a Solution Expert. GIRO: James DeJohn comentó en el ticket que es el mismo bug que DSG — RCS-27806 "Dick's Sporting Goods — User Data is immediately deleted after it is saved" (reportado por él el 13-jul, asignado a Shandana Khan, Under Engineering Review) — o sea bug real multi-cliente en Secure user data, no training → el ticket volvió a Under Support Review y se linkea con el de DSG. Lección: "that's the beauty of having the communication" — el enrutamiento inicial del CSM puede corregirse al cruzar información.

CASO 2 — Samsung 3rd Party Infra Readiness (RCS-27847, ASIGNADO A JUAN). Vineet Saurav (Accenture, Samsung Operations Lead) pidió por correo la validación de infraestructura para el Flagship launch del 22-jul 6AM PST (preventa 22-jul→8-ago, monitoreo reforzado 48h post-launch). Llegó al buzón porque es CONTRATISTA: los clientes no suelen dar acceso al portal a contractors, así que no puede abrir tickets — está atascado. Proceso enseñado por Kristin: soporte NO tiene los datos del cuestionario (load tests, tráfico esperado, scale-up, rate limits, timeouts, fallback/RTO, code freeze) → los tiene el equipo de Infraestructura. Se crea ticket con JUAN como reporter (no hay nadie de Samsung en el portal a quien poner), se adjunta el cuestionario, se mueve a Under Infrastructure Review y — regla de la matriz del 09-jul — EN TICKETS DE INFRAESTRUCTURA SOPORTE SE QUEDA ASIGNADO. Prioridad Low porque no es break/fix ("información necesaria, pero no para ya"). La comunicación con infra va por EMAIL directo (excepción; normalmente no se comunica por email). Seguimiento MANUAL: el status de infra no vuelve solo a Work in Progress — hay que vigilar el ticket. Pendiente de Juan: vigilar respuesta de infra, y responder formalmente a Vineet con el cuestionario lleno antes del 22-jul.

Reglas destiladas de la sesión: el buzón existe para gente fuera del portal (contractors, contactos no registrados); todo trabajo se formaliza como ticket venga por donde venga; validar prioridad y product type con el CSM antes de guardar; copiar el texto literal del cliente; elegir reporter registrado para que fluyan las notificaciones; apagar la notificación automática si el CSM lleva la comunicación; nota interna siempre que el enrutamiento sea excepcional; linkear tickets con el mismo síntoma entre clientes.

TICKETS DE REFERENCIA (estado al 15-jul):
- RCS-27843 "LULU - Issue with Uploading document" — Incident, Medium, Under Support Review, sin assignee. Síntoma: CSV en Secure user data se guarda "exitosamente" pero desaparece de la lista. Empezó 15-jul; semana anterior funcionaba.
- RCS-27806 "Dick's Sporting Goods Inc - User Data is immediately deleted after it is saved" — Incident, Medium, Under Engineering Review, assignee Shandana Khan, reporter James DeJohn (13-jul). MISMO BUG que el de LULU → linkear.
- RCS-27847 "Samsung - 3rd Party Infra Readiness Checklist information needed" — tipo SOW Estimation, Low, Under Infrastructure Review, reporter y assignee JUAN MARTINEZ. Deadline real: launch 22-jul 6AM PST. Contacto externo: Vineet Saurav (Accenture, vineet.saurav@accenture.com).

CORRECCIONES DE NOMBRES vs sesiones previas (ASR): "Jim Dijon" = James DeJohn (Sr. Solution Expert); "Brian/Bryant" = Bryant McAnnally (CSM Lululemon); "Alexa/SELISA" = Alyssa Garrison (contacto Lulu con portal).

## DOC OFICIAL — Escalación a L3: matriz completa de statuses/assignees (Confluence RTS)
_chunk 1265 · 2026-07-15 · fuente: confluence-rts-478006902856_

DOC OFICIAL (Confluence RTS, Aimee Wadsworth, 15-jul-2026): "Escalating Tickets to L3 Departments: Procedures and Responsibilities"
https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478006902856

Contexto: L2 triagea TODOS los tickets de todas las aplicaciones EXCEPTO Engage. L2 investiga recreando el issue y documentando hallazgos como nota interna. Si L2 no puede resolver, se avisa al cliente que el ticket pasa a otro equipo.

CHECKLIST OBLIGATORIO antes de escalar a cualquier L3:
- Environment donde vive el issue (Test/QA/Prod)
- Documentación completa de cómo reproducir (paso a paso + screenshots)
- Notas COMPLETAS de Claude/AI usadas en el troubleshooting
- Notas de conversaciones con otros ingenieros fuera del ticket

MATRIZ OFICIAL (statuses y assignees):
- Secure/Incident Engineering → "Under Engineering Review" + Shandana Khan. Al mover se AUTO-CREA ticket ENG; los comentarios se copian en ambas direcciones.
- Engage Engineering → "Under Engineering Review" + Ian Williams + mensaje de Teams. Si Ian no está: Shruti Golwalker o Kenny Vu. Kevin Woo y Shruti manejan POS changes de Engage; Kevin también trickle transactions. Critical/high → L1 postea en el canal Engage Issues de Teams (Retail Ops).
- Infrastructure → "Under Infrastructure Review"; TE QUEDAS ASIGNADO. Se auto-crea ticket RTAILIT; comentarios sincronizan ambos lados.
- Security (InfoSec) → "Under Security Review"; TE QUEDAS ASIGNADO. Se auto-crea ticket INFOSEC; comentarios sincronizan.
- Delivery · Secure 5 → "Under Delivery Review" + Peyman Motlagh + agregar "RCS Support Team" al campo Sprint.
- Delivery · Incident → "Under Delivery Review" + Ryan Barlow + mensaje de Teams.
- Solutions Experts → "Under Solutions Experts Review" + James DeJohn.
- CSM → "Under CSM Review" + el CSM responsable + mensaje de Teams.

MAPA DE COLAS DE ENGINEERING: AALPS = engineering de Incident Audit / (legacy) Aspect y APIS · "Secure 5" = Secure EBR y Secure 5 · "Legacy Secure Issues" = Secure 3 y 4.

CORRECCIONES vs transcripts previos (ASR): "Lehman" = Peyman Motlagh (Delivery Secure 5); el ticket de security es INFOSEC (antes anotado como "NERC (sic)"). NOTA: Aimee confirmó que J.R. planea cambiar/simplificar este proceso — matriz vigente hoy, sujeta a cambio.

## Release Calendar — cheat sheet de Kristin (link oficial)
_chunk 1267 · 2026-07-15 · fuente: kristin-cheat-sheet_

https://docs.apprissretail.com/products/product-docs/general/release-calendar — Calendario oficial de releases por producto (Appriss Retail Documentation). Enviado por Kristin el 15-jul-2026: parte de su cheat sheet personal ("you will want this one"); se revisa en el shadow del viernes 18-jul. Usos: (1) triage — si algo que funcionaba se rompe de golpe para varios clientes, revisar si hubo release esa semana (patrón DSG/Lulu); (2) prometer fechas reales al cliente cuando un fix va "en el próximo release" (cadencia semanas 2 y 4); (3) responder la sección de code freeze en readiness checks como el de Samsung (RCS-27847).

## DOC OFICIAL — RCS Ticket Status Guide: qué significa cada status (taxonomía completa)
_chunk 1268 · 2026-07-15 · fuente: kristin-articles-2026-07-15_

Artículo KB enviado por Kristin 15-jul-2026 ('Couple More Articles'). Complementa la matriz de escalación (chunk 1265) con la taxonomía COMPLETA:

RCS Ticket Status Guide

This knowledge base article explains what each RCS ticket status means, who typically owns the next action, and how support teams should interpret the ticket’s current stage.

Active Support Statuses

Under Support Review
The ticket has just come in and is being triaged by the support team. No engineer has taken ownership yet.

Work in Progress
A support engineer has taken ownership and is actively investigating the issue.

Escalated
The ticket has been flagged as requiring elevated attention, typically due to urgency, complexity, or customer impact.

Resolution Suggested
The support engineer has proposed a fix or workaround and is waiting to confirm it resolves the issue.

Under Customer Review
The ball is in the customer's court -- we've asked a question or provided a solution and are waiting for their response.

Routing Statuses: Waiting on an Internal Team

Routing statuses indicate that the ticket has been assigned to a specific internal team for input or action. Support is waiting for that team to respond before moving the ticket forward.

	•	Under Engineering Review: Requires a developer to investigate or fix a code-level issue.
	•	Under Solutions Expert Review: Requires input from a Solutions Expert or User Consultant.
	•	Under Analytics Review: Requires review or action from the Analytics team.
	•	Under CSM Review: Requires input from the Customer Success Manager.
	•	Under Infrastructure Review: Requires review or action from the Infrastructure team.
	•	Under Database Services Review: Requires Database Services to run queries or make data changes.
	•	Under Delivery Review: Requires review or action from the Delivery team.
	•	Under Product Management Review: Requires Product Management input, such as for feature requests or product decisions.
	•	Under Security Review: Requires review or action from the Security team.

Release and Backlog Statuses
Waiting for Software Release
The fix is confirmed and built, but it cannot be deployed until the next scheduled software release.

Added to the General Backlog for Future Consideration
The request or issue is valid but will not be addressed immediately. It has been logged for potential future work.

Closed Statuses

	•	Completed: The issue has been fully resolved to the customer’s satisfaction.
	•	Closed: The ticket is finished and can be reopened if the issue resurfaces.
	•	Duplicate: The ticket covers an issue that is already being tracked in another ticket.

## DOC OFICIAL — Ticket Types (Incident/SOW/SOW Est/New Feature) + Queue Review process
_chunk 1272 · 2026-07-15 · fuente: confluence-rts-478007263240_

DOC OFICIAL (Confluence RTS, Aimee Wadsworth, actualizado 10-jul-2026): "Updating Ticket Type: Steps to Follow"
https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478007263240

LOS 4 TICKET TYPES DE JIRA (RCS):
- Incident: break/fix — algo roto o dando errores.
- SOW: preguntas generales, how-to, y solicitudes de cambio simples.
- SOW Estimation: cuando hay que crear un SOW (estimar trabajo facturable). Lo usan típicamente los CSMs; suele moverse entre CSM y engineering sin involucrar a soporte.
- New Feature: solicitudes de funcionalidad nueva.

POR QUÉ EL TYPE CASI SIEMPRE LLEGA MAL: el cliente solo ve 2 opciones al crear el ticket — "Change Request" (default → New Feature) o "Support Ticket" (default → TODO cae como Incident). Por eso el Queue Review debe corregir el type manualmente.

REGLA DE ORO (email de Aimee 15-jul): "anything that is broken or giving errors = Incident; anything that is simply a question, or request to change something = SOW".

PASOS PARA CAMBIAR EL TYPE: botón de tipo arriba del ticket → dropdown → New Issue Type → Next → Next (nada cambia) → Confirm.

QUEUE REVIEW (proceso asignado a Camila y Juan mientras Aimee está fuera 2 semanas desde 16-jul-2026): revisar que todos los tickets de la cola sin asignar tengan (1) ticket type correcto, (2) prioridad correcta (Critical/High/Med/Low según el issue), (3) label Support_Data_Team en tickets de data de Secure 5. Dudas → Kristin.

## Queue Review con Kristin 16-jul — reglas de prioridad, canal Support Team Priority, Kohl's a Infra, handoff de emails 20-jul
_chunk 1280 · 2026-07-16 · fuente: kristin-queue-review-2026-07-16_

Llamada 16-jul con Kristin (~24 min): validación de 3 tickets del Queue Review + 2 anuncios de proceso.

TICKET 1 — ASICS RCS-27768 (inventory upload, SOW): SE QUEDA MEDIUM. Regla: un change request solo sube a High si el CSM lo empuja ("this is affecting XYZ"). Un Incident que bloquea el trabajo del cliente sí se sube. Mención de paso: Kristin Dyer (Solution Expert) relacionada con el tema. NOTA: la pregunta por RCS-27767 (Incident ASICS, ~$1.7M ventas faltantes) no se hizo — aplicar la misma regla: que lo empuje el CSM.

TICKET 2 — Casey's RCS-27824 ("information is critical", caso FBI): NO se toca el campo Priority; se acelera posteando en el canal de Teams "Support Team Priority" ("this needs to be picked up sooner than later"). Kristin lo posteó ella misma porque Juan aún no tiene acceso al canal (pedido a Aimee hace ~2 semanas, pendiente con J.R.). Regla cultural: NUNCA asignan tickets a dedo — el conteo engaña (3 tickets de data > 8 tickets simples); se pregunta en el canal quién puede.

TICKET 3 — Kohl's RCS-27840 (Workday WAF, deadline 1-ago): Kristin CONFIRMÓ que es Infrastructure, no Support Data Team. Plan (mismo patrón que Samsung RCS-27847): responder al cliente Kyle Kimmerly ("your ticket will be moved to the Infrastructure Team; once information is available we will provide updates" — sin sobreprometer), Juan se asigna el ticket (regla infra: soporte queda asignado), mover a Under Infrastructure Review, y ping por Teams a Russ (Russell Harmon) de infra. Infra trabaja en hora del PACÍFICO y acaban de perder a una persona.

ANUNCIO 1 — Desde el LUNES 20-jul el flujo de emails de soporte (los que hoy recibe Kristin) pasa a Juan y Camila, con Kristin en copia para monitorear. J.R. lo decidió esta mañana; le pidió a Kristin un doc del proceso (no empezado). "Another big review on Friday" (sesión 18-jul).

ANUNCIO 2 — Kristin pidió a Juan priorizar el shadowing: a ella le quedan 2 semanas (sale 31-jul) vs Aimee que estará ~2 meses más. Usar a Kristin para lo que solo ella sabe: el proceso de email/help inbox (que además Juan hereda el lunes).

REGLAS DESTILADAS (Queue Review / prioridades):
- Change request (SOW) → Medium por defecto; solo High si el CSM lo empuja con impacto concreto.
- Incident que bloquea el trabajo del cliente → sí amerita subir prioridad.
- Ticket urgente sin dueño → NO subir Priority a mano: postear en el canal Teams "Support Team Priority" para que alguien lo tome. Pedir acceso al canal (pendiente con J.R.).
- Nunca asignar a dedo: la carga real no es el número de tickets (data tickets pesan más).
- Enrutamiento a Infrastructure = responder al cliente sin sobreprometer + quedarte asignado + Under Infrastructure Review + ping a Russell Harmon. Infra = Pacific Time, equipo corto de gente.

## Rutina matinal L2 — shadow Kristin 17-jul-2026 (playbook)
_chunk 1301 · 2026-07-17_

RUTINA MATINAL DE L2/PROCESS ANALYST (shadow de Kristin Krogman, 17-jul-2026, meeting 74; transcript oficial de Teams).

ORDEN DEL DÍA (cadencia de Kristin, adaptable):
1. EMAILS/NOTIFICACIONES: revisar todo lo de overnight (UK/EU), alertas de SLA breach (con la cola alta NO se postean; con cola normal se postea al team: "este ticket está por breach, que alguien lo tome"), mensajes de Teams pendientes de follow-up.
2. TICKETS ESCALADOS/HIGH PRIORITY sin dueño: si tienes el conocimiento, tómalos tú (ej. hoy: 2 tickets del platform change de Incident — clientes deben seguir usando la URL/dominio viejo hasta migrar).
3. BACKLOG (ahora Juan+Camila): summaries con nombre de compañía, prioridades bien puestas, NO hay tickets Engage (L2 no los triagea: password reset/mirror sí se toman; el resto → Marissa Johnson o Shruti en Engineering), ticket types correctos (el portal defaultea a Incident; hoy corrigió un SOW→Incident en vivo), labels de data.
4. TICKETS PROPIOS: follow-ups a clientes ("¿recibiste mi última respuesta?"), validaciones pendientes.
5. EMAILS DE AUTOMATIZACIÓN 7/14/28 días: Dean maneja los de 14; el de 28 días CIERRA el ticket (pasará a 21 días). Revisar cada cierre: ¿hay razón para reabrir? Internos → quedan cerrados. TJX/clientes high-priority → doble check. RTI portal access → normalmente queda cerrado (cliente no responde si funcionó); si ves varios del mismo cliente → preguntar al CSM.
6. ALERTAS DE COMENTARIO DE CSM: cuando un CSM comenta un fix hecho, el ticket debe volver al assignee ORIGINAL de soporte para testear y avisar al cliente (ej.: Paul mencionó a Carl y Jim pero el assignee era Dean → avisarle a Dean).
7. HELP@APPRISS INBOX: revisar nuevos (viernes suele estar quieto). CC a Juan/Camila en respuestas. Conocer contactos clave de clientes (ej. Corey Hendrick, Home Depot — responde rápido, útil en emergencias).
8. FILTROS/REPORTES: (a) status Complete → revisar comunicación y cerrar del todo (Closed NO se reabre si el cliente responde; Complete SÍ vuelve a WIP si responden — muchas veces es solo un "gracias": se cierra de nuevo). Buena práctica: "el trabajo está completo; si no necesitas nada más, se cierra en 2 días hábiles". Cualquier associate puede mover a Closed, no solo leads. (b) Tiger Team (tickets viejos). (c) Dashboard de tickets por persona en soporte: estándar máx ~10 tickets por persona (data tickets cuentan más porque tardan); úsalo para saber a quién pedirle capacidad.

DATOS DEL DÍA: backlog en 31 = muy alto (lo normal era ~10, ideal 0). Payman con 40 tickets y recibiendo los de Smeet (último día de Smeet). RCS-27765 (Winn-Dixie data file check) asignado a Juan EN VIVO en esta sesión. Kohl's RCS-27840 (Infra, due 1-ago): si el RTAILIT no está asignado el lunes/martes 20-21 jul, follow-up con Infra. RCA: solo se comparte con el cliente SI LO PIDE, y pasa por management qué se comparte.

## KT Kristin 21-jul — Backlog, asignación, prioridad, on-call, ruteo (transcript oficial, meeting 77)
_chunk 1356 · 2026-07-21_

Sesión KT con Kristin Krogman (21-jul-2026, 54 min, meeting 77). Conocimiento operativo durable para el sign-off; corrige los errores del speech-to-text en vivo: "payment"/"Paimon"/"Payman" = Peyman (Motlagh); "Shelly/Jelly" = Shelley Cameron.

ASIGNACIÓN DE TICKETS (modelo pull, no push). No se asigna directo salvo 3 casos: (1) cluster de duplicados linkeados de un mismo issue → se asigna a quien investiga, el resto ayuda a responder al cliente; (2) balanceo por carga/expertise vía dashboard (unos son mejores en Incident, otros en EBR) — Kristin/Aimee contactan directo cuando la cola está saturada; (3) área especialista: Engage → Marissa Johnson siempre trabaja esos.

ON-CALL. Soporte NUNCA tuvo on-call: era el equipo de Delivery/engineering + L1 manejaba casi todo. Ahora los leads (Juan/Camila) entran a ese esquema. Para dudas de on-call → Peyman Motlagh (ha hecho on-call con el data team; por eso el data team se pasó a soporte, para descargarlo). High-priority off-hours se postean en el priority channel.

REGLA AURORA (cheat sheet): cualquier ticket que menciona el sistema AURORA va a Delivery — Soporte NO tiene acceso a Aurora. Route on sight.

THINKLP → AURORA (RCS-27822). ThinkLP no es de Appriss (empresa distinta, tipo incident). Migración ThinkLP→Aurora. Quién deshabilita ThinkLP = por confirmar; Kristin preguntó a Shelley Cameron (estuvo en esas calls). Involucrados: Carl Costelow, Jeff y Flavio (Delivery Council). Probablemente lo hace el implementation team de Carl (disable/enable Aurora). Soporte NO deshabilita → sacar de la cola.

DECOMMISSION (DCOM). Lo abre el CSM (el cliente le avisó que se va o cambia de plataforma). Viene acompañado de un ticket de engineering (bajar DB, etc.) y a veces un ticket "AA" (acceso/portal) para quitar acceso de la organización. Ejemplo: Dollar General se decommisiona por completo (no migra a otro producto) → linkear el AA al RCS, asignado a Austin Flannery; cerrar el RCS cuando Austin termine su parte. Además: mover al cliente a "previous/canceled" en el client contact sheet y quitarlo de todas las listas vivas (outage listing, contact listing). Proceso también en Confluence.

HIGIENE DE TICKETS (revisar en cada uno del backlog):
- Etiquetar el CLIENTE/compañía siempre (ayuda a reports, evita que scrolleen). Acrónimos: PSCB = PacSun Eddie Bauer; también SSP, Waitrose, Mid Counties.
- Sprint & Team Ownership = "support delivery" + "backlog" → son las labels que Peyman quiere en tickets NUEVOS para verlos entrar en su dashboard; él decide el ruteo. Por eso NO mandarlos tú al backlog: márcalos support-delivery y Peyman triagea.
- Ticket type correcto: break-fix = Incident; change request; question; new feature. Corregir "work type" si entró mal.
- Complexity: ya se autopobla.
- Data issue → etiquetar para Peyman (data team). Linkear tickets DO relacionados como "relates to" (ej. DO-9170). Clientes que migraron de Secure 3 suelen generar data tickets.

PRIORIDAD (definiciones):
- Critical = aplicación caída, nadie puede entrar. All-hands. Rarísimo ("the world has ended").
- High = un grupo/región no puede entrar (app sigue arriba) O afecta el trabajo diario del cliente (ej. Jira caído para nosotros; un equipo que trabaja incidents no puede acceder). Regla: ¿cómo afecta al cliente?
- L1 valida high priority con el cliente antes de postear ("how is this affecting you? why high priority?"); suele acertar; el call final lo hacen los leads.
- EXCEPCIÓN CONTRACTUAL: TJX — si abre high priority, se queda high pase lo que pase (por su contrato). ECA/ICA igual por ahora (puede cambiar).

RUTEO POR DOMINIO (contactos):
- Peyman Motlagh = data / on-call. John Morgan = Snowflake (primero para platform/Snowflake; si no está, Peyman). Carl Costelow = CCTV/CC y Aurora/implementation. Secure 3-4: solo Vlad Bogus, Matt Everett, Carlos. Dudas de EBR / triage → Carrie (Carolyn Allison). Engage → Marissa Johnson.
- Tickets Engage-sobre-plataforma: no existe label/type de "platform ticket" → los Secure-side no los ven en su dashboard. Mecanismo: heads-up a Peyman (o John Morgan si es Snowflake) con nº de ticket + resumen corto + marcar "not urgent". Si es high priority, postear en el Engage channel; si no, NO cargar al SRE (dejarlo libre para high priority real).

ETIQUETA OVERSEAS: a John Morgan, Carl y gente de EU/UK NO pingear en Teams after-hours → mandar EMAIL. Lo agradecen; es fácil de seguir y se retoma al día siguiente.

NAMING DE CLIENTE: en emails al cliente usar el nombre completo — Lululemon, NO "Lulu" (error que Kristin cometió una vez).

EMAIL DESDE TELÉFONO (flujo L1→email, no portal): L1 (ej. Aisha Mehar) recibe una llamada y manda email a soporte. No todo email = ticket. Si es un issue conocido y ya se dio guía al cliente (ej. la unificación de plataforma: usar el email como login ID, no el ID viejo), NO abrir ticket → buscar al ADMIN del cliente (mirar quién abrió tickets de tipo soporte recientemente), meterlo en el hilo (ej. Richard) para que resuelva el primer nivel (agregar usuarios, accesos) con su gente. Solo abrir ticket si es grande/nuevo y afecta a muchos → entonces abrir ticket, avisar al equipo y poner al admin como reporter. Los admins están entrenados para el primer nivel; no deben venir a soporte por eso.

HANDOFF DE PMs (nuevo cliente): cuando un cliente queda listo y se entrega a soporte, los Project/Product Managers mandan un email con una hoja de info (tickets abiertos, contactos para el client listing). Kristin los archiva; el equipo debe actualizar client listing / contact listing / outage listing. Cuidado con nombres espejo (ej. lío SSP vs SSP Markets = dos cosas distintas).

CHASING DE TICKETS ESTANCADOS (Juan+Camila harán mucho): los asignados (sobre todo EU/UK) no ven los @mentions (no revisan email). Método: Teams message / @mention primero; si no responden, cada 4-6 semanas mandar un email con la lista de tickets que necesitan update. Para gente en PTO (ej. Marissa), email para que lo vea al volver. No molestar de más: se da la oportunidad de mirar el ticket antes del email-recordatorio.

CIERRE DE TICKETS: tras resolver, dar 1-2 días de gracia para que el cliente valide; si no responde, mensaje "no hemos sabido de ti, asumimos que está bien, movemos a Complete y cerramos". Login issues (ID viejo vs email) se cierran así.

Horario de Kristin: intenta terminar 4pm (a veces más tarde). Disponible para follow-ups. Sale 31-jul.

## KT Kristin — resumen general y estado
_chunk 1095 · 2026-07-02 · fuente: KT Pair Tracker Kristin - Juan.xlsx_

Knowledge Transfer entre Kristin Krogman (Sr. Business Process Analyst, Appriss Retail, kkrogman@apprissretail.com) y Juan Martinez (Lead Support Engineer, nuaav, jmartinez@apprissretail.com). Periodo: junio 2026 (7 sesiones entre jun-4 y jun-24). Estado: 7 de 7 topics COMPLETADOS, 17 artifacts compartidos. PENDIENTE: el sign-off formal — las columnas "Signed off by" y "Sign off Date" de la hoja Artifacts están vacías. El companero original de shadowing (David) ya no está, por lo que Juan hace la revisión parcial y el sign-off directamente con Kristin en un meet. Los 7 topics: T-034 APIs + User Provisioning + Access reference; T-035 Eng escalation packaging standard; T-036 Cross-product knowledge map; T-037 Top-customer access/security playbook; T-075 User provisioning playbook; T-084 Decision tree API access + permissions; T-096 Client migration / downtime notification process.

## Portal de soporte — agregar customers y organizaciones
_chunk 1184 · 2026-07-14 · fuente: kt-kristin-2026-07-14_

Proceso (sesión 2026-07-14):
- Agregar persona: Customers → Organizations → buscar la org (ej. Meijer) → Add Customer → email → OK → le llega invite. Antes de agregar, buscar si ya existe (por email): si ya está, avisarle que ya tiene acceso y pasarle la URL del portal.
- Validación: si el solicitante es desconocido, confirmar con otro admin de la organización antes de agregarlo ("¿está bien agregar a esta persona?"). Si copian a alguien conocido en el email, eso vale como aval. Lo ideal: que el cliente abra ticket y lo haga L1. Muchas solicitudes llegan reenviadas por CSMs — válidas.
- Agregar organización (cliente nuevo que pasa a soporte): Customers → Organizations → Add Organization → nombre comercial; se usan paréntesis para aliases (ej. "Air Force (APs)").
[Fuente: KT Kristin 2026-07-14 — meeting 65]

## DOC OFICIAL — RCS Ticket Status Workflow Guide: cuándo cambiar cada status (principio: el status dice quién tiene la próxima acción)
_chunk 1269 · 2026-07-15 · fuente: kristin-articles-2026-07-15_

Artículo KB enviado por Kristin 15-jul-2026 ('Couple More Articles'). Guía paso a paso de cuándo actualizar el status; incluye la tabla situación→status:

RCS Ticket Status Workflow Guide
Article purpose: Use this guide to determine when to update an RCS ticket status so ownership, next steps, and customer expectations are clear.
Audience: Support engineers and internal teams working RCS tickets.
Key principle: The ticket status should always indicate who owns the next action.

Step 1: Ticket Comes In
Status: UNDER SUPPORT REVIEW
This is the default status when a ticket is first created. A support engineer should take ownership as soon as possible.
Action: After taking ownership, leave a customer-facing comment confirming that you are investigating, then move the ticket to WORK IN PROGRESS.

Step 2: Actively Working the Ticket
Status: WORK IN PROGRESS
Use this status whenever you own the ticket and are responsible for the next action.
  - You own the ticket. You are investigating, researching, or communicating
    with the customer.
  - This should be the status any time the ticket is in your hands and you
    are the one who needs to act next.

Change status when:
    - You need another internal team's help          --> Use the appropriate routing status (see Step 3)
    - You have proposed a fix to the customer        --> RESOLUTION SUGGESTED
    - You are waiting on the customer to respond     --> UNDER CUSTOMER REVIEW
    - The issue needs urgent attention               --> ESCALATED
    - The ticket is resolved                         --> COMPLETED

Step 3: Route to Another Internal Team
Use the routing status that matches the team receiving the ticket. After routing, that team owns the next action.
Sending to
Set status to
Engineering
UNDER ENGINEERING REVIEW
Solutions Expert
UNDER SOLUTIONS EXPERT REVIEW
Analytics
UNDER ANALYTICS REVIEW
Customer Success (CSM)
UNDER CSM REVIEW
Infrastructure
UNDER INFRASTRUCTURE REVIEW
Database Services
UNDER DATABASE SERVICES REVIEW
Delivery Team
UNDER DELIVERY REVIEW
Product Management
UNDER PRODUCT MGMT REVIEW
Security
UNDER SECURITY REVIEW

Important: Always leave an internal comment explaining what you need from the receiving team before changing the status.
When the team responds: Move the ticket back to WORK IN PROGRESS and continue investigating.

Step 4: Waiting on the Customer
Status: UNDER CUSTOMER REVIEW
 - Use this when you have asked the customer a question or proposed a
    solution and you are waiting for their reply.
  - The customer needs to act -- not you.

  CHANGE STATUS WHEN:
    - Customer responds with an answer               --> WORK IN PROGRESS
    - Customer confirms the issue is resolved        --> COMPLETED

Step 5: Proposed Fix Shared
Status: RESOLUTION SUGGESTED
- Use this when you have identified a fix or workaround and have shared
    it with the customer, but have not yet confirmed it worked.

  CHANGE STATUS WHEN:
    - Customer confirms it resolved the issue        --> COMPLETED
    - Customer says it did not work                  --> WORK IN PROGRESS

Step 6: Waiting for Software Release
Status: WAITING FOR SOFTWARE RELEASE
- Use this when Engineering has confirmed a code fix is ready but it
    cannot go live until the next scheduled software release.
 - The ticket is parked -- no action needed until the release happens.

  CHANGE STATUS WHEN:
    - The software release goes out and the fix is confirmed --> COMPLETED
    - Something changes and a workaround is found first      --> RESOLUTION SUGGESTED

Step 7: Escalation Required
Status: ESCALATED

  - This is used by the client when the issue is urgent, has high customer impact, or has
    been stuck without resolution for too long.
  - This flags the ticket for senior attention.

  CHANGE STATUS WHEN:
    - Escalation is resolved and work resumes        --> WORK IN PROGRESS

Step 8: Close or Defer the Ticket
COMPLETED
    - The issue is fully resolved and the customer is satisfied.
    - Use this as the standard closure status.

  CLOSED
    - The ticket is finished. Similar to Completed but can be reopened
      if the issue comes back.

  DUPLICATE
    - This ticket covers the same issue as another open ticket.
    - Link to the original ticket in a comment before closing.

  ADDED TO BACKLOG FOR FUTURE CONSIDERATION
    - The request is valid but will not be worked now.
    - Use this for feature requests or low-priority issues with no near-term fix.
    - Leave a comment explaining why it is being deferred.

Quick Reference Cheat Sheet

Situation
Status to set
Ticket just arrived, not yet owned
Under Support Review
I own it and am actively working it
Work in Progress
I need Engineering to look at it
Under Engineering Review
I need Database Services to run a query
Under Database Services Review
I need the Delivery team
Under Delivery Review
I need Analytics
Under Analytics Review
I need the CSM involved
Under CSM Review
I need Infrastructure
Under Infrastructure Review
I need Solutions Expert
Under Solutions Expert Review
I need Product Management input
Under Product Mgmt Review
I need Security to review
Under Security Review
Waiting for the customer to respond
Under Customer Review
Proposed a fix, waiting for confirmation
Resolution Suggested
Fix is built, waiting on a software release
Waiting for Software Release
Ticket is urgent or needs escalation
Escalated
Issue is fully resolved
Completed
Same issue exists in another ticket
Duplicate
Valid request, no near-term fix planned
Added to Backlog for Future Consideration

## Topics de APIs: T-034, T-037, T-084 (AALPS)
_chunk 1096 · 2026-07-02 · fuente: KT Pair Tracker Kristin - Juan.xlsx_

T-034 "APIs + User Provisioning + Access reference" (SME Transfer: APIs, live session 6.10.26, demo hecha). Docs: Linking Tickets.docx; "Creating Ticket link" y "How to open a ticket" en SharePoint de Kristin. T-037 "Top-customer access/security playbook" (doc review 6.16.26) y T-084 "Decision tree: API access + permissions" (video review 6.16.26) — ambos apoyados en la misma wiki: Confluence espacio AALPS, página "APIS" (https://trebuco.atlassian.net/wiki/spaces/AALPS/pages/273453096/APIS). Sesión relacionada (jun-5): login de APIs y ticket actual; Kristin compartió el link de la lista de clientes de soporte y el espacio WIKI de documentación APIS. Sesión jun-12: APIs start up process — doc "APIS Start First Steps.docx"; David quedó de configurar su acceso en los sitios PROD y Prep (pendiente heredado).

## Verify (Engage) portal — resets, altas con mirror y 2FA
_chunk 1185 · 2026-07-14 · fuente: kt-kristin-2026-07-14_

El portal Verify es la cara admin de Engage (cliente aún lo llama Verify). Juan necesita acceso: Kristin pregunta a Marissa Johnson; plan B, request a ITHD (Austin). Solo Juan por ahora, no Camila. Kristin montó este proceso por iniciativa propia: el grupo que hace resets entra 2-3h más tarde y el cliente no debería esperar por algo así de simple.
- RESET (lo más frecuente): Admin → Web User Listing → buscar por email/nombre → si el checkbox "disabled" está marcado, click en reset → le llega link. Avisar al solicitante ("ya envié el link para X"). Ojo Home Depot: tienen varias aplicaciones — pedir screenshot para confirmar que es Engage antes de tocar.
- ALTA con mirror: petición típica "dale a X el mismo acceso que Y". Edit sobre Y muestra sus checkmarks (áreas visibles) → tomar FOTO/screenshot → Add User → email del nuevo, marcar los mismos checkboxes, seleccionar retailer, y TELÉFONO obligatorio (2FA) — si no lo dieron, pedirlo → Save Changes.
- Frecuencia: en ráfagas (varios de golpe, luego un mes sin nada) — por eso está documentado con ejemplos de tickets en los docs del sign-off.
- Lo que soporte NO hace en Engage: cosas específicas del producto → Marissa Johnson (solution expert). Claims eligibility / void claim requests → SIEMPRE Marissa. Accesos de ABIS/incident: NO los cambia soporte, van por el lado del cliente (seguridad); SSO es la excepción parcial.
[Fuente: KT Kristin 2026-07-14 — meeting 65]

## T-035 Escalación a Engineering + T-036 mapa cross-product y SLAs
_chunk 1097 · 2026-07-02 · fuente: KT Pair Tracker Kristin - Juan.xlsx_

T-035 "Eng escalation packaging standard" (Process: Escalation, live session 06.16.26, demo hecha). Doc: "Escalating to Engineering.docx" — estándar de empaquetado para escalar de L2 a Engineering. La sesión de jun-16 cubrió además: cuándo/cómo contactar clientes, escalaciones L2→engineering, mover tickets con certificate requests y SSH Keys por expirar. T-036 "Cross-product knowledge map" (shadow session 6.10.26). Docs clave: proceso de 28-day closure follow-up (SharePoint Kristin) y SLA WIKI (https://trebuco.atlassian.net/wiki/spaces/RTS/pages/477582491649/Service+Level+Agreements). Sesión jun-10 (ciclo de vida y SLAs): notificaciones 7/14/28 días, Ticket Escalation, SRE, OpsGenie; docs de creación de tickets, linking, cambio de tipo de ticket, 28 day closure.

## Rutina diaria de cierres — completed, 28-day, backlog hygiene
_chunk 1186 · 2026-07-14 · fuente: kt-kristin-2026-07-14_

Rutina admin diaria de Kristin (pasa a Juan; ~10-20 tickets, "bueno mantenerlos alrededor de eso"):
1. COMPLETED → CLOSE: completed = Appriss terminó, solo falta validación del cliente; si el cliente responde, salta a work-in-progress y notifica al assignee. Barrido: leer lo último y decidir. "Customer says done" = cerrar sin más. Si el assignee prometió plazo ("lo cierro en 3 días hábiles"), honrar su timeline. Si hay RCA pendiente (outages), dejar unos días y preguntar a quien haga los RCA (hoy: Dean). Si dudas con cargas a prod, validar con el data engineer (ej. Vlad) antes de cerrar.
2. 28-DAY FORCED CLOSE (cambiará a 21): llega email con los cerrados a la fuerza → verificar que estaba bien cerrarlos. Si el cliente seguía esperando a su IT interno, reabrir CON nota del porqué y avisar al assignee ("¿reabrimos?"). Las notas del ticket casi siempre dicen si se puede quedar cerrado.
3. BACKLOG HYGIENE: en el backlog NUNCA debe haber tickets unassigned en estado distinto de under-X-review / waiting-on-engineering/delivery. Un "work in progress" sin assignee = anomalía → investigar (caso Best Buy: quedó así sin asignar; la clienta confirmó resuelto y se cerró directo).
4. AL RESOLVER: dos dropdowns obligatorios (si falta el segundo — "perform customer requested operation" — NO completa y te rebota). La resolución se escribe como INTERNAL NOTE en el ticket; no duplicarla en el bubble de cierre. Canned response útil: "ticket resuelto, pasa a completed, si no se necesita nada se cierra en una semana".
[Fuente: KT Kristin 2026-07-14 — meeting 65]

## T-075 User provisioning portal + T-096 notificaciones de migración/outage
_chunk 1098 · 2026-07-02 · fuente: KT Pair Tracker Kristin - Juan.xlsx_

T-075 "User provisioning playbook" (Process: Customer Interaction, live session 06.24.26, demo hecha). Doc: "Adding Organizations and Customers to Jira Portal". Cubre: agregar usuarios y organizaciones al portal Jira, y quién agrega usuarios a las aplicaciones (no es soporte para todo — hay dueños por aplicación). T-096 "Client migration / downtime notification process" (Q&A 06.24.26). Docs: "Maintenance Outage Notification Process", "Maintenance Notification Overview" (mapa del proceso) y "Maintenance or Outage Notice Process" (proceso en profundidad). Cubre el proceso de notificación a clientes de mantenimientos, outages y migraciones con downtime.

## Tiger Team — cadencia y método de Kristin
_chunk 1187 · 2026-07-14 · fuente: kt-kristin-2026-07-14_

Proceso que Juan vio en acción (2026-07-14; el doc del Tiger Team ya está en el knowledge share):
- Cada ~6 semanas (no mensual estricto), barrido del reporte buscando assignees con múltiples tickets viejos sin movimiento (sin respuesta a Teams o a @menciones).
- Por cada uno: email con su lista de tickets + LA ÚLTIMA NOTA de cada ticket (para que no tengan que pensar) — anoche envió la tanda con copia a Juan y Camila.
- Respuestas: por email o con @mención interna en el ticket (como hizo Zach). Si el assignee responde por fuera (ej. Marzen esperando a Honeywell), Kristin agrega ella misma la internal note al ticket — ayuda al assignee y deja rastro de que se revisó.
- Fin de mes: Excel de totales a Aimee (ella saca las métricas).
- Estado al 14-jul: Smeet se va al FINAL DE ESTA SEMANA (consiguió trabajo nuevo) y deja varios tickets que deben reasignarse; Sevda tiene 3 tickets desde abril en work-in-progress sin movimiento.
[Fuente: KT Kristin 2026-07-14 — meeting 65]

## Log cronológico de las 7 sesiones del KT
_chunk 1099 · 2026-07-02 · fuente: KT Pair Tracker Kristin - Juan.xlsx_

Sesión 1 (jun-4, 1.25h): Tickets and Contacts — básicos de ticket, creación, backlog. Sesión 2 (jun-5, 1h): APIs basics — login y ticket en curso; links de client list y wiki APIS. Sesión 3 (jun-9, 1h): tickets APIS y help email, tickets Retailit (linked issues); follow-up al cliente desde help@appriss en tickets "waiting for customer"; wiki de triaging. Sesión 4 (jun-10, 1h): ciclo de vida de tickets y SLAs — notificaciones 7/14/28 días, escalación, SRE, OpsGenie. Sesión 5 (jun-12, 1.25h): estados Completed/Closed de tickets RCS, Engage password reset y client set up, APIS start up process; action item: David configuraría su acceso en PROD y Prep. Sesión 6 (jun-16, 1h): ticket lifecycle con certificados/SSH keys por expirar, escalaciones L2→engineering, cuándo contactar clientes. Sesión 7 (jun-24, 1h): agregar usuarios/organizaciones al portal, quién agrega usuarios a aplicaciones, proceso de notificación de mantenimientos y outages.

## Cheat sheet de Kristin — aliases, SREs, trust portal y casos tipo
_chunk 1188 · 2026-07-14 · fuente: kt-kristin-2026-07-14_

Contenido de la cheat sheet que Kristin comparte (más piezas sueltas de la sesión 2026-07-14):
- ALIASES de productos (el cliente habla viejo): NetTrack = Incident (también LPMS); CAMS = Audit; Verify = Engage. También cómo habla la empresa: "Delivery team" = implementation.
- SREs ON-CALL: cubren zonas horarias; schedules en la herramienta on-call (secure → DevOps) con vistas EU y US — ahí está quién debe responderte HOY si posteas en Teams y nadie contesta. Dean publica el calendario del mes por email (screenshot y a mano). Juan entra a on-call el 17-jul.
- Team leads del día: si necesitas ayuda, suelen decir "asígnamelo a mí".
- TRUST PORTAL (página pública de la empresa): para clientes que piden los docs anuales de seguridad/pentest (DHL cada año, Kohl's empezó) — se les comparte el link y ellos solicitan los documentos ahí.
- Casos tipo: Dick's Sporting Goods abre ticket por "archivo faltante" → casi siempre timing, responder "recibido, ten paciencia, si no llega en X tiempo avísanos" y si de verdad falta, escalar a Payman (data ops; él tiene formato propio de tickets — está en la cheat sheet). Decommissioning ticket process → link en la cheat sheet.
- Truco para ubicar el equipo de alguien: abrir sus chats/Teams y ver con quién trabaja.
- Knowledge tracker de Kristin: está agregando también los links de las sesiones que hizo con David (mismo material, por si un tema se cubrió en distinta dirección).
- Docs del sign-off: Aimee subió algunos a Confluence; el resto queda a criterio de Juan+Camila (pueden quedarse como material del equipo sin publicar).
[Fuente: KT Kristin 2026-07-14 — meeting 65]

## Los 17 artifacts compartidos (docs y links)
_chunk 1100 · 2026-07-02 · fuente: KT Pair Tracker Kristin - Juan.xlsx_

Artifacts del KT (todos con columna "Signed off by" vacía — pendiente): 1. RCS Ticketing Triaging Process (06.6). 2. APIS AALPS — toda la documentación APIS en Confluence (6.5). 3. Client Contacts.xlsx — contactos de todos los clientes (6.5). 4. SRE Calendar — on-call schedules The Retail Equation (6.10). 5. SLA WIKI Doc (6.10, Confluence RTS/477582491649). 6. Changing Ticket Types (6.10). 7. Linking Tickets (6.10). 8. How to Create an RCS Ticket (6.10). 9. 28 Day RCS ticket closure process (6.10). 10. Completed Closed RCS Process (06.12). 11. APIS Start First Steps.docx (06.12). 12. Engage Password Reset Locked Out.docx (06.12). 13. How to set up Engage Portal user.docx (06.12). 14. Escalating to Engineering.docx (06.16). 15. Adding customers and organizations to Jira portal (06.24). 16. Maintenance Notification Overview (06.24). 17. Maintenance or Outage Notice Process (06.24).

## Guion del meet de sign-off con Kristin (checklist)
_chunk 1101 · 2026-07-02 · fuente: KT Pair Tracker Kristin - Juan.xlsx_

Objetivo del meet: revisar el tracker con Kristin y firmar el sign-off parcial (el shadow original, David, ya no está). Checklist por topic — Juan valida que puede ejecutar solo: T-034/T-084: sabe crear/linkear tickets APIS, dónde está el decision tree de acceso y permisos (wiki AALPS), y el access reference. T-035: sabe empaquetar una escalación a Engineering según el estándar (qué incluir antes de escalar). T-036: maneja SLAs (7/14/28 días), 28-day closure, cuándo entra SRE/OpsGenie. T-037: playbook de acceso/seguridad de top customers. T-075: puede agregar organizaciones/usuarios al portal Jira y sabe a quién dirigir user-adds por aplicación. T-096: puede ejecutar el proceso de notificación de mantenimiento/outage. Pendientes a levantar en el meet: (1) acceso PROD y Prep de APIS que iba a configurar David — verificar si Juan lo necesita y quién lo aprueba; (2) llenar "Signed off by" + "Sign off Date" en la hoja Artifacts; (3) completar KT End Date, Department y Goal en la portada del tracker; (4) confirmar canal para dudas post-KT con Kristin.

## Los 7 reflejos de troubleshooting APIS (conocimiento tácito del KT)
_chunk 1132 · 2026-07-09 · fuente: aspectos-clave.html §1_

Reflejos de diagnóstico que salieron de los demos EN VIVO del KT con Kristin, no de ninguna página de Confluence. Son la primera reacción ante casi cualquier ticket de APIS.

1) System Options = feature flags por cliente. El archivo "System Option List-Update this one.xlsx" es la lista maestra. La MAYORÍA de los "bugs" son solo una opción apagada para ese cliente. Primer lugar donde mirar.
2) Impersonation = método #1. Entra COMO el usuario que reporta para ver sus permisos, su vista y su jerarquía reales. Resuelve casi todos los "yo no veo esto".
3) Location hierarchy = scoping de permisos. "No veo el incidente / el reporte" casi siempre es jerarquía mal asignada, no un bug del sistema.
4) Label cache reset. Si cambias etiquetas de pantalla y no aparecen, resetea el label cache. Síntoma clásico de "ya lo cambié y no se ve".
5) 270 vs 275 = misma data, otra UI; toggle por usuario/cliente. 270 clásica/pesada, 275 renovada. Confirma en qué versión está el cliente ANTES de diagnosticar.
6) ⚠ ALERTA: en admin → Users → Edit las contraseñas se muestran en TEXTO PLANO. Nunca compartir pantalla en esa vista durante una llamada con cliente.
7) AdHoc reports = priorizar por Last Run Date. La UI no tiene spinner: si no pasa nada, ya está corriendo, no re-clickees.

Riesgo de continuidad: estos 7 reflejos no están escritos en ninguna página; solo existieron en los demos. Acción acordada: redactar la "APIS Survival Guide" (Juan autor, Kristin reviewer) en AALPS antes de que salga Kristin. El respaldo concreto del reflejo #1 es promover el archivo System Option List a §4 del hub.

## SLA deep-dive (wiki RTS, vigente abr-2026): estándar vs ICA/TJX
_chunk 1102 · 2026-07-02 · fuente: Confluence RTS/477582491649 + RTS/476545810442_

De la página "Service Level Agreements" (Confluence RTS 477582491649, autora Aimee Wadsworth, actualizada abr-2026): Support maneja DOS sets de SLA — RCS ticket SLA y Uptime SLA. NO hay SLA para data loads. Todos los clientes están en estructura estándar EXCEPTO TJX e ICA, que tienen cláusulas de penalidad financiera en contrato. Los SLAs se estandarizaron en Jira para reporting; si un cliente pide reportes de SLA → escalar a Support Management. Uptime SLA público: apprissretail.com/service-availability-schedule. Proceso ICA (efectivo jun-2025): los Secure EBR Core Work Items deben estar disponibles cada día a las 8am CET; si no están y no se resuelve en 1 hora = 1 delay; 2+ delays en un mes calendario → service credits (% del MRR según tabla). Operación diaria: monitorear proyectos RTS y RCS con el dashboard Jira "ICA Missed Work Item Loads" (id 23940); si el ticket se resolvió antes de 9am CET → label SLA_Checked; si no (y no fue culpa del cliente) → labels SLA_Checked + ICAmissed (alimenta PowerBI de penalidades). Contexto de investigación en canales Teams "Secure 5 Issues" y "Secure 5 Outage". La página de TJX (476218785811) devuelve 404 sin permisos — verificar acceso.

## APIS: qué es + runbook de feed errors + ALERTA de docs desactualizados
_chunk 1103 · 2026-07-02 · fuente: Confluence AALPS/273453096 + AALPS/294198150_

APIS = Asset Protection Information System: case management para Loss Prevention / Risk, con módulo de auditoría (forms + reports). La wiki AALPS "APIS" (273453096) que respalda los topics T-034/T-037/T-084 del KT es un índice de ago-2021 con autora desactivada (Julie Barber) y links a dominios viejos (wiki.appriss.com, jira.appriss.com, SharePoint apprisscloud) — probablemente rotos. Su única subpágina útil: "APIS Feed Error Documentation" (sep-2021), runbook real de feed failures: (1) llega email de feed failure con feed+cliente en el subject; (2) login a Azure Portal con usuario propio (NO LDAP); (3) entrar al ETL server P-APIS-ETL01 con credenciales "Apis prod EVD Feeds" del vault GSOC en 1Password; (4) share Azure retailalpprod.file.core.windows.net/apis-prod-evd/Feeds → carpeta del cliente → Data Directory → feed; (5) revisar clientyymm.log primero, luego client_feed.log; (6) para re-run: share p-ingest-fsla4/DLZ/<cliente>/Prod, restaurar archivo desde Archive/Prod/YYYY/MM/DD si falta, y correr el scheduled task del feed en el ETL server; (7) si requiere dev: ticket AALPS asignado a Lawrence Kim (o story de Import/Export a Matt Kaminga) — nombres de 2021, confirmar si siguen vigentes; (8) cierre manual: Resolved + "SYS Followed Support Process". PREGUNTA CLAVE para Kristin en el sign-off: ¿cuál es la fuente de verdad ACTUAL de APIS — esta wiki de 2021 o los docs de su SharePoint personal? ¿Siguen vigentes los assignees y el proceso GSOC?

## Sign-off meet con Kristin (2026-07-02) — resultados y accesos
_chunk 1119 · 2026-07-02 · fuente: meet-signoff-2026-07-02_

El meet de sign-off del KT se realizó el 2-jul-2026. Resultados: (1) ACCESO PREP: usuario JMARTINEZ creado en vivo en J.Crew Prep — Prep se identifica por "UAT" en la URL y sufijo "-prep" en el company ID; posible bloqueo Cloudflare en primer login (reportar a IT si pasa). (2) ACCESO PROD: vía la cuenta de Julie Barber que sigue activa; credenciales compartidas por Kristin (guardadas en nota segura, no en texto plano). (3) Kristin confirmó que sale de la empresa ("They're firing me anyway") — sus documentos viven en su OneDrive personal (trebu-my.sharepoint.com): riesgo de continuidad idéntico al de Julie Barber. Pedirle ANTES de su salida: export de docs a espacio compartido, cheat sheet Prod-vs-Prep, Client Contacts.xlsx en ubicación compartida, template de notificaciones. (4) Demo en vivo cubrió: impersonation como método #1 de troubleshooting, system options como feature flags por cliente, versiones 270 (clásica/clunky) vs 275 (renovada) toggle por usuario, location hierarchy como scoping de permisos, label cache reset, triage de AdHoc reports por Last Run Date, y ALERTA: admin→Users→Edit muestra passwords en claro — nunca compartir pantalla en esa vista. (5) Deliverable acordado: "APIS Survival Guide" redactada por Juan con Kristin como reviewer antes de su salida.

## Auditoría documental APIS/AALPS (2026-07-02) — capas, gaps y plan
_chunk 1120 · 2026-07-02 · fuente: apis-doc-audit-2026-07-02_

Investigación completa del espacio AALPS (98 páginas). VEREDICTO: dos capas — capa 2021 muerta (índice APIS 273453096 con 2 de 3 links rotos y manual admin en OneDrive personal de Julie Barber desactivada; Training docs 273452949 vacía; feed runbook 294198150 con assignee Lawrence Kim y jira.appriss.com obsoletos) y capa viva de Ryan Barlow/Matt Kamminga (Customer Server Profile 474658570288 actualizada 30-jun-2026 con matriz de 11 nodos node-f…node-n/AUS/EU/CA, pares pd-lpms-iis + pd-lpms-iz, Walmart casi dedicado en node-n, leyenda: * = DB-only migration usa platform DB no lpguys, ** = unification login NO usar lpguys; RCS Queue 474926907395 con el triage: cola AALPS engineering tickets → ownership → Shan/Mission Control para bugs, Sholan Narine/Jon Ross para features, Ryan Barlow para data imports; SLA Labels 474845282319: source:RCS dispara due date por prioridad, reglas 9am EST etiquetan SLA:Met/SLA:Exceeded, métricas por mes del due date). GAPS críticos: sin runbook de acceso, conocimiento operativo (impersonation/system options/jerarquías/label cache) sin escribir, docs de las dos SME salientes en OneDrive personales. La leyenda de migración explica el patrón Tahoe Donner RCS-27573 (tablas faltantes en platform DB que existían en lpguys). PLAN: survival guide en AALPS (Juan autor, Kristin reviewer), actualizar feed runbook (Matt Kamminga, trebuco.atlassian.net), banner deprecated en páginas 2021, columna versión 270/275 en la matriz. Documento completo: ~/Desktop/moscu-ops/APIS-doc-audit.md

## KT Pair Tracker (xlsx real, 2-jul-2026) — artifacts, links y riesgo de continuidad
_chunk 1125 · 2026-07-07 · fuente: ~/Downloads/KT Pair Tracker Kristin - Juan.xlsx_

Copia descargada del "KT Pair Tracker Kristin - Juan.xlsx" (4 hojas: Our KT Space, Topics, Sessions, Artifacts). Kristin Krogman (Sr. Business Process Analyst, kkrogman@apprissretail.com) ↔ Juan Martinez (Lead Support Engineer). Estado: 7/7 topics Completed; sign-off SIN registrar (columnas "Signed of by" y "Sign off Date" VACÍAS en las 18 filas); portada con KT End Date, Department y Goal aún en placeholder.

RIESGO DE CONTINUIDAD #1 — docs SOLO en el OneDrive PERSONAL de Kristin (kkrogman_trebu_co, mueren cuando salga, igual que ya pasó con Julie Barber): Creating Ticket link / Changing Ticket Types, How to open a ticket (Create RCS), Linking Tickets, 28 Day RCS closure, Completed/Closed RCS process, APIS Start First Steps, Engage Password Reset (Locked Out), How to set up Engage Portal user, Escalating to Engineering. ACCIÓN: copiarlos al sitio compartido RetailSupport o a Confluence AALPS/RTS antes de su último día.

YA en ubicación SEGURA (compartida): Client Contacts.xlsx está en trebu.sharepoint.com/:x:/s/RetailSupport/ (sitio compartido, NO personal). Wikis en trebuco.atlassian.net (Confluence): RCS triaging 357465227677; APIS-AALPS 273453096 (índice muerto 2021); SLA 477582491649; Adding customers/orgs al portal 357465358603; Maintenance Notification Overview (whiteboard) 476153348117; Maintenance or Outage Notice Process 475931901982. SRE on-call: trebuco.atlassian.net/jira/ops/who-is-on-call.

Topics (todos Completed): T-034 APIs+User Provisioning+Access ref (6.10, live); T-035 Eng escalation packaging (6.16, live, Escalating to Engineering.docx); T-036 Cross-product map (6.10, shadow; 28-day + SLA wiki); T-037 Top-customer access/security (6.16, doc review, wiki APIS); T-075 User provisioning portal (6.24, live, Adding orgs/customers); T-084 Decision tree API access+permissions (6.16, video, wiki APIS); T-096 Client migration/downtime notification (6.24, Q&A).

CORRECCIÓN a notas previas: Engage SÍ se cubrió parcialmente (artifacts 12/13: Password Reset + Person Set Up). Client Contacts NO está en OneDrive personal sino en el sitio compartido RetailSupport.

## Matriz de enrutamiento y ownership (KT Kristin 28-jul, meeting M84)
_chunk 1408 · 2026-07-28_

Handoff de Kristin (sale 31-jul) a Camila+Juan. Enrutamiento por producto y reglas de metadata/comunicación.

ENGAGE (el L2 nunca trabajó Engage):
- Claims / "claims to void" / gaps-claims-void -> Marissa Johnson (Solution Expert). Asignar manual, poner Under Solution Expert Review, nota al cliente "moved to our solution expert team". Mensaje directo opcional (ella es buena viendolos).
- Engage roto (fix de codigo) -> ingenieros Shirude e Ian. Ian es lead pero pidio EMPEZAR por Shirude (ella triangula: lo tomo / no es mi equipo).
- Engage migro "a la plataforma" -> algunas cosas ahora las arregla el equipo Secure 5 -> preguntar.
- TJX Engage usa "the shell" (portal distinto) -> Engineering -> Tom Duncan (lead grupo RTIAS, en EU). Claims/insights TJX -> Marissa.
- Consumer ID / identity linking / quejas de consumidor -> empezar con Andrea (consumer complaints); si roto -> Shirude/Ian.
- Insights (antes Engage Analytics) -> VP Kenny Vu -> Ian -> Shirude/Hal.
- Incident + Audit -> Jim DeJohn (lead Solution Experts); si no esta -> Dan Orquist.
- EBR US -> Kristin Dyer / Kelly.
- Profile history que no carga hacia atras (2024) -> preguntar a Marissa.

RTS (proactivos por alerta): L1 (pre-support) los ve primero; si necesitan ayuda postean en canal "please L2 pick it up". RTS engine tipicamente va directo a Engineering.

METADATA/TAXONOMIA: Solo poner Team Ownership + Sprint si es DATA ticket. Data -> ownership Support-Delivery; en Sprint escribir "support". Label "data" SIEMPRE en data tickets (Peyman arma su dashboard con esos labels para asignar).

COMUNICACION: No abusar de @menciones en Teams (interrumpe). Kristin usa EMAIL ("confirmar que el ticket esta en la cola") que leen en la manana. EU (Tom Duncan) fuera de horario: no pingear si no es high. SLA a punto de romper: tomar el ticket y postear en el canal PRIORITY del grupo.

BACKLOG GROOMING: Tickets viejos no asignados a nuestro equipo inflan nuestros numeros -> mover fuera o cerrar (se crea uno nuevo). SOW / feature request -> Under CSM Review, asignar al CSM (ej. Colleen) con nota interna "please see Matt comments"; el CSM aclara con el cliente.

ACCESO ENGAGE: Juan y Camila no tenian permisos. Kristin abrio ticket con help desk para igualar sus permisos a los de ella; Jr. lo aprobo, deberia quedar antes del jueves.

Escalacion Engage general: Solution Expert (do-work) = Marissa; fix = Shirude/Ian; lead SE = Jim DeJohn.

## Prep meet APIS reorg con Kristin (2026-07-09) — 4 puntos + agenda de valor
_chunk 1126 · 2026-07-09 · fuente: ~/Desktop/apis-reorg/_

Reunión de HOY para caminar con Kristin la reestructuración de la página APIS (AALPS/273453096) antes de su salida. La página viva sigue firmada por Julie Barber (desactivada), última edición ago-2021, con el manual admin apuntando al OneDrive de jbarber y el feed runbook a wiki.appriss.com (muerto).

LOS 4 PUNTOS QUE KRISTIN PIDIÓ ACLARAR (con respuesta ya lista):
(1) APIS Admin Customer Support Manual — está en el OneDrive de JULIE (jbarber), NO de Kristin; probablemente perdido. Preguntar: ¿tienes copia local? Prioridad mayor: rescatar los 9 docs de proceso del OneDrive PERSONAL de Kristin (mueren cuando salga).
(2) Ruta de acceso PROD — YA resuelto el 2-jul: se entra por la cuenta aún activa de Julie Barber (creds compartidas). No re-preguntar. El desbloqueo real: ¿quién es el application owner de APIS que aprovisiona una cuenta PROD propia? (por T-075 hay dueños por aplicación).
(3) Feed-error runbook — el proceso sigue válido (email failure → Azure Portal usuario propio NO LDAP → P-APIS-ETL01 vault GSOC 1Password → logs clientyymm.log/client_feed.log → re-run scheduled task). Desactualizado: assignees Lawrence Kim / Matt Kamminga y jira.appriss.com. Confirmar assignees + vault + que Matt Kamminga lo actualice en trebuco.
(4) Mapeo de clientes 270/275 — NO existe documentado en ningún lado. La matriz viva Customer Server Profile (474658570288, Barlow/Kamminga, act. 30-jun-2026, 11 nodos) NO tiene columna de versión. Propuesta: agregar columna 270/275 a esa matriz viva. Este es el mayor gancho de valor.

3 RESULTADOS A AMARRAR HOY: (a) rescate de los 9 docs de OneDrive de Kristin al sitio compartido RetailSupport/Confluence AALPS-RTS antes de su último día; (b) nombre del application-owner que aprovisiona cuentas PROD reales; (c) firmar el sign-off del tracker (columnas Signed off by / Sign off Date VACÍAS en las 18 filas pese a 7/7 topics Completed) + completar portada (End Date/Department/Goal).

## Artefactos de prep APIS (2026-07-09) — index.html corregido + aspectos-clave.html
_chunk 1127 · 2026-07-09 · fuente: ~/Desktop/apis-reorg/_

Dos documentos HTML locales en ~/Desktop/apis-reorg/ (servir con `python3 -m http.server 8080`, no doble-clic; los diagramas necesitan http).

1) index.html — REVISIÓN DE ESTRUCTURA (para caminar con Kristin). Inventario real de los 41 docs de la página APIS mapeados 5 cajones → 9 secciones con dueño, con acción por archivo (keep/remove/update/investigate/restrict), drafts de texto propuesto, tabla de migración de los docs de OneDrive, y 8 preguntas de validación con checkbox. Correcciones aplicadas hoy: Q7 acceso PROD ahora pregunta por el application owner (no re-pregunta lo ya resuelto); Q5 aclara que el manual admin es de Julie no de Kristin; nuevo bloque §8 propone la columna 270/275 sobre la matriz Customer Server Profile.

2) aspectos-clave.html — REPASO GENERAL + MAPA DE FLUJOS (el que Kristin recomendó). Contiene: los 7 reflejos de troubleshooting (system options=feature flags, impersonation=método #1, location hierarchy=permisos, label cache reset, 270 vs 275, ALERTA passwords en claro en Users→Edit, AdHoc por Last Run Date); qué es APIS + 270/275; las dos capas de docs (muerta 2021 vs viva 2026 con IDs); cadenas de acceso (Prep JMARTINEZ ok / Prod frágil vía Julie / cuenta propia pendiente); registro de 5 riesgos con acción. Tres diagramas mermaid: (D1) operación APIS + feed runbook end-to-end; (D2) ticket lifecycle L1→L2→L3 + ownership cola AALPS + SLA con caso ICA/TJX; (D3) ANTES vs DESPUÉS de la estructura documental con las 5 propuestas.

Fuente de datos: auditoría del espacio AALPS (98 páginas, doc completo en ~/Desktop/moscu-ops/APIS-doc-audit.md) + KT Pair Tracker real + chunks del folder 21.

## Clientes APIS — lista oficial con hosting, contactos, IDs y migración (jul-2026)
_chunk 1142 · 2026-07-09_

Fuente: Client Contacts.xlsx, tab "APIS Outage List" (mantenido por Kristin/Aimee; documento INTERNO-ONLY, nunca compartir fuera).

CLIENTES APIS ACTIVOS (15):
- 7-ELEVEN — hosted — MIGRA A INCIDENT ~sep/oct 2026 — IDs: 7eleven / 7-eleven-prep — contactos: vinh.luong@7-11.com, brent.smerczynski@7-11.com, garry.kortz@7-11.com — CSM: Bryant McAnnally
- ACADEMY SPORTS + OUTDOORS — hosted — migración a Incident in progress — IDs: academy / academy-prep — CSM: Shelley Cameron
- CLAIRE'S STORES (US) — hosted — migración in progress — IDs: claires-live / claires-prep — beth.jeske@claires.com
- CLAIRE'S UK — hosted — URL DISTINTA: https://apisuk.apprissretailcloud.com — IDs: claires-uk / clairesuk-prep — richie.clements@claires.co.uk
- JCREW — hosted — migración in progress — IDs: Jcrew / jcrew-prep
- AAFES (Army & Air Force Exchange) — ON-PREM, gobierno — solo exchange-prep — NO migra por ahora — CSM: Rae Hatfield
- NEXCOM (Navy Exchange) — ON-PREM, gobierno — demo de Incident hecha + RFP — sin acceso a su data (solo prep site nexcom-prep) — CSM: Rae Hatfield
- LOWES FOODS — on-prem — lowes-prep — CSM: Colleen
- NORTH CAROLINA EDUCATION LOTTERY — hosted — ncel / ncel-prep
- SIX FLAGS — hosted — sixflags / sixflags-prep
- TAPESTRY (ex Coach) — hosted — data extract request RCS-22729
- TIFFANY AND CO. — on-prem — Tiffany-prep
- VICTRA — hosted — Victra
- WWE — hosted — wwe / wwe-prep (último login feb-2026)
- COLLEEN KNOBLOCK es la CSM de la mayoría de clientes APIS (Kristin le dio follow-up por email 5.27 y 6.4, sin respuesta; reenvía jul-09).

SUNSET APIS: rumor de cierre a fin de 2026; Kristin escéptica — AAFES/NEXCOM son entidades de gobierno y no se pueden "apagar". Hace 5 años le dijeron que APIS duraría 6 meses.

## Workflow RCS definitivo — matriz assign/unassign por equipo y tickets linkeados
_chunk 1143 · 2026-07-09_

Confirmado por Kristin en vivo (2026-07-09), con ejemplos reales en Jira.

MATRIZ AL ESCALAR UN TICKET RCS (dropdown de status + asignación):
- Engineering → under engineering review + UNASSIGN (su lead lo asigna desde su dashboard)
- Delivery/Implementation → under delivery review + UNASSIGN (Carl Costello es lead en Europa; CCTV y SSO son de su grupo; disponible hasta ~11-12 CT)
- CSM (SOW / change request) → asignar a su cola + UNASSIGN (si sabes qué CSM es, asígnaselo directo)
- Customer review → KEEP
- Infrastructure → KEEP: se crea un ticket Retail IT linkeado al RCS; infra trabaja su ticket, sus notas aparecen en tu RCS como internal note; TÚ comunicas al cliente y cierras
- Database Services → KEEP (mismo patrón, ticket DBA Services linkeado; poco frecuentes)
- Security/InfoSec → KEEP (ticket CISS linkeado)
- Product management → UNASSIGN
- Solution expert → no se usa

REGLAS: Incident = break-fix, NUNCA al CSM. SOW = solución >2h, la aprueba el CSM. Duplicados: tomar el segundo ticket, avisar al cliente con el nº del original, linkear como duplicate y añadirlo como requested participant al original.

JIRA/PORTAL: Requested participants = donde vive el CSM del ticket + contactos del cliente que reciben alertas (con acceso al portal ven cualquier ticket de su org aunque no reciban alertas). Customers → buscar cliente → view all = tickets abiertos por el cliente (los internos ocultos requieren reporte). Cambiar tipo de ticket: click al tipo → dropdown → next → saltar página 2 → confirm. Cambiar reporter: permitido, dejar nota interna explicando. Activity → History: auditoría de quién movió/asignó cada paso (herramienta clave para training y para ubicar en qué equipo está alguien). Campo sentiment: automático y abandonado — ignorar.

ALTA PRIORIDAD: L1 postea criticals/high en el canal de priorities y en Retail Apps; si el ticket llega sin info, pedir screenshot/URL al reporter ANTES de que alguien lo tome (sin asignártelo). Canales a watchear: incident, Appriss, legacy products, Engage, data issues (Peyman).

## KT Pair Tracker — links y artefactos compartidos por Kristin (SharePoint/Confluence)
_chunk 1144 · 2026-07-09_

Fuente: KT Pair Tracker Kristin - Juan-2.xlsx (7 topics completados, sign-off pendiente).

LINKS CLAVE:
- Creating/Linking Tickets: https://trebu-my.sharepoint.com/:w:/g/personal/kkrogman_trebu_co/IQBdRYFtDdi6QYtWjPYst_RFAblRUAIfTOvc0GffA-c932k
- How to open a ticket: https://trebu-my.sharepoint.com/:w:/g/personal/kkrogman_trebu_co/IQAU9D8mLyDcRaIOPhJ3atluAQECq8GplKUSy4pNB0nsxHk
- 28 day closure follow-up: https://trebu-my.sharepoint.com/:w:/g/personal/kkrogman_trebu_co/IQCWqWCry_pzR7h0H6LEtk8XASNGxYRs6kmjRGAaVPsJJsw
- SLA WIKI: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/477582491649/Service+Level+Agreements
- APIS AALPS (toda la doc APIS): https://trebuco.atlassian.net/wiki/spaces/AALPS/pages/273453096/APIS

ARTEFACTOS COMPARTIDOS (docs Word de Kristin): RCS Ticketing Triaging Process · SRE Calendar (OpsGenie on-call) · Changing Ticket Types · Linking Ticket Process · How to Create an RCS Ticket · 28 Day RCS closure · Completed Closed RCS Process · APIS Start First Steps.docx · Engage Password Reset Locked Out.docx · How to set up Engage Portal user.docx · Escalating to Engineering.docx · Adding customers and organizations to Jira portal · Maintenance Notification Overview · Maintenance or Outage Notice Process · Client Contacts.xlsx

CONTINUIDAD: Kristin junta sus docs en UNA carpeta de su OneDrive para compartirla completa antes de irse (plan original con David); los docs aprobados irán a Confluence; también linkea cada doc en el chat del screen-share. Su último día: viernes 31 de julio de 2026. Pedirle el Appriss Admin Customer Super Manual (lo tiene descargado en su desktop, no está accesible vía el drive de Julie Barber).

## KT Kristin 22-jul — Triage y etiquetado de tickets (shadowing en vivo)
_chunk 1371 · 2026-07-22_

Sesión de shadowing (1h40) con Kristin Krogman revisando y etiquetando ~20 tickets de la cola RCS uno por uno. Contexto: Juan asignó los tickets en la mañana; Kristin guía el triage. Kristin sale de Appriss el 31-jul.

REGLA DE ORO (Kristin): lo más importante es que el ticket llegue a alguien que pueda trabajarlo para el cliente. Los labels son para reporting y métricas — importantes, pero secundarios. Un error de tipo no es el fin del mundo: se puede revertir.

TICKETS DE DATA (van al Support Data Team, el equipo de Peyman):
- Label: Support_Data_Team (campo Labels, en Details).
- Team Ownership = "Support Delivery" (Delivery department).
- Sprint = "RCS Support Team" (escribir "support" y autocompleta).
- Así es como Peyman encuentra sus tickets en su dashboard; es petición suya y filtra por esos labels.
- Team Ownership + Sprint SOLO se ponen si el ticket va al equipo de datos/pagos. Si va a Delivery u otro equipo, NO se ponen.

TIPOS DE TICKET:
- Incident = break/fix (algo funcionaba y se rompió).
- Change Request (SOW / SOW Estimation) = el cliente pide algo, hace una pregunta o pide un cambio; no es un break. Regla de Aimee: si el cliente está preguntando/pidiendo → SOW/Change Request, no Incident.
- Cambiar el tipo: icono del tipo junto al número de ticket (recuadro amarillo) → dropdown → elegir Change Request / SOW Estimation → saltar la 2ª pantalla → Confirm. Una automatización cambia el request type solo; no hay que tocar nada más. Se puede revertir a Incident si resulta que sí estaba roto.
- New Feature: si el cliente pide función nueva, va por Pendo (proceso aparte), no como ticket normal.

CAMPO "PROBLEM" (categoría en el cuerpo del ticket): casi nunca debe quedar "Other". Reclasificar a "Data" (u otro) según corresponda. Muy rara vez algo es legítimamente Other.

IDENTIFICACIÓN DE CLIENTE / ORGANIZACIÓN:
- Algunos clientes tienen otro nombre: KFC = organización "Yum Brands" (Yum es la matriz; KFC y Taco Bell están debajo). Verlo en el campo Organization del cuerpo del ticket.
- Ubicación (US/EU/CA/AU): validar en el Client Listing / contact sheet. Yum Brands = EU. Importa para saber a quién y cómo escalar.
- Campo "Export to Power BI" (arriba): a veces hay que anteponer el nombre de la org, ej. "TJX-" delante del valor, para identificar la compañía en reportes. Guardar con el check.

DUPLICADOS (ej. RCS-27906 original vs RCS-27907 duplicado, PSEB credit card numbers):
- Confirmar que son el mismo issue.
- Link work item → "Duplicates" → poner el otro RCS (con prefijo RCS-).
- Mantener abierto el ORIGINAL (el que abrió el cliente/Roseanne).
- Nota interna en el original: "linked 27907, opened as duplicate".
- En el duplicado: transición a "Duplicate" (al fondo del dropdown de estado) y Reply to customer (NO nota interna): "This ticket was opened as a duplicate to your high-priority ticket RCS-27906. Please continue to work on the original ticket." Así sale de la cola y no cuenta contra reporting.

REASIGNACIÓN entre personas: si hay que intercambiar tickets (ej. acceso a SnowTime que solo tiene una persona configurado localmente), está bien reasignar; avisar por Teams a la persona ("este ticket ahora es tuyo").

CASOS CONCRETOS:
- Nordstrom RCS-27928 (Sarah armando aggregation search / campo no aparece): no se sabe si está roto o nunca estuvo disponible → Change Request (puede volver a Incident si resulta roto). Label data.
- KFC/Yum (data discrepancy, high-value tender, cash kiosk, montos no coinciden) → data, Support_Data_Team, cliente EU.
- Ticket de Gulshan (monitor/index no corre, Secure 3.4, parece infra): el equipo aún no tiene ese conocimiento; escalar a Vlad Bogus, Matt Everett o Carlos Jacinto (equipo de Polonia).
- Ticket de feature roto que NO es data → equipo de Carl (implementation): solo triage + comentario interno, sin labels de data.
- BUG DE AUTOMATIZACIÓN: al asignar a Edwin Garzón, una automatización de Jira quitó el label Support_Data_Team (lo dejó en "none") en 3 tickets (…21, …32, …34). Acción: screenshot del History + escribir a Austin Flannery (Jr. IT) preguntando por qué la automatización lo removió, notando que solo pasó en tickets asignados a Edwin.

WALMART (usuario no está en el portal): Walmart no quiere que empleados de tienda abran tickets; deben ir por sus administradores. Flujo Kristin: 1) responder a L1 "I'll take care of it" para que sepan que lo tomaste; 2) responder al cliente (Josh) pegando la info del cheat-sheet de Walmart ("this information has been supplied to us by Walmart's admins…"); 3) si vuelven sin respuesta, añadir al application administrator. Kristin mantiene un cheat-sheet (Walmart, Asda, Aurora, etc.) que ofreció compartir.

DASHBOARD DE LA COLA: Dashboards (izquierda) → Support Dashboard → esperar → scroll → "Support Open tickets" muestra lo asignado a cada persona por colores.

PENDIENTE: Juan debe firmar/revisar los documentos de KT de Kristin y avisar a JR que están OK antes de que JR los firme (sign-off del KT).

## Acceso al portal por email — pedir permiso al admin (caso Kimberly Baney, 22-jul)
_chunk 1374 · 2026-07-22_

Reunión corta con Kristin (meeting 81) mostrando el flujo cuando un usuario escribe pidiendo ayuda pero NO está en el Customer Ticketing Portal.

PROCEDIMIENTO (caso Kimberly Baney):
- No agregar a la persona de una. Reenviar su email al application administrator del cliente (ej. Ronald) preguntando si esa persona debe tener acceso al portal: "we're happy to add her, we just need your permission".
- Copiar al CSM (ej. Colleen) en ese email.
- Esperar la respuesta del admin; los siguientes pasos dependen de lo que diga.

REGLA DE DECISIÓN (down vs. trouble):
- Si la aplicación estuviera COMPLETAMENTE caída: agregar a la persona de inmediato (dar acceso) y resolver después quién debe tenerlo.
- Si la persona TIENE acceso y solo está teniendo problemas para llegar a algo (este caso): seguir el proceso — confirmar con el admin antes de agregar.

CONTEXTO / FILOSOFÍA:
- El objetivo es forzar a los clientes a abrir tickets en el portal. Si mandan emails sueltos, se pierden.
- Kristin quiere que Juan maneje estas solicitudes de aquí en adelante (es más rápido cuando ellos no están disponibles).
- Kristin ofreció darle a Juan el borrador del email para que él lo envíe, o añadirlo al hilo, como prefiera.
- Nota: este tipo de solicitudes "está llegando mucho" últimamente.

Relacionado: sección 11 (inbox help@appriss) y 12 (administración del portal) de la guía de KT; regla general de redirigir al application administrator.

## Crear ticket de punta a punta + link interno vs cliente (Easy Corp / Kimberly Baney, RCS-27930, 22-jul)
_chunk 1375 · 2026-07-22_

Corrida completa hecha por Juan con Kristin mirando (sesión en vivo 22-jul). Ticket RCS-27930, cliente Easy Corp (organización "EZ Corp" en el portal), issue "unable to edit a case".

Pasos:
1. Crear el Incident. Summary = compañía, guion, issue: "Easy Corp - Unable to edit case". Copiar las palabras exactas del cliente en la descripción y pegar el screenshot también en la descripción.
2. Priority Medium para arrancar.
3. Workaround del reporter: si el solicitante NO está en el portal todavía, abrir el ticket con uno mismo como reporter y cambiar el reporter al cliente recién DESPUÉS de agregarlo al portal. Si ya está en el portal, se pone como reporter desde el arranque.
4. Al seleccionar la organización, los requested participants se ponen solos y el CSM (Colleen) aparece por su cuenta como CSM.
5. Avisar en DOS emails: (a) reply-all en el hilo original para que todos vean que se abrió un ticket en su nombre y que va un invite al portal; (b) email aparte solo al cliente con las instrucciones de acceso (asunto: "Appriss Retail Customer Support ticketing portal access information").
6. Agregar al portal: Jr. > Customers > Organizations > escribir "EZ" para que salga EZ Corp > Add Customer > email > OK. Queda invitada (tarda un minuto, a veces refrescar).
7. Poner como reporter: en el ticket, campo reporter, escribir "Kim". Gotcha de escritura: el apellido es "Banee" (no Baney). Refrescar el ticket si el nombre no aparece a la primera.

REGLA link interno vs link de cliente (importante): un ticket tiene dos links y no son intercambiables.
- Link interno: muestra todo, comentarios internos y externos. Se manda solo a gente interna.
- Link de cliente: es la vista que ve el cliente al entrar al portal. Al mandarle un link al cliente, se saca de esa vista de cliente, NUNCA el link interno de Jira. Mandar el interno expone las notas internas.

Si el cliente pega contra un error después de ser agregado (Kimberly recibió un mensaje en el primer login): disculparse en la respuesta a su email, que pruebe con el link de cliente al ticket, y darle la URL del portal. Si sigue, ir a next steps.

## Canales de Teams que hay que tener visibles (en vivo con Kristin, 22-jul)
_chunk 1376 · 2026-07-22_

En palabras de Kristin, estos canales van a ser tu mejor amigo. El acceso ya existe pero los canales pueden no mostrarse: hay que entrar a "ver más canales" y poner los ocultos en mostrar, no aparecen solos. Nadie avisa de esto en el onboarding. Los que hay que vigilar, todos bajo Retail Ops:
- AALPS issues, Data issues, Legacy and security issues, Engage issues: acá aparece de todo, en todos los productos.
- Priority issues channel: era el grupo actual de L2. Camila y Juan probablemente tengan el suyo o Aimee desbloquee este. Es también donde se postea un ticket high-priority para que el equipo lo tome y le mande una nota al cliente ("recibimos tu high priority, estamos triaging", luego "tu ticket pasó al equipo de Delivery", etc.).
- R&D channel (2026 Engage size, alpha y beta): tiene lo de Snowflake y la platform unification, que sigue en curso. Camila y Juan tienen que vigilar este.
- Canal de SnowTime / Snowflake: también se mandan comunicaciones para estos.

## Cruce de producto, self-service del portal, release y pendientes (call Kristin 22-jul)
_chunk 1377 · 2026-07-22_

Cruce de producto vía la persona que ya lo trabaja (ejemplo Ryan Barlow, 22-jul): mientras se creaba el ticket de Easy Corp, entró un error muy parecido al high-priority channel desde Secure Audit ("no puede ver ni editar un caso sin importar quién lo asignó", ingresando safety meeting notes). Ryan Barlow (Delivery) ya trabajaba en uno similar, así que Kristin le escribió directo en vez de triagear a ciegas. Lógica: avisarle a quien ya está en el tema porque puede ser un issue más grande en todos los productos de incident. Si es el mismo, se linkean los tickets; si es distinto, vuelve al triage normal.

Búsqueda self-service del cliente en el portal: una vez adentro, el cliente puede buscar sus propias respuestas. "release" saca los release notices; "calendar" o "schedule" lleva al release calendar; los artículos how-to enlazan a la wiki, GitBook o user guides. Útil para saber a dónde apuntar al cliente.

Detalle de release (vista en vivo de Kristin): la próxima semana releasean tanto incident como secure; secure siempre va el segundo día, miércoles y jueves. Importa porque los tickets se reasignan al assignee original cuando sale un bug fix, para que lo testee y le diga al cliente que valide de su lado.

Por qué pedir permiso al admin antes de agregar a alguien al portal (Kristin): no toda empresa quiere ciertas personas viendo cada ticket; muchas veces es control sobre con quién nos comunicamos. Otras dicen "el que sea". En cualquier caso se sigue el proceso, para forzar a los clientes a abrir tickets en el portal.

Pendientes del 22-jul: (1) Acceso de Juan al portal Engage/Verify sin confirmar; Kristin contacta a Marissa (o Nicole, que trabaja con Marissa) para los permisos. (2) Help inbox help@appriss: Juan tiene acceso pero no aparece configurado en su Outlook; falta hacer que el inbox compartido se muestre (dropdown debajo del nombre / favoritos).

## Cheat sheet Kristin — Ruteo por cliente (a quién redirigir cada cliente)
_chunk 1378 · 2026-07-22_

Directorio operativo de Kristin (armado con años). La mayoría de estos clientes NO se agregan al portal: se los reenvía a su admin o buzón.

TJX: app admins chris_moore@tjx.com (Chris Moore) y christine_harkness@tjx.com (Christine Barski). Prioridad siempre como la pide el cliente.
Home Depot: lockouts de Engage -> levantar RCS. Todo lo demas -> HD_Investigations@homedepot.com (NO agregar al portal). Nuevos (Marissa 16-jul): corey_hendrick@homedepot.com, AP_Returns_Inquiries@homedepot.com. Logins que siguen fallando: Wilton Redd (WILTON_REDD@homedepot.com). Canada Engage: Nadia Vivan (nadia_vivan@homedepot.com). Contacto: Denver Culpepper. THD es el unico cliente con return override por Engage Portal (engage.apprissretailcloud.com); link TRE en myApron (grupo TRE_StoreManagers en myTHDaccess, email @HomeDepot.com, seleccionar US).
Walmart: script aprobado por Jovan (18-mar-2026): http://wmlink/AP1 tile "Secure Store"; reportar por "Contact Support" (survey). Backup wmlink/securehelp. Cualquier ticket que mencione Auror -> Delivery (sin acceso).
Shell (RTIaaS): usuarios van por el RSI Admin Team (ITSO-SOM-DS-RSI-Admin-Team@shell.com), no Appriss directo. Guia: Jessica Easley (Jessica.Easley@shell.com) o Connie Gimbel. Auto-close 14 dias. Lead PM James Bell. Ej RCS-17690, RCS-14217.
ASDA: reenviar a lposa@asda.co.uk. Admin carl.reeson@asda.co.uk.
ICA: effektivrutinanalys@ica.se.
Costco: lossprevention@costco.com, adamtabor@costco.com.
Ahold/Delhaize: LPMSSupport@retailbusinessservices.com. Zeus: AskZeus@adusa.com (Becky LaPierre).
Kohls: alta de asociados. James Edwards (James.Edwards@kohls.com).
GAP: admin Secure 5 Michelle_Anderson-Silva@gap.com. Reportar por Secure Issue/Feedback Intake form (Quick Links).
Meijer: video Genetec -> Ryan Theem (Ryan.Themm@meijer.com).
Vitamin Shoppe: tiendas -> su RLPM. Contacto Joe Austin (joseph.austin@vitaminshoppe.com).
McDonalds: admins Hugo y Paulett (NO Erika).
Nordstrom: EBR Brent Hamlin (per Michael F); ademas contacto APIS.
Bamboo Health / MethCheck: ya no es Appriss Retail (MethCheck ahora con Equifax). Redirigir a bamboohealth.com/contact. MethCheck URL https://methcheck.appriss.com/retail/pharmacy/loginForm.do

## Cheat sheet Kristin — Respuestas tipo (canned) para acceso al portal y archivos faltantes
_chunk 1379 · 2026-07-22_

Templates reutilizables de Kristin (se envian en ingles al cliente).

Invite de acceso al portal (asunto: "Appriss Retail Customer Support Ticketing Portal Access Information"): It has been requested by XXXX that you will need access to our ticketing portal. Once your credentials are set up you will be able to open tickets. You will be receiving an invite in a few minutes from Appriss/Jira. The link does expire quickly, set up your credentials ASAP. Check junk mail if you do not see it within 10 to 15 minutes. Please make your password 12 characters or less [nota: casi seguro error de Kristin, deberia ser "or more"; confirmar minimo real]. You may receive an error message when you go to the link, but go to Log In and click to proceed. If it does not work, let me know and we continue to next steps. Portal: https://support.apprissretailcloud.com

Reporter que no esta en el portal: This ticket has been created after XXX contacted our Level One team. You have been set as the reporter due to XXX not having access to the portal. If XXX is someone who should have access, please advise, and an invitation will be sent out.

Agregar un application administrator al hilo: Our support teams work through our customer support ticketing portal. I am including an application administrator in this email thread who has access to our portal. If additional individuals need access, contact me, or submit a ticket requesting the addition.

DSG archivo faltante (Dick's Sporting Goods repite el mismo ticket; ej RCS-22191, archivo DKS_incent4dsg_YYYYMMDD*.csv.gpg): It's possible our process was slower than expected, so the report was not generated on time. Typically the next report includes records from the missed night. The file should be sent later today with the missing transactions. If still missing tomorrow morning, reach out via this ticket.

## Cheat sheet Kristin — Reglas de prioridad (Aimee), team leads, Verify y links clave
_chunk 1380 · 2026-07-22_

Regla de prioridad de Aimee (email 5-ene-2024): TJX siempre queda con la prioridad que pidio el cliente. Para el resto se usa juicio, pero NO bajar a Medium: cualquier problema de acceso a la app aunque sea 1 usuario, app lenta o timeouts, y errores/problemas de permisos (sobre todo Admin/Power User). Work Items faltantes o que no cargan -> post HIGH PRIORITY en el canal Secure Outages; si es un solo item, sin OpsGenie. OpsGenie del equipo Secure 5 Issues: dataops 8 a 8 los fines de semana, entre semana quieren el OpsGenie.

Como saber en que equipo esta alguien: mirar su Teams Profile y bajo que arbol cae (hay "engineers" que en realidad son Delivery); no olvidar el SRE on-duty (calendario on-call). Aliases: EBR=Secure 5, Incident=LPMS/NetTrack, Audit=CAMS, Engage=Verify/TRE, Legacy=ASPECT y APIS, Delivery=implementation, DevOps=engineering.

Team leads: Carl Costello (Impl EBR, config, CCTV, SSO); Jon Morgan (Engineer EBR); Matt Kamminga (Development Incident/Audit y Legacy APIS); Ian Williams (Impl/Eng Engage).

Verify (Marissa): al crear o resetear una cuenta el access code dura 14 dias. Una vez adentro hay que loguear cada 90 dias o se deshabilita (se avisa antes). El access code se limpia cuando el usuario loguea.

Links clave del cheat sheet: Trust Portal https://trustportal.apprissretail.com (Security Information). RCS-22987 tiene la info del Appriss DR Plan & Annual Test Documentation, SE PUEDE compartir. IT Help desk ticketing https://trebuco.atlassian.net/servicedesk/customer/portal/6 ; numero nuevo del IT help desk (desde 8-2023) 1 (928) 272-4889. Platform Unification: https://docs.apprissretail.com/products/general/platform-unification-everything-you-need-to-know . Decommissions los inicia el CSM. Busqueda en el portal: lupa arriba a la derecha en la landing de abrir ticket, el cliente tipea lo que necesita y salen articulos.

## Kristine Guide — parte 1
_chunk 1617 · 2026-07-30 · fuente: Kristine Guide.md_

# Support operations

These are my notes from the handover with Kristin Krogman (Sr. Business Process Analyst). I wrote them to keep them handy for myself and so Camila, Viraj and the rest of the team know where everything landed once she leaves. Her last day is **Friday, July 31, 2026**.

They cover the seven formal KT topics (June 4 to July 21), the recorded sessions, the July shadowing, the eighteen artifacts she shared with me, and the Confluence pages that back each process. What follows is how support works today and where each document lives.

---

## 1. The KT program at a glance

**Status:** 7 of 7 topics completed and signed off (July 14, 2026). Tracker: "KT Pair Tracker Kristin - Juan.xlsx".

**The seven formal topics:**

| ID | Topic | Method | Date |
|---|---|---|---|
| T-034 | APIs + User Provisioning + Access reference | Live session | 06/10 |
| T-035 | Engineering escalation packaging standard | Live session | 06/16 |
| T-036 | Cross-product knowledge map | Shadow session | 06/10 |
| T-037 | Top customer access and security playbook | Docs review | 06/16 |
| T-075 | User provisioning playbook (Jira portal) | Live session | 06/24 |
| T-084 | Decision tree: API access and permissions | Video review | 06/16 |
| T-096 | Migration and downtime notification process | Q&A | 06/24 |

On top of the formal topics, the July sessions transferred the operational core: ticket statuses and escalation (07/14), the help inbox and live ticket creation (07/15), queue review and priority rules (07/16), the L2 morning routine (07/17), and backlog, assignment, on-call and routing (07/21).

---

## 2. The support model: triage and routing

Support runs as a **routing graph**. Every ticket gets classified and sent to the team that owns the next action.

**L1 (triage, non-technical team under J.R.):** classifies priority and product type, and routes. The main destination for most products (Secure 3/4/5, RTI, LPMS, CAMS, APIS, Aspect) is **Under Support Review, which lands in L2 Support**. Only RTIaaS goes straight to Under Engineering Review. Change Requests go to the L2 queue without touching priority. L1 also posts Critical/High tickets in the Teams priority channels.

**L2 (Support, engineers with a code background):** triages, routes and resolves Incidents across all products. The Under Support Review queue is managed by leadership. Data tickets carry the **Support_Data_Team** label. L2 resolves most tickets before they ever reach L3.

**L3 has two arms**, and you escalate based on the nature of the issue:

- **Engineering:** code-level bugs and defects. Reproduces the issue and does root cause analysis.
- **Delivery:** data and configuration problems already in production, including smaller-scope data mapping, setup and config.

Billable changes go to the **CSM** as a Change Request. New feature requests go through the **Customer Feedback / Ideas Portal** and the RCS ticket is closed.

**Effort rule:** support keeps anything that takes **4 hours of work or less**; everything beyond that escalates. This threshold will drop to 2 hours.

---

## Kristine Guide — 3. Ticket lifecycle: statuses and when to change them
_chunk 1618 · 2026-07-30 · fuente: Kristine Guide.md_

## 3. Ticket lifecycle: statuses and when to change them

Source documents (both shared by Kristin on July 15):
- **RCS Ticket Status Guide** (what each status means)
- **RCS Ticket Status Workflow Guide** (when to change each status)

**Key principle: the ticket status must always show who owns the next action.**

### 3.1 The standard flow

1. **Under Support Review.** Default status when a ticket arrives. A support engineer takes ownership as soon as possible.
2. **Work in Progress.** Mandatory first touch: change to this status and send the canned response **"New Ticket Assignment First Response"** to confirm ownership to the customer. This is the status whenever the ticket is in your hands.
3. **Under Customer Review.** The ball is on the customer's side. It is the **only status that pauses the SLA timers**. When the customer replies, the ticket returns on its own to Work in Progress, which is how you catch the reply.
4. **Resolution Suggested.** A fix or workaround was proposed and you are waiting on customer confirmation.
5. **Completed.** Appriss finished the work; the customer can still reply and the ticket jumps back to Work in Progress. Tickets are only completed or closed **from Work in Progress**.
6. **Closed.** Final state. A Closed ticket does **not** reopen when the customer replies; a Completed one does.

When you resolve, **two dropdowns are mandatory**. If the second one ("perform customer requested operation") is missing, the transition fails. The resolution goes in as an **internal note** on the ticket, without duplicating it in the closing message.

### 3.2 Routing statuses (waiting on an internal team)

| Send to | Status |
|---|---|
| Engineering | Under Engineering Review |
| Solutions Expert | Under Solutions Expert Review |
| Analytics | Under Analytics Review |
| Customer Success (CSM) | Under CSM Review |
| Infrastructure | Under Infrastructure Review |
| Database Services | Under Database Services Review |
| Delivery | Under Delivery Review |
| Product Management | Under Product Mgmt Review |
| Security | Under Security Review |

Always leave an **internal comment** explaining what you need from the receiving team before changing the status. When they respond, move the ticket back to Work in Progress.

**Warning:** Under Infrastructure Review does **not** return on its own to Work in Progress when Infrastructure updates the linked ticket. You have to watch it manually. There is an open action item with Austin to automate this.

### 3.3 Other statuses

- **Escalated:** urgent, high customer impact, or stalled too long. Flags the ticket for senior attention.
- **Waiting for Software Release:** the fix is built and parked until the next scheduled release.
- **Added to Backlog for Future Consideration:** valid request, no near-term work planned. Leave a comment explaining why.
- **Duplicate:** link to the original ticket in a comment before closing.

---

## Kristine Guide — 4. Ticket types and Queue Review
_chunk 1619 · 2026-07-30 · fuente: Kristine Guide.md_

## 4. Ticket types and Queue Review

Source document: **Updating Ticket Type: Steps to Follow** (Confluence RTS)
https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478007263240

The four RCS ticket types:

- **Incident:** break/fix. Something broken or throwing errors.
- **SOW:** general questions, how-to and simple change requests.
- **SOW Estimation:** billable work estimation, usually handled between the CSM and engineering without involving support.
- **New Feature:** new functionality requests.

**Why the type almost always comes in wrong:** the customer portal only offers two options. "Support Ticket" defaults everything to Incident and "Change Request" defaults to New Feature. The rule to fix them is simple: **anything broken or erroring is an Incident; any question or change request is a SOW.**

**Change the type:** click the type button at the top of the ticket, pick the new type in the dropdown, Next, Next (nothing changes on page two), Confirm.

**Queue Review:** go through every unassigned ticket in the queue on three fronts.

1. Correct ticket type.
2. Correct priority.
3. **Support_Data_Team** label on Secure 5 data tickets.

Hygiene checks that go with it:

- Always **tag the customer/company** on every ticket. It feeds the reports and saves everyone the scrolling. Known acronyms: PSCB is PacSun Eddie Bauer.
- **Sprint and Team Ownership = "support delivery" + "backlog"** are the labels Peyman wants on new data tickets so they show up in his dashboard. He decides the routing from there. Mark them support-delivery and let Peyman triage; the team should avoid sending tickets straight to the backlog.
- Link related DataOps tickets as "relates to".
- Complexity auto-populates.

### 4.1 Fine points of labeling (live shadowing, Jul 22)

I nailed this down on July 22 going through about 20 queue tickets with Kristin, one by one:

- **Exact values for a data ticket:** Label `Support_Data_Team`, **Team Ownership = "Support Delivery"**, **Sprint = "RCS Support Team"** (type "support" and it autocompletes). This corrects the "backlog" that sometimes gets mentioned for Sprint: the value Kristin uses is "RCS Support Team". Team Ownership plus Sprint only go on if the ticket goes to the data/payments team; if it goes to Delivery or another team, they do not.
- **The "Problem" field in the ticket body:** it should almost never stay on "Other". Reclassify it to "Data" (or another) as the case fits.
- **Tag the organization in the "Export to Power BI" field:** prepend the company name, for example `TJX-`, to identify it in reports and in Claude queries. Save with the check.
- **Mirror customer names:** KFC shows up as the organization **"Yum Brands"** (Yum is the parent; KFC and Taco Bell sit under it). The US/EU/CA/AU location is validated in the **Client Listing / contact sheet** (Yum Brands = EU).
- **Change Request is reversible:** if the customer is missing something and it is unclear whether it is broken or was never available, mark it a Change Request; it can move back to Incident if it turns out to be broken. Aimee's rule (repeated): if the customer is asking or requesting something (not break/fix), it is a SOW/Change Request. A real New Feature goes through **Pendo**, not as a ticket.
- **Automation gotcha:** when you assign to **Edwin Garzón**, a Jira automation stripped the `Support_Data_Team` label (left it on "none") on several tickets. If it happens: screenshot the History and write to **Austin Flannery** (Jr. IT).
- **Reassigning between people** (for example SnowTime access that only one person has configured): it is fine to swap tickets; give a heads-up on Teams to whoever receives it.

---

## Kristine Guide — 5. L3 escalation matrix
_chunk 1620 · 2026-07-30 · fuente: Kristine Guide.md_

## 5. L3 escalation matrix

Source document: **Escalating Tickets to L3 Departments: Procedures and Responsibilities** (Confluence RTS)
https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478006902856

**Mandatory checklist before escalating anywhere:**

- Environment where the issue lives (Test/QA/Prod).
- Complete reproduction documentation (step by step, with screenshots).
- Full notes from any AI-assisted troubleshooting.
- Notes from conversations with other engineers outside the ticket.

**The matrix:**

| Destination | Status | Assignee and actions | Ownership |
|---|---|---|---|
| Secure/Incident Engineering | Under Engineering Review | Shandana Khan. An ENG ticket is auto-created; comments sync both ways. | Unassign (their lead distributes) |
| Engage Engineering | Under Engineering Review | Ian Williams, plus a **mandatory Teams message** (he does not see the assignment alone). Backups: Shruti Golwalker, Kenny Vu. | Unassign |
| Infrastructure | Under Infrastructure Review | An RTAILIT ticket is auto-created, comments sync. | **You stay assigned.** You communicate to the customer and close. |
| Security (InfoSec) | Under Security Review | An INFOSEC ticket is auto-created, comments sync. | **You stay assigned.** |
| Database Services | Under Database Services Review | Linked DBA Services ticket. | **You stay assigned.** |
| Delivery, Secure 5 | Under Delivery Review | Peyman Motlagh, and add "RCS Support Team" to the Sprint field. | Transfers |
| Delivery, Incident | Under Delivery Review | Ryan Barlow, plus a Teams message. | Transfers |
| Solutions Experts | Under Solutions Experts Review | James DeJohn. | Transfers |
| CSM | Under CSM Review | The responsible CSM, plus a Teams message. | Transfers |
| Product Management | Under Product Mgmt Review | | Unassign |

Engineering queue map: **AALPS** covers Incident Audit, Aspect legacy and APIS engineering. **Secure 5** covers Secure EBR and Secure 5. **Legacy Secure Issues** covers Secure 3 and 4.

Practical notes from the live sessions:

- Support has limited visibility into ENG tickets; engineering comments do not always reflect back into the RCS.
- When assigning to Delivery or CSMs, always send **email plus a Teams message**. Ian and Ryan often do not see the assignment on its own.
- Engage training and how-to requests go to James DeJohn, who distributes to his team.
- **Duplicates:** take the second ticket, tell the customer the original number, link it as a duplicate, and add the customer as a requested participant on the original.
- **Incident tickets never go to the CSM.** A SOW (solutions over 2 hours) is approved by the CSM.
- J.R. plans to simplify this process; the matrix above is what is in effect today.

---

## 6. Priority rules

**Definitions (Kristin, July 21):**

- **Critical:** the application is down and nobody can get in. All hands. Extremely rare.
- **High:** a group or region cannot get in even though the app is still up, or the issue blocks the customer's daily work. The guiding question is always: how does this affect the customer?
- L1 validates High priority with the customer before posting ("how is this affecting you?"). The final call is the leads'.

**Contractual exception:** **TJX** tickets opened as High stay High no matter what, by contract. **ECA/ICA** follows the same rule today.

**Queue Review rules (July 16):**

- A change request (SOW) stays at **Medium** by default. It only moves to High if the CSM pushes it with concrete impact.
- An Incident that blocks the customer's work does justify raising the priority.
- An urgent ticket with no owner: **do not raise the Priority field by hand.** Post it in the Teams channel **"Support Team Priority"** so someone picks it up sooner.

---

## 7. Ticket assignment: pull model

As a rule, nobody hand-assigns tickets. Engineers pull them from the queue. Direct assignment happens in exactly **three cases**:

1. **Linked duplicate clusters** of the same issue: assigned to whoever investigates; the rest of the team helps answer the customers.
2. **Load or expertise balancing via the dashboard** when the queue is saturated. Some are stronger on Incident, others on EBR. Leads reach out directly.
3. **Specialist areas:** Engage always goes to Marissa Johnson.

**Load measurement:** the max standard is around **10 tickets per person**, with the caveat that data tickets weigh more because they take longer. Three data tickets can be more load than eight simple ones, which is why the raw count is misleading and why the culture avoids hand-assignment. Use the per-person dashboard to see who has capacity.

---

## 8. The Support Data Team (Secure 5 only)

Source document: **Support Data Team Ticket Triage** (Confluence RTS)
https://trebuco.atlassian.net/wiki/spaces/RTS/pages/477555982355

The Support Data Team is responsible for **customer-uploaded data on Secure 5 only**: retailer data ingest, incorrect data in receipts or reports. It does not monitor other products.

- L2 triages; data issues carry the **Support_Data_Team** label and are worked by an L2 cross-trained on data.
- If L2 cannot resolve it: Team Ownership = "Support (Delivery dep.)", Sprint = "RCS Support Team", status = Under Delivery Review, assignee = **Peyman Motlagh**, who reassigns to an engineer.
- Critical/High data issues: email notification to data team management plus an L1 heads-up on Teams.
- **Weekly update rule:** the engineer updates the ticket at least once a week even with no changes ("testing in progress" is enough).
- **Complete is different from Closed:** Complete means resolved with resolution details filled in; the customer verifies and only then it moves to Closed.
- Customers migrated off Secure 3 tend to generate data tickets.

---

## Kristine Guide — 9. Routing by domain: who owns what
_chunk 1621 · 2026-07-30 · fuente: Kristine Guide.md_

## 9. Routing by domain: who owns what

| Domain | Contact |
|---|---|
| Data, and on-call questions | Peyman Motlagh |
| Snowflake / platform | John Morgan first; Peyman if he is out |
| CCTV, Aurora, implementation | Carl Costelow |
| Secure 3 and 4 | Vlad Bogus, Matt Everett, Carlos (only these three) |
| EBR and triage questions | Carrie (Carolyn Allison) |
| Engage | Marissa Johnson |
| Engage engineering | Ian Williams (backups Shruti Golwalker, Kenny Vu) |
| Secure/Incident engineering triage | Shandana Khan |
| Delivery Incident | Ryan Barlow |
| Solutions Experts (training, how-to) | James DeJohn |
| Portal access tickets (AA) | Austin Flannery |
| Infrastructure contact | Russell Harmon (Pacific time) |

**Aurora rule:** any ticket mentioning the **Aurora** system routes to Delivery immediately. Support has no access to Aurora.

**ThinkLP:** ThinkLP is another company's product (incident type). For ThinkLP to Aurora migrations, disabling ThinkLP is handled by Carl Costelow's implementation side, with Jeff and Flavio in the Delivery Council loop. Support pulls these tickets out of the queue.

**Engage-over-platform tickets:** there is no "platform ticket" label or type, so the Secure-side teams do not see them in their dashboards. The mechanism is a heads-up to Peyman (or John Morgan for Snowflake) with the ticket number, a short summary, and an explicit "not urgent" when it applies. High priority goes to the Engage channel. Avoid loading the on-call SRE with non-urgent items.

**Overseas etiquette:** for John Morgan, Carl Costelow and EU/UK colleagues outside hours, send **email instead of Teams pings**. They appreciate it and pick it up the next morning.

**Customer naming:** in customer emails always use the full name. Lululemon, never "Lulu".

**Product aliases customers still use:** NetTrack means Incident (also LPMS). CAMS means Audit. Verify means Engage. Internally, "Delivery team" means implementation.

### 9.1 Teams channels to keep visible (live with Kristin, Jul 22)

Kristin's words: these channels will be your best friend. I already had access to them but they were not showing; you have to go into "see more channels" and set the hidden ones to show, they do not appear on their own. Nobody flags this in onboarding, so worth writing down. The ones to watch, all under Retail Ops:

- **AALPS issues**, **Data issues**, **Legacy and security issues**, **Engage issues**: things surface here across all products.
- **Priority issues channel:** this was the current L2 group. Camila and I will likely get our own or Aimee will unlock this one. It is also where you post a high-priority ticket so the team can grab it and send the customer a note ("we received your high priority, currently triaging", then "your ticket has been moved to the Delivery team", and so on).
- **R&D channel** (2026 Engage size, alpha and beta): has the Snowflake items and platform unification, which is ongoing. Camila and I have to watch this one; Aimee will probably help while she is still here.
- **SnowTime / Snowflake channel:** we send out communications for these too.

---

## Kristine Guide — 10. Daily operational routine (L2 lead)
_chunk 1622 · 2026-07-30 · fuente: Kristine Guide.md_

## 10. Daily operational routine (L2 lead)

The morning routine inherited from Kristin, in order:

1. **Overnight email and notifications** (UK/EU activity), SLA breach alerts, pending Teams follow-ups. With a normal queue, post the breach alerts to the team so someone grabs the ticket; with a saturated queue this posting is suspended.
2. **Escalated / high priority tickets with no owner:** if you have the knowledge, take them yourself.
3. **Backlog review:** summaries carry the company name, correct priorities, correct ticket types, data labels applied, and **no Engage ticket sits in the L2 queue** (password resets and mirrors are taken; the rest route to Marissa Johnson or Engage engineering).
4. **Your own tickets:** customer follow-ups and pending validations.
5. **7/14/28 day automation emails.** The 28-day email force-closes tickets (moving to 21 days). Review each forced close: if the customer was still waiting on their internal IT, reopen it **with a note explaining why** and ask the assignee. Internal tickets stay closed. TJX and other high-priority customers get a double check. RTI portal access tickets usually stay closed; several from the same customer means asking the CSM.
6. **CSM comment alerts:** when a CSM comments that a fix is done, the ticket goes back to the **original support assignee** to test and notify the customer.
7. **help@appriss inbox** (section 11).
8. **Filters and reports:** sweep Completed tickets and move them to Closed (good-practice message: "the work is complete; if nothing else is needed, it closes in 2 business days"; any associate can close, it is not a leads-only task). Tiger Team report. Per-person ticket dashboard.

**Backlog hygiene rule:** the backlog should never hold unassigned tickets in a status other than Under-X-Review or a waiting one. A "Work in Progress" with no assignee is an anomaly to investigate.

**Closing grace:** after resolving, give the customer 1 or 2 days to validate. No reply: "we have not heard from you, we assume it is resolved, moving to Complete and closing".

**Chasing stalled tickets** (recurring lead task): assignees, especially EU/UK, tend to lose the @mentions. Method: Teams message or @mention first; if silence, every 4 to 6 weeks send an email with the list of tickets that need an update. For people on PTO, email so they see it when they are back.

### Tiger Team (tickets over 60 days)

About every 6 weeks, sweep the report for assignees with multiple old tickets with no movement. For each one, send an email with their ticket list **including the last note on each ticket** so they can act without digging. Replies come by email or internal @mention. If an assignee replies outside the ticket, add the internal note yourself; it helps them and leaves a review trail. At month end, the totals Excel goes to whoever pulls the metrics. Process doc: **Tiger Team tickets Process.docx** (link in section 15).

---

## Kristine Guide — 11. The help@appriss inbox
_chunk 1623 · 2026-07-30 · fuente: Kristine Guide.md_

## 11. The help@appriss inbox

Inherited responsibility: the email flow passed to us (we already have mailbox access) on July 20, with Kristin copied until she leaves. L1 also watches this inbox. It exists for people **outside the customer portal**: contractors and unregistered contacts.

**How to read the inbox:**

- Subject with "RCS-####": the conversation already lives in a ticket. Leave it alone.
- No RCS number: someone needs help. Check if they are in the portal; if not, redirect them to their **application administrator** or the customer channel.
- Organizations control who opens tickets. Walmart requires a single contact (their application administrator channels everything). ASDA has a dedicated email for its stores.
- Reply **from your work email**, so the sender has a human contact back. A reply from the generic address leaves a user with no portal and nobody to answer to.
- To find the right admin for an organization: portal, Customers section, review who opened recent tickets and of what type. Whoever opens incident report tickets is the application admin; whoever opens data tickets is the wrong contact for access requests.
- The legacy "Retail Client Services" inbox is no longer operating: just junk and legal mail. Legal mail gets the canned response Legal provided; anything odd is forwarded to Legal.

**When an email becomes a ticket (live LULU case playbook):**

1. Search first for an existing ticket.
2. Validate priority and product type **with the CSM** before saving.
3. Create the ticket copying the customer's text **verbatim**.
4. Pick as reporter a **user registered in the portal** so notifications flow (the actual requester may not be in the portal).
5. Turn off the automatic customer notification if the CSM is running the communication.
6. Add an internal note whenever the routing is out of the ordinary.
7. **Link tickets with the same symptom across customers.** In the live case, a LULU upload issue turned out to be the same Secure user data bug as a Dick's Sporting Goods ticket already in engineering review. The CSM's initial routing can be corrected once you cross-reference.

**Cross-product linking through the person already on it (Ryan Barlow example, Jul 22):** while I was creating the Easy Corp ticket, a very similar error came into the high-priority channel from Secure Audit ("cannot view or edit a case regardless of who assigned it", trying to key in safety meeting notes). Ryan Barlow in Delivery was already working a similar one, so Kristin messaged him directly instead of triaging blind. The logic: flag it to whoever is already on it, because it could be a bigger issue across all incident products. If it is the same issue, link the tickets so they travel together; if it is different, it goes back to normal team triage.

**Contractor case (Samsung readiness):** contractors usually do not get portal access, so their requests arrive by email. The ticket is created with the support engineer as reporter, the questionnaire is attached, it moves to Under Infrastructure Review, and **support stays assigned** by the infrastructure rule. Communication with Infrastructure goes by direct email (an exception), and the status has to be watched by hand.

**Emails from phones (L1 flow):** an email is not automatically a ticket. For known issues with existing guidance (for example the platform unification: log in with the email instead of the old ID), skip the ticket, find the customer's admin, and pull them into the thread so they handle the first level with their own people. Open a ticket only when the issue is new or large and affects many users, and then put the admin as reporter.

### 11.1 Creating a ticket end to end (Kimberly Baney / Easy Corp, live, Jul 22)

The full run I did myself with Kristin watching. Ticket was **RCS-27930**, customer Easy Corp (the organization is named "EZ Corp" in the portal), issue "unable to edit a case":

1. **Create the Incident.** Summary format is company, then a dash, then the issue: "Easy Corp - Unable to edit case". Copy her exact words into the description, and paste the screenshot into the description too.
2. **Priority Medium** to start.
3. **Reporter workaround:** she was not in the portal yet, so I opened the ticket with myself as reporter, and swapped the reporter to her only after adding her to the portal. If the requester is already in the portal, you set them as reporter from the start.
4. **Requested participants and CSM auto-fill:** selecting the organization sets the requested participants automatically, and the CSM (Colleen) shows up on her own as CSM.
5. **Notify her in two emails.** First, reply-all on the original email thread so everyone sees that we opened a ticket on her behalf and that an invite to the portal is coming. Second, a separate email just to her with the portal access instructions (subject: "Appriss Retail Customer Support ticketing portal access information").
6. **Add her to the portal:** Jr., Customers, Organizations, type "EZ" so EZ Corp comes up, Add Customer, enter her email, OK. She is now invited (it can take a minute, sometimes you have to refresh).
7. **Set her as reporter:** back on the ticket, open the reporter field, type "Kim". Spelling gotcha: her last name is spelled **Banee** (not Baney), so backspace and fix it. Refresh the ticket if her name does not grab the first time.

**Internal link vs customer link (important).** A ticket has two links and they are not interchangeable:

- The **internal link** shows everything on the ticket, internal and external comments. Send this one only to people internally.
- The **customer link** is the view the customer sees when they log into the portal. When you send a link to the customer, grab it from that customer view, never the internal Jira link. Sending the internal one exposes internal notes.

If the customer still hits an error after being added (Kimberly got one message on first login), apologize in a reply to her email, have her try the customer link to the ticket, and give her the portal URL. If it keeps happening, move to next steps.

---

## Kristine Guide — 12. Portal administration and Verify (Engage)
_chunk 1624 · 2026-07-30 · fuente: Kristine Guide.md_

## 12. Portal administration and Verify (Engage)

### Support portal: adding people and organizations

Source document: **Adding customers and organizations to the support portal** (Confluence RTS)
https://trebuco.atlassian.net/wiki/spaces/RTS/pages/357465358603

- **Add a person:** Customers, Organizations, find the organization, Add Customer, email, OK. They get an invite. Search by email first: if they already exist, tell them and share the portal URL.
- **Validation:** with unknown requesters, confirm first with another admin at the organization. A known person copied on the email counts as vouching. Requests forwarded by CSMs are valid.
- **Add an organization:** Customers, Organizations, Add Organization, trade name. Parentheses hold aliases, for example "Air Force (APs)".

**Access request via email, ask the admin for permission (Kimberly Baney case, Jul 22).** When someone writes in asking for help but is **not in the portal**, you do not just add them: you forward their email to the customer's **application administrator** (for example Ronald) asking whether that person should have access to the Customer Ticketing Portal ("we're happy to add her, we just need your permission"), with the **CSM copied** (for example Colleen). Decision rule:

- If the application were **completely down**: add the person immediately and sort out who should have access afterward.
- If they **have access and are just having trouble** (like this case): follow the process and confirm with the admin before adding.

The reason to hold to this, in Kristin's words: not every company wants certain people in there seeing every ticket, often it is just control over who we communicate with. Other companies say "whoever" and put too many people in, and that is their call. Either way we follow the process. I can handle this from here on (it is faster when they are not around). The underlying goal: **force customers to open tickets in the portal**; otherwise emails get lost.

**Customer self-service search in the portal:** once in the portal, a customer can search for their own answers. Typing "release" pulls up release notices; "calendar" or "schedule" gets the release calendar; how-to articles link out to the wiki, GitBook or user guides. Good to know when pointing a customer at where to look.

### Verify portal (Engage)

Verify is the admin face of Engage; customers still call it Verify.

- **Password reset (the most frequent):** Admin, Web User Listing, search by email or name, check the "disabled" checkbox, click reset, the link appears. Notify the requester. With Home Depot, ask for a screenshot first: they run several applications and it may not be Engage.
- **Provisioning with a mirror:** the typical request is "give X the same access as Y". Edit user Y, screenshot the checkmarks, Add User with the new email, replicate the checkboxes, select the retailer, and **the phone is mandatory for 2FA**. Ask for it if it is missing. Save Changes.
- **What support does not touch in Engage:** product-specific topics go to Marissa Johnson. Claims eligibility and void-claim requests always go to Marissa. ABIS/incident access changes run through the customer side for security; SSO is the partial exception.

---

## Kristine Guide — 13. APIS
_chunk 1625 · 2026-07-30 · fuente: Kristine Guide.md_

## 13. APIS

**What it is:** Asset Protection Information System, a case management product for Loss Prevention and Risk, with an audit module (forms and reports).

### 13.1 What I check first in APIS

Seven things that came out of the live demos and are not written down anywhere else (they also go into the APIS Survival Guide when I put it together):

1. **System Options are per-customer feature flags.** The master list is "System Option List-Update this one.xlsx". Most reported "bugs" are an option turned off for that customer. First place to look.
2. **Impersonation is the number one method.** Log in as the reporting user to see their real permissions, view and hierarchy. It solves almost every "I cannot see this".
3. **Location hierarchy is the permission scoping.** "I cannot see the incident/report" is almost always a badly assigned hierarchy.
4. **Label cache reset.** Changed screen labels that do not show up need a label cache reset.
5. **Version 270 versus 275.** Same data, different UI, toggled per user or customer. 270 is the heavy classic, 275 the refreshed one. Confirm which version the customer is on before diagnosing.
6. **Warning: admin, Users, Edit shows passwords in plain text.** Never screen-share that view during a customer call.
7. **AdHoc reports: prioritize by Last Run Date.** The UI has no spinner. If it looks like nothing is happening, it is already running.

### 13.2 Access

- **Prep:** identified by "UAT" in the URL and the "-prep" suffix in the company ID. The first login can hit a Cloudflare block; report it to IT if it happens.
- **Prod:** currently runs on a shared legacy account. Your own individual PROD account requires identifying the APIS application owner who provisions accounts; still an open item.

### 13.3 Feed errors runbook (summary)

1. A feed failure email arrives with the feed and customer in the subject.
2. Log in to Azure Portal with your own user (not LDAP).
3. Get into the ETL server **P-APIS-ETL01** with the "Apis prod EVD Feeds" credentials from the GSOC vault in 1Password.
4. Azure share: retailalpprod.file.core.windows.net/apis-prod-evd/Feeds, customer folder, Data Directory, feed.
5. Check **clientyymm.log** first, then **client_feed.log**.
6. Re-run: share p-ingest-fsla4/DLZ/customer/Prod, restore the file from Archive/Prod/YYYY/MM/DD if missing, run the feed's scheduled task on the ETL server.
7. Manual close: Resolved plus "SYS Followed Support Process".

The assignees named in the runbook are from 2021 and need confirmation. Full documentation: Confluence AALPS space, **APIS** page (https://trebuco.atlassian.net/wiki/spaces/AALPS/pages/273453096/APIS), keeping in mind that index is from 2021 and parts point to dead domains. The live operational page is **Customer Server Profile** (Confluence 474658570288, maintained by Ryan Barlow and Matt Kamminga, updated June 30, 2026) with the node matrix.

### 13.4 APIS customers (15 active)

Source: Client Contacts.xlsx, "APIS Outage List" tab. **Internal only, never share outside.**

Hosted: 7-Eleven (migrates to Incident around Sep/Oct 2026), Academy Sports + Outdoors, Claire's US, Claire's UK (**different URL: apisuk.apprissretailcloud.com**), J.Crew, North Carolina Education Lottery, Six Flags, Tapestry, Victra, WWE.
On-prem: AAFES and NEXCOM (both government, do not migrate), Lowes Foods, Tiffany and Co.
Colleen Knoblock is the CSM for most APIS customers.

### 13.5 AALPS engineering queue triage

Bugs go to Shan / Mission Control. Features go to Sholan Narine and Jon Ross. Data imports go to Ryan Barlow.

---

## Kristine Guide — 14. SLAs
_chunk 1626 · 2026-07-30 · fuente: Kristine Guide.md_

## 14. SLAs

Source document: **Service Level Agreements** (Confluence RTS)
https://trebuco.atlassian.net/wiki/spaces/RTS/pages/477582491649

- Support handles two SLA sets: **RCS ticket SLA** and **Uptime SLA**. **There is no SLA for data loads.**
- All customers follow the standard structure **except TJX and ICA**, whose contracts carry financial penalty clauses.
- If a customer asks for SLA reports, escalate to Support Management.
- Public Uptime SLA: apprissretail.com/service-availability-schedule.

**ICA process, Work Item SLA (expanded in Dean Korbakis' session, Jul 22).** Effective June 1, running through May 27; the percentage rises about 3% a year (validate with the ICA CSM every May). Secure EBR Core Work Items must be available every day by **8am CET**, with a buffer until **9am CET** to resolve. Not resolved by 9am CET and not the customer's fault = **1 hit**.

- **Counting is by calendar day, not by ticket or by number of work items.** If 10, 30 or 50 fail on one day, or if 3 admins report the same day, it is still **1 hit** (put `ICAmissed` on one of them only). A multi-day outage counts **1 hit per day**: real example, an incident from late August, then all of September, then all of October, then 12 days into November, reported under a single RCS but charged per calendar day (about 30 hits in September, 31 in October), always at the 10+ cap for the month.
- **Credit grid** on monthly revenue: 1st instance of the month = grace (no credit), 2nd to 4th = 2%, 5th to 10th = 5%, 10+ = cap (about $1350). Validate figures with the contract/CSM.
- **Exact labels** (Jira treats variants as distinct labels and breaks the feed): `SLA_Checked` (reviewed, with or without a violation) and `ICAmissed` (violation; feeds the "ICA Work Item Reporting to PowerBI" gadget). Convert the resolution timestamp to CET (World Time Buddy) to know whether it was inside the 8 to 9am window.
- **Detection:** L1 catches it in monitoring (first as RTS), reports it in Teams "Secure 5 Issues"; L1 re-runs the simple ones, L2+ investigates and escalates to L3 if a workaround is needed. Watch RTS and RCS with the **"ICA Missed Work Item Loads"** dashboard (id 23940).
- **Monthly close:** the Power BI report is owned by **Austin** (Dean does not edit its visibility); it must be refreshed by the 5th of the following month with everything closed. Set a monthly calendar reminder (day 1 to 5).
- **Access:** share ownership of dashboard 23940 with Camila/Juan/Viraj; do **not** make it public, restrict by department (J.R., so CSMs do not share data without vetting). The team works in UTC; watch out for DST (the CET/CEST offset changes).
- **TJX is left for another session** (two fronts: on-time resolution of High/Critical plus on-time performance). Official source: Confluence RTS "ICA Work Item SLA Process" (pageId 476545810442) and "TJX Companies SLA Agreements and Specifications" (pageId 476218785811).

**Release calendar** (part of triage): https://docs.apprissretail.com/products/product-docs/general/release-calendar. Three uses: correlate sudden multi-customer breaks with that week's release, promise real fix dates (release cadence is weeks 2 and 4), and answer code-freeze questions in readiness checks. Kristin showed the live view: next week both incident and secure release, secure always goes on the second day, Wednesday and Thursday. Knowing the release date matters because tickets get assigned back to the original assignee when a bug fix ships, so they can test it and tell the customer to validate on their end.

---

## 15. Maintenance, outage and migration notifications

Source documents:
- **Maintenance or Outage Notice Process** (in depth): https://trebuco.atlassian.net/wiki/spaces/RTS/pages/475931901982
- **Maintenance Notification Overview** (process whiteboard): https://trebuco.atlassian.net/wiki/spaces/RTS/whiteboard/476153348117

They cover notifying customers of maintenance windows, outages and migrations with downtime, including who sends what and when. During platform migrations, customers keep using their old URL/domain until their migration completes.

---

## 16. On-call

Support historically had no on-call; Delivery/engineering carried it and L1 handled almost all inbound. The support team now joins the rotation. Reference for on-call questions: **Peyman Motlagh**, who did on-call with the data team. High-priority issues outside hours go in the priority channel. SRE on-call schedules: https://trebuco.atlassian.net/jira/ops/who-is-on-call (EU and US views).

---

## 17. Decommissions (DCOM)

The CSM opens the decommission when a customer announces they are leaving or a platform change. It comes with an engineering ticket (bringing down the database and the like) and sometimes an **"AA" ticket** (access/portal) to remove the organization's access, which links to the RCS and is assigned to **Austin Flannery**. The RCS closes when the AA work is done. Additional steps: move the customer to previous/canceled in the client contact sheet and remove it from all live lists (outage listing, contact listing). Full process in Confluence.

**PM handoffs (new customers):** when a customer goes live and moves to support, the Project/Product Managers send an email with an info sheet (open tickets, contacts for the client listing). The team updates the client listing, contact listing and outage listing. Watch out for mirror names (SSP and SSP Markets are two different things).

---

## Kristine Guide — 18. RCA and Retro process
_chunk 1627 · 2026-07-30 · fuente: Kristine Guide.md_

## 18. RCA and Retro process

Dean Korbakis demo on July 17 (Viraj was among the attendees). Two Claude skills generate the documents:

1. **Retro:** "create a retro using [RCS ticket] + [meeting/chat links]" produces a pre-filled worksheet (naming RET + incident date + customer). Anything unanswered is left blank for the live retro session with engineering. Record the session.
2. **External RCA:** "create RCA from this retro" produces the customer-facing document in plain business language. A full-detail internal RCA is optional and a management decision.

**Trigger:** the external RCA happens **only by customer request**, never automatically off a P1. First you try to resolve the explanation inside the ticket.

**Approval chain:** direct manager (Camila), then the manager of the department that touched the issue, then J.R. as final review. Delivery goes back through the same channel the request came in (ticket, email or CSM).

**Jira tracking:** adding the **"problem management"** label to the RCS auto-creates two PBM tickets (retro plus RCA). Finished documents are published in Confluence, Problem Management space, "Root Cause Report List", in the year folder (naming RCAYYYYMMDD - Customer - Description). Close all three tickets at the end. RCA content shared with the customer goes through a management filter.

---

## 19. Key documents and links (full artifact list)

The 18 KT artifacts, signed off on July 14, 2026.

**Confluence (shared, permanent):**

| Document | Link |
|---|---|
| RCS ticket triaging process | https://trebuco.atlassian.net/wiki/spaces/RTS/pages/357465227677/RCS+ticket+triaging+process |
| APIS documentation (AALPS space) | https://trebuco.atlassian.net/wiki/spaces/AALPS/pages/273453096/APIS |
| Service Level Agreements | https://trebuco.atlassian.net/wiki/spaces/RTS/pages/477582491649/Service+Level+Agreements |
| Updating Ticket Type | https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478007263240/Updating+the+Type+of+Ticket+Steps+to+Follow |
| Creating Linked Tickets in RCS | https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478008344588/Creating+Linked+Tickets+in+RCS+Steps+and+Examples |
| How to Open a Ticket in JIRA | https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478007689352/How+to+Open+a+Ticket+in+JIRA+Steps+and+Guidelines |
| Escalating Tickets to L3 Departments | https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478006902856/Escalating+Tickets+to+L3+Departments+Procedures+and+Responsibilities |
| Adding customers/organizations to the support portal | https://trebuco.atlassian.net/wiki/spaces/RTS/pages/357465358603/Adding+customers+organizations+to+the+support+portal |
| Maintenance or Outage Notice Process | https://trebuco.atlassian.net/wiki/spaces/RTS/pages/475931901982/Maintenance+or+Outage+Notice+Process |
| Maintenance Notification Overview (whiteboard) | https://trebuco.atlassian.net/wiki/spaces/RTS/whiteboard/476153348117 |
| Support Ticket Workflow (RCS), new hire playbook | https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478022631425 |
| Support Data Team Ticket Triage | https://trebuco.atlassian.net/wiki/spaces/RTS/pages/477555982355 |
| SRE on-call schedules | https://trebuco.atlassian.net/jira/ops/who-is-on-call |
| Release Calendar | https://docs.apprissretail.com/products/product-docs/general/release-calendar |

**SharePoint, shared team site (secure location):**

| Document | Link |
|---|---|
| Client Contacts.xlsx (all customer contacts, includes APIS Outage List tab) | https://trebu.sharepoint.com/:x:/s/RetailSupport/EVxU-hgt0PhFmvDpGR8Dxl0Bi6O_hgPcy5Cgwv-xSmAgWg |

**SharePoint, Kristin's personal OneDrive (needs migration before July 31, see section 20):**

| Document | Link |
|---|---|
| 28 Day RCS ticket closure process | https://trebu-my.sharepoint.com/:w:/g/personal/kkrogman_trebu_co/IQCWqWCry_pzR7h0H6LEtk8XASNGxYRs6kmjRGAaVPsJJsw |
| Completed Closed RCS Process | https://trebu-my.sharepoint.com/:w:/g/personal/kkrogman_trebu_co/IQC7tjRK64p-To9yo6W-W7oZAS05fXWavHFJ2yVUtLwh_6Y |
| APIS Start First Steps.docx | https://trebu-my.sharepoint.com/:w:/g/personal/kkrogman_trebu_co/IQC-lRcHB290SoGWL1Tk_aOtAdQz1SDgB1s3XJbZGQ0vn0w |
| Engage Password Reset Locked Out.docx | https://trebu-my.sharepoint.com/:w:/g/personal/kkrogman_trebu_co/IQBcjpZcgI9bT6kdFaffDIKSAYzw4_l8sg9MM1itVqvno94 |
| How to set up Engage Portal user.docx | https://trebu-my.sharepoint.com/:w:/g/personal/kkrogman_trebu_co/IQCkCGMNHbfQSq2pjYb2-HoWAa4Rdxt-mHa4ENgiaN8xDqQ |
| Tiger Team tickets Process.docx | https://trebu-my.sharepoint.com/:w:/g/personal/kkrogman_trebu_co/IQDkauokzHRXTKlVQzfjjqQsAbJfwScb5a7IUgxWXCTXm1o |
| Creating Ticket link / Changing Ticket Types | https://trebu-my.sharepoint.com/:w:/g/personal/kkrogman_trebu_co/IQBdRYFtDdi6QYtWjPYst_RFAblRUAIfTOvc0GffA-c932k |
| How to open a ticket | https://trebu-my.sharepoint.com/:w:/g/personal/kkrogman_trebu_co/IQAU9D8mLyDcRaIOPhJ3atluAQECq8GplKUSy4pNB0nsxHk |

**Session recordings (Kristin's OneDrive):** the shadowing recordings from June 9, 10, 12, 16 and 24 are linked in the KT Pair Tracker sheets.

---

## Kristine Guide — 20. Continuity risks and open items (before July 31)
_chunk 1628 · 2026-07-30 · fuente: Kristine Guide.md_

## 20. Continuity risks and open items (before July 31)

1. **Nine process documents live only in Kristin's personal OneDrive** (table above). A personal OneDrive's content becomes inaccessible once the account is deactivated, and that already happened once with a previous SME's documentation. Action: copy them to the shared RetailSupport site or to Confluence before her last day. Kristin's plan is to consolidate them into a single folder to share; the approved ones move to Confluence.
2. **APIS Survival Guide:** I agreed to write it, with Kristin as reviewer before she leaves. It captures the seven APIS checks and the operational knowledge that is not written down anywhere.
3. **Appriss Admin Customer Super Manual:** Kristin has a downloaded copy on her desktop. Ask for it before she leaves; the original lives in a deactivated account's OneDrive.
4. **Individual APIS PROD account:** identify the application owner who provisions real PROD accounts, replacing the current shared legacy account access.
5. **Access to the Teams channel "Support Team Priority"** for me: requested, pending with J.R. It is the channel where urgent tickets are sped up instead of touching the Priority field.
6. **Automatic return from Under Infrastructure Review:** open action item with Austin so the status goes back to Work in Progress when Infrastructure responds.
7. **Email process document:** J.R. asked Kristin for a written doc of the support email process that passed to Camila and me on July 20.
8. **Departmental ticket process doc:** the consolidated status document Kristin started belongs to the migration list.
9. **The 28-day auto-close becomes 21:** watch for the change and adjust the daily review.
10. **The support effort threshold drops from 4 hours to 2:** more tickets will escalate to L3 once this takes effect.
11. **Kristin's availability:** she works until around 4pm and stays available for follow-ups through July 31.
12. **My Engage/Verify portal access:** not confirmed yet. Kristin is reaching out to Marissa (or Nicole, who works with Marissa now) to sort the permissions; it looks like a permissions issue. If Engage comes up before that is fixed, we screen-share and walk through it.
13. **Help inbox in Outlook:** I have access to the help@appriss inbox but it is not showing up configured in my Outlook yet. Still to sort out how to make the shared inbox appear (it usually shows under a dropdown below your name / in favorites).
