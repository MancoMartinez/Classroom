# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Correction
None. No prior statement to ADUSA on this ticket needs correcting.

## 2. Environment and steps to reproduce
Environment: Production, AHL/DLZ tenant, Delhaize brands.

### AHL/DLZ, reported 8/29

1. Provision a new LPMS user for a Delhaize brand employee through the standard onboarding flow. Do not manually assign a hierarchy location.
2. Sign in as that user.
3. Attempt to select a store location to open a case.

Expected: the user has a hierarchy location available and can select a store.
Actual: no hierarchy is present. The location selector is empty and the user cannot start a case. Confirmed against Gabriel Quist, the ticket reporter, 8/29. After support manually added a hierarchy location to his profile, he confirmed he could select locations and create cases.

## 3. Findings
Third report of the same symptom. RCS-28415 and RCS-28519 both closed by manually correcting the individual account. Three reports on the same provisioning path point at how new accounts arrive without a hierarchy, not at three isolated accounts.

Root cause suspected, per Megha Rathi's note on this ticket on 9/2: the Delhaize unification change leaves new user accounts without a default hierarchy assignment on provisioning. This is a hypothesis. It has not been confirmed in code.

## 4. Troubleshooting performed, and the limits of support access
Manual workaround applied for Gabriel Quist on 8/29, adding a hierarchy location by hand through the admin user profile screen. That unblocked him. Support does not have visibility into the provisioning pipeline that assigns hierarchy on account creation, so confirming whether this is a one time backfill gap for already migrated users or an ongoing default assignment bug for all new users requires engineering. No AI assisted troubleshooting used beyond drafting this note. No conversation with engineers occurred outside this ticket.

## 5. Ruled out. Do not repeat
The manual workaround is confirmed to work case by case. It does not scale and does not answer whether this recurs for every new Delhaize user going forward.

## 6. Still open
1. Confirm whether hierarchy assignment for a new user should come from the SSO claim or from the store file at provisioning time, or whether it is a client administration task done by ADUSA. This decides whether the ticket is a defect or an admin process gap. ADUSA asked this question directly on 8/29 and it has gone unanswered for 5 days.
2. Please clone this into an ENG ticket and link it back here. Ticket is 5 days old with no defect ticket created yet.
