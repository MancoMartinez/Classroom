---
name: reference_proceso_rca_appriss
description: "Proceso oficial de RCA en Appriss (Shorthand vs Report, SLA desde resolución, ticket OUTM previo, tres Claude Skills existentes) verificado en Confluence el 18 ago 2026"
metadata: 
  node_type: memory
  type: reference
  originSessionId: a8293f75-ab64-479b-971f-f586abf0f63b
  modified: 2026-08-18T17:44:00.432Z
---

Guía completa consultable en `~/Desktop/Cerebro/inbox/2026-08-18-guia-proceso-rca.md` y en
Moscú, carpeta 19 "RCS — Procesos & Playbook", chunk 1673. Puntos que no hay que
re-investigar:

- **Dos documentos, no uno.** Shorthand RCA (2-3 frases, en el ticket o correo, SLA 1 día
  para Critical/High) y RCA Report (documento completo aparte, SLA 10 días para
  Critical/High). Plantillas en Confluence: RCA Ticket Template (474654900291) y RCA
  Report Template (474654965776), espacio RSI.
- **El SLA corre desde la resolución del incidente, no desde que el cliente lo pide.** Si
  el outage sigue activo, solo corresponde el Shorthand.
- **Falta el ticket OUTM antes del RCA.** El "Outage Ticket Process" (Confluence RTS
  478022696993) pide crear un ticket OUTM con Timeline/Classification/Root Cause antes de
  escalar a RCA. Confirmado que no existe ninguno para Stater Bros al 18 ago.
- **Tres Claude Skills ya construidos para esto**, ninguno instalado en esta máquina:
  `appriss-rca-generator` (interno, de Avi), `appriss-rca-generator-retro` (worksheet
  pre-llenado desde Jira, marca en verde lo ya sabido y en blanco lo que falta),
  `appriss-rca-generator-external` (PDF final para cliente, 13 secciones, sin nombres
  propios ni tickets Jira ni jerga interna, dueños de action items por rol). Adjuntos en
  las páginas Confluence RTS 477550018564 / 477856825345 / 477584359429. Orden correcto:
  retro primero, external después.
- **Precedente de comportamiento a seguir: RCS-27009** (Sainsbury's, Dean Korbakis, mismo
  puesto que Juan). Causa confirmada primero en Teams por quien la vivió, luego llamada
  interna con ingenieros, aviso de retraso si hace falta, publicación solo con causa
  confirmada. RCS-20226 (2025) es solo informal, no sirve de molde de comportamiento.

Ver [[project_moscu_sin_gpt]], [[project_flujo_trabajo_cerebro]].
