---
ticket: RCS-28838
cliente: ICA / c163_ica (EU)
analista: Diego Buelvas
estado_ficha: Work in Progress
sintoma: la busqueda de Efterregistrering av bonus devuelve casi nada
causa: XMLGET salta el nodo intermedio VRArtsPoslogExt:LoyaltyAccount en flat_receipt_loyalty.sql, card_number queda NULL y el modelo descarta el 100% de las filas
fix: corregir el path XML, dbt build en lab y backfill-ardm desde el go-live
familia: mapeo ARDM v2 SnowTime
relacionados: RCS-23065, RCS-25192
confluence_id: 478190731280
modificado: 2026-09-09
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478190731280
---

# RCS-28838 — ICA: Cannot get correct results for "Post registration of bonus"

Prepared: 09 September 2026 | Analyst: Diego Buelvas | Status: Work in Progress

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28838 |
| Customer | ICA |
| Issue Type | SOW Estimation |
| Priority | High |
| Status | Work in Progress |
| Opened | 09 September 2026 |
| Reporter | effektivrutinanalys@ica.se |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28838 |

## 2. Problem Statement

The customer reports that the search "8_1 Efterregistrering av bonus sorterad kassor och ICAkort" (Post registration of bonus, sorted by cashier and ICA card), located under Utredning – Bonus, returns very few results. The customer does not trust the system and asks whether the search logic is correct or whether something is broken.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | c163_ica |
| Region | EU |
| ARDM Version | V2 |
| Snowflake Output DB/Schema | ARDM_PRODUCTION.C163_ICA |
| Snowflake Working Schema | ARDM_PRODUCTION.C163_ICA_SNOWTIME |
| Go-live date (SnowTime) | 2026-05-27 |
| Active feed involved | raw_receipt (POSLog XML, Base64-wrapped in JSON) |

## 4. Investigation

### 4.1 Baseline volume of RetrospectiveLoyalty in production ARDM

Query: counted ARDM_LOYALTYCARD rows by x_bonusreturnflg for the ticket's date range (Jun–Sep 2026).

FAIL. 100% of rows were x_bonusreturnflg=false. No RetrospectiveLoyalty (post-registered bonus) records exist in the reported window at all.

### 4.2 Historical range check for RetrospectiveLoyalty

Query: MIN/MAX(tradingday) for x_bonusreturnflg=TRUE.

POINT OF FAILURE FOUND. 71,044 rows exist from 2025-10-28 to 2026-05-27 — then zero. The cutoff lands exactly on the SnowTime go-live date, initially suggesting a cutover regression.

### 4.3 Search proxy universe check (chain-wide)

Query: counted rows matching the search's actual filter (Ticket Amount=0, Void=False, Suspended=False, LOYALTY CARD Points>0) across ALL stores.

FAIL. Only 17 rows / 16 stores in 3 months chain-wide — implausibly low for a national retailer, consistent with the underlying data being lost upstream of the search.

### 4.4 Raw feed presence check (ruling out a feed cutoff)

Query: searched RAW_DATA.raw_receipt for the literal string RetrospectiveLoyalty around the go-live date.

FAIL (method). 0 matches both pre- and post-go-live — but a control search for LoyaltyCardRegistration (known to be common) also returned 0, exposing a methodology flaw: data:posLog is Base64-encoded inside the JSON payload; a plain CONTAINS on the raw VARCHAR never matches.

### 4.5 Raw feed presence check (corrected method)

Query: repeated 4.4 with TRY_BASE64_DECODE_STRING(data:posLog::VARCHAR) before CONTAINS.

PASS. RetrospectiveLoyalty is present with stable volume on both sides of go-live (658 rows pre / 634 rows post, 2-day windows). This rules out an upstream feed cutoff — the go-live date correlation from 4.2 was coincidental.

### 4.6 XML structure inspection

Query: extracted a raw XML snippet around a RetrospectiveLoyalty match using REGEXP_SUBSTR with dotall mode on the Base64-decoded payload.

POINT OF FAILURE FOUND. The real XML nests LoyaltyProgram inside an intermediate VRArtsPoslogExt:LoyaltyAccount element — one level deeper than the SnowTime flat model assumes.

## 5. Root Cause Statement

| What broke | dbt/clients/eu/c163_ica/models/flat/receipt/flat_receipt_loyalty.sql, CTE retro_loyalty, line ~171 |
| --- | --- |
| Why | XMLGET(XMLGET(li.li_value, 'RetrospectiveLoyalty'), 'LoyaltyProgram') skips the intermediate VRArtsPoslogExt:LoyaltyAccount node that actually wraps LoyaltyProgram in the live XML. This makes _loyalty_program (and therefore card_number) always NULL for every RetrospectiveLoyalty event. Downstream, map_ardm_loyaltycard.sql computes loyaltyidno = COALESCE(card_number, customer_id) — both NULL for this record type — and the model's final WHERE loyaltyidno IS NOT NULL silently drops 100% of these rows before they ever reach ARDM_LOYALTYCARD. |
| Scope | Every RetrospectiveLoyalty (post-registered bonus) transaction for c163_ica, since the client's SnowTime onboarding — not a regression, the extraction never worked correctly. |
| Business impact | The "Post registration of bonus" search (and any other search/report relying on x_bonusreturnflg/RetrospectiveLoyalty) has been structurally blind to this transaction type the entire time SnowTime has been live for this client. |
| Evidence | ARDM_LOYALTYCARD.x_bonusreturnflg=TRUE: 71,044 rows 2025-10-28 to 2026-05-27 (legacy/backfilled), 0 rows since. Raw feed (Base64-decoded): 634–658 RetrospectiveLoyalty XML nodes per 2-day window, stable across the go-live boundary — confirming the source never stopped sending the data. |

## 6. Additional Findings

* Methodology trap (not a bug, a process note): RAW_DATA.data for raw_receipt stores the full POSLog XML Base64-encoded inside the posLog key of a JSON wrapper. Any future ad-hoc CONTAINS/text search on this feed must decode first (TRY_BASE64_DECODE_STRING(data:posLog::VARCHAR)), or it will silently return false negatives that look like a missing feed.
* Composer search design (non-blocking): the Secure search "8_1 Efterregistrering av bonus" identifies post-registered bonus via a proxy (Ticket Amount=0 + LOYALTY CARD Points>0) rather than filtering directly on x_bonusreturnflg=true. Once the mapping fix lands, it may be worth revisiting whether the search should target the flag directly instead of the indirect heuristic.
* Same-client pattern: RCS-23065 (bonus correction shows positive instead of negative) and RCS-25192 (Loyaltycard_Redemption Amount field always 0.00) show a recurring history of loyalty/bonus mapping defects for this client.

## 7. Recommended Fix

### Option A — Fix the XML extraction path (Recommended)

In dbt/clients/eu/c163_ica/models/flat/receipt/flat_receipt_loyalty.sql, CTE retro_loyalty:

```sql
-- Current (bug)
XMLGET(XMLGET(li.li_value, 'RetrospectiveLoyalty'), 'LoyaltyProgram') as _loyalty_program,

-- Fix
XMLGET(XMLGET(_retro, 'LoyaltyAccount'), 'LoyaltyProgram') as _loyalty_program,
```

If plain XMLGET doesn't resolve the namespace-prefixed VRArtsPoslogExt:LoyaltyAccount node reliably, fall back to the same VARIANT-path + XMLGET hedge already used for LoyaltyCardRegistration's prefixed elements in the same file.

Steps:

1. Apply the SQL fix above.
2. dbt build in lab over a window with known RetrospectiveLoyalty activity (e.g. 2026-05-27 to 2026-05-29) and confirm card_number / loyaltyidno are no longer NULL for these rows.
3. Run /backfill-ardm to recover the historical RetrospectiveLoyalty records lost since go-live (2026-05-27 onward).
4. Optionally revisit the composer search to filter on x_bonusreturnflg directly.

## 8. Open Questions

* Should the composer search be rebuilt to filter directly on x_bonusreturnflg=true instead of the Ticket Amount=0 proxy, once the mapping fix is deployed?
* Confirm with the customer the expected volume of post-registered bonus transactions, to validate the fix's output against their own reconciliation once backfilled.

## 9. Queries Run

| # | Purpose | Database / Schema | Outcome |
| --- | --- | --- | --- |
| 1 | ARDM_LOYALTYCARD volume by x_bonusreturnflg, ticket window | ARDM_PRODUCTION.C163_ICA | 100% false, 0 RetrospectiveLoyalty rows |
| 2 | MIN/MAX(tradingday) for x_bonusreturnflg=TRUE | ARDM_PRODUCTION.C163_ICA | 2025-10-28 to 2026-05-27, 71,044 rows |
| 3 | Chain-wide count matching the search's proxy filter | ARDM_PRODUCTION.C163_ICA | 17 rows / 16 stores in 3 months |
| 4 | CONTAINS(data::VARCHAR,'RetrospectiveLoyalty') around go-live | ARDM_PRODUCTION.C163_ICA_SNOWTIME | 0 / 0 (flawed method) |
| 5 | Control: CONTAINS(data::VARCHAR,'LoyaltyCardRegistration') | ARDM_PRODUCTION.C163_ICA_SNOWTIME | 0 / 0 (confirmed method flaw) |
| 6 | Raw sample rows to inspect data structure | ARDM_PRODUCTION.C163_ICA_SNOWTIME | Revealed Base64-encoded posLog |
| 7 | Corrected CONTAINS with TRY_BASE64_DECODE_STRING | ARDM_PRODUCTION.C163_ICA_SNOWTIME | 658 pre / 634 post — feed confirmed healthy |
| 8 | REGEXP_SUBSTR snippet extraction around match | ARDM_PRODUCTION.C163_ICA_SNOWTIME | Revealed true XML nesting (the bug) |

## 10. Extras / Additional Screenshots

Composer search definition and search results grid — [See Jira attachment / link in ticket]
