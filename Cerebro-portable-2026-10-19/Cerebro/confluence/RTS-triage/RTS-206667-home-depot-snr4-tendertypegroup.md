---
ticket: RTS-206667
cliente: Home Depot (THD / 085) / c085_thd
analista: Diego Buelvas
estado_ficha: Work in Progress
sintoma: 1 de 101 Work Items falla con invalid identifier T3.TENDERTYPEGROUP
causa: la migracion ARDM v1 a v2 renombro TenderTypeGroup a StdTenderTypeGrp y el catalogo de campos de Secure no se resincronizo
fix: escalar a Delivery como defecto agrupado de resync del catalogo, no parchar busqueda por busqueda
familia: rename de columnas ARDM v2 sin resync del catalogo
relacionados: RCS-28606, RTS-206610, RTS-206268
confluence_id: 478154752025
modificado: 2026-08-28
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478154752025
---

# RTS-206667 — Home Depot (THD/085): Failed Work Item — Same Name Refunds (SNR4) Invalid Identifier

Prepared: 28 August 2026 | Analyst: Diego Buelvas | Status: Work in Progress

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RTS-206667 |
| Customer | Home Depot (THD / 085) |
| Issue Type | Incident |
| Priority | Medium |
| Status | Work in Progress |
| Opened | 28 August 2026 |
| Reporter | svc rts (svc-rts@apprissretail.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RTS-206667 |

## 2. Problem Statement

Grafana Work Item alert fired for Home Depot (THD/085): 1 active Work Item alert. Of 101 scheduled Work Items, 100 completed successfully and 1 failed — "SNR4 - Same Name Refunds - Pro Xtra Name Match.fti" — with a NonRetryableException. Transaction dataload for trading day 2026-08-27 was confirmed complete (5,185,741 transactions); this is not a dataload issue.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | c085_thd |
| Region | US |
| ARDM Version | V2 (snowtimeBase + snowtimeV2) |
| Snowflake Schema | ARDM_PRODUCTION.C085_THD (output) / C085_THD_SNOWTIME (working) |
| Domain | 85_THD |

## 4. Investigation

### 4.1 Ops Overview check

PASS. Dataload complete (5,185,741 transactions); 100/101 Work Items completed; only 1 WI failed.

### 4.2 WI error detail

POINT OF FAILURE FOUND. `SearchAccessException` on VFP `/public/internal investigation lookups/- general searches/transactions by register all activities.search` — Snowflake `SQL compilation error: invalid identifier 'T3.TENDERTYPEGROUP'` at line 24, position 87.

### 4.3 Prior-incident pattern match

FINDING. Identical bug-class confirmed in 3 prior tickets:

* RCS-28606 (Williams Sonoma / c139_wil) — same exact field, `TENDERTYPEGROUP`.
* RTS-206610 (Floor&Decor / c058_fad) — `CustomerNumber` to `X_CUSTOMERNUMBER`.
* RTS-206268 (Kinney Drugs / c179_kny) — `POS_ARTICLEID` to `ARTICLEID`.

All four share the same root cause: an ARDM v1 to v2 column rename not resynced in Secure's search field catalog.

### 4.4 Snowflake schema confirmation

```sql
SELECT column_name FROM ARDM_PRODUCTION.INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'C085_THD' AND TABLE_NAME = 'ARDM_TENDER'
  AND COLUMN_NAME ILIKE '%TENDERTYPEGR%' ORDER BY column_name
```

FAIL (confirms hypothesis). Only `STDTENDERTYPEGRP` exists; `TENDERTYPEGROUP` does not exist.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | The search "transactions by register all activities.search" (linked to WI "SNR4 - Same Name Refunds - Pro Xtra Name Match") generates SQL referencing column `T3.TENDERTYPEGROUP`, which does not exist in the client's current ARDM schema. |
| Why | THD's SnowTime/ARDM v2 migration renamed `TenderTypeGroup` to `StdTenderTypeGrp`. Secure's Composer/search field catalog was not resynced to the new column name after migration — same defect class confirmed in 3 other clients. |
| Scope | 1 of 101 scheduled Work Items for THD; will keep failing on every future run until the catalog or the search definition is fixed. Confirmed bug-class impacts at least 4 clients across ARDM v2. |
| Business impact | The "Same Name Refunds" fraud-detection Work Item is non-functional for THD, blocking loss-prevention visibility into that refund pattern. |
| Evidence | Snowflake confirms `ARDM_TENDER` has `STDTENDERTYPEGRP`, not `TENDERTYPEGROUP` — identical break already documented for c139_wil (RCS-28606). |

## 7. Recommended Fix

### Option A — Escalate to Delivery as a grouped defect (Recommended)

Group with RCS-28606 / RTS-206610 / RTS-206268 / RTS-206667 as one defect: Secure's field catalog for clients migrated to SnowTime/ARDM v2 needs a resync mechanism for renamed columns, instead of four separate point patches. Delivery to assess a one-time metadata resync/fix across all impacted clients.

No Option B — Composer-side point fixes (re-adding/re-saving the search field) were attempted on this same bug-class in a prior ticket (RTS-206268) and did not hold; editing broadened the blast radius (3 to 11 failing) because the binding lives at a catalog level, not the individual search.

## 8. Open Questions

* Confirm final resolution once Delivery addresses the catalog resync — per-client re-point of the WI's search, or a global metadata migration?
* Confirm whether other clients beyond the 4 identified expose `StdTenderTypeGrp`-class renamed fields in searches/WIs that would also break.

## 9. Queries Run

| # | Query | Environment | Result |
| --- | --- | --- | --- |
| 1 | INFORMATION_SCHEMA.COLUMNS for C085_THD.ARDM_TENDER ILIKE '%TENDERTYPEGR%' | Snowflake (MCP snowflake-us) | Only `STDTENDERTYPEGRP` returned |

## 10. Extras / Additional Screenshots

Ops Overview screenshots and WI failure detail (NonRetryableException). [See Jira attachment / link in ticket]
