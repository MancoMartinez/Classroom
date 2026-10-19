Pull the latest main first (git pull). Read only: do not modify files, no DML or DDL, SELECT statements only through the snowflake-us MCP.

Context: we have just migrated client C021_AAP from pyardm to SnowTime, around October 2, 2026. Check ARDM_PRODUCTION (ardmprod) and the raw data layer. Compare the SnowTime code with the existing pyardm code to look for regressions.

Known so far, cause unproven: INVENTORY_ITEMPOSITION totalsalesquantity and totalreturnedquantity are 0 on almost every row for October 2 to 12, while ARDM_ITEM holds 0.5M to 1M sales units per day. Only October 5 and 6 have partial values. Commit 4a3097a5c is from October 5. Arrivals in UTC: strinvdt all day from 01:17, POS at 07:20, tlog at 22:10. map_inventory_itemposition.sql reads ardm_item only for transactions in the current run.

Tasks:
1. In pyardm, how were the inventory sales and return totals calculated, and when? Does it wait for POS or recalculate when POS lands late? Show the file and the logic.
2. In SnowTime, what behaves differently? List every change that can produce zero totals.
3. Baseline: INVENTORY_ITEMPOSITION for tradingday 2026-09-15 to 2026-10-01, rows with zero sales and returns, and the sum of totalsalesquantity against the ardm_item sales sum (types 1 and 6).
4. Why do October 5 and 6 differ? Check task history, REBUILD_RANGE runs and commit 4a3097a5c.
5. Same regression check for department and taxamount on Verify rows in ardm_item against pyardm behavior.

Show the queries, mark anything unproven, and give any proposed fix as text only.
