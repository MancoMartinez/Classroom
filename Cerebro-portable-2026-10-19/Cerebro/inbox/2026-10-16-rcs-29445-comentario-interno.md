OBSOLETE. Use 2026-10-16-rcs-29445-comentario-interno-v2.md. Revised at Juan’s request.

OBSOLETO. Sustituido por inbox/2026-10-16-rcs-29445-comentario-interno-v2.md. Motivo: la frase sobre Vedant del 23 de septiembre sobrepasaba el comentario 3361084.

INTERNAL NOTE. NOT FOR CUSTOMER

1. Correction
Escalate Izenda reporting separately from blank Security IDs. Root cause is unconfirmed. Do not transfer the Ahold waiting times discussed on the call to TBI.

2. Environment and steps to reproduce
Production, Tailored Brands, Client ID 209, tenant tbi. Database sqldb-prd-wus2-arp-production-209-tbi-platform. Reporter Colton Neal.
Step 1: Open /tailoredbrands/nettrack/AdHoc/reportlist.aspx through Incident.
Step 2: Open Open Investigations and use its saved filters. Record the filter values; the failing run's full values are unavailable.
Step 3: Try the Excel export.
Step 4: Edit the September cases report to Fiscal October, 4 to 31 October 2026. The customer calls it Cases by Month; the timeout URL identifies Cases MTD September. Confirm the saved report identity.
Expected: render and export the report without errors. No target duration documented.
Actual: Colton reported 2 to 5 minutes for the list and another 2 to 4 for a report, blank pages, export failures and server errors on 14 October.
Screenshots: RCS-29060, image-20261014-154021.png and image-20261014-160957.png. The latter shows HTTP 524 at 2026-10-14 16:07:16 UTC.
https://trebuco.atlassian.net/browse/RCS-29060?focusedCommentId=3396117

3. Findings
Vedant reproduced slow reporting on 23 September, comment 3361084. Other affected reports include Closed Investigations 2026 Summary, Closed Cases 2026 and 2026 Cases Summary. RCS-29445 has no attachments; originals remain in RCS-29060 and RCS-28256.

4. Troubleshooting and access limits
Reviewed Jira history, original screenshots and the 16 October call with J.R. and Matt. AI assisted evidence extraction and drafting. No new timed production reproduction or server trace was performed. Talos suggests checking performance flags; their current effective values and routing remain unverified. Historical True values do not prove today's state.

5. Ruled out
A 524 screenshot does not establish a WAF block. No evidence links this report failure to the Security ID defect or proves a common cause with ENG-9990.

6. Still open
Shandana: investigate report and SQL execution versus timeout handling and effective flags. Confirm coverage against ENG-9990 and name an owner. Matt considered the screenshots sufficient for Izenda review. J.R. requested engineering review on 16 October and customer priority treatment, not a fix date. Confirm the next update.
