---
name: project_bucket_review_sesion2
description: "Bucket review de la Unificación al 13 ago 2026: 88 tickets etiquetados / 50 abiertos, lo que la reunión agregó a la página de JR y las decisiones abiertas"
metadata: 
  node_type: memory
  type: project
  originSessionId: a8293f75-ab64-479b-971f-f586abf0f63b
  modified: 2026-08-13T18:19:18.748Z
---

Página de JR: **RET20260727 - Platform Unification Jul 26 Wave - Bucket Review**, espacio PBM, pageId **478085283848**. Es distinta de la de Juan (RTS, 478077845530). La sesión 1 fue el 6 ago con 7 de 20 buckets trabajados.

**Conteos verificados al 13 ago 2026: 88 tickets con label de la ola, 50 abiertos.** La página imprime "71 tickets, 46 open, ticket data as at 6 August 16:30 EDT" y sus filas por bucket también están vencidas (Login and Access imprime 21, el link devuelve 25). **La cifra impresa nunca es la fuente de verdad; el link JQL de la propia página sí.** Informe del barrido en https://claude.ai/code/artifact/b12d1d7a-b89c-4f13-9287-219039bc2e6c

**El label de PVH que quité, JR lo volvió a poner.** En RCS-28247 el changelog muestra 2026-08-13T01:27 Juan Martinez quitando `Uni_Jul_26_ReportsExports` (mi llamada de API) y 2026-08-13T04:27 **J.R. Teagle agregándolo de vuelta**. No se re-quitó: es su página y su criterio. La remoción en RCS-27233 sí quedó. Refuerza [[feedback_jira_read_only]]: quitar un label ajeno se propone, no se ejecuta.

**Lo que la reunión del 13 ago agregó a la página** (esto no estaba el 6):
- **Attachments**: adjuntos grandes liberados a PROD la mañana del 13. La subida a blob tenía **tope de 4 MB** y no tenía nada que ver con archivos bloqueados. Cadena de prueba escrita: *"Matt, then Support, then customer"*.
- **Alerts**: fix a PROD el 13. Las smart alerts fallaban por adjunto o documento de impresión ausente en el blob. A Support le toca verificar que el monitoreo de smart alerts esté en pie.
- **Reports/Exports**: PR del export de audit log arriba, se prueba el 13, dueño Jack. **Izenda por fin tiene dueño: Jack**, con la hipótesis de load balancing.
- **Timeouts**: hechos blob append, locks estáticos removidos, log level a ERROR, exception storm removido; Jon confirma mejora en App Insights. Pendiente el módulo HTTP (riesgoso) y **la caché de screen labels, en PR, en USDEV**.
- **Data Integrity**: remediación de usuario bloqueado `UPDATE membership.Users SET Locked = 0 WHERE UserID = X` más purgar (no borrar) la caché del cliente. Ripp debe definir si se permite desbloquear desde la UI.
- **Login/Access**: "Ripp - done - in PR".
- **Location Hierarchy**: resuelto; el problema de Associate / Employee Lookup **no es de la Unificación**.
- **Date/TimeZone**: se agregará a Incident la actualización de timezone por navegador, que la plataforma ya hace y los clientes Incident-only se saltan.

**Juan no tiene ningún ticket abierto en los dos buckets que recibieron fix en PROD.** Su único de Attachments (RCS-28124) ya está Completed. Los tres que ese release destraba son de otros: RCS-28167 y RCS-28331 (Viraj) y RCS-28305 (Camila), los tres en *Waiting for Software Release*. Lo que sí tiene es el pedido directo de Matt y la cadena escrita que lo pone en el medio.

**Decisiones abiertas** (siguen igual salvo Izenda, que ya tiene dueño):
1. **Ray IDs de Vitamin Shoppe.** RCS-27766 y RCS-28289 en WAFAccess; RCS-28032, 28175 y 28214 en SSOMapping. Misma queja. No unificar sin leer el Ray ID — regla de [[reference_waf_cloudflare_bloqueos]].
2. **Izenda: podar o justificar.** RCS-28332 (Sportsman's) empezó *una semana antes* de su migración. Tercer cliente, segunda señal de platform-wide.
3. **Timezone.** RCS-28294 (Vallarta) con el análisis de David Vargas: la IANA timezone solo se escribe por ajax al login, las cuentas Incident-only migradas quedan en UTC. Enlaza con RCS-28065. La página del 13 le da la razón.
4. **La página debe generarse desde los labels**, no a mano.
5. **Dueños para los buckets sin revisar.**

**Cuentas silenciosas: quedan 4.** Hablaron McDonald's (RCS-28223), 3sixty (RCS-28267) y Rack Room (RCS-28330, login arreglado con reset de contraseña = firma del job de Hatter). Faltan chanel, christiandior, indianagrocery.

Ver [[reference_confluence_unificacion_bucket_review]], [[reference_unificacion_patrones]], [[project_estado_abierto_2026_08_13]].
