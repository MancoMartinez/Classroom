# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Environment and steps to reproduce

**Environment: Production**, Stater Bros, netTrack Incident.

### Stater Bros, reported 24 sep 2026

1. Log in to Stater Bros production as an admin user.
2. Open Admin, Manage Smart Alerts. The warning letter alert filters on `Shoplifting Extra Root Cause Equals Written Warning OR Equals Last and Final Warning`.
3. Open case 2026-008-DISCIPLINE REQUEST-3, ShopliftingID 205148, Employee Relations Follow Up. Disposition is Last and Final Warning, saved 9/24/2026.
4. Open Smart Alert History for that case.

Expected: one run of the warning letter alert.
Actual: No Matching Alerts Found. Customer screenshots attached to this ticket, 24 sep 2026.

## 2. Findings

| Check | Result | Status |
|---|---|---|
| `InProcess` for 205148 and 205157 | **1 on both** | verified, SELECT run by Support |
| `RootCause` for 205148 | Last and Final Warning, matches the filter | verified |
| `RootCause` for 205157, customer test case | NULL, would not match the filter | verified |
| Rows with `InProcess = 1` in `incident.Shoplifting` | **32** | verified, count only |

With `InProcess = 1` the engine exits before it evaluates the filter. That matches the stuck flag pattern from https://trebuco.atlassian.net/browse/RCS-28465 and https://trebuco.atlassian.net/browse/RCS-28534, same customer. RCS-28534 is open as https://trebuco.atlassian.net/browse/ENG-8698.

## 3. Troubleshooting performed, and the limits of support access

Claude flagged the stuck `InProcess` flag as the likely root cause, based on RCS-28465 and RCS-28534. We checked three things ourselves: the flag on both cases, the `RootCause` value against the alert filter, and the total count of stuck rows. The filter reads the right column. The flag is set on both cases. Could someone evaluate this and give us your thoughts?

Unverified, from AI triage, listed so it is not re-explored: the control panel debug log should show `Quit ProcessSmartAlert because the smart alert for the case is still on processing` on the next save of 205148. We have not checked the debug logs yet.

Support runs SELECT only in production. We did not change any row.

No conversations outside the ticket beyond an internal chat between Support engineers.

## 4. Ruled out. Do not repeat

| Hypothesis | Refuted by |
|---|---|
| Filter reads a column the Disposition field does not write | `RootCause` on 205148 holds Last and Final Warning |
| `FiltersSQL` not regenerated after editing the alert | Customer recreated the alert. Same result |

## 5. Still open

1. Does ENG-8698 cover the cause of the flag getting stuck, or only the release of individual cases?
2. Is it safe to reset `InProcess` on the 32 rows, or does any of them belong to a run still in progress?
3. After a reset, should we expect the `BlobNotFound` on `Printing.CreateDocument` seen in https://trebuco.atlassian.net/browse/RCS-28294?
