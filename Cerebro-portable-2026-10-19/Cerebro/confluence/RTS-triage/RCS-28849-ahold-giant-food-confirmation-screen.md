---
ticket: RCS-28849
cliente: Ahold-Delhaize (Giant Food / ADUSA)
analista: Diego Buelvas
estado_ficha: Work in Progress
sintoma: no aparece la pantalla de confirmacion al asignar o reasignar un caso
causa: el redirect a IncidentMessage.aspx esta comentado en ReAssignCase.aspx desde hace unos 3.5 anos, decision de diseno
fix: requiere sign-off de Product para reinstaurarlo, o cerrar como working as designed
relacionados: RCS-28123, RCS-28766
confluence_id: 478193188867
modificado: 2026-09-10
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478193188867
---

# RCS-28849 — Ahold-Delhaize (Giant Food): Users Not Receiving Confirmation Screen When Assigning a Case

Prepared: 10 September 2026 | Analyst: Diego Buelvas | Status: Work in Progress

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28849 |
| Customer | Ahold-Delhaize (Giant Food / ADUSA) |
| Issue Type | Incident |
| Priority | Medium |
| Status | Work in Progress |
| Opened | 09 September 2026 |
| Reporter | Jim Cosseboom (james.cosseboom@adusa.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28849 |

## 2. Problem Statement

The assignment confirmation screen (with the view/print report option) is not appearing when a case is assigned or reassigned — the user is redirected straight to the workbench instead. The rejected-case message screen (attached to the ticket) shows this confirmation correctly, proving the mechanism exists elsewhere in the app. This behavior was previously flagged during testing on 8/26 under RCS-28123, logged separately for engineering review, but that ticket was closed before a resolution was communicated — hence this new ticket.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID (dbt/ARDM) | N/A — not a SnowTime/ARDM client; legacy Incident (LPMS) module only |
| ARDM version | N/A |
| Snowflake schema | N/A |
| Module | Incident (LPMS), Giant Food banner (StoreIdent 11717 per screenshot) |

## 4. Investigation

### 4.1 Prior ticket & memory review

Query: Reviewed RCS-28123 (same customer, same UI symptom) via Jira MCP + local memory.

FINDING. RCS-28123 tracked the identical symptom (confirmation popup / print option missing after case reassignment). Engineering (Matthew Kamminga, comment 2026-09-01) confirmed the reassign redirect to the confirmation page was intentionally commented out in code ~3.5 years ago. That ticket was closed as "working as designed" — only the "User Cannot be Blank" validation error and a duplicate reassignment email were fixed as part of its remediation.

### 4.2 Code-level verification (repo Secure)

Query: Read `ReAssignCase.aspx` and `RejectCase.aspx` client-side `hidepage()` handlers, and the parent frame `LPMSEditMenu.aspx` (defines `hidepopup` / `hidepopupRedirectToIncidentMessage` / `hidepopuprefresh`).

POINT OF FAILURE FOUND. `RejectCase.aspx:28-31` actively calls `window.parent.hidepopupRedirectToIncidentMessage('rejectcase')`, navigating to `IncidentMessage.aspx?...&mess=rejectcase`, rendering the confirmation/print screen (the exact screenshot attached to this ticket). `ReAssignCase.aspx:29-32` has the equivalent call commented out and instead calls `window.parent.hidepopuprefresh('showreassigncase')`, which only reloads the current page (`window.location.assign(CurrentUrl)`) — it never navigates to `IncidentMessage.aspx`, so no confirmation screen or print option is ever shown after an assign/reassign action.

### 4.3 Regression check

Query: Compared this finding against recent PR history near `ReAssignCase.aspx` (PR 56138 / ENG-7192-Part2, tied to related ticket RCS-28766) to rule out a recent regression as the cause.

PASS (ruled out). PR 56138 removed the `CreateAlertInQueue("REASSIGN")` email-trigger call — a different, unrelated symptom tracked separately under RCS-28766. It does not touch the client-side `hidepage()`/redirect logic examined in 4.2. The missing confirmation screen is not a side effect of that PR; it predates it by ~3.5 years per the RCS-28123 finding.

## 5. Root Cause Statement

| What broke | Nothing broke — the confirmation/print screen was never wired up for the assign/reassign flow |
| --- | --- |
| Why | `ReAssignCase.aspx`'s `hidepage()` JS handler has the redirect-to-confirmation call (`hidepopupRedirectToIncidentMessage`) commented out, replaced by a plain page refresh (`hidepopuprefresh`), intentionally, per code comment history (~3.5 years, confirmed by Engineering in RCS-28123) |
| Scope | All Incident (LPMS) module users performing a case assign/reassign action; the reject-case flow is unaffected (uses the active redirect) |
| Business impact | Users lose the immediate visual confirmation and the one-click view/print report option after assigning a case. No data-loss or missing-notification scope here (notification email is tracked separately under RCS-28766) |
| Evidence | Direct code comparison — `RejectCase.aspx:30` (active redirect) vs `ReAssignCase.aspx:30` (same line, commented out) + `ReAssignCase.aspx:31` (`hidepopuprefresh` in its place). Both functions defined in `LPMSEditMenu.aspx:127-146` |

## 6. Additional Findings

RCS-28123 already closed this exact behavior as "working as designed." RCS-28849 effectively re-opens that product decision, now backed by direct visual evidence (reject-case screen works, assign-case screen does not) rather than a description alone.

## 7. Recommended Fix

### Option A — Reinstate confirmation screen (Recommended, requires Product/Engineering sign-off)

Un-comment `window.parent.hidepopupRedirectToIncidentMessage('showreassigncase')` in `ReAssignCase.aspx` (line 30) and remove/replace the `hidepopuprefresh` call, mirroring `RejectCase.aspx`'s active pattern. This reverses a deliberate ~3.5-year-old design decision (per RCS-28123), so it needs explicit Product approval before an Engineering PR — not a plain bugfix.

### Option B — No code change

Confirm to the customer this is existing, intentional platform behavior (same conclusion as RCS-28123) and close as "working as designed." Route any further request for the screen through the Product feature-request process instead of as an incident.

## 8. Open Questions

* Does Product want to reinstate the confirmation/print screen for assign/reassign, given the customer has now raised this twice with visual evidence?
* If reinstated, should assign and reassign share the same `mess=showreassigncase` path, or does assign need its own `mess=` value (only reject/reassign values are currently wired)?

## 9. Queries Run

No queries on record — code-level investigation only; no Snowflake/SQL queries required.

## 10. Extras / Additional Screenshots

"Rejected case message.JPG" — screenshot of `IncidentMessage.aspx?...&mess=rejectcase`, confirming the confirmation-screen mechanism works correctly for the reject-case flow. [See Jira attachment / link in ticket]
