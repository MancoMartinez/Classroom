**New data after ENG-8659 closed: the 9/25 regeneration shows 2 of the 17 work items.** This is why the customer cannot find the replacement for 248159. https://trebuco.atlassian.net/browse/ENG-8659

## 1. Environment and steps to reproduce

Prod, USPROD, client 85 C085_THD, platform DB. SELECT only.

1. Query workview.Workview for the 17 original IDs listed in my note of 2026-09-02.
2. Query workview.Workview for PeriodFromDateTime and PeriodToDateTime = 2026-08-27, CreatedDateTime from 2026-09-01.
3. Query workview.Workview for MD03 definitions at stores 7135 and 7161, newest first.

Expected: 17 replacements with period 2026-08-27.
Actual: 0 originals, 2 replacements.

## 2. Findings, all verified 2026-09-28

| Check | Result |
|---|---|
| Original 17 IDs | 0 rows |
| Period 2026-08-27, created since 9/1 | **252329** MKD2 store 3615, 3 events. **252328** COM1 store 865 |
| Newest MD03 at 7135 | 186824, created 2025-10-11 |
| Newest MD03 at 7161 | 217484, created 2026-03-04 |
| Generation runs 9/25 | 9 runs, all EventType 0. Runs 8C9DA172 and F163CC7D at 16:55 hold the two items above |

Replacements for 248159 and 248160 do not exist. Original COM1 248162 was store 635, so 252328 may not be its replacement.

## 3. Troubleshooting performed

Claude flagged the gap from Ericka's comment. I ran each query myself and confirmed every row. Could someone evaluate the result? Outside the ticket: Teams message to Mohammed Mutahhar on 2026-09-28 with the same data.

## 4. Still open

1. Did the reruns for the other 15 definitions execute, and did they return no rows or duplicates?
2. Is the WISC New Run by definition and period in Control Panel the path support should use for the remaining 15, or does this stay with Engineering?
