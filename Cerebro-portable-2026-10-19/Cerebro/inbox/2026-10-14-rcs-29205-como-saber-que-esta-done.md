# RCS-29205, como saber que esta listo antes de escribirle a Manish

Aprobar el PR no aplica nada. Hay 4 etapas y cada una se revisa distinto.

1. PR fusionado. En la pagina del PR 58962, arriba, el estado debe decir Completed (no Active).
2. Desplegado. Azure DevOps, Sysrepublic Secure, Pipelines, buscar "Deploy - SnowTime DBT / US - C166_SBX". Debe haber una corrida verde con fecha posterior al merge.
3. Datos reconstruidos (operador). Snowflake, consultas A y B abajo.
4. Work items regenerados. Snowflake consulta C y Executive Workbench.

Solo con las 4 en verde se le escribe a Manish.

-- A. Existe la tabla nueva y tiene datos (seed hecho)
SELECT COUNT(*) AS tokens, MAX(endtransdatetime) AS ultimo
FROM ARDM_PRODUCTION.C166_SBX.REFERENCE_PARTNEROWNEDTENDERTOKEN;
-- Error "does not exist": no esta desplegado. 0 filas: no corrio el seed.

-- B. Refunds con token de partner por semana (rebuild hecho)
SELECT DATE_TRUNC('week', h.TradingDay) AS semana,
       COUNT_IF(t.x_partnerownedtoken = TRUE) AS refunds_token_partner
FROM ARDM_PRODUCTION.C166_SBX.ARDM_HEADER h
JOIN ARDM_PRODUCTION.C166_SBX.ARDM_TENDER t
  ON t.TransactionID = h.TransactionID AND t.TradingDay = h.TradingDay
WHERE h.TradingDay BETWEEN '2026-07-27' AND CURRENT_DATE
  AND h.TransactionType = 2
GROUP BY 1 ORDER BY 1;
-- Listo: las semanas desde el 27 ago ya no estan en 0, cerca de ~900 por semana como antes.

-- C. La busqueda del work item ya trae filas
SELECT start_time, execution_status, rows_produced
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
WHERE user_name = 'SVC_ARP_PRODUCTION_166_USER'
  AND query_text ILIKE '%x_partnerownedtoken%'
  AND start_time >= DATEADD('day', -3, CURRENT_TIMESTAMP)
ORDER BY start_time DESC
LIMIT 10;
-- Executive Workbench: Workview Monitor con la definicion de Refunds Partners SVC, rango 1 jul a hoy.
-- Listo: hay una corrida con items del periodo 24 ago a 27 sep.
