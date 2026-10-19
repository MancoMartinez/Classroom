---
name: reference_escalacion_l3_procedimiento
description: "Procedimiento real de escalación de RCS a L3: estado, a quién se asigna y qué ticket se auto-crea, según el doc de Aimee"
metadata: 
  node_type: memory
  type: reference
  originSessionId: a8293f75-ab64-479b-971f-f586abf0f63b
  modified: 2026-08-13T18:26:17.210Z
---

Corrección verificada el 13 octubre 2026: consultar `inbox/2026-10-13-l2-l3-rcs-ticket-management.md` antes de aplicar esta memoria. La página 474627801097 versión 26 indica Peter Just para Solutions Experts. Ryan Barlow aclara en su comentario publicado hoy que su cola de Delivery no requiere mensaje adicional de Teams. La guía 478006902856 todavía conserva James DeJohn y Teams a Ryan. Las filas históricas siguientes requieren esas dos correcciones; Engage Engineering y CSM conservan el aviso de Teams de la guía.

Fuente original de esta memoria: **"Escalating Tickets to L3 Departments: Procedures and Responsibilities"**, de Aimee Wadsworth, Confluence espacio RTS, página `478006902856`. Enlazada desde "L2 Support Team Ticket Triage" (`477650845697`), también de Aimee. Esto reemplaza lo que decía la skill `appriss-jira-support`, que tenía el procedimiento mal.

**El ENG no se crea a mano.** La transición de estado lo auto-crea y los comentarios sincronizan en ambos sentidos.

| Destino | Estado | Assignee | Auto-crea |
|---|---|---|---|
| Secure / Incident Engineering | Under Engineering Review | **Shandana Khan** | ENG |
| Engage Engineering | Under Engineering Review | **Ian Williams** + mensaje de Teams | ENG |
| Infrastructure | Under Infrastructure Review | **te quedas tú** | RTAILIT |
| Security / InfoSec | Under Security Review | **te quedas tú** | INFOSEC |
| Delivery, Secure 5 | Under Delivery Review | **Peyman Motlagh** + Sprint `RCS Support Team` | |
| Delivery, Incident | Under Delivery Review | **Ryan Barlow** + mensaje de Teams | |
| Solutions Experts | Under Solutions Experts Review | James DeJohn | |
| CSM | Under CSM Review | el CSM responsable + mensaje de Teams | |

O sea: **solo en Infrastructure y Security el ticket se queda a tu nombre.** En los demás se reasigna.

Verificado de nuevo en vivo el 7 sep 2026 contra la misma pagina de Confluence, `478006902856`,
modificada por ultima vez el 27 ago 2026. Aparece una fila nueva que no estaba en la version del
13 ago: **RTI/RTIaaS**, cambia estado a Under Engineering Review y se deja sin asignar, los
ingenieros la toman de su cola. El resto de la tabla no cambio.

**Blue Team no tiene fila en este doc, ni la tuvo nunca.** No existe ninguna mencion a Blue Team,
Jon Morgan ni Database Services en toda la pagina, en ninguna de las dos versiones revisadas.

**Hallazgo aparte, no documentado en ningun lado.** `getTransitionsForJiraIssue` sobre RCS-28671 el
7 sep 2026 devuelve una transicion real, global y disponible ahora mismo: `Waiting for Database
Services` (id 591), lleva a `Under Database Services Review` (status id 14718), sin pantalla. El
nombre calza con la definicion de Blue Team en Confluence, "Scrum Teams (colours/colors)",
Platform and Database Services, Jon Morgan. Pero esta transicion no aparece en el doc oficial de
Aimee ni en ningun otro documento de Confluence encontrado hasta ahora, y no hay un solo ticket en
tickets/ donde se haya usado. No se sabe si alguien monitorea esa cola, si auto-crea un ticket
enlazado como las demas filas de esta tabla, ni quien queda de assignee. Usarla sin confirmar antes
con alguien de ingenieria es apostar a una cola que puede estar muerta. Precedente real distinto,
RCS-28068 y RCS-27991, Jon Morgan da un dictamen tecnico y es Shandana Khan quien ejecuta la
transicion, normalmente a Accepted into Development, no a Under Database Services Review.

**Confirmado por el propio Jon Morgan, 8 sep 2026, por Teams.** Preguntado directo si Waiting for
Database Services es la ruta real hacia su equipo, respondio: "This should be waiting for
Engineering IMO." Cierra la pregunta. Blue Team no tiene cola propia en Jira. Se llega por Under
Engineering Review con Shandana Khan de assignee, la fila que ya estaba en la tabla oficial, igual
que el precedente de RCS-28068. No usar Waiting for Database Services para escalaciones a Blue
Team.

**Qué debe estar en el ticket antes de escalar**, sin excepción: el entorno (Test, QA o Prod), pasos completos de reproducción con capturas, las notas de IA usadas en el troubleshooting, y cualquier conversación con otros ingenieros que ocurrió fuera del ticket. Además hay que avisarle al cliente que el ticket se está moviendo.

**Esta regla se hace cumplir de verdad.** El 13 ago 2026, entre las 9:43 y las 9:47 ET, Aimee comentó el mismo texto en cuatro tickets de Vedant Shirude (RCS-27971, RCS-28007, RCS-28010, RCS-28247), todos parados en *Under Support Review*: *"before this ticket can be moved to Engineering they need you to add your notes regarding what you did to triage/troubleshoot and explaining what we need from them"*. Juan iba en copia junto con Viraj Kansara, Camila Cortes y J.R. Teagle, no como destinatario. Lección práctica: un ticket puede quedarse semanas atascado no por falta de investigación sino porque la investigación nunca se escribió en el ticket. El RCS-28007 es el caso extremo, tenía la investigación completa de Tyrone Whitney (índice `nci_msft_` faltante, comparación de esquemas) y aun así no pasaba, porque el assignee solo había puesto "CC: Matthew Kamminga".

**Regla de a dónde va** (del doc de onboarding L2, página `477936910361`): código o bug a Engineering, dato o configuración ya en producción a Delivery, cambio facturable al CSM, feature nueva al Feedback Portal.

Nomenclatura de colas: AALPS es ingeniería de Incident, Audit, Aspect legacy y Apis. Secure 5 cubre Secure EBR y Secure 5. Legacy Secure Issues es Secure 4 y Secure 3.

Cierre, del doc de triage L2: se pone en **Complete** con los dos dropdowns de Resolution, el cliente verifica, y después **Closed**. Coincide con [[reference_jira_rcs_workflow]].

Cadencia de actualización exigida por prioridad: Critical cada hora, High diario, Medium y Low al menos una vez por semana aunque no haya cambios.

Relacionado: [[project_flujo_tickets]], [[project_rcs_27973_28283]], [[reference_peyman_motlagh]].
