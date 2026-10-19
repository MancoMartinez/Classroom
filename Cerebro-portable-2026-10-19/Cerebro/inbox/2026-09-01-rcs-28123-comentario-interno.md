# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Correction

A note posted to Ahold on 26 August said the missing confirmation and print option had been logged and was under engineering review. No such record exists. A search of RCS and ENG created between 25 and 28 August returns nothing for ADUSA. This ticket carries one link and that link is ENG-7192.

Close that gap before the next ADUSA call.

Second correction, to the scope attributed to ENG-7192. Its recorded scope is that a reassignment writes to Changes/History and that one notification email goes out. It did not close the "Assigned to can't be blank" validation error. ENG-557 tracks that separately and sits in Backlog. Ahold reported the validation error again on 19 August, two days after the 17 August deploy, and support could not reproduce it that day.

## 2. Environment and steps to reproduce

Environment: not recorded in this ticket. The issue type is Incident, which this project defines as a production outage, and the users named are live ADUSA users. Confirm PROD and write it here.

### Missing confirmation after assignment. Ahold Delhaize (ADUSA), reported 13 August 2026

1. Open a case in LPMS.
2. Click Send to Approver.
3. Type and select the approver name.
4. Save.
5. Read the screen returned, then read the Assigned to field.

Expected: a confirmation screen stating the case has been assigned, carrying an option to print the case as PDF. Ahold reports this existed before the platform move.
Actual: the screen goes blank. No confirmation text. The Assigned to field stays empty until a manual refresh. The PDF now requires leaving the case, opening the workbench and using View / Print Incident. Attachments from 13 August 2026 document both states.

### Original validation error, not reproducible from what is written

No case number was ever supplied. Support asked twice, on 3 August and on 10 August. Ahold escalated the request internally on 11 August and the number never came back. Only the intended assignee is known, Patrick Barnes.

One partial variant reproduces. Type a name in the lookup, erase it, type it again. The lookup degrades and stops returning results after a few attempts.

## 3. Findings

The reassign path to the confirmation page was closed off in code 3.5 years ago, deliberately. Marking a case complete still redirects to a page of that kind and behaves as designed. Restoring the path from reassign changes product behaviour that was removed on purpose. That routes as a product change with a business justification, not as a defect fix.

The requirement Ahold is actually describing is narrower than the screen they remember. Written on 13 August: assigning a case returns no immediate confirmation, and the user has to wait for the left panel to refresh to know the case moved. An immediate refresh of that panel satisfies the requirement without restoring a removed screen.

No attachment in this ticket shows the earlier confirmation screen. Engineering has nothing to compare against.

The ticket carries four symptoms under one key. Three closed. One open. The status does not distinguish them.

## 4. Troubleshooting performed, and the limits of support access

19 August: full walkthrough of approve and reassign against one record. The process completed as expected on a clean first attempt. Noticeable slowness observed, and the lookup degradation described above. The reported view could not be reproduced.

1 September: confirmed reassign does not produce the popup, and confirmed the code path was commented out 3.5 years ago on purpose. Confirmed mark case complete redirects correctly.

28 August: end to end validation run at Stop & Shop location 9999, authorised by Ahold on 18 August. The report still prints from the workbench through View / Print Incident.

AI assistance: this note was drafted with AI assistance. Ticket states, link states, comment timestamps and quoted text were read directly from Jira on 1 September 2026. The absence of a logged record for the confirmation screen was tested with a JQL search over RCS and ENG created 25 to 28 August.

Conversations outside the ticket: the ADUSA escalation call on 1 September 2026 covered this ticket. Matt is following up with Kelly, one of the Hannaford managers, and will bring notes to the Thursday call. On that call the popup was described as tied to approve as well as to mark case completed. Only mark case completed is established. Treat approve as unverified.

## 5. Ruled out. Do not repeat

| Hypothesis | Why it is dead |
|---|---|
| The 17 August deploy left the assignment broken | Ahold confirmed assignment works on 26 August |
| ENG-7192 covers the confirmation screen | Its recorded scope is Changes/History and single email. Neither touches a confirmation screen |
| The PDF is unreachable | It prints from the workbench through View / Print Incident, validated 28 August |
| The popup appears on reassign in current code | The path was commented out 3.5 years ago |

## 6. Still open

1. Decide the route. Feedback Portal as a product change, or ENG with a written business justification. This cannot move until that is settled.
2. Ask Ahold whether the screen they remember is Mark Case Completed. That question was raised on 1 September and has no answer.
3. Get a screenshot of the earlier behaviour from Ahold, showing the confirmation text and the print option.
4. Decide whether the real requirement is an immediate refresh of the left panel rather than a restored screen. That version is smaller and solves what Ahold described on 13 August.
5. Confirm whether ENG-557 will carry the validation error to a fix, and whether it needs raising out of Backlog.

Ticket opened 3 August 2026. Priority Medium. Reporter leighann.stubbs@adusa.com. Assigned to Juan Martinez.
