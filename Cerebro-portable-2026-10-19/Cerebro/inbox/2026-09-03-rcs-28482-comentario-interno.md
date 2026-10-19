# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Environment and steps to reproduce

Environment: Production, AHL/DLZ tenant, Izenda AdHoc Reporting.

### PBI - Current Location Listing (Jim Cosseboom Test), reproduced 9/3

1. Open Izenda AdHoc Reporting, category Jim Cosseboom Test.
2. Open PBI - Current Location Listing (Jim Cosseboom Test) in Report Designer.
3. Click the MISC tab.

Expected: MISC opens the report's distribution settings, same as any working report.
Actual: MISC renders as plain grey text. It does not highlight on hover and does not respond to clicking. Data Sources, Fields and the other tabs behave normally.

### Outlook Export (Jim Cosseboom Test), reproduced 9/3

Same three steps. Same actual result, MISC does not respond.

Originally reported by Jim Cosseboom on 8/19, screenshot Izenda Greyed Out fields.png. Clarified on 8/22, screenshot Appriss Izenda 08-22-2026.png, that the blocked tab is MISC and not Data Sources.

## 2. Findings

| Report | MISC | Fields tab |
|---|---|---|
| PBI - Current Location Listing (Jim Cosseboom Test) | Does not respond | Plain field list, no summary function |
| Outlook Export (Jim Cosseboom Test) | Does not respond | Plain field list, no summary function |
| Unusual Incidents Top 30, control report | Opens normally | Group and Count Distinct functions |

Hypothesis, not confirmed: MISC availability may depend on whether the report has a summary function defined, not on report type as first proposed on 8/24.

## 3. Troubleshooting performed, and the limits of support access

Matt and Leigh Ann confirmed live on the 9/3 call that Engineering already sees the same behavior on Appriss side.

Support reproduced the same behavior independently today, opening both reports in Report Designer and testing the MISC tab directly.

AI assisted in drafting this note and organizing the reproduction steps. The reproduction itself was performed manually in the tenant by Support.

No conversation with engineers occurred outside this ticket besides the 9/3 call referenced above.

Support has no visibility into what determines MISC availability per report. That is what Engineering needs to confirm.

## 4. Ruled out. Do not repeat

Report type based on a Distinct checkbox and Results selector, proposed 8/24 from a reading of the customer's screenshots. Not confirmed against a live comparison until today. The comparison instead points to the summary function, see Findings.

## 5. Still open

1. Confirm whether the summary function, Group and Count Distinct, is what enables MISC for a report.
2. Confirm whether rebuilding either affected report as a summary report restores MISC. Do not run this against the client's live reports without Engineering's guidance.
3. Clone this into an ENG ticket and link it back here, per J.R. Teagle's request on the 9/3 call.
