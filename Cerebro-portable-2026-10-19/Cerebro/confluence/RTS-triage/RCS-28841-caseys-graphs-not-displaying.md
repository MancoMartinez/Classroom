---
ticket: RCS-28841
cliente: Casey's / c184_csy
analista: Diego Buelvas
estado_ficha: Work in Progress
sintoma: la serie Closed Work Items no se dibuja en el grafico, la tabla si muestra el dato
causa: dos causas distintas, eje Y compartido autoescalado en la reproduccion y binding obsoleto del campo calculado en la busqueda de produccion
fix: borrar y recrear el campo calculado Closed Work Items
familia: binding por posicion o nombre
relacionados: RCS-28843, RCS-28300, RTS-206261
confluence_id: 478193352706
modificado: 2026-09-10
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478193352706
---

# RCS-28841 — Casey's: Graphs Not Displaying All Results

Prepared: 10 September 2026 | Analyst: Diego Buelvas | Status: Work in Progress

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28841 |
| Customer | Casey's |
| Issue Type | Incident |
| Priority | Medium |
| Status | Work in Progress |
| Opened | 09 September 2026 |
| Reporter | Aubrey Hastings (aubrey.hastings@caseys.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28841 |

## 2. Problem Statement

On the "Work Item Status" reports (both By Division and By User), the graphs do not display the "Closed Work Items" series, while the tabular results show the data correctly. The issue began after the client updated the calculated field formula for Closed Work Items (removing "In Investigation" items, which were also being double-counted in Open Assigned Work Items). These reports feed a Dashboard, so the missing series is customer-visible.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | c184_csy |
| Region | US |
| ARDM Version | NOT AVAILABLE |
| Snowflake Schema | NOT AVAILABLE |
| Active Products | Reporting / Dashboards (Work Item Status searches) |

## 4. Investigation

### 4.1 Chart payload inspection (/getchart)

Query: Inspected the chart payload for the three-series column chart (Unclaimed 0–6, Open Assigned 12–73, Closed 146–2,382).

POINT OF FAILURE FOUND. All three series share a single linear Y-axis, auto-scaled to the max value across series (2,382). A bar with value 6 or 73 renders at under 3% of chart height on that scale — visually invisible even though hover tooltips always showed the correct value. This was never a data/binding problem on the reproduction chart.

### 4.2 Reproduction with a clean private search + chart

Query: Rebuilt the same 3-series chart from scratch, fully isolated from production.

PASS. Symptom reproduced identically with 100% fresh data, ruling out corruption specific to the client's original search/chart objects.

### 4.3 False leads ruled out

Query: Checked for duplicate series on the same Value Source, differing series Type in the Advanced tab, and orphaned field binding (stale internal ID behind a correct-looking label, per precedent RTS-206261).

PASS. All three ruled out — confirmed same Type across series, no duplicate source, and the binding-staleness theory was dropped once the clean reproduction still showed the symptom.

### 4.4 Client response — production chart does not match the reproduction's root cause

Query: Client reported their actual chart's Y-axis max is 8 (not thousands), with Closed Work Items = 7 — fully representable on that scale — and it still does not render, even after enabling the Y2 axis.

FAIL. This contradicts the shared-axis-scale explanation. The scale fix (4.1) only applies to the reproduction/test chart's magnitude range. The client's production search has a distinct, real issue — most likely stale binding on the recently-edited calculated field "Closed Work Items," consistent with the originally-dismissed hypothesis from 4.3.

## 5. Root Cause Statement

| Aspect | Detail |
| --- | --- |
| What broke | "Closed Work Items" series fails to render on the client's production Dashboard-linked charts ("Work Item Status By Division" / "By User") |
| Why | Two distinct causes conflated: (1) on the reproduction chart, a single shared linear Y-axis auto-scaled to the largest series masked small bars — not present on the client's real chart; (2) on the client's actual production chart, current working hypothesis is a stale binding on the calculated field "Closed Work Items," introduced when the client edited its formula — unconfirmed, pending client validation |
| Scope | Casey's (c184_csy) "Work Item Status By Division" and "By User" Dashboard searches |
| Business impact | Closed Work Items count invisible in customer-facing Dashboard charts, despite correct underlying data |
| Evidence | Client's chart: Y-axis max = 8, Closed Work Items = 7 (representable on scale); enabling Y2 axis has no effect; tabular results show correct values |

## 6. Additional Findings

Attempting to re-save the client's original production search (not the test copy) returns "The search being saved is used by some dependencies and can't be changed" — a guard in ComposerService.SaveSearch (ComposerService.cs:1417) triggered because the search is referenced by a Dashboard. It can be bypassed with the canSaveAnyway permission (Permission Group to Search Composer to "Save Anyway"), which this client's user does not have. Bug-class note for future tickets: any search under Dashboard Searches that a client wants to edit directly can hit this same block.

## 7. Recommended Fix

### Option A — Remove and re-create the calculated field (Recommended, pending confirmation)

In the original search definition (not just the chart), remove and re-create the calculated field "Closed Work Items." This clears potential binding staleness left over from the client's formula edit. Client has been asked to perform this and confirm. Do not close the ticket until confirmed.

## 8. Open Questions

* Pending client confirmation that re-creating the "Closed Work Items" calculated field resolves the production chart rendering issue.
* If re-creating the field does not resolve it, next step is a deeper binding trace on the production search object itself.

## 9. Queries Run

| # | Query / Action | Result |
| --- | --- | --- |
| 1 | Inspected /getchart payload for the 3-series chart | Shared linear Y-axis, auto-scaled to max series value |
| 2 | Rebuilt chart in a clean private search+chart | Symptom reproduced with fresh data |
| 3 | Checked series Type, duplicate Value Source, field binding ID | All ruled out as causes on reproduction |
| 4 | Enabled Y2 axis + re-tested on client's real chart (max=8, Closed=7) | No effect — confirms distinct production issue |
| 5 | Attempted re-save of original production search | Blocked by ComposerService.SaveSearch dependency guard (ComposerService.cs:1417) |

## 10. Extras / Additional Screenshots

Client-provided screenshots on record in the ticket folder, plus a screen recording (2026-09-09_11-04-19.mp4). [See Jira attachment / link in ticket]
