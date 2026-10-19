---
ticket: RTS-206268
cliente: Kinney Drugs (KNY/179) / c179_kny
analista: Diego Buelvas
estado_ficha: WORK IN PROGRESS
sintoma: Work Item de stock count adjustments falla en la deaggregacion con invalid identifier T2.POS_ARTICLEID
causa: la migracion SnowTime renombro la columna a ARTICLEID y la metadata de Instant Analytics no se resincronizo, hay dos objetos de campo distintos con la misma etiqueta Article ID
fix: traza en runtime por Engineering para hallar donde se resuelve el binding de Expanded Display Fields, y congelar ediciones en Composer
advertencia: editar el campo en Composer empeoro el fallo de 3/30 a 11/30
familia: rename de columnas ARDM v2 sin resync del catalogo
relacionados: RCS-28352, RCS-28606, RTS-206610, RTS-206667
confluence_id: 478143053843
modificado: 2026-08-25
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478143053843
---

# RTS-206268 — Kinney Drugs (KNY/179): WI Deaggregation Failure (invalid identifier T2.POS_ARTICLEID)

Prepared: 21 August 2026 | Analyst: Diego Buelvas | Status: WORK IN PROGRESS

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RTS-206268 |
| Customer | Kinney Drugs (KNY/179) |
| Issue Type | Incident |
| Priority | Medium |
| Status | Work in Progress |
| Opened | 20 August 2026 |
| Reporter | svc rts (svc-rts@apprissretail.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RTS-206268 |

## 2. Problem Statement

Grafana Work Item alert fired for Kinney Drugs (KNY/179). Investigation traced the failure to WI definition `stock count adjustments.fti` (entity ADJUSTMENT, Inventory Data Area), which fails during Step3 deaggregation with a Snowflake SQL compilation error on `T2.POS_ARTICLEID` — a physical column that no longer exists following the client's SnowTime migration.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | c179_kny |
| Region | US |
| ARDM Version | V2 (snowtimeV2) |
| Snowflake Schema | ARDM_PRODUCTION.C179_KNY (+ working schema C179_KNY_SNOWTIME) |
| Active Modules | Inventory (custom tables: inventory_adjustment, inventory_itemposition, inventory_document) |

## 4. Investigation

### 4.1 Initial log review

POINT OF FAILURE FOUND — Snowflake error: SQL compilation error, invalid identifier 'T2.POS_ARTICLEID', SqlState 42000, VendorCode 904.

### 4.2 dbt/Snowflake schema verification

PASS — INVENTORY_ADJUSTMENT's canonical column is ARTICLEID; X_POS_ARTICLEID is a separate, always-NULL placeholder. No POS_ARTICLEID column exists. Schema is correct by design post-migration.

### 4.3 Composer "Display Fields" fix

PASS (partial) — Re-added entity ADJUSTMENT's "Article ID" field (Display Fields section). Resolved 27/30 WI results; 3/30 still failing.

### 4.4 Data consistency check on the 3 failures

PASS — All values (T1/T2/T3) matched the WI's expected parameters exactly, including a negative-value stock adjustment. Ruled out data/dbt issue.

### 4.5 Second field object identified

POINT OF FAILURE FOUND — A DISTINCT "Article ID" field object exists under "Expanded Display Fields" (same visible label, different binding), used by the deaggregation SQL builder, still bound to the stale name (generates alias `posarticleid`).

### 4.6 Re-add attempt on "Expanded Display Fields" field

FAIL — Deleting/re-adding this field worsened the failure count from 3/30 to 11/30. Re-adding via Composer re-copies the same stale binding rather than curing it.

### 4.7 Secure repo code search

PASS — Zero hardcoded POS_ARTICLEID/ArticleId references in `Sources/Core/Core/Instant Analytics/**` or the Snowflake UDF folder. Rules out a code-level hardcode.

### 4.8 Platform DB metadata search

POINT OF FAILURE FOUND (partial) — Found the literal string only in output/audit-log tables (stats.Search.NativeCommand, workview.WorkItemDefinitionGenerationRequest.DeaggregationSql and DeaggregationNativeCommand) — generated-SQL snapshots of past executions, not the source catalog.

### 4.9 Code path trace

FAIL (unresolved) — Confirmed exact code path: `WorkItemDeaggregationProcessor.GetDeaggregatedEvents` (`WorkItemDeaggregationProcessor.cs:507`), called via `WorkItemDeaggregationProcessorBase.ExecuteDeaggregationRequests` (Step3). No hardcoded binding; source of the physical-column mapping not yet located.

## 5. Root Cause Statement

| Aspect | Details |
| --- | --- |
| What broke | WI stock count adjustments.fti (entity ADJUSTMENT, c179_kny) — Step3 deaggregation SQL references physical column POS_ARTICLEID, which does not exist |
| Why | SnowTime migration renamed the column to canonical ARTICLEID (+ separate always-NULL X_POS_ARTICLEID placeholder). Secure's Instant Analytics field metadata for entity ADJUSTMENT was never resynced. Two distinct field objects share the label "Article ID" — one in "Display Fields" (fixed), one in "Expanded Display Fields" (still stale, source not located) |
| Scope | WI generated 30 results for 2026-08-19; currently 11/30 fail (was 3/30 before the last Composer edit) |
| Business impact | Stock Count Adjustments WI cannot fully generate — partial results block downstream review of stock-count outliers; repeat Grafana WI-failure alerts |
| Evidence | Three QueryIds all show the same invalid-identifier error; Snowflake schema + data confirmed correct; Platform DB search confirms the string only lives in output logs |

## 6. Additional Findings

This defect class — a second, independently-bound field object hidden under "Expanded Display Fields"/supporting-search collections that the main Composer editor doesn't fully resolve on edit — mirrors RCS-28352 (Floor&Decor, WISC SupportingSearches type mismatch). Worth flagging to Engineering as a recurring metadata-resync gap after SnowTime migrations.

## 7. Recommended Fix

Option A — Recommended: Engineering runtime trace. Escalate to Engineering to trace, via debugger/runtime inspection, where `WorkItemDeaggregationProcessor.GetDeaggregatedEvents` resolves the "Expanded Display Field" physical column name for entity ADJUSTMENT at runtime. Once located, correct the binding from `POS_ARTICLEID` to `ARTICLEID` (never `X_POS_ARTICLEID`, a distinct always-NULL placeholder).

Option B — Freeze further Composer edits. Do not keep trial-and-error editing "Expanded Display Fields" — each round has widened the failure blast radius (3 to 11 of 30). Hold until Engineering fixes the true metadata source.

## 8. Open Questions

* Where does Composer's "Expanded Display Fields" Article ID binding get sourced from at write-time?
* Does this defect class affect other SnowTime-migrated clients with the Inventory module enabled?
* Should the "Expanded Display Fields" Article ID entry be removed entirely instead of repaired?

## 9. Queries Run

Query 1 — inventory_adjustment data check for location 74 / tradingday 2026-08-19 / three articles:

| ArticleID | x_DepartmentNumber | x_Description | UnitCost | Quantity | TotalCost |
| --- | --- | --- | --- | --- | --- |
| 0045072 | 0003 | PHOTO BOOK PINCH 8X10 BLK | 5.71 | 19 | 108.49 |
| 0556475 | 0003 | 4X6 PRINT | 0.12 | 212 | 25.44 |
| 5416256 | 0006 | SECRET EXP IS LAVNDR 2.7OZ | -5.48 | -40 | 219.20 |

Query 2 — inventory_document data check: T3 carries the signed value (-219.20 for 5416256), matching the WI's deagg parameters exactly.

Query 3 — inventory_itemposition join-key check: PositionID matches the corresponding T2 row exactly.

Query 4 — Snowflake schema check: INVENTORY_ADJUSTMENT is a base table with no POS_ARTICLEID column.

Query 5 — Platform DB full-text metadata search for 'POS_ARTICLEID': matches only in stats.Search (NativeCommand, NativeCommandParameters) and workview.WorkItemDefinitionGenerationRequest (DeaggregationSql, DeaggregationNativeCommand) — all output/audit-log tables, not the source catalog.

## 10. Extras / Additional Screenshots

Composer views of the WI definition and the "Expanded Display Fields" list showing the second "Article ID" field object. [See Jira attachment / link in ticket]
