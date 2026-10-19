-- 1. Corridas del trigger search desde hoy. ACCOUNT_USAGE tarda hasta 45 min en reflejarlas.
SELECT DATE_TRUNC('hour', start_time) AS hora,
       execution_status,
       error_code,
       COUNT(*) AS corridas
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
WHERE user_name = 'SVC_ARP_PRODUCTION_166_USER'
  AND query_text ILIKE '%Star_Farming_same_day_high_volume%'
  AND start_time >= '2026-10-05'
GROUP BY 1, 2, 3
ORDER BY 1;

-- 2. Como quedo la condicion en la corrida mas reciente
SELECT start_time, execution_status, rows_produced,
       REGEXP_SUBSTR(query_text, 'x_MemberID[^)]{0,40}', 1, 1, 'i') AS condicion
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
WHERE user_name = 'SVC_ARP_PRODUCTION_166_USER'
  AND query_text ILIKE '%Star_Farming_same_day_high_volume%'
  AND start_time >= '2026-10-05'
ORDER BY start_time DESC
LIMIT 5;
