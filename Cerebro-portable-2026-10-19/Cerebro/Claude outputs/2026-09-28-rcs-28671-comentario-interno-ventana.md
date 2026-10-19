**Why 248159 and 248160 were not regenerated: the MD03 sub-search window follows the run date, not the period.**

## Findings, verified 2026-09-28

| Check | Result |
|---|---|
| WISC run 92b446fe-85d1-4463-ac8f-03ee9acd1164, md03-cit-d, period 8/27, run 9/24 | Success, 0 results, 0 generated |
| Show Query, outer search | TradingDay = 2026-08-27 |
| Show Query, sub-search T4AsCte | TradingDay BETWEEN 2026-09-23 AND 2026-09-24 |
| Same SQL in Snowflake ARDM_PRODUCTION.C085_THD, sub-search set to 2026-08-27 | 2 rows: **7135 DXM6269, 3 transactions** and **7161 GXH3486, 3 transactions** |

The data for both work items is there. A rerun of a past period returns 0 because the sub-search window is anchored to the execution date. A WISC New Run for 8/27 would return 0 again.

## Troubleshooting performed

Claude flagged the date mismatch in the Show Query output. I ran the modified SQL myself, read only, and confirmed both rows.

## Still open

1. Is there a way to rerun md03-cit-d for 8/27 with the sub-search window anchored to the period?
2. Could the same rolling window explain the other definitions from the 17 that did not come back?
