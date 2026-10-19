---
ticket: RCS-28649
cliente: The Home Depot (THD) / c085_thd
analista: Diego Buelvas
estado_ficha: Resolved (investigacion), Jira aun en Escalated
sintoma: transacciones del 27 y 28 de agosto sin detalle de item ni tender en el recibo
causa: la task horaria PRODUCTION_C085_THD_TASK quedo SUSPENDED tras un ciclo de RESUME/SUSPEND durante un backfill activo
fix: correr las queries de fill del backfill, y ante recurrencia ALTER TASK RESUME con SNOWTIME_ENGINEERING_ADMIN_ROLE
nota_reutilizable: descartar la teoria del cliente midiendo ratios item/header y tender/header por dia antes de aceptarla
confluence_id: 478158094339
modificado: 2026-08-30
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478158094339
---

# RCS-28649 — The Home Depot: Item/Tender Detail Missing for Recent Transactions

Prepared: 30 August 2026 | Analyst: Diego Buelvas | Status: Resolved (investigation) — Jira ticket status still shows Escalated

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28649 |
| Customer | The Home Depot (THD) |
| Issue Type | Incident |
| Priority | High |
| Status (Jira) | Escalated |
| Opened | 28 August 2026 |
| Reporter | Ericka Smith (ericka_d_smith@homedepot.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28649 |

## 2. Problem Statement

Original report: an error pop-up occurred when viewing a receipt via the 'i' icon for a recently-loaded transaction. Resolved same-day via a configuration fix.

Follow-up issue (subject of this triage): after the config fix, the client reported a large volume of transactions from 8/27 and 8/28 with item/tender line detail missing from the receipt view. The client identified this via their own reconciliation report, which compares a transaction's header subtotal against the subtotal derived from item-level data.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | `c085_thd` |
| Region | US |
| Snowflake schema | `ARDM_PRODUCTION.C085_THD` (output) / `C085_THD_SNOWTIME` (working) |
| ARDM version | V1 (legacy pyardm-based schema) |
| Active product | EBR Secure |

## 4. Investigation

### 4.1 Raw ingestion health — file-naming theory

PASS. Volumes and ratios (item/header ~3.3, tender/header ~0.94) were stable every day including 8/27. Only 9 file-level errors across the whole 9-day window, all transient, none on 8/27-8/28, all auto-recovered on retry. File-naming theory ruled out.

### 4.2 Aggregate ARDM coverage by tradingday

PASS. 8/27 aggregate was completely normal (5.18M header rows, 3.30 item/header, 0.93 tender/header).

### 4.3 Point-transaction check

POINT OF FAILURE FOUND. For store 6568, register 90, ticket 9636, tradingday 2026-08-27, subtotal $2,074.00: header row present in `ARDM_HEADER`; `ARDM_ITEM` and `ARDM_TENDER` = 0 rows. The raw detail (2 item rows) and tender row WERE present in `RAW_DATA` — arrived 2026-08-28 08:39, a day after the transaction. The gap was downstream of raw ingestion.

### 4.4 Build cadence check

POINT OF FAILURE FOUND. Normal hourly production builds (148-149 models, 0 errors) ran through the morning of 8/28, last one closing its window at 08:05:09 and ending 09:23:59. Every invocation after that point had only 4 models, in weekly-slice windows walking backward through history — the `/backfill-ardm` signature, not the regular incremental build.

### 4.5 Task state check

POINT OF FAILURE FOUND. Task `state = SUSPENDED`. `QUERY_HISTORY` showed Dan Endersby cycling RESUME/SUSPEND on the task three times that morning (05:05, 05:19, 05:37 PT), with the last action being a SUSPEND — coincident with the active `/backfill-ardm` run launched by Sumeet Jain on 8/26.

### 4.6 Resolution validation

PASS. Ryan DeVries executed the backfill fill queries against the backfill table; the data gap closed successfully.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | `PRODUCTION_C085_THD_TASK` (the client's hourly incremental dbt production task) was left in `SUSPENDED` state |
| Why | RESUME/SUSPEND cycled three times (05:05, 05:19, 05:37 PT on 8/28) during an active `/backfill-ardm` run, leaving it suspended after the last action. While suspended, no incremental build merged newly-arrived `RAW_DATA` into `ARDM_ITEM`/`ARDM_TENDER` |
| Scope | Transactions whose raw detail/tender files arrived after the last successful build window closed (~08:05 UTC on 8/28) through the remainder of the suspension |
| Business impact | Investigators in EBR Secure could not see item/tender line detail for affected transactions |
| Evidence | Example transaction: header present, 0 rows in ARDM_ITEM/ARDM_TENDER, matching raw rows present in RAW_DATA arrived 2026-08-28 08:39. QUERY_HISTORY confirmed `ALTER TASK ... SUSPEND` at 2026-08-28 05:37:16 -07:00 as the last state-changing action |

## 6. Additional Findings

Investigated and ruled out the client's own hypothesis that a file naming-convention change (8/23 to 8/24) caused the gap. RAW_DATA arrival volumes and ratios were verified normal across the full window; MONITORING.RAW_FILE_LOG showed no naming-related or elevated errors.

## 7. Recommended Fix

### Option A — Applied

Ryan DeVries executed the backfill fill queries against the backfill table, which closed the data gap without requiring further RESUME/SUSPEND coordination.

### Option B — Standing alternative for recurrence

If the task is found suspended again after a future backfill: confirm with whoever suspended it that no conflicting operation is in progress, then `ALTER TASK ARDM_PRODUCTION.C085_THD_SNOWTIME.PRODUCTION_C085_THD_TASK RESUME` (role `SNOWTIME_ENGINEERING_ADMIN_ROLE`).

## 8. Open Questions

* Confirm why the task was suspended/resumed repeatedly on 8/28, to prevent recurrence during future backfills.
* Confirm current state of `PRODUCTION_C085_THD_TASK` post-fix so it doesn't silently stay down for future incremental loads.

## 9. Queries Run

| # | Query | Result |
| --- | --- | --- |
| 1 | RAW_DATA counts + ratios per day, 8/19-8/28 | Stable every day, incl. 8/27 |
| 2 | MONITORING.RAW_FILE_LOG attempts/errors, 9-day window | 9 transient errors total |
| 4 | RAW_FILE_LOG row-level failures since 8/26 | 0 rows |
| 5 | ARDM_HEADER/ITEM/TENDER per-tradingday counts + ratios | 8/27 normal |
| 7 | ARDM_HEADER point lookup store 6568 reg 90 ticket 9636 | Header found, subtotal matches |
| 8 | ARDM_ITEM/ARDM_TENDER count for that transactionid | 0 rows both tables |
| 9 | RAW_DATA point lookup same natural key | 2 item rows + 1 tender row, arrived 2026-08-28 08:39 |
| 10 | MONITORING.DBT_RUNS recent history | Full hourly builds stop after 09:23:59 |
| 11 | SHOW TASKS PRODUCTION_C085_THD_TASK | state = SUSPENDED, USER_SUSPENDED |
| 12 | QUERY_HISTORY ALTER TASK SUSPEND/RESUME | 3 cycles, last action SUSPEND 05:37:16 -07:00 |

## 10. Extras / Additional Screenshots

Client screenshots (file naming comparison, receipt without item lines, Explorer file listing). Internal write-up: `.claude/skills/investigate-dataload/findings/2026-08-28_c085_thd_task_suspended_during_backfill.md`
