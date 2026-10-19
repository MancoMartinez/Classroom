---
ticket: RCS-28718
cliente: Sainsbury's / c107_sby (EU)
analista: Diego Buelvas
estado_ficha: Work in Progress
sintoma: Receipt Visualization no muestra Nectar Points en transacciones de refund del feed EMR
causa: pointsRedeemed nunca se implemento, el CR RCS-26350 lleva en Under CSM Review desde 2026-06-25, y el feed EMR ni siquiera esta onboarded en SnowTime
fix: destrabar la aprobacion del SOW de RCS-26350 y despues extraer pointsRedeemed en la capa flat
relacionados: RCS-26699, RCS-26350
confluence_id: 478178672641
modificado: 2026-09-04
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478178672641
---

# RCS-28718 — Sainsbury's: Receipt Visualization for Emerald txns missing Nectar Points info for Refund Transactions

Prepared: 04 September 2026 | Analyst: Diego Buelvas | Status: Work in Progress

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28718 |
| Customer | Sainsbury's |
| Issue Type | Incident |
| Priority | Medium |
| Status | Work in Progress |
| Opened | 02 September 2026 |
| Reporter | Sai.Guduri@sainsburys.co.uk |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28718 |

## 2. Problem Statement

Nectar Points information in Receipt Visualization is missing for Emerald (EMR) Refund Transactions. The client provided EMR/R10 TLOG ID pairs across three scenarios (sale + goodwill, sale no goodwill, return) and requested receipt images for both EMR and R10 transactions.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID (dbt) | `c107_sby` |
| Secure client ID | 107 |
| ARDM version | V2 (snowtimeV2) |
| Snowflake schema | `ARDM_PRODUCTION.C107_SBY` (output) / `C107_SBY_SNOWTIME` (working) |
| Active products | SnowTime (live, ARDM_JSON enabled) for the R10 feed (raw_postransactions); EMR/Emerald feed not onboarded |

## 4. Investigation

### 4.1 Duplicate-ticket check (Jira search)

FINDING. Found RCS-26699 (2026-04-30), identical title/summary — closed by 28-day auto-close automation, never actually fixed.

### 4.2 Root-cause chain trace

POINT OF FAILURE FOUND. RCS-26350 ("Request to Configure New Loyalty Attribute for Redeemed Points") has been in "Under CSM Review" since 2026-06-25, awaiting SOW approval (~16h estimated) — no engineering work started.

### 4.3 SnowTime mapping code check

Query: Reviewed dbt/clients/eu/c107_sby/models/mapping/map_ardm_loyaltycard.sql and flat_postransactions_loyaltycards.sql.

FAIL. `redemptionamount` is hardcoded to `0.00` in mapping; `pointsRedeemed` is never extracted from the raw JSON in the flat layer.

### 4.4 GetTransactionJson.sql check (Secure repo)

PASS. The function selects `ARDM_LOYALTYCARD.*` wholesale into the receipt JSON — no Secure-side change needed once the mapping/flat gap is fixed; the field will flow through automatically.

### 4.5 EMR transaction existence check (Snowflake)

POINT OF FAILURE FOUND. Zero rows in both RAW_DATA and ARDM_HEADER — the EMR transactions referenced in the ticket (store 7188 / pos 0003 / ticket 1964) do not exist anywhere in c107_sby's SnowTime pipeline.

### 4.6 Alternate-client hypothesis (Argos) check

Ruled out. `C053_ARG` schema exists in ARDM_PRODUCTION but has zero tables deployed (scaffolded, never built); no GetTransactionJson.sql or legacy Greenplum equivalent found for client 53. Operator confirmed EMR is instead a not-yet-onboarded feed within c107_sby itself.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | Nectar Points (pointsRedeemed) data does not populate on Receipt Visualization, and the EMR (Emerald) transaction set referenced in the ticket is entirely absent from the pipeline |
| Why | (1) pointsRedeemed was never implemented on the Appriss side — enabling CR RCS-26350 has been stuck in "Under CSM Review" since 2026-06-25 awaiting SOW approval; map_ardm_loyaltycard.sql hardcodes redemptionamount to 0.00 and the flat layer never extracts pointsRedeemed. (2) Separately, the EMR_Outbound_Appriss feed has not been onboarded into SnowTime for c107_sby at all |
| Scope | All Sainsbury's (c107_sby) loyalty-card records lack redemptionamount; EMR transaction volume unmeasurable since the feed isn't onboarded |
| Business impact | Client-visible Receipt Visualization gap for Nectar Points on refund transactions; 2nd time the same symptom has been reported (RCS-26699 closed unresolved) |
| Evidence | RCS-26350 status = "Under CSM Review" (checked 2026-09-04); map_ardm_loyaltycard.sql:41 hardcodes 0.00; zero matching rows in RAW_DATA/ARDM_HEADER across multiple probes |

## 6. Additional Findings

Argos (c053_arg) was initially suspected as the source of "EMR" transactions (same Sainsbury's group, distinct POS) — ruled out; Argos has never been built/deployed in SnowTime (zero tables in ARDM_PRODUCTION.C053_ARG). Documented as a dead end so a future investigator doesn't re-walk it.

## 7. Recommended Fix

### Option A — Escalate RCS-26350 SOW approval (Recommended, business blocker)

Primary blocker. Once approved: extend flat_postransactions_loyaltycards.sql to extract pointsRedeemed from the raw JSON; update map_ardm_loyaltycard.sql to map it into redemptionamount (or an x_ extension if it doesn't match standard ARDM semantics — confirm against dbt/docs/ARDMV2/ardm_loyaltycard.md). No Secure-side change required.

### Option B — Clarify and onboard the EMR_Outbound_Appriss feed

Independent of Option A: confirm with Sainsbury's/Engineering whether EMR/Emerald transactions are meant to load through SnowTime as a new feed. If yes, candidate for /setup-data-feed once blob/Ingest coordinates are known.

## 8. Open Questions

* Is RCS-26350's SOW approved or still pending? (Confirmed pending as of 2026-09-04.)
* Is EMR_Outbound_Appriss meant to be a brand-new SnowTime feed under c107_sby, or does the data arrive through another mechanism not yet identified?
* Once pointsRedeemed is available, does it map 1:1 to ARDM_LOYALTYCARD.redemptionamount, or does it need an x_ extension?

## 9. Queries Run

| # | Target | Result |
| --- | --- | --- |
| 2 | C107_SBY_SNOWTIME.RAW_DATA GROUP BY data_feed | Confirmed raw_postransactions |
| 3 | RAW_DATA colon-path filter storeNo/posNo/ticketNo (7188/0003/1964) | 0 rows |
| 4 | RAW_DATA storeNo ILIKE '%7188%' 4-day window | 0 rows |
| 6 | C107_SBY.ARDM_HEADER storeno=7188, posno=3, ticketno=1964 | 0 rows |
| 7 | C053_ARG.ARDM_HEADER same lookup | Error — table does not exist |
| 9 | INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA='C053_ARG' | 0 rows — no tables deployed |
| 10 | INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA='C107_SBY' | Full table list, confirms c107_sby is live |
