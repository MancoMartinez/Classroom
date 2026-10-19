-- RCS-28671. Query del run 92b446fe con la ventana del CTE cambiada a 2026-08-27. Solo lectura, Snowflake, esquema THD.
set UniqueCountofApprissSecureID = 2;
set calendarStartDate = '2026-08-27';
set calendarEndDate = '2026-08-27';
set RefSearch2_SubSearchParam_1_totalpretenderreductionamount = 20;
set RefSearch2_SubSearchParam_1_suspendedtransactionflg = false;
set RefSearch2_SubSearchParam_1_trainingmodeflg = false;
set RefSearch2_SubSearchParam_1_voidticketflg = false;
set RefSearch2_SubSearchParam_1_cashierno = 'PTM01,SPOS01';
set RefSearch2_SubSearchParam_1_cashierno1 = 'SELF';
set RefSearch2_SubSearchParam_1_totaltendercount = 1;
set AutoCreated_ArrayParam1 = '["0006"]';
set AutoCreated_ArrayParam2 = '["PTM01","SPOS01"]';
set AutoCreated_ArrayParam3 = '["0230","0249"]';

WITH T4AsCte AS (
  SELECT
  T5.TransactionID AS transactionid
  FROM ardm_Header AS T5
  LEFT JOIN reference_location AS T6
    ON (T5.StoreNo = T6.LocationID)
  LEFT JOIN ardm_Tender AS T7
    ON (T5.TransactionID = T7.TransactionID AND T5.TradingDay = T7.TradingDay)
  LEFT JOIN ardm_OperatorAction AS T8
    ON (T5.TransactionID = T8.TransactionID AND T5.TradingDay = T8.TradingDay)
  WHERE
  (
  (T5.TradingDay BETWEEN CAST('2025-08-25T00:00:00' AS DATE) AND CAST('2026-09-24T23:59:59' AS DATE))
  )
  AND
  (LOWER(T6.LocationHierarchy1) IN (SELECT LOWER(VALUE) FROM TABLE(FLATTEN(PARSE_JSON($AutoCreated_ArrayParam1)))) AND T5.TradingDay BETWEEN CAST('2026-08-27T00:00:00' AS DATE) AND CAST('2026-08-27T23:59:59' AS DATE) AND T5.TransactionType = 1 AND ROUND(CAST(T5.TotalPreTenderReductionAmount AS NUMERIC(38,2)), 2) > ROUND(CAST($RefSearch2_SubSearchParam_1_totalpretenderreductionamount AS NUMERIC(38,2)), 2) AND T5.SuspendedTransactionFlg = $RefSearch2_SubSearchParam_1_suspendedtransactionflg AND T5.TrainingModeFlg = $RefSearch2_SubSearchParam_1_trainingmodeflg AND T5.VoidTicketFlg = $RefSearch2_SubSearchParam_1_voidticketflg AND T7.StdTenderTypeGrp IN (2, 4, 8) AND T5.TillType <> 7 AND NOT ( LOWER(T5.CashierNo) IN (SELECT LOWER(VALUE) FROM TABLE(FLATTEN(PARSE_JSON($AutoCreated_ArrayParam2)))) ) AND T5.CashierNo NOT ILIKE $RefSearch2_SubSearchParam_1_cashierno1 || '%'AND
  ((T8.ManagerID IS NULL OR T8.ManagerID = '')OR T8.ManagerID = T5.CashierNo)
  AND T5.TotalTenderCount = $RefSearch2_SubSearchParam_1_totaltendercount)
)

SELECT
T2.LocationHierarchy2Description AS "location_hierarchy2description",
T2.LocationHierarchy3Description AS "location_hierarchy3description",
T1.StoreNo AS "storeno",
T1.CashierNo AS "cashierno",
T3.AccountNumber AS "tender_accountnumber",
COUNT(DISTINCT T1.TransactionID) AS "UniqueCountofApprissSecureID",
MAX(T1.TradingDay) AS "MaxofTransactionDate"
FROM ardm_Header AS T1
LEFT JOIN reference_location AS T2
  ON (T1.StoreNo = T2.LocationID)
LEFT JOIN ardm_Tender AS T3
  ON (T1.TransactionID = T3.TransactionID AND T1.TradingDay = T3.TradingDay)
LEFT JOIN T4AsCte AS T4
  ON (T1.TransactionID = T4.transactionid)
WHERE
(T1.TradingDay BETWEEN $calendarEndDate AND $calendarStartDate AND
(T1.TradingDay BETWEEN CAST('2025-08-25T00:00:00' AS DATE) AND CAST('2026-09-24T23:59:59' AS DATE))
)
AND
(T4.transactionid IS NOT NULL AND
(T4.transactionid IS NOT NULL OR T4.transactionid IS NOT NULL)
AND NOT ( LOWER(T2.LocationHierarchy3) IN (SELECT LOWER(VALUE) FROM TABLE(FLATTEN(PARSE_JSON($AutoCreated_ArrayParam3)))) ))
GROUP BY T2.LocationHierarchy2Description, T2.LocationHierarchy3Description, T1.StoreNo, T1.CashierNo, T3.AccountNumber
HAVING
(COUNT(DISTINCT T1.TransactionID) > $UniqueCountofApprissSecureID)
ORDER BY "UniqueCountofApprissSecureID" DESC
LIMIT 1000;
