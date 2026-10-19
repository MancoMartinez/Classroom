-- RCS-29053 Wegmans, GP6 prod, schema ardm_171. Solo SELECT.
-- overshort_dailyreconciliation no tiene cashierno: el over/short llega por tienda, registradora, dia y x_tendertype.

-- Q1. Total real de la tienda 73 en 90 dias, desde el feed. Comparalo con -247.07 del reporte.
SELECT x_tendertype,
       COUNT(DISTINCT tradingday) AS dias_con_registro,
       SUM(overshortamount) AS total_os
FROM ardm_171.overshort_dailyreconciliation
WHERE storeno = 73
  AND tradingday >= CURRENT_DATE - 91
GROUP BY ROLLUP (x_tendertype)
ORDER BY x_tendertype;

-- Q2. Simula el cruce del data area: cada cajero de la registradora hereda el monto completo.
SELECT CASE WHEN r.cashierno = '0' THEN 'cashier0' ELSE 'cajeros' END AS grupo,
       COUNT(DISTINCT r.cashierno) AS cajeros_distintos,
       COUNT(DISTINCT r.tradingday) AS dias,
       SUM(d.overshortamount) AS total_os_heredado
FROM ardm_171.overshort_dailyreconciliation d
JOIN ardm_171.overshort_registeractivity r
  ON r.storeno = d.storeno AND r.posno = d.posno AND r.tradingday = d.tradingday
WHERE d.storeno = 73
  AND d.tradingday >= CURRENT_DATE - 91
GROUP BY 1;

-- Q3. Un caso concreto: registradoras con over/short en un dia y los cajeros que lo heredan.
SELECT d.tradingday, d.posno, d.x_tendertype, d.overshortamount, r.cashierno
FROM ardm_171.overshort_dailyreconciliation d
JOIN ardm_171.overshort_registeractivity r
  ON r.storeno = d.storeno AND r.posno = d.posno AND r.tradingday = d.tradingday
WHERE d.storeno = 73
  AND d.overshortamount <> 0
  AND d.tradingday >= CURRENT_DATE - 91
ORDER BY d.tradingday DESC, d.posno, r.cashierno
LIMIT 40;
