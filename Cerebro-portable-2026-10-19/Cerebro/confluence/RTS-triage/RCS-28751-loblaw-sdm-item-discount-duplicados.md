---
ticket: RCS-28751
cliente: Loblaw / SDM / c212_lcl (legacy ARDM_212)
analista: Diego Buelvas
estado_ficha: Work in Progress
sintoma: Total Item Discount Amount inflado, 2709.95 cuando el descuento real fue 416.93
causa: el export cerebro_ext_appriss_trans_item_dsct llega en 5 partes con snapshots distintos del mismo item y ARDM_30_ItemDiscount.sql inserta 1:1 sin dedup
fix: escalar al dueno del pipeline legacy en el proyecto DO, no hay fix desde SnowTime
relacionados: DO-9923, DO-2828
confluence_id: 478182211808
modificado: 2026-09-07
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478182211808
---

# RCS-28751 — Loblaw (SDM): Item Discount Amount Not Correct

Prepared: 07 September 2026 | Analyst: Diego Buelvas | Status: Work in Progress

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28751 |
| Customer | Loblaw / SDM |
| Issue Type | Incident |
| Priority | Medium |
| Status | Work in Progress |
| Opened | 03 September 2026 |
| Reporter | James Plasse |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28751 |

## 2. Problem Statement

Total Item Discount Amount (Header) does not show the correct amount for discounts within a transaction. It displays $2,709.95 when only $416.93 in discounts occurred (TXN ID 2608290003063667671, store 3169 – SDM Scarborough, 2026-08-29). Individual Item Discount amounts within the transaction exceed the item's Original Amount.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client (dbt) | c212_lcl |
| Client (legacy) | ARDM_212 |
| Region | US |
| SnowTime build status | Not built — all `models/mapping/map_ardm_*.sql` are empty stub placeholders (never run through `/onboard-client`) |
| Data source in production | Legacy `ARDMPROD.ARDM_212` schema (pyardm-style Greenplum pipeline), mirrored into Snowflake for Secure to read |
| ARDM version | N/A — pre-SnowTime legacy pipeline |

## 4. Investigation

### 4.1 Confirm SnowTime build status for c212_lcl

POINT OF FAILURE FOUND (scope). All mapping models are auto-generated empty stubs — c212_lcl was never onboarded to SnowTime. This ticket is out of SnowTime's scope entirely.

### 4.2 Confirm production table existence in SnowTime output schema

```sql
SELECT COUNT(*) FROM ARDM_PRODUCTION.C212_LCL.ARDM_ITEMDISCOUNT WHERE TRANSACTIONID = 2608290003063667671
```

FAIL. Object does not exist — confirms Secure is not reading SnowTime output for this client.

### 4.3 Locate legacy schema and confirm as data source

```sql
SELECT SCHEMA_NAME FROM ARDMPROD.INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME LIKE '%212%'
```

PASS. Found ARDM_212 — the legacy schema actually serving Secure.

### 4.4 Row count for the transaction in the legacy table

POINT OF FAILURE FOUND. 67 rows returned, matching the "Total Item Discount Count: 67" shown in Secure — but only 15 unique articles exist in the transaction.

### 4.5 Sum validation against reported wrong value

POINT OF FAILURE FOUND. SUM(AMOUNT) = 2709.95 — exact match to the incorrect value reported in the ticket.

### 4.6 Row-level duplication pattern

FINDING. Each article duplicated 1–12 times with identical AMOUNT/ORIGINALAMOUNT/ACTUALPRICE and identical INSERTEDDATETIME; only RECORDSEQNO/ITEMRECORDSEQNO differ.

### 4.7 pyardm source code review (read-only reference)

FINDING. The observed RECORDSEQNO range (20001–20067) matches the offset used by INSERT block 3 ("Item Discount from HDR/dsct", reading tlog_212.raw_trans_item_dsct). That block performs no DISTINCT/GROUP BY before inserting — it loads whatever rows the raw table contains 1:1.

### 4.8 Greenplum validation — original transaction (direct DB access)

INCONCLUSIVE (data no longer available). 0 rows — tlog_212.raw_trans_item_dsct is a transient staging table, truncated/reloaded per cycle. At query time it held only trans_dt = 2026-09-02. The original 2026-08-29 data was already purged.

### 4.9 Reproduction on live current-day data

```sql
SELECT pos_trans_id, scan_cd, COUNT(*) AS row_count
FROM tlog_212.raw_trans_item_dsct
GROUP BY pos_trans_id, scan_cd
HAVING COUNT(*) > 1
ORDER BY row_count DESC;
```

POINT OF FAILURE FOUND. Same duplication pattern reproduced live on unrelated current data (2026-09-02 load) — dozens of pos_trans_id+scan_cd combinations with 5–8 duplicate rows.

### 4.10 Row-level drill-down on a live duplicate case

ROOT CAUSE ISOLATED. The 8 rows are NOT identical copies — they are 4 distinct discount codes (ZD01 ARCP, ZDP1 Deposits, ZD02 Colleague, ZECP Ecology fee), each appearing twice with different amounts (e.g. ZD02: 0.14 and 0.28; ZDP1: -0.1 and -0.2; ZD01: 1.1 and 5.2), spread across parts 00000, 00001, 00003, 00004 of a 5-part daily export (apprisssourcefilename pattern cerebro_ext_appriss_trans_item_dsct-...-2026-09-02-0000X-of-00005.parquet.pgp); part 00002 held nothing for this transaction.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | Total Item Discount Amount and any aggregate over ARDM_ITEMDISCOUNT for c212_lcl (Loblaw/SDM) |
| Why | The source export cerebro_ext_appriss_trans_item_dsct (Loblaw's SAP/cerebro system) splits each day's file into 5 parts; discount-line snapshots for the same transaction+item land non-deterministically across multiple parts with different amounts per snapshot (not identical duplicates). The Greenplum load script (ARDM_30_ItemDiscount.sql, INSERT block 3) performs no dedup/collapse-to-latest before inserting, so every snapshot becomes an independent ARDM_ITEMDISCOUNT row and inflates any SUM over the table. |
| Scope | Confirmed on the reported transaction (2026-08-29: 67 rows / 15 unique articles) and reproduced live on unrelated current-day data (2026-09-02 load) — ongoing systemic condition, not a one-off. |
| Business impact | Item Discount totals inflated up to ~6x observed on affected transactions — materially misleads investigators reviewing discount activity in Secure for this client. |
| Evidence | See Queries Run — rows 4–14. |

Note: c212_lcl has no SnowTime build — this is entirely a legacy Greenplum pipeline issue, out of SnowTime/dbt scope.

## 7. Recommended Fix

### Option A — Escalate to legacy pipeline owner (Recommended)

File/comment in Jira project DO (same project as precedent tickets DO-9923 "LCL - Hypercare - Item Discounts Duplicating Results", closed 2026-04-20, owner Bartosz Pohoryles, and DO-2828), citing:

* This transaction as a historical repro (2026-08-29, 67 rows / 15 articles).
* The live current-day repro (4.9–4.10) — stronger evidence since it's reproducible today.
* The specific mechanism: cerebro_ext_appriss_trans_item_dsct 5-part export produces multiple differently-valued snapshots per transaction+item, not collapsed before/during Greenplum load (ARDM_30_ItemDiscount.sql block 3, no DISTINCT/latest-wins logic).
* Ask to confirm whether this is a regression of the DO-9923 fix or a new duplication source, and whether the fix belongs in the export process or the load script.

No fix is possible from the SnowTime/dbt side — the pipeline and its source code are outside this repo's ownership and runtime.

## 8. Open Questions

* Is this a regression of the DO-9923 fix (closed 2026-04-20), or a new/different duplication source?
* Does the export/loader team confirm the "multi-snapshot, non-deterministic file-part distribution" mechanism?
* Is c212_lcl's eventual onboarding onto SnowTime planned?

## 9. Queries Run

| # | Environment | Schema/DB | Result |
| --- | --- | --- | --- |
| 1 | Snowflake | ARDM_PRODUCTION.C212_LCL | Object does not exist |
| 2 | Snowflake | ARDMPROD.INFORMATION_SCHEMA | Found ARDM_212 |
| 3 | Snowflake | ARDMPROD.ARDM_212 | 67 rows for the transaction |
| 4 | Snowflake | ARDMPROD.ARDM_212 | SUM(AMOUNT)=2709.95 |
| 5 | Snowflake | ARDMPROD.ARDM_212 | 67 rows / 15 articles, dup pattern confirmed |
| 6 | Greenplum | ardm_212 | Got x_postransid |
| 7 | Greenplum | tlog_212 | raw_sdm_poslogs_lineitem: 0 rows |
| 8 | Greenplum | tlog_212 | raw_trans_item_dsct: 0 rows (purged) |
| 11 | Greenplum | tlog_212 | Single batch, 2026-09-06 |
| 12 | Greenplum | tlog_212 | Single day, 2026-09-02 |
| 13 | Greenplum | tlog_212 | GROUP BY pos_trans_id, scan_cd HAVING COUNT(*)>1: dozens of dup groups |
| 14 | Greenplum | tlog_212 | 8 non-identical snapshot rows |
| 15 | Greenplum | tlog_212 | Confirms 4-of-5-part distribution pattern |

## 10. Extras / Additional Screenshots

Store receipt screenshot, Secure item-discount grid with duplicate Client Record Seq No rows, raw source-system export view. [See Jira attachment / link in ticket]
