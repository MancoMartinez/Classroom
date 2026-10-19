---
ticket: RTS-206639
cliente: Petco (PTC/064) / c064ptc legacy Greenplum
analista: Vismaya Thottada
estado_ficha: Work in Progress, fix listo pendiente de deploy
sintoma: alerta de dataload, GP Process Error por StringDataRightTruncation en ardm_customer_stg
causa: trim(firstname)||' '||trim(lastname) sin guarda de longitud contra una columna varchar(100), un registro con una nota de servicio en lastname llego a 105 caracteres
fix: envolver con left(...,100) en ardm_7_customer.sql, y avisar al cliente que el extract PSD_02Cust mete texto libre en last_name
confluence_id: 478153277444
modificado: 2026-08-27
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478153277444
---

# RTS-206639 — Petco: CustomerFullName varchar(100) truncation

Prepared: 27 August 2026 | Analyst: Vismaya Thottada | Status: Work in Progress (code fix ready, pending deploy)

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RTS-206639 |
| Customer | Petco (PTC/064) |
| Issue Type | Incident |
| Priority | Medium |
| Status | Under Support Data Team Review |
| Opened | 27 August 2026 |
| Reporter | Neha Haridas (nharidas@apprissretail.com) |
| Assignee | Vismaya Thottada (vthottada@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RTS-206639 |

## 2. Problem Statement

Grafana raised a Dataload Alert for Petco (PTC/064) — GP Process Error on trading day 2026-08-24. The Azure DevOps pipeline run (build 816356) failed during the `load_ardm` task with a Greenplum `StringDataRightTruncation` error while inserting into `ardm_customer_stg`.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | c064ptc (dbt naming) / `ardm_064` (Greenplum schema) |
| ARDM version | Legacy pyardm (ARDM v1) — no SnowTime/dbt project exists for this client |
| Snowflake account | N/A — legacy Greenplum (dsprod1) |
| Active products | Legacy pyardm ETL (venv_svc\c064ptc\engage) |

## 4. Investigation

### 4.1 Pipeline log review

FAIL. Task `load_ardm` errored: `psycopg2.errors.StringDataRightTruncation: value too long for type character varying(100)` on `insert into ardm_customer_stg`.

### 4.2 Source script identification

POINT OF FAILURE FOUND. Traced the failing insert to `pyardm/us/c064ptc/ardm/sql/load_ardm_scripts/ardm_7_customer.sql` line 22 — `trim(firstname)||' '||trim(lastname) as CustomerFullName`, written into `customerfullname varchar(100)`. Concatenation of two varchar(100) fields has no truncation guard.

### 4.3 Root-cause data verification (Greenplum)

```sql
SET search_path TO 'ardm_064';
SELECT loyaltyid, firstname, lastname,
       length(trim(firstname)||' '||trim(lastname)) AS full_len
FROM ref_loyalty_db
WHERE length(trim(firstname)||' '||trim(lastname)) > 100
ORDER BY full_len DESC;
```

FAIL (confirms dirty data). Returned loyaltyid 710278564 — free-text grooming note stored in the `last_name` field (full_len = 105).

### 4.4 Source feed trace

FINDING. `first_name`/`last_name` load verbatim from the client's PSD_02Cust extract (tlog_064.ref_psd_02cust). Each individually fits varchar(100), so the loyalty load itself never fails — only the downstream concatenation overflows.

### 4.5 dbt/SnowTime scope check

PASS (scope confirmed). No dbt/SnowTime project exists for c064ptc — pure legacy pyardm/Greenplum pipeline on dsprod1.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | Insert into `ardm_customer_stg`, `CustomerFullName` column build in `ardm_7_customer.sql` |
| Why | `trim(firstname)||' '||trim(lastname)` concatenates two varchar(100) source fields with no length guard against the varchar(100) target column; a loyalty record with a free-text service note in `last_name` pushed the value to 105 characters, causing Greenplum to reject the entire insert |
| Scope | Trading day 2026-08-24, Petco (PTC/064) `load_ardm` task; at least 1 offending record; blocks the whole `ardm_customer_stg` batch load until fixed |
| Business impact | Dataload alert triggered; ARDM customer data for the affected trading day failed to process until re-run |
| Evidence | Pipeline log (build 816356); Greenplum verification query confirmed 1 row with full_len=105 |

## 7. Recommended Fix

### Option A — Code guardrail (Recommended, applied)

`left(trim(db.firstname)||' '||trim(db.lastname), 100) as CustomerFullName` in `ardm_7_customer.sql` line 22. Defensive fix — stops one dirty record from failing the whole batch. Ready on branch `dbuelvas/RTS-206639/c064ptc-customerfullname-truncation`, pending commit/PR and deploy to dsprod1 (legacy release process, not SnowTime dbt CI/CD).

### Option B — Source data correction

Notify Petco that the PSD_02Cust loyalty extract leaks free-text service notes into `last_name`. Client-side data-quality fix; recommended in parallel with Option A.

## 8. Open Questions

* Confirm with Petco whether the PSD_02Cust extract can be corrected.
* No open questions on the code fix itself.

## 9. Queries Run

| # | Query | Result |
| --- | --- | --- |
| 1 | length check on ref_loyalty_db concatenation > 100 | 1 row returned, full_len=105 (loyaltyid 710278564) |
