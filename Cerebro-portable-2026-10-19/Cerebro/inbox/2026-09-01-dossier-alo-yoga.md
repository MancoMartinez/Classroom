# Dossier Alo Yoga — tickets RCS, verificado en Jira el 1 sep 2026

Fuente: Jira cloud 7eb600cf-c7e0-43ed-acc4-90b277d43514, proyecto RCS. Solo lectura.
Recolectado el 2026-09-01. Todos los estados y fechas son literales de Jira.
Donde Jira no tiene el dato, dice "no consta en Jira".

## Cómo se armó el universo

Tres JQL ejecutadas y unificadas:

1. `project = RCS AND text ~ "Alo Yoga" ORDER BY created DESC` — 42 resultados.
2. `project = RCS AND summary ~ "Alo" AND created >= "2026-06-01" ORDER BY created DESC` — 14 resultados, todos ya en la primera.
3. `project = RCS AND text ~ "ALO" AND created >= "2026-08-10" ORDER BY created DESC` — 3 resultados, todos ya en la primera.

Consultas de control adicionales, todas para descartar huecos:

- `project = RCS AND created >= "2026-08-15" AND (text ~ "Alo" OR text ~ "yoga" OR text ~ "aloyoga")` — **cero resultados**.
- `project = RCS AND (text ~ "Alo" OR text ~ "yoga") AND updated >= "2026-08-18"` — 4 resultados: RCS-27598, RCS-26196, RCS-28108, RCS-27557.
- `project = RCS AND text ~ "Alo Yoga" AND statusCategory = Done AND updated >= "2026-08-10"` — 4 resultados, todos resueltos antes del 18 ago (RCS-28297, RCS-28296, RCS-28293, RCS-28183).
- `project = RCS AND statusCategory != Done AND (description ~ "aloyoga" OR summary ~ "ALO" OR comment ~ "Alo Yoga")` — 5 resultados, coincide con el grupo A más RCS-27598.
- `project = RCS AND text ~ "Alo Yoga" AND assignee WAS "Camila Espinosa"` — **cero resultados**.

Descartes verificados:

- **RCS-21548** es de 7-Eleven ("7-Eleven - Secure 5 - Store leader and designee cannot access POS dashboard for their store"), estado Closed. No es ticket de Alo Yoga.
- **RCS-27598** es de Guess. Reporter `sbenedetti@guess.com`. Se queda como referencia cruzada, no como ticket del cliente. Ver sección D.
- **RCS-27966** "Delete Work Order" apareció en la búsqueda de texto. Cerrado el 2026-07-27, muy antes del corte. Fuera de los tres grupos. No se verificó el cuerpo.

## Resultado de la clasificación, dicho de frente

- **Grupo A, abiertos hoy: 4 tickets.** RCS-28108, RCS-27557, RCS-27389, RCS-26196.
- **Grupo B, cerrados después del 18 ago 2026: cero tickets.** Ningún ticket de Alo Yoga tiene `resolutiondate` posterior al 2026-08-18, y ninguno de los que están en estado Done tiene `updated` posterior al 2026-08-18. Un ticket transicionado a Closed después de esa fecha tendría `updated` posterior por fuerza. El grupo está vacío en Jira, no por falta de búsqueda.
- **Grupo C, nuevos desde el 18 ago 2026: cero tickets.** Ningún ticket RCS creado el 2026-08-18 o después menciona Alo, Yoga o aloyoga en ningún campo indexado. El último ticket de Alo Yoga creado es RCS-28108, del 2026-07-31.

Dato para la reunión: en los 14 días desde la salida de Camila Espinosa, Alo Yoga no abrió un solo ticket nuevo y Appriss no cerró ninguno de los abiertos. Los cuatro abiertos son los mismos cuatro que ya estaban abiertos el 18 de agosto.

---

# GRUPO A — abiertos hoy, 1 sep 2026

## A1. RCS-28108 — Alo Yoga - Cameras failing to load. Order #41213355

| Campo | Valor literal de Jira |
|---|---|
| key | RCS-28108 |
| summary | `Alo Yoga - Cameras failing to load. Order #41213355` |
| status | `Under Customer Review` (statusCategory To Do) |
| issuetype | Incident |
| assignee | Carl Costelow (ccostelow@apprissretail.com) |
| reporter | krislyn vara (krislyn.vara@aloyoga.com) |
| priority | Medium |
| created | 2026-07-31T15:41:10.393-0400 |
| updated | 2026-08-27T09:04:23.717-0400 |
| resolution | null |
| resolutiondate | null |
| labels | ninguna |
| issuelinks | ninguno |

**Problema reportado.** La descripción del ticket está vacía en Jira (`description` es un documento sin contenido). El reporte llega solo por el summary y por dos capturas de pantalla adjuntas en el primer comentario. El problema declarado es que las cámaras no cargan para la orden 41213355.

**Cronología de comentarios**

- **2026-07-31, krislyn vara.** Comentario solo con dos imágenes, sin texto.
- **2026-07-31, Neha Haridas.** Acuse automático de soporte: "We have received your ticket. This is being forwarded to the appropriate team for assistance."
- **2026-08-03, Carl Costelow.** "This has been resolved. Can you confirm please?"
- **2026-08-03, Carl Costelow.** Causa declarada: "The scheduled job was switched off. This was due to some fixes in the release."
- **2026-08-05, Automation for Jira.** "Resolution Details has been set to: Delivery Resolved - Data Corrected"
- **2026-08-14, krislyn vara.** Reapertura desde el cliente: **"This is not resolved."** Adjunta tres capturas.
- **2026-08-14, Automation for Jira.** "Thank you for your email. Given that this ticket was previously closed, we will carefully assess your comments. If necessary, we will provide further evaluation."
- **2026-08-17, Carl Costelow.** "I will investigate and get back to you."
- **2026-08-20, Carl Costelow.** "Can you check this order again please?"
- **2026-08-27, Automation for Jira.** "Email sent to assignee informing that customer has not responded for 7 days."

**Quién tiene la pelota.** El cliente. Carl Costelow pidió reverificación el 20 de agosto y krislyn vara no ha contestado. La automatización lo confirmó el 27 de agosto. Ese es el último movimiento del ticket.

**Siguiente paso comprometido.** Krislyn vara debe reverificar la orden y responder. Appriss no comprometió nada más después del 20 de agosto.

**Tickets enlazados.** Ninguno.

**Alerta para la reunión.** El ticket ya se cerró una vez con la etiqueta "Delivery Resolved - Data Corrected" el 5 de agosto y el cliente lo reabrió nueve días después con un "This is not resolved". Si Alo pregunta por este, la posición de Appriss es que espera confirmación desde el 20 de agosto. No hay hallazgo técnico nuevo escrito en el ticket después del 3 de agosto.

---

## A2. RCS-27557 — Alo Yoga - Incorrect time on Appriss receipt

| Campo | Valor literal de Jira |
|---|---|
| key | RCS-27557 |
| summary | `Alo Yoga - Incorrect time on Appriss receipt ` (con espacio final) |
| status | `Work in progress` (statusCategory In Progress) |
| issuetype | Incident |
| assignee | Thomas Walker (twalker@apprissretail.com) |
| reporter | krislyn vara (krislyn.vara@aloyoga.com) |
| priority | Medium |
| created | 2026-06-25T13:31:29.052-0400 |
| updated | 2026-08-20T20:56:09.723-0400 |
| resolution | null |
| resolutiondate | null |
| labels | ninguna |
| issuelinks | Relates to RCS-26512 (Closed, High), Relates to RCS-26196 (Accepted into Development, Medium) |

**Problema reportado.** Cita literal de la descripción: "For several orders, the timestamp shown on the Appriss receipt does not match the corresponding Shopify order timestamp. Examples included." Cuatro capturas adjuntas con los ejemplos.

**Cronología de comentarios**

- **2026-06-25, Vismaya Thottada.** Acuse automático de soporte.
- **2026-07-01, Constantine Korbakis, al cliente.** Confirma causa: "The times on the Appriss receipts are currently being recorded in UTC (GMT) rather than the local time of the store, which is why they do not line up with the times you see against the Shopify order. We have passed this to our engineering team to correct how the time zone is applied for your orders." Pide decisión: "could you confirm which time you consider correct: the local time at the physical store, or the time as displayed in your Shopify admin? For your Canadian stores these can differ".
- **2026-07-01, Constantine Korbakis, nota interna (visibilidad Service Desk Team).** "Measured a consistent seven hour offset across all four example events on orders 1516417 and 1520071, which matches UTC versus the Pacific time Shopify's admin displays." Localiza el defecto: "The defect is in the shopify_mapping function, OrderMapping_GQL-MDM.cs. The mapping timezone defaults to UTC and is only replaced by a geo lookup on the store location latitude and longitude. Alo's Shopify location records have no latitude or longitude, so the timezone stays at UTC and no conversion is applied."
- **2026-07-01, Constantine Korbakis, brief de escalación completo.** Impacto: "All Alo Shopify-sourced receipts display event times in UTC instead of local time. Confirmed +7h on orders 1516417 and 1520071 (both Edmonton stores)." Y el punto que importa para la reunión: "the same UTC value drives CCTV video linkage, so investigator video pulls land about 7h off (same concern raised in RCS-26512). No financial or return-decision impact." Evidencia: "4 of 4 timestamp pairs equal exactly +7h. Both Shopify orders show 'No shipping / No billing address provided'." Pide tres cosas a ingeniería: cambiar el fallback de timezone para usar la zona configurada de tienda o cliente en lugar de UTC, confirmar la zona objetivo, y decidir si Alo debe poblar latitud, longitud y el metafield storenumber en sus locations de Shopify como arreglo durable.
- **2026-07-08, Automation for Jira.** "Email sent to assignee informing that customer has not responded for 7 days."
- **2026-07-09, krislyn vara.** Respuesta del cliente, literal y completa: **"It should display in local time. Thanks"**
- **2026-07-10, Constantine Korbakis, nota interna.** "Customer confirmed on 2026-07-09 that the Appriss receipt should display the transaction time in the physical store's local time. This resolves the open target-timezone question raised in the escalation brief above. [...] No further input is needed from the customer to proceed."
- **2026-07-10, Constantine Korbakis, al cliente.** Confirma que ingeniería usará hora local de tienda como objetivo.
- **2026-07-23, Kristin Krogman, interno.** "@Thomas Walker can you provide an update or timeline for this ticket, please? Thank you"
- **2026-07-23, Kristin Krogman, al cliente.** "Your ticket is with our engineering team. They are continuing to investigate the best way to move forward with this ticket. **There is no specific timeline for completion that can be shared at this time.**"
- **2026-07-29, Thomas Walker.** Posición de ingeniería: "Shopify currently send all times over in UTC, we look to handle this in the code by resolving the timezone from the latitude and longitude of the store that the transaction is happening at but it looks like for most (if not all) stores this is not set by Alo. **If they set the latitude and longitude for store locations in Shopify then this will automatically start to work and correctly derive the timezone.**" Y la alternativa: "We can try to derive the timezone from the 'Shop' query but that covers the whole domain so any domains covering multiple timezones may still end up with transactions a few hours askew."
- **2026-08-18, Paul Marderosian, al cliente.** Traslada la pelota a Alo: "i spoke with our engineering team that has been working on this request and they determined that we are not being passed the latitude and longitude of the store that the transaction is happening at. This is needed for our side to do a conversion to the actual store time. **Is this something you could have your side add?**"
- **2026-08-20, Paul Marderosian, interno a Thomas Walker.** La respuesta de Alo, tal como Paul la reporta: "Alo's IT team reached out and said that **we (Appriss) need to derive this separately based on the store address. They said this data is not available in Shopify.** See attached. Is that something we can do? This is regarding ticket RCS-27557." Adjunta una imagen.

**Quién tiene la pelota.** Ingeniería, en la persona de Thomas Walker. Paul Marderosian le preguntó directamente el 20 de agosto si Appriss puede derivar la zona desde la dirección de la tienda, y **no hay respuesta en el ticket**. El ticket lleva 12 días sin movimiento.

**Siguiente paso comprometido.** Thomas Walker debe contestar si Appriss puede derivar timezone desde la dirección de tienda. Nadie ha respondido esa pregunta en Jira.

**Tickets enlazados.** RCS-26512 (Closed) y RCS-26196 (Accepted into Development). Misma familia de código, `shopify_mapping` / `ardm_json_loader`.

**Alerta para la reunión.** Aquí hay un desacuerdo abierto y sin resolver sobre quién arregla qué. Appriss dijo el 18 de agosto que Alo debe poblar latitud y longitud en Shopify. Alo respondió que ese dato no existe en Shopify y que Appriss debe derivarlo de la dirección. Nadie ha cerrado ese punto. Si Juan entra a la reunión sin una posición definida sobre esto, el cliente la va a pedir.

---

## A3. RCS-27389 — Alo Yoga - Incorrect data mapping

| Campo | Valor literal de Jira |
|---|---|
| key | RCS-27389 |
| summary | `Alo Yoga - Incorrect data mapping` |
| status | `Under Engineering Review` (statusCategory To Do) |
| issuetype | Incident |
| assignee | Thomas Walker (twalker@apprissretail.com) |
| reporter | krislyn vara (krislyn.vara@aloyoga.com) |
| priority | Medium |
| created | 2026-06-11T14:26:50.411-0400 |
| updated | 2026-08-15T10:08:53.439-0400 |
| resolution | null |
| resolutiondate | null |
| labels | ninguna |
| issuelinks | RCS-27470 relates to RCS-27389 (RCS-27470 está Closed) |

**Problema reportado.** Cita literal de la descripción: "Receipts are displaying incorrect transaction history and causing works items that do not meet our thresholds to populate. Please see an example below. If there are follow up questions, please schedule a call with me." Ejemplo dado: Order #36756557, work item wi=33374, con link a la plataforma.

**Cronología de comentarios**

- **2026-06-11, Deekshitha Seetharama.** Acuse automático de soporte.
- **2026-06-22, Carolyn Allison.** Toma el ticket: "I have taken ownership of this ticket and will be investigating it for you."
- **2026-06-24, krislyn vara.** "Do you have an update?"
- **2026-06-24, Carolyn Allison, análisis completo publicado en el ticket.** Estado que ella misma pone: "Root cause confirmed — pending fix". Causa raíz: "A Shopify order's store number is set from the raw Shopify location if it cannot be mapped to an Alo store number." Ocurre en dos capas, header y item. "The online location resolves to 40480962 instead of the online sentinel 99." Y el mecanismo del falso positivo: "Because the work item counts distinct stores per customer per day, these raw ids inflate the count and the work item fires incorrectly."
  Evidencia medida en Greenplum GP3, schema ardm_500, client_id 505: "**161 transactions with storeno > 1000000** (raw Shopify location ids) across 5 distinct ids; first_seen 2025-06-20, last_seen 2026-06-19. Split: 148 sale rows, 13 sale+return, 0 pure return."
  Sobre el ejemplo del cliente: "At item level this one order spans **four** store numbers. [...] Only 10083 is a real Alo store; the rest are raw Shopify location ids. This single order is what triggered wi=33374."
  Onset: "sale-side store synthesis introduced 2025-06-18; raw-store rows first appear 2025-06-20. Ongoing."
  Atribución: "This is **not** a Secure platform (ENG) bug and **not** customer-side data." Owner: DataOps Platform, repo shopify_mapping.
  Plan de siete pasos, incluye el punto 6: "Reload affected history. After the fix deploys, reload affected Alo transactions (2025-06-20 onward) so existing work items reflect corrected store assignment."
- **2026-06-24, Carolyn Allison, al cliente.** Versión suavizada: "It appears a set of online orders, and items within some orders, are being associated with a specific location identifier rather than being recognized simply as online. [...] This affects a specific set of transactions rather than your data as a whole."
- **2026-06-24, Carolyn Allison, interno a Thomas Walker.** Traspaso con el análisis.
- **2026-06-25, Shandana Khan.** "we need to ensure we're tracking any significant effort spent on this in ENG - please flag if this is something you need to own and not a quick fix"
- **2026-07-02, J.R. Teagle.** El comentario comercial que importa: "@Thomas Walker any rough ETA on when you'll be able to review this one? **Alo is chasing us saying they don't want to buy anything else from us (we're trying to get them to go with sidekick) until we get these issues resolved.**"
- **2026-07-03, Thomas Walker.** "Im testing the fix for this one today. Will update when i've verified it's working in staging"
- **2026-07-06, Aimee Wadsworth.** "We have a status meeting with the customer on 7/7 - could you please provide an update?"
- **2026-07-07, Thomas Walker.** "I currently have a fix for this in Staging but same as the other ticket **we are still figuring out how to handle distribution centres (purchase in store, fulfilled by distribution centres).** Once i've had my meeting with Paul in 2 hours we will make a decision on how to deal with them or whether to go ahead with the 90% fix"
- **2026-07-07, Aimee Wadsworth.** Pega una captura con update de Tom y pide a Carolyn Allison confirmar los hallazgos.
- **2026-07-08, Carolyn Allison.** Verificación: "I ran the same report in production that the customer showed in the description and the data already looks corrected." Añade que en GP1 dev "The order does not exist in GP1, but there is a sample of correct store numbers as well as well as some that are '99' or the longer number."
- **2026-07-23, Kristin Krogman.** "@Thomas Walker is there an update that can be provided?"
- **2026-07-23, Thomas Walker.** "Apologies I should have updated this ticket. **The fix for this should be in production now. Any new or updated orders should have the correct values**"
- **2026-07-23, Kristin Krogman, al cliente.** "The fix has now been deployed to production. Please be advised that **this correction is not retroactive; it will only impact orders placed or updated subsequent to the implementation of the fix.**"
- **2026-07-23, Automation for Jira.** "Resolution Details has been set to: Engineer Resolved - Bug - Resolved w/ Release"
- **2026-08-14, krislyn vara.** Reapertura desde el cliente, con síntoma nuevo: **"Our ship from store orders are flagging as in-store purchases & causing the 'impossible travel' work item to flag orders that do not actually meet the threshold."** Dos capturas adjuntas.
- **2026-08-14, Automation for Jira.** "Thank you for your email. Given that this ticket was previously closed, we will carefully assess your comments. If necessary, we will provide further evaluation."

**Quién tiene la pelota.** Appriss, específicamente ingeniería. El cliente reportó un síntoma nuevo el 14 de agosto y **nadie de Appriss ha respondido en el ticket**. El único movimiento posterior es el `updated` del 2026-08-15T10:08:53, y en Jira no consta qué comentario o cambio lo produjo. Van 18 días de silencio de Appriss.

**Siguiente paso comprometido.** Ninguno escrito después del 14 de agosto. Lo último que Appriss comprometió fue el arreglo del 23 de julio, que el cliente ya declaró insuficiente.

**Tickets enlazados.** RCS-27470 "Alo Yoga - Location ID populating randomized numeric value as opposed to name", Closed, resolutiondate 2026-07-23T09:27:50.153-0400. Mismo arreglo según Carolyn Allison.

**Alertas para la reunión.** Tres.
Primero, el reclamo comercial de J.R. Teagle del 2 de julio queda escrito en Jira: Alo no quiere comprar nada más hasta que estos problemas se resuelvan. Segundo, el arreglo del 23 de julio se comunicó al cliente como no retroactivo, y el análisis de Carolyn pedía explícitamente un reload del histórico desde 2025-06-20 que no consta que se haya hecho. Tercero, el síntoma nuevo del 14 de agosto sobre "ship from store" e "impossible travel" no ha recibido respuesta. Ese es el hueco más visible del dossier.

---

## A4. RCS-26196 — Appriss Internal: ALO Yoga 505 ardm_json_loader: data quality fixes required in ardm_500 & Snowflake replication

| Campo | Valor literal de Jira |
|---|---|
| key | RCS-26196 |
| summary | `Appriss Internal: ALO Yoga 505 ardm_json_loader: data quality fixes required in ardm_500 & Snowflake replication` |
| status | `Accepted into Development` (statusCategory In Progress) |
| issuetype | SOW Estimation |
| assignee | Thomas Walker (twalker@apprissretail.com) |
| reporter | James Fitton (jfitton@apprissretail.com), cuenta inactiva en Jira |
| priority | Medium |
| created | 2026-03-26T18:25:00.030-0400 |
| updated | 2026-08-27T11:20:00.717-0400 |
| resolution | null |
| resolutiondate | null |
| labels | `engage-dataverse-client-data-defect` |
| issuelinks | Relates to AREQ-1734 (Done), Relates to RCS-27557 (Work in progress), is cloned by ENG-5223 (Done) |

**Ojo con este ticket.** El summary dice "Appriss Internal". El reporter es de Appriss, no de Alo. **No es un ticket que el cliente haya abierto ni que el cliente vea.** Aparece en el dossier porque está abierto, es sobre datos de Alo Yoga, y bloquea la Engage Opportunity de Alo. No lo lleves a la reunión como ticket del cliente.

**Problema reportado.** La descripción es un análisis técnico largo. Contexto literal: "This ticket is raised following an investigation by The Retail Equation (jfitton@apprissretail.com) into data quality issues blocking the ALO Yoga Engage Opportunity (see AREQ-1734). Engage Opportunity dashboard we're building on top of ardm_500 can't reliably replicate what Secure shows."

Cinco bugs documentados en `OrderJsonToARDM.cs` del Azure Function `ardm_json_loader`:

1. **TRADINGDAY.** Usa `end_date_time` en lugar de `date_time`. "For exchange orders processed weeks after original purchase, TRADINGDAY reflects the exchange processing date, not the actual transaction date." Además guarda solo fecha sin hora.
2. **TICKETNO.** "The value is correctly assigned in C# but the column is absent from the Snowflake INSERT SQL statement. As a result, TICKETNO is always NULL in ardm_500 for every ALO Yoga record." Confirmado NULL en tres órdenes. "TICKETNO is the primary field used for transaction lookup in Appriss Secure and is required for receipt-level deep links."
3. **STORENO.** "Return events carry a Shopify location_id that does not match the Appriss store number. Purchase rows are mapped correctly; return rows are not. This means ardm_500 shows the wrong store for all return and exchange transactions."
4. **TRANSACTIONID / ORIGTRANSACTIONID.** "Purchases and returns cannot be distinguished by TRANSACTIONID, and ORIGTRANSACTIONID (which is absent from OrderJsonToARDM.cs entirely) is therefore also identical or unpopulated — making return-to-purchase linkage impossible."
5. **Datos rancios en Snowflake.** "Shopify data missing for Jan 12th - March 26th 2026"

Impacto declarado: "The Engage Opportunity for ALO Yoga cannot proceed until ardm_500 contains correct TRADINGDAY, TICKETNO, STORENO, and unique TRANSACTIONID / ORIGTRANSACTIONID values. **A data backfill for historical ALO data will also be required after fixes are deployed.**"

**Cronología de comentarios**

- **2026-03-26, Automation for Jira.** Réplica de un comentario en AREQ-1734 de James Fitton: "Opened RCS ticket for Flavio; he said there's no plan for a ardm_505 schema (like the one shown in GP3, which he thinks might be a placeholder) and that Alo is remains to be switched to the V3 standard."
- **2026-06-18, Flavio Smirne.** "all mapping issues need to go through @Paul Gardner 's team. Right now delivery is unable to help with this until we migrate to Snowflake"
- **2026-06-18, Flavio Smirne.** "@Thomas Walker can you take a look at this?"
- **2026-06-18, Paul Gardner.** "@Thomas Walker lets have a chat about this one, **changing how the dates are mapped will have multiple impacts, so we'll need to be careful.**"
- **2026-07-30, Automation for Jira**, replicando a Thomas Walker desde el ticket ENG: "Closing in favour of split tickets" con links a **ENG-6496** y **ENG-6495**.
- **2026-08-24, Aimee Wadsworth.** "Assigning to @Thomas Walker as it is a Shopify ticket/issue."
- **2026-08-25, Jenny Wang.** El comentario técnico más reciente. Pega datos de las tablas header, event e item para la orden 7170735047015 y concluye: "**Based on these values, we believe bugs 1, 2, 3, and 4 should all have been resolved.** We're in disagreement on the TransactionID mentioned in bug 4. The TransactionID should be the same for the same order number, and the id column in the event table can distinguish between each event. We also noticed that **some of the original sales information is missing from the item table for exchanges and returns.** It would be nice to have, but it's not a showstopper."

**Quién tiene la pelota.** Ingeniería, Thomas Walker. Jenny Wang afirmó el 25 de agosto que los bugs 1 a 4 parecen resueltos y planteó un desacuerdo técnico sobre el diseño de TRANSACTIONID. No hay respuesta de Thomas Walker en el ticket. El `updated` del 27 de agosto a las 11:20 no tiene un comentario asociado, así que no consta en Jira qué lo produjo.

**Siguiente paso comprometido.** Ninguno escrito con fecha. El trabajo se partió a ENG-6495 y ENG-6496 el 30 de julio, y el estado de esos dos no se consultó para este dossier.

**Tickets enlazados.** AREQ-1734 "Engage Opportunity - Alo Yoga" (Done, High). RCS-27557 (Work in progress). ENG-5223 "Shopify - Data Quality Fixes" (Done, Low), relación clones. Mencionados en comentarios sin link formal: **ENG-6495** y **ENG-6496**.

**Alerta para la reunión.** El bug 5 y el backfill histórico no aparecen resueltos en ninguna parte. Jenny Wang solo se pronunció sobre los bugs 1 a 4. El ticket sigue abierto con estado `Accepted into Development` desde antes del 18 de agosto y el desacuerdo sobre TRANSACTIONID está sin cerrar.

---

# GRUPO B — cerrados después del 18 ago 2026

**Vacío.** Cero tickets.

Verificación explícita, para que nadie tenga que rehacerla:

| Ticket de Alo Yoga en estado Done con actividad reciente | resolutiondate | updated |
|---|---|---|
| RCS-28297 | 2026-08-13T09:56:56.946-0400 | 2026-08-13T09:57:04.836-0400 |
| RCS-28296 | 2026-08-13T09:56:31.774-0400 | 2026-08-13T09:56:37.123-0400 |
| RCS-28293 | 2026-08-13T09:56:09.155-0400 | 2026-08-13T09:56:14.710-0400 |
| RCS-28183 | 2026-08-12T06:31:38.634-0400 | 2026-08-12T06:31:44.491-0400 |
| RCS-28092 | 2026-08-05T00:31:38.598-0400 | 2026-08-05T00:32:09.355-0400 |

Los cuatro primeros son SOW de "Mass Clearing of a Work Order" con resolution `Resolved`. Todos cerrados antes del 18 de agosto. Ninguno cae en el grupo B.

Cerrados anteriores del mismo cliente, por si el cliente los saca a colación:

| key | summary | created | resolutiondate |
|---|---|---|---|
| RCS-27780 | Alo Yoga  - No Access | 2026-07-11 | 2026-07-13T12:43:30.644-0400 |
| RCS-27568 | Alo Yoga-Can you update the rolling weeks from 6 to 12 in ALO | 2026-06-26 | 2026-06-26T11:48:28.513-0400 |
| RCS-27508 | Alo Yoga - Work item not populating correct information | 2026-06-22 | 2026-07-23T16:51:43.201-0400 |
| RCS-27470 | Alo Yoga - Location ID populating randomized numeric value as opposed to name | 2026-06-17 | 2026-07-23T09:27:50.153-0400 |

---

# GRUPO C — nuevos desde el 18 ago 2026

**Vacío.** Cero tickets.

El ticket de Alo Yoga más reciente por fecha de creación es RCS-28108, creado el 2026-07-31T15:41:10.393-0400. La consulta `project = RCS AND created >= "2026-08-15" AND (text ~ "Alo" OR text ~ "yoga" OR text ~ "aloyoga")` devuelve cero filas.

**Límite de esta afirmación, dilo si te lo preguntan.** La búsqueda es por texto indexado. Un ticket de Alo Yoga creado después del 18 de agosto que no mencione "Alo", "Yoga" ni "aloyoga" en summary, descripción o comentarios no aparecería. No se consultó un campo de organización o cliente porque no se identificó uno en el esquema de RCS durante esta recolección.

---

# SECCIÓN D — referencia cruzada, no es ticket de Alo Yoga

## RCS-27598 — Guess - Izenda reports will not export/download and dates are disappearing since switchover to new URL

| Campo | Valor literal de Jira |
|---|---|
| key | RCS-27598 |
| status | `Work in progress` |
| assignee | Viraj Kansara (vkansara@apprissretail.com) |
| reporter | Stephanie Benedetti (sbenedetti@guess.com) |
| created | 2026-06-29T14:26:13.003-0400 |
| updated | 2026-09-01T12:04:08.611-0400 |
| labels | `60daysopen`, `EB&F_scheduled` |

**Por qué está aquí.** El cliente es Guess. Salió en la búsqueda porque una nota interna nombra a Alo Yoga. Cita literal de Tyrone Whitney, 2026-07-02, sección "Scope — Not Guess-Specific":

> "This likely affects all ✓ Complete PC-mode tenants with Prod Sync = N: Guess, Tailored Brands, Casey's, Chemist Warehouse, WSS, PVH, **Alo Yoga**, Secure Integration. Recommend Engineering validate export AND SQL compilation across all completed tenants."

El defecto es el pipeline de export y compilación de queries de Izenda en modo Platform Cohesion. Un fix se liberó a producción el 2026-08-27 según Viraj Kansara. Guess reportó el 2026-09-01 que sigue mal: "The dates are not updating properly and its exporting is intermittent. [...] It took over 5 minutes to ultimately not update and revert back to the original dates it had before I started."

**Qué hacer con esto.** No consta en Jira que nadie haya validado el export de Izenda en el tenant de Alo Yoga. La recomendación de Tyrone del 2 de julio de validar todos los tenants no tiene respuesta escrita. Si Alo Yoga usa Izenda, hay un riesgo latente que Appriss identificó hace dos meses y no verificó. No lo menciones al cliente sin verificarlo primero.

---

# Lo que falta y hay que verificar antes de la reunión

1. **RCS-27389, el reporte del 14 de agosto.** El cliente reportó que "ship from store orders are flagging as in-store purchases" y que el work item "impossible travel" dispara falsos positivos. Appriss no ha respondido en 18 días. Es el hueco más expuesto del dossier. Verifica si alguien trabajó esto fuera de Jira antes de entrar a la reunión.
2. **RCS-27389, el reload histórico.** El plan de Carolyn Allison del 24 de junio pedía recargar las transacciones de Alo desde 2025-06-20. Kristin Krogman le dijo al cliente el 23 de julio que el arreglo no es retroactivo. En Jira no consta que el reload se haya hecho ni que se haya descartado. Si el cliente pregunta por sus datos históricos, no hay respuesta escrita.
3. **RCS-27557, el desacuerdo sobre latitud y longitud.** Appriss pidió a Alo poblar el dato en Shopify el 18 de agosto. Alo respondió que el dato no está en Shopify y que Appriss debe derivarlo de la dirección. Thomas Walker no ha contestado desde el 20 de agosto. Necesitas una posición antes de la reunión.
4. **RCS-26196, estado real de ENG-6495 y ENG-6496.** El trabajo se partió a esos dos tickets el 30 de julio. No se consultaron. Sin su estado no se puede decir qué está entregado del cluster de bugs del `ardm_json_loader`.
5. **RCS-26196, bug 5 y backfill.** Jenny Wang solo se pronunció sobre los bugs 1 a 4. El bug de datos rancios de Snowflake (enero 12 a marzo 26 de 2026) y el backfill histórico no tienen estado en Jira.
6. **RCS-28108, descripción vacía.** El ticket no tiene descripción en Jira. El contenido del reporte vive solo en capturas de pantalla adjuntas. Si necesitas el detalle del problema, hay que abrir las imágenes en la interfaz de Jira.
7. **RCS-28108, silencio del cliente.** Krislyn vara no responde desde el 20 de agosto. Es la ocasión para pedirle la confirmación en persona y cerrarlo, o para reabrir la investigación si sigue roto.
8. **RCS-27389 y RCS-26196, cambios sin comentario.** RCS-27389 tiene `updated` 2026-08-15T10:08:53 y RCS-26196 tiene `updated` 2026-08-27T11:20:00, ninguno con comentario asociado. Fueron cambios de campo o de estado. Para saber qué pasó hay que mirar el changelog en la interfaz de Jira. No se consultó en esta recolección.
9. **Izenda en el tenant de Alo Yoga.** Ver sección D. Riesgo identificado el 2 de julio, nunca validado para Alo.
10. **Camila Espinosa.** La consulta `assignee WAS "Camila Espinosa"` sobre tickets de Alo Yoga devuelve cero resultados. Según el historial de Jira, ella nunca fue asignada a un ticket RCS de Alo Yoga. La resolución del nombre de usuario en JQL no se confirmó de forma independiente, así que trata este punto como indicativo y no como cerrado.

# ANEXO — detalle de los cinco SOW de Mass Clearing cerrados en agosto

Datos leídos en vivo de Jira el 1 sep 2026. Solo lectura. Todo valor ausente se marca como "no consta en Jira".

Nota sobre el campo resolución: el campo `resolution` de Jira vale `Resolved` en los cinco. El texto más específico ("Support Resolved - Performed Customer Requested Operation" y variantes) proviene del campo Resolution Details, que Automation for Jira registra como comentario. Se anota por separado en cada ficha.

## RCS-28297

- Summary exacto: Alo Yoga - Mass Clearing of a Work Order (Low Value Transactions with a Low Value Item)
- Tipo: SOW. Prioridad: Medium
- Status literal: Closed
- Resolution literal: Resolved
- Resolution Details según comentario de automatización: Support Resolved - Performed Customer Requested Operation
- Assignee: Diego Buelvas (dbuelvas@apprissretail.com)
- Reporter: Martin Medina (martin.medina@aloyoga.com), Internal Investigations Manager
- Created: 2026-08-11 13:24:20 -0400
- Resolutiondate: 2026-08-13 09:56:56 -0400
- Updated: 2026-08-13 09:57:04 -0400

Qué pidió el cliente. Limpiar y cerrar los work items del work order "Low Value Transactions with a Low Value Item" con fecha 30 de junio o anterior. Pidió limpiar todos los items asignados y sin asignar, y declaró 302 items en ese work order.

Qué hizo Appriss y cuándo. El 11 de agosto Neha Haridas acusó recibo. El 12 de agosto a las 09:18 Diego Buelvas tomó el ticket. Ese mismo día a las 09:25 pidió a Medina desambiguar el alcance, porque la descripción mezclaba dos criterios: opción A, limpiar los 302 items sin importar la fecha; opción B, limpiar solo los creados el 30 de junio o antes. El 13 de agosto a las 09:44 envió seguimiento por falta de respuesta. A las 09:48 Medina contestó "Thank you. Please close as it has been resolved." A las 09:53 Buelvas cerró con la nota interna "WI were abandoned correctly."

Cifras. El cliente declaró 302 items en la descripción. Cuántos work items abandonó Appriss no consta en Jira. El rango de fechas efectivamente aplicado tampoco consta en Jira.

Condiciones y pendientes. La pregunta de alcance A contra B nunca recibió respuesta explícita. Medina pidió cerrar sin elegir opción. La nota de cierre afirma que los work items quedaron abandonados correctamente y no dice qué criterio de fecha se usó. A las 09:55 Medina escribió "Resolved" sobre el ticket ya cerrado y la automatización respondió que evaluará el comentario si es necesario.

## RCS-28296

- Summary exacto: Alo Yoga - Mass Clearing of a Work Order (Multiple Stores Visited on Same Day)
- Tipo: SOW. Prioridad: Medium
- Status literal: Closed
- Resolution literal: Resolved
- Resolution Details según comentario de automatización: Support Resolved - Performed Customer Requested Operation
- Assignee: Diego Buelvas (dbuelvas@apprissretail.com)
- Reporter: Martin Medina (martin.medina@aloyoga.com)
- Created: 2026-08-11 13:16:28 -0400
- Resolutiondate: 2026-08-13 09:56:31 -0400
- Updated: 2026-08-13 09:56:37 -0400

Qué pidió el cliente. Limpiar los work order items del work order "Multiple Stores Visited on Same Day" con fecha 1 de junio de 2026 o anterior.

Qué hizo Appriss y cuándo. El 11 de agosto Anil P acusó recibo. El 12 de agosto a las 09:19 Diego Buelvas tomó el ticket. A las 09:44 del mismo día pidió a Medina confirmar si el cambio ya se reflejaba en sus resultados de WI, con la indicación de probar en pestaña de incógnito para descartar caché. Esa redacción implica que la limpieza ya se había ejecutado. El 13 de agosto a las 09:44 envió seguimiento. A las 09:48 Medina pidió cerrar. A las 09:50 Buelvas cerró con la nota interna "WI results abandoned correctly".

Cifras. Ninguna cifra de work items limpiados consta en Jira. El total del work order tampoco consta en Jira. El único rango de fechas registrado es el del pedido: 1 de junio de 2026 o anterior.

Condiciones y pendientes. Medina nunca confirmó de forma explícita que el cambio se reflejara en su vista. Cerró tras el seguimiento. A las 09:55 escribió "Resolved" sobre el ticket cerrado y la automatización acusó recibo.

## RCS-28293

- Summary exacto: Alo Yoga - Mass Clearing of a Work Order (Same Day Cash Refunds with Refund 30 min or less after sale)
- Tipo: SOW. Prioridad: Medium
- Status literal: Closed
- Resolution literal: Resolved
- Resolution Details según comentario de automatización: Support Resolved - Performed Customer Requested Operation
- Assignee: Diego Buelvas (dbuelvas@apprissretail.com)
- Reporter: Martin Medina (martin.medina@aloyoga.com)
- Created: 2026-08-11 12:59:56 -0400
- Resolutiondate: 2026-08-13 09:56:09 -0400
- Updated: 2026-08-13 09:56:14 -0400

Qué pidió el cliente. Limpiar el work order "Same Day Cash Refunds with Refund 30 min or less after sale", cerrando todos los items asignados y sin asignar. Declaró 420 work items y una última actualización del work order el 14 de mayo de 2026.

Qué hizo Appriss y cuándo. El 11 de agosto Anil P acusó recibo. El 12 de agosto a las 09:19 Diego Buelvas tomó el ticket. A las 09:50 pidió a Medina confirmar si el cambio se reflejaba en sus resultados de WI, con la misma indicación de pestaña de incógnito. El 13 de agosto a las 09:44 seguimiento. A las 09:48 Medina pidió cerrar. A las 09:52 Buelvas cerró con la nota interna "WI results were abandoned correctly."

Cifras. El cliente declaró 420 work items y fecha de última actualización 14 de mayo de 2026. Cuántos abandonó Appriss no consta en Jira. Rango de fechas aplicado por Appriss, no consta en Jira.

Condiciones y pendientes. Sin confirmación explícita del cliente de que la limpieza se viera reflejada. Cierre a pedido tras el seguimiento. Comentario posterior de Medina "Resolved" sobre el ticket ya cerrado.

## RCS-28183

- Summary exacto: Alo yoga-Mass Clearing of a Work Order (Entire Cash Orders Refunded by Store)
- Tipo: SOW. Prioridad: Medium
- Status literal: Closed
- Resolution literal: Resolved
- Resolution Details según comentario de automatización: Support Resolved - Fixed Configuration
- Assignee: Vlad Bogus (vbogus@apprissretail.com)
- Reporter: Martin Medina (martin.medina@aloyoga.com)
- Created: 2026-08-05 12:25:37 -0400
- Resolutiondate: 2026-08-12 06:31:38 -0400
- Updated: 2026-08-12 06:31:44 -0400

Qué pidió el cliente. Una limpieza masiva parcial del work order "Entire Cash Orders Refunded by Store", cubriendo items asignados y sin asignar, limitada a los items con fecha 4 de junio e inferior. Declaró 3159 items en el work order.

Qué hizo Appriss y cuándo. El 5 de agosto Muralidhara Poojari acusó recibo. El 10 de agosto a las 07:34 Vlad Bogus publicó el script de actualización sobre `[workview].[Workview]`, que fija `StatusID = 3`, `AbandonReasonID = 5` y `AbandonReasonNotes = 'Abandoned by Support for RCS-28183'`, filtrando por `convert(date,CreatedDateTime) < '2026-06-04'`, `Headline like '%Entire Cash Orders Refunded by Store%'` y `StatusID not in (3)`. El propio comentario del script deja una advertencia abierta sobre el AbandonReasonID: "ENTER THE REASON ID ONCE YOU CONFIRM WITH THE CLIENT WHAT THIS SHOULD BE." A las 07:35 informó a Medina que los work items no se pueden borrar, solo abandonar, y que había abandonado 2576. El 11 de agosto a las 12:56 Medina respondió "Closed". El 12 de agosto a las 06:31 Bogus cerró con la nota "I have abandoned the work items as requested and the client confirmed we can close the ticket."

Cifras. Declarado por el cliente: 3159 items en el work order. Abandonados por Appriss: 2576. Filtro de fecha efectivo del script: `CreatedDateTime` estrictamente menor que 2026-06-04.

Condiciones y pendientes. El script traía un TODO expreso para confirmar el AbandonReasonID con el cliente. Que esa confirmación ocurriera no consta en Jira. El filtro usa "menor que 2026-06-04", lo que excluye el propio 4 de junio, y el pedido decía "dated 6/4 and before". Esa discrepancia no se discute en ningún comentario. La restricción de plataforma quedó registrada: los work items no se borran, solo se abandonan.

## RCS-28092

- Summary exacto: Alo Yoga - Mass Clearing of a Work Order (High Weekly Amount Cash Refunds)
- Tipo: SOW. Prioridad: Medium
- Status literal: Closed
- Resolution literal: Resolved
- Resolution Details según comentario de automatización: Support Resolved - Performed Customer Requested Operation
- Assignee: Viraj Kansara (vkansara@apprissretail.com)
- Reporter: Martin Medina (martin.medina@aloyoga.com)
- Created: 2026-07-31 11:40:42 -0400
- Resolutiondate: 2026-08-05 00:31:38 -0400
- Updated: 2026-08-05 00:32:09 -0400

Qué pidió el cliente. Limpiar todos los datos del work order "High Weekly Amount of Cash refunds", asignados y sin asignar. Declaró 1532 transacciones en el work order.

Qué hizo Appriss y cuándo. Este es el ticket con la traza técnica más completa de los cinco. El 31 de julio Deekshitha Seetharama acusó recibo. El 3 de agosto a las 01:03 Viraj Kansara confirmó que estaba trabajando el pedido. El 4 de agosto a las 12:32 vinculó RCS-28039 como ticket similar en curso de identificación de work items. El 4 de agosto a las 23:52 publicó el SELECT de conteo sobre `[sqldb-prd-wus2-arp-production-505-alo-platform].[workview].[Workview]` filtrando `Headline = 'High Weekly Amount of Cash Refunds'` y `StatusID != 3`, con el desglose: 1532 sin asignar en StatusID 0, 10 asignados en StatusID 1, total 1542. El 5 de agosto a las 00:27 publicó la nota técnica de cierre con el UPDATE masivo dentro de BEGIN/COMMIT TRANSACTION, que fija `StatusID = 3`, `AbandonReasonID = 5`, `AbandonedDateTime = GETUTCDATE()` y `AbandonReasonNotes = 'Mass cleared per customer request (RCS-28092).'`. Registró verificación posterior con 0 registros abiertos remanentes y referenció RCS-27273 como ticket similar manejado por Matthew para Alo Yoga. A las 00:31 comunicó el cierre al cliente con el resumen de cifras.

Cifras. Total limpiado: 1542 registros. Sin asignar, StatusID 0: 1532. Asignados, StatusID 1: 10. El cliente había declarado 1532 transacciones, que corresponde solo a la porción sin asignar. Rango de fechas: el pedido no fijó ninguno y el UPDATE no filtró por fecha, solo por Headline y `StatusID != 3`. Tenant: Alo Yoga. Base: sqldb-prd-wus2-arp-production-505-alo-platform.

Condiciones y pendientes. La nota técnica afirma "Confirmed AbandonReasonID = 5 for this tenant" y "Confirmed with customer to clear both assigned and unassigned". Ningún comentario del cliente en el ticket registra esa confirmación. Appriss cerró el ticket por iniciativa propia el 5 de agosto y ofreció abrir un ticket nuevo ante discrepancias. Medina no comentó en este ticket.

## Patrones transversales de los cinco

1. Reporter único en los cinco: Martin Medina, Internal Investigations Manager de Alo Yoga.
2. Tipo de issue único: SOW. Prioridad única: Medium. Status final único: Closed. Resolution única: Resolved.
3. Tres dueños distintos: Diego Buelvas en los tres del 11 de agosto, Vlad Bogus en RCS-28183, Viraj Kansara en RCS-28092.
4. El mecanismo es abandono, no borrado. RCS-28183 lo dice de forma explícita: "We cannot delete the work items but we can abandon them." Los dos tickets con SQL visible usan el mismo patrón: `StatusID = 3`, `AbandonReasonID = 5`.
5. Solo dos de los cinco tickets registran cifras de work items abandonados: 2576 en RCS-28183 y 1542 en RCS-28092. Los tres de Buelvas cierran con notas de una línea sin cifra ni SQL.
6. Los tres tickets de Buelvas se cerraron el 13 de agosto entre las 09:50 y las 09:56, en una misma tanda, tras el mismo seguimiento por falta de respuesta y la misma frase del cliente pidiendo cerrar.
