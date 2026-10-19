---
ticket: RCS-28725
cliente: WinCo Foods LLC / c124_wco
analista: Diego Buelvas
estado_ficha: Work in Progress, escalado a Engineering
sintoma: los items con isRefused=true restan del conteo de items y muestran precio original en vez de 0.00
causa: map_ardm_item.sql hace OR de isRefused con has_voiding_child en voidedflg, herencia literal del pyardm legacy ARDM_20_Item.sql
fix: desacoplar isRefused de voidedflg y numberofitems, y poner en cero los campos monetarios
familia: mapeo heredado de pyardm
confluence_id: 478182146343
modificado: 2026-09-07
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478182146343
---

# RCS-28725 — WinCo Foods LLC: "isRefused" flag

Prepared: 07 September 2026 | Analyst: Diego Buelvas | Status: Work in Progress

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28725 |
| Customer | WinCo Foods LLC |
| Issue Type | Incident |
| Priority | Medium |
| Status | Work in Progress |
| Opened | 02 September 2026 |
| Reporter | Sarah Widdison (sarah.widdison@wincofoods.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28725 |

## 2. Problem Statement

Client requests that items with isRefused=true be shown as $0.00 on receipts. Additionally, refused items are being subtracted from the total item sale count on some transactions: TRX 1051 (Store 25, Surfside) — item(s) marked isRefused=true, count should show 14, shows 13; TRX 6889 (Store 75) — 5 items (Modelos) marked isRefused=true, item count should show 8, shows 3.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | c124_wco |
| Region | US |
| Snowflake schema | ARDM_PRODUCTION.C124_WCO |
| Source feed | Emerald JSON (NCR Emerald POS) |
| ARDM version | NOT AVAILABLE — inferred v2 (snowtimeV2-style model naming), not explicitly confirmed |

## 4. Investigation

### 4.1 Raw TLOG field inspection

PASS. Confirmed isVoided and isRefused are independent boolean flags in the source (isVoided: false, isRefused: true, refusalInfo.refusalType: "BRM").

### 4.2 Mapping code review — map_ardm_item.sql

POINT OF FAILURE FOUND. isRefused is OR'd with has_voiding_child into voidedflg, and also flips the sign of numberofitems — treating refused items as voids. Inherited verbatim from legacy pyardm ARDM_20_Item.sql (line 55 + post-update 181-182), not an intentional design decision for this business case. (emerald_final CTE, dbt/clients/us/c124_wco/models/mapping/map_ardm_item.sql, ~lines 260-269, ~320.)

### 4.3 Downstream count validation

FINDING. ARDM_HEADER.numberofitems (COUNT DISTINCT articleid, non-voided) already returns the correct value (8, 14). The broken field is totalitemsalecount, which excludes refused items because voidedflg=TRUE is set for them.

### 4.4 Client confirmation of desired behavior

PASS. Client confirmed (2026-09-07): (a) refused items must still count toward total item count; (b) always show $0.00 regardless of original price; (c) no distinction by refusalType (e.g. BRM) — all isRefused=true items behave identically.

## 5. Root Cause Statement

| What broke | map_ardm_item.sql (c124_wco, emerald_final CTE) treats isRefused as equivalent to isVoided |
| --- | --- |
| Why | Mapping logic copied 1:1 from legacy pyardm ARDM_20_Item.sql, which conflates isVoided/isRefused. In the source tlog these are independent flags; the fusion was inherited, not intentional |
| Scope | All Emerald-source transactions at WinCo (c124_wco) carrying isRefused=true items — a mapping-level bug, not isolated to the two sampled transactions |
| Business impact | Item sale count under-reports on receipts/audit tooling whenever refused items are present; refused items also display their original charged price instead of $0.00 |
| Evidence | TRX 6889: item count shows 3, should show 8 (5 isRefused items). TRX 1051: item count shows 13, should show 14 |

## 7. Recommended Fix

### Option A — Decouple isRefused from voidedflg/numberofitems (Recommended)

In map_ardm_item.sql, emerald_final CTE:

1. voidedflg = has_voiding_child only (remove OR isrefused).
2. numberofitems sign flip = has_voiding_child only (remove isrefused).
3. Zero out monetary fields (amountcharged, pricechargedperuom, originalpriceperuom, originalamount, pricediffperuom, linediscountamount, differenceamount, differencepercentage, taxamount) when isrefused=true, via a CASE WHEN isrefused THEN 0 ELSE <existing> wrap on the underlying base amount fields.
4. No refusalType branching needed — client confirmed uniform treatment.

Status: ESCALATED TO ENGINEERING — not implemented. Design was drafted and reviewed internally, then reverted per explicit decision not to apply the change directly; it is being handed to Engineering as a documented finding/proposal rather than shipped via a direct SnowTime PR.

## 8. Open Questions

* Which team (Engineering vs Delivery) owns implementation of this client-specific mapping fix?
* When implemented, document the divergence from pyardm legacy behavior with a code comment, since this client may later run /refine-ardmprod-parity.

## 9. Queries Run

No queries on record — see investigation narrative above.

## 10. Extras / Additional Screenshots

Receipt PDF examples (TRX 1051, TRX 6889) and TLOG JSON snippet showing isVoided/isRefused/refusalInfo.refusalType fields. [See Jira attachment / link in ticket]
