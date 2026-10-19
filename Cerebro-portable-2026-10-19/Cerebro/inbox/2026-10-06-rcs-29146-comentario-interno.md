**Mass completion done in production for J Crew.** 751 work items completed under the scope the requester confirmed: all open items. Full queries, results and revert path below.

## 1. Environment
Production, J Crew Platform database (`sqldb-prd-wus2-arp-production-154-jcg-platform`). Table `workview.Workview` only. Cases (`incident.*`) untouched.

## 2. Before and after

| StatusID | Meaning | Before | After | Action |
|---|---|---|---|---|
| 0 | Unassigned | 699 | 0 | Completed |
| 1 | Assigned | 52 | 0 | Completed |
| 4 | Investigating | 9 | 9 | Left open, each attached to a factboard |
| Total open | | 760 | 9 | |
| Marked with the ticket note | | 0 | 751 | |

Completed rows carry: StatusID 3, AbandonReasonID 8 (No Problem Found), StandardCompleteReasonID 3, ActionedDateTime set, AbandonReasonNotes `Mass completed per customer request (RCS-29146).` AssignedToUserID was not changed.

## 3. Queries and results, in the order I ran them

### 3.1 Open items by status and assignment
```sql
SELECT StatusID,
       CASE WHEN AssignedToUserID IS NULL THEN 'unassigned' ELSE 'assigned' END AS assignment,
       COUNT(*) AS Cnt,
       MIN(CreatedDateTime) AS oldest,
       MAX(CreatedDateTime) AS newest
FROM workview.Workview
WHERE StatusID <> 3
GROUP BY StatusID,
         CASE WHEN AssignedToUserID IS NULL THEN 'unassigned' ELSE 'assigned' END
ORDER BY StatusID;
```

| StatusID | Assignment | Cnt |
|---|---|---|
| 0 | unassigned | 699 |
| 1 | assigned | 52 |
| 4 | assigned | 9 |

### 3.2 Scope check: cases and factboards
```sql
SELECT StatusID,
       CASE WHEN CaseID IS NULL THEN 0 ELSE 1 END AS withCase,
       CASE WHEN FactboardID IS NULL THEN 0 ELSE 1 END AS withFactboard,
       COUNT(*) AS Cnt
FROM workview.Workview
WHERE StatusID <> 3
GROUP BY StatusID,
         CASE WHEN CaseID IS NULL THEN 0 ELSE 1 END,
         CASE WHEN FactboardID IS NULL THEN 0 ELSE 1 END
ORDER BY StatusID;
```

| StatusID | withCase | withFactboard | Cnt |
|---|---|---|---|
| 0 | 0 | 0 | 699 |
| 1 | 0 | 0 | 52 |
| 4 | 0 | 1 | 9 |

Scope for the UPDATE: StatusID 0 and 1 with no CaseID and no FactboardID, 751 rows. The 9 StatusID 4 rows stay open because completing them could orphan investigations in progress.

### 3.3 Does a "case item" object exist
```sql
SELECT TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE '%Case%';
SELECT TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE COLUMN_NAME LIKE '%Case%' ORDER BY TABLE_SCHEMA, TABLE_NAME;
```
Result: no CaseItem table. Secure Incident cases live in `incident.*`, and the UI shows 3 open cases. Reading "case items" as Work View items is a hypothesis, stated as such in the reply to the requester.

### 3.4 Who holds the assigned items
```sql
SELECT AssignedToUserID, StatusID, COUNT(*) AS Cnt, MAX(AssignedToDateTime) AS last_assignment
FROM workview.Workview
WHERE StatusID IN (1,4)
GROUP BY AssignedToUserID, StatusID
ORDER BY Cnt DESC;
```
Result: 61 assigned items across 12 users. Only one item was assigned recently (2026-09-10). The rest are months old.

### 3.5 Reason list for this tenant
```sql
SELECT DISTINCT EnumerationType, [Key], Value
FROM secure.EnumerationReferenceData
WHERE EnumerationType = 'WorkviewAbandonReason'
ORDER BY [Key];

SELECT * FROM workview.AbandonReason ORDER BY ID;
```

| Key | Value |
|---|---|
| 8 | No Problem Found |
| 11 | No Coaching Needed |
| 50 | Case Created |
| 51 | Equipment Issue (Prevented Investigation) |
| 52 | Policy Violation (Referred for C/A) |
| 53 | Training Issue (Referred DM/HR) |

The legacy table `workview.AbandonReason` only holds IDs 1 to 10. The tenant list changed on 2026-07-16 via https://trebuco.atlassian.net/browse/RCS-27570. The runbook ID 11 is "No Coaching Needed" here, so I did not use it.

### 3.6 How this tenant closes items today
```sql
SELECT AbandonReasonID, StandardCompleteReasonID, COUNT(*) AS Cnt
FROM workview.Workview
WHERE StatusID = 3
GROUP BY AbandonReasonID, StandardCompleteReasonID
ORDER BY Cnt DESC;

SELECT TOP 20 ID, AbandonReasonID, StandardCompleteReasonID, AbandonedDateTime, ActionedDateTime
FROM workview.Workview
WHERE StatusID = 3
ORDER BY ActionedDateTime DESC;
```

| AbandonReasonID | StandardCompleteReasonID | Cnt |
|---|---|---|
| 5 | 4 | 715 |
| 8 | 3 | 483 |
| 7 | 5 | 221 |
| 10 | 1 | 102 |
| 9 | 6 | 30 |
| 4 | 6 | 11 |
| 1 | 6 | 10 |
| 6 | 4 | 4 |
| 51 | 4 | 3 |

Findings: reason 8 always pairs with StandardCompleteReasonID 3. The 20 most recent closes (2026-07-23 to 2026-09-15) are mostly reason 8 with ActionedDateTime set and AbandonedDateTime NULL. A UI close fills ActionedDateTime and leaves AbandonedDateTime NULL, so my first filter on AbandonedDateTime returned an empty set and I discarded it.

## 4. Backup
The login has no CREATE TABLE permission (Msg 262), so a `SELECT INTO` copy was not possible. I saved the rows to be changed as a CSV with a plain SELECT and "Save Results As":

```sql
SELECT ID, StatusID, AssignedToUserID, AbandonReasonID, AbandonReasonNotes,
       AbandonedDateTime, ActionedDateTime, StandardCompleteReasonID
FROM workview.Workview
WHERE StatusID IN (0,1) AND CaseID IS NULL AND FactboardID IS NULL
ORDER BY ID;
```

File: `backup-pre-update-20261006.csv`, 751 data rows (699 StatusID 0, 52 StatusID 1). All reason fields were NULL before the change. It is stored in my ticket folder for RCS-29146. The same WHERE clause as the UPDATE guarantees the CSV holds exactly the rows touched.

## 5. UPDATE
```sql
SELECT HAS_PERMS_BY_NAME('workview.Workview', 'OBJECT', 'UPDATE') AS can_update;

BEGIN TRANSACTION;

UPDATE workview.Workview
SET StatusID = 3,
    AbandonReasonID = 8,
    AbandonReasonNotes = N'Mass completed per customer request (RCS-29146).',
    ActionedDateTime = GETUTCDATE(),
    StandardCompleteReasonID = 3
WHERE StatusID IN (0,1) AND CaseID IS NULL AND FactboardID IS NULL;

SELECT @@ROWCOUNT AS rows_updated;
-- 751: COMMIT TRANSACTION;
-- any other number: ROLLBACK TRANSACTION;
```

| Check | Result |
|---|---|
| can_update | 1 |
| rows_updated | 751 |

The count matched the CSV, so I ran `COMMIT TRANSACTION`.

## 6. Post-change checks
```sql
SELECT @@TRANCOUNT AS open_transactions;

SELECT StatusID, COUNT(*) AS Cnt FROM workview.Workview WHERE StatusID <> 3 GROUP BY StatusID;

SELECT COUNT(*) AS marked
FROM workview.Workview
WHERE AbandonReasonNotes = N'Mass completed per customer request (RCS-29146).';
```

| Check | Result |
|---|---|
| @@TRANCOUNT after the UPDATE, before COMMIT | 1 |
| @@TRANCOUNT after COMMIT | 0 |
| Open items | StatusID 4 = 9 rows, nothing else |
| marked | 751 |

The first verification ran in the same session as the UPDATE, so it showed uncommitted data. The numbers above are from after the COMMIT.

## 7. Troubleshooting performed
The procedure follows the RTS how-to https://trebuco.atlassian.net/wiki/spaces/RTS/pages/123297955891 with these changes:

| Runbook | This run | Why |
|---|---|---|
| Unassigned items older than 90 days | All open items, StatusID 0 and 1 | The requester confirmed all open items |
| Reason ID 11 | Reason 8 with StandardCompleteReasonID 3 | Tenant reason list changed in https://trebuco.atlassian.net/browse/RCS-27570 |
| Full table copy with `SELECT INTO` | CSV of the 751 rows | No CREATE TABLE permission |
| IDs table | Unique note plus the CSV | Same revert capability without creating a table |

Errors hit along the way:
- Msg 156: I used `backup` as a column alias, which is a reserved word. The batch failed to compile and nothing ran.
- Msg 262: CREATE TABLE denied, which led to the CSV backup.
- Transaction left open after the first UPDATE attempt: found with `@@TRANCOUNT` = 1 and committed after the 751 check.

Claude proposed the scope split and the reason mapping. I ran every query, read the recent completions and the tenant reason list myself, saved the CSV, ran the UPDATE in a transaction, saw 751 rows and committed. No conversations outside this ticket so far.

## 8. Revert
Filter on `AbandonReasonNotes = N'Mass completed per customer request (RCS-29146).'` and restore from the CSV. Per ID, restore StatusID (0 or 1) from the CSV and set AbandonReasonID, AbandonReasonNotes, AbandonedDateTime, ActionedDateTime and StandardCompleteReasonID back to NULL, which is how all 751 rows were before.

## 9. Still open
1. The requester wrote "case items", not work items. My reply states that reading.
2. Impersonate a tenant user and confirm their "new" work items no longer show. The CSV gives the count that user had before.
3. Does anyone see a reason to treat the 9 investigating items differently?
