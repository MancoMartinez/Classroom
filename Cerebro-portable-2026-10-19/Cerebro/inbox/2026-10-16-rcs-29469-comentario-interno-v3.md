**Supplementing the existing Secure Engineering investigation.** Colton supplied follow-up files for [RCS-29451](https://trebuco.atlassian.net/browse/RCS-29451) and [ENG-10069](https://trebuco.atlassian.net/browse/ENG-10069). **Do not treat this follow-up as proof of a separate defect or create a duplicate engineering issue automatically.**

## 1. Correction

Talos could not read the attachments or recover the prior investigation. Its lack of a matching precedent does not invalidate the published Rachel evidence. Matt has now posted the SSO+ process in the meeting chat, as supplied by Juan. His written explanation is no longer pending.

## 2. Environment and steps to reproduce

**Environment:** Production. Tailored Brands, **Client ID 209**, tenant tbi.

```yaml
Database: sqldb-prd-wus2-arp-production-209-tbi-platform
UI: Portal > Settings > Users > Secure Incident
Source: Appriss Incident Security ID Examples.xlsx
```

### Customer examples supplied 16 October 2026

1. Open Jacinta Titus, Emeldia Pryor, Christi Winters, Rahim Mehdiyev or Cheneria Chevalier under Users.
2. Open Secure Incident and inspect Incident Security ID.
3. Compare the user with the supplied teams, permissions and locations files, then the effective SSO+ level and account state.

**Expected:** the configured level applies when the user signs in through SSO.

**Actual:** all five profiles show no selected level in the workbook screenshots. **This is attachment evidence, not a fresh production reproduction.** A last-login timestamp does not establish account creation or a first-login failure.

## 3. Findings

| Example | Brand / Location in CSV | Team / Group | Evidence |
| --- | --- | --- | --- |
| Jacinta Titus | KNG / 314 | Location Manager / ApprissCase Users | Blank level in workbook; present in all three CSVs |
| Emeldia Pryor | KNG / 706 | Location Manager / ApprissCase Users | Same observations |
| Christi Winters | TMW / 1604 | Location Manager / ApprissCase Users | Same; earlier investigation recorded persistent level 5 from April |
| Rahim Mehdiyev | TMW / 4151 | Location Manager / ApprissCase Users | Blank level in workbook; present in all three CSVs |
| Cheneria Chevalier | JAB / 761 | Location Manager / ApprissCase Users | Same; last-login screenshot shows January 2026 |

Source: the three `appriss_sso_*_20261014*.csv` attachments and the workbook on [RCS-29469](https://trebuco.atlassian.net/browse/RCS-29469). Inspected all 29 embedded images. The workbook's empty cells do not mean its image-based evidence is empty.

**Matt's written process:** customer teams CSV contains email and team. The loader truncates and reloads `sso.teams`, looks up team text to a numeric securityid and replicates to `sso.SecurityLevelAssignments`. Expected output is **one row per user**, used at SSO login. This documents intended behavior; no TRUNCATE or production repair was executed during this investigation.

**Chris:** locations CSV line 301 contains `Brand=SSU`, `Location=2005`. The earlier SSO+ row held `90002005`, dated 13 October. The supplied CSV is dated 14 October. It does not contain that literal code for Chris. **Match the consumed batch before attributing the prefix's origin.** Colton confirmed 40002005 as the correct location; Juan manually assigned it. Successful incident creation after that correction still needs confirmation.

**Empty locations:** 111 rows have no Location, all in teams other than Location Manager. Validate intended regional, district or administrative hierarchy before declaring these invalid store assignments.

## 4. Troubleshooting performed, and the limits of support access

Crosschecked the original CSVs, workbook images, previous SQL and Grafana findings, Ryan's Teams replies and the 16 October call with Matt and J.R. AI assisted extraction and drafting. **No fresh production account check, loader trace or controlled login test was executed in this review.**

The [published Rachel timeline](https://trebuco.atlassian.net/browse/RCS-29451?focusedCommentId=3397050) records level 5 before account creation, followed by a NULL account SecurityID while groups and team applied. Her next login preserved a manual correction; it does not prove automatic second-login recovery.

**Conversations outside Jira:** Ryan's 15 October Teams replies, the customer call and the internal Matt/J.R./Juan call on 16 October, plus Matt's subsequent written SSO+ explanation supplied by Juan. No direct permalink to that final chat message was provided. Ryan said it appears we add the 9; Matt requested the original file. The precise transformation remains unverified.

The historical security-level insertion timestamp was 13 October. Matt mentioned inserts on the 15th without a recoverable table name. Neither a successful replication task nor a filename establishes which file reached SSO+.

## 5. Ruled out so far

| Interpretation | Evidence limit |
| --- | --- |
| Five users absent from the supplied files | They are present with Location Manager and ApprissCase Users. Ingestion and application still require validation. |
| All five are first-login failures | Their creation and login sequences have not all been established. |
| A second login or replacing 9 with 4 fixes everyone | Neither is a validated general remedy. Store numbers can occur under multiple brands. |
| Adding Security ID to the locations file is an approved workaround | Matt rejected it as a simple fix and described the existing teams-based implementation. |

## 6. Still open

1. Compare CSV, `sso.teams`, text-to-ID lookup, `sso.SecurityLevelAssignments` and account state at login for the five examples. Preserve ingestion and login timestamps.
2. Check Matt's expected row count. Clarify how historical and manual `Persistent` rows interact with the one-row expectation before calling extra rows defective.
3. Confirm ENG-10069 coverage for existing accounts such as Christi; append validated examples to the existing investigation.
4. Trace Chris's SSU+2005 through the loader for the same batch, and confirm the corrected account can create an incident.
5. Identify the exact table and query behind Matt's 15 October observation. Support's [published offer of manual level assistance](https://trebuco.atlassian.net/browse/RCS-29451?focusedCommentId=3397054) remains the recorded workaround. **No bulk correction is approved.**
