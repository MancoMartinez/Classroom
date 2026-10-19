# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Correction
None. No prior statement to ADUSA on this ticket needs correcting.

## 2. Environment and steps to reproduce
Environment: confirmed against both Production and Test, per Leigh Ann Stubbs on 9/2.
Production sign-in URL: https://apps.apprissretail.com/adusa/signin
Test sign-in URL: https://test.apprissretail.com/adusa/signin

Two separate defects are tracked in this ticket and they point in opposite directions.

### Defect 1, Harrison Xu, cannot authenticate

User: Giant Food store 233, Asset Protection for Giant District 104, group AP Level 2 Ahold.
Control user provided by ADUSA with the same permission profile: Kyle Moses.
Steps: Harrison Xu attempts to sign in and receives an error. Full error text is in the attachments LPMS SSO Issue.png and LPMS SSO Issue pt 2.docx, not yet transcribed into this ticket.
Expected: successful authentication with the AP Level 2 Ahold role.
Actual: authentication fails. Leigh Ann Stubbs is sending Harrison the test sign-in link and will report the result.

### Defect 2, Paula Dotson, over-authenticated

1. Select any tenant user with no LPMS provisioning in Azure and no history of provisioning.
2. Navigate to either sign-in URL above.
3. Authenticate with that user.

Expected: authentication is refused and no role is granted.
Actual: the session opens and the user receives the Store Reporter role. Confirmed against Paula Dotson, who has never been provisioned to LPMS. ADUSA verified her Azure state on their side and attached screenshots of the open session, 9/1.

## 3. Findings
The two defects run in opposite directions, sub-permissioning against over-permissioning, which makes it unlikely they share one root cause. Both surfaced against the current sign-in URLs, so the URL change itself is a variable in both, not yet ruled in or out.

Defect 2 is the more serious of the two. A user with no LPMS provisioning obtained a valid production session and a role. Client-side group membership cannot explain this, because there is no group assigned to that identity.

## 4. Troubleshooting performed, and the limits of support access
Vlad Bogus confirmed on 9/2 that Test and Production SSO configurations match, except for identity provider and certificate. Matthew Kamminga is separately working with Ryan Barlow on the Delhaize store mapping as a short term workaround for new users generally, not specific to either defect here. Support cannot see the SSO fallback logic that assigns a default role, so confirming why an unprovisioned identity gets Store Reporter requires engineering. No AI assisted troubleshooting used beyond drafting this note.

## 5. Ruled out. Do not repeat
Client-side Azure group membership as the explanation for defect 2 is ruled out. There is no group on that identity for a group to be misconfigured in.
Client-side Azure group membership for defect 1 is not ruled out yet, Vlad Bogus is still comparing SSO claims against the control user.

## 6. Still open
1. Requesting a routing decision on defect 2. It is an access control defect in production and may belong under Security Review rather than Engineering Review. Open since 9/1, unresolved for 2 days.
2. Defect 1 stays with Vlad Bogus pending Harrison Xu's test result against the test sign-in URL.
3. Transcribe Harrison Xu's literal error text from the attachments into this ticket once his result comes back.
