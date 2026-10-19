---
ticket: RCS-28379
cliente: ADUSA / Delhaize, marca Hannaford
analista: Diego Buelvas
estado_ficha: Work in Progress
sintoma: Case Owner, Case Creator y Assigned To en blanco en casos creados desde el 2026-08-01
causa: dos defectos de la migracion Unification, el script de limpieza de RCS-28135 marco Inactive=1 cuentas activas con correo sufijado, y membership.Users.IncidentUserID quedo con un ID nuevo 50000-50100 que no corresponde al UserID de LPUser2
fix: reactivar las filas de LPUser2 y corregir IncidentUserID, ruta ENG-6555
relacionados: RCS-28135, ENG-6555
confluence_id: 478143512577
modificado: 2026-08-25
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478143512577
---

# RCS-28379 — Delhaize (Hannaford): Case Owner, Case Creator and Assigned To is blank

Prepared: 14 August 2026 | Analyst: Diego Buelvas | Status: WORK IN PROGRESS

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28379 |
| Customer | ADUSA / Delhaize (Hannaford brand) |
| Issue Type | Incident |
| Priority | Medium |
| Status | Work in Progress |
| Opened | 14 August 2026 |
| Reporter | leighann.stubbs@adusa.com |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28379 |

## 2. Problem Statement

Multiple cases in LPMS show no Case Owner, Case Creator, or Assigned To for the Hannaford brand. Example: case at store 8389 (Wells, ME) — Medical Incident, 8/4/2026, all three identity fields blank in both the search grid and the case detail view.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client | ADUSA / Delhaize, brand Hannaford |
| Module | Secure Incident (LPMS) — SQL Server, schemas `incident` + `membership` |
| ARDM version | N/A |
| Related tickets | RCS-28135 (Ahold-Duplicated Users), ENG-6555 (LPUser2 / membership.Users LoginID mismatch) |

## 4. Investigation

### 4.1 Table discovery

PASS. Identified incident.MasterCase as the case header table, with AssignedToID, CaseOwnerID, CreatedBy, PreviousAssignToID.

### 4.2 Case header structure

PASS. No CaseNo text field — case identity is composite (StoreIdent + MasterCaseId); no direct Brand column on the case table.

### 4.3 Brand resolution

PASS. StoreIdent 4688 = Wells, ME (StoreNo 8389) — matches the case in the reported screenshot.

### 4.4 Null-value check

PASS (ruled out). 0 rows with raw NULL owner fields — the affected fields are populated with an ID that fails to resolve to a display name.

### 4.5 Orphan FK check

POINT OF FAILURE FOUND. Cases created 2026-08-01 onward consistently use IDs in the 50000–50100 range, none present in LPUser2.UserID. (Older orphaned rows from 2011–2019 use unrelated legacy IDs — pre-existing noise, out of scope.)

### 4.6 ID-space identification

POINT OF FAILURE FOUND. All 10 IDs matched real, active accounts in membership.Users with Unification migration dedup-suffixed emails — the same duplicate-account pattern reported in RCS-28135.

### 4.7 Cross-check against LPUser2 by email

POINT OF FAILURE FOUND. Matching legacy rows exist under a different UserID (e.g. 11284 vs. membership.Users' 50040) and all have Inactive = 1.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | incident.MasterCase.CaseOwnerID / AssignedToID / CreatedBy resolve to no display name in the Incident UI, for cases created since 2026-08-01 for a subset of ADUSA/Delhaize/Hannaford users |
| Why | Two compounding defects from the Platform Unification migration: (1) incident.LPUser2 rows for genuinely-active users with migration-assigned duplicate-pattern logins (email suffixed 1/2/3) were marked Inactive = 1 by the RCS-28135 bulk-cleanup script, which assumed every suffixed login was an unused duplicate; (2) membership.Users.IncidentUserID was populated with a newly generated ID (50000–50100 range) that does not match the pre-existing incident.LPUser2.UserID for the same person — the same defect class tracked in ENG-6555 |
| Scope | ADUSA/Delhaize, Hannaford brand, cases created 2026-08-01 onward. At least 10 distinct user identities confirmed impacted. Full scope across other ADUSA brands not yet quantified. |
| Business impact | Blank Case Owner/Assigned To/Created By breaks case routing, accountability, and audit trail for LP incident management |
| Evidence | 0 cases with raw NULL owner fields; 10/10 sampled 50xxx IDs matched active membership.Users accounts with suffixed emails; matching LPUser2 rows exist under a different legacy UserID, all Inactive=1 |

## 6. Additional Findings

The disable script run for RCS-28135 (DELETE FROM membership.Users WHERE Email LIKE '%[0-9]@%' + UPDATE incident.LPUser2 SET Inactive=1 WHERE LoginID LIKE '%[0-9]@%') did not distinguish between genuinely-unused duplicate accounts and duplicate-pattern accounts still in active use. This ticket surfaces collateral damage from that script.

## 7. Recommended Fix

### Option A — Escalate to Engineering (Recommended)

1. Reactivate (Inactive = 0) the incident.LPUser2 rows for confirmed-active migration-suffixed accounts, across all ADUSA brands.
2. Correct membership.Users.IncidentUserID to reference the correct pre-existing incident.LPUser2.UserID, for every account affected by the Unification migration.
3. Route through the ENG-6555 owners (Kiran Vadday / Juan Martinez), since this is the same underlying defect class.

No interim workaround identified.

## 8. Open Questions

* Full blast radius across all ADUSA brands is not yet quantified.
* Whether the RCS-28135 disable script run can be audited for a complete list of deactivated accounts.
* Whether the ENG-6555 fix scope already covers this ID-mismatch defect.

## 9. Queries Run

1. INFORMATION_SCHEMA.COLUMNS in schema incident for Owner/Assign/CreatedBy columns — confirmed incident.MasterCase as the case header table.
2. Column list of MasterCase — MasterCaseId, StoreIdent, CreatedBy, AssignedToID, CaseOwnerID, PreviousAssignToID, CreatedDate.
3. Column list of Store — no Brand column; brand implicit in StoreName.
4. incident.Store WHERE StoreName LIKE '%HANNAFORD%' — StoreIdent 4688 matches the reported case.
5. MasterCase JOIN Store filtered to NULL owner fields — 0 rows.
6. LEFT JOIN incident.LPUser2 on the three ID columns — all post-2026-08-01 breakage isolated to the 50000–50100 ID range.
7. membership.Users WHERE IncidentUserID IN (50017, 50026, 50028, 50040, 50046, 50052, 50057, 50058, 50072, 50081) — 10/10 real active accounts with Unification duplicate-suffix emails.
8. incident.LPUser2 by base email pattern — matching rows under different UserIDs, all Inactive=1.

## 10. Extras / Additional Screenshots

Search grid and case detail screenshots showing blank Case Owner / Assigned To / Created By. [See Jira attachment / link in ticket]
