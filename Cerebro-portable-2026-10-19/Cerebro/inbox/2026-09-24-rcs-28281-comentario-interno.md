# INTERNAL NOTE. NOT FOR CUSTOMER

@Viraj Kansara @Anil P, tagging you as the data and feeds owners for Ahold, client 112, AHL.

## 1. Environment and steps to reproduce

**Production.** Ahold Secure 5.4, GP9 schema `ardm_112`, and Snowflake `ARDMPROD.ARDM_112`.

1. Run a minute count on `ardm_112.ardm_header` for `endtransdatetime` between 2026-08-12 20:20 and 22:30.
2. Run the same count on `ARDMPROD.ARDM_112.ARDM_HEADER`.
3. Compare with `8.12.2026 Transactions Per Minute Per Hour.xlsx`, attached by Jacquelyn on 9/24.

Expected: about 1,000 to 2,000 transactions per minute, in line with 8/19, 8/20, 8/22 and 8/25.
Actual: zero from 20:34 to 20:36 and from 20:55 to 22:19, except one transaction at 21:44. Under 10 per minute from 20:30 to 20:33 and 20:50 to 20:54.

## 2. Findings

1. **GP9, Snowflake and the customer file match minute by minute.** Verified 9/24.
2. No duplicates. Trading day 8/12 has 1,922,680 rows and 1,922,680 distinct `filename` values in Snowflake. Verified 9/24.
3. Four loads carried the 8/12 evening. None filled the gap. Verified 9/24 by `inserteddatetime`:

| Load | Transactions covered | Rows |
| --- | --- | --- |
| 2026-08-14 00:15 | 8/12 19:00 to 23:59 | 196,886 |
| 2026-08-15 23:37 | 8/12 20:46 to 20:49 | 1,191 |
| 2026-08-26 00:28 | 8/12 19:00 to 23:59 | 99,618 |
| 2026-08-30 00:21 | 8/12 20:38 to 21:44 | 9 |

4. **Files did arrive during the gap hours.** Blob `stprdwus2shrdtlog/112ahl/Archive/Prod/2026/08/13` holds 164 zips. `Ahold_TLOG_20260812*` zips landed about every 10 minutes from 00:17 UTC, with name suffixes 2015 through 2315. Verified 9/24.
5. Each XML inside a zip is one transaction, and its name starts with the transaction timestamp. `2026081220256579042801481.xml` is 8/12 20:25, store 6579. Source: `ARDM_0_0_Header.sql` line 98 and `xml_ingest.py` line 73, branch Production.
6. Smaller dips on 8/19 16:26 to 16:28 and 8/20 12:27 to 12:29, about 6,600 and 5,200 transactions. 8/22 and 8/25 are clean.

## 3. Troubleshooting performed, and the limits of support access

Claude proposed the load, blob and repo checks and wrote the queries. I ran them myself in GP9 and Snowflake, and read the blob listing in Storage Explorer and the c112ahl repo. This is what I think is happening: the zips that arrived during 20:30 to 22:20 did not carry the transactions for that window, or those XMLs errored during ingest. Could someone else evaluate this and give me your thoughts?

Support cannot decrypt the `.zip.pgp` files. I tried the pyARDM log share `\\dsprod1\retail\logs\c112ahl\ardm` from the Bastion VM QA-LPMS-RDP-001 and got `0x80004005`, so the logs and the `xml\error` folder remain unchecked.

Pipeline `Migrated To Snowflake - c112ahl ARDM Daily Production GP9` is Disabled since 9/3. Its 8/27 scheduled run failed and was rerun manually twice.

Outside the ticket: Ayesha's Teams thread in Retail Ops, Data Issues, 8/27, and the ADUSA email thread https://trebuco.atlassian.net/browse/RTS-205639. No calls.

## 4. Still open

1. Does any `Ahold_TLOG_20260812*` zip contain XMLs whose names start with `202608122055` through `202608122219`? That answers whether DXC sent the window.
2. Do the pyARDM logs for the 8/14 00:15, 8/15 23:37 and 8/26 00:28 loads, or the `xml\error` folder, show errored files for 8/12?
3. If ADUSA resends 8/12 20:29 to 22:19 now, does it load into Snowflake through the new pipeline, and does it skip transactions already loaded?

Ticket is High and open since 8/11.
