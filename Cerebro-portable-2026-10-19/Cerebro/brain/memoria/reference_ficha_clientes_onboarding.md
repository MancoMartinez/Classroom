---
name: reference_ficha_clientes_onboarding
description: "Dónde vive la ficha de cada cliente (CSM, PM, dev engineers, client ID): los tickets RCS de Set Up System Monitoring. Incluye la de CWH cliente 248"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 88e09d4f-347d-4f38-b220-2a56ce38322f
  modified: 2026-08-05T20:58:06.785Z
---

Cada cliente tiene su ficha completa en los tickets RCS titulados **"<Cliente> - Set Up System Monitoring - <Producto>"**, uno por producto. Traen client ID, abreviatura, URLs de QA y Prod, ARDM o CRDM, retención, go live, **CSM, PM y Dev Engineers**, y el detalle de los feeds (carpetas, storage account, frecuencia, volúmenes esperados). Es la fuente canónica para saber a quién escalar algo que no es soporte, y no está en Moscú ni en `~/Downloads`, hay que sacarla de Jira.

**Chemist Warehouse (CWH), cliente 248** — de RCS-26977 (EBR) y RCS-26016 (Incident):
- CSM: Bryant McAnnally
- PM: **Ruchi Vora** (es quien convierte los tickets de DO Project Hypercare a RCS)
- Dev Engineers EBR: Ryan Barlow, Katy Scheldberg, Tomasz Sutkowski, Przemysław Dudkiewicz, Bartosz Bereski
- Productos: Secure 5 Core EBR (go live 9 abr 2026) e Incident (12 mar 2026). ARDM, no CRDM. Retención 13 meses.
- Feeds por API en tiempo real, storage `prddatastoreneu`, carpetas `c248_rawdata_*`. ~491k transacciones lunes a viernes, 600+ tiendas.
- Contactos técnicos del cliente: dataengineering@sigmahealthcare.com.au, security@chemistwarehouse.com.au

**Ruta para un change request** (no incidente): decide el PM del cliente, no el ingeniero. Para trabajo de loaders y mapeo ARDM el equipo es pyARDM / Data Ops, dueño **Peyman Motlagh** (ver el KT tracker en Moscú, T-009 y T-012; Luke Du lleva el código pero sale el 30 nov 2026). Primero el PM, después Peyman.

Ver [[project_appriss_support_team]] (roster interno de Support, distinto de esto) y [[feedback_comentarios_reglas]].
