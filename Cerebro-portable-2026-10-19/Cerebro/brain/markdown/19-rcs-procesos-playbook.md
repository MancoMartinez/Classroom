# RCS — Procesos & Playbook

Carpeta 19 de la base de Moscú. 230 fragmentos.

## Color Teams QA — Estructura de equipos de ingeniería
_chunk 995 · 2026-06-24 · fuente: Color Teams QA.docx_

## Color Teams — Mapa de Equipos de Ingeniería (Appriss Retail)

Documento de intake creado por Camila para preparar sesiones con cada color team. Cada equipo tiene 5 categorías de preguntas: Day-to-Day Collaboration, Communication & Escalation, Tools & Knowledge, Dependencies & Blockers, How We Can Better Support Them.

### Equipos:

Purple Team — Manager: Peter Tuttle
- Focus: Cloud and Infrastructure — on-prem & Azure infrastructure, Terraform, Azure cost optimization

Green Team — Manager: Nick Hawkins
- Focus: Apps — Platform UI, C#, ASP.NET, React, JS/JSX

Yellow Team — Manager: Kenny Vu
- Focus: Engage API — Build/manage Engage, new modules, operational support, implementation/delivery

Cyan Team — Manager: Matt Kamminga
- Focus: Incident and Audit — Legacy apps, Secure Incident & Audit, Classic Quick Entry, APIs

Blue Team — Manager: Jon Morgan
- Focus: Platform & Database Services — Snowflake/Greenplum optimization, .NET services

QA Team — Manager: Gina Pilato
- Focus: Testing — Manual/automated tests, Go/No-Go on deployments, UI testing, API & load testing

### Guia de escalacion por tipo de ticket:
- Infra/Azure/Terraform -> Purple (Peter Tuttle)
- UI/React/C#/ASP.NET -> Green (Nick Hawkins)
- Engage API/modulos -> Yellow (Kenny Vu)
- LPMS/Secure Incident/Audit/Legacy -> Cyan (Matt Kamminga)
- DB/Snowflake/Greenplum/.NET services -> Blue (Jon Morgan)
- Testing/deploys/Go-No-Go -> QA (Gina Pilato)

## DOC OFICIAL — RCS Ticket Workflow (playbook 5 fases de BJ) + mapa de espacios Confluence
_chunk 1266 · 2026-07-15 · fuente: confluence-rts-478022631425_

DOC OFICIAL (Confluence RTS, publicado por Aimee Wadsworth 15-jul-2026, creado por BJ): "Support Ticket Workflow (RCS) — New Hire Playbook"
https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478022631425

Playbook de 5 fases para cualquier ticket RCS:
1. TAKE IT & FRAME IT: tomar ownership (comentario "taken ownership, investigating"), leer TODO (descripción, comentarios, adjuntos), clasificar: Incident/Bug · Config/Change Request · SOW/Feature · Data Issue · Access/SSO.
2. RESEARCH BEFORE TOUCHING: buscar tickets relacionados/duplicados (cliente + keywords — suele haber un gemelo ya resuelto); buscar en el KB.
3. REPRODUCE / EVIDENCE: reproducir, capturar el error exacto, ejemplos concretos (record/store/user). Confirmar root cause con evidencia ANTES de escalar — no entregar una adivinanza.
4. DECIDE — fix, gather o route: feature existente no habilitada → Product Delivery (ARPFiles → QA → PROD) · comportamiento roto/error/SQL malo → Engineering · data mal/tarde → Support Data Team/DataOps · SSO/identity → Engineering/Delivery (SSO nuevo → Professional Services) · capability nueva/facturable → SOW → ProfServices/Delivery · falta info → volver al cliente primero.
5. HAND OFF O RESOLVE: handoff completo (ticket+cliente+producto, root cause confirmada, qué se hizo, qué falta, tickets precedentes, criterios de aceptación) o resolución en lenguaje de negocio sin jerga + workaround + siguiente paso.

MAPA DE ESPACIOS DE CONFLUENCE (dónde vive qué):
- RTS (Retail Tenant Support): runbooks de soporte + páginas de clientes
- RCS: guías admin de netTrack/LPMS ("Getting Started")
- PD (Product Delivery): guía ARPFiles, setup de SSO / Smart Tracks
- AALPS: SSO setup, Incident integration
- ARPDT (R&D): PRDs, referencias técnicas, release/sprint notes

3 GOTCHAS: (1) revisar la CAPA — fields no es page flow, display no es calculation, export no es email notification; (2) buscar el ticket duplicado/precedente antes de investigar a fondo; (3) confirmar root cause con evidencia antes de escalar.

Preguntas aclaratorias reutilizables: config (qué pantalla/rol exacto, end state deseado, todos o subset, quién aprueba si hay PII) · bug (pasos exactos, esperado vs real, texto del error, desde cuándo, cuántos afectados) · data/SSO (2-3 ejemplos concretos con fecha, records nuevos o migrados, SSO o login local).

Sesión 15-jul con Aimee (meeting 70): Solution Experts = TRAINERS (how-to, construir reportes/searches) vs Delivery = onboarding de clientes nuevos; cuando un cliente pasa a producción, Delivery empieza a crear tickets en el portal RCS (hay doc del proceso de transición — pedido a Aimee); todo ticket nuevo cae PRIMERO en la cola de L1 salvo que cambies status/assignee al crearlo; BJ agregará el status esperado por paso al workflow doc; Aimee fuera desde el 16-jul — dudas a BJ o cualquier L2.

## DOC OFICIAL — Support Data Team Ticket Triage (Secure 5): label, Peyman, cadencia semanal, cierre
_chunk 1273 · 2026-07-15 · fuente: confluence-rts-477555982355_

DOC OFICIAL (Confluence RTS, Aimee Wadsworth, 05-jul-2026): "Support Data Team Ticket Triage"
https://trebuco.atlassian.net/wiki/spaces/RTS/pages/477555982355

QUÉ ES: el Support Data Team (SOLO Secure 5) es responsable de los datos subidos por clientes de Secure 5: ingest de data del retailer, data incorrecta en receipts o reportes. NO monitorea otros productos.

A. ASIGNACIÓN: L1 manda todo por la cola "Waiting for Support". L2 triagea; si determina que es tema del data team, agrega el label "SuppotDataTeam" [sic — así está escrito en el doc; en la práctica los tickets llevan "Support_Data_Team"] y lo trabaja un L2 cross-trained en data. Si L2 no puede resolver: Team Ownership = "Support (Delivery dep.)", Sprint = "RCS Support Team", status = Under Delivery Review, assignee = Peyman Motlagh (él re-asigna a un engineer). Coincide con la matriz de escalación del 15-jul (chunk 1265). Otros equipos (CSM/Engineering) devuelven tickets al data team poniéndolos en Under Support Review. Critical/High → notificación email a management del data team + L1 avisa por Teams (JSM como fallback).

B. TRABAJO: Peyman monitorea la cola y asigna. Statuses que usa el data team: Waiting For Support Data Team, Work in Progress, Waiting For Customer, InQueue, InTesting, In Progress.

C. UPDATES: el engineer debe actualizar el ticket MÍNIMO una vez por semana aunque no haya cambios ("testing in progress" basta). Comentarios internal-only o customer-facing.

D. CIERRE: Complete = resuelto (con Resolution details del dropdown) pero NO cerrado; el cliente verifica y entonces se pasa a Closed.

E. SOW ESTIMATION: lo usan los CSMs para estimar trabajo/SOW; soporte (L1/L2) normalmente NO se involucra — el ticket se mueve entre CSM y engineering. Workflow: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/474627801097

## Proceso Retro/RCA con Claude — demo Dean 17-jul-2026 (playbook)
_chunk 1302 · 2026-07-17_

PROCESO RETRO + RCA CON CLAUDE (demo de Dean Korbakis, 17-jul-2026, meeting 75; transcript oficial de Teams; asistentes: Juan, Viraj Kansara, J.R.).

DOS SKILLS DE CLAUDE (las plantillas viven DENTRO de la skill — no hay doc en blanco):
1. RETRO: "create a retro using [ticket RCS] + [links de meetings/chats]" → genera worksheet RET+fecha_del_incidente+cliente (ej. RET20260711-Wegmans). Pre-llena todo lo que sabe del ticket; lo no respondido queda en blanco (se llena a mano en la sesión de retro con engineering/Data Science). Respuestas confirmadas en verde. Grabar la sesión de retro en video. Guardar copia del retro original antes de convertir.
2. RCA EXTERNO: "create RCA from this retro" → documento customer-facing (lenguaje humano, sin jerga interna). Sale a OneDrive (compartible en vivo con Camila/J.R.). Existe también RCA INTERNO (opcional, decisión de management): más detalle crudo, timestamps completos, wins/failures, análisis de chats de Teams — sirve de coaching/aprendizaje.

EDICIÓN DE PDF: en la misma conversación de Claude, pegar screenshot + "change X to Y" / "fix word wrapping" / describir el blank ("Y3: [texto]") / "undo last change". Para sesión nueva: copy-as-path del archivo y referenciarlo.

TRIGGER: el RCA externo se hace SOLO por request del cliente (no automático por P1) — se intenta resolver la explicación dentro del ticket; si el cliente lo acepta, no hay RCA.

APROBACIÓN (en orden): manager directo (Camila) → manager del departamento que tocó el issue (ej. John Morgan si fue engineering) → J.R. (VP, vista final) → se envía por la MISMA vía en que se pidió (ticket, email, o CSM).

TRACKING EN JIRA/CONFLUENCE (proyecto PBM, interno, NO customer-facing):
1. Al recibir el request: agregar label "problem management" al ticket RCS → auto-crea 2 tickets PBM (ej. PBM-425 retro + PBM-426 "Create RCA").
2. Ticket PBM #1 (retro) = information gathering: TODOS los internal notes, links de chats (secure issues channel, L1/L2/L3), docs usados. Ticket PBM #2 (RCA) = ligero.
3. "Send retro to Confluence" / "Send this RCA to Confluence" → la skill los sube al espacio Problem Management → "Root Cause Report List" (carpetas RCA2024/2025/2026; naming RCAYYYYMMDD - Cliente - Descripción). Puede caer como draft en la carpeta principal → mover a mano al folder del año.
4. Link page: en PBM #1 linkear el retro de Confluence; en PBM #2 linkear el RCA.
5. Al terminar: CERRAR los 3 tickets (RCS + 2 PBM).

LOOP ABIERTO (pregunta de Juan): si el RCA sale con investigación en curso (ej. Wegmans: Whys pendientes, migración de DB feature este quarter), normalmente el doc es "open and closed" — se explica lo resuelto + lo que se explora a futuro; casos con action items en curso son minoría.

PENDIENTES DE DEAN: documentación escrita del proceso completo en Confluence (la va a publicar y compartir) + grabación de esta sesión en SharePoint. Recomendación (Viraj/Dean): practicar creando RCAs un par de veces para saber qué funciona.

## Estilo de comunicación — escribir en mi voz, no sonar a AI
_chunk 1410 · 2026-07-29_

Regla de comunicación (2026-07-29, feedback de J.R.): los mensajes que envío en Teams/Jira/email a colegas o clientes NO deben sonar a AI. J.R. me llamó la atención porque se notaba el uso de AI en mis respuestas.

Tells de AI que debo evitar:
- Rayas largas (guion largo) en mitad de las frases. Usar comas, puntos o parentesis. Es el delator numero uno.
- Listas de tres puntos perfectamente balanceadas y vinetas pulidas dentro de un chat. En chat se escribe corrido, 2 a 4 frases.
- Muletillas tipo: Net:, One thing worth flagging, Happy to action, That said, Thanks X con raya, Just to clarify, for what it is worth, I would want your steer on.
- Gramatica y puntuacion demasiado perfectas. En chat va casual: frases cortas, contracciones, algun yeah/agreed/my bad, a veces sin mayuscula inicial.

Como debe leerse: directo, corto, humano. Primero el si/no o la conclusion, luego una razon breve. Ingles competente pero casual (soy no-nativo fluido), no florido.

Ojo: esto cambia solo el tono y la forma. La sustancia tecnica y las reglas de soporte (neutral, sin conclusiones de LP, sin especular, no escribir en Jira sin mi OK) siguen intactas.

## Informe operativo 2026-08-03 — 14 tickets de Juan con paso a paso
_chunk 1443 · 2026-08-03 · fuente: ~/Downloads/INFORME-2026-08-03.md_

# Informe del lunes
Juan Martinez, Lead Support Engineer · 3 ago 2026 · datos leídos de Jira hoy

Contenido: (1) tus 14 tickets en orden de atención, (2) el hilo de J.R. y en qué quedó, (3) lo que repartió Peyman el sábado, (4) los dos mensajes de Viraj y a quién poner, (5) el pedido de J.R. sobre Ollie's.

El análisis del backlog sin asignar va aparte, en `TRIAGE-BACKLOG-2026-08-03.md`.

---

# 1. Tus tickets, en orden de atención

Tienes **14 abiertos**: 3 High, 10 Medium, 1 Low. El orden no es el de prioridad de Jira, es el de riesgo real hoy. Cada uno trae el paso a paso.

**Rutas que se repiten, para no anotarlas cada vez:**

```
Sign-in de un tenant       https://apps.apprissretail.com/<slug>/signin
Screen Manager de un tenant https://apps.apprissretail.com/<slug>/nettrack/Admin/ScreenManager.aspx?admin=9QQP
Impersonación              Control Panel USPROD, buscar el cliente, Impersonate
DB de plataforma           sqldb-prd-wus2-arp-production-<número cliente>-<ABV>-platform
```

El número de cliente y el ABV de cada tenant salen del tracker **Incident Migration 2026**. Ejemplos que ya tienes: Santikos 411 STI, Vitamin Shoppe 433 VSE.

---

## Bloque 1: se cierran o se mueven hoy sin investigar nada

### RCS-27840 · Kohl's · Medium · Under Security Review

**Ya está resuelto y nadie se lo dijo al cliente.**

El 28 de julio Carlson Quick preguntó directo: *"Could you please confirm if these IPs are already allow-listed on your end?"* con las tres IPs. La respuesta ya existe en el RETAILIT-20526 del mismo día. Y el 30 de julio John Mason cerró el CISS con *"Nothing is required here. We dont need to do the certificate validation."*

Trabajo terminado el 30 de julio, deadline del cliente el 1 de agosto, y **6 días sin contestarle**. Resuelto pero percibido como abandonado, en un ticket de seguridad con fecha límite.

**Nota de precisión.** Ni tú ni yo tenemos acceso a RETAILIT-20526, así que la única fuente es la línea que la automatización copió a tu ticket: *"The 3 IP addresses are already part of Kohl's SFTP allow list."* Eso no dice en qué firewall vive la lista. El comentario está redactado para responder exactamente lo que Carlson preguntó sin afirmar de qué lado está, así que es correcto en cualquiera de las dos lecturas.

#### Paso a paso

1. Abre `https://trebuco.atlassian.net/browse/RCS-27840`
2. **Add comment**, tipo **Reply to customer** (el visible para el reporter), y pega el texto de abajo
3. Ahora la transición. **No busques "Completed", desde Under Security Review no existe esa ruta.** Y "Close Ticket" está en el workflow pero con condición no cumplida, por eso no te sale el botón
4. Mueve primero a **Waiting for customer**, que deja el ticket en `Under Customer Review`. Es además el estado correcto por contenido, le acabas de pedir que avise si ve interrupción
5. Desde ahí **Close Ticket** debería habilitarse. Si sigue sin salir, avísame y vuelvo a consultar las transiciones desde el nuevo estado
6. Al cerrar, si te pide **Resolution**, la que aplica es la de trabajo completado, no "Won't Do"

#### Comentario al cliente

> Hi Carlson, Kyle,
>
> Confirming the three IPs you listed are already allow-listed for the Kohl's SFTP integration, so no change was needed to keep the weekly people.txt upload running:
>
> 34.145.42.5
> 34.187.197.14
> 34.11.179.67
>
> Our InfoSec team also reviewed the certificate item and confirmed the GTS Root CA validation is not required for this integration. Nothing further is needed from Kohl's for the August 1 change.
>
> I will close this ticket out. Please reply here or reopen if you see any interruption on the weekly file.
>
> Kind regards,
> Juan Martinez
> Support Engineer

---

### RCS-28030 · Ahold · Medium · Under Customer Review

**Resuelto, solo falta la confirmación del cliente.** Matt confirmó hoy a las 11:58 que la validación y migración de timezone corrió para el resto de los usuarios de ADUSA.

**Corrección de lo que decía antes este documento.** Yo había puesto que había una llamada de una hora propuesta por Viraj y respaldada por J.R., y que la prueba de incógnito seguía pendiente. **Las dos cosas estaban mal**, salieron de mi nota del viernes sin volver a leer el ticket.

Lo que realmente pasó:
- Viraj pidió el incógnito y ofreció una llamada en **un solo comentario, el 31 jul 10:45**. No hay llamada de una hora ni respaldo de J.R. en el ticket.
- **Leigh Ann contestó 16 minutos después, el 31 jul 11:01:** *"I went into a test case this morning and attached a journal entry to the case at 9:50 AM. It was reflected correctly in the platform. I noticed a lot of users with UTC as their time zone. Would each of them have to adjusted to EST?"* O sea, **a ella ya le sale bien** y su pregunta abierta es otra: si a los demás hay que ajustarlos uno por uno.
- Chris Rippingale el 31 jul 14:26: *"Confirmed fix for one user. Run the validation and migration for all other users. Matt doing this right now."*

Consecuencia: el comentario de incógnito que se pegó hoy a las 12:48 pide algo que ella ya había resuelto e ignora su pregunta real. Hay que corregirlo con el seguimiento de abajo.

#### Paso a paso

1. **Pega el comentario al cliente de abajo hoy mismo**, para corregir el de las 12:48
2. **No muevas el estado.** `Under Customer Review` ahora sí es correcto, la pelota volvió a ella
3. Cuando confirme, comentario de cierre y transición. Si "Close Ticket" no aparece, ver la nota del workflow en el RCS-27840
4. **Avisa a Vedant por el RCS-28065**, con el mensaje de abajo, y con la pregunta de PST

⚠️ **Lo que hay que confirmarle a Matt antes de que Vedant cierre el 28065.** ADUSA va a **EST**. Stater Bros es California y su ticket dice textual *"should be PST"*. Si la corrida aplicó EST a los dos tenants, se arregló uno y se rompió el otro. Pregúntale qué zona quedó en cada uno.

#### Comentario al cliente

> Hello Leigh Ann,
>
> Please disregard my earlier message today, I had missed your update from Thursday. Thank you for confirming the journal entry showed the correct time.
>
> To answer your question about the other users showing UTC, no, they do not need to be corrected one by one. The update has now been applied across all of your users.
>
> One thing to expect. The time zone is read from the browser session, so each person will see the corrected time only after they sign out and sign back in. If anyone still shows UTC, a fresh sign in should settle it.
>
> Could you confirm with a couple of your team members once they have signed back in? Once you do, I will close this out.
>
> Thank you.

#### Comentario interno

> Matt confirmed today at 11:58 that the timezone validation and migration ran for the rest of the ADUSA users. Asked the customer to verify with a couple of team members after a fresh sign in, since Incident reads the time zone from the browser session rather than from the profile. Once she confirms, this can be closed.

#### Mensaje para Vedant

> Hi Vedant, on 28065 for Stater Bros, Matt ran the timezone validation and migration and told me it covered the other tenant too, so yours may already be fixed. Two things before you tell the customer. Incident reads the time zone from the browser session rather than the profile, so nobody sees the change until they sign out and back in, and it will look like it failed if you skip that. And Stater Bros should be PST, not EST like ADUSA, so worth confirming with Matt which zone the run actually set for them before you close it out.
---

### RCS-28023 · Ahold · Medium · Under Customer Review

Kiran ya respondió al cliente el 30 de julio con el fix amplio, así que **no mandes nada al cliente**, sería duplicar. Lo único abierto es la verificación interna que él pidió el 30 a la 1:45 PM.

#### Paso a paso

1. Consigue el nombre de la DB de plataforma de Ahold del tracker **Incident Migration 2026**, patrón `sqldb-prd-wus2-arp-production-<n>-<ABV>-platform`
2. Conéctate con tu acceso de lectura y **mira primero la forma de la vista**, porque los nombres de columna deciden la comparación:
   ```sql
   SELECT TOP 1 * FROM incident.lpuser;
   ```
3. Busca a la usuaria reportada:
   ```sql
   SELECT * FROM incident.lpuser
   WHERE email = 'leighann.stubbs@adusa.com';
   ```
4. **Lo que confirma el fix es el conteo de filas por usuario.** Si antes salían duplicadas y ahora sale una sola, está verificado:
   ```sql
   SELECT email, COUNT(*) AS filas
   FROM incident.lpuser
   GROUP BY email
   HAVING COUNT(*) > 1;
   ```
   Si esa consulta vuelve vacía para los usuarios del ticket, ya está.
5. **No consultes `lhua` para esto.** Regla de Kiran: `secure.LocationHierarchyUserAssignments` es destino de migración, no la capa que decide si puedes crear un caso. La app se maneja con la vista
6. Pega el comentario interno de abajo, **ajustado a lo que realmente viste**
7. Deja el ticket en `Under Customer Review`, no lo muevas. Kiran ya cerró el lazo con el cliente

⚠️ **El comentario afirma un resultado.** Si el paso 4 sale distinto, cambia el texto antes de pegarlo.

#### Comentario interno

> @Kiran Vadday Verified on my side. Checking the lpuser view for the reported users, they now resolve to a single row and the duplicate assignments are gone. Leaving this in Under Customer Review since you already confirmed the broad fix to the customer.

**Y no menciones los 380.** Salieron de `lhua`, que no es la capa que decide la creación de casos.

---

## Bloque 2: los High con cliente caliente

### RCS-28033 · Big Y · High · Work in progress

**Actualizado hoy a las 11:25.** Kevin Snyder contestó tus dos preguntas y encima solo tiene el auto acuse de Deekshitha de las 11:28. Es tu High con respuesta de cliente más fresca y sin atender, y por eso abre el día.

**Primero: el problema original está resuelto.** Los agentes entran por `apps.apprissretail.com/bigy/signin`. El ticket se llama "LPMS Login Issue" y ya no es eso. Lo abierto es **Add Person**, que apareció el 30 de julio. Vale decidir si lo renombras o si cierras la parte de login y sigues el Person Detail aparte, porque el título no describe el trabajo.

**Lo que dijo Kevin y por qué importa.** Afecta **solo a algunos usuarios**, y los que fallan **fallan distinto**:

| Usuario | Síntoma | Qué significa |
|---|---|---|
| Kevin Snyder | **Funciona**, puede agregar persona | La pantalla existe y es alcanzable |
| Jose Flores | Llena los campos, al guardar el spinner gira y no termina | Falla en el **guardado**, perfil de timeout de request |
| Taylor Larese | No puede ni abrir la ventana de Add Person, page not found | Falla en la **carga**, perfil de 404 de página |

**El dato que descarta lo obvio.** Un archivo faltante en el app service compartido fallaría para todos por igual, incluido Kevin. No es el caso. Entonces **el archivo ausente solo no explica esto**, y aquí manda algo por usuario: rol, permiso de pantalla o jerarquía.

**Hipótesis, marcada como hipótesis.** Las dos cosas se reconcilian si la URL se construye con contexto del usuario. En Santikos (RCS-28022) el defecto era que la app armaba la ruta **sin el tramo `screens/incident/<número de cliente>/lpms/screens/`**. Si ese tramo sale del contexto del usuario, un usuario con contexto mal resuelto recibe URL incompleta y ve 404, mientras otro entra normal. **No está confirmado.** La URL completa de Taylor lo confirma o lo mata en un minuto.

**Corrección a lo que decía antes este documento.** Yo había escrito "si faltan pantallas, Build All Screens y se prueba". **No lo corras a ciegas.** En Santikos el rebuild del 31 de julio coincidió con que la lista de incident types quedó en cero, y esa secuencia está documentada sin causalidad probada. Mirar el Screen Manager sí, reconstruir no.

#### Paso a paso

1. **Pega el comentario al cliente primero**, porque Kevin lleva desde las 11:25 con solo un auto acuse encima. Los dos pedidos técnicos van en el mismo mensaje
2. **Compara los tres usuarios**, que es lo único que aprovecha el "solo algunos". Entra al tenant y ve a `Settings > Users`:
   ```
   https://apps.apprissretail.com/bigy/signin
   ```
   Busca **Kevin Snyder**, **Jose Flores** y **Taylor Larese**, abre cada uno y compara tres cosas: **rol**, **jerarquía de ubicación asignada** y **permisos de pantalla**. Anota en qué difieren Jose y Taylor de Kevin, que es el que funciona
3. Ahí mismo resuelves el pendiente de Chris, que pidió *"Check in Settings > Users if they are signing in since this post or not"*. En esa misma pantalla se ve el último acceso
4. **Los tres contra la vista**, con la DB de plataforma de Big Y:
   ```sql
   SELECT * FROM incident.lpuser
   WHERE email IN ('kevin.snyder@bigy.com');
   ```
   Con la forma de la vista, trae las tres filas y busca la diferencia. Los correos de Jose y Taylor los pides a Kevin en el comentario, o los sacas de Settings > Users
5. **Reproduce por impersonación.** Control Panel USPROD, impersona a **Taylor Larese**, abre un caso, intenta Add Person, y **con devtools abierto en la pestaña Network** captura la URL exacta que se pide cuando aparece el 404. Eso es lo que confirma o mata la hipótesis del tramo faltante, y no dependes de que ella te la mande
6. Después impersona a **Jose Flores**, llena Add Person, dale guardar, y en **Network** mira si el request queda pendiente o devuelve error, y anota la hora exacta para cruzar contra los registros del app service
7. **Screen Manager solo para mirar**, sin reconstruir:
   ```
   https://apps.apprissretail.com/bigy/nettrack/Admin/ScreenManager.aspx?admin=9QQP
   ```
   Busca si existe la pantalla de Add Person o Person Detail y en qué Build Status y Last Build Date está
8. Pega el comentario interno para Chris con lo que encuentres

#### Comentario al cliente

> Hello Kevin,
>
> Thank you for the detail, that helps. The two users are hitting different failures, so I want to handle them separately.
>
> For Taylor Larese, the page not found means the Add Person screen is not being reached at all. Could you ask her to send the full URL from the address bar when the error appears, plus the Cloudflare Ray ID shown on the error page? That tells us whether the link being built for her account is incomplete.
>
> For Jose Flores, the fields load and the save never completes, which looks like the request timing out rather than a missing page. Could you send the date and approximate time of one of his save attempts in your local time? With that I can pull the server side records for that exact request.
>
> Since it works for you and not for them, we are also comparing the three accounts on our side for role and location hierarchy differences.
>
> On the earlier sign-in item, glad the /bigy/signin URL is working. Please make sure any saved bookmarks point to that address rather than the root domain, as the root will keep returning the block page.
>
> Thank you.

#### Comentario interno para Chris

> @Chris Rippingale Following up now. Kevin replied today, the sign-in problem is resolved, agents are getting in through /bigy/signin. What is open is Add Person, and it is user specific rather than tenant wide: Kevin can add a person, Jose Flores fills the fields but the save never completes, Taylor Larese gets a page not found on the Add Person window itself. Since the same screen works for one user and 404s for another, a missing page on the shared app service does not explain it on its own. My working hypothesis is the URL construction defect we documented on Santikos in RCS-28022, where the path was built without the screens/incident/{client number}/lpms/screens segment, which would only misfire for users whose context resolves incorrectly. That is a hypothesis, not confirmed. I am comparing the three accounts in Settings > Users and in the incident.lpuser view, and reproducing Taylor's 404 through impersonation to capture the exact requested URL.

---

### RCS-28112 · Stater Bros · High · Work in progress

El cliente confirmó que ya puede entrar casos pero traer tiendas sigue lento. La alerta #42348 sigue abierta y **se recuperó sola, no la arreglamos**. Está escalado a Jose Parocua.

**Y aquí está el punto del día:** RCS-28114 se abrió el sábado, **Critical**, mismo cliente, misma reportera (Angie Martinez), "UNABLE TO SUBMIT CASE", varias tiendas, y está a nombre de J.R. Teagle. Es la continuación de lo tuyo del viernes por la noche y **ese contexto no está en el 28114**.

#### Paso a paso

1. Abre `https://trebuco.atlassian.net/browse/RCS-28114`
2. **Add comment**, tipo **interno** (visibilidad de equipo, no Reply to customer, porque menciona otros clientes y números de infraestructura), y pega el texto de abajo
3. **Add watcher** con tu usuario, para que las respuestas de Angie te lleguen. Es la razón por la que no te enteraste el sábado
4. En el **RCS-28112**, linkea el 28114 con relación **relates to**: botón `Link` o `More > Link`, tipo `relates to`, key `RCS-28114`
5. Mándale un mensaje a J.R. ofreciendo la reproducción, no la hagas sin que él la pida, porque el ticket es suyo y ya le dijo al cliente que el equipo está encima
6. Deja la alerta #42348 abierta hasta que haya causa. Cerrarla porque se recuperó es lo que hizo que nadie escalara

#### Comentario interno

> Adding context from RCS-28112, same client and same reporter, opened Friday night. Between roughly 20:30 and 22:35 UTC on July 31 the nettrack app service showed around 2495 client timeouts against 255 HTTP 500s, with 248 of those 500s concentrated on POST /nettrack/api/internal/SendSmartAlert.aspx. Alert #42348 recovered on its own rather than being fixed, and it is still open. Case entry started working again for the reporter but pulling up stores stayed slow. My own reading of that ratio is a web request timeout rather than a SQL command timeout, since a command timeout would surface as a 500 with an exception and we don't see that volume, but that is an interpretation and not something the logs state. Happy to run the reproduction across Stater Bros, Santikos and ADUSA if that helps narrow it, since all three are July 27 wave and all three are on the shared nettrack app service.

---

### RCS-28022 · Santikos · Medium en Jira, High en realidad · Work in progress

Escalado por el Director de Seguridad del cliente. Dos partes siguen fuera de Support: el archivo `ShowAttachments.aspx` ausente en el deployment compartido, y los cero items en `fld_MasterCase_CaseType`.

**Lo que falta no es investigación tuya**, es una revisión del filesystem del app service que ya nadie ha hecho. Y esa misma revisión cubre 28058 (Stater Bros), 28124 (ADUSA) y posiblemente 28101 (Costco).

#### Paso a paso

1. Mándale el mensaje de abajo a **Matt Kamminga** por Teams. Es una petición de una sola acción para cuatro tickets, eso es lo que la hace pasar
2. Llévalo también a la reunión de triage como petición formal, para que quede con dueño y no en un chat
3. Mientras eso avanza, en el ticket **no dejes de hablar con Maricela**. Lleva desde el 29 de julio sin servicio en la función principal
4. La segunda parte, los cero incident types, **no la persigas todavía**. Está documentada en la nota interna y depende de saber si el rebuild puede vaciar listas, que es la misma pregunta abierta del 28033

#### Mensaje para Matt

> Hi Matt, one request that covers four tickets instead of one. Could someone check the filesystem of the shared nettrack app service for the pages under /nettrack/lpms/, specifically whether ShowAttachments.aspx is present in the current deployment? On Santikos the 404 comes from ASP.NET's own CheckVirtualFileExists, so the file is genuinely absent rather than misrouted. Stater Bros 28058 and ADUSA 28124 look like the same gap from the customer side, and Costco 28101 fails on upload rather than read. While someone is in there, the allowed extension list and the size limit would answer 28124 and 28101 in one go. Right now that is four parallel investigations for what might be one deployment gap.

---

### RCS-27991 · Appriss interno · High · Work in progress

Engage Analytics no puebla secciones. Sin tocar desde el 30 de julio.

**Hallazgo:** RCS-28068 (lululemon, "Top 10 SKUs and Consumers not loading", sin asignar desde el 30 de julio) es el mismo síntoma en el mismo dashboard. El tuyo es interno, el de lululemon es un cliente esperando.

#### Paso a paso

1. Abre `https://trebuco.atlassian.net/browse/RCS-28068` y asígnatelo, o llévalo a la reunión como tu ticket del reparto
2. Linkea los dos: en el 28068, `Link > relates to > RCS-27991`
3. **Comenta el 28068 hoy**, aunque no tengas causa. Lleva 4 días con solo el auto acuse y la clienta ya probó cambiar rangos de fecha, o sea descartó lo obvio sola
4. Trabaja uno solo. Si el interno y el del cliente tienen la misma causa, una investigación cierra los dos

#### Comentario al cliente para el 28068

> Hello,
>
> Thank you for the detail, and for noting that adjusting the date ranges made no difference, that helps narrow it.
>
> We have the same behaviour reproduced on our side in the Top 10 tables of the Engage Analytics dashboard, so this is being looked at as a platform item rather than something specific to your configuration. I am picking it up directly and will update you as soon as I have something concrete.
>
> Thank you for your patience.

---

## Bloque 3: esperando a alguien más, mantener el pulso

### RCS-28032 · Vitamin Shoppe · Work in progress
Joe Austin lleva **5 días** sin responder, tu último comentario fue el 29 de julio.

**Paso a paso.** Un solo mensaje a Joe cubre tres tickets, así que no mandes tres. Pide en el mismo comentario: si Brandon sigue bloqueado (28032), un ejemplo concreto de audit con nombre, tienda y número de caso (28005) y el screenshot con URL, error completo, Ray ID y número de tiendas (28084). Después avisa a los dueños de los otros dos que el pedido salió consolidado.

> Hello Joe,
>
> Following up on this one. Login to the Incident platform is working on our side, so I need to confirm whether Brandon is still seeing the error. If he is no longer blocked, I will close this ticket. If the error is still there, a screenshot of what he sees would let me pick it up from where we left off.
>
> While I have you, two other open items would move much faster with a detail from your side. For the audit item, a concrete example with the audit name, store and case number. For the timeout item, a screenshot showing the full error and the Cloudflare Ray ID on the page, plus roughly how many stores are affected.
>
> Kind regards,
> Juan Martinez
> Support Engineer

### RCS-28021 · Ahold · Resolution Suggested
Jie Chen confirmó que era configuración del reporte, un join mal armado, no capacidad de plataforma.

**Paso a paso.** Recordatorio al cliente pidiendo la validación, y si no contesta en 48 horas se cierra por resolución sugerida. Y no lo cuentes como evidencia de degradación del origen en ninguna conversación de timeouts, contamina la muestra.

### RCS-27959 · PACSUN · Under Customer Review
Whitelisting de IPs para MuleSoft. **Mismo cliente que el 28040 de Viraj.**

**Paso a paso.** Que quien tome el 28040 se lleve este también, ver sección 4. Una sola relación con PSEB.

### RCS-27765 · Winn-Dixie · Under Customer Review
Data file check, sin movimiento desde el 27 de julio. **Paso a paso:** recordatorio de estado, es lo único que falta.

---

## Bloque 4: los que se están envejeciendo en silencio

### RCS-27573 · Tahoe Donner · Medium · **38 días** (26 jun)
Error persistente entrando incident reports. Es tu ticket más viejo y es funcional, no una pregunta.

**Paso a paso.** Decide hoy una de dos y no una tercera: o entra en tu semana con fecha, o le dices al cliente dónde está. Lo que no puede seguir es en silencio a los 38 días. Si no entra esta semana, este comentario:

> Hello,
>
> I want to be straight with you about where this sits. The error you reported is still open on our side and has not had the attention it should have had, largely because of the platform work of the last few weeks.
>
> I am picking it back up. To restart it cleanly rather than from old notes, could you confirm whether the error is still happening, and send a screenshot of the current message along with the approximate time it last occurred?
>
> Thank you for your patience.

### RCS-27941 · Tailored Brands · 12 días
SSO y permisos en Incident, sin tocar desde el 29 de julio. **Paso a paso:** revisa si el síntoma cae en el patrón de rol y jerarquía del G2 del triage, porque si sí, entra en la investigación de Diego y no en la tuya.

### RCS-27676 · Ralph Lauren · Low · 28 días
Cambio de IP y hostname de SFTP. **Paso a paso:** es el mismo tipo de trabajo que el 27840 de Kohl's, va por Infra con ticket RETAILIT. Mira si ya hay uno abierto antes de crearlo.

---

## El orden, resumido

| # | Ticket | Primera acción concreta |
|---|---|---|
| 1 | **RCS-28033** | Comentario a Kevin, y comparar los tres usuarios en Settings > Users |
| 2 | **RCS-27840** | Comentario, mover a Waiting for customer, cerrar |
| 3 | **RCS-28114 / 28112** | Comentario interno, ponerte como watcher, linkear |
| 4 | **RCS-28030** | Comentario de corrección al cliente, y avisar a Vedant con la pregunta de PST |
| 5 | **RCS-28022** | Mensaje a Matt, una revisión para cuatro tickets |
| 6 | **RCS-28023** | Correr la consulta de duplicados, comentario interno a Kiran |
| 7 | **RCS-27991 + 28068** | Linkear y comentar el del cliente |
| 8 | **RCS-28032** | Un pedido consolidado a Joe Austin por tres tickets |
| 9 | **RCS-27573** | Decidir: entra con fecha o se le dice al cliente |
| 10 | El resto | Por estado normal |
---

# 2. El hilo de J.R. y en qué quedó

Tu respuesta pasó. J.R. contestó el sábado a las 11:41: *"Eso me funciona bien, Juan."*

Eso significa que **hoy no arrancas leyendo la cola en frío**, arrancas con la cola ya agrupada, que es exactamente lo que quedó autorizado. El documento `TRIAGE-BACKLOG-2026-08-03.md` es ese primer pase, hecho.

Lo que cambió desde el viernes: Peyman movió la cola de 40 a 26 el sábado, pero **entraron 9 nuevos entre sábado y hoy**, así que hoy hay **37 sin asignar**. Vale decirlo al abrir la reunión, porque si no, parece que el trabajo del sábado no sirvió, y sí sirvió.

---

# 3. Lo que repartió Peyman el sábado

Peyman se movió solo sobre la cola y bajó de 40 a 26. Reparto que hizo:

| Ticket | A quién | Nota |
|---|---|---|
| RCS-27935 | David Beck | |
| RCS-28079 | Ian Williams (Engage Engineering) | "He will advise" |
| RCS-27977, RCS-27983 | Peyman | En el 27983 pidió ayuda a Adrash Kumar |
| RCS-27978, RCS-27951, RCS-28047 | Sebastian Rueda | |
| RCS-27951, RCS-28016, RCS-28017 | Vlad | ⚠️ **27951 aparece dos veces**, a Sebastian y a Vlad. Uno de los dos va a trabajar en algo que ya tiene dueño. Vale aclararlo antes de la reunión |
| RCS-28008 | Carl Costelow | Home Depot. Peyman cree que termina en Engineering. En Jira hoy figura a nombre de **David Parraga**, en Under Delivery Review, tocado hoy a las 06:35. O Carl lo reasignó o Peyman se equivocó de nombre. Verifica |
| RCS-28074 | Nikita Rathore | Lulu, nuevo tender type Google Pay eComm. Confirmado en Jira |
| RCS-28086 | Edwin Garzon | Kohl's, NULL EndTransDateTime. Confirmado en Jira |

**Dos cosas para ti como lead:** el 28074 y el 28086 entraron a tu equipo sin pasar por ti, así que Nikita queda en 9 y Edwin en 9. Eso cambia la aritmética del reparto de hoy. Y el duplicado del 27951 es un choque real que cuesta horas si nadie lo ve.

**Nota de nombres:** el "Sebastian" de Peyman es **Sebastian Rueda**, de tu equipo. **David Beck no es de tu equipo**, el David del equipo es **David Vargas**. Vale tenerlo claro al hacer seguimiento, porque son personas distintas.

---

# 4. Los dos mensajes de Viraj

## 4.1 RCS-28040, PSEB / PacSun, reunión el martes 10 am PST

**Qué es de verdad.** No es "necesito la URL de test". Eso ya se lo dio Viraj el 29 de julio (`https://pacsun-qa.apprissretailcloud.com/`). El problema real está dos comentarios más abajo: Roseanne Auran entra a la pantalla de Appriss, le sale el **Microsoft Sign In**, y no le acepta ninguno de sus dos correos. Ella misma da la pista buena: *"We had this problem before when we switched from PACIFIC SUNWEAR to PACSUN in our email addresses."* Y el 31 de julio empeoró, ya no puede ni cargar el sitio, le sale error de acceso.

O sea: **identidad y federación en el entorno QA de Secure 5, con un cambio de dominio de correo de por medido**. No es un problema de datos ni de reporte.

Contexto de la reunión: la agenda la maneja **Paul Marderosian** (CSM), y él la unificó con el tema de credit card number vs account number que Roseanne también tenía abierto. Invitación ya enviada para el martes 4 a las 10 am PST, o sea **12 del mediodía hora Colombia**, horario cómodo. Paul puso a Tyler y Carlos como opcionales, y Carlos Jacinto ya está desactivado en Jira, así que ese asiento está vacío de verdad.

**Mi recomendación: Luis Hernandez.**

Los candidatos reales de Colombia en tu equipo son cinco: Diego Buelvas, Sebastian Rueda, Edwin Garzon, Luis Hernandez y David Vargas.

| Persona | Puesto | Abiertos | Ajuste al problema |
|---|---|---|---|
| **Luis Hernandez** | **Senior Full Stack Engineer** | **0** | **El mejor por las dos vías.** El fallo es de identidad y federación en la capa de aplicación, no de datos, y eso es full stack. Siendo senior sostiene la llamada con Roseanne y con Paul sin escalar. Y está en cero, así que no hay argumento de carga contra |
| David Vargas | Full Stack Engineer | 8, pero 6 esperando cliente | Perfil correcto y carga activa real de 2. Es el respaldo |
| Diego Buelvas | Full Stack Engineer | 7 | Perfil correcto pero tiene tres High encima, incluidos 28078 y 28084. No le cargues una llamada de cliente |
| Sebastian Rueda | Senior Data Engineer | **13** 🔴 | Descartado. Es perfil de datos y además el segundo más cargado del equipo, con un Critical y un High activos |
| Edwin Garzon | Data Engineer | 9 | Mismo caso, es de datos |

Carga verificada de todo el equipo: Vedant 21, Juan 14, Sebastian 13, Bikash 10, Nikita 9, Edwin 9, David Vargas 8, Diego 7, Gulshan 5, **Luis 0**.

Respuesta para Viraj (un párrafo, es Teams):

> Hi Viraj, I'd put Luis Hernandez on 28040 and on the Tuesday call. What's failing is the Microsoft sign in on the QA tenant rather than anything on the data side, so it needs a full stack pair of eyes, and being senior he can hold the call with Roseanne and Paul without escalating. Worth noting the ticket has drifted from the original ask, Roseanne has the URL already, what she can't get past is the sign in, and she points at the PACIFIC SUNWEAR to PACSUN domain change as having caused something similar before. We also have RCS-27959 open for the same client, so I'd keep both with whoever takes this one.

## 4.2 "Can we meet today later to review unassigned queue and tickets for guys who left?"

Sí, y llegas con datos. Dos hallazgos concretos para esa reunión:

**Carlos Jacinto está desactivado en Jira y sigue con dos tickets abiertos a su nombre:**

| Ticket | Cliente | Prioridad | Edad | Estado |
|---|---|---|---|---|
| **RCS-27549** | ICA SE | **High** | **39 días** (25 jun) | Work in progress. "Degraded system performance, slow response times and delayed loading". El cliente pidió explícitamente root cause analysis |
| RCS-27762 | SSP Group | Medium | 24 días | Secure 3 usando MDS completo en vez de MDS Lite |

El 27549 es lo grave: un **High de rendimiento, con petición formal de RCA, en manos de una cuenta desactivada, hace 39 días**. Y en la cola sin asignar está **RCS-27994**, también de ICA, también lentitud, abierto el 28 de julio. Mismo cliente, mismo síntoma, uno huérfano y el otro sin dueño. Van juntos al mismo dueño y hoy.

De Tyrone no encontré tickets abiertos a su nombre en RCS, así que su traspaso a Vedant sí se completó. Los cuatro (28058, 28062, 28063, 28065) están a nombre de Vedant, confirmado.

**Consecuencia de eso que vale decir en voz alta:** Vedant quedó en **21 abiertos**, el más cargado del grupo por mucho. Tú vas segundo con 14. Si hoy repartimos por "el que menos tiene", Vedant no recibe nada.

Y el punto de proceso que Viraj ya planteó el viernes y tiene razón: pedir que quien se va deje **OOO permanente** en Teams y que su cola se vacíe antes del último día, no después. Vale llevarlo como acción a J.R., porque un High de 39 días en una cuenta muerta no lo agarra ninguna alerta.

Respuesta para Viraj (un párrafo, es Teams):

> Hi Viraj, yes let's meet, I'll come with the 37 unassigned already grouped. On the people who left, Carlos still has two tickets under his deactivated account and one is RCS-27549, an ICA performance High open 39 days with a formal RCA request, plus RCS-27994 is another ICA slowness ticket unassigned since the 28th, so those two need one owner today. Tyrone's four did move to Vedant so that one is clean, though Vedant is now at 21 open and shouldn't be in today's round. And I'm with you on the permanent OOO, a 39 day High on a dead account is not something any alert catches.

---

# 5. El pedido de J.R. sobre Ollie's, RCS-28085

**Contexto que J.R. no puso en el mensaje.** El ticket está **sin asignar** desde el 31 de julio a las 08:11. Lo único que tiene es el auto acuse de Shireesh Ramdas un minuto después. **Cero contacto humano en 3 días.** Eso es lo que hay que arreglar primero, antes de investigar nada.

**Qué reporta el cliente.** Charity Mackey (cmackey@ollies.us): el RLPM **Scott Blackwell** aparece como **DLPM** y perdió accesos, entre ellos aprobar casos enviados por DLPMs. Antes estaba bien. El IT de Ollie's ya confirmó que el archivo de empleados que nos manda trae el rol correcto, RLPM.

**Lo que significa técnicamente.** Si el archivo entra correcto y el sistema resuelve mal el rol, el problema está del lado de la resolución de rol y jerarquía, no del feed. Y ahí no está solo:

| Ticket | Cliente | Síntoma | Estado |
|---|---|---|---|
| **RCS-28085** | Ollie's | RLPM resuelto como DLPM, pierde aprobación | Sin asignar |
| RCS-28093 | Ahold | Empleados no restringidos por ubicación de tienda | Edwin |
| RCS-28054 | Genuine Parts | RAPMs deberían ver solo su área, varios ven solo New York | Sin asignar |
| RCS-28031 | Genuine Parts | Location Hierarchy "Region" no funciona en New Work Items | Sin asignar |
| RCS-27857 | Wild Fork | Jerarquía puesta en una sola tienda, ve todas | Diego, desde el 16 jul |
| RCS-28118 | Myer | Usuario sin la opción de transferir a Incident, permisos se ven bien | Sin asignar, hoy |
| RCS-28070 | DHL | OM no puede editar audit aunque el security setting está activo | Sin asignar |

Son **siete tickets de resolución de rol y jerarquía**, seis clientes distintos, cinco sin dueño. Ese es el patrón más grande del backlog y el 28085 es su cara visible ahora porque J.R. lo está mirando.

**El otro dato de Ollie's:** también tienen **RCS-28018** sin asignar desde el 29 de julio, "Secure 5 multiple issues", con cuatro cosas dentro: Receipted Flag y Cash Back Flag dando resultados inexactos, el link del campo Emp Sale ID roto, y filter groups guardados que desaparecieron de la librería de Charity Mackey. **Es la misma reportera.** Charity tiene dos tickets abiertos con nosotros, ninguno con dueño, y uno de los dos dice que sus filtros guardados desaparecieron. Si atendemos solo el que J.R. señaló, la percepción del cliente no mejora.

**Recomendación:** los dos al mismo dueño, hoy, y el comentario público sale hoy en los dos. Son productos distintos (Incident y Secure 5) así que técnicamente no es el mismo trabajo, pero la relación con Charity Mackey sí es una sola.

Respuesta para J.R. y Camila (un párrafo, es Teams):

> Hi J.R., taking care of it. 28085 has been unassigned since Thursday with nothing on it but the auto acknowledgement, so the first fix is a real reply today rather than the investigation. Same reporter also has RCS-28018 unassigned since the 29th, so I'm putting both under one owner instead of only the one that got escalated. On the technical side their IT confirmed the employee file has Scott Blackwell as RLPM, so if he resolves as DLPM it sits with role and hierarchy resolution on our side, which is the same pattern as five other unassigned tickets I'm grouping for today's triage.

---

# 6. Lo que hay que preguntar hoy

1. **A Peyman:** el 27951 está repartido a Sebastian y a Vlad al mismo tiempo. Cuál queda.
2. **A Peyman o Carl:** el 28008 aparece a nombre de David Parraga, no de Carl Costelow. Cuál es.
3. **A J.R.:** cuál es el label correcto para tickets de Incident. El que tienes documentado es `Support_Data_Team` y es de Secure 5. Sigue sin respuesta desde el viernes.
4. **A J.R.:** los 5 tickets de Chemist Warehouse en la cola tienen prioridad `Undefined` y son handover de hypercare, no incidentes de cliente. ¿Entran al reparto del equipo o vuelven al equipo de proyecto? Son 5 de 37, la respuesta cambia el tamaño del problema.
5. **A Matt:** la revisión única del filesystem del app service de nettrack para `/nettrack/lpms/`. Cubre 28022, 28058, 28124 y posiblemente 28101 de una sola vez.

## Workflow RCS en Jira — transiciones y por que no sale el boton de cerrar
_chunk 1446 · 2026-08-03 · fuente: Jira API getTransitionsForJiraIssue_

Workflow del proyecto RCS en Jira, consultado por API el 3 de agosto de 2026 desde un ticket en estado Under Security Review (RCS-27840).

HALLAZGO PRINCIPAL
La transicion "Close Ticket" (id 791, lleva al estado Closed) existe en el workflow pero viene con isAvailable false e isConditional true. Por eso el boton de cerrar no aparece en la interfaz desde ciertos estados. La API no expone cual es la condicion, solo que existe.

NO HAY RUTA DIRECTA A "Completed" desde Under Security Review. El estado Completed existe en el proyecto, hay tickets en el, pero no se llega desde ahi. Buscar ese boton es perder tiempo.

El unico estado de categoria Done alcanzable directo desde Under Security Review es Duplicate (id 811).

RUTA PRACTICA PARA CERRAR
Poner el comentario al cliente, mover a "Waiting for customer" (transicion id 641, deja el ticket en Under Customer Review), y desde ahi intentar Close Ticket. Under Customer Review es ademas el estado correcto por contenido cuando se le acaba de responder al cliente y se le pide que avise si el problema vuelve. Es el mismo patron que uso Kiran Vadday en RCS-28023.

IDs DE TRANSICION UTILES, todos globales
231 Waiting for Engineering -> Under Engineering Review
431 Waiting for Analytics -> Under Analytics Review (tiene pantalla)
631 Waiting for CSM -> Under CSM Review
641 Waiting for customer -> Under Customer Review
651 Escalate Ticket -> Escalated
661 Transition to -> Under Infrastructure Review
681 Work in progress
691 Accepted into Development
731 Waiting for Project Management -> Waiting for PMO
741 Waiting for Delivery -> Under Delivery Review
751 Waiting for User Consultant -> Under Solutions Expert Review
761 Waiting for Product Mgmt -> Under Product Mgmt Review
771 Waiting for Security -> Under Security Review
781 Add to the backlog for Future Consideration
791 Close Ticket -> Closed (CONDICIONAL)
801 Waiting for support -> Under Support Review
811 Duplicate
821 Waiting for Software Release
841 Added to the Prioritized Roadmap

Esto vive en la configuracion del workflow del proyecto RCS, no en ninguna base de datos consultable ni en Moscu.

## Notas de triage obligatorias antes de mover un ticket a Engineering
_chunk 1495 · 2026-08-13 · fuente: session-2026-08-13_

Un ticket puede quedarse semanas atascado no porque falte investigacion sino porque la
investigacion nunca se escribio en el ticket.

LA REGLA
Antes de mover un RCS a Engineering el assignee tiene que dejar un comentario interno con
que hizo para triaje y troubleshooting, y que necesita concretamente de Engineering.
Sin eso Engineering no lo recibe. Esto ya estaba en el doc de escalacion de Aimee Wadsworth
(Confluence RTS 478006902856) junto con entorno, pasos de reproduccion con capturas y
cualquier conversacion que ocurrio fuera del ticket.

COMO SE HACE CUMPLIR
El 13 de agosto de 2026, entre las 9:43 y las 9:47 hora del este, Aimee comento el mismo
texto en cuatro tickets de Vedant Shirude, todos parados en Under Support Review:
RCS-27971 GW Manasota, RCS-28007 Vitamin Shoppe, RCS-28010 Casey's y RCS-28247 PVH Corp.
Texto literal: "before this ticket can be moved to Engineering they need you to add your
notes regarding what you did to triage/troubleshoot and explaining what we need from them".
Juan iba en copia junto con Viraj Kansara, Camila Cortes y J.R. Teagle, no como destinatario.

EL CASO QUE MAS DUELE
RCS-28007 tenia la investigacion completa de Tyrone Whitney: comparacion de esquemas dbo
contra incident, el indice de cobertura nci_msft_AuditMasterStore que no se migro, conteos
de auditorias mes a mes. Aun asi no pasaba a Engineering, porque el assignee solo habia
puesto "CC: Matthew Kamminga". Trabajo hecho, ticket frenado.

## Diagnostico de SSO y SAML en un tenant de Incident
_chunk 1496 · 2026-08-13 · fuente: session-2026-08-13_

Fuente: SSO Training Guide Summary, Confluence espacio RTS, pagina 477557096452.

EL DISCRIMINADOR, Y ES EL PRIMER PASO SIEMPRE
En Control Panel cada cliente tiene dos pestanas de SSO. La pestana SSO es la configuracion
del handshake, incluido el mapeo de campos del claim. El SSO Response Log es el registro de
cada claim recibido en cada intento de login, simplificado a los elementos que Appriss usa.

Con eso el caso se parte en dos sin adivinar:
- Si los intentos del usuario aparecen en el Response Log, el IdP del cliente si esta
  respondiendo y el problema esta en nuestro mapeo.
- Si no aparece nada, el claim nunca llego, y entonces es el ACS URL o el Entity ID del lado
  del cliente. Pedirlo por correo otra vez sin esta evidencia no mueve el ticket.

DONDE ESTA CADA COSA
XML crudo del claim: New Relic filtrando por Category LIKE '%SAML%'. Ahi se ve si es
audience mismatch, ACS mismatch o certificado.
Mapeo de campos del cliente: repo arpfiles en Azure DevOps.
Claim minimo obligatorio: nombre, apellido y email. Ubicacion y grupos son opcionales.
Bandera Persistent en el SSO Portal: TRUE vino de import de archivo, FALSE se puso a mano.
Solo 1 de cada 5 clientes automatiza esto. Un TRUE con fecha vieja puede ser una carga
masiva unica de hace anos, no un pipeline vivo.

## Automated Customer Updates — Accepted into Development
_chunk 996 · 2026-06-24 · fuente: Confluence RTS page 477942644765_

## Automated Customer Updates for Accepted into Development Status

Autor: Aimee Wadsworth | Confluence RTS | Ultima actualizacion: 22-jun-2026

### Overview
Cuando un ticket RCS pasa a Accepted into Development, se envia un mensaje automatico al reporter cada 14 dias para mantener transparencia.

### Trigger and Conditions
Se dispara cuando:
- Status = Accepted into Development
- 14 dias desde ultimo mensaje automatico (o desde transicion)
- Ticket no cerrado/resuelto
- Reporter es un contacto de cliente (no interno Appriss)

NO se dispara cuando:
- Status diferente a Accepted into Development
- Ticket resuelto/cerrado/cancelado
- Reporter vacio o usuario interno

### Cadencia
Ciclo rolling de 14 dias:
- Send 1: Dia 14 despues de transicion
- Send 2: Dia 28
- Send 3+: Cada 14 dias hasta resolucion o cambio de status

### Template del mensaje automatico
Hello reporter.displayName, Informing that this issue is still being investigated by our Engineering team. We will keep you updated on any developments. We appreciate your ongoing patience.

### Notas importantes
- Si el cliente responde al mensaje automatico, crea un comentario en el ticket y debe triagearse.
- Si Engineering da update, el agente agrega comentario manual y opcionalmente resetea el timer.
- Tickets con mas de 90 dias en Accepted into Development deben flaggearse en el SCRUM semanal para revision manual.

## RCS Ticket 7/14/28 Day Process — Under Customer Review
_chunk 997 · 2026-06-24 · fuente: Confluence RTS page 477913776130_

## RCS Ticket 7/14/28 Day Process — Reminder and Closure Workflow

Autor: Aimee Wadsworth | Confluence RTS | Ultima actualizacion: 12-jun-2026

### Proposito
Define la cadencia de reminders y proceso de cierre para tickets en status Under Customer Review (UCR) en RCS.

### Scope
- Aplica a TODOS los tickets RCS en Under Customer Review
- Todas las prioridades: Critical, High, Medium, Low
- NO aplica a tickets RTS (tenant/automation)

### Comportamiento del SLA
Cuando un ticket pasa a UCR, TODOS los relojes SLA se pausan inmediatamente. Se reanudan solo cuando el cliente responde y el ticket sale de UCR.

### Cadencia de Reminders (igual para todas las prioridades)
- 1st Reminder: Dia 7 sin respuesta - Email reminder + log interno
- 2nd Reminder: Dia 14 sin respuesta - Email reminder + log interno
- 3rd Reminder (final): Dia 28 sin respuesta - Email final + log interno
- Auto-close: Despues del dia 28 sin respuesta - Cierre automatico

### Templates de Email
- Dia 7: This issue will be closed automatically in the upcoming 21 days if we do not receive any response.
- Dia 14: This issue will be closed automatically in the upcoming 14 days if we do not receive any response.
- Dia 28: This issue will now be closed automatically.

### Workflow End-to-End
1. Agente transiciona ticket a UCR (esperando respuesta del cliente)
2. SLA pausado, timer de reminder arranca
3. Dia 7 -> 1er reminder
4. Dia 14 -> 2do reminder
5. Dia 28 -> reminder final
6. Sin respuesta despues del dia 28 -> auto-close
7. Si el cliente responde en cualquier punto -> ticket se reabre, SLA se reanuda

## Support SCRUM Meeting Guide — Jueves semanal
_chunk 998 · 2026-06-24 · fuente: Confluence RTS page 477917282308_

## Support SCRUM Meeting Guide

Autor: Aimee Wadsworth | Confluence RTS | Ultima actualizacion: 15-jun-2026

### Overview
Reunion recurrente cada jueves. Las primeras 3 semanas del mes rotan presentadores; la semana 4 es revision mensual completa.

### Rotacion de Presentadores
- Week 1 (1er jueves): BJ, Carlos, Carrie, Matt
- Week 2 (2do jueves): Dean, Mohammad, Tyrone, Vlad
- Week 3 (3er jueves): Peyman, Smeet, Chenuka, Dave
- Week 4 (4to jueves): Monthly Review — Full Team

Cada grupo revisa sus tickets Critical o High priority.

### Color Coding del Kanban Board
- Olive = Escalated -> discutir inmediatamente
- Dark red = Aged -> discutir inmediatamente
- Pink = Unassigned -> discutir inmediatamente
- Salmon = Stale -> confirmar owner y asegurar status update
- Green = Work in Progress -> verificar que esta avanzando

### Agenda Semanas 1-3
- 0:00-0:05: Welcome and housekeeping (Meeting Lead)
- 0:05-0:15: Kanban Board Review — Critical and High RCS Ticket Discussion (Team)

### Agenda Semana 4 (Monthly Review)
- 0:00-0:05: Welcome and housekeeping (Meeting Lead)
- 0:05-0:15: Monthly Recap — review topics from Weeks 1, 2 and 3 (Team)

### Que revisar en el Kanban
- Flaggear tickets Escalated (olive), Aged (dark red), Unassigned (pink)
- Confirmar que Stale (salmon) tienen owner y tendran update
- Verificar que WIP (green) estan avanzando

## KT Session — Queue Management & Routing Rules (Aimee)
_chunk 999 · 2026-06-24 · fuente: KT transcript - queue management session_

## KT Session: Queue Management y Routing en Jira RCS

Fuente: KT session con Aimee Wadsworth, jun-2026. Tema: como manejar el Total Backlog queue diariamente.

### Por que Total Backlog y no Support Backlog
- Total Backlog incluye tickets movidos a engineering/delivery review que a veces no se asignan rapidamente
- El speaker (Aimee) y Kristen monitorean el queue TODO EL DIA para asegurar que tickets se asignan

### Reglas de routing desde el queue
- Incident y Secure (cualquier ticket) -> Shandana (ella distribuye a su equipo internamente)
- Engage engineering -> Ian
- Solution experts -> Jim DeJohn primero (el decide cual solution expert trabaja con el cliente)
- Delivery review (Secure 5) -> Peyman primero
- Si un ticket esta en Under Engineering Review: solo verificar el producto y enviarlo a Shan o Ian. No es necesario revisar el contenido del ticket.
- Si esta en Under Delivery Review: generalmente va a delivery team porque support ya hizo todo lo que podia

### Columnas recomendadas en Total Backlog view
1. RCS Issue Type - para ver si es Incident, Change Request, o SOW
2. Target Assignment Times - SLAs de asignacion (estan fallando muchos recientemente)
3. Support Data Team Label - indica si el equipo de datos ya intervino
- Se configuran en Edit Queue > agregar columnas. Cada persona configura su propia vista.

### Workflow diario
- Ordenar por created date (nuevos arriba, viejos abajo)
- Prioridad maxima: Critical/High + Incident type
- Scroll al fondo para ver tickets viejos no asignados
- Meta: que ningun ticket quede sin asignar al final del dia

### Notas
- Shandana es el punto central de routing para engineering (confirma lo que vimos en los tickets de Jira: 54/57 tickets en Accepted into Development asignados a ella)
- Jim DeJohn es el manager de solution experts (no de un color team del doc Color Teams QA)
- El proceso de delivery puede cambiar pronto segun Aimee

## KT Session — Ticket Classification & Queue Hygiene (Aimee)
_chunk 1000 · 2026-06-24 · fuente: KT transcript - classification and queue hygiene_

## KT Session: Clasificacion de tickets y limpieza del queue

Fuente: KT session con Aimee Wadsworth, 24-jun-2026.

### Clasificacion de RCS Issue Type
- 95-98% de clientes seleccionan "Support Ticket" al crear, que auto-etiqueta como Incident
- Pero muchos son realmente Change Requests o SOW - hay que reclasificar manualmente
- Proceso: leer el summary del ticket. Si dice "not loading", "error", "not working" -> Incident. Si dice "can you change", "add", "request" -> Change Request o SOW
- Hay que entrar al ticket si el summary es ambiguo para determinar si es algo roto vs algo que quieren cambiar

### Tiempos y proceso cuando hay backlog
- Meta: ningun ticket mas de 1 semana sin asignar
- A las 2 semanas: asignacion manual forzada - Aimee/lead envia tickets directamente a tecnicos individuales
- Normalmente dejan que los tecnicos escojan sus tickets, pero cuando hay backlog severo se asignan forzadamente
- Cuando un cliente comenta pidiendo update y nadie ha tomado el ticket -> mensaje inmediato en Teams al equipo US/EU pidiendo que alguien lo tome

### Problema actual: data tickets
- Antes: ~5 tickets en queue, se limpiaban constantemente
- Desde que empezaron a tomar data tickets: se quedaron atras porque toman mas tiempo y mas trabajo
- Resultado: tickets de 2+ semanas sin pickup (semana del 8 de junio seguia sin asignar el lunes 22)

### First Response Metrics
- Hay dos metricas: "actual first response" (incluye la auto-respuesta de L1 "gracias por contactar a Appriss") y "assigned team member first response" (desde que el tecnico toma el ticket hasta su primer comentario sustantivo)
- La metrica que importa es la segunda

### Comunicacion con el equipo
- Canal Teams "US Support" para tickets urgentes
- Se envia link del ticket + mensaje pidiendo que alguien con disponibilidad lo tome
- Para EU: canal separado, solo durante horario EU

### Proceso de delivery
- Ticket Secure 5 en Under Delivery Review -> va a Peyman primero
- Si ya paso por Support Review -> el data team ya hizo todo lo que podia
- Shopify: va directo a los 2 tecnicos que saben Shopify (documentado, hay link)

## Playbook — Admin-abandon masivo de Work Items en Secure (SQL directo, 3 gotchas)
_chunk 1150 · 2026-07-14 · fuente: ingesta-2026-07-14_

Abandono masivo "por edad" de Work Items en Secure = procedimiento RTS documentado = UPDATE SQL directo sobre [<CID>_Platform].[workview].[Workview], NO el stored proc AbandonWork. How-to en Confluence: "How to: 'delete' all unassigned Work Items created more than three months ago (Secure 5)" (espacio RTS, página 123297955891). Es data-fix → requiere engineering/RTS (Platform DB = SQL Server / Azure SQL MI, sin UI self-service para bulk por fecha).

Abandonar = StatusID=3 + AbandonReasonID=<id por tenant> + AbandonReasonNotes. Unassigned activos = AssignedToUserID IS NULL AND StatusID=0. StatusTypes: 0=Unassigned, 1=Assigned, 2=AttachedToCase, 3=Abandoned, 4=Investigating (Sources/Core/Core/WorkView/Models/StatusTypes.cs). Los unassigned no tienen investigation/factboard → el UPDATE crudo NO deja huérfanos (esa preocupación aplica solo a assigned/investigated).

GOTCHA 1 (la mayor): el cliente dice "WIs creados antes de <fecha>" pero casi siempre quiere decir el PERIODO cubierto = PeriodToDateTime, NO CreatedDateTime (los WIs se generan días DESPUÉS de cerrar el periodo: periodo cierra 3/29 → CreatedDateTime 4/01). Filtrar por CreatedDateTime da resultados vacíos/erróneos. Confirmar contra el screenshot del cliente.
GOTCHA 2: AbandonReasonID es enum por tenant: SELECT DISTINCT EnumerationType,[Key],Value FROM [<CID>_Platform].[secure].[EnumerationReferenceData] WHERE EnumerationType='WorkviewAbandonReason'.
GOTCHA 3: la tabla de equipos es workview.Team (singular), join Team.WorkviewID=Workview.ID. El nombre del "work flow" NO es una tabla de workflow — scope por Workview.VirtualFilePath o SourceApp.

Siempre: backup (SELECT * INTO workview.Workview_backup_<fecha>), UPDATE batcheado (~100k), guardar IDs para revert, verificar impersonando un usuario del tenant. Caso resuelto de referencia: RCS-27635 Starbucks.
[Fuente: memoria Daniel Buelvas, 2026-07-10]

## ALERTA: Target Assignment Time SLA brecheado masivamente
_chunk 1001 · 2026-06-24 · fuente: Screenshots Total Backlog 24-jun-2026_

## Problema detectado 24-jun-2026: SLA de Target Assignment Time brecheado

### Evidencia
- RCS-27502 (Hot Topic - Employee Purchases Missing Staff ID on Quick Receipt): Target Assignment Time "Yesterday 09:00 AM" - brecheado, sin asignar
- Total Backlog muestra 26 work items, casi todos Under Support Review, sin asignar, con SLA en rojo
- Tickets desde jun-17 hasta jun-23 sin asignar = hasta 7 dias sin pickup

### Tickets visibles en el backlog (24-jun-2026)
- RCS-27522: Wegmans - Employee File Feed Inquiry (High-Touch, SOW) - 1 day ago
- RCS-27520: EZ Pawn - Addition of new Divisions (Community) - 1 day ago  
- RCS-27518: Kinney Drug - Over and Short Data not loading (Designated, Incident) - SLA breached
- RCS-27514: VS&Co - BPMS system for case linking function (Incident) - SLA breached
- RCS-27512: Tillys - Data Privacy Compliance Deletion Notification (SOW) - 1 day ago
- RCS-27509: Alo Yoga - Work Item not populating correct info (Incident) - SLA breached
- RCS-27507: Wegmans - New Group Added to SSO (SOW Estimation) - 2 days ago
- RCS-27502: Hot Topic - Employee Purchases Missing Staff ID (Incident) - SLA breached 
- RCS-27500: AAP - Reports not drillable after Smart Tracks update (Incident) - SLA breached
- RCS-27498: Sams Club - User Unable to access market reporting quick links - 1 day ago
- RCS-27496: THD Canada Division 0006 - SLA breached (5 days ago!)
- RCS-27481: Tractor Supply - Metrics have stopped running - 6 days ago
- RCS-27474: Meijer - Original Amount vs Amount Charged Discrepancy (Incident) - 6 days ago, SLA breached jun-18

### Accion sugerida por Camila
Configurar alertas automaticas para SLA breach de Target Assignment Time en Jira Service Management.

## Técnica — Conseguir el SQL real de un report/search del cliente y dárselo a Claude
_chunk 1151 · 2026-07-14 · fuente: ingesta-2026-07-14_

Cuando un ticket dice "mi report no muestra datos" sin más info (muy común), la palanca más poderosa es obtener el SQL real que corre el report:
1. En Secure, ubicar el search/report (ej. homepage de investigator → quick links → Cashier Risk Report).
2. Correrlo con parámetros dummy (aunque devuelva 0 filas — no importa).
3. Abrir la vista del query → copiar el SQL generado.
4. Dárselo a Claude: "Este es el SQL que corre el cliente; ignora el filtro X que puse dummy; investiga por qué no ve resultados".

En el caso H&M (2026-07-10) esto pinneó la causa en minutos: Claude detectó que el filtro ActionType NOT IN descartaba 94% de los headers → regresión de las filas sintéticas ActionType 99. Sin el SQL, la investigación previa se había quedado en la capa del filtro de fechas.
Regla general de Daniel Endersby: "si vas a pasar una hora buscando algo a mano, pregúntate si hay una forma mejor" — investiga primero automático (Claude + MCPs), manual después si falla.
Tips de calidad de tickets: pedir transaction IDs y nombre exacto del search; los tickets con IDs concretos se resuelven de una (el segundo ticket de esa sesión salió al instante porque traía transaction IDs).
[Fuente: call Daniel Endersby 2026-07-10]

## Técnica — Encontrar el search de un cliente vía la tabla repo de Secure
_chunk 1152 · 2026-07-14 · fuente: ingesta-2026-07-14_

Los clientes reportan issues sobre searches sin decir cuál es ("veo ceros en mi report"). Buscar carpeta por carpeta es lento (hasta 1h). Método correcto: buscar en la tabla repo (todos los archivos de aplicación viven en "repo").

En Secure: Make a search → cambiar área a repo/support → filtro display name contains <término> → Run. Devuelve todas las coincidencias en searches privados, públicos y de sistema.
Cómo leer los resultados (prefijo del file path):
- system… → search de sistema
- <GUID>… → search privado de un usuario
- public… → carpeta pública (ej. "public quick lookup cashier risk report")
Claves: el FILE PATH nunca cambia aunque el cliente renombre el search (decisión histórica) — el display name sí; aparecen múltiples versiones del mismo search porque se trackea version history en el nombre del archivo (la UI solo muestra la última; sirve para rewind si algo se rompe). Ej. real: "Cashier Risk Report" era originalmente "Cashier Risk Report Last 30 Days".
Con acceso a DB se puede consultar la tabla repo directamente. Feature Q4: spotlight search para esto.
[Fuente: call Daniel Endersby 2026-07-10]

## Modelo de escalación corregido — L1 enruta a Support · L3 = Engineering + Delivery (data mapping)
_chunk 1128 · 2026-07-09 · fuente: moscu-ops · corrección J.R._

CORRECCIÓN al modelo de soporte (raíz: feedback de J.R. sobre moscu-ops, 2026-07-09). El soporte NO es una escalera lineal L1→L2→L3; es triage y enrutamiento.

L1 · Triage (equipo no técnico, bajo J.R.): no resuelve, clasifica prioridad + Product Type y ENRUTA. La mayoría de productos (Secure 3/4/5, RTI, LPMS, CAMS, APIS, ASPECT) van a «Under Support Review» → L2 SUPPORT. Solo RTIaaS entra directo a «Under Engineering Review». Los Change Requests van a la cola L2 sin tocar la prioridad. → Su destino principal es SUPPORT, no Engineering/Delivery (error que teníamos: decíamos que L1 escalaba directo a Eng/Del).

L2 · Support (técnicos con background de código): triage, routing, ejecución y resolución de Incidents de todos los productos. Cola «Under Support Review» gestionada por leadership (Aimee, Kristin, Dean). Tickets de data → label Support_Data_Team. Resuelve la mayoría antes de que lleguen a L3.

L3 tiene DOS brazos (se escala por naturaleza del issue, ver KB Escalación L2→L3):
- ENGINEERING: bugs / defectos de código en la app, reproduce y hace RCA (tipo Incident). Triage por Shandana (Shan) / Mission Control.
- DELIVERY: problemas de DATA y CONFIGURACIÓN ya en producción, incluido DATA MAPPING de menor alcance y setup/config (tipo Incident). Contactos: Matt Kamminga (LPMS/CAMS), Ian Williams/Kenny Vu (Engage), Tomasz Mikunda/Carl Costelow (Secure 3/4/5). Para mover a Delivery: Team Ownership → "Support (Delivery Dep.)" y Sprint → "RCS Support Team".
Además: cambios billables → CSM (Change Request); features nuevos → Customer Feedback / Ideas Portal (el RCS se cierra).

Fuente: Moscú Topic 1 (Triage L1, Triage L2, Escalación L2→L3, Equipos Delivery por producto) + reunión 2026-06-12 "Delivery vs Engineering" (Delivery = front-end, UI, data mapping, setup/config; Engineering = back-end y bugs).

## ICA Work Item SLA — Monitoreo, labels y créditos (sesión Dean, 22-jul)
_chunk 1372 · 2026-07-22_

Sesión con Dean Korbakis (autor de los artículos de Confluence de ICA y TJX). Asistieron Camila, JR, Viraj y Juan. ICA y TJX son dos clientes con acuerdos SLA especiales. Esta sesión cubrió SOLO ICA; TJX queda para otra sesión (es de dos frentes: resolución a tiempo de High/Critical + on-time performance).

ACUERDO ICA (efectivo 1-jun, vigente hasta 27-may; sube ~3%/año — validar cifras con el CSM de ICA cada mayo):
- Los Secure EBR Core Work Items deben estar disponibles cada día a las 8am CET. Hay buffer hasta las 9am CET para resolver. Si no se resuelve antes de 9am CET (y no fue causado por el cliente) = 1 "delay"/hit.
- EL CONTEO ES POR DÍA CALENDARIO, no por ticket ni por cantidad de work items. Si un día fallan 10/30/50 work items = 1 hit. Si 3 admins reportan el mismo día = 1 hit (poner el label ICAmissed en UNO solo; el dashboard cuenta por día, no por cantidad de tickets).
- Un outage multi-día cuenta 1 hit POR CADA DÍA. Ejemplo real: incidente de fin de agosto → todo septiembre → todo octubre → 12 días de noviembre; se reportó bajo un único RCS pero se cobró por día calendario (≈30 hits en sept, 31 en oct), siempre al tope de 10+ por mes.
- Grid de créditos (sobre el ingreso mensual / MRR): 1ª instancia del mes = gracia (sin crédito). 2ª–4ª = 2%. 5ª–10ª = 5%. 10+ = tope (≈$1350). Validar cifras exactas con el contrato/CSM.

FLUJO DE DETECCIÓN Y MONITOREO:
- L1 detecta el error en el monitoreo (aparece como ticket RTS primero) y lo reporta en el canal Teams "Secure 5 Issues". L1 puede re-correr work items simples; L2+ investiga los complejos y escala a L3 si hace falta un workaround técnico.
- Si el problema cruza al día hábil del cliente, puede terminar como ticket RCS. Observar AMBOS proyectos, RTS y RCS, sobre todo en la revisión de fin de mes.
- No todo ticket es violación: muchos RTS son "no corrió pero lo arreglamos a tiempo". Filtrar por keyword "ICA work items"; descartar los no relacionados (fechas viejas cargadas, link roto receipts↔work item, etc.).

LABELS (ortografía EXACTA — Jira trata variantes como labels distintos y rompe el feed a Power BI):
- SLA_Checked = revisado (con o sin violación).
- ICAmissed = violación confirmada; es el label que popula el gadget "ICA Work Item Reporting to PowerBI" y alimenta el reporte Power BI que calcula los créditos.
- Evidencia: en las notas del ticket / chat de Teams adjunto suele estar el timestamp de "corrió exitosamente". Convertir a CET (usar World Time Buddy) para saber si estuvo dentro de la ventana 8–9am.

SECCIÓN SLA_Checked / SLA notes del ticket: resumir el análisis, enlazar el email/documento con el timeline, y linkear known issues + known fixes/workarounds para resolver más rápido (petición de Camila). Dean lo pondrá en los docs de Confluence (petición de JR: enviar timeline claro del proceso día 31 → día 5).

CIERRE MENSUAL: el reporte Power BI lo POSEE Austin (Dean no puede editar su visibilidad). Debe refrescarse por el día 5 del mes siguiente con todo investigado y cerrado. Problema actual: el reporte solo estaba actualizado hasta abril; Austin trabaja en junio 2026 y crea la copia 2026→2027. Recomendación de JR: recordatorio de calendario mensual (día 1–5) para dar el mes por cerrado.

ACCESOS / GOBERNANZA:
- Dashboard Jira "ICA Missed Work Item Loads" (jira/dashboards/23940): Camila pidió compartir OWNERSHIP con Camila, Juan y Viraj para no perder acceso. NO hacerlo público (JR): restringir por DEPARTMENT para que los CSMs no lo vean sin vetting.
- Power BI: propiedad de Austin; pedirle acceso.
- Confluence: espacio RTS = fuente de verdad de acuerdos y customizaciones por cliente (contratos, conversión de zona horaria, folders por cliente, Walmart on-prem, etc.). Todo está alimentado a Claude también.

NOTA OPERATIVA: el equipo trabaja en UTC (gente en India y Colombia); Dean convertirá el reporte a CET/UTC consistente. Ojo con DST: CET↔CEST cambia el offset (1h en invierno / 2h en verano), así que la conversión UTC no es fija.

Fuente oficial: Confluence RTS — "ICA Work Item SLA Process" (pageId 476545810442) y "TJX Companies SLA Agreements and Specifications" (pageId 476218785811, acceso pendiente).

## Como remedir una queja de lentitud: tenant de control, DevTools y el TTFB que decide
_chunk 1490 · 2026-08-17 · fuente: moscu://memoria/2026-08-13_

Cuando un cliente reporta "tarda 30 segundos", lo unico que existe son autorreportes. Sin numeros propios y sin linea base, Engineering no actua y el cliente puede discutir la cifra. Protocolo.

ANTES DE MEDIR: CONSEGUIR UN TENANT DE CONTROL
Si el defecto afecta a 3 bases de 39, quedan 36 sanas. Medir los mismos pasos en una sana convierte "30 segundos" en "N veces mas lento de lo normal", que es la unica forma de un numero defendible. Sin control no hay medicion, hay anecdota.

LOS TRES ERRORES QUE ARRUINAN LA MEDICION EN DEVTOOLS
1. Preserve log sin marcar. El log se borra en cada redireccion, y los saltos entre aplicaciones son cadenas de redirecciones: se pierde justo lo que se queria medir.
2. Throttling activo. Debe estar en No throttling. Disable cache desmarcado para la corrida tibia, marcado para una corrida fria al final.
3. Una sola corrida. Tres corridas y se toma la mediana.

QUE NUMERO IMPORTA
No el total. El Waiting for server response (TTFB) de cada request de tipo document, en la pestana Timing. Registrar tambien requests, transferred, Finish, DOMContentLoaded y Load. Guardar evidencia con Save all as HAR with content.

EL DISCRIMINADOR, QUE ES EL PUNTO DE TODO EL EJERCICIO
Si la suma de los TTFB se come el tiempo reportado, el tiempo se va en el servidor y una cache de front-end no arregla nada para ese cliente.
Si los TTFB son rapidos, menos de unos 2 s cada uno, y el total sigue alto por cientos de requests pequenos, el tiempo se va en el cliente y una cache de assets o de labels es exactamente el arreglo.

Esa respuesta casi nunca la tiene nadie, y es lo que se le lleva a Engineering. Aplicado por primera vez en RCS-28256 (Tailored Brands, 13 ago 2026).

Complemento del lado de base de datos: la deteccion de regresion de plan en Query Store. Si el sintoma es un 524, primero leer el Ray ID de Cloudflare.

## Leer el PR, no el mensaje que lo describe
_chunk 1494 · 2026-08-17 · fuente: moscu://memoria/2026-08-13_

Cuando alguien comparte un enlace con una descripcion, la descripcion puede estar mal. Abrir la fuente antes de razonar sobre ella.

EL CASO, 13 AGO 2026
Chris Rippingale pego en el chat de la Unificacion los PR 55858 y 55859 llamandolos "this caching optimisation". Los dos son en realidad ENG-6975, Platform Cohesion - Self service incident user migration, rama ripp/rnd/incident-user-emails: migracion autoservicio de usuarios de Incident, no cache. Ademas el 55858 estaba Active, con un conflicto de merge en Program.cs, sin aprobacion de los revisores requeridos y con 3 de 4 checks sin correr, o sea ni cerca de produccion. Haberle creido al mensaje habria dejado todo el analisis del trabajo de cache apuntando al lugar equivocado.

POR QUE
Un mensaje de chat es la interpretacion de una persona apurada, no el artefacto. Los PR, los changelogs de Jira y las paginas de Confluence dicen quien hizo que y en que estado esta; el chat dice lo que alguien recuerda.

COMO APLICARLO
Si hay enlace, abrirlo y leer titulo, rama, estado, checks y archivos tocados antes de sacar conclusiones. Lo mismo con "ya esta desplegado", "ya se cerro" o "es el mismo problema". Y decirlo explicitamente cuando la fuente contradice al mensaje, sin dramatizarlo.

RESTRICCION DE ACCESO
En Azure DevOps y en cualquier sistema ajeno, solo consultar y leer, nunca modificar ni accionar. Nada de aprobar, comentar, hacer merge ni tocar botones de accion.

CASO HERMANO: LOS LABELS SON DE QUIEN LOS PONE
El 13 ago quite el label Uni_Jul_26_ReportsExports de RCS-28247 y J.R. Teagle lo volvio a poner tres horas despues. No se re-quito. Quitar el label de otro es su decision: se le pregunta y ya.

## ACCIONES-2026-07-31
_chunk 1570 · 2026-07-31 · fuente: ACCIONES-2026-07-31.md_

# Acciones del día — 31 jul 2026
Juan Martinez · basado en el estado real de Jira de esta mañana

---

## Hallazgo que refuerza el 28033

El 404 original de **Vitamin Shoppe (RCS-28005)** se arregló **reconstruyendo las pantallas de audit el 28 de julio**. Vitamin Shoppe es de la ola del 27 de julio, igual que Santikos (RCS-28022) y Big Y (RCS-28033).

Con eso, entrar al Screen Manager de `bigy` ya no es una intuición: hay **dos precedentes confirmados en la misma ola de migración**. Va en el comentario interno del 28033.

```
https://apps.apprissretail.com/bigy/nettrack/Admin/ScreenManager.aspx?admin=9QQP
```

Si faltan pantallas, Build All Screens y se prueba de nuevo.

---

## 1. RCS-28023 — Kiran espera verificación

**Estado:** Under Customer Review · Assignee: Juan Martinez · Medium

**Kiran ya respondió al cliente** (público, 30 jul 7:42 PM):

> The fix has been implemented and applied broadly. Please let us know if you continue to experience any issues.

Eso contesta la pregunta de Leigh Ann sobre "uno por uno o a nivel general". **No enviar el comentario al cliente que se había preparado el 30**, sería duplicar.

Lo que sigue abierto es el pedido interno de verificación de Kiran (30 jul 1:45 PM).

### Cómo verificar

La vista `incident.lpuser` es lo que maneja la app, no `lhua`. La verificación va contra la vista.

```sql
SELECT * FROM incident.lpuser
WHERE email IN ('leighann.stubbs@adusa.com');
```

Con la forma de la vista, comparar contra los usuarios que estaban duplicados y confirmar que ahora resuelven a una sola fila.

### Comentario interno

> @Kiran Vadday Verified on my side. Checking the lpuser view for the reported users, they now resolve to a single row and the duplicate assignments are gone. Leaving this in Under Customer Review since you already confirmed the broad fix to the customer.

**No mencionar los 380.** Salieron de `lhua`, que no es la capa que decide la creación de casos.

---

## 2. RCS-28030 — prueba de 30 segundos antes de la llamada de 60 minutos

**Estado:** Under Customer Review · Assignee: Juan Martinez · Medium

Viraj propuso una llamada de una hora (31 jul 8:38 AM) y J.R. la respaldó. Pero Matt aclaró en Teams que **Incident toma el timezone de la cookie de secure**, y Chris propuso incognito. Si es la cookie, el cambio de perfil sí funcionó y la llamada se evita.

### Mensaje a Viraj

> Viraj, antes de la llamada vale probar una cosa que sale gratis: Matt mencionó que Incident toma el timezone de la cookie de secure, así que si Leigh Ann abre una ventana de incognito y entra ahí, deberíamos ver si el cambio de perfil ya está aplicado y lo que falla es la cookie vieja de su navegador. Si sale bien nos ahorramos la hora, y si sale mal entramos a la llamada sabiendo que no es eso.

**Cuidado:** que el desfase de 4 horas "apunta a UTC en lugar de EST" es interpretación de un resumen, no cita de un comentario. No afirmarlo en el ticket sin verlo directamente.

---

## 3. RCS-28032 — seguimiento a Joe Austin

**Estado:** Under Customer Review · Assignee: Juan Martinez · Medium
Último comentario propio: 29 jul 4:45 PM. **Dos días sin respuesta.**

Joe Austin es el contacto en los tres tickets de Vitamin Shoppe, así que se puede preguntar por Brandon en la misma conversación.

### Comentario al cliente

> Hello Joe,
>
> Following up on this one. Login to the Incident platform is working on our side, so I need to confirm whether Brandon is still seeing the error.
>
> If he is no longer blocked, I will close this ticket. If the error is still there, a screenshot of what he sees would let me pick it up from where we left off.
>
> Kind regards,
> Juan Martinez
> Support Engineer

---

## Lo que NO requiere acción

**RCS-28084** (Application Time out) — Assignee: Vedant Shirude · High · creado hoy 7:26 AM.
Akshaya ya pidió a las 7:34 el screenshot, la URL exacta, el error completo, el Cloudflare Ray ID y el número de tiendas afectadas. **No repetirlo**, ya está en el ticket. El SLA de primera respuesta del equipo está incumplido por 34 minutos, pero el ticket no es propio.

**RCS-28005** (Secure Audit) — Assignee: Tyrone Whitney · High.

---

## Para la reunión de Vitamin Shoppe

Los tres tickets de Vitamin Shoppe esperan lo mismo: que **Joe Austin** entregue datos concretos.

El aporte limpio es salir con **un solo pedido consolidado a Joe**:

| Ticket | Qué se necesita de Joe |
|---|---|
| RCS-28005 | Un ejemplo concreto de audit: nombre, tienda, número de caso |
| RCS-28084 | Screenshot, URL, error completo, Ray ID, tiendas afectadas |
| RCS-28032 | Si Brandon sigue viendo el error |

Tres tickets desatascados con una conversación.

**Sobre la hipótesis de volumen:** Vitamin Shoppe es el 7º cliente más grande de 76 (12,154,843 registros contra una mediana de 1,667,568). Sigue siendo hipótesis y el Ray ID la resuelve más rápido que cualquier análisis de carga. Mencionarla solo si preguntan por qué Vedant no reproduce el timeout.

---

## Datos de referencia — Vitamin Shoppe

| | |
|---|---|
| Slug / ABV / número | `vitaminshoppe` / VSE / 433 |
| Servidor | 8 |
| Fase | 3, prod 27 jul 2026 |
| CSM | Colleen Knoblock |
| Volumen migrado | 12,154,843 registros |
| DB | `sqldb-prd-wus2-arp-production-433-vse-platform` |

**Otros tenants del servidor 8 que salieron el 27 de julio:** christiandior, mcdonalds, skechers, vallarta.
Preguntar si alguno reportó algo parecido separa "problema del tenant" de "problema del servidor" con una sola pregunta.

**Guess NO pertenece a esta ola:** servidor 7, producción 17 de junio. No conectar el 524 de Guess con los timeouts de Vitamin Shoppe.

## CATEGORIZACION-UNIFICACION-2026-08-04 — parte 1
_chunk 1571 · 2026-08-05 · fuente: CATEGORIZACION-UNIFICACION-2026-08-04.md_

# Categorización — Filtro Unificación (Jira filter 43256)
Fecha: 4 ago 2026 · Fuente: filtro 43256, 68 tickets totales

## Resumen de conteo

| Categoría | Tickets |
|---|---|
| Uni_Jul_26_SSOMapping | 7 |
| Uni_Jul_26_Attachments | 5 |
| Uni_Jul_26_LocationHierarchy | 3 |
| Uni_Jul_26_Timeouts | 2 |
| Uni_Jul_26_SessionExpiry | 2 |
| Uni_Jul_26_IzendaRepoint | 2 |
| Uni_Jul_26_Latency | 1 |
| Uni_Jul_26_DuplicateEmail | 1 |
| Uni_Jul_26_URLRouting | 1 |
| Uni_Jul_26_DateTimeZone | 1 |
| Uni_Jul_26_CaseAssignment | 1 |
| Uni_Jul_26_MissingDBObjects | 0 (ninguno en este filtro; sí existe RCS-27573 Tahoe Donner, pero no está en el filtro 43256) |
| **Sin clasificar (revisión manual)** | 19 |
| **Fuera de alcance** (previo al corte de migración del cliente, o no es un defecto de migración) | 23 |

**Nota importante:** el filtro 43256 no está acotado a Unificación, trae tickets desde 2023. El 34% del filtro (23 de 68) es ruido fuera del alcance que pidió J.R. Antes de presentar esto, conviene pedirle a quien mantiene el filtro que lo acote por fecha de creación ≥ fecha de corte de cada cliente, para no tener que filtrar a mano cada vez.

---

## Uni_Jul_26_SSOMapping (7)

| Ticket | Cliente | Síntoma real | Estado |
|---|---|---|---|
| RCS-28078 | Stater Bros | Usuarios no pueden iniciar sesión ni reciben email de reseteo de password. Mismo mecanismo que Mattress Firm/Caribou (ver abajo): usuarios que no vincularon su email antes del corte quedan sin password migrado. No confirmado en este cliente puntual, es inferencia por patrón. | Under Customer Review |
| RCS-28057 | Mattress Firm | Access Blocked, no puede loguearse con su email/password previo. Root cause documentado: en lpguys el LoginID podía ser cualquier cosa, la plataforma nueva exige email; quien no inició sesión en las 6 semanas previas al corte para vincular su email quedó sin password migrado, y Forgot Password no tiene a dónde mandar el correo. | Under Customer Review |
| RCS-28053 | Adusa/Delhaize | Piden el link NON-SAML que existía antes, para los usuarios de Central Station. Config de SSO/SAML post-migración. | Under Customer Review |
| RCS-28046 | Mattress Firm | No puede asignar case work, el nombre del manager aprobador no aparece. Documentado como mismo root cause que 28057: la cuenta del manager tampoco tiene el mapeo de login resuelto, por eso no populate en el dropdown de asignación. | Under Customer Review |
| RCS-28033 | Big Y | Login falla al cambiar password, la app crashea. Root cause confirmado esta semana: `GetSSOPermissionGroupsByUserName` no recibe el username (GlobalID no llega), no puede mapear el usuario. | Work in progress, tuyo |
| RCS-28032 | Vitamin Shoppe | Mismo crash de password update que 28033, mismo patrón SSO. (Tiene además un sub-tema de jerarquía de ubicación para Dayna Rivera, ya resuelto hoy, pero el síntoma original reportado es el de login/password.) | Work in progress, tuyo |
| RCS-28024 | Vallarta | No puede loguearse porque nunca se vinculó el email en ERMS pese a la notificación previa. Mismo mecanismo de "email no vinculado antes del corte" que el cluster de Mattress Firm. | Under Engineering Review |

## Uni_Jul_26_Attachments (5)

| Ticket | Cliente | Síntoma real | Estado |
|---|---|---|---|
| RCS-28124 | ADUSA | Adjuntos PDF y MOV no visibles. Root cause confirmado esta semana: no es por tipo de archivo, es por marca/división (Stop & Shop funciona, el resto no), header `Content-Disposition` duplicado. | Work in progress, tuyo |
| RCS-28105 | Wakefern/VSM | No puede subir archivos .exe ni video, además error al visitar el sitio. Duplicado de RCS-28027 (mismo cliente, mismo síntoma), confirmar antes de investigar dos veces. | Work in progress |
| RCS-28058 | Stater Bros | No puede acceder a adjuntos en el nuevo entorno de URL. | Under Customer Review |
| RCS-28027 | Wakefern/VSM | Error al subir cualquier dato tras la migración. Root cause ya documentado: regla de seguridad bloqueando archivos .zip que contienen .exe. Ya cerrado según nota del 31/07. | Under Customer Review (verificar si ya cerró) |
| RCS-28025 | Ahold | No puede ver adjuntos, screenshots ni videos desde la migración a la nueva URL. | Work in progress |

## Uni_Jul_26_LocationHierarchy (3)

| Ticket | Cliente | Síntoma real | Estado |
|---|---|---|---|
| RCS-28093 | Ahold | Empleados de Store 0001 aparecen visibles entre marcas (Food Lion y Stop & Shop) cuando antes estaban restringidos por marca. Confirmado como la misma investigación que 28023/28043. | Under Engineering Review |
| RCS-28043 | Ahold | Usuarios con ubicaciones de tienda duplicadas entre marcas, ven empleados y stores que no les corresponden. Hermano directo de RCS-28023, mismo investigador (Kiran). | Under Customer Review |
| RCS-28023 | Ahold | No pueden crear casos por restricción de División mal migrada. Root cause confirmado: jerarquía de compañía/store mal alineada tras la migración. | Under Customer Review, tuyo |

## Uni_Jul_26_Timeouts (2)

| Ticket | Cliente | Síntoma real | Estado |
|---|---|---|---|
| RCS-28138 | Stater Bros | Página se congela al generar reportes, error de host en `us.apprissretail.com`. Mismo dominio de origen que 28112. | Under Support Review |
| RCS-28112 | Stater Bros | Sistema no usable, la página gira y hace timeout. Confirmado como Cloudflare 524, origen sin responder a tiempo. | Work in progress, tuyo |

## CATEGORIZACION-UNIFICACION-2026-08-04 — Uni_Jul_26_SessionExpiry (2)
_chunk 1572 · 2026-08-05 · fuente: CATEGORIZACION-UNIFICACION-2026-08-04.md_

## Uni_Jul_26_SessionExpiry (2)

| Ticket | Cliente | Síntoma real | Estado |
|---|---|---|---|
| RCS-28153 | (cliente ER files, no identificado en el título) | Usuarios deslogueados a mitad de trabajo en un ER file, pierden el progreso sin guardar. | Under Support Review |
| ~~RCS-28075~~ | ~~Ahold~~ | **CORREGIDO 5 ago: este ticket no es SessionExpiry, va a `Uni_Jul_26_Timeouts`.** La causa de los 300 a 30 min de sesión se le atribuyó por error, no aparece en ningún comentario del ticket. La evidencia real es un Cloudflare 524 (origen sin responder) más la hipótesis de Izenda de Chris Rippingale. La URL que dio el cliente es `NewIncident.aspx`, misma operación que el RCS-28084 ya cerrado con hotfix. Ver `HANDOFF-RCS-28075-2026-08-05.md`. | Escalated |

## Uni_Jul_26_URLRouting (1)

| Ticket | Cliente | Síntoma real | Estado |
|---|---|---|---|
| RCS-28062 | Stater Bros | Usuarios reciben error 404 / redirect. Mismo patrón de segmento de ruta faltante visto en Santikos y Big Y. | Under Customer Review |

## Uni_Jul_26_DateTimeZone (1)

| Ticket | Cliente | Síntoma real | Estado |
|---|---|---|---|
| RCS-28065 | Stater Bros | Zona horaria mostrando UTC en vez de PST (California). Mismo tipo de defecto que RCS-28030 (Ahold, UTC vs zona del tenant). | Under Customer Review |

## Uni_Jul_26_IzendaRepoint (2)

| Ticket | Cliente | Síntoma real | Estado |
|---|---|---|---|
| RCS-28063 | Stater Bros | Dashboards de Izenda no refrescan a tiempo, o no cargan. | Under Customer Review |
| RCS-28021 | Ahold | No puede guardar cambios en reportes de Izenda, página en blanco sin error. Root cause: Izenda no repuntado a la URL nueva. | Resolution Suggested, tuyo |

## Uni_Jul_26_CaseAssignment (1)

| Ticket | Cliente | Síntoma real | Estado |
|---|---|---|---|
| RCS-28123 | ADUSA | Error "Assigned to can't be blank" al asignar un caso; queda asignado en el caso pero no aparece en la búsqueda por individuo. | Work in progress, tuyo |

## Uni_Jul_26_MissingDBObjects (0)

Ninguno en este filtro. El caso de referencia de esta categoría (RCS-27573, Tahoe Donner, tabla `ACCIDENTEQUIPMENT` faltante) no aparece en el filtro 43256, revisar si el filtro debería incluirlo.

---

## Sin clasificar — necesitan revisión manual antes de forzar una categoría (19)

| Ticket | Cliente | Por qué no encaja limpio |
|---|---|---|
| RCS-28161 | Delhaize | Stores.csv no abre para editar lineup. No es de las 12 categorías, es un problema de generación/formato de export. |
| RCS-28159 | Smart & Final | Usuarios completos no pueden loguearse tras el update, no es duplicado sino ausente. Distinto mecanismo a DuplicateEmail. |
| RCS-28158 | McDonald's | No es un defecto, es un pedido de subir un reporte. |
| RCS-28156 | Skechers | No es un defecto, es una solicitud de spec de Workday/COA. |
| RCS-28151 | Vitamin Shoppe | Export to Excel no funciona en Business Intelligence. Podría ser afín a IzendaRepoint pero no hay evidencia de que sea Izenda específicamente. |
| RCS-28149 | Vitamin Shoppe | Email autogenerado trunca "075" a "75". Bug de formato, no encaja en ninguna de las 12. |
| RCS-28141 | Smart & Final | Admin sin acceso, "Permission Required". Podría ser SSOMapping por similitud con el patrón de Mattress Firm, pero no hay evidencia directa para este cliente, no se fuerza. |
| RCS-28131 | Sportsman's | Smart Alerts dejaron de funcionar tras la migración de base de datos. No hay categoría que cubra alerts. |
| RCS-28125 | Delhaize | Es una tarea de validación de datos de prueba (EBT), no un defecto reportado por el cliente. |
| RCS-28122 | Blain's | No puede acceder a campos de usuario para editarlos. Insuficiente detalle para saber si es permisos, jerarquía u otra cosa. |
| RCS-28115 | Ahold-Delhaize | Campos desplegables y botón SAVE no responden en ciertos casos. Bug de UI sin causa clara todavía. |
| RCS-28109 | Ahold | Acción "Send to Flock" aparece y no se puede ocultar. Config de UI, no encaja en las 12. |
| RCS-28083 | Vitamin Shoppe | Es un pedido de capacitación sobre la UI nueva, no un bug. |
| RCS-28077 | Ahold | Búsquedas de reembolso devuelven líneas duplicadas (efecto cartesiano). Es un bug de datos/query, no hay categoría de "duplicados en búsqueda" entre las 12. |
| RCS-28067 | Vallarta | No puede loguearse, sin más detalle. Podría ser SSOMapping por la misma lógica que 28024, pero acá no hay evidencia del mecanismo específico, no se fuerza. |
| RCS-28044 | Mattress Firm | Descripción vacía, reporter de un dominio externo no relacionado (broker de seguros). Ya señalado como ticket roto en el plan del 31/07, no investigar hasta aclarar qué pide. |
| RCS-28036 | Big Y | Caso borrado al subir un documento a un ER file. Es pérdida de datos, no encaja en las 12. |
| RCS-28007 | Vitamin Shoppe | Reportes muestran datos del año incorrecto (julio 2026 muestra julio 2025) más un error de carga. Distinto mecanismo al de DateTimeZone (eso es despliegue de hora, esto es filtro de fecha). |
| RCS-28005 | Vitamin Shoppe | Error genérico en CAMS al completar un audit, sin detalle técnico suficiente. |

## Fuera de alcance — anteriores al corte de migración del cliente, o no son defectos de Unificación (23)

RCS-27990 (Delhaize, cambio de formato de EBT, no defecto de migración), RCS-27868, RCS-27827, RCS-27807 (Delhaize, todos creados 13–16 jul, antes del corte del 27/28 jul), RCS-27803 (Sportsman's, creado 13 jul), RCS-27766 (Vitamin Shoppe, creado 10 jul), RCS-27600, RCS-27530, RCS-27077, RCS-26953, RCS-26930, RCS-26897, RCS-26508, RCS-26317, RCS-26248, RCS-24906, RCS-23168, RCS-22866, RCS-22368, RCS-21490, RCS-20978, RCS-16514, RCS-8327 (todos con fecha de creación entre 2023 y abril 2026, sin relación con el corte de julio).

## GUION-LLAMADA-unificacion-2026-07-31 — parte 1
_chunk 1573 · 2026-07-31 · fuente: GUION-LLAMADA-unificacion-2026-07-31.md_

# Guion para la llamada de unificación
31 jul 2026 · Juan Martinez lidera · filtro de J.R.: Incident type, Product Type Incident (LPMS) o Audit (CAMS), creados en los últimos 3 días

**43 tickets. 13 sin dueño.** Dos clientes concentran 20 de los 43.

| | |
|---|---|
| Ahold / ADUSA / Delhaize | **11** |
| Stater Bros | **9** |
| Vitamin Shoppe | 4 |
| Vallarta | 3 |
| Mattress Firm | 3 |
| Big Y | 2 |

Por estado: 13 Work in progress, 13 Under Support Review, 8 Under Customer Review, 2 Resolution Suggested, y uno en Escalated.

---

# 1. Abre con esto: 13 sin dueño

**Diez de los trece están en `Under Support Review`**, o sea que nadie los ha tomado. Y dos son High.

| Ticket | Prioridad | Estado | Asunto |
|---|---|---|---|
| **RCS-28059** | **High** | Under Engineering Review | Ahold, "Sorry, you have been blocked" con la nueva URL de LPMS. **Enrutado a Engineering sin nombre** |
| **RCS-28080** | **High** | Under Customer Review | Stater Bros, no puede actualizar usuarios siendo admin. **Esperando al cliente sin nadie que responda** |
| RCS-28014 | **Critical** | Closed | "New Appriss URL is asking for email address". Cerrado sin dueño |
| RCS-28027 | Medium | Under Support Review | VSM, LPMS Error |
| RCS-28036 | Medium | Under Support Review | Big Y, Case deleted |
| RCS-28044 | Medium | Under Support Review | Mattress Firm, Admin Access |
| RCS-28046 | Medium | Under Support Review | Mattress Firm, no puede asignar case work |
| RCS-28057 | Medium | Under Support Review | Mattress Firm, Access Blocked |
| RCS-28070 | Medium | Under Support Review | DHL, Operations Manager no puede editar Audit |
| RCS-28085 | Medium | Under Support Review | Ollie's, User Access Incorrect |
| RCS-28091 | Medium | Under Support Review | Caribou Coffee, no puede entrar al sitio nuevo después de la migración |
| RCS-28093 | Medium | Under Support Review | Ahold, empleados no restringidos por ubicación |
| RCS-28101 | Medium | Under Support Review | "Web Server Returned Unexpected Response" después de subir archivo |

Los dos que hay que señalar en voz alta son **28059**, porque está en cola de Engineering y nadie va a comunicarle nada al cliente, y **28080**, porque está esperando respuesta del cliente y no hay quien la lea.

Mattress Firm tiene **tres** tickets de acceso sin tocar desde el 29.

---

# 2. Tu aporte más fuerte: RCS-28059 ya tiene causa

High, sin dueño, en Under Engineering Review. Ahold, "Sorry, you have been blocked" con la URL nueva de LPMS.

Es el mismo error que Big Y reportó y que diagnosticaste ayer. No es la aplicación ni un timeout, es un **bloqueo del WAF de Cloudflare** que se dispara al pegarle al dominio raíz `apps.apprissretail.com` sin el slug del tenant. Ray ID de la instancia de Big Y: `a23606220b52590b`.

> On 28059 I already have the cause, it's the same thing Big Y reported. It isn't the application and it isn't a timeout, it's a Cloudflare WAF block that fires when you hit the root domain without the tenant slug. I have the Ray ID from the Big Y occurrence. Users get in fine through apps.apprissretail.com/slug/signin. The broader point is that the root domain serves a WAF block page instead of a redirect, so it will keep catching migrated clients who bookmarked the old entry point.

---

# 3. Recorrido por patrón

## Adjuntos que no abren

| Ticket | Cliente | Estado | Dueño |
|---|---|---|---|
| **RCS-28022** | Santikos | **Escalated** | Juan |
| RCS-28058 | Stater Bros | Under Customer Review, High | Tyrone |
| RCS-28067 | Vallarta | Under Customer Review | David |
| RCS-28025 | Ahold | Closed | Viraj |
| RCS-28101 | | Under Support Review | sin dueño |

**Lo tuyo:** en Santikos la excepción es `The file '/nettrack/lpms/ShowAttachments.aspx' does not exist`, desde `CheckVirtualFileExists`, en el app service compartido. Reproducido a demanda hoy 16:46:19 con referrer y return URL distintos a los del cliente y excepción idéntica, así que no depende de sesión ni navegación. Ripp confirmó que el slug solo existe antes del reverse proxy YARP y que en disco nunca hay slug, así que la ruta interna es la correcta y el archivo no está.

**La pregunta para la llamada:** si falta esa página en el deployment compartido, los de Stater Bros y Vallarta pueden ser lo mismo. Vale que alguien mire el filesystem del app service **una vez** en lugar de investigar tres tickets aparte.

Cuidado: el de Vallarta trae un 500 en `GetPlatformCookie` desde `UrlRewriteModule`, no un 404. Misma función afectada, mecanismo distinto. No los fusiones.

## GUION-LLAMADA-unificacion-2026-07-31 — Login, contraseñas y correos no ligados
_chunk 1574 · 2026-07-31 · fuente: GUION-LLAMADA-unificacion-2026-07-31.md_

## Login, contraseñas y correos no ligados

| Ticket | Cliente | Estado | Dueño |
|---|---|---|---|
| RCS-28014 | | **Critical**, Closed | sin dueño |
| RCS-28033 | Big Y | Work in progress, High | Juan |
| RCS-28024 | Vallarta | Work in progress | David |
| RCS-28061 | Stater Bros | Work in progress | Tyrone |
| RCS-28071 | Stater Bros | Work in progress, High | Kiran |
| RCS-28078 | Stater Bros | Work in progress, High | Tyrone |
| RCS-28080 | Stater Bros | Under Customer Review, High | **sin dueño** |
| RCS-28062 | Stater Bros | Work in progress | Tyrone |
| RCS-28091 | Caribou Coffee | Under Support Review | **sin dueño** |
| RCS-28044 / 28046 / 28057 | Mattress Firm | Under Support Review | **sin dueño** |
| RCS-28085 | Ollie's | Under Support Review | **sin dueño** |
| RCS-28042 | Ahold | Resolution Suggested | Viraj |
| RCS-28053 | Adusa | Work in progress | Viraj |
| RCS-28009 | Sportsmans | Work in progress, Low | Kiran |

**Es el grupo más grande y la causa ya la explicó Matt hoy.** En lpguys el LoginID podía ser cualquier cosa, la plataforma nueva necesita un correo. Durante seis semanas antes de migrar un proceso forzaba a ligar un correo **cuando el usuario entraba**, y aprovechaba ese momento para re-hashear la contraseña bajo el cifrado nuevo. Quien no entró en esa ventana no tiene correo ligado ni contraseña trasladada, y para esos el reset necesita un buzón que nunca existió.

La acción de la retro ya se decidió: mover ese proceso a después de la migración, al primer login en la plataforma nueva. Lo que lo bloquea es llevar el cifrado de lpguys a la app de sign-in.

**Lo que ofreces:** correr la verificación de correos contra los 10 clientes del 10 de agosto antes del corte, con el select que mencionó Matt, para marcar a quien no tenga correo antes y no después.

## Timeouts y lentitud

| Ticket | Cliente | Estado | Dueño |
|---|---|---|---|
| RCS-28072 | Guess | Under Support Review, High | Diego |
| RCS-28075 | Ahold | Under Customer Review | Vedant |
| RCS-28084 | Vitamin Shoppe | Under Customer Review, High | Vedant |
| RCS-28063 | Stater Bros | Work in progress | Tyrone |

**La corrección que tienes que decir:** RCS-28021 de Ahold **sale de este grupo**. Jie Chen confirmó hoy que era configuración del reporte, un join mal armado, no capacidad de la plataforma. Está en Resolution Suggested esperando que el cliente valide. Si sigue contando como evidencia de degradación del origen, la muestra queda contaminada.

**Y Guess tampoco es de la ola del 27:** servidor 7, producción 17 de junio.

**El dato de clasificación:** en el app service de nettrack había unos 2495 client timeouts contra 255 errores 500, y 248 de esos 500 en un solo endpoint, `POST /nettrack/api/internal/SendSmartAlert.aspx`. Un command timeout de SQL saldría como 500 con excepción y no vemos ese volumen, así que apunta a web request timeout. Esa última parte es lectura mía, no algo que digan los logs.

Nadie ha separado los timeouts por tenant. Es ofrecible y es tuyo.

## Zona horaria

| Ticket | Cliente | Estado | Dueño |
|---|---|---|---|
| RCS-28030 | Ahold | Work in progress | Juan |
| RCS-28065 | Stater Bros | Work in progress | Tyrone |

Matt confirmó hoy que **Incident toma el timezone de la cookie de secure**, así que cambiar el perfil no surte efecto hasta que el usuario abre sesión nueva. Viraj impersonó a Leigh Ann y vio EST correcto, ella sigue viendo mal por la cookie vieja. Chris propuso incognito.

**Consecuencia para el bulk update de los 2519 usuarios:** va a quedar bien pero no se va a ver hasta que cada usuario tenga sesión nueva. Hay que decirlo cuando se ejecute o va a parecer que falló.

## Restricción por ubicación y jerarquías

| Ticket | Cliente | Estado | Dueño |
|---|---|---|---|
| RCS-28023 | Ahold | Work in progress | Juan |
| RCS-28043 | Ahold | Under Customer Review | Viraj |
| RCS-28093 | Ahold | Under Support Review | **sin dueño** |
| RCS-28070 | DHL | Under Support Review | **sin dueño** |

Kiran aplicó el fix de forma amplia y lo comunicó al cliente en 28023. **La regla que enseñó y que ahorra tiempo:** la vista `incident.lpuser` es lo que maneja toda la app. `secure.LocationHierarchyUserAssignments` es un destino de la migración, no la capa que decide si puedes crear un caso. Para síntomas funcionales, la vista primero.

## Vitamin Shoppe, los cuatro

| Ticket | Estado | Dueño |
|---|---|---|
| RCS-28007 | Under Customer Review | Tyrone |
| RCS-28032 | Under Customer Review | Juan |
| RCS-28083 | Under Support Review, New UI | Daniel Ortquist |
| RCS-28084 | Under Customer Review, High | Vedant |

Los cuatro esperan lo mismo: que **Joe Austin** entregue datos. En 28084 Akshaya ya pidió screenshot, URL, error completo, Ray ID y número de tiendas. Un solo pedido consolidado a Joe desatasca los cuatro.

## Sueltos

| Ticket | Cliente | Nota |
|---|---|---|
| RCS-28037 | Luxottica | **Critical**, sitio caído en `appserver1.lpguys.net`, Completed |
| RCS-28041 | Ahold-Delhaize | Nombre del remitente de correo, en Product Mgmt |
| RCS-28010 | Casey's | Reassign Incident Bug, Vedant |
| RCS-28094 | Vallarta | Appriss Admin Function, David |
| RCS-28064 | Stater Bros | Duplicate |

---

# 4. Cierre: tres peticiones concretas

1. **Dueño para los 13 sin asignar**, empezando por 28059 y 28080 que son High, y por los tres de Mattress Firm que llevan dos días intactos.
2. **Una sola revisión del filesystem del app service compartido** para las páginas de `/nettrack/lpms/`. Cubre Santikos, Stater Bros y posiblemente Vallarta de una vez, en lugar de tres investigaciones paralelas.
3. **La verificación de correos contra los 10 clientes del 10 de agosto** antes del corte, que es la prioridad que se fijó esta mañana.

## GUION-TRIAGE-COLOMBIA-2026-08-04 — parte 1
_chunk 1575 · 2026-08-04 · fuente: GUION-TRIAGE-COLOMBIA-2026-08-04.md_

# Guion — Triage cola sin asignar, equipo Colombia
**Fecha:** 4 ago 2026
**Lead de la reunión:** Juan Martinez
**Duración estimada:** 40–45 min (7 tickets × hasta 5 min de discusión + 30 min bloqueados en el calendario de cada uno para trabajar después)
**Asistentes:** Diego Buelvas, Sebastian Rueda, Edwin Garzon, David Vargas
**No incluido:** Luis Hernandez. Sigue en onboarding con Diego Buelvas, no tiene los permisos ni el acceso necesario todavía. No se le asigna nada en esta sesión, y hay que decirlo explícito al abrir la reunión para que nadie asuma lo contrario.

---

## 0. Por qué existe este guion

J.R. Teagle pidió el sábado que cada lead (vos y Viraj) corriera una reunión de triage de emergencia con su propio equipo, siguiendo un proceso puntual: revisar de más viejo a más nuevo, discutir hasta 5 minutos por ticket, pedir voluntario, si nadie se ofrece asignar a quien tenga menos carga, apuntar a 5 tickets por persona, dejar un comentario público de "estamos investigando" y bloquear hasta 30 minutos por ticket nuevo el lunes.

Dado el huso horario, la decisión fue que el equipo de Viraj (India) corriera primero su pasada y te dejara un handoff, para que vos completes con Colombia lo que quede, sin duplicar trabajo. Eso ya pasó: quedan **7 tickets** de los 21 originales.

**Esto no es una reunión para "repartir números".** Es una reunión de triage real: cada ticket se inspecciona antes de asignarlo, se buscan relaciones con trabajo que el equipo ya hizo esta semana, y la asignación se justifica con esa relación, no solo con quién tiene menos tickets. La carga es el criterio de desempate, no el criterio principal.

---

## 1. Contexto que hay que tener en la cabeza antes de arrancar

Tres flujos distintos convergieron esta semana, y el equipo tiene que entender cuál es cuál para no mezclar conversaciones:

1. **La cola masiva original (~40 tickets).** J.R. la reportó el sábado. Peyman (India) hizo una primera pasada y la bajó a 26.
2. **La cola de 21 que armaste vos, agrupada por patrón, y que le pasaste a Viraj.** Su equipo tomó 14. Quedan los **7 de este guion**.
3. **18 tickets huérfanos de gente que ya no está en el equipo** (hilo aparte de Camila en "Nuaav Leadership Support"). Ya se repartieron parcialmente: Diego +6, Edwin +2, David +3, además de Gulshan y Nikita en India. **Este reparto ya está hecho, no se discute hoy, pero sí cuenta para la carga de cada uno.**

Si alguien en la reunión menciona un ticket que no está en la lista de 7, probablemente sea de uno de los otros dos flujos. No lo asignes ahí mismo, anotalo y confirmá con Camila o Viraj después para no pisar lo que ya está repartido.

---

## 2. Carga real de cada uno, antes de tocar los 7 de hoy

| Persona | Carga base (mensaje de Camila) | + huérfanos ya asignados | Carga real hoy |
|---|---|---|---|
| Juan | 17 | — | 17 |
| Sebastian | 15 | — | 15 |
| Edwin | 12 | +2 | 14 |
| David | 10 | +3 | 13 |
| Diego | 6 | +6 | 12 |

Con esto ya nadie parte de cero real. Diego, que en el mensaje de Camila parecía el más liviano, en realidad ya está en 12. Esto importa porque si alguien en la reunión propone "dale todo a Diego que tiene menos", hay que corregir con estos números actualizados, no con los de la captura original.

---

## 3. Antes de cada ticket: qué inspeccionar

Para cada uno de los 7, abrí el ticket en Jira **durante** la reunión (no antes, para que el equipo vea el mismo estado que vos) y mirá, en este orden:

1. **Descripción y último comentario.** ¿Qué exactamente reporta el cliente, y quién habló por última vez?
2. **Cliente y tipo de producto** (Secure 5 - EBR, Incident/LPMS, Audit/CAMS). Esto determina si alguien del equipo ya tiene contexto reciente ahí.
3. **¿Hay un ticket relacionado ya trabajado esta semana con el mismo síntoma o el mismo cliente?** Esto es lo que justifica la asignación, no solo "quién tiene menos". Antes de la reunión, ya crucé esto por vos (ver sección 5), pero decilo en voz alta igual, para que quede como parte de la discusión y no como una imposición tuya.
4. **¿El ticket ya tiene next steps escritos por alguien de soporte L1, o llega en blanco?** Si ya hay un paso claro, la discusión de 5 minutos se acorta a "¿alguien lo toma?". Si no hay next steps, hay que decidir en la reunión cuál es el primer paso de investigación antes de asignarlo, no solo el nombre.

---

## 4. Preguntas para hacerle al equipo en cada ticket (no solo "¿quién lo toma?")

Usalas como guía, no las leas todas siempre, elegí las que apliquen:

- ¿Alguien ya vio este mismo síntoma esta semana en otro ticket, aunque sea de otro cliente?
- ¿Esto es de un cliente donde ya tenemos contexto por otro ticket abierto?
- ¿Es un bug de aplicación (Full Stack) o un problema de datos/configuración (Data Engineer)? Eso decide si el candidato natural es Diego/David o Sebastian/Edwin, más allá de la carga.
- ¿Necesita reproducirse primero, o ya viene reproducido y solo falta escalar?
- Si nadie se ofrece: ¿hay alguna razón para NO asignárselo a la persona de menor carga (por ejemplo, que ya tenga tres tickets del mismo cliente y esto sería el cuarto)?

---

## GUION-TRIAGE-COLOMBIA-2026-08-04 — 5. Los 7 tickets, con inspección, relación y justificación
_chunk 1576 · 2026-08-04 · fuente: GUION-TRIAGE-COLOMBIA-2026-08-04.md_

## 5. Los 7 tickets, con inspección, relación y justificación

### Ticket 1 — RCS-28060 (Starbucks Coffee Company NA)
**Qué es:** el toggle "show all open investigations" no filtra, cuando está desactivado el usuario sigue viendo todas las investigaciones en vez de solo las propias.
**Qué inspeccionar:** confirmar si es un bug de estado en frontend (el toggle no persiste su valor) o si el filtro no se está aplicando en el backend al armar el listado.
**Relación con trabajo reciente:** no hay cluster con otro ticket de esta semana, es un bug aislado de UI.
**Por qué a Diego:** es un bug de comportamiento de aplicación, no de datos ni de jerarquía, encaja con su perfil Full Stack, y es autocontenido, bueno para alguien que ya sumó carga esta semana con los huérfanos.
**Asignación sugerida por carga (si nadie se ofrece):** Diego, es quien tiene menos carga real hoy (12).
**Pregunta para la reunión:** ¿alguien tiene ya abierto un ticket de Starbucks esta semana que dé contexto extra antes de asignarlo a ciegas?

### Ticket 2 — RCS-28099 (Chemist Warehouse)
**Qué es:** la lógica de descuento por ítem es más compleja de lo esperado, abarca varias tablas, sin timeline claro. Está esperando que el cliente actualice su fuente de datos.
**Qué inspeccionar:** confirmar que sigue en estado de espera al cliente y no hay nada nuevo de su parte desde el 3 de agosto.
**Relación con trabajo reciente:** mismo cluster que RCS-28100 y RCS-28097 (Chemist Warehouse, ambos ya asignados a India). Este es el tercero de la misma familia.
**Por qué a Diego:** no requiere investigación activa ahora mismo, solo monitoreo hasta que el cliente responda. No tiene sentido cargarlo en alguien con trabajo de investigación profunda pendiente.
**Asignación sugerida por carga (si nadie se ofrece):** David, es el segundo con menos carga (13) después de Diego.
**Pregunta para la reunión:** ¿lo dejamos en "esperando cliente" sin dueño de investigación activa, solo alguien que lo revise cuando el cliente actualice, o preferimos que quien lo tome sea el mismo que quede con los otros dos de Chemist Warehouse para consistencia?

### Ticket 3 — RCS-28070 (DHL Global Mail)
**Qué es:** un Operations Manager no puede editar un LP Compliance Audit pese a tener los permisos correctos habilitados en las tres secciones de audit.
**Qué inspeccionar:** revisar si el problema es a nivel de facility (BOS) específicamente, o si se reproduce en otras facilities del mismo cliente.
**Relación con trabajo reciente:** mismo patrón conceptual que viste hoy en RCS-28023 (jerarquía/rol que no resuelve como debería pese a verse bien configurado), pero en un producto distinto (Audit/CAMS, no Secure 5/Incident). No asumir que la misma consulta SQL aplica acá, es otra tabla y otro módulo.
**Por qué a David:** ya viene de resolver temas de acceso y rol en Ollie's (RCS-28018, RCS-28085), tiene el hábito reciente de este tipo de investigación aunque el producto cambie.
**Asignación sugerida por carga (si nadie se ofrece):** Edwin, tercero en la lista de menor a mayor carga (14).
**Pregunta para la reunión:** ¿alguien conoce el módulo de Audit/CAMS lo suficiente como para saber si comparte la misma lógica de permisos que Secure 5, o es efectivamente independiente?

### Ticket 4 — RCS-28103 (Sycamore Partners : Hot Topic Inc.)
**Qué es:** el envío de restitución está roto, el usuario tuvo que sacar a "Zelman" de la lista de proveedores para ver las opciones, y no encuentra la opción SETUP en Admin. El ticket ya sugiere que probablemente haya que escalar a seguridad.
**Qué inspeccionar:** confirmar si "no encuentra SETUP" es porque no tiene el permiso asignado (falta de rol) o porque el menú no existe para ese tipo de cuenta.
**Relación con trabajo reciente:** mismo tipo de investigación de configuración de acceso/admin que David ya trae de Ollie's y de este mismo bloque (28070).
**Por qué a David:** consistencia de contexto con el ticket anterior, y su perfil ya viene tocando temas de permisos esta semana.
**Asignación sugerida por carga (si nadie se ofrece):** Sebastian, cuarto en la lista (15).
**Pregunta para la reunión:** si se confirma que es un tema de seguridad y no de aplicación, ¿quién hace la escalación formal a Security, David o vos como lead?

### Ticket 5 — RCS-28054 (Genuine Parts Co.)
**Qué es:** los RAPM deberían ver solo sus ubicaciones asignadas en Work Items. Después de un cambio de configuración, varios usuarios solo ven "New York" sin ningún work item, incluso usuarios correctamente configurados.
**Qué inspeccionar:** esto es prácticamente el mismo síntoma que resolviste hoy en RCS-28023 (Ahold) y en RCS-28032 (Dayna Rivera, Vitamin Shoppe). Antes de asignarlo, mostrale al equipo cómo lo resolviste hoy: revisar `secure.LocationHierarchyUserAssignments` contra la jerarquía de ubicación esperada, y en el caso de Vitamin Shoppe, verificar si falta el nodo de District en vez de asumir que son ubicaciones sueltas.
**Relación con trabajo reciente:** es el tercer caso de la semana del mismo patrón (Ahold, Vitamin Shoppe, y ahora Genuine Parts). Vale la pena decirlo en voz alta en la reunión, porque si son tres clientes distintos con el mismo síntoma post-configuración, es candidato a patrón sistémico, no un bug puntual de cada cliente.
**Por qué a Edwin:** Data Engineer, encaja con el tipo de consulta que se necesita, y podés pasarle directamente el mismo método que usaste hoy para que no arranque de cero.
**Asignación sugerida por carga (si nadie se ofrece):** Juan, quinto y último de la ronda (17). Vos mismo, si nadie del equipo se ofrece y le toca por orden.
**Pregunta para la reunión:** ¿deberíamos documentar este patrón de jerarquía de ubicación como un tema recurrente y avisarle a alguien de Delivery o Engineering, en vez de seguir resolviéndolo cliente por cliente?

### Ticket 6 — RCS-28104 (Albertson's-Safeway Group)
**Qué es:** una búsqueda está devolviendo datos de 2023, 2024 y 2025 pese a que Safeway solo tiene 90 días de historial configurado. Pasa cuando se sacan ciertos filtros de visualización.
**Qué inspeccionar:** confirmar si el problema es que la ventana de retención no se está aplicando en el query, o si es un tema de índice/caché que muestra datos que ya deberían estar purgados.
**Relación con trabajo reciente:** no hay cluster directo, pero es del mismo tipo de trabajo de datos/configuración que el resto de lo que ya tiene Edwin.
**Por qué a Edwin:** mismo perfil de Data Engineer, y agruparlo con el anterior le da dos tickets de configuración de datos seguidos, más eficiente que alternar entre tipos de problema distintos.
**Asignación sugerida por carga (si nadie se ofrece):** Diego, la ronda vuelve a empezar por el de menor carga (12 antes de este bloque, ya llevaría uno de esta sesión).
**Pregunta para la reunión:** ¿alguien sabe si el límite de 90 días se aplica a nivel de query o a nivel de purga física de datos? Esa distinción cambia por completo el enfoque de investigación.

### Ticket 7 — RCS-28055 (Genuine Parts Co.)
**Qué es:** un work item de reembolso muestra solo 1 ítem en el recibo dentro de Appriss, cuando el sistema origen (TAMS) muestra 4 partes compradas y 4 devueltas.
**Qué inspeccionar:** aunque es el mismo cliente que el ticket 5 (RCS-28054), es un bug distinto, de agregación de líneas de recibo, no de jerarquía de ubicación. No asumir que es el mismo root cause solo por ser el mismo cliente.
**Relación con trabajo reciente:** mismo cliente que RCS-28054, pero mecanismo de falla diferente. Vale la pena que quien lo tome esté al tanto de que hay otro ticket abierto del mismo cliente, por si en algún punto se cruzan.
**Por qué a Sebastian:** Data Engineer senior, y es el tipo de bug de mapeo/agregación de datos donde su experiencia pesa más que la carga.
**Asignación sugerida por carga (si nadie se ofrece):** David, siguiente en la ronda después de Diego.
**Pregunta para la reunión:** ¿deberíamos linkear este ticket con RCS-28054 aunque el root cause sea distinto, solo para que quien atienda a Genuine Parts tenga visibilidad de todo lo abierto con ese cliente?

---

## GUION-TRIAGE-COLOMBIA-2026-08-04 — 6. Guion de apertura (para leer o parafrasear al empezar)
_chunk 1577 · 2026-08-04 · fuente: GUION-TRIAGE-COLOMBIA-2026-08-04.md_

## 6. Guion de apertura (para leer o parafrasear al empezar)

> Buenas a todos. Esto es lo que pidió J.R. el sábado: bajar la cola de tickets sin asignar. El equipo de Viraj ya hizo su pasada y tomó 14 de los 21 originales, así que hoy solo nos quedan 7. La idea no es repartir números, es revisar cada uno, ver si se conecta con algo que ya venimos trabajando esta semana, y asignarlo con esa lógica. Si alguien se quiere ofrecer para alguno, mejor que asignarlo por carga. Luis no participa de la asignación hoy, sigue en onboarding.
>
> Vamos de más viejo a más nuevo, máximo 5 minutos por ticket. Al que le toque, deja un comentario público de que lo estamos investigando, y bloquea hasta 30 minutos el lunes para arrancar.

## 7. Guion de cierre

> Recapitulando: [leer la tabla final con quién quedó con qué]. Todos dejen el comentario público antes de salir de la reunión, no después. Yo le aviso a Viraj qué quedó tomado de nuestro lado para que no se pise con India. Si alguien encuentra en su ticket que en realidad es el mismo patrón que otro cliente, avisen en el canal para que lo linkeemos, como puede pasar con los de jerarquía de ubicación.

---

## 8. Después de la reunión, checklist para vos

- [ ] Confirmar que los 7 tickets tienen comentario público de "investigando".
- [ ] Confirmar que cada uno movió el status a `Work in Progress`.
- [ ] Mandarle a Viraj la lista final de quién quedó con qué, para cerrar el loop del handoff.
- [ ] Si se linkearon RCS-28054 y RCS-28055 por cliente, dejarlo anotado en ambos tickets.
- [ ] Si el patrón de jerarquía de ubicación (RCS-28023, 28032, 28054) se mencionó como sistémico en la reunión, escalarlo aparte a Delivery o Engineering, no dejar que se pierda como comentario suelto de la reunión.

## LABELS-UNIFICACION-FINAL-2026-08-04 — parte 1
_chunk 1578 · 2026-08-05 · fuente: LABELS-UNIFICACION-FINAL-2026-08-04.md_

# Labels Unificación — lista final APLICADA
Fecha: 4 ago 2026 · Fuentes: filtro 43256 + barrido all-statuses de los 20 clientes desde el corte (27/28 jul) · Cada ticket verificado contra descripción y comentarios, no solo título.

**Estado: los 61 labels ya están aplicados en Jira** (verificado por JQL el 4 ago, 15:52 ET). Labels preexistentes preservados en todos los casos.

> ### ⚠️ Corrección pendiente de aplicar — RCS-28075 (añadida 5 ago 2026)
>
> **Este documento registra lo que se aplicó el 4 de agosto, así que las filas de abajo NO se modificaron.** Pero al leer el ticket completo el 5 de agosto quedó claro que un label está mal:
>
> **RCS-28075 (Ahold) está en `Uni_Jul_26_SessionExpiry` y debería estar en `Uni_Jul_26_Timeouts`.**
>
> La causa que se le atribuyó, el cambio de 300 a 30 minutos de sesión que explicó Kiran, **no aparece en ningún comentario del ticket**. Se importó de la llamada del 3 de agosto y se pegó al ticket sin respaldo. La evidencia real del ticket es un Cloudflare 524 (timeout de request, origen sin responder) más la hipótesis de Izenda de Chris Rippingale. Una sesión que expira da redirect al login, no un 524.
>
> Agrava el error que en este mismo documento, sobre el RCS-28084, quedó escrito *"Es timeout de request, no expiración de sesión"*. La distinción se hizo para ese ticket y no se aplicó a este.
>
> **Además:** la URL que dio el cliente el 31 jul es `NewIncident.aspx`, o sea timeout al crear incidente, que es la misma operación del **RCS-28084** ya cerrado con *"Unification platforms hotfix created and published"*. Hay que confirmar si ese hotfix llegó al tenant adusa.
>
> **Si se aplica la corrección**, los conteos quedan: `Uni_Jul_26_Timeouts` 3 → **4**, `Uni_Jul_26_SessionExpiry` 2 → **1**. El total de 61 no cambia.
>
> **Pendiente de coordinar con Vedant Shirude** (dueño del ticket) antes de tocar Jira. Detalle completo en `HANDOFF-RCS-28075-2026-08-05.md`.

## Resumen de conteo

| Label | Tickets |
|---|---|
| Uni_Jul_26_SSOMapping | 14 |
| Uni_Jul_26_Attachments | 5 |
| Uni_Jul_26_Requests | 5 |
| Uni_Jul_26_Permissions | 4 |
| Uni_Jul_26_UIBehavior | 4 |
| Uni_Jul_26_LocationHierarchy | 3 |
| Uni_Jul_26_Timeouts | 3 |
| Uni_Jul_26_URLRouting | 3 |
| Uni_Jul_26_ReportsExports | 3 |
| Uni_Jul_26_AlertsNotifications | 3 |
| Uni_Jul_26_SessionExpiry | 2 |
| Uni_Jul_26_IzendaRepoint | 2 |
| Uni_Jul_26_DateTimeZone | 2 |
| Uni_Jul_26_Latency | 2 |
| Uni_Jul_26_DataIntegrity | 2 |
| Uni_Jul_26_DuplicateEmail | 1 |
| Uni_Jul_26_MissingDBObjects | 1 |
| Uni_Jul_26_CaseAssignment | 1 |
| Uni_Jul_26_WAFAccess | 1 |
| **Total aplicado** | **61** |
| Excluidos | 4 (28064, 28026, 28044, 27990) |

Nota sobre la cifra: en el chat se le dijo 45 a J.R., que era lo que traía el filtro 43256. El barrido con todos los estados que él mismo pidió sumó 17 tickets cerrados/completados que el filtro no incluía, más RCS-27573. De ahí sale 61. El encuadre correcto para él: "45 era lo que veía el filtro, con los cerrados de la misma ola son 61".

## Vista en vivo para J.R. y Chris

JQL, agrupable por label desde la barra de búsqueda:

```
project = RCS AND labels in (Uni_Jul_26_SSOMapping, Uni_Jul_26_Attachments, Uni_Jul_26_LocationHierarchy, Uni_Jul_26_Timeouts, Uni_Jul_26_SessionExpiry, Uni_Jul_26_IzendaRepoint, Uni_Jul_26_URLRouting, Uni_Jul_26_DateTimeZone, Uni_Jul_26_CaseAssignment, Uni_Jul_26_Latency, Uni_Jul_26_DuplicateEmail, Uni_Jul_26_MissingDBObjects, Uni_Jul_26_ReportsExports, Uni_Jul_26_AlertsNotifications, Uni_Jul_26_Permissions, Uni_Jul_26_UIBehavior, Uni_Jul_26_DataIntegrity, Uni_Jul_26_Requests, Uni_Jul_26_WAFAccess)
```

Para recorrer un solo bucket en la reunión: `project = RCS AND labels = Uni_Jul_26_SSOMapping` (cambiando el nombre del label).

---

## Uni_Jul_26_SSOMapping (14)

| Ticket | Cliente | Estado | Evidencia |
|---|---|---|---|
| RCS-28078 | Stater Bros | Under Customer Review | Usuarios sin login ni email de reset, patrón email-no-vinculado |
| RCS-28057 | Mattress Firm | Under Customer Review | Root cause documentado: LoginID legacy sin email, password no migrado |
| RCS-28053 | Adusa/Delhaize | Under Customer Review | Pedido del link NON-SAML, config SSO post-migración |
| RCS-28046 | Mattress Firm | Under Customer Review | Manager no aparece en dropdown, misma cuenta sin mapeo que 28057 |
| RCS-28033 | Big Y | Work in progress | Crash al cambiar password, GetSSOPermissionGroupsByUserName sin username |
| RCS-28032 | Vitamin Shoppe | Work in progress | Mismo crash de password update que 28033 |
| RCS-28024 | Vallarta | Under Engineering Review | Email nunca vinculado en ERMS antes del corte |
| RCS-28159 | Smart & Final | Under Support Review | Verificado: usuarios ausentes post-update sin poder loguear, mismo patrón que 28009 (solo migró quien vinculó email); sin investigación aún, clasificación por mecanismo descrito |
| RCS-28067 | Vallarta | Under Customer Review | Verificado: L1 marcó "issue due to recent migration", fix fue proceso masivo de acceso + login por email. Confirma SSOMapping |
| RCS-28009 | Sportsman's | Closed | Verificado: cientos de usuarios no migrados por email no vinculado, LoginID/EmailAddr desalineados, script de migración re-corrido + fixes de Kiran en LPUser2/membership.Users |
| RCS-28042 | Ahold | Closed | Loop de sign-in, GlobalID no llega al SP de grupos SSO |
| RCS-28061 | Stater Bros | Closed | Session Error al actualizar password, familia SecurityLevel NULL / pipeline SSO (RCS-27269) según análisis interno en 28059 |
| RCS-28071 | Stater Bros | Completed | Tiendas que no cambiaron email antes del switch sin login; Kiran corrigió emails en DB. Es email-no-vinculado, no duplicado |
| RCS-28091 | Caribou | Closed | Sin acceso post-migración y el email de recovery nunca llega, mismo patrón de cuenta sin email vinculado |

## LABELS-UNIFICACION-FINAL-2026-08-04 — Uni_Jul_26_Attachments (5)
_chunk 1579 · 2026-08-05 · fuente: LABELS-UNIFICACION-FINAL-2026-08-04.md_

## Uni_Jul_26_Attachments (5)

| Ticket | Cliente | Estado | Evidencia |
|---|---|---|---|
| RCS-28124 | ADUSA | Work in progress | Adjuntos fallan por marca/división, header Content-Disposition duplicado |
| RCS-28105 | Wakefern/VSM | Work in progress | Upload de .exe/video falla, posible duplicado de 28027 |
| RCS-28058 | Stater Bros | Under Customer Review | Sin acceso a adjuntos en la URL nueva |
| RCS-28027 | Wakefern/VSM | Under Customer Review | Regla de seguridad bloqueando .zip con .exe post-migración |
| RCS-28025 | Ahold | Work in progress | No ve adjuntos ni videos desde la URL nueva |

## Uni_Jul_26_LocationHierarchy (3)

| Ticket | Cliente | Estado | Evidencia |
|---|---|---|---|
| RCS-28093 | Ahold | Under Engineering Review | Empleados visibles entre marcas, misma investigación que 28023/28043 |
| RCS-28043 | Ahold | Under Customer Review | Ubicaciones duplicadas entre marcas en jerarquía |
| RCS-28023 | Ahold | Under Customer Review | División mal alineada bloquea creación de casos |

## Uni_Jul_26_Timeouts (3)

| Ticket | Cliente | Estado | Evidencia |
|---|---|---|---|
| RCS-28138 | Stater Bros | Under Support Review | Host error us.apprissretail.com al generar reportes |
| RCS-28112 | Stater Bros | Work in progress | Cloudflare 524 confirmado, origen sin responder |
| RCS-28084 | Vitamin Shoppe | Closed | Verificado: timeout al crear incidente, cerrado con "Unification platforms hotfix created and published". Es timeout de request, no expiración de sesión |

## Uni_Jul_26_SessionExpiry (2)

| Ticket | Cliente | Estado | Evidencia |
|---|---|---|---|
| RCS-28153 | Big Y | Under Support Review | Deslogueo a mitad de trabajo en ER file, pierde progreso |
| RCS-28075 | Ahold | Escalated | 300 min NetTrack vs 30 min Secure, confirmado por Kiran |

## Uni_Jul_26_IzendaRepoint (2)

| Ticket | Cliente | Estado | Evidencia |
|---|---|---|---|
| RCS-28063 | Stater Bros | Under Customer Review | Dashboards Izenda no refrescan post-migración |
| RCS-28021 | Ahold | Resolution Suggested | Save en Izenda caía a página en blanco, config repuntada |

## Uni_Jul_26_URLRouting (3)

| Ticket | Cliente | Estado | Evidencia |
|---|---|---|---|
| RCS-28062 | Stater Bros | Under Customer Review | 404/redirect, patrón de segmento de ruta faltante |
| RCS-28022 | Santikos | Completed | Verificado: URL generada omitía screens/incident/411/lpms/screens, RCA completo y fix de Engineering (ENG-6612 relacionado) |
| RCS-28139 | Sportsman's | Closed | Verificado: pantallas de Audit inaccesibles post-migración, resuelto con rebuild de screens; familia de generación de screens/URLs (RCA de Diego documenta además el 524 del rebuild síncrono en Cohesion mode) |

## Uni_Jul_26_DateTimeZone (2)

| Ticket | Cliente | Estado | Evidencia |
|---|---|---|---|
| RCS-28065 | Stater Bros | Under Customer Review | UTC en vez de PST |
| RCS-28030 | Ahold | Closed | UTC en vez de EST, timestamps renderizados del lado servidor, evidencia completa en el ticket |

## Uni_Jul_26_CaseAssignment (1)

| Ticket | Cliente | Estado | Evidencia |
|---|---|---|---|
| RCS-28123 | ADUSA | Work in progress | "Assigned to can't be blank", asignación no refleja en búsqueda |

## Uni_Jul_26_Latency (2)

| Ticket | Cliente | Estado | Evidencia |
|---|---|---|---|
| RCS-28140 | Skechers | Work in progress | Consulta sobre la degradación de performance de la plataforma post-corte |
| RCS-28107 | Santikos | Closed | Verificado: lag 10x al entrar casos justo después del corte, cerrado tras normalización |

## Uni_Jul_26_DuplicateEmail (1)

| Ticket | Cliente | Estado | Evidencia |
|---|---|---|---|
| RCS-28135 | Ahold | Work in progress | Cuentas duplicadas con sufijo 1/2/3 generadas por migración |

## Uni_Jul_26_MissingDBObjects (1)

| Ticket | Cliente | Estado | Evidencia |
|---|---|---|---|
| RCS-27573 | Tahoe Donner | Completed | Recomendado incluir: aunque fue creado el 26/06 (tabla ACCIDENTEQUIPMENT faltante en tenant DB-only, defecto de completitud de migración), su recaída del 29/07 vino del corte del 27/07 y se resolvió con rebuild de screens. Es exactamente el tipo de caso que el checklist de Chris busca prevenir |

## Uni_Jul_26_ReportsExports (3)

| Ticket | Cliente | Estado | Evidencia |
|---|---|---|---|
| RCS-28151 | Vitamin Shoppe | Under Support Review | Export to Excel no funciona en BI |
| RCS-28007 | Vitamin Shoppe | Work in progress | Reportes muestran año incorrecto |
| RCS-28161 | Delhaize | Under Support Review | Stores.csv no abre para editar lineup |

## Uni_Jul_26_AlertsNotifications (3)

| Ticket | Cliente | Estado | Evidencia |
|---|---|---|---|
| RCS-28131 | Sportsman's | Work in progress | Smart Alerts no funcionan tras migración de DB |
| RCS-28149 | Vitamin Shoppe | Under Support Review | Email autogenerado trunca "075" a "75" |
| RCS-28106 | Santikos | Work in progress | Verificado: Smart Alerts no auto-envían al crear incidentes, relacionado al fix ENG-6612 (SmartAlert attachment path en Cohesion mode) |

## Uni_Jul_26_Permissions (4)

| Ticket | Cliente | Estado | Evidencia |
|---|---|---|---|
| RCS-28141 | Smart & Final | Work in progress | Admin recibe "Permission Required" |
| RCS-28122 | Blain's | Under Support Review | No puede editar campos de usuario |
| RCS-28080 | Stater Bros | Completed | Verificado: admin ve todo gris/readonly post-migración, no puede actualizar usuarios |
| RCS-28094 | Vallarta | Completed | Verificado: tres admins perdieron visibilidad de funciones admin tras el server update, acceso restituido |

## LABELS-UNIFICACION-FINAL-2026-08-04 — Uni_Jul_26_UIBehavior (4)
_chunk 1580 · 2026-08-05 · fuente: LABELS-UNIFICACION-FINAL-2026-08-04.md_

## Uni_Jul_26_UIBehavior (4)

| Ticket | Cliente | Estado | Evidencia |
|---|---|---|---|
| RCS-28115 | Ahold-Delhaize | Under Customer Review | Dropdowns y botón SAVE no responden |
| RCS-28109 | Ahold | Under Engineering Review | Acción "Send to Flock" no se puede ocultar |
| RCS-28005 | Vitamin Shoppe | Under Engineering Review | Secure Audit falla al completar audit |
| RCS-28114 | Stater Bros | Completed | Verificado: botón Save no hace nada al enviar caso, sin spinner ni error, familia UI no responsiva |

## Uni_Jul_26_DataIntegrity (2)

| Ticket | Cliente | Estado | Evidencia |
|---|---|---|---|
| RCS-28036 | Big Y | Under Customer Review | Caso borrado al subir documento a un ER file |
| RCS-28077 | Ahold | Under Delivery Review | Búsquedas de refund devuelven filas duplicadas |

## Uni_Jul_26_Requests (5)

| Ticket | Cliente | Estado | Evidencia |
|---|---|---|---|
| RCS-28158 | McDonald's | Under Support Review | Pedido de subir reporte, no defecto |
| RCS-28156 | Skechers | Under Support Review | Solicitud de spec Workday/COA |
| RCS-28125 | Delhaize | Work in progress | Tarea de validación de datos de prueba EBT (ver nota de consistencia abajo) |
| RCS-28083 | Vitamin Shoppe | Under Customer Review | Pedido de capacitación sobre la UI nueva |
| RCS-28041 | Ahold-Delhaize | Closed | Verificado: pedido de cambiar el display name del sender de los emails, no defecto |

---

## Uni_Jul_26_WAFAccess (1)

| Ticket | Cliente | Estado | Evidencia |
|---|---|---|---|
| RCS-28059 | Ahold | Closed | El bloqueo "Sorry, you have been blocked" fue el Cloudflare WAF default-block rechazando tráfico de Zscaler ruteado por Canadá; el fix fue un allowlist de país. Categoría propia porque el paso de checklist que se deriva ("revisar reglas de WAF por cliente antes del corte") es distinto del de rutas. El RCA interno además detectó SecurityLevel NULL masivo, pero el síntoma reportado y resuelto fue el WAF |

## Excluidos (4)

| Ticket | Motivo |
|---|---|
| RCS-28064 | Status Duplicate (de 28061), J.R. pidió eliminar duplicados |
| RCS-28026 | TJX Europe, no es cliente de la ola de Unificación, falso positivo del barrido |
| RCS-28044 | Descripción vacía, reporter externo no relacionado, ticket inválido |
| RCS-27990 | Verificado: expansión de dígitos EBT es un cambio de formato del lado POS del cliente, independiente de la migración. Fuera de alcance. Nota de consistencia: RCS-28125 (ya aprobado en Requests) es la tarea de prueba del mismo tema EBT; si J.R. considera 27990 fuera de alcance, valdría revisar si 28125 también |

---

## Listas planas para aplicar labels

Cada línea: label → tickets. Entre paréntesis, labels preexistentes a preservar al editar (el resto tiene el campo vacío).

```
Uni_Jul_26_SSOMapping: RCS-28078, RCS-28057 (FromEmail, L1), RCS-28053, RCS-28046 (FromEmail, L1), RCS-28033, RCS-28032 (FromEmail, L1), RCS-28024, RCS-28159, RCS-28067, RCS-28009, RCS-28042, RCS-28061, RCS-28071, RCS-28091 (FromEmail, L1)

Uni_Jul_26_Attachments: RCS-28124, RCS-28105, RCS-28058, RCS-28027, RCS-28025

Uni_Jul_26_LocationHierarchy: RCS-28093, RCS-28043, RCS-28023 (Support_Data_Team)

Uni_Jul_26_Timeouts: RCS-28138, RCS-28112, RCS-28084

Uni_Jul_26_SessionExpiry: RCS-28153, RCS-28075 (Escalated)

Uni_Jul_26_IzendaRepoint: RCS-28063, RCS-28021

Uni_Jul_26_URLRouting: RCS-28062, RCS-28022 (Escalated), RCS-28139

Uni_Jul_26_DateTimeZone: RCS-28065, RCS-28030

Uni_Jul_26_CaseAssignment: RCS-28123

Uni_Jul_26_Latency: RCS-28140, RCS-28107 (Escalated)

Uni_Jul_26_DuplicateEmail: RCS-28135

Uni_Jul_26_MissingDBObjects: RCS-27573 (EB&F_scheduled, Escalated)

Uni_Jul_26_ReportsExports: RCS-28151, RCS-28007, RCS-28161

Uni_Jul_26_AlertsNotifications: RCS-28131, RCS-28149, RCS-28106 (Escalated)

Uni_Jul_26_Permissions: RCS-28141, RCS-28122, RCS-28080, RCS-28094

Uni_Jul_26_UIBehavior: RCS-28115, RCS-28109, RCS-28005, RCS-28114 (AALPS_LPMS_DevOps_OpsGenie)

Uni_Jul_26_DataIntegrity: RCS-28036, RCS-28077

Uni_Jul_26_Requests: RCS-28158, RCS-28156, RCS-28125, RCS-28083, RCS-28041

Uni_Jul_26_WAFAccess: RCS-28059
```

## PLAN-LEAD-unificacion-2026-07-31 — parte 1
_chunk 1581 · 2026-07-31 · fuente: PLAN-LEAD-unificacion-2026-07-31.md_

# Asignaciones pendientes · Tickets de unificación
Juan Martinez, Lead Support Engineer · 31 jul 2026

Tyrone traspasa sus cuatro a Vedant por decisión propia (28058, 28062, 28063, 28065), así que salen de tu reparto. Quedan **nueve** por asignar.

**Ya asignados hoy, no tocar:** 28106 Sebastian · 28084 y 28107 Diego · 28044 y 28091 Nikita · 28053 David.

---

# JUAN MARTINEZ (tú) · 3 tickets
**13 → 16, pero dos se cierran hoy**

## RCS-28080 · Stater Bros · High
*"I use to be able to update like users email address how do I now correct any user information now, looks like everything is grey and readonly."*

**Es un cierre rápido, no un caso de dev.** Tyrone lo dejó en el grupo de "esperando al equipo de dev", pero está en `Under Customer Review`, no en Engineering, y la pregunta es la misma que ya respondieron dos veces: dónde quedó la administración de usuarios en la interfaz nueva. **David ya mandó un video** en el 28083.

| Corregir | Estado |
|---|---|
| Problem | ✅ Ya está bien en `App Functionality Unavailable` |
| Label | ❌ Vacío |
| Team Ownership y Sprint | ❌ Vacíos |

**Links útiles:** RCS-28083 (Vitamin Shoppe, New UI) y RCS-28094 (Vallarta, Admin Function). Son la misma pregunta y ya tienen respuesta.

## RCS-28078 · Stater Bros · High
*"users are unable to log in and are not receiving emails to change password when both using the forgot password option or the reset password option from admin screen"*

Este sí está esperando a dev, y es el caso donde aplica lo que Matt planteó en la reunión sobre **validar en SendGrid** si el correo salió o no. No llegan ni desde el reset del admin.

| Corregir | Estado |
|---|---|
| Problem | ✅ Ya está bien en `Unable to Login` |
| **Assignee** | ⚠️ Está en `Under Engineering Review` **sin nombre**. Debería ser **Shandana Khan** según la matriz. Compara con el 28077, que sí la tiene |
| Label | ❌ Vacío |
| Team Ownership y Sprint | ❌ Vacíos |

**Link útil:** RCS-28053, el de Leigh Ann. Mismo hueco del correo no ligado y del reset que no llega.

## RCS-28059 · Ahold · High
"Sorry, you have been blocked" con la URL nueva de LPMS.

**Ya tienes la causa.** Bloqueo del WAF de Cloudflare al pegarle al dominio raíz `apps.apprissretail.com` sin el slug del tenant. Ray ID `a23606220b52590b` de la instancia de Big Y. Se cierra hoy diciéndole al cliente la URL correcta.

| Corregir | Estado |
|---|---|
| Problem | ❌ Está en `Other`, debería ser `Unable to Login` |
| **Assignee** | ⚠️ En `Under Engineering Review` **sin nombre** |
| Label | ❌ Vacío |
| Team Ownership y Sprint | ❌ Vacíos |

**Link útil:** RCS-28033 (Big Y), que es donde está el Ray ID y el diagnóstico. Y RCS-27766 de Vitamin Shoppe, que lleva tres semanas esperando por el mismo mensaje.

---

# EDWIN GARZON · 2 tickets
**7 → 9 · Data Engineer**

Es el único colombiano al que no le has puesto nada hoy, y los dos son de datos.

## RCS-28036 · Big Y · Medium
Caso borrado, el cliente lo quiere de vuelta.

| Corregir | Estado |
|---|---|
| Problem | ❌ Está en `Other`, debería ser `Data Issue` |
| Label | ❌ Vacío |
| Team Ownership y Sprint | ❌ Vacíos |

**Links:** no hay ninguno obvio, este va solo.

## RCS-28093 · Ahold · Medium
Empleados no restringidos por ubicación de tienda.

| Corregir | Estado |
|---|---|
| Problem | ❌ Está en `Other`, debería ser `Data Issue` |
| Label | ❌ Vacío |
| Team Ownership y Sprint | ❌ Vacíos |

**Links útiles y aquí sí importan:** RCS-28023 (el tuyo) y RCS-28043 (de Viraj). Es la misma investigación y **Kiran ya aplicó un fix amplio**, así que puede que esto ya esté resuelto y solo falte verificar.

## Mensaje

> Edwin, two for you, both data side. RCS-28036 for Big Y, a case was deleted and they want it recovered, so worth checking whether it was lost in the migration or deleted in the app afterwards, because that changes where you look. Big Y moved to the unified platform on July 27.
>
> RCS-28093 for Ahold, employees not being restricted by store location. I linked it to 28023 and 28043 because it's the same investigation and Kiran already pushed a broad fix, so this might just need verifying rather than investigating.
>
> One thing Kiran taught us that saves time: the incident.lpuser view is what the application actually drives on. secure.LocationHierarchyUserAssignments is a migration destination, not the layer that decides whether someone can create a case. For functional symptoms, check the view first.

---

# DIEGO BUELVAS · 2 tickets
**6 → 8 · Full Stack**

Ya tiene 28084 y 28107, los dos de timeouts. Estos dos son de la familia de 404 y URLs, que es el patrón que cerré hoy en Santikos.

## RCS-28027 · VSM · Medium
"VSM - LPMS Error"

| Corregir | Estado |
|---|---|
| Problem | ❌ Está en `Other`, sugerido `App Functionality Unavailable` |
| Label | ❌ Vacío |
| Team Ownership y Sprint | ❌ Vacíos |

## RCS-28105 · VSM · Medium
"VSM-LPMS Errors", creado hoy a las 14:33.

⚠️ **Casi seguro es duplicado del 28027.** Mismo cliente, mismo título prácticamente. **Que lo confirme antes de trabajar los dos**, y si lo es, se linkean como `duplicates` y se cierra uno.

No alcancé a revisar los campos de este, hay que mirarlos.

**Link útil para los dos:** RCS-28022 (Santikos), donde está documentado el bug de generación de URL sin el tramo `screens/incident/<número de cliente>/lpms/screens/`.

## PLAN-LEAD-unificacion-2026-07-31 — Mensaje
_chunk 1582 · 2026-07-31 · fuente: PLAN-LEAD-unificacion-2026-07-31.md_

## Mensaje

> Diego, two more, RCS-28027 and RCS-28105, both VSM. First thing: they look like duplicates of each other, same client and nearly the same summary, so confirm that before you work both.
>
> They might already be fixed. I linked them to RCS-28022 which I closed on Santikos this afternoon, where the app was building URLs without the screens/incident/{client number}/lpms/screens segment so everything past the first step 404'd. It started working after a rebuild and I'm still confirming with Matt what changed. Worth reproducing through Control Panel first to see whether the URLs come through with the full path now.
>
> VSM is Wakefern/ShopRite, migrated July 27, server 7.

---

# NIKITA RATHORE · 2 tickets, para el lunes
**8 → 10 · Full Stack, equipo de India**

Completa su bloque de Mattress Firm. Mándaselo hoy aunque lo lea el lunes, así arranca con contexto y no perdiendo la mañana.

## RCS-28046 · Mattress Firm · Medium
No puede asignar case work.

| Corregir | Estado |
|---|---|
| Problem | ❌ Está en `Other`, sugerido `App Functionality Unavailable` |
| Label | `FromEmail`, `L1`, son automáticos de ingreso por correo |
| Team Ownership y Sprint | ❌ Vacíos |

## RCS-28057 · Mattress Firm · Medium
Access Blocked.

| Corregir | Estado |
|---|---|
| Problem | ✅ Ya está bien en `Unable to Login` |
| **RCS: Issue Type** | ⚠️ **Está vacío** |
| Label | `FromEmail`, `L1` |
| Team Ownership y Sprint | ❌ Vacíos |

**Links útiles:** RCS-28044 y RCS-28091, que ya son de ella. Los cuatro son el mismo patrón.

## ⚠️ El 28044 que ya tiene está roto

Antes del lunes hay que arreglarlo o va a abrir un ticket que no dice nada:
- Product Type dice `Audit (CAMS)`, los otros dos de Mattress Firm son `Incident (LPMS)`
- **La descripción está completamente vacía**
- El reporter es `dennis.lonergan@epicbrokers.com`, un dominio de corredores de seguros que no es Mattress Firm
- Su SLA de asignación lleva horas incumplido

## Mensaje

> Nikita, adding RCS-28046 and RCS-28057 to the two you already have. All four are Mattress Firm and Caribou and they're the same root cause, so one investigation should cover them. No rush on these today, they'll be there Monday.
>
> The cause: in the old lpguys environment a LoginID could be anything, but the new platform needs an email. For six weeks before migration there was a process that forced users to link an email when they signed in, and it re-hashed their password at that same moment. Anyone who didn't sign in during that window has no linked email and no password carried over. For those, Forgot Password goes nowhere because there's no real mailbox, so we set the password directly from admin, Users, Edit.
>
> Both clients migrated July 27 and they're on the same server, 15.
>
> Heads up on 28044, don't start there. The description is empty and the reporter is from an outside domain, so I'm working out what it's actually asking before you spend time on it.

---

# RESUMEN

| Persona | Tickets | Carga |
|---|---|---|
| **Juan** | 28080, 28078, 28059 | 13 → 16, dos cierran hoy |
| **Edwin Garzon** | 28036, 28093 | 7 → 9 |
| **Diego Buelvas** | 28027, 28105 | 6 → 8 |
| **Nikita Rathore** (lunes) | 28046, 28057 | 8 → 10 |

**A Vedant por decisión de Tyrone:** 28058, 28062, 28063, 28065.

---

# LO QUE APLICA A TODOS

**`Team Ownership` y `Sprint` están vacíos en los nueve.** Hay dos campos con nombre casi idéntico en este Jira, confirma cuál alimenta los reportes antes de llenar.

**El label correcto para Incident no lo sé.** El documentado es `Support_Data_Team` y es de Secure 5. Los `FromEmail` y `L1` son automáticos, no de equipo. Pregúntaselo a J.R.

**Valores de Problem en uso:** `Unable to Login`, `App Functionality Unavailable`, `Data Issue`, `Performance Degradation`, `Other`. No conozco la lista completa del desplegable.

---

# ANTES DE CERRAR

**Recuérdale a Tyrone que mueva los cuatro.** A las 16:20 seguían a su nombre.

> Tyrone, thanks, that helps a lot. I'll take the two unassigned ones. Just flagging that 28058, 28062, 28063 and 28065 still show you as assignee, so if you can move those to Vedant before you log off that'd be great, otherwise they'll be sitting under your name on Monday and nobody will spot them.
>
> One thing on 28080, it looks less like a dev item and more like the same read only admin screen question we've had from Vitamin Shoppe and Vallarta, where user administration moved in the new UI. David already answered those with a walkthrough, so I think we can close it out quickly. Let me know if you saw something that says otherwise.

**Y pregúntale a J.R. lo del label.**

> J.R., none of these have Team Ownership, Sprint or a label set. Which label should we be using on Incident tickets? The one I have documented is Support_Data_Team and that's Secure 5.

## PASO-A-PASO-tickets-fuera-de-la-investigacion — parte 1
_chunk 1583 · 2026-07-30 · fuente: PASO-A-PASO-tickets-fuera-de-la-investigacion.md_

# Paso a paso — tickets FUERA de la investigación de migración/unificación
Juan Martinez · L2 Support · actualizado 30 jul 2026, 12:00

Estos 8 tickets no tienen nada que ver con el cutover de ADUSA/Delhaize ni con la ola del 7/27. Nadie los está mirando en ningún war-room, y ahí está el riesgo: **son los que se caen por el hueco mientras todo el foco está en la migración.**

Reglas aplicadas (Kristine Guide + skill de comentarios): interno = directo y técnico; cliente = neutral, factual, sin filler ni empatía excesiva, sin especulación, sin asignar culpa. Cada comentario interno va con el toggle *Internal note* activado.

---

## PRIORIDAD 1 · RCS-27991 — Engage Analytics Not Populating Sections

**High · 3 días · `Under Support Review` · reportado por Paul Marderosian**

Tu mayor riesgo de SLA hoy. Es **High**, lleva 3 días, y sigue en `Under Support Review` estando asignado a ti — o sea, en la cola nadie lo ve como tuyo ni como libre.

### Paso 1 — Status, ya
`Under Support Review` → **`Work in progress`**. Antes de investigar nada.

### Paso 2 — Comentario al CLIENTE (canned response oficial, texto tal cual)

> Hello Paul,
>
> I have taken ownership of this ticket and will be investigating it for you. Please allow some time for me to research the issue and I will get back with you just as soon as I have any information.
>
> Kind regards,
> Juan Martinez
> Support Engineer

### Paso 3 — 30 minutos de análisis
Revisa primero **`Engage Analytics Issue.docx`** (en Downloads) — puede ser un caso ya documentado y te ahorras el ciclo completo.

### Paso 4 — Si no hay causa en 30 min, escala
Checklist L3 obligatorio primero, o Engineering lo devuelve:
- Entorno (Prod / QA / Test).
- Repro paso a paso con screenshots.
- Notas del troubleshooting hecho, incluido lo asistido por IA.
- Notas de conversaciones fuera del ticket.

Luego: status → **`Under Engineering Review`**, asignar a **Ian Williams** (backups: Shruti Golwalker, Kenny Vu), **te desasignas** (en esta ruta la propiedad se transfiere).

**Comentario INTERNO antes de escalar:**

> Escalating to Engage Engineering. Environment: Prod. Repro steps and screenshots above.
>
> Analysis performed: [rellenar — qué revisaste y qué descartaste].
> Cause not identified at L2.
>
> @Ian Williams assigned; flagging on Teams as well.

**Mensaje de Teams a Ian — obligatorio, no ve la asignación solo:**

> Ian — escalating RCS-27991 to you: Engage Analytics not populating sections. Reported by Paul Marderosian, High, open since 7/27. Repro steps and screenshots are in the ticket. Flagging here since the assignment alone doesn't surface for you.

---

## PRIORIDAD 2 · RCS-27840 — Kohl's, Mandatory Workday Security Updates

**Medium · 15 días · `Under Security Review` · deadline del cliente: 1 de agosto**

El deadline es **pasado mañana**. Está en `Under Security Review`, así que la acción técnica es de InfoSec — pero en esa ruta **tú sigues asignado, tú comunicas y tú cierras**. Si el 1 de agosto pasa sin nada, el que queda mal frente a Kohl's eres tú.

### Paso 1 — Comentario INTERNO con el reloj encima

> Deadline check: the customer's mandatory Workday security update deadline is **August 1, 2026** — two days out. This has been in Under Security Review since 7/15.
>
> @InfoSec / linked INFOSEC ticket: I need a status before end of day. If the work will not land by August 1, I need to inform Kohl's now rather than after the fact, including what the impact is if the deadline passes.

### Paso 2 — Ping en Teams a Security hoy
Con el número del ticket INFOSEC linkeado. No el lunes.

### Paso 3 — Según lo que respondan

**Si va a llegar a tiempo** — comentario al cliente:

> Hello Kyle,
>
> Confirming that the required security updates are on track to be completed ahead of the August 1 deadline. Our security team is handling the implementation.
>
> I will confirm here once the work is complete.
>
> Kind regards,
> Juan Martinez
> Support Engineer

**Si NO va a llegar** — avísale hoy, no el 1 de agosto:

> Hello Kyle,
>
> An update on the required security updates. Our security team is still working through the implementation and I do not want to leave you without visibility ahead of your August 1 deadline.
>
> Current position: [rellenar con lo que responda InfoSec — qué queda y cuándo].
>
> If the deadline is a hard requirement on your side, let me know and I will escalate accordingly.
>
> Kind regards,
> Juan Martinez
> Support Engineer

---

## PASO-A-PASO-tickets-fuera-de-la-investigacion — PRIORIDAD 3 · RCS-27573 — Tahoe Donner, Persistent Error Entering Inci
_chunk 1584 · 2026-07-30 · fuente: PASO-A-PASO-tickets-fuera-de-la-investigacion.md_

## PRIORIDAD 3 · RCS-27573 — Tahoe Donner, Persistent Error Entering Incident Reports

**Medium · 34 días · `Work in progress`**

Dos motivos para tocarlo ya:

1. **A 60 días entra a Tiger Team.** Le quedan 26. Ahí se convierte en reporte mensual al support manager.
2. **Tahoe Donner está en la ola de migración del 7/27/2026** (confirmado en `Incident Migration 2026.xlsx`, prod date 7/27, CSM Colleen Knoblock). El ticket es de hace 34 días, o sea **anterior** al cutover — pero conviene verificar si el error cambió, desapareció o empeoró después. Si empeoró, deja de ser un ticket viejo y pasa a ser parte del cluster de post-migración, que es donde hay atención y recursos.

### Paso 1 — Verifica el efecto del cutover antes de cualquier otra cosa

Comentario al CLIENTE:

> Hello Sydney,
>
> Following up on this. Tahoe Donner was moved to our unified platform on July 27, so I want to confirm the current behaviour before continuing.
>
> Are you still seeing the same error when entering incident reports, and is it the same message as originally reported? If the behaviour has changed since July 27, a current screenshot would help.
>
> Kind regards,
> Juan Martinez
> Support Engineer

### Paso 2 — Status
`Under Customer Review` mientras esperas (**pausa el SLA**, que con 34 días encima importa).

### Paso 3 — Según lo que responda
- **Cambió o empeoró tras el 7/27** → comentario interno linkeándolo al cluster de post-migración y súbelo en el canal correspondiente. Deja de ser un ticket huérfano.
- **Idéntico a antes** → sigue siendo un ticket de 34 días con causa sin identificar. Escala con el checklist L3 completo antes de que llegue a 60.

**Comentario INTERNO en cualquiera de los dos casos:**

> Age check: 34 days, approaching the 60-day Tiger Team threshold.
>
> Tahoe Donner migrated to the unified platform on 7/27/2026 (prod wave, CSM Colleen Knoblock). This ticket predates the cutover, so asking the customer to confirm whether the behaviour changed post-migration before continuing L2 analysis. If it changed, this belongs with the post-migration cluster rather than as a standalone.

---

## PRIORIDAD 4 · RCS-28001 (SEA) + RCS-27959 (PacSun) — allow-list de IPs

Hazlos **en la misma sentada**: son la misma clase de trabajo, mecánico, y el contexto mental se reutiliza.

### RCS-28001 — SEA, Engage API IP Allow List
**Medium · 2 días · `Under Security Review`**

Ruta correcta (Security → tú sigues asignado, tú comunicas y cierras). Solo necesita seguimiento:

**Comentario INTERNO:**

> @InfoSec / linked INFOSEC ticket: status check on the IP allow-list addition. Customer has been waiting since 7/28. Do you need anything further from me or from the customer to complete this?

### RCS-27959 — PacSun, IP Whitelisting para acceso MuleSoft
**Medium · 7 días · `Work in progress`**

Este está en tus manos y lleva 7 días. Tienes los adjuntos en `RCS-27959_attachments`. Revisa qué falta y decide: o lo completas o lo rutas.

**Si necesitas datos del cliente** — comentario al cliente:

> Hello,
>
> To proceed with the whitelisting change we need the following confirmed:
>
> 1. [IP/rango exacto a añadir o quitar]
> 2. [Entorno: Prod / Test]
> 3. [Fecha en que necesitan que esté activo]
>
> Once confirmed I will submit the request and update this ticket.
>
> Kind regards,
> Juan Martinez
> Support Engineer

Luego status → `Under Customer Review`.

**Nota de triage:** PacSun aparece como **PSCB (PacSun Eddie Bauer)** en algunos registros. Verifica que la empresa esté taggeada correctamente y que el campo *Export to Power BI* lleve el prefijo — si no, no sale en los reportes.

---

## PRIORIDAD 5 · RCS-27941 — Tailored Brands, SSO/Permissions Issues in Incident

**Medium · 8 días · `Work in progress`**

**Míralo con una lente nueva.** El patrón que salió en la migración es:

```
Failed to create or update sso user
 → Failed to get groups for sso user with the username
 → Procedure or function 'GetSSOPermissionGroupsByUserName'
   expects parameter '@userName', which was not supplied
```

Confirmado por Matt: SSO está configurado para usar **GlobalID** como username y no está llegando, así que el usuario no se puede mapear. Y en la reunión de hoy salió el dato de fondo: en la plataforma nueva el login requiere **email**, mientras que antes usaban un **LoginID**.

Tailored Brands es "SSO/Permissions Issues in Incident". Puede ser la misma familia de fallo de resolución de username y no lo sabes porque llegó antes de que el patrón fuera visible.

### Paso 1 — Comentario INTERNO

> Re-examining this against a pattern that surfaced during the platform migration: SSO user resolution failing with `GetSSOPermissionGroupsByUserName expects parameter '@userName', which was not supplied` — the username claim not arriving, so the user cannot be mapped to permission groups.
>
> Checking whether this ticket is the same failure class. Specifically comparing: which claim is being sent as the username, and whether the account resolves by email vs by legacy LoginID.
>
> Tailored Brands is not part of the migration waves, so if it is the same failure it is not migration-induced — which would make it a pre-existing defect in the SSO user-resolution path rather than a migration side effect.

### Paso 2 — Verifica antes de afirmar
Si confirmas que es el mismo fallo, es un hallazgo fuerte: significa que el bug **no lo introdujo la migración**, la migración solo lo hizo visible a escala. Pero verifícalo antes de decirlo en un canal — es una afirmación con peso.

---

## PASO-A-PASO-tickets-fuera-de-la-investigacion — PRIORIDAD 6 · RCS-27765 (Winn-Dixie) + RCS-27676 (RLC) — rutina Tiger 
_chunk 1585 · 2026-07-30 · fuente: PASO-A-PASO-tickets-fuera-de-la-investigacion.md_

## PRIORIDAD 6 · RCS-27765 (Winn-Dixie) + RCS-27676 (RLC) — rutina Tiger Team

Los dos en `Under Customer Review`, SLA pausado, sin respuesta del cliente. El proceso Tiger Team dice exactamente qué hacer: revisar si se puede mandar comunicación adicional para conseguir respuesta, y **si ya se le dio al cliente la información que pedía**, avisarle con canned response que el ticket se va a completar, **con un plazo concreto**. El plazo depende de cuánto se ha esperado ya y de la naturaleza del ticket.

### RCS-27765 — Winn-Dixie, Data file check (20 días, Heaven Poirot)

> Hello Heaven,
>
> Following up on this ticket. We provided the results of the data file check on [fecha] and have not received a response since.
>
> If there is nothing further you need on this, we will move it to completed on [fecha + 5 días laborales]. If you do still need something, reply here and the ticket will stay open — a reply reopens it automatically even after it is completed.
>
> Kind regards,
> Juan Martinez
> Support Engineer

### RCS-27676 — RLC, SFTP IP/Hostname Change (24 días, Low, Tyler Aken)

Low y 24 días. Plazo más corto:

> Hello Tyler,
>
> Following up on the SFTP IP/hostname change. The information was provided on [fecha] and we have not had a response since.
>
> We will move this to completed on [fecha + 3 días laborales]. If you still need anything, reply here and the ticket stays open.
>
> Kind regards,
> Juan Martinez
> Support Engineer

**Cierre de los dos:** recuerda que solo se completa o cierra **desde `Work in progress`**, y que al resolver son **dos dropdowns obligatorios** — si falta el segundo ("perform customer requested operation") la transición falla. La resolución va como **nota interna**, sin duplicarla en el mensaje de cierre.

Diferencia que importa: **Completed** reabre si el cliente responde; **Closed** no. Para estos dos usa Completed.

---

## Resumen ejecutable

| # | Ticket | Acción concreta | Status destino |
|---|---|---|---|
| 1 | RCS-27991 | Work in progress + canned response + 30 min análisis, luego Ian Williams | WIP → Under Engineering Review |
| 2 | RCS-27840 | Comentario interno con el deadline + ping a Security HOY | Under Security Review |
| 3 | RCS-27573 | Preguntar si el error cambió tras el cutover del 7/27 | Under Customer Review |
| 4 | RCS-28001 | Status check a InfoSec | Under Security Review |
| 4 | RCS-27959 | Pedir IP/entorno/fecha al cliente | Under Customer Review |
| 5 | RCS-27941 | Contrastar contra el patrón `GetSSOPermissionGroupsByUserName` | Work in progress |
| 6 | RCS-27765 | Aviso de cierre con plazo de 5 días | Under Customer Review |
| 6 | RCS-27676 | Aviso de cierre con plazo de 3 días | Under Customer Review |

**Carga actual:** 13 tickets abiertos. El estándar es ~10 por persona, y los de datos pesan más. Estás por encima. Los pasos 6 (cerrar dos) y las transferencias reales de propiedad son lo que baja el número — no el esfuerzo.

## TRIAGE-BACKLOG-2026-08-03 — parte 1
_chunk 1586 · 2026-08-03 · fuente: TRIAGE-BACKLOG-2026-08-03.md_

# Triage del backlog sin asignar
Primer pase agrupado, autorizado por J.R. el sábado · Juan Martinez · 3 ago 2026

---

# El titular

**37 tickets sin asignar hoy.** Ninguno es High. Ninguno es Critical. 34 Medium, 1 Low, 5 sin prioridad puesta.

Eso es lo primero que hay que decir en la reunión, porque cambia la estrategia: esto es **volumen, no severidad**. Y por eso agrupar funciona.

**La aritmética de la reunión.** Al ritmo de 5 minutos por ticket que planteó J.R., 37 tickets son **3 horas y 5 minutos**. Imposible en una hora. Agrupados quedan **11 grupos**, y 11 por 5 minutos son **55 minutos**. Entra justo. Esa es la razón por la que el primer pase valía la pena y por la que J.R. lo aprobó.

## El dato que nadie ha dicho todavía

| Producto | Tickets sin asignar |
|---|---|
| Secure 5 - EBR | **24** |
| Incident (f.k.a. LPMS) | 8 |
| Otros (Audit, Legacy Apis, Engage, Secure 3/4) | 5 |

**El backlog no es la unificación.** La unificación es Incident. Este backlog es Secure 5 en un 65%. Por eso se estancó: todo el mundo lleva dos semanas metido en Incident y en la ola del 27 de julio, y la cola de Secure 5 se fue acumulando sin que nadie la mirara.

Consecuencia práctica: **la gente quemada en unificación no es la que tiene que vaciar esta cola.** Los perfiles de datos del equipo, que es donde vive Secure 5, casi no han tocado unificación.

---

# El equipo real

Tomado de la pestaña Miembros de **Support Appriss** en Teams, no deducido de Jira.

| Persona | Puesto | Grupo | Abiertos | Nota |
|---|---|---|---|---|
| Vedant Shirude | Senior Full Stack Engineer | India | **21** | Recibió los cuatro de Tyrone. **Fuera del reparto** |
| Juan Martinez | Lead Support Engineer | Colombia | **14** | |
| **Sebastian Rueda** | Senior Data Engineer | Colombia | **13** 🔴 | **1 Critical + 1 High.** Y dos tickets de 137 y 101 días. **Fuera del reparto** |
| Bikash Kumar | Data Engineer | India | **10** | |
| Nikita Rathore | Full Stack Engineer | India | **9** | |
| Edwin Garzon | Data Engineer | Colombia | **9** | |
| David Vargas | Full Stack Engineer | Colombia | **8** | Pero **6 en Under Customer Review**, carga activa real 2 |
| Diego Buelvas | Full Stack Engineer | Colombia | **7** | Tres High |
| Gulshan Kumar | DevOps / SRE | India | **5** | 4 en Work in progress |
| **Luis Hernandez** | Senior Full Stack Engineer | Colombia | **0** ✅ | **El primer nombre por la regla de J.R.** |
| Camila Cortes | Support Manager | Colombia | propietaria | Comunicación con cliente |
| Viraj Kansara | Lead Data Engineer | India | el otro lead | Par tuyo, no subordinado |

**Los dos datos que mandan en el reparto de hoy:**

**Luis Hernandez está en cero.** J.R. dijo textual *"start assigning in order one to each person, starting with the person who has the lowest amount of tickets"*. Ese es Luis, y se lleva el bloque más grande.

**Sebastian Rueda es el segundo más cargado y no lo puede recibir.** 13 abiertos, con el Critical de Santikos y el High de refunds de Ahold. Lo único que se le acerca hoy es una consolidación, no trabajo nuevo.

## Los números crudos engañan en dos casos

**David Vargas, 8 pero 6 esperando al cliente.** Está esperando, no trabajando. Carga activa 2. Puede recibir.

**El problema de antigüedad no está en esta cola.** El ticket sin asignar más viejo tiene 82 días. Sebastian tiene **RCS-26088 con 137 días** y **RCS-26632 con 101**, los dos de duplicación de datos. Los tickets realmente viejos ya tienen dueño y nadie los mira. Vale decirlo en la reunión, porque el ejercicio de hoy no los toca y son peores que todo lo que vamos a repartir.

## Cruce urgente que no puede esperar a la reunión

**RCS-28106**, "Santikos SmartAlerts Not working", **Critical**, de Sebastian desde el 31 de julio.

En el análisis del RCS-28112 el viernes, de los 255 errores HTTP 500 del app service de nettrack, **248 estaban en `POST /nettrack/api/internal/SendSmartAlert.aspx`**. Es el mismo endpoint.

Su Critical de Santikos y la degradación de Stater Bros están mirando lo mismo desde dos lados. Habla con Sebastian hoy y linkea 28106 con 28112 y 28114.

## Antes de repartir: dos tickets huérfanos que no están en la cola

No aparecen como "sin asignar" porque tienen nombre, pero el nombre está desactivado.

| Ticket | Cliente | Prioridad | Edad | Detalle |
|---|---|---|---|---|
| **RCS-27549** | ICA SE | **High** | **39 días** | "Degraded system performance". El cliente pidió RCA formal. Asignado a **Carlos Jacinto, cuenta desactivada** |
| RCS-27762 | SSP Group | Medium | 24 días | Secure 3 usando MDS completo en vez de MDS Lite. Misma cuenta desactivada |

**El 27549 es el ticket más grave de todo este ejercicio** y no está en la lista que J.R. mandó. Es el único High, es el más viejo con síntoma activo, y lleva 39 días en una cuenta que ya no existe. Ábrele la reunión con esto si quieres que la sala entienda por qué el proceso falló.

---

# Los 11 grupos

## TRIAGE-BACKLOG-2026-08-03 — G1 · Chemist Warehouse, handover de hypercare (5 tickets)
_chunk 1587 · 2026-08-03 · fuente: TRIAGE-BACKLOG-2026-08-03.md_

## G1 · Chemist Warehouse, handover de hypercare (5 tickets)

| Ticket | Edad | Asunto |
|---|---|---|
| **RCS-28098** | **82 días** | Códigos de ítem vuelven a PLU en items anulados en vez de MyChem/MyMID |
| RCS-28096 | 18 días | Si los datos de recibo reimpreso se están recibiendo y mapeando |
| RCS-28100 | 18 días | Si los datos de apertura de caja se están recibiendo |
| RCS-28097 | 6 días | Hueco de transacciones anuladas del 29 jun al 15 jul |
| RCS-28099 | 5 días | Lógica de descuento por ítem, más compleja de lo esperado |

**Los cinco son iguales por dentro.** Reporter interno (James McKenna), label `clientproject`, título "CWH - HYP to RCS", prioridad **sin poner**, y todos son preguntas de descubrimiento de datos, no incidentes de un usuario bloqueado.

El 28099 lo dice textual: *"plan is to let this be the way it is, continue with hypercare and CW can add this as a ticket in RCS for us to check once CW updates the issue."* O sea, ese ni se trabaja todavía.

**El 28098 es el ticket más viejo de toda la cola, 82 días.** Es el que va a salir en cualquier reporte de aging y va a hacer ver mal al equipo, aunque no sea un cliente esperando.

> **Decisión que hay que sacarle a J.R.:** ¿estos 5 entran al reparto del equipo de soporte o vuelven al equipo de proyecto de Chemist Warehouse? Son 5 de 37. Si vuelven, la cola baja a 32 antes de repartir nada.
>
> Si se quedan: **un solo dueño para los cinco**, no repartidos. Propuesta **Bikash Kumar**, Data Engineer. **No Sebastian Rueda**, que está en 13 con un Critical y ya arrastra cuatro tickets de duplicación de datos. Y ponerles prioridad, porque `Undefined` no aparece en ningún filtro de nadie.

## G2 · Resolución de rol y jerarquía de ubicación (6 tickets)

**El patrón técnico más grande del backlog.**

| Ticket | Cliente | Edad | Síntoma |
|---|---|---|---|
| RCS-28031 | Genuine Parts | 5 días | "Region" de Location Hierarchy no funciona en New Work Items |
| RCS-28054 | Genuine Parts | 4 días | RAPMs configurados por área, varios solo ven New York |
| RCS-28070 | DHL | 4 días | OM no puede editar audit aunque el security setting está activo |
| RCS-28085 | Ollie's | 3 días | RLPM resuelto como DLPM, pierde aprobación de casos |
| RCS-28118 | Myer | hoy | Usuario sin el tile de transferir a Incident, permisos se ven bien |
| RCS-28122 | Blain's | hoy | "With the change we are not able to get to the user fields" |

**Ya asignados, misma familia:** RCS-27857 (Wild Fork, jerarquía en una tienda pero ve todas, **Diego, desde el 16 de julio**) y RCS-28093 (Ahold, empleados no restringidos por tienda, Edwin). Y desde hoy también **RCS-28033** (Big Y, Add Person falla solo a algunos usuarios, tuyo).

Tres cosas que ahorran trabajo:

1. **28031 y 28054 son el mismo problema en el mismo cliente.** El 28054 dice *"when Jim made that change"* y Jim Gould es el reporter del 28031. Se linkean y uno de los dos probablemente se cierra como duplicado.
2. **28122 ya tiene respuesta.** "No podemos llegar a los campos de usuario tras el cambio" es exactamente la pregunta de RCS-28080 (Stater Bros, cerrado) y RCS-28094 (Vallarta), ya contestada con un video. Es cierre de 10 minutos, no investigación.
3. **Regla de Kiran que aplica a todo el grupo:** la vista `incident.lpuser` es lo que maneja la app. `secure.LocationHierarchyUserAssignments` es destino de migración, no la capa que decide permisos. Para síntoma funcional, la vista primero.

**Propuesta: Diego Buelvas** para 28031, 28054 y 28070. Ya lleva el 27857 que es el mismo bug en otro cliente, así que es una investigación, no tres. Los otros tres salen a otros dueños por relación con el cliente, ver G9 y G11.

## G3 · Adjuntos y subida de archivos (3 tickets)

| Ticket | Cliente | Edad | Síntoma |
|---|---|---|---|
| RCS-28000 | Luxottica | 6 días | Factura adjunta desapareció de la sección vendor payment |
| RCS-28101 | Costco | 3 días | "Web Server Returned Unexpected Response" al adjuntar archivo |
| RCS-28124 | ADUSA | hoy | jpeg sí se ve, PDF y MOV no |

**Ya asignados, misma familia:** RCS-28022 (Santikos, `ShowAttachments.aspx` 404, **Juan**), RCS-28058 (Stater Bros, Vedant), RCS-28067 (Vallarta), RCS-28027 (VSM, regla de seguridad bloqueando zips con exe, Diego, ya cerrado).

Tres mecanismos distintos que no hay que fusionar:
- **archivo ausente en el deployment** (28022)
- **regla de seguridad por tipo de archivo** al subir (28101, y el 28027 ya cerrado)
- **filtro de extensiones al leer** (28124)

Pero **la petición a Matt es una sola** y cubre a los tres: revisar el filesystem del app service compartido de nettrack para `/nettrack/lpms/`, y de paso decir cuál es la lista de extensiones permitidas y el límite de tamaño. Una acción, cuatro tickets.

**Propuesta: Juan** para 28000 y 28101, porque ya llevas el 28022 y la conversación con Matt. El 28124 va con el bloque de ADUSA, ver G9.

## TRIAGE-BACKLOG-2026-08-03 — G4 · Conteos e items en búsquedas de Secure 5 (4 tickets)
_chunk 1588 · 2026-08-03 · fuente: TRIAGE-BACKLOG-2026-08-03.md_

## G4 · Conteos e items en búsquedas de Secure 5 (4 tickets)

| Ticket | Cliente | Edad | Síntoma |
|---|---|---|---|
| RCS-28026 | TJX EU | 5 días | Smart track del receipt viewer da 16 txns, el quick link da 31. El cliente sospecha duplicación por filas |
| RCS-28049 | Smyths | 4 días | Búsqueda de Manual Discount duplicando filas, antes no lo hacía |
| RCS-28055 | Genuine Parts | 4 días | Devolución muestra 1 ítem, en TAMS son 4 partes |
| RCS-28117 | Alshaya | 1 día | EC Count 1 y Amount 0.25 en la búsqueda, en el recibo son 3 y 1.85 |

**28026 y 28049 son la misma hipótesis:** fan out de un join a nivel de ítem que multiplica filas cuando hay condición de item level. El 28026 lo dice el cliente solo: *"I wonder if the reason is because its duplicating over several rows."* El 28049 dice *"it does have an Item Level condition"*. Dos clientes distintos, mismo mecanismo probable.

**28055 y 28117 son el espejo:** en vez de duplicar, subcuentan. 1 ítem cuando son 4, EC count 1 cuando son 3.

Duplicar y subcontar en el mismo agregado suelen ser el mismo bug visto desde los dos lados. Vale investigarlos juntos aunque terminen separándose.

**Propuesta: Luis Hernandez** para 28026, 28049 y 28055, porque está en cero y es el primer nombre por la regla de J.R.

**El 28117 va a Sebastian Rueda como consolidación, no como trabajo nuevo.** Él ya lleva **RCS-27951**, "Alshaya - Error Correct Count not captured". El 28117 es "Alshaya - Error correct count and amount incorrect". Mismo cliente, mismo síntoma, muy probablemente duplicado. Se linkea y se cierra uno.

**Y hay contexto que Luis debe leer antes de arrancar:** Sebastian tiene **RCS-27910**, "Alshaya - SHR Report Duplicate lines", que es la misma duplicación de filas de 28026 y 28049 en otro cliente. Linkear los tres ahorra la mitad del trabajo.

## G5 · Datos de item ausentes o retención (3 tickets)

| Ticket | Cliente | Edad | Síntoma |
|---|---|---|---|
| **RCS-27546** | Loblaw / SDM | **40 días** | Campos de ítem en blanco para códigos abiertos de prescripción. Lo abrió la SE Kristen Dyer a nombre del cliente |
| RCS-27846 | 7-Eleven | 19 días | Money order search sin transacciones. Solo trae screenshots, sin texto |
| RCS-28104 | Safeway | 3 días | Búsqueda trae 2023, 2024 y 2025 cuando solo hay 90 días de histórico |

El 27546 es el segundo más viejo de la cola y **lo abrió un SE nuestro, no el cliente**, o sea hay alguien interno esperando también.

El 28104 es el interesante: si solo hay 90 días de retención y la búsqueda devuelve 2023, o la retención no se aplica o los datos viejos no se borraron. Cualquiera de las dos es un hallazgo que aplica a más clientes.

**Propuesta: Edwin Garzon** para los tres. Es trabajo de datos puro, es su perfil, y ya lleva siete de Secure 5.

## G6 · Rendimiento (1 en cola + 1 huérfano)

| Ticket | Cliente | Edad | Estado |
|---|---|---|---|
| **RCS-27549** | ICA SE | **39 días** | **High**, huérfano en cuenta desactivada |
| RCS-27994 | ICA SE | 6 días | Sin asignar. "Slow to get results when loading receipts, and when loading store number adding a work item" |

**Mismo cliente, mismo síntoma, uno huérfano y uno sin dueño.** El cliente reportó lentitud el 25 de junio, pidió RCA, no pasó nada, y volvió a reportarla el 28 de julio con capturas. Desde su lado esto es un mes y medio de silencio.

**Propuesta: Gulshan Kumar.** Es el único **DevOps / SRE** del equipo y esto es exactamente un RCA de rendimiento, no un bug funcional. Está en 5 abiertos, así que tiene espacio. Los dos tickets al mismo dueño y linkeados.

Si Gulshan no puede, esto **no** entra en rotación por carga, sube a Engineering hoy mismo. Es el único High del ejercicio y trae petición formal de RCA.

## G7 · Dashboards y comportamiento de UI (2 tickets)

| Ticket | Cliente | Edad | Síntoma |
|---|---|---|---|
| RCS-28068 | lululemon | 4 días | Engage Analytics, Top 10 SKUs y Top 10 Consumers vacíos. Probó cambiando rangos de fecha |
| RCS-28060 | Starbucks NA | 4 días | Open investigations muestra todas aunque el toggle "show all" esté apagado |

**El 28068 es el mismo síntoma que RCS-27991, que ya es tuyo** ("Engage Analytics Not Populating Sections", High, desde el 27 de julio). El tuyo es interno, el de lululemon es un cliente esperando. Es el único ticket de la cola que cae directo sobre algo que ya tienes abierto.

**Propuesta: Juan** toma el 28068 y lo linkea al 27991. El **28060** es comportamiento de toggle, va con David Vargas en G11.

## G8 · Feeds, archivos y confirmaciones (4 tickets)

| Ticket | Cliente | Edad | Qué es | Esfuerzo |
|---|---|---|---|---|
| RCS-28012 | interno C175_GEU | 6 días | 13 archivos raw_pos_log con error CDATA. Ya investigado en RCS-27225, ~650 ocurrencias en dos meses | Medio |
| RCS-28087 | Academy | 3 días | Empleados en el feed de HR pero no en APIS. 4 números de empleado dados | Medio |
| RCS-28121 | ICA SE | hoy | Confirmación de flujos de datos existentes | **Bajo** |
| RCS-28126 | Kinney Drug | hoy | Avisan que desde el viernes 8/7 dejan de mandar el archivo EmpHours | **Muy bajo** |

**El 28126 no es un problema, es un aviso con fecha.** El cliente está siendo cortés avisando que un archivo va a dejar de llegar el 7 de agosto para que no lo reportemos como faltante. Necesita un acuse y un aviso a monitoreo, nada más. Si nadie lo lee, el viernes generamos una alerta falsa.

El 28012 tiene precedente documentado (RCS-27225, donde ya se ajustó el SnowTime Data Loader para datos malformados), así que arranca con la mitad del camino hecho.

**Propuesta: Bikash Kumar.** Data Engineer, y los cuatro son feeds y archivos. Está en 10 abiertos, así que cuatro es carga razonable si dos de ellos se cierran hoy mismo.

## TRIAGE-BACKLOG-2026-08-03 — G9 · ADUSA / Ahold, la ola de hoy (3 tickets)
_chunk 1589 · 2026-08-03 · fuente: TRIAGE-BACKLOG-2026-08-03.md_

## G9 · ADUSA / Ahold, la ola de hoy (3 tickets)

| Ticket | Edad | Síntoma |
|---|---|---|
| RCS-28123 | hoy | "Assigned to can't be blank" al asignar caso. Muestra asignado en el caso pero no al individuo en la búsqueda. Y llegan varios correos de "you have been assigned case" |
| RCS-28124 | hoy | PDF y MOV no visibles en adjuntos, jpeg sí |
| RCS-28125 | hoy | Datos de prueba de EBT para Delhaize en Zeus 3.5 y Secure 5.4. Relacionado con RCS-27990 |

**Los tres entraron hoy y dos son de Leigh Ann Stubbs**, que ya es la reportera de tus RCS-28023 y RCS-28030. **Es una sola persona con cuatro tickets abiertos con nosotros.** Si los repartimos entre cuatro dueños distintos va a recibir cuatro conversaciones desconectadas, y ella es la voz de ADUSA en la migración.

El 28123 vale mirarlo bien: "asignado en el caso pero no al individuo" más correos duplicados de asignación huele a la misma resolución de usuario del G2, no a un bug de UI.

El 28125 es distinto, es Secure 3/4, es carga de datos de prueba, y ya tiene ticket padre (RCS-27990). Es tarea de datos programada, no un incidente.

**Propuesta: Luis Hernandez** para 28123 y 28124, que son los dos de Leigh Ann y los dos de aplicación. **Edwin Garzon** para el 28125, que es carga de datos.

Y un dato de continuidad: **David Vargas ya lleva el RCS-28053 de Leigh Ann**, el del link non-SAML. Si Luis toma estos dos, los dos tienen que hablarse, porque ella tendría tres tickets abiertos con dos ingenieros distintos.

## G10 · No se pueden trabajar como están (2 tickets)

| Ticket | Cliente | Edad | Problema |
|---|---|---|---|
| **RCS-27753** | PVH Corp | **25 días** | Descripción **completamente vacía**. Título: "Incident report are complete when I click save". Problem = Performance Degradation |
| RCS-28108 | Alo Yoga | 3 días | Descripción **completamente vacía**. Título: "Cameras failing to load. Order #41213355" |

Mismo defecto estructural que el RCS-28044 del viernes. **Nadie puede trabajar esto**, y el 27753 lleva 25 días en los que el cliente cree que estamos investigando algo que no sabemos qué es.

No es trabajo técnico, es una llamada de vuelta al reporter. Es lo más rápido de todo el ejercicio y lo que más mejora la percepción, porque el cliente descubre que sí leímos su ticket.

**Propuesta: Camila Cortes.** Es la manager del equipo y ya hace este seguimiento (lo hizo en el 27840 de Kohl's el 23 de julio). Son dos mensajes, no dos investigaciones. Que salgan hoy los dos.

## TRIAGE-BACKLOG-2026-08-03 — G11 · Sueltos con dueño claro (6 tickets)
_chunk 1590 · 2026-08-03 · fuente: TRIAGE-BACKLOG-2026-08-03.md_

## G11 · Sueltos con dueño claro (6 tickets)

| Ticket | Cliente | Edad | Nota | Propuesta |
|---|---|---|---|---|
| **RCS-28018** | Ollie's | 5 días | "Secure 5 multiple issues", **cuatro problemas en uno**: Receipted Flag y Cash Back Flag dando resultados inexactos, link de Emp Sale ID roto, filter groups desaparecidos de la librería. **Misma reportera que el 28085** | David Vargas |
| **RCS-28085** | Ollie's | 3 días | El que J.R. pidió priorizar. Ver informe | David Vargas |
| RCS-28060 | Starbucks NA | 4 días | Toggle de open investigations ignorado | Luis Hernandez |
| RCS-28103 | Hot Topic | 3 días | Restitución no se envía, no encuentra SETUP en Admin settings, tuvo que quitar a Zelman del provider para ver la lista | Nikita Rathore |
| RCS-28127 | Wegmans | hoy | 674 registros en blanco a borrar por batch delete. **Trae dos precedentes: RCS-18639 y RCS-18926** | Nikita Rathore |
| RCS-28122 | Blain's | hoy | Campos de usuario, ya tiene respuesta conocida | **David Vargas**, es la misma pregunta que su RCS-28094 de Vallarta |
| RCS-27664 | Sainsbury's | 31 días | Estadísticas de uso del reporte TLP. Es pregunta de datos de uso, no incidente | Bikash Kumar |
| RCS-27967 | Target AUS | 10 días | Añadir "Investigation Completed" como Reason for completing. **Ya está en Waiting for Software Release**, el trabajo está encolado | Camila Cortes, solo comunicar |

**Los dos de Ollie's van juntos.** Charity Mackey tiene dos tickets abiertos, ninguno con dueño, y uno de ellos dice que sus filtros guardados desaparecieron. Si atendemos solo el que J.R. señaló, la percepción del cliente no mejora. Son productos distintos, Incident y Secure 5, pero es una sola relación.

**El 28127 es el cierre más rápido de la cola:** tarea de runbook con dos tickets de precedente ya documentados.

**El 27967 no necesita trabajo, necesita un mensaje.** Ya está esperando release.

---

# Propuesta de reparto

Excluye a Vedant (21 abiertos). Reparte por perfil primero y por carga después, que es lo que J.R. pidió al revés, pero en esta cola el perfil manda porque el 65% es Secure 5.

| Persona | Tickets | Nuevos | Queda en | Por qué |
|---|---|---|---|---|
| **Luis Hernandez** | 28123, 28124, 28026, 28049, 28055, 28060 | **6** | 6 | Está en **cero**, es el primer nombre por la regla de J.R. Senior Full Stack. Se lleva los dos de Leigh Ann y el bloque de agregados de Secure 5 |
| **Edwin Garzon** | 27546, 27846, 28104, 28125 | 4 | 13 | Datos puros, ya lleva siete de Secure 5 |
| **Bikash Kumar** | 28012, 28087, 28121, 27664 | 4 | 14 | Data Engineer, feeds y archivos. Dos cierran hoy |
| **Camila Cortes** | 27753, 28108, 27967, 28126 | 4 | | Contacto al reporter y comunicación de estado. Los cuatro son mensajes, no investigación |
| **David Vargas** | 28085, 28018, 28122 | 3 | 11 | Carga activa real 2. El 28122 es la misma pregunta que su 28094 de Vallarta, cierre rápido. Ollie's completo bajo un dueño |
| **Diego Buelvas** | 28031, 28054, 28070 | 3 | 10 | Ya lleva el 27857, mismo bug de jerarquía. Una investigación, no tres |
| **Nikita Rathore** | 28103, 28127, 28118 | 3 | 12 | Incident y permisos, y uno con respuesta conocida |
| **Gulshan Kumar** | 27549, 27994, 28101 | 3 | 8 | DevOps / SRE. Los dos de ICA son un RCA de rendimiento y el 28101 es respuesta del servidor al subir archivo |
| **Juan Martinez** | 28068, 28000 | 2 | 16 | Caen sobre familias que ya llevas, Engage Analytics y adjuntos |
| **Sebastian Rueda** | 28117 | **1** | 13 | **No es trabajo nuevo, es consolidación.** El 28117 de Alshaya es "Error correct count and amount incorrect" y él ya lleva **RCS-27951**, "Alshaya - Error Correct Count not captured". Mismo cliente, mismo síntoma. Muy probablemente duplicado. Se linkea y se cierra uno |
| **Vedant Shirude** | ninguno | 0 | 21 | Excluido, el más cargado |

**Suma: 33 repartidos**, más el 27549 huérfano que no estaba en la lista de J.R.

Quedan **5 de Chemist Warehouse** esperando la decisión. **Si se quedan van a Bikash Kumar, no a Sebastian.** Sebastian está en 13 con un Critical, y además ya arrastra cuatro tickets de duplicación de datos, tres de ellos de 13, 55 y 101 días. Cargarle cinco más de descubrimiento de datos es hundirlo.

## TRIAGE-BACKLOG-2026-08-03 — Lo que hay que proteger, no repartir
_chunk 1591 · 2026-08-03 · fuente: TRIAGE-BACKLOG-2026-08-03.md_

## Lo que hay que proteger, no repartir

**Sebastian Rueda no recibe nada.** Tiene el Critical de Santikos (28106), el High de refunds de Ahold (28077) y dos tickets de 137 y 101 días. Lo que necesita es lo contrario del reparto: que alguien le saque los dos viejos o los cierre. Vale plantearlo en la reunión como el otro lado del ejercicio.

**Y su Critical toca lo tuyo.** Ver el cruce del `SendSmartAlert.aspx` más arriba.

---

# Los 6 cierres rápidos

Si la reunión se alarga y hay que mostrar movimiento hoy mismo:

| Ticket | Por qué es rápido |
|---|---|
| **RCS-27840** (tuyo, Kohl's) | El trabajo está hecho desde el 30 de julio. Solo falta el comentario y cerrar |
| **RCS-28122** (Blain's) | Misma pregunta del 28080 y el 28094, ya contestada con video |
| **RCS-28126** (Kinney) | Es un aviso. Acuse y notificar a monitoreo |
| **RCS-27967** (Target AUS) | Ya está en Waiting for Software Release. Solo comunicar |
| **RCS-28127** (Wegmans) | Runbook con dos precedentes documentados |
| **RCS-28031 + RCS-28054** (GPC) | Probablemente duplicados entre sí. Se linkean y uno se cierra |

---

# Guion de la reunión, 55 minutos

**Minuto 0 a 5. El marco.**
37 sin asignar, ninguno High ni Critical, 65% Secure 5 y no unificación. Peyman bajó de 40 a 26 el sábado pero entraron 9 nuevos, así que el trabajo del sábado sí sirvió. Y el que de verdad importa no está en la lista: RCS-27549, High de ICA, 39 días, en una cuenta desactivada.

**Minuto 5 a 45. Los 11 grupos.**
Un grupo a la vez, no un ticket a la vez. Por cada grupo: qué tienen en común, quién ya lleva algo parecido, voluntario y si no hay voluntario, la propuesta de la tabla. Cuatro minutos por grupo.

**Minuto 45 a 50. Las decisiones que no son tuyas.**
Chemist Warehouse (¿los 5 vuelven al proyecto?), el High de ICA (¿Gulshan o Engineering?), el 27951 repartido a Sebastian Rueda y a Vlad al mismo tiempo, el label correcto para Incident, y **qué se hace con los dos tickets de Sebastian de 137 y 101 días**, que son más viejos que todo lo que estamos repartiendo.

**Minuto 50 a 55. El compromiso.**
Comentario público hoy en cada ticket nuevo. 30 minutos por ticket repartidos en el día, tope de 30, como pidió J.R. Los seis cierres rápidos primero, para que la cola se mueva de verdad hoy y no solo cambie de nombre.

## Lo que hay que decir aunque incomode

Repartir no es resolver. El viernes Chris Rippingale hizo una pasada de comentarios y **14 de unos 20 eran pedidos de seguimiento al cliente**, no hallazgos técnicos. Este backlog no está atascado porque el diagnóstico sea difícil, está atascado porque **nadie está hablando con los clientes**.

La prueba está dentro de esta misma cola: el RCS-27753 de PVH lleva 25 días con la descripción vacía. El 27840 de Kohl's llevaba 6 días resuelto sin que se le dijera. El 27967 de Target ya está esperando release y el cliente no lo sabe.

Si el compromiso de hoy es "comentario público en cada ticket nuevo", eso es lo que va a mover la aguja, más que las 30 horas de investigación repartidas. Vale decirlo así: **el entregable de hoy son 37 clientes que sepan que alguien tiene su ticket**, y el trabajo técnico viene después.

## INFORME-2026-08-03 — parte 1
_chunk 1592 · 2026-08-03 · fuente: INFORME-2026-08-03.md_

# Informe del lunes
Juan Martinez, Lead Support Engineer · 3 ago 2026 · datos leídos de Jira hoy

Contenido: (1) tus 14 tickets en orden de atención, (2) el hilo de J.R. y en qué quedó, (3) lo que repartió Peyman el sábado, (4) los dos mensajes de Viraj y a quién poner, (5) el pedido de J.R. sobre Ollie's.

El análisis del backlog sin asignar va aparte, en `TRIAGE-BACKLOG-2026-08-03.md`.

---

# 1. Tus tickets, en orden de atención

Tienes **14 abiertos**: 3 High, 10 Medium, 1 Low. El orden no es el de prioridad de Jira, es el de riesgo real hoy. Cada uno trae el paso a paso.

**Rutas que se repiten, para no anotarlas cada vez:**

```
Sign-in de un tenant       https://apps.apprissretail.com/<slug>/signin
Screen Manager de un tenant https://apps.apprissretail.com/<slug>/nettrack/Admin/ScreenManager.aspx?admin=9QQP
Impersonación              Control Panel USPROD, buscar el cliente, Impersonate
DB de plataforma           sqldb-prd-wus2-arp-production-<número cliente>-<ABV>-platform
```

El número de cliente y el ABV de cada tenant salen del tracker **Incident Migration 2026**. Ejemplos que ya tienes: Santikos 411 STI, Vitamin Shoppe 433 VSE.

---

## INFORME-2026-08-03 — Bloque 1: se cierran o se mueven hoy sin investigar nada
_chunk 1593 · 2026-08-03 · fuente: INFORME-2026-08-03.md_

## Bloque 1: se cierran o se mueven hoy sin investigar nada

### RCS-27840 · Kohl's · Medium · Under Security Review

**Ya está resuelto y nadie se lo dijo al cliente.**

El 28 de julio Carlson Quick preguntó directo: *"Could you please confirm if these IPs are already allow-listed on your end?"* con las tres IPs. La respuesta ya existe en el RETAILIT-20526 del mismo día. Y el 30 de julio John Mason cerró el CISS con *"Nothing is required here. We dont need to do the certificate validation."*

Trabajo terminado el 30 de julio, deadline del cliente el 1 de agosto, y **6 días sin contestarle**. Resuelto pero percibido como abandonado, en un ticket de seguridad con fecha límite.

**Nota de precisión.** Ni tú ni yo tenemos acceso a RETAILIT-20526, así que la única fuente es la línea que la automatización copió a tu ticket: *"The 3 IP addresses are already part of Kohl's SFTP allow list."* Eso no dice en qué firewall vive la lista. El comentario está redactado para responder exactamente lo que Carlson preguntó sin afirmar de qué lado está, así que es correcto en cualquiera de las dos lecturas.

#### Paso a paso

1. Abre `https://trebuco.atlassian.net/browse/RCS-27840`
2. **Add comment**, tipo **Reply to customer** (el visible para el reporter), y pega el texto de abajo
3. Ahora la transición. **No busques "Completed", desde Under Security Review no existe esa ruta.** Y "Close Ticket" está en el workflow pero con condición no cumplida, por eso no te sale el botón
4. Mueve primero a **Waiting for customer**, que deja el ticket en `Under Customer Review`. Es además el estado correcto por contenido, le acabas de pedir que avise si ve interrupción
5. Desde ahí **Close Ticket** debería habilitarse. Si sigue sin salir, avísame y vuelvo a consultar las transiciones desde el nuevo estado
6. Al cerrar, si te pide **Resolution**, la que aplica es la de trabajo completado, no "Won't Do"

#### Comentario al cliente

> Hi Carlson, Kyle,
>
> Confirming the three IPs you listed are already allow-listed for the Kohl's SFTP integration, so no change was needed to keep the weekly people.txt upload running:
>
> 34.145.42.5
> 34.187.197.14
> 34.11.179.67
>
> Our InfoSec team also reviewed the certificate item and confirmed the GTS Root CA validation is not required for this integration. Nothing further is needed from Kohl's for the August 1 change.
>
> I will close this ticket out. Please reply here or reopen if you see any interruption on the weekly file.
>
> Kind regards,
> Juan Martinez
> Support Engineer

---

### RCS-28030 · Ahold · Medium · Under Customer Review

**Resuelto, solo falta la confirmación del cliente.** Matt confirmó hoy a las 11:58 que la validación y migración de timezone corrió para el resto de los usuarios de ADUSA.

**Corrección de lo que decía antes este documento.** Yo había puesto que había una llamada de una hora propuesta por Viraj y respaldada por J.R., y que la prueba de incógnito seguía pendiente. **Las dos cosas estaban mal**, salieron de mi nota del viernes sin volver a leer el ticket.

Lo que realmente pasó:
- Viraj pidió el incógnito y ofreció una llamada en **un solo comentario, el 31 jul 10:45**. No hay llamada de una hora ni respaldo de J.R. en el ticket.
- **Leigh Ann contestó 16 minutos después, el 31 jul 11:01:** *"I went into a test case this morning and attached a journal entry to the case at 9:50 AM. It was reflected correctly in the platform. I noticed a lot of users with UTC as their time zone. Would each of them have to adjusted to EST?"* O sea, **a ella ya le sale bien** y su pregunta abierta es otra: si a los demás hay que ajustarlos uno por uno.
- Chris Rippingale el 31 jul 14:26: *"Confirmed fix for one user. Run the validation and migration for all other users. Matt doing this right now."*

Consecuencia: el comentario de incógnito que se pegó hoy a las 12:48 pide algo que ella ya había resuelto e ignora su pregunta real. Hay que corregirlo con el seguimiento de abajo.

#### Paso a paso

1. **Pega el comentario al cliente de abajo hoy mismo**, para corregir el de las 12:48
2. **No muevas el estado.** `Under Customer Review` ahora sí es correcto, la pelota volvió a ella
3. Cuando confirme, comentario de cierre y transición. Si "Close Ticket" no aparece, ver la nota del workflow en el RCS-27840
4. **Avisa a Vedant por el RCS-28065**, con el mensaje de abajo, y con la pregunta de PST

⚠️ **Lo que hay que confirmarle a Matt antes de que Vedant cierre el 28065.** ADUSA va a **EST**. Stater Bros es California y su ticket dice textual *"should be PST"*. Si la corrida aplicó EST a los dos tenants, se arregló uno y se rompió el otro. Pregúntale qué zona quedó en cada uno.

#### Comentario al cliente

> Hello Leigh Ann,
>
> Please disregard my earlier message today, I had missed your update from Thursday. Thank you for confirming the journal entry showed the correct time.
>
> To answer your question about the other users showing UTC, no, they do not need to be corrected one by one. The update has now been applied across all of your users.
>
> One thing to expect. The time zone is read from the browser session, so each person will see the corrected time only after they sign out and sign back in. If anyone still shows UTC, a fresh sign in should settle it.
>
> Could you confirm with a couple of your team members once they have signed back in? Once you do, I will close this out.
>
> Thank you.

#### Comentario interno

> Matt confirmed today at 11:58 that the timezone validation and migration ran for the rest of the ADUSA users. Asked the customer to verify with a couple of team members after a fresh sign in, since Incident reads the time zone from the browser session rather than from the profile. Once she confirms, this can be closed.

#### Mensaje para Vedant

> Hi Vedant, on 28065 for Stater Bros, Matt ran the timezone validation and migration and told me it covered the other tenant too, so yours may already be fixed. Two things before you tell the customer. Incident reads the time zone from the browser session rather than the profile, so nobody sees the change until they sign out and back in, and it will look like it failed if you skip that. And Stater Bros should be PST, not EST like ADUSA, so worth confirming with Matt which zone the run actually set for them before you close it out.
---

### RCS-28023 · Ahold · Medium · Under Customer Review

Kiran ya respondió al cliente el 30 de julio con el fix amplio, así que **no mandes nada al cliente**, sería duplicar. Lo único abierto es la verificación interna que él pidió el 30 a la 1:45 PM.

#### Paso a paso

1. Consigue el nombre de la DB de plataforma de Ahold del tracker **Incident Migration 2026**, patrón `sqldb-prd-wus2-arp-production-<n>-<ABV>-platform`
2. Conéctate con tu acceso de lectura y **mira primero la forma de la vista**, porque los nombres de columna deciden la comparación:
   ```sql
   SELECT TOP 1 * FROM incident.lpuser;
   ```
3. Busca a la usuaria reportada:
   ```sql
   SELECT * FROM incident.lpuser
   WHERE email = 'leighann.stubbs@adusa.com';
   ```
4. **Lo que confirma el fix es el conteo de filas por usuario.** Si antes salían duplicadas y ahora sale una sola, está verificado:
   ```sql
   SELECT email, COUNT(*) AS filas
   FROM incident.lpuser
   GROUP BY email
   HAVING COUNT(*) > 1;
   ```
   Si esa consulta vuelve vacía para los usuarios del ticket, ya está.
5. **No consultes `lhua` para esto.** Regla de Kiran: `secure.LocationHierarchyUserAssignments` es destino de migración, no la capa que decide si puedes crear un caso. La app se maneja con la vista
6. Pega el comentario interno de abajo, **ajustado a lo que realmente viste**
7. Deja el ticket en `Under Customer Review`, no lo muevas. Kiran ya cerró el lazo con el cliente

⚠️ **El comentario afirma un resultado.** Si el paso 4 sale distinto, cambia el texto antes de pegarlo.

#### Comentario interno

> @Kiran Vadday Verified on my side. Checking the lpuser view for the reported users, they now resolve to a single row and the duplicate assignments are gone. Leaving this in Under Customer Review since you already confirmed the broad fix to the customer.

**Y no menciones los 380.** Salieron de `lhua`, que no es la capa que decide la creación de casos.

---

## INFORME-2026-08-03 — Bloque 2: los High con cliente caliente
_chunk 1594 · 2026-08-03 · fuente: INFORME-2026-08-03.md_

## Bloque 2: los High con cliente caliente

### RCS-28033 · Big Y · High · Work in progress

**Actualizado hoy a las 11:25.** Kevin Snyder contestó tus dos preguntas y encima solo tiene el auto acuse de Deekshitha de las 11:28. Es tu High con respuesta de cliente más fresca y sin atender, y por eso abre el día.

**Primero: el problema original está resuelto.** Los agentes entran por `apps.apprissretail.com/bigy/signin`. El ticket se llama "LPMS Login Issue" y ya no es eso. Lo abierto es **Add Person**, que apareció el 30 de julio. Vale decidir si lo renombras o si cierras la parte de login y sigues el Person Detail aparte, porque el título no describe el trabajo.

**Lo que dijo Kevin y por qué importa.** Afecta **solo a algunos usuarios**, y los que fallan **fallan distinto**:

| Usuario | Síntoma | Qué significa |
|---|---|---|
| Kevin Snyder | **Funciona**, puede agregar persona | La pantalla existe y es alcanzable |
| Jose Flores | Llena los campos, al guardar el spinner gira y no termina | Falla en el **guardado**, perfil de timeout de request |
| Taylor Larese | No puede ni abrir la ventana de Add Person, page not found | Falla en la **carga**, perfil de 404 de página |

**El dato que descarta lo obvio.** Un archivo faltante en el app service compartido fallaría para todos por igual, incluido Kevin. No es el caso. Entonces **el archivo ausente solo no explica esto**, y aquí manda algo por usuario: rol, permiso de pantalla o jerarquía.

**Hipótesis, marcada como hipótesis.** Las dos cosas se reconcilian si la URL se construye con contexto del usuario. En Santikos (RCS-28022) el defecto era que la app armaba la ruta **sin el tramo `screens/incident/<número de cliente>/lpms/screens/`**. Si ese tramo sale del contexto del usuario, un usuario con contexto mal resuelto recibe URL incompleta y ve 404, mientras otro entra normal. **No está confirmado.** La URL completa de Taylor lo confirma o lo mata en un minuto.

**Corrección a lo que decía antes este documento.** Yo había escrito "si faltan pantallas, Build All Screens y se prueba". **No lo corras a ciegas.** En Santikos el rebuild del 31 de julio coincidió con que la lista de incident types quedó en cero, y esa secuencia está documentada sin causalidad probada. Mirar el Screen Manager sí, reconstruir no.

#### Paso a paso

1. **Pega el comentario al cliente primero**, porque Kevin lleva desde las 11:25 con solo un auto acuse encima. Los dos pedidos técnicos van en el mismo mensaje
2. **Compara los tres usuarios**, que es lo único que aprovecha el "solo algunos". Entra al tenant y ve a `Settings > Users`:
   ```
   https://apps.apprissretail.com/bigy/signin
   ```
   Busca **Kevin Snyder**, **Jose Flores** y **Taylor Larese**, abre cada uno y compara tres cosas: **rol**, **jerarquía de ubicación asignada** y **permisos de pantalla**. Anota en qué difieren Jose y Taylor de Kevin, que es el que funciona
3. Ahí mismo resuelves el pendiente de Chris, que pidió *"Check in Settings > Users if they are signing in since this post or not"*. En esa misma pantalla se ve el último acceso
4. **Los tres contra la vista**, con la DB de plataforma de Big Y:
   ```sql
   SELECT * FROM incident.lpuser
   WHERE email IN ('kevin.snyder@bigy.com');
   ```
   Con la forma de la vista, trae las tres filas y busca la diferencia. Los correos de Jose y Taylor los pides a Kevin en el comentario, o los sacas de Settings > Users
5. **Reproduce por impersonación.** Control Panel USPROD, impersona a **Taylor Larese**, abre un caso, intenta Add Person, y **con devtools abierto en la pestaña Network** captura la URL exacta que se pide cuando aparece el 404. Eso es lo que confirma o mata la hipótesis del tramo faltante, y no dependes de que ella te la mande
6. Después impersona a **Jose Flores**, llena Add Person, dale guardar, y en **Network** mira si el request queda pendiente o devuelve error, y anota la hora exacta para cruzar contra los registros del app service
7. **Screen Manager solo para mirar**, sin reconstruir:
   ```
   https://apps.apprissretail.com/bigy/nettrack/Admin/ScreenManager.aspx?admin=9QQP
   ```
   Busca si existe la pantalla de Add Person o Person Detail y en qué Build Status y Last Build Date está
8. Pega el comentario interno para Chris con lo que encuentres

#### Comentario al cliente

> Hello Kevin,
>
> Thank you for the detail, that helps. The two users are hitting different failures, so I want to handle them separately.
>
> For Taylor Larese, the page not found means the Add Person screen is not being reached at all. Could you ask her to send the full URL from the address bar when the error appears, plus the Cloudflare Ray ID shown on the error page? That tells us whether the link being built for her account is incomplete.
>
> For Jose Flores, the fields load and the save never completes, which looks like the request timing out rather than a missing page. Could you send the date and approximate time of one of his save attempts in your local time? With that I can pull the server side records for that exact request.
>
> Since it works for you and not for them, we are also comparing the three accounts on our side for role and location hierarchy differences.
>
> On the earlier sign-in item, glad the /bigy/signin URL is working. Please make sure any saved bookmarks point to that address rather than the root domain, as the root will keep returning the block page.
>
> Thank you.

#### Comentario interno para Chris

> @Chris Rippingale Following up now. Kevin replied today, the sign-in problem is resolved, agents are getting in through /bigy/signin. What is open is Add Person, and it is user specific rather than tenant wide: Kevin can add a person, Jose Flores fills the fields but the save never completes, Taylor Larese gets a page not found on the Add Person window itself. Since the same screen works for one user and 404s for another, a missing page on the shared app service does not explain it on its own. My working hypothesis is the URL construction defect we documented on Santikos in RCS-28022, where the path was built without the screens/incident/{client number}/lpms/screens segment, which would only misfire for users whose context resolves incorrectly. That is a hypothesis, not confirmed. I am comparing the three accounts in Settings > Users and in the incident.lpuser view, and reproducing Taylor's 404 through impersonation to capture the exact requested URL.

---

### RCS-28112 · Stater Bros · High · Work in progress

El cliente confirmó que ya puede entrar casos pero traer tiendas sigue lento. La alerta #42348 sigue abierta y **se recuperó sola, no la arreglamos**. Está escalado a Jose Parocua.

**Y aquí está el punto del día:** RCS-28114 se abrió el sábado, **Critical**, mismo cliente, misma reportera (Angie Martinez), "UNABLE TO SUBMIT CASE", varias tiendas, y está a nombre de J.R. Teagle. Es la continuación de lo tuyo del viernes por la noche y **ese contexto no está en el 28114**.

#### Paso a paso

1. Abre `https://trebuco.atlassian.net/browse/RCS-28114`
2. **Add comment**, tipo **interno** (visibilidad de equipo, no Reply to customer, porque menciona otros clientes y números de infraestructura), y pega el texto de abajo
3. **Add watcher** con tu usuario, para que las respuestas de Angie te lleguen. Es la razón por la que no te enteraste el sábado
4. En el **RCS-28112**, linkea el 28114 con relación **relates to**: botón `Link` o `More > Link`, tipo `relates to`, key `RCS-28114`
5. Mándale un mensaje a J.R. ofreciendo la reproducción, no la hagas sin que él la pida, porque el ticket es suyo y ya le dijo al cliente que el equipo está encima
6. Deja la alerta #42348 abierta hasta que haya causa. Cerrarla porque se recuperó es lo que hizo que nadie escalara

#### Comentario interno

> Adding context from RCS-28112, same client and same reporter, opened Friday night. Between roughly 20:30 and 22:35 UTC on July 31 the nettrack app service showed around 2495 client timeouts against 255 HTTP 500s, with 248 of those 500s concentrated on POST /nettrack/api/internal/SendSmartAlert.aspx. Alert #42348 recovered on its own rather than being fixed, and it is still open. Case entry started working again for the reporter but pulling up stores stayed slow. My own reading of that ratio is a web request timeout rather than a SQL command timeout, since a command timeout would surface as a 500 with an exception and we don't see that volume, but that is an interpretation and not something the logs state. Happy to run the reproduction across Stater Bros, Santikos and ADUSA if that helps narrow it, since all three are July 27 wave and all three are on the shared nettrack app service.

---

### RCS-28022 · Santikos · Medium en Jira, High en realidad · Work in progress

Escalado por el Director de Seguridad del cliente. Dos partes siguen fuera de Support: el archivo `ShowAttachments.aspx` ausente en el deployment compartido, y los cero items en `fld_MasterCase_CaseType`.

**Lo que falta no es investigación tuya**, es una revisión del filesystem del app service que ya nadie ha hecho. Y esa misma revisión cubre 28058 (Stater Bros), 28124 (ADUSA) y posiblemente 28101 (Costco).

#### Paso a paso

1. Mándale el mensaje de abajo a **Matt Kamminga** por Teams. Es una petición de una sola acción para cuatro tickets, eso es lo que la hace pasar
2. Llévalo también a la reunión de triage como petición formal, para que quede con dueño y no en un chat
3. Mientras eso avanza, en el ticket **no dejes de hablar con Maricela**. Lleva desde el 29 de julio sin servicio en la función principal
4. La segunda parte, los cero incident types, **no la persigas todavía**. Está documentada en la nota interna y depende de saber si el rebuild puede vaciar listas, que es la misma pregunta abierta del 28033

#### Mensaje para Matt

> Hi Matt, one request that covers four tickets instead of one. Could someone check the filesystem of the shared nettrack app service for the pages under /nettrack/lpms/, specifically whether ShowAttachments.aspx is present in the current deployment? On Santikos the 404 comes from ASP.NET's own CheckVirtualFileExists, so the file is genuinely absent rather than misrouted. Stater Bros 28058 and ADUSA 28124 look like the same gap from the customer side, and Costco 28101 fails on upload rather than read. While someone is in there, the allowed extension list and the size limit would answer 28124 and 28101 in one go. Right now that is four parallel investigations for what might be one deployment gap.

---

### RCS-27991 · Appriss interno · High · Work in progress

Engage Analytics no puebla secciones. Sin tocar desde el 30 de julio.

**Hallazgo:** RCS-28068 (lululemon, "Top 10 SKUs and Consumers not loading", sin asignar desde el 30 de julio) es el mismo síntoma en el mismo dashboard. El tuyo es interno, el de lululemon es un cliente esperando.

#### Paso a paso

1. Abre `https://trebuco.atlassian.net/browse/RCS-28068` y asígnatelo, o llévalo a la reunión como tu ticket del reparto
2. Linkea los dos: en el 28068, `Link > relates to > RCS-27991`
3. **Comenta el 28068 hoy**, aunque no tengas causa. Lleva 4 días con solo el auto acuse y la clienta ya probó cambiar rangos de fecha, o sea descartó lo obvio sola
4. Trabaja uno solo. Si el interno y el del cliente tienen la misma causa, una investigación cierra los dos

#### Comentario al cliente para el 28068

> Hello,
>
> Thank you for the detail, and for noting that adjusting the date ranges made no difference, that helps narrow it.
>
> We have the same behaviour reproduced on our side in the Top 10 tables of the Engage Analytics dashboard, so this is being looked at as a platform item rather than something specific to your configuration. I am picking it up directly and will update you as soon as I have something concrete.
>
> Thank you for your patience.

---

## INFORME-2026-08-03 — Bloque 3: esperando a alguien más, mantener el pulso
_chunk 1595 · 2026-08-03 · fuente: INFORME-2026-08-03.md_

## Bloque 3: esperando a alguien más, mantener el pulso

### RCS-28032 · Vitamin Shoppe · Work in progress
Joe Austin lleva **5 días** sin responder, tu último comentario fue el 29 de julio.

**Paso a paso.** Un solo mensaje a Joe cubre tres tickets, así que no mandes tres. Pide en el mismo comentario: si Brandon sigue bloqueado (28032), un ejemplo concreto de audit con nombre, tienda y número de caso (28005) y el screenshot con URL, error completo, Ray ID y número de tiendas (28084). Después avisa a los dueños de los otros dos que el pedido salió consolidado.

> Hello Joe,
>
> Following up on this one. Login to the Incident platform is working on our side, so I need to confirm whether Brandon is still seeing the error. If he is no longer blocked, I will close this ticket. If the error is still there, a screenshot of what he sees would let me pick it up from where we left off.
>
> While I have you, two other open items would move much faster with a detail from your side. For the audit item, a concrete example with the audit name, store and case number. For the timeout item, a screenshot showing the full error and the Cloudflare Ray ID on the page, plus roughly how many stores are affected.
>
> Kind regards,
> Juan Martinez
> Support Engineer

### RCS-28021 · Ahold · Resolution Suggested
Jie Chen confirmó que era configuración del reporte, un join mal armado, no capacidad de plataforma.

**Paso a paso.** Recordatorio al cliente pidiendo la validación, y si no contesta en 48 horas se cierra por resolución sugerida. Y no lo cuentes como evidencia de degradación del origen en ninguna conversación de timeouts, contamina la muestra.

### RCS-27959 · PACSUN · Under Customer Review
Whitelisting de IPs para MuleSoft. **Mismo cliente que el 28040 de Viraj.**

**Paso a paso.** Que quien tome el 28040 se lleve este también, ver sección 4. Una sola relación con PSEB.

### RCS-27765 · Winn-Dixie · Under Customer Review
Data file check, sin movimiento desde el 27 de julio. **Paso a paso:** recordatorio de estado, es lo único que falta.

---

## Bloque 4: los que se están envejeciendo en silencio

### RCS-27573 · Tahoe Donner · Medium · **38 días** (26 jun)
Error persistente entrando incident reports. Es tu ticket más viejo y es funcional, no una pregunta.

**Paso a paso.** Decide hoy una de dos y no una tercera: o entra en tu semana con fecha, o le dices al cliente dónde está. Lo que no puede seguir es en silencio a los 38 días. Si no entra esta semana, este comentario:

> Hello,
>
> I want to be straight with you about where this sits. The error you reported is still open on our side and has not had the attention it should have had, largely because of the platform work of the last few weeks.
>
> I am picking it back up. To restart it cleanly rather than from old notes, could you confirm whether the error is still happening, and send a screenshot of the current message along with the approximate time it last occurred?
>
> Thank you for your patience.

### RCS-27941 · Tailored Brands · 12 días
SSO y permisos en Incident, sin tocar desde el 29 de julio. **Paso a paso:** revisa si el síntoma cae en el patrón de rol y jerarquía del G2 del triage, porque si sí, entra en la investigación de Diego y no en la tuya.

### RCS-27676 · Ralph Lauren · Low · 28 días
Cambio de IP y hostname de SFTP. **Paso a paso:** es el mismo tipo de trabajo que el 27840 de Kohl's, va por Infra con ticket RETAILIT. Mira si ya hay uno abierto antes de crearlo.

---

## INFORME-2026-08-03 — El orden, resumido
_chunk 1596 · 2026-08-03 · fuente: INFORME-2026-08-03.md_

## El orden, resumido

| # | Ticket | Primera acción concreta |
|---|---|---|
| 1 | **RCS-28033** | Comentario a Kevin, y comparar los tres usuarios en Settings > Users |
| 2 | **RCS-27840** | Comentario, mover a Waiting for customer, cerrar |
| 3 | **RCS-28114 / 28112** | Comentario interno, ponerte como watcher, linkear |
| 4 | **RCS-28030** | Comentario de corrección al cliente, y avisar a Vedant con la pregunta de PST |
| 5 | **RCS-28022** | Mensaje a Matt, una revisión para cuatro tickets |
| 6 | **RCS-28023** | Correr la consulta de duplicados, comentario interno a Kiran |
| 7 | **RCS-27991 + 28068** | Linkear y comentar el del cliente |
| 8 | **RCS-28032** | Un pedido consolidado a Joe Austin por tres tickets |
| 9 | **RCS-27573** | Decidir: entra con fecha o se le dice al cliente |
| 10 | El resto | Por estado normal |
---

# 2. El hilo de J.R. y en qué quedó

Tu respuesta pasó. J.R. contestó el sábado a las 11:41: *"Eso me funciona bien, Juan."*

Eso significa que **hoy no arrancas leyendo la cola en frío**, arrancas con la cola ya agrupada, que es exactamente lo que quedó autorizado. El documento `TRIAGE-BACKLOG-2026-08-03.md` es ese primer pase, hecho.

Lo que cambió desde el viernes: Peyman movió la cola de 40 a 26 el sábado, pero **entraron 9 nuevos entre sábado y hoy**, así que hoy hay **37 sin asignar**. Vale decirlo al abrir la reunión, porque si no, parece que el trabajo del sábado no sirvió, y sí sirvió.

---

# 3. Lo que repartió Peyman el sábado

Peyman se movió solo sobre la cola y bajó de 40 a 26. Reparto que hizo:

| Ticket | A quién | Nota |
|---|---|---|
| RCS-27935 | David Beck | |
| RCS-28079 | Ian Williams (Engage Engineering) | "He will advise" |
| RCS-27977, RCS-27983 | Peyman | En el 27983 pidió ayuda a Adrash Kumar |
| RCS-27978, RCS-27951, RCS-28047 | Sebastian Rueda | |
| RCS-27951, RCS-28016, RCS-28017 | Vlad | ⚠️ **27951 aparece dos veces**, a Sebastian y a Vlad. Uno de los dos va a trabajar en algo que ya tiene dueño. Vale aclararlo antes de la reunión |
| RCS-28008 | Carl Costelow | Home Depot. Peyman cree que termina en Engineering. En Jira hoy figura a nombre de **David Parraga**, en Under Delivery Review, tocado hoy a las 06:35. O Carl lo reasignó o Peyman se equivocó de nombre. Verifica |
| RCS-28074 | Nikita Rathore | Lulu, nuevo tender type Google Pay eComm. Confirmado en Jira |
| RCS-28086 | Edwin Garzon | Kohl's, NULL EndTransDateTime. Confirmado en Jira |

**Dos cosas para ti como lead:** el 28074 y el 28086 entraron a tu equipo sin pasar por ti, así que Nikita queda en 9 y Edwin en 9. Eso cambia la aritmética del reparto de hoy. Y el duplicado del 27951 es un choque real que cuesta horas si nadie lo ve.

**Nota de nombres:** el "Sebastian" de Peyman es **Sebastian Rueda**, de tu equipo. **David Beck no es de tu equipo**, el David del equipo es **David Vargas**. Vale tenerlo claro al hacer seguimiento, porque son personas distintas.

---

# 4. Los dos mensajes de Viraj

## INFORME-2026-08-03 — 4.1 RCS-28040, PSEB / PacSun, reunión el martes 10 am PST
_chunk 1597 · 2026-08-03 · fuente: INFORME-2026-08-03.md_

## 4.1 RCS-28040, PSEB / PacSun, reunión el martes 10 am PST

**Qué es de verdad.** No es "necesito la URL de test". Eso ya se lo dio Viraj el 29 de julio (`https://pacsun-qa.apprissretailcloud.com/`). El problema real está dos comentarios más abajo: Roseanne Auran entra a la pantalla de Appriss, le sale el **Microsoft Sign In**, y no le acepta ninguno de sus dos correos. Ella misma da la pista buena: *"We had this problem before when we switched from PACIFIC SUNWEAR to PACSUN in our email addresses."* Y el 31 de julio empeoró, ya no puede ni cargar el sitio, le sale error de acceso.

O sea: **identidad y federación en el entorno QA de Secure 5, con un cambio de dominio de correo de por medido**. No es un problema de datos ni de reporte.

Contexto de la reunión: la agenda la maneja **Paul Marderosian** (CSM), y él la unificó con el tema de credit card number vs account number que Roseanne también tenía abierto. Invitación ya enviada para el martes 4 a las 10 am PST, o sea **12 del mediodía hora Colombia**, horario cómodo. Paul puso a Tyler y Carlos como opcionales, y Carlos Jacinto ya está desactivado en Jira, así que ese asiento está vacío de verdad.

**Mi recomendación: Luis Hernandez.**

Los candidatos reales de Colombia en tu equipo son cinco: Diego Buelvas, Sebastian Rueda, Edwin Garzon, Luis Hernandez y David Vargas.

| Persona | Puesto | Abiertos | Ajuste al problema |
|---|---|---|---|
| **Luis Hernandez** | **Senior Full Stack Engineer** | **0** | **El mejor por las dos vías.** El fallo es de identidad y federación en la capa de aplicación, no de datos, y eso es full stack. Siendo senior sostiene la llamada con Roseanne y con Paul sin escalar. Y está en cero, así que no hay argumento de carga contra |
| David Vargas | Full Stack Engineer | 8, pero 6 esperando cliente | Perfil correcto y carga activa real de 2. Es el respaldo |
| Diego Buelvas | Full Stack Engineer | 7 | Perfil correcto pero tiene tres High encima, incluidos 28078 y 28084. No le cargues una llamada de cliente |
| Sebastian Rueda | Senior Data Engineer | **13** 🔴 | Descartado. Es perfil de datos y además el segundo más cargado del equipo, con un Critical y un High activos |
| Edwin Garzon | Data Engineer | 9 | Mismo caso, es de datos |

Carga verificada de todo el equipo: Vedant 21, Juan 14, Sebastian 13, Bikash 10, Nikita 9, Edwin 9, David Vargas 8, Diego 7, Gulshan 5, **Luis 0**.

Respuesta para Viraj (un párrafo, es Teams):

> Hi Viraj, I'd put Luis Hernandez on 28040 and on the Tuesday call. What's failing is the Microsoft sign in on the QA tenant rather than anything on the data side, so it needs a full stack pair of eyes, and being senior he can hold the call with Roseanne and Paul without escalating. Worth noting the ticket has drifted from the original ask, Roseanne has the URL already, what she can't get past is the sign in, and she points at the PACIFIC SUNWEAR to PACSUN domain change as having caused something similar before. We also have RCS-27959 open for the same client, so I'd keep both with whoever takes this one.

## INFORME-2026-08-03 — 4.2 "Can we meet today later to review unassigned queue and tickets fo
_chunk 1598 · 2026-08-03 · fuente: INFORME-2026-08-03.md_

## 4.2 "Can we meet today later to review unassigned queue and tickets for guys who left?"

Sí, y llegas con datos. Dos hallazgos concretos para esa reunión:

**Carlos Jacinto está desactivado en Jira y sigue con dos tickets abiertos a su nombre:**

| Ticket | Cliente | Prioridad | Edad | Estado |
|---|---|---|---|---|
| **RCS-27549** | ICA SE | **High** | **39 días** (25 jun) | Work in progress. "Degraded system performance, slow response times and delayed loading". El cliente pidió explícitamente root cause analysis |
| RCS-27762 | SSP Group | Medium | 24 días | Secure 3 usando MDS completo en vez de MDS Lite |

El 27549 es lo grave: un **High de rendimiento, con petición formal de RCA, en manos de una cuenta desactivada, hace 39 días**. Y en la cola sin asignar está **RCS-27994**, también de ICA, también lentitud, abierto el 28 de julio. Mismo cliente, mismo síntoma, uno huérfano y el otro sin dueño. Van juntos al mismo dueño y hoy.

De Tyrone no encontré tickets abiertos a su nombre en RCS, así que su traspaso a Vedant sí se completó. Los cuatro (28058, 28062, 28063, 28065) están a nombre de Vedant, confirmado.

**Consecuencia de eso que vale decir en voz alta:** Vedant quedó en **21 abiertos**, el más cargado del grupo por mucho. Tú vas segundo con 14. Si hoy repartimos por "el que menos tiene", Vedant no recibe nada.

Y el punto de proceso que Viraj ya planteó el viernes y tiene razón: pedir que quien se va deje **OOO permanente** en Teams y que su cola se vacíe antes del último día, no después. Vale llevarlo como acción a J.R., porque un High de 39 días en una cuenta muerta no lo agarra ninguna alerta.

Respuesta para Viraj (un párrafo, es Teams):

> Hi Viraj, yes let's meet, I'll come with the 37 unassigned already grouped. On the people who left, Carlos still has two tickets under his deactivated account and one is RCS-27549, an ICA performance High open 39 days with a formal RCA request, plus RCS-27994 is another ICA slowness ticket unassigned since the 28th, so those two need one owner today. Tyrone's four did move to Vedant so that one is clean, though Vedant is now at 21 open and shouldn't be in today's round. And I'm with you on the permanent OOO, a 39 day High on a dead account is not something any alert catches.

---

# 5. El pedido de J.R. sobre Ollie's, RCS-28085

**Contexto que J.R. no puso en el mensaje.** El ticket está **sin asignar** desde el 31 de julio a las 08:11. Lo único que tiene es el auto acuse de Shireesh Ramdas un minuto después. **Cero contacto humano en 3 días.** Eso es lo que hay que arreglar primero, antes de investigar nada.

**Qué reporta el cliente.** Charity Mackey (cmackey@ollies.us): el RLPM **Scott Blackwell** aparece como **DLPM** y perdió accesos, entre ellos aprobar casos enviados por DLPMs. Antes estaba bien. El IT de Ollie's ya confirmó que el archivo de empleados que nos manda trae el rol correcto, RLPM.

**Lo que significa técnicamente.** Si el archivo entra correcto y el sistema resuelve mal el rol, el problema está del lado de la resolución de rol y jerarquía, no del feed. Y ahí no está solo:

| Ticket | Cliente | Síntoma | Estado |
|---|---|---|---|
| **RCS-28085** | Ollie's | RLPM resuelto como DLPM, pierde aprobación | Sin asignar |
| RCS-28093 | Ahold | Empleados no restringidos por ubicación de tienda | Edwin |
| RCS-28054 | Genuine Parts | RAPMs deberían ver solo su área, varios ven solo New York | Sin asignar |
| RCS-28031 | Genuine Parts | Location Hierarchy "Region" no funciona en New Work Items | Sin asignar |
| RCS-27857 | Wild Fork | Jerarquía puesta en una sola tienda, ve todas | Diego, desde el 16 jul |
| RCS-28118 | Myer | Usuario sin la opción de transferir a Incident, permisos se ven bien | Sin asignar, hoy |
| RCS-28070 | DHL | OM no puede editar audit aunque el security setting está activo | Sin asignar |

Son **siete tickets de resolución de rol y jerarquía**, seis clientes distintos, cinco sin dueño. Ese es el patrón más grande del backlog y el 28085 es su cara visible ahora porque J.R. lo está mirando.

**El otro dato de Ollie's:** también tienen **RCS-28018** sin asignar desde el 29 de julio, "Secure 5 multiple issues", con cuatro cosas dentro: Receipted Flag y Cash Back Flag dando resultados inexactos, el link del campo Emp Sale ID roto, y filter groups guardados que desaparecieron de la librería de Charity Mackey. **Es la misma reportera.** Charity tiene dos tickets abiertos con nosotros, ninguno con dueño, y uno de los dos dice que sus filtros guardados desaparecieron. Si atendemos solo el que J.R. señaló, la percepción del cliente no mejora.

**Recomendación:** los dos al mismo dueño, hoy, y el comentario público sale hoy en los dos. Son productos distintos (Incident y Secure 5) así que técnicamente no es el mismo trabajo, pero la relación con Charity Mackey sí es una sola.

Respuesta para J.R. y Camila (un párrafo, es Teams):

> Hi J.R., taking care of it. 28085 has been unassigned since Thursday with nothing on it but the auto acknowledgement, so the first fix is a real reply today rather than the investigation. Same reporter also has RCS-28018 unassigned since the 29th, so I'm putting both under one owner instead of only the one that got escalated. On the technical side their IT confirmed the employee file has Scott Blackwell as RLPM, so if he resolves as DLPM it sits with role and hierarchy resolution on our side, which is the same pattern as five other unassigned tickets I'm grouping for today's triage.

---

# 6. Lo que hay que preguntar hoy

1. **A Peyman:** el 27951 está repartido a Sebastian y a Vlad al mismo tiempo. Cuál queda.
2. **A Peyman o Carl:** el 28008 aparece a nombre de David Parraga, no de Carl Costelow. Cuál es.
3. **A J.R.:** cuál es el label correcto para tickets de Incident. El que tienes documentado es `Support_Data_Team` y es de Secure 5. Sigue sin respuesta desde el viernes.
4. **A J.R.:** los 5 tickets de Chemist Warehouse en la cola tienen prioridad `Undefined` y son handover de hypercare, no incidentes de cliente. ¿Entran al reparto del equipo o vuelven al equipo de proyecto? Son 5 de 37, la respuesta cambia el tamaño del problema.
5. **A Matt:** la revisión única del filesystem del app service de nettrack para `/nettrack/lpms/`. Cubre 28022, 28058, 28124 y posiblemente 28101 de una sola vez.

## Cheat Sheet — parte 1/5
_chunk 1660 · 2026-07-22 · fuente: Cheat Sheet.docx_

Cheat Sheet
EBR Exception Based Reporting  (AKA- SECURE 5)
Incident (AKA- LPMS/NetTrack)
Audit (AKA-CAMS)
Engage (AKA – Verify/ TRE)
Legacy ASPECT and APIS
Delivery team is also implementation
Dev Ops is engineering
TIP:  If you don’t know what team someone is on check their Teams Profile and see which tree they fall under.  Some people’s profile says they are engineers, but they are actually in the delivery team. Don’t forget the SRE on duty. Check the calendar. On-call schedules - The Retail Equation, Inc
Team leads:  Carl Costello --- Implementation EBR, application configuration, CCTV, SSO
Jon Morgan --- Engineer EBR
Matt Kamminga --- Development (Incident/Audit and Legacy APIS)
Ian Williams --- Implementation/Engineering Engage
Engage tickets to go to Solution Expert Marissa Johnson:
Gap Claims eligibility tickets are also seen as void claims requests.
Any issue with the portal that support cannot complete.
LINKS:
Release Calendar | Appriss Retail Documentation
RCS ticket triaging process
Apis WIKI page with all training documents
APIS - AALPS - Confluence
Client Contacts.xlsx
GitBook External
Security Information Trust Portal for Appriss Retail
RCS-22987    Has information for clients looking for Appriss DR Plan & Annual Test Documentation We can give this out, YES!
https://trustportal.apprissretail.com
Decommission Tickets Must be initiated by CSM’s
Decommission Application Ticket Process
Portal Link
https://support.apprissretailcloud.com
Help desk  This information is also found  in company links: Go to Help Desk Folder > Help desk Ticket
https://trebuco.atlassian.net/servicedesk/customer/portal/6
Steps for Peyman’s team    Data Support Team
.
Platform Unification - everything you need to know | Product Documentation
Our support teams operate from a customer support ticketing portal.  I am adding an application administrator that has access to our portal on this email string.
@ please see the request below. If technical assistance is required, please open a ticket.
Our support teams are fully dedicated to providing you with the highest level of assistance. Our teams work through our customer support ticketing portal. To assist with the issue you are reporting, I am including an application administrator in this email thread who has access to our portal.
If there is a need for additional individuals to have access to our portal, please feel free to contact me. I am happy to assist in adding those who require the ability to open tickets and communicate with our support teams through our portal. Furthermore, you may submit a ticket requesting the addition of someone to our customer support ticketing portal, and we will be happy to facilitate this request.
Kristin Krogman
October 15, 2025 at 2:04 PM
Hello Julie,
This ticket has been created after XXX contacted our Level One team. You have been set as the reporter due to XXX not having access to the portal. If XXX is someone who should have access, please advise, and an invitation will be sent out.
I have also sent an email to you with this information.
Please let us know if you will be reaching out to the associate to provide the necessary information or if technical assistance is needed; this ticket can be moved to our support engineers to review.
Please let us know how you would like to proceed.
Dick’s Sporting Goods opens the same ticket often. Here is an Example Ticket RCS-22191  DSG - Missing file DKS_incent4dsg_20250724*.csv.gpg* from Apriss
Message that can be sent:
Hello
I hope this message finds you well.
It's possible that our process was slower than expected, resulting in the report not being generated on time. Typically, when this occurs, the next report will include records from the missed night.
The file should be sent later today, and it will contain the missing transactions. If you find that this file is still missing tomorrow morning, please don't hesitate to reach out via this ticket and the team will follow up.
Thank you for your understanding and patience.
Demo info:
Product Launches:   https://trebu.sharepoint.com/:f:/s/ApprissRetailMarketing/EmW3gm8vZdxNiten7YJQLPABeJfJuxtHGG8fOjrYiJsncw?e=z1ANup
Portal Search Steps
If you go to the portal on the landing page where you can open a ticket, you will see a magnifying glass in the upper right corner.
You can type in what you need assistance from our teams. For example, case types brought up several different articles.
Work Items
For WORK ITEMS MISSING/NOT LOADING needs to become a HIGH PRIORITY post in SECURE OUTAGES CHANNEL. If it is a single item, then no OpsGenie.
From: Aimee Wadsworth Sent: Friday, January 5, 2024 1:05 PMTo: DG-L1RetailCustomerSupport <l1retailcustomersupport@apprissretail.com>Cc: DG-L2RetailCustomerSupport <L2retailcustomersupport@apprissretail.com>Subject: RE: Updating priority on ticketsImportance: High
Hello again.
I have some clarifications and updates regarding the below.

## Cheat Sheet — parte 2/5
_chunk 1661 · 2026-07-22 · fuente: Cheat Sheet.docx_

The original email below will remain in place for all TJX tickets.  Any ticket priority created by/for TJX will remain as requested by the customer.
As for others, we will go back to using our judgement. However, there are times that we have changed to Medium in the past, where we will not change it moving forward – items such as:
Any TJX ticket (as mentioned above)
Any issues accessing the application(s), even for one user
Application Slow / Timeout issues
Permissions issues/errors, especially if they are an Admin/Power User
Thank you for your hard work and understanding.  Please let me know if you have any questions.
High Priority and Ops Genie: Secure 5 Issues Team 4.2.24 (only dataops 8-8 on the weekends.  They want the Opsgenie during the week.  Per Aimee via Kenny and Team)
Client Listing PW information:
DoNotTouch666!
Signet RTI:
TJX  01.16.25
Hi Kristin,
Thank you for passing on the information below. Is it possible for you to update who our Application Admin is? Jonathan Bouchard has moved to another role. If you could replace his information with mine (chris_moore@tjx.com), it would be greatly appreciated. If we can have more than one admin listed, please add Christine Barski (christine_harkness@tjx.com) to the list as well.
Thanks.
Chris Moore
Senior Investigations Analyst
Nordstrom Apis contact
Nordstrom EBR  Brent Hamlin  per Michael F
McDonalds Admins
Hugo and Paulett (Not Erika)
IT HELP DESK NEW NUMBER 8.2023 Hey all, it has come to my attention that the our IT help desk phone number has changed. If you need to call in due to issues with your computer you would need this number. 1 (928) 272-4889
Information to get to BAMBOO HEALTH.
https://apprissretail.com/about/contact/ This is a link to the business form and contact information for BAMBOO.  https://bamboohealth.com/contact/
MethCheck is now with Equifax.
I was provided the following URL: https://methcheck.appriss.com/retail/pharmacy/loginForm.do
PSE MethCheck is part of Bamboo Health products and not Appriss Retail product, We request you reach out to your contacts on Bamboo Health side, We hope this helps. Thank you!
https://bamboohealth.com/contact
https://bamboohealth.com/customer-support/
VERIFY ACCT INFO: [11:01 AM] Marissa Johnson
Once an account is created or reset, the access code lasts for 14 days. Once logged in, they have to access the system every 90 days or else we disable it. We send notification that we're going to disable.
How do I find their Pin for a reset if it doesn’t get sent? (See notes below)
correct and the code is good for 14 days
once he logs in, the access code field will clear out
search for his name and click on his account.
and it's here
RTIaas portal
A ticket came in for a shell single site employee looking for access to the “portal”
For Shell you should request access from the RSI Admin team, or you could ask Jessica Easley/Connie Gimbel for guidance.
Thanks,Toby Jackson
SHELL INFO
The way the process is to work, is the requestor should contact the RSI Admin Team who manages the UAM request for the SIP EAV/Tooling.  Shell users should not contact Appriss directly.  The RSI Admin Team supports all UAM request for Project and Operations for all environments of SIP; TST, PPE, and PRD.
The RSI Admin Team will follow our process which includes an approval step before submitting the request to Appriss via the RCS Ticketing Portal.
RSI Admin will try to verify with the user once the request is completed an update the RCS ticket accordingly.
If response is not received, we have an agreement that the RCS tickets can be auto closed after 14 days (2 weeks).
I would recommend you not grant access to Dilip-kumar-reddy.l@shell.com and instead advise the requestor to follow the defined process.  They can reach out to me directly if additional assistance is required.
Thanks,
Jessica
Jessica.Easley@shell.com
RCS-17690
Hey Appriss, Shell has defined teams who have access to your RCS portal for raising tickets. David’s request should be processed by one of teams he represents. If he is a member of that team, that team’s supervisor will raise the request for access to the RCS Portal. And then he will be able to raise RCS tkts directly. If he is not a member of a support team for SIP and simply needs assistance with a request, he should direct that to one of the support teams. I am not sure what your requirements are, but this is the alignment we previously agreed upon with Shell SOM. If you have not already, I would advise David to engage with myself to explain the process further and I will try to redirect him to the correct Shell side Team.
RTI portal Access    Shell
RTIaas Portal Access Request
Re: [RCS-14217] Re: RTIaaS Portal Access Request
Hi Murat,
All portal access requests need to be sent to the RSI Admin team within Shell. These requests are fulfilled by them rather than our Support team.
@ITSO-SOM-DS-RSI-Admin-Team@shell.com – please can you assist Murat.

## Cheat Sheet — parte 3/5
_chunk 1662 · 2026-07-22 · fuente: Cheat Sheet.docx_

This ticket will be closed as there is no further action required by the Appriss/SIP team at this time.
Best,
James.
---
James Bell
Lead Technical Program Manager
Appriss Retail
Meijer info
Point of contact for Genetec video integration issues is Ryan Theem. Ryan.Themm@meijer.com
Jason Schuitema is no longer with the asset protection team.
VITAMIN SHOPPE
I will reach out to the store.  Also, I don’t know if you can add this to your notes, but if a store contacts the Appriss Support team, can you tell them to contact their respective RLPM?  This will help alleviate any calls that you are getting and the RLPM can let them know the proper steps to follow.
If not, no worries, just thought I would ask.
Thanks
Joe Austin   joseph.austin@vitaminshoppe.com
Safety & Loss Prevention, Supply Chain
Husband. Father. Health Enthusiast
Shop with us   |
KOHLS:  Setting up associates in the application. (per Kathleen)
Here is his information:
James Edwards (ROB) Team Lead, LP Exception Based Reporting James.Edwards@kohls.com Office: 262 703 6706 Cell: 505 400 9239
Ahold/Delhaize    LPMSSupport@retailbusinessservices.com     Zeus info
I have been provided with the following email regarding questions/issues with Zues. AskZeus@adusa.com
If you reach out to that email address, they will be able to assist you.
Becky LaPierre provided that information.
They know to reach out to LPMS Support and then if I can’t fix it or requires your assistance then I will log a ticket.   You can reject and refer them to LPMSSupoort@retailbusinessservices.com in order for me to try and fix first.
Thanks,
Leigh Ann StubbsAdministrator, Corporate Asset Protection
ICA  --   effektivrutinanalys@ica.se
Hello,
I have added the following email to this chain. effektivrutinanalys@ica.se  this team should be able to assist with your request.  If they are having difficulty with your request, they will open a support ticket for assistance.
ASDA
Canned response to stores:
Hello,
We have been asked by the ASDA application administrators that you refer your inquiry to the following:  lposa@asda.co.uk.
The administrators will open a ticket with our support team if they need assistance investigating your request.
carl.reeson@asda.co.uk  is an Admin contact.
From: Carl Reeson <Carl.Reeson@asda.co.uk> Sent: Wednesday, January 17, 2024 9:17 AMTo: Kristin Krogman <kkrogman@apprissretail.com>Subject: RE: Appriss access
EXTERNAL SENDER
Hi Kristin
Can you refer all enquiries for the new system to lposa@asda.co.uk
We have been asked by the ASDA application administrators that you refer your inquiry to the following email address:  lposa@asda.co.uk.
The administrators will open a ticket with our support team if they need assistance investigating your request.
Regards
Carl
Costco
lossprevention@costco.com
adamtabor@costco.com
Walmart Help Desk Here is the script that Jovan approved: March 18, 2026
For issues and access to Secure, follow this link, http://wmlink/AP1. Once on the landing page of this page, you may click on the “Secure Store” tile to gain access to the application.  To report issues for the application please click “Contact Support” in the User Menu and complete a survey.  A member of the Secure investigation team will contact you regarding your issue.
If you do not receive assistance with the previous link, you can also reach out to the Walmart Help desk.
http://wmlink/securehelp
or
https://wmlink.wal-mart.com/secureaudithelp
https://trebuco.atlassian.net/browse/RCS-16890
Any ticket for Walmart that references their Auror system has to go to delivery.  We do not have access to that system
GAP Admin for Secure 5:   Michelle_Anderson-Silva@gap.com
Also, for future reference, please leverage the Secure Issue/Feedback intake form linked under the Quick Links menu to report issues or give feedback.
Secure (EBR) Issue/Feedback Intake.
The Home Depot Secure and Engage
——- this was the below note I had shared before with the L1 team ——- HOME DEPOT CALLSFor home depot calls we receive you can raise RCS when it's Engage related and they have been locked out. Rest of the other issues of Home depot goes to HD_Investigations@homedepot.com. We don't want them added to the portal though.  - Please make note of their Email address correctly. Any call for THD Return where the customer is reporting they can’t override return authorization they have to Override Via the Engage Portal THD is the only customer to have the return override through their Engage Portal. We can always let the user check with their store manager or Team Lead on this.FYI if they would call back THD US stores recently they moved that functionality (return overrides) to the Engage reporting portal instead they are supposed to go to the Engage portal. https://engage.apprissretailcloud.com/   They could still ask their team lead. Your team isn't responsible for opening a ticket for them on this issue.
We have been asked to have you submit your request to HD_Investigations@homedepot.com.

## Cheat Sheet — parte 4/5
_chunk 1663 · 2026-07-22 · fuente: Cheat Sheet.docx_

We have been asked by the Home Depot Application Administrators to have you submit your request to HD_Investigations@homedepot.com.
INFORMATION for VERIFY for an override: Go to My Apron on the POS screen.   That is the area they will need to go to be able to get the override they need.  There will be a TRE Link there.   Hopefully you won't have to give out this information.
Kristin is correct, the Appriss link is located on myApron. You can find the link under several paths, including by searching for “TRE” or “Appriss” in the search bar, or myApron<Applications <S-Z <T(2) < The Retail Equation/Appriss. If you don’t have access to the Appriss Store Manager Override Portal, please submit a request for access group “TRE_Storemanagers” in myTHDaccess.
The Appriss link is located on myApron.  You can find the link under several paths including searching for “TRE” or “Appriss” in the search bar, or myApron<Applications <S-Z < T(2) <The retail Equation/Aprriss.   If you don’t have access to the Appriss Store Manager Override Portal, please submit a request for access group “TRE_Storemanagers” in myTHDaccess.
Hello,
We have different applications that you might be trying to access. If you are trying to access TRE/Verify… There are a few reasons why you may not be able to access the portal. Please follow the below steps to troubleshoot the error:
•    Ensure that you have access in myTHDaccess. If you don’t, please request access to entitlement group “TRE_StoreManagers”.
•    On the Appriss/TRE homepage, ensure that the email address you enter ends with @HomeDepot.com
•    On the Appriss/TRE homepage, ensure that you select “US”. Canada is selected by default.
If you are trying to access Secure we have been asked to have you submit your request to HD_Investigations@homedepot.com.
We have been asked by the Home Depot Administrators to have you submit your request to HD_Investigations@homedepot.com.
The Home Depot Canada Engage:  For Canada, you can refer to Nadia Vivan. nadia_vivan@homedepot.com
New information from Marissa 7/16/26
corey_hendrick@homedepot.com
AP_Returns_Inquiries@homedepot.com.
Please respond and copy the following email address into it:
AP_Returns_Inquiries@homedepot.com
We’ll address!
Thanks,
Heather Bolling | The Home Depot | Asset Protection
o: 770.433.8211 x81904
m: 678.296.0202
Hi Donna,
Thank you for reaching out regarding your access issue.
There could be a few reasons why you may not be able to access the portal. Please follow the below steps to troubleshoot the error:
•    Ensure that you have access in myTHDaccess. If you don’t, please request access to entitlement group “TRE_StoreManagers”.
•    On the Appriss/TRE homepage, ensure that the email address you enter ends with @HomeDepot.com
•    On the Appriss/TRE homepage, ensure that you select “US”. Canada is selected by default.
Changed information for HD
Hello Javier,
Thank you for reaching out in regard to your access issue!
There are a few reasons why you may not be able to access the portal. Please follow the below steps to troubleshoot the error:
•    Ensure that you have access in myTHDaccess. If you don’t, please request access to entitlement group “TRE_StoreManagers”.
•    On the Appriss/TRE homepage, ensure that the email address you enter ends with @HomeDepot.com
•    On the Appriss/TRE homepage, ensure that you select “US”. Canada is selected by default.
If you still experience login issues after completing these steps, please reach out to Wilton Redd WILTON_REDD@homedepot.com.   He is copied on this email.
US Contacts
Denver Culpepper
Melissa Somer
Nicholas Faiola
Marc Boissoneault
Matthew Crider
Canada
Christopher Dacosta
Doug Hill
Blain Mcavoy
Ericka Smith
Thanks,
2 hours ago
EXTERNAL SENDER
Hi Kristin,
For support tickets that come across regarding access issues, can we direct the individuals to submit a request to HD_Investigations@homedepot.com?
We have a couple of know issues that our IT partners are working through and this will help reduce some of the redundancy.
Thanks!
Denver Culpepper
Manager Investigative Analytics | Asset Protection
THE HOME DEPOT
Denver_J_Culpepper@HomeDepot.com
IT Help desk ticketing URL: https://trebuco.atlassian.net/servicedesk/customer/portal/6
Subject line
Appriss Retail Customer Support Ticketing Portal Access Information
It has been requested by XXXX that you will need access to our ticketing portal. Once your credentials are set up you will be able to open tickets for any concerns or questions with our applications.
You will be receiving an invite in a few minutes from Appriss/Jira to set up your credentials. Be advised that the link that is being sent to you does expire quickly.  Please set up your credentials as soon as possible after receiving the invitation.  Check your junk mail if you do not see the invite within 10 – 15 minutes of this email.
Please make your password 12 characters or less for your credentials.

## Cheat Sheet — parte 5/5
_chunk 1664 · 2026-07-22 · fuente: Cheat Sheet.docx_

You may receive an error message when you go to the link, but please go to where it says Log In and click on it to proceed.
If this doesn’t work for you, please let me know and we will continue to our next steps if necessary.
https://support.apprissretailcloud.com

## Tiger Team tickets Process
_chunk 1665 · 2026-07-30 · fuente: Tiger Team tickets Process.docx_

Tiger Team tickets Process
Monthly Excel spreadsheet is updated weekly by removing and adding tickets that are over 60 days old. This is completed by running the following filter
https://trebuco.atlassian.net/issues/?filter=35856
Export the file and compare the new file to the current one. Remove completed/closed tickets. Mark tickets that are no longer on the list in the closed tab.
Add the new tickets to the spreadsheet and mark totals on the new to the list on the total tab page.
Update any new dates, statuses, and comments.
Follow up on under customer review by checking if additional communication can be sent to retrieve a response. If the client has been provided with the needed information let the client know by using the canned response function that the ticket has been completed and will be moved to completed/closed status. Provide a timeline for ticket closure to allow the client time to respond. Timeline is dependent upon how long we have already waited for a response and the nature of the ticket.
Follow up via email with assignees every 4-6 weeks to be sure they are aware of their open tickets. If an assignee has one or two tickets that are not under customer review status, you can reach out via teams to be sure they are aware of the ticket or internally communicate within the ticket ask for an update.
Final step is to update the Tiger Team ticket created over 3 months ago. (Shared doc)
At the end of the month the Tiger Team spreadsheet is sent to the support manager for additional reporting.

## How to set up Engage Portal user
_chunk 1666 · 2026-07-30 · fuente: How to set up Engage Portal user.docx_

Setting up an Engage portal user
The following ticket is an example for this type of request. RCS-18625
You will need to have access to the Engage portal. Speak with your manager about access.  An ITHD may need to be opened for this request.
To complete the request, you will need the associates:
cell phone (We text an access code as part of our two-factor authentication during initial login)
email address
access needed (easiest to ask whose access can be replicated)
*Note - If they do not have someone’s access they want to replicate, then this ticket should be sent to the Engage Solution Expert to complete.
Go to the Engage Portal
Bring up the person they want to replicate access.
Click edit to see what access they have. (Screenshot the page or move it to a side screen to copy access.)
Admin > Add user > You should be on the page below:
enter email
check boxes they need for access
retailer dropdown pick the organization
add phone number.
click on save changes
You will receive the following message:
Send a note on the ticket that says:
XXX’s account has been created. They should have an email with his temporary credentials. Please let me know if they run into any issues.

## Engage Password Reset Locked Out
_chunk 1667 · 2026-07-30 · fuente: Engage Password Reset Locked Out.docx_

Engage portal customer is locked out of system and needs a reset password.
Example ticket:  RCS-25784
These requests can also come in via phone call or email to the support address.  If they are not in the customer support ticketing portal a ticket will not be opened for them.
Before doing a reset for call or email requests, validate that the request coming in is from a current associate. Check the email address and signature line.  If you have doubts, reach out to the organization’s administrator for Engage and verify that this request should be completed.
You will need the associates email address that is locked out of the application.
Login to Engage portal
Go to Admin Web Users Listing
Add their email address to the search and click on the refresh button. (yellow arrow)
You will be prompted by the following message:
Click Yes, reset password for user.
You will then receive the following message:
Send confirmation to the client either via email or ticket.

## Support_Schedule 1 — parte 1/3
_chunk 1668 · 2026-07-22 · fuente: Support_Schedule 1.docx_

Appriss Retail
Service Availability and Support Schedule
Effective Date: [EFFECTIVE DATE]  --  Version 2.0
Overview
This Schedule sets forth Appriss Retail's ("Company") service availability commitments, incident response priorities, support services, and training obligations applicable to Client as specified in the applicable Order Form. This Schedule supersedes all prior versions of the Service Availability Schedule and Training and Support Schedule and consolidates them into a single unified document.
1. Ways to Contact Us
All support requests -- regardless of priority level -- must be submitted through the Appriss Retail Support Portal:
Support Portal: https://support.apprissretailcloud.com  (available 24x7x365)
For P1 - Critical incidents, submit a ticket through the portal at any time. Company maintains 24/7 Level 1 support coverage and will escalate to on-call resources for all P1 incidents, including those submitted outside of Business Hours.
2. Hours of Operation
a. Standard Support Hours
Standard support is available Monday through Friday, 9:00 AM to 5:00 PM Eastern Time, excluding US public holidays ("Business Hours"). This applies to P2, P3, and P4 priority levels.
b. P1 - Critical Incidents (24/7 Coverage)
P1 - Critical incidents may be submitted through the Support Portal at any time. Company maintains 24/7 Level 1 support coverage. All P1 tickets submitted outside of Business Hours are actively monitored and will result in engagement of on-call resources.
c. Portal Availability
The Support Portal is available 24x7x365 for ticket submission, status tracking, and all support communications across all priority levels.
3. Service Availability
a. Uptime Commitment
Company will make commercially diligent efforts to maintain the Appriss Retail Platform and applicable Module(s) at no less than ninety-nine and 7/10ths percent (99.7%) availability ("Uptime Availability") during each month of the Initial Term and any Renewal Terms, excluding Scheduled Maintenance (which shall not occur between the hours of 6:00 AM and 9:00 PM Pacific Time) and Exclusion Events as defined in Section 7.
b. Service Level Credits
In the event that the Module(s) fail to achieve Uptime Availability during any month of the Term, Client shall be entitled to a credit of monthly fees according to Table 1 below ("Service Level Credit").
Uptime Availability
Service Level Credit (% of Monthly Fee)
At or above 99.7%
0%
93.00% - 99.69%
2%
Below 93.00%
5%
c. Credit Request Process
To receive a Service Level Credit, Client must submit a written request no later than sixty (60) days following the month in which the non-conformity occurred. Service Level Credits are Client's sole monetary remedy for any Service Commitment failure.
4. Incident Priority Levels and Response Times
For all incidents reported by Client or independently identified by Company, Company will strive to provide a First Response based on the priority level defined in Table 2 below. Priority classification shall be determined by Company's support engineering team using reasonable commercial judgment. Response time targets apply during Business Hours for P2-P4. P1 targets apply 24/7 -- submit P1 tickets through the Support Portal at any time.
Priority
Definition
Target Response Time
P1 - Critical
The Appriss Retail Platform and/or Module(s) have completely ceased to function for all users, or core functionalities (e.g., transaction processing, data ingestion, or platform login) are entirely non-operational for all users.
1 hour (24/7 via portal)
P2 - High
A majority of the Platform or Module(s) cannot be accessed, or a majority of users cannot access the Platform or Services (e.g., significant feature degradation, widespread data discrepancies, or large-scale login failures).
4 business hours
P3 - Medium
The Platform is operational for most users, but certain functionalities are degraded or unavailable for a limited subset of users (e.g., specific report failures, module-specific issues, or integration delays).
12 business hours
P4 - Low
Issues that do not significantly impact the ability to use the Platform or Module(s), including cosmetic issues, known issues with existing workarounds, feature or enhancement requests, or general questions addressable during Business Hours.
Reasonable period
Note: Response time commitments represent the time from receipt of a reported incident to First Response (as defined in Section 11). These commitments do not constitute a guarantee of Remediation within the same timeframes. Company will communicate progress and work diligently toward timely Remediation in all cases.
5. Escalation Procedure
In the event of concerns regarding the pace or quality of support, Client may escalate as follows:
a. 1st Level of Escalation
Customer Support Manager
b. 2nd Level of Escalation
Customer Success Manager and/or Customer Account Manager
c. 3rd Level of Escalation
VP of Customer Support

## Support_Schedule 1 — parte 2/3
_chunk 1669 · 2026-07-22 · fuente: Support_Schedule 1.docx_

Company and Client shall each maintain and share at least three levels of escalation contacts (including name, title, email address, and mobile/office numbers) through VP levels. Escalation contacts shall be exchanged at the time of contract execution and updated as needed.
6. Chronic Termination Rights
Client may, upon ten (10) days prior written notice to Company, elect to terminate the applicable Order Form without liability, charge, or penalty under the following circumstances:
a. Service Level Deficiency
The Module(s) fail to comply with the Service Availability Level for three (3) consecutive months, as established by Company's IT records.
b. Incident Response Deficiency
Four (4) or more P1 or P2 incidents fail to meet target response times for three (3) consecutive months, as established by Company's IT records.
Chronic termination rights must be exercised within sixty (60) days of the last month containing a qualifying deficiency.
7. Exclusion Events
Company will not be responsible for downtime or Service Level deficiency resulting from any of the following ("Exclusion Events"):
Failure of any component not under Company's control, including but not limited to third-party AI foundational models incorporated into the Products, Client-provided or Client-managed power sources, networking equipment, computer hardware, software, or internet and telecommunications access;
Acts of God, war, insurrection, terrorism, riot, strikes, interruption of power or communications service, or other causes beyond Company's reasonable control;
Client-initiated changes, whether implemented by Client directly or by Company on Client's behalf;
Viruses, except where downtime results from failure to apply a generally available and approved remedy or patch within twelve (12) hours of a documented outbreak;
Operating system software revisions or hardware/software configurations that are not tested and approved by Company;
Client's failure to adhere to Company's change management processes and procedures;
Acts or omissions of Client, its employees, agents, or third-party contractors (other than Company);
Corrupt or incorrectly formatted Client data; or
Failures that cannot be remediated because Client is inaccessible.
8. Support Services
a. Generally
Subject to payment of the applicable Subscription Fee, Company agrees to provide Client with the maintenance and technical support services described in this Section ("Support Services"). Unless otherwise agreed in writing, Support Services consist of 2nd and 3rd Line Support during Business Hours for defects in software used to perform the Services and for user requests that cannot be resolved by Client's trained 1st line support staff.
b. Support Portal
Company's technical support staff will provide Client 24x7x365 access to the Support Portal at https://support.apprissretailcloud.com for submission of all software (non-service-availability) issues and questions. Tickets will be processed based on their assigned priority level as defined in Section 4. Client may view ticket status at any time through the portal.
c. Training and Business Process Issues
Issues related to training, business process questions, general end-user system use, or other non-defect matters are not considered support issues and will be escalated to the User Consultant team. If the associated effort falls outside the scope of the Client's Module-specific Customer Assurance Program, the hours may be billable to Client at the then-current consultant rate.
d. Enhancement Requests
Issues identified as enhancement requests will be escalated to the Customer Success Manager to determine whether Client wishes to proceed with a formal estimate or Statement of Work. The CSM will coordinate with development operations and Client to scope the effort and applicable fees.
e. Tracking
Company will track and log all Support Services requests and provide Client a secure means of contacting Company during Business Hours to inquire about any request.
9. Training
a. Initial Training
Company will conduct administration and analyst training on the use of the applicable Module(s) during the Implementation process. Up to twenty (20) hours of post-implementation training and consultancy will be provided within the three (3) months following production availability. Up to eight (8) hours of end-user training will also be provided, delivered either as direct training or as a train-the-trainer session.
b. Additional Training
Additional training beyond the hours specified above may be arranged through the Customer Success Manager at mutually agreed costs. Client is responsible for developing and maintaining any internal training materials, training videos, or other resources for its employees.
10. Updates and Custom Services
a. Software Updates

## Support_Schedule 1 — parte 3/3
_chunk 1670 · 2026-07-22 · fuente: Support_Schedule 1.docx_

Company will make available regular releases of updated software to its customers. Updates include enhancements and other changes to the Appriss Retail Platform or Module(s) covered under Client's license. Release notes will accompany each update. Features delivered in an off state require Client to open a support case to enable them.
b. Custom Services
If Client requests Support Services not covered by this Schedule ("Custom Services"), the parties will negotiate in good faith on an agreement that describes the Custom Services and the fees applicable to those services.
11. Definitions
Availability / Available: Access to the Appriss Retail Platform and applicable Module(s) through Company's provided user interface.
Business Hours: Monday through Friday, 9:00 AM to 5:00 PM Eastern Time, excluding US public holidays.
Exclusion Event: Any event described in Section 7 of this Schedule.
First Response: Occurs when an incident has been reported by Client and the Company technician assigned to the case commences efforts to diagnose the issue.
Incident: A technical problem in the accessibility or performance of the Appriss Retail Platform or Module(s) that is under Company's control. Incidents do not include problems caused by Exclusion Events.
Remediation: The state in which a reported Incident has been sufficiently addressed that Client is able to resume normal or near-normal business operations, whether through a hotfix, workaround, configuration change, or other interim measure. Remediation does not require full resolution of the underlying root cause.
Response Time: The time between Company's receipt of Client's notification of an incident and First Response.
Scheduled Maintenance: Planned maintenance windows, which shall not be scheduled between 6:00 AM and 9:00 PM Pacific Time.
Service Level Credit: A credit against Client's monthly fees as set forth in Table 1 of Section 3.
Support Portal: The Appriss Retail customer support portal, accessible at https://support.apprissretailcloud.com, through which all support requests must be submitted.
Uptime Availability: The percentage of time in a given calendar month during which the Platform and applicable Module(s) are Available, excluding Scheduled Maintenance and Exclusion Events.
12. Version History
Version
Effective Date
Notes
1.0
October 20, 2021
Initial release
1.1
December 6, 2021
Minor updates to service availability terms
1.2
January 14, 2022
Training and support schedule updates
2.0
[EFFECTIVE DATE]
Consolidated schedule; P1-P4 priority framework; escalation procedure; definitions added
Appriss Retail -- Confidential and Proprietary. This document is incorporated by reference into the applicable Master License and Services Agreement or Order Form.

## ANALISIS-TICKETS-2026-07-30
_chunk 1671 · 2026-07-30 · fuente: ANALISIS-TICKETS-2026-07-30.md_

# Análisis de mis tickets asignados — 30 jul 2026
Juan Martinez · L2 Support · RCS

---

## 0. Qué es "hacer triage" (respuesta directa)

En Appriss, **triage no es "resolver"**: es *clasificar y dejar el ticket apuntando al dueño correcto de la siguiente acción*. Es una operación de 6 chequeos que se hace en minutos, ticket por ticket:

| # | Chequeo | Qué corregir |
|---|---|---|
| 1 | **Tipo** | ¿Roto/con error → `Incident`. ¿Pregunta o cambio → `SOW`. El portal del cliente solo ofrece 2 opciones, así que casi siempre llega mal. |
| 2 | **Prioridad** | Critical = app caída para todos. High = un grupo/región no entra o bloquea el trabajo diario. Lo demás Medium. No subas Priority a mano por urgencia: publícalo en el canal Teams *Support Team Priority*. |
| 3 | **Status = dueño de la siguiente acción** | Es *la* regla. Si está en mis manos → `Work in Progress`. Si espero al cliente → `Under Customer Review` (**único status que pausa el SLA**). Si espero a un equipo interno → el `Under X Review` correspondiente. |
| 4 | **Labels / campos** | `Support_Data_Team` en tickets de datos Secure 5, `Team Ownership = Support Delivery`, `Sprint = RCS Support Team`, campo *Problem* fuera de "Other", empresa taggeada y prefijo en *Export to Power BI*. |
| 5 | **Duplicados / vínculos** | Cluster del mismo incidente → linkear, un solo investigador, el resto responde a sus clientes. |
| 6 | **Primer toque obligatorio** | Pasar a `Work in Progress` + enviar la canned response **"New Ticket Assignment First Response"**. Eso es el comentario de "tomo tu ticket" que estás preguntando. |

**Regla de esfuerzo:** lo que cuesta ≤4 h se queda en Support (bajará a 2 h). Más que eso, escala a L3 con el checklist obligatorio: entorno (Test/QA/Prod), repro paso a paso con screenshots, notas de troubleshooting con IA, y notas de conversaciones fuera del ticket.

---

## 1. El contexto que hay que tener en la cabeza

**Qué está pasando:** migración + unificación de la plataforma Incident (LPMS / NetTrack). Se está sacando a los clientes de los servidores legacy —`apps.lpguys.net/<slug>` y `<ABV>.apprissretailcloud.com`— hacia la **plataforma unificada `apps.apprissretail.com/<slug>`**.

**Escala (Incident Migration 2026.xlsx):**
- 143 clientes en 6 fases.
- Prod Data Migrated: **44 / 143 (31 %)**. Client Test Site Confirmation: solo 26 %.
- Comunicación al cliente enviada: 77 %. Firewall rules: 80 %.

**La ola que está doliendo:** los **19 clientes con Plan Prod Date = 7/27/2026** — que son exactamente la lista que circuló en el chat:

`3sixty · bigy · blains · caribou · chanel · christiandior · indianagrocery · mattressfirm · mcdonalds · prada · rackroom · santikos · skechers · smartandfinal · sportsmans · tahoedonner · vallarta · vitaminshoppe · vsm`

…**más `delhaize`, que cortó el 7/29** (slug `adusa`, ABV `DAI`, cliente 441, servidor 15, CSM **Shaun Callow**). Delhaize es el que tiene su propio chat de crisis ("Delhaize Platform Unification", 12 personas, Matt Kamminga liderando).

**El dato clave que cambia el análisis:** en el modelo legacy **cada cliente tenía su propio servidor** (delhaize = 15, bigy = 14, prada = 17…). En la plataforma unificada **los tenants comparten servidor** (delhaize, equinox, mattressfirm, tahoedonner y amf están todos en 15). Todo lo que antes se configuraba *a nivel de servidor por cliente* —zona horaria del OS, rutas de storage, endpoints de Izenda, jerarquías— ya no puede resolverse así. Esa es la raíz común de casi todo lo que está entrando.

**Quién es quién en el war-room de Delhaize:**
- **Matt Kamminga** — lidera, reparte y quiere cierres inmediatos.
- **J.R. Teagle** — trae gente de Support (Camila Cortes, Juan, Viraj).
- **Viraj Kansara** — está haciendo la comunicación al cliente en varios.
- **Jack Chen** — tomó el fix del blob/attachment (sanitizar la coma en el filename).
- **Kiran Vadday** — los de stores/location mapping (28023, 28043).
- **Scott Buric** — al que Matt le pasó **mi** RCS-28030 ("this looks like a datetime conversion issue").
- **Chris Rippingale** (UK) y **Vedant Shirude** (India) — reproduciendo.
- **Sofia Sandner** — mensajería al cliente.
- **Leigh Ann Stubbs** (ADUSA, Salisbury NC, EDT) — la reportera de los 8 tickets de Delhaize.

---

## 2. Mis 13 tickets abiertos

### Los 5 que son de la migración (bloque prioritario)

| Ticket | Cliente | Título | Status hoy | Prio |
|---|---|---|---|---|
| **RCS-28033** | Big Y | LPMS Login Issue | Under Customer Review | **High** |
| **RCS-28030** | ADUSA | Server time needs adjusted to EST | Work in progress | Medium |
| **RCS-28023** | ADUSA | Unable to create cases when restricted by Division | Under Support Review | Medium |
| **RCS-28021** | ADUSA | Unable to use Izenda | Under Support Review | Medium |
| **RCS-28032** | Vitamin Shoppe | Access Issues | Under Customer Review | Medium |

### Los 8 de backlog normal

| Ticket | Cliente | Título | Status | Prio | Edad |
|---|---|---|---|---|---|
| **RCS-27991** | — | Engage Analytics Not Populating Sections | Under Support Review | **High** | 3 d |
| RCS-28001 | SEA | Engage API IP Allow List | Under Security Review | Medium | 2 d |
| RCS-27959 | PacSun | IP Whitelisting MuleSoft | Work in progress | Medium | 7 d |
| RCS-27941 | Tailored Brands | SSO/Permissions en Incident | Work in progress | Medium | 8 d |
| RCS-27840 | Kohl's | Workday Security Updates (deadline **1 ago**) | Under Security Review | Medium | 15 d |
| RCS-27765 | Winn-Dixie | Data file check | Under Customer Review | Medium | 20 d |
| RCS-27676 | RLC | SFTP IP/Hostname Change | Under Customer Review | Low | 24 d |
| RCS-27573 | Tahoe Donner | Persistent Error Entering Incident Reports | Work in progress | Medium | 34 d |

### Errores de triage en mi propia cola (corregir hoy)

1. **RCS-28023 y RCS-28021 están en `Under Support Review` pero asignados a mí.** Contradice la regla del status: si están en mis manos van a `Work in Progress`; si los estoy pasando a otro equipo, van al `Under X Review` correcto. Ahora mismo son invisibles: nadie sabe que tienen dueño.
2. **RCS-27991 es High, tiene 3 días y sigue en `Under Support Review`.** Riesgo de SLA real y no está en ningún war-room que lo tape.
3. **RCS-27573 (Tahoe Donner) tiene 34 días.** A 60 días entra en Tiger Team. Y Tahoe Donner *también* está en la ola del 7/27 → vale la pena revisar si el error persistente es post-migración.

---

## 3. Análisis técnico por ticket

### RCS-28030 — "Server time needs adjusted to EST" (el mío, con evidencia nueva)

**Lo que tengo confirmado con los screenshots que mandó Leigh Ann esta mañana:**

| Momento | Reloj de ella (EDT) | Lo que muestra la app | Delta |
|---|---|---|---|
| Journal Date (default del Edit Form) | 8:29 AM | 7/30/2026 **12:28 PM** | +4 h = **UTC exacto** |
| Attachments → Upload Date | 8:32 AM | 7/30/2026 **12:32 PM** | +4 h = **UTC exacto** |

**Lo que añade la reproducción interna (~9:24–9:25 a.m. COT = 14:24–14:25 UTC):**

- Chris Rippingale (UK) abrió el Edit Form → Journal Date **3:24 PM**.
- Vedant Shirude (India, reloj de su máquina 19:55 IST) → Journal Date **3:25 PM**.
- Los dos, en husos totalmente distintos, vieron **15:2x = UTC+1 = BST**.

**Dos conclusiones duras:**

1. **El timestamp no viene del navegador, viene del servidor.** Si viniera del cliente, Vedant habría visto 19:55 y Chris 15:24. Vieron lo mismo. Chris lo interpretó bien: *"Correct for British Summer Time"*.
2. **Las dos lecturas no coinciden (UTC para ella a las 8:30, UTC+1 para nosotros a las 9:25).** O alguien tocó la zona del servidor entre esas dos horas, o son dos caminos distintos: `Upload Date` se guarda/renderiza en UTC y el default de `Journal Date` sale de la hora local del OS del app server. **Hay que confirmarlo con Infra antes de prometer nada.**

**Los dos puntos que nadie ha dicho todavía en el chat y que valen el ticket:**

- **"EST" es una trampa.** Hoy, 30 de julio, la costa este está en **EDT (UTC−4)**, no EST (UTC−5). Si esto se arregla clavando un offset fijo de −5, queda bien en enero y mal ahora — o al revés. El fix tiene que ser **`America/New_York` con DST**, no un offset.
- **Cambiar la zona del OS del servidor ya no es una opción.** ADUSA comparte el servidor 15 con equinox, mattressfirm, tahoedonner y amf; y la plataforma unificada aloja tenants de UK, EU, CA y AU. Mover el OS a Eastern rompe a todos los demás. Es decir: **esto no es "ajustar el reloj del servidor", es una brecha de arquitectura de la unificación** — guardar en UTC y renderizar por zona del tenant/usuario. Eso explica el comentario de Matt ("I'm kind of surprised something like this still exists") y significa que **el mismo bug está latente en los otros 43 tenants ya migrados**, no solo en ADUSA.

**Destino:** no es Infrastructure (no hay reloj que ajustar). Es **Engineering** — conversión datetime por tenant. Scott Buric ya está mirándolo por pedido de Matt, así que primero le paso la evidencia y coordinamos, no lo transiciono a ciegas.

### RCS-28023 — Cases restringidos por Division

Jerarquía de compañía/stores mal migrada. Ejemplo concreto: la usuaria **Rebecca Ries** pertenece a **Food Lion**, el store **2204** es Food Lion, pero buscando bajo la marca **Ahold Delhaize USA Services** no devuelve nada → los usuarios quedan restringidos a una división que no corresponde a sus stores. Bloquea a AP Level 1, 2 y Level 2 leads: **no pueden crear casos**. Eso es "bloquea el trabajo diario del cliente" → **justifica High, hoy está en Medium**.

Es problema de **datos/configuración en producción**, no de código → **Delivery** (`Under Delivery Review`, para Incident el dueño es **Ryan Barlow** + mensaje de Teams obligatorio). Matt ya se lo pidió a **Kiran Vadday** en el chat, y RCS-28043 (assignee Kiran) es el hermano de este ("another one linked to stores"). **Linkear 28023 ↔ 28043.** Ya tiene el label `Support_Data_Team`, correcto.

### RCS-28021 — Izenda

No es "no puedo entrar": ella **sí** entra. El fallo es al **guardar** un cambio en el reporte *Future Stores to Review* (carpeta *Jim Cosseboom Test*): mueve la columna Store Open date, pulsa Save y cae a **página en blanco, sin mensaje de error**. URL: `https://apps.apprissretail.com/adusa/nettrack/adhoc/LPSLogin.aspx`. Reportado también en Teams → Retail Ops → canal *AALPS Issues*.

Página blanca al hacer POST = excepción no manejada del lado servidor. Lo más probable es que **Izenda no quedó repuntado a la URL nueva** (callback/base URL del designer sigue apuntando al host legacy). Es config de migración. Matt se lo asignó a **Jack Chen** en el chat. Yo aporto la repro exacta y **pido los logs del servidor en el momento del save** — sin eso Engineering no puede hacer nada.

### RCS-28033 (Big Y) + RCS-28032 (Vitamin Shoppe) — el patrón que se está pasando por alto

Los dos son de la **misma ola del 7/27**. Los dos reportan **literalmente el mismo síntoma**:

- Big Y (Kevin Snyder): *"It prompted us to change our login credentials and then crashed"*.
- Vitamin Shoppe (Brandon Bigelow): *"I was able to login and it prompted me to update my password but upon changing my password I am now receiving the below message"*.

Y en el chat de Delhaize aparece **la tercera instancia del mismo tipo de fallo de login**, con stack trace:

```
System.Exception: Failed to create or update sso user.
 ---> Failed to get groups for sso user with the username:
 ---> Procedure or function 'GetSSOPermissionGroupsByUserName'
      expects parameter '@userName', which was not supplied
```

Es decir: el username no llega al SP → el usuario no se puede mapear → crash. Matt lo confirmó para RCS-28042: *"with SSO its set up to use GlobalID as the username. That's not coming across for this user so we can't map"*.

**Consecuencia:** a Big Y se le respondió que *"the error is originating from the Big Y side"* y se le mandó a hablar con su IT. Su IT metió la excepción en el web filter y **volvió a fallar**, y ellos mismos dijeron que el segundo error parece ser del vendor. Con dos tenants distintos de la misma ola dando el mismo síntoma, **el diagnóstico "es de tu lado" no se sostiene**. Hay que corregirlo antes de que se convierta en un problema de credibilidad — es un cliente High esperando desde ayer.

**Acción:** tratar 28033 + 28032 como un cluster de post-migración (flujo de reset/actualización de password + mapeo de usuario en el tenant unificado), linkearlos, y llevarlo al mismo canal donde ya se está trabajando el de SSO de Delhaize. Sigo necesitando de Big Y el **Cloudflare Ray ID** y la confirmación de si entran por `apps.apprissretail.com` a secas o por `apps.apprissretail.com/bigy/signin` (entrar sin el slug del tenant es, por sí solo, causa de fallo).

---

## 4. Orden de ataque — paso a paso

### Bloque A — hoy, antes de mediodía (60–75 min)

**A1. RCS-28030 — cerrar el análisis y entregarlo (20 min).** Es el único donde tengo evidencia completa y donde el cliente ya respondió lo que pedí. Además Leigh Ann dejó una queja explícita: *"This is the only ticket that I have received any feedback/request for info"* — o sea, mi ticket es el único bien atendido de los 8 suyos. Hay que capitalizarlo, no perderlo.
1. Comentario interno con la tabla de evidencia (los 4 datapoints: ella +4 h = UTC; Chris y Vedant = UTC+1 desde husos distintos).
2. Mensaje de Teams a **Scott Buric** en el chat de Delhaize con los dos puntos: EST≠EDT y "el OS del servidor compartido no puede ser Eastern".
3. Preguntar a Infra: ¿qué zona tiene el OS del server 15 nuevo vs el legacy de ADUSA? ¿cambió alguien algo entre 8:30 y 9:25 EDT hoy?
4. Respuesta al cliente (borrador abajo) y dejarlo en `Work in Progress`.

**A2. RCS-28023 — subir prioridad y rutear (15 min).** Priority → **High** (bloquea creación de casos a tres niveles de AP). Comentario interno con el ejemplo Rebecca Ries / store 2204 / marca ADUSA Services. Linkear con **RCS-28043**. Status → `Under Delivery Review`, **Ryan Barlow** + mensaje de Teams. Mantener `Support_Data_Team`. Confirmar con Kiran en el chat para no duplicar trabajo con RCS-28043.

**A3. RCS-28021 — sacarlo de `Under Support Review` (10 min).** Comentario interno con la repro exacta (carpeta, reporte, acción, URL) + pedir logs del app server en la ventana del save. Coordinar con **Jack Chen** (ya lo tomó por pedido de Matt) y mover el status a donde de verdad está: `Under Engineering Review` si Jack va por código, o `Under Delivery Review` si es repointing de config. **No dejarlo en Under Support Review.**

**A4. RCS-28033 — corregir el diagnóstico (20 min).** Es mi único **High** con cliente esperando. Comentario interno linkeando **RCS-28032** y señalando el patrón de los 3 casos (Big Y, Vitamin Shoppe, el SSO de Delhaize). Responder a Kevin: retirar el "es de su lado", pedir Ray ID + confirmación de URL con slug, y decir que ya se está investigando como tema de la plataforma. Que sea `Under Customer Review` **solo** después de pedir el dato concreto.

### Bloque B — hoy por la tarde (45 min)

**B1. RCS-28032** — linkear a 28033, y como ya respondí ayer pidiendo confirmación a Joe Austin, hacer follow-up con el contexto nuevo (deja de ser "no reproducimos" y pasa a "es un patrón conocido de la migración"). Ojo: Brandon Bigelow **no existe en el portal**, la comunicación va por Joe Austin.

**B2. RCS-27991 (High, 3 días, sin dueño visible)** — el que se está cayendo por el hueco mientras todo el foco está en Delhaize. Sacarlo de `Under Support Review` → `Work in Progress` + primer toque al cliente. Si en 30 min de análisis no hay causa, escalar: Engage Engineering = **Ian Williams** + mensaje de Teams obligatorio (no ve la asignación sola).

**B3. RCS-27840 (Kohl's, deadline 1 de agosto = pasado mañana)** — está en `Under Security Review` así que la acción es de InfoSec, pero **yo sigo asignado y yo comunico y cierro**. Un ping a Security hoy, no el lunes.

### Bloque C — mañana / cuando baje la marea

- **RCS-27573 (Tahoe Donner, 34 días)** — Tahoe Donner está en la ola del 7/27. Revisar si el error persistente es en realidad post-migración; si sí, se une al cluster. Y sea como sea, a 60 días entra a Tiger Team.
- **RCS-28001, RCS-27959** — IP allow-list / whitelisting. Mecánicos, van juntos.
- **RCS-27941 (Tailored Brands, SSO/permisos)** — mismo dominio que el patrón `GetSSOPermissionGroupsByUserName`. Vale la pena mirarlo con esa lente.
- **RCS-27765, RCS-27676** — en `Under Customer Review`, SLA pausado. Aplicar la rutina Tiger Team: si ya dimos la info, avisar con canned response y dar un plazo de cierre.

### Regla de foco

Nunca más de una cosa a la vez en el war-room. Cuando Matt te nombra en el chat, la respuesta correcta es la de Viraj: una línea confirmando qué vas a hacer y cuándo vuelves. Eso es lo que él está midiendo.

---

## 5. Borradores de comentarios

### Plantilla base — "New Ticket Assignment First Response"

> Hello [Nombre],
>
> I have taken ownership of this ticket and will be investigating it for you. Please allow some time for me to research the issue and I will get back with you just as soon as I have any information.
>
> Kind regards,
> Juan Martinez
> Support Engineer

Va **siempre** acompañada del cambio de status a `Work in Progress`. Es el primer toque obligatorio.

### RCS-28030 — respuesta al cliente (Leigh Ann)

> Hi Leigh Ann,
>
> Thank you for the screenshots — they were exactly what we needed and they confirm the problem.
>
> Your Journal Date showed 12:28 PM while your local time was 8:29 AM, and the attachment Upload Date showed 12:32 PM at 8:32 AM local. That is a consistent 4-hour offset, which means the platform is rendering timestamps in UTC rather than converting them to your local Eastern time. We also reproduced it internally from two different time zones and both saw the same server-side value, which confirms this is coming from our side and not from your browser or workstation.
>
> This is now with our engineering team as a datetime conversion issue on the new platform. One note so we set the right expectation: the fix needs to follow Eastern time with daylight saving (currently EDT, UTC-4), not a fixed offset, so we want to correct it properly rather than shift the clock.
>
> I will keep this ticket updated as soon as I have a timeline from engineering. Thank you for the detail you provided — it moved this forward significantly.
>
> Kind regards,
> Juan Martinez
> Support Engineer

### RCS-28030 — comentario interno

> **Evidence summary — timestamps are rendering server-side, not client-side.**
>
> | Source | Local time | Displayed | Delta |
> |---|---|---|---|
> | Customer, Journal Date default | 08:29 EDT | 12:28 PM | +4h (UTC) |
> | Customer, attachment Upload Date | 08:32 EDT | 12:32 PM | +4h (UTC) |
> | Chris Rippingale (UK), Journal Date | ~14:24 UTC | 3:24 PM | +1h (BST) |
> | Vedant Shirude (India, clock 19:55 IST), Journal Date | ~14:25 UTC | 3:25 PM | +1h (BST) |
>
> Two viewers in different time zones saw the same value → the timestamp originates on the app server, not in the browser.
>
> The customer's readings (UTC) and ours (UTC+1) do not match. Either the server timezone was changed between 08:30 and 09:25 EDT today, or the two fields resolve differently (stored UTC for Upload Date vs server OS local time for the Journal Date default). **Needs confirmation from Infrastructure: what is the OS timezone on the new server 15 vs the legacy ADUSA server, and was anything changed this morning?**
>
> Two constraints on the fix:
> 1. The customer says "EST" but Eastern is currently **EDT (UTC-4)**. A fixed -5 offset will be wrong half the year. It must be DST-aware `America/New_York`.
> 2. **Changing the server OS timezone is not viable.** ADUSA shares server 15 with equinox, mattressfirm, tahoedonner and amf, and the unified platform hosts UK/EU/CA/AU tenants. Per-server timezone worked in the legacy one-server-per-client model; it cannot work post-unification. This needs store-in-UTC / render-per-tenant-timezone.
>
> Implication: this is likely latent for the other migrated tenants, not specific to ADUSA. Coordinating with Scott Buric per Matt's request in the Delhaize Platform Unification chat.

### RCS-28023 — comentario interno

> Raising to High: this blocks case creation for AP Level 1, Level 2 and Level 2 leads — it stops the customer's daily work.
>
> The company/store hierarchy did not migrate correctly. Concrete example from the customer: user **Rebecca Ries** belongs to **Food Lion** and store **2204** is a Food Lion store, but searching under the **Ahold Delhaize USA Services** brand returns no results. Users are restricted to a division that does not match their assigned stores.
>
> This is a production data/configuration issue rather than a code defect → routing to Delivery. Related to **RCS-28043** (store locations duplicated across brands, assigned to Kiran Vadday) — linking both so they travel together. Kiran, flagging so we don't duplicate the investigation.
>
> Label `Support_Data_Team` retained.

### RCS-28021 — comentario interno

> Correcting the framing: the customer **can** log in to Izenda. The failure is on **save**.
>
> Exact repro from the customer: folder *Jim Cosseboom Test* → report *Future Stores to Review* → move the Store Open date column beside the store number → click Save → redirected to a **blank page with no error message**, cannot proceed.
> URL: `https://apps.apprissretail.com/adusa/nettrack/adhoc/LPSLogin.aspx`
> Also reported in Teams → Retail Ops → *AALPS Issues*.
>
> A blank page on POST points to an unhandled server-side exception. Working hypothesis: Izenda was not repointed to the new URL after the migration (designer callback/base URL still resolving to the legacy host).
>
> **Need: app server logs for the save request window.** Without them there is nothing for engineering to work from.
>
> Jack Chen picked this up in the Delhaize Platform Unification chat — coordinating there. Moving the status off Under Support Review so ownership of the next action is visible.

### RCS-28033 — respuesta al cliente (Kevin, Big Y)

> Hello Kevin,
>
> Thank you for working with your IT team on this, and apologies for the earlier direction — based on what your team found, and on what we are now seeing across other accounts, we do believe this needs to be investigated on our side.
>
> Big Y was migrated to our unified platform on July 27, and we are seeing similar password-update failures on other recently migrated accounts. We are treating this as a platform issue rather than something local to Big Y.
>
> To pin down the exact failure, could you please send us:
> 1. The **Cloudflare Ray ID** from the error page (the screenshot was cut off before that value).
> 2. Confirmation of the exact URL being used — `apps.apprissretail.com` on its own, or `apps.apprissretail.com/bigy/signin`? The account-specific path matters after the migration.
>
> As soon as we have those I will update you with what we find.
>
> Kind regards,
> Juan Martinez
> Support Engineer

### RCS-28033 — comentario interno

> Linking **RCS-28032** (Vitamin Shoppe). Same wave, same symptom.
>
> - Big Y (prod cutover 7/27/2026): *"It prompted us to change our login credentials and then crashed."*
> - Vitamin Shoppe (prod cutover 7/27/2026): *"I was able to login and it prompted me to update my password but upon changing my password I am now receiving the below message."*
> - Third instance, Delhaize (RCS-28042), with a stack trace: `Failed to create or update sso user → Failed to get groups for sso user with the username → Procedure or function 'GetSSOPermissionGroupsByUserName' expects parameter '@userName', which was not supplied`. Matt Kamminga confirmed SSO is configured to use GlobalID as the username and it is not coming across, so the user cannot be mapped.
>
> Three tenants from the same migration wave failing on the user-mapping / password-update path is a platform pattern, not a customer-side issue. Retracting the earlier "error originating from the Big Y side" assessment — their IT added the site as a web filter exception and hit a second error, which they correctly identified as vendor-side.
>
> Still needed from the customer: Cloudflare Ray ID and confirmation of whether they are hitting the tenant-scoped URL (`/bigy/signin`) or the bare host.

---

## 6. Preguntas abiertas que hay que resolver con alguien

1. **Infra:** ¿zona horaria del OS en el server 15 nuevo vs el legacy de ADUSA? ¿Se tocó algo entre 8:30 y 9:25 EDT del 30/07?
2. **Engineering/Producto:** ¿cómo renderiza la plataforma unificada las fechas por tenant? Si es por OS del servidor, es un defecto de diseño que afecta a los 44 tenants migrados.
3. **Delivery:** ¿la jerarquía de compañía/stores se migró con un script? Si sí, los otros 19 tenants del 7/27 tienen el mismo riesgo que ADUSA en 28023.
4. **Matt / Colleen Knoblock:** ¿se validó el flujo de cambio de password en la ola del 7/27 antes del cutover? Big Y y Vitamin Shoppe fallan igual.
5. **Yo mismo:** ¿RCS-27573 (Tahoe Donner, 34 días) es en realidad post-migración? Tahoe Donner está en la ola del 7/27.

## plan-2026-08-12
_chunk 1672 · 2026-08-12 · fuente: plan-2026-08-12.md_

# Plan de acción, 12 de agosto de 2026

## 1. RCS-27973, GAP, órdenes canceladas visibles en Identify

**Dónde está.** Incident, Medium, Work in progress, asignado a Bikash Kumar, reportado por Sridhar (sridhar_mediga@gap.com) el 24 de julio. Product Type es Engage In-Store Return Authorization (Verify), que enruta a Yellow Team, Kenny Vu e Ian Williams. Label `Support_Data_Team`.

**Causa raíz, ya sustentada.** `ARDM_10_Header.sql` línea 82 fija `voidticketflg = 0` para todo ECOM. El CASE de `ord_typ` solo tiene SALES, RETURN, REFUND y EXCHANGE, así que las canceladas caen al `ELSE 99`. Bikash lo verificó contra base: 356M de transacciones ECOM y ninguna con `voidticketflg = 1`. Las 6 órdenes reportadas están en `ardm_049.ardm_header` con `voidticketflg = 0` y `netsalesamount = 0.00`. Chris Howard confirmó del lado del mapeo que nunca existió la rama CANCELLED.

**Lo que falta y no depende de nosotros.** Qué campo manda GAP en el feed NGCC para marcar cancelación. `netsalesamount = 0.00` y cantidad 0 no alcanzan como base para el arreglo, Chris fue explícito en eso. Bikash ya le hizo la pregunta a Sridhar en el ticket el 12 a las 6:48 am.

**Qué hago.**

1. Mandar el mensaje a Bikash preguntando por el dueño del cambio en el loader antes de agendar nada. Kenny Vu etiquetó a Bryant McAnnally el 11 de agosto, puede que ya haya dueño.
2. Si aparece dueño, la llamada se agenda con él presente. Si no aparece, preguntarlo en la llamada con Peyman, que es la autoridad de ARDM y `c049gap` es cliente 049.
3. Agendar con Sridhar, 9 a 11 am PST, que es 11 am a 1 pm Colombia.
4. Pedir muestra de archivo crudo de P-INGEST para una de las 6 órdenes. Con eso podemos responder la pregunta del campo sin depender de que Sridhar la conteste.

**Lo que NO hago.** No prometo ETA en la llamada. El arreglo son dos cosas separadas, cambio de código en el loader más backfill de las 6 órdenes ya cargadas, y ninguna de las dos es nuestra.

---

## 2. RCS-28283, TG Jones, opción de tienda duplicada en SSO+

**Dónde está.** Incident, Medium, **Under Support Review**, asignado a Nikita Rathore, reportado por Brett Betton (brett.betton@tgj.co.uk) el 14 de julio. Vino de hypercare el 11 de agosto vía Ruchi Vora. Product Type Secure 5 EBR. Label `clientproject`.

**El hallazgo.** Nikita cree que ya escaló porque lo posteó en un canal. No escaló. No hay ENG vinculado, `issuelinks` está vacío, y el ticket sigue en Under Support Review. Además el cliente lleva 29 días con nada más que el auto-reply.

**Procedimiento verificado.** Fuente: "Escalating Tickets to L3 Departments", Aimee Wadsworth, Confluence RTS página 478006902856, enlazada desde "L2 Support Team Ticket Triage" (477650845697).

Para **Secure e Incident Engineering**: estado a Under Engineering Review y **asignar a Shandana Khan**. El ENG se auto-crea con esa transición y los comentarios sincronizan en ambos sentidos. No se crea a mano.

Quedarse uno como assignee aplica solo a **Infrastructure** (Under Infrastructure Review, auto-crea RTAILIT) y **Security** (Under Security Review, auto-crea INFOSEC).

Si resulta ser configuración y no código, la ruta es Delivery: Secure 5 va a Under Delivery Review con **Peyman Motlagh** y "RCS Support Team" en el Sprint. Incident va a Ryan Barlow más mensaje de Teams. Engage Engineering va a Ian Williams más mensaje de Teams.

**Requisito previo antes de escalar**, según el mismo doc, y RCS-28283 no cumple ninguno salvo la captura del cliente:

- Entorno donde ocurre (Test, QA o Prod)
- Pasos completos de reproducción con capturas
- Las notas de IA usadas en el troubleshooting
- Conversaciones con otros ingenieros fuera del ticket
- Comunicación al cliente avisando que el ticket se mueve

**Qué le pido a Nikita, en este orden.**

1. Reproducir y documentar. Sin eso el ENG se devuelve.
2. Comentario a Brett. 29 días con solo el auto-reply es lo más urgente del ticket, más que el bug.
3. Under Engineering Review y asignar a Shandana Khan. El ENG sale solo.

**Duda abierta sobre el ruteo.** Product Type dice Secure 5 EBR. La descripción etiqueta a Carl Costelow, que en la matriz de onboarding es Delivery para Secure Store. La regla es código o bug a Engineering, dato o configuración ya en producción a Delivery. La descripción dice bug de aplicación, así que Engineering es lo razonable, pero eso lo decide la reproducción, no la descripción.

---

## Orden del día

1. Llamada con Peyman. Sigue siendo lo primero, no ha ocurrido. Correr la línea 1 de `1.sql` antes de marcar.
2. Mandar los dos mensajes de Teams, Bikash y Nikita.
3. Seguir con la cola del 11: RCS-28153 Big Y (timeout 240), RCS-28032 Vitamin Shoppe (a Brandon Bigelow), RCS-28123 a Under Customer Review, RCS-27978 Myer a cerrar en dos pasos, RCS-28055 Gen Parts, RCS-28152 a Manisha.

## Proceso RCA: Shorthand vs Report, SLA, OUTM, skills Claude, precedentes RCS-20226/27009
_chunk 1673 · 2026-08-18 · fuente: terminal_

# Guía: cómo armar un RCA para un cliente (Appriss)

Consolidado el 18 ago 2026, verificado contra Confluence, Jira y el disco. Referencia
permanente, no se borra al cerrar el caso de Stater Bros.

## 1. Los dos documentos, nunca uno solo

| | Shorthand RCA | RCA Report |
|---|---|---|
| Qué es | 2-3 frases: qué pasó, impacto, causa si se conoce, resolución corto/largo plazo | Documento completo aparte |
| Dónde va | Pegado directo en el ticket o por correo | PDF adjunto |
| SLA (Critical/High) | 1 día desde la **resolución** | 10 días desde la **resolución** |
| SLA (Medium/Low) | 10 días desde la resolución | (no aplica / mismo shorthand) |
| Plantilla Confluence | RCA Ticket Template (474654900291) | RCA Report Template (474654965776) |

**El reloj corre desde que el incidente se resuelve, no desde que el cliente lo pide.**
Si el outage sigue activo, lo único que corresponde entregar es el Shorthand, y hay que
decírselo al cliente con esa razón, no quedarse callado.

## 2. Antes del RCA: el ticket OUTM

El "Outage Ticket Process" (Confluence RTS 478022696993) dice que todo outage genera un
ticket en el proyecto **OUTM** con: Description, Environment, RCS tickets vinculados,
Timeline (start/end), Classification (Issue Level, Availability %, Impact, Urgency),
Scope, Root Cause, Alerting. Ese ticket es la fuente del Timeline que después pide el
RCA Report. **Si no existe, hay que crearlo o pedir que se cree antes de escribir el RCA
a mano** — sin él, el Timeline se arma de memoria y eso es lo que después no cuadra.

## 3. Plantilla del RCA Report (RSI 474654965776)

```
<Título>
Date: <fecha del incidente>
Author: <autor>

Introducción / Summary
<resumen del incidente y el impacto>

Incident Details
  Timeline: tabla Date | Time (UTC) | Description
  Impact: sitios afectados, volumen de requests, ventana de tiempo
  Root Cause: descripción
  Resolution: cómo se resolvió
  Recurrence Preventative Measures: qué se hace para que no vuelva a pasar
```

## 4. Quién lo escribe (RSI 474840268801)

Cualquiera que estuvo involucrado, aunque sea de paso, tiene la responsabilidad de que
el RCA arranque. Una vez arrancado, la info clave se comparte con el Delivery Manager y
el Senior Implementation Consultant, que arman el documento final para el cliente.
Usar el comentario interno del ticket para todo lo sensible mientras se investiga.

## 5. Los tres Claude Skills que ya existen para esto

Documentados por Dean Korbakis, **ninguno instalado todavía en esta máquina**. Se instalan
desde Claude Code → Settings → Skills → Install from file. Los archivos `.skill` están
adjuntos a sus páginas de Confluence.

| Skill | Página | Qué hace |
|---|---|---|
| `appriss-rca-generator` (de Avi) | RTS 477550018564 | PDF interno con branding, base de los otros dos |
| `appriss-rca-generator-retro` | RTS 477856825345 | Antes del final: worksheet pre-llenado desde el ticket de Jira. Marca en verde lo que ya se sabe, deja en blanco lo que necesita respuesta de ingeniería (5-Whys, Root Cause, Business Impact) |
| `appriss-rca-generator-external` | RTS 477584359429 | Convierte eso en el PDF para el cliente: sin nombres, sin tickets de Jira, sin jerga interna, 13 secciones fijas, cadena de 5-Whys en lenguaje plano |

**Orden correcto: retro primero, external después.** El retro te dice con precisión qué
falta por preguntar; sin eso se termina preguntando cosas que ya estaban en el ticket.

Reglas duras de la versión externa (RTS 477584359429): nunca nombres de personas propias,
dueños de action items siempre por rol ("Appriss Retail Engineering Team", nunca "John
Smith"); nunca números de ticket Jira internos; nunca "Internal Use Only"; si la causa no
está confirmada, escribir "Under investigation", no especular; ante la duda, se deja por
fuera. Nombre de archivo: `RCA<YYYYMMDD>-<Cliente>-<TemaCamelCase>-External.pdf`.

## 6. Los dos precedentes reales, comparados

**RCS-20226 (marzo 2025, Secure EBR).** Informal: se prometió el PDF, se adjuntó una
semana después sin rastro de proceso en el ticket. Sirve solo para confirmar el
mecanismo de entrega (adjunto + "Support Resolved - Provided Requested Information"),
no como ejemplo de comportamiento.

**RCS-27009 (mayo-junio 2026, Sainsbury's, Dean Korbakis — mismo puesto que Juan).**
Este es el molde de comportamiento a seguir:
1. La causa técnica se investiga y confirma primero en Teams por quien la vivió, antes
   de prometerle nada al cliente.
2. Se anuncia una llamada interna con los ingenieros involucrados antes de escribir nada.
3. Si esa llamada no basta (gente de vacaciones), se avisa el retraso con la razón real,
   no en silencio.
4. El RCA solo se publica cuando la causa está confirmada por quien la investigó.
5. Ante una pregunta directa del cliente sobre responsabilidad, la respuesta es corta y
   honesta, sin sobre-explicar.

## 7. Checklist de arranque, en orden

1. Confirmar si el incidente está realmente resuelto. Si no, escribir solo el Shorthand
   y decir por qué el Report todavía no corresponde.
2. Verificar o pedir que se cree el ticket OUTM.
3. Reunir toda la evidencia ya disponible en Jira/Teams (esto lo hace Claude, no hay que
   pedirle a otra persona que la reúna si ya está escrita en un ticket o comentario).
4. Instalar los tres skills si no están instalados.
5. Correr `appriss-rca-generator-retro` con el ticket RCS/RTS correspondiente. Revisar
   qué quedó en verde (ya resuelto) y qué quedó en blanco (de verdad falta).
6. Conseguir solo lo que de verdad falta, directamente de quien lo sepa, con una pregunta
   concreta, no un pedido genérico de "reúne información".
7. Correr `appriss-rca-generator-external` para el PDF final.
8. Publicar como adjunto en el ticket, comentario "Provided RCA", esperar confirmación
   del cliente antes de cerrar. Cerrar es dos pasos: Resolve → Completed, después Close.

Ver también `2026-08-18-brief-reunion-adusa.md` para el caso Stater Bros específico que
disparó esta guía, y las memorias `project_rcs_...` relacionadas con RCS-28431/28058.

## Regla de Shandana: no comentar al cliente antes de Under Support Review — RCS-28161, 20 ago 2026
_chunk 1694 · 2026-08-20 · fuente: inbox/2026-08-20-rcs-28161-aclaracion-shandana.md_

# RCS-28161, aclaración de Shandana Khan, 20 ago 2026

## El ticket

Delhaize, Stores.csv no exportaba desde Manage Stores. Bug de plataforma, no de Izenda.
Confirmado por Matt Kamminga el 19 ago a las 16:31. Fix desplegado a producción hoy 20 ago
a las 09:55, confirmado por Matt y por Viraj.

## Lo que pasó

El 19 ago a las 19:37 Juan comentó directo a la clienta (Leigh Ann Stubbs) confirmando que
ingeniería estaba terminando el fix. En ese momento el ticket seguía asignado a Shandana Khan,
con estado Waiting for Software Release, sin transicionar a Under Support Review.

## La aclaración de Shandana, 20 ago 04:51

Cita textual: "our usual process is for Engineering to internally comment, and update from
Accepted into Development → Under Support Review for Support to communicate/confirm with the
Customer once a given fix is in Prod. Leaving this assigned to me with a status of Waiting for
Software Release has confused this. I'll assign to you to manage comms once the fix is in Prod."

## Qué hizo mal Juan

Juan comunicó al cliente el estado del fix de ingeniería antes de que el ticket transicionara
a Under Support Review. Ese paso marca el traspaso formal de Engineering a Support y evita que
dos personas comuniquen el mismo estado desde dos roles distintos. Comentar mientras el ticket
seguía asignado a Shandana con status Waiting for Software Release generó la confusión que ella
señaló.

## Regla para aplicar

Antes de comentarle a un cliente sobre un fix en desarrollo, verificar el status del ticket.
Si sigue en Accepted into Development o Waiting for Software Release y el assignee es de
Engineering, esperar el comentario interno de Engineering y la transición a Under Support Review.
Comentar recién ahí. Se puede escalar o preguntar por el avance sin ser assignee, pero la
comunicación con el cliente sobre el estado del fix es del que tiene el ticket en Under Support
Review.

Relacionado: reference_escalacion_l3_procedimiento (Secure/Incident Engineering, assignee
Shandana Khan, Under Engineering Review).

## Verificación de la transición Work in progress a Under Customer Review — 18 ago 2026
_chunk 1695 · 2026-08-18 · fuente: inbox/2026-08-18-transicion-under-customer-review.md_

# Verificacion de transicion Jira: Work in progress -> Under Customer Review
18 ago 2026

## Pregunta
Los 4 tickets marcados "Resolved" en el tracker pero con status Jira "Work in progress"
(RCS-28177, RCS-28364, RCS-28365, RCS-28415): se pueden mover a "Under Customer Review"
en vez de dejarlos quietos o cerrarlos directo?

## Verificacion (solo lectura, getTransitionsForJiraIssue)
Se consulto el listado de transiciones disponibles para los 4 tickets. Los 4 comparten el
mismo workflow y los 4 tienen la transicion "Under Customer Review" (id 571) disponible:
isAvailable: true, isConditional: false, hasScreen: false (no pide campos obligatorios).

Confirmado en: RCS-28177, RCS-28364, RCS-28365, RCS-28415.

## Recomendacion
Si, moverlos a Under Customer Review es correcto y mejor que mi sugerencia inicial de
esperar sin tocar nada. Esa transicion no afirma que el cliente confirmo por escrito
(eso seria Completed/Closed), solo dice "Appriss ya hizo su parte, esperando que el
cliente lo verifique", que es exactamente el estado real segun la llamada de hoy.

## Como hacerlo (Juan lo ejecuta manualmente, Claude no transiciona ni comenta)
Transicion a usar: "Under Customer Review" (id 571), en cada uno de los 4 tickets.
No pide campos obligatorios (hasScreen: false), asi que es solo click y confirmar.

Comentario sugerido para pegar al transicionar (en ingles, mismo texto para los 4,
ajustando el ticket si se quiere mencionar el contexto puntual):

> Appriss considers this resolved based on today's call. Moving to Under Customer Review
> pending written confirmation from ADUSA.

## Nota aparte (ya senalada en el informe de verificacion del 18 ago)
El borrador de correo a Jim lista como "cuatro para cerrar" a RCS-28177, RCS-28364,
RCS-28378 y RCS-28415, pero RCS-28378 ya tiene status distinto de Work in progress
(no es parte de este grupo de 4), mientras que RCS-28365 si lo es y no aparece en esa
lista del correo. Vale la pena revisar esa lista antes de enviar.

## ENG-6492. Reunión con Kiran, 28 ago 2026. Qué puede absorber soporte — 2026-08-28
_chunk 1707 · 2026-08-28 · fuente: inbox/2026-08-28-meet-kiran-handoff.md_

Ticket ENG-6492. Trabajado el 2026-08-28. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
18 tickets ENG con Kiran como asignado, tocados entre el 7 y el 28 de agosto, más los RCS enlazados. Todo verificado en Jira en vivo. --- Kiran es asignado en 9 de los 10 tickets del cluster de permisos y en los 8 del cluster de identidad. El cuello de botella de ingeniería para todo el dominio Incident es una persona.

## Rastro
2026-08-28 inbox/2026-08-28-meet-kiran-handoff.md

## ENG-7184. Guía del día, lunes 31 ago 2026 — 2026-08-31
_chunk 1709 · 2026-08-31 · fuente: inbox/2026-08-31-guia-del-dia.md_

Ticket ENG-7184. Trabajado el 2026-08-31. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Los 16 tickets abiertos de Juan, ordenados por lo que desbloquea más con menos esfuerzo. Cada bloque trae el estado verificado en Jira hoy, el paso concreto de investigación, el texto listo para pegar y lo que no se debe decir. Jira es de solo lectura desde acá. Todos los textos los pega Juan.

## Rastro
2026-08-31 inbox/2026-08-31-guia-del-dia.md

## ENG-7189. Preguntas por ticket, Kiran, 28 ago 2026 — 2026-08-28
_chunk 1710 · 2026-08-28 · fuente: inbox/2026-08-28-meet-kiran-preguntas-por-ticket.md_

Ticket ENG-7189. Trabajado el 2026-08-28. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Inglés para leer en la llamada. Español para que sepas qué estás preguntando y por qué. --- **EN** > "Matt asked you for this SELECT so Support could stop resolving permission complaints by > assertion. You delivered it in one day.

## Rastro
2026-08-28 inbox/2026-08-28-meet-kiran-preguntas-por-ticket.md

## RCS-27598. Dossier Alo Yoga — tickets RCS, verificado en Jira el 1 sep 2026 — 2026-09-01
_chunk 1713 · 2026-09-01 · fuente: inbox/2026-09-01-dossier-alo-yoga.md_

Ticket RCS-27598. Trabajado el 2026-09-01. 1 notas en inbox.

## Evidencia
Fuente: Jira cloud 7eb600cf-c7e0-43ed-acc4-90b277d43514, proyecto RCS. Solo lectura.
Recolectado el 2026-09-01. Todos los estados y fechas son literales de Jira.
Donde Jira no tiene el dato, dice "no consta en Jira".

## Rastro
2026-09-01 inbox/2026-09-01-dossier-alo-yoga.md

## RCS-27941. Kiran cruzó `incident.Suspect` contra `incident.Shoplifting` y `incident.MasterCase`, y sacó el `CaseType` de — 2026-09-01
_chunk 1714 · 2026-09-01 · fuente: inbox/2026-08-25-rcs-27941-plan-verificacion-escalamiento.md;2026-09-01-rcs-27941-causa-raiz-case-type-security.md_

Ticket RCS-27941. Trabajado el 2026-08-25 a 2026-09-01. 2 notas en inbox.

## Causa
Kiran cruzó `incident.Suspect` contra `incident.Shoplifting` y `incident.MasterCase`, y sacó el
`CaseType` de cada Peters. Después abrió Manage Case Type, pestaña Security, en
`apps.apprissretail.com/tailoredbrands/nettrack/Admin/CaseTypeConfig.aspx`.

## Evidencia
El RCA del 28 de julio sostiene dos cosas. Las dos quedan sin respaldo con las capturas nuevas.

**Afirmación 1 del RCA:** "Beverly resolves to Security Level 11 (Corporate User), which does not have
Incident search access", y el nivel 5 Location Manager sí la tiene.

**Lo que muestra la evidencia:** Francesca Ramos tiene Incident Security ID **Location Manager** y su
búsqueda de "Peters" devuelve el mismo "No data to display" que la de Beverly, que está en
**Corporate User**. Dos niveles distintos, el mismo síntoma exacto. El nivel de seguridad no separa el
caso que funciona del que falla. Escalar cargando esta premisa le entrega a Engineering un
diagnóstico ya falsificado.

**Afirmación 2 del RCA:** los claims de Okta re-derivan el nivel 11 en cada login y por eso el DELETE
no persiste.

**Lo que muestra la evidencia:** Colton sacó a Beverly y a Francesca del grupo
TMW-APP-OKTA-SSO-Appriss-EBR-CorporateUser del archivo diario el 13 de agosto. El RCA predice que con
eso el nivel del feed gana. Siete días después Beverly sigue apareciendo como Corporate User en la UI
y la búsqueda sigue vacía. O el cambio del feed no propagó, o el nivel no es la variable que manda.
El caso de Franc

## Que sigue
[2026-08-25] Que la fila faltante **cause** la búsqueda vacía. Es correlación con cuatro casos y cero
contraejemplos, no causalidad demostrada.

| Usuario | Fila en LPUser2 | Búsqueda en Incident |
|---|---|---|
| Dexter Monroe | sí, UserID 22 | funciona |
| Matthew Sincic | sí, no aparece en la lista de colgantes | funciona, su Edit se resolvió |
| Beverly Wright | no | falla |
| Francesca Ramos | no | falla |

Cuatro de cuatro consistentes. Con 267 colgantes y solo tres quejas, la pregunta que falta es por qué
los otros 264 no reclaman. La respuesta probable es que no usan la búsqueda de Incident, y hay que
demostrarlo, no suponerlo.
[2026-09-01] Appriss no define qué roles ven qué tipos de incidente. Tailored Brands sí. Beverly usa Incident para
bajar documentación de casos de empleados para reclamos de desempleo, así que Employee Work Injury y
Refund Fraud encajan con su función. Confirmalo con ellos antes de tocar nada.

Preguntale a Kiran quién aplica el cambio, si el admin del cliente desde esa pantalla o Delivery.

---

## Rastro
2026-08-25 inbox/2026-08-25-rcs-27941-plan-verificacion-escalamiento.md
2026-09-01 inbox/2026-09-01-rcs-27941-causa-raiz-case-type-security.md

## RCS-28032. Fecha: 2026-08-25 Client ID 433. Estado en Jira: Work in progress, assignee Juan, Medium, labels FromEmail, L1 — 2026-08-25
_chunk 1716 · 2026-08-25 · fuente: inbox/2026-08-25-rcs-28032-cierre-evidencia-y-escalacion.md_

Ticket RCS-28032. Trabajado el 2026-08-25. 1 notas en inbox.

## Causa
Fecha: 2026-08-25
Client ID 433. Estado en Jira: Work in progress, assignee Juan, Medium, labels FromEmail, L1, Uni_Jul_26_WAFAccess.
Ultimo movimiento del cliente: Joe Austin, 18 ago, con las capturas. Siete dias sin respuesta nuestra.

## Que sigue
`brain/memoria/reference_multidistrito_lhua.md` afirma que un usuario con dos distritos solo ve uno a la vez,
y usa este caso como confirmacion. Hoy no hay evidencia de que Dayna tenga dos distritos asignados, tiene tres
tiendas y las tres estan en el 501. La memoria queda sin respaldo hasta que corra el experimento de la tienda
948. No la borres todavia, marcala como en verificacion.

`brain/memoria/reference_jerarquia_ubicaciones_incident.md` dice que el distrito se hereda del StoreIdent
primario, verificado en cuatro usuarios el 10 de agosto. Esa parte del modelo no la toca la evidencia de hoy.
El ejemplo de Dayna que usa como prueba si queda invalidado.

## Rastro
2026-08-25 inbox/2026-08-25-rcs-28032-cierre-evidencia-y-escalacion.md

## RCS-28094. Vallarta Supermarkets, quién abre y administra los tickets en el portal — 2026-08-31
_chunk 1719 · 2026-08-31 · fuente: inbox/2026-08-31-vallarta-admins-portal.md_

Ticket RCS-28094. Trabajado el 2026-08-31. 1 notas en inbox.

## Que sigue
Agregar Vallarta al cheat sheet de ruteo: contacto Hector Flores, admins Hector Flores, Carlos Ardon
y Noemi Casas.

## Rastro
2026-08-31 inbox/2026-08-31-vallarta-admins-portal.md

## RCS-28223. Las dos auditorias juntas, para comparar de un vistazo. ```sql SELECT acs.AuditConfigID, acs.SectionDescriptio — 2026-08-27
_chunk 1723 · 2026-08-27 · fuente: inbox/2026-08-27-rcs-28223-EVIDENCIA.md;2026-08-27-rcs-28223-causa-raiz.md;2026-08-27-rcs-28223-consultas-parte2.md;2026-08-27-rcs-28223-consultas-parte3.md;2026-08-27-rcs-28223-consultas-parte4.md;2026-08-27-rcs-28223-consultas.md;2026-08-27-rcs-28223-continuidad-david-vargas.md;2026-08-27-rcs-28223-esquema-audit.md;2026-08-27-rcs-28223-hallazgos-pdf.md_

Ticket RCS-28223. Trabajado el 2026-08-27. 9 notas en inbox.

## Que pasa
Las dos auditorias juntas, para comparar de un vistazo.

```sql
SELECT  acs.AuditConfigID,
        acs.SectionDescription,
        acq.QuestionType,
        COUNT(*) AS Preguntas,
        SUM(CASE WHEN acq.GridCols IS NULL THEN 1 ELSE 0 END) AS SinGridCols,
        SUM(CASE WHEN acq.GridConfig IS NULL THEN 1 ELSE 0 END) AS SinGridConfig,
        MIN(DATALENGTH(acq.GridCols)) AS GridCols_Min,
        MAX(DATALENGTH(acq.GridCols)) AS GridCols_Max
FROM    incident.AuditConfigQuestion acq
JOIN    incident.AuditConfigSection acs ON acs.AuditConfigSectionID = acq.AuditConfigSectionID
WHERE   acs.AuditConfigID IN (2, 4)
  AND   ISNULL(acq.DeleteFlag, 0) = 0
GROUP BY acs.AuditConfigID, acs.SectionDescription, acq.QuestionType
ORDER BY acs.AuditConfigID, acs.SectionDescription, acq.QuestionType;
```

---

## Evidencia
Corrido el 27 y 28 ago 2026 contra el tenant mcdonalds, Client ID 402, AuditConfigID 4.
Todo sale de SELECT.

## Que sigue
[2026-08-27] Reproducir primero y contestarle a Matt con repro completo, o contestarle hoy con lo que hay y
declarar que el repro va aparte. Sin repro el ticket puede volver a rebotar.
[2026-08-27] El SELECT de `inbox/2026-08-27-rcs-28223-plan-repro.sql` ya se puede correr con Client ID 402.
Sirve para numerar las preguntas de Crew y confirmar su FieldType.

## Rastro
2026-08-27 inbox/2026-08-27-rcs-28223-EVIDENCIA.md
2026-08-27 inbox/2026-08-27-rcs-28223-causa-raiz.md
2026-08-27 inbox/2026-08-27-rcs-28223-consultas-parte2.md
2026-08-27 inbox/2026-08-27-rcs-28223-consultas-parte3.md
2026-08-27 inbox/2026-08-27-rcs-28223-consultas-parte4.md
2026-08-27 inbox/2026-08-27-rcs-28223-consultas.md
2026-08-27 inbox/2026-08-27-rcs-28223-continuidad-david-vargas.md
2026-08-27 inbox/2026-08-27-rcs-28223-esquema-audit.md
2026-08-27 inbox/2026-08-27-rcs-28223-hallazgos-pdf.md

## RCS-28256. Cola del 1 sep 2026, refresco automatico — 2026-09-01
_chunk 1725 · 2026-09-01 · fuente: inbox/2026-09-01-cola.md_

Ticket RCS-28256. Trabajado el 2026-09-01. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Corrida programada antes del turno. Jira en vivo, 18 tickets abiertos asignados a Juan. `bin/eval_cola.py` da exactitud 8 de 13, 62 por ciento. El lexico de promesas se desactualizo y la cola cruda salio mal ordenada.

## Rastro
2026-09-01 inbox/2026-09-01-cola.md

## RCS-28289. Arreglo del clasificador de cola, 2026-09-03 — 2026-09-03
_chunk 1727 · 2026-09-03 · fuente: inbox/2026-09-03-fix-clasificador.md_

Ticket RCS-28289. Trabajado el 2026-09-03. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Se hicieron tres cambios en bin/cola.py y bin/eval_cola.py, los tres ya corridos y verificados contra el volcado de hoy. RCS-28289 traia el comentario "I'll be waiting for the update once Scott is back" y el clasificador lo mandaba a nivel 4 en vez de nivel 3. El patron `i'?ll wait for` no cubria la forma progresiva con "be" en medio. `i'?ll be waiting`, `i will be waiting`, `we'?ll be waiting`, `we will be waiting`, `still waiting (to hear|for|on)`.

## Rastro
2026-09-03 inbox/2026-09-03-fix-clasificador.md

## RCS-28327. RCS-28327 Instructivo Cinco pasos. Los dos primeros cierran la validación que quedó abierta desde el 24 de ago — 2026-09-04
_chunk 1729 · 2026-09-04 · fuente: inbox/2026-09-04-rcs-28327-informe.md;2026-09-04-rcs-28327-instructivo.md_

Ticket RCS-28327. Trabajado el 2026-09-04. 2 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
RCS-28327 Instructivo Cinco pasos. Los dos primeros cierran la validación que quedó abierta desde el 24 de agosto. El paso 3 se ejecuta con una de dos ramas según el resultado. El paso 4 es la transición.

## Rastro
2026-09-04 inbox/2026-09-04-rcs-28327-informe.md
2026-09-04 inbox/2026-09-04-rcs-28327-instructivo.md

## RCS-28334. Revision de tickets en Completed, 31 ago 2026 — 2026-08-31
_chunk 1730 · 2026-08-31 · fuente: inbox/2026-08-31-completed-a-closed.md_

Ticket RCS-28334. Trabajado el 2026-08-31. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Pedido de Vedant Shirude en el mensaje al equipo. El aviso hablaba de 25 tickets en Completed entre Vedant, Sebastian Rueda y Juan. Esto es solo el corte de Juan. Consulta a Jira, project = RCS, assignee = currentUser(), status = Completed.

## Rastro
2026-08-31 inbox/2026-08-31-completed-a-closed.md

## RCS-28342. Kiran, 10 de agosto, cortando de raíz: > "No. Once deployed, all the clients get the same code." Úsalo tú mism — 2026-08-28
_chunk 1731 · 2026-08-28 · fuente: inbox/2026-08-28-meet-kiran-preguntas-RCS.md_

Ticket RCS-28342. Trabajado el 2026-08-28. 1 notas en inbox.

## Causa
Kiran, 10 de agosto, cortando de raíz:
> "No. Once deployed, all the clients get the same code."

Úsalo tú mismo como ejemplo de algo que ya no hay que volver a preguntar.

---

## Rastro
2026-08-28 inbox/2026-08-28-meet-kiran-preguntas-RCS.md

## RCS-28618. H1. El filtro de `audit_result` no matchea el valor real. El search fija audit_result = 'Expired'. Si el feed — 2026-08-31
_chunk 1738 · 2026-08-31 · fuente: inbox/2026-08-31-rcs-28618-analisis.md_

Ticket RCS-28618. Trabajado el 2026-08-31. 1 notas en inbox.

## Causa
H1. El filtro de `audit_result` no matchea el valor real.
El search fija audit_result = 'Expired'. Si el feed ahora escribe 'EXPIRED', 'expired', un código,
o mete padding en el varchar(20), da cero filas sin error. Es la explicación más económica de
"cero limpio". Prueba: correr el quick link "Refund Audit" genérico, sin el filtro de resultado.

H2. El feed externo de INKIRU no llegó al pipeline SnowTime.
Tabla vacía o congelada para 2026. Prueba: `SELECT MAX(trading_day)` y conteo por trading_day
sobre ext_inkiru_rva. Un conteo por metadata en Snowflake es casi gratis, responde de estadísticas.

H3. El tipo o el formato de la columna de tienda cambió.
La columna original es `store integer`, renombrada a `storeno` en 2023. Si tras el cutover llega
como varchar con padding, '03238' o '3238 ', el "Equal to 3238" da cero sin error. Prueba: quitar
el filtro de Store No y dejar solo Trading Day.

H4. El filtro Trading Day Between mata las filas por tipado.
Es la hipótesis de Edwin en RCS-28620, y tiene respaldo documental. Confluence 475893137434,
espacio DO, fija la regla: columnas DATE van como `Sysrepublic.Date`, columnas TIMESTAMP van como
`System.DateTime`. Un campo tipado DateTim

## Evidencia
Clave        RCS-28618
    Summary      WMT-QL Refund Audits Not Working
    Tipo         Incident
    Prioridad    Medium
    Estado       Work in progress
    Assignee     Sebastian Garces
    Reporter     Steve Curry, james.curry@walmart.com, Walmart, cliente 300
    Creado       27 ago 2026 07:33 EDT
    Updated      28 ago 2026 14:57 EDT
    Comentarios  2, los dos de acuse. Cero investigación escrita.
    Descripción  vacía. Son solo las cuatro imágenes.
    URL          https://trebuco.atlassian.net/browse/RCS-28618

Dos avisos de proceso antes de lo técnico.

El ticket no es de Juan. Es de Sebastian Garces, y `inbox/2026-08-31-flag-roster-garces.md` ya lo
marcó como uno de los que hay que revisar si Garces no pertenece al roster de Colombia.

El ticket lleva cuatro días sin una sola línea de investigación. Aimee Wadsworth ya cobró esto en
cuatro tickets de Vedant Shirude el 13 ago. La regla de Confluence 478006902856 exige repro con
capturas, entorno y las notas de IA escritas *en el ticket* antes de escalar.

## Que sigue
La barra de Composer tiene Parameters, Columns & Filters y Query. El botón Query imprime el SQL
generado. Ese SQL contesta de un tiro cuatro de las seis hipótesis, sin pedir acceso a base y sin
esperar a nadie:

    H1  el literal exacto contra el que se compara audit_result
    H3  el nombre físico y el formato de la columna de tienda
    H4  cómo se materializó el Between de Trading Day y contra qué columna
    H5  si hay una condición adicional que no aparece en Parameters

El indicador naranja con el número 2, junto a Query, marca dos condiciones fijas o bloqueadas.
Abrir Columns & Filters revela cuáles son. Si ahí aparece una tercera condición además de Store No
y Trading Day, H5 pasa a primera posición.

## Rastro
2026-08-31 inbox/2026-08-31-rcs-28618-analisis.md

## RCS-28621. Viraj Kansara cargo el archivo gemelo, RCS-28622, el mismo dia. Su log declara la ruta del INI: C:\Users\vkans — 2026-08-31
_chunk 1739 · 2026-08-31 · fuente: inbox/2026-08-28-rcs-28621-datos-no-visibles-diagnostico.md;2026-08-28-rcs-28621-quien-carga-el-archivo.md;2026-08-31-flag-roster-garces.md_

Ticket RCS-28621. Trabajado el 2026-08-28 a 2026-08-31. 3 notas en inbox.

## Causa
Viraj Kansara cargo el archivo gemelo, RCS-28622, el mismo dia. Su log declara la ruta del INI:

    C:\Users\vkansara\The Retail Equation, Inc\LP Software - Clients\Advance Auto\LPMS\LPMS.INI

Esa ruta esta bajo el perfil personal de Viraj. La carpeta "LP Software - Clients" es la carpeta de
cliente sincronizada en la maquina de cada agente, con el LPMS.INI que apunta a la base de datos de
ese cliente especifico.

Sebastian declara un origen distinto. Corrio LPImport.exe en QA-LPMS-RDP-001, un Bastion de Azure.
La base de conocimiento describe ese Bastion con acceso de grupo `qa-lpms-rdp_Reader_Bastion_Access`,
alcance de lectura y QA. Fuente: `brain/markdown/13-appriss-onboarding-base-de-conocimiento.md`,
seccion "Acceso a logs de LPMS / nettrack via Azure Bastion".

La bitacora de esta manana ya habia marcado el riesgo antes de que Sebastian ejecutara nada:

> "Sebastian no aparece con historial de imports en esta lista. Antes de que Sebastian lo ejecute,
> confirmar que tiene el acceso [a LP Software - Clients de Advance Auto]."

Sebastian no tiene esa carpeta sincronizada. Corrio la herramienta desde el Bastion compartido en su
lugar. El runbook exige verificar la base de dato

## Evidencia
[2026-08-28] RCS-28621 sigue en Work in progress. Cathryn Garcia comento a las 13:43 del 28 ago:

> "I spot checked and am not seeing newly hired TM's populate. For example, I don't see any results
> for TM #1012863. Is it possibly still loading?"

Sebastian habia comentado a las 12:29:

> "Import was completed via LPImport.exe on the QA-LPMS-RDP-001 Bastion (Employee Import tab, Comma
> delimiter, "Use Employee ID as key"). Test import result: [# updated 27178 / # created 6674].
> Final import result: [# updated 27178 / # created 6674]."
[2026-08-28] | Ticket | Qué | Estado | Assignee |
|---|---|---|---|
| RCS-28621 | AAP employee file para Incident | Work in progress | Sebastian Garces |
| RCS-28622 | AAP location file para Incident | Closed, Resolved | Viraj Kansara |
| RCS-25389 | El ticket enlazado, alta de SFTP | Closed, Resolved | Kathryn Scheldberg |
| RCS-27345 | AAP employee file, junio | Closed, Resolved | BJ Probert |
| RCS-25133 | AAP, LP Import Tool no instalable | Closed, Resolved | Dean Korbakis |

## Precedentes
Juan no tiene sincronizada "LP Software - Clients" y no puede entrar a otra cuenta que la tenga.
RCS-25133 ya resolvio exactamente esta situacion, del lado del cliente, no de un agente, pero la
mecanica es la misma herramienta.

Cathryn no podia instalar LPImport en su laptop nueva por politica de InfoSec. Dean Korbakis le
adjunto el ejecutable portable directo en el ticket, `LPImport6.50.3839.exe`, 1888256 bytes, 1.8 MB.
Coincide en tamano con el archivo de la captura de Juan. Instruccion textual de Dean:

> "It automatically will run without an install process, but you will need to copy over the
> lpms.ini file from your old machine and place it into your C:Windows folder on the new machine."

LPImport.exe es portable. No requiere instalacion ni la carpeta OneDrive de nadie. Lo unico que fija
la base de datos a la que se conecta es el archivo `lpms.ini` que este en `C:\Windows` junto al
ejecutable. Sin ese INI, o con uno de otra sesion, el header muestra lo que sea que diga ese archivo,
en el caso de Sebastian, AALPS-QA.

Camino sin la carpeta de Viraj y sin otra cuenta: pedirle a Viraj el `lpms.ini` que uso para el
gemelo RCS-28622, apuntado a produccion de Advance Auto. Copiarl

## Rastro
2026-08-28 inbox/2026-08-28-rcs-28621-datos-no-visibles-diagnostico.md
2026-08-28 inbox/2026-08-28-rcs-28621-quien-carga-el-archivo.md
2026-08-31 inbox/2026-08-31-flag-roster-garces.md

## RCS-28649. Seis archivos de la hora 16 del 29 de agosto cargaron la cabecera sin el detalle de item ni de tender, y dejar — 2026-09-01
_chunk 1742 · 2026-09-01 · fuente: inbox/2026-09-01-rcs-28649-informe.md;2026-09-01-rcs-28649-instructivo.md_

Ticket RCS-28649. Trabajado el 2026-09-01. 2 notas en inbox.

## Que pasa
Seis archivos de la hora 16 del 29 de agosto cargaron la cabecera sin el detalle de item ni de
tender, y dejaron 878,922 transacciones de THD sin lineas. El ticket lleva desde el 28 de agosto a
las 11:31 sin una respuesta sustantiva de Appriss, solo acuses, y el cliente escalo contando 61
horas. La peticion de recarga nunca salio de RCS: no existe ningun ticket DO ni ENG que referencie
RCS-28649. El remedio es reprocesar el rango con `REBUILD_RANGE`, que escribe en produccion y exige
rol admin, y antes de dispararlo hay que fijar quien lo ejecuta, si duplica lo ya cargado y que
rango recibe.

Version 2 de este informe, 2026-09-01. La evidencia que Juan aporto en siete capturas cambio tres
conclusiones de la version anterior. Ver la seccion de evidencia mas abajo.

## Causa
DO-10275, `085 THD client source data file handling`, Luke Du, creado 2026-04-15, estado Selected
for Development, assignee Flavio Smirne con la cuenta inactiva, cero comentarios, ultima
actualizacion 2026-08-18. Cita textual de la descripcion:

> All clients should have data loading process, especially data file handling with general code
> `appriss_files`. While 085 THD we have its own `files.py` independent to `appriss_files`, even the
> script also use `file_registry` table. But we met issues for the special `files.py` code file.

> 2. When THD changed file name pattern (without `.csv` as part of data file name), the `files.py`
> code file fails. We need to change code file for that. This is done two weeks ago.

> 3. Today on-call person (@Jenny Wang who is the original designer) found another issue: the
> `files.py` use special file path and file name and combine them for copying. Somehow today the
> file path and the file name are not matching. We need to change `files.py` again.

Y el diseno que propone Luke, todavia sin implementar:

> 4. If all files in the list already registered in `file_registry` table, we copy these files to
> DLZ; set `ingested_flg=1` for this `MARKER

## Evidencia
Consulta `text ~ "RCS-28649" AND project != RCS`. Cero resultados. Consulta de tickets DO y ENG
creados desde el 28 de agosto, filtrada por THD, carga, archivos y detalle. Cero resultados
relacionados con este incidente. Los unicos DO y ENG de THD activos son de Passport, dashboards de
Canada, claims y la migracion SnowTime.

**La peticion de recarga nunca se convirtio en trabajo asignable.** Vive solo como texto en un
comentario de RCS.

## Impacto
El impacto lo escribio el cliente: todos los investigadores de THD. Un investigador que abre una
transaccion sin detalle de item ni de tender no puede sustentar un caso. THD opera en US y Canada
sobre el mismo tenant, y las dos divisiones estan en el ticket.

El riesgo de proceso pesa mas que el tecnico ahora mismo. El cliente conto las horas en voz alta y
escalo. La escalacion vino sin trabajo de fondo detras, porque el ticket no tiene una sola nota de
investigacion escrita desde el 28 de agosto. Repetimos el patron que Aimee corrigio el 13 de agosto
en cuatro tickets: la investigacion nunca llego al ticket, asi que el ticket no avanza.

Riesgo secundario. Cuanto mas se demore la recarga, mas dias de trading quedan con discrepancia
acumulada en el reporte del cliente, y mas grande se vuelve el lote a recargar.

## Que sigue
El remedio identificado es reprocesar el 29 de agosto para que el pipeline vuelva a insertar las
lineas de item y tender que no llegaron a la tabla final. Juan verifico que el dato crudo existe.
El procedimiento es `REBUILD_RANGE`, escribe en produccion y exige rol admin.

Tres cosas quedan por resolver antes de ejecutarlo, y ninguna es opcional.

**Quien tiene el rol admin.** Si Juan no lo tiene, el escalamiento sigue en pie y el destinatario
cambia segun quien ejecute el procedimiento. La regla de
`brain/memoria/reference_escalacion_l3_procedimiento.md` manda dato o configuracion ya en produccion
a Delivery, que para Secure 5 va a Peyman Motlagh con el Sprint `RCS Support Team`. Un procedimiento
almacenado que reescribe tablas de produccion tambien encaja en Database Services, transicion 591,
disponible sobre este ticket y ausente del flujo escrito. Pregunta antes de mover.

**Que hace `REBUILD_RANGE` con las cabeceras que ya estan.** El cerebro no tiene una sola linea
sobre este procedimiento. Nadie documento si borra y reconstruye el rango o si inserta encima. Si
inserta encima, 878,922 transacciones duplicadas convierten un ticket escalado en un incidente
mayor. Exige la respu

## Precedentes
No existe flujo escrito para recargar archivos de transacciones POS. El cerebro lo declara como
hueco en `inbox/2026-08-28-rcs-28621-quien-carga-el-archivo.md`: "No existe flujo en `flujos/` para
'import attached file'". El unico runbook de carga manual que existe cubre archivos de employee y
location para Incident con LPImport, no transacciones.

El precedente real mas cercano es RCS-28581 y DO-9495, en
`inbox/2026-08-31-rcs-28581-cwh-pos-number-regresion.md`:

> Bartosz recargo a mano el archivo c248_rawdata_postransactions/2026/02/17/17/data_6_5_0.json.gz
> para materializar el fix.

Dos cosas que se sacan de ahi. La particion es `cliente/anio/mes/dia/hora/`, que es exactamente el
nivel de granularidad que pide THD. Y quien ejecuto fue ingenieria, no soporte. Existe ademas un
estado de Jira llamado `Reload Required`, que ese mismo ticket recorrio.

Precedente de recibos que no renderizan por hueco de dato y no por defecto del visor: RCS-27140 de
Alo Yoga, en `brain/markdown/16-rcs-soluciones.md`, donde `image_url` nulo en
`ardm_Item.extra_fields` dejaba al visor sin renderizar. Confirma el patron de que el visor de
recibos falla hacia abajo cuando el dato no esta.

## Rastro
2026-09-01 inbox/2026-09-01-rcs-28649-informe.md
2026-09-01 inbox/2026-09-01-rcs-28649-instructivo.md

## RCS-28683. PLAN. Escalación a ENG y tracker interno — 2026-09-01
_chunk 1745 · 2026-09-01 · fuente: inbox/2026-09-01-contexto-para-el-chat-de-jim.md;2026-09-01-escalar-a-eng.md_

Ticket RCS-28683. Trabajado el 2026-09-01. 2 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Martes 1 de septiembre de 2026, verificado con `date`. Estados leídos de Jira en vivo hoy. Jira quedó en solo lectura. Criterio de Matt, que J.R.

## Rastro
2026-09-01 inbox/2026-09-01-contexto-para-el-chat-de-jim.md
2026-09-01 inbox/2026-09-01-escalar-a-eng.md

## A quién asignar al escalar un RTS: Under Engineering Review vs Under Support Data Team Review — 2026-08-27
_chunk 1757 · 2026-08-27 · fuente: inbox/2026-08-27-rts-escalacion-a-quien-asignar.md_

# A quién asignar al escalar un RTS: Under Engineering Review vs Under Support Data Team Review

Fecha: 2026-08-27. Fuente: Confluence RTS en vivo más Jira en vivo.

## 1. Under Engineering Review

Fuente: "Escalating Tickets to L3 Departments: Procedures and Responsibilities", RTS 478006902856,
Aimee Wadsworth. La página se modificó hace una hora, así que está vigente.

| Producto | Assignee | Extra |
|---|---|---|
| Secure / Incident Engineering | Shandana Khan | Se auto crea un ENG y los comentarios sincronizan en ambos sentidos |
| Engage Engineering | Ian Williams | Mensaje obligatorio por Teams. Backups: Shruti Golwalker, Kenny Vu |
| RTI / RTIaaS | Dejar sin asignar | Los engineers lo toman de su cola |

Kevin Woo y Shruti manejan cambios de POS en Engage. Kevin también trickle transactions.

## 2. Under Support Data Team Review

Fuente: "Support Data Team Ticket Triage", RTS 477555982355, Aimee Wadsworth, 05-jul-2026.

Assignee: **Peyman Motlagh**. Él monitorea la cola del Support Data Team y reasigna al engineer que
corresponde. El engineer recibe correo del assignment.

Campos que van con la escalación:

- Label `Support_Data_Team`
- Team Ownership: "Support (Delivery dep.)"
- Sprint: "RCS Support Team"

Alcance del equipo: solo Secure 5. Ingest de data del retailer, data incorrecta en receipts o
reportes. No monitorea ningún otro producto.

## 3. Detalle que hay que tener presente

La página oficial de escalación L3 no lista el Support Data Team entre sus destinos. Para el camino
L2 documentado usa `Under Delivery Review` con Peyman Motlagh y Sprint "RCS Support Team". El status
`Under Support Data Team Review` sí existe en el workflow de RTS y hoy tiene 7 tickets abiertos.

Evidencia de cómo se usa hoy en RTS, tomada de RTS-206598 el 27-ago-2026. Anil P de L1 toma el
ticket, lo pasa a Work in progress, lo mueve a Under Support Data Team Review con el label
`Support_Data_Team`, y lo reasigna dentro de L1 a Ayesha Mehar. El status enruta, el assignee se
queda en L1. En los 50 tickets RTS que pasaron por ese status en los últimos 60 días, los 13
assignees distintos son todos del equipo L1 de India.

Los assignees reales del Support Data Team aparecen en los tickets viejos de esa cola:
Peyman Motlagh en RTS-177546, Luke Du en RTS-172310 y RTS-172317, Hao T Nguyen en RTS-168877.

Conclusión operativa: asigna a Peyman Motlagh y él distribuye. Si el ticket lo trabaja L1 y no L2,
el status solo enruta y el assignee no cambia.

## 3b. La matriz es de RCS, no de RTS

La página 478006902856 lo dice literal: "Please note the following status and/or assignee processes
when moving **RCS** tickets to different L3 departments". No hay matriz publicada de assignees para
RTS.

Medición en Jira, 27-ago-2026:

- RTS con assignee Shandana Khan, Peyman Motlagh o Ian Williams, creados en los últimos 365 días: 1
  ticket en total entre los tres.
- Los 15 RTS más recientes que pasaron por `Under Engineering Review` en 180 días conservan su
  assignee de L1 y llevan el label `L1`. Ninguno se reasignó a Shandana.
- RTS abiertos hoy en `Under Engineering Review`: 2. Uno sin asignar, uno con Matthew Kamminga.

En RTS el status enruta y el assignee se queda con el ingeniero de L1 que tiene el alert.

Camino que sí mueve a alguien en RTS, según "Process - Internal Alerts", espacio DS, Chris Howard,
12-ago-2026. Si el retry en Snowflake no lo arregla, escalar a Data Engineering por Teams y OpsGenie
y avisar en el canal Data Engineering > Alerts. Miembros al 12-ago-2026: Chris Howard,
Nicholas Turner, Saddam Hussain como manager.

Si el problema necesita comunicación con el cliente, L1 crea un RCS. Ahí sí aplica la matriz con
Shandana Khan o Peyman Motlagh.

## 3c. El único precedente del equipo: RTS-206268

Consulta en Jira el 27-ago-2026. Los 11 miembros del equipo Support solo han tocado 12 RTS en toda
la historia del proyecto. De esos, uno solo pasó por `Under Engineering Review`. Ese es el caso
completo.

RTS-206268, "[Grafana] - Kinney Drugs (KNY/179) - Active Alerts: 1". Reporter svc rts. Labels
Grafana, L1, cat-GR-Secure, grafana-cid-179, subcat-Work-Item.

Timeline medido del changelog:

| Fecha y hora | Quién | Qué hizo |
|---|---|---|
| 20-ago 20:22 | Automation | Initiate → Open |
| 20-ago 20:23 | Madhuraj Gujaran (L1) | Se asigna, pasa a Work in progress |
| 20-ago 20:49 | Madhuraj Gujaran | Se quita el assignee, pasa a `Under L2 Support Review` |
| 21-ago 10:19 | Diego Buelvas | Se asigna, pasa a Work in progress |
| 21-ago 12:34:06 | Diego Buelvas | Publica el informe de triage completo |
| 21-ago 12:34:17 | Diego Buelvas | Work in progress → `Under Engineering Review` |
| 21-ago 12:34:34 | Diego Buelvas | Se quita el assignee, queda sin asignar |
| 22, 23 y 24-ago | svc rts | El alert sigue firing, nadie de engineering lo toca |
| 24-ago 06:13 | Vlad Bogus | Comenta "Ticket Moved to RCS: RCS-28543" |
| 24-ago 06:14 | Vlad Bogus | Under Engineering Review → Completed, y Automation lo cierra |

Lo que hizo Diego: dejarlo sin asignar. Nadie de engineering lo recogió en tres días. El ticket se
resolvió convirtiéndolo en RCS-28543, y Vlad Bogus hizo esa conversión.

Lo que sí movió la aguja fue Teams. Shireesh Ramdas de L1 pegó el 21-ago a las 05:30 el link al
canal R&D > 2026 SnowTime con el mensaje de Daniel Endersby, y ahí quedó la causa raíz: la migración
SnowTime, error de compilación de Snowflake, invalid identifier `T2.POS_ARTICL...`. El diagnóstico
llegó por el canal, no por el status.

Conclusión operativa para el equipo. Al pasar un RTS a `Under Engineering Review` se deja sin
asignar, igual que la regla de RTI/RTIaaS. El status por sí solo no consigue que nadie actúe. Hay
que postear en el canal de Teams del dominio, Secure 5 Issues para Secure 5, y si hay impacto en
cliente hay que convertirlo en RCS, que es donde la matriz con Shandana Khan aplica de verdad.

## 4. Pregunta abierta para Aimee o Kristin

Pedir que la página 478006902856 agregue la fila del Support Data Team, con el status exacto y el
assignee. Hoy hay dos caminos, `Under Delivery Review` documentado y `Under Support Data Team
Review` en uso, y la página no los distingue.

## Fuentes

- https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478006902856
- https://trebuco.atlassian.net/wiki/spaces/RTS/pages/477555982355
- https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478022959146 (Queue Process)
- https://trebuco.atlassian.net/browse/RTS-206598


## Rastro
2026-08-27 inbox/2026-08-27-rts-escalacion-a-quien-asignar.md

## Cosecha asignacion-reglas — 2026-08-28 — 2026-08-28
_chunk 1760 · 2026-08-28 · fuente: inbox/2026-08-28-cosecha-asignacion-reglas.md_

# Cosecha asignacion-reglas — 2026-08-28
Fuente: sesión local_659260da-3f2b-4ed2-9e99-7ad7ddd931ce

## Hallazgos verificados

La skill de asignación ordenaba por fecha de creación y no por vencimiento de SLA. La consulta no traía el campo Target Assignment Time. Ese error hizo aparecer RCS-28571 como el más viejo en lugar del más vencido.

Medición del techo de tickets por persona:

| Palanca | Cupo del día | Abiertos del equipo |
|---|---|---|
| Techo 16, sin cambio | 8 | 46 |
| Techo 18 | 12 | 46 |
| Techo 20 | 13 | 46 |
| Cerrar los 17 en Under Customer Review | 13 | 29 |

Subir a 20 y hacer el barrido dan el mismo cupo del día, 13, porque el incremento diario topa en 3 y 2 por persona. El techo reparte los 46. El barrido los baja a 29.

Tasa de aplicación de las propuestas: 11 de 20, 55%. Los cuatro desviados son exactamente los cuatro huérfanos de David. Ninguna de las once propuestas de la cola normal se movió de sitio.

Luis Hernandez lleva 1 ticket abierto de 5 posibles. Se le propusieron dos el 25 de agosto con cita textual de precedente y no se aplicó ninguno. Su perfil en el clasificador dice React y .NET, y la cola no trae frontend puro. Son 4 slots vacíos hace tres días.

Sebastián Garcés tiene 3 abiertos de 5 y los tres están en Under Customer Review. Tiene cero trabajo activo.

Los seis huérfanos de David quedaron colocados y David tiene 0 abiertos. Dos terminaron con Juan, RCS-28099 y RCS-28223.

RCS-28595 Stater Bros no estaba en la cola sin asignar. Está con Ryan Barlow en Under Delivery Review. La lista que mandó Aimee traía cinco tickets y solo cuatro eran válidos.

De los 17 sin asignar al final del día, 16 son Medium y 1 es Low. No hay High ni Critical. El criterio que queda es antigüedad.

No existe procedimiento escrito para correr la carga de archivos de empleados. Se buscó tres veces en la base y no está.

Advertencia registrada para las cargas de archivo, del RCS-28085 de Ollie's: el IT del cliente confirmó que el archivo traía el rol correcto y el sistema igual resolvió mal el rol. No prometer al cliente que la carga arregla el síntoma.

Decisión en mesa, item 241: devolver los archivos de empleados incompletos al cliente para que los corrija. Los errores en la data de empleados producen discrepancias en reportes.

## Decisiones y compromisos

Juan ejecutó cuatro asignaciones: RCS-28593 DSG y RCS-28599 Lululemon y RCS-28606 Williams Sonoma para Diego, RCS-28590 Floor & Decor para Rueda.

Recomendación fijada: subir el techo a 18, no a 20. Da 12 slots, destraba a Edwin y a Rueda, y no quita el argumento del barrido de Under Customer Review.

Corregir la skill de asignación para que traiga Target Assignment Time y ordene por vencimiento de SLA.

Regla de alcance aclarada: un cliente un dueño aplica cuando coinciden cliente y subsistema. TG Jones con Edwin en RCS-28274 no bloquea RCS-28627 para Luis, porque RCS-28274 es mapeo de Original Transaction Amount a nivel de header.

Candidatos para Luis con precedente verificado: RCS-28611 Appriss Internal, gráfico tipo Gauge, apoyado en que el Chart Wizard documenta Area, Bar, Bubble, Column, Line, Pie y Scatter sin incluir Gauge. Y RCS-28627 TG Jones, con procedimiento de diagnóstico en la guía de Kristine sección 13.1.

Candidatos para Garcés: RCS-28621 APP y RCS-28634 DHL, los dos imports de empleados. Lo dejan en 5 de 5. El costo es una sesión de veinte minutos de Edwin o de Rueda para correr el primero con él mirando. La salida es tres tickets y un procedimiento que hoy no existe en la base.

Tickets descartados con motivo: RCS-28626 ASDA SAML tiene precedente en contra, el análisis de RCS-28442 Torrid desmonta la premisa del certificado. RCS-28624 Lux CAMS upload choca con Edwin en RCS-28574. RCS-28629 Big 5 no tiene precedente ni alcance claro. RCS-28625 Shell ya está en Under Engineering Review.

Las tres transcripciones cosechadas quedaron en inbox. No se corrió `bin/guardar`, espera aprobación de Juan.

## Pendiente de verificar

RCS-28606 Williams Sonoma volvió a la cola sin asignar, ahora en Under Delivery Review, después de que Juan lo asignara a Diego. Revisar quién lo movió a Delivery y le quitó el dueño.

RCS-28571 Winn-Dixie venció hace 27 horas y su dueño natural, Rueda, está en 16 de 16. Sigue sin colocar mientras el techo no suba.

Los 3 tickets de Garcés en Under Customer Review son su desbloqueo real. Perseguirlos libera techo sin subirle carga.


## Rastro
2026-08-28 inbox/2026-08-28-cosecha-asignacion-reglas.md

## Cosecha azure-pr — 2026-08-28 — 2026-08-28
_chunk 1761 · 2026-08-28 · fuente: inbox/2026-08-28-cosecha-azure-pr.md_

# Cosecha azure-pr — 2026-08-28
Fuente: sesion local_19ba3b08-1343-4154-940d-76ecfee6008b, "Azure links y PR"

## Hallazgos verificados

Organizacion unica de Azure DevOps: `dev.azure.com/apprissdevops`.

Rutas de PR y builds:

```
https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/Secure/pullrequest/<ID>
https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/Secure/pullrequests?_a=all
https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_build?definitionScope=\Azure\Builds
https://dev.azure.com/apprissdevops/DataOps/_git/c026kro/pullrequest/56772
https://apprissretail.visualstudio.com/VerifyDatabase/_build?definitionId=209
```

DataOps ordena los repos de datos por cliente con el patron `c[ClientID][abrev]`. La branch de
trabajo es `Production`, nunca `master`.

Repos clave: `Secure`, que es el mono repo, `arpfiles`, que guarda configuracion por cliente y se
clona en `C:\arpfiles`, y `Tools`.

Los numeros de PR corren en una sola secuencia para toda la organizacion. El numero no identifica
el repo. El 55297 vive en `c001adm` y el 55640 en `Secure`, y quedan pegados en el mismo rango.
Abrir la URL con el repo equivocado devuelve error, ADO no redirige. Entra por la vista de PRs del
proyecto cuando no sepas de donde salio el numero.

PR 56323 y PR 55640 de Sysrepublic Secure ya estan citados en
`brain/memoria/project_teams_unificacion_2026_08_12.md`.

Paginas de Confluence localizadas:
- Raising a Pull Request (PR), espacio ARPDT, pagina `474635763949`, actualizada jul 2026.
- Code Review for Pull Requests, ARPDT, `474707591321`.
- Azure DevOps Permissions, ARPDT, `475770847254`. Define los grupos Secure y Approval y quien
  puede aprobar PRs.
- Azure DevOps, ARPDT, `1172807180`. Variable groups por entorno.
- Pull Request Review Checklist, espacio DO, `475092680745`. Version DataOps para SQL y Python.
- AI Use Case: Connecting Claude to Azure DevOps via MCP, espacio RTS, `477499654145`. Chenuka
  monto un MCP de ADO para leer PRs desde Claude.

## Decisiones

Ninguna cerrada. La sesion ofrecio guardar la tabla de links en `inbox/` y Juan no respondio. Este
archivo cubre esa oferta.

## Pendiente de verificar

Si Juan quiere el MCP de ADO montado para leer PRs directo en vez de pegar links. La pagina de
Chenuka describe el montaje y nadie lo probo en esta sesion.

Los grupos de permisos de Juan en ADO. La pagina existe, nadie verifico en cual grupo esta.


## Rastro
2026-08-28 inbox/2026-08-28-cosecha-azure-pr.md

## Cosecha luxottica — 2026-08-28 — 2026-08-28
_chunk 1765 · 2026-08-28 · fuente: inbox/2026-08-28-cosecha-luxottica.md_

# Cosecha luxottica — 2026-08-28
Fuente: sesion local_acf1b969-2fc1-4284-a566-d094def0cf73, "Luxottica - Edwin"

Ticket: RCS-28601. Edwin es el assignee, Juan lo asesora.

## Hallazgos verificados

`appserver1.lpguys.net` no esta deprecada. La busqueda no encontro un solo ticket ni una sola
pagina que la depreciara. Es un forward especifico de Luxottica hacia CAMS que se rompe y se
repara.

Reincidencia documentada desde 2022. La ultima fue RCS-28037 del 29 de julio, con summary identico
caracter por caracter. David Vargas lo cerro en 27 minutos con "Our team has applied a fix" y el
cliente confirmo sin cambiar de URL.

Precedente decisivo, RCS-17591 de septiembre 2024. Jie Chen propuso el mismo cambio de URL que
propuso Edwin. Dean Korbakis lo rechazo: "They refused to change it due to the fact of their mass
scale across the globe has utilized the original URL." Jie arreglo el forward y cerro como Code
Fix Provided. La negativa de Michael Kahrig hoy repite una posicion que Appriss acepto hace dos
años.

Falla logica del argumento de Edwin. Los dos hosts son `lpguys.net`. Si la unificacion cerrara
lpguys.net, la URL que el ofrecio como reemplazo tambien moriria.

Causa probable, sin confirmar. DO-12224, upgrade de produccion a netTrack en LpGuys, completado el
25 de agosto por Ryan Barlow. El smoke testing no reporto hallazgos y el forward legacy quedo
fuera de alcance.

Corroboracion. RTS-206515, sintetico de Grafana LPMS, alerta desde el 25 de agosto a las 19:45 y
sigue abierto. Los seis anteriores cerraron con Active Alerts en 0.

Ruta de escalacion, sacada de las guias de Confluence y de las transiciones reales del ticket, no
de memoria. Canal de Teams `Retail Ops: AALPS Issues and Outages`, con `@channel`, el tag
`@Infra-all` y mencion directa a Ryan Barlow por haber ejecutado DO-12224. Sin acuse de recibo a
los 30 minutos, OpsGenie via label hacia AALPS DevOps.

Guias usadas: "How to Escalate Critical/High Priority Tickets", RTS `123301200564`, y "Customer
Escalation Handoffs, Secure Audit & Legacy", RTS `478022139957`.

Deuda estructural. Las repeticiones cerraron como "Restored Services". Nadie abrio nunca un item
para meter ese forward en el smoke testing de LpGuys. El proximo upgrade lo rompe otra vez.

## Decisiones

Edwin corrige hoy la respuesta al cliente. La afirmacion de deprecacion es incorrecta y se corrige
sin suavizar.

Se entrego un procedimiento de nueve pasos. Los tres primeros son los urgentes: tomar el ticket y
pasarlo a Work in progress, corregir el comentario al cliente, verificar si
`apps.lpguys.net/luxottica/nettrack/` carga. Ese ultimo dato define si la escalacion va como
forward roto o como tenant caido.

La clasificacion Sev1 queda a criterio de Juan. Mas de 4000 tiendas caidas encaja en Major
Incident Management. La guia no fija umbral por numero de tiendas.

## Pendiente de verificar

Si `apps.lpguys.net/luxottica/nettrack/` carga. Sin ese dato la escalacion no tiene forma.

El conteo exacto de reincidencias. La sesion dice cinco veces desde 2022 en un momento y seis
cierres como "Restored Services" en otro. Reconciliar contra Jira antes de citarlo.

La causa DO-12224 sigue como probable. Nadie de Infra la confirmo.

Abrir el item que meta el forward de Luxottica en el smoke testing de LpGuys.


## Rastro
2026-08-28 inbox/2026-08-28-cosecha-luxottica.md

## Cosecha 4 sep 2026 — RCS-28753 Nike, precedente de campo de descuento manual — 2026-09-04
_chunk 1796 · 2026-09-04 · fuente: inbox/2026-09-04-cosecha-rcs28753-nike-precedente-descuento.md_

# Cosecha 4 sep 2026 — RCS-28753 Nike, precedente de campo de descuento manual

Sesión fuente: "RCS-28753 ticket" (local_499e196c), transcripción del 3 sep 2026.

## Hallazgo verificado

Precedente clave: RCS-21540, mismo cliente Nike, cerrado el año pasado. Peyman Motlagh de Ingeniería definió ocho campos de descuento con su columna fuente en ese ticket. El más cercano a "Manual Discount Amount" es "Total Discount Modify Amount", descrito por Peyman como "the monetary value of the sum of all manual overrides... the price was manually entered by the cashier".

Función PostgreSQL real que calcula esa familia de montos durante la ingesta: `SalePriceModifyAmount` y `SalePriceOverrideAmount`, filtradas por `manual_price_flag = 1`. Es la única fórmula concreta de un campo de descuento manual encontrada en la búsqueda completa.

Ruta de respaldo si Peyman confirma que es un campo distinto: `GetTransactionJson.sql`, override de Nike, cliente 67.

## Estado al cierre de la sesión

Comentario interno quedó pegado en RCS-28753 dirigido a Peyman Motlagh, preguntando si Manual Discount Amount es el mismo campo que él ya definió con otro nombre, con link a RCS-21540. Sin fecha de respuesta.


## Rastro
2026-09-04 inbox/2026-09-04-cosecha-rcs28753-nike-precedente-descuento.md

## RCS-28058. Los 7 casos de Stater Bros, informe para responder mañana — 2026-09-03
_chunk 1717 · 2026-09-03 · fuente: inbox/2026-09-03-informe-actualizaciones-cliente-viraj.md_

Ticket RCS-28058. Trabajado el 2026-09-03. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Rovo confirmo en Jira, hoy, estado, assignee, issuelinks y los ultimos tres comentarios de cada uno de los quince RCS y seis ENG de este correo. Los datos de este informe ya no son un cruce entre cerebro y el correo de Viraj, son el estado real de Jira a esta hora. Donde cerebro tenia un dueño distinto al que Jira confirma hoy, lo digo explicito, porque el cambio en si mismo es un dato util. Segunda verificacion, mas tarde el mismo dia, directo contra la API de Jira sin pasar por Rovo, sobre los veintiun tickets.

## Rastro
2026-09-03 inbox/2026-09-03-informe-actualizaciones-cliente-viraj.md

## RCS-28253. ICA — Issues in Secure, verificado en Jira 2026-09-03 — 2026-09-03
_chunk 1724 · 2026-09-03 · fuente: inbox/2026-09-03-ica-issues-secure.md_

Ticket RCS-28253. Trabajado el 2026-09-03. 1 notas en inbox.

## Evidencia
Cliente: ICA (163). Hilo de correo "Issues in Secure" entre J.R. Teagle, Chris Rippingale, Viraj
Kansara y Nikita Rathore. Cinco tickets involucrados, estado confirmado en Jira a las 11:36 am hora
Bogotá del 3 de septiembre, no en las fichas del cerebro porque ninguno tiene ficha local todavía.

## Rastro
2026-09-03 inbox/2026-09-03-ica-issues-secure.md

## RCS-28612. RCS-28612, Delivery Fee ausente en transacciones de Point of Sale — 2026-09-01
_chunk 1737 · 2026-09-01 · fuente: inbox/2026-09-01-rcs-28612-delivery-fee-pos.md_

Ticket RCS-28612. Trabajado el 2026-09-01. 1 notas en inbox.

## Evidencia
Jira vivo, getJiraIssue RCS-28612, RCS-28638 y RCS-25061, 1 sep 2026. Diez adjuntos del reporter,
guardados en `adjuntos/RCS-28612/` y descritos abajo. Cerebro completo, busqueda sobre
brain, flujos, investigaciones, tickets, inbox y bitacora.

## Que sigue
`adjuntos/RCS-28612/` quedo con diez archivos duplicados con prefijo de UUID truncado. El sandbox no
los pudo borrar. Los diez con nombre limpio son los buenos. Borra los que empiezan por cuatro
caracteres y guion.

## Rastro
2026-09-01 inbox/2026-09-01-rcs-28612-delivery-fee-pos.md

## Cosecha RCS-27941 — 2026-09-01 — 2026-09-01
_chunk 1776 · 2026-09-01 · fuente: inbox/2026-09-01-cosecha-rcs-27941.md_

# Cosecha RCS-27941 — 2026-09-01
Fuente: sesion local_1305e0cf-dfd9-47a5-9cd1-6ecee9c5032a, "Cerebro Ticket RCS-27941"

Tailored Brands. Beverly Wright y Francesca Ramos no obtienen resultados en el suspect search. La hipotesis de LPUser2 quedo derribada en esta sesion.

## Hallazgos verificados

- No hay fix aplicado en LPUser2. Ningun comentario reporta un cambio. Lo que Kiran describe es Dexter, que funciona desde el 28 de julio.
- El LEFT JOIN confirma que las dos usuarias siguen sin fila:

```
UserName                              IncidentUserID  UserID  LoginID
beverly.wright@tailoredbrands.com     50267           NULL    NULL
francesca.ramos@tailoredbrands.com    50268           NULL    NULL
```

- La hipotesis de LPUser2 esta muerta. Esta consulta la mato:

```sql
SELECT COUNT(*) AS con_fila
FROM membership.Users mu
JOIN incident.LPUser2 lp ON lp.UserID = mu.IncidentUserID
WHERE mu.IncidentUserID BETWEEN 50000 AND 50406;
```

Resultado: 0. Ningun usuario del bloque 50000 a 50406 tiene fila en LPUser2. No es un subconjunto, es el bloque completo. Los 267 estan todos igual y solo dos reclamaron. La ausencia de LPUser2 no causa el sintoma.

- El numero 140 que se uso antes es falso. Salio de restar 267 de 407 asumiendo que el rango estaba poblado sin huecos. Los 140 que se contaban como sanos no existen en `membership.Users`.
- El comentario de escalacion pegado el 25 de agosto contiene ese dato falso. Dice "140 of them resolve correctly, interleaved one by one". Engineering lo esta leyendo. Hay que corregirlo en Jira: retira el item B de la escalacion, deja en pie el A y el C.
- Explicacion de Kiran sobre el origen, textual: los usuarios se agregaron directo en platform y por eso no estan en LPUser2, y el bloque `IncidentUserID` que arranca en 50000 marca ese origen. Explica el origen. No explica el sintoma.
- Matt Gladden no participa en el proyecto Incident ni en el proceso de migracion, segun Kiran. Su lectura del 26 de agosto como "possibly a migration miss" ya no sostiene el argumento. Hay que sacarlo del ticket.
- Colton nunca mando el screenshot del 25 de agosto. La imagen mide 200x183, identica a su firma corporativa. Pego la firma.
- Dexter es `IncidentUserID` 22, de la carga vieja. No sirve como control del bloque 50000.
- Security level, groups, hierarchy y store coinciden entre Dexter y Beverly. Cada uno verificado.

## Lo que falta

Dos cosas pedidas a Kiran, ambas en su terreno:
- Contra que resuelve el suspect search al usuario que consulta. La tabla o el procedimiento que decide el result set.
- Alguien del bloque 50000 que busque bien. Es el control que nunca existio.

## Regla de estilo confirmada por Juan

Los mensajes de chat a Kiran van cortos y conversacionales, con el mismo largo de linea que ella usa. Nada de parrafos. El comentario formal del ticket si va en parrafos porque lo lee Shandana.

## Texto para pegar

Mensaje de chat a Kiran, ingles, sin markdown:

```
You're right, I ran it properly this time

Zero users in the 50000 to 50406 block have LPUser2 rows, not a subset

My earlier number was wrong, I subtracted instead of querying

So LPUser2 is out, all 267 are in the same state and only these two reported it

Noted on Matt, I'll drop that from the ticket

Since you asked what to check, two things would help most

What does the suspect search resolve the requesting user against? If I know the table or proc that decides the result set I can stop guessing

And do you know anyone in that same 50000 block who searches fine? That's the control I never had

Correcting my comment in the ticket now
```

Comentario al cliente, version final aprobada por Juan. Sin correccion, sin disculpa y sin compromiso de proximo contacto, como planteo Kiran:

```
Hi Colton,

Checking in on this one. Are Beverly and Francesca still running into issues, or is this resolved on their end?

If they are still seeing it, send me the URL of the search page, a screenshot with the filters visible, the values they entered, and the name they expected to find.

Thank you,
Juan
```

Va dirigido a Colton. El reporter formal es Mike DiTommaso. Colton coordina con Beverly desde el 6 de agosto y es quien consigue lo que se pide.

## Pendiente

Corregir en Jira el dato falso del comentario de escalacion del 25 de agosto.


## Rastro
2026-09-01 inbox/2026-09-01-cosecha-rcs-27941.md

## RCS-28148, M&S, el bloqueo no era de 1Password del equipo — 2026-09-03
_chunk 1789 · 2026-09-03 · fuente: inbox/2026-09-03-cosecha-rcs-28148-ms-1password-decision.md_

---
fecha: 2026-09-03
fuente: cosecha de sesion local, RCS-28148 data loading issue
sesion: local_234dc114-1f0e-4f9f-ac8e-5b3742dc36de
---

# RCS-28148, M&S, el bloqueo no era de 1Password del equipo

El ticket lleva desde el 20 de agosto sin que Appriss confirme un correo alternativo a Hari, pese a
dos recordatorios suyos y una intervencion de Shaun Callow el 1 de septiembre pidiendole detalles a
Edwin Garzon, que sigue sin respuesta.

Kelly Murray es la contacto de cuenta designada para M&S, no la unica via. Todo el equipo de soporte
ya tiene 1Password. El bloqueo real era a quien dirigir a M&S ahora que Kelly no esta disponible,
no un problema de acceso.

## Dos rutas documentadas en Confluence

Pedir acceso basico a 1Password via MyAccess, aprobacion en 1 dia, para quien reciba el archivo.
Usar la storage account EU `wa1tlogsharedneu`, ya habilitada para subidas de archivo de cliente, que
no depende de que una persona tenga 1Password.

No hay ningun ticket ni proceso previo en Cerebro sobre este mismo bloqueo de contacto.

## Decision tomada y texto listo

Juan da su correo, jmartinez@apprissretail.com, como destinatario del share de 1Password. Recibe el
archivo, lo pasa al canal de trabajo del equipo para que Edwin lo cargue, y confirma con el.

El texto para que Edwin pegue en Jira va dirigido a Hari, que pregunto directamente tres veces, no a
Liz, que es la reporter formal pero no ha tocado el hilo. Sin fecha futura, sin pedir nada mas alla
del archivo. El proximo contacto queda anclado a que llegue el archivo, no a un dia del calendario.
El archivo con el texto ya se entrego en esa sesion para que Juan lo revise y Edwin lo pegue.


## Rastro
2026-09-03 inbox/2026-09-03-cosecha-rcs-28148-ms-1password-decision.md

## ENG-8008. No tienes nada de esto en tu cola. El ticket es RCS-28653, Stater Bro Print Journal not working, lo trabaja Di — 2026-09-09
_chunk 1808 · 2026-09-09 · fuente: inbox/2026-09-09-eng-8008-print-journal-stater-bros.md_

Ticket ENG-8008. Trabajado el 2026-09-09. 1 notas en inbox.

## Que pasa
No tienes nada de esto en tu cola. El ticket es RCS-28653, Stater Bro Print Journal not working,
lo trabaja Diego Buelvas y hoy esta asignado a Shandana Khan en Accepted into Development. Los
dos PR de ENG-8008 ya se probaron en USdev.

## Evidencia
- Jira 9 sep: RCS-28653 assignee Shandana Khan, estado Accepted into Development, clona ENG-8008.
- ENG-8008 sigue en Backlog con Matthew Kamminga, actualizado el 4 sep. Los PR corren adelante
  del estado de Jira.
- `assignee = currentUser() AND statusCategory != Done` devuelve 18 tickets, ninguno de Stater
  Bros ni de impresion.

## Precedentes
- RCS-28242 Stater Bros, Unable to Print Journal Notes, cerrado el 28 ago contra ENG-7191.
- `tickets/ENG-7191.md`: cubre journal notes al imprimir, no cubre el panel post asignacion.
- Diego lleva tres updates seguidos sin ETA a Angie, 28 ago, 4 sep y 7 sep. El cuarto necesita
  contenido nuevo o el cliente lo va a leer como silencio.

## Rastro
2026-09-09 inbox/2026-09-09-eng-8008-print-journal-stater-bros.md

## RCS-27942. Dos reclamos en un ticket. El de Tracking # ya tiene respuesta. El de CartonClass y CartonContentCode vacios t — 2026-09-10
_chunk 1810 · 2026-09-10 · fuente: inbox/2026-09-10-rcs-27942.md_

Ticket RCS-27942. Trabajado el 2026-09-10. 1 notas en inbox.

## Que pasa
Dos reclamos en un ticket. El de Tracking # ya tiene respuesta. El de CartonClass y
CartonContentCode vacios tras Reload Cartons sigue abierto y con un compromiso vencido de 22 dias.

## Evidencia
ENG-1071 punto 4: "batch call the API to enrich the cartons with Class (or Contents Category),
Units, Total Retail $". Esos campos los llena Appriss, no el archivo del cliente.
Cliente 11 ago: "The retail value is populating but not the Class and Content Code", con cuatro
cartones y confirmacion de su IT de que el API si devuelve valores.
Bikash 6 ago, query con datos reales: ShopliftingID 5333930, TrackingNo 1ZH4E0790301911717,
CartonClass NULL, CartonContentCode NULL, CartonType Carton Not Received.

## Precedentes
ENG-1071 SOW del carton import, Done feb 2026. ENG-4225 combos contra ListMaster, Done 25 jun 2026.
ENG-5055 y ENG-5056, casos Xray de ese cambio, en Backlog, nunca ejecutados.
brain/markdown/27-cerebro-sistema-decisiones.md, conexion SSMS a LPMS produccion US.

## Rastro
2026-09-10 inbox/2026-09-10-rcs-27942.md

## RCS-28240. El clasificador decidia entre pedido y promesa por posicion en el texto: `p_preg > p_prom`. Juan cierra sus co — 2026-09-09
_chunk 1811 · 2026-09-09 · fuente: inbox/2026-09-09-diagnostico-promesa-condicionada-y-nivel-4.md_

Ticket RCS-28240. Trabajado el 2026-09-09. 1 notas en inbox.

## Que pasa
El clasificador decidia entre pedido y promesa por posicion en el texto: `p_preg > p_prom`.
Juan cierra sus comentarios con cortesia, asi que la promesa queda siempre al final y gana.
Los dos tickets subian a PROMESA SIN CUMPLIR con el cliente debiendo datos.

## Evidencia
RCS-28240  p_prom 542  p_preg -1   antes nivel 2, real 3
    RCS-28351  p_prom 308  p_preg -1   antes nivel 2, real 3
    RCS-28342  p_prom -1   p_preg -1   antes nivel 4, real 2
    niveles antes:   2=3 3=5 4=11      exactitud 13/13
    niveles despues: 2=1 3=8 4=10      exactitud 13/13

## Rastro
2026-09-09 inbox/2026-09-09-diagnostico-promesa-condicionada-y-nivel-4.md

## RCS-28753. La exactitud cayo a 77% con tres fallos: RCS-28753, RCS-27941, RCS-28294. Ninguno tenia la misma causa. Tratar — 2026-09-09
_chunk 1813 · 2026-09-09 · fuente: inbox/2026-09-09-eval-clasificador-77-a-100.md_

Ticket RCS-28753. Trabajado el 2026-09-09. 1 notas en inbox.

## Que pasa
La exactitud cayo a 77% con tres fallos: RCS-28753, RCS-27941, RCS-28294. Ninguno tenia la
misma causa. Tratarlos como un solo problema de lexico habria roto casos que funcionaban.

## Evidencia
exactitud 10/13 = 77%   antes
    exactitud 13/13 = 100%  despues
    niveles antes:   1=0 2=3 3=5 4=11
    niveles despues: 1=0 2=3 3=6 4=10

## Precedentes
El 8 sep 2026 paso lo contrario: 73% con dos de cuatro fallos por etiquetas vencidas, y el
diagnostico equivocado vivio semanas en ESTADO.md como deuda tecnica. La leccion no es que
las caidas sean siempre calendario. Es que hay que separar los fallos uno por uno antes de
tocar el lexico.

## Rastro
2026-09-09 inbox/2026-09-09-eval-clasificador-77-a-100.md

## RCS-28756. Ayesha pidio tres veces hoy la informacion segura para el cliente. El ticket esta en Under Support Review con — 2026-09-10
_chunk 1814 · 2026-09-10 · fuente: inbox/2026-09-09-instructivo-cierre-del-dia.md;2026-09-09-rcs-28756-chat-nichols.md;2026-09-09-rcs-28756-chat-peyman.md;2026-09-09-rcs-28756-fraseo-corte.md;2026-09-09-rcs-28756-instructivo.md;2026-09-09-rcs-28756.md;2026-09-10-rcs-28756.md_

Ticket RCS-28756. Trabajado el 2026-09-09 a 2026-09-10. 7 notas en inbox.

## Que pasa
[2026-09-09] Madhuraj devolvio el ticket el 2026-09-09 con cinco preguntas de Customer Insights de Nike. Peyman
confirmo el mismo dia que hay una API de Appriss entre Nike y el blob. Eso mueve la causa.
[2026-09-10] Ayesha pidio tres veces hoy la informacion segura para el cliente. El ticket esta en Under Support
Review con Juan. La arquitectura ya esta documentada y las cinco respuestas estan listas.

## Evidencia
[2026-09-09] EntityName c67_rawdata_order, 30 dias, leido por Juan: Incoming Messages 64.50M y Captured
Messages 64.61M, ambas en cero desde el 27 de agosto. Delta de 0.17%. El Capture proceso todo lo
que entro. Nada llego al hub despues del corte.
adjuntos/RCS-28756/2026-09-09-azure-incoming-messages-c67.png
Derivado: 3.63M mensajes por dia sobre 17.8 dias con dato. Contra 195352 a 234363 transacciones
ECOM cargadas por dia, salen entre 15 y 19 mensajes por transaccion. Un mensaje no es una orden.
[2026-09-10] Confluence PD 477499490306, Ingestion API - EventHub, Carl Costelow: "Customers POST data to the
API, which routes it into Azure Event Hub (small payloads) or Azure Blob Storage". El hub se nombra
solo como c{customerID}_rawdata_{dataType}, de ahi c67_rawdata_order.
Tres validaciones inbound: nombre de cliente 400/10, identidad contra ClientID y ClientScope 401/12,
dataType permitido 400/11.
Incoming Messages y Captured Messages de c67_rawdata_order en cero desde 2026-08-27 19:02 UTC.

## Precedentes
[2026-09-09] tickets/RTS-206999.md. Investigacion tecnica y canal con Nike.
tickets/RCS-27485.md. TJX EU, proveedor upstream dejo de enviar archivos diarios.
[2026-09-10] investigaciones/ingestion-api-como-entra-la-data.md. Flujo completo y criterio de que compartir.
RCS-28753. Peyman compartio nombres de campos y feeds con Nike, no codigo. Mismo criterio.
tickets/RTS-206999.md. Canal con Nike.

## Rastro
2026-09-09 inbox/2026-09-09-instructivo-cierre-del-dia.md
2026-09-09 inbox/2026-09-09-rcs-28756-chat-nichols.md
2026-09-09 inbox/2026-09-09-rcs-28756-chat-peyman.md
2026-09-09 inbox/2026-09-09-rcs-28756-fraseo-corte.md
2026-09-09 inbox/2026-09-09-rcs-28756-instructivo.md
2026-09-09 inbox/2026-09-09-rcs-28756.md
2026-09-10 inbox/2026-09-10-rcs-28756.md

## RCS-28838. Charla de emergencia 9 sep 2026: que toca a Juan y al equipo Colombia — 2026-09-09
_chunk 1816 · 2026-09-09 · fuente: inbox/2026-09-09-charla-emergencia-ica-bunnings.md_

Ticket RCS-28838. Trabajado el 2026-09-09. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Revision de los tickets citados en el resumen de estado que circulo hoy. comentarios de Jira leidos el 9 sep. RCS-28838 y RCS-28834, ICA, los trabajo Diego Buelvas, no Gabor Remenyi. Diego tomo ownership de ambos hoy, publico dos RCA completos con queries y punto de falla, y pidio routing a Shandana Khan.

## Rastro
2026-09-09 inbox/2026-09-09-charla-emergencia-ica-bunnings.md

## RCS-28873. Corpus de triage de Confluence bajado a Cerebro — 2026-09-10
_chunk 1817 · 2026-09-10 · fuente: inbox/2026-09-10-confluence-triage-diego.md_

Ticket RCS-28873. Trabajado el 2026-09-10. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
carpeta Triage del espacio RTS en Confluence, id 478142038021, mantenida por Diego Buelvas. https://trebuco.atlassian.net/wiki/spaces/RTS/folder/478142038021 46 fichas, 412KB, a `confluence/RTS-triage/`. Una por ticket, no son procesos genéricos. Cada una sigue el mismo formato de 10 secciones:

## Rastro
2026-09-10 inbox/2026-09-10-confluence-triage-diego.md

## chat peyman lectura cliente — 2026-09-09
_chunk 1818 · 2026-09-09 · fuente: inbox/2026-09-09-chat-peyman-lectura-cliente.md_

On 28756 I would wait before we call it that. The ones asking are their Customer Insights team, not the group that set up the feed. And we have not cleared our own ingestion API yet, Nichols is checking whether their calls hit it after 27 Aug. If they did, the gap is on our side.

If you also meant 28753, want me to ask Damir to consolidate what is still open, or book 30 minutes with him?


## Rastro
2026-09-09 inbox/2026-09-09-chat-peyman-lectura-cliente.md

## RCS-27765. La tienda 358 sigue con 773 transacciones el 25/06/2026, medido hoy. El reenvio del cliente si llego y se proc — 2026-09-14
_chunk 1822 · 2026-09-14 · fuente: inbox/2026-09-14-rcs-27765-guia-verificacion.md;2026-09-14-rcs-27765-sql-corregido.md;2026-09-14-rcs-27765.md_

Ticket RCS-27765. Trabajado el 2026-09-14. 3 notas en inbox.

## Que pasa
La tienda 358 sigue con 773 transacciones el 25/06/2026, medido hoy. El reenvio del cliente si
llego y se proceso. No contenia el 25 de junio.

## Evidencia
- Conteo hoy en `ARDM_121`, tienda 358: 24/06 = 2,323 · 25/06 = 773 · 26/06 = 2,421. Identico al
  27 jul. Las 773 se cargaron el 26 y 27 jun en 10 lotes `seg_121_<uuid>.zip.pgp`, 468 mas 305.
- Carga diaria del tenant, 8 al 12 sep: 259 a 261 tiendas todos los dias. El 10 sep sube a 339,872
  filas contra ~296,000 de un dia normal. Ese salto es el reenvio.
- `MIN(TradingDay)` de la carga del 10 sep es `2026-07-02`. Los demas dias arrancan en el dia
  anterior. Nada anterior al 2 de julio entro ese dia, asi que el 25/06 no estaba en el lote.

## Que sigue
Juan saco el SQL real con el boton Query. Motor confirmado Snowflake: sintaxis `set var` con `$var`
y `TABLE(SECURE_SQUAREHIERARCHY...)`. No hay CTE de Greenplum.

## Precedentes
- `inbox/2026-09-14-rcs-27765-sql-corregido.md`. El SQL del Composer contaba lineas de item y
  filtraba por `OrigTradingDay`. `inserteddatetime` y `filename` en `ardm_Header` fueron la prueba.
- `brain/markdown/09-appriss-kt-topic-1-data-pipeline-devops.md`. Registra este ticket como el caso
  de aviso de confirmar la ruta antes de afirmarle algo a un cliente.

## Rastro
2026-09-14 inbox/2026-09-14-rcs-27765-guia-verificacion.md
2026-09-14 inbox/2026-09-14-rcs-27765-sql-corregido.md
2026-09-14 inbox/2026-09-14-rcs-27765.md

## RCS-28871. Walgreens pidio el 10 sep, via cuestionario Peak Season Readiness: certificados que expiren antes de medio ene — 2026-09-15
_chunk 1831 · 2026-09-15 · fuente: inbox/2026-09-15-rcs-28871.md_

Ticket RCS-28871. Trabajado el 2026-09-15. 1 notas en inbox.

## Que pasa
Walgreens pidio el 10 sep, via cuestionario Peak Season Readiness: certificados que expiren antes
de medio enero 2027, deployments nov-dic 2026, si hubo stress testing y si el sistema soporta
auto-scaling, y el contact list/escalation matrix. Juan tomo el ticket ese dia y prometio respuesta;
van 3 dias sin contestar. Jira: Work in progress, assignee Juan.

## Evidencia
- RCS-27847 Samsung, 15-jul: "soporte NO tiene los datos del cuestionario (load tests, trafico,
  scale-up, rate limits, timeouts, fallback/RTO, code freeze) -> los tiene Infraestructura"
  (brain/markdown/21-kt-kristin-sign-off-procesos-rts.md L54).
- Matriz: Infrastructure -> Under Infrastructure Review, assignee se queda Juan, auto-crea RTAILIT
  (brain/memoria/reference_escalacion_l3_procedimiento.md).
- Infra: Russell Harmon, horario Pacifico, mismo patron en Kohl's RCS-27840 (mismo doc, L180 y
  L1073). CSM Walgreens: Paul Marderosian, Client Contacts.xlsx pestaña 209 fila 282.

## Precedentes
- RCS-27847 Samsung, cuestionario identico: tickets/RCS-27847.md
- RCS-27840 Kohl's, mismo ruteo a Infra con deadline: 21-kt-kristin-sign-off-procesos-rts.md L180

## Rastro
2026-09-15 inbox/2026-09-15-rcs-28871.md

## RCS-28881. Carlo Conty y dos usuarios mas de NEXCOM no pueden abrir en edicion el template de audit Annual Ops/Services R — 2026-09-14
_chunk 1832 · 2026-09-14 · fuente: inbox/2026-09-11-rcs-28881.md;2026-09-14-apis-accesos-y-hallazgo-jcrew-prep.md;2026-09-14-rcs-28881-ping-megha.md;2026-09-14-rcs-28881.md_

Ticket RCS-28881. Trabajado el 2026-09-11 a 2026-09-14. 4 notas en inbox.

## Que pasa
[2026-09-11] Carlo Conty y dos usuarios mas de NEXCOM no pueden abrir en edicion el audit Annual
Ops/Services Review en APIS. El panel de contenido sale vacio. Under Support Review,
Medium, Megha Rathi, desde el 10 sep 16:46 ET.
[2026-09-14] Carlo Conty y dos usuarios mas de NEXCOM no pueden abrir en edicion el template de audit
Annual Ops/Services Review en APIS prod. Panel de contenido vacio. Under Support Review,
Medium, Megha Rathi, sin comentarios de ella desde el 10 sep.

## Evidencia
[2026-09-11] - image-20260910-204539.png: el frame de navegacion carga completo con la pestaña Admin
  visible para Carlo, contenido en blanco. Sesion, auth y jerarquia resuelven.
- Carlo en la descripcion: "I am currently working on updating an Audit... I've tried to do
  it in my computer, Claude's and Ayla's". Falla al editar, en tres maquinas.
- NEXCOM es APIS on-prem, gobierno, sin acceso nuestro a su data ni su servidor, solo
  nexcom-prep. `21-kt-kristin-sign-off-procesos-rts.md:611` y `:1253`. Rebuild de pantallas,
  label cache reset y SQL quedan fuera del alcance de Soporte aqui.
[2026-09-14] - Probado el 14 sep en nexcom-prep con la cuenta jbarber. Abren bien el Audit Center, el audit
  14-HIA-0001-25, la pestaña Audit admin y el Template editor AT1000000106 de OPS Review
  Administration, codigo OPSA, con sus pestañas, Forms y Change History. El modulo de Audit
  del tenant rinde.
- El Template editor carga en la seccion Forms una referencia a un formulario por ID, en el
  caso probado `OPS Review - Administration( ID:361 )`. Ese es el punto de fallo candidato.
- En las cuatro pantallas de Audit de prep salen claves de screen label sin resolver:
  `Audit.status.1`, `Audit.date due`, `Letter.actions`, `Form status.0`, `Template deleted.0`,
  `Audit.template code`, `Audit score category.secondary category`. La capa de etiquetas de
  este tenant esta degradada. Mismo patron que RCS-28032 en Vitamin Shoppe.
- Annual Ops/Services Review no existe en prep. Sin templates ocultos: destildar
  "Hide expired/deleted templates" no revelo ninguno.

## Precedentes
[2026-09-11] - RCS-28139 Sportsman's, audit screens inaccesibles, BuildAllScreens sincrono contra el
  timeout de 100s. Secure, no APIS.
- RCS-28032 Vitamin Shoppe, Screen Labels sin resolver. `bitacora/RCS-28032.md`.
- RCS-28709 Stater Bros, blank screen sin causa ni ENG. `inbox/2026-09-04-rcs-28709-informe.md`.
- RCS-28449 Meijer, Secure not loading, restaurado en 47 min el 18 ago. Otro producto y otro
  hosting. La comparacion de Shannon Clark no aplica.
- RCS-28852 Rack Room, StartAudit=10, `confluence/RTS-triage/`. Descartado, Carlo es admin.
[2026-09-14] - RCS-28032 Vitamin Shoppe, NewAudit.aspx y AuditLog.aspx con Screen Labels sin resolver.
  `bitacora/RCS-28032.md`.
- RCS-28139 Sportsman's, audit screens inaccesibles, BuildAllScreens sincrono contra el timeout
  de 100s. Secure, no APIS.
- RCS-28709 Stater Bros, blank screen sin causa confirmada ni ENG.
- RCS-28449 Meijer, Secure not loading, restaurado en 47 min el 18 ago. Otro producto y otro
  hosting. La comparacion de Shannon Clark no aplica.
- Nota de Cerebro sobre `GetScreenLabelByFormField`, cientos de llamadas a base por recurso sin
  cache, PR 55972, marcada como causa candidata de pantallas que no cargan. Encaja con los
  labels crudos vistos hoy. Sin confirmar.

## Rastro
2026-09-11 inbox/2026-09-11-rcs-28881.md
2026-09-14 inbox/2026-09-14-apis-accesos-y-hallazgo-jcrew-prep.md
2026-09-14 inbox/2026-09-14-rcs-28881-ping-megha.md
2026-09-14 inbox/2026-09-14-rcs-28881.md

## ENG-6450. Facteus, guía para hablar con Viraj mañana — 2026-09-25
_chunk 1835 · 2026-09-25 · fuente: inbox/2026-09-24-facteus-complemento-viraj.md;2026-09-25-facteus-llamada-viraj-primera-persona.md;2026-09-25-facteus-llamada-viraj-talking-points-en.md;2026-09-25-facteus-llamada-viraj-talking-points.md_

Ticket ENG-6450. Trabajado el 2026-09-24 a 2026-09-25. 4 notas en inbox.

## Evidencia
**ENG-6450**, "Create Support Process Surrounding Facteus Daily Processing", estado Done. https://trebuco.atlassian.net/browse/ENG-6450

Es el ticket donde Chris fue documentando todo el trabajo desde julio. Su comentario del 15 de septiembre trae la misma lista del correo que llegó al equipo, con checkboxes:

- Marcados listos: triage en el ticket, detalle de datos faltantes, árbol de decisión, definir INTERNAL, definir EXTERNAL, contactos de Facteus, dashboard enlazado.
- Sin marcar todavía: accesos de Support antes del handover, lectura a PRODDATACLOUD, lectura a FACTEUS_DATASHARE, y enviar el correo de feedback de vuelta al hilo.

Ese último punto sin marcar es exactamente lo que Camila está pidiendo con su recordatorio de hoy.

**ENG-9367**, "Handover Support Process", creado hoy mismo por Chris, en Backlog, depende de ENG-6450. https://trebuco.atlassian.net/browse/ENG-9367. Su descripción dice que el handover completo se espera para el sprint de octubre. Este ticket es nuevo, todavía no tiene comentarios.

**RETAILDB-2972**, "Facteus Access For Support Team", estado Open, sin assignee, sin comentarios, creado el 16 de septiembre por Chris. https://trebuco.atlassian.net/browse

## Rastro
2026-09-24 inbox/2026-09-24-facteus-complemento-viraj.md
2026-09-25 inbox/2026-09-25-facteus-llamada-viraj-primera-persona.md
2026-09-25 inbox/2026-09-25-facteus-llamada-viraj-talking-points-en.md
2026-09-25 inbox/2026-09-25-facteus-llamada-viraj-talking-points.md

## ENG-7189. Flujo nuevo: verificar SecurityID post migracion — 2026-09-28
_chunk 1836 · 2026-09-28 · fuente: inbox/2026-08-28-meet-kiran-preguntas-por-ticket.md;2026-09-28-flujo-securityid-eng-7189.md_

Ticket ENG-7189. Trabajado el 2026-08-28 a 2026-09-28. 2 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Guardado el 28 sep 2026 desde RCS-29147, Prada. Kiran Vadday entrego en ENG-7189, el 13 ago 2026, un SELECT que compara incident.LPUser2.SecurityID contra membership.Users.SecurityID y marca OK o MISMATCH por usuario. El adjunto SecurityIDMismatchCheckandFix.txt trae ademas el UPDATE de correccion. Es la herramienta para cualquier ticket de SecurityLevel NULL, permisos que cambiaron con la migracion o Session Error al entrar a Incident.

## Rastro
2026-08-28 inbox/2026-08-28-meet-kiran-preguntas-por-ticket.md
2026-09-28 inbox/2026-09-28-flujo-securityid-eng-7189.md

## RCS-23141. Customer Name no pasa a Excel. hipótesis de alta confianza del mismo defecto de RCS-26238 — 2026-09-17
_chunk 1840 · 2026-09-17 · fuente: inbox/2026-09-17-RCS-23141-root-cause.md_

Ticket RCS-23141. Trabajado el 2026-09-17. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Customer Name no pasa a Excel. hipótesis de alta confianza del mismo defecto de RCS-26238. Ambos campos de texto tenían tipo System.Double. El historial del archivo conserva esos tipos durante septiembre de 2025.

## Rastro
2026-09-17 inbox/2026-09-17-RCS-23141-root-cause.md

## RCS-26238. Account # y Customer Full Name aparecen en pantalla y quedan vacíos al exportar Same Tender Card. tender_accou — 2026-09-17
_chunk 1841 · 2026-09-17 · fuente: inbox/2026-09-17-RCS-26238-root-cause.md_

Ticket RCS-26238. Trabajado el 2026-09-17. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Account # y Customer Full Name aparecen en pantalla y quedan vacíos al exportar Same Tender Card. tender_accountnumber y customer_customerfullname declarados System.Double en repo/44/system/ebr/smarttracksearches/sametendercard.search. El escritor Excel convierte según el tipo; la grilla muestra texto. Timothy Mulrenan, 6 abr 2026, comentario 3075525, identifica archivo, campos y comparación con clientes 57 y 138.

## Rastro
2026-09-17 inbox/2026-09-17-RCS-26238-root-cause.md

## RCS-27233. Cobertura y trazabilidad / Coverage and traceability — 2026-10-07
_chunk 1842 · 2026-10-07 · fuente: inbox/2026-10-07-talos-cobertura-y-evidencia.md_

Ticket RCS-27233. Trabajado el 2026-10-07. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
28 septiembre a 7 octubre, America/Bogota. Se recuperaron 1.309 comentarios de estos 61 tickets; son registros, no 1.309 hechos independientes. RCS-27233 tiene 145 y se paginó completo. ENG-7219 se consultó como candidato histórico adicional sin comentarios.

## Rastro
2026-10-07 inbox/2026-10-07-talos-cobertura-y-evidencia.md

## RCS-27667. Nordstrom Inc., quien del equipo Colombia mas tickets ha manejado (2 oct 2026) — 2026-10-02
_chunk 1843 · 2026-10-02 · fuente: inbox/2026-10-02-nordstrom-quien-mas-ha-manejado-colombia.md_

Ticket RCS-27667. Trabajado el 2026-10-02. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Jira en vivo, JQL project = RCS AND organizations = "Nordstrom Inc.", 320 tickets. Conteo por assignee actual. RCS-27667, 27771, 27814, 27876, 28300, 28489, 28526, 28914 (jul a sep 2026). David Vargas, ya fuera del equipo:

## Rastro
2026-10-02 inbox/2026-10-02-nordstrom-quien-mas-ha-manejado-colombia.md

## RCS-27676. Revisión del 16 de septiembre de 2026, 12:57 Bogotá. Qué pasa 43 días UCR; el cliente respondió después del av — 2026-09-16
_chunk 1844 · 2026-09-16 · fuente: inbox/2026-09-16-rcs-27676-revision-cola.md_

Ticket RCS-27676. Trabajado el 2026-09-16. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Revisión del 16 de septiembre de 2026, 12:57 Bogotá. Qué pasa 43 días UCR; el cliente respondió después del aviso final de julio. Causa Falta evidencia de IP públicas; aviso de julio invalidado. Evidencia https://trebuco.atlassian.net/browse/RCS-27676?focusedCommentId=3269647 Comentarios del ticket consultados en Jira en vivo.

## Rastro
2026-09-16 inbox/2026-09-16-rcs-27676-revision-cola.md

## RCS-27765. La tienda 358 sigue con 773 transacciones el 25/06/2026, medido hoy. El reenvio del cliente si llego y se proc — 2026-09-28
_chunk 1845 · 2026-09-28 · fuente: inbox/2026-09-14-rcs-27765-guia-verificacion.md;2026-09-14-rcs-27765-sql-corregido.md;2026-09-14-rcs-27765.md;2026-09-16-rcs-27765-revision-cola.md;2026-09-24-rcs-27765-seguimiento-ucr.md;2026-09-28-rcs-27765-prioridad-auditoria.md_

Ticket RCS-27765. Trabajado el 2026-09-14 a 2026-09-28. 6 notas en inbox.

## Que pasa
La tienda 358 sigue con 773 transacciones el 25/06/2026, medido hoy. El reenvio del cliente si
llego y se proceso. No contenia el 25 de junio.

## Evidencia
- Conteo hoy en `ARDM_121`, tienda 358: 24/06 = 2,323 · 25/06 = 773 · 26/06 = 2,421. Identico al
  27 jul. Las 773 se cargaron el 26 y 27 jun en 10 lotes `seg_121_<uuid>.zip.pgp`, 468 mas 305.
- Carga diaria del tenant, 8 al 12 sep: 259 a 261 tiendas todos los dias. El 10 sep sube a 339,872
  filas contra ~296,000 de un dia normal. Ese salto es el reenvio.
- `MIN(TradingDay)` de la carga del 10 sep es `2026-07-02`. Los demas dias arrancan en el dia
  anterior. Nada anterior al 2 de julio entro ese dia, asi que el 25/06 no estaba en el lote.

## Que sigue
Juan saco el SQL real con el boton Query. Motor confirmado Snowflake: sintaxis `set var` con `$var`
y `TABLE(SECURE_SQUAREHIERARCHY...)`. No hay CTE de Greenplum.

## Precedentes
- `inbox/2026-09-14-rcs-27765-sql-corregido.md`. El SQL del Composer contaba lineas de item y
  filtraba por `OrigTradingDay`. `inserteddatetime` y `filename` en `ardm_Header` fueron la prueba.
- `brain/markdown/09-appriss-kt-topic-1-data-pipeline-devops.md`. Registra este ticket como el caso
  de aviso de confirmar la ruta antes de afirmarle algo a un cliente.

## Rastro
2026-09-14 inbox/2026-09-14-rcs-27765-guia-verificacion.md
2026-09-14 inbox/2026-09-14-rcs-27765-sql-corregido.md
2026-09-14 inbox/2026-09-14-rcs-27765.md
2026-09-16 inbox/2026-09-16-rcs-27765-revision-cola.md
2026-09-24 inbox/2026-09-24-rcs-27765-seguimiento-ucr.md
2026-09-28 inbox/2026-09-28-rcs-27765-prioridad-auditoria.md

## RCS-27791. Revisión del 16 de septiembre de 2026, 12:57 Bogotá. Qué pasa Aviso de 14 días hoy; no respuesta humana nueva — 2026-09-16
_chunk 1846 · 2026-09-16 · fuente: inbox/2026-09-16-rcs-27791-revision-cola.md_

Ticket RCS-27791. Trabajado el 2026-09-16. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Revisión del 16 de septiembre de 2026, 12:57 Bogotá. Qué pasa Aviso de 14 días hoy; no respuesta humana nueva. Causa Cambios comunicados el 2 sep; validación pendiente. Evidencia https://trebuco.atlassian.net/browse/RCS-27791?focusedCommentId=3348277 Comentarios del ticket consultados en Jira en vivo.

## Rastro
2026-09-16 inbox/2026-09-16-rcs-27791-revision-cola.md

## RCS-27941. Kiran cruzó `incident.Suspect` contra `incident.Shoplifting` y `incident.MasterCase`, y sacó el `CaseType` de — 2026-10-05
_chunk 1847 · 2026-10-05 · fuente: inbox/2026-08-25-rcs-27941-plan-verificacion-escalamiento.md;2026-09-01-rcs-27941-causa-raiz-case-type-security.md;2026-09-16-rcs-27941-revision-cola.md;2026-10-05-mapa-criticidad-clientes.md_

Ticket RCS-27941. Trabajado el 2026-08-25 a 2026-10-05. 4 notas en inbox.

## Causa
Kiran cruzó `incident.Suspect` contra `incident.Shoplifting` y `incident.MasterCase`, y sacó el
`CaseType` de cada Peters. Después abrió Manage Case Type, pestaña Security, en
`apps.apprissretail.com/tailoredbrands/nettrack/Admin/CaseTypeConfig.aspx`.

## Evidencia
El RCA del 28 de julio sostiene dos cosas. Las dos quedan sin respaldo con las capturas nuevas.

**Afirmación 1 del RCA:** "Beverly resolves to Security Level 11 (Corporate User), which does not have
Incident search access", y el nivel 5 Location Manager sí la tiene.

**Lo que muestra la evidencia:** Francesca Ramos tiene Incident Security ID **Location Manager** y su
búsqueda de "Peters" devuelve el mismo "No data to display" que la de Beverly, que está en
**Corporate User**. Dos niveles distintos, el mismo síntoma exacto. El nivel de seguridad no separa el
caso que funciona del que falla. Escalar cargando esta premisa le entrega a Engineering un
diagnóstico ya falsificado.

**Afirmación 2 del RCA:** los claims de Okta re-derivan el nivel 11 en cada login y por eso el DELETE
no persiste.

**Lo que muestra la evidencia:** Colton sacó a Beverly y a Francesca del grupo
TMW-APP-OKTA-SSO-Appriss-EBR-CorporateUser del archivo diario el 13 de agosto. El RCA predice que con
eso el nivel del feed gana. Siete días después Beverly sigue apareciendo como Corporate User en la UI
y la búsqueda sigue vacía. O el cambio del feed no propagó, o el nivel no es la variable que manda.
El caso de Franc

## Que sigue
[2026-08-25] Que la fila faltante **cause** la búsqueda vacía. Es correlación con cuatro casos y cero
contraejemplos, no causalidad demostrada.

| Usuario | Fila en LPUser2 | Búsqueda en Incident |
|---|---|---|
| Dexter Monroe | sí, UserID 22 | funciona |
| Matthew Sincic | sí, no aparece en la lista de colgantes | funciona, su Edit se resolvió |
| Beverly Wright | no | falla |
| Francesca Ramos | no | falla |

Cuatro de cuatro consistentes. Con 267 colgantes y solo tres quejas, la pregunta que falta es por qué
los otros 264 no reclaman. La respuesta probable es que no usan la búsqueda de Incident, y hay que
demostrarlo, no suponerlo.
[2026-09-01] Appriss no define qué roles ven qué tipos de incidente. Tailored Brands sí. Beverly usa Incident para
bajar documentación de casos de empleados para reclamos de desempleo, así que Employee Work Injury y
Refund Fraud encajan con su función. Confirmalo con ellos antes de tocar nada.

Preguntale a Kiran quién aplica el cambio, si el admin del cliente desde esa pantalla o Delivery.

---

## Rastro
2026-08-25 inbox/2026-08-25-rcs-27941-plan-verificacion-escalamiento.md
2026-09-01 inbox/2026-09-01-rcs-27941-causa-raiz-case-type-security.md
2026-09-16 inbox/2026-09-16-rcs-27941-revision-cola.md
2026-10-05 inbox/2026-10-05-mapa-criticidad-clientes.md

## RCS-28008. Verificación directa del 22 sep 2026. Completed, Mauricio Zapata — 2026-09-22
_chunk 1848 · 2026-09-22 · fuente: inbox/2026-09-22-THD-RCS-28008.md_

Ticket RCS-28008. Trabajado el 2026-09-22. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Verificación directa del 22 sep 2026. Completed, Mauricio Zapata. Corey reporta en Carrera 73 14, 00:13 a 02:27, que Transaction ID sigue vacío al cruzar Work View y Secure, pese a la conversión previa a entero. Es un síntoma nuevo que requiere seguimiento propio.

## Rastro
2026-09-22 inbox/2026-09-22-THD-RCS-28008.md

## RCS-28032. Fecha: 2026-08-25 Client ID 433. Estado en Jira: Work in progress, assignee Juan, Medium, labels FromEmail, L1 — 2026-10-09
_chunk 1849 · 2026-10-09 · fuente: inbox/2026-08-25-rcs-28032-cierre-evidencia-y-escalacion.md;2026-10-09-acceso-bastion-nettrack-logs.md_

Ticket RCS-28032. Trabajado el 2026-08-25 a 2026-10-09. 2 notas en inbox.

## Causa
Fecha: 2026-08-25
Client ID 433. Estado en Jira: Work in progress, assignee Juan, Medium, labels FromEmail, L1, Uni_Jul_26_WAFAccess.
Ultimo movimiento del cliente: Joe Austin, 18 ago, con las capturas. Siete dias sin respuesta nuestra.

## Que sigue
`brain/memoria/reference_multidistrito_lhua.md` afirma que un usuario con dos distritos solo ve uno a la vez,
y usa este caso como confirmacion. Hoy no hay evidencia de que Dayna tenga dos distritos asignados, tiene tres
tiendas y las tres estan en el 501. La memoria queda sin respaldo hasta que corra el experimento de la tienda
948. No la borres todavia, marcala como en verificacion.

`brain/memoria/reference_jerarquia_ubicaciones_incident.md` dice que el distrito se hereda del StoreIdent
primario, verificado en cuatro usuarios el 10 de agosto. Esa parte del modelo no la toca la evidencia de hoy.
El ejemplo de Dayna que usa como prueba si queda invalidado.

## Rastro
2026-08-25 inbox/2026-08-25-rcs-28032-cierre-evidencia-y-escalacion.md
2026-10-09 inbox/2026-10-09-acceso-bastion-nettrack-logs.md

## RCS-28240. El clasificador decidia entre pedido y promesa por posicion en el texto: `p_preg > p_prom`. Juan cierra sus co — 2026-09-28
_chunk 1853 · 2026-09-28 · fuente: inbox/2026-09-09-diagnostico-promesa-condicionada-y-nivel-4.md;2026-09-16-rcs-28240-revision-cola.md;2026-09-28-rcs-28240-prioridad-auditoria.md_

Ticket RCS-28240. Trabajado el 2026-09-09 a 2026-09-28. 3 notas en inbox.

## Que pasa
El clasificador decidia entre pedido y promesa por posicion en el texto: `p_preg > p_prom`.
Juan cierra sus comentarios con cortesia, asi que la promesa queda siempre al final y gana.
Los dos tickets subian a PROMESA SIN CUMPLIR con el cliente debiendo datos.

## Evidencia
RCS-28240  p_prom 542  p_preg -1   antes nivel 2, real 3
    RCS-28351  p_prom 308  p_preg -1   antes nivel 2, real 3
    RCS-28342  p_prom -1   p_preg -1   antes nivel 4, real 2
    niveles antes:   2=3 3=5 4=11      exactitud 13/13
    niveles despues: 2=1 3=8 4=10      exactitud 13/13

## Rastro
2026-09-09 inbox/2026-09-09-diagnostico-promesa-condicionada-y-nivel-4.md
2026-09-16 inbox/2026-09-16-rcs-28240-revision-cola.md
2026-09-28 inbox/2026-09-28-rcs-28240-prioridad-auditoria.md

## RCS-28256. Cola del 1 sep 2026, refresco automatico — 2026-09-28
_chunk 1854 · 2026-09-28 · fuente: inbox/2026-09-01-cola.md;2026-09-16-rcs-28256-confirmacion-cliente.md;2026-09-16-rcs-28256-revision-cola.md;2026-09-24-rcs-28256-auditoria-avance.md;2026-09-25-rcs-28256.md;2026-09-28-rcs-28256.md_

Ticket RCS-28256. Trabajado el 2026-09-01 a 2026-09-28. 6 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Comentario nuevo de Colton, 28 sep 2026. Qué pasa Colton pidió el 28 sep 12:54 ET asignar Incident Security ID Location Manager a Paul Bubelnik Jr. La captura del Portal muestra el campo vacío. El ticket sigue en Under Engineering Review con Shandana Khan.

## Rastro
2026-09-01 inbox/2026-09-01-cola.md
2026-09-16 inbox/2026-09-16-rcs-28256-confirmacion-cliente.md
2026-09-16 inbox/2026-09-16-rcs-28256-revision-cola.md
2026-09-24 inbox/2026-09-24-rcs-28256-auditoria-avance.md
2026-09-25 inbox/2026-09-25-rcs-28256.md
2026-09-28 inbox/2026-09-28-rcs-28256.md

## RCS-28282. Revisión del 16 de septiembre de 2026, 12:57 Bogotá. Qué pasa Espera lista de países permitidos; UCR desde 21 — 2026-09-16
_chunk 1856 · 2026-09-16 · fuente: inbox/2026-09-16-rcs-28282-revision-cola.md_

Ticket RCS-28282. Trabajado el 2026-09-16. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Revisión del 16 de septiembre de 2026, 12:57 Bogotá. Qué pasa Espera lista de países permitidos; UCR desde 21 ago. Causa Configuración pendiente de indicación del cliente. Evidencia https://trebuco.atlassian.net/browse/RCS-28282?focusedCommentId=3327262 Comentarios del ticket consultados en Jira en vivo.

## Rastro
2026-09-16 inbox/2026-09-16-rcs-28282-revision-cola.md

## RCS-28289. Arreglo del clasificador de cola, 2026-09-03 — 2026-09-25
_chunk 1857 · 2026-09-25 · fuente: inbox/2026-09-03-fix-clasificador.md;2026-09-16-rcs-28289-revision-cola.md;2026-09-25-rcs-28289-revision-cola.md_

Ticket RCS-28289. Trabajado el 2026-09-03 a 2026-09-25. 3 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Qué pasa Completed desde el 24; Joe confirmó corregido el 23. Causa Cliente confirma corrección; no se reabrió diagnóstico. Evidencia https://trebuco.atlassian.net/browse/RCS-28289?focusedCommentId=3361180 Consulta actual de Jira y comentarios. Qué hago hoy Cerrar manualmente conforme a confirmación y promesa de Juan.

## Rastro
2026-09-03 inbox/2026-09-03-fix-clasificador.md
2026-09-16 inbox/2026-09-16-rcs-28289-revision-cola.md
2026-09-25 inbox/2026-09-25-rcs-28289-revision-cola.md

## RCS-28339. /Users/MancoMenStudio/Downloads/Urban Outfitters - Ticket Review Aug 2026.xlsx. Tickets contains only RCS-2833 — 2026-09-17
_chunk 1859 · 2026-09-17 · fuente: inbox/2026-09-17-RCS-28339-root-cause.md;2026-09-17-UO-excel-long-term-solution.md_

Ticket RCS-28339. Trabajado el 2026-09-17. 2 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
/Users/MancoMenStudio/Downloads/Urban Outfitters - Ticket Review Aug 2026.xlsx. Tickets contains only RCS-28339. Long-term solutions row 5 references all three tickets. missing field values and zero-result asynchronous exports Related Tickets:

## Rastro
2026-09-17 inbox/2026-09-17-RCS-28339-root-cause.md
2026-09-17 inbox/2026-09-17-UO-excel-long-term-solution.md

## RCS-28496. Revisión del 16 de septiembre de 2026, 12:57 Bogotá. Qué pasa Sin información solicitada; UCR desde 20 ago — 2026-09-16
_chunk 1862 · 2026-09-16 · fuente: inbox/2026-09-16-rcs-28496-revision-cola.md_

Ticket RCS-28496. Trabajado el 2026-09-16. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Revisión del 16 de septiembre de 2026, 12:57 Bogotá. Qué pasa Sin información solicitada; UCR desde 20 ago. Causa Diagnóstico pendiente de evidencia del cliente. Evidencia https://trebuco.atlassian.net/browse/RCS-28496?focusedCommentId=3326061 Comentarios del ticket consultados en Jira en vivo.

## Rastro
2026-09-16 inbox/2026-09-16-rcs-28496-revision-cola.md

## RCS-28649. Seis archivos de la hora 16 del 29 de agosto cargaron la cabecera sin el detalle de item ni de tender, y dejar — 2026-09-22
_chunk 1867 · 2026-09-22 · fuente: inbox/2026-09-01-rcs-28649-informe.md;2026-09-01-rcs-28649-instructivo.md;2026-09-21-RCS-28649-precedente.md;2026-09-22-THD-RCS-28649.md_

Ticket RCS-28649. Trabajado el 2026-09-01 a 2026-09-22. 4 notas en inbox.

## Que pasa
Seis archivos de la hora 16 del 29 de agosto cargaron la cabecera sin el detalle de item ni de
tender, y dejaron 878,922 transacciones de THD sin lineas. El ticket lleva desde el 28 de agosto a
las 11:31 sin una respuesta sustantiva de Appriss, solo acuses, y el cliente escalo contando 61
horas. La peticion de recarga nunca salio de RCS: no existe ningun ticket DO ni ENG que referencie
RCS-28649. El remedio es reprocesar el rango con `REBUILD_RANGE`, que escribe en produccion y exige
rol admin, y antes de dispararlo hay que fijar quien lo ejecuta, si duplica lo ya cargado y que
rango recibe.

Version 2 de este informe, 2026-09-01. La evidencia que Juan aporto en siete capturas cambio tres
conclusiones de la version anterior. Ver la seccion de evidencia mas abajo.

## Causa
DO-10275, `085 THD client source data file handling`, Luke Du, creado 2026-04-15, estado Selected
for Development, assignee Flavio Smirne con la cuenta inactiva, cero comentarios, ultima
actualizacion 2026-08-18. Cita textual de la descripcion:

> All clients should have data loading process, especially data file handling with general code
> `appriss_files`. While 085 THD we have its own `files.py` independent to `appriss_files`, even the
> script also use `file_registry` table. But we met issues for the special `files.py` code file.

> 2. When THD changed file name pattern (without `.csv` as part of data file name), the `files.py`
> code file fails. We need to change code file for that. This is done two weeks ago.

> 3. Today on-call person (@Jenny Wang who is the original designer) found another issue: the
> `files.py` use special file path and file name and combine them for copying. Somehow today the
> file path and the file name are not matching. We need to change `files.py` again.

Y el diseno que propone Luke, todavia sin implementar:

> 4. If all files in the list already registered in `file_registry` table, we copy these files to
> DLZ; set `ingested_flg=1` for this `MARKER

## Evidencia
Consulta `text ~ "RCS-28649" AND project != RCS`. Cero resultados. Consulta de tickets DO y ENG
creados desde el 28 de agosto, filtrada por THD, carga, archivos y detalle. Cero resultados
relacionados con este incidente. Los unicos DO y ENG de THD activos son de Passport, dashboards de
Canada, claims y la migracion SnowTime.

**La peticion de recarga nunca se convirtio en trabajo asignable.** Vive solo como texto en un
comentario de RCS.

## Impacto
El impacto lo escribio el cliente: todos los investigadores de THD. Un investigador que abre una
transaccion sin detalle de item ni de tender no puede sustentar un caso. THD opera en US y Canada
sobre el mismo tenant, y las dos divisiones estan en el ticket.

El riesgo de proceso pesa mas que el tecnico ahora mismo. El cliente conto las horas en voz alta y
escalo. La escalacion vino sin trabajo de fondo detras, porque el ticket no tiene una sola nota de
investigacion escrita desde el 28 de agosto. Repetimos el patron que Aimee corrigio el 13 de agosto
en cuatro tickets: la investigacion nunca llego al ticket, asi que el ticket no avanza.

Riesgo secundario. Cuanto mas se demore la recarga, mas dias de trading quedan con discrepancia
acumulada en el reporte del cliente, y mas grande se vuelve el lote a recargar.

## Que sigue
El remedio identificado es reprocesar el 29 de agosto para que el pipeline vuelva a insertar las
lineas de item y tender que no llegaron a la tabla final. Juan verifico que el dato crudo existe.
El procedimiento es `REBUILD_RANGE`, escribe en produccion y exige rol admin.

Tres cosas quedan por resolver antes de ejecutarlo, y ninguna es opcional.

**Quien tiene el rol admin.** Si Juan no lo tiene, el escalamiento sigue en pie y el destinatario
cambia segun quien ejecute el procedimiento. La regla de
`brain/memoria/reference_escalacion_l3_procedimiento.md` manda dato o configuracion ya en produccion
a Delivery, que para Secure 5 va a Peyman Motlagh con el Sprint `RCS Support Team`. Un procedimiento
almacenado que reescribe tablas de produccion tambien encaja en Database Services, transicion 591,
disponible sobre este ticket y ausente del flujo escrito. Pregunta antes de mover.

**Que hace `REBUILD_RANGE` con las cabeceras que ya estan.** El cerebro no tiene una sola linea
sobre este procedimiento. Nadie documento si borra y reconstruye el rango o si inserta encima. Si
inserta encima, 878,922 transacciones duplicadas convierten un ticket escalado en un incidente
mayor. Exige la respu

## Precedentes
No existe flujo escrito para recargar archivos de transacciones POS. El cerebro lo declara como
hueco en `inbox/2026-08-28-rcs-28621-quien-carga-el-archivo.md`: "No existe flujo en `flujos/` para
'import attached file'". El unico runbook de carga manual que existe cubre archivos de employee y
location para Incident con LPImport, no transacciones.

El precedente real mas cercano es RCS-28581 y DO-9495, en
`inbox/2026-08-31-rcs-28581-cwh-pos-number-regresion.md`:

> Bartosz recargo a mano el archivo c248_rawdata_postransactions/2026/02/17/17/data_6_5_0.json.gz
> para materializar el fix.

Dos cosas que se sacan de ahi. La particion es `cliente/anio/mes/dia/hora/`, que es exactamente el
nivel de granularidad que pide THD. Y quien ejecuto fue ingenieria, no soporte. Existe ademas un
estado de Jira llamado `Reload Required`, que ese mismo ticket recorrio.

Precedente de recibos que no renderizan por hueco de dato y no por defecto del visor: RCS-27140 de
Alo Yoga, en `brain/markdown/16-rcs-soluciones.md`, donde `image_url` nulo en
`ardm_Item.extra_fields` dejaba al visor sin renderizar. Confirma el patron de que el visor de
recibos falla hacia abajo cuando el dato no esta.

## Rastro
2026-09-01 inbox/2026-09-01-rcs-28649-informe.md
2026-09-01 inbox/2026-09-01-rcs-28649-instructivo.md
2026-09-21 inbox/2026-09-21-RCS-28649-precedente.md
2026-09-22 inbox/2026-09-22-THD-RCS-28649.md

## RCS-28678. URBN reporta conteos de items que no coinciden entre Ejournal y Appriss en tres transacciones desde el 19 de a — 2026-09-22
_chunk 1870 · 2026-09-22 · fuente: inbox/2026-09-22-rcs-28678.md_

Ticket RCS-28678. Trabajado el 2026-09-22. 1 notas en inbox.

## Que pasa
URBN reporta conteos de items que no coinciden entre Ejournal y Appriss en tres transacciones desde el 19 de agosto. El reportero dice que no puede completar sus investigaciones de perdida por esto y que esta perdiendo confianza en los datos de Appriss. El ticket lleva 22 dias abierto. Sigue en Work in progress, prioridad Medium, sin escalar a L3.

## Evidencia
Interno 3338626, 11 sep: "confirmed ingestion-layer data loss... not a display/rendering bug".
Interno 3359863, 22 sep: "Data ingestion is not at fault... defect is in transaction-detail rendering/counting logic".
Cliente 3359872, 22 sep: generaliza a "every discrepancy you've flagged", sin verificar.

## Precedentes
RCS-28649 Home Depot, item/tender detail faltante por task de Snowflake suspendida durante backfill. Prioridad High, estado Escalated. confluence/RTS-triage/RCS-28649-home-depot-item-tender-detail-missing.md

## Rastro
2026-09-22 inbox/2026-09-22-rcs-28678.md

## RCS-28799. Consulta directa del 22 sep 2026. Under Engineering Review, Mohammed Mutahhar — 2026-09-22
_chunk 1875 · 2026-09-22 · fuente: inbox/2026-09-21-RCS-28799-rendimiento.md;2026-09-22-THD-RCS-28799.md_

Ticket RCS-28799. Trabajado el 2026-09-21 a 2026-09-22. 2 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Consulta directa del 22 sep 2026. Under Engineering Review, Mohammed Mutahhar. ENG-8650, Gabor Remenyi, está Development Complete; versión Secure September 2026 Release 2/2 del 24 sep, released=false. consultas sin optimizar y falta de enforcement del timeout de una hora documentadas.

## Rastro
2026-09-21 inbox/2026-09-21-RCS-28799-rendimiento.md
2026-09-22 inbox/2026-09-22-THD-RCS-28799.md

## RCS-28871. Walgreens pidio el 10 sep, via cuestionario Peak Season Readiness: certificados que expiren antes de medio ene — 2026-09-28
_chunk 1877 · 2026-09-28 · fuente: inbox/2026-09-15-rcs-28871.md;2026-09-16-rcs-28871-revision-cola.md;2026-09-24-rcs-28871-seguimiento-ucr.md;2026-09-24-rcs-28871-stress-testing-contacto.md;2026-09-28-rcs-28871-prioridad-auditoria.md_

Ticket RCS-28871. Trabajado el 2026-09-15 a 2026-09-28. 5 notas en inbox.

## Que pasa
Walgreens pidio el 10 sep, via cuestionario Peak Season Readiness: certificados que expiren antes
de medio enero 2027, deployments nov-dic 2026, si hubo stress testing y si el sistema soporta
auto-scaling, y el contact list/escalation matrix. Juan tomo el ticket ese dia y prometio respuesta;
van 3 dias sin contestar. Jira: Work in progress, assignee Juan.

## Evidencia
- RCS-27847 Samsung, 15-jul: "soporte NO tiene los datos del cuestionario (load tests, trafico,
  scale-up, rate limits, timeouts, fallback/RTO, code freeze) -> los tiene Infraestructura"
  (brain/markdown/21-kt-kristin-sign-off-procesos-rts.md L54).
- Matriz: Infrastructure -> Under Infrastructure Review, assignee se queda Juan, auto-crea RTAILIT
  (brain/memoria/reference_escalacion_l3_procedimiento.md).
- Infra: Russell Harmon, horario Pacifico, mismo patron en Kohl's RCS-27840 (mismo doc, L180 y
  L1073). CSM Walgreens: Paul Marderosian, Client Contacts.xlsx pestaña 209 fila 282.

## Precedentes
- RCS-27847 Samsung, cuestionario identico: tickets/RCS-27847.md
- RCS-27840 Kohl's, mismo ruteo a Infra con deadline: 21-kt-kristin-sign-off-procesos-rts.md L180

## Rastro
2026-09-15 inbox/2026-09-15-rcs-28871.md
2026-09-16 inbox/2026-09-16-rcs-28871-revision-cola.md
2026-09-24 inbox/2026-09-24-rcs-28871-seguimiento-ucr.md
2026-09-24 inbox/2026-09-24-rcs-28871-stress-testing-contacto.md
2026-09-28 inbox/2026-09-28-rcs-28871-prioridad-auditoria.md

## RCS-28881. Diez de los catorce formularios del template ANNUAL OPS/SERVICES REVIEW no abren para NEXCOM. La pantalla qued — 2026-10-08
_chunk 1879 · 2026-10-08 · fuente: inbox/2026-09-11-rcs-28881.md;2026-09-14-apis-accesos-y-hallazgo-jcrew-prep.md;2026-09-14-rcs-28881-ping-megha.md;2026-09-14-rcs-28881.md;2026-09-16-rcs-28881-revision-cola.md;2026-09-21-rcs-28881.md;2026-09-22-tecnica-frameset-oculto-apis.md;2026-09-24-rcs-28881-auditoria-avance.md;2026-09-28-rcs-28881-guion-llamada-grabacion-en.md;2026-09-28-rcs-28881-guion-llamada-grabacion.md;2026-09-28-rcs-28881-gu_

Ticket RCS-28881. Trabajado el 2026-09-11 a 2026-10-08. 16 notas en inbox.

## Que pasa
[2026-09-14] Carlo Conty y dos usuarios mas de NEXCOM no pueden abrir en edicion el template de audit
Annual Ops/Services Review en APIS prod. Panel de contenido vacio. Under Support Review,
Medium, Megha Rathi, sin comentarios de ella desde el 10 sep.
[2026-09-21] Diez de los catorce formularios del template ANNUAL OPS/SERVICES REVIEW no abren para NEXCOM.
La pantalla queda en blanco y el navegador se cuelga entre 8 y 10 minutos. Work in progress,
Medium, assignee Juan desde el 15 sep. El cliente lleva cinco dias esperando respuesta.

## Evidencia
[2026-09-14] - Probado el 14 sep en nexcom-prep con la cuenta jbarber. Abren bien el Audit Center, el audit
  14-HIA-0001-25, la pestaña Audit admin y el Template editor AT1000000106 de OPS Review
  Administration, codigo OPSA, con sus pestañas, Forms y Change History. El modulo de Audit
  del tenant rinde.
- El Template editor carga en la seccion Forms una referencia a un formulario por ID, en el
  caso probado `OPS Review - Administration( ID:361 )`. Ese es el punto de fallo candidato.
- En las cuatro pantallas de Audit de prep salen claves de screen label sin resolver:
  `Audit.status.1`, `Audit.date due`, `Letter.actions`, `Form status.0`, `Template deleted.0`,
  `Audit.template code`, `Audit score category.secondary category`. La capa de etiquetas de
  este tenant esta degradada. Mismo patron que RCS-28032 en Vitamin Shoppe.
- Annual Ops/Services Review no existe en prep. Sin templates ocultos: destildar
  "Hide expired/deleted templates" no revelo ninguno.
[2026-09-21] - Carlo Conty, 16 sep: "The page sits blank as soon as I click the audit and it takes about 8-10
  minutes for the This Page Isn't Responding prompt to pop up". Eso es el hilo del navegador
  bloqueado, no un timeout de borde que devuelve error.
- Captura del 16 sep: host `whqapisiis01.nexad.nexweb.us`, ruta `/apis270/`, titulo NEXCOM-270.
  El tenant corre la UI **270**, no 275. Confluence Modules by Client dice 275 y esta obsoleta,
  ultima modificacion sep 2019.
- Verificado por Juan el 14 sep en nexcom-prep: Audit Center, un audit y el template editor
  AT1000000106 abren. El modulo de Audit del tenant esta sano.

## Precedentes
[2026-09-14] - RCS-28032 Vitamin Shoppe, NewAudit.aspx y AuditLog.aspx con Screen Labels sin resolver.
  `bitacora/RCS-28032.md`.
- RCS-28139 Sportsman's, audit screens inaccesibles, BuildAllScreens sincrono contra el timeout
  de 100s. Secure, no APIS.
- RCS-28709 Stater Bros, blank screen sin causa confirmada ni ENG.
- RCS-28449 Meijer, Secure not loading, restaurado en 47 min el 18 ago. Otro producto y otro
  hosting. La comparacion de Shannon Clark no aplica.
- Nota de Cerebro sobre `GetScreenLabelByFormField`, cientos de llamadas a base por recurso sin
  cache, PR 55972, marcada como causa candidata de pantallas que no cargan. Encaja con los
  labels crudos vistos hoy. Sin confirmar.
[2026-09-21] - RCS-28139 Sportsman's, BuildAllScreens sincrono contra el timeout de 100s. Descartado aqui, la
  pantalla aguanta 8 a 10 minutos sin devolver error.
- RCS-28852 Rack Room, StartAudit=10. Descartado, Carlo es admin.
- RCS-28032 Vitamin Shoppe, Screen Labels sin resolver. Mismo patron visto en prep, sin confirmar
  que sea la causa aqui.
- RCS-28212, Viraj el 18 ago: todo APIS va directo a Matt Kamminga.

## Rastro
2026-09-11 inbox/2026-09-11-rcs-28881.md
2026-09-14 inbox/2026-09-14-apis-accesos-y-hallazgo-jcrew-prep.md
2026-09-14 inbox/2026-09-14-rcs-28881-ping-megha.md
2026-09-14 inbox/2026-09-14-rcs-28881.md
2026-09-16 inbox/2026-09-16-rcs-28881-revision-cola.md
2026-09-21 inbox/2026-09-21-rcs-28881.md
2026-09-22 inbox/2026-09-22-tecnica-frameset-oculto-apis.md
2026-09-24 inbox/2026-09-24-rcs-28881-auditoria-avance.md
2026-09-28 inbox/2026-09-28-rcs-28881-guion-llamada-grabacion-en.md
2026-09-28 inbox/2026-09-28-rcs-28881-guion-llamada-grabacion.md
2026-09-28 inbox/2026-09-28-rcs-28881-guion-llamada-verbatim-en.md
2026-09-28 inbox/2026-09-28-rcs-28881-prioridad-auditoria.md
2026-10-04 inbox/2026-10-04-rcs-28881-correccion-ruta-escalacion.md
2026-10-06 inbox/2026-10-06-tempo-worklogs-octubre.md
2026-10-08 inbox/2026-10-08-rcs-28881-guion-intro-llamada-en.md
2026-10-08 inbox/2026-10-08-rcs-28881-guion-intro-llamada-es.md

## RCS-28910. D23 generado y reconfirmado contra Jira — 2026-09-17
_chunk 1880 · 2026-09-17 · fuente: inbox/2026-09-17-d23-generado.md_

Ticket RCS-28910. Trabajado el 2026-09-17. 1 notas en inbox.

## Que sigue
Se le agrego una frase a la columna I diciendo que el item que venia de RCS-28910 continua ahi. No
se toco la fecha de la columna G, que sigue en 9/9, porque en el hilo de RCS-28683 no hubo
actividad. La actividad fue en RCS-28910. Si prefieres que la fila no diga nada hasta que se mueva
su propio hilo, se quita en un minuto.

## Rastro
2026-09-17 inbox/2026-09-17-d23-generado.md

## RCS-28915. Michaela Rodacker (client 382, goodwillsacto) no recibe Smart Alerts desde el 8/31. Megha marco su causa como — 2026-10-13
_chunk 1881 · 2026-10-13 · fuente: inbox/2026-10-07-rcs-28915.md;2026-10-13-ithd-acceso-rdp-servidores-lpms.md_

Ticket RCS-28915. Trabajado el 2026-10-07 a 2026-10-13. 2 notas en inbox.

## Que pasa
Michaela Rodacker (client 382, goodwillsacto) no recibe Smart Alerts desde el 8/31. Megha marco su causa como CONFIRMED por los pasos Classic y Special en blanco del tracker.

## Evidencia
1. Debug 08.31: caso 10609 Employee Accident, 17:43:41 UTC, Runquery SELECT completo, EMAIL SENT. Es la ultima corrida buena.
2. Debug 09.01: caso 10612 Critical Incident, 00:59:35 UTC, Runquery solo WHERE, warning 16 de sintaxis. Igual en 10613 a 10615 (9/1), 10652, 10813, 10839 (10/6) y 10841, 10842, 10846 (10/7). Los error log lo repiten.
3. Los casos 10610 y 10611 no tenian alerta aplicable, la ventana queda entre 8/31 17:44 y 9/1 00:59 UTC. El legacy GoodwillSacto conserva el SELECT original.

## Precedentes
RCS-27407 PPG, ManageSmartAlerts.aspx no regenera Filters ni FiltersSQL, inbox/2026-09-04-rcs-27407-instructivo.md

## Rastro
2026-10-07 inbox/2026-10-07-rcs-28915.md
2026-10-13 inbox/2026-10-13-ithd-acceso-rdp-servidores-lpms.md

## RCS-28951. Se cruzarán el historial completo, los enlaces del ticket, Confluence y precedentes de Cerebro. Jira se mantie — 2026-09-16
_chunk 1882 · 2026-09-16 · fuente: inbox/2026-09-16-rcs-28951.md_

Ticket RCS-28951. Trabajado el 2026-09-16. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Se cruzarán el historial completo, los enlaces del ticket, Confluence y precedentes de Cerebro. Jira se mantiene en solo lectura.

## Rastro
2026-09-16 inbox/2026-09-16-rcs-28951.md

## RCS-28959. Reparto de Supp Backlog, 16 sep 2026 — 2026-09-16
_chunk 1883 · 2026-09-16 · fuente: inbox/2026-09-16-supp-backlog-asignacion.md_

Ticket RCS-28959. Trabajado el 2026-09-16. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Cola Support Backlog Unassigned 82, 8 tickets. project RCS, statusCategory distinto de Done. Jira quedó en solo lectura. | Persona | Abiertos | UCR | Carga activa sin UCR | Límite | |---|---:|---:|---:|---:| | Sebastian Rueda | 20 | 2 | 18 | 20 | | Edwin Garzon | 19 | 6 | 13 | 20 | | Diego Buelvas | 15 | 7 | 8 | 20 | | Sebastian Garces | 7 | 4 | 3 | 10 a 12 | | Enrique Jimenez | 5 | 2 | 3 | 10 a 12 | | Luis Hernandez | 8 | 2 | 6 | 10 a 12 | | Persona | Tickets | Queda en | |---|---|---:| | Diego Buelvas | RCS-28959 Lululemon, recibos sin autorización de Engage; RCS-28952 TJX, Verify Header Fie

## Rastro
2026-09-16 inbox/2026-09-16-supp-backlog-asignacion.md

## RCS-28968. Verificado en Jira el 22 sep 2026: Under Customer Review, Bikash Kumar — 2026-09-22
_chunk 1884 · 2026-09-22 · fuente: inbox/2026-09-21-RCS-28968-actualizacion.md;2026-09-22-THD-RCS-28968.md_

Ticket RCS-28968. Trabajado el 2026-09-21 a 2026-09-22. 2 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Verificado en Jira el 22 sep 2026: Under Customer Review, Bikash Kumar. importe derivado discrepante con recibos completos. En llamada Matthew añade Total Item Quantity desactualizado.

## Rastro
2026-09-21 inbox/2026-09-21-RCS-28968-actualizacion.md
2026-09-22 inbox/2026-09-22-THD-RCS-28968.md

## RCS-28992. RCS-28992 ICA, Duplication records — 2026-10-05
_chunk 1886 · 2026-10-05 · fuente: inbox/2026-09-18-correccion-ica-163-snowflake.md;2026-09-24-chat-original-guia-gpg.md;2026-10-05-rcs-28992.md_

Ticket RCS-28992. Trabajado el 2026-09-18 a 2026-10-05. 3 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Peter Just pidió el 18 sep revisar el dato crudo de la transacción 2609179959263358647 de ICA, por registros con varios tenders. El ticket sigue en Work in progress con Enrique Jimenez. Enrique no comenta desde el 18 sep. Shaun Callow pidió update el 5 oct y Viraj Kansara preguntó en Teams si ya se subió al equipo SnowTime.

## Rastro
2026-09-18 inbox/2026-09-18-correccion-ica-163-snowflake.md
2026-09-24 inbox/2026-09-24-chat-original-guia-gpg.md
2026-10-05 inbox/2026-10-05-rcs-28992.md

## RCS-28997. RCS-28997 reporta que Store 449 de FinishLine no puede ingresar singles info en el sistema. El ticket esta en — 2026-09-22
_chunk 1887 · 2026-09-22 · fuente: inbox/2026-09-18-rcs-28997-finish-line-client-ids-prod-staging.md;2026-09-22-rcs-28997-singles-info.md_

Ticket RCS-28997. Trabajado el 2026-09-18 a 2026-09-22. 2 notas en inbox.

## Que pasa
RCS-28997 reporta que Store 449 de FinishLine no puede ingresar singles info en el sistema. El ticket esta en Work in progress desde el 18 sep 2026, asignado a Enrique Jimenez, sin adjuntos ni mensaje de error registrado.

## Evidencia
getJiraIssue RCS-28997, campo description completo. "Store 449 is not able to enter singles information into the system." Sin adjuntos. Dos comentarios de plantilla, 18 sep 11:32 y 12:55.
bin/buscar "singles" y "SinglesInfo" contra brain/markdown, memorias, tickets y confluence/RTS-triage. Cero coincidencias.
inbox/2026-09-18-rcs-28997-finish-line-client-ids-prod-staging.md, nota propia sobre este mismo ticket. Deja pendiente confirmar si Store 449 pertenece al client 375 FLP o al 376 FIN.

## Precedentes
tickets/RCS-28701.md, misma pareja de client IDs 375 y 376 de Finish Line, sin resolver a que tienda pertenece cada uno.
inbox/2026-09-18-rcs-28997-finish-line-client-ids-prod-staging.md, nota propia sobre Prod vs Staging para este ticket.

## Rastro
2026-09-18 inbox/2026-09-18-rcs-28997-finish-line-client-ids-prod-staging.md
2026-09-22 inbox/2026-09-22-rcs-28997-singles-info.md

## RCS-29000. D25 generado y reconfirmado contra Jira — 2026-09-21
_chunk 1888 · 2026-09-21 · fuente: inbox/2026-09-21-d25-generado.md_

Ticket RCS-29000. Trabajado el 2026-09-21. 1 notas en inbox.

## Que sigue
RCS-29026 sin asignar. Es el mas urgente de la lista, alerta que no disparo en un caso de perdida
grande, y con la pregunta abierta de si hay mas casos silenciosos.
RCS-29000 con Shandana Khan en ingenieria.
RCS-28824 con Sebastian Rueda y el equipo de datos, cashier profile y area map, cuatro dias quieto.
RCS-28281 con el reloj de auto cierre corriendo.
RCS-28683 con Kamminga, doce dias sin movimiento propio.
RCS-28667 con Kamminga, dieciocho dias sin movimiento propio. Sigue siendo el mas frio de la lista.
RCS-28589 en Ready for Test del lado de ingenieria, segun el espejo del 9/21.

## Rastro
2026-09-21 inbox/2026-09-21-d25-generado.md

## RCS-29021. HATR Scheduled Tasks y Durable Functions Monitor, rutas en USPROD — 2026-10-09
_chunk 1889 · 2026-10-09 · fuente: inbox/2026-10-09-hatr-autorecuperacion.md;2026-10-09-hatr-scheduled-tasks-rutas.md_

Ticket RCS-29021. Trabajado el 2026-10-09. 2 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Verificado por Juan el 9 oct 2026 con su usuario. Scheduled Tasks por cliente: https://usprod.apprissretailcloud.com/control/#/hatr/scheduled Menu lateral, seccion Hatr: Hatr Stats, Hatr Scheduled Tasks, Hatr Trigger Task, Hatr Lock Diagnostics, Monitor.

## Rastro
2026-10-09 inbox/2026-10-09-hatr-autorecuperacion.md
2026-10-09 inbox/2026-10-09-hatr-scheduled-tasks-rutas.md

## RCS-29023. RCS-29023. Proceso para escalar a Infraestructura un bloqueo de Cloudflare — 2026-09-21
_chunk 1890 · 2026-09-21 · fuente: inbox/2026-09-21-rcs-29023-proceso-infra-bloqueo-cloudflare.md_

Ticket RCS-29023. Trabajado el 2026-09-21. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Pregunta de Juan sobre el proceso con Infra para RCS-29023, 3Sixty Duty Free. No hay ficha ni bitacora de este ticket todavia en Cerebro, es nuevo de hoy. RCS-29023, https://trebuco.atlassian.net/browse/RCS-29023. Reporter Jose Montenegro, 3Sixty Duty Free.

## Rastro
2026-09-21 inbox/2026-09-21-rcs-29023-proceso-infra-bloqueo-cloudflare.md

## RCS-29037. Chris Angelica confirmo por correo del 24 sep 10:44 que todas las integraciones externas de Claire's estan cai — 2026-09-24
_chunk 1892 · 2026-09-24 · fuente: inbox/2026-09-21-feedback-internal-note-md-lado.md;2026-09-21-rcs-29037.md;2026-09-24-rcs-29037-shreyas.md;2026-09-24-rcs-29037.md_

Ticket RCS-29037. Trabajado el 2026-09-21 a 2026-09-24. 4 notas en inbox.

## Que pasa
[2026-09-21] Claire's (client 439) tiene VPN caida desde el sabado. Se corto la transmision API a
c439_rawdata_postransactions. El cliente pregunta en RTS-207993 si basta con que la transmision
regular se reanude o si hace falta un archivo historico. RCS-29037 quedo Under Support Review,
asignado a Juan, sin dueno de Engineering todavia.
[2026-09-24] Chris Angelica confirmo por correo del 24 sep 10:44 que todas las integraciones externas de Claire's estan caidas desde el sabado 19 sep, sin ETA. Shreyas Amai lo subio al ticket, que sigue Under Support Review y asignado a Juan.

## Evidencia
[2026-09-21] RCS-28170, TJX, mismo tipo de feed postransactions via API. Trading day 04 ago quedo en 200408
contra minimo 1700000, se saltaron 23 definiciones. Al reanudar el 05 ago el volumen se
normalizo solo, sin archivo historico aparte.
SLA Rules 9.5, brain/markdown/13-appriss-onboarding-base-de-conocimiento.md linea 685. Archivo con
File Source Gateway va a Engineering, product type RTIaaS, Support no investiga por cuenta propia.
RCS-28618/RCS-28620, Walmart INKIRU, pregunta identica de backfill lleva meses sin cerrar.
[2026-09-24] Correo de Chris Angelica, 24 sep 10:44, adjuntos/RCS-29037/image-20260924-210107.png. Dice: offline desde el 19 sep, sin ETA, contactara a cada partner para acordar si la transmision solo se enciende, si hay historicos y otros temas.
Comentario 3363154 de Shreyas Amai, 24 sep 17:01, pide recomendaciones de recuperacion para Claire's.
Estado Jira 24 sep: Under Support Review. El comentario 3359297 del 21 sep anuncia el paso a Engineering por SLA 9.5 y el estado no cambio.

## Precedentes
[2026-09-21] RCS-28170, confluence/RTS-triage/RCS-28170-tjx-no-work-items-populated.md, feed API resumido sin
catch-up file, Work Items saltados solo el dia de volumen bajo.
investigaciones/ingestion-api-como-entra-la-data.md, mecanismo del Ingestion API.
tickets/RCS-28620.md, advertencia de backfill sin resolver, mismo tipo de pregunta.
[2026-09-24] RCS-28170 TJX, feed API reanudado sin archivo historico, confluence/RTS-triage/RCS-28170-tjx-no-work-items-populated.md.
tickets/RCS-28620.md, pregunta identica de backfill sin cerrar.
Entregable previo inbox/2026-09-21-rcs-29037.md.

## Rastro
2026-09-21 inbox/2026-09-21-feedback-internal-note-md-lado.md
2026-09-21 inbox/2026-09-21-rcs-29037.md
2026-09-24 inbox/2026-09-24-rcs-29037-shreyas.md
2026-09-24 inbox/2026-09-24-rcs-29037.md

## RCS-29053. Vito lee cashier 0 como duplicado de los faltantes en su reporte Composer. La respuesta del 22 sep le dijo que — 2026-09-25
_chunk 1894 · 2026-09-25 · fuente: inbox/2026-09-22-backlog-sin-asignar-candidatos.md;2026-09-22-rcs-29053.md;2026-09-24-rcs-29053.md;2026-09-25-rcs-29053-revision-cola.md_

Ticket RCS-29053. Trabajado el 2026-09-22 a 2026-09-25. 4 notas en inbox.

## Que pasa
[2026-09-22] Vito Zona pregunta que representa cashier 0 en el Over Short Data Area, que segun el aparece sumado al total del dia, y si hace falta para el dataset. No pide cambio.
[2026-09-24] Vito lee cashier 0 como duplicado de los faltantes en su reporte Composer. La respuesta del 22 sep le dijo que cashier 0 traia cero dolares y eso es incorrecto. Cliente esperando desde el 23 sep 07:59 ET.

## Evidencia
[2026-09-22] - ardm_171.overshort_registeractivity, tienda 80, 21 sep 2026: 36 filas con cashierno = '0', una por cada posno activo de la tienda ese dia. Las 36 traen totalnumberoftransactions = 1, totalotherdrawopeningcount = 1, totalcashtenderamount = 0, totalcashbackamount = 0, totalchangeamount = 0. Query y resultado completo en la sesion de DBeaver del 22 sep.
- ardm_171.reference_overshortcustomreport no aplica a esta pregunta. Trae cashierno reales de siete digitos, es configuracion de reporte por empleado, no la fuente del cajero 0.
- Sin precedente en la base para este dataset, primera vez que se documenta.
[2026-09-24] - GP6 ardm_171, Q2, tienda 73, 91 dias: cashier0 1 cajero, 91 dias, -837.62. Igual al total de Q1. Cajeros reales 247, -2374.18, 2.8 veces el total.
- Q3, 23 sep, posno 13: 0.11 repetido en cashier 0 y cuatro cajeros. posno 17: -0.65 en cashier 0 y cinco cajeros.
- overshort_dailyreconciliation no tiene cashierno. Consultas en inbox/2026-09-24-rcs-29053-queries.sql.

## Precedentes
[2026-09-22] Ninguno en la base. Hallazgo nuevo, candidato a subir a investigaciones/ como referencia de la familia Over/Short.
[2026-09-24] Ninguno en la base ni en confluence/RTS-triage. KT 17 jun 2026, brain/markdown/10-appriss-kt-topic-1-dashboards-metricas.md, describe la correlacion registradora a cajero. Candidato a investigaciones/RCS-29053-overshort-cashier0.md.

## Rastro
2026-09-22 inbox/2026-09-22-backlog-sin-asignar-candidatos.md
2026-09-22 inbox/2026-09-22-rcs-29053.md
2026-09-24 inbox/2026-09-24-rcs-29053.md
2026-09-25 inbox/2026-09-25-rcs-29053-revision-cola.md

## RCS-29054. Nancy Barajas pide actualizar la alineacion de distrito y LP para varias tiendas. Adjunta el xlsx "District & — 2026-10-06
_chunk 1895 · 2026-10-06 · fuente: inbox/2026-09-22-rcs-29054.md;2026-09-28-rcs-29054-prioridad-auditoria.md;2026-10-02-rcs-29054-confirmacion-llamada.md;2026-10-06-rcs-29054-conclusion-llamada.md;2026-10-06-rcs-29054-guion-llamada-big5.md;2026-10-06-rcs-29054-por-que-llamada.md_

Ticket RCS-29054. Trabajado el 2026-09-22 a 2026-10-06. 6 notas en inbox.

## Que pasa
Nancy Barajas pide actualizar la alineacion de distrito y LP para varias tiendas. Adjunta el xlsx "District & LP Alignment for Appriss and ThinkLP".

## Evidencia
- Peyman Motlagh, Teams, 22 sep: "We should never accept any modification to the reference location table via RCS tickets so if I were you, I would tell the client to make these changes in their location file that they sent us and it would automatically go into our reference location table."
- RCS-8330, ficha de onboarding Big 5: el cliente envia tres archivos de referencia a diario junto con el POS, Store, Employee, Item/Merchandise, mas un T2 File. El archivo Store es el candidato para este cambio.
- Confirmado antes en Control Panel: hierarchyId 1 en la URL de Location Hierarchies, canonica, no editable desde el tenant.

## Precedentes
RCS-8330 Big 5 Sporting Goods, ficha de onboarding con el detalle de los feeds diarios, https://trebuco.atlassian.net/browse/RCS-8330

## Rastro
2026-09-22 inbox/2026-09-22-rcs-29054.md
2026-09-28 inbox/2026-09-28-rcs-29054-prioridad-auditoria.md
2026-10-02 inbox/2026-10-02-rcs-29054-confirmacion-llamada.md
2026-10-06 inbox/2026-10-06-rcs-29054-conclusion-llamada.md
2026-10-06 inbox/2026-10-06-rcs-29054-guion-llamada-big5.md
2026-10-06 inbox/2026-10-06-rcs-29054-por-que-llamada.md

## RCS-29055. Kohl's reporta un idle timer nuevo que los saca de Secure en minutos y les hace perder el trabajo. Piden 60 mi — 2026-09-28
_chunk 1896 · 2026-09-28 · fuente: inbox/2026-09-28-rcs-29055.md_

Ticket RCS-29055. Trabajado el 2026-09-28. 1 notas en inbox.

## Que pasa
Kohl's reporta un idle timer nuevo que los saca de Secure en minutos y les hace perder el trabajo. Piden 60 minutos o quitarlo. Work in progress, assignee Enrique Jimenez, Kyle insistio el 28 sep.

## Evidencia
1. Descripcion de Kyle Kimmerly, 22 sep: "new idle timer", "not documented in the release notes".
2. ENG-7184: el timeout sale de COALESCE(NULLIF(CustomerEditedValue,''), Value) por ClientID, default 60. inbox/2026-08-27-rcs-28153-verificacion-tenant.md
3. Cerebro no tiene una regla escrita de quien aprueba cambiar un config item. Solo la regla de ruteo: configuracion en produccion a Delivery, cambio facturable al CSM. brain/memoria/reference_escalacion_l3_procedimiento.md

## Precedentes
RCS-28153 Big Y, timeout de 240 pedido por el cliente, tickets/RCS-28153.md
RCS-28346 Stater Bros, sesion expirando antes del valor configurado, tickets/RCS-28346.md
Unificacion, timeout 300 a 30 es decision de producto, brain/memoria/reference_unificacion_patrones.md

## Rastro
2026-09-28 inbox/2026-09-28-rcs-29055.md

## RCS-29083. Del 9/21 9:00 PM al 9/25 7:20 PM no salio ningun archivo de claims WC ni GL. Ryan Barlow envio el 9/25 un arch — 2026-09-26
_chunk 1899 · 2026-09-26 · fuente: inbox/2026-09-25-rcs-29083.md;2026-09-26-rcs-29083.md_

Ticket RCS-29083. Trabajado el 2026-09-25 a 2026-09-26. 2 notas en inbox.

## Que pasa
[2026-09-25] Desde el 21 sep ningun claim WC ni GL de 7-Eleven llega a los TPAs. Jira 25 sep: Work in progress, High, assignee Megha Rathi, RETAILIT-20890 con Russell Harmon consultando a Ryan Barlow. John Smithson pide estimado para el equipo de Risk.
[2026-09-26] Del 9/21 9:00 PM al 9/25 7:20 PM no salio ningun archivo de claims WC ni GL. Ryan Barlow envio el 9/25 un archivo con 95 registros y sigue investigando. Jira: Work in progress, assignee Ryan Barlow.

## Evidencia
[2026-09-25] 1. Ryan Barlow, RCS-29083, 24 sep 14:32 ET: timeout de 3600 s alcanzado antes de dejar el archivo en el fileshare.
2. Captura del cliente: dashboards 7 Day Rolling GL y WC con Process Status vacio en toda fila desde 9/21, estados Pending y New.
3. RCS-26609, 23 abr: mismo feed, otra etapa. Colgado en gpg, Ryan relanzo y confirmo 6 archivos por SFTP.
[2026-09-26] 1. RCS-29083, Ryan 9/25 7:01 PM y 7:17 PM: SQL sobre 4813 registros y codigos de error de la pagina .asp.
2. Adjuntos de Ryan: Load_lp.log 9/25 19:28 con SFTP ok a Sedgwick y Gallagher; carpeta Done con SEV0921.620 9:00 PM y luego SEV0925.619 7:20 PM, 980 KB.
3. APIS PROD, IN-37827-COR-2026-0023: 26 Sedgwick.Submit del 9/23 12:49 AM al 9/25 7:17 PM, ninguno despues. Salio en SEV0925.619.

## Precedentes
[2026-09-25] RCS-26609 7-Eleven, feed Sedgwick y GB colgado en gpg, relanzado, Delivery Resolved Load Job Modified.
ENG-7353 y ENG-7354, integraciones Sedgwick y GB para Incident, Kamminga, Backlog y Blocked. 7-Eleven migra a Incident sep/oct.
brain/markdown/21-kt-kristin-sign-off-procesos-rts.md, runbook de feed errors APIS y acceso PROD.
[2026-09-26] RCS-26609 7-Eleven abril, mismo feed colgado en gpg, relanzado por Ryan.

## Rastro
2026-09-25 inbox/2026-09-25-rcs-29083.md
2026-09-26 inbox/2026-09-26-rcs-29083.md

## RCS-29099. RCS-29099. Apoyo a reunión 3Sixty — 2026-09-25
_chunk 1900 · 2026-09-25 · fuente: inbox/2026-09-25-rcs-29099-apoyo-meet.md_

Ticket RCS-29099. Trabajado el 2026-09-25. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Actualización interna compartida por Juan el 25/09: Sebastián confirma build exitoso y aprobación de otra persona pendiente. Sin despliegue confirmado. Aclarar qué significa “falso positivo desde código” y quién debe aprobar; no convertir esa frase en diagnóstico.

## Rastro
2026-09-25 inbox/2026-09-25-rcs-29099-apoyo-meet.md

## RCS-29100. RCS-29100. Apoyo a reunión 3Sixty — 2026-09-25
_chunk 1901 · 2026-09-25 · fuente: inbox/2026-09-25-rcs-29100-apoyo-meet.md_

Ticket RCS-29100. Trabajado el 2026-09-25. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Actualización interna compartida por Juan el 25/09: Sebastián confirma mensajes enviados a John y Derek, ambos sin respuesta, y solicita apoyo de Juan para seguimiento. Esto confirma contacto, no aprobación ni cambio aplicado. No se enviaron mensajes desde esta tarea.

## Rastro
2026-09-25 inbox/2026-09-25-rcs-29100-apoyo-meet.md

## RCS-29103. La alerta de warning letter de Discipline Request no dispara en Stater Bros. Assignee Enrique Jimenez, Work in — 2026-09-24
_chunk 1902 · 2026-09-24 · fuente: inbox/2026-09-24-rcs-29103.md_

Ticket RCS-29103. Trabajado el 2026-09-24. 1 notas en inbox.

## Que pasa
La alerta de warning letter de Discipline Request no dispara en Stater Bros. Assignee Enrique Jimenez, Work in progress, High. Angie ya recreo la alerta y sigue igual.

## Evidencia
SELECT InProcess: 205148 = 1, 205157 = 1. Captura de Enrique en chat, 24 sep.
Alcance: 32 filas con InProcess = 1 en incident.Shoplifting, conteo de Enrique 24 sep.
SELECT RootCause: 205148 = Last and Final Warning, 205157 = NULL. Misma captura.
Smart Alert History vacio en ambos. adjuntos/RCS-29103/04 y 05

## Precedentes
RCS-28465 y RCS-28534, Stater Bros, inprocess trabado, ENG-2819. tickets/RCS-28465.md
Flujo de debug logs, RCS-28294. inbox/2026-09-18-flujo-debug-smart-alerts-inprocess.md
Familia de siete mecanismos. investigaciones/smart-alerts-familia-de-fallas.md

RCS-28534, mismo cliente, Accepted into Development, ENG-8698 Ready for Development con Matthew Kamminga. RCS-29103 ya esta enlazado Relates a RCS-28534.

## Rastro
2026-09-24 inbox/2026-09-24-rcs-29103.md

## RCS-29104. GPC, c356_gpc en GP11, investiga refunds fraudulentos del cajero 1037 en CHA266 y Secure no muestra el medio d — 2026-10-07
_chunk 1903 · 2026-10-07 · fuente: inbox/2026-09-24-rcs-29104.md;2026-09-28-rcs-29104-prioridad-auditoria.md;2026-10-07-rcs-29104-evaluacion-talos.md_

Ticket RCS-29104. Trabajado el 2026-09-24 a 2026-10-07. 3 notas en inbox.

## Que pasa
GPC, c356_gpc en GP11, investiga refunds fraudulentos del cajero 1037 en CHA266 y Secure no muestra el medio de pago. El hueco no es de refunds ni del cajero: una parte grande de la cadena carga sin filas en ardm_tender. Jira: Under Support Review, High, Juan.

## Evidencia
1. TXN 2609179617330521193: HEADER 1, ITEM 2, TENDER 0 en Snowflake ARDMPROD.ARDM_356 y en GP11 ardm_356. Header cuadra con la factura: -450.47, tax -28.48. totaltendercount NULL.
2. Tienda de CHA266, 1 al 22 sep: ~1000 headers, 1 sola transaccion con tender.
3. GP11 14 al 20 sep por tienda: sin tender 834 tiendas y 356710 headers; bajo 819 y 475720; normal 4033 y 1516936.

## Precedentes
RCS-28632 NAPA GPC c356, backload y load log, confluence/RTS-triage/RCS-28632-napa-work-items-detenidos.md
RCS-28649 Home Depot, header sin item ni tender, confluence/RTS-triage/RCS-28649-home-depot-item-tender-detail-missing.md
RCS-28834 ICA, busquedas header driven con LEFT JOIN a tender, confluence/RTS-triage/RCS-28834-ica-bank-withdrawal-deposit.md

## Rastro
2026-09-24 inbox/2026-09-24-rcs-29104.md
2026-09-28 inbox/2026-09-28-rcs-29104-prioridad-auditoria.md
2026-10-07 inbox/2026-10-07-rcs-29104-evaluacion-talos.md

## RCS-29126. Mike Croze convirtio tres investigaciones de Secure a casos en Incident. Dos casos recibieron el PDF vacio y u — 2026-10-07
_chunk 1905 · 2026-10-07 · fuente: inbox/2026-09-30-rcs-29126.md;2026-10-07-rcs-29126-evaluacion-talos.md_

Ticket RCS-29126. Trabajado el 2026-09-30 a 2026-10-07. 2 notas en inbox.

## Que pasa
Mike Croze convirtio tres investigaciones de Secure a casos en Incident. Dos casos recibieron el PDF vacio y uno quedo sin sujeto, por eso no lo encuentra. Ticket en Work in progress con Enrique. Paul pidio update el 30 sep.

## Evidencia
1. factboard.Board, 30 sep: 5 CaseID 451 2026-150020-1; 6 CaseID 461 2026-150020-2; 7 CaseID 482 2026-150020-3. StatusID 3 en los tres.
2. exported_pdf_5 y el PDF del caso 461 en blanco con "#". exported_pdf_7 IronPdf 21 sep trae 17 eventos.
3. Incident Active Cases de Mike, 22 casos: no figura 2026-150020-2.

## Precedentes
ENG-6676 y RCS-28006 Casey's, PDF con "#", Reopened 29 sep.
ENG-7440 y ARPP-644 Bunnings, combined PDF en blanco.
RCS-29171 GAP, estados de factboard.Board y CaseRecordNumber.
RCS-26453 y RCS-28898 Urban Outfitters, In Case sin caso. Aqui se descarto.

## Rastro
2026-09-30 inbox/2026-09-30-rcs-29126.md
2026-10-07 inbox/2026-10-07-rcs-29126-evaluacion-talos.md

## RCS-29128. RCS-29128: mayor incertidumbre — 2026-09-25
_chunk 1907 · 2026-09-25 · fuente: inbox/2026-09-25-rcs-29128-evaluacion.md_

Ticket RCS-29128. Trabajado el 2026-09-25. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Albertsons reporta ausencia de pagos de Jewel, división 32, para el 24 sep. Under Support Review, sin asignar, Medium, verificado 25 sep. Falta distinguir registros ausentes, tender ausente, carga parcial y presentación. Talos propone revisar la carga; sus afirmaciones sobre configuración y monitoreo no cuentan con validación independiente en esta revisión.

## Rastro
2026-09-25 inbox/2026-09-25-rcs-29128-evaluacion.md

## RCS-29129. RCS-29129 PacSun, MERCH CARD Refund Ranking — 2026-10-07
_chunk 1908 · 2026-10-07 · fuente: inbox/2026-09-25-backlog-82-facilidad.md;2026-09-25-rcs-29129-evaluacion.md;2026-09-25-rcs-29129-flags-factibilidad.md;2026-09-25-rcs-29129-ticket-nuevo-flags.md;2026-09-25-rcs-29129.md;2026-10-07-rcs-29129-evaluacion-talos.md_

Ticket RCS-29129. Trabajado el 2026-09-25 a 2026-10-07. 6 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Talos assessment / Evaluación Talos. Issue / Qué pasa MERCH CARD refund ranking / Ranking de devoluciones. Cause and assessment / Causa y evaluación Useful routine triage / Triage rutinario útil. Talos correctly treated this as a report configuration request.

## Rastro
2026-09-25 inbox/2026-09-25-backlog-82-facilidad.md
2026-09-25 inbox/2026-09-25-rcs-29129-evaluacion.md
2026-09-25 inbox/2026-09-25-rcs-29129-flags-factibilidad.md
2026-09-25 inbox/2026-09-25-rcs-29129-ticket-nuevo-flags.md
2026-09-25 inbox/2026-09-25-rcs-29129.md
2026-10-07 inbox/2026-10-07-rcs-29129-evaluacion-talos.md

## RCS-29130. Talos assessment / Evaluación Talos. Issue / Qué pasa One-hour load gap / Una hora sin cargas — 2026-10-07
_chunk 1909 · 2026-10-07 · fuente: inbox/2026-09-28-rcs-29130-prioridad-auditoria.md;2026-10-07-rcs-29130-evaluacion-talos.md_

Ticket RCS-29130. Trabajado el 2026-09-28 a 2026-10-07. 2 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Talos assessment / Evaluación Talos. Issue / Qué pasa One-hour load gap / Una hora sin cargas. Cause and assessment / Causa y evaluación Useful direction, overstrong cache exclusion / Orientación útil, descarte excesivo. Talos directed support to load progress.

## Rastro
2026-09-28 inbox/2026-09-28-rcs-29130-prioridad-auditoria.md
2026-10-07 inbox/2026-10-07-rcs-29130-evaluacion-talos.md

## RCS-29132. Talos assessment / Evaluación Talos. Issue / Qué pasa Three exception views / Tres vistas de excepciones — 2026-10-07
_chunk 1910 · 2026-10-07 · fuente: inbox/2026-09-28-rcs-29132-prioridad-auditoria.md;2026-10-07-rcs-29132-evaluacion-talos.md_

Ticket RCS-29132. Trabajado el 2026-09-28 a 2026-10-07. 2 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Talos assessment / Evaluación Talos. Issue / Qué pasa Three exception views / Tres vistas de excepciones. Cause and assessment / Causa y evaluación Correct request type, feasibility overstated / Tipo correcto, factibilidad exagerada. Talos's high-confidence statement that all necessary pieces already existed was stronger than the verification available in the local feasibility review.

## Rastro
2026-09-28 inbox/2026-09-28-rcs-29132-prioridad-auditoria.md
2026-10-07 inbox/2026-10-07-rcs-29132-evaluacion-talos.md

## RCS-29135. Guardia Colombia sobre tickets de India, 1 oct 2026 — 2026-10-01
_chunk 1911 · 2026-10-01 · fuente: inbox/2026-10-01-guardia-tickets-india.md_

Ticket RCS-29135. Trabajado el 2026-10-01. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Jira en vivo, leído 1 oct 9:16 Bogotá. Viraj los pidió en Nuaav Leadership Support el 30 sep. RCS-29135 Ross Stores, Aspect Step03 deadlock. Ross reprocesaba el batch 3685 hoy a las 7:00 Bogotá (5 AM PT).

## Rastro
2026-10-01 inbox/2026-10-01-guardia-tickets-india.md

## RCS-29140. Talos assessment / Evaluación Talos. Issue / Qué pasa Property Damage alerts / Alertas Property Damage — 2026-10-07
_chunk 1912 · 2026-10-07 · fuente: inbox/2026-10-07-rcs-29140-evaluacion-talos.md_

Ticket RCS-29140. Trabajado el 2026-10-07. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Talos assessment / Evaluación Talos. Issue / Qué pasa Property Damage alerts / Alertas Property Damage. Cause and assessment / Causa y evaluación Plausible discriminator, unverified outcome / Prueba plausible, desenlace sin verificar. Talos correctly distinguished send history from delivery and recommended checking alert-specific configuration.

## Rastro
2026-10-07 inbox/2026-10-07-rcs-29140-evaluacion-talos.md

## RCS-29146. RCS-29146 J Crew Group, mass complete de "case items" — 2026-10-06
_chunk 1914 · 2026-10-06 · fuente: inbox/2026-10-06-rcs-29146-guion-enrique.md;2026-10-06-rcs-29146-queries-verificacion.md;2026-10-06-rcs-29146.md_

Ticket RCS-29146. Trabajado el 2026-10-06. 3 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Que pasa Joe Rapacz (Asset Protection) pide completar en bloque todos los case items abiertos porque un tercero ajusta su tamano. Confirmo el 29 sep que son todos. Estado Work in progress, Low, assignee Enrique Jimenez, sin respuesta nuestra hace 7 dias. Juan ejecuta el cierre en la DB.

## Rastro
2026-10-06 inbox/2026-10-06-rcs-29146-guion-enrique.md
2026-10-06 inbox/2026-10-06-rcs-29146-queries-verificacion.md
2026-10-06 inbox/2026-10-06-rcs-29146.md

## RCS-29147. James Brown de Prada no entra a Incident. Work in progress, assignee Enrique Jimenez. Todo lo que soporte pued — 2026-09-28
_chunk 1915 · 2026-09-28 · fuente: inbox/2026-09-28-rcs-29147.md_

Ticket RCS-29147. Trabajado el 2026-09-28. 1 notas en inbox.

## Que pasa
James Brown de Prada no entra a Incident. Work in progress, assignee Enrique Jimenez. Todo lo que soporte puede revisar salio limpio.

## Causa
El dato del usuario esta sano. Mismo texto exacto que RCS-28061 Stater Bros, que resolvio Engineering con un cambio de configuracion via ENG-7000. La falla esta en el handoff de sesion de Secure a Incident, fuera del alcance de soporte.

## Evidencia
1. Enrique, 28 sep 16:35: SecurityID 1 en LPUser2 y en membership.Users, nivel "10" existe en LPSecurity.
2. Enrique, 28 sep 16:45: Enabled, Deleted No, sin filas en sso.SecurityLevelAssignments.
3. Texto exacto: "Session Error. Your Incident session could not be established. This is usually caused by a temporary account configuration issue." Igual a RCS-28061 y RCS-28486.

## Precedentes
RCS-28061 Stater Bros, mismo texto, ENG-7000 Kiran, tickets/RCS-28061.md
RCS-28486 McDonald's, segundo login entra, tickets/RCS-28486.md
RCS-28977 Vallarta, mismo texto, abierto en Under Engineering Review con Shandana Khan
ENG-7189 y ENG-7312, flujos/verificar-securityid-post-migracion.md

## Rastro
2026-09-28 inbox/2026-09-28-rcs-29147.md

## RCS-29179. Estee Lauder GP3 cayo de 338 tiendas el 9/17 a 266 el 9/28. Ticket en Under Customer Review, asignado a Luis H — 2026-10-09
_chunk 1916 · 2026-10-09 · fuente: inbox/2026-10-09-rcs-29179.md_

Ticket RCS-29179. Trabajado el 2026-10-09. 1 notas en inbox.

## Que pasa
Estee Lauder GP3 cayo de 338 tiendas el 9/17 a 266 el 9/28. Ticket en Under Customer Review, asignado a Luis Hernandez, sin respuesta del cliente desde el 10/01.

## Evidencia
1. Captura cruda de Event Hub c225_rawdata_sales: datos presentes hasta el ultimo dia activo de cada tienda y ausentes despues. Comentario de Anil P con hallazgos de Peyman, 2026-09-30 09:42.
2. GP3 ardm_225.ardm_header coincide con SECURE. Join de reference_location, timing de batch y volumen de blob descartados. Luis, 2026-10-01 16:31.
3. Shireesh propone cierre, Camila ya notifico al CSM. 2026-10-08 12:50. RTS-208603 vinculado ya esta Closed.

## Precedentes
RCS-29225 Burlington Store 213, mismo patron de tienda que deja de cargar, inbox/2026-10-02-reparto-unassigned.md

## Rastro
2026-10-09 inbox/2026-10-09-rcs-29179.md

## RCS-29195. Holly, 6 oct 9:50 AM ET: el correo no llego y la Smart Alert History de 26-288-15 esta en blanco. No hay fila — 2026-10-07
_chunk 1917 · 2026-10-07 · fuente: inbox/2026-09-30-rcs-29195-paso-a-paso.md;2026-09-30-rcs-29195.md;2026-10-01-rcs-29195-guion-llamada-diego.md;2026-10-06-rcs-29195-guia-diagnostico.md;2026-10-07-rcs-29195-evaluacion-talos.md_

Ticket RCS-29195. Trabajado el 2026-09-30 a 2026-10-07. 5 notas en inbox.

## Que pasa
[2026-09-30] Holly Garcia, dominio gimi.org, reporta que las Smart Alerts de Property Damage no salen, con el caso 26-288-15 como ejemplo. Work in progress, assignee Diego Buelvas, creado 30 sep 11:11 ET.
[2026-10-06] Holly, 6 oct 9:50 AM ET: el correo no llego y la Smart Alert History de 26-288-15 esta en blanco. No hay fila en SmartAlertProcess. Tenant 387 gwmek sin confirmar contra gimi.org.

## Evidencia
Jira, Talos 30 sep 11:23: sin falla de plataforma, sugiere revisar config y traza del caso. No es evidencia.
Control Panel USPROD: clientId 387, goodwill.org, slug gwmek. Dominio de Holly gimi.org, validar en Contacts.
Fix PR 58273 en US prod desde 28 sep, inbox/2026-09-28-smart-alerts-mecanismo-8-deadlock.md.

## Precedentes
Guia v2: flujos/smart-alert-disparo-manual.md
Lectura de Grafana: inbox/2026-09-28-grafana-smart-alerts-lectura.md
Mecanismos 1 a 7: investigaciones/smart-alerts-familia-de-fallas.md
Mecanismo 8: inbox/2026-09-28-smart-alerts-mecanismo-8-deadlock.md
Cuelgue en 12b, Stater Bros: inbox/2026-09-30-rcs-28534-grafana-hallazgos.md

## Rastro
2026-09-30 inbox/2026-09-30-rcs-29195-paso-a-paso.md
2026-09-30 inbox/2026-09-30-rcs-29195.md
2026-10-01 inbox/2026-10-01-rcs-29195-guion-llamada-diego.md
2026-10-06 inbox/2026-10-06-rcs-29195-guia-diagnostico.md
2026-10-07 inbox/2026-10-07-rcs-29195-evaluacion-talos.md

## RCS-29205. Starbucks NA reporta cero resultados en el run mensual del 29 sep para esta definicion. Jira: Under Support Re — 2026-10-09
_chunk 1918 · 2026-10-09 · fuente: inbox/2026-09-30-rcs-29205.md;2026-09-30-sbx-work-items-hallazgos-paso2.md;2026-09-30-sbx-work-items-paso-a-paso.md;2026-10-01-rcs-29205-paquete.md;2026-10-02-rcs-29205-escalacion-delivery.md;2026-10-02-sbx-work-items-escalacion-estado.md;2026-10-07-mejoras-flujo-soporte.md;2026-10-07-rcs-29205-evaluacion-talos.md;2026-10-07-sbx-work-items-estado.md;2026-10-07-talos-evaluacion-en-curso.md;2026-10-08-rcs_

Ticket RCS-29205. Trabajado el 2026-09-30 a 2026-10-09. 14 notas en inbox.

## Que pasa
Starbucks NA reporta cero resultados en el run mensual del 29 sep para esta definicion. Jira: Under Support Review, High, asignado a Juan, sin respuesta sustantiva al cliente.

## Evidencia
[2026-09-30] 1. Tres definiciones en cero en el mismo periodo 24 ago a 27 sep, RCS-29205/06/07, mismo reporter.
2. Cutover SBX 27 ago verificado contra ARDM_PRODUCTION.C166_SBX, RCS-28873, Sebastian 10 sep 17:07.
3. Talos reviso el config de arpfiles. No reviso la columna fisica en Snowflake.
[2026-10-09] RCS-29205: Work in progress, Juan. Ultimo comentario 8 oct 11:21 (avance al cliente). Sin nota interna sobre el branch de Ryan. Falta avance diario 9 oct.
RCS-29206: Under Customer Review. Juan publico seguimiento generico 9 oct 13:31. Automation aviso 7 dias sin respuesta el 8 oct.
RCS-29207: Completed desde 6 oct, falta Closed.
Pendiente confirmar si se enviaron los Teams del 8 oct a Ryan (cierre) y a Anushka/Adarsh (branch).

Teams del 8 oct a Ryan y a Anushka/Adarsh: enviados.
Anushka, 8 oct 11:00: el branch de Ryan ayuda; enrich_ardm_tender requiere cambios de mapeo; ella sube el PR; el rebuild necesita rol admin que ella no tiene, pedira a alguien tras el deploy.
Anushka, 9 oct 12:35: PR 58962 (achaudhary/c166_rcs29205_token_paidinout) con paid in/out, arreglos al acumulador de Ryan (column_spec, fuente prod, NULL en vez de FALSE, aproximacion x_refundtoown) y RCS-29205_fix_summary.md. Pide revision de Juan antes de deploy y rebuild.
Juan, 9 oct 12:42: preguntas antes de aprobar: validacion en lab, tokens ligados despues de la transaccion (seed hasta 26 ago, rebuild desde 22 ago, chunks diarios), paid in/out desde 26 ago cubre eventos desde 25 ago, aproximacion x_refundtoown 

## Que sigue
[2026-10-01] 1. Con el nombre del dueño, el ticket va a ese equipo. Es un mapeo de datos en producción, así que lo más probable es Delivery o el equipo de SnowTime que hizo el cutover. En RCS-28671 de THD ese equipo fue el de Dan Endersby.
2. Cuando lo arreglen, falta una pregunta para el mismo equipo: si recargan el campo en los refunds del 27 ago en adelante. Sin recarga, el periodo 24 ago a 27 sep sigue en cero aunque el mapeo quede bien.
3. Después, la corrida del periodo hay que repetirla. El rerun por WISC no crea duplicados aquí porque el periodo está vacío.
[2026-10-07] El documento investigaciones/SBX-snowtime-work-items-mensuales-cero.md conserva hipótesis del 30 septiembre. Ya existen tres resultados distintos: campo sin valores en 29205, cero compatible con los umbrales en 29206 y comparación numérica fallida en 29207. Una búsqueda todavía puede recuperar el documento inicial sin las tres correcciones.

Propuesta: conservar historia y añadir relaciones explícitas entre afirmaciones: contradice, sustituye, confirma o limita. Guardar fecha del evento y fecha de publicación por separado. Al recuperar una afirmación antigua, cargar su corrección y fuente juntas. Una fecha reciente no convierte un borrador en hecho. Criterio de aceptación: preguntar por la causa de cada uno de los tres tickets devuelve su mecanismo propio y las salvedades de validación, nunca una causa compartida por coaparición.

RCS-29231 demuestra por qué importa: el análisis del 2 octubre recomendó tratar x_rcpt_count como texto; la corrección del 5 octubre cuestionó el mapeo posicional y explicó que cambiar el predicado podía eliminar el error destruyendo el significado del reporte. Fuente: comentarios 3375965 y 3381773. La nota local del 2 octubre también proponía NULLIF ante

## Precedentes
RCS-28873 SBX, catalogo desincronizado tras cutover, tickets/RCS-28873.md
RCS-28848 SBX, filtro memberid contra x_memberid, Gabor 17 sep
RTS-206268 Kinney, placeholder X_ siempre NULL, confluence/RTS-triage/RTS-206268-kinney-drugs-pos-articleid.md
RCS-28671 THD, WISC no regenera por dedup, tickets/RCS-28671.md

## Rastro
2026-09-30 inbox/2026-09-30-rcs-29205.md
2026-09-30 inbox/2026-09-30-sbx-work-items-hallazgos-paso2.md
2026-09-30 inbox/2026-09-30-sbx-work-items-paso-a-paso.md
2026-10-01 inbox/2026-10-01-rcs-29205-paquete.md
2026-10-02 inbox/2026-10-02-rcs-29205-escalacion-delivery.md
2026-10-02 inbox/2026-10-02-sbx-work-items-escalacion-estado.md
2026-10-07 inbox/2026-10-07-mejoras-flujo-soporte.md
2026-10-07 inbox/2026-10-07-rcs-29205-evaluacion-talos.md
2026-10-07 inbox/2026-10-07-sbx-work-items-estado.md
2026-10-07 inbox/2026-10-07-talos-evaluacion-en-curso.md
2026-10-08 inbox/2026-10-08-rcs-29205-analisis-branch-ryan.md
2026-10-08 inbox/2026-10-08-sbx-work-items-estado.md
2026-10-09 inbox/2026-10-09-rcs-29205-revision-pr-58962.md
2026-10-09 inbox/2026-10-09-sbx-work-items-estado.md

## RCS-29206. Starbucks NA reporta cero resultados en el run mensual del 29 sep para esta definicion. Jira: Under Support Re — 2026-10-07
_chunk 1919 · 2026-10-07 · fuente: inbox/2026-09-30-rcs-29206.md;2026-10-01-rcs-29206-paquete.md;2026-10-07-rcs-29206-evaluacion-talos.md_

Ticket RCS-29206. Trabajado el 2026-09-30 a 2026-10-07. 3 notas en inbox.

## Que pasa
Starbucks NA reporta cero resultados en el run mensual del 29 sep para esta definicion. Jira: Under Support Review, High, asignado a Juan, sin respuesta sustantiva al cliente.

## Evidencia
1. Tres definiciones en cero en el mismo periodo 24 ago a 27 sep, RCS-29205/06/07, mismo reporter.
2. Cutover SBX 27 ago verificado contra ARDM_PRODUCTION.C166_SBX, RCS-28873, Sebastian 10 sep 17:07.
3. Talos dice que el umbral de espera paso el 30 sep. Hoy ya se puede comprobar si aparecieron items.

## Que sigue
1. Si pide ver los partners que estuvieron más cerca, armo la lista desde Snowflake con la misma regla.
2. Si prefiere esperar la próxima corrida, revisa ese día en Executive Workbench si la definición generó items.
3. Si confirma que con la explicación basta, pásalo a Complete con los dos campos de Resolution, y a Closed cuando él lo verifique.
4. Si no responde, el seguimiento va con la frase del banco: sin presión, solo para ver si se le pasó.

## Precedentes
RCS-28873 SBX, catalogo desincronizado tras cutover, tickets/RCS-28873.md
RTS-206268 Kinney, placeholder X_ siempre NULL, confluence/RTS-triage/RTS-206268-kinney-drugs-pos-articleid.md
RCS-28248 Jumbo, busqueda sin join a Header_Ext tras cutover, confluence/RTS-triage/RCS-28248-jumbo-workview-items-no-cargan.md

## Rastro
2026-09-30 inbox/2026-09-30-rcs-29206.md
2026-10-01 inbox/2026-10-01-rcs-29206-paquete.md
2026-10-07 inbox/2026-10-07-rcs-29206-evaluacion-talos.md

## RCS-29224. AAP quiere mover todos sus archivos de 1:30 AM EST a 9:30 AM EST. STRINVDT origina el cambio. Fecha mas tempra — 2026-10-13
_chunk 1921 · 2026-10-13 · fuente: inbox/2026-10-08-rcs-29224.md;2026-10-13-rcs-29224.md_

Ticket RCS-29224. Trabajado el 2026-10-08 a 2026-10-13. 2 notas en inbox.

## Que pasa
[2026-10-08] AAP pide mover el inicio del envio de STRINVDT (inventory) de 1:30 AM EST a 9:30 AM EST y pregunta el impacto en la ingesta. Jira: Escalated, Enrique, sin respuesta tecnica al cliente. El cambio de AAP aun no ocurrio ("We would change", Tim Young, 30 sep).
[2026-10-13] AAP quiere mover todos sus archivos de 1:30 AM EST a 9:30 AM EST. STRINVDT origina el cambio. Fecha mas temprana de AAP: 21 oct, sujeta a su gestion de cambios. AAP pregunta si eso crea un problema de nuestro lado. Jira: Escalated, Enrique. Rocky pidio confirmacion el 12 oct 11:08 EDT y no tiene respuesta.

## Evidencia
[2026-10-08] 1. Correo de Tim Young, 30 sep (adjunto .msg): los archivos salen poco despues de 1:30 AM EST y STRINVDT llega "much later", "likely already lagging a day". La recepcion real no es 1:30.
2. Captura de AAP, anterior al 7 oct 14:35 UTC: POS llega a 10/6. Inventario llega a 10/7 con 3145 tiendas y 532M filas, contra 5391 tiendas y 935M del 10/6. El 10/7 estaba incompleto.
3. RCS-29224, Shireesh Ramdas, 1 oct: "AAP is being moved to SnowTime". La causa que Enrique dio a AAP en RCS-29244 cita a Daniel Endersby y no tiene evidencia propia.
[2026-10-13] 1. Rocky, 9 oct: "move all the files from 130 to 930", "Earliest we would see the change would be 10/21". https://trebuco.atlassian.net/browse/RCS-29224?focusedCommentId=3386223
2. Talos, 1 oct: datos esperados a las 6:00 AM ET, tolerancia de dos dias, medida sobre ventas. Anterior al cambio de lag. https://trebuco.atlassian.net/browse/RCS-29224?focusedCommentId=3373927
3. Tim Young, 30 sep, en el .msg: STRINVDT llega "much later" que el resto. Hora real sin medir.

## Precedentes
[2026-10-08] RCS-29244 AAP, mismo cliente, Completed 8 oct, Jira.
RCS-27837 Ollie's, file_registry para separar retraso de archivo y de pipeline, Confluence RTS 478054547467.
RCS-28126 Kinney, aviso de cambio de feed, db:knowledge_chunks/1444.
[2026-10-13] RCS-29244 AAP, Completed 8 oct. RCS-27837 Ollie's, patron de file_registry: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478054547467/Secure+Pipeline+Late+Load+Case+Study

## Rastro
2026-10-08 inbox/2026-10-08-rcs-29224.md
2026-10-13 inbox/2026-10-13-rcs-29224.md

## RCS-29231. El reporte y sus derivados fallan desde el 30 sep con Numeric value '' is not recognized. Ticket High, Work in — 2026-10-07
_chunk 1922 · 2026-10-07 · fuente: inbox/2026-10-02-rcs-29231.md;2026-10-07-rcs-29231-evaluacion-talos.md_

Ticket RCS-29231. Trabajado el 2026-10-02 a 2026-10-07. 2 notas en inbox.

## Que pasa
El reporte y sus derivados fallan desde el 30 sep con Numeric value '' is not recognized. Ticket High, Work in progress, assignee Enrique Jimenez.

## Evidencia
1. RTS-208663, Ganesh 30 sep 11:25 ET: QUARANTINE_ARDM_HEADER failed on column X_RCPT_COUNT, Numeric value '' is not recognized.
2. RTS-208663, Vismaya 30 sep 13:27 ET: Sumeet dice que la causa fue un PR previo.
3. RCS-29231, Ayesha 1 oct: mismo error en RunAsyncSearchActivity, clientId 44, QueryId 01c77149-0109-d5e7-0120-d20111089fc7.

## Precedentes
RCS-29207 SBX c166, TEXT comparado con literal numerico, inbox/2026-10-01-rcs-29207-comentario-interno.md
RCS-28873 Starbucks, mismo 22018 en MemberID, confluence/RTS-triage/RCS-28873-starbucks-searches-error-slowness.md
Urban c044, tipos de campo en arpfiles, investigaciones/excel-urban-root-cause-2026-09-17.md

## Rastro
2026-10-02 inbox/2026-10-02-rcs-29231.md
2026-10-07 inbox/2026-10-07-rcs-29231-evaluacion-talos.md

## RCS-29237. Revisión PR 58961, commit fab5580b2cfbf70d1e6d931852dae4fe3bf0999c. Qué pasa El PR normaliza UPC en catálogo, — 2026-10-09
_chunk 1924 · 2026-10-09 · fuente: inbox/2026-10-09-rcs-29237-revision-pr-58961.md_

Ticket RCS-29237. Trabajado el 2026-10-09. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Revisión PR 58961, commit fab5580b2cfbf70d1e6d931852dae4fe3bf0999c. Qué pasa El PR normaliza UPC en catálogo, artículos y ambas ramas de descuentos. Corrige la coincidencia 019649504565 con 19649504565. corregir compatibilidad histórica antes de aprobar.

## Rastro
2026-10-09 inbox/2026-10-09-rcs-29237-revision-pr-58961.md

## RCS-29288. Talos assessment / Evaluación Talos. Issue / Qué pasa Monthly alignment import / Importación mensual — 2026-10-07
_chunk 1925 · 2026-10-07 · fuente: inbox/2026-10-07-rcs-29288-evaluacion-talos.md_

Ticket RCS-29288. Trabajado el 2026-10-07. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Talos assessment / Evaluación Talos. Issue / Qué pasa Monthly alignment import / Importación mensual. Cause and assessment / Causa y evaluación Useful routine triage / Triage rutinario útil. Talos correctly identified the established import and warned to use the latest attachment.

## Rastro
2026-10-07 inbox/2026-10-07-rcs-29288-evaluacion-talos.md

## RCS-29293. RCS-29293 Chanel, Smart Alert marcada enviada y el correo no llega — 2026-10-07
_chunk 1926 · 2026-10-07 · fuente: inbox/2026-10-05-rcs-29293.md;2026-10-07-rcs-29293-evaluacion-talos.md_

Ticket RCS-29293. Trabajado el 2026-10-05 a 2026-10-07. 2 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Talos assessment / Evaluación Talos. Issue / Qué pasa Sent status without received email / Enviado sin recepción. Cause and assessment / Causa y evaluación Useful observability warning, unproven attribution / Advertencia útil, atribución no probada. Talos correctly warned that a sent status is not a delivery receipt and proposed recipient/provider checks.

## Rastro
2026-10-05 inbox/2026-10-05-rcs-29293.md
2026-10-07 inbox/2026-10-07-rcs-29293-evaluacion-talos.md

## RCS-29338. Corinne Booth (SpartanNash) imprime plantillas del año fiscal nuevo y sale el texto de referencia. Jira: Work — 2026-10-08
_chunk 1929 · 2026-10-08 · fuente: inbox/2026-10-08-rcs-29338.md_

Ticket RCS-29338. Trabajado el 2026-10-08. 1 notas en inbox.

## Que pasa
Corinne Booth (SpartanNash) imprime plantillas del año fiscal nuevo y sale el texto de referencia. Jira: Work in progress, asignado a Enrique. Corinne respondió el 8 oct y falta la respuesta de Enrique.

## Evidencia
1. RCS-26171, Carlos Jacinto 31 mar 2026: para excluir la referencia, pon Display Reference en No en cada pregunta. 3 abr: cambió todas las preguntas y listó las pendientes con un SELECT sobre DisplayRef = 1.
2. RCS-29338, Corinne 8 oct 2026: afectadas Piggly Wiggly Test y Fresh Encounter (importadas) y Metcalfe's Self (solo versión). Otras importadas no.
3. Confluence RTS 474948206640 Audit Template Import Specifications: el CSV tiene 28 columnas y ninguna es Display Reference.

## Precedentes
RCS-19415 Feb 2025, fix de código en release 26 mar 2025
RCS-26171 Mar 2026, cambio masivo por Carlos
RCS-27315 Jun 2026, quitado a mano
RCS-27794 Jul 2026, cerrado sin causa

## Rastro
2026-10-08 inbox/2026-10-08-rcs-29338.md

## RCS-29350. Sean Parello reporta que un export programado de usuario para finanzas deja la notificacion en la cola de noti — 2026-10-09
_chunk 1930 · 2026-10-09 · fuente: inbox/2026-10-09-rcs-29350-consultas.md;2026-10-09-rcs-29350-monitor.md;2026-10-09-rcs-29350.md_

Ticket RCS-29350. Trabajado el 2026-10-09. 3 notas en inbox.

## Que pasa
Sean Parello reporta que un export programado de usuario para finanzas deja la notificacion en la cola de notificaciones de Secure y no la reenvia al correo, con la preferencia de reenvio activa en todos los usuarios. Jira 10/9: Under Support Review, asignado a Diego Buelvas, sin links ni adjuntos.

## Evidencia
1. Grafana 10/9 15:59:32 UTC, clientId 354: "Successful Email(s) 56" instancia 354x8573... y "Successful Email(s) 6" instancia 354x0ab7d455..., la del Run Now. Cero intentos desde el 10/8 17:50 UTC.
2. SendGrid 10/9 15:59:31 a 15:59:32 UTC, Delivered 250: alex.gonzalez2 6, luis.ramirez 4, brandon.stewart 4. sean.parello sin verificar, la busqueda no se aplico.
3. Luis y Brandon tienen tres Daily Push, 308, 311 y 317, y recibieron cuatro: los 6 del Run Now parecen duplicados de NotificationUser 324 a 329. HIPOTESIS.

## Precedentes
RCS-29021 Claire's, mismo sintoma, job NotificationEmail_Scheduled atascado, reinicio. Sin ficha en Cerebro.
RCS-29138 Casey's, correos de asignacion duplicados, ENG-9087. Ruta distinta, no aplica.
investigaciones/smart-alerts-familia-de-fallas.md, los siete mecanismos de Smart Alerts. No aplica.
confluence/RTS-triage sin precedente. Confluence en vivo sin resultados para NotificationEmail_Scheduled.

## Rastro
2026-10-09 inbox/2026-10-09-rcs-29350-consultas.md
2026-10-09 inbox/2026-10-09-rcs-29350-monitor.md
2026-10-09 inbox/2026-10-09-rcs-29350.md

## RCS-29361. Tim Berry reporta que la devolucion de Store 124, Pos 2, Trans 1408 imprime REFUND WITHOUT RECEIPT y a la vez — 2026-10-08
_chunk 1931 · 2026-10-08 · fuente: inbox/2026-10-08-rcs-29361-queries-snowflake.md;2026-10-08-rcs-29361.md_

Ticket RCS-29361. Trabajado el 2026-10-08. 2 notas en inbox.

## Que pasa
Tim Berry reporta que la devolucion de Store 124, Pos 2, Trans 1408 imprime REFUND WITHOUT RECEIPT y a la vez trae el bloque Original Transaction Information. Jira: Under Support Review, sin assignee, prioridad High, creado el 8 oct 16:50 ET.

## Evidencia
1. Respuesta del visor, journal/event/2609079422895513998, GenericEventProvider, ardm_json fetch+resolve. No contiene el texto REFUND WITHOUT RECEIPT. Header: receiptedkeyedreturncount 1, nonreceipted* 0, recalledflg true con recalledtransaction de la venta 2682.
2. Items del mismo JSON. Striped Acid Was: itemrecordtype 2, refundwithreceiptflg true. Oxford Shirt: itemrecordtype 1, voidedflg true, refundwithreceiptflg false.
3. ARDM_JSON es tabla de SnowTime (rol SNOWTIME_PRODUCTION_DBT_C044_URB, creada el 5 ago, 121 millones de filas). Las banderas de ARDM_ITEM no cambiaron desde el 1 oct.

## Precedentes
RCS-28510 Wild Fork, el visor solo dibuja lo que trae el JSON, confluence/RTS-triage/RCS-28510-wild-fork-origorderinfo-v1.md. Otro cliente.
RCS-29028 y RCS-29231 revisados, sin relacion probada, inbox/2026-10-08-urban-investigacion.md

## Rastro
2026-10-08 inbox/2026-10-08-rcs-29361-queries-snowflake.md
2026-10-08 inbox/2026-10-08-rcs-29361.md

## RCS-29367. BOARD EQUIPO COLOMBIA V2 (9 oct 2026). REEMPLAZA EL ALCANCE DEL PASO 1 — 2026-10-09
_chunk 1932 · 2026-10-09 · fuente: inbox/2026-10-09-board-equipo-colombia-v2.md_

Ticket RCS-29367. Trabajado el 2026-10-09. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
BOARD EQUIPO COLOMBIA V2 (9 oct 2026). REEMPLAZA EL ALCANCE DEL PASO 1. ALCANCE Solo los tickets asignados a los 6 del equipo (Luis Hernandez, Sebastian Garces, Diego Buelvas, Edwin Garzon, Sebastian Rueda, Enrique Jimenez) mas el Supp Backlog, la cola sin asignar (JQL: project = RCS AND assignee IS EMPTY AND statusCategory != Done).

## Rastro
2026-10-09 inbox/2026-10-09-board-equipo-colombia-v2.md

## RTS-206667. Consulta directa del 22 sep 2026. Under L2 Support Review, Vlad Bogus — 2026-09-22
_chunk 1933 · 2026-09-22 · fuente: inbox/2026-09-21-RTS-206667-actualizacion.md;2026-09-21-THD-conclusiones-cruzadas.md;2026-09-21-THD-explicacion-camila.md;2026-09-22-THD-RTS-206667.md_

Ticket RTS-206667. Trabajado el 2026-09-21 a 2026-09-22. 4 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Consulta directa del 22 sep 2026. Under L2 Support Review, Vlad Bogus. El ticket empezó por SNR4 y ahora contiene cancelaciones y lentitud de otras búsquedas. rename TenderTypeGroup a StdTenderTypeGrp confirmado para el error original.

## Rastro
2026-09-21 inbox/2026-09-21-RTS-206667-actualizacion.md
2026-09-21 inbox/2026-09-21-THD-conclusiones-cruzadas.md
2026-09-21 inbox/2026-09-21-THD-explicacion-camila.md
2026-09-22 inbox/2026-09-22-THD-RTS-206667.md

## RTS-206998. RTS-206998 | Actualizado 2026-09-22 | Peyman y Gulshan Fuentes: mensajes y capturas aportados por Juan — 2026-09-21
_chunk 1934 · 2026-09-21 · fuente: inbox/2026-09-21-RTS-206998-confirmacion-peyman.md_

Ticket RTS-206998. Trabajado el 2026-09-21. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
RTS-206998 | Actualizado 2026-09-22 | Peyman y Gulshan Fuentes: mensajes y capturas aportados por Juan. No se inspeccionaron los logs completos en vivo. El enlace de Gulshan llegó truncado; build identificado:

## Rastro
2026-09-21 inbox/2026-09-21-RTS-206998-confirmacion-peyman.md

## RTS-207427. Avance para Camila | 2026-09-22 Juan aporta el texto enviado al cliente como contexto del seguimiento. Respues — 2026-09-22
_chunk 1936 · 2026-09-22 · fuente: inbox/2026-09-22-lululemon-avance-camila.md_

Ticket RTS-207427. Trabajado el 2026-09-22. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Avance para Camila | 2026-09-22 Juan aporta el texto enviado al cliente como contexto del seguimiento. Respuesta basada en las confirmaciones de Ryan, Peyman y Gulshan recogidas en las notas previas; sin nueva consulta en vivo. SQL quedó confirmado con Ryan: el cambio aplica a todas las ejecuciones posteriores.

## Rastro
2026-09-22 inbox/2026-09-22-lululemon-avance-camila.md

## RTS-207712. Consulta directa del 22 sep 2026. Under L2 Support Review, Enrique Jimenez — 2026-09-22
_chunk 1937 · 2026-09-22 · fuente: inbox/2026-09-22-THD-RTS-207712.md_

Ticket RTS-207712. Trabajado el 2026-09-22. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Consulta directa del 22 sep 2026. Under L2 Support Review, Enrique Jimenez. RTS-208103 y RTS-208130 están Closed por seguimiento en este ticket. Último conteo documentado:

## Rastro
2026-09-22 inbox/2026-09-22-THD-RTS-207712.md

## RTS-207848. RTS-207848 | 2026-09-21 | Investigación y email draft Borrador no enviado. Sin ETA ni verificación operativa e — 2026-09-21
_chunk 1938 · 2026-09-21 · fuente: inbox/2026-09-21-RTS-207848-lululemon-investigacion.md_

Ticket RTS-207848. Trabajado el 2026-09-21. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
RTS-207848 | 2026-09-21 | Investigación y email draft Borrador no enviado. Sin ETA ni verificación operativa en vivo. Recuperación no implica prevención definitiva. comentarios 3352388/3352399 de https://trebuco.atlassian.net/browse/RTS-207848; fix en https://trebuco.atlassian.net/browse/RTS-207427; antecedentes RTS-206318, RTS-206749, RTS-206998 y RTS-207875.

## Rastro
2026-09-21 inbox/2026-09-21-RTS-207848-lululemon-investigacion.md

## RTS-208690. RTS-208690. CVS C037 STREAM_TRUNCATED. Cómo bajar y desencriptar desde la VM — 2026-10-07
_chunk 1939 · 2026-10-07 · fuente: inbox/2026-10-02-rts-208690-cvs-blob-desencriptar.md;2026-10-07-talos-informe-es.md;2026-10-07-talos-report-en.md_

Ticket RTS-208690. Trabajado el 2026-10-02 a 2026-10-07. 3 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
an AI engineering assessment of its contribution to support Review period: 28 September to 7 October 2026. Internal opinion grounded in the reviewed evidence. My assessment is that Talos demonstrated value in initial classification and diagnostic test selection, but the visible record does not establish reliable diagnostic autonomy.

## Rastro
2026-10-02 inbox/2026-10-02-rts-208690-cvs-blob-desencriptar.md
2026-10-07 inbox/2026-10-07-talos-informe-es.md
2026-10-07 inbox/2026-10-07-talos-report-en.md

## Guia setup desencriptar PGP en VM (via Sebastian Rueda, Teams) — 2026-09-21
_chunk 1942 · 2026-09-21 · fuente: inbox/2026-09-21-guia-desencriptar-pgp-vm-eu.md_

# Guia setup desencriptar PGP en VM (via Sebastian Rueda, Teams)

Fuente: chat de Teams con Sebastian Rueda, no Confluence. Confirmado 21 sep 2026.
Contexto: Juan ya tenia la VM de EU seteada, path OK, gpg4win instalado y el repo appriss_pipeline clonado.
Sebastian aporto el archivo gpg_looper.sh corregido (el compartido se llamaba "gpg_looper 2.sh", hay que renombrarlo a gpg_looper.sh) y confirmo el flujo completo.

## Prerequisito

Tener el PAT de Azure DevOps. Se pide en uno de los pasos del setup, sin el, el script de instalacion no avanza.

## Instalar el pipeline (una sola vez por VM/region)

1. Clonar el repo dentro de la VM, en Users, carpeta CODE:
   git clone https://apprissdevops@dev.azure.com/apprissdevops/DataOps%20Platform/_git/appriss_pipeline
2. Correr el script de setup (env_setup.ps1) para que PowerShell reconozca apprissgpg como comando. Sin este paso, apprissgpg no se reconoce como comando conocido.

## Importar la clave del cliente

En PowerShell:
apprissgpg i [clientID+abreviacion]
ejemplo: apprissgpg i c171seg

## Desencriptar

Colocar el archivo gpg_looper.sh en la misma carpeta donde estan los archivos .pgp del cliente.
Correrlo y usar el mismo codigo de cliente que se importo arriba.

El archivo original compartido por Sebastian se llama "gpg_looper 2.sh", hay que corregir el nombre a gpg_looper.sh antes de usarlo.

## Nota de Juan

El punto donde se traba la gente la primera vez es que apprissgpg no se reconoce como comando hasta correr el setup del pipeline (clonar repo + correr el script). Una vez hecho eso, el resto es tedioso pero no complejo: importar clave, correr el .sh con el codigo de cliente.


## Rastro
2026-09-21 inbox/2026-09-21-guia-desencriptar-pgp-vm-eu.md

## THD. Para hablar con Camila después de la llamada — 2026-09-22
_chunk 1944 · 2026-09-22 · fuente: inbox/2026-09-22-THD-conversacion-camila-postcall.md_

# THD. Para hablar con Camila después de la llamada

22 de septiembre de 2026. Base principal: grabación 15 completa, 20:24. Complemento: grabación 14 completa, 35:01. Transcripción automática local; tiempos relativos a cada archivo. Jira verificado durante este análisis. Las afirmaciones del cliente y de Camila conservan su atribución; no sustituyen pruebas de Ingeniería.

[Qué decirle](#conversacion) · [Qué cambió](#hallazgos) · [Qué confirmar](#acciones) · [Correcciones](#correcciones) · [Otros pendientes](#otros) · [Fuentes](#fuentes)

<a id="conversacion"></a>
## Para abrir la conversación

Camila, me quedé con que Matt necesita volver a confiar en el reporte para identificar faltantes reales. Hoy puede encontrar todos los artículos en el recibo y seguir viendo una discrepancia en el total calculado. Además, reportó lo mismo con Total Item Quantity. Yo pondría esos dos campos en la validación de cada recarga y pediría confirmar qué fechas quedaron conciliadas, especialmente el 22, que durante la llamada todavía estaba pendiente de confirmación.

Lo de las tres y cuatro horas tiene otro sentido al que inicialmente interpretamos con la captura. Matt considera rápida la carga y quiere confirmar que esperamos el marker file, que indica que THD terminó de entregar el lote. Él mismo dijo que es una teoría. Podemos revisar esa secuencia con Infraestructura sin dar por hecho que ahí está la causa.

Para el correo de mañana, alinearía contigo qué podemos respaldar sobre la expectativa de fin de semana, quién queda a cargo del monitoreo diario y qué respuesta nos falta de Ingeniería. También separaría la recuperación de los work items del arreglo del timeout, porque hoy tienen estados diferentes.

<a id="hallazgos"></a>
## Lo que cambió con las grabaciones

| Tema | Qué sabemos ahora | Qué significa para nosotros |
| --- | --- | --- |
| Total Item Sale Amount | Matt observa recibos completos e importe calculado discrepante. Sospecha que la recarga no actualiza el campo. Audio 15, 00:00 a 01:55. | RCS-28968 sigue siendo el caso principal. Camila también describe esa falta de recálculo en audio 14, 14:47 a 16:33, y menciona a Andres haciendo el rebuild. Falta respaldo técnico del mecanismo y del despliegue. |
| Total Item Quantity | Matt reporta cantidad 1 con 3 artículos visibles en recibo. Dice que en ese momento ya no ve discrepancias tras la recarga. Audio 15, 05:07 a 07:04. | Añadir este campo al alcance de revisión. Validar cantidades según su definición, sin asumir que número de líneas siempre equivale a unidades. |
| Otros calculados | Menciona campos de transacción anterior y siguiente como candidatos. Camila prioriza los dos anteriores y revisará el resto después. Audio 15, 07:04 a 09:17 y 13:03 a 13:57. | No decir que todos esos campos fallan. Acordar inventario y pruebas posteriores a recarga. |
| Tres y cuatro horas | THD envía lotes cada 4 h. Matt observa unos 3 a 3,5 h de atraso y recuerda 5 a 8 h antes. Pregunta si extraemos antes de terminar el lote. Audio 15, 09:17 a 17:49. | Corrige nuestra lectura provisional de la captura. No estaba pidiendo simplemente cargar más rápido. |
| Marker file | Según Matt, THD publica este archivo cuando termina el lote en GCS. Estima unos 30 min para prepararlo. Audio 15, 11:53 a 12:34 y 14:03 a 15:55. | Revisar marcador, extracción e ingestión del mismo lote. Matt reconoce expresamente que su explicación es una teoría. |
| Compromiso siguiente | Camila promete correo mañana 23 sep con resumen y novedades disponibles. Audio 15, 18:52 a 19:59. | Es compromiso de actualización. No prometió resolver todo mañana. |

Un lote cada 4 h puede contener transacciones mucho más recientes. Matt lo aclara a 14:03. El promedio de atraso, la antigüedad de la última transacción y la frecuencia de envío miden cosas distintas. Ninguno demuestra por sí solo que ignoremos el marcador.

<a id="acciones"></a>
## Lo que conviene concretar con ella

| Con quién coordinar | Pregunta concreta | Evidencia que necesitamos |
| --- | --- | --- |
| Bikash, Andres y Datos, RCS-28968 | ¿Qué fechas y campos quedaron corregidos? ¿Quién confirma el 22? | Misma transacción antes y después: Subtotal, detalle, recibo, Total Item Sale Amount y Total Item Quantity. Usar el ejemplo 4909, tienda 8918, registro 51, ID 2609210101525048961. |
| Responsable del arreglo permanente | ¿Qué mecanismo falla, cuál es el ticket técnico y qué respalda la expectativa de esta semana? | Dueño, alcance, pruebas, despliegue previsto y validación de una carga nueva sin intervención. Separar del arreglo de suspendidas. |
| Datos e Infraestructura | ¿La extracción espera el marker file del lote correcto? | Horas con zona de publicación del último archivo, marcador, extracción, carga y recálculo; archivos esperados frente a recibidos. No retrasar cargas a ciegas. |
| Responsable de la contención | ¿Quién revisa cada día y cuándo avisa a Camila? | Horario, resultado, recarga si hace falta y conciliación de todos los campos dependientes. Revisar el SOP de recarga y recibos ya prometido en RCS-28649. |
| Shandana e Ingeniería | ¿Podemos recuperar el work item señalado antes del arreglo general? | Plan de ENG-8659, responsable y preservación de notas/asignaciones. Verificar los 17 históricos; no mezclarlos con 25 trabajos de cola. |
| Mohammed y responsable de ENG-8650 | ¿Qué falta para publicar y validar el timeout? | Fecha efectiva, prueba y alcance. La versión 24 sep sigue sin publicar. No es ETA del datafeed. |

<a id="correcciones"></a>
## Precisiones para el próximo mensaje

1. Fin de semana. Camila lo expresó como expectativa a 02:55 y 03:11 del audio 15. Hasta obtener respaldo de Ingeniería, mantener esa diferencia frente a una ETA confirmada. El cliente ya escuchó esa expectativa.
2. Recarga del 22. El correo previo daba por recargado 20 a 22; a 03:11 del audio 15 Camila aún esperaba confirmación del 22. Puede tratarse de etapas distintas. Confirmar si falta carga, recálculo o validación antes de repetir que todo quedó correcto.
3. Work items. En audio 14, 03:03 a 04:20, la explicación de Accepted into Development sugirió arreglo listo esperando publicación. ENG-8659 sigue Backlog, sin asignado ni versión. ENG-8650 sí está Development Complete. Corregir la explicación para cada caso.
4. Causa única. La llamada no demuestra que marcador, faltantes, calculados, suspendidas y búsquedas lentas compartan causa. Tampoco demuestra que Snowflake explique por sí solo la mejora de tiempos.
5. Validación completa. Un recibo completo resuelve una parte del problema. Matt necesita que los campos de búsqueda y monitoreo también concilien para distinguir errores reales.

<a id="otros"></a>
## Otros pendientes de la primera grabación

Comunicación y SOP, audio 14, 16:33 a 26:52. Ericka pide instrucciones para que cada corrección incluya todas las salidas afectadas; recuerda problemas de marzo. Camila ofrece revisar esa historia con Valerie y reforzar el SOP. Corey valora la respuesta de Soporte y p

## Rastro
2026-09-22 inbox/2026-09-22-THD-conversacion-camila-postcall.md

## Informe de tickets RCS por persona, agosto y septiembre 2026 — 2026-09-22
_chunk 1947 · 2026-09-22 · fuente: inbox/2026-09-22-informe-tickets-equipo-ago-sep.md_

# Informe de tickets RCS por persona, agosto y septiembre 2026

Fuente: Jira, proyecto RCS, consulta en vivo el 22 sep 2026. Ventana agosto 1 a septiembre 22.
Cerrado agrupa Closed, Completed y Duplicate. Pendiente agrupa el resto de estados activos.
Asignados cuenta tickets por fecha de creacion dentro de la ventana, no por fecha de asignacion,
Jira no registra ese campo por separado. Backlog vivo es una foto de hoy, incluye tickets creados
antes de agosto que siguen abiertos.

Equipo: 7 en Colombia (Juan Martinez, Diego Buelvas, Enrique Jimenez, Sebastian Rueda, Sebastian
Garces, Edwin Garzon, Luis Hernandez), 7 en India (Viraj Kansara, Harini Shankarakrishnan, Bikash
Kumar, Megha Rathi, Nikita Rathore, Gulshan Kumar, Vedant Shirude). Clasificacion por nombre.

### Combinado, agosto 1 a septiembre 22

| Persona | Grupo | Asignados | Cerrados | % cierre | Pendientes del periodo | Backlog vivo hoy |
|---|---|---|---|---|---|---|
| Diego Buelvas | Colombia | 55 | 44 | 80.0% | 11 | 12 |
| Edwin Garzon | Colombia | 50 | 29 | 58.0% | 21 | 24 |
| Juan Martinez | Colombia | 31 | 16 | 51.6% | 15 | 17 |
| Sebastian Rueda | Colombia | 24 | 10 | 41.7% | 14 | 20 |
| Sebastian Garces | Colombia | 21 | 9 | 42.9% | 12 | 12 |
| Luis Hernandez | Colombia | 13 | 9 | 69.2% | 4 | 5 |
| Enrique Jimenez | Colombia | 10 | 2 | 20.0% | 8 | 8 |
| Viraj Kansara | India | 83 | 73 | 88.0% | 10 | 13 |
| Vedant Shirude | India | 39 | 26 | 66.7% | 13 | 13 |
| Nikita Rathore | India | 35 | 22 | 62.9% | 13 | 16 |
| Bikash Kumar | India | 34 | 19 | 55.9% | 15 | 18 |
| Gulshan Kumar | India | 20 | 18 | 90.0% | 2 | 6 |
| Megha Rathi | India | 14 | 5 | 35.7% | 9 | 9 |
| Harini Shankarakrishnan | India | 10 | 5 | 50.0% | 5 | 5 |

Total equipo: 439 asignados, 287 cerrados, 65.4% de cierre, 152 pendientes del periodo.
Backlog vivo total hoy: 178 tickets abiertos, 98 en Colombia, 80 en India.

### Agosto completo

| Persona | Grupo | Asignados | Cerrados | % cierre | Pendientes del periodo |
|---|---|---|---|---|---|
| Diego Buelvas | Colombia | 33 | 32 | 97.0% | 1 |
| Edwin Garzon | Colombia | 24 | 17 | 70.8% | 7 |
| Juan Martinez | Colombia | 23 | 14 | 60.9% | 9 |
| Sebastian Rueda | Colombia | 11 | 4 | 36.4% | 7 |
| Sebastian Garces | Colombia | 6 | 6 | 100.0% | 0 |
| Luis Hernandez | Colombia | 3 | 3 | 100.0% | 0 |
| Enrique Jimenez | Colombia | 0 | 0 | 0.0% | 0 |
| Viraj Kansara | India | 64 | 58 | 90.6% | 6 |
| Vedant Shirude | India | 18 | 17 | 94.4% | 1 |
| Nikita Rathore | India | 24 | 18 | 75.0% | 6 |
| Bikash Kumar | India | 21 | 15 | 71.4% | 6 |
| Gulshan Kumar | India | 17 | 16 | 94.1% | 1 |
| Megha Rathi | India | 4 | 2 | 50.0% | 2 |
| Harini Shankarakrishnan | India | 5 | 2 | 40.0% | 3 |

### Septiembre, dias 1 a 22

| Persona | Grupo | Asignados | Cerrados | % cierre | Pendientes del periodo |
|---|---|---|---|---|---|
| Diego Buelvas | Colombia | 22 | 12 | 54.5% | 10 |
| Edwin Garzon | Colombia | 26 | 12 | 46.2% | 14 |
| Juan Martinez | Colombia | 8 | 2 | 25.0% | 6 |
| Sebastian Rueda | Colombia | 13 | 6 | 46.2% | 7 |
| Sebastian Garces | Colombia | 15 | 3 | 20.0% | 12 |
| Luis Hernandez | Colombia | 10 | 6 | 60.0% | 4 |
| Enrique Jimenez | Colombia | 10 | 2 | 20.0% | 8 |
| Viraj Kansara | India | 19 | 15 | 78.9% | 4 |
| Vedant Shirude | India | 21 | 9 | 42.9% | 12 |
| Nikita Rathore | India | 11 | 4 | 36.4% | 7 |
| Bikash Kumar | India | 13 | 4 | 30.8% | 9 |
| Gulshan Kumar | India | 3 | 2 | 66.7% | 1 |
| Megha Rathi | India | 10 | 3 | 30.0% | 7 |
| Harini Shankarakrishnan | India | 5 | 3 | 60.0% | 2 |

Septiembre lleva 22 de 30 dias. Compara el volumen absoluto de septiembre contra agosto completo
con esa diferencia de base en mente, no contra el mismo numero de dias.

### Comparativa Colombia vs India

| Periodo | Grupo | Asignados | Cerrados | % cierre | Pendientes del periodo | Prom. asignados/persona |
|---|---|---|---|---|---|---|
| Agosto | Colombia | 100 | 76 | 76.0% | 24 | 14.3 |
| Agosto | India | 153 | 128 | 83.7% | 25 | 21.9 |
| Septiembre (1-22) | Colombia | 104 | 43 | 41.3% | 61 | 14.9 |
| Septiembre (1-22) | India | 82 | 40 | 48.8% | 42 | 11.7 |
| Combinado | Colombia | 204 | 119 | 58.3% | 85 | 29.1 |
| Combinado | India | 235 | 168 | 71.5% | 67 | 33.6 |

India asigna mas volumen y cierra mas rapido en agosto. La brecha de cierre se achica en septiembre,
41.3% contra 48.8%. El cierre baja en ambos grupos en septiembre frente a agosto. La causa mas
probable es el corte del mes en curso, los tickets creados en los ultimos dias de septiembre no
tuvieron tiempo de cerrarse todavia. Confirma esto comparando contra backlog vivo, no contra
pendientes del periodo puro.

### Backlog vivo hoy, 22 sep 2026 (abiertos sin importar fecha de creacion)

| Grupo | Tickets abiertos hoy | Prom./persona |
|---|---|---|
| Colombia | 98 | 14.0 |
| India | 80 | 11.4 |
| Total | 178 | 12.7 |

### Estados de los tickets asignados en el periodo combinado

| Estado | Colombia | India | Total |
|---|---|---|---|
| Closed | 99 | 162 | 261 |
| Under Customer Review | 39 | 24 | 63 |
| Work in progress | 26 | 30 | 56 |
| Under Support Review | 14 | 7 | 21 |
| Completed | 19 | 1 | 20 |
| Waiting for Software Release | 3 | 3 | 6 |
| Duplicate | 1 | 5 | 6 |
| Accepted into Development | 0 | 2 | 2 |
| Resolution Suggested | 2 | 0 | 2 |
| Under CSM Review | 0 | 1 | 1 |
| Under Delivery Review | 1 | 0 | 1 |

Nota: Enrique Jimenez no tuvo tickets creados en agosto, los 10 de su cohorte combinada caen todos
en septiembre. Revisa si estuvo fuera o si el registro de asignacion tiene un hueco ahi.


## Rastro
2026-09-22 inbox/2026-09-22-informe-tickets-equipo-ago-sep.md

## APS legacy, a quien preguntar — 2026-09-24
_chunk 1948 · 2026-09-24 · fuente: inbox/2026-09-24-aps-legacy-contacto.md_

# APS legacy, a quien preguntar
Kiran Vadday, llamada del 24 sep 2026: no conoce APS. Jackson es quien lo trabajaba. Pocos clientes siguen en APS y la idea es salir de esa plataforma. Matt le dijo a Juan que Juan seria quien resuelve temas de APS.


## Rastro
2026-09-24 inbox/2026-09-24-aps-legacy-contacto.md

## facteus opinion dashboards — 2026-09-25
_chunk 1952 · 2026-09-25 · fuente: inbox/2026-09-25-facteus-opinion-dashboards.md_

Facteus, opinion on the dashboards for Viraj

Date 2026-09-25. What to say if Viraj asks what I think and what I'd suggest.

My take, neither dashboard means much until it's been checked against a real alert. They exist, Chris linked them in a comment, but nobody has confirmed either one actually reflects what happens when Facteus fires. Two dashboards with no live validation is worse than one, we'd be choosing between them blind.

What I'd suggest, three things.

Pick one as the source of truth for Support, not both. Two dashboards for the same thing means we'll end up checking the wrong one under pressure, or checking both and wasting time reconciling them.

Whichever one we pick, validate it the next time a real alert fires, or ask Data Engineering to walk us through what it looked like the last time one did. We shouldn't put a link in the Confluence pages that nobody's actually opened during an incident.

Once it's picked and validated, get it linked into the internal and external process pages directly. Right now it only lives in a Jira comment from August, that's why Support almost missed it. If it's not in the runbook, it doesn't exist for whoever's on call.


## Rastro
2026-09-25 inbox/2026-09-25-facteus-opinion-dashboards.md

## tickets por estado equipo colombia india septiembre — 2026-09-25
_chunk 1953 · 2026-09-25 · fuente: inbox/2026-09-25-tickets-por-estado-equipo-colombia-india-septiembre.md_

---
tema: tickets RCS creados en septiembre 2026 por equipo y estado
fecha: 2026-09-25
---

Conteo de tickets RCS con created >= 2026-09-01, agrupados por team Colombia y team India,
desglosados por estado: Complete, Closed, Under Customer Review (UCR), Under Support Review (USR),
Work in progress (WIP). Roster usado es el corregido de 14 personas en
brain/memoria/project_appriss_support_team.md (25 sep 2026).

## Totales por equipo, solo septiembre

| Equipo   | Complete | Closed | UCR | USR | WIP | Total |
|----------|----------|--------|-----|-----|-----|-------|
| Colombia | 0        | 57     | 23  | 9   | 21  | 110   |
| India    | 0        | 50     | 25  | 3   | 24  | 102   |

## Detalle por persona, solo septiembre

### Team Colombia

| Persona            | Complete | Closed | UCR | USR | WIP | Total |
|--------------------|----------|--------|-----|-----|-----|-------|
| Juan Martinez      | 0        | 2      | 3   | 2   | 2   | 9     |
| Diego Buelvas      | 0        | 17     | 5   | 0   | 0   | 22    |
| Sebastian Rueda    | 0        | 6      | 2   | 3   | 3   | 14    |
| Edwin Garzon       | 0        | 19     | 2   | 3   | 3   | 27    |
| Luis Hernandez     | 0        | 6      | 1   | 1   | 4   | 12    |
| Sebastian Garces   | 0        | 7      | 9   | 0   | 4   | 20    |
| Enrique Jimenez    | 0        | 0      | 1   | 0   | 5   | 6     |

### Team India

| Persona                  | Complete | Closed | UCR | USR | WIP | Total |
|---------------------------|----------|--------|-----|-----|-----|-------|
| Viraj Kansara             | 0        | 15     | 4   | 0   | 0   | 19    |
| Nikita Rathore            | 0        | 7      | 4   | 0   | 4   | 15    |
| Vedant Shirude            | 0        | 10     | 6   | 2   | 7   | 25    |
| Bikash Kumar              | 0        | 5      | 4   | 1   | 5   | 15    |
| Gulshan Kumar             | 0        | 1      | 0   | 0   | 0   | 1     |
| Megha Rathi               | 0        | 5      | 4   | 0   | 6   | 15    |
| Harini Shankarakrishnan   | 0        | 7      | 3   | 0   | 2   | 12    |

Nadie del equipo tiene tickets en estado Complete en septiembre.

Fuente: JQL project = RCS AND assignee = "<nombre>" AND created >= "2026-09-01" AND status in
(Complete, Closed, Under Customer Review, Under Support Review, Work in progress), corrida el
25 sep 2026 para las 14 personas del roster corregido. Ver
inbox/2026-09-25-tickets-por-estado-equipo-colombia-india.md para los totales sin filtro de fecha
y para la nota sobre la correccion del roster.


## Rastro
2026-09-25 inbox/2026-09-25-tickets-por-estado-equipo-colombia-india-septiembre.md

## Tickets por estado, equipo Colombia y equipo India, 25 sep 2026 — 2026-09-25
_chunk 1954 · 2026-09-25 · fuente: inbox/2026-09-25-tickets-por-estado-equipo-colombia-india.md_

# Tickets por estado, equipo Colombia y equipo India, 25 sep 2026

Jira en vivo, project RCS. Correccion sobre la corrida anterior del 25 sep: el roster usado tenia
solo 11 personas y venia de brain/memoria/project_appriss_support_team.md sin actualizar. Faltaban
Enrique Jimenez y Sebastian Garces en Colombia, Megha Rathi y Harini Shankarakrishnan en India, y
sobraba David Vargas, que ya salio del equipo, cero tickets y cero actividad en 60 dias. Roster real
de 14 verificado contra inbox/2026-09-22-informe-tickets-equipo-ago-sep.md y
inbox/2026-09-04-cosecha-carga-equipo-completo.md, y ya quedo corregido en
brain/memoria/project_appriss_support_team.md.

Estados: Complete, Closed, Under Customer Review, Under Support Review, Work in progress.
Nadie tiene tickets en Complete ahora mismo.

## Colombia (7)

Juan Martinez: Closed 31, Under Customer Review 10, Under Support Review 2, Work in progress 5
Diego Buelvas: Closed 77, Under Customer Review 8
Sebastian Rueda: Closed 27, Under Customer Review 5, Under Support Review 6, Work in progress 8
Edwin Garzon: Closed 46, Under Customer Review 6, Under Support Review 6, Work in progress 4
Luis Hernandez: Closed 8, Under Customer Review 1, Under Support Review 2, Work in progress 4
Sebastian Garces: Closed 13, Under Customer Review 9, Work in progress 4
Enrique Jimenez: Under Customer Review 1, Under Support Review 1, Work in progress 5

Totales Colombia: Closed 202, Under Customer Review 40, Under Support Review 17, Work in progress 30

## India (7)

Viraj Kansara: Closed 92, Under Customer Review 8
Nikita Rathore: Closed 44, Under Customer Review 9, Work in progress 6
Vedant Shirude: Closed 48, Under Customer Review 6, Under Support Review 2, Work in progress 7
Bikash Kumar: Closed 33, Under Customer Review 7, Under Support Review 1, Work in progress 8
Gulshan Kumar: Closed 28
Megha Rathi: Closed 9, Under Customer Review 4, Work in progress 6
Harini Shankarakrishnan: Closed 13, Under Customer Review 7, Work in progress 2

Totales India: Closed 267, Under Customer Review 41, Under Support Review 3, Work in progress 29


## Rastro
2026-09-25 inbox/2026-09-25-tickets-por-estado-equipo-colombia-india.md

## Hisense WD3S1543BT frente a Midea MF200D150WB/T-CO en Colombia — 2026-09-28
_chunk 1958 · 2026-09-28 · fuente: inbox/2026-09-28-lavasecadoras-colombia.md_

# Hisense WD3S1543BT frente a Midea MF200D150WB/T-CO en Colombia

Consulta: 28 de septiembre de 2026. Destino: compra doméstica en Bogotá. Investigación de fuentes públicas, sin llamadas ni solicitudes enviadas a marcas. El archivo adjunto aporta contexto y preguntas; sus especificaciones iniciales no constituyen hechos verificados.

## Decisión práctica

Elegiría Midea si la prioridad principal es la cobertura del equipo durante los primeros dos años y basta secar hasta 8 kg por tanda. Hisense merece consideración si necesitas mayor capacidad de secado, después de confirmar por escrito si la unidad entregada admite 10 kg. No encontré evidencia suficiente para declarar que una falla menos o que su servicio en Bogotá responde mejor.

La recomendación compara condiciones publicadas. No equivale a una prueba independiente de durabilidad.

## Comparación verificada y límites

| Criterio | Hisense WD3S1543BT | Midea MF200D150WB/T-CO | Ventaja |
|---|---|---|---|
| Lavado | 15 kg | 15 kg | Empate |
| Secado | 10 kg en ficha regional y Éxito; Falabella dice 9 kg | 8 kg en fabricante colombiano | Hisense, condicionada a placa y confirmación |
| Dimensiones, ancho × fondo × alto | 59,5 × 66 × 84,5 cm en fabricante colombiano | 59,5 × 59,5 × 85 cm | Midea para menor fondo nominal |
| Cobertura general publicada | 12 meses | 24 meses | Midea |
| Motor | 120 meses suplementarios, solo repuesto | 10 años anunciados; alcance adicional pendiente de certificado | Sin empate contractual demostrado |
| Vapor | Sí anunciado en Colombia | Steamcare anunciado en Colombia | Empate de función anunciada |
| Programas | 16 anunciados por fabricante colombiano | Éxito anuncia 20; manual enlazado no confirma ese total para /T-CO | Sin ganadora |
| Electricidad | Ficha regional: 115–127 V, 60 Hz | Ficha colombiana: 120 V, 60 Hz, 1250 W | No decide eficiencia |
| Consumo por ciclo completo | No verificado | No verificado | Sin ganadora |
| Ruido de variante colombiana | No verificado | No verificado | Sin ganadora |
| Confiabilidad y rapidez de reparación en Bogotá | Sin muestra suficiente | Sin muestra suficiente | Sin ganadora |

Fuentes: [Hisense Colombia](https://hisense.com.co/producto/lavadora-secadora-hisense-carga-frontal-3s-15-kg/), [Hisense regional](https://www.hisensecac.com/producto/hisense-lavadora-secadora-15kg-wd3s1543bt-2/), [Midea Colombia](https://www.midea.com/co/lavanderia/lavasecadora/lavasecadora-carga-frontal-15kg-healthguard.mf200d150wb-t-co), [Hisense Falabella](https://www.falabella.com.co/falabella-co/product/73215088/Lavadora-Secadora-Hisense-Electrica-15-kg-WD3S1543BT/73215088), [Hisense Éxito](https://www.exito.com/lavadora-secadora-hisense-electrica-15-kg-wd3s1543bt-titanium-gray-3192327/p).

Mide también conexiones, apertura de puerta y espacio de servicio. El fondo nominal no representa todo el espacio instalado.

## Garantía y atención en Colombia

Hisense Colombia S.A.S publica 12 meses generales y 120 meses para motor inverter. La cobertura suplementaria paga el repuesto; el cliente asume mano de obra y otros costos de sustitución. La política exige importación o distribución autorizada. Publica reparación en 30 días hábiles y suministro de repuestos básicos durante 12 meses tras la garantía, salvo disposiciones aplicables. Son condiciones publicadas, no tiempos observados ni inventario probado. [Política oficial](https://hisense.com.co/politica-de-garantia/).

Midea anuncia dos años totales y diez de motor. Falabella añade tina y habla de partes y componentes. No pude verificar el certificado específico colombiano que aclare mano de obra, desplazamientos y exclusiones de los años adicionales. Conserva la oferta y exige ese documento antes de pagar. [Fabricante](https://www.midea.com/co/lavanderia/lavasecadora/lavasecadora-carga-frontal-15kg-healthguard.mf200d150wb-t-co), [Falabella](https://www.falabella.com.co/falabella-co/product/73283971/Lavadora-Secadora-Midea-15Kg-MF200D150WB-T-CO/73283971).

| Canal oficial | Hisense | Midea |
|---|---|---|
| Bogotá | 601 357 0850 | 601 580 0207 |
| Nacional | 018000 114766 | No verificado |
| Correo | infocolombia@hisense.com | garantias.colombia@midea.com |
| Solicitud | Página de soporte | Formulario oficial de servicio |

Fuentes: [Soporte Hisense](https://hisense.com.co/soporte/), [Contacto Midea](https://www.midea.com/co/contacto), [Solicitud Midea](https://www.midea.com/co/contacto/iservice-request).

No confirmé un taller autorizado de lavado con dirección en Bogotá para ninguno. Pide que la marca asigne el taller y entregue número de orden. La página de Hisense separa centros de televisión, refrigeración y aire; esa lista no demuestra autorización para lavasecadoras. El localizador de Midea no devolvió resultados identificables en la consulta. No encontré tarifas públicas verificadas de visita fuera de garantía ni existencias locales de tarjetas, bombas, módulos de secado o seguros de puerta.

Una página denominada CSA Hisense Colombia anuncia instalación gratuita y atención domiciliaria para este modelo. Su alojamiento en Google Sites requiere confirmar vigencia y alcance directamente con la marca. [Referencia](https://sites.google.com/view/academia-de-servicio/lavado/lavasecadora/wd3s1543bt).

La campaña Hisense de cuatro años revisada corresponde a televisores seleccionados. No la apliques a esta lavasecadora. [Condiciones](https://hisense.com.co/tyc-demundialamundial/).

Midea publica un programa de satisfacción con registro, productos participantes y condiciones. No pude confirmar elegibilidad y plazo de esta compra concreta. No lo interpretes como prueba gratuita incondicional. [Programa oficial](https://www.midea.com/co/satisfaccion-garantizada).

## Testimonios y referencias que sí aportan información

Los relatos siguientes son declaraciones de usuarios. No verifiqué facturas ni expedientes de servicio. La fecha de una reseña no demuestra duración de uso.

| Referencia | Qué relata | Valor y límite |
|---|---|---|
| [Reddit Medellín, Hisense](https://www.reddit.com/r/medellin/comments/1kw13d2/1650000_es_buen_precio_por_un_televisor_de_60/) | Televisor averiado después de dos años; la marca reconoció cobertura de tres años y entregó bono para comprar en Falabella | Testimonio colombiano positivo de posventa. Producto y garantía distintos; no da días exactos |
| [Mercado Libre Colombia, Midea MF200](https://www.mercadolibre.com.co/lavasecadora-midea-carga-frontal15kg-healthguard-mf200d150wb-color-gris/p/MCO44957641) | 4,6/5 y 15 calificaciones; comentarios colombianos sobre relación precio y prendas casi secas | El catálogo mezcla países. No documenta reparaciones ni seis meses de uso |
| [Walmart México, Midea /W](https://www.walmart.com.mx/ip/lavasecadora-midea-carga-frontal-smart-dial-blanca-15-kg-8-kg-mf200d150wb-w/00694587833610) | Tania, 31 agosto 2024, compra verificada: secado de un grupo descrito de toallas en unas tres horas, frente a estimación inicial de 6:55 | Detalla carga y resultado; no p

## Rastro
2026-09-28 inbox/2026-09-28-lavasecadoras-colombia.md

## facteus confirmacion horario santhosh — 2026-09-29
_chunk 1960 · 2026-09-29 · fuente: inbox/2026-09-29-facteus-confirmacion-horario-santhosh.md_

Facteus, confirmar horario con Santhosh

Fecha 2026-09-29. Mañana miércoles 30, 11:00 AM Colombia equivale a 9:30 PM IST, dentro de su ventana.

```
Wednesday works well for us, 9:30 PM your time, which is 11 AM for me. I'll send the invite for 30
minutes.

Thanks,
Juan
```


## Rastro
2026-09-29 inbox/2026-09-29-facteus-confirmacion-horario-santhosh.md

## A quien escalar un agente de pipeline sin RAM o CPU — 2026-09-30
_chunk 1961 · 2026-09-30 · fuente: inbox/2026-09-30-contacto-agente-pipeline-sin-recursos.md_

# A quien escalar un agente de pipeline sin RAM o CPU

## Que pasa
Un equipo donde corre un pipeline ARDM de Azure DevOps se cuelga, con sospecha de falta de RAM o CPU.

## Respuesta
Confirmado. Contacto: Mike Tasch (Michael Tasch), Infra & Cloud Engineer, equipo de Peter Tuttle.
Es dueno de los agent pools de DataOps (prod_ardm1, prod_nonsas) y de las cajas DSPROD-LA01 a LA12.
Ruta formal desde un RCS: Under Infrastructure Review. El ticket queda a tu nombre y auto crea RETAILIT.

## Evidencia
1. RETAILIT-20895, 20721, 20713, 20425, 20777: todos asignados a Mike Tasch sobre agent pools y DSPROD.
2. Confluence RTS 478234214401, runbook de pipelines, patrones 3 y 8: lentitud por contencion de recursos y agente que abandona el job. Escalar a infra si se repite en la misma caja.
3. Confluence on-call: Infrastructure cubre CPU, memoria y disco. brain/memoria/reference_escalacion_l3_procedimiento.md.

## Que hago hoy
1. Del log del build, anota el nombre del agente (DSPROD-LAxx o VM Azure), build ID y hora de la ultima linea.
2. Revisa config_control por un STARTED huerfano antes de relanzar (patron 6).
3. Escribe a Mike por Teams. Si hay RCS, transiciona a Under Infrastructure Review.
4. Peyman Motlagh en copia si el pipeline es de Secure 5, el runbook lo nombra como destinatario del estado.

## Contexto que cambia el diagnostico
RETAILIT-20721 mueve prod_ardm1 de agentes SAS on prem a VMs Azure. RETAILIT-20713 decomisiona DSPROD-LA01 a LA12, en hold hasta 09-28. Menos agentes o VMs mas chicas pueden explicar la contencion.
Si la maquina es VisualCron o LPMS, el dueno tambien es Infra (RETAILIT-20742, Mike Tasch con Matt K).

## Borrador Teams
Hi Mike, quick question. The agent running <pipeline name> (build <ID>) seems to be hanging, and it looks like it may be running out of memory or CPU. Last log line was at <time> on <agent name>. Is this something your team can take a look at, or should I route it somewhere else? Could it be related to the prod_ardm1 agent pool changes, or am I reading this wrong?

## Compromisos
Ninguno abierto.


## Rastro
2026-09-30 inbox/2026-09-30-contacto-agente-pipeline-sin-recursos.md

## facteus preguntas l1 — 2026-10-07
_chunk 1968 · 2026-10-07 · fuente: inbox/2026-10-07-facteus-preguntas-l1.md_

Facteus, las tres preguntas que dejó L1 en la llamada

Fecha 2026-10-07. Separadas por a quién le corresponde contestarlas.

Pregunta 1, es para Chris, no para Support

Si un cliente deja de enviar datos por un problema de su lado, ¿ese cliente sigue generando alerta a través de Facteus?

La plantilla del ticket de Missing Clients sí trae una variable por cliente, {{ $labels.customer }}, además de staleness_hours y drop_ratio, así que el mecanismo está pensado para alertar por cliente individual, no solo de forma agregada. Pero el umbral exacto que dispara la alerta, el valor de drop_ratio y cuántas horas de staleness por encima de las 26 ya cuentan como problema, nunca quedó confirmado por Chris. Esto se señaló en la revisión del 22 de septiembre y quedó pendiente, no se volvió a preguntar en los correos del 26 ni del 29, que se enfocaron en SLA, horario, escalación y dashboards. Sin ese número, no se puede responder con certeza si el caso que describe L1 dispara la alerta o no. Hay que devolverle esto a Chris.

Preguntas 2 y 3, son decisión de Support, no de Chris

Si llega un correo o alerta de Facteus por un problema de cliente, ¿se debe escalar siempre primero a L2? Y si el cliente reporta el problema directamente como urgente, ¿también se escala a L2?

El árbol de decisión que ya documentó Data Engineering no tiene ningún paso de L2, las alertas internas y los correos externos van directo a Data Engineering por la ruta de Jira Operations. Meter a L2 en el medio sería una capa nueva que Support decide agregar, no algo que Chris tenga que aprobar ni definir. La pregunta real para resolver con Camila y Viraj es si L1 triagea y manda directo a Data Engineering como está documentado hoy, o si quieren que L2 revise primero antes de escalar, y si la urgencia reportada directamente por el cliente cambia esa regla.

Qué hacer con esto

La pregunta 1 se suma a la lista de cosas por confirmar con Chris, junto con el umbral de drop_ratio que ya estaba pendiente desde el 22 de septiembre. Las preguntas 2 y 3 hay que resolverlas internamente antes de decirle nada a L1, no tiene sentido devolverles una respuesta a medias.


## Rastro
2026-10-07 inbox/2026-10-07-facteus-preguntas-l1.md

## SnowTime Migration: lista de clientes del despliegue del 8 de octubre — 2026-10-07
_chunk 1973 · 2026-10-07 · fuente: inbox/2026-10-07-snowtime-migration-lista-despliegue-8oct.md_

# SnowTime Migration: lista de clientes del despliegue del 8 de octubre

Fuente: captura del chat de Teams "SnowTime Migration Checkin" (22 miembros), mensaje de Sofia Sandner del 2026-10-07 1:23 p.m. Bogota. Tres reacciones de pulgar arriba.

Lista del despliegue del 8 de octubre

Locked in (confirmados)
ELC 225
DBI 80 (engage)
CWH 248

Confirmed by EOD (se confirman al final del dia del 7 de octubre)
GAP 049 (engage, facteus)
TBI 209
RLC 57 (facteus)
CES 439
PHA 140

Formato: CODIGO DE CLIENTE seguido del numero de cliente en la base de datos (por ejemplo ELC 225 es el cliente ELC con ID 225 en la DB). Los parentesis marcan productos: engage y facteus.

Accion pedida
Sofia pidio a Camila Cortes que asegure que estos clientes reciban notificacion.

Readiness del go-live de manana (resumen del chat)
1. Client list: Sofia publica la lista locked, pending y la confirmacion de fin de dia, y luego envia la solicitud de comunicaciones a Camila.
2. Readiness target: mover todo cliente de desarrollo restante a parallel run antes del 19 de octubre, para tener cinco dias habiles de validacion y mitigacion.
3. Victoria's Secret: verificar que los rolling reports y otras adiciones downstream esten incluidos en la validacion en paralelo.

Uso futuro
Si un ticket RCS menciona SnowTime, migracion, parallel run o alguno de estos codigos (ELC, DBI, CWH, GAP, TBI, RLC, CES, PHA), este archivo dice si el cliente estaba en la ola del 8 de octubre y en que estado (locked o confirmado por EOD).
Si Victoria's Secret reporta diferencias en rolling reports, el chequeo en parallel run era compromiso explicito del equipo de migracion.


## Rastro
2026-10-07 inbox/2026-10-07-snowtime-migration-lista-despliegue-8oct.md

## L2 to L3 RCS ticket management: conocimiento contrastado — 2026-10-13
_chunk 1977 · 2026-10-13 · fuente: inbox/2026-10-13-l2-l3-rcs-ticket-management.md_

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

Comentario 477582852097, crea

## Rastro
2026-10-13 inbox/2026-10-13-l2-l3-rcs-ticket-management.md

## RCS-23834. Ubicación de Manager Dashboard — 2026-10-15
_chunk 1978 · 2026-10-15 · fuente: inbox/2026-10-15-manager-dashboard-ubicacion.md_

Ticket RCS-23834. Trabajado el 2026-10-15. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
dónde encontrar Manager Dashboard en Jira, Confluence o Cerebro. Hallazgo confirmado en la descripción consultada en vivo de RCS-23834, THD - Dashboard Reassignment: existe una referencia a CIT Manager Dashboard y el solicitante pide reasignar su propiedad para editarlo. Esto no confirma los permisos ni el propietario actuales.

## Rastro
2026-10-15 inbox/2026-10-15-manager-dashboard-ubicacion.md

## RCS-26420. RCS-26420 A quien pasar el cambio de pipeline y el borrado de duplicados — 2026-10-14
_chunk 1979 · 2026-10-14 · fuente: inbox/2026-10-14-rcs-26420.md_

Ticket RCS-26420. Trabajado el 2026-10-14. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Que pasa Sebas confirmo la causa en datos de produccion de ardm_057 y necesita dos acciones que Support no ejecuta: corregir StandardScripts.transfer (appriss_ardm/queries.py) y borrar unas 31.5M filas de ardm_operatoraction y 55.8M de ardm_document. Work in progress, asignado a Garces, label 60daysopen. Causa CONFIRMADA por Sebas, comentario del 13 oct.

## Rastro
2026-10-14 inbox/2026-10-14-rcs-26420.md

## RCS-28240. Conteo (13 tickets tuyos abiertos): nivel 1: 1 · nivel 2: 5 · nivel 3: 7 · nivel 4: 0. Días = desde el último — 2026-10-15
_chunk 1980 · 2026-10-15 · fuente: inbox/2026-09-09-diagnostico-promesa-condicionada-y-nivel-4.md;2026-09-16-rcs-28240-revision-cola.md;2026-09-28-rcs-28240-prioridad-auditoria.md;2026-10-15-resumen-manana.md_

Ticket RCS-28240. Trabajado el 2026-09-09 a 2026-10-15. 4 notas en inbox.

## Que pasa
[2026-09-09] El clasificador decidia entre pedido y promesa por posicion en el texto: `p_preg > p_prom`.
Juan cierra sus comentarios con cortesia, asi que la promesa queda siempre al final y gana.
Los dos tickets subian a PROMESA SIN CUMPLIR con el cliente debiendo datos.
[2026-10-15] Conteo (13 tickets tuyos abiertos): nivel 1: 1 · nivel 2: 5 · nivel 3: 7 · nivel 4: 0.
Días = desde el último comentario de Appriss.

Nivel 1, te toca responder
RCS-28240 United/Albertsons, Medium, 2 días. Emma respondió el 13 oct. Hoy: acusar recibo, mantener abierto.
Cerebro: inbox/2026-09-28-rcs-28240-prioridad-auditoria.md, SSO pendiente de IT de United (AADSTS previos a Appriss).

Nivel 2, promesa abierta
RCS-28881 NEXCOM, Medium, 6 días. Hoy: publicar resultado sesión 13 oct.
Cerebro: bitacora/RCS-28881.md (8 oct, pendiente con Matt: lock de sesión ASP). Auditoría del cliente 19 oct.
RCS-29205 Starbucks, High, 1 día. Hoy: verificar rebuild antes de escribir.
Cerebro: inbox/2026-10-14-rcs-29205-verificacion-resultado.md, desplegado pero no aplicado, rebuild espera rol admin.
RCS-29054 Big 5, Medium, 1 día. Hoy: seguir carga del archivo UKG.
Cerebro: inbox/2026-10-06-rcs-29054-conclusion-llamada.md, causa UKG; prometiste publicar el resultado.
RCS-29437 VF Corp (interno, Paul), Medium, 1 día. Hoy: pedir a Austin reenviar invitación.
Cerebro: inbox/2026-10-14-rcs-29437.md, cuenta Invited sin aceptar más solicitud de acceso pendiente.
RCS-29435 Starbucks, Low, 1 día. Hoy: investi

## Evidencia
RCS-28240  p_prom 542  p_preg -1   antes nivel 2, real 3
    RCS-28351  p_prom 308  p_preg -1   antes nivel 2, real 3
    RCS-28342  p_prom -1   p_preg -1   antes nivel 4, real 2
    niveles antes:   2=3 3=5 4=11      exactitud 13/13
    niveles despues: 2=1 3=8 4=10      exactitud 13/13

## Rastro
2026-09-09 inbox/2026-09-09-diagnostico-promesa-condicionada-y-nivel-4.md
2026-09-16 inbox/2026-09-16-rcs-28240-revision-cola.md
2026-09-28 inbox/2026-09-28-rcs-28240-prioridad-auditoria.md
2026-10-15 inbox/2026-10-15-resumen-manana.md

## RCS-28256. Cola del 1 sep 2026, refresco automatico — 2026-10-14
_chunk 1981 · 2026-10-14 · fuente: inbox/2026-09-01-cola.md;2026-09-16-rcs-28256-confirmacion-cliente.md;2026-09-16-rcs-28256-revision-cola.md;2026-09-24-rcs-28256-auditoria-avance.md;2026-09-25-rcs-28256.md;2026-09-28-rcs-28256.md;2026-10-14-rcs-28256-paso-a-paso.md;2026-10-14-rcs-28256-resultado-feed.md;2026-10-14-rcs-28256-revision-profunda.md;2026-10-14-rcs-28256.md_

Ticket RCS-28256. Trabajado el 2026-09-01 a 2026-10-14. 10 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Que pasa El ticket mezcla tres problemas. La lentitud Secure a Incident vive ahora en https://trebuco.atlassian.net/browse/ENG-9990 (Backlog, Medium, sin asignar, descripcion sin hallazgos). Los accesos individuales (Paul Bubelnik Jr, Chris Orth, Chaz Hyman, Nancy Bolhoff) los resuelve Soporte segun Matthew Kamminga. Teagle pidio en el hilo Secure Incident ID Choose a Value que alguien revise RCS-28256, RCS-27269, RCS-27578 y RCS-27941 y conteste ahi.

## Rastro
2026-09-01 inbox/2026-09-01-cola.md
2026-09-16 inbox/2026-09-16-rcs-28256-confirmacion-cliente.md
2026-09-16 inbox/2026-09-16-rcs-28256-revision-cola.md
2026-09-24 inbox/2026-09-24-rcs-28256-auditoria-avance.md
2026-09-25 inbox/2026-09-25-rcs-28256.md
2026-09-28 inbox/2026-09-28-rcs-28256.md
2026-10-14 inbox/2026-10-14-rcs-28256-paso-a-paso.md
2026-10-14 inbox/2026-10-14-rcs-28256-resultado-feed.md
2026-10-14 inbox/2026-10-14-rcs-28256-revision-profunda.md
2026-10-14 inbox/2026-10-14-rcs-28256.md

## RCS-29104. GPC, c356_gpc en GP11, investiga refunds fraudulentos del cajero 1037 en CHA266 y Secure no muestra el medio d — 2026-10-14
_chunk 1983 · 2026-10-14 · fuente: inbox/2026-09-24-rcs-29104.md;2026-09-28-rcs-29104-prioridad-auditoria.md;2026-10-07-rcs-29104-evaluacion-talos.md;2026-10-14-cerebro-v2-1.md_

Ticket RCS-29104. Trabajado el 2026-09-24 a 2026-10-14. 4 notas en inbox.

## Que pasa
GPC, c356_gpc en GP11, investiga refunds fraudulentos del cajero 1037 en CHA266 y Secure no muestra el medio de pago. El hueco no es de refunds ni del cajero: una parte grande de la cadena carga sin filas en ardm_tender. Jira: Under Support Review, High, Juan.

## Evidencia
1. TXN 2609179617330521193: HEADER 1, ITEM 2, TENDER 0 en Snowflake ARDMPROD.ARDM_356 y en GP11 ardm_356. Header cuadra con la factura: -450.47, tax -28.48. totaltendercount NULL.
2. Tienda de CHA266, 1 al 22 sep: ~1000 headers, 1 sola transaccion con tender.
3. GP11 14 al 20 sep por tienda: sin tender 834 tiendas y 356710 headers; bajo 819 y 475720; normal 4033 y 1516936.

## Precedentes
RCS-28632 NAPA GPC c356, backload y load log, confluence/RTS-triage/RCS-28632-napa-work-items-detenidos.md
RCS-28649 Home Depot, header sin item ni tender, confluence/RTS-triage/RCS-28649-home-depot-item-tender-detail-missing.md
RCS-28834 ICA, busquedas header driven con LEFT JOIN a tender, confluence/RTS-triage/RCS-28834-ica-bank-withdrawal-deposit.md

## Rastro
2026-09-24 inbox/2026-09-24-rcs-29104.md
2026-09-28 inbox/2026-09-28-rcs-29104-prioridad-auditoria.md
2026-10-07 inbox/2026-10-07-rcs-29104-evaluacion-talos.md
2026-10-14 inbox/2026-10-14-cerebro-v2-1.md

## RCS-29195. Holly, 6 oct 9:50 AM ET: el correo no llego y la Smart Alert History de 26-288-15 esta en blanco. No hay fila — 2026-10-14
_chunk 1984 · 2026-10-14 · fuente: inbox/2026-09-30-rcs-29195-paso-a-paso.md;2026-09-30-rcs-29195.md;2026-10-01-rcs-29195-guion-llamada-diego.md;2026-10-06-rcs-29195-guia-diagnostico.md;2026-10-07-rcs-29195-evaluacion-talos.md;2026-10-14-login-legacy-url-1password.md_

Ticket RCS-29195. Trabajado el 2026-09-30 a 2026-10-14. 6 notas en inbox.

## Que pasa
[2026-09-30] Holly Garcia, dominio gimi.org, reporta que las Smart Alerts de Property Damage no salen, con el caso 26-288-15 como ejemplo. Work in progress, assignee Diego Buelvas, creado 30 sep 11:11 ET.
[2026-10-06] Holly, 6 oct 9:50 AM ET: el correo no llego y la Smart Alert History de 26-288-15 esta en blanco. No hay fila en SmartAlertProcess. Tenant 387 gwmek sin confirmar contra gimi.org.

## Evidencia
Jira, Talos 30 sep 11:23: sin falla de plataforma, sugiere revisar config y traza del caso. No es evidencia.
Control Panel USPROD: clientId 387, goodwill.org, slug gwmek. Dominio de Holly gimi.org, validar en Contacts.
Fix PR 58273 en US prod desde 28 sep, inbox/2026-09-28-smart-alerts-mecanismo-8-deadlock.md.

## Precedentes
Guia v2: flujos/smart-alert-disparo-manual.md
Lectura de Grafana: inbox/2026-09-28-grafana-smart-alerts-lectura.md
Mecanismos 1 a 7: investigaciones/smart-alerts-familia-de-fallas.md
Mecanismo 8: inbox/2026-09-28-smart-alerts-mecanismo-8-deadlock.md
Cuelgue en 12b, Stater Bros: inbox/2026-09-30-rcs-28534-grafana-hallazgos.md

## Rastro
2026-09-30 inbox/2026-09-30-rcs-29195-paso-a-paso.md
2026-09-30 inbox/2026-09-30-rcs-29195.md
2026-10-01 inbox/2026-10-01-rcs-29195-guion-llamada-diego.md
2026-10-06 inbox/2026-10-06-rcs-29195-guia-diagnostico.md
2026-10-07 inbox/2026-10-07-rcs-29195-evaluacion-talos.md
2026-10-14 inbox/2026-10-14-login-legacy-url-1password.md

## RCS-29205. Starbucks NA reporta cero resultados en el run mensual del 29 sep para esta definicion. Jira: Under Support Re — 2026-10-14
_chunk 1985 · 2026-10-14 · fuente: inbox/2026-09-30-rcs-29205.md;2026-09-30-sbx-work-items-hallazgos-paso2.md;2026-09-30-sbx-work-items-paso-a-paso.md;2026-10-01-rcs-29205-paquete.md;2026-10-02-rcs-29205-escalacion-delivery.md;2026-10-02-sbx-work-items-escalacion-estado.md;2026-10-07-mejoras-flujo-soporte.md;2026-10-07-rcs-29205-evaluacion-talos.md;2026-10-07-sbx-work-items-estado.md;2026-10-07-talos-evaluacion-en-curso.md;2026-10-08-rcs_

Ticket RCS-29205. Trabajado el 2026-09-30 a 2026-10-14. 17 notas en inbox.

## Que pasa
Starbucks NA reporta cero resultados en el run mensual del 29 sep para esta definicion. Jira: Under Support Review, High, asignado a Juan, sin respuesta sustantiva al cliente.

## Evidencia
[2026-10-09] RCS-29205: Work in progress, Juan. Ultimo comentario 8 oct 11:21 (avance al cliente). Sin nota interna sobre el branch de Ryan. Falta avance diario 9 oct.
RCS-29206: Under Customer Review. Juan publico seguimiento generico 9 oct 13:31. Automation aviso 7 dias sin respuesta el 8 oct.
RCS-29207: Completed desde 6 oct, falta Closed.
Pendiente confirmar si se enviaron los Teams del 8 oct a Ryan (cierre) y a Anushka/Adarsh (branch).

Teams del 8 oct a Ryan y a Anushka/Adarsh: enviados.
Anushka, 8 oct 11:00: el branch de Ryan ayuda; enrich_ardm_tender requiere cambios de mapeo; ella sube el PR; el rebuild necesita rol admin que ella no tiene, pedira a alguien tras el deploy.
Anushka, 9 oct 12:35: PR 58962 (achaudhary/c166_rcs29205_token_paidinout) con paid in/out, arreglos al acumulador de Ryan (column_spec, fuente prod, NULL en vez de FALSE, aproximacion x_refundtoown) y RCS-29205_fix_summary.md. Pide revision de Juan antes de deploy y rebuild.
Juan, 9 oct 12:42: preguntas antes de aprobar: validacion en lab, tokens ligados despues de la transaccion (seed hasta 26 ago, rebuild desde 22 ago, chunks diarios), paid in/out desde 26 ago cubre eventos desde 25 ago, aproximacion x_refundtoown 
[2026-10-14] RCS-29205: Work in progress, Juan. Sin actualizacion desde el 9 oct 14:04; faltaron avances diarios del 12 y 13 oct.
Anushka respondio la revision del PR 58962: validado en lab; seed corregido a 21 ago y rebuild de tender dia por dia (~0.3% de tokens pueden diferir de pyardm); paid in/out desde 26 ago cubre 25 ago y rehace ardm_json; x_refundtoown aproximacion ~6 filas/semana, con firma del dueno o documentada. Seed, rebuild y recarga los corre un operador con rol admin. Pide a Juan verificar la regeneracion de work items 24 ago a 27 sep.
Duda abierta: la corrida del periodo termino con 0 filas (no fallo), puede no regenerarse sola.
RCS-29206: Completed el 13 oct. RCS-29207: Completed, falta Closed.

## Que sigue
[2026-10-01] 1. Con el nombre del dueño, el ticket va a ese equipo. Es un mapeo de datos en producción, así que lo más probable es Delivery o el equipo de SnowTime que hizo el cutover. En RCS-28671 de THD ese equipo fue el de Dan Endersby.
2. Cuando lo arreglen, falta una pregunta para el mismo equipo: si recargan el campo en los refunds del 27 ago en adelante. Sin recarga, el periodo 24 ago a 27 sep sigue en cero aunque el mapeo quede bien.
3. Después, la corrida del periodo hay que repetirla. El rerun por WISC no crea duplicados aquí porque el periodo está vacío.
[2026-10-07] El documento investigaciones/SBX-snowtime-work-items-mensuales-cero.md conserva hipótesis del 30 septiembre. Ya existen tres resultados distintos: campo sin valores en 29205, cero compatible con los umbrales en 29206 y comparación numérica fallida en 29207. Una búsqueda todavía puede recuperar el documento inicial sin las tres correcciones.

Propuesta: conservar historia y añadir relaciones explícitas entre afirmaciones: contradice, sustituye, confirma o limita. Guardar fecha del evento y fecha de publicación por separado. Al recuperar una afirmación antigua, cargar su corrección y fuente juntas. Una fecha reciente no convierte un borrador en hecho. Criterio de aceptación: preguntar por la causa de cada uno de los tres tickets devuelve su mecanismo propio y las salvedades de validación, nunca una causa compartida por coaparición.

RCS-29231 demuestra por qué importa: el análisis del 2 octubre recomendó tratar x_rcpt_count como texto; la corrección del 5 octubre cuestionó el mapeo posicional y explicó que cambiar el predicado podía eliminar el error destruyendo el significado del reporte. Fuente: comentarios 3375965 y 3381773. La nota local del 2 octubre también proponía NULLIF ante

## Precedentes
RCS-28873 SBX, catalogo desincronizado tras cutover, tickets/RCS-28873.md
RCS-28848 SBX, filtro memberid contra x_memberid, Gabor 17 sep
RTS-206268 Kinney, placeholder X_ siempre NULL, confluence/RTS-triage/RTS-206268-kinney-drugs-pos-articleid.md
RCS-28671 THD, WISC no regenera por dedup, tickets/RCS-28671.md

## Rastro
2026-09-30 inbox/2026-09-30-rcs-29205.md
2026-09-30 inbox/2026-09-30-sbx-work-items-hallazgos-paso2.md
2026-09-30 inbox/2026-09-30-sbx-work-items-paso-a-paso.md
2026-10-01 inbox/2026-10-01-rcs-29205-paquete.md
2026-10-02 inbox/2026-10-02-rcs-29205-escalacion-delivery.md
2026-10-02 inbox/2026-10-02-sbx-work-items-escalacion-estado.md
2026-10-07 inbox/2026-10-07-mejoras-flujo-soporte.md
2026-10-07 inbox/2026-10-07-rcs-29205-evaluacion-talos.md
2026-10-07 inbox/2026-10-07-sbx-work-items-estado.md
2026-10-07 inbox/2026-10-07-talos-evaluacion-en-curso.md
2026-10-08 inbox/2026-10-08-rcs-29205-analisis-branch-ryan.md
2026-10-08 inbox/2026-10-08-sbx-work-items-estado.md
2026-10-09 inbox/2026-10-09-rcs-29205-revision-pr-58962.md
2026-10-09 inbox/2026-10-09-sbx-work-items-estado.md
2026-10-14 inbox/2026-10-14-rcs-29205-como-saber-que-esta-done.md
2026-10-14 inbox/2026-10-14-rcs-29205-verificacion-resultado.md
2026-10-14 inbox/2026-10-14-sbx-work-items-estado.md

## RCS-29224. AAP pide mover el inicio del envio de STRINVDT (inventory) de 1:30 AM EST a 9:30 AM EST y pregunta el impacto — 2026-10-14
_chunk 1986 · 2026-10-14 · fuente: inbox/2026-10-08-rcs-29224.md;2026-10-13-rcs-29224-avance-validado.md;2026-10-13-rcs-29224-hallazgos-repo.md;2026-10-13-rcs-29224-hallazgos-snowflake.md;2026-10-13-rcs-29224-resumen.md;2026-10-13-rcs-29224.md;2026-10-14-rcs-29224-alcance-actualizado.md;2026-10-14-rcs-29224-regresion-resultado.md_

Ticket RCS-29224. Trabajado el 2026-10-08 a 2026-10-14. 8 notas en inbox.

## Que pasa
AAP pide mover el inicio del envio de STRINVDT (inventory) de 1:30 AM EST a 9:30 AM EST y pregunta el impacto en la ingesta. Jira: Escalated, Enrique, sin respuesta tecnica al cliente. El cambio de AAP aun no ocurrio ("We would change", Tim Young, 30 sep).

## Evidencia
1. Correo de Tim Young, 30 sep (adjunto .msg): los archivos salen poco despues de 1:30 AM EST y STRINVDT llega "much later", "likely already lagging a day". La recepcion real no es 1:30.
2. Captura de AAP, anterior al 7 oct 14:35 UTC: POS llega a 10/6. Inventario llega a 10/7 con 3145 tiendas y 532M filas, contra 5391 tiendas y 935M del 10/6. El 10/7 estaba incompleto.
3. RCS-29224, Shireesh Ramdas, 1 oct: "AAP is being moved to SnowTime". La causa que Enrique dio a AAP en RCS-29244 cita a Daniel Endersby y no tiene evidencia propia.

## Precedentes
RCS-29244 AAP, mismo cliente, Completed 8 oct, Jira.
RCS-27837 Ollie's, file_registry para separar retraso de archivo y de pipeline, Confluence RTS 478054547467.
RCS-28126 Kinney, aviso de cambio de feed, db:knowledge_chunks/1444.

## Rastro
2026-10-08 inbox/2026-10-08-rcs-29224.md
2026-10-13 inbox/2026-10-13-rcs-29224-avance-validado.md
2026-10-13 inbox/2026-10-13-rcs-29224-hallazgos-repo.md
2026-10-13 inbox/2026-10-13-rcs-29224-hallazgos-snowflake.md
2026-10-13 inbox/2026-10-13-rcs-29224-resumen.md
2026-10-13 inbox/2026-10-13-rcs-29224.md
2026-10-14 inbox/2026-10-14-rcs-29224-alcance-actualizado.md
2026-10-14 inbox/2026-10-14-rcs-29224-regresion-resultado.md

## RCS-29394. RCS-29394 PPG, Smart Alerts sin generar y ajuste al reporte Audit Schedule — 2026-10-14
_chunk 1987 · 2026-10-14 · fuente: inbox/2026-10-14-rcs-29394.md_

Ticket RCS-29394. Trabajado el 2026-10-14. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Que pasa Annie Brown (PPG) pide dos cosas. Las Smart Alerts de auditoria no se generan solas y Tyrone no le responde hace tiempo. El reporte Audit Schedule 2 necesita un par de filtros para igualar el original. Ofrece llamada de Teams con pantalla compartida.

## Rastro
2026-10-14 inbox/2026-10-14-rcs-29394.md

## RCS-29437. RCS-29437 VF Corp, usuario sin acceso al portal (relación con RCS-29436) — 2026-10-14
_chunk 1988 · 2026-10-14 · fuente: inbox/2026-10-14-rcs-29437.md_

Ticket RCS-29437. Trabajado el 2026-10-14. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Qué pasa Zachary Brinkman (zachary_brinkman@vfc.com) no entra al portal. Help Center lo manda a Jira y Jira dice "you've already requested access". La organización VF Corp lo muestra como Invited. El reenvío de invitación falla con "You don't have permission to invite customers to this service space".

## Rastro
2026-10-14 inbox/2026-10-14-rcs-29437.md

## ENG-10069. Contiene información interna y no sirve para hablar con el cliente. Sustituido por investigaciones/2026-10-16- — 2026-10-16
_chunk 1999 · 2026-10-16 · fuente: inbox/2026-10-16-eng-10069-guion-llamada.md_

Ticket ENG-10069. Trabajado el 2026-10-16. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Contiene información interna y no sirve para hablar con el cliente. Sustituido por investigaciones/2026-10-16-tailored-guion-cliente-v2.md. Desarrollo del defecto de primer ingreso. Guion bilingüe, 16 octubre 2026.

## Rastro
2026-10-16 inbox/2026-10-16-eng-10069-guion-llamada.md

## ENG-7824. Contiene información interna y no sirve para hablar con el cliente. Sustituido por investigaciones/2026-10-16- — 2026-10-16
_chunk 2000 · 2026-10-16 · fuente: inbox/2026-10-16-eng-7824-guion-llamada.md_

Ticket ENG-7824. Trabajado el 2026-10-16. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Contiene información interna y no sirve para hablar con el cliente. Sustituido por investigaciones/2026-10-16-tailored-guion-cliente-v2.md. Engineering del caso de búsquedas HR. Guion bilingüe, 16 octubre 2026.

## Rastro
2026-10-16 inbox/2026-10-16-eng-7824-guion-llamada.md

## ENG-9990. Contiene información interna y no sirve para hablar con el cliente. Sustituido por investigaciones/2026-10-16- — 2026-10-16
_chunk 2001 · 2026-10-16 · fuente: inbox/2026-10-16-eng-9990-guion-llamada.md_

Ticket ENG-9990. Trabajado el 2026-10-16. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Contiene información interna y no sirve para hablar con el cliente. Sustituido por investigaciones/2026-10-16-tailored-guion-cliente-v2.md. Desarrollo de rendimiento. Guion bilingüe, 16 octubre 2026.

## Rastro
2026-10-16 inbox/2026-10-16-eng-9990-guion-llamada.md

## RCS-26519. Contiene información interna y no sirve para hablar con el cliente. Sustituido por investigaciones/2026-10-16- — 2026-10-16
_chunk 2002 · 2026-10-16 · fuente: inbox/2026-10-16-rcs-26519-guion-llamada-v2.md;2026-10-16-rcs-26519-guion-llamada-v3.md;2026-10-16-rcs-26519-guion-llamada.md_

Ticket RCS-26519. Trabajado el 2026-10-16. 3 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Contiene información interna y no sirve para hablar con el cliente. Sustituido por investigaciones/2026-10-16-tailored-guion-cliente-v2.md. permisos de Incident tras unificación. Guion bilingüe, 16 octubre 2026.

## Rastro
2026-10-16 inbox/2026-10-16-rcs-26519-guion-llamada-v2.md
2026-10-16 inbox/2026-10-16-rcs-26519-guion-llamada-v3.md
2026-10-16 inbox/2026-10-16-rcs-26519-guion-llamada.md

## RCS-26584. Contiene información interna y no sirve para hablar con el cliente. Sustituido por investigaciones/2026-10-16- — 2026-10-16
_chunk 2003 · 2026-10-16 · fuente: inbox/2026-10-16-rcs-26584-guion-llamada-v2.md;2026-10-16-rcs-26584-guion-llamada-v3.md;2026-10-16-rcs-26584-guion-llamada.md_

Ticket RCS-26584. Trabajado el 2026-10-16. 3 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Contiene información interna y no sirve para hablar con el cliente. Sustituido por investigaciones/2026-10-16-tailored-guion-cliente-v2.md. Guion bilingüe, 16 octubre 2026. ENGLISH This was an earlier search-access issue for Beverly and Francesca.

## Rastro
2026-10-16 inbox/2026-10-16-rcs-26584-guion-llamada-v2.md
2026-10-16 inbox/2026-10-16-rcs-26584-guion-llamada-v3.md
2026-10-16 inbox/2026-10-16-rcs-26584-guion-llamada.md

## RCS-27325. Contiene información interna y no sirve para hablar con el cliente. Sustituido por investigaciones/2026-10-16- — 2026-10-16
_chunk 2005 · 2026-10-16 · fuente: inbox/2026-10-16-rcs-27325-guion-llamada-v2.md;2026-10-16-rcs-27325-guion-llamada-v3.md;2026-10-16-rcs-27325-guion-llamada.md_

Ticket RCS-27325. Trabajado el 2026-10-16. 3 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Contiene información interna y no sirve para hablar con el cliente. Sustituido por investigaciones/2026-10-16-tailored-guion-cliente-v2.md. Traslados de tienda y jerarquía. Guion bilingüe, 16 octubre 2026.

## Rastro
2026-10-16 inbox/2026-10-16-rcs-27325-guion-llamada-v2.md
2026-10-16 inbox/2026-10-16-rcs-27325-guion-llamada-v3.md
2026-10-16 inbox/2026-10-16-rcs-27325-guion-llamada.md

## RCS-28157. Contiene información interna y no sirve para hablar con el cliente. Sustituido por investigaciones/2026-10-16- — 2026-10-16
_chunk 2008 · 2026-10-16 · fuente: inbox/2026-10-16-rcs-28157-guion-llamada-v2.md;2026-10-16-rcs-28157-guion-llamada-v3.md;2026-10-16-rcs-28157-guion-llamada.md_

Ticket RCS-28157. Trabajado el 2026-10-16. 3 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Contiene información interna y no sirve para hablar con el cliente. Sustituido por investigaciones/2026-10-16-tailored-guion-cliente-v2.md. Guion bilingüe, 16 octubre 2026. ENGLISH This ticket was a request to change an individual case number from INT to INC.

## Rastro
2026-10-16 inbox/2026-10-16-rcs-28157-guion-llamada-v2.md
2026-10-16 inbox/2026-10-16-rcs-28157-guion-llamada-v3.md
2026-10-16 inbox/2026-10-16-rcs-28157-guion-llamada.md

## RCS-28452. Qué pasa SpartanNash recibe PDF con TempArea unido al nombre. Under Support Review, Sebastián Rueda — 2026-10-15
_chunk 2010 · 2026-10-15 · fuente: inbox/2026-10-15-rcs-28452-desbloqueo.md_

Ticket RCS-28452. Trabajado el 2026-10-15. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Qué pasa SpartanNash recibe PDF con TempArea unido al nombre. Under Support Review, Sebastián Rueda. Leí los siete comentarios. La última investigación interna, 3359208 del 21 sep, coincide con el handoff de Juan.

## Rastro
2026-10-15 inbox/2026-10-15-rcs-28452-desbloqueo.md

## RCS-28966. Revisión para Juan, 15 octubre 2026. Análisis, no mensaje pegable — 2026-10-15
_chunk 2012 · 2026-10-15 · fuente: inbox/2026-10-15-rcs-28966-revision-jr.md_

Ticket RCS-28966. Trabajado el 2026-10-15. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Revisión para Juan, 15 octubre 2026. Análisis, no mensaje pegable. Work in progress, Medium, Bikash. solo el acuse del 17 sep es público.

## Rastro
2026-10-15 inbox/2026-10-15-rcs-28966-revision-jr.md

## RCS-28992. RCS-28992 ICA, Duplication records — 2026-10-15
_chunk 2014 · 2026-10-15 · fuente: inbox/2026-09-18-correccion-ica-163-snowflake.md;2026-09-24-chat-original-guia-gpg.md;2026-10-05-rcs-28992.md;2026-10-15-rcs-28992-jr.md;2026-10-15-rcs-28992-revision-jr.md_

Ticket RCS-28992. Trabajado el 2026-09-18 a 2026-10-15. 5 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Revisión para Juan, 15 octubre 2026. Análisis, no mensaje pegable. Historial Jira completo, 24 cambios: Enrique enlazó el 24 sep; Viraj reasignó a Bikash y marcó Duplicate el 8 oct; RCS-28966 sigue Work in progress.

## Rastro
2026-09-18 inbox/2026-09-18-correccion-ica-163-snowflake.md
2026-09-24 inbox/2026-09-24-chat-original-guia-gpg.md
2026-10-05 inbox/2026-10-05-rcs-28992.md
2026-10-15 inbox/2026-10-15-rcs-28992-jr.md
2026-10-15 inbox/2026-10-15-rcs-28992-revision-jr.md

## RCS-29210. Qué pasa Rueda consultó goodwillcc en pd-lpms-uswest2-sqldb-001.database.windows.net y no la encontró en SQL M — 2026-10-15
_chunk 2017 · 2026-10-15 · fuente: inbox/2026-10-15-rcs-29210-desbloqueo.md_

Ticket RCS-29210. Trabajado el 2026-10-15. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Qué pasa Rueda consultó goodwillcc en pd-lpms-uswest2-sqldb-001.database.windows.net y no la encontró en SQL MI Platform. Work in progress, Sebastián Rueda. Leí los siete comentarios. Causa y límites La ausencia en SQL MI no invalida la consulta legacy.

## Rastro
2026-10-15 inbox/2026-10-15-rcs-29210-desbloqueo.md

## RCS-29245. RCS-29245 AAP, Store State muestra la ciudad Jira en vivo 16 oct: QUE PASA En AAP, cliente 21, el campo Store — 2026-10-16
_chunk 2019 · 2026-10-16 · fuente: inbox/2026-10-16-rcs-29245-aap-store-state.md_

Ticket RCS-29245. Trabajado el 2026-10-16. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
RCS-29245 AAP, Store State muestra la ciudad Jira en vivo 16 oct: QUE PASA En AAP, cliente 21, el campo Store State de Location en Secure Store muestra la ciudad. CAUSA Confirmada por el diff del PR 59286: location.searchable tenía Description City en la línea 467 y el PR la devuelve a State.

## Rastro
2026-10-16 inbox/2026-10-16-rcs-29245-aap-store-state.md

## RCS-29326. RCS-29326 Big Y, adjuntos de un caso antiguo no abren Jira en vivo 16 oct: Work in progress, asignado a Enriqu — 2026-10-16
_chunk 2020 · 2026-10-16 · fuente: inbox/2026-10-16-rcs-29326-big-y-adjuntos.md_

Ticket RCS-29326. Trabajado el 2026-10-16. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
RCS-29326 Big Y, adjuntos de un caso antiguo no abren Jira en vivo 16 oct: Work in progress, asignado a Enrique, sin ENG enlazado. QUE PASA Kevin Snyder abre un adjunto del caso 7546660907071138MB y recibe la pantalla "Something Unexpected Happened". La URL es attachments.aspx con filename \KCCMS Attachments\Case 7546\HPIM0285[1].jpg y system=LPMS, tenant bigy.

## Rastro
2026-10-16 inbox/2026-10-16-rcs-29326-big-y-adjuntos.md

## RCS-29351. RCS-29351 AAP, Smart Track Cashier Refunding to Own Card sin resultados Jira en vivo 16 oct: Under Customer Re — 2026-10-16
_chunk 2021 · 2026-10-16 · fuente: inbox/2026-10-16-rcs-29351-aap-smart-track.md_

Ticket RCS-29351. Trabajado el 2026-10-16. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
RCS-29351 AAP, Smart Track Cashier Refunding to Own Card sin resultados Jira en vivo 16 oct: Under Customer Review, Enrique, esperando respuesta a sus tres preguntas del 14 oct. QUE PASA Cathryn Garcia, AAP cliente 21, editó una query. El link desde Store SRA Activity Lookup abre la query 1d vacía.

## Rastro
2026-10-16 inbox/2026-10-16-rcs-29351-aap-smart-track.md

## RCS-29368. RCS-29368. Coordinación de llamada, 15 octubre 2026 — 2026-10-15
_chunk 2023 · 2026-10-15 · fuente: inbox/2026-10-15-RCS-29368-responsable.md_

Ticket RCS-29368. Trabajado el 2026-10-15. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Ross reportó Aspect down mientras repiten el export. Jira consultado en esta sesión: Escalated, Megha asignada, ocho comentarios leídos. comentario público 3397027 del 15 oct 13:38 Bogotá.

## Rastro
2026-10-15 inbox/2026-10-15-RCS-29368-responsable.md

## RCS-29417. RCS-29417: relación con RCS-29205 — 2026-10-16
_chunk 2025 · 2026-10-16 · fuente: inbox/2026-10-15-rcs-29417-rebuild-hallazgos-edwin.md;2026-10-15-rcs-29417-verificacion-relacion-29205.md;2026-10-16-eow-resumen-semana-v2.md_

Ticket RCS-29417. Trabajado el 2026-10-15 a 2026-10-16. 3 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
EoW 16 oct 2026 v2, corto y conversacional. Sustituye 2026-10-16-eow-resumen-semana.md EN Hey team, happy Friday! Quick chat about the week, mostly what we worked on together. Edwin, thanks for the RCS-29417 rebuild findings. They tie nicely into what we saw on the Starbucks refunds ticket, so we have a clearer picture of the missing data now.

## Rastro
2026-10-15 inbox/2026-10-15-rcs-29417-rebuild-hallazgos-edwin.md
2026-10-15 inbox/2026-10-15-rcs-29417-verificacion-relacion-29205.md
2026-10-16 inbox/2026-10-16-eow-resumen-semana-v2.md

## RCS-29435. Manish Sethia ve varias tiendas en Home Store Dept Name para el partner 37045592. El 32164302 sale con una. Ji — 2026-10-15
_chunk 2026 · 2026-10-15 · fuente: inbox/2026-10-15-rcs-29435.md_

Ticket RCS-29435. Trabajado el 2026-10-15. 1 notas en inbox.

## Que pasa
Manish Sethia ve varias tiendas en Home Store Dept Name para el partner 37045592. El 32164302 sale con una. Jira 15 oct: Under Support Review, tuyo, Low. Sin compromisos al cliente, solo el aviso de toma del 14 oct.

## Evidencia
1. Snowflake 15 oct, C166_SBX.REFERENCE_EMPLOYEE: 37045592 tiene 5 filas y 3 nombres. 00559 AGOURA & WESTLAKE en 3 filas, 10109 CAMPUS PARK & COLLINS insertada 06 oct, 06609 SYCAMORE & COCHRAN insertada 07 oct y actualizada 15 oct 04:46:04.
2. Mismo schema: 32164302 tiene 10 filas con un solo nombre, 18869 MULHOLLAND & CALABASAS, porque no cambio de tienda desde el 27 ago. Por eso sale bien.
3. C166_SBX_SNOWTIME.FLAT_EMPLOYEE, archivo del 15 oct: 37045592 con una fila, 06609. 32164302 con una fila, 18869. El feed manda una tienda actual.

## Que sigue
Canal Data Issues, Retail Ops en Teams: publica ahi la escalacion con las evidencias 1 a 3 y la pregunta del paso 2. No abras grupo ni chat privado con ingenieria, regla de Ripp en inbox/2026-10-15-directrices-updates-y-canales-teams.md.
Manish Sethia: update antes del viernes 16 oct, a 2 business days de tu comentario del 14 oct. Confirma en Jira la fecha del ultimo comentario publico. Sin hallazgos de investigacion, solo estado.

## Precedentes
RCS-28809 Kohl's, REFERENCE_EMPLOYEE crea fila nueva por transferencia, inbox/2026-10-05-rcs-28809.md. Otro cliente, sostiene la hipotesis, no confirma esta causa.

## Rastro
2026-10-15 inbox/2026-10-15-rcs-29435.md

## RCS-29448. RCS-29448. Recomendación Diego Buelvas — 2026-10-15
_chunk 2028 · 2026-10-15 · fuente: inbox/2026-10-15-rcs-29448-triage-backlog.md_

Ticket RCS-29448. Trabajado el 2026-10-15. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Qué pasa Sainsbury’s solicita verificar en Test el cambio de artículos rechazados por edad o BRM a líneas anuladas y confirmar implicaciones. Jira en vivo, 15 oct 14:25 Bogotá: sin asignar, Under Customer Review, Medium, SOW Estimation. Causa La descripción del cliente informa fix en staging.

## Rastro
2026-10-15 inbox/2026-10-15-rcs-29448-triage-backlog.md

## RCS-29449. RCS-29449. Recomendación Edwin Garzon — 2026-10-15
_chunk 2029 · 2026-10-15 · fuente: inbox/2026-10-15-rcs-29449-triage-backlog.md_

Ticket RCS-29449. Trabajado el 2026-10-15. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Qué pasa DSW pregunta si envía descripción de artículos y si llega al reporte Engage Insights Top Returned SKUs. Jira en vivo, 15 oct 14:25 Bogotá: sin asignar, Under Support Review, Medium. Falta validar cliente y Engage ID, dato de entrada y dato agregado.

## Rastro
2026-10-15 inbox/2026-10-15-rcs-29449-triage-backlog.md

## RCS-29452. RCS-29452 Big 5, quitar tienda 359 del empleado 2449872 — 2026-10-15
_chunk 2031 · 2026-10-15 · fuente: inbox/2026-10-15-rcs-29452-triage-backlog.md;2026-10-15-rcs-29452.md_

Ticket RCS-29452. Trabajado el 2026-10-15. 2 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
https://trebuco.atlassian.net/browse/RCS-29452 Qué pasa Nancy Barajas pide quitar la tienda 359 del perfil del empleado 2449872. asignado a Juan, Under Support Review, Medium. tu comentario de toma, 15 oct 15:29. Causa CONFIRMADA en datos:

## Rastro
2026-10-15 inbox/2026-10-15-rcs-29452-triage-backlog.md
2026-10-15 inbox/2026-10-15-rcs-29452.md

## RCS-29460. Niamh McCann pregunta cómo borrar la evidencia de un lead sin seleccionar una por una en el transaction viewer — 2026-10-16
_chunk 2032 · 2026-10-16 · fuente: inbox/2026-10-16-rcs-29460-paso-a-paso-v2.md;2026-10-16-rcs-29460-paso-a-paso.md;2026-10-16-rcs-29460.md_

Ticket RCS-29460. Trabajado el 2026-10-16. 3 notas en inbox.

## Que pasa
Niamh McCann pregunta cómo borrar la evidencia de un lead sin seleccionar una por una en el transaction viewer, y qué hace la función copy del video. Jira: Under Support Review, asignado a Juan. Time to Resolution vence el 30 oct 2026 a las 9:41 AM. Compromisos: ninguno.

## Evidencia
1. Talos 3398089, confianza media: cada ítem tiene botón de quitar, sin quitar todo para evidencia que no es transacción. Copy duplica el ítem en otro lead y deja el original. No vio el video.
2. Primer cuadro del video Recording 2026-10-16 143942.mp4: lead NMFY270126-490 con 221 Secure Store Transactions y botón View in Event Viewer.
3. Dato que decide: si el transaction viewer ofrece seleccionar todo.

## Que sigue
Niamh McCann: solo si el video no aclara qué botón llama copy. Pregunta el segundo del video y qué quiere lograr.
Juan: decide la solicitud de mejora tras el paso 2.

## Precedentes
Ninguno. Cerebro no tiene casos de borrar evidencia de un lead ni del botón copy.

## Rastro
2026-10-16 inbox/2026-10-16-rcs-29460-paso-a-paso-v2.md
2026-10-16 inbox/2026-10-16-rcs-29460-paso-a-paso.md
2026-10-16 inbox/2026-10-16-rcs-29460.md

## RCS-29462. Venkateshwaran Jayapal, de Ralph Lauren, pide por correo antes del 23 oct 2026 la matriz de escalamiento 24/7, — 2026-10-16
_chunk 2033 · 2026-10-16 · fuente: inbox/2026-10-16-rcs-29462.md_

Ticket RCS-29462. Trabajado el 2026-10-16. 1 notas en inbox.

## Que pasa
Venkateshwaran Jayapal, de Ralph Lauren, pide por correo antes del 23 oct 2026 la matriz de escalamiento 24/7, el SLA P1, las ventanas de freeze, la capacidad ante picos y un checklist de credenciales. Matt Reid y Tyler Aken van en copia. Jira: Under Support Review, asignado a Juan. Rajith acusó recibo. Compromisos de contenido: ninguno.

## Evidencia
1. Comentario 3398155: correo completo. El punto 4 trae el texto de plantilla [e.g., 3x-5x] sin completar.
2. Talos 3398169, confianza alta: ninguna respuesta vive en la configuración del cliente.
3. svc rts 3398153, 11:09 AM EDT: se creó un CASD asignado a TSOC support. Su contenido no está en Cerebro.

## Que sigue
CSM de Ralph Lauren: matriz, SLA P1 y PIN o contrato. Falta tu paso 2.
Infraestructura: puntos 4 y 5. Falta confirmar el dueño actual, en septiembre fue Russell Harmon.
Matt Reid: aviso de que la respuesta sale antes del 23 oct. No prometas contenido.

## Precedentes
RCS-28871 Walgreens, cuestionario Peak Season Readiness, inbox/2026-09-15-rcs-28871.md y bitacora/RCS-28871.md.
RCS-27847 Samsung y RCS-27840 Kohl's, brain/markdown/21-kt-kristin-sign-off-procesos-rts.md líneas 54, 180 y 1073.

## Rastro
2026-10-16 inbox/2026-10-16-rcs-29462.md

## RCS-29465. pchan@wsgc.com quiere agregar la reference search 1b - Emp HR Info with User ID V2 a su búsqueda Order Refund — 2026-10-16
_chunk 2034 · 2026-10-16 · fuente: inbox/2026-10-16-flujo-secure-referencia-en-busqueda.md;2026-10-16-lecciones-rcs-29465.md;2026-10-16-pr-59321-analisis.md;2026-10-16-rcs-29465-v2.md;2026-10-16-rcs-29465-v3.md;2026-10-16-rcs-29465.md_

Ticket RCS-29465. Trabajado el 2026-10-16. 6 notas en inbox.

## Que pasa
[2026-10-16] pchan@wsgc.com pide agregar la referencia 1b - Emp HR Info with User ID V2 a Order Refund Categories- SP and RS para traer la ubicacion del empleado. Estado y fecha: confirma en Jira en vivo. Compromisos: ninguno.
[2026-10-16] pchan@wsgc.com quiere agregar la reference search 1b - Emp HR Info with User ID V2 a su búsqueda Order Refund Categories- SP and RS para traer la employee location. Jira: Under Support Review, asignado a Juan. Sin fecha del cliente. Compromisos: ninguno.

## Evidencia
[2026-10-16] Mediciones en inbox/2026-10-16-rcs-29465-pasos.md. Analisis del PR en inbox/2026-10-16-pr-59321-analisis.md: cambia diez Description del cliente 139 y no toca Employee, auto joins ni agregados. No resuelve el inflado. ENG-10078 en Backlog, asignado a Enrique, segun Jira del 16 oct.
[2026-10-16] 1. RCS-29363, Work in progress, assignee Enrique Jimenez: el comentario del 15 oct 8:04 PM EDT dice que halló por qué la búsqueda falla al cambiar la carpeta de la referencia. Causa sin texto en Jira.
2. ENG-10078, Backlog, enlazado como causa, con el PR https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/arpfiles/pullrequest/59321 publicado el 16 oct.
3. Adjunto image-20261016-161358.png: la columna User ID in Lower Case aparece poblada en 1 de 11 filas visibles. Es una muestra, no una medición.

## Impacto
La CTE hace auto join de reference_Employee por EmployeeID. Hay 609 User ID repetidos, y un reembolso de esos cajeros entra de 2 a 9 veces. Medido el 16 oct 2026 sobre 13 meses: sin referencia 4297884 filas y suma -80458795.81, con la CTE 4444633 filas y suma -123035024.88. Quien la use en un resumen con Sum o Count recibe totales inflados. El origen del auto join está sin confirmar. Se preguntó a Enrique por RCS-29363 y el PR 59321.

## Que sigue
[2026-10-16] Enrique: aprobador, evidencia de staging y hashes con NULL.
Patricia: sin mensaje hasta decidir la salida del inflado. El PR no la cubre.
[2026-10-16] Enrique: causa y estado del PR 59321. Falta confirmar si aplica a este ticket.
pchan@wsgc.com: ambiente de las capturas, el Store No 88888 en todas las filas visibles sugiere pruebas, y si los empleados del reporte tienen User ID in Lower Case poblado.

## Precedentes
[2026-10-16] RCS-29363, ENG-10078 y PR 59321. La ficha tickets/RCS-29363.md dice Nordstrom y Jira dice Williams-Sonoma.
[2026-10-16] RCS-29363 Williams-Sonoma, mismo reporter y misma referencia. La ficha tickets/RCS-29363.md dice Nordstrom y Jira dice Williams-Sonoma. Confía en Jira.
db:knowledge_chunks/312 y 518, contexto de join, sin causa.

## Rastro
2026-10-16 inbox/2026-10-16-flujo-secure-referencia-en-busqueda.md
2026-10-16 inbox/2026-10-16-lecciones-rcs-29465.md
2026-10-16 inbox/2026-10-16-pr-59321-analisis.md
2026-10-16 inbox/2026-10-16-rcs-29465-v2.md
2026-10-16 inbox/2026-10-16-rcs-29465-v3.md
2026-10-16 inbox/2026-10-16-rcs-29465.md

## RCS-29471. Cat Saeteurn, de Gap Inc, pide cambiar una imagen de https://apps.apprissretail.com/bananarepublicfactory/retu — 2026-10-16
_chunk 2036 · 2026-10-16 · fuente: inbox/2026-10-16-rcs-29471-v2.md;2026-10-16-rcs-29471-v3.md;2026-10-16-rcs-29471.md;2026-10-16-traspaso-tickets-juan.md_

Ticket RCS-29471. Trabajado el 2026-10-16. 4 notas en inbox.

## Que pasa
[2026-10-16] Cat Saeteurn, de Gap Inc, pide cambiar una imagen de la página de reclamos de BR Factory antes del 22 oct 2026. Jira 16 oct: Under Support Review, asignado a Juan, toma de propiedad publicada. Compromisos con el cliente: ninguno.
[2026-10-16] Cat Saeteurn, de Gap Inc, pide cambiar una imagen de https://apps.apprissretail.com/bananarepublicfactory/returns#/search antes del 22 oct 2026. Jira 16 oct 4:39 PM EDT: Under Support Review, asignado a Juan, toma de propiedad ya publicada. Compromisos con el cliente: ninguno.

## Evidencia
[2026-10-16] 1. Comentario 3398479, 3:51 PM EDT: "update the page with new image by 10/22".
2. Adjunto 1443025 BRFS261022_SITE_Nov_Appriss.jpg, 10,064,032 bytes, foto de dos personas sin texto ni logo.
3. Talos 3398486, confianza media: la página tiene tres imágenes configuradas, logo del título, banner del pie e icono de pestaña. No vio los archivos. Es hipótesis de Talos.
[2026-10-16] Lectura hecha el 16 oct 2026 después de las 4:39 PM EDT. Jira manda sobre esta nota. Reverifica antes de actuar.

| Ticket | Cliente | Reporter | Estado | Asignado | Prioridad | Fecha que importa |
|---|---|---|---|---|---|---|
| [RCS-29471](https://trebuco.atlassian.net/browse/RCS-29471) | Gap Inc, BR Factory | Cat Saeteurn | Under Support Review | Juan Martinez | Medium | El cliente pide el cambio de imagen antes del 22 oct 2026 |
| [RCS-29462](https://trebuco.atlassian.net/browse/RCS-29462) | Ralph Lauren Corporation, White Glove | Matt Reid | Under Support Review | Juan Martinez | Medium | El cliente pide respuesta antes del 23 oct 2026 |
| [RCS-29460](https://trebuco.atlassian.net/browse/RCS-29460) | TJX Europe | Niamh McCann | Under Support Review | Juan Martinez | Medium | TJX Time to Resolution vence el 30 oct 2026 a las 9:41 AM, 336 horas |
| [RCS-29465](https://trebuco.atlassian.net/browse/RCS-29465) | Williams-Sonoma, Inc | pchan@wsgc.com | Under Support Review | Juan Martinez | Medium | Sin fecha del cliente. La primera respuesta ya cumplió el SLA |

Juan ya se asignó los cuatro entre las 4:38 y las 4:39 PM EDT y publicó el comentario de toma de propiedad en cada uno. N

## Que sigue
[2026-10-16] Cat Saeteurn: confirmar que reemplaza la foto grande de la derecha y que el adjunto es el archivo final. Falta tu paso 1.
Quien publique archivos de returns de BR Factory: cambiar footer.jpg y decir si hace falta despliegue. Falta confirmar quién es.
[2026-10-16] Cat Saeteurn: cuál de las tres posiciones reemplaza la foto y si el adjunto es el archivo final. Falta tu resultado de los pasos 1 a 3 para formular la pregunta con precisión.
Quien tenga acceso a los archivos de returns: ubicar la imagen actual y confirmar si hace falta despliegue. Falta confirmar quién es.

## Precedentes
[2026-10-16] Ninguno. Cuatro búsquedas en español e inglés no traen un cambio de assets de BR Factory.
[2026-10-16] Ninguno. Busqué con tres variantes en español e inglés y no existe un caso de cambio de assets de BR Factory.

## Rastro
2026-10-16 inbox/2026-10-16-rcs-29471-v2.md
2026-10-16 inbox/2026-10-16-rcs-29471-v3.md
2026-10-16 inbox/2026-10-16-rcs-29471.md
2026-10-16 inbox/2026-10-16-traspaso-tickets-juan.md

## Corrección de dirección del board — 2026-10-15
_chunk 2040 · 2026-10-15 · fuente: inbox/2026-10-15-board-supervision-v2.md_

# Corrección de dirección del board

Juan rechazó la versión editorial por perder utilidad, indicadores por persona, legibilidad y efectos interactivos. La propuesta anterior de portada con imagen y mínimos indicadores queda superada por esta corrección. No hay borradores para terceros.

Implementación en curso: cabecera de supervisión compacta, alertas por motivo, monitores por persona con carga y distribución equipo/cliente, tipografía de tickets mayor, atención seleccionada por defecto. Humanoide construido como geometría de puntos WebGL desde el arte original, con profundidad, repulsión por cursor y dispersión al pulsar. No es un modelo anatómico completo; sí son partículas renderizadas e interactivas.

Conservar datos actuales y plantilla. Espera cliente separada del reloj activo. Sin acciones Jira o Teams.

Cambios terminados: monitores por persona ordenados por cantidad de casos con señal de atención; al pulsar filtran tickets. Métricas separadas para respuesta, ownership y actualización. Filas con prioridad, estado, responsable y acción visible; títulos de 17 px en escritorio y 16 px en móvil, motivos de 13 px. Los indicadores siguen el snapshot existente, sin consulta nueva a Jira.

Validación: build correcto, siete pruebas previas de clasificación/turnos correctas. Navegador sin errores WebGL; canvas activo, dispersión al pulsar y filtro Por responder devuelve un caso. Foco por persona comprobado. Móvil 390 px sin desborde horizontal del documento. Capturas supervision-desktop.jpg y supervision-mobile.jpg en .impeccable/review/ del proyecto.

Límite visual: nube de puntos con profundidad derivada del arte, no malla anatómica de 360 grados. El corte puede cambiar por el recolector habitual. No se validaron SLA ni compromisos contra Jira en vivo.

Revisión visual independiente final: ship, sin bloqueantes comprobados en las capturas. Detalle expandible comprobado tras compilar. Fuente y plantilla actualizadas, datos conservados. Servidor temporal detenido. Las notas editoriales previas conservan valor histórico; esta corrección fija la dirección vigente.


## Rastro
2026-10-15 inbox/2026-10-15-board-supervision-v2.md

## fuentes de logs juan — 2026-10-15
_chunk 2041 · 2026-10-15 · fuente: inbox/2026-10-15-fuentes-de-logs-juan.md_

Fuentes de logs que Juan tiene disponibles. 15 oct 2026. Dicho por Juan.

1. Control Panel del tenant: seccion Incident Logs y seccion Logs.
2. Grafana.
3. Base del tenant por SSMS en bastion: secure.Log (UpdatedDateTime, LogID, MachineName, Component, Sender, MessageType, Message, UserID, UserToken, LogCount, MessageHash, InsertedDateTime), secure.UserActivityLogins (UserID, LoginTime, TimeZone), sso.ResponseLog (Id, InsertedDateTime UTC, ProviderID, Summary, Response con el XML SAML). Tambien existen dbo.CommandLog, ops.RunLog, sdl.BatchInterfaceLog, incident.ActivityLog, incident.EvidenceLog.
Ojo: las consultas de base de tenant se corren en SSMS dentro del bastion, no en Snowflake. En Snowflake falla con "session does not have a current database" porque sys.columns y OBJECT_ID son sintaxis de SQL Server.
Grafana muestra hora Bogota; la base guarda UTC, cinco horas mas (flujos/smart-alert-disparo-manual.md).


## Rastro
2026-10-15 inbox/2026-10-15-fuentes-de-logs-juan.md

## Respuesta solicitada por Juan a Luis sobre DevOps — 2026-10-16
_chunk 2044 · 2026-10-16 · fuente: inbox/2026-10-16-luis-contactos-devops.md_

# Respuesta solicitada por Juan a Luis sobre DevOps

Fuente: db:knowledge_chunks/1131, líneas 1 a 3. Organigrama de julio de 2026, no roster actual verificado. La ruta depende del ticket y del producto. No se indicó ID ni quién pidió escalar.

Borrador interno v2 en español solicitado por Juan, no enviado. Sustituye el anterior en inglés, que queda obsoleto. Verificado con verificar_borrador: sin bloqueantes ni verificaciones pendientes en Jira. Las preguntas no requieren respaldo factual.

Luis, en el organigrama que tengo de julio aparecen Diego Garcia, Jesus Veira y Juan Restrepo en DevOps bajo Michael Tasch, y Natalia Alzate y Rajesh Kancharla bajo Jose Parocua Andrade. ¿Cuál es el ticket y quién te pidió escalarlo? Con eso confirmamos a quién corresponde.

Siguiente paso: Luis, solicitar el ticket y quién pidió escalar para confirmar el contacto correspondiente.


## Verificación de ruta, 16 octubre 2026

El borrador anterior conserva valor como roster histórico. Queda superado como respuesta a qué opción seleccionar: los nombres no determinan la cola.

Consulta en vivo de Confluence:
https://trebuco.atlassian.net/wiki/spaces/RTS/pages/474627801097
L2 to L3 RCS ticket management, versión 27, 14 octubre 2026.
https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478006902856
Escalating Tickets to L3 Departments: Procedures and Responsibilities, versión 5, 27 agosto 2026.

Ambas fuentes indican Infrastructure: Under Infrastructure Review, el analista conserva la asignación. La guía complementaria documenta creación automática de RTAILIT y sincronización de comentarios. No se probó esa automatización. DevOps no figura como destino independiente en estas matrices.

La captura muestra Waiting For Infrastructure hacia Under Infrastructure Review. Esa es la opción correspondiente si el trabajo requerido pertenece a Infrastructure. Decir DevOps por sí solo no prueba esa clasificación. La página principal dirige problemas de código de aplicaciones a Engineering. Falta ID, producto y trabajo solicitado para decidir el caso concreto. No se consultó un ticket en Jira ni se ejecutaron transiciones.

Siguiente paso: Luis, pedir ticket, producto y trabajo concreto solicitado a DevOps para confirmar Infrastructure o Engineering.

Corrección documental adicional detectada: la versión 27 ahora indica David Parraga para Delivery Secure 5. La nota del 13 octubre y la guía complementaria conservan Peyman. Este hallazgo no cambia la ruta de Infrastructure.


## Rastro
2026-10-16 inbox/2026-10-16-luis-contactos-devops.md

## tailored guion cliente v2 — 2026-10-16
_chunk 2046 · 2026-10-16 · fuente: inbox/2026-10-16-tailored-guion-cliente-v2.md_

OBSOLETO. Sustituido por investigaciones/2026-10-16-tailored-guion-cliente-v3.md, que explica trabajo realizado, pendientes y próximos pasos.

Guion externo bilingüe para Tailored Brands, versión 2. 16 octubre 2026.

Corrección solicitada por Juan: la llamada incluye representantes del cliente. El guion anterior mezclaba información interna y quedó obsoleto. También quedaron obsoletas sus 14 tarjetas; se marcaron 16 archivos en total.

Guion para abrir durante la llamada: investigaciones/2026-10-16-tailored-guion-cliente-v2.md.
Incluye apertura, 11 respuestas por ticket RCS, 10 respuestas a preguntas y cierre, en inglés y español.
Las tarjetas nuevas están en inbox/2026-10-16-rcs-XXXXX-guion-llamada-v2.md.

El texto hablado usa comunicaciones públicas verificadas y preguntas para confirmar resultados. Excluye identificadores y estados de Engineering, responsables internos, logs, bases de datos, conteos internos, chats, hipótesis de código y discrepancias de notas internas. No se envió ni publicó nada.

El análisis anterior continúa siendo preparación privada. No usarlo como guion externo.

Siguiente paso:
Participantes de la llamada: confirmar acceso de los usuarios reportados y resultado de Chris.
Appriss y Tailored Brands: acordar resultado esperado por pendiente y fecha del próximo update.



## Rastro
2026-10-16 inbox/2026-10-16-tailored-guion-cliente-v2.md

## tailored llamada ejemplos jacinta emeldia — 2026-10-16
_chunk 2050 · 2026-10-16 · fuente: inbox/2026-10-16-tailored-llamada-ejemplos-jacinta-emeldia.md_

Nueva evidencia compartida por Juan durante la llamada. 16 octubre 2026.

Fuente: captura codex-clipboard-f4666cb1-b3f6-492c-aa1a-d519300770ac.png. Libro visible: Appriss Incident Security ID Examples. No se recibió el archivo Excel original.

Hechos visibles
Jacinta Titus y Emeldia Pryor tienen Incident Security ID en Choose a value. Las imágenes del archivo muestran ApprissCase Users y team Location Manager para ambas. Se ve información de ubicación parcial; no se verifica toda la fila ni su aplicación efectiva. Colton dice que siguen trabajando y que el último login fue en junio. Esa declaración no se comprobó en logs. Colton indica que enviará los ejemplos después de la llamada; no consta recepción.

Impacto sobre borradores
No invalida la evidencia de Rachel. Invalida extender a estas dos usuarias la explicación de primer ingreso o presentar todos los casos como el mismo defecto. Tampoco demuestra que el archivo actual estuviera cargado antes del login de junio. La respuesta anterior sobre derivación frente a campo explícito sigue pendiente de recomendación de Matt.

Respuesta EN para la llamada
Thank you, Colton. These examples show the expected group and team in the file alongside a blank Incident Security ID in the account. You also mentioned that their last sign-in was in June. The next check is to establish whether those assignments had already reached the system before that sign-in, or arrived afterward. That will help distinguish whether the assignment was available but not applied, or has not yet been picked up at a subsequent sign-in. We cannot conclude which applies from the screenshot alone.

ES
Gracias, Colton. Estos ejemplos muestran el grupo y el equipo esperados en el archivo junto con el nivel de Incident vacío en la cuenta. Mencionas que su último ingreso fue en junio. La siguiente comprobación es establecer si esas asignaciones ya habían llegado al sistema antes de ese ingreso o llegaron después. Eso permite distinguir entre una asignación disponible que no se aplicó y otra que todavía no se ha recogido en un ingreso posterior. La captura por sí sola no permite concluir cuál ocurrió.

Siguiente paso:
Juan y revisión técnica: contrastar carga de asignaciones, último ingreso y nivel efectivo de ambas usuarias cuando se reciba el archivo; no prometer que otro login las resolverá.


## Rastro
2026-10-16 inbox/2026-10-16-tailored-llamada-ejemplos-jacinta-emeldia.md

## tailored llamada jr consulta matt — 2026-10-16
_chunk 2052 · 2026-10-16 · fuente: inbox/2026-10-16-tailored-llamada-jr-consulta-matt.md_

Tailored Brands. Nueva información de la llamada, 16 octubre 2026.

Fuente: captura compartida por Juan, codex-clipboard-d47dfa99-2de6-4ca2-a30d-8fe221db1170.png.

Hecho observado
J.R. pide a Juan consultar con Matthew Kamminga tanto en el ticket como en Teams. Pregunta si mantener el nivel de Incident derivado del archivo de equipos o recibir Security ID explícito y ubicación para explorar una alternativa que desbloquee antes de la corrección completa. La captura no muestra aceptación de Matt, viabilidad técnica ni acuerdo definitivo de cambio de formato. La última frase de J.R. queda truncada.

Borradores afectados
La recomendación de no cambiar el archivo en inbox/2026-10-16-tailored-llamada-respuesta-jr-securityid.md y la sección equivalente del guion v4 dejan de ser la respuesta vigente: ahora corresponde evaluar ambas opciones con Matt. El resto del guion v4 mantiene su alcance de tres problemas abiertos.

ENGLISH, respuesta breve para la llamada
Understood. We need Matt's recommendation on whether to keep deriving the Incident security level from the teams file or provide it explicitly, together with the location. We also need to confirm whether that would address the current access problem. That will establish what, if anything, needs to change in your files.

ESPAÑOL
Entendido. Necesitamos la recomendación de Matt sobre mantener el nivel de Incident derivado del archivo de equipos o enviarlo explícitamente junto con la ubicación. También debemos confirmar si eso resolvería el problema actual de acceso. Con esa respuesta podremos establecer qué necesitan cambiar en sus archivos, si corresponde.

Siguiente paso:
Matthew Kamminga: pedir recomendación entre derivación y campo explícito, efecto sobre accesos y ubicaciones, y requisitos antes de solicitar cambios al cliente.
Juan: J.R. solicitó reflejar la pregunta en ticket y Teams; no se ha confirmado envío. El agente no escribe en Jira ni envía Teams sin autorización directa de Juan.


## Rastro
2026-10-16 inbox/2026-10-16-tailored-llamada-jr-consulta-matt.md

## tailored llamada uso esporadico — 2026-10-16
_chunk 2054 · 2026-10-16 · fuente: inbox/2026-10-16-tailored-llamada-uso-esporadico.md_

Tailored Brands. Dato de negocio aportado por Mike durante la llamada, 16 octubre 2026.

Fuente: captura codex-clipboard-11eb1590-dfd5-491a-84f0-ec500e49cdc4.png compartida por Juan.

Hecho declarado por el cliente
Mike explica que algunos usuarios de tiendas entran una o dos veces al año, cuando tienen un incidente. Los últimos ingresos de mayo o junio pueden reflejar ese uso normal. No constituyen por sí solos abandono ni baja laboral.

Hecho visible
El libro muestra Christi Winters con Incident Security ID en Choose a value, grupo ApprissCase Users y equipo Location Manager. También muestra Rahim Mehdiyev con el nivel vacío y grupo ApprissCase Users; el equipo queda fuera de la parte visible. La captura no fecha los datos de origen ni prueba su procesamiento.

Efecto sobre preparación anterior
La comparación de carga y login sigue siendo una prueba técnica válida. Debe corregirse cualquier lectura de login antiguo como abandono o como obligación del cliente de ingresar frecuentemente. No se ha probado que estos usuarios sean casos de primer ingreso ni que otro login los resuelva. El criterio de validación debe incluir regreso después de meses y acceso operativo cuando ocurre un incidente.

ENGLISH
That makes sense, Mike. Infrequent sign-ins are part of how your stores use Incident. The expected outcome is that users can access it when an incident occurs, with the correct permissions and store assignment. We should use that as the validation criterion for the access correction, including users returning after several months.

ESPAÑOL
Entendido, Mike. Los ingresos esporádicos forman parte del uso de Incident en las tiendas. El resultado esperado es que los usuarios puedan acceder cuando ocurra un incidente, con los permisos y la tienda correctos. Ese debe ser el criterio de validación de la corrección, incluidos los usuarios que regresan después de varios meses.

Siguiente paso:
Juan y revisión técnica: incorporar el uso esporádico al criterio propuesto de validación; no darlo por compromiso aceptado de implementación.


## Rastro
2026-10-16 inbox/2026-10-16-tailored-llamada-uso-esporadico.md

## Wegmans C171_WEG, SQL para conteo diario de work items — 2026-10-16
_chunk 2058 · 2026-10-16 · fuente: inbox/2026-10-16-wegmans-c171-sql.md_

# Wegmans C171_WEG, SQL para conteo diario de work items

Acceso documentado en brain/memoria/reference_acceso_sql_tenants.md y brain/memoria/project_juan_accesos.md. Azure Bastion, SSMS, instancia sqlmi-prd-wus2-arp-001, login jmartinez@trebu.co. Usa el login de lectura. Solo SELECT.

Q0. Ubica la base de Wegmans. El Client ID sale del selector Client de la página Cache del Control Panel. No asumas 171.
SELECT name FROM sys.databases
WHERE state = 0 AND database_id > 4 AND name LIKE '%platform' AND name LIKE '%weg%'
ORDER BY name;
Selecciona esa base en el desplegable antes de seguir. Sin eso la consulta corre contra master.

Q1. Columnas reales de las tablas de runs, para localizar la columna de duplicados.
SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'workview'
  AND TABLE_NAME IN ('WorkItemDefinitionGenerationRequest', 'WorkItemDeaggregationRequest')
ORDER BY TABLE_NAME, ORDINAL_POSITION;

Q2. Generados por día de Period, 1 sep a 15 oct. Debe coincidir con Daily WI COUNT de Explorer.
SELECT CAST(PeriodFromDateTime AS date) AS Periodo, COUNT(*) AS Generados
FROM workview.Workview WITH (NOLOCK)
WHERE PeriodFromDateTime >= '2026-09-01' AND PeriodFromDateTime < '2026-10-16'
GROUP BY CAST(PeriodFromDateTime AS date)
ORDER BY Periodo;

Resultado Q1 el 16 oct: WorkItemDeaggregationRequest trae RunId, RowId, Failed, Duplicate, Skipped. WorkItemDefinitionGenerationRequest trae RunId, DefinitionVirtualFilePath, PeriodType, PeriodStartDateTime, PeriodEndDateTime, Failed.
Resultado Q2 el 16 oct: coincide con Explorer en octubre, 35 contra 35. Septiembre da 58 contra 57. El 1 sep suma 2 porque incluye el work item mensual, que Explorer muestra en la columna Monthly. Un work item cambia del 21 al 20 sep, el total del par es igual.

Q3. Total, duplicados, fallos y skipped por día de Period, 1 sep a 15 oct.
SELECT g.PeriodType, CAST(g.PeriodStartDateTime AS date) AS Periodo,
       COUNT(*) AS Total,
       SUM(CAST(d.Duplicate AS int)) AS Duplicados,
       SUM(CAST(d.Failed AS int)) AS Fallos,
       SUM(CAST(d.Skipped AS int)) AS Skipped,
       COUNT(DISTINCT g.RunId) AS Runs
FROM workview.WorkItemDefinitionGenerationRequest g WITH (NOLOCK)
JOIN workview.WorkItemDeaggregationRequest d WITH (NOLOCK) ON d.RunId = g.RunId
WHERE g.PeriodStartDateTime >= '2026-09-01' AND g.PeriodStartDateTime < '2026-10-16'
GROUP BY g.PeriodType, CAST(g.PeriodStartDateTime AS date)
ORDER BY g.PeriodType, Periodo;

Q4. Qué definición aporta los duplicados.
SELECT g.DefinitionVirtualFilePath,
       SUM(CAST(d.Duplicate AS int)) AS Duplicados, COUNT(*) AS Total
FROM workview.WorkItemDefinitionGenerationRequest g WITH (NOLOCK)
JOIN workview.WorkItemDeaggregationRequest d WITH (NOLOCK) ON d.RunId = g.RunId
WHERE g.PeriodStartDateTime >= '2026-09-01' AND g.PeriodStartDateTime < '2026-10-16'
GROUP BY g.DefinitionVirtualFilePath
ORDER BY Duplicados DESC;


## Rastro
2026-10-16 inbox/2026-10-16-wegmans-c171-sql.md
