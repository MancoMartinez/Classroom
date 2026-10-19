---
ticket: RCS-28095
cliente: WinCo Foods
analista: Diego Buelvas
estado_ficha: WORK IN PROGRESS
sintoma: Open Investigations muestra las de todos con el toggle Show all visualmente apagado
causa: el checkbox usa value en vez de checked, queda no controlado y su estado visual nunca refleja el contexto de React, que persiste durante la sesion del SPA
fix: cambiar value por checked en list-toolbar.component.js:81 y revisar el componente hermano
confluence_id: 478142693379
modificado: 2026-08-25
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478142693379
---

# RCS-28095 — WinCo Foods: Open Investigations is showing everyone's investigations

Prepared: 03 August 2026 | Analyst: Diego Buelvas | Status: WORK IN PROGRESS

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28095 |
| Customer | WinCo Foods |
| Issue Type | Incident |
| Priority | Low |
| Status | Work in Progress |
| Opened | 31 July 2026 |
| Reporter | John Geil (john.geil@wincofoods.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28095 |

## 2. Problem Statement

When clicking "Open Investigations", the view displays investigations from all users even though the "Show all open Investigations." toggle is visually off (851 results, multiple owners visible). If the user toggles it on and then off again, the view correctly shows only their own investigations.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client | WinCo Foods |
| Product | Secure — Investigations module |
| Feature | Open Investigations list + "Show all" toggle |
| Permission required for toggle | `CAN_READ_ALL_INVESTIGATIONS` |
| Snowflake schema | N/A (Secure app issue) |

## 4. Investigation

### 4.1 Affected app and component

PASS. App confirmed: `investigations` SPA. Toggle component: `list-toolbar.component.js`. Toggle is only rendered for users with `CAN_READ_ALL_INVESTIGATIONS`.

### 4.2 React context initial state

PASS. `const [showAllInvestigations, setShowAllInvestigations] = useState(false);` (context.js:7) — initial state is correctly `false`.

### 4.3 Checkbox prop — value vs checked

POINT OF FAILURE FOUND.

```
// list-toolbar.component.js:81 — BUG
<input
    id='show-all-investigations-toggle'
    type='checkbox'
    value={this.context.showAllInvestigations}   // WRONG: should be checked
    onChange={this.toggleShowAllInvestigations}
/>
```

For `<input type="checkbox">` in React, `value` sets the form submission value — it does NOT control the visual checked state. Without a `checked` prop, the checkbox is uncontrolled: its visual state never reflects the React context.

### 4.4 State persistence within the SPA session

PASS (behaviour confirmed). `AppProvider` wraps the entire `RouterProvider` — it is NOT unmounted when navigating between internal routes. If the user toggled "show all" on earlier in the same session, `showAllInvestigations = true` is retained when they return to the list, while the toggle visually shows as off.

### 4.5 Parameter logic in OpenInvestigations

PASS. Logic is correct: passes the parameter when `true`, empty array when `false`. The issue is solely in the toggle display.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | The "Show all open Investigations." toggle does not reflect the actual React context state |
| Why | `value={this.context.showAllInvestigations}` on the checkbox input — wrong React prop. Without `checked`, the checkbox is uncontrolled and its visual state never updates in response to React state changes. |
| Scope | All WinCo users with `CAN_READ_ALL_INVESTIGATIONS` who toggle "show all" on at any point in their session and then navigate back to the list without a full page reload |
| Business impact | User sees the toggle visually off while all investigations are displayed |
| Evidence | Screenshot (2026-07-31): 851 results with multiple owners while toggle appears off. Video confirms the workaround (toggle ON then OFF). |

## 7. Recommended Fix

### Option A — Replace `value` with `checked` on the checkbox (Recommended)

File: `Sources/UI/Components/src/_react/src/apps/investigations/components/list-toolbar.component.js` line 81

```
// BEFORE:
value={this.context.showAllInvestigations}
// AFTER:
checked={this.context.showAllInvestigations}
```

Steps: edit the line, check whether the same pattern exists in `completed-investigations.component.js`, update the snapshot test, verify visually, raise the PR.

## 8. Open Questions

1. Does the same `value` vs `checked` pattern exist in `completed-investigations.component.js`?
2. ENG ticket pending for the frontend fix.

## 9. Queries Run

| # | Description | Result |
| --- | --- | --- |
| 1 | Text search "Show all open" in Sources/UI/ | Located toggle component, constants, snapshot tests |
| 2 | Read context.js | useState(false) — correct |
| 3 | Read list-toolbar.component.js:81 | value vs checked bug confirmed |
| 4 | Read open-investigations.component.js:44 | Parameter logic correct |
| 5 | Read index.js:46-48 | AppProvider persists across session navigation |

## 10. Extras / Screenshots

Screenshot of 851 results with the toggle off, and a screen recording of the workaround. [See Jira attachment]
