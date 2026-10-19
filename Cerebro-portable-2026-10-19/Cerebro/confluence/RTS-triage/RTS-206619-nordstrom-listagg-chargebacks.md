---
ticket: RTS-206619
cliente: Nordstrom (NOR / client 138)
analista: Diego Buelvas
estado_ficha: Resolved
sintoma: Work Item falla con LISTAGG result too long
causa: el motor de Work Items inyecta columnas LISTAGG usando el GROUP BY de la busqueda, el agrupado por Region desborda el limite de Snowflake
fix: agregar Cashier # como Display Field para bajar el grano del GROUP BY
confluence_id: 478152589314
modificado: 2026-08-27
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478152589314
---

# RTS-206619 — Nordstrom: [Grafana] Active Alerts — Work Item "Chargebacks by Region" LISTAGG Failure

Prepared: 27 August 2026 | Analyst: Diego Buelvas | Status: Resolved

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RTS-206619 |
| Customer | Nordstrom (NOR / client 138) |
| Issue Type | Incident |
| Priority | Medium |
| Status | Closed |
| Opened | 8/27/2026 |
| Reporter | svc rts (svc-rts@apprissretail.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RTS-206619 |

## 2. Problem Statement

Grafana Work Item alert fired for Nordstrom (1 active alert, "[WI] NOR – Failed Work Items"). One scheduled Work Item — `900 - chargebacks by cashier.fti` (Instant Analytics definition, underlying search `1045 - Chargebacks by Region`) — failed with a Snowflake error while 27 of 28 other Work Items completed successfully. Data load was healthy (402,955 transactions loaded for trading day 2026-08-26).

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | c138_nor |
| Region | US |
| Snowflake schema (SnowTime/ARDM) | `ARDM_PRODUCTION.C138_NOR` |
| Snowflake schema (Secure app) | `ARP_PRODUCTION.C138_NOR` (separate DB from the SnowTime ARDM pipeline, not reachable from the SnowTime Snowflake MCP role) |
| ARDM version | Not available |

## 4. Investigation

### 4.1 Confirm client/region mapping

Query: Located `c138_nor` under `dbt/clients/us/` to resolve the correct Snowflake MCP region.

**PASS.** Client confirmed as Nordstrom, region US.

### 4.2 Retrieve the actual failing SQL from Snowflake query history

Query: Pulled the exact query text and error by `QueryId` (`01c6ac76-0109-6674-0001-20d2dffb59e2`) from `SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY`.

**POINT OF FAILURE FOUND.** The WI-executed query contained two columns absent from the manually-run search the operator provided:

```sql
LISTAGG(T1.transactionid, ',') AS "Aggregated_Event_Ids",
LISTAGG(T1.endtransdatetime, ',') AS "Aggregated_Event_DateTimes"
```

Error: `String '(LISTAGG result)' is too long and would be truncated`, SqlState 22000, VendorCode 100078.

### 4.3 Trace the code path generating the extra columns

Query: Searched the Secure repo for the LISTAGG-injection logic.

**POINT OF FAILURE FOUND.** `WorkItemDefinitionProcessor.cs:910-939` (`AddAggregatedEventDataFieldsToSearch`) confirmed the Work Item engine auto-injects these two `STRING_AGG`/`LISTAGG` columns for event-linking/drill-down, using the search's own grouping and joining only on `CashierNo` — with no restriction to the actual chargeback transactions.

### 4.4 Quantify the fan-out with real data

Query: Row/cashier counts and estimated LISTAGG byte size per region against `ARDM_PRODUCTION.C138_NOR.ardm_Header` for the WI's execution window (2026-07-12 to 2026-08-22).

**POINT OF FAILURE FOUND.** Regions `N.COM` (18,009 cashiers, ~48 MB estimated), `WEST RACKS` (~19.4 MB) and `EAST RACKS` (~16.1 MB) all exceed Snowflake's practical LISTAGG limit (~16 MB); small regions like `LAST CHANCE` (95 cashiers, ~0.36 MB) are unaffected.

### 4.5 Fix validation

Confirmed by the operator: after adding Cashier # as a Display Field on `1045 - Chargebacks by Region`, the Work Item reran successfully (operator comment and screenshot on the ticket, 2026-08-27 17:00).

**PASS.**

## 5. Root Cause Statement

| What broke | Work Item `900 - chargebacks by cashier.fti` (search `1045 - Chargebacks by Region`) |
| --- | --- |
| Why | The Secure Work Item engine auto-adds `LISTAGG` event-linking columns (`Aggregated_Event_Ids`, `Aggregated_Event_DateTimes`) using the search's own GROUP BY. The search grouped only by Region (`LocationHierarchy4Description`, a broad hierarchy level) and joined the linking data by `CashierNo` only — pulling every transaction a flagged cashier processed in the window, not just chargeback transactions. For regions with thousands of cashiers, the concatenated string exceeded Snowflake's LISTAGG size limit. |
| Scope | Regions N.COM, WEST RACKS, EAST RACKS for the WI window 2026-07-12 to 2026-08-22; other regions unaffected. |
| Business impact | 1 of 28 daily scheduled Work Items failed, blocking the Chargebacks-by-Region report for the affected regions; Grafana alert fired and was escalated to L2. |
| Evidence | Query history showed the exact failing SQL (4.2); code trace confirmed the injection mechanism (4.3); volume query confirmed region-level byte estimates exceeding the limit (4.4). |

## 6. Additional Findings

* Systemic pattern, not client-specific: `AddAggregatedEventDataFieldsToSearch` applies to any Work Item combining broad grouping with high transaction volume — the same failure could recur on another client/report. Not yet escalated to Engineering.
* Precedent: RCS-28302 (same client, same underlying subsearch `1011 - Chargebacks by Cashier`) broke on 2026-08-11 after a client edit and was fixed by reverting to a prior saved version, without a root-cause investigation at the time.

## 7. Recommended Fix

### Option A — Add Cashier # as a Display Field (Applied)

Added Cashier # as an additional non-aggregate Display Field on `1045 - Chargebacks by Region`, changing the GROUP BY from Region-only to Region+Cashier. Each `LISTAGG` now concatenates only one cashier's transactions in the window (~130–250 rows) instead of an entire region's — well under Snowflake's limit. Confirmed working after the change.

Trade-off: the report grain changed from one row per Region to one row per Region+Cashier; the "Unique Count of Cashier #" metric no longer conveys a meaningful rollup (always 1 per row post-fix).

### Option B — Tighten subsearch qualification criteria (Not applied, alternative)

Raise the `Chargeback Total >= 500` threshold or shorten the `Within the last 6 Months` window on subsearch `1011 - Chargebacks by Cashier` to reduce how many cashiers qualify per region. Preserves the original report grain but changes the business threshold for flagging a cashier — requires business sign-off.

## 8. Open Questions

No Engineering ticket has been filed yet for the systemic linking-join design flaw (see section 6). Recommend opening one if the same error pattern recurs on another client or report with broad grouping and high volume.

## 9. Queries Run

| # | Query | Target | Result |
| --- | --- | --- | --- |
| 1 | `SELECT QUERY_TEXT, ERROR_MESSAGE, ERROR_CODE, DATABASE_NAME, SCHEMA_NAME, START_TIME FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY WHERE QUERY_ID = '01c6ac76-0109-6674-0001-20d2dffb59e2'` | Snowflake (snowflake-us MCP) | Recovered the exact failing WI SQL, confirming the 2 extra LISTAGG columns |
| 2 | `SELECT COUNT(*) header_rows, COUNT(DISTINCT CashierNo) distinct_cashiers, MIN(TradingDay), MAX(TradingDay) FROM ARDM_PRODUCTION.C138_NOR.ardm_Header WHERE TradingDay BETWEEN '2026-07-12' AND '2026-08-22'` | `ARDM_PRODUCTION.C138_NOR` | 6,373,571 header rows, 26,554 distinct cashiers in window |
| 3 | `SELECT T7.LocationHierarchy4Description region, COUNT(*), COUNT(DISTINCT T6.CashierNo), SUM(LENGTH(T6.TransactionID)+1) estimated_listagg_bytes FROM ARDM_PRODUCTION.C138_NOR.ardm_Header T6 LEFT JOIN ARDM_PRODUCTION.C138_NOR.reference_location T7 ON T6.StoreNo=T7.LocationID WHERE T6.TradingDay BETWEEN '2026-07-12' AND '2026-08-22' GROUP BY region ORDER BY estimated_listagg_bytes DESC` | `ARDM_PRODUCTION.C138_NOR` | N.COM ~48MB, WEST RACKS ~19.4MB, EAST RACKS ~16.1MB — all above Snowflake's LISTAGG limit; LAST CHANCE ~0.36MB, unaffected |

## 10. Extras / Additional Screenshots

Search definition failing.png — Composer view of `1045 - Chargebacks by Region`, showing the Region-level grouping and the nested `1011 - Chargebacks by Cashier` condition/expanded fields. [See Jira attachment / link in ticket]

High level search to cashier # definition.png — Composer view of subsearch `1011 - Chargebacks by Cashier`, showing the qualification conditions and display filters (Chargeback Total >= 500, Most Recent Transaction within 6 months). [See Jira attachment / link in ticket]
