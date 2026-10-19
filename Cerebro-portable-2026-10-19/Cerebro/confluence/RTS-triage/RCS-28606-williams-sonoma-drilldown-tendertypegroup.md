---
ticket: RCS-28606
cliente: Williams Sonoma / c139_wil
analista: Diego Buelvas
estado_ficha: Work in Progress
sintoma: el drill down falla con invalid identifier T2.TENDERTYPEGROUP
causa: la migracion ARDM v1 a v2 renombro TenderTypeGroup a StdTenderTypeGrp y el catalogo de campos de Secure no se resincronizo
fix: escalar a Engineering agrupado con RTS-206610 y RTS-206268 como un solo resync de metadata
familia: rename de columnas ARDM v2 sin resync del catalogo
relacionados: RTS-206610, RTS-206268, RTS-206667
confluence_id: 478151507983
modificado: 2026-08-27
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478151507983
---

# RCS-28606 — Williams Sonoma: Error Message on the Drill Down

Prepared: 27 August 2026 | Analyst: Diego Buelvas | Status: Work in Progress

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28606 |
| Customer | Williams Sonoma |
| Issue Type | Incident |
| Priority | Medium |
| Status | Work in Progress |
| Opened | 26 August 2026 |
| Reporter | Trish Chan (pchan@wsgc.com) |
| Assignee | Diego Buelvas |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28606 |

## 2. Problem Statement

User is able to run the "Emp Trans Tender Details - All Channels and Brands" report, but drill-down fails with a SQL compilation error. Confirmed affecting multiple users at the client.

Reported error:

```plaintext
Async search with ID '5f4419a4-ab95-4636-8061-3928c3da976a' was 'Failed'.
Error: SQL compilation error: error line 57 at position 87
invalid identifier 'T2.TENDERTYPEGROUP' SqlState: 42000, VendorCode: 904
QueryId: 01c6ad83-0109-6672-0001-20d2e048c5e2
```

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | c139_wil |
| Region | US |
| ARDM Version | v2 (snowtimeV2) |
| Snowflake Schema | ARDM_PRODUCTION.C139_WIL / C139_WIL_SNOWTIME |

## 4. Investigation

### 4.1 Client / ARDM version confirmation

PASS. Client project at `dbt/clients/us/c139_wil` — dependency confirms `snowtimeV2` framework (ARDM v2).

### 4.2 v1 to v2 rename check

FINDING. `dbt/docs/ARDMV2/ardm_v1_vs_v2.md` shows the field was renamed during the migration: `TenderTypeGroup` to `StdTenderTypeGrp`.

### 4.3 Live schema validation

```sql
SELECT COLUMN_NAME FROM ARDM_PRODUCTION.INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA='C139_WIL' AND TABLE_NAME='ARDM_TENDER' AND COLUMN_NAME ILIKE '%TENDERTYPEGR%'
```

POINT OF FAILURE FOUND. Only `STDTENDERTYPEGRP` exists. No column named `TENDERTYPEGROUP`.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | Drill-down SQL for "Emp Trans Tender Details" references `T2.TENDERTYPEGROUP`, a column name that no longer exists |
| Why | ARDM v1 to v2 migration renamed the physical column to `StdTenderTypeGrp`; Secure's search/drill-down field catalog was never resynced to the new name |
| Scope | All users of this drill-down for c139_wil; potentially any other search/WI referencing the legacy field name |
| Business impact | Drill-down fully broken (100% failure) — confirmed affecting multiple users |
| Evidence | ARDM_TENDER schema query returns only STDTENDERTYPEGRP |

## 6. Additional Findings

Same bug class as two prior tickets, both post-v1-to-v2-migration field catalog drift:

* RTS-206610 (Floor & Decor, c058_fad) — CustomerNumber to X_CUSTOMERNUMBER
* RTS-206268 (Kinney Drugs, c179_kny) — POS_ARTICLEID to ARTICLEID

In both prior cases the stale binding was not locatable in Snowflake, dbt, or the Secure git repo — it lives in backend field-catalog metadata (Platform DB) with no known resync mechanism after a SnowTime column rename.

## 7. Recommended Fix

### Option A — Escalate to Engineering (Recommended)

Update/resync the Secure field-catalog binding for "Tender Type Group" from legacy TenderTypeGroup to StdTenderTypeGrp for c139_wil's drill-down definition. Recommend Engineering group this with RTS-206610 and RTS-206268 as one metadata-resync fix rather than three point patches.

## 8. Open Questions

* Is the underlying field-catalog binding storage location known to Engineering? Not located in Snowflake, dbt, or the Secure repo in prior investigations (RTS-206268).
* Does this affect other ARDM v2 clients exposing StdTenderTypeGrp in their searches/WIs?

## 9. Queries Run

| # | Query | Result |
| --- | --- | --- |
| 1 | INFORMATION_SCHEMA.COLUMNS for C139_WIL.ARDM_TENDER ILIKE '%TENDERTYPEGR%' | Only STDTENDERTYPEGRP returned |

## 10. Extras / Additional Screenshots

Error screenshots. [See Jira attachment / link in ticket]
