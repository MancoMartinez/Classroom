OBSOLETE. Use 2026-10-16-rcs-29469-comentario-interno-v2.md. Matt has now provided his written explanation.

INTERNAL NOTE. NOT FOR CUSTOMER

1. Correction
This is Colton's evidence follow up to the TBI call, not a new diagnosis. Continue the access investigation in RCS-29451 and ENG-10069. Talos missed the attachments and prior history.

2. Environment and reported reproduction
Production, Tailored Brands, Client ID 209, tenant tbi.
Step 1: In Portal, Settings, Users, open Jacinta Titus, Emeldia Pryor, Christi Winters, Rahim Mehdiyev or Cheneria Chevalier.
Step 2: Open Secure Incident and inspect Incident Security ID.
Expected: the intended level applies from the configured mapping.
Actual: all five profiles show no selected level in Appriss Incident Security ID Examples.xlsx. These are screenshots, not a fresh reproduction.

3. Findings
Read all three 14 October CSVs and the workbook's 29 embedded screenshots. All five users appear with Team Location Manager and Group ApprissCase Users. File presence does not prove ingestion or application.
Locations CSV line 301: Chris.Orth@tailoredbrands.com, Brand SSU, Location 2005. Teams line 301 and permissions line 319 identify Location Manager and ApprissCase Users. The CSV does not contain his historical SSO+ LocationID 90002005. That SSO+ row was dated 13 October. Trace the same consumed batch before assigning the prefix's origin.
111 Location values are blank, all in higher teams. Check hierarchy before treating them as errors.

4. Troubleshooting and limits
Crosschecked the original files, workbook images, prior SQL/log findings, Ryan's Teams replies and the 16 October call with Matt and J.R. AI assisted extraction and drafting. No fresh production account or loader trace was performed.
Rachel's level 5 preceded account creation; creation left SecurityID NULL while groups and team applied:
https://trebuco.atlassian.net/browse/RCS-29451?focusedCommentId=3397050
Matt says team and level names must match and rejected adding the ID to the locations file as a simple fix. He offered a written explanation. Ryan and Matt have not resolved the prefix origin. A successful replication task does not prove file consumption.

5. Ruled out
Do not use the second login as a proven universal fix, or replace 9 with 4 in bulk. The five new cases are not all proven first logins.

6. Still open
Validate each user's feed level, account level and login timing; confirm coverage under ENG-10069. Trace SSU+2005 through the current loader. Support publicly offered manual level assistance in RCS-29451; no bulk repair is approved.
