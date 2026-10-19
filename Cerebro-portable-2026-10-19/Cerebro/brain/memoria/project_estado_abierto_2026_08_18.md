---
name: project_estado_abierto_2026_08_18
description: "Estado abierto al 18 ago 2026 tarde — RCS-28379/Izenda global (ENG-5649), Stater Bros RCA (RCS-28431 sigue activo), tracker ADUSA del día"
metadata: 
  node_type: memory
  type: project
  originSessionId: a8293f75-ab64-479b-971f-f586abf0f63b
  modified: 2026-08-18T19:58:54.982Z
---

Detalle completo consolidado en Moscú, carpeta 26 "ADUSA — Estado, Tickets & Reuniones",
chunk 1674, y en `~/Desktop/Cerebro/inbox/2026-08-18-guia-proceso-rca.md`.

**RCS-28379** (Case Owner/Creator/Assigned en blanco): Kiran ya tiene el mapeo
UserID<->LoginID hecho, revisando ~100 registros de MasterCase/Shoplifting. No cerrado,
con progreso real.

**Izenda global**: falla de exportación confirmada por Matt para todos los clientes,
Diego se está asignando. Corresponde a **ENG-5649** ("Ready for Development", dueño Scott
Buric, actualizado hoy). Causa: operaciones de exportación no reciben el contexto
pCohesion en modo Platform Cohesion; cuando funciona, cae a connection string vieja con
filtros de reporte guardados. Alcance documentado: Guess, Tailored Brands, Casey's,
Chemist Warehouse, WSS, PVH, Alo Yoga, Secure Integration — **Stater Bros y ADUSA no
aparecen nombrados ahí todavía**, aunque el patrón es el mismo que RCS-28058 (adjuntos
Stater Bros). RCS-28379 NO tiene relación causal con esto, solo coincide en fecha.

**Stater Bros (RCS-28431)**: sigue activo hoy, última reincidencia reportada 12:39pm.
Causa raíz del outage 17-18 ago genuinamente no documentada en ningún ticket (RTS-206092
es solo un duplicado cerrado sin narrativa técnica). RCS-27269 fue una cita errónea en un
RCA de otra herramienta, sin relación real, debe quitarse. J.R. pidió RCA formal por
correo; según [[reference_proceso_rca_appriss]] el SLA del Report corre desde la
resolución, y como el outage sigue activo solo corresponde el Shorthand por ahora.

**Reunión cliente ADUSA (Chris/Matt presentando), 18 ago, transcrita en vivo por Moscú.**
Detalle completo en `~/Desktop/Cerebro/inbox/2026-08-18-reunion-cliente-causa-raiz-izenda.md`
(pendiente de pasar a Moscú carpeta 26 cuando la app se cierre, estaba transcribiendo).
Lo confirmado en vivo por Appriss, no inferido:
- **Causa raíz de los 502 en Incident**: la carga de Izenda/Reporting dispara el conteo de
  threads y eso tumba la app de Incident. Confirma en vivo ENG-5649/RCS-28058. Prioridad 1
  de Appriss: separar ambos sistemas. Esperan luz verde de QA esta semana.
- RCS-28177: Jonathan Wright confirmado, pregunta abierta sin resolver (fix específico o
  universal); otra usuaria confirmó resuelto en vivo.
- RCS-28342: causa aclarada — el título llega como SSO claim desde Active Directory y no
  sincroniza a LPMS para una lista de usuarios, no es un caso aislado.
- RCS-28093: número de tienda no es único entre marcas, el dato de marca llega intermitente
  en un campo "miscellaneous 1". Prioridad baja, confirmado en vivo.
- RCS-28196: resuelto y probado, pero el campo ahora exige Sí/No aunque nadie contestó —
  duda de UX sin cerrar.
- RCS-28124: los archivos .txt no funcionan al subir adjuntos, pendiente confirmar con
  Leigh Ann si eso se usa en ADUSA.
- RCS-28413: confirmado que es un reporte programado exportado de Izenda (no manual),
  bajó de ~268 a 67 registros; Appriss va a mandar el conteo real.

**Reconciliación de barrido (13:41, ver
`~/Desktop/Cerebro/inbox/2026-08-18-reconciliacion-28021-28196-28415.md`):** RCS-28196 y
RCS-28415 sí estaban confirmados resueltos por fuentes propias antes de comentar al
cliente. **RCS-28021 NO estaba confirmado** — el síntoma real (export a Excel no hace
nada) seguía sin arreglo según Leigh Ann 17 ago, solo se arregló el síntoma del scheduler
con datos viejos. Es el mismo error del 14 ago repetido (confundir el visor con la
entrega programada), documentado en [[feedback_verificar_la_fuente_no_el_resumen]].

**Cheat sheet bilingüe para la llamada:**
`~/Desktop/Cerebro/inbox/2026-08-18-cheatsheet-adusa-tracker2.html`, los 35 tickets del
tracker Tracker-2 de Chris, respuesta corta ES/EN por ticket, buscador. Abrir con
`open "~/Desktop/Cerebro/inbox/2026-08-18-cheatsheet-adusa-tracker2.html"`.

Ver [[reference_proceso_rca_appriss]], [[project_adusa_ficha_y_tickets]],
[[reference_esquema_usuarios_incident]], [[feedback_verificar_la_fuente_no_el_resumen]].
