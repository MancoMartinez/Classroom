**Escalating to Delivery, Secure 5.** The Refunds to a Partners SVC or Credit Debit Card with no Partner Discount definition returns 0 for fiscal period 24 Aug to 27 Sep. The field it filters on stopped arriving at the 27 Aug SnowTime cutover. Support cannot change the mapping.

## 1. Environment and steps to reproduce

Prod. Tenant starbucks-us, c166_sbx, ARDM_PRODUCTION.C166_SBX.

### Starbucks NA (SBX), reported 30 Sep

1. Snowflake, SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY, user SVC_ARP_PRODUCTION_166_USER, 30 Sep 02:08:49 PT. Trigger search with `T1.TransactionType = 2 AND T3.x_partnerownedtoken = :tender_ext_partnerownedtoken`.
2. Run:

```
SELECT CASE WHEN h.TradingDay < '2026-08-27' THEN 'before' ELSE 'after' END AS window,
       t.x_partnerownedtoken, COUNT(*) AS refunds
FROM ARDM_PRODUCTION.C166_SBX.ARDM_HEADER h
JOIN ARDM_PRODUCTION.C166_SBX.ARDM_TENDER t
  ON t.TransactionID = h.TransactionID AND t.TradingDay = h.TradingDay
WHERE h.TradingDay BETWEEN '2026-07-27' AND '2026-09-27' AND h.TransactionType = 2
GROUP BY 1, 2 ORDER BY 1, 2;
```

Expected: x_partnerownedtoken TRUE on partner refunds in both windows.
Actual: TRUE on 3,927 refunds before 27 Aug, on none after. 204,745 refunds after 27 Aug, all NULL.

## 2. Findings

Detail in my internal note of 1 Oct. Refund volume is normal. Only the token is missing, so the trigger search returns 0 rows with no error.

## 3. Troubleshooting performed

Snowflake query history and the query above. Partner flags on ardm_header checked in the same window, unchanged. Asked Sebastian Rueda on 1 Oct who owns the SnowTime tender mapping for c166_sbx. He did not know. No other conversations.

## 4. Still open

1. Is x_partnerownedtoken mapped for c166_sbx in the SnowTime tender model, and who owns that mapping?
2. Once mapped, can the field be reloaded for refunds from 27 Aug, and the 24 Aug to 27 Sep run regenerated?

Related: https://trebuco.atlassian.net/browse/RCS-29207
