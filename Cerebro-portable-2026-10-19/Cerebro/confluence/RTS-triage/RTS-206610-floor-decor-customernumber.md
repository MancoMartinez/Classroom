---
ticket: RTS-206610
cliente: Floor & Decor (FAD / client 058) / c058_fad
analista: Diego Buelvas
estado_ficha: Work in Progress
sintoma: dos Work Items fallan con invalid identifier T1.CUSTOMERNUMBER
causa: en la migracion a ARDM v2 el campo se reclasifico como extension x_customernumber y el binding del catalogo de Secure quedo apuntando al nombre viejo
fix: corregir el binding del catalogo, no se puede desde el Composer porque la llave del join no esta expuesta
familia: rename de columnas ARDM v2 sin resync del catalogo
relacionados: RTS-206268, RCS-28606, RTS-206667
confluence_id: 478151180290
modificado: 2026-08-27
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478151180290
---

# RTS-206610 — Floor&Decor: Failed Work Items — CustomerNumber Invalid Identifier

Prepared: 27 August 2026 | Analyst: Diego Buelvas | Status: Work in Progress

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RTS-206610 |
| Customer | Floor & Decor (FAD / client 058) |
| Issue Type | Incident |
| Priority | Medium |
| Status | Work in Progress |
| Opened | 27 August 2026 |
| Reporter | svc rts (svc-rts@apprissretail.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RTS-206610 |

## 2. Problem Statement

Grafana Work Item Alert fired for Floor&Decor (FAD/058): 1 active alert — "[WI] FAD – Failed Work Items". Two Work Items are failing during scheduled run with a SQL compilation error referencing an invalid identifier tied to the `CustomerNumber` field.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | 058 (c058_fad) |
| Region | US |
| ARDM Version | v2 (SnowTime) |
| Snowflake Schema | `ARDM_PRODUCTION.C058_FAD` |
| Active Products | Secure (Work Items / Instant Analytics), SnowTime pipeline |

## 4. Investigation

### 4.1 Ops overview triage

FAIL. 69,983 transactions loaded successfully; 19 of 21 Work Items completed; 2 failed. WI 238 "/system/ebr/instant analytics/definitions/customer name match cashier name.fti" errored with:

```sql
SQL compilation error: error line 10 at position 5 invalid identifier 'T1.CUSTOMERNUMBER'
SqlState: 42000, VendorCode: 904
```

### 4.2 Column existence check (Snowflake)

POINT OF FAILURE FOUND. `ARDM_HEADER` has no `CUSTOMERNUMBER` column. Only `X_CUSTOMERNUMBER` exists. `ARDM_CUSTOMER` has no equivalent field either.

### 4.3 dbt mapping cross-check

PASS (confirms root cause). The legacy pyardm field `ARDM_90:1042 CustomerNumber` (standard in ARDM v1) is not a standard ARDM v2 field. SnowTime intentionally remapped it as client extension `x_customernumber` during the FAD migration (map_ardm_header.sql:183, ArdmProdParity.md:144) — by design, not a mapping bug.

### 4.4 Search Composer review

POINT OF FAILURE FOUND. The "Customer Name" (CLIENT EXT) field used in Conditions drives an implicit JOIN `ardm_Header.CustomerNumber = reference_client.CUST_POS_NBR`. This join key is not exposed anywhere in the Composer UI — not fixable by the operator via UI.

### 4.5 Secure repository code search

FAIL (negative result). No hardcoded binding found in versioned code. The field-catalog binding is resolved via backend metadata/config not reachable from Snowflake, dbt, or the Secure repo.

### 4.6 Second Work Item correlation

POINT OF FAILURE FOUND. A second failing WI shows the same SQL error, containing a condition literally named "Customer Number". Raises the hypothesis from a single search's implicit JOIN to a field-catalog-level defect.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | Two Secure Work Items for FAD fail with invalid identifier 'CUSTOMERNUMBER' |
| Why | Both reference a Secure field-catalog entry bound to the legacy column name CustomerNumber. When FAD migrated from pyardm (ARDM v1) to SnowTime (ARDM v2), the field was reclassified as a client-specific extension and renamed X_CUSTOMERNUMBER. The Secure field-catalog binding was never updated to match |
| Scope | Confirmed on 2 Work Items for FAD; binding appears catalog-level rather than WI-specific, so other searches/WIs referencing this field may also be exposed |
| Business impact | Failed Work Items block automated EBR case generation for the "customer name matches cashier name" refund-fraud pattern; 2 of 21 WI runs failing for trading day 2026-08-26; triggered Grafana L1 to TSOC escalation chain |
| Evidence | Snowflake: ARDM_HEADER has X_CUSTOMERNUMBER, no CUSTOMERNUMBER. dbt confirms intentional v1 to v2 rename |

## 6. Additional Findings

The backend source of the field-catalog binding could not be located in Snowflake, dbt, or the Secure repository — it lives in metadata/config not reachable with the tools available to this investigation. Same class of unresolved-binding-source issue previously seen on RTS-206268 (KNY, POS_ARTICLEID invalid identifier).

## 7. Recommended Fix

### Option A — Escalate to Engineering (Recommended)

Correct the Secure field-catalog binding for the "Customer Number" / "Customer Name" (CLIENT EXT) field for FAD so it resolves to X_CUSTOMERNUMBER instead of the legacy CustomerNumber column. Audit other ARDM v2-migrated clients where this field was similarly remapped to an x_ extension. Not fixable via Search Composer UI.

## 8. Open Questions

* Confirm the field type of the second failing WI's "Customer Number" condition (HEADER standard vs CLIENT EXT).
* Determine full blast radius across FAD and other ARDM v2 clients.
* Locate the actual backend metadata source of the field binding — requires Engineering with backend/DB access.

## 9. Queries Run

| # | Query | Source | Result |
| --- | --- | --- | --- |
| 1 | INFORMATION_SCHEMA.COLUMNS for C058_FAD ARDM_HEADER/ARDM_CUSTOMER | Snowflake MCP (snowflake-us) | X_CUSTOMERNUMBER exists; no CUSTOMERNUMBER |
| 2 | Grep customernumber across dbt/clients/us/c058_fad | Local repo search | Extension x_customernumber, intentional rename |
| 3 | Grep CUST_POS_NBR / CustomerNumber / ClientExt across Secure repo | Local repo search | No hardcoded binding in versioned code |

## 10. Extras / Additional Screenshots

Search definition screenshot confirming no exposed join-key field. [See Jira attachment / link in ticket]
