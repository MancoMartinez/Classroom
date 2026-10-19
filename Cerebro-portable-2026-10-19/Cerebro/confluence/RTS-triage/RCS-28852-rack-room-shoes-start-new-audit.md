---
ticket: RCS-28852
cliente: Rack Room Shoes
analista: Diego Buelvas
estado_ficha: Work in Progress
sintoma: usuario no puede iniciar un audit nuevo, solo verlos
causa: LPUser.SecurityID apuntaba al grupo 5 Store con StartAudit=10, que es solo lectura
fix: reasignar al grupo 8 Audit Only, mismo alcance de visibilidad con permiso de creacion
confluence_id: 478193844226
modificado: 2026-09-10
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478193844226
---

# RCS-28852 — Rack Room Shoes: User Cannot Start New Audit

Prepared: 10 September 2026 | Analyst: Diego Buelvas | Status: Work in Progress

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28852 |
| Customer | Rack Room Shoes |
| Issue Type | Incident |
| Priority | Medium |
| Status | Work in progress |
| Opened | 09 September 2026 |
| Reporter | Trevor Monroe (trevor.monroe@rackroom.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28852 |

## 2. Problem Statement

User Kyle Estep (UserID 50006), first user onboarded after the URL migration, could view audits but could not start a new one ("Start New Audit"). Client asked whether a different user group was needed; screenshot of current groups attached to ticket.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client | Rack Room Shoes |
| Application | Secure (Incident/Audit module) |
| Affected user | Kyle Estep, UserID 50006 |
| ARDM version | NOT AVAILABLE |
| Snowflake schema | NOT AVAILABLE |

## 4. Investigation

### 4.1 Permission gate identification

Query: Reviewed server-side gate `AuditAuthorizationService.CanStartAudit()` (`Core/Incident/Services/Audit/AuditAuthorizationService.cs:110-135`, port of legacy `NewAudit.aspx.vb`).

FINDING. Gate requires 0 < LPSecurity.StartAudit < 10. StartAudit = 10 is explicitly view-only.

### 4.2 User's assigned security group

Query: LPUser JOIN LPSecurity ON SecurityID.

POINT OF FAILURE FOUND. Kyle's LPUser.SecurityID = 5 ("Store"), with LPSecurity.StartAudit = 10 — view-only, blocking audit creation. Admin UI listed multiple group-sounding labels (ApprissCase Search Users, ApprissCase Users, Audit Users, Basic Users, Secure Audit Search Users) but these are not combinable memberships — LPUser.SecurityID is a single FK to one LPSecurity row; the actual permission lives only there.

### 4.3 Candidate group search

Query: SELECT * FROM incident.LPSecurity WHERE StartAudit BETWEEN 1 AND 9, matched by ActiveAudits scope equal to user's current group.

PASS. SecurityID = 8 ("Audit Only") — StartAudit = 1, ActiveAudits = 7 — same visibility scope as "Store" but with create permission. Selected as correct target group.

## 5. Root Cause Statement

| What broke | LPUser.SecurityID for Kyle Estep pointed to security group 5 ("Store"), which has StartAudit = 10 (view-only) |
| --- | --- |
| Why | Incorrect role classification at user onboarding — not a code bug |
| Scope | Single user (Kyle Estep, UserID 50006), Rack Room Shoes tenant |
| Business impact | New/first-onboarded user unable to perform their audit function |
| Evidence | LPSecurity.StartAudit gate requires 1–9; group 5 = 10 (blocked); group 8 "Audit Only" = 1 (allowed), matching ActiveAudits scope |

## 7. Recommended Fix

### Option A — Reassign user's security group (Applied)

`UPDATE incident.LPUser SET SecurityID = 8 WHERE UserID = 50006`. Reassigns Kyle to "Audit Only" (same visibility scope as before, adds create permission). Do not modify the shared group's StartAudit value — that would affect every other user in that group. Confirmed with client before applying, since this is a business-role decision, not a code fix.

Status: Applied 2026-09-10. Verified post-update: SecurityID=8, SecurityGroupName='Audit Only', StartAudit=1, ActiveAudits=7 — within valid range. Client (Trevor Monroe) confirmed "Audit Only" as the correct role. Client notified Kyle should now be able to start audits; final client-side confirmation pending before closing ticket.

## 8. Open Questions

Client to confirm from their side that Kyle Estep can now successfully start a new audit before closing.

## 9. Queries Run

| # | Query | Purpose |
| --- | --- | --- |
| 1 | `SELECT * FROM incident.LPUser JOIN incident.LPSecurity ON SecurityID WHERE UserID=50006` | Identify user's current security group + StartAudit value |
| 2 | `SELECT * FROM incident.LPSecurity WHERE StartAudit BETWEEN 1 AND 9` | Find candidate group with create permission + matching ActiveAudits scope |
| 3 | `UPDATE incident.LPUser SET SecurityID=8 WHERE UserID=50006` | Apply fix — reassign user to "Audit Only" |

## 10. Extras / Additional Screenshots

Client-attached screenshot of Kyle Estep's user groups in Secure admin UI — [See Jira attachment / link in ticket].
