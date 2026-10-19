---
ticket: RCS-28873
cliente: Starbucks Coffee Company (NA) / c166_sbx
analista: Sebastian Rueda
estado_ficha: Work in Progress
sintoma: varias busquedas dan "Sorry but we couldn't process your search" y Transaction Viewer lento
causa: catalogo de campos de Secure desincronizado del esquema fisico de Snowflake (X_STOREMANAGER inexistente, cast numerico en MemberID)
fix: resync del catalogo en secure.Repo, escalacion a Delivery
confluence_id: 478194466827
modificado: 2026-09-10
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478194466827
---

# RCS-28873 — Starbucks Coffee Company (NA): Multiple Searches Showing Error Message, General Slowness in Search Results

Prepared: 10 September 2026 | Analyst: Sebastian Rueda | Status: Work in Progress

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28873 |
| Customer | Starbucks Coffee Company (NA) |
| Issue Type | Incident |
| Priority | High |
| Status | Work in Progress |
| Opened | 10 September 2026 |
| Reporter | Nancy Sciascia (nsciasci@starbucks.com) |
| Assignee | Sebastian Rueda (srueda@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28873 |

## 2. Problem Statement

In addition to Star Rewards searches, the Store Details search shows an error message ("Sorry but we couldn't process your search"), and Transaction Viewer is loading very slowly. Multiple searches appear to be impacted.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | c166_sbx (US) |
| ARDM version | N/A — not on SnowTime; legacy pyardm |
| Snowflake schema | ARDMPROD.ARDM_166 |
| Active products | Secure search/reporting; no SnowTime cutover |

## 4. Investigation

### 4.1 Error log analysis

Query: Reviewed error logs supplied by operator.

**POINT OF FAILURE FOUND.** Two distinct Snowflake errors: `invalid identifier 'T2.X_STOREMANAGER'` (SQL compilation, 42000) and `Numeric value '1931449134107160' is not recognized` (22018/100038).

### 4.2 Client cutover status check

Query: Checked prior-ticket memory for c166_sbx cutover status.

**PASS.** Confirmed c166_sbx has no SnowTime cutover — exists only in `ARDM_LAB_PRODUCTION` (lab, no real build). Live app reads legacy `ARDMPROD.ARDM_166`.

### 4.3 Physical column verification — STOREMANAGER

```sql
SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE
FROM ARDMPROD.INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA='ARDM_166' AND COLUMN_NAME ILIKE '%STOREMANAGER%'
```

**POINT OF FAILURE FOUND.** Column exists as `REFERENCE_LOCATION_EXT.STOREMANAGER` (TEXT), with no `X_` prefix. The Store Details search generates SQL referencing `T2.X_STOREMANAGER`, which does not exist — direct cause of the "invalid identifier" error.

### 4.4 Physical column verification — MEMBERID

```sql
SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE, NUMERIC_PRECISION, NUMERIC_SCALE
FROM ARDMPROD.INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA='ARDM_166' AND COLUMN_NAME ILIKE '%MEMBERID%'
```

**PASS** (rules out physical column as cause). `ARDM_LOYALTYCARD_EXT.MEMBERID` and `ARDM_ITEMDISCOUNT_EXT.MEMBERID` are both `NUMBER(38,0)` — ample precision for the reported 16-digit value. The overflow error is not a physical-column limitation; it points to an implicit cast to a lower-precision NUMBER elsewhere in the search/parameter definition.

### 4.5 Storage migration timing check

```sql
SELECT TABLE_NAME, CREATED, LAST_ALTERED, ROW_COUNT, BYTES
FROM ARDMPROD.INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA='ARDM_166'
  AND TABLE_NAME IN ('ARDM_LOYALTYCARD_EXT','REFERENCE_LOCATION_EXT','ARDM_HEADER','ARDM_HEADER_EXT')
```

**PASS** (rules out recent migration). All relevant tables `CREATED` 2024-04-26 — the Greenplum to Snowflake storage move is not recent. `LAST_ALTERED` 2026-08-27/28 reflects normal daily load activity, not a schema migration event.

### 4.6 Secure catalog / git trace

Query: Searched Secure repository git history and code for `X_STOREMANAGER`, `X_MEMBERID`, and recent commits touching c166/sbx.

No matches found. Confirms these field/search definitions are user/system-authored in `secure.Repo` (Platform DB, SQL Server), not git-tracked.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | Multiple Secure searches for c166_sbx (Store Details, Star Rewards MemberID search/drilldown, Transaction Viewer) failing or degraded |
| Why | Secure's field catalog/search definitions reference field names and casts that no longer match the physical Snowflake schema of legacy `ARDMPROD.ARDM_166` — an `X_`-prefixed field name (`X_STOREMANAGER`) with no physical `X_` prefix (`STOREMANAGER`), plus a numeric cast/precision issue on the MemberID parameter. Catalog-desync bug-class, not a data or migration issue — storage has been stable since 2024-04-26 |
| Scope | c166_sbx (Starbucks NA). Related RCS-28848 (opened one day earlier, same client) reports the same failure class |
| Business impact | Multiple customer-facing searches broken/degraded; general search slowness (Transaction Viewer) |
| Evidence | `REFERENCE_LOCATION_EXT.STOREMANAGER` confirmed with no `X_` prefix; `MEMBERID` columns confirmed `NUMBER(38,0)`; table `CREATED` timestamps rule out a recent migration |

## 6. Additional Findings

RCS-28848 (opened 2026-09-09, same client) reports: Star Reward Transaction MemberID search failing with the same error class, "2-Stars Accrued by MemberID" drilldown failing, and Star accrual/redemption data missing retroactively from previously-correct transactions. Ticket reassigned to the same reviewer (Sebastian Rueda) as likely related root cause.

## 7. Recommended Fix

### Option A — Secure field catalog resync (Recommended)

Locate the Secure Platform DB (`secure.Repo`, SQL Server) definitions for the affected searches (Store Details field catalog / extension mapping for Reference_Location_Ext; Star Rewards MemberID search parameter). Confirm the declared field mapping/cast against the actual Snowflake physical schema and correct the mismatch (remove erroneous `X_` prefix mapping for StoreManager; fix MemberID parameter precision/cast). Requires access to Secure's Platform DB (SQL Server) — not available from the SnowTime/Snowflake tooling used in this investigation.

Escalation note: this bug-class (Secure field catalog desynced from the physical schema) is owned by Delivery, not Engineering, per prior precedent — recommend escalating there once the SQL Server-side confirmation is done.

## 8. Open Questions

* Confirm via `secure.Repo` lookup the exact declared mapping for `X_STOREMANAGER` and the MemberID parameter precision (needs SQL Server / Platform DB access).
* Confirm whether RCS-28848's "stars missing retroactively" symptom shares the same root cause or is a separate data issue.
* Confirm escalation target (Delivery) once catalog mismatch is verified.

## 9. Queries Run

| # | Query | Environment | Result |
| --- | --- | --- | --- |
| 1 | `... COLUMN_NAME ILIKE '%STOREMANAGER%'` | Snowflake (ARDMPROD, US) | `REFERENCE_LOCATION_EXT.STOREMANAGER`, TEXT — no `X_` prefix |
| 2 | `... COLUMN_NAME ILIKE '%MEMBERID%'` | Snowflake (ARDMPROD, US) | `ARDM_LOYALTYCARD_EXT.MEMBERID` / `ARDM_ITEMDISCOUNT_EXT.MEMBERID`, both `NUMBER(38,0)` |
| 3 | `... INFORMATION_SCHEMA.TABLES ... CREATED, LAST_ALTERED` | Snowflake (ARDMPROD, US) | All 4 tables `CREATED` 2024-04-26; `LAST_ALTERED` 2026-08-27/28 (routine daily load) |

## 10. Extras / Additional Screenshots

Error screenshot: "Sorry but we couldn't process your search", tracking code `53539c20-9a49-57d2-ba5a-169d447f526a` — [See Jira attachment / link in ticket]. Local copy: `image-20260910-170034.png`.
