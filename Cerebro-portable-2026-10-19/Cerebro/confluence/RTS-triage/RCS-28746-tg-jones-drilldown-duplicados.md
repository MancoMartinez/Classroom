---
ticket: RCS-28746
cliente: TG Jones / c438_tgj (EU)
analista: Diego Buelvas
estado_ficha: Work in Progress
sintoma: drill down desde el dashboard sale en blanco, y desde la busqueda directa devuelve filas duplicadas
causa: dos defectos distintos, join a ARDM_TENDER 1:N sin proteccion anti cartesiana, y la URL de drill down se completa con el query string de la pagina actual que el dashboard hash-routed no tiene
fix: proteccion anti cartesiana en el generador SQL, y sacar el contexto de la busqueda sin depender de window.location.search
relacionados: RCS-28730, RCS-28691, RCS-28320, RCS-28436
confluence_id: 478183260163
modificado: 2026-09-07
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478183260163
---

# RCS-28746 — TG Jones: Drill down option - greyed out

Prepared: 07 September 2026 | Analyst: Diego Buelvas | Status: Work in Progress

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28746 |
| Customer | TG Jones |
| Issue Type | Incident |
| Priority | Medium |
| Status | Work in Progress |
| Opened | 03 September 2026 |
| Reporter | Jeanette Birchall |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28746 |

## 2. Problem Statement

The ticket title ("Drill down option - greyed out") does not match the actual content. The body is a forwarded email thread describing two distinct symptoms on the "Large Value Transactions" dashboard and the SNIPER dashboard:

1. Drilling down from a dashboard tile shows a blank screen.
2. Drilling down from the underlying search question directly works, but returns duplicated/inflated results (54 rows instead of 13; expected 10 unique items but shows inflated totals).

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | c438_tgj |
| Region | EU |
| ARDM Version | V3 (confirmed via ARDM_TENDER schema: TYPE, EXTRA_FIELDS, ORDER_ID columns) |
| Snowflake | `ARDM_PRODUCTION.C438_TGJ` |

## 4. Investigation

### 4.1 Ticket content review

POINT OF FAILURE FOUND. Title reflects only one symptom ("greyed out"); the real content describes two independent bugs (blank drill-down from dashboard + duplicate rows on direct drill-down).

### 4.2 Similar-ticket search

FINDING. Symptom 1 (blank drill-down from dashboard) is not unique to TG Jones — identical behavior reported in RCS-28730 (Kroger, 2026-09-02) and RCS-28691 (Fraser Group, 2026-09-01), both still open, Engineering reproduced but no root cause confirmed as of ticket dates. Symptom 2 (duplicates) matches the bug-class in RCS-28320 (TJX, WIP — anti-cartesian join breaks on adding a joined-table field) and RCS-28436 (Alshaya, resolved — different root cause: ambiguous reference_tendertype across feeds).

### 4.3 Snowflake data validation

Query: Resolved TransactionID via ARDM_HEADER (Store 3292, TradingDay 2026-09-01, TicketNo 902981), then queried ARDM_TENDER for that TransactionID.

PASS — data is correct. Found exactly 2 legitimate rows: cash tendered (61.00) and cash change (-0.48, CHANGE_FLAG=true). No duplicate data in ARDM.

### 4.4 Secure code trace — blank drill-down (Symptom 1)

Query: Traced the shared drill-down pipeline used by both Composer and Dashboard grids — data-grid.component.js + data-grid-helper.service.js (repo Secure).

HYPOTHESIS FOUND — not yet confirmed via browser devtools. Track type 1 (drilldown, target _self) does a full navigation: window.location.href = encodedUrl (data-grid.component.js:481-493) — not an SPA-routing bug. The URL is built in hydrateTrackUrl (data-grid-helper.service.js:188-201): when the track template contains @urlParams, it completes the URL via WebService.buildHrefUsingCurrentQueryString(trackUrl), which reads window.location.search of the CURRENT page. Composer/Explorer runs top-level and carries its filter context in the ?query string; dashboards route via #hash, so when the same search is embedded in a dashboard, window.location.search may be empty or missing the params Composer needs (folder, dataArea, avfp, filters) — the resulting drill URL is incomplete, producing a blank results screen. Running the search directly from Explorer works because those params ARE present in that page's real query string. This also explains why removing/re-adding the search (tried by Vlad Bogus on RCS-28730) did not fix it — the saved search isn't the problem, the origin page's query string is.

Still needed to confirm: compare the actual drill-down URL generated on click from a dashboard tile vs. from Composer directly (Network tab), for the same search, and diff the missing parameter(s).

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | Search "Large Value or Quantity Transactions" duplicates every result row when the "TGJ Tender Type" column is added |
| Why | The search joins ARDM_TENDER (1:N per transaction) via the Tender Type column without anti-cartesian aggregation. Since a transaction legitimately has 2 tender rows (cash tendered + cash change), every detail row fans out x2. Same code pattern as RCS-28320 (Secure SQL generator, AntiCartesianDataSetMode) — not an ARDM/SnowTime data issue |
| Scope | TG Jones (c438_tgj) — confirmed on "Large Value or Quantity Transactions"; SNIPER dashboard reported with same symptom, not yet independently validated |
| Business impact | Analysts see inflated/misleading transaction counts on drill-down, undermining confidence in dashboard results |
| Evidence | ARDM_TENDER for TransactionID 2609019821792495050: 2 real rows vs. 54 rows returned by the search after column addition |

## 6. Additional Findings

Symptom 1 (blank drill-down from dashboard tile, works fine when the same search is run directly) is a separate, cross-client defect affecting RCS-28730 (Kroger) and RCS-28691 (Fraser Group) as well, both still open with Engineering. Code trace (4.4) points to a likely cause. Recommend linking RCS-28746 to RCS-28730/RCS-28691 and handing Engineering this lead instead of 3 parallel investigations.

## 7. Recommended Fix

### Option A — Fix search/SQL generator join (Recommended, for duplicates)

Engineering to add anti-cartesian protection (or proper aggregation) when a Tender-table field is added to a search that already returns transaction/item-level rows. Same code area as RCS-28320: Secure/Sources/Core/Core/Data Providers/Sql/Generator/, AntiCartesianDataSetMode.

### Option B — Validate and fix blank drill-down query-string context loss (for symptom 1)

Engineering to compare the drill-down URL generated on click from a dashboard tile vs. Composer directly (Network tab) for the same search, confirming whether hydrateTrackUrl / WebService.buildHrefUsingCurrentQueryString (data-grid-helper.service.js:188-201) is dropping required params when the origin page is hash-routed. If confirmed, the fix is to source the search's own context independently of window.location.search. Link RCS-28746 to RCS-28730 and RCS-28691 so Engineering treats it as one cross-client defect.

## 8. Open Questions

* Blank-screen drill-down (symptom 1): code trace points to a query-string-context hypothesis but it is NOT yet confirmed via live browser devtools — still open with Engineering (tracked in RCS-28730 / RCS-28691).
* Whether the SNIPER dashboard duplicate-rows report shares the exact same Tender-join root cause has not been independently validated in Snowflake.

## 9. Queries Run

| # | Query | Result |
| --- | --- | --- |
| 1 | ARDM_HEADER WHERE STORENO=3292 AND TRADINGDAY='2026-09-01' AND TICKETNO=902981 | PASS — resolved TransactionID 2609019821792495050 |
| 2 | ARDM_TENDER WHERE TRANSACTIONID=2609019821792495050 AND TRADINGDAY='2026-09-01' ORDER BY RECORDSEQNO | POINT OF FAILURE FOUND — 2 legitimate rows; data correct, root cause is search-join design |

## 10. Extras / Additional Screenshots

8 screenshots attached to the ticket (dashboard tile, blank drill-down screen, Composer transaction detail with 27/54 duplicated item rows, SNIPER dashboard, Explorer search library path). [See Jira attachment / link in ticket]
