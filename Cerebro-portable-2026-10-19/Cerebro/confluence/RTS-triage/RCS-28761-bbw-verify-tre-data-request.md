---
ticket: RCS-28761
cliente: Bath & Body Works (BBWLP) / c081_bbw US, c281_bbc Canada
analista: Diego Buelvas
estado_ficha: Work in Progress
sintoma: piden reporte de returns, denials y overrides por tienda para dos rangos anuales
causa: el modulo Engage en SnowTime solo tiene datos desde 2026-07-13 en US y no esta habilitado en Canada, el rango pedido es anterior
fix: escalar a quien tenga acceso al portal legacy Verify/TRE, no hay fix de codigo
confluence_id: 478185324553
modificado: 2026-09-08
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478185324553
---

# RCS-28761 — BBW: Verify/TRE Data Request

Prepared: 08 September 2026 | Analyst: Diego Buelvas | Status: Work in Progress

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28761 |
| Customer | Bath & Body Works (BBWLP) |
| Issue Type | Incident |
| Priority | Medium |
| Status | Work in Progress |
| Opened | 03 September 2026 |
| Reporter | Keith Jablonski (kjablonski@bbw.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28761 |

## 2. Problem Statement

Reporter requests return, denial, and override data by store, for both US and Canada, across two date ranges: TY 08/03/25–08/01/26 and LY 08/04/24–08/02/25. Reporter states they cannot self-service pull this data for these ranges and have requested support for the same report before. Four example xlsx files (same target format: store_num, region, district, city, state, return/denial/override count+amount, override rate) were attached, dated September 2025 and authored by Marissa Johnson (Appriss Retail support, Verify/TRE portal access) and Keith Jablonski.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID (US) | c081_bbw |
| Client ID (Canada) | c281_bbc |
| ARDM Version | V2 (snowtimeV2) |
| Snowflake Schema (US) | ARDM_PRODUCTION.C081_BBW |
| Region | US |
| Active module (US) | Engage (Appriss Verify), engage_enabled: true, retailer id 81 |
| Active module (Canada) | None — Engage not enabled on c281_bbc |

## 4. Investigation

### 4.1 Source-of-truth identification

Query: Inspected the four attached xlsx files' embedded metadata (docProps/core.xml). Created by Marissa Johnson / Keith Jablonski, September 2025 — same column layout requested now.

FINDING. This report has historically been produced manually via the legacy Verify/TRE portal/database (not SnowTime/ARDM), by an Appriss support agent with direct portal access. Confirmed by RCS-28130 ("BBW - Verify/TRE Access", closed 2026-08-04), where Marissa Johnson is shown exporting user lists directly from the Verify/TRE US and Canada portals.

### 4.2 SnowTime Engage module coverage (US)

Query: Checked dbt/clients/us/c081_bbw/dbt_project.yml and models/engage_mapping.md: engage_enabled: true, feed documented as live since 2026-08-24. ardm_engageheader carries exactly the requested shape — one row per return, authorizationaction enum (denied=15, overridden=18, approved=12), storeno, totalreturnamount.

```sql
SELECT MIN(tradingday) AS min_td, MAX(tradingday) AS max_td, COUNT(*) AS row_cnt
FROM ARDM_PRODUCTION.C081_BBW.ARDM_ENGAGEHEADER
```

Result: min_td = 2026-07-13, max_td = 2026-09-08, 116,762 rows.

POINT OF FAILURE FOUND. Documented go-live (2026-08-24) is stale — actual data starts 2026-07-13. Either way, the requested ranges barely overlap: TY overlaps only 19 days out of 363 requested; LY has 0% overlap — the entire LY range predates any Engage data in SnowTime.

### 4.3 Canada coverage

Query: Checked dbt/clients/us/c281_bbc/dbt_project.yml: no engage_enabled var present.

FAIL. Canada has no Engage module enabled at all — zero return/denial/override data exists in ARDM for c281_bbc, for any date range.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | Nothing is broken — the requested data does not exist in SnowTime/ARDM for the requested date ranges |
| Why | SnowTime's Engage module (the ARDM mirror of Verify/TRE return-authorization data) only carries data from 2026-07-13 forward for c081_bbw (US), and is not enabled at all for c281_bbc (Canada). The requested ranges fall almost entirely before that coverage start |
| Scope | US: 19 of 363 requested TY days overlap SnowTime coverage; 0 of 363 LY days. Canada: 0% coverage for any date, any range |
| Business impact | Report cannot be produced from SnowTime/ARDM as requested; must be sourced from the legacy Verify/TRE portal/database the same way it was in September 2025 |
| Evidence | ARDM_PRODUCTION.C081_BBW.ARDM_ENGAGEHEADER MIN(tradingday)=2026-07-13, MAX(tradingday)=2026-09-08, 116,762 rows (queried 2026-09-08) |

## 6. Additional Findings

The Engage module go-live date documented in dbt/clients/us/c081_bbw/models/engage_mapping.md ("live since 2026-08-24") does not match the actual earliest data in production (2026-07-13). Not itself customer-impacting, relevant to any future coverage assessment for this client — verify against live Snowflake data rather than the doc when evaluating date-range feasibility.

## 7. Recommended Fix

### Option A — Escalate to Verify/TRE legacy reporting (Recommended)

This is a data-sourcing request, not a SnowTime/ARDM defect — there is no code or dbt fix possible; the requested historical range was never loaded into Snowflake by design (Engage only exists from its own go-live forward, no retroactive backfill path exists for pre-feed history). Escalate/reassign to whoever currently holds Verify/TRE portal or database access to run the report directly against the legacy system for both US and Canada, full requested ranges.

### Option B — Partial SnowTime extract (supplementary only)

For the small TY overlap window (07/13/26–08/01/26, US only), ardm_engageheader can be queried directly by store/authorizationaction to produce a partial return/denial/override breakdown. This does not cover Canada or the bulk of the requested range and should not be presented as a substitute for the full report.

## 8. Open Questions

* Who currently holds Verify/TRE legacy portal/database access to run this report for BBW US and Canada?
* Should Option B's partial SnowTime extract be delivered alongside the escalation, or held until the legacy-system report is available?

## 9. Queries Run

| # | Query | Target | Result |
| --- | --- | --- | --- |
| 1 | `SELECT MIN(tradingday), MAX(tradingday), COUNT(*) FROM ARDM_ENGAGEHEADER` | ARDM_PRODUCTION.C081_BBW (MCP snowflake-us) | min_td=2026-07-13, max_td=2026-09-08, 116,762 rows |

## 10. Extras / Additional Screenshots

4 attached xlsx files (TRE Overrides_{US,CAN} {TY,LY}) — used only for format/metadata inspection. [See Jira attachment / link in ticket]
