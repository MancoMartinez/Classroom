**Escalating to Secure Engineering.** On 16 October J.R. asked for engineering review of this ticket and customer priority treatment. He did not ask for a fix date.

## 1. Correction

Izenda reporting and the blank Security ID defect in https://trebuco.atlassian.net/browse/RCS-29451 are separate tracks. No common root cause is demonstrated. The twenty minute and one hour waiting times mentioned on the 16 October call followed a discussion of Ahold. They are not TBI measurements.

## 2. Environment and steps to reproduce

**Environment:** Production. Tailored Brands, Client ID 209, tenant tbi.

```
Database: sqldb-prd-wus2-arp-production-209-tbi-platform
Path:     /tailoredbrands/nettrack/AdHoc/reportlist.aspx
```

### Tailored Brands (TBI), reported 14 October 2026 by Colton Neal

1. Open /tailoredbrands/nettrack/AdHoc/reportlist.aspx through an authenticated Incident session.
2. Open Open Investigations with its saved filters. Record the filter values. The failing run's full values are unavailable.
3. Try the Excel export.
4. Edit the September cases report to Fiscal October, 4 to 31 October 2026. The customer calls it 2026 Cases by Month. The timeout URL identifies Cases MTD September. The saved report identity is unconfirmed.

Expected: the list, the report and the export complete without errors. No target duration is documented.

Actual: the list takes 2 to 5 minutes and a report another 2 to 4. Users see blank pages after the error, failed exports and server errors. Source: https://trebuco.atlassian.net/browse/RCS-29060?focusedCommentId=3396117

Screenshots on https://trebuco.atlassian.net/browse/RCS-29060: `image-20261014-154021.png` shows the server error. `image-20261014-160957.png` shows HTTP 524 at 2026-10-14 16:07:16 UTC.

## 3. Findings

| Finding | Status | Source |
|---|---|---|
| Report list 2 to 5 minutes, report open 2 to 4 more, Excel export fails | **verified as customer report**, not measured by support | https://trebuco.atlassian.net/browse/RCS-29060?focusedCommentId=3396117 |
| Vedant on 23 September: reports loaded for him, the application overall was too slow | verified, partial support reproduction | https://trebuco.atlassian.net/browse/RCS-29060?focusedCommentId=3361084 |
| Also slow or erroring: Closed Investigations 2026 Summary, Closed Cases 2026, 2026 Cases Summary, Cases MTD September | verified as customer report | https://trebuco.atlassian.net/browse/RCS-29060?focusedCommentId=3374260 |
| This ticket has no attachments. Originals sit in RCS-29060 and RCS-28256 | verified in Jira on 16 October | https://trebuco.atlassian.net/browse/RCS-29060 and https://trebuco.atlassian.net/browse/RCS-28256 |
| Talos lead: performance flags and dedicated report routing | **unverified, from AI triage**. Effective values unread | Talos comment 3396516 on this ticket |
| ENG-9990 tracks Incident slow load times. Backlog, unassigned on 16 October. Izenda coverage unconfirmed | verified status, unverified scope | https://trebuco.atlassian.net/browse/ENG-9990 |

## 4. Troubleshooting performed, and the limits of support access

The Talos triage and Claude proposed the flag lead and extracted the evidence. I reviewed the Jira history, the original screenshots and the 16 October call with J.R. and Matt myself. I ran no new timed production reproduction and collected no server trace. I have not read the effective flag values or request level timings. Could Engineering evaluate the flag lead?

Conversations outside the ticket: the 16 October call with Tailored and the internal call with J.R. and Matt. Matt considered the screenshots sufficient for Izenda review. He also said TBI feels slower than other clients. That is an impression, not a measurement.

## 5. Ruled out so far

| Hypothesis | Status |
|---|---|
| WAF block | A 524 screenshot does not establish one |
| Common cause with the Security ID defect in https://trebuco.atlassian.net/browse/RCS-29451 | No evidence links them |
| Common cause with https://trebuco.atlassian.net/browse/ENG-9990 | Not proven |
| Flags already correct | `Feature.Incident.EnableAdHocInitCaching` and `Feature.Incident.EnableAdHocPerRequestUserScope` read True on 10 August in https://trebuco.atlassian.net/browse/RCS-28256?focusedCommentId=3283895. That says nothing about today |

## 6. Still open

1. Does the 524 come from report or SQL execution, or from timeout handling in front of it?
2. What are today's effective values for the Izenda performance flags and the dedicated report routing on tenant tbi?
3. Does https://trebuco.atlassian.net/browse/ENG-9990 cover Izenda reporting, and who owns it?
4. Who owns this review, and when is the next update?
