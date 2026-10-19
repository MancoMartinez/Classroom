---
name: reference_jira_product_type_field
description: "El campo Product Type en Jira (cf[15196]) es el filtro correcto para separar Incident de Secure 5; verificado 6 ago 2026"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 88e09d4f-347d-4f38-b220-2a56ce38322f
  modified: 2026-08-06T18:56:02.202Z
---

**Product Type es un campo real en Jira RCS: `customfield_15196`, en JQL `cf[15196]`.** Está poblado y es confiable. Valores vistos: `Incident (f.k.a. LPMS)`, `Audit (f.k.a. CAMS)`, `Secure 5 - EBR`.

**Es el filtro que hay que usar para cualquier barrido por producto.** El 6 de agosto 2026 se comprobó sobre los 75 tickets de la ola de Unificación: 66 Incident, 6 Audit, 3 Secure 5 - EBR. Los 3 de Secure 5 (RCS-28077, RCS-28172, RCS-28215) fueron exactamente los que Chris Rippingale marcó como "not incident / also secure". Coincidencia perfecta.

Combinado con `issuetype = SOW` (que sacó RCS-28156 y RCS-28158), esos dos campos atrapaban 5 de los 6 errores de clasificación del barrido del 4 de agosto. El barrido correcto habría sido:

```
project = RCS AND cf[15196] = "Incident (f.k.a. LPMS)" AND issuetype = Incident
AND <cuentas> AND created >= <fecha corte>
```

**Trampa de nombres.** `issuetype = Incident` significa "production outage", NO el producto Incident. Y "Secure" es ambiguo: **Secure Incident** (ex-LPMS, módulo de netTrack, el producto migrado) es distinto de **Secure 5 / EBR** (plataforma de datos, dominio del Support Data Team). RCS-28172 dice "Secure 5.4" en la descripción y aun así su issuetype es Incident.

**Cosas rotas en la documentación** (halladas 6 ago 2026, sin corregir):
- El "Secure Incident & Audit — Triage Decision Tree" (Confluence RTS 478022139909, rama 3) manda usar un label `Secure Incident` o `Secure Audit` en Jira. **Cero tickets en RCS/RTS lo tienen en todo 2026.** La convención nunca se implementó; Product Type ya hace ese trabajo.
- "L2 Support Team Ticket Triage" escribe `Support_Data_Team`; "Support Data Team Ticket Triage" escribe `SuppotDataTeam` (sin la r). Ningún ticket tiene la versión con typo.
- El label `Support_Data_Team` NO se aplicó a los 3 tickets de Secure 5 de la ola, así que no sirve como filtro. Product Type sí.

Docs de proceso relevantes en Confluence: L2 Support Team Ticket Triage (477650845697), Support Data Team Ticket Triage (477555982355), GreenPlum Issues Labelling (475990753283, precedente de etiquetar en el intake), Triage Decision Tree (478022139909).

Ver [[reference_jira_rcs_workflow]] y [[reference_confluence_unificacion_bucket_review]].
