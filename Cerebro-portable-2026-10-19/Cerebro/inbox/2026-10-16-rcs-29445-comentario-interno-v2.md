**Escalated to Secure Engineering.** J.R. requested engineering review on 16 October and customer priority treatment. **No fix date was promised.** Jira now shows Under Engineering Review, assigned to Shandana Khan.

## 1. Correction

Izenda reporting and the blank Security ID defect in [RCS-29451](https://trebuco.atlassian.net/browse/RCS-29451) are separate investigation tracks. No common root cause is demonstrated. The twenty-minute and one-hour waiting narrative on the call followed a discussion of Ahold. Do not use it as a TBI measurement.

## 2. Environment and steps to reproduce

**Environment:** Production. Tailored Brands, **Client ID 209**, tenant tbi. Reporter: Colton Neal.

```yaml
Database: sqldb-prd-wus2-arp-production-209-tbi-platform
Path: /tailoredbrands/nettrack/AdHoc/reportlist.aspx
```

### Tailored Brands, reported 14 October 2026

1. Open the report-list path through an authenticated Incident session.
2. Open **Open Investigations** with the saved filters. Record the values; the complete failing-run filter values are unavailable.
3. Try the Excel export and check whether a file downloads.
4. Edit the September cases report to Fiscal October, 4 to 31 October 2026. Colton calls it **2026 Cases by Month**. The timeout URL identifies **Cases MTD September**. Confirm the saved report identity.

**Expected:** the list, report and export complete without server errors. No response-time target is documented.

**Actual:** Colton reports 2 to 5 minutes for the list, another 2 to 4 for a report, intermittent blank pages, failed exports and server errors. These are customer timings, not new support measurements.

**Screenshots:** `image-20261014-154021.png` shows a server error; `image-20261014-160957.png` shows **HTTP 524 at 2026-10-14 16:07:16 UTC**. Both are on [the original customer report](https://trebuco.atlassian.net/browse/RCS-29060?focusedCommentId=3396117).

## 3. Findings

| Finding | Evidence status | Source |
| --- | --- | --- |
| Multi-minute list/report loads, failed export and edit timeout | Verified as customer report | [Colton, 14 October](https://trebuco.atlassian.net/browse/RCS-29060?focusedCommentId=3396117) |
| Vedant could load reports and observed overall slowness | Partial support reproduction, 23 September | [Internal observation](https://trebuco.atlassian.net/browse/RCS-29060?focusedCommentId=3361084) |
| Closed Investigations 2026 Summary, Closed Cases 2026, Cases Summary and September MTD also affected | Customer reports; outcomes differ by report | [1 October](https://trebuco.atlassian.net/browse/RCS-29060?focusedCommentId=3374260), [14 October](https://trebuco.atlassian.net/browse/RCS-29060?focusedCommentId=3396117) |
| RCS-29445 has no attachments of its own | Verified in Jira, 16 October | Originals in [RCS-29060](https://trebuco.atlassian.net/browse/RCS-29060) and [RCS-28256](https://trebuco.atlassian.net/browse/RCS-28256) |
| Performance flags and dedicated report routing | **Investigation lead from AI triage. Current values unverified** | [Talos note](https://trebuco.atlassian.net/browse/RCS-29445?focusedCommentId=3396516) |
| ENG-9990 tracks Incident slow load times | Backlog, unassigned on this read; **Izenda coverage unconfirmed** | [ENG-9990](https://trebuco.atlassian.net/browse/ENG-9990) |

## 4. Troubleshooting performed, and the limits of support access

Reviewed the ticket history and original reporting screenshots. Crosschecked Colton's reported timings against the dedicated ticket description and Vedant's earlier observation. AI assisted extraction, comparison and drafting. Talos proposed the flag and routing lead; no effective production settings were verified in this review.

**No new timed production reproduction, HAR, server trace or request-to-SQL correlation was collected.** Current flag values, routing and exact failing saved-report identity remain open. Screenshots preserve the error and timestamp; they do not identify the root cause.

**Conversations outside Jira:** the customer call and internal call with J.R., Matt and Juan on 16 October. The supplied internal transcript is automatic, with inferred speakers. Matt considered the screenshots sufficient to submit an Izenda-focused review. He also observed TBI feeling slower than other clients; that is not a timed measurement. J.R. requested escalation and customer priority treatment.

## 5. Ruled out so far

| Interpretation | Evidence limit |
| --- | --- |
| WAF block | A 524 identifies a timeout; the screenshot does not establish a security block. |
| Same cause as blank Security ID or ENG-9990 | **Not established.** Track and validate separately. |
| Disabled AdHoc flags explain the current issue | `Feature.Incident.EnableAdHocInitCaching` and `Feature.Incident.EnableAdHocPerRequestUserScope` were True on 10 August. That is historical evidence, not today's effective state. See [the recorded check](https://trebuco.atlassian.net/browse/RCS-28256?focusedCommentId=3283895). |

## 6. Still open

1. Correlate the October 14 report endpoint and timestamp with report execution, SQL duration and timeout handling. Where does the time go?
2. Read today's effective performance flags and dedicated report routing for tenant tbi. Evaluate the AI lead before proposing configuration changes.
3. Confirm whether ENG-9990 covers Izenda and identify the engineering issue for this reporting review.
4. Name the review owner and next update. **Do not infer a fix date from J.R.'s review request.**
