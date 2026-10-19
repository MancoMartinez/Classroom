Read only. SELECT statements only, through the snowflake-us MCP. Do not modify files or data. Client C021_AAP, last 14 days. Show the query you used for each answer and do not guess table names.

1. For each tradingday: min and max file_arrival_time for strinvdt, for TRE header, detail and tender, and for the tlog zip.
2. For the same days: does the first strinvdt chunk arrive before or after the first POS file? Does any strinvdt chunk arrive in a different fire (hourly :30 UTC) than the POS for that day?
3. For each tradingday since October 2: count inventory_itemposition rows with totalsalesquantity = 0 and totalreturnedquantity = 0. Compare the sum of totalsalesquantity with the sum of salesquantity from ardm_item for record types 1 and 6, excluding voided, training and cancelled lines. List the days where they differ.
4. For each day since October 1: count ardm_item rows with null department or zero taxamount, to check whether the cleanup repaired October 1 to 7.
