---
ticket: RTS-206261
cliente: WinCo (WCO/124)
analista: Diego Buelvas
estado_ficha: RESOLVED
sintoma: el Work Item Hand Keyed Bulk Greater than $100 no genera, SearchMissingRequiredFieldException
causa: el binding interno del campo SumofAmountCharged no resuelve contra la busqueda actual aunque la etiqueta se vea igual, WorkItemGenerator2 valida por clave interna, no por etiqueta
fix: volver a agregar el Display Field con su alias y guardarlo en estado ligado, luego regenerar
familia: binding por posicion o nombre
relacionados: RTS-205224, RTS-205361, RCS-28841
confluence_id: 478142103572
modificado: 2026-08-25
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478142103572
---

# RTS-206261 — WinCo: Hand Keyed Bulk Work Item Missing Display Field

Prepared: 20 August 2026 | Analyst: Diego Buelvas | Status: RESOLVED

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RTS-206261 |
| Customer | WinCo (WCO/124) |
| Issue Type | Incident |
| Priority | Medium |
| Status | Closed |
| Opened | 20 August 2026 |
| Reporter | svc rts (svc-rts@apprissretail.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RTS-206261 |

## 2. Problem Statement

Grafana alert fired for WinCo (WCO/124): 1 active Work Item Alert. Investigation traced the failure to the Work Item "Hand Keyed Bulk Greater than $100," which was not generating due to a `SearchMissingRequiredFieldException`.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client | WinCo (WCO/124) |
| ARDM Version | NOT AVAILABLE |
| Snowflake Schema | NOT AVAILABLE |

## 4. Investigation

### 4.1 Work Item definition review

PASS. Target search meets requirements: has a grouping, not based on another search, permission present.

### 4.2 Search definition review

PASS on visual inspection — the field appeared present in Display Fields. The search groups by header fields (Store No, Cashier No, POS No, End Trans Date Time, Transaction ID) and aggregates Sum of Number Of Items and Sum of Amount Charged (alias "$ Hand Keyed Bulk"), filtered `$ Hand Keyed Bulk > 100`.

### 4.3 Application error log analysis

POINT OF FAILURE FOUND. `SearchMissingRequiredFieldException`: search missing required display field `SumofAmountCharged`, used in Synopsis, Work card section "$ Hand Keyed Bulk," and PotentialValue — despite the field being visually present. Indicates a broken field binding: WorkItemGenerator2 validates by internal field key, not display label; the WI's stored reference no longer resolved to the search's current field instance (consistent with the field having been recreated or edited without being saved in its final bound state).

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | WorkItemGenerator2 field resolution for WI "Hand Keyed Bulk Greater than $100" — required display field `SumofAmountCharged` failed to resolve against the target search |
| Why | Internal field-key mismatch between the WI reference and the current search field, despite identical visible label/alias |
| Scope | Single WI definition for WinCo; WI generation failed entirely until fixed |
| Business impact | No Work Items generated for hand-keyed bulk transactions over $100 during the failure window |
| Evidence | `SearchMissingRequiredFieldException` thrown from `WorkItemDefinitionProcessor.Execute` / `WorkItemGeneratorBase.ProcessSingleWorkItemRequest` |

## 6. Additional Findings

The WI's Value Potential field is set to "Ticket Amount," which exists only under the search's Expanded Display Fields, not the main Display Fields. Not confirmed as a root cause here, flagged as the same failure class and worth reviewing.

## 7. Recommended Fix

### Option A (Applied)

Re-add the "Sum of Amount Charged" Display Field in the "Hand Keyed Bulk Transactions" search with alias "$ Hand Keyed Bulk," ensure it is saved in its bound state, then re-generate the Work Item.

## 8. Open Questions

No open questions — ticket resolved. Follow-up suggestion: review whether Value Potential ("Ticket Amount") should be moved to a main Display Field to pre-empt a similar failure.

## 9. Queries Run

No SQL queries on record — investigation based on WI/Search Composer screenshots and the WorkItemGenerator2 application error log.

## 10. Extras / Additional Screenshots

Work Item Composer definition and Composer search definition. [See Jira attachment / link in ticket]
