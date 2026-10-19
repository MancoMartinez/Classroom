# SnowTime — Monitoring & Migración

Carpeta 20 de la base de Moscú. 10 fragmentos.

## KT SnowTime 2026-07-02 — Monitoreo, KPIs y proceso de migración (Raman Kumar + Nitish Raj)
_chunk 1089 · 2026-07-02 · fuente: Teams meeting 2026-07-02_

Reunión "Snow Time Migration and Monitoring" (2-jul-2026, 37 min). Presentaron Raman Kumar y Nitish Raj a Viraj + equipo RTS. Juan hizo 2 preguntas que produjeron entregables.

DASHBOARD DE MONITOREO (SnowTime monitoring): página única para clientes US y EU. Pipeline: feeds → loader → transformación DBT (raw → staging → ARDM final) → business teams. 6 áreas monitoreadas: (1) file arrival vs histórico, (2) data loader (archivos corruptos, formato inválido, loader caído; fallas file-level y row-level), (3) DBT/transformación (fallas por corrida), (4) pipeline scheduler (trigger horario de DBT sobre data nueva en raw), (5) data quality (duplicados/nulls en primary keys de tablas ARDM — header, operation action, tender), (6) volume trends. Histórico consultable: hasta 180 días (6 meses).

KPIs CLAVE: • Volume trends: patrón cíclico por día de semana (domingo bajo, viernes >1M transacciones); línea azul = actual, punteada = promedio del day-of-week. • Data readiness: % de data lista vs promedio histórico intradía; para clientes trickle (envían cada hora) y batch (ej. Corp client que manda todo ~11PM — se espera hasta esa hora antes de alertar; umbral ej. 2.5M transacciones esperadas, alerta si <5% recibido). Si el SLA del cliente es "data lista a las 7PM" y el ARDM no la tiene, breach. • Trading day distribution: qué % de la data de un día pertenece a ese trading day (algunos clientes envían 100% del mismo día al cierre de tiendas; otros 10% día anterior + 90% antier). Drift = recibir data de un trading day inesperado → preguntar al cliente.

FILE ARRIVAL RULES: cada feed tiene reglas (auto-asignadas o manuales). Ej. fraud prevention: histórico llega ~12PM → deadline con slack = 1PM → si se pasa, breach y alerta inmediata. Breaches múltiples del mismo cliente el mismo día NO crean tickets separados: se agregan como COMENTARIO al mismo ticket.

MIGRACIÓN (Greenplum → Snowflake/SnowTime): etapas: desarrollo → PROD PARALLEL (staging, ~1 semana; solo team alerts, los devs las atienden, NO soporte) → LIVE (alertas RTS Jira automáticas). Validación en prod parallel: dashboard de comparación que joinea tablas finales SnowTime vs Greenplum, row counts + valores columna por columna; se exigen 5 días de "clean numbers" antes del cutover. Si valores no alinean = bug de lógica en transformación (se arregla ANTES del go-live). Go-live: los devs llaman stored procedure ARDM_LAB_PRODUCTION.MONITORING.SP_UPDATE_CLIENT_CONFIG con listas de live_clients y prod_parallel_clients (transición usualmente a medianoche); luego avisar a Austin Flannery para actualizar Jira out-of-hours alerts.

FALLAS TÍPICAS POST-MIGRACIÓN (respuesta a Viraj): (1) en prod parallel: DBT failures por data real (formatos, casting no manejado) — responsabilidad del dev madurar la lógica; (2) en live: file arrival breaches (soporte hace RCA, contacta cliente por email) y data loader con archivos corruptos (reintentar no sirve — falla siempre).

PENDIENTES/RECURSOS: • Nitish comparte: Excel de clientes migrados por semana (para correlacionar tickets con migraciones recientes — pregunta de Viraj) + link del dashboard de comparación (pregunta de Juan). • Lista de clientes en transformación: sprint activo en Jira board. • FAQ: https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/477664444418/FAQs

## SnowTime FAQ — Acceso y permisos (dashboard Streamlit-in-Snowflake)
_chunk 1090 · 2026-07-02 · fuente: Confluence ARPDT 477664444418_

Fuente: Confluence ARPDT pageId 477664444418 "FAQs" (Raman Kumar, act. jun-2026).

ACCESO: el dashboard es una app Streamlit-in-Snowflake, corre en el browser dentro de Snowflake — sin VPN ni instalación. Links directos: EU = app.snowflake.com/streamlit/okb13541/neuaz/#/apps/az3znzw6tli65q5uxotf · US = app.snowflake.com/streamlit/okb13541/jn80103/#/apps/c5ed652cmowhxeustg3t

ROL REQUERIDO: SNOWTIME_ENGINEERING_ROLE o SNOWTIME_SUPPORT en tu usuario Snowflake — da lectura al schema ARDM_LAB_PRODUCTION.MONITORING. El dashboard es READ-ONLY: no se cierran incidentes ni se cambia config desde ahí; el ciclo de vida de incidentes es 100% en Jira.

CONTACTOS: • Role grants / acceso Snowflake → Christopher Beck (también Daniel Endersby según Quick Reference) • Errores del dashboard / feature requests / creación de tickets Jira → Raman Kumar. Compartir el link a alguien sin el rol = error de acceso; pedir grant al admin.

## SnowTime FAQ — Básicos del dashboard: refrescos y semáforo de salud
_chunk 1091 · 2026-07-02 · fuente: Confluence ARPDT 477664444418_

Fuente: Confluence ARPDT 477664444418.

NO ES REAL-TIME — cadencias fijas: • KPIs checks: cada 15 min (estado puede estar 15 min desactualizado) • Jira incident tickets: cada 15 min • Trading Volume y Data Quality: 1 vez al día a las 06:00 UTC (muestra la data del día anterior en ARDM). Reducir el intervalo tiene costo de warehouse Snowflake — pedir a SnowTime Engineering.

SEMÁFORO (Client Summary): • GREEN/Healthy: todo pasa — nada que hacer. • AMBER/Warning: issue no crítico (data aging, éxito parcial, tablas stale) — monitorear, puede auto-resolverse o requerir investigación si persiste. • RED/Critical: falla detectada (pipeline failed, task suspended, data stale, PK issues) — investigar YA, buscar el ticket en Incident Center. • GREY/Unknown: sin data de pipeline aún — normal en clientes recién onboarded.

"—" en Data Quality = cliente nuevo sin primer pipeline run; se llena tras el primer dbt build exitoso. Los clientes aparecen AUTOMÁTICAMENTE al crearse su schema _SNOWTIME (discovery vía ARDM_PRODUCTION.INFORMATION_SCHEMA.SCHEMATA) — sin registro manual.

## SnowTime FAQ — Incidentes y alertas: creación automática, dedup, flujo post-alerta
_chunk 1092 · 2026-07-02 · fuente: Confluence ARPDT 477664444418_

Fuente: Confluence ARPDT 477664444418.

CREACIÓN AUTOMÁTICA: un stored procedure corre CADA HORA al minuto :20 y escanea 6 tipos de issue: (1) Pipeline Failed — dbt run con FAILED/ERROR; (2) SLA Breached — feed sin archivos nuevos más allá del umbral en Azure storage; (3) Raw Loader Error — errores file-level del Azure Data Loader; (4) Task Suspended — task programada de Snowflake en SUSPENDED; (5) Volume Anomaly — volumen bajo el rango promedio; (6) Data Quality — PK uniqueness o null checks fallando en ARDM.

Al detectar: crea Jira bug ticket AUTOMÁTICO en proyecto RTS con contexto completo (cliente, tipo, razón, run ID — ej. RTS-196264) + notificación Teams al canal "Snowtime - Test Alert Channel" + cuenta en el KPI Incident del dashboard.

DEDUP: UN solo ticket por cliente por tipo de alerta a la vez; recurrencias = COMENTARIO en el ticket existente con occurrence count. EXCEPCIÓN: file arrival SLA breaches SÍ crean ticket nuevo cada día (tracking diario). Guía de alertas: Confluence ARPDT 477668671491 "Jira Teams Alerting Guide".

FLUJO POST-INCIDENTE: L1 actúa primero — RCA y cierre; hay RUNBOOK por tipo de incidente en Confluence ARPDT folder 477757997059. SIN auto-resolución: aunque el issue se arregle, el incidente queda OPEN hasta que un humano cierre el ticket.

## SnowTime FAQ — Runbooks de investigación: pipeline failed, no data feed, loader errors, task suspended
_chunk 1093 · 2026-07-02 · fuente: Confluence ARPDT 477664444418_

Fuente: Confluence ARPDT 477664444418.

PIPELINE FAILED: Client Summary → cliente → tab dbt Executions → expandir el run FAILED → Stage summary (¿qué etapa falló: STAGING/ARDM/REFERENCE/FINAL?) → Model results (qué modelo erró; SQL viewer muestra query compilada) → Test results (¿tests de calidad fallaron?) → usar Snowflake Run ID para rastrear en Snowflake. Si es issue conocido: resolver y cerrar ticket; si no: escalar a SnowTime Engineering con Run ID + dbt Invocation ID.

NO DATA FEED: detail view → Observability → Feed Health → identificar el feed stale (raw_transaction vs raw_location) → tab Azure Function Loader → historial de archivos (¿último archivo cargó? ¿cuándo llegó?). Causas comunes: cliente dejó de enviar (contactar client data operations), issue de Azure Blob Storage (infra), cambio de formato con rechazos silenciosos (revisar loader errors).

LOADER ERRORS: detail view → Azure Function Loader → toggle "Show: Errors Only" → expandir Error Drill-Down: fila, columna, mensaje y preview del registro rechazado. Patrones: schema mismatch, parse errors (JSON/XML/CSV malformado), encoding no-UTF-8. Recurrente/masivo → SnowTime Engineering.

TASK SUSPENDED: la Snowflake Task es el scheduler que dispara el dbt pipeline del cliente. Causas: límite de fallas consecutivas (auto-suspend), suspensión manual por mantenimiento, warehouse no disponible. Resolver: card "Snowflake Task Health" muestra la razón → arreglar causa raíz → Engineering reanuda la task → cerrar ticket cuando esté activa.

## SnowTime FAQ — Data Readiness KPI: lógica de evaluación diaria
_chunk 1094 · 2026-07-02 · fuente: Confluence ARPDT 477664444418_

Fuente: Confluence ARPDT 477664444418 (FAQ 16).

OBJETIVO: evaluar temprano el volumen de la data final en ARDM para detectar anomalías de volumen en la carga reciente.

CÓMO FUNCIONA: cada mañana a las 5AM hora local del cliente corre la evaluación de data readiness: compara #transacciones del "evaluation trading day" contra los promedios baseline. Umbral: debe ser >= 80% del promedio. Si NO cumple → crea RTS Jira Issue con todos los detalles; si cumple → skip.

LÓGICA DEL EVALUATION TRADING DAY: (1) cada mañana en TZ del cliente = fecha X; (2) delay day offset configurable POR CLIENTE (guardado en DB), ej. 1 día; (3) evaluation trading day = X - offset; (4) se calculan las transacciones de ese trading day en la tabla ARDM y se comparan contra baselines.

Nota de contexto del KT 2026-07-02: esto complementa la vista intradía de data readiness del dashboard (progresión horaria vs histórico por day-of-week, con espera extendida para clientes batch que envían al final del día).

## SnowTime — Setup Claude + MCPs Snowflake (workspace C:\git, arranque desde la raíz)
_chunk 1153 · 2026-07-14 · fuente: ingesta-2026-07-14_

Repo SnowTime en C:\git\SnowTime (main). Ingiere POS retail → Snowflake → ARDM star schema. Componentes: .NET Raw Data Loader (dotNet/), dbt (dbt/snowtimeV2/), pyardm (ETL legacy de referencia).

REGLA CRÍTICA: los MCPs de Snowflake solo cargan si Claude Code arranca DESDE C:\git\SnowTime (o C:\git con la config espejo). Arrancar desde otro dir no los carga, y hacer cd dentro de la sesión NO sirve. Lo mismo aplica a Secure: arrancar Claude en la raíz del repo o pierde docs/skills/contexto (Chris Rippingale, misma semana).
MCPs (en .mcp.json): snowflake-eu (cuenta OKB13541-NEUAZ), snowflake-us (OKB13541-JN80103), azure, dataloader-eu/us, azuredevops. Auth: PROGRAMMATIC_ACCESS_TOKEN vía env vars SNOWFLAKE_MCP_USER, SNOWFLAKE_MCP_PAT_EU/US. Role SNOWTIME_ENGINEERING_ROLE, warehouse SNOWTIME_ENGINEERING_XS_WH. Contrato efectivo read-only: query_manager (SELECT/DESCRIBE/SHOW) + object_manager.

Workspace root C:\git tiene CLAUDE.md índice + .mcp.json espejo de SnowTime (path del --service-config-file reescrito a SnowTime/.snowflake-mcp/tools_config.yaml porque resuelve relativo al cwd) + settings con allowlist MCP. Si SnowTime/.mcp.json cambia, re-espejar.
Recomendaciones de Daniel Endersby en Snowflake UI: fijar (pin) dbt projects, Workspaces y Query History; rol default "snowtime engineer"; usar SIEMPRE warehouse XS salvo razón de peso (XL corriendo un SELECT descuidado cuesta una fortuna).
[Fuentes: memorias Daniel Buelvas + call Daniel Endersby, 2026-07-10]

## SnowTime — Incidente FLI (EU cliente 47): dbt shutdown tras 3 fallos y flujo de investigación
_chunk 1154 · 2026-07-14 · fuente: ingesta-2026-07-14_

Patrón del incidente (2026-07-09 noche): el data loader se auto-apaga tras 3 fallos consecutivos de dbt run → alerta a L1 → "DBT has been shut down, 3 failures".

Flujo de investigación demostrado por Daniel Endersby:
1. git pull de main ANTES de investigar (nunca investigar sobre código viejo). Usar un Git UI (él usa Sublime Merge).
2. Snowflake → Transformation → dbt projects → abrir el run fallido; el error está al final del log. Distinguir tests CRÍTICOS (cancelan todo el load) vs opcionales.
3. Prompt a Claude (desde la raíz de SnowTime): "EU FLI client 47 failed dbt run 3 times in a row and the process shut down. Investigate. More info: <link ticket RCS>" — el MCP de Atlassian lee el ticket (pero NO puede descargar imágenes adjuntas).
4. Claude leyó logs vía MCP Snowflake, encontró la causa: record sequence number NULL (transacción Engage sin item asociado, caso nunca visto) → propuso fix en el mapping (filtrar item sequence number not null), se testeó y se aprobó PR.
5. Deploy: al cambiar un cliente, el pipeline lo despliega automático. PERO la task queda suspendida: hay que re-habilitarla a mano — ALTER TASK … RESUME (candidato a automatizar).

Filosofía: investigar automático primero (Claude + MCPs), manual solo si no lo saca. Crear pocos skills buenos, no cientos: pendientes de Daniel — "investigate data load errors" y "support investigation" (con fechas de cutover y shutdown de pyARDM precargadas). Registrar cada incidente en una carpeta incidents/ del cliente (futuro: Jira, concepto de Matt Everett).
[Fuente: call Daniel Endersby 2026-07-10]

## SnowTime — Gotchas de validación: ventana de llegada de datos ≠ trading day; PIM shutdown al comparar
_chunk 1155 · 2026-07-14 · fuente: ingesta-2026-07-14_

Dos trampas al validar cargas o comparar legacy vs SnowTime:

1. VENTANA DE LLEGADA ≠ DÍA DE TRADING. "Cargar los días 10-11" carga lo que el cliente ENVIÓ en esa ventana, no los datos DE esos días. Los clientes mandan con retraso variable (mayoría 1 día detrás; Starbucks manda el día 10: ~6M transacciones del 9, 1M del 8, 100K del 7… y puede venir un update de un mes atrás). Consecuencia: al validar un fix re-corriendo 2 días, una discrepancia pequeña (ej. 0.08%) es esperable — datos de esos trading days llegaron en envíos posteriores que el test no procesó. Umbral práctico de Daniel: ≥99.5% de match está bien; probarlo "perfecto" exigiría recargar todo.

2. FECHAS DE SHUTDOWN DE PYARDM/PIM. Al comparar volúmenes legacy (ARDMPROD) vs SnowTime (ARDM_PRODUCTION), limitar la comparación hasta la fecha en que el loader viejo se apagó — si no, los números dan "34× más filas" y desorientan la investigación (le pasó a Claude con junio completo). Esto debe ir precargado en el futuro skill de investigación.

Referencia de esquemas: ARDM_PRODUCTION = nuevo (SnowTime V2); ARDMPROD = legacy (pyardm). Ambos se mantuvieron en paralelo durante la transición. Clientes XML (ej. H&M, 1 transacción = un árbol XML enorme) son los más lentos de cargar — un rerun de 2 días puede tardar ~13 min en warehouse XS y está bien.
[Fuente: call Daniel Endersby 2026-07-10]

## SnowTime — dbt DAG y selección de modelos (+model), lineage por cliente
_chunk 1156 · 2026-07-14 · fuente: ingesta-2026-07-14_

Herramientas de lineage para entender qué recalcular:
- Sintaxis de selección dbt: "+map_ardm_operator_actions" = ese modelo y TODO lo anterior (upstream); "model+" = ese modelo y todos los que dependen de él (downstream). Al cambiar un modelo intermedio, solo hace falta re-correr su downstream.
- Flujo típico: flat (lee y aplana data cruda del cliente) → modelos map_* → header/item/operator_action → consumidores.
- Visualización: en Snowflake, dbt project del cliente → pestaña DAG — muestra qué tablas se leen y combinan para producir cada output (útil para explicar y para debug).
- Query History de Snowflake permite ver el SQL que dbt ejecutó realmente (pin recomendado).
- Consultas de conteo por metadata (SELECT trading_day, COUNT(1) … GROUP BY 1) son casi gratis en Snowflake — no lee la tabla, responde de estadísticas.
[Fuente: call Daniel Endersby 2026-07-10]
