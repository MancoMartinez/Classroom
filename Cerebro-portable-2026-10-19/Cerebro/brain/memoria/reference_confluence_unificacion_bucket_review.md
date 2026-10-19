---
name: reference_confluence_unificacion_bucket_review
description: "La página de Confluence que es la base del retrospective de la Unificación: dónde está, qué contiene y los 3 labels que faltan aplicar en Jira"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 88e09d4f-347d-4f38-b220-2a56ce38322f
  modified: 2026-08-06T14:22:01.983Z
---

**"Platform Unification Jul 26 - Issue Review by Bucket"**, espacio RTS, pageId **478077845530**, autor Juan.
https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478077845530

Es el documento base del retrospective con J.R., Chris Rippingale, Matt Kamminga y Kiran. Responde las cinco preguntas por bucket: qué lo causó, cómo lo arreglamos, qué falta, si está en el checklist de Platform Migration, y cómo lo probamos la próxima vez.

**Versión 4 (6 ago 2026)**: alcance de 61 a **64 tickets** en 19 buckets, verificado contra Jira en vivo, contra el tracker de ADUSA del 5 ago 3:00 PM ET y contra `LPMS Attachment Results 08-04-2026.xlsx`.

**Tres tickets están contados en la página pero NO tienen label en Jira todavía** (regla: Jira es read-only, los aplica Juan a mano). Hasta que se apliquen, el filtro por label devuelve 61 y la página dice 64. El link de la página usa `labels in (...) OR key in (...)` para compensar.
- RCS-28014 → `Uni_Jul_26_SSOMapping` (ADUSA, no tiene ningún label)
- RCS-28166 → `Uni_Jul_26_Permissions` (Stater Bros, creado después del barrido)
- RCS-28167 → `Uni_Jul_26_Attachments` (Stater Bros, creado después del barrido)
- Además RCS-28075 pasa de `Uni_Jul_26_SessionExpiry` a `Uni_Jul_26_Timeouts`.

**El punto más fuerte del documento** es que no hay forma de desbloquear una cuenta ni de cambiar un email, ni para el cliente ni para Support. Lo dijeron por separado J.R. en RCS-28166 ("I'd also like to understand when we can get admins the ability to unlock their own users"), ADUSA en RCS-28053, y RCS-28080 lo dejó como by design. Cada caso se ha resuelto con un UPDATE directo a la base por un solo ingeniero.

Ver [[reference_unificacion_patrones]] y [[feedback_jira_read_only]].
