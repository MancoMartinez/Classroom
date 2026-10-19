---
name: project-appriss-support-role
description: Juan es L2 Support Engineer en Appriss Retail (cola RCS en trebuco.atlassian.net); contexto de la migración/unificación de Incident en curso desde julio 2026.
metadata: 
  node_type: memory
  type: project
  originSessionId: 9fc04b4a-14c1-4cb0-b5b5-97ac10fcabe5
  modified: 2026-07-30T14:51:13.750Z
---

Juan Martinez (jmartinez@apprissretail.com) trabaja como **L2 Support Engineer** en Appriss Retail. Su cola es el proyecto **RCS** (Retail Customer Support, L1/L2) en `trebuco.atlassian.net`; **RTS** es Retail Tenant Support (automatización/monitoreo).

**Contexto mayor (desde jul 2026):** migración + unificación de la plataforma Incident (LPMS/NetTrack). Los clientes salen de los servidores legacy `apps.lpguys.net/<slug>` y `<ABV>.apprissretailcloud.com` hacia la plataforma unificada `apps.apprissretail.com/<slug>`. 143 clientes en 6 fases; ~31% en prod a fines de julio 2026. Tracker: `~/Downloads/Investigacion migracion e unificacion/Incident Migration 2026.xlsx`.

**El cambio arquitectónico que causa la mayoría de los incidentes post-cutover:** en legacy cada cliente tenía su propio servidor, así que la config por servidor (zona horaria del OS, storage de attachments, endpoints de Izenda, jerarquías de stores) servía a un solo tenant. En la plataforma unificada **los tenants comparten servidor**, así que nada de eso puede seguir resolviéndose a nivel de servidor.

**Documentación operativa de referencia** (en `~/Downloads/`): `Kristine Guide.md` es la fuente principal — modelo de triage L1/L2/L3, ciclo de vida de statuses, matriz de escalamiento, reglas de prioridad, SLAs. `Tiger Team tickets Process.docx` cubre tickets de más de 60 días.

Ver [[feedback-jira-read-only]] para cómo trabajar sus tickets.
