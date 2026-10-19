---
ticket: RCS-28595
cliente: Stater Bros / Platform client 423
analista: Diego Buelvas
estado_ficha: Work in Progress
sintoma: piden cambiar el username y correo de un usuario
causa: no hay UI para editar UserName ni Email en una cuenta migrada, el correo es el UPN de ingreso y la pantalla de admin quedo de solo lectura por diseno
fix: escalar a Engineering con el patron de ENG-6555, update pareado de membership.Users e incident.LPUser2 en una transaccion, nunca a mano desde soporte
relacionados: RCS-28080, RCS-28455, RCS-28357, RCS-28166, ENG-6555
confluence_id: 478151770138
modificado: 2026-08-27
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478151770138
---

# RCS-28595 — Stater Bros: Update Username/Email

Prepared: 27 August 2026 | Analyst: Diego Buelvas | Status: Work in Progress

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28595 |
| Customer | Stater Bros |
| Issue Type | SOW |
| Priority | Medium |
| Status | Work in Progress |
| Opened | 26 August 2026 |
| Reporter | Angie Martinez (angie.martinez@staterbros.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28595 |

## 2. Problem Statement

Customer requests that Nathan Molina's platform username and email be changed to `Nathan.MolinaRamirez@staterbros.com`.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client | Stater Bros |
| Platform Client ID | 423 (US region) |
| dbt / ARDM project | None — not a SnowTime/ARDM data client, pure Secure/Platform-DB scope |
| Snowflake schema | NOT AVAILABLE — no ARDM footprint for this client |

## 4. Investigation

### 4.1 dbt/ARDM client scope check

PASS. No client project exists — confirms this is a pure Secure/Platform-DB request, not a data-pipeline issue.

### 4.2 Self-service migration flow applicability

FAIL (not applicable). `docs/03-architecture/features/incident-user-migration.md` only lets an unmigrated legacy Incident user capture an email address once, at first sign-in. It has no path for an admin-initiated username/email change on an already-migrated account.

### 4.3 Precedent ticket review (same customer)

POINT OF FAILURE FOUND. Four prior tickets confirm the same gap: RCS-28080 (no UI — post-migration, email is the sign-in UPN, admin edit screen is read-only by design), RCS-28455 and RCS-28357 (same "update email" request, resolved by direct DB update), RCS-28166 (related account-access issue from the same migration). RCS-28357 explicitly links to internal ticket ENG-6555, which documents the only sanctioned procedure.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | Nothing is broken — no UI exists for Support/admin to edit `UserName`/`Email` on a migrated account |
| Why | Post-Platform-migration sign-in uses the email address as the UPN; the legacy admin edit screen was intentionally made read-only for these fields |
| Scope | Recurring pattern for Stater Bros (4 prior tickets) and any client that went through the Incident to Platform migration |
| Business impact | Low impact if done correctly; high impact if `membership.Users.UserName`/`Email` and `incident.LPUser2.LoginID` are updated out of sync — that desync breaks the user's login entirely |
| Evidence | ENG-6555 documents a paired-update procedure wrapped in a transaction, authored and executed by Engineering (Kiran Vadday), not Support |

## 6. Additional Findings

RCS-28080 establishes the underlying design decision (email = UPN, no self-service edit) that all four related tickets trace back to.

## 7. Recommended Fix

### Option A — Escalate to Engineering via linked internal ticket (Recommended)

Do not hand-edit the database from Support. Open/attach an internal Engineering ticket (same pattern as ENG-6555) requesting the update. Engineering then:

1. Generates the paired `UPDATE` statements for `membership.Users` (`UserName`, `Email`) and `incident.LPUser2` (`LoginID`) from the target `UserID`/`IncidentUserId` — never hand-written.
2. Previews affected rows before applying.
3. Wraps the batch in `BEGIN TRANSACTION`, verifies, then `COMMIT`.
4. Confirms the exact PROD execution time on the ticket.
5. Support closes with the customer once Engineering confirms.

## 8. Open Questions

* Need Nathan Molina's `UserID` / `IncidentUserId` to hand to Engineering.
* Confirm whether the account is Incident-linked (requires the `LPUser2.LoginID` update too) or platform-only.

## 9. Queries Run

No queries on record — no Platform-DB/SQL Server MCP access from this workspace; all checks were repo/Jira-based.
