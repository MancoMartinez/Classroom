---
name: project_estado_abierto_2026_08_05
description: "Estado del trabajo abierto al 5 ago 2026: RCS-28075, pedido de la próxima ola de unificación, y dónde están los documentos nuevos"
metadata: 
  node_type: memory
  type: project
  originSessionId: dcaa0a43-9bf1-4e1e-a4f3-8c5929cae784
  modified: 2026-08-05T20:10:42.044Z
---

Corte del 5 ago 2026, antes de un reinicio de la máquina.

**Documentos nuevos en `~/Downloads`**, ninguno importado a Moscú todavía (la app estaba corriendo, hay que arrastrarlos a la carpeta "Reuniones — Prep" para que el importador los procese):
- `HANDOFF-RCS-28075-2026-08-05.md` — análisis completo del ticket con los tres borradores de mensaje
- `REUNION-L2-L3-2026-08-05.md` — readout de la reunión del 5 ago (meeting 94 en Moscú)
- `SYNC-L2-L3-RESUMEN-BILINGUE-2026-08-05.md` — qué decir en el sync, inglés y español

**RCS-28075 (Ahold, Escalated, dueño Vedant Shirude)** es lo más urgente. Tiene dos problemas metidos en uno: los timeouts que escaló Jim Cosseboom el 1 ago (abierto) y el bloqueo de Leigh Ann y April, que Juan resolvió el 3 ago restaurando el permission group `Administrators` más los tres básicos, y que solo espera confirmación del cliente. Vedant pidió ayuda porque no entendía ese comentario.

Lo accionable, en orden: (1) confirmar si el hotfix que cerró el **RCS-28084** llegó al tenant adusa, porque la URL que dio el cliente es `NewIncident.aspx` y es la misma operación; (2) preguntar a Chris Rippingale o a Jack si se hizo el cambio de thumbnails de Izenda que Chris propuso el 31 jul y nadie cerró; (3) update al cliente, lleva días quieto estando escalado. Ver [[reference_unificacion_patrones]] para el error de label que se corrigió.

**Pedido pendiente de la reunión del 5 ago:** J.R. y el equipo pidieron sugerencias a Juan y a Camila para la próxima ola de unificación, por nombre. Esperan **80 a 90 tickets** contra los 61 de la ola de 20 clientes. Lo que Juan tiene para ofrecer es la verificación de correos contra los 10 clientes del 10 de agosto **antes** del corte, que es lo que evita que el bucket de SSO mapping (el más grande, 14 tickets) se multiplique.

**Otros pendientes vivos:** el label correcto para tickets de Incident sigue sin respuesta de J.R.; los 5 de Chemist Warehouse esperan decisión; el valor real del timeout de sesión por tenant no está confirmado (Kiran dijo 30, Engineering 60/240 en RCS-28153); RCS-27549 (ICA SE, High, RCA formal) sigue en la cuenta desactivada de Carlos Jacinto; RCS-27941 de Tailored Brands corre SLA con la acción del lado de Juan.

**Cola verificada por API el 5 ago 14:00** (artefacto "Mi cola RCS", https://claude.ai/code/artifact/65167352-8403-47dc-8bc0-2a40acc81db8): 21 tickets de Juan, 14 abiertos (7 Work in progress, 1 Resolution Suggested, 6 Under Customer Review) y 7 cerrados. **Sin asignar: 36**, de los cuales 22 entraron después de la reunión del 4 ago y 14 son arrastre del triage del 3 ago. El reparto de ayer no bajó la cola, la dejó igual. RCS-27798 (PVH Corp, High) lleva 23 días sin asignar y sin tocar.

**Infra:** el MCP de Atlassian Rovo **sí funciona** en esta sesión (scopes read:jira-work y write:jira-work sobre trebuco.atlassian.net, cloudId `7eb600cf-c7e0-43ed-acc4-90b277d43514`). Las consultas JQL devuelven más tokens de los que caben, hay que procesarlas con jq sobre el archivo que guarda la herramienta. Backup de la base hecho en `sessions.db.bak-pre-reboot-20260805-1051`.

Ver [[project_appriss_support_role]], [[project_backlog_triage_2026_08_03]], [[feedback_jira_read_only]].
