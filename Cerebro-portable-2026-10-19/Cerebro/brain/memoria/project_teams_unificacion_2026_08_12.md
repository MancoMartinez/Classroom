---
name: project_teams_unificacion_2026_08_12
description: "Chat de Unificación, 12 ago 2026: performance de Chris, PRs 55640 y 55972, AutoZone P1 no es unificación, flags de Walmart 300"
metadata: 
  node_type: memory
  type: project
  originSessionId: a8293f75-ab64-479b-971f-f586abf0f63b
  modified: 2026-08-12T14:33:01.041Z
---

Lo que pasó en el chat de Unificación el 12 de agosto de 2026.

**Performance (hilo de Chris Rippingale).** Análisis del 12 ago: blob y SQL ya están baratos, 0 a 137 ms, o sea el cuello dejó de estar ahí. Quedan dos cosas abiertas:
- La tormenta de excepciones sigue. PR `55640` en Azure DevOps (Sysrepublic Secure). Le advirtieron que necesita mucha prueba antes de mergear.
- Hallazgo nuevo: `GetScreenLabelByFormField` hace cientos de llamadas a base por recursos, sin caché. PR `55972`.

Sirve como causa candidata para las quejas de lentitud y de pantallas que no cargan, pero no está confirmado como causa de ningún ticket concreto ([[feedback_agrupar_no_es_causa_raiz]]).

**Walmart, cliente 300.** Las optimizaciones no estaban activas para ellos. Jon Morgan encendió los flags en la columna Value ese mismo día, con demora porque no pudo conectarse desde el jump server normal, lo está viendo con Jessey. Ver [[reference_configuration_items_features]].

**RCS-28313 AutoZone, P1, Secure Incident no carga.** Shreyas lo atribuyó al despliegue mensual de LPMS, con NODE I siendo redesplegado por Matt, todavía en `lpguys.net`. **Matt Kamminga confirmó que el despliegue falló y que no tiene relación con la unificación.** La hoja de seguimiento del cliente decía migración el 14 de septiembre. El arreglo de attachments sale con el release de la mañana del 13 de agosto. Camila lleva la comunicación al cliente.

**RCS-28307 Smart & Final**, usuario no puede enviar casos. Lo reportó Neha Haridas y lo tomó ella misma.

Relacionado: [[project_estado_juan_2026_08_11]], [[reference_erms_lpms_descarga_pdf]], [[project_appriss_support_team]].
