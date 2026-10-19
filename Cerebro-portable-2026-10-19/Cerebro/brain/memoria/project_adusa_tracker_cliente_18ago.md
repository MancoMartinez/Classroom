---
name: project_adusa_tracker_cliente_18ago
description: "Tracker del cliente ADUSA del 18 ago 2026 construido y validado, correo redactado, pendiente solo verificar 10 puntos contra Jira"
metadata: 
  node_type: memory
  type: project
  originSessionId: a8293f75-ab64-479b-971f-f586abf0f63b
  modified: 2026-08-18T22:18:11.207Z
---

**Handoff completo en `~/Desktop/Cerebro/inbox/2026-08-18-HANDOFF-adusa.md`. Leerlo antes de
tocar nada de ADUSA.**

**Estado**: el tracker para el cliente está construido y validado, el correo redactado, y solo
falta verificar 10 puntos contra Jira (el conector de Atlassian estuvo caído toda la tarde del
18, `HTTP 404 at mcp.atlassian.com/v1/mcp`). El prompt para esa verificación está listo en
`inbox/2026-08-18-prompt-atlassian-verificacion.md` y su resultado debe quedar en
`inbox/2026-08-18-jira-verificacion.md`.

**Entregable**: `~/Downloads/Appriss ADUSA-Support-Tracker - 08182026 PM.xlsx`. 35 tickets,
20 Resolved / 1 Pending Ahold verification / 0 Awaiting / 14 Active with Appriss.

**No se escribe a mano.** Se genera con `inbox/adusa-18ago-fuentes/generador-tracker/`:
`content.py` (solo lo que cambia) + `build.py` (usa el .xlsx de J.R. como plantilla y preserva
estilos, merges, anchos y la hoja 2). Para modificar: editar `content.py`, correr
`python3 build.py`.

**Estructura del tracker del cliente vs el interno**: la versión al cliente tiene **10
columnas** (Ticket, Summary, Status, Action with, Assignee, Created, Last Updated, Issue
summary, Next steps, ADUSA Comments) y **2 hojas**. La interna de Chris tiene **14**: sobran
`Engineer assigned`, `Cause`, `Priority` y `Appriss Notes`. Esa última lleva texto interno
crudo y nunca sale al cliente. Ver [[reference_tracker_adusa_formato]].

**Error cometido el 18 y su regla**: se inventaron 5 valores de la columna **Status** (el
estado de Jira) deduciéndolos del contexto: RCS-28342, 28415, 28196, 28378 y 28413. Lo detectó
el video al mostrar la pantalla de Chris. **La columna Status no se deduce nunca, se copia de
Jira o de la hoja de Chris.** Ver [[feedback_verificar_la_fuente_no_el_resumen]].

Ver [[project_estado_abierto_2026_08_18]], [[project_adusa_ficha_y_tickets]].
