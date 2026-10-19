---
name: reference_query_store_regresion_plan
description: "Detectar una regresión de plan de ejecución en SQL Server con Query Store: el estimador de cardinalidad 140 vs 160"
metadata: 
  node_type: memory
  type: reference
  originSessionId: a8293f75-ab64-479b-971f-f586abf0f63b
  modified: 2026-08-13T18:19:52.096Z
---

Firma del caso: **la misma consulta, el mismo query_id, pasa de subsegundo a decenas de segundos de un día para otro, sin despliegue de código y solo en algunos tenants.** Eso no es carga ni red, es un plan nuevo.

Hallazgo original (Tailored Brands, 10 ago 2026): las consultas de LPUser promediaban 0,5 a 0,8 s hasta el 5 de agosto y saltaron a 57 s de promedio con máximo de 120 s desde el 6 de agosto 17:35 UTC. Mismos query IDs, planes distintos. **Los planes buenos se compilaron con estimador de cardinalidad 140 y los malos con 160.** Las 137 bases de producción están en nivel de compatibilidad 160, y solo 3 de las 39 que corren la consulta se degradaron: el nivel es la condición, no la causa; el disparador es la recompilación.

Nivel de compatibilidad:

```sql
SELECT name, compatibility_level FROM sys.databases WHERE name = DB_NAME();
```

Planes y estimador de los últimos días. `CardinalityEstimationModelVersion` es un atributo XML de `StmtSimple` dentro de `query_plan`:

```sql
WITH planes AS (
  SELECT q.query_id, p.plan_id, p.is_forced_plan,
         CAST(p.query_plan AS xml).value(
           '(//*:StmtSimple/@CardinalityEstimationModelVersion)[1]','int') AS ce_version,
         rs.count_executions, rs.avg_duration, rs.max_duration, i.start_time
  FROM   sys.query_store_query q
  JOIN   sys.query_store_query_text t ON t.query_text_id = q.query_text_id
  JOIN   sys.query_store_plan p ON p.query_id = q.query_id
  JOIN   sys.query_store_runtime_stats rs ON rs.plan_id = p.plan_id
  JOIN   sys.query_store_runtime_stats_interval i
         ON i.runtime_stats_interval_id = rs.runtime_stats_interval_id
  WHERE  t.query_sql_text LIKE '%LPUser%'
    AND  i.start_time > DATEADD(day, -3, SYSUTCDATETIME())
)
SELECT query_id, plan_id, is_forced_plan, ce_version,
       MIN(start_time) AS desde, SUM(count_executions) AS ejecuciones,
       AVG(avg_duration)/1000.0 AS avg_ms, MAX(max_duration)/1000.0 AS max_ms
FROM   planes
GROUP  BY query_id, plan_id, is_forced_plan, ce_version
ORDER  BY avg_ms DESC;
```

**Dos advertencias.** Query Store puede estar apagado en esa base, y entonces la comprobación no se puede correr y hay que pedirla. Y **forzar un plan es un cambio de producción, no un diagnóstico**: se propone, no se ejecuta desde Support.

**El techo de 120 s no es casualidad**: es el `CommandTimeout` de la aplicación. Cloudflare corta a los 100 s, así que el usuario ve un 524 antes de que la aplicación alcance a rendirse.

Ver [[project_rcs_28256_tailored_brands]], [[reference_medir_lentitud_web_devtools]], [[reference_acceso_sql_tenants]].
