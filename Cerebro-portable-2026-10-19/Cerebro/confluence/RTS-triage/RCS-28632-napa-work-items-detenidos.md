---
ticket: RCS-28632
cliente: NAPA (Genuine Parts Company) / c356_gpc
analista: Diego Buelvas
estado_ficha: Work in Progress
sintoma: los Work Items no se ejecutan desde el 2 de agosto
causa: el backload del 17 de agosto restauro los datos pero no las filas de PYARDM_CENTRAL_LOAD_LOG_TABLE para el 04 al 10 de agosto, el generador es secuencial y se quedo trabado en el primer dia sin marcador
fix: insertar las 7 filas faltantes en el load log con los conteos reales de ARDM_HEADER, requiere rol DataOps sobre ARDM_000
nota_reutilizable: el chequeo Go/No Go de Work Items avanza dia por dia y no salta un dia sin marcador de carga
confluence_id: 478155571201
modificado: 2026-08-28
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478155571201
---

# RCS-28632 — NAPA: Investigate and resolve stalled work item execution following data synchronisation

Prepared: 28 August 2026 | Analyst: Diego Buelvas | Status: Work in Progress

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28632 |
| Customer | NAPA (Genuine Parts Company — c356_gpc) |
| Issue Type | Incident |
| Priority | High |
| Status | Work in Progress |
| Opened | 27 August 2026 |
| Reporter | James DeJohn (jdejohn@apprissretail.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28632 |

## 2. Problem Statement

NAPA Work Items have not executed since August 2, 2026. Following the Secure migration to Snowflake, the Snowflake replication task was found missing — data continued loading into Greenplum but was not transferred to Snowflake. The missing task was added and a backload was completed on August 17, bringing data up to date. Work Items did not resume, with no activity visible since August 2. Issue surfaced during a live customer training session, raising urgency.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | c356_gpc |
| Region | US |
| Client numeric ID (Secure) | 356 |
| ARDM schema (legacy pyardm) | `ARDMPROD.ARDM_356` |
| Shared load-log schema | `ARDMPROD.ARDM_000` |
| Active product | Secure 5 — EBR (Work Items / Instant Analytics) |

## 4. Investigation

### 4.1 GNG mechanism review

Reviewed Confluence spec ("Secure - Work Items Go/No Go Check (GNG)") and Secure source (`ArdmMonitoringClient.cs`). Confirmed the Work Item Generator calls `secure.ArdmBatchStatusPeriodSelect`, which queries a per-trading-day transaction count. It advances sequentially, day by day, and will not proceed past a day it considers "not loaded."

### 4.2 Load-log table check

POINT OF FAILURE FOUND. Rows exist for 08-01 to 08-03, then a complete gap for 2026-08-04 through 2026-08-10 (zero rows), then rows resume from 08-11 onward — all inserted in a single batch at 2026-08-17 09:51 (the backload event). The Work Item Generator stalled at the first missing day (08-04), never reaching the later days that are actually complete.

### 4.3 Underlying data validation

PASS. Real transactional data is complete and normal for the entire gap window (~410K–443K transactions/day, ~5,650–5,680 stores/day). Confirms the underlying data was never missing — only the load-completion marker was.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | The Work Item Go/No-Go (GNG) check found no "batch loaded" marker for 2026-08-04 through 2026-08-10 in the shared load-log table |
| Why | The August 17 backload restored real ARDM transactional data for the full gap window but did not insert the corresponding rows into `ARDMPROD.ARDM_000.PYARDM_CENTRAL_LOAD_LOG_TABLE` for those 7 specific days |
| Scope | c356_gpc (NAPA), trading days 2026-08-04 to 2026-08-10; Work Item generation halted from that point through 2026-08-28 |
| Business impact | ~26 days of Work Item generation withheld from production, surfaced during a live customer training session |
| Evidence | Load-log table: 0 rows for 08-04 to 08-10 vs. real data: 442,914 / 435,729 / 428,885 / 414,734 / 205,705 / 47,656 / 431,915 transactions respectively |

## 7. Recommended Fix

### Option A — Backfill the missing load-log rows (Recommended)

```sql
INSERT INTO ARDMPROD.ARDM_000.PYARDM_CENTRAL_LOAD_LOG_TABLE
  (client_id, tradingday, transaction_count, store_count, insert_timestamp, _row_created)
VALUES
  ('356', '2026-08-04', 442914, 5671, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()),
  ('356', '2026-08-05', 435729, 5673, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()),
  ('356', '2026-08-06', 428885, 5678, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()),
  ('356', '2026-08-07', 414734, 5653, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()),
  ('356', '2026-08-08', 205705, 5052, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()),
  ('356', '2026-08-09', 47656, 1630, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()),
  ('356', '2026-08-10', 431915, 5666, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP());
```

Requires a DataOps-privileged role on `ARDMPROD.ARDM_000` (shared cross-client table — not self-service). Once inserted, the GNG passes for 08-04 and the Work Item Generator resumes automatically on its next scheduled run, working through the remaining backlog unattended.

### Option B — Skip GNG check (workaround, use with caution)

Documented emergency bypass exists to force the Work Item Generator past the stalled day without the log-table fix. Not recommended here since Option A directly addresses the root cause and is low-risk given data is confirmed present.

## 8. Open Questions

* Pending: DataOps (or an operator with write grant on `ARDMPROD.ARDM_000`) to execute the Option A INSERT.
* Pending: confirm Work Item Generator resumes automatically post-insert and processes the full backlog without further intervention.

## 9. Queries Run

| # | Query | Executed against | Result |
| --- | --- | --- | --- |
| 1 | PYARDM_CENTRAL_LOAD_LOG_TABLE WHERE client_id='356' AND tradingday >= '2026-08-01' | `ARDMPROD.ARDM_000` | Gap confirmed: no rows 08-04 to 08-10 |
| 2 | COUNT(*) and COUNT(DISTINCT storeno) per tradingday from ARDM_HEADER, 08-04 to 08-10 | `ARDMPROD.ARDM_356` | Real data complete for the full gap window |

## 10. Extras / Additional Screenshots

Task Logs screenshot (client 356, trading day 2026-08-04, GNG skip messages). [See Jira attachment / link in ticket]
