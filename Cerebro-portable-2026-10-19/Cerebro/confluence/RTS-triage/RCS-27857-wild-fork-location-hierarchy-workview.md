---
ticket: RCS-27857
cliente: Wild Fork Foods
analista: Diego Buelvas
estado_ficha: WORK IN PROGRESS, fix aplicado pendiente de confirmacion
sintoma: usuarios restringidos a una tienda ven Work Items de las 287 ubicaciones
causa: ningun grupo tenia el permiso appliesto sobre la data policy location.mandatorycondition, sin ese permiso el bloque de condicion no se escribe y la clausula WHERE nunca se agrega
fix: otorgar appliesto al grupo EBR Store Users desde Secure Admin, Permissions
nota_reutilizable: si otro cliente reporta lo mismo, correr primero el EXEC de diagnostico, 0 filas confirma la misma causa
tags: data-policy
relacionados: RCS-27517
confluence_id: 478143381525
modificado: 2026-08-25
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478143381525
---

# RCS-27857 — Wild Fork: Location Hierarchy Not Working in Work View

Prepared: 05 August 2026 | Analyst: Diego Buelvas | Status: WORK IN PROGRESS (Pending Client Confirmation)

Tags: `data-policy`

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-27857 |
| Customer | Wild Fork Foods |
| Issue Type | Incident |
| Priority | Medium |
| Status | WORK IN PROGRESS |
| Opened | 16 July 2026 |
| Reporter | Sean Parello (sean.parello@wildfork.ca) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-27857 |

## 2. Problem Statement

Wild Fork Foods reported that users with a Location Hierarchy restricted to a single store (e.g., Kristan Higgins — store 8910) were seeing Work Items from all 287+ locations in Work View instead of only their assigned store. The issue affected all store-level users. Initially linked to RCS-27517, re-opened by the client on 31 July 2026.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client | Wild Fork Foods |
| Application | Appriss Retail — Secure |
| Affected Feature | Work View — New Work Items (unassigned) |
| Affected Group | EBR Store Users |
| Affected Users | 95 users in `secure.LocationHierarchyUserAssignments` |
| Tested User | Kristan Higgins — store 8910 |

## 4. Investigation

### 4.1 User Hierarchy Assignment — Legacy Table

PASS (context). 0 rows in `structure.LocationHierarchyMemberUsers` for the tested user. Ruled out: the function `GetAllLocationsByUserIDHierarchyID` reads from `structure.LocationUsers` directly and correctly resolves store 8910.

### 4.2 User Hierarchy Assignment — New Table

PASS. 1 row — HierarchyID=1, LocationHierarchy2='Canadian', LocationId=8910. Correctly assigned to a single store.

### 4.3 Location Resolution Function

PASS. Returns LocationID=8910 only — the function works correctly.

### 4.4 Work View Items — LocationID Population

PASS. 64 distinct LocationIDs, all populated. Work Items carry their store's LocationID.

### 4.5 Data Policy Groups Check

```
EXEC membership.GroupsInPermissionsByVirtualFilePathAndPermissionNamesSelect
    '/system/datapolicy/workview/location.mandatorycondition', 'appliesto'
```

POINT OF FAILURE FOUND. 0 rows returned. No group has the `appliesto` permission on the Work View location data policy. Without this grant, the `IsUserInLocationHierarchy` SQL condition block is skipped at runtime (`DoNotWriteConditionBlock = true`) and the mandatory WHERE clause is never added — all items pass through to every user.

### 4.6 Data Policy Repo Object Verification

PASS (exists). Object ID = `F6F15DE8-B5A5-450E-BCFA-43AD3364EEC0`. The policy object exists; it was never granted to any group.

### 4.7 Permission Record Verification

FAIL. 0 rows. The `appliesto` permission record for this data policy did not exist.

### 4.8 Target Group Identification

PASS. The tested user belongs to Basic Users, EBR Store Users (`3095FB0C-3C63-4B31-A1BD-8D76F4595838`), Everyone. EBR Store Users identified as the correct target group.

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | Data policy `/system/datapolicy/workview/location.mandatorycondition` was not enforced for any user group |
| Why | No group had the `appliesto` permission on the data policy's `secure.Repo` object. The `IsUserInLocationHierarchy` SQL generator checks for this permission before writing the location WHERE clause — without it, the condition block is entirely skipped and all Work Items are returned. |
| Scope | All EBR Store Users (95 users) since initial Wild Fork configuration |
| Business impact | Store-level users could view Work Items from all 64 locations, fully bypassing the location hierarchy restriction |
| Evidence | 0 rows from data policy groups EXEC; 0 rows from `membership.Permission` for the ObjectID; 287 results visible to a single-store user before fix |

## 7. Recommended Fix

### Option A — Grant appliesto Permission to EBR Store Users (APPLIED)

Via Secure Admin, Permissions UI: create and assign the `appliesto` permission on `/system/datapolicy/workview/location.mandatorycondition` to group EBR Store Users.

Status: Applied via UI on 05 August 2026. Verified using impersonate view — only Work Items for store 8910 are now visible. Pending client confirmation.

Note for similar cases: if another client reports the same symptom (store users see all locations in Work View), run the diagnostic EXEC first. 0 rows means the same root cause; apply the same permission grant to their equivalent store user group.

## 8. Open Questions

1. Awaiting confirmation from the client that the fix works for all affected users.

## 9. Queries Run

| # | Query | Outcome |
| --- | --- | --- |
| 1 | structure.LocationHierarchyMemberUsers for the user | 0 rows — not in legacy table |
| 2 | secure.LocationHierarchyUserAssignments for the user | 1 row — LocationId=8910 |
| 3 | structure.GetAllLocationsByUserIDHierarchyID(user, 1) | Returns 8910 only |
| 4 | DISTINCT LocationID from workview.Workview WHERE StatusID IN (0,1) | 64 locations, all populated |
| 5 | EXEC GroupsInPermissionsByVirtualFilePathAndPermissionNamesSelect ... 'appliesto' | 0 rows — POINT OF FAILURE |
| 6 | secure.Repo WHERE VirtualFilePath = the data policy | F6F15DE8-B5A5-450E-BCFA-43AD3364EEC0 |
| 7 | membership.Permission WHERE ObjectID = ... AND Name='appliesto' | 0 rows — permission did not exist |
| 8 | Groups query via membership.Groups + GroupMembers | EBR Store Users identified |

## 10. Extras / Additional Screenshots

Screenshot showing the user's Work View with 287 results from multiple stores despite the single-store restriction. [See Jira attachment — RCS-27857]
