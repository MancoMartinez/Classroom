---
ticket: RCS-28352
cliente: Floor & Decor / clientId 58
analista: Diego Buelvas
estado_ficha: UNDER CUSTOMER REVIEW
sintoma: los Work Items no corren antes del SLA de 9:30 EST, uno queda Pending sin timestamps
causa: FtiDefinitonModel.SupportingSearches esta declarado string[] pero el contrato real es LinkedParameterisedSearch[], la deserializacion falla y el endpoint wisc/run devuelve 500
fix: eliminar la propiedad SupportingSearches del modelo, no se usa en WiscService
familia: modelo ligero desincronizado del contrato real
relacionados: RTS-206268
confluence_id: 478142857223
modificado: 2026-08-25
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478142857223
---

# RCS-28352 — Floor & Decor: Work Items Not Run by 9:30 EST SLA

Prepared: 13 August 2026 | Analyst: Diego Buelvas | Status: UNDER CUSTOMER REVIEW

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28352 |
| Customer | Floor & Decor (clientId 58) |
| Issue Type | Incident |
| Priority | High |
| Status | UNDER CUSTOMER REVIEW |
| Opened | 13 August 2026 |
| Reporter | Anthony Aloisio (anthony.aloisio@flooranddecor.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28352 |

## 2. Problem Statement

Work Items for today have not run yet, usually completed by 9:30 EST. Ops Overview for client 58 shows 7 Work Items complete and 14 pending for trading day 2026-08-12 / Day 230.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID | 58 |
| Environment | US Production |
| Snowflake schema | NOT AVAILABLE |
| ARDM version | NOT AVAILABLE — issue is Secure/WISC-side, not SnowTime pipeline |

## 4. Investigation

### 4.1 Ops Overview status check

FINDING. Work Item `/system/ebr/instant analytics/definitions/refunds on associate cards.fti` shown in Pending state with no Run Log Inserted/Updated Time and no Start/End Time — never began execution.

### 4.2 Manual Rerun reproduction

FAIL. `POST https://usprod.apprissretailcloud.com/control/api/wisc/run?clientId=58` returns 500 Internal Server Error.

detail: "The JSON value could not be converted to System.String. Path: $.supportingSearches[0] | LineNumber: 0 | BytePositionInLine: 661."

traceId: "00-2658bec6d0b0889c2a956e001a0f79cb-5015ca57bd5bc388-01"

### 4.3 Code-level root cause (repo: Secure)

POINT OF FAILURE FOUND.

* `WiscController.RunDefinitionRequests` (`WiscController.cs:179`) calls `WiscService.RunAsync`.
* `WiscService.RunAsync` (`WiscService.cs:185`) loads WI metadata via `RepoService.GetRepo<FtiDefinitonModel>(vfp, clientId)`.
* `RepoService.GetRepo` (`RepoService.cs:60`) reads the raw `.fti` file and calls `CommonFileBase.Deserialise<T>` (`CommonFileBase.cs:166`).
* `FtiDefinitonModel.SupportingSearches` (`FtiDefinitonModel.cs:61`) is typed `string[]`, but the real `.fti` definition follows the `InstantAnalyticsDefinition` contract (`InstantAnalyticsDefinition.cs:129`), where `SupportingSearches` is `LinkedParameterisedSearch[]` — an array of objects.
* When a WI definition has `supportingSearches` populated with real linked searches, deserialization into `string[]` throws, and the exception propagates unhandled to the controller's generic catch, producing a 500.

### 4.4 Scope confirmation — why only this WI

PASS. A different WI ("Tony fnd card bust out model") ran successfully via the same Rerun flow. Its `.fti` definition has `supportingSearches` empty/null, so deserialization into `string[]` succeeds trivially.

### 4.5 Search engine health check

PASS. The underlying "refunds on associate cards" search executes and returns correct results when run manually inside Secure. The failure occurs earlier, while loading WI definition metadata for scheduling.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | `FtiDefinitonModel.SupportingSearches` (ControlPanel model, `FtiDefinitonModel.cs:61`) declared as `string[]` |
| Why | The field's real shape per `InstantAnalyticsDefinition.SupportingSearches` is `LinkedParameterisedSearch[]`. System.Text.Json cannot convert a JSON object into System.String, so `WiscService.RunAsync` throws while loading the `.fti` definition, before the WI ever executes. The field is unused anywhere in `WiscService.cs`. |
| Scope | Any WI definition with `supportingSearches` populated fails on both scheduled and manual runs. Confirmed on client 58, WI "refunds on associate cards.fti", trading day 2026-08-12. 14 WI shown pending at time of investigation; only this one confirmed to reproduce the exact failure. |
| Business impact | Daily Work Item generation blocked for this WI definition past the client's expected 9:30 EST SLA |
| Evidence | 500 response with the traceId above; code confirmed at the five file/line references. Manual search execution outside WISC returns correct results. |

## 7. Recommended Fix

### Option A — Remove unused SupportingSearches property (Recommended)

`SupportingSearches` is never read in `WiscService.cs`. Since `CommonFileBase.DeserializeJson`'s `JsonSerializerOptions` does not set `UnmappedMemberHandling.Disallow`, removing the property from `FtiDefinitonModel.cs` (lines 58-61) makes System.Text.Json silently ignore `supportingSearches` in the JSON regardless of its shape — zero risk to WI that already run successfully.

1. Delete the `SupportingSearches` property from `FtiDefinitonModel.cs`.
2. Build and validate locally against the captured payload.
3. Engineering PR + deploy to Secure ControlPanel.
4. Retry manual Rerun in prod for client 58 — confirm 200 OK and populated timestamps.
5. Audit the other 13 pending WI for the same pattern; re-run any that match.

## 8. Open Questions

* Fix not yet applied to the Secure repo — pending Engineering approval/PR.
* Unconfirmed whether the remaining 13 pending WI share this exact failure or are normal processing backlog.

## 10. Extras / Additional Screenshots

Ops Overview pending state, DevTools Headers tab with the 500 response, response body with the deserialization error, and the request payload. [See Jira attachment / link in ticket]
