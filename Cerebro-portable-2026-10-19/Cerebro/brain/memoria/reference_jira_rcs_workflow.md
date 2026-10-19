---
name: reference_jira_rcs_workflow
description: "Cómo se cierra de verdad un ticket RCS: Resolve a Completed y después Close, y por qué el botón Close Ticket nunca aparece"
metadata: 
  node_type: memory
  type: reference
  originSessionId: f1250f28-e367-4743-9ca8-90b661b376fc
  modified: 2026-08-04T23:34:35.771Z
---

Verificado por API el 4 ago 2026 sobre tickets tipo **Incident** en RCS.

**Cerrar son dos pasos, los dos los puede hacer Juan.**

1. **Resolve** (transición 111), desde `Work in progress` a **`Completed`**. Abre pantalla y pide Resolution Details. Una automatización confirma el valor con un comentario del tipo *"Resolution Details has been set to: Support Resolved - Fixed Configuration"*.
2. **Close** (transición 91), desde `Completed` a **`Closed`**. Solo existe estando en Completed, y ahí sí está disponible.

**Por qué parece que no se puede cerrar.** Hay dos transiciones distintas hacia `Closed`. La global se llama **Close Ticket** (581), es condicional y llega siempre con `isAvailable: false`, así que nunca se ve el botón. La que sirve se llama solo **Close** (91) y aparece únicamente cuando el ticket ya está en Completed. Buscar el botón desde `Work in progress` es perder el tiempo.

**Nada cierra solo.** No hay automatización que pase de Completed a Closed. Un ticket resuelto y no cerrado se queda en Completed indefinidamente. Revisar cada tanto con `assignee = currentUser() AND status = Completed`.

**Cuando el cliente responde, la automatización devuelve el ticket a `Work in progress`** desde `Under Customer Review`. Por eso un ticket con respuesta del cliente aparece de nuevo como activo.

**Secuencia completa que usa el equipo** (ejemplo real, Viraj en RCS-28030 el 4 ago, tres acciones en 76 segundos):

1. Comentario al cliente confirmando el cierre.
2. Comentario interno con lo que realmente se arregló, que alimenta el Resolution Details.
3. Resolve, después Close.

**Si le prometiste al cliente que ibas a cerrar, cierra en ese momento.** En RCS-28030 Juan escribió *"I'll go ahead and close this ticket"* y lo dejó en `Under Customer Review`. Al día siguiente Leigh Ann tuvo que pedirlo otra vez y lo cerró Viraj.

Existe también el estado `Needs attention - add resolution details` para los que se resuelven sin llenar ese campo.

Otras transiciones útiles: 571 Under Customer Review · 641 Under Support Review · 561 Escalate Ticket · 551 Work in progress · 651 Duplicate · 121 Back to work in progress (desde Completed).

Los IDs varían por tipo de issue, así que no asumirlos entre tipos distintos.

Ver [[feedback_jira_read_only]] y [[feedback_comentarios_reglas]].
