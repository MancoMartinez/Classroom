---
ticket: RCS-28834
cliente: ICA / c163_ica (EU)
analista: Diego Buelvas
estado_ficha: Work in Progress
sintoma: Bank Withdrawal y Bank Deposit desaparecieron del resumen de medios de pago y el drill down sale vacio
causa: las busquedas son header-driven, FROM ardm_header LEFT JOIN ardm_tender, y los tender EPS 186/187 nunca generan fila de header
fix: reconstruir ambas busquedas tender-driven, sin tocar el pipeline dbt
familia: busquedas Composer federadas Snowflake mas SQL Server
confluence_id: 478190534658
modificado: 2026-09-09
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478190534658
---

# RCS-28834 — ICA: Can not find bank withdrawal or bank deposit

Prepared: 09 September 2026 | Analyst: Diego Buelvas | Status: Work in Progress

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28834 |
| Customer | ICA |
| Issue Type | SOW Estimation |
| Priority | Critical |
| Status | Work in Progress |
| Opened | 09 September 2026 |
| Reporter | effektivrutinanalys (effektivrutinanalys@ica.se) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28834 |

## 2. Problem Statement

Client reports that the "9.1 Betalmedel sammanställning" search (tender-type summary, all stores) no longer shows Bank Withdrawal or Bank Deposit as tender types, although it did previously. Additionally, running "10.1 Insättningar till kort" for store 11891 returns 3 grouped results, but opening any one of them for drill-down detail returns an empty result ("No Results Found").

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | c163_ica |
| Region | EU |
| ARDM Version | V2 (snowtimeBase + snowtimeV2) |
| Snowflake Schema | ARDM_PRODUCTION.C163_ICA (output) / C163_ICA_SNOWTIME (working) |
| Affected Store | 11891 (and confirmed store-agnostic — all stores affected) |

## 4. Investigation

### 4.1 EPS tender data-gap check (Snowflake, all stores)

Query: Aggregated ARDM_TENDER row counts/day for TenderType 186 (EPS Deposit) and 187 (EPS Withdrawal) over the last 30 days, all stores.

PASS. Continuous daily activity (500–1800+ rows/day per type) through 2026-09-09, no pipeline gap. Ruled out a SnowTime/dbt data issue.

### 4.2 Drill-down transaction existence check

Query: Looked up the 3 card-masked transactions from the "10.1" drill-down screenshot directly in ARDM_TENDER.

PASS. All 3 underlying transactions exist with correct amounts (summing to the -6,540 shown in the search). Confirms underlying tender data is not corrupted or missing.

### 4.3 Enumeration catalog check (secure.EnumerationReferenceData)

Query: `SELECT * FROM secure.EnumerationReferenceData WHERE EnumerationType='tendertype' AND KeyAsInt IN (186,187)`

PASS. Catalog has correct, distinct labels — 186 = "Insättning" (SortOrder 8), 187 = "Uttag" (SortOrder 30) — present for cultures en, en-GB, en-US. Ruled out catalog/label misconfiguration.

### 4.4 Search architecture identification

Finding: ardm_header/ardm_tender referenced in the search SQL do not exist in the SQL Server database (INFORMATION_SCHEMA.TABLES returned 0 rows) — confirmed they resolve to Snowflake tables (ARDM_PRODUCTION.C163_ICA.ARDM_*), while secure_EnumerationReferenceData is a composer alias for secure.EnumerationReferenceData in SQL Server.

INFO. Secure Composer searches over ARDM data are federated Snowflake + SQL Server queries; the exported SQL is not directly executable against a single engine.

### 4.5 Header/tender join-direction check

Query: For the 3 sampled transactions of card 5342430000008514 (TenderType 186), looked up matching rows in ARDM_HEADER by transactionid.

POINT OF FAILURE FOUND. Zero rows returned in ARDM_HEADER for any of the transactions. Confirmed across 6 transactions of the same card (2026-06-17 through 2026-09-07, 4 different stores): ARDM_TENDER populated, ARDM_HEADER always empty. Both affected searches are built FROM ardm_header ... LEFT JOIN ardm_tender ... (header as the driving table) — a transactionid with no header row is structurally excluded from the result set, regardless of any filter logic.

## 5. Root Cause Statement

| What broke | Both "9.1 Betalmedel sammanställning" (summary) and "10.1 Insättningar till kort" (drill-down) searches |
| --- | --- |
| Why | EPS Deposit/Withdrawal tender rows (TenderType 186/187) are bank/cash-management operations, not customer sales — they legitimately never generate an ARDM_HEADER row (correct, expected data behavior, not a SnowTime/dbt defect). Both searches are built header-driven (FROM ardm_header LEFT JOIN ardm_tender), so any tender row without a matching header is structurally dropped from the result set. |
| Scope | Tenant-wide, all stores, not date-bound — every EPS Deposit/Withdrawal transaction is affected, ongoing since these searches were built this way |
| Business impact | Client cannot reconcile bank deposits/withdrawals via Secure reporting — both the aggregate summary and the transaction-level drill-down are unusable for these 2 tender types |
| Evidence | ARDM_TENDER: continuous EPS activity, no gap (4.1). ARDM_HEADER: 0 matching rows across 6 sampled transactions / 4 stores (4.5). Enumeration catalog: correct and complete (4.3). |

## 6. Additional Findings

Secure Composer searches over ARDM data are federated queries spanning two engines: ardm_header/ardm_tender (and other ARDM/reference tables) resolve to Snowflake; secure_<TableName> aliases resolve to secure.<TableName> in SQL Server. The composer's exported "preview SQL" text is not directly runnable against a single engine — each alias must be translated to its real location before manual testing. Useful precedent for any future ticket involving Secure search behavior over ARDM data.

## 7. Recommended Fix

### Option A — Rebuild both searches tender-driven (Recommended)

Rebuild "9.1 Betalmedel sammanställning" and the "10.1 Insättningar till kort" drill-down as FROM ardm_tender T1 LEFT JOIN ardm_header T2 ON (...) instead of header-driven. Source StoreCashierNo/POSNo/TicketNo/EndTransDateTime directly from ardm_tender (already present on every tender row — confirmed in the client's dbt mapping model). This is a change to the saved search/report definitions in Secure Composer for c163_ica — no dbt/SnowTime pipeline change required.

## 8. Open Questions

* Confirm whether other clients' equivalent tender-type summary searches share the same header-driven join pattern (potential broader bug class, not ICA-specific).
* Confirm whether any other tender type besides EPS Deposit/Withdrawal can legitimately be headerless (e.g. till float adjustments), which would also be silently affected by the same pattern.
* Confirm ownership (Delivery vs. Engineering) for editing the saved Composer search definitions for c163_ica, to route the fix.

## 9. Queries Run

| # | Query | Environment | Outcome |
| --- | --- | --- | --- |
| 1 | ARDM_TENDER daily counts for tendertype 186/187, last 30 days | Snowflake (snowflake-eu) | PASS — continuous daily volume |
| 2 | ARDM_TENDER lookup by cardnumberlast4 for the 3 drill-down cards | Snowflake (snowflake-eu) | PASS — transactions confirmed real |
| 3 | `SELECT * FROM secure.EnumerationReferenceData WHERE EnumerationType='tendertype' AND KeyAsInt IN (186,187)` | Secure SQL Server (client-run) | PASS — catalog correct |
| 4 | INFORMATION_SCHEMA.TABLES LIKE '%header%' / '%tender%' | Secure SQL Server (client-run) | INFO — 0 results, confirms tables live in Snowflake |
| 5 | ARDM_TENDER LEFT JOIN ARDM_HEADER on transactionid+tradingday for card 5342430000008514 | Snowflake (snowflake-eu) | POINT OF FAILURE FOUND — header_storeno NULL for all rows |
| 6 | ARDM_HEADER lookup by transactionid list | Snowflake (snowflake-eu) | POINT OF FAILURE FOUND — 0 rows, confirms no header exists |

## 10. Extras / Additional Screenshots

Result tables of "9.1" and "10.1" plus the empty drill-down — [See Jira attachment / link in ticket]
