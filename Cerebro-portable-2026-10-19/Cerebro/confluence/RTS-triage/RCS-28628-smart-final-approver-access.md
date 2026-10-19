---
ticket: RCS-28628
cliente: Smart & Final
analista: Diego Buelvas
estado_ficha: Resolved
sintoma: el usuario no aparece en el dropdown de aprobadores de Approve Case
causa: regresion de la migracion a Platform login, SupervisorFlag=0 en membership.Users y LpSecurity.Approver=9 en vez de 8
fix: UPDATE puntual de SupervisorFlag para ese usuario, nunca tocar el Approver del SecurityID compartido
relacionados: RCS-28552, RCS-28307, ENG-7782
confluence_id: 478152294405
modificado: 2026-08-27
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478152294405
---

# RCS-28628 — Smart & Final: Approver Access Not Working + Incorrect Title

Prepared: 27 August 2026 | Analyst: Diego Buelvas | Status: Resolved

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28628 |
| Customer | Smart & Final |
| Issue Type | Incident |
| Priority | Medium |
| Status | Resolved |
| Opened | 27 August 2026 |
| Reporter | Mark Flores (mark.flores@smartandfinal.com) |
| Assignee | Diego Buelvas |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28628 |

## 2. Problem Statement

Mark Flores, Regional Manager of Loss Prevention at Smart & Final, reported that he needed to be added as an approver for all cases in the company via LPMS. He later clarified he had always had approver status prior to a platform login upgrade — indicating a regression rather than a net-new configuration request.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client | Smart & Final |
| Client ID (dbt/ARDM) | Not applicable — Secure application (LPMS) configuration issue |
| Database | Secure Platform DB (SQL Server) — schemas `incident`, `membership` |
| Login mode | Platform login (`Incident.LogInFromPlatform = True`) |

## 4. Investigation

### 4.1 Related-ticket context review

FINDING. Found RCS-28552 (same client — Daniel Rodriguez unable to forward cases to Mark Flores for approval) and ENG-7782/RCS-28307 (Approve Case recipient search returns no results even for manually-added Contacts). Both confirm that adding a user as a Contact does not make them a valid approver.

### 4.2 Code review — approver eligibility logic

Reviewed `Sources/Core/Core/Sidekick/Tools/Case/CasePermissionHelper.cs:32` (repo Secure). A user is a valid approver only if:

```
((SupervisorFlag = 1 OR SupervisorFlag = -1) OR Approver = 8) AND Inactive = 0
```

POINT OF FAILURE FOUND (mechanism identified).

### 4.3 User record lookup — Smart & Final Platform DB

POINT OF FAILURE FOUND. Mark Flores has an active account (UserID=15, Active=1, Inactive=0) but `SupervisorFlag = 0`.

Operational note: the first attempt at this query was mistakenly run against Floor & Decor's database instead of Smart & Final's, returning 0/unrelated rows — corrected once the right connection was confirmed.

### 4.4 Security level check

POINT OF FAILURE FOUND. `Approver = 9` for SecurityID = 1, not the required value `8` ("yes"), confirmed against legacy mapping in `LPUser.vb` (Approver=8 yes, Approver=9 no).

### 4.5 Login-mode branch confirmation

FINDING. `Incident.LogInFromPlatform = True` confirms the Platform-login branch of the `incident.LPUser` view is active, meaning `SupervisorFlag` is sourced from `membership.Users`, not `incident.LPUser2` — critical for targeting the correct table with the fix.

### 4.6 Client confirmation of regression

Mark Flores confirmed he "always had approval status prior to the upgrade."

FINDING. Confirms root cause is a migration regression — the legacy `SupervisorFlag` value was not carried over from `LPUser2` to `membership.Users` when Smart & Final was migrated to Platform login.

### 4.7 Post-fix visual confirmation

PASS. Mark Flores (UserId=15) now appears alongside other valid Smart & Final approvers.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | Mark Flores did not appear in the "Approve Case" approver/recipient dropdown |
| Why | Neither approver-eligibility condition was met: `membership.Users.SupervisorFlag = 0`, and his security level (`SecurityID=1`) mapped to `LpSecurity.Approver = 9` instead of the required `8` |
| Scope | Confirmed for one user at Smart & Final; root cause is a Platform-login migration regression — whether other users/clients are similarly affected was not investigated |
| Business impact | Blocked the Regional LP Manager from receiving/approving cases routed to him |
| Evidence | `SupervisorFlag=0`, `SecurityID=1` to `LpSecurity.Approver=9` (needs `8`); confirmed against `CasePermissionHelper.cs` logic |

## 6. Additional Findings

Client also reported the "Title" shown for Mark Flores in the approver dropdown was incorrect ("Loss Prevention Representative" instead of "LP Regional"). Root cause: outdated value stored in both `membership.UserExtensionData` (`AttributeName='Title'`) and `incident.LPUser2.Title` — the view's `COALESCE` prioritizes the former.

## 7. Recommended Fix

### Option A — Targeted single-user update (Applied)

```
BEGIN TRAN;
UPDATE membership.Users
SET SupervisorFlag = 1
OUTPUT deleted.UserId, deleted.UserName, deleted.SupervisorFlag AS OldValue, inserted.SupervisorFlag AS NewValue
WHERE UserName = 'mark.flores@smartandfinal.com';
COMMIT;
```

Chosen over changing `LpSecurity.Approver` at the shared `SecurityID` level, which would have granted approver rights to every other user sharing that security level.

Also applied — Title correction on both `membership.UserExtensionData` and `incident.LPUser2`.

## 8. Open Questions

No open questions — ticket resolved, client confirmed both fixes. Non-blocking follow-up: whether other Smart & Final users, or other clients migrated to Platform login, have the same unmigrated `SupervisorFlag` gap.

## 9. Queries Run

| # | Query | Result |
| --- | --- | --- |
| 1 | incident.LPUser lookup by last name/email | Run against wrong DB (Floor & Decor) — corrected |
| 2 | incident.LPUser WHERE EmailAddr='mark.flores@smartandfinal.com' | SupervisorFlag=0, SecurityID=1 |
| 3 | incident.LpSecurity WHERE SecurityID=1 | Approver=9 |
| 4 | secure.ConfigurationItem 'Incident.LogInFromPlatform' | True |
| 5 | Title lookup in UserExtensionData / LPUser2 | Both "Loss Prevention Representative" |
| 6 | UPDATE membership.Users SET SupervisorFlag=1 | Fix applied, confirmed by client |
| 7 | UPDATE Title to 'LP Regional' in both tables | Fix applied |

## 10. Extras / Additional Screenshots

"Approve Case — Assigned To" dropdown showing Mark Flores now listed. [See Jira attachment / link in ticket]
