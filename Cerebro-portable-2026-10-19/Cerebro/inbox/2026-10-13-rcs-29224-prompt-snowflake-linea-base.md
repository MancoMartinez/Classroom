Read only. SELECT statements only, through the snowflake-us MCP. Do not modify files or data. Client C021_AAP. Show the query for each answer and say what you could not prove.

1. Baseline for INVENTORY_ITEMPOSITION: for tradingday 2026-09-15 to 2026-10-01, rows, rows with zero sales and returns, and sum of totalsalesquantity against the ardm_item sales sum (types 1 and 6). Say whether any column or table shows which engine loaded each day (pyardm or SnowTime).
2. Why do 10-05 and 10-06 have non-zero totals? Check task run history and any REBUILD_RANGE run between 10-05 and 10-07, and what commit 4a3097a5c (2026-10-05) changed.
3. For strinvdt files arriving 10-07 to 10-12, show arrival date against the tradingday each file carries.
4. Use the real task run history, not the :30 approximation, to count strinvdt files processed in the same run as the POS of their tradingday.
5. Zero tax baseline: Verify and XBR rows for 09-20 to 09-30, same counts as before. Does XBR taxamount arrive populated from the source? PR 58891 copies taxamount from the XBR twin.
