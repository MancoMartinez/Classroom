---
name: project-flujo-tickets
description: "Flujo obligatorio para trabajar cualquier ticket de Juan — arrancar siempre desde la base de conocimiento, no desde cero."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9fc04b4a-14c1-4cb0-b5b5-97ac10fcabe5
  modified: 2026-07-30T17:21:48.367Z
---

Cada vez que Juan traiga un ticket, **no tratarlo como consulta aislada**. Arrancar consultando la base de conocimiento antes de responder, y entregar un paso a paso concreto de investigación + los mensajes listos.

**Fuentes a consultar, en este orden:**
1. `~/Downloads/Kristine Guide.md` — triage, ciclo de vida de statuses, matriz de escalamiento L3, reglas de prioridad, SLAs, runbooks por producto (APIS, Engage, AALPS). Es la fuente principal.
2. `~/Downloads/Cheat Sheet.docx` — canned responses y notas por cliente.
3. `~/Downloads/Tiger Team tickets Process.docx` — tickets de más de 60 días.
4. Confluence espacio **RTS** (triage, SLAs, statuses) y **AALPS** (APIS). Vía MCP de Atlassian.
5. La base de Moscú: `~/Library/Application Support/InterviewApp/sessions.db` — tabla `meetings` (transcripciones, summary, action_items, decisions), `knowledge_chunks`, `items`. Ahí están las reuniones grabadas, que muchas veces tienen el RCA antes de que llegue al ticket.
6. Docs de proceso sueltos en `~/Downloads/` (Engage, LPMS, etc.) y adjuntos en `RCS-*_attachments/`.
7. Jira, **solo lectura** — ver [[feedback-jira-read-only]].

**Qué debe salir siempre:** el triage correcto (tipo, prioridad, status que refleje quién tiene la siguiente acción, labels), los pasos de investigación aterrizados en los runbooks de la guía, y los comentarios interno y de cliente redactados listos para pegar según las reglas de la skill `appriss-jira-support` (interno terse y técnico; cliente neutral y factual, sin filler ni especulación).

**Why:** Juan pidió explícitamente (30 jul 2026) que dejara de ser una consulta individual por ticket y pasara a ser un flujo con el conocimiento base ya cargado. Solo debería preguntar por contexto extra cuando él tenga chats o info que no está en ninguna fuente.

**Pendiente en Moscú:** Juan quiere esta misma función dentro del chat de la app — que al mencionar un ticket se disparen automáticamente el RAG de la guía, las reuniones y los adjuntos. No implementado.

Relacionado: [[project-appriss-support-role]], [[project-juan-accesos]]
