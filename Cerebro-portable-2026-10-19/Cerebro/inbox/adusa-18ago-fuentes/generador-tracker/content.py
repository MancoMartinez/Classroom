# -*- coding: utf-8 -*-
# Updated cell content for the 18 Aug post-call client tracker.
# Only cells that changed are listed. Everything else stays as J.R. wrote it.

T = 46252  # 2026-08-18

HEADER = {
 (2,'A'): "Status as of Tuesday, August 18, 2026, following the afternoon checkpoint call. Ticket states verified directly against Jira.",
}

# theme row -> (tickets, resolved, pending, awaiting, active)
SUMMARY = {
 7:  ("Login and access",                        4,4,0,0,0),
 8:  ("User accounts and duplicates",            5,4,0,0,1),
 9:  ("Store and brand restrictions",            5,3,0,0,2),
 10: ("Case entry and assignment",               6,3,0,0,3),
 11: ("Attachments and file handling",           2,1,1,0,0),
 12: ("Reporting and exports",                   3,0,0,0,3),
 13: ("Performance and timeouts",                4,1,0,0,3),
 14: ("Platform configuration and notifications",3,3,0,0,0),
 15: ("Transaction, tender and POS data",        2,1,0,0,1),
 16: ("Change requests and scoping",             1,0,0,0,1),
 17: ("Total",                                  35,20,1,0,14),
}

# row: {col: value}
CELLS = {

# ---------- User accounts and duplicates ----------
29: {  # RCS-28177
 'D': "Resolved",
 'G': T,
 'I': "Cause identified as mismatched user identifiers between the old and new user records, together with an incorrect home store on some accounts. 44 records were corrected on 8/14 and the Hannaford account for jonathan.wright2 was corrected on 8/17. The correction was applied to every account matching that pattern rather than to the named users alone. ADUSA confirmed on 8/18 that Jonathan Wright can see his historical cases and that Christina Cordero can search by name and complete a new case. Appriss will close this out in Jira.",
 'J': "8/13/2026 - Still an issue. Currently being worked on by Appriss.\n8/14/2026 - Appriss believes that it has been fixed.\n8/18/2026 - Cleared for the named users.",
},
30: {  # RCS-28342
 'D': "Active with Appriss",
 'G': T,
 'H': "Anthony Lopez appeared twice when selecting a case approver, one entry with a blank job title and one showing Specialist Investigator, so users could not tell which record was correct and approvals could route to the wrong one. Sampling since then shows the job title is missing on other accounts as well, so this is wider than the one user. Where names are common the job title is what tells an approver they have picked the right person.",
 'I': "The Anthony Lopez record was corrected on 8/14 and the job title now shows on both entries. ADUSA has since confirmed that the title is present in its own directory for the accounts still affected, so the value should be reaching Appriss in the claim data. Appriss is therefore reviewing how the title is mapped into the user file rather than correcting records one at a time. Janai Harrison, Stacie Whetzel, Jonathan Wright and Melanie Engleman are being used as the working examples. Appriss will confirm the cause and how many accounts are affected.",
 'J': "8/13/2026 - Still an issue with some users not having their job title updated in the LPMS user file from claim data. Anthony Lopez was manually updated.\n8/18/2026 - Data is still missing. Janai Harrison and Stacie Whetzel are examples where the title field from the SSO claim data does not appear to be populating the User table.",
},
31: {  # RCS-28364
 'D': "Resolved",
 'G': T,
 'I': "His record was updated on 8/14 to match the identifier from the previous system. A search run on 8/18 returned his cases back to the start of the year and the account shows as active. ADUSA confirmed it is resolved and will close the ticket. Appriss will come back separately on Anthony Powell, reported on 8/14 with the same symptom.",
 'J': "Ticket opened 08/13/2026\n8/18/2026 - Appears to be resolved as a substantial number of cases are showing now.",
},
32: {  # RCS-28379
 'D': "Resolved",
 'G': T,
 'I': "A correction pass across the affected case records was completed on 8/17. A sample drawn on 8/18 from the case list ADUSA supplied on the second tab of this workbook returned a populated Case Owner, Case Creator and Assigned To on every case checked. ADUSA confirmed on the call that it is resolved. Appriss will close this out in Jira.",
 'J': "Ticket opened 08/13/2026\n8/17/2026 - Still appears to be an issue. Some case examples are on the next sheet\n8/18/2026 - Sampled cases now show the owner populated.",
},

# ---------- Store and brand restrictions ----------
36: {  # RCS-28093
 'G': T,
 'H': "Two parts. Users who could only see stores from the wrong brand, which was corrected on 7/31 and confirmed working on 8/12. And employee search still returning associates from more than one brand for the same store number, both inside a case and from the admin employee table, which remains open.",
 'I': "ADUSA estimates around 300 store numbers exist in more than one brand, so a search on store 0001 returns Food Lion and Stop & Shop associates together. The brand is carried on the employee record in the Misc 1 field, which LPMS refers to as the division, but it is not populated on every record. Appriss is producing a count of how many employee records carry that value and how many do not, and will come back with that before proposing a route. The same behaviour is present in the previous environment, so this is a change to how the search works rather than something introduced by the move. ADUSA indicated on 8/18 that this sits below the current system issues in priority.",
 'J': "8/13/2026 - Still an issue from both inside a case and when an admin searches the employee table.\n08/14/2026 - Still an issue\n8/18/2026 - Searching Food Lion Store #0001 returns employees at Stop & Shop Store #0001 as well. Happens from the Admin Menu for Employees and within a case using the Associate Lookup.",
},
37: {  # RCS-28365
 'G': T,
 'I': "Location 7225 was assigned on 8/13 and ADUSA confirmed on 8/17 that the issue is resolved. Appriss will close this out in Jira. Reviewed alongside RCS-28415, which had the same symptom for two new users. Her account is separately one of the examples where the job title is not populated, which is tracked under RCS-28342.",
},
38: {  # RCS-28415
 'E': "Appriss Support",
 'G': T,
 'I': "Both users have been corrected. One had no location assigned at all, and the other had a location added at the wrong level of the hierarchy, which limited them to Food Lion instead of Stop & Shop. Appriss is now checking that the location is carried in the SSO claim so that new accounts provision correctly without a manual correction each time. Appriss has also offered to walk the ADUSA team through assigning locations in the new application, since that screen differs from the one used previously.",
 'J': "Ticket opened 08/17/2026\n8/18/2026 - Both users confirmed corrected on the call.",
},

# ---------- Case entry and assignment ----------
41: {  # RCS-28123
 'G': T,
 'I': "An update was deployed on 8/17 and is being verified. ADUSA agreed on 8/18 that Appriss may create a case at Stop & Shop location 9999, assign it and take it through approval, so the whole path can be followed in production without touching live data. Appriss will report the result. Appriss will also respond on the separate point raised on 8/14, that users can no longer print a case PDF from the confirmation screen and must go to the workbench instead.",
 'J': "8/13/2026 - Still an issue\n8/14/2026 - Fix is in progress and is expected to be part of the release early next week\n8/18/2026 - Agreed Appriss may validate end to end at location 9999.",
},
42: {  # RCS-28196
 'G': T,
 'I': "The change was deployed and ADUSA confirmed on 8/18 that the two fields no longer default to No and that the conditional formatting behaves correctly. The fields now display as null and greyed out rather than blank. Both sides agreed on the call that blank is the right behaviour, so that a user does not think a value is present which the system will not accept, and Appriss is making that change. ADUSA may still want to decide whether cases entered between cutover and the fix need reviewing for these two fields.",
 'J': "8/13/2026 - Still an issue\n8/14/2026 - Fix is in progress and is expected to be part of the release early next week\n8/18/2026 - Fields no longer default to No. Now showing as null rather than blank.",
},
43: {  # RCS-28304
 'D': "Active with Appriss",
 'G': T,
 'I': "No data is lost or altered. Widening the field is a change to the screen layout rather than a defect fix, so it needs an enhancement request. ADUSA confirmed on 8/18 that it would like one raised and that it is low priority and can sit behind the current system issues. Appriss will raise it with the account team and come back with the reference.",
 'J': "8/13/2026 - Not affecting functionality. Is a display limitation on the Case entry Screen. Will submit as an enhancement request to restore previous view\n8/18/2026 - Yes please, however this is low priority and can be shelved until the other system issues are resolved.",
},
45: {  # RCS-28378
 'D': "Resolved",
 'G': T,
 'I': "ADUSA confirmed on 8/18 that the buttons are present and that the original report related to the Hannaford shoplifting page, which has since been resolved. Testing on the ADUSA side shows it working. Appriss will close this out in Jira.",
 'J': "Ticket opened 08/13/2026\n8/18/2026 - Testing showed that this is resolved.",
},

# ---------- Attachments ----------
48: {  # RCS-28124
 'G': T,
 'H': "PDF and MOV attachments were not visible where JPEG was. Closed on 8/11 and reopened on 8/13 when the Hannaford brand reported it could not attach videos and was still receiving a Forbidden message. Viewing and downloading attachments is now working and the remaining problem is uploading.",
 'I': "A further fix was included in the release on the morning of 8/18. Appriss has tested a range of file types and all behave as expected apart from .txt, which is still being looked at. Please have the Hannaford users retry a video upload and confirm, and send the case number if any attempt still fails. It would also help to know whether .txt is a format the ADUSA teams actually use, so Appriss can judge how much weight to give it. Appriss will keep the ticket open until ADUSA confirms rather than closing it again on our own testing.",
 'J': "8/11/2026 - Reported as resolved.\n8/13/2026 - Users still reporting issues, ticket was re-opened.\n8/14/2026 - Appriss advised that a fix has been deployed\n8/18/2026 - Viewing and downloading is no longer an issue. Uploading is still being reported.",
},

# ---------- Reporting and exports ----------
50: {  # RCS-28021
 'G': T,
 'I': "Appriss reproduced the behavior on 8/14 and established that the date range on the report does not hold reliably, so a report can return older records without saying so. The records themselves are present. The scheduled reports were rerun on 8/14 against current data. ADUSA supplied two named reports on 8/18. PBI - Incident Export 2026 Q3 will not export to CSV but does export to XLS, and the scheduled CSV of that same report was delivered correctly by email. PBI - Current Location Listing will not export in either format. Appriss is tracing those two reports specifically, which is what was needed to move this past a general description. This item also sits behind the reporting work described under RCS-28356.",
 'J': "8/11/2026 - Still an issue. Automated reports are running but some data is missing. Some Adhoc reports run and export, however the file is blank\n8/18/2026 - Still not resolved. Able to export one report to XLS but not CSV, and a second report will not export in either format.",
},
51: {  # RCS-28161
 'G': T,
 'H': "The store file export downloads but the resulting CSV is blank, so brand lineup changes cannot be made. The export is taken from the location search screen and is the file ADUSA edits and returns by FTP to update location assignments in bulk. Confirmed on a screen share with ADUSA on 8/11.",
 'I': "The fix was tested successfully in the test environment on 8/18 and is being deployed to production the same day. Appriss will verify in production and confirm. Appriss is providing daily updates on this one until it is closed out.",
 'J': "8/13/2026 - Still remains an issue.\n8/14/2026 - Fix is in progress and is expected to be part of the release early next week\n8/18/2026 - Still an issue. The export runs but the file is blank.",
},
52: {  # RCS-28413
 'G': T,
 'H': "The Central Division report generated for managers on the morning of 8/17 showed 66 cases where the division previously held around 268. The other divisions on the same report appear correct. The report is Interview Data with Source, which is distributed automatically to a list of recipients.",
 'I': "ADUSA supplied the report name and the expected figure on 8/18, together with the version produced on 7/27 for comparison, and has asked for a corrected report to be issued to the managers who received the 66 case version. A preview taken directly in the reporting tool showed the same shortfall, so this is not limited to the distributed copy. Appriss has added an address to the distribution list in order to see the report as recipients receive it, and will verify the true case count for the division before a correction goes out. Nothing so far indicates case data has been lost.",
 'J': "Ticket opened 08/17/2026\n8/18/2026 - We will need this corrected. It is showing 66 cases for Central but should be around 268 as of July 27, 2026, the day prior to switch. The report is Interview Data with Source (AP REPORTS FOOD LION).",
},

# ---------- Performance and timeouts ----------
55: {  # RCS-28353
 'G': T,
 'H': "Updating a name in the store profile returned a 502 error, alongside general slowness. The error occurs specifically when adding a manager to the store record, where the lookup against the employee data is slow to return.",
 'I': "Being worked together with RCS-28356 and RCS-28407, since the 502 responses and the slowness appear to share an underlying cause. A set of fixes reached production on the evening of 8/17 and this path was one of the areas specifically targeted. A test run during the call on 8/18 returned a good result, which is encouraging but not proven over a full working day. Please retry a store profile update and confirm whether the 502 still occurs. If it does, ADUSA offered a screen share to capture a browser trace and Appriss will take that up.",
 'J': "Ticket opened 8/13/2026\n8/18/2026 - To be retested following the 8/17 release.",
},
56: {  # RCS-28356
 'G': T,
 'I': "This is the highest priority item on this list. The cause has been isolated to the reporting component rather than the incident application itself. Long running reports drive resource use up, and because the incident application shares that capacity it is affected by report activity. The other products on the platform are not affected. Work to separate the two is complete in the Appriss staging environment and is now in quality assurance. If it passes this week it will be released over the weekend and the effect should be visible from Monday. Separating them addresses the slowness and the 502s in the incident application; improving the reporting tools themselves is the next piece of work after that. A set of fixes already reached production on the evening of 8/17. What would help most now is whether users are seeing a difference since then, ideally from the Hannaford users who reported the longest page open times.",
 'J': "Ticket opened 8/13/2026\n8/18/2026 - No 502 errors this morning but experiencing a lot of latency moving from one page to the next.",
},
57: {  # RCS-28407
 'G': T,
 'I': "Engineering has identified the underlying issue and a set of fixes reached production on the evening of 8/17. Tracked together with RCS-28356 and RCS-28353 as one problem rather than three. Unlike RCS-28353 this one has not been narrowed to a single path, so it is expected to be addressed by the separation work described under RCS-28356. Across all traffic the 502 responses accounted for well under one percent, which is of little comfort to a user who hits one part way through a case. A 502 was reported on the morning of 8/18 with detail on the ticket and Appriss is tracing it.",
 'J': "Ticket opened 08/17/2026\n8/18/2026 - 502 errors received this morning, detail provided on the ticket.",
},

# ---------- Transaction, tender and POS data ----------
63: {  # RCS-28281
 'G': T,
 'I': "All files received have been loaded. Duplicate files in the delivery accounted for a material share of the volume received, which reduced the usable total. Why the day's data stops in the early afternoon is still being established. ADUSA has asked for this to be handled separately from the incident workstream and has nominated Lauren Linsenbach and Jacquelyn Wunders as the contacts. Appriss will take it up with them directly and confirm whether the shortfall can be backfilled or whether a corrected figure for the date is sufficient.",
 'J': "This is a ticket for the Secure system (Zeus), not Incident (LPMS)\n8/18/2026 - Required data does not appear to be reaching Appriss. Not connected with LPMS and should be separated out from this workstream.",
},

# ---------- Change requests and scoping ----------
66: {  # RCS-28292
 'G': T,
 'I': "ADUSA confirmed on 8/13 that the existing IP address will carry over to the new server, and confirmed on 8/18 that April Valerio is the contact during the window and will validate the store file on the morning of 8/21. Appriss will confirm before the window that no allow list change is needed on our side and will watch for the file on the morning of 8/21.",
 'J': "Not related to URL change. Migration scheduled for 8/20-8/21.\n8/18/2026 - April Valerio would be the POC. Will validate on the morning of the 21st.",
},
}
