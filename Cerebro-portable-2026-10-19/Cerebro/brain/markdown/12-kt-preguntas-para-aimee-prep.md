# KT — Preguntas para Aimee (Prep)

Carpeta 12 de la base de Moscú. 15 fragmentos.

## KT Prep — Resumen ejecutivo y estado post-Session 1
_chunk 272 · 2026-06-05 · fuente: /Users/MancoMenStudio/Desktop/KT_Notes_Session1_Updated.docx_

Documento de preparación de las sesiones KT con Aimee — Juan & Camila, junio 2026.

ESTADO: Session 1 completada. T-001 parcialmente cubierto. Sessions 2+ pendientes.

EQUIPO: Juan Martinez (receiving), Camila Cortes (receiving), Aimee Wadsworth (outgoing Support Manager).

TÓPICOS 16 priorizados de alta prioridad: T-001 Team & Links, T-002 Customer cadence, T-003 Aged close-out, T-004 Queue grooming, T-005 Escalation playbook, T-006 Eng escalation packaging, T-007 Ticket lifecycle map, T-008 Done definitions, T-071 Update Rate compliance, T-088 Jira automations, T-089 Jira statuses, T-090 Jira fields, T-091 Inbound channels, T-092 Priority, T-093 Customer-facing docs, T-095 Migration/downtime notifications.

NOTAS GENERALES SESSION 1:
- Aimee disponible vía Teams para preguntas rápidas entre sesiones.
- Todos los docs de Confluence y SharePoint son living documents, algunos mantenidos por más de 15 años.
- Session 1 fue grabada.
- Aimee recomendó revisar todo lo que NO esté bajo "Archive" en SharePoint Support Home.

## T-001 (1.1) — Acceso CRM y Lista de CSMs: RESUELTO
_chunk 273 · 2026-06-05 · fuente: /Users/MancoMenStudio/Desktop/KT_Notes_Session1_Updated.docx_

PREGUNTA: ¿Podemos obtener acceso al CRM para todo el equipo?
RESPUESTA: Ir a Help Desk (Company Links en el homepage de Google). Crear un ticket de "Access Change". Campos obligatorios: Summary, Priority, Business Justification. La justificación es el campo más crítico — InfoSec siempre la requiere. Ejemplo: "[Nombre] needs access to [System] in order to perform job duties." IT lo toma desde ahí y puede hacer preguntas de seguimiento antes de otorgar acceso.

PREGUNTA: ¿Existe una lista de CSMs y los clientes asignados a cada uno? ¿Dónde está?
RESPUESTA: Sí. Archivo: "Account Assignment and Service Levels March 21 2024.xlsx". Ubicación: SharePoint, sección Marketing (marketing lo crea y mantiene desde exportaciones de Salesforce). Link compartido por Aimee en el chat de la sesión. Color-coded por CSM, clientes alfabetizados. Colleen tiene 100+ clientes. Salesforce es el source of record real.

ACCIÓN ABIERTA: Aimee debe verificar que el Excel de CSM Assignments sea accesible para Juan y Camila.

## T-001 (1.2) — Consumer Dispute Process: Definición, RAR y Timelines — RESUELTO
_chunk 274 · 2026-06-05 · fuente: /Users/MancoMenStudio/Desktop/KT_Notes_Session1_Updated.docx_

PREGUNTA: ¿Qué es un Dispute? ¿Cuáles son los requisitos?
RESPUESTA: Un cliente va a un retailer (ej: TJ Maxx), intenta una devolución, el sistema Return Authorization lo deniega. Llama a nuestro call center, se le ofrece un RAR, y si no está de acuerdo con la denegación, envía un email explicando por qué — ese email es el dispute. Entra al sistema y pasa por el proceso de dispute (manejado por Andrea).
PENDIENTE: Definición formal aún no está en Confluence. Aimee le pidió a Andrea que la agregue.

PREGUNTA: ¿Qué es un RAR? ¿Cómo difiere de un Dispute?
RESPUESTA: RAR = Return Activity Report. Muestra el historial de compras y devoluciones del cliente para ese retailer, incluyendo todas las tiendas bajo el mismo grupo padre (TJ Maxx, Home Goods y Marshalls comparten un RAR). Cubre exactamente 2 años hacia atrás. El RAR es informativo — ayuda al cliente a entender por qué fue denegado. El Dispute es la solicitud formal de revisión de esa denegación. El RAR NO es automático; solo se extrae cuando el cliente llama y lo pide.

PREGUNTA: ¿Cuál es el timeline de respuesta del retailer?
RESPUESTA: Regla general: 2 a 4 semanas totales al consumidor. Appriss/Andrea envía el dispute al retailer dentro de 1 business day. Tiempo de respuesta varía: Home Depot responde el mismo día; la mayoría en 2 semanas. Ningún retailer supera consistentemente 2-4 semanas.
FOLLOW-UP ABIERTO: Aimee verificará con Andrea si existe lista de tiempos de respuesta por retailer.

PREGUNTA: ¿Cuál es la acción para cada status de respuesta? ¿Cómo es la comunicación con el cliente?
RESPUESTA: Toda la comunicación es vía email, completamente a través del CRM. El CRM maneja, rastrea y registra cada paso del proceso de dispute. No hay llamadas salientes por status — todo va por el CRM.

PENDIENTE: URL de letter templates — no cubierto en Session 1. A tratar en sesión futura.

## T-001 (1.3) — Support General: Confluence, Jira, SharePoint — RESUELTO
_chunk 275 · 2026-06-05 · fuente: /Users/MancoMenStudio/Desktop/KT_Notes_Session1_Updated.docx_

PREGUNTA: Customer Support Knowledge Base / Confluence (aparecía sin info)
RESPUESTA: Aclarado: son contenedores de sección de Confluence, no páginas vacías. Hacer click en la flecha para expandir y ver todas las subpáginas. No es un gap de documentación — era un malentendido de la navegación de Confluence. Lo mismo aplica para Consumer Support Team.

PREGUNTA: Jira no funcionaba
RESPUESTA: Resuelto: era un problema de permisos. Aimee compartió el link correcto del Kanban board y otorgó acceso durante la sesión. Guardar el nuevo link del chat de la sesión.

PREGUNTA: Support Home (revisar todos los documentos)
RESPUESTA: Confirmado: todo lo que no esté bajo "Archive" es relevante. Documentos clave señalados por Aimee:
(1) Client Contacts spreadsheet — lista maestra para notificaciones de outage, por producto/región, hoja principal bloqueada para Aimee y Kristin (actualizar a Juan/Camila). Green rows = clientes en implementation.
(2) Claude Skills list — desactualizada, Aimee la actualizará.
(3) US Support Calendar — schedule del equipo, menos relevante post-transición.

NOTA: Implementation handoff — cuando implementation termina, PM envía email a Aimee/Kristin (actualizar a Juan/Camila) con: nombre del cliente, producto, tipo, delivery engineer, open items. Luego actualizar Client Contacts: remover green, agregar contactos. Ref Confluence: "Project Management to Support Transition".
ACCIÓN: Juan y Camila deben revisar todos los documentos en SharePoint Support Home (empezar con Client Contacts y Claude Skills).

## T-001 (1.4) — Work Items, Azure Blob y GreenPlum — RESUELTO
_chunk 276 · 2026-06-05 · fuente: /Users/MancoMenStudio/Desktop/KT_Notes_Session1_Updated.docx_

PREGUNTA: ¿Qué es exactamente "Work Item not functioning properly"?
RESPUESTA: Work Items son listas de investigación para el personal de Loss Prevention del retailer, generadas desde Secure basadas en datos de transacciones que el retailer envía a Appriss. Delay en carga de datos = Work Items no se generan = LP staff no puede trabajar. Todos los tickets de Work Items son automáticamente HIGH PRIORITY.
Problemas más comunes: (1) Work items no generándose por delay en carga de datos; (2) Datos faltantes para una fecha específica; (3) Carga de datos incompleta.
Proceso: verificar datos recibidos, revisar el upload, luego recargar o pedir al cliente que reenvíe.

PREGUNTA: ¿Los archivos siguen en Azure Blob Containers? ¿Hay planes de migración?
RESPUESTA: La migración a Azure está en progreso pero no completada para todos los clientes. Preguntar a JR el estado actual de la migración.

PREGUNTA: ¿GreenPlum sigue en uso?
RESPUESTA: Sí, aún usado activamente por la mayoría de los clientes. Ruta de migración: GreenPlum → Snowflake → Snowtime. El objetivo es eventualmente eliminar GreenPlum. Sin fecha de finalización fija.

## T-001 (1.5) — L2 Ticket Management: Preguntas abiertas para Session 2
_chunk 277 · 2026-06-05 · fuente: /Users/MancoMenStudio/Desktop/KT_Notes_Session1_Updated.docx_

Preguntas NO cubiertas en Session 1. Llevar a la próxima sesión con Aimee.

TIMELINES:
- ¿Cuáles son los timelines si el cliente no confirma la resolución? Cadencia de pings si hay silencio.

ENGAGE:
- ¿Cómo es el proceso de triage para tickets de Engage?

CANNED RESPONSES:
- ¿Hay alguna automatización de Jira para canned responses?
PENDIENTE: No existe automatización aún. Acción: crear automatización en Jira para canned responses.

IP WHITELISTING:
- ¿Quién tiene acceso a InfoSec?
- ¿Cuál es el timeline de respuesta?

RCS/RTS RESOLUTION DETAILS:
- ¿Hay una definición de cada opción de resolución?

L2 to L3:
- ¿Hay una página por producto?

SOW:
- ¿Tenemos una definición de SOW? ¿Qué hace que un ticket sea relacionado a SOW?

## T-001 (1.6) — Support Data Team: Preguntas abiertas para Session 2
_chunk 278 · 2026-06-05 · fuente: /Users/MancoMenStudio/Desktop/KT_Notes_Session1_Updated.docx_

Preguntas NO cubiertas en Session 1. Llevar a próxima sesión.

SECURE5 ONLY:
- ¿Por qué solo Secure5?
- ¿Cómo es el proceso de triage?
- ¿Qué hace que un ticket requiera un ticket adicional en la cola de Support Data Team?
- ¿Cuál es el timeline de respuesta del data team?

DATAFLOW / SFTP:
- ¿Hay un doc sobre el gateway? (link: trebuco.atlassian.net/wiki/spaces/ARIT/pages/477753638913/Azure+Application+Gateway+Infrastructure+Documentation)
- ¿Hay un doc para SFTP? SFTP Process (For automated Import Feeds) — Confluence (sin info)
- DevOps Repository & Pipeline — Confluence (sin acceso: trebuco.atlassian.net/wiki/spaces/RTS/folder/476111339586)

ON-CALL:
- ¿Cómo obtener acceso a los schedules de on-call?
- ¿Cómo está configurado? ¿Se puede crear un schedule/team que no envíe alertas activas?

REPORTES:
- ¿Cuál es el baseline de las métricas de Retail Customer Support Reports?

## T-002 (2/16) — Customer "Still Working It" Cadence: Preguntas para Session 2
_chunk 279 · 2026-06-05 · fuente: /Users/MancoMenStudio/Downloads/KT Notes - Appriss Juan & Camila.docx_

Referencia: docs.apprissretail.com/products/general/best-practices-when-creating-a-ticket-in-the-portal

PREGUNTAS para Session 2:
- Si el cliente abre un ticket como "incident", ¿se declara como tal aunque en realidad no lo sea?
- ¿Qué actualizaciones son automáticas y cuáles se escriben a mano?

NOTAS: (sin notas aún)
GAPS: (sin gaps documentados aún)

## T-003 — Aged Ticket Close-Out (7/14/28 días): Preguntas para Aimee
_chunk 280 · 2026-06-05 · fuente: /Users/MancoMenStudio/Desktop/KT_Notes_Session1_Updated.docx_

Referencia: Assigned ticket monitoring — Retail Tenant Support — Confluence

ASSIGNED TICKET MONITORING:
- ¿Qué significa exactamente "Support owned" vs "non-Support owned"?
- ¿Quién es el dueño del ticket durante su vida? Cuando pasa a un equipo L3 (Engineering/Delivery), ¿el monitoreo de tiempo de respuesta sigue aplicando? ¿Quién responde al cliente entonces?
- La ventana Critical es 1 hora y la de escalación es 15 minutos — ¿esos 15 minutos cuentan desde el mensaje de Teams o desde que expira la ventana de 1 hora?
- ¿Cuál es la expectativa del cliente en tiempo de respuesta? El doc define ventanas internas (1h/6h/1día) pero no qué se le promete al cliente.
- ¿Las ventanas 1h/6h/1día se pausan mientras el ticket está en "Waiting for Customer" y se reanudan solo cuando el cliente responde?

L2 SUPPORT TEAM TICKET TRIAGE:
- ¿Cuándo se usa OpsGenie vs un mensaje de Teams para Critical/High? ¿Quién recibe el page?
- El label "Support_Data_Team" enruta un ticket a los engineers cross-trained de datos. ¿Qué criterios hacen que un ticket sea del Support Data Team?
- ¿La automatización que trae status/comments de ENG/INT/DO al RCS también resetea el reloj de respuesta del ticket RCS?

L2 TO L3 RCS:
- Delivery vs Engineering están definidos, pero ¿quién decide feasibility/billable cuando Engineering, Delivery y CSM no están de acuerdo?
- "Get help from Engineering without assigning the ticket to them" — ¿cuál es el mecanismo? ¿Pausa el RCS SLA mientras esperamos?

TICKET CLOSURE:
- Después de "Complete", el cliente debe verificar antes de "Closed" — ¿qué pasa si el cliente nunca verifica? ¿Hay auto-close después de N días? (este es probablemente el ciclo 7/14/28 días del título del topic)

NOTA: Agregar definición de cada severidad para mayor claridad.

## T-004 (4/16) — Personal Queue Grooming + Kanban Prep: Preguntas para Session 2
_chunk 652 · 2026-06-12 · fuente: /Users/MancoMenStudio/Downloads/KT Notes - Appriss Juan & Camila.docx_

Referencia: trebuco.atlassian.net/wiki/spaces/RTS/pages/475023081474

PREGUNTAS para Session 2:
- ¿Cómo se decide si un ticket necesita un Tiger Team o un grooming normal?
- ¿Qué capacidades / expertise debería tener el nuevo tiger team?
- ¿Cuál es la cadencia semanal de grooming vs el check diario, y qué se lleva específicamente al Kanban?
- ¿Cómo se organiza por Account Service Level?
- ¿Cuáles son los requisitos para que un ticket esté "ready to discuss"?

NOTAS: (sin notas aún)
GAPS: (sin gaps documentados aún)

## T-005 (5/16) — Customer-Escalation Playbook: Preguntas y gaps para Session 2
_chunk 653 · 2026-06-12 · fuente: /Users/MancoMenStudio/Downloads/KT Notes - Appriss Juan & Camila.docx_

Referencia: trebuco.atlassian.net/wiki/spaces/RTS/pages/474828701731

PREGUNTAS para Session 2:
- ¿Existe un camino separado para una escalación iniciada por el cliente, o hoy es informal?
- ¿Esta guía es para el equipo L1? ¿Cómo interactúa el equipo L2 en estas escalaciones?
- ¿Hay documentación externa sobre este tipo de escalaciones? ¿Cuáles son las expectativas del cliente? ¿Sabe el cliente que fue escalado?
- ¿Cómo se gestionan las escalaciones cuando el cliente las solicita?
- ¿Cuál es la diferencia (en proceso y ejecución) entre una escalación de cliente y una escalación interna?
- ¿Estas alertas reflejan los schedules y políticas en OpsGenie?
- ¿Existe un runbook para gestionar escalaciones?
- ¿Cuál es la definición de un "cliente difícil"? ¿Cómo se maneja? ¿Qué acciones se toman?
- ¿La acción de escalar en el portal del cliente está disponible para todos los clientes? ¿Cuál es el SLA de respuesta al cliente? ¿Quién es el dueño?

GAPS:
- No hay un playbook documentado de escalación iniciada por el cliente.
- Los criterios de involucramiento del CSM en el loop son informales.
- Falta definición de roles en una escalación.
- Falta definición de "cliente difícil": cómo manejarlo y qué acciones tomar.

## T-006 (6/16) — Eng Escalation Packaging Standard: Preguntas para Session 2
_chunk 654 · 2026-06-12 · fuente: /Users/MancoMenStudio/Downloads/KT Notes - Appriss Juan & Camila.docx_

Referencia: trebuco.atlassian.net/wiki/spaces/RTS/pages/123301200564

PREGUNTAS para Session 2:
- ¿Los tags de escalación de Infra/DB y el contacto clave siguen vigentes?

NOTAS:
- Definir con J.R. cuál es el nuevo scope para L2 vs L3.

GAPS: (sin gaps documentados aún)

## T-008 (8/16) — Definiciones de "Done" por tipo de ticket: Preguntas para Session 2
_chunk 655 · 2026-06-12 · fuente: /Users/MancoMenStudio/Downloads/KT Notes - Appriss Juan & Camila.docx_

Referencia: trebuco.atlassian.net/wiki/spaces/RTS/pages/477554638871

PREGUNTAS para Session 2:
- ¿Cómo se define el estado "done" para los distintos root causes / productos?

NOTAS: (sin notas aún)
GAPS: (sin gaps documentados aún)

## T-007, T-071 a T-095 y Adicional — Temas pendientes sin preguntas documentadas aún
_chunk 281 · 2026-06-05 · fuente: /Users/MancoMenStudio/Downloads/KT Notes - Appriss Juan & Camila.docx_

Tópicos con estructura lista pero sin preguntas ni notas documentadas aún. Programar sesiones para cada uno.

T-007 Ticket lifecycle ownership map RCS vs RTS (ref: trebuco.atlassian.net/wiki/spaces/RTS/pages/477554638871)
T-071 Update Rate compliance process
T-088 Jira automation / triggers inventory
T-089 Jira status definitions
T-090 Jira field-by-field reference
T-091 Inbound customer channels by product
T-092 Priority — current state
T-093 Customer-facing docs creation/update process
T-095 Client migration / downtime notification process

ADICIONAL: Maintenance/Outage templates (.oft → Word) — L1 no puede abrir .oft sin Outlook instalado. Convertir a Word.

## Post-Session 1 — Acciones abiertas y resueltas
_chunk 282 · 2026-06-05 · fuente: /Users/MancoMenStudio/Desktop/KT_Notes_Session1_Updated.docx_

ACCIONES ABIERTAS (pendientes de seguimiento):
1. Aimee: verificar que el Excel de CSM Assignments sea accesible para Juan y Camila.
2. Andrea: agregar definición formal de "Dispute" a Confluence (solicitado por Aimee en sesión).
3. Aimee: confirmar con Andrea si existe lista de tiempos de respuesta de dispute por retailer.
4. Aimee: actualizar Claude Skills list en SharePoint.
5. Juan y Camila: configurar reuniones recurrentes de KT con Aimee (1-2 por semana — su calendario está actualizado).
6. Juan y Camila: revisar todos los documentos en SharePoint Support Home (empezar con Client Contacts y Claude Skills).
7. Juan: consultar a JR el estado actual de la migración de Azure Blob.

RESUELTO EN SESSION 1:
✅ Acceso al Kanban board de Jira: era problema de permisos. Aimee compartió el link correcto y otorgó acceso. Guardar del chat de la sesión.
✅ Secciones de Confluence (Customer Support KB, Consumer Support Team): confirmadas como contenedores de navegación, no páginas vacías. Resuelto.

DECISIÓN: Client contact list se mantendrá manualmente por ahora. Razón: herramientas de automatización aún no evaluadas completamente.
