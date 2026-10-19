**Work items 248159 and 248160 regenerated and verified on 2026-09-29.** Follows my note of 2026-09-28 and the rerun approach Mohammed Mutahhar proposed on Teams. https://trebuco.atlassian.net/browse/ENG-8659

## Steps, Prod USPROD, client 85

1. Consecutive Markdowns subsearch, Transaction Date changed from Within the last 1 days to Between 08/27/2026 and 08/27/2026.
2. WISC Rerun on 92b446fe-85d1-4463-ac8f-03ee9acd1164.
3. Condition reverted to Within the last 1 days.

## Result, verified

| Run | Status | Results | Generated |
|---|---|---|---|
| 32afd25e-39f2-4de2-aede-3fd2edb1cf14 | Success | 2 | 2 |

| New | Replaces | Store | Events | Potential value |
|---|---|---|---|---|
| **253175** | 248159 | 7135 | 3 | 148.08 |
| **253176** | 248160 | 7161 | 3 | 129.87 |

Events on 253175 lists transactions 8989, 8990 and 8991. Both items are unassigned.

## Troubleshooting performed

Claude traced the zero result to the subsearch date window. I ran each step and query myself and confirmed the results above. Could someone confirm this is the expected path for past periods?

## Still open

1. Do the other 13 work items from the original 17 need the same procedure?
2. Are the six searches Simon listed as blocked on 8/31 resolved?
