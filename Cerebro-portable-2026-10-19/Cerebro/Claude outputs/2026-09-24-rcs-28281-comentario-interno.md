# INTERNAL NOTE. NOT FOR CUSTOMER

DataOps team, requesting a review of the Ahold pipeline error folder and the 8/12 gap. Client 112, AHL.

## 1. Environment and steps to reproduce

**Production.** GP9 `ardm_112`, Snowflake `ARDMPROD.ARDM_112`, blob `stprdwus2shrdtlog/112ahl`, share `\\dsprod1\retail`.

1. Count `ardm_112.ardm_header` by minute of `endtransdatetime`, 2026-08-12 20:20 to 22:30.
2. Run the same count on `ARDMPROD.ARDM_112.ARDM_HEADER`.
3. Compare with `8.12.2026 Transactions Per Minute Per Hour.xlsx`, attached by Jacquelyn on 9/24.
4. List `\\dsprod1\retail\data\c112ahl\xml\error`.

Expected: 1,000 to 2,000 transactions per minute, in line with 8/19, 8/20, 8/22 and 8/25.
Actual: zero from 20:34 to 20:36 and from 20:55 to 22:19, except one transaction at 21:44.

## 2. Findings

1. **GP9, Snowflake and the customer file match minute by minute.** Verified 9/24.
2. No duplicates. 8/12 has 1,922,680 rows and 1,922,680 distinct `filename` values. Verified 9/24.
3. Four loads carried the 8/12 evening, by `inserteddatetime`. None filled the gap. Verified 9/24.

| Load | Transactions covered | Rows |
| --- | --- | --- |
| 2026-08-14 00:15 | 8/12 19:00 to 23:59 | 196,886 |
| 2026-08-15 23:37 | 8/12 20:46 to 20:49 | 1,191 |
| 2026-08-26 00:28 | 8/12 19:00 to 23:59 | 99,618 |
| 2026-08-30 00:21 | 8/12 20:38 to 21:44 | 9 |

4. Blob folder `Archive/Prod/2026/08/13` shows `Ahold_TLOG_20260812*` zips arriving about every 10 minutes from 00:17 UTC, suffixes 2015 through 2315. Verified 9/24.
5. **Six August zips never loaded and remain in `xml\error`.** Verified 9/24.

| Zip | Size |
| --- | --- |
| 20260813211832251-Ahold_TLOG_2026081308701715.zip.pgp | 44.4 MB |
| 20260815232950113-Ahold_TLOG_2026081514001926.zip.pgp | 46.1 MB |
| 20260816135725133-Ahold_TLOG_2026081609000955.zip.pgp | 19.0 MB |
| 20260816141814815-Ahold_TLOG_2026081609301015.zip.pgp | 71.8 MB |
| 20260817143721575-Ahold_TLOG_2026081708501035.zip.pgp | 21.9 MB |
| 20260817193820049-Ahold_TLOG_2026081710801536.zip.pgp | 13.2 MB |

6. `ardm_prod_ardm_logs_base_20260814_002734.log`, lines 229 to 246: `ParseError: not well-formed (invalid token): line 1, column 0` at `xml_ingest.py` lines 70 and 72 for the 8/13 zip. Line 294: `Number of errored files has exceeded allowed threshold of 0%. Number of errored files: 1. Files loaded correctly: 127`. The run ended as conditional success. Decryption worked. One malformed XML dropped the whole zip. Verified 9/24.
7. The error folder holds 86 zips dated 7/6/2025 through 8/17/2026. I do not know whether any were reprocessed through another path.

## 3. Troubleshooting performed, and the limits of support access

Claude proposed the checks and wrote the queries and PowerShell. I ran them myself: GP9 and Snowflake queries, the blob listing in Storage Explorer, the c112ahl repo on branch Production, `Select-String` over `\\dsprod1\retail\logs\c112ahl\ardm`, and the error folder listing. This is what I think is happening: the six August zips explain part of the low days on 8/15, 8/16 and 8/17. The 8/13 zip weighs 44 MB, about one normal batch, since 8/26 averaged 6.63 GB over 159 files. That is roughly 15,000 transactions, well short of the 94,000 missing on 8/12. Could someone else evaluate this and give me your thoughts?

My account has no PGP secret key. `gpg --list-secret-keys` returns nothing, so I cannot list the XMLs inside the zips.

The c112ahl GP9 daily pipeline shows Disabled and Migrated To Snowflake since 9/3.

Outside the ticket: Ayesha's Teams thread in Retail Ops, Data Issues, 8/27, and the ADUSA email thread https://trebuco.atlassian.net/browse/RTS-205639. No calls.

## 4. Ruled out

| Hypothesis | Why |
| --- | --- |
| Fallback GPG setup failed caused the gap | It appears in all three nightly runs, 8/13 to 8/15, including runs that loaded in full |
| Duplicate rows inflate or hide the 8/12 count | Rows equal distinct filenames |

## 5. Still open

1. Could DataOps list the XML names inside the six August error zips? The first 12 digits give transaction date and time, which tells us which trading days and windows each zip holds.
2. Does any of them hold 8/12 20:55 to 22:19? If none does, is asking ADUSA to resend that window the right next step?
3. Did part of each zip load before the malformed XML stopped it? That decides whether a reprocess would duplicate rows.
4. With Ahold on Snowflake since 9/3, which path would a reprocess of these August zips take?

Ticket is High and open since 8/11.
