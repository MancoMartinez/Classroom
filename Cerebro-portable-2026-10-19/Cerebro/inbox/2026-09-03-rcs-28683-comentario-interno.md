# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Correction
None. No prior statement to ADUSA on this ticket needs correcting.

## 2. Environment and steps to reproduce
Environment: Production, AHL/DLZ tenant.

### AHL/DLZ, reported 8/31

1. Open an existing case for a Delhaize brand tenant.
2. Select Add additional associate.
3. Select the items to copy to the new associate's case.
4. Submit.

Expected: the new associate's case is created without error and opens directly for further entry.
Actual: the submit returns HTTP 404. The case is still created despite the error. Selecting Return to home lands on the workbench, where the newly created case must be located and selected by hand before anything more can be added to it. Reported by Leigh Ann Stubbs, 8/31. ADUSA confirmed they run multiple suspects on the same case often, so this recurs regularly, not as an edge case.

## 3. Findings
A submit that returns 404 and still writes the record to the database points at application code returning the wrong response after a successful write, not at tenant data or configuration.

## 4. Troubleshooting performed, and the limits of support access
Confirmed the case record is created despite the 404 by checking the workbench after the error. Support cannot see the endpoint that returns the 404 or the application logs behind it, so isolating which call fails requires engineering. No AI assisted troubleshooting used beyond drafting this note. No conversation with engineers occurred outside this ticket.

## 5. Ruled out. Do not repeat
Having to select the new case by hand after Return to home is workflow friction, separate from the 404. Do not fold it into this defect, it dilutes the actual bug.

## 6. Still open
1. Please clone this into an ENG ticket and link it back here, per J.R. Teagle's note directly on this ticket on 9/1: "once you're able to get steps to reproduce in here, let's please get an ENG ticket created for this and linked, and sent to Matthew Kamminga."
2. Confirm whether the created case ever lands incomplete or partial, or always complete despite the 404.
3. Identify the endpoint returning the 404 so it can be checked against the associate copy flow specifically.
