# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Correction

The summary reads as a broken quick link. It is not. The report definition, the join and the filter literals are all correct. The source table stopped receiving data on 30 March 2025 and the report enforces a rolling 60 day window, so the window never intersects the data that exists. Do not spend time on the searchable.

## 2. Environment and steps to reproduce

Environment: Production. `apps.apprissretail.com/walmart-usa/platform`, tenant walmart-usa, client 300. Query engine is Snowflake.

### Walmart (WMT), reported 2026-08-27 by Steve Curry, reproduced 2026-08-31 by Support

1. Log in to Portal, Secure Store, Explorer, Composer.
2. Open Quick Links, tab Refund Audit, entry `Refund Audit - Expired`.
3. Set `EXT_INKIRU_RVA Store No` equal to `3238`.
4. Set `HEADER Trading Day` between `2020-01-01` and `2026-08-31`. The customer used `2026-01-01` to `2026-08-27`. Both return the same result.
5. Run. Read the Tabular tab.

Expected: rows for store 3238. Walmart internal reporting shows 16 expired audits for that store in WM Week 27 of 2026, out of 77 total audits.

Actual: `0 results`, `No Results Found`. No error is raised. Screenshots `image-20260827-113306.png` and `image-20260827-113328.png`, attached by the reporter on 2026-08-27.

Reproduced with a Support account. The customer account is not a factor.

## 3. Findings

### The generated SQL

```sql
set inkirustoreno = 3238;
set tradingday = '2020-01-01';
set tradingday1 = '2026-08-31';
set auditresult = 'expired';

SELECT T3.storeno, T3.audit_result, COUNT(DISTINCT T3.tc_nbr)
FROM ardm_Header AS T1
LEFT JOIN ardm_RecalledTransaction AS T2
  ON (T1.TransactionID = T2.TransactionID AND T1.TradingDay = T2.TradingDay)
LEFT JOIN inkiru_rva AS T3
  ON (T2.x_TCNumber = T3.tc_nbr)
WHERE
((T1.TradingDay BETWEEN CAST('2026-07-02T00:00:00' AS DATE) AND CAST('2026-08-31T23:59:59' AS DATE)))
AND
(T3.storeno = $inkirustoreno AND T1.TradingDay BETWEEN $tradingday AND $tradingday1 AND T3.audit_result = $auditresult)
GROUP BY T3.storeno, T3.audit_result
ORDER BY 3 DESC LIMIT 1000
```

Two `TradingDay` filters sit in the same WHERE. The first is not exposed as a parameter. Today is 2026-08-31 and that filter starts on 2026-07-02, which is 60 days back. It is a rolling window the generator recomputes on every run. The effective range is always the last 60 days regardless of what the user asks for.

### Defect 1. The source feed stopped on 30 March 2025

`SELECT COUNT(1), COUNT(DISTINCT storeno), MIN(scanned_time), MAX(scanned_time) FROM inkiru_rva`

| Metric | Value |
|---|---|
| Rows | 31,442,997 |
| Distinct stores | 4,634 |
| Earliest scanned_time | 0005-01-20 11:02:06 |
| **Latest scanned_time** | **2025-03-30 08:11:00** |

Not a single row after 30 March 2025, across 4,634 stores. Per store, checked against four stores from the customer report:

| storeno | rows | non null TradingDay | latest scanned_time |
|---|---|---|---|
| 3062 | 611 | 0 | 2025-03-23 21:00:56 |
| 3238 | 513 | 0 | 2025-03-25 17:07:00 |
| 4470 | 331 | 0 | 2025-03-20 22:13:03 |
| 5693 | 532 | 0 | 2025-03-26 19:29:26 |

All four cut off in the same week. Store 4470 reports 36 expired audits in the customer file and store 5693 reports zero, so the pattern is independent of audit volume. This is tenant wide, not store specific.

**The report has returned zero since roughly May 2025, 60 days after the feed stopped. That is 16 months. It was first reported on 2026-08-27.**

### Defect 2. The rolling 60 day window overrides the user parameter

The user cannot detect defect 1 from the UI. Any range they request is intersected with the last 60 days, so nobody can look far enough back to see that data exists through March 2025 and then stops. The two defects hide each other.

### The SnowTime cutover is not the cause

ENG-2829, `GP10 - WMT300 - Parallel Run`, resolved 2026-07-31. The feed stopped 16 months earlier. Do not attribute this to migration instability.

### Scope

All seven quick links under the Refund Audit folder read `inkiru_rva`. All of them return zero for the same reason. Closing this one covers `Refund Audit`, `Refund Audit - Conducted Own Audit`, `Refund Audit Cashier - Fail`, `Refund Audit Cashier - Fail - Item Missing`, `Refund Audit Supervisor - Fail`, `Refund Audit Supervisor - Fail - Item Missing` and `Refund Audit - Expired`.

### Data quality note, not the cause

`MIN(scanned_time)` returns year 0005 and `TradingDay` is null in 100% of the rows sampled. Same family as ENG-7205, `AuditCompletionDate` reset to 1900-01-01 in `AuditMasterStore`, which also affects Walmart. Any query ordering by `scanned_time` will misreport.

## 4. Troubleshooting performed, and the limits of support access

Performed on 2026-08-31, in this order:

1. Reproduced the failure in Production with a Support account.
2. Pulled the generated SQL from the Composer Query button.
3. Ran four read only queries against Snowflake. Value distribution of `audit_result`, per store row counts for stores 3238, 4470, 3062 and 5693, and table wide counts with min and max `scanned_time`.
4. Reviewed the two prior failures on this same table, RCS-9452 and RCS-17323, and the sibling ticket RCS-28620.

AI assisted. Claude was used for the historical search across Jira and Confluence, for reading the generated SQL and for drafting this note. Every figure above comes from a query run against Production, not from the model.

Conversations outside the ticket: none held yet with Engineering or Data. Steve Curry stated on RCS-28620 on 2026-08-28 that Zack Graas identified an issue during a call with him. That conversation is not documented on any ticket and its scope is unknown.

What Support cannot see: why the INKIRU feed stopped delivering on 30 March 2025, and whether the historical data from 30 March 2025 backwards can be reprocessed once the feed is restored.

## 5. Ruled out. Do not repeat

| Hypothesis | Refutation |
|---|---|
| Case mismatch on the `audit_result` literal | The table stores `success`, `expired` and `fail` in lower case. The literal `'expired'` matches exactly |
| Wrong or missing column name in the searchable | `storeno` resolves. The 2023 rename from RCS-9452 is still in place. The query raises no error |
| User hierarchy or SSO, as in RCS-28380 | Reproduced with a Support account. Same result |
| Date field typed as `System.DateTime` instead of `Sysrepublic.Date` | The generator wraps the literal in `CAST(... AS DATE)`, which truncates the time component |
| Broken join through `x_TCNumber` | Not reachable. `inkiru_rva` has no rows in the filtered window, so the join is never exercised |

## 6. Still open

1. Confirm why the INKIRU refund verification audit feed stopped delivering to `ardm_300.inkiru_rva` on 2026-03-30, and what is required to restore it.
2. Confirm whether the 16 months of missing data can be backfilled once the feed resumes, or whether only forward data will be available.
3. Confirm where the 60 day rolling `TradingDay` filter is defined. If it lives in the tenant searchable XML in `[C300_WMT_Platform].[secure].[Repo]` this is a Delivery change. If the SQL generator injects it, it is a platform defect and needs its own ENG ticket.
4. Zack Graas, please confirm what you found on the call with Steve Curry on 2026-08-28 and whether it covers this ticket as well as RCS-28620.

Related: RCS-28620, same reporter, same week, zero row Composer report. RCS-28602, same tenant, `C300_WMT` raw file count drop, currently Under Delivery Review. RCS-9452 and RCS-17323, prior failures on this same table. RCS-27485, TJX EU, closest precedent where an upstream provider stopped supplying daily files.

Priority Medium, ticket age 4 days, underlying outage 16 months.

Routing: Under Delivery Review, assignee Zackary Graas, label `Support_Data_Team`, Team Ownership `Support (Delivery dep.)`, Sprint `RCS Support Team`.
