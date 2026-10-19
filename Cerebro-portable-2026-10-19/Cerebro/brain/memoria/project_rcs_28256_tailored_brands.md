---
name: project_rcs_28256_tailored_brands
description: "RCS-28256 Tailored Brands al 13 ago 2026: sign in resuelto, quedan el salto lento a Incident y el timeout de Izenda (dueño: Jack), y cómo remedirlo"
metadata: 
  node_type: memory
  type: project
  originSessionId: 254b4d73-4509-4741-99d1-56c88cb6d56c
  modified: 2026-08-13T18:20:28.494Z
---

Tailored Brands, **Client ID 209, tenant `tbi`**, base `sqldb-prd-wus2-arp-production-209-tbi-platform`. Contactos: Colton Neal y Mike DiTommaso. SLA de resolución ya vencido (11 ago 4:02 PM, en rojo).

**Cronología cerrada**

- 10 ago 12:12 — Jon Morgan encuentra `Feature.Incident.EnableAdHocInitCaching` y `Feature.Incident.EnableAdHocPerRequestUserScope` apagados por el release. No los apagó nadie: faltaban en la tabla de seed history y el default es false, así que el despliegue los reseteó. Los vuelve a encender, corre lunar para todos los clientes que necesitaban el config item y levanta PRs retroactivos en `arpfiles` (release 55855, main 55856).
- 10 ago 12:28 — Jon: los tiempos de respuesta bajan tras encenderlos, con gráficas de App Insights.
- 10 ago 15:51 — Matt pregunta si sigue lento. Kiran responde **"Hitting cloudflare"** con captura de un **524 en el tenant del propio cliente**, `apps.apprissretail.com/tailoredbrands/nettrack/AdHoc/reportlist.aspx`, edge Ashburn. Es **después** del arreglo de Jon.
- 10 ago 15:52 — Matt: "can you validate the 3 FF that jon had posted above for tbi directly… you will want to review via DB, not from control panel". Kiran lo hace y publica el resultado (IDs 1077, 1078, 1087).
- 11 ago 13:19 — Kiran cierra la hipótesis del despliegue faltante: **"No. Once deployed, all the clients get the same code."** El hotfix de RCS-28084 está en este tenant.
- 11 ago 18:56:16 UTC — Colton comenta en el ticket: timeouts y creación de incidentes resueltos para los usuarios con los que habló, **el reporting de Izenda sigue cayendo**. Captura con **Cloudflare 524, Ray ID `a299728c9ee465e3`**, host `us.apprissretail.com`. La IP del cliente no está: la página dice "Your IP: Click to reveal".

**Valores verificados en la base del 209** (los mismos que Kiran publicó, misma marca de milisegundo):

| Flag | Value | CustomerEditedValue |
|---|---|---|
| `Feature.Incident.EnableAdHocInitCaching` | True | True |
| `Feature.Incident.EnableAdHocPerRequestUserScope` | True | True |
| `Feature.Incident.EnableBlobAppendLogging` | False | False, editado 2026-08-10 14:09:57 UTC |

**Qué queda abierto:** solo el timeout de Izenda (`nettrack/AdHoc/reportlist.aspx`), sin dueño asignado. Y confirmar cuál debería ser el valor de `EnableBlobAppendLogging`, el único en False.

**Qué está descartado y no hay que volver a mirar:** los dos flags de AdHoc (confirmados True), y un despliegue faltante. **No hace falta pedirle nada más al cliente**: Kiran reprodujo el fallo contra el tenant de ellos.

**Causa raíz encontrada el 10 ago: regresión de plan de ejecución.** Las consultas de LPUser pasaron de 0,5–0,8 s a 57 s de promedio (120 s máximo) desde el 6 ago 17:35 UTC, mismos query IDs, planes nuevos: los buenos con estimador de cardinalidad 140, los malos con 160. 3 bases afectadas de las 39 que corren la consulta. El máximo de 120 s es el `CommandTimeout` de la app y Cloudflare corta a los 100 s, de ahí el 524. Procedimiento completo en [[reference_query_store_regresion_plan]].

**Actualización 13 ago 2026**

- **Izenda ya tiene dueño: Jack**, según la página de bucket review, con hipótesis de load balancing. Es el nombre que Juan venía pidiendo desde el 11.
- Sigue sin haber **una sola medición propia**. Todo son autorreportes de Colton (39 s, luego ~30 s), Mike DiTommaso ~45 s y Sam Fuentes ~45 s (los dos el 12 ago 15:25). Nadie ha documentado cuánto *debería* tardar el salto de Secure a Incident, así que "30 segundos" solo no significa nada.
- **Protocolo de remedición** en 6 fases (tenant de control → DevTools → Query Store → flags → Izenda aparte → conclusión) escrito en el artifact de la mesa de trabajo: https://claude.ai/code/artifact/41529835-12f4-4819-a814-b105c9819bba. El método general quedó en [[reference_medir_lentitud_web_devtools]].
- **El discriminador que decide el caso:** si los TTFB se comen los 30–45 s, el tiempo está en el servidor y la caché de screen labels de Chris (en PR, en USDEV) no le arregla nada a este cliente; si los TTFB son rápidos y el total es alto por cientos de requests pequeños, esa caché es exactamente el arreglo.
- **ENG-7182** está enlazado pero acotado al 524 al guardar, que es justo lo que el cliente dice que ya funciona, y sigue en Backlog. Hay que confirmar si debe cubrir el 524 de Izenda o si va uno nuevo.

Referencia ENG-6777, que Matt enlazó para el fallo de *export* de Izenda de Vitamin Shoppe (RCS-28151, de Diego Buelvas). Es referencia, no está establecido que sea el mismo defecto.

Ver [[reference_configuration_items_features]], [[reference_waf_cloudflare_bloqueos]], [[reference_acceso_sql_tenants]].
