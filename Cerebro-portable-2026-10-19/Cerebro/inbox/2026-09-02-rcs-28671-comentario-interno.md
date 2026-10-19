# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Root cause found, and the scope number

@Viraj Kansara @Valerie Cerezo @J.R. Teagle, this answers both the quantification question and
Denver's email.

**Scope: 17 work items, all created on 28 August 2026 between 12:05 and 13:07. Zero on every other
day from 1 August through 2 September.** On 28 August the tenant generated 50 work items and 17 came
out without transaction data. This is a single window, not an ongoing fault.

**Cause: the work items were created without their underlying event records.** The instant analytics
result exists and the work item counts its events. The transaction rows were never written.

**The failure is intermittent, not tied to any definition.** This matters for where the ticket goes
next, so the evidence is in section 2.4. Eight different definitions were hit, healthy runs of the
same definitions sit between the failures, and I do not believe the six blocked searches explain it.

## 2. Evidence

I reproduced the failure on 2 September at 18:14:20 UTC under my own support account, so this is not
specific to the reporting user. My exception, UserToken 5baeb119-3d7b-4552-8fae-fa7a7427b130:

```
System.Exception: The Events relating to this instant analytics result could not be found.
   at Sysrepublic.Secure.Core.InstantAnalytics.InstantAnalyticsService.GetInstantAnalyticsEvents(Guid ftiID, Guid tileID, JObject parameters)
   in Sources\Core\Core\Instant Analytics\Core\InstantAnalyticsService.cs:line 306
   at PlatformUI.Areas.Viewer.Controllers.ApiController.InstantAnalyticsEventsAsync(String sourceApp, Guid ftiID, Guid tileID)
   in Sources\UI\PlatformUI\Areas\Viewer\Controllers\ApiController.cs:line 156
```

Component Core.InstantAnalytics.InstantAnalyticsService, sender GetInstantAnalyticsEvents.

Work item 248159 in workview.Workview:

| Field | Value |
|---|---|
| Headline | MD03-APS-D, Consecutive Markdowns for Same Payment Card |
| CountOfEvents | 3 |
| PotentialValue | 0 |
| StatusID | 1 |
| LocationID | 7135 |
| CreatedDateTime | 2026-08-28 12:17:46 |
| Period | 2026-08-27 to 2026-08-27 |
| FtiID | D1D505D6-9285-46F2-A115-497A48878D92, created 2026-08-28 12:17:28 |

`SELECT COUNT(*) FROM fti.Transactions WHERE FtiID = 'D1D505D6-9285-46F2-A115-497A48878D92'`
returns **0**.

The work item claims 3 events. The event table holds none for it. That is exactly what the exception
reports.

Method for the count, so anyone can rerun it. Join workview.Workview to fti.AnalysisResults on
WorkViewID, then look for FtiIDs with no rows in fti.Transactions. Group by CreatedDateTime.

### 2.4 The failure is intermittent

Grouping the 28 August runs by definition shows the same definitions producing both healthy and
empty work items.

| Definition | Generated | Without events |
|---|---|---|
| ext1 - sku velocity at sco by xref | 26 | 7 |
| liv5 - line item voids - employee last name match | 4 | 3 |
| md03-cit-d - consecutive markdowns for same payment card | 2 | 2 |
| com1 - same name refunds for com orders | 2 | 1 |
| denver - mkd2 - back-to-back manually entered markdowns | 1 | 1 |
| liv3 - line item voids - employee name match | 1 | 1 |
| snr1 - same name refunds - account name match | 1 | 1 |
| snr3 - same name refunds - nrr store credit name match | 1 | 1 |
| liv17 - high frequency daily line item voids | 6 | 0 |
| com12 - same name bopis locker orders v2 | 5 | 0 |
| sls4 - gift card amount equals markdown amount | 1 | 0 |

EXT1 is the clearest case. Twenty six work items from one definition in one run, nineteen of them
fine and seven empty.

The timeline shows healthy runs interleaved with the failures:

```
12:05:32  liv3     empty
12:05:35  sls4     ok
12:05:52  mkd2     empty
12:05:59  liv5     empty x3
12:06:21  liv17    ok x6
12:07:06  com12    ok x5
12:07:57  ext1     empty 7 of 26
12:14:19  snr1     empty
12:17:46  md03     empty x2
13:06:45  snr3     empty
13:06:49  com1     empty 1 of 2
```

No definition is broken. Something transient prevented the event rows from being written during that
window, and it hit by instant rather than by work item type.

## 3. Answering Denver's two questions

Denver asked J.R. by email on 2 September whether we can share how many work items are impacted, and
whether the affected items will need regenerating.

On the count: 17, all from 28 August. That is a small enough set that a targeted note to the owners
of those work items beats a broad field communication. I am pulling the list of the 17 with their
definitions, stores and assignees so the message can be aimed.

On remediation: the transaction rows do not exist for these work items, so displaying them requires
producing the events again. I am not stating regeneration as the plan until Engineering confirms the
mechanism. What I can say is that no fix applied to a search definition will populate events that
were never written.

This also corrects what support would otherwise have told Corey. Regenerating is likely to be part
of the answer, and the earlier framing that the stored artifact was intact was wrong on this point.
The work item record is intact. Its events are not.

## 4. Environment and steps to reproduce

Environment: USPROD, client 85, C085_THD.

Originally reported by Ericka Smith on 1 September at 15:20, Canada Field Team.

1. Open the work item viewer at the tenant host: `homedepot.apprissretailcloud.com/platform/viewer#/store/live/fti/d1d505d6-9285-46f2-a115-497a48878d92?wi=248159`
2. The Events page loads with the Transactions panel empty.
3. The page returns "There has been a system error. Please contact support."
4. Click Show Me Details for the tracking code, then open the exception in Control Panel.

Expected: the Transactions panel lists 3 transactions, matching CountOfEvents.

Actual: empty panel and the exception in section 2.

Reproduced under a support account on 2 September at 18:14:20 UTC. Ericka reproduced it on
1 September under hers, tracking code 774fbb98-fc34-4cd0-8ee8-538f85d2967d.

## 5. Ruled out. Do not repeat

| Hypothesis | Why it fell |
|---|---|
| A SQL compilation error like the original search defect | The exception is an application level Events not found, not an invalid identifier |
| Work item generation failed | Failed 0 across the 50 most recent markdown runs |
| Deaggregation failed for this item | Both requests on run 2706EDE9 carry Failed 0 |
| The generated SQL is persisted and stale | DeaggregationSql is NULL throughout in THD |
| Store 7135 is missing from the location catalogue | place.Location row 7135 exists. AURORA, country CA, open, last updated 2026-07-31 |
| Canada lost its location hierarchy | LocationHierarchy4 is NULL for all 3169 active locations across all 24 divisions, US included. THD does not use level 4 |
| Specific to the reporting user or her permissions | Reproduced under a support account |

## 6. Troubleshooting performed

All queries were read only against sqldb-prd-wus2-arp-production-085-thd-platform. No definition was
opened for editing.

AI assistance was used to review the ticket history, to correlate this ticket with DO-12041 and
RCS-28543, and to build the queries above.

No conversations about this ticket took place outside the ticket.

## 7. Still open

1. Do we know of anything that ran or broke in C085_THD on 28 August between 12:05 and 13:07. Section 2.4 rules out a definition level cause, so the answer is more likely infrastructure or a transient service fault during work item generation.
2. What rewrites the event rows for these 17, and who runs it. THD is waiting on this one.
3. @Simon Smith, I do not think the six blocked searches explain this. Confirm if you disagree, since that would send the ticket somewhere else.
4. Whether snr4 - same name refunds - pro xtra name match gets its own ticket. It carries 4 real deaggregation failures out of 15 across 27 and 28 August, and nobody has raised it.

## 5. Cause confirmed, and WISC rerun tested

@Simon Smith confirmed 28 August was the SnowTime cutover for C085_THD, a full database swap. That
lines up exactly with the window in section 2.4 and closes the cause. Credit to Dan Endersby's team,
who led that cutover.

I tested whether WISC's rerun repairs an affected work item. Target: 248158, snr1 - same name
refunds - account name match, unassigned, so no one's queue was at risk.

Baseline before the rerun: work item 248158, FtiID 81EBBBE5-19F3-4D28-A691-05C7AA134F29, 0 rows in
fti.Transactions.

Reran the definition for 27 August in WISC. Result: 824 results, 1 gen, 823 skip. Checked the work
item afterward. Still 0 events, same FtiID, no duplicate created.

Ran it a second time to confirm. Same outcome. 0 results, 0 gen.

**WISC does not repair this.** It deduplicates against the existing work item and skips it rather
than repopulating its events. Simon flagged going in that dedup logic exists but he did not know the
mechanics, and this is the mechanics. No duplicate risk, and no fix either.

This now points to the SnowTime cutover itself rather than a rerun mechanism support can run.
Recommending this route to Dan Endersby's team, since they own the cutover this traces to.

Holding the ticket in Work in progress until someone confirms where it lands.

## 8. Related

DO-12041 SnowTime C085_THD Testing and Verification, In Development, Simon Smith.

RCS-28543 Kinney Drugs KNY/179, Under Engineering Review. Different failure mode. Keeping the link
because both trace to the same SnowTime migration path.
