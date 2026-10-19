---
ticket: RTS-205224
cliente: Burlington Coat Factory (BCF / 089)
analista: Diego Buelvas
estado_ficha: WORK IN PROGRESS, fix aplicado y verificado
sintoma: 1 de 20 Work Items falla con NonRetryableException por 3 display fields faltantes
causa: la busqueda destino fue modificada y perdio purchasingemployeeid, ticketamount y totalitemsalecount, que el Synopsis referencia
fix: agregarlos como Display Fields ocultos y re ejecutar el Work Item
nota_reutilizable: el motor de Work Items valida que todo campo usado en el Synopsis exista en los Display Fields, oculto o visible
relacionados: RTS-205361
confluence_id: 478142267412
modificado: 2026-08-25
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478142267412
---

# RTS-205224 — Burlington Coat Factory (BCF): Failed Work Item — Associate Purchases with Line Void

Prepared: 04 August 2026 | Analyst: Diego Buelvas | Status: WORK IN PROGRESS

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RTS-205224 |
| Customer | Burlington Coat Factory (BCF / 089) |
| Issue Type | Incident |
| Priority | Medium |
| Status | Work in Progress |
| Opened | 04 August 2026 |
| Reporter | svc rts (svc-rts@apprissretail.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RTS-205224 |

## 2. Problem Statement

A Grafana alert fired on 2026-08-04 indicating 1 failed Work Item for BCF. Of the 20 Work Item definitions that executed for trading day 2026-08-03, 19 completed successfully and 1 failed. The failed WI — Associate Purchases with Line Void (`/system/ebr/instant analytics/definitions/associate purchases with lv.fti`) — threw a `NonRetryableException` and generated 0 work items due to 3 missing Display Fields in its target search.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client | Burlington Coat Factory |
| Client ID | BCF / 089 |
| Product | Secure (Work Items / Instant Analytics) |
| ARDM Version | N/A |

## 4. Investigation

### 4.1 Work Item Support Console Review

PASS — 19 of 20 WI definitions ran successfully. Total transactions loaded: 659,821 for trading day 2026-08-03.

### 4.2 Failed WI Identification

POINT OF FAILURE FOUND — Run ID `8ffd78a1-bb26-4914-bcc2-064dd0936752`. Queued 2026-08-04 14:53:21 UTC, ended 14:54:13 UTC. Total results 0, generated WIs 0, 0 deaggregation requests — run aborted at validation stage.

### 4.3 Error Message Analysis

POINT OF FAILURE FOUND — `NonRetryableException — Search with VFP ... is missing 3 required display field(s): Field "purchasingemployeeid", used in Synopsis | Field "ticketamount", used in Synopsis | Field "totalitemsalecount", used in Synopsis`. The WI engine validates all Synopsis variable references against the target search's Display Fields at runtime.

### 4.4 Search Definition Review in Secure Composer

POINT OF FAILURE FOUND — Current Display Fields: Trading Day, Territory, District, Store No, Cashier No, First name, Last name, Total Line Void Count, Total Line Void Amount, Unique Count of Transaction ID. The 3 Synopsis variables were absent. The search had been modified at an undetermined point, likely when the `_Txn Count_updated` variant was created.

### 4.5 Manual Search Execution Validation

PASS — Search returned 21 results for 2026-08-03, confirming the underlying query logic is sound.

### 4.6 Fix Application

PASS — Fields added as hidden Display Fields. The WI engine requires Display Field presence but not visibility.

### 4.7 WI Re-Run Verification

PASS — WI run completed successfully. Work items generated as expected.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | WI definition `associate purchases with lv.fti` — Synopsis references 3 fields absent from target search Display Fields |
| Why | The target search was modified at an undetermined point, removing `purchasingemployeeid`, `ticketamount`, and `totalitemsalecount`. The WI engine enforces hard validation: all Synopsis variables must exist as Display Fields (hidden or visible); any missing field triggers an immediate `NonRetryableException`, no retry. |
| Scope | Trading day 2026-08-03, one WI definition |
| Business impact | 0 work items generated for "Associate Purchases with Line Void"; 19 other WI definitions unaffected |
| Evidence | Run ID with 0 results, 0 generated WIs, 0 deaggregation requests. 659,821 transactions loaded — purely a configuration issue. |

## 7. Recommended Fix

### Option A — Add missing fields as hidden Display Fields (Applied)

1. Open the search in Secure Store Composer.
2. Add `purchasingemployeeid`, `ticketamount`, and `totalitemsalecount` as Display Fields.
3. Set each field as hidden.
4. Save the search.
5. Re-run the WI definition for the affected trading day.

Status: Applied and verified. WI re-run successful.

## 8. Open Questions

No open questions — ticket resolved.

## 9. Queries Run

No SQL queries — investigation conducted entirely via Secure UI (Work Item Support Console, Composer, Explorer).

## 10. Extras / Additional Screenshots

WI Support Console failure, Definition Request Details with 0 deaggregation requests, Composer views of the search and the WI Synopsis, and the manual run returning 21 results. [See Jira attachment]
