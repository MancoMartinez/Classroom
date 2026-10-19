# INTERNAL NOTE. NOT FOR CUSTOMER

@Peyman Motlagh, tagging you since you handled the c112ahl load change in https://trebuco.atlassian.net/browse/RCS-27641. Ahold, client 112, AHL.

## 1. Environment and steps to reproduce

**Production.** GP9 `ardm_112`, Snowflake `ARDMPROD.ARDM_112`, `\\dsprod1\retail\data\c112ahl\xml\error`, blob `stprdwus2shrdtlog/112ahl`.

1. Count `ardm_112.ardm_header` by minute of `endtransdatetime` for 2026-08-12 20:20 to 22:30.
2. Copy the six August zips from `xml\error` to a temp folder and decrypt them with `apprissgpg d c112ahl`.
3. List the XML names inside each zip. The first 12 digits are the transaction date and time.
4. Look up sample XML names in `ardm_header.filename`.

Expected: every XML from those zips present in `ardm_header`, and 1,000 to 2,000 transactions per minute on 8/12 evening.
Actual: see findings.

## 2. Findings

1. **The 8/12 gap never reached us.** `ardm_header` is at zero from 20:34 to 20:36 and from 20:55 to 22:19. None of the six error zips holds a transaction stamped 8/12 21:00 to 22:59. GP9 and Snowflake match. Verified 9/24 and 9/25.
2. **Each error zip holds one or two XMLs filled with zero bytes.** That is the `ParseError: not well-formed (invalid token): line 1, column 0` in `ardm_prod_ardm_logs_base_20260814_002734.log` line 229. Verified 9/25.

| Error zip | XMLs | Transactions inside | Zero-filled XML |
| --- | --- | --- | --- |
| 20260813211832251 | 15,684 | 8/11 20h and 21h, 8/12 20h | 2026081220490540041901601.xml |
| 20260815232950113 | 15,874 | 8/14 20h | 2026081420386054070202581.xml |
| 20260816135725133 | 6,523 | 8/11 18h and 19h | 2026081119012587040501481.xml, 2026081119012588003101041.xml |
| 20260816141814815 | 23,757 | 8/14 18h, 8/16 09h | 2026081418160637001400491.xml |
| 20260817143721575 | 40,668 | 8/13 22h and 23h | 2026081323002552053400021.xml |
| 20260817193820049 | 4,132 | 8/16 17h | 2026081617100638007701591.xml |

3. 15 of 18 sample XMLs are in `ardm_header`, loaded later on 8/15, 8/17, 8/26 and 8/27. Most of the error zip content came back through resends. Verified 9/25.
4. **Still missing:** `2026081609270072001200101.xml` and `2026081609346051040200201.xml` from zip 20260816141814815, both 8/16 09h. Also `2026081220490540041901601.xml`, the zero-filled one. Verified 9/25.

## 3. Troubleshooting performed, and the limits of support access

Claude proposed the checks and wrote the queries and scripts. I ran all of them myself on DEVWUS2DSM01 after running `env_setup.ps1` from appriss_pipeline: `apprissgpg i c112ahl`, `apprissgpg d c112ahl` on copies of the six zips, a Python listing of XML names, and a GP9 lookup of 18 sample names. The copies were deleted afterwards. Nothing in `xml\error` was moved or changed.

This is what I think is happening: `xml_ingest.py` walks the XMLs in name order and stops at the zero-filled one, so everything that sorts after it in that zip is lost. In zip 20260816141814815 the sample before the bad XML loaded and the two samples after it did not. Could someone else evaluate this and give me your thoughts?

The GP9 daily pipeline for c112ahl shows Disabled and Migrated To Snowflake since 9/3.

Outside the ticket: Teams thread in Retail Ops, Data Issues, 8/27. Guidance from Sebastian Rueda on `apprissgpg`. No calls.

## 4. Ruled out

| Hypothesis | Why |
| --- | --- |
| The 8/12 20:55 to 22:19 window is in an error zip | No error zip holds 8/12 21h or 22h |
| Fallback GPG setup failed caused the drops | It appears every night, including clean loads |
| Duplicate rows on 8/12 | 1,922,680 rows and 1,922,680 distinct filenames |

## 5. Still open

1. Could zip 20260816141814815 be reprocessed without the zero-filled XML, to recover 8/16 09h? Its first half is already loaded, so a skip on existing filenames would avoid duplicates.
2. Is the whole-zip drop on one bad XML, with a conditional success result, expected behavior? The error folder holds 86 zips since 7/6/2025.
3. With Ahold on Snowflake since 9/3, which path would that reprocess take?

I am asking ADUSA to resend 8/12 20:29 to 22:19. Ticket is High and open since 8/11.
