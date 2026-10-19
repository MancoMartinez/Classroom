---
ticket: RCS-28077
cliente: AHL / Ahold Delhaize USA (ADUSA) / c112_ahl legacy ARDM_112
analista: Diego Buelvas
estado_ficha: WORK IN PROGRESS
sintoma: el drill down de las busquedas de refund repite cada fila 6 veces, la tabla agregada esta bien
causa: el pipeline pyardm corrio 6 veces el 2026-07-30 entre 23:07 y 23:10 UTC e inserto todos los productos sin UPSERT ni constraint unico, REFERENCE_PRODUCT quedo con 6 filas por ArticleID y el join del query expandido multiplica
fix: borrar las 6,945,460 filas duplicadas dejando la mas reciente por ArticleID, y agregar MERGE o constraint unico
nota_reutilizable: si el agregado esta bien y el expandido duplica, comparar los dos SQL generados y buscar el join extra
confluence_id: 478142332933
modificado: 2026-08-25
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478142332933
---

# RCS-28077 — AHL (Ahold Delhaize USA): Refund Searches Are Broken

Prepared: 31 July 2026 | Analyst: Diego Buelvas | Status: WORK IN PROGRESS

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28077 |
| Customer | AHL / Ahold Delhaize USA (ADUSA) |
| Issue Type | Incident |
| Priority | High |
| Status | Work in Progress |
| Opened | 30 July 2026 |
| Reporter | Jacquelyn Wunders (jacquelyn.wunders@adusa.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28077 |

## 2. Problem Statement

Client reported that refund searches in Secure display multiple identical rows for each transaction in the expanded (drill-down) view. The aggregate results table works correctly. Client described the effect as "cartesian" — the number of duplicate rows correlates with item-based conditions in the search. Issue started July 30, 2026. Only refund searches are affected.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | `c112_ahl` |
| Snowflake Schema (legacy) | `ARDMPROD.ARDM_112` |
| ARDM Version | Legacy pyardm (SnowTime project exists at dbt/clients/us/c112_ahl but not yet live) |
| Affected Feature | Expanded / drill-down view in Refund Searches |

## 4. Investigation

### 4.1 Aggregate vs. expanded query comparison

POINT OF FAILURE FOUND. The expanded query contains an additional JOIN not present in the aggregate query:

```
LEFT JOIN reference_product AS T3 ON (T2.ArticleID = T3.ArticleID)
```

If reference_product contains N rows for the same ArticleID, the expanded query produces N identical rows per ardm_item row.

### 4.2 Discarded hypotheses

PASS — all discarded.

* UNION ALL in generated SQL: query uses a single LEFT JOIN.
* Hierarchy UDF duplicating LocationIDs: source ends with SELECT DISTINCT LOCATIONID.
* Duplicates in ardm_item: only 1 row passes the filters for the test transaction.
* Duplicates in reference_location: 839 rows, 0 duplicates.
* ENG-6514 LHUA contamination: affected user has exactly 1 LHUA row, no cross-brand contamination.

### 4.3 reference_product row count for ArticleID = '43'

POINT OF FAILURE FOUND. CNT = 6. All 6 rows share the same ReceiptDescription and all other fields are identical. Only INSERTEDDATETIME differs.

### 4.4 Content of the 6 duplicate rows

POINT OF FAILURE FOUND. INSERTEDDATETIME values between 2026-07-30 23:07:45 and 23:10:50 UTC — 6 inserts within ~3 minutes on the same day the bug started. The pyardm pipeline ran 6 times and inserted all products without UPSERT logic or a UNIQUE constraint on ArticleID.

### 4.5 Total scope of duplicates in reference_product

POINT OF FAILURE FOUND. 8,334,552 total rows / 1,389,092 unique ArticleIDs = exact 6x factor across 100% of products. Duplicate rows: 6,945,460.

### 4.6 reference_location integrity check

PASS. 839 total rows, 839 unique, 0 duplicates. Issue is exclusive to reference_product.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | `ARDMPROD.ARDM_112.REFERENCE_PRODUCT` — 6 duplicate rows for every ArticleID |
| Why | The AHL pyardm pipeline executed 6 times on 2026-07-30 between 23:07–23:10 UTC. Each run performed a plain INSERT of all products with no UPSERT logic and no UNIQUE constraint on ArticleID. |
| Scope | Start: 2026-07-30. Entire table affected: 100% of 1,389,092 ArticleIDs. |
| Business impact | Every refund search expanded view returns 6x duplicate rows. The aggregate results table is unaffected. |
| Evidence | 8,334,552 rows / 1,389,092 unique = exact 6x factor. Duplicate INSERTEDDATETIME values all on 2026-07-30 UTC. reference_location: 0 duplicates. |

## 7. Recommended Fix

### Option A — Data cleanup in ARDMPROD (Delivery/Ops — Immediate)

Delete the 6,945,460 duplicate rows from REFERENCE_PRODUCT, keeping the row with the latest INSERTEDDATETIME per ArticleID.

```
-- Pre-flight check (expected: 6,945,460)
SELECT COUNT(*) FROM ARDMPROD.ARDM_112.REFERENCE_PRODUCT
WHERE INSERTEDDATETIME NOT IN (
    SELECT MAX(INSERTEDDATETIME)
    FROM ARDMPROD.ARDM_112.REFERENCE_PRODUCT
    GROUP BY ArticleID
);
-- DELETE — requires write access to ARDMPROD and DBA approval
DELETE FROM ARDMPROD.ARDM_112.REFERENCE_PRODUCT
WHERE INSERTEDDATETIME NOT IN (
    SELECT MAX(INSERTEDDATETIME)
    FROM ARDMPROD.ARDM_112.REFERENCE_PRODUCT
    GROUP BY ArticleID
);
```

### Option B — Investigate and fix the pyardm pipeline (Engineering — Root cause)

Determine why the pipeline ran 6 times within ~3 minutes. Add a UNIQUE constraint or MERGE/UPSERT logic on ArticleID. Note: if AHL migrates to SnowTime, this issue disappears — SnowTime uses reference_merge with an idempotent MERGE.

## 8. Open Questions

1. What process or job triggered the AHL pyardm pipeline 6 times on 2026-07-30?
2. What is the AHL migration roadmap to SnowTime?

## 9. Queries Run

| # | Description | Key Result |
| --- | --- | --- |
| 1 | Row count for ArticleID='43' | CNT = 6 |
| 2 | Field diff across the 6 duplicate rows | Only INSERTEDDATETIME differs |
| 3 | Full content of the 6 rows | INSERTEDDATETIME 23:07–23:10 UTC, 2026-07-30 |
| 4 | Total duplicate scope | 8,334,552 total / 1,389,092 unique / 6,945,460 duplicates |
| 5 | reference_location integrity check | 839 rows, 0 duplicates |
| 6 | LHUA row for affected user | 1 row, no cross-brand contamination |

## 10. Screenshots

Refund search with duplicate rows, receipt vs. results comparison, and a working item-based search for reference. [See Jira attachment]
