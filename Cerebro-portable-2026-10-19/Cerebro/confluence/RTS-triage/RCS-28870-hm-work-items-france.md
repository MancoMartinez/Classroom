---
ticket: RCS-28870
cliente: H&M / c127_ham (EU)
analista: Diego Buelvas
estado_ficha: Work in Progress
sintoma: usuarios no ven Work Items para Francia, los nuevos aparecen como ya completados
causa: cierre masivo del 2026-03-31 con AbandonReasonID=38, codigo inexistente en la tabla de lookup, mato la generacion de la carpeta lex profile work items
fix: redirigir a las definiciones global vivas y escalar a Engineering la regla Refunds que no tiene sustituto
confluence_id: 478193647652
modificado: 2026-09-10
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478193647652
---

# RCS-28870 — H&M: Users Unable to See Work Items for France

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28870 |
| Customer | H&M |
| Issue Type | Incident |
| Priority | Medium |
| Status | Work in Progress |
| Opened | 10 September 2026 |
| Reporter | Karen Merrylees (karen.merrylees@hm.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28870 |

## 2. Problem Statement

H&M users Karen Merrylees and Luc Marcil report seeing no Work Items for France, despite having what they believe are correct permissions/locations/teams. SE user Kelly Murray sees historical Work Items but no new ones — new items appear as if already completed.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client ID (dbt) | c127_ham |
| Region | EU |
| ARDM Version | NOT AVAILABLE — Secure app / Work View issue, not ARDM/dbt |
| Snowflake Schema | NOT AVAILABLE |
| Active Product | Work View / EBR Instant Analytics Work Items |

## 4. Investigation

### 4.1 Location Hierarchy Assignment Check

Query: `secure.LocationHierarchyUserAssignments` for Karen, Luc, Kelly UserIDs.

PASS (partial). Luc Marcil has a correct explicit H&M/FR assignment. Karen Merrylees has no France assignment (only H&M/IE, H&M/GB) — a real gap, but secondary: it does not explain why Luc (who IS correctly assigned) also sees nothing.

### 4.2 Location String Mismatch Check

Query: DISTINCT LocationHierarchy1, LocationHierarchy2 from place.Location for H&M/FR.

PASS. String matches exactly ('H&M'/'FR') — rules out the string-mismatch pattern seen in RCS-28519/RCS-28811.

### 4.3 Work Item Data Inspection (screenshot IDs)

Query: workview.Workview for IDs 62462–62465 (the items shown in the ticket screenshot).

FINDING. StatusID=0, LocationID populated, CreatedDateTime=2026-02-24 — 7 months old, belonging to the legacy "lex profile work items" folder.

### 4.4 Generation Timeline Check

Query: top 20 most recent rows by CreatedDateTime for that same VirtualFilePath.

POINT OF FAILURE FOUND. All rows StatusID=3, AbandonReasonID=38, last CreatedDateTime=2026-03-31. Work Item generation for this definition stopped entirely five months before the ticket.

### 4.5 Client-Wide Generation Scope Check

Query: MAX(CreatedDateTime) grouped by VirtualFilePath, scoped to H&M.

FINDING. All 3 definitions under "lex profile work items" died on 2026-03-31. A parallel folder, "global hm refund work items", is mostly alive through 2026-09-08 — except its own "Refunds" definition, which stopped earlier (2026-03-03 overall, 2025-03-17 for France).

### 4.6 Abandon Reason Validation

Query: workview.AbandonReason lookup for ID=38, then full table scan.

POINT OF FAILURE FOUND. AbandonReasonID=38 does not exist in the lookup table (valid range is 1–10). This is an orphaned code from an untracked migration/cleanup script, not a legitimate business abandon reason.

### 4.7 Global Replacement Coverage Check — Gift Cards

Query: global hm refund work items/high amount cash cards tendered by credit card.fti, filtered to France.

PASS. Actively generating France Work Items weekly through 2026-09-08 — a live substitute exists for this rule.

### 4.8 Global Replacement Coverage Check — Refunds

Query: global hm refund work items/refunds to the same payment card...fti, filtered to France.

FAIL. Last France row: 2025-03-17. No live substitute exists for this specific business rule, in any folder.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | Work Item generation for the legacy "lex profile work items" folder (3 definitions, including the 2 named in this ticket) |
| Why | A bulk-closure event on 2026-03-31 abandoned all pending items using AbandonReasonID=38, a code absent from the workview.AbandonReason lookup table — consistent with an untracked migration/cleanup script, likely tied to the rollout of the parallel "global hm refund work items" folder. Root cause is NOT permissions or location hierarchy. |
| Scope | All 3 "lex profile work items" definitions, all countries, since 2026-03-31. The Refunds business rule additionally has no working successor anywhere — its global version stopped for all countries on 2026-03-03, and for France specifically as far back as 2025-03-17. |
| Business impact | France LP users have received zero actionable Refunds Work Items since the rule died, and Gift Cards/other legacy-folder rules are stale unless users are redirected to the live global definitions. Investigators may incorrectly conclude there is no ongoing risk activity in these categories. |
| Evidence | See Section 9 — Queries Run |

## 6. Additional Findings

* Karen Merrylees has no France entry in secure.LocationHierarchyUserAssignments (only IE/GB) — a real provisioning gap, independent of the root cause, worth remediating regardless.
* Karen Merrylees and Luc Marcil both have SecurityID = NULL in membership.Users, vs. Kelly Murray's SecurityID = 9. Anomalous; impact on other functionality not confirmed — flagged for Delivery review.

## 7. Recommended Fix

### Option A — Redirect to live global definitions (Recommended for Gift Cards)

Confirm with Delivery/Engineering whether "lex profile work items" was deliberately superseded by "global hm refund work items". If confirmed, redirect Karen's, Luc's, and Kelly's Work View dashboard/Category configuration to the live global definitions (already generating France data through 2026-09-08).

### Option B — Restore Refunds generation (Required — no live substitute exists)

Escalate to Engineering to investigate and restart generation for "refunds to the same payment card with original tender different card no," globally. Neither the legacy nor the global definition has produced Work Items since March 2026.

Additionally: investigate the source of the 2026-03-31 bulk-abandon event (AbandonReasonID=38) to prevent recurrence, and separately remediate Karen Merrylees' missing France location hierarchy assignment.

## 8. Open Questions

* Was the "lex profile work items" to "global hm refund work items" migration deliberate and documented? (Delivery/Engineering to confirm)
* Why did the global Refunds business rule itself stop generating for all countries in March 2026? (Engineering to investigate)
* Does the SecurityID = NULL anomaly on Karen's and Luc's accounts affect other functionality? (Delivery to review)

## 9. Queries Run

1. Users lookup:

```sql
SELECT UserID, FirstName, LastName, Email, SecurityID, PrimaryLocationID, UserStoreNo, Disabled, Deleted
FROM membership.Users
WHERE Email IN ('karen.merrylees@hm.com','luc.marcil@hm.com','kelly.murray@apprissretail.com')
   OR (FirstName + ' ' + LastName) IN ('Karen Merrylees','Luc Marcil','Kelly Murray');
```

Result: Karen/Luc: SecurityID NULL; Kelly: SecurityID=9

2. Location hierarchy assignments:

```sql
SELECT UserId, HierarchyId, LocationId, LocationHierarchy1, LocationHierarchy2, LocationHierarchy3,
       LocationHierarchy4, LocationHierarchy5, LocationHierarchy6, HierarchyUserAssignmentId
FROM secure.LocationHierarchyUserAssignments
WHERE UserId IN ('863FAC2F-D632-47EB-B778-3842846434DF','935808F6-BAF5-437E-BAA4-3F16DE784686','5EB42FEA-C3C2-4067-8D32-C3AE162BBE97');
```

Result: Luc has H&M/FR; Karen has H&M/IE, H&M/GB, no FR

3. Location string check:

```sql
SELECT DISTINCT LocationHierarchy1, LocationHierarchy2
FROM place.Location
WHERE LocationHierarchy1 = 'H&M' AND LocationHierarchy2 IN ('FR', 'France');
```

Result: Exact match 'H&M'/'FR'

4. Screenshot WI IDs:

```sql
SELECT TOP 1 * FROM workview.Workview WHERE ID = 62462;
```

Result: StatusID=0, LocationID=2500047, CreatedDateTime=2026-02-24

5. Recent rows for lex profile Refunds definition:

```sql
SELECT TOP 20 ID, StatusID, LocationID, AssignedToUserID, SnoozeDateTime, CreatedDateTime,
       AbandonedDateTime, AbandonReasonID, ResolutionDateTime
FROM workview.Workview
WHERE VirtualFilePath = '/system/ebr/instant analytics/definitions/lex profile work items/refunds to the same payment card with original tender different card no.fti'
ORDER BY CreatedDateTime DESC;
```

Result: All StatusID=3, AbandonReasonID=38, last 2026-03-31

6. Client-wide generation scope:

```sql
SELECT w.VirtualFilePath, MAX(w.CreatedDateTime) AS LastCreated, COUNT(*) AS TotalRows
FROM workview.Workview w
JOIN place.Location l ON l.LocationID = w.LocationID
WHERE l.LocationHierarchy1 = 'H&M'
GROUP BY w.VirtualFilePath
ORDER BY LastCreated DESC;
```

Result: lex profile folder dead 2026-03-31; global folder alive to 2026-09-08 except Refunds def (dead 2026-03-03)

7. Abandon reason lookup (specific): `SELECT * FROM workview.AbandonReason WHERE ID = 38;` Result: 0 rows

8. Abandon reason lookup (full): `SELECT * FROM workview.AbandonReason ORDER BY ID;` Result: Only IDs 1–10 exist

9. Global Refunds definition, France: last row 2025-03-17

10. Global Gift Cards definition, France: active weekly, last row 2026-09-08

All queries executed against SecureAppDb (SQL Server) manually by the operator — no SQL Server MCP available in this session.

## 10. Extras / Additional Screenshots

Screenshot in ticket: Work View "New Work Items" screen, filtered Country=FR, showing Gift Cards/Refunds cards dated February 2026 ("7 months ago"), consistent with the frozen "lex profile work items" folder. [See Jira attachment / link in ticket]
