---
ticket: RTS-205361
cliente: Walmart / dominio 300_WMT
analista: Diego Buelvas
estado_ficha: RESOLVED
sintoma: 4 de 57 Work Items semanales fallan con NonRetryableException por display fields faltantes
causa: las definiciones de busqueda perdieron campos que el Synopsis del Work Item todavia referencia
fix: agregar los campos como Display Fields ocultos, y no volver a quitarlos
nota_reutilizable: un campo usado en el Synopsis tiene que existir en los Display Fields de la busqueda aunque este oculto
confluence_id: 478142660611
modificado: 2026-08-25
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478142660611
---

# RTS-205361 — Walmart (300): Work Items Failing — Missing Required Display Fields

Prepared: 06 August 2026 | Analyst: Diego Buelvas | Status: RESOLVED

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RTS-205361 |
| Customer | Walmart (Domain: 300_WMT) |
| Issue Type | Incident |
| Priority | N/A |
| Status | RESOLVED |
| Opened | 06 August 2026 |
| Reporter | svc rts (svc-rts@apprissretail.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RTS-205361 |

## 2. Problem Statement

A Grafana alert fired on 2026-08-06 for WMT (300): WI Pending/Executing (starthour=10). Out of 57 weekly Work Items, 4 failed with `NonRetryableException`. Transaction loading for trading day 2026-08-05 completed successfully.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client | Walmart |
| Domain | 300_WMT |
| Application | Secure (Instant Analytics — Work Items) |
| SnowTime / ARDM | N/A |

## 4. Investigation

### 4.1 Data Load Verification

PASS — Transaction loading completed successfully. Root cause is not a dataload issue.

### 4.2 Work Item Failure Analysis

POINT OF FAILURE FOUND — All 4 failures share the same error pattern: `Caught NonRetryableException, Search with VFP ... is missing N required display field(s): Field "X", used in Synopsis`

| WI Definition | Search Definition | Missing Field(s) |
| --- | --- | --- |
| gift card refund redeem.fti | gift card refund redeem 2026-03-21 053145.search | `tendercashamount` |
| gift card load redeem.fti | gift card refund redeem 2026-03-21 053145.search | `tendercashamount` |
| price reducing activity with associate owned tender.fti | price reduction associate owned tender secure store work item variation.search | `header_ext_pgcustid` |
| after hour line voids.fti | after hours line voids work item variation.search | `header_ext_pgcustid`, `SumofTotalLineVoidAmount` |

### 4.3 Fix Applied — Hidden Display Fields Added

PASS — WIs re-executed successfully. Grafana alerts resolved.

| Search Definition | Field Added | Visibility |
| --- | --- | --- |
| Gift Card Refund Redeem 2026-03-21 053145 | Tender Cash Amount (`tendercashamount`) | Hidden |
| After Hours Line Voids Work Item Variation | Sum of Total Line Void Amount (`SumofTotalLineVoidAmount`) | Hidden |
| After Hours Line Voids Work Item Variation | PG Cust ID (`header_ext_pgcustid`) | Visible |
| Price Reduction Associate Owned Tender Secure Store Work Item Variation | PG Cust ID (`header_ext_pgcustid`) | Visible |

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | 4 Work Item Synopsis configurations referenced Display Fields no longer present in their linked Search Definitions |
| Why | Search definitions had fields removed without accounting for Work Item Synopsis dependencies — fields used in Synopsis must exist in the Search's Display Fields list at WI execution time, even if hidden |
| Scope | WMT tenant (300), 2026-08-06, 4 WI definitions across 3 search definitions |
| Business impact | 4 out of 57 weekly Work Items failed; 53 completed successfully |
| Evidence | `NonRetryableException` with field name in error message; Ops Overview confirmed clean data load; WIs succeeded after fields re-added |

## 7. Recommended Fix

### Option A — Add Missing Fields as Hidden Display Fields (Applied)

For each affected Search Definition, open the Composer and add the required field(s) to the Display Fields section, marked as Hide. This makes the field available to the Synopsis engine without surfacing it in the search results view.

Important: these fields must not be removed from the Search Definitions. Removing them will immediately re-trigger the same `NonRetryableException` on the next WI run.

## 8. Open Questions

No open questions — ticket resolved. Customer recommendation posted on the Jira ticket advising which fields must not be removed and why.

## 9. Queries Run

No SQL queries on record — investigation performed through UI (Ops Overview, WI batch output, Composer).

## 10. Extras / Additional Screenshots

WI queue before and after, plus Composer views of the corrected search definitions. [See OneDrive: RTS-205361]
