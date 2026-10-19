# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Environment and steps to reproduce

**Environment: Production.** Client 356, GPC. ARDM schema `ardm_356` on GP11, replicated to Snowflake `ARDMPROD.ARDM_356`.

### GPC (356), reported 24 Sep 2026 by SE Kristen Dyer

1. Log in to the Portal in Production and go to Secure Store, Explorer.
2. Open the search All Refunds by Cashier and run it for store CHA266.
3. Open the receipt for Transaction ID 2609179617330521193, trading day 2026-09-17, ticket 533653.

Expected: a Visa tender line for 450.47 CR. GPC's own invoice shows Visa, 450.47 CR.
Actual: the receipt has no tender line. Tender Type, Tender Card Number and Tender Amount are blank on every visible row of the 99 results, and the Tender Amount footer total is 0.00. Screenshots attached to the ticket by Kristen Dyer on 24 Sep.

## 2. Findings

All queries below are SELECT only, run by me on 24 Sep 2026.

| Check | Result |
|---|---|
| TXN 2609179617330521193 in GP11 `ardm_356` | header 1, item 2, **tender 0**. Header matches the invoice: total -450.47, tax -28.48 |
| Same TXN in Snowflake `ARDMPROD.ARDM_356` | header 1, item 2, tender 0. Replication is not the cause |
| Daily chain ratio, transactions with a tender row over headers | 0.90 to 0.99 from 2026-04-15 to 2026-05-03. **0.577 on 2026-05-04** |
| Same ratio in the windows checked after the break | 2026-05-04 to 05-10, 07-01 to 08-03 and 09-12 to 09-20: between 0.35 and 0.77, with one outlier at 0.971 on 2026-05-09 |
| Stores with zero tender rows, week of 2026-09-14 | 834 of 5,686 stores, 356,710 headers. Another 819 stores below 30% |
| Same check on GP11 clients 352 and 354 on 2026-05-01, 05-04 and 09-15 | 352 at 0.82, 0.80 and 0.77. 354 at 0.997, 0.997 and 0.998. No break on 05-04 |

`ardm_header.totaltendercount` is NULL on the example transaction and on every September header of its store except one, so the header does not tell us whether the POS sent a tender.

## 3. Troubleshooting performed, and the limits of support access

Claude flagged a tender load gap as the likely root cause, after a first Talos triage pointed to a display issue with a second card brand field. I checked the example transaction in GP11 and Snowflake, the daily tender to header ratio for the whole chain in the windows above, the per store coverage for one week, and the same ratio on clients 352 and 354. The display theory does not hold. There is no tender row to display. This is what I think is happening: since 2026-05-04 roughly 40% of GPC transactions load into ARDM without tender rows, and the gap now covers about 1,650 stores. Could someone else evaluate this and give me your thoughts?

No conversations outside this ticket so far.

Support cannot see the raw 356 input files, the pyardm load logs or the tender mapping for this client. That is where the cause sits, either the feed from GPC or the load step.

## 4. Still open

1. Did anything change on 2026-05-04 in the 356 feed, the file layout or the pyardm tender mapping?
2. Do the raw files for store CHA266 on 2026-09-17 carry the tender for ticket 533653?
3. If the tender is in the raw files, can 2026-05-04 onward be reprocessed for 356?
4. Is 2026-05-09 at 0.971 a partial reload, and does it point to the step that fails?

Related: https://trebuco.atlassian.net/browse/RCS-28632 covers the August backload for the same client 356. Priority High, opened 24 Sep 2026.
