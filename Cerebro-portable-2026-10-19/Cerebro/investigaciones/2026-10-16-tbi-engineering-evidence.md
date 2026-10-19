# Internal technical evidence. Tailored Brands. 16 October 2026

Production. Client ID 209, tenant tbi. Database sqldb-prd-wus2-arp-production-209-tbi-platform.

This appendix preserves the evidence behind the two internal notes. Attach it when handing off the investigation. It does not claim that an attachment, transition or message has already been posted. The performance and access tracks have no demonstrated common root cause.

## A. Izenda reporting: RCS-29445

### Scope and concrete failures

Colton Neal reported continued reporting problems on 14 October in RCS-29060, comment 3396117. Report list loading takes 2 to 5 minutes. Opening Open Investigations takes another 2 to 4 minutes. Excel export sometimes produces no download. The report displays server errors; acknowledging the error may leave a blank page. Repeated attempts sometimes work.

The report list path is /tailoredbrands/nettrack/AdHoc/reportlist.aspx. Screenshots show ReportViewer.aspx and ReportDesigner.aspx beneath the same AdHoc path. Enter through an authenticated Incident session. No exact report GUID, fresh HAR, browser version, failing-request trace or production SQL correlation was collected in this session.

Affected reports include Open Investigations Summary, Closed Investigations 2026 Summary, Closed Cases 2026, 2026 Cases Summary and September Cases MTD. The customer describes editing 2026 Cases by Month September to Fiscal October, 4 to 31 October 2026. The timeout screenshot's URL identifies a saved Cases MTD September report. Confirm the report identity before reproducing the edit path. Do not silently treat the two labels as identical.

Customer reproduction:

1. Open the Izenda report list through Incident.
2. Open Open Investigations Summary with the saved filters. The complete failing filter values were not recorded. A successful support screenshot on 23 September shows Stage Investigation and CaseStatus Open; do not assume those are the exact October failing values.
3. Export to Excel and inspect whether a file arrives.
4. Edit the September saved report and set the stated Fiscal October range.

Expected: report list, report content and requested export complete without server errors. No contractual response-time target was found.
Actual: the reported multi-minute loads, intermittent server errors and failed export or edit. The 14 October screenshot records a 524 at 16:07:16 UTC. The screenshot is a timestamp anchor; the upload time and filename do not identify the exact start of the request.

### Evidence and prior support reproduction

https://trebuco.atlassian.net/browse/RCS-29060?focusedCommentId=3361084
Vedant, 23 September, internal: reports load for him and the overall application is too slow. His screenshots show report output. This is partial support reproduction, not an assertion that he reproduced every customer error or measured the customer timings.

https://trebuco.atlassian.net/browse/RCS-29060?focusedCommentId=3374260
Colton, 1 October: Open Investigations timeouts, slow list, Cases MTD September sometimes loads, Closed Investigations loads with an error, Cases Summary loads slowly. Five screenshots preserve the individual observations.

https://trebuco.atlassian.net/browse/RCS-29060?focusedCommentId=3396117
Colton, 14 October: list and report timings, Excel export failure and report edit timeout. Attachments image-20261014-154021.png and image-20261014-160957.png show the server error and 524 respectively.

https://trebuco.atlassian.net/browse/RCS-29060
The 22 September original description includes image-20260922-211934.png, Open Investigations Summary with a server-side error; image-20260922-212640.png, a report that partially loads; image-20260922-213544.png, a 524 on the report list path. Inspect original attachments before extracting case details. The investigation does not require copying employee allegations or report narratives into a new note.

RCS-29445 has no attachments of its own in the live read. Its Duplicate link currently points to RCS-29060, which is itself Duplicate and points to RCS-28256. The customer has an open dedicated reporting case. This link chain does not establish a shared cause and must not hide the original screenshots from Engineering.

### Historical fixes and limitations

RCS-28256, comment 3283895, 11 August: an earlier sign-in and incident-creation timeout had been reported resolved for the users contacted. Izenda remained affected. Feature.Incident.EnableAdHocInitCaching and Feature.Incident.EnableAdHocPerRequestUserScope had been checked True on 10 August. Feature.Incident.EnableBlobAppendLogging was False, and its expected value remained open.

https://trebuco.atlassian.net/browse/RCS-28256?focusedCommentId=3283895

RCS-28256, comment 3335408, 8 September: the support investigation recorded the screen-label caching fix and effective flags, with continued customer transition delays. The August release did not establish resolution of all symptoms. This is historical configuration evidence, not a new 16 October read.

https://trebuco.atlassian.net/browse/RCS-28256?focusedCommentId=3335408

Talos internal note 3396516 on RCS-29445 suggests checking the performance flags and dedicated report routing. Treat this as an investigation lead. It did not confirm effective production values. Do not present toggling a flag, increasing a timeout or enabling dedicated routing as a verified fix.

ENG-9990 tracks Incident slow load times. Shandana separated it from ENG-7182 on 14 October because a relation was not established. Do not assume ENG-9990 covers Izenda without review. The older LPUser query-plan regression and the report failures are not proven to have the same current cause.

### 16 October call and escalation

The supplied transcript has inferred speakers and automatic transcription errors. At 12:36 to 15:46, the participants review the dedicated Izenda ticket, server errors and 524. Matt considers the screenshots adequate if the escalation focuses on Izenda. J.R. asks for Waiting for Engineering, assignment to Shandana and a note that this is a customer priority. J.R. refers to an engineering-review commitment for 16 October; he does not promise a fix that day.

Matt independently says TBI feels slower than other clients. That observation does not provide request-level timing or root cause. The detailed twenty-minute and one-hour waiting story follows a discussion of Ahold. The Lunar React call awaiting Jim's availability also appears within that discussion. Do not use those as TBI measurements or assign that scheduling task to Juan.

On the current read RCS-29445 is Medium, Work in progress, Vedant. Customer priority language in the call is not a Jira priority change. The transition available to the authenticated user is Waiting for Engineering, ID 231; it leads to Under Engineering Review. The current escalation procedure assigns Secure/Incident Engineering to Shandana and documents automatic ENG creation. Verify the resulting link after the human transition; no automation was exercised by the agent.

Ask Engineering to correlate the concrete October 14 endpoint and timestamp with application and query execution, investigate effective configuration and routing, distinguish list/viewer/designer/export paths, confirm scope against ENG-9990 and identify the owner and next update. Do not wait for all missing diagnostics before submitting the evidence Matt already accepted; gather targeted traces in parallel as requested by the investigator.

## B. Access evidence: RCS-29469, RCS-29451 and ENG-10069

### Four customer attachments

The 16 October follow-up contains:

appriss_sso_locations_20261014024505.csv: 4094 data rows, 4094 unique usernames. Columns Username, Company, Brand, DeptDescrShort, Zone, Region, District, Location.

appriss_sso_teams_20261014034500.csv: 4094 data rows, 4094 unique usernames, the same users as locations. Team values: Location Manager 3983, District Manager 82, Regional Manager 16, Field Loss Prevention 8, Administrators 5.

appriss_sso_permissions_20261014014506.csv: 4241 data rows, 4075 unique usernames and one exact duplicate row. 51 users in locations have no permissions row. Those 51 are not a diagnosed failure population; expected access needs validation. All five workbook examples have the expected group row.

Appriss Incident Security ID Examples.xlsx: No Security Incident ID and Emails sheets, 29 embedded PNG images. Cells are empty; visual content is not empty. A cell-only extraction or index cannot substitute for reviewing the images.

### Five customer examples

Jacinta.Titus@kgstores.com: Brand KNG, Location 314, Location Manager, ApprissCase Users. Profile screenshot has no selected Incident Security ID. Last-login screenshot shows 3 June 2026.

Emeldia.Pryor@kgstores.com: KNG, 706, Location Manager, ApprissCase Users. Blank level in the screenshot. Last login 15 May 2026.

Christi.Winters@menswearhouse.com: TMW, 1604, Location Manager, ApprissCase Users. Blank level in the screenshot. Last login 14 July 2026. The earlier investigation recorded persistent level 5 from 17 April and requires separate analysis from new October accounts.

Rahim.Mehdiyev@menswearhouse.com: TMW, 4151, Location Manager, ApprissCase Users. Blank level in the screenshot. Last login 16 September 2026.

Cheneria.Chevalier@josabank.com: JAB, 761, Location Manager, ApprissCase Users. Blank level in the screenshot. Last login 2 January 2026. Do not label this a first-login reproduction from the available evidence.

These are source-file and screenshot observations. No fresh SQL check for these five accounts was performed in the current session. Last login is not creation date and does not prove inactive employment. Mike explained that store users may sign in only once or twice a year.

### Existing engineering anchor

https://trebuco.atlassian.net/browse/RCS-29451?focusedCommentId=3397050

Rachel.Dill@menswearhouse.com had level 5 in sso.SecurityLevelAssignments loaded at 2026-10-13 10:42 UTC. At 19:23:49 UTC her first SSO sign-in created the account with SecurityID NULL. The sequence shows groups and the Location Manager team assigned afterwards. The recorded current sso.GetUserSecurityLevel result returns 5. There is no trace establishing the exact code branch responsible. The absence of a security-level log line is not proof by itself that a branch did not execute.

Juan manually set Rachel's level on 14 October. Her subsequent sign-in preserved 5. That does not prove a second sign-in repairs an unmodified account. Nine observed creation histories were consistent with a later-login pattern; they were not a controlled universal repair test. The historical cohort of 49 accounts with positive feed level and NULL account level is not a verified current incident count or 49 proven first-login cases.

Matt previously confirmed that assignment should work at creation and subsequent logins and requested an engineering issue, now ENG-10069. In the 16 October call he again supports Engineering investigation when the data exists and is not picked up. Confirm scope for returning users rather than creating another first-login ENG.

https://trebuco.atlassian.net/browse/RCS-29451?focusedCommentId=3397054

Published support commitment: Engineering is reviewing the blank-level reports and Support can set the level for additional reported users. The comment does not approve a bulk update, promise a fix date or prove that any of the five newly delivered examples has been corrected.

### Teams to security level design

At 01:22 to 02:53 and 18:05 to 19:03, Matt describes the implemented design as team-file load into SSO+ teams followed by replication into security-level assignments. Team and level names must match exactly. He rejects adding the ID to the locations file as a simple workaround and says changing the design would redo the implementation. J.R. drops that larger change. Matt offered a written explanation of the requirements. Juan subsequently supplied the text Matt posted in the meeting chat on 16 October: the customer teams file is truncated and loaded into sso.teams; the team text is looked up to a numeric securityid and replicated into sso.SecurityLevelAssignments; this should produce one row per user, used whenever the user signs in through SSO. This fulfills the write-up commitment. There is no direct chat permalink in the supplied evidence.

This written design is not a code audit of the current SnowTime transformation or a new production observation. The stated truncate/load behavior is not an instruction for Support to run TRUNCATE. Check row cardinality and ask how manual Persistent assignments are handled before declaring extra rows defective. The live level catalog, exact match behavior, duplicates and override precedence still require inspection. The five examples all say Location Manager in the supplied file; presence alone does not prove effective security level in the account.

### Chris and the 9 prefix

The locations CSV, line 301, supplies Chris.Orth@tailoredbrands.com with Brand SSU, Location 2005 and Zone CORPORATE. Company is blank. Teams line 301 supplies Location Manager; permissions line 319 supplies ApprissCase Users. No Location value in this CSV starts with 9000.

The investigation observed 90002005 in sso.LocationHierarchyMembers with an insertion timestamp of 13 October 10:42 UTC. Colton confirmed 40002005, #2005 MW TUX DC, as Chris's correct location in RCS-28256 comment 3396106. Juan manually added the persistent correct assignment. The October 16 screen shows that assignment, not proof of successful incident creation.

https://trebuco.atlassian.net/browse/RCS-28256?focusedCommentId=3396106

The supplied CSV is named for 14 October. It is not proven to be the consumed source of the row loaded on 13 October. The evidence disproves a literal 90002005 in this supplied Chris record. It does not yet identify the exact component that produced the historical row.

Ryan's 15 October Teams replies say it appears we add the 9, advise against assuming a replacement with 4, and leave the correct DC representation open. He says TBI moved to SnowTime and that he has not been involved with its change process. Matt initially interprets the SSO+ record as customer feed data and explicitly asks to see the original file at 33:40. Do not convert either person's interpretation into a confirmed origin.

The historical comparison found 266 TBI-domain users across 32 unmatched 9000xxxx codes and 4000xxxx counterparts in the location master. This is an older database observation, not the same population as the new CSV. Store 2005 exists under multiple brand prefixes in the historical investigation; a bulk replacement can choose the wrong brand.

### Empty location values

The CSV has 111 empty Location values. All belong to District Manager, Regional Manager, Field Loss Prevention or Administrators teams. None belongs to Location Manager. 337 rows have Brand SSU: 92 with an empty Location and 245 with a nonempty Location across 32 values. 19 of the empty-location users have ApprissCase Users.

Treat these as a role-scope validation question, not 111 confirmed broken accounts. An upper-level user may require district, regional or broader effective hierarchy instead of a single store. Verify the intended and effective scope before asking the customer to invent store assignments.

### Feed freshness

Historical checks found the latest security assignment insertion at 13 October 10:42 UTC. The reported ReferenceDataBackLoad runs completed on 14 and 15 October without observed new corresponding rows. The manually inserted Chris location row has a later timestamp and is not proof of daily feed advancement. Ryan saw no task errors and suggested an upstream possibility; he did not prove file absence or root cause.

At 06:41 on the call, Matt says the last insert was on the 15th without a recoverable table name. Obtain the exact table, tenant, query and batch. Determine whether the current loader updates only changed rows before using MAX InsertedDateTime as a freshness signal. A filename dated 14 October proves neither delivery time nor successful ingestion. Its timezone is not established.

### Email examples need classification

The Emails sheet contains Jennifer Alba-Faust, 14 October, app not loading and errors; Johnny Hernandez, 14 September, inability to proceed after short-name/password entry; Nuri Ceylan, 8 September, denied access; Rachel Dill, 13 October, login and incident submission trouble. Do not label all four as missing Security ID. Only Rachel has the separately investigated level evidence in this packet.

## C. Concrete read-only validation for the five examples

Use Juan's previously verified SSMS/Bastion tenant access. All commands below are SELECT statements. No production write or repair is authorized by this packet.

```sql
SELECT UserName, SecurityID, LastLoginDate
FROM membership.Users
WHERE UserName IN (
 'Jacinta.Titus@kgstores.com',
 'Emeldia.Pryor@kgstores.com',
 'Christi.Winters@menswearhouse.com',
 'Rahim.Mehdiyev@menswearhouse.com',
 'Cheneria.Chevalier@josabank.com'
);

SELECT UserName, SecurityID, Persistent, InsertedDateTime, UtcDateFrom, UtcDateTo
FROM sso.SecurityLevelAssignments
WHERE UserName IN (
 'Jacinta.Titus@kgstores.com',
 'Emeldia.Pryor@kgstores.com',
 'Christi.Winters@menswearhouse.com',
 'Rahim.Mehdiyev@menswearhouse.com',
 'Cheneria.Chevalier@josabank.com'
)
ORDER BY UserName, Persistent DESC, InsertedDateTime DESC;

SELECT UserName, LocationID, Persistent, InsertedDateTime
FROM sso.LocationHierarchyMembers
WHERE UserName = 'Chris.Orth@tailoredbrands.com'
ORDER BY InsertedDateTime;
```

These queries have not been executed in this session. The names and fields come from the previously used tenant queries. Preserve the timestamp and batch context of results. Validate effective role scope and catalog mappings through the already used Portal user pages; do not invent a source table for the mapping that has not been inspected.

## D. Routing and source limits

https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478006902856
Current read, version 5: environment, complete reproduction with screenshots, AI-assisted troubleshooting notes and conversations outside Jira are required before escalation. Notify the customer of the move. Secure/Incident Engineering goes to Under Engineering Review and Shandana. The live transition name Waiting for Engineering resolves the wording difference in J.R.'s request.

RCS-29469 is evidence follow-up, not a reason to automatically create a duplicate ENG. Add the review note, preserve original attachments, reference RCS-29451 and ENG-10069, and use Relates if a human adds a formal Jira relationship. Relates exists on the site. No Jira linking permission was exercised here.

The transcript and Ryan screenshots are supplied meeting evidence, not proof that notes have been posted to Jira or Teams. The six meeting screenshots remain in the earlier HTML. The full call transcript is the user-supplied Texto pegado.txt under attachment e41225b0-672e-4b96-92b5-98e7b94f92de. It has automatic speaker attribution and possible transcription errors. Do not export its unrelated staff-travel or product-documentation discussion as TBI incident evidence.

All new notes are drafts. Juan posts and transitions manually. No Jira, Teams or production data was changed by the agent.

## E. Update after Matt's written chat explanation

Source: Juan supplied Matt's posted text in this conversation on 16 October; preserved in inbox/2026-10-16-tbi-matt-proceso-sso-confirmado.md. No independent chat retrieval or message permalink is available. The explanation is now delivered, not pending.

Validation sequence: original teams CSV, sso.teams contents, team-text lookup to securityid, resulting sso.SecurityLevelAssignments row, and membership.Users.SecurityID applied at SSO login. Match ingestion and login times. The new source confirms the intended one-row-per-user contract. It does not verify actual production cardinality or explain the location prefix.

If the user is present in the file and absent from sso.teams, investigate receipt, consumed batch and load. If present in sso.teams and missing a valid security-level assignment, inspect the lookup and replication. If the correct effective level exists before sign-in and the account stays blank, append evidence to the existing RCS-29451/ENG-10069 investigation. Distinguish manual Persistent rows, historical rows and current feed rows before assigning a duplicate-row cause. A correct level observed after login does not by itself prove it existed before login.

Read the team table's schema before drafting a filtered query against its columns:

```sql
SELECT COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'sso' AND TABLE_NAME = 'teams'
ORDER BY ORDINAL_POSITION;
```

This query is proposed and not executed. Do not guess whether its username column is named Username, UserName or otherwise. Preserve effective assignment details and timestamps from the existing SELECT block in section C.
