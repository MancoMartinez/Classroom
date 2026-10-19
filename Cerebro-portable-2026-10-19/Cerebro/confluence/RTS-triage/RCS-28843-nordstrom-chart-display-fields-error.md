---
ticket: RCS-28843
cliente: Nordstrom / c138_nor
analista: Diego Buelvas
estado_ficha: Work in Progress
sintoma: editar display fields rompe el chart, no se puede revertir el tipo ni deshabilitarlo
causa: alias interno posicional (UniqueCountofWorkviewID_N) queda obsoleto y ChartFormatter.GetDescriptionValue lanza NullReferenceException sin manejo defensivo
fix: borrar y recrear el campo calculado; a largo plazo alias por identidad y manejo defensivo en ChartFormatter.cs:4931-4940
familia: binding por posicion o nombre
relacionados: RCS-28841, RCS-28300, RTS-206268, RTS-206610
confluence_id: 478193647619
modificado: 2026-09-10
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478193647619
---

# RCS-28843 — Nordstrom: Changes to Search Display Fields Causing Error for Chart

Prepared: 10 September 2026 | Analyst: Diego Buelvas | Status: Work in Progress

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28843 |
| Customer | Nordstrom |
| Issue Type | Incident |
| Priority | Medium |
| Status | Work in Progress |
| Opened | 09 September 2026 |
| Reporter | Sara Beaty (sara.beaty@nordstrom.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28843 |

## 2. Problem Statement

The client edited the display fields on a search — adding a new field and changing how another was calculated (formula + alias). The search itself still ran fine, but the chart began throwing an error on open. Attempting to switch the chart type works, but switching back to the original chart type throws another error. The client also cannot disable the chart to reset it.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | c138_nor |
| Region | US |
| ARDM Version | NOT AVAILABLE |
| Snowflake Schema | NOT AVAILABLE |
| Active Products | Reporting / Dashboards (Search Composer Chart Wizard) |

## 4. Investigation

### 4.1 Client-provided error screenshot / stack trace

Query: Reviewed the error banner captured by the client during chart render.

**POINT OF FAILURE FOUND.** `System.NullReferenceException: Failed to generate description for search field UniqueCountofWorkviewID_4 method "GetDescriptionValue()"`, thrown from `ChartFormatter.GetDescriptionValue()` to `PieSeriesDataFormatter()` to `GetChart()`.

### 4.2 Source review — ChartFormatter.cs

Query: Located `GetDescriptionValue()` (`Sources/UI/PlatformUI/Areas/Reporting/Contract/ChartFormatter.cs:4931-4940`) and compared it against its sibling `GetPointValue()` (same file, lines 4900-4923).

**FAIL — root cause confirmed.** `GetDescriptionValue()` looks up `RowData.FirstOrDefault(DisplayFieldID == pointDataID)`; when no match is found it throws an unhandled NullReferenceException. `GetPointValue()` hits the identical missing-match case and instead returns `(false, 0.00F)` gracefully. The pie chart's data-label rendering path calls the throwing variant.

### 4.3 Cross-reference against prior incident memory

Query: Searched local incident history for the same trigger ("edited a calculated/display field, chart broke").

**POINT OF FAILURE FOUND — matches known bug class.** Same root cause family as RCS-28300 (confirmed: Composer assigns internal field aliases like UniqueCountofWorkviewID_N by position, not stable identity — collides/desyncs after edits) and RCS-28841 (Casey's, currently "Under Engineering Review", same trigger, no code-level root cause on record yet). Also same binding-fragility family as RTS-206268 / RTS-206610.

## 5. Root Cause Statement

| Aspect | Detail |
| --- | --- |
| What broke | The "Work Item Breakdown by Type" pie chart stops rendering after the client edits display fields; chart type cannot be reverted, chart cannot be disabled |
| Why | Editing/adding display fields reassigns Composer's internal position-based field aliases (UniqueCountofWorkviewID_N). The chart series definition still references the stale alias. ChartFormatter.GetDescriptionValue() (line 4936) throws an unhandled NullReferenceException when it can't resolve that alias against current RowData — crashing every subsequent call to GetChart(), which is why type-revert and disable also fail |
| Scope | Nordstrom (c138_nor), "Store Work Item Breakdown by Type" search/chart. Same underlying defect confirmed independently on Casey's (RCS-28841) and on another client (RCS-28300) |
| Business impact | Chart becomes unusable after any edit to its calculated/display fields, with no client-side recovery path (can't revert type, can't disable) |
| Evidence | Exact exception + field name (UniqueCountofWorkviewID_4) and code line numbers; pre-edit screenshot shows the chart working correctly before the field edit |

## 6. Additional Findings

`GetDescriptionValue()` has no defensive handling for a missing field match, unlike its sibling `GetPointValue()` (lines 4900-4923), which tolerates the identical case. This asymmetry is what turns an otherwise recoverable stale-binding condition into a hard, unhandled crash of the entire chart render — a distinct, previously undocumented code-level finding beyond the alias-collision root cause already known from RCS-28300.

## 7. Recommended Fix

### Option A — Client workaround (short-term)

In the search definition (not the chart), delete and re-add the edited/added calculated display field(s) to force the Composer to regenerate clean internal aliases. Note: if the search is attached to a Dashboard, this may trigger the `ComposerService.SaveSearch` dependency guard (documented on RCS-28841), requiring the "Save Anyway" permission or temporary removal from the Dashboard.

### Option B — Engineering fix (recommended, long-term)

1. Make the Composer's internal display-field alias assignment stable/identity-based instead of positional, removing the collision class shared with RCS-28300 / RTS-206268 / RTS-206610.
2. Patch ChartFormatter.GetDescriptionValue() (ChartFormatter.cs:4931-4940) to handle a missing DisplayFieldID match defensively — mirroring GetPointValue() — instead of throwing, so a stale binding degrades gracefully rather than crashing the chart pipeline.

## 8. Open Questions

* Confirm with Nordstrom whether Option A (remove/re-add the calculated field) resolves the chart error.
* Recommend linking this ticket to RCS-28841 in Jira — same underlying defect class, and RCS-28843 supplies the concrete stack trace/code location RCS-28841 does not yet have on record.

## 9. Queries Run

| # | Query / Action | Result |
| --- | --- | --- |
| 1 | Reviewed client screenshot of chart error / stack trace | NullReferenceException in ChartFormatter.GetDescriptionValue(), field UniqueCountofWorkviewID_4 |
| 2 | Reviewed ChartFormatter.cs (GetDescriptionValue() vs GetPointValue()) | Confirmed GetDescriptionValue() throws unhandled exception on missing field match; GetPointValue() tolerates it |
| 3 | Searched local incident memory for prior tickets with the same trigger | Matched RCS-28300 and RCS-28841 |

## 10. Extras / Additional Screenshots

"Original Output Table and Chart.png" — pre-edit baseline, chart rendering correctly. "image-20260909-162414.png" — error banner with the NullReferenceException stack trace. "Chart Error.mp4" — screen recording of the client attempting to revert chart type back to pie. [See Jira attachment / link in ticket]

## 11. Related / Similar Tickets

| Ticket | Customer | Status | Relationship |
| --- | --- | --- | --- |
| RCS-28841 | Casey's (c184_csy) | Under Engineering Review | Same trigger and same client-visible symptom. Already escalated to Engineering, without the code-level root cause captured here. Recommend linking. |
| RCS-28300 | (Sara — Work View Composer) | Closed | Confirmed root cause: Composer's internal display-field alias is assigned by position, not stable identity, and collides/desyncs when fields are added/edited/reordered. Closed via workaround, not a code fix. |
| RTS-206268 | KNY | Closed | Same binding-fragility family: internal field ID (POS_ARTICLEID) breaks after rename/reorder, invalid identifier error. |
| RTS-206610 | FAD | Under Support Data Team Review | Same family: CUSTOMERNUMBER renamed to X_CUSTOMERNUMBER in ARDM v2 breaks Work Item search bindings. |

Pattern: four tickets across four different clients over ~7 weeks, all rooted in the platform's internal field-binding-by-position/name mechanism breaking whenever the underlying field is edited, renamed, or reordered. RCS-28843 is the first to pin down an exact throwing code line, which strengthens the case for a platform-level fix rather than continuing to patch per-ticket.
