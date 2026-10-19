---
name: feedback_fechas_jira_updated
description: No usar created ni updated de la API de Jira como fecha de silencio o de actividad; contar desde el último comentario real
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a8293f75-ab64-479b-971f-f586abf0f63b
  modified: 2026-08-12T15:30:16.182Z
---

Nunca deducir "lleva N días sin respuesta" del campo `created` ni del campo `updated` de la API de Jira. Contar siempre desde el **último comentario real** del hilo, y mirar los SLA del ticket.

**Por qué:** dos errores ya cometidos.

En RCS-28283 usé `created` (14 jul) para decir que el cliente llevaba 29 días esperando. Falso: el ticket vivía en hypercare bajo DO-11495 y solo entró a la cola RCS el 11 de agosto, con el auto-reply el mismo día y el SLA de primera respuesta cumplido. El reloj del cliente empieza cuando el ticket entra a la cola, no cuando se creó.

En el barrido del 12 de agosto, `updated` decía 2026-08-12 en casi todos los tickets de Juan. No era trabajo, era un cambio masivo de labels `Uni_Jul_26_*`. Un `updated` fresco no significa que alguien tocara el ticket.

**Cómo aplicarlo:** pedir el campo `comment` en la consulta, ordenar por `created` del comentario, y filtrar los automáticos (Automation for Jira, acuses de recibo de L1) antes de contar. El panel de SLAs en la UI es la fuente para primera respuesta y tiempo de asignación.

Relacionado: [[feedback_agrupar_no_es_causa_raiz]], [[feedback_borradores_al_final]].
