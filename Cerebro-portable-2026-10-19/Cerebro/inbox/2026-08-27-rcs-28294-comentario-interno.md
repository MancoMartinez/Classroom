# INTERNAL NOTE. NOT FOR CUSTOMER

Consolidated escalation package. This replaces the need to read the earlier comments on this ticket.

## 1. Correction

**The explanation support gave the customer on 12 August is wrong.** She was told Smart Alerts fire only when a case is fully saved or completed, and that case `2026-ADUP-40-96` behaved as intended. Both statements fail against the tenant configuration and against her own attachment.

She was right. The case report attached to this ticket shows Case Stage `Pending Report to be Completed`, HR Case Status `Open`, every interview field set to Pending, and the Investigation, Recommendation and Resolution sections empty. The case was never completed. An alert went out anyway.

The customer stated that before the platform move, saving a case triggered the alert regardless of stages marked Pending. That matches the configured filter exactly. Treat her statement as accurate.

**The `relates to ENG-6612` link was removed on 25 August and should not be restored.** ENG-6612 covers attachment handling in Cohesion mode, reached Done, and deployed to production on 4 August, one week before this was reported. One narrow exception applies. HR Alert 10 filters on `RelatedDoc_AttachmentType` and configures Include Attachment Types, so that alert alone touches the pipeline ENG-6612 changed. The reported case does not involve HR Alert 10.

## 2. Environment and steps to reproduce

**Environment: Production.** Vallarta tenant, `/vallarta/nettrack/`. All configuration and database findings below were read in production on 25 August with read only access.

### Preconditions

| Item | Value |
| --- | --- |
| Tenant | Vallarta, production, `/vallarta/nettrack/` |
| Module | ERMS, reached through `NewIncident.aspx` |
| Form | `HRFirstReport.aspx` |
| Alert | HR Alert 1, `SmartAlertConfigID = 14`, System `Case`, Status Active, Begin Date 9/8/2019 |
| Alert Case Types | `Complaints` |
| Effective filter | `Shoplifting_DateReported Is not blank AND HRDetail_HR1 Is not blank` |
| Test account | Any account with `TimeZone = UTC` and `LastLoginDate = NULL`. 308 of 419 accounts qualify |

Two other active alerts carry Case Types `Complaints` and fired on the same case, `ConfigID 16` and `ConfigID 18`.

### Steps

1. Sign in to the Vallarta tenant as an HR user.
2. Open **New Incident**. Select a location. Use store `40`, district `D3` to match the reported case.
3. Select Case Class **Employee Relations**. Select Incident Type **Complaints**. Select a Case Tier.
4. Click Next. The form loads `HRFirstReport.aspx`.
5. Enter the AWD name and the complainant. Write narrative text into the HR detail field that maps to `HRDetail.HR1`.
6. Leave Allegations, Location of Incident and every interview field set to **Pending**. Leave the Investigation, Recommendation and Resolution sections empty.
7. **Save. Do not complete the case. Do not approve it.**
8. Confirm the case sits at Case Stage `Pending Report to be Completed` with HR Case Status `Open`.

### Verification

```sql
SELECT S.CaseNo, S.DateEntered, SAP.SmartAlertConfigID, SAP.RunDate, SAP.RunStatus
FROM incident.Shoplifting S
LEFT JOIN incident.SmartAlertProcess SAP ON SAP.ShopliftingID = S.ShopliftingID
WHERE S.CaseNo = '<new case number>'
```

**Expected:** rows for ConfigIDs 14, 16 and 18. The filter needs only a non blank `DateReported` and a non blank `HRDetail.HR1`. Nothing in the filter references completion.

**Actual:** the outcome varies between cases that satisfy the same filter. See section 3.

**Screenshot:** the case report for `2026-ADUP-40-96` is already attached to this ticket. It documents the stage and status at the time the alert fired.

## 3. Findings

### 3.1 No active alert filters on completion

The tenant holds 19 Smart Alerts. Three active alerts carry Case Types `Complaints`, the Incident Type of the reported case.

| Alert | Email Subject | Filter |
| --- | --- | --- |
| HR Alert 1 | Investigation Open | `Shoplifting_DateReported Is not blank And (HRDetail_HR1 Is greater than '1' Or HRDetail_HR1 Is not blank)` |
| HR Alert 10 | Issue Response Letter | `RelatedDoc_AttachmentType Equals 'HR - Final Response Letter' And AccidentExtra_RelatedToAssociatePersonalItem Equals '1'` |
| HR Alert 13 | Investigation Open - Corporate Employee | `Accident_CumulativeInjury Equals '1'` |

`Shoplifting_CaseStatus` and `Shoplifting_Stage` both exist as available form fields. Both sit unused.

The first filter reduces to `Shoplifting_DateReported Is not blank AND HRDetail_HR1 Is not blank`. A value greater than `1` is a value that is present, so the `Or` collapses into its second term.

Begin Dates run from 2018 to 2025. No alert was reconfigured at the July cutover. The configuration held. The behaviour changed.

### 3.2 The engine ran for the reported case

`incident.SmartAlertProcess` for `2026-ADUP-40-96`:

| ConfigID | ShopliftingID | RunDate | RunStatus | SystemType |
| --- | --- | --- | --- | --- |
| 14 | 48575 | 2026-08-11 14:34:05 | Success | C |
| 16 | 48575 | 2026-08-11 14:34:13 | Success | C |
| 18 | 48575 | 2026-08-11 14:34:22 | Success | C |

`SystemType = 'C'` confirms ERMS cases evaluate through the Case branch.

### 3.3 The gating field is never blank

| Period | Complaints cases | HR1 blank |
| --- | --- | --- |
| Pre cutover | 405 | 0 |
| Post cutover | 39 | 0 |

The effective filter evaluates true for essentially every Complaints case.

### 3.4 A second case produced nothing at all

| | 2026-ADUP-40-96 | 2026-ADUP-45-79 |
| --- | --- | --- |
| ShopliftingID | 48575 | **48786** |
| DateEntered | 2026-08-11 00:23 | 2026-08-18 23:11 |
| Case Stage | Pending Report to be Completed | Pending Summary-HR Investigation Specialist |
| Case Status | Open | Open |
| `HRDetail.HR1` | populated | populated |
| Rows in `SmartAlertProcess` | 3, all Success, ConfigIDs 14, 16, 18 | **zero** |
| RunDate | 2026-08-11 14:34:05 / 13 / 22 | none |

Same tenant. Same Case Type. Same alerts. Same filter satisfied. Seven days apart. One generated three rows. The other generated nothing.

**Zero rows means the engine was never invoked for 48786. That is a different failure from the engine running and the filter evaluating false.** Both failures are present in this ticket and they may have separate causes.

## 4. Troubleshooting performed, and the limits of support access

Order of work:

1. Read the 19 Smart Alert configurations in production and reduced the filter of HR Alert 1 by hand.
2. Compared the customer attachment against the configured filter and established that no active filter references completion.
3. Queried `incident.SmartAlertProcess` for the reported case and confirmed three Success rows.
4. Counted blank `HRDetail.HR1` across 405 pre cutover and 39 post cutover Complaints cases to test whether the gating field explains the variance.
5. Tested whether evaluation moved from synchronous to batch by comparing `DateEntered` distributions.
6. Swept post cutover Complaints cases for any that satisfy the filter and produced no rows, which surfaced `2026-ADUP-45-79`.

**What support cannot determine.** Support holds read access to data. Support does not hold application code or application logs. Two things need engineering eyes:

- `RunStatus = Success` means the process executed. It does not mean mail reached a recipient. The customer reports alerts not received. The send path needs checking separately from the evaluation path.
- Zero rows for `ShopliftingID 48786` cannot be explained from the data layer. It needs the application log for that timestamp.

## 5. Ruled out. Do not repeat

| Hypothesis | Result |
| --- | --- |
| `HRDetail.HR1` gates the alert | Refuted. Zero blanks across both periods |
| Evaluation moved from synchronous to batch | Refuted against `DateEntered`. One hour share 40.3% pre and 34.8% post, inside the margin of error for n=112 |
| Hourly distribution of `RunDate` as a signal | Unusable. 308 of 419 accounts carry a wrong timezone, so the defect contaminates the measurement variable |
| The twelve HR named alerts under System Case are the defect | Refuted. `SystemType = 'C'` confirms ERMS cases evaluate through the Case branch |

## 6. Still open

**What is needed from Engineering, in order:**

1. Diff the execution path between `ShopliftingID 48575` and `ShopliftingID 48786`. Start with the application log around `2026-08-18 23:11` for 48786.
2. Confirm whether `RunStatus = Success` on 48575 corresponds to a delivered message. The customer reports alerts not received.
3. Confirm whether this is already covered by an existing work item. Three candidates below.

**Candidate work items. Support has not confirmed any of these and is not asserting a match.**

| Ticket | Why it is worth checking |
| --- | --- |
| **ENG-7359** | "Smart Alert not working with Quick Entry", High, Backlog, Matthew Kamminga. Its description states that users in Quick Entry do not receive a CPF cookie or authenticate at log in, and that the alert is never created. The zero row outcome on 48786 matches that mechanism. This tenant also carries 308 of 419 accounts with `LastLoginDate = NULL`, meaning those accounts never reach the platform through a browser. Whether case 48786 was created through Quick Entry has not been verified |
| **ENG-2819** | "Smart Alert failing to run in Incident/Audit", Done, resolved in Secure April 2026 Release 2/2. Same observable symptom, nothing written to Smart Alert history. Diagnosed from the application log with `LPSBO.SendHatrJob - Exception in HatrSmartAlert`. That is the log signature worth searching for 48786 |
| **ENG-6541** | "Harden smartalerts functionality", Backlog, Matthew Kamminga. Umbrella item |

**Related support ticket.** RCS-28131 for Sportman carries the same symptom and already sits in Under Engineering Review.

**Carried over and unresolved.** 308 of 419 accounts on this tenant show `TimeZone = UTC` with `LastLoginDate = NULL`. ENG-7236 covers this and has sat in Backlog since 13 August. Vallarta never received the remediation applied to Ahold under RCS-28030. The `STORE HR##` service accounts belong in that set. They never reach the platform through a browser and never self correct.

**Timestamps on this tenant are not reliable as evidence.** The case record shows Date Case Reported `8/10/2026`. The Change History shows the earliest `SAVE.CASE` at `8/11/2026 12:23 AM` on `HRFirstReport.aspx`, with no event at 4:23 PM on 8/10 across its 23 entries. The two differ by exactly 8 hours, which is UTC minus PST. California ran on PDT, minus 7, in August. Confirm which surface renders UTC and which renders local before quoting any timestamp from this tenant.

**Ticket age.** Reported 11 August. 16 days open. Medium priority. The customer has been given a correction and is waiting.
