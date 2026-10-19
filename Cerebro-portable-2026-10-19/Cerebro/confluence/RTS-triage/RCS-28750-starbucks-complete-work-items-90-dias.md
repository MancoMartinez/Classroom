---
ticket: RCS-28750
cliente: Starbucks Coffee Company (NA)
analista: Diego Buelvas
estado_ficha: Resolved (Closed)
sintoma: pedido de completar en bloque los Work Items sin asignar con mas de 3 meses
causa: sin defecto, mantenimiento administrativo, dos Work Items sin asignar desde 2026-06-03
fix: UPDATE directo a StatusID=3 con AbandonReasonID=11 y nota
nota_reutilizable: los codigos de abandon reason no son tabla SQL fija, salen de un Excel por tenant, hay que resolver el ID antes de ejecutar
confluence_id: 478175657988
modificado: 2026-09-03
fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478175657988
---

# RCS-28750 — Starbucks: Request to "Complete" Work Items older than 90 days

Prepared: 03 September 2026 | Analyst: Diego Buelvas | Status: Resolved (Closed)

## 1. Ticket Details

| Field | Value |
| --- | --- |
| Ticket | RCS-28750 |
| Customer | Starbucks Coffee Company (NA) North America |
| Issue Type | Incident |
| Priority | Low |
| Status | Closed |
| Opened | 03 September 2026 |
| Reporter | Erik Figueroa (efiguero@starbucks.com) |
| Assignee | Diego Buelvas (dbuelvas@apprissretail.com) |
| Jira URL | https://trebuco.atlassian.net/browse/RCS-28750 |

## 2. Problem Statement

Client requested a bulk "Complete" of all UNASSIGNED Work Items created more than 3 months ago, using completion reason "Admin Only - Do Not Use" and note "Abandoned due to age." Reference: saved search "Unassigned WIs older than 3 mos" under Public to Administration to Work Items.

## 3. Client Profile

| Field | Value |
| --- | --- |
| Client | Starbucks Coffee Company (NA) North America |
| Application | Secure — Work View module |
| ARDM / SnowTime client | NOT AVAILABLE — Secure tenant is separate from SnowTime; legacy pyardm client `c166sbx` exists but has no dbt/ARDM relevance to this ticket |
| Snowflake schema | N/A — no Snowflake/ARDM component involved |

## 4. Investigation

### 4.1 Scope confirmation

Confirmed which `StatusID` represents "Unassigned" per Secure's `StatusTypes` enum (0 Unassigned, 1 Assigned, 2 AttachedToCase, 3 Abandoned, 4 InFactboard) — matches the ticket's explicit "UNASSIGNED" wording; no other StatusID in scope.

PASS.

### 4.2 Match volume validation

```sql
SELECT StatusID, COUNT(*) AS Cnt, MIN(CreatedDateTime) AS Oldest, MAX(CreatedDateTime) AS Newest
FROM workview.Workview
WHERE StatusID = 0
  AND CreatedDateTime <= DATEADD(MONTH, -3, GETUTCDATE())
GROUP BY StatusID;
```

PASS. Only 2 rows matched, both created 2026-06-03 — right at the 3-month cutoff.

### 4.3 Identify matching Work Items

PASS. Identified `Id 149910` and `149912`, Headline "Benefits - Receiving Partner Single Week High Volume Bean Markouts", Category "Benefits-Weekly".

### 4.4 Completion reason resolution

Resolved the completion reason code for "Admin Only - Do Not Use." Reason codes are tenant-specific, sourced from a per-tenant reference workbook (`/system/workview/referencedata/wokview enumerations.xlsx`, sheet `WorkviewAbandonReason`) rather than a fixed SQL table. Confirmed with operator: ID = 11 for the Starbucks tenant.

PASS.

### 4.5 Fix execution

```sql
UPDATE workview.Workview
SET StatusID = 3,
    AbandonReasonID = 11,
    AbandonReasonNotes = N'Abandoned due to age.',
    ActionedDateTime = GETUTCDATE()
WHERE Id IN (149910, 149912)
  AND StatusID = 0;
```

PASS. Both Work Items transitioned to `StatusID=3` with the requested reason and note. Client confirmed in their WI view ("Looks good on my end, thanks!").

## 5. Root Cause Statement

| Field | Detail |
| --- | --- |
| What broke | Nothing — no defect. Routine admin housekeeping request. |
| Why | Two auto-generated Work Items sat Unassigned since 2026-06-03, aging past the client's internal 90-day cleanup threshold. |
| Scope | 2 Work Items, tenant-wide search (no Headline/Category restriction). |
| Business impact | Minimal / cosmetic. |
| Evidence | Pre-fix count query returned exactly 2 matching rows; post-fix client confirmed via UI. |

## 6. Additional Findings

Completion/abandon reason codes in Secure are not a fixed SQL lookup table — they are read per-tenant from an uploaded Excel reference file (`WorkviewAbandonReason` sheet), via `WorkviewService.GetWorkviewAbandonReasons()`. Any future "complete WI with reason X" request must resolve the reason ID per-tenant before executing — it cannot be assumed to match across clients.

## 7. Recommended Fix

### Option A — Direct UPDATE (Applied)

Mirrors the pattern used in prior Alo Yoga mass-clearing tickets (StatusID to 3 direct UPDATE). Followed by a Nuke Cache Clear if the UI doesn't refresh immediately (not required here).

## 8. Open Questions

No open questions — ticket resolved.

## 9. Queries Run

| # | Query | Purpose | Result |
| --- | --- | --- | --- |
| 1 | COUNT by StatusID with 3-month cutoff | Validate match volume before acting | 2 rows matched |
| 2 | SELECT Id, Headline, Category | Identify exact Work Item IDs | Id 149910, 149912 |
| 3 | UPDATE workview.Workview SET StatusID=3 | Apply the fix | 2 rows updated, client-confirmed |
