-- Correr DESPUES de que Anushka confirme seed, rebuild de tender y recarga de paid in / paid out.

-- 1. Refunds con x_partnerownedtoken TRUE por semana. Antes del cutover habia ~3,900 al mes.
--    Despues del rebuild, las semanas desde el 27 ago deben dejar de estar en 0.
SELECT DATE_TRUNC('week', h.TradingDay) AS semana,
       COUNT_IF(t.x_partnerownedtoken = TRUE) AS refunds_token_partner,
       COUNT(*) AS refunds_total
FROM ARDM_PRODUCTION.C166_SBX.ARDM_HEADER h
JOIN ARDM_PRODUCTION.C166_SBX.ARDM_TENDER t
  ON t.TransactionID = h.TransactionID AND t.TradingDay = h.TradingDay
WHERE h.TradingDay BETWEEN '2026-07-27' AND CURRENT_DATE
  AND h.TransactionType = 2
GROUP BY 1 ORDER BY 1;

-- 2. Paid in / paid out con razon, por semana. Antes ~10,000 por semana.
SELECT DATE_TRUNC('week', TradingDay) AS semana,
       COUNT(X_PAIDINPAIDOUTREASONCODE) AS con_razon
FROM ARDM_PRODUCTION.C166_SBX.ARDM_HEADER
WHERE TradingDay BETWEEN '2026-07-27' AND CURRENT_DATE
GROUP BY 1 ORDER BY 1;

-- 3. Trigger search del work item despues de la regeneracion: debe traer filas.
SELECT start_time, execution_status, rows_produced
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
WHERE user_name = 'SVC_ARP_PRODUCTION_166_USER'
  AND query_text ILIKE '%x_partnerownedtoken%'
  AND start_time >= DATEADD('day', -2, CURRENT_TIMESTAMP)
ORDER BY start_time DESC
LIMIT 10;

-- 4. Executive Workbench: Workview Monitor con esta definicion, rango 1 jul a hoy.
--    Debe aparecer una corrida con items del periodo 24 ago a 27 sep.
