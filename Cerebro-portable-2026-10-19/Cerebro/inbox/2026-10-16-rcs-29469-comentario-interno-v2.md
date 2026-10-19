OBSOLETE. Use 2026-10-16-rcs-29469-comentario-interno-v3.md. Revised at Juan’s request.

INTERNAL NOTE. NOT FOR CUSTOMER

1. Correction
Colton supplied evidence for the existing RCS-29451 and ENG-10069 investigation. Talos missed the attachments and history. Matt has now posted the SSO+ design in the meeting chat; his written explanation is no longer pending.

2. Environment and reported reproduction
Production, Tailored Brands, Client ID 209, tenant tbi.
Step 1: Open Portal, Settings, Users for Jacinta Titus, Emeldia Pryor, Christi Winters, Rahim Mehdiyev or Cheneria Chevalier.
Step 2: Open Secure Incident and inspect Incident Security ID.
Expected: the intended level applies at SSO sign in.
Actual: all five profiles show no selected level in Appriss Incident Security ID Examples.xlsx. These are screenshots, not a fresh reproduction.

3. Findings
The three 14 October CSVs contain all five users with Location Manager and ApprissCase Users. Reviewed the workbook's 29 images. Presence in a file does not prove ingestion.
Matt's written design: truncate and load the customer teams file into sso.teams, look up each team text to a numeric securityid, and replicate to sso.SecurityLevelAssignments. Expected: one row per user, used whenever the user signs in through SSO. This describes the loader; no TRUNCATE was run during support review.
Chris's locations CSV line 301 contains SSU and 2005, not his historical SSO+ code 90002005 from the 13 October load. The supplied CSV is dated 14 October. Trace the same consumed batch to identify the transformation. 111 Location values are empty, none in Location Manager; check intended hierarchy before calling this an error.

4. Troubleshooting and limits
Reviewed files, screenshots, prior SQL/log findings, Ryan's Teams replies and the 16 October call with Matt and J.R. AI assisted extraction and drafting. No fresh production or loader trace was performed.
Rachel had level 5 before account creation, which left SecurityID NULL while groups and team applied:
https://trebuco.atlassian.net/browse/RCS-29451?focusedCommentId=3397050

5. Ruled out
A second login is not a universal fix. Do not replace 9 with 4 in bulk. The five examples are not all proven first logins. The prefix origin and file consumption remain open.

6. Still open
Compare CSV to sso.teams, lookup output, effective level and account at login. Check expected row count and manual Persistent precedence. Confirm ENG-10069 coverage for existing accounts. Support offered manual level assistance in RCS-29451; no bulk repair is approved.
