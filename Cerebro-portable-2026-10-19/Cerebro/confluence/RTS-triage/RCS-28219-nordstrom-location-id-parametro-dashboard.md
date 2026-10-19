---
ticket: RCS-28219
cliente: Nordstrom
analista: Diego Buelvas
estado_ficha: Work in Progress
sintoma: el filtro de Location ID o Store_Num nunca aparece en la barra de parametros del dashboard, sin error
causa: DashboardParameterService no tiene builder para una condicion numerica plana sin el tag isLocationId, y si ningun builder hace match la condicion se descarta en silencio
fix: agregar el tag isLocationId a nivel de definicion de campo, o crear un builder generico para numericos
nota_reutilizable: el tag isLocationId no se puede poner desde ninguna UI, ni Composer ni SearchableManager
confluence_id: 478146134019
modificado: 2026-08-26
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478146134019
---

# RCS-28219 — Nordstrom: Location ID Parameter in Workview data area is not working on Dashboards

Prepared: 26 August 2026 | Analyst: Diego Buelvas | Status: Work in Progress

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28219 |
| Customer | Nordstrom |
| Issue Type | Incident |
| Priority | Medium |
| Status | Work in Progress |
| Opened | 06 August 2026 |
| Reporter | Sara Beaty (sara.beaty@nordstrom.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28219 |

## 2. Problem Statement

When a dashboard widget filters on a numeric Location/Store ID field exposed as an Optional Parameter, the corresponding filter control never appears in the dashboard's parameter bar — silently, with no error. Reported on two example dashboards: "Test Dashboard" (search "Region Open Work Items Test", field `Location ID`) and "wi dashboard test" (search "Test Search for WI Dashboard", field `Store_Num`).

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client | Nordstrom |
| Client ID | NOT AVAILABLE |
| ARDM Version | NOT AVAILABLE |
| Snowflake Schema | NOT AVAILABLE |
| Active Products | Secure — Workview / Dashboards module |

## 4. Investigation

### 4.1 Direct search execution test

PASS. Ran "Test Search for WI Dashboard" directly with `Store_Num = 714`. The search filtered correctly; generated T-SQL was correct. Rules out a data or search-definition issue.

### 4.2 Composer condition review (both searches)

FINDING. Both searches have the numeric ID field correctly defined as an "Optional parameter" condition, alongside a companion string field, also Optional. Customer screenshots confirm that on the live dashboard only the string field renders as a filter — the numeric ID field's filter control is completely absent, no error shown.

### 4.3 Dashboard parameter builder code review

POINT OF FAILURE FOUND. `DashboardParameterService.BuildDashboardParametersFromCondition` (`DashboardParameterService.cs:360-398`) loops through registered builders and uses the first one whose `IsMatch` returns true. There is no else/fallback — if no builder matches, the condition is silently dropped, with no exception and no log. Existing builders only match: String fields, Enum fields, Date fields, fields tagged `isLocationId`, or fields wrapped in a location-hierarchy function. No builder exists for a plain numeric (BIGINT/Int64) equality condition that lacks the `isLocationId` tag.

### 4.4 Self-service workaround check (SearchableManager / Composer)

FAIL — no self-service path exists. The Search Composer only reads `Tags`, never writes it. `SearchableManager`'s backend (`ApiController.SaveSearchableDef`) can technically persist a `Tags` value, but its edit UI exposes no control for that property. The tag can only be set at field-definition authoring time (platform/Engineering).

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | Dashboard filter controls for numeric Location/Store ID fields never render, even though the fields are correctly configured as Optional parameters |
| Why | The parameter-builder pipeline has no generic builder for a plain numeric equality condition; a match requires either the `isLocationId` tag or a location-hierarchy function wrapper. When neither applies, the condition is silently discarded |
| Scope | Confirmed on 2 dashboards/searches for this client; the code path is platform-wide |
| Business impact | Users cannot filter affected dashboard widgets by store/location, with no error to explain why |
| Evidence | Direct search execution with `Store_Num = 714` filters correctly; customer screenshots show only the paired string field rendering; code review confirms no matching builder |

## 6. Additional Findings

Investigated whether the `isLocationId` tag could be applied as a workaround by the client or by Support. Confirmed no such path exists anywhere in the platform UI — this is a hard platform gap, not a configuration oversight.

## 7. Recommended Fix

### Option A — Point fix (Recommended for fastest resolution)

Engineering adds the `isLocationId` tag to the `Location ID` and `Store_Num` fields at the field-definition level, so both route to `LocationDashboardParameterBuilder` and render the standard Location picker.

### Option B — Platform fix (Recommended to prevent recurrence)

Engineering adds a generic `IDashboardParameterBuilder` implementation covering numeric equal-to conditions that carry no tag.

## 8. Open Questions

* Confirm whether to raise a formal Engineering ticket now, referencing this root cause.
* Decide whether to ship Option A only, or both A and B.

## 9. Queries Run

| # | Query / Action | Result |
| --- | --- | --- |
| 1 | Ran "Test Search for WI Dashboard" directly with `Store_Num = 714` | Filtered correctly; T-SQL generated correctly |

No Snowflake queries — investigation entirely within the Secure/SQL Server side.

## 10. Extras / Additional Screenshots

Composer condition screenshots and the live dashboard filter bar showing only the string field. [See Jira attachment / link in ticket]
