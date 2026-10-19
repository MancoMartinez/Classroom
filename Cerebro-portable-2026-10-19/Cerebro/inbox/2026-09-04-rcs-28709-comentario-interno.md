# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Correction

The September 3 screen rebuild did not resolve this defect. It reduced the frequency for a few hours. The same failure mode recurred on two additional stores on September 4, less than 24 hours after the second rebuild.

## 2. Environment and steps to reproduce

Production. Stater Bros Holdings Inc, LPMS and Incident.

### Store 356, September 1 to 3, original case

1. Open case 2026-083-STORE SHOPLIFT-220 at https://apps.apprissretail.com/staterbros/nettrack/LPMS/LPMSEditMenu.aspx?MasterCaseID=198806&ShopliftingID=203783&SuspectID=203783&StoreIdent=356
2. Make any change on the case.
3. Click Save.

Expected: case saves and remains accessible.
Actual: screen goes blank and the case becomes inaccessible. Confirmed by Viraj Kansara on September 3, screen recording attached to RCS-28709, file RCS-28709 Repro Recording 2026-09-03 163736.mp4.

### Store 208, overnight into September 4

1. Store manager opened a new incident and entered all fields.
2. Clicked Save. No visible error on screen.

Expected: case saves with the entered data and shows a case status.
Actual: cases 2026-208-STORE SHOPLIFT-529 and 2026-208-STORE SHOPLIFT-530 exist in the Investigations queue with Total Stolen at 0.00, no case status, and no investigator in the Assigned column. Reported by Angie Martinez on September 4 at 14:03, screenshot Screenshot 2026-09-04 105912.png attached to RCS-28709.

### Store 139, overnight into September 4

1. Store manager attempted to submit a case last night. The manager is not reachable today to confirm the exact steps taken.

Expected: case saves with the entered data and shows a case status.
Actual: cases 2026-139-STOREINCIDENT-44 and 2026-139-STOREINCIDENT-45 show the same pattern, 0.00, no case status, no investigator assigned. Reported by Angie Martinez on September 4.

| Date | Store | Case | Result |
| --- | --- | --- | --- |
| Sept 1 to 3 | 356 | 2026-083-STORE SHOPLIFT-220 | Blank screen, case inaccessible |
| Sept 4 | 208 | 2026-208-STORE SHOPLIFT-529, 530 | Saves with 0.00, no status, no investigator |
| Sept 4 | 139 | 2026-139-STOREINCIDENT-44, 45 | Saves with 0.00, no status, no investigator |

## 3. Findings

This is the same defect reported on the linked ticket RCS-28742, closed September 4 at 02:10 with no ENG created. Shandana Khan's condition on that ticket, September 3 at 08:23, was to accept the symptom as a legitimate bug before raising the linked ENG. The recurrence documented above across three stores meets that condition.

RCS-28022, Santikos, July 31, is a precedent for the rebuild action itself. Build All Screens on that tenant coincided with the Incident Types list going to zero afterward. Sequence observed, causality not confirmed, per the existing note on that ticket. Build All Screens ran twice on the Stater Bros tenant this week, September 3 morning by Viraj Kansara and September 3 at 20:57 by Juan Martinez. Nobody has confirmed since whether the Stater Bros Incident Types list is still fully populated.

## 4. Troubleshooting performed, and the limits of support access

Viraj Kansara reproduced the original defect on case 220 on September 3 and ran Build All Screens per Matthew Kamminga's suggestion. Angie confirmed at 12:04 that the blank screen still happened intermittently after that first rebuild. Juan Martinez ran Build All Screens a second time on the same tenant at 20:57 and retested case 220 seven times, all seven clean. No SQL or backend trace has been pulled yet for the store 208 or store 139 cases. Support does not have visibility into why the row saves with zeroed fields instead of failing outright or keeping the entered data.

AI assistance, Claude, was used to reconstruct this ticket history and structure this comment. No case narrative content was shared with the AI system beyond case numbers and dollar totals already visible in the reporter's own screenshots.

Conversation outside the ticket: Teams thread with Shandana Khan on September 3, asking whether the evening test was enough to accept the symptom as a confirmed bug. No response received as of September 4.

## 5. Ruled out. Do not repeat

Isolated to one screen or one case. Ruled out, now confirmed across three stores, 356, 208 and 139.

Rebuild fully resolved the defect. Ruled out, recurred within 24 hours of the second rebuild.

## 6. Still open

1. Confirm this now qualifies as an accepted bug and create the linked ENG, per your September 3 comment on RCS-28742.
2. Confirm whether the Incident Types list for the Stater Bros tenant is still fully populated after the two Build All Screens runs this week.
3. Advise whether a third Build All Screens run is safe to attempt or whether this needs backend investigation instead of another rebuild.
