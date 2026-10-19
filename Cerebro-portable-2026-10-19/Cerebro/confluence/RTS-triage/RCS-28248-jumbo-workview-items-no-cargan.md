---
ticket: RCS-28248
cliente: Jumbo Supermarkets / c128_jmo (EU)
analista: Diego Buelvas
estado_ficha: WORK IN PROGRESS
sintoma: faltan items de WorkView que se esperan cada mes fiscal
causa: sin defecto tecnico confirmado, el desplome de voids es un cambio real de comportamiento del cliente, y Promoties en 0 candidatos sigue sin causa aislada
fix: confirmar con el cliente si espera resultados en el periodo fiscal actual, cerrar como no-bug si aplica
nota_reutilizable: comparar RAW_TLOG contra ARDM_HEADER a ambos lados del cutover separa cambio de comportamiento de defecto de pipeline
confluence_id: 478143479809
modificado: 2026-08-25
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478143479809
---

# RCS-28248 — Jumbo Supermarkets: Workview Items Not Loaded Correctly

Prepared: 18 August 2026 | Analyst: Diego Buelvas | Status: WORK IN PROGRESS

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28248 |
| Customer | Jumbo Supermarkets (client 128, c128_jmo, EU) |
| Issue Type | Incident |
| Priority | Medium |
| Status | WORK IN PROGRESS |
| Opened | 10 August 2026 |
| Reporter | Timo Bakker |
| Assignee | Diego Buelvas |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28248 |

## 2. Problem Statement

Customer reports several WorkView items expected each fiscal month are missing, with no noticeable change made to the underlying search questions. Asked whether items may still be processing in the background.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | c128_jmo |
| Region | EU |
| ARDM Version | NOT AVAILABLE |
| Snowflake Schema | C128_JMO / C128_JMO_SNOWTIME |
| Active Products | Secure WorkView / WISC |

## 4. Investigation

### 4.1 Filiaal - Bon annuleren (Void amount collapse)

Query: Compared daily void-count/SUM(x_voidamount) for values >€50 around trading day 2026-05-28 to 2026-05-29; verified raw XML (RAW_TLOG) against ARDM_HEADER on both sides of the cutover (201.76 and 1099.89 respectively).

PASS. Raw and ARDM values match — not a SnowTime/RDL bug. POS version (R10) unchanged across the cutover. Void count dropped ~37x (~700 to ~18/day) with stable ticket volume — a real behavior/policy change at Jumbo, not a technical defect.

### 4.2 Promoties / Filiaal - Promoties (zero candidates since fiscal 2025-P13)

FAIL (hypothesis ruled out). A join to a nonexistent `ardm_Header_Ext` table appeared only in a stale/cached `DefinitionNativeCommand`; the live query references `T1.x_ECommFlg` directly. No structural search bug found.

POINT OF FAILURE FOUND (tentative). Resaving both Search Compose definitions (SearchVersion bumped: ondernemers 13 to 14, filialen 12 to 13) and running manually returned results, but only under a ~13-month wide date range — not the narrow fiscal-period window WISC actually uses — so this may be a false positive picking up old Aug–Dec 2025 matches.

FAIL. Automatic WISC rerun after the resave confirmed the new SearchVersion with Failed=0, still 0 candidates for the current fiscal period.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | (1) `X_VOIDAMOUNT` totals dropped sharply per day; (2) Promoties searches return 0 candidates for the current fiscal period |
| Why | (1) Confirmed real behavior/policy change at Jumbo — no technical defect; (2) Unconfirmed — leading hypothesis is a similar genuine behavior change, not a bug; the SearchVersion bump coinciding with the cutoff may be correlation, not causation |
| Scope | c128_jmo, EU — 2 of 14 active WorkView definitions affected; void issue isolated to the 2026-05-28/29 cutover; Promoties at 0 candidates since fiscal period 2025-P13 (Dec 2025) |
| Business impact | Customer-visible: fewer/no WorkView items generated for 2 of 14 monthly searches |
| Evidence | Void: RAW_TLOG matches ARDM_HEADER exactly; void count ~700 to ~18/day at the same ticket volume. Promoties: 0 candidates before and after the resave under the narrow fiscal window |

## 6. Additional Findings

A cached/stale `DefinitionNativeCommand` referencing a nonexistent `ardm_Header_Ext` join was found during investigation but ruled out as the cause.

## 7. Recommended Fix

### Option A — Confirm with customer, no technical fix (Recommended)

Both findings currently point to genuine behavior changes at Jumbo, not pipeline or search-engine defects. Confirm with the customer whether they expect results to still be generated in the current fiscal period. If confirmed as expected business behavior, close as no-bug on both fronts.

## 8. Open Questions

1. Does the customer expect any results in the current fiscal period for Promoties?
2. Is the SearchVersion bump coincidental with the 0-candidate cutoff, or could the resave itself have altered narrow-window matching behavior?
3. Where in Search Compose is the date range actually parameterized for Run/Preview? Needed to replicate WISC's narrow fiscal-period window manually.

## 9. Queries Run

| # | Query | Result |
| --- | --- | --- |
| 1 | Daily void count/SUM comparison around the cutover | Confirms ~37x drop, real not technical |
| 2 | RAW_TLOG vs ARDM_HEADER value comparison at cutover | Values match exactly on both sides |
| 3 | Search Compose live definition inspection | No `ardm_Header_Ext` join in live query |
| 4 | Manual Promoties search run post-resave (wide range) | Returned results — likely false positive |
| 5 | WorkItemDefinitionGenerationRequest / WorkItemDeaggregationRequest post-resave | SearchVersion updated, Failed=0, candidate_rows=0 |

## 10. Extras / Additional Screenshots

Customer screenshot of the WorkView items view. Full void-amount investigation detail: `.claude/skills/investigate-dataload/findings/2026-08-14_c128_jmo_void_amount_collapse.md` (SnowTime repo).
