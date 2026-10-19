Post para Retail Ops, Data Issues. Mismo formato que el post de RCS-29435.

RCS-28256 Tailored Brands 209: SSO file not loaded on Oct 14 and 15, plus 9000xxxx locations

Issue
The SSO+ tables for TBI have no new rows since October 13. Ryan Barlow checked ReferenceDataBackLoad and it ran without errors, so the gap looks upstream.

Evidence
sso.SecurityLevelAssignments and sso.LocationHierarchyMembers, latest feed rows 2026-10-13 10:42 UTC
ReferenceDataBackLoad for 209: Oct 13 ran 09:00 to 11:00 UTC and loaded rows. Oct 14 finished in 3 minutes and Oct 15 in 13 minutes, with no new rows either day

Second item
266 TBI users get one of 32 LocationIDs in the 9000xxxx range that do not exist in place.Location, so they get no hierarchy and cannot pick a store in Incident. Each one has a 4000xxxx twin. Ryan mentioned the 9 seems to be added on our side, and that offices and DCs should probably come as locations in the customer file.

Questions
1. Did the TBI SSO file arrive on Oct 14 and 15, and did it load in SnowTime?
2. Is the 9 prefix added by our load or does it come in the file? If TBI needs to send offices and DCs as locations, I will ask them.

Ticket: https://trebuco.atlassian.net/browse/RCS-28256
Thanks.
