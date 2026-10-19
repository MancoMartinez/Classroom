---
ticket: RCS-28740
cliente: Wal-Mart / c300_wmt
analista: Diego Buelvas
estado_ficha: Work in Progress
sintoma: Spark Shopper Audit History muestra Passed, Failed y Bypassed en 0
causa: el display field Bypassed compara audit_interaction_status='Audit Bypassed' en vez de audit_item_outcome_details='Audit Items: Outcome Unknown', pierde el 97.4% de las filas
fix: corregir la expresion CASE en el composer, cambio de configuracion en Secure, ruta Delivery
confluence_id: 478185160730
modificado: 2026-09-08
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478185160730
---

# RCS-28740 — Wal-Mart: Spark Shopper Audit History Missing Results

Prepared: 08 September 2026 | Analyst: Diego Buelvas | Status: Work in Progress

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28740 |
| Customer | Wal-Mart |
| Issue Type | Incident |
| Priority | Medium |
| Status | Work in Progress |
| Opened | 03 September 2026 |
| Reporter | Steve Curry (james.curry@walmart.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28740 |

## 2. Problem Statement

Results show correctly in the "Spark Shopper History" search but not in the "Spark Shopper Audit History" search. For driver DEJABLU2168@GMAIL.COM at store 5155, all 5 result rows show Passed/Failed/Bypassed Audits = 0, despite the sister search showing real audit interaction data for the same trip IDs.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | c300_wmt |
| ARDM Version | V2 (snowtimeBase + snowtimeV2) |
| Snowflake schema | `ARDM_PRODUCTION.C300_WMT` (output) / `C300_WMT_SNOWTIME` (working) |
| Relevant table | OMNI_SPARK_SHOPPER_AUDIT (custom table, BigQuery source, pass-through mapping map_omni_spark_shopper_audit.sql) |

## 4. Investigation

### 4.1 Mapping model review

Query: Reviewed map_omni_spark_shopper_audit.sql — pure pass-through of pyardm ardm_300.omni_spark_shopper_audit.

PASS. Confirmed no data loss in the SnowTime mapping — only 3 categorical fields (audit_interaction_status, audit_item_outcome_details, was_finalized_removed) exist in source; no raw item-level pass/fail counts exist anywhere upstream (BigQuery or SnowTime).

### 4.2 Snowflake data verification for reported trips

Query: OMNI_SPARK_SHOPPER_AUDIT WHERE storenumber='5155' AND shopperid ILIKE '%DEJABLU2168%'.

All 5 reported trips show order_status='Pending', audit_item_outcome_details='Audit Items: Outcome Unknown'. No update since 2026-09-01.

### 4.3 Feed volume regression ruled out

Checked RCS-28792 (OMNI SPARK feed volume drop). That incident starts 2026-09-03; the 5 trips in this ticket were already stalled before that date. Not the same root cause.

### 4.4 Fleet-wide pattern check

Query: aggregate order_status='Pending' count across OMNI_SPARK_SHOPPER_AUDIT.

~15% (3.06M of 20.6M) of Pending rows carry no update for 14+ days — initially read as a generalized Walmart-side non-resolution pattern (pre-client-response hypothesis).

### 4.5 Client clarification (2026-09-08)

Walmart confirmed via email: audit_item_outcome_details = 'Audit Items: Outcome Unknown' is the Bypassed Audits state (not an unresolved/pending state), and order_status='Expired' (audit never conducted) should also be treated as Bypassed. This reframed the investigation — the data is a valid final state, not missing/stuck data.

### 4.6 Search composer definition review

Client supplied the composer-generated SQL for "Spark Shopper Audit History". The Bypassed Audits display field (Count_3) is computed as:

```sql
COUNT(CASE WHEN (T2.audit_interaction_status = 'Audit Bypassed') THEN 1 END) AS "Count_3"
```

while Passed/Failed correctly compare T2.audit_item_outcome_details against 'Audit Items: Passed' / 'Audit Items: Failed'.

POINT OF FAILURE FOUND. Bypassed Audits compares the wrong column/value.

### 4.7 Fleet-wide distribution validation

| audit_interaction_status | audit_item_outcome_details | Row count |
| --- | --- | --- |
| Audit Required | Outcome Unknown | 20,079,978 |
| Audit Bypassed | Outcome Unknown | 538,425 |
| Audit Required | Passed | 623,948 |
| Audit Required | Failed | 8,334 |
| Audit Bypassed | Passed | 11 |
| Audit Bypassed | Failed | 7 |

POINT OF FAILURE FOUND (confirmed). The search's Bypassed criterion only ever matches 538,425 of the 20,618,414 rows carrying an outcome value (2.6%) — it misses the 20,079,978 rows (97.4%) where the audit was genuinely bypassed but the interaction status still reads "Audit Required."

### 4.8 Screenshot cross-validation

Operator-supplied screenshots corroborate the Snowflake query results exactly, including one real example of audit_interaction_status='Audit Bypassed' confirming it is a rare/distinct value, not what applies to the reported trips.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | "Bypassed Audits" (Count_3) display field in the "Spark Shopper Audit History" search composer (Secure app, client c300_wmt) |
| Why | The backing CASE expression compares audit_interaction_status = 'Audit Bypassed' instead of audit_item_outcome_details = 'Audit Items: Outcome Unknown' — the column the client confirmed actually determines Bypassed status, mirroring the pattern already used correctly for Passed/Failed |
| Scope | Fleet-wide for c300_wmt — 20,079,978 of 20,618,414 outcome-bearing rows (97.4%) are undercounted as 0 Bypassed |
| Business impact | The search materially misrepresents store/driver Spark Shopper audit compliance |
| Evidence | Distribution table (4.7); example trip fa35b105-acb8-4758-bb1c-60608203481a / order 200015188659847 |

## 6. Additional Findings

None beyond the root cause above — the "no update in 14+ days" pattern noted in 4.4 is explained by 4.5 as expected Bypassed/Expired final states, not a separate defect.

## 7. Recommended Fix

### Option A — Correct the Bypassed Audits Count expression (Recommended)

```sql
COUNT(CASE WHEN (T2.audit_item_outcome_details = 'Audit Items: Outcome Unknown') THEN 1 END) AS "Count_3"
```

This is a search/composer configuration change in Secure (not SnowTime/dbt framework code) — route to Delivery, consistent with prior catalogue-mismatch escalations for this client base.

## 8. Open Questions

1. Should order_status='Expired' also be OR'd into the Bypassed criteria per the client's stated mapping, or does audit_item_outcome_details='Audit Items: Outcome Unknown' alone fully cover it?
2. Reply to Steve Curry (Walmart) confirming the diagnosis, using the example trip ID above.

## 9. Queries Run

| # | Query | Purpose | Result |
| --- | --- | --- | --- |
| 1 | DESCRIBE TABLE OMNI_SPARK_SHOPPER_AUDIT | Confirm actual column names | No driver_email column; located SHOPPERID |
| 2 | Trips for store 5155 / shopper DEJABLU2168 | Pull the 5 reported trips' current state | All order_status='Pending', outcome='Outcome Unknown' |
| 3 | GROUP BY audit_interaction_status, audit_item_outcome_details | Fleet-wide distribution | Confirmed 97.4% of Bypassed cases undercounted |

## 10. Extras / Additional Screenshots

Composer definition, results grid with zeros, and sister-search raw values for the same trip IDs. [See Jira attachment / link in ticket]
