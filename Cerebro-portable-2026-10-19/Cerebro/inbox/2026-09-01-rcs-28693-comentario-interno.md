# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Correction

The ticket title reads that the SSO error should have defaulted to the Store Reporter role. The evidence in this ticket points the other way. A user with no LPMS provisioning in Azure reaching a Store Reporter session is the defect, not the expected fallback. Treat the default role grant as the failure.

## 2. Environment and steps to reproduce

Environment: not recorded yet. Confirm PROD and write it here before this moves.
Sign in URL: not recorded yet. Ahold tested against a new sign in URL. Paste the literal URL here.

### Defect A. Unprovisioned identity receives a role. Ahold Delhaize (ADUSA), reported 9/1/2026

1. Take a tenant user with no LPMS provisioning in Azure. Ahold verified Paula Dotson has none and has never had any.
2. Navigate to the new LPMS sign in URL.
3. Authenticate as that user.
4. Look at the role granted on the landing screen.

Expected: authentication refused, no session, no role.
Actual: session opens and the user holds the Store Reporter role. Screenshots attached by leighann.stubbs@adusa.com on 9/1/2026 at 13:06.

### Defect B. Provisioned user cannot authenticate. Ahold Delhaize (ADUSA), reported 9/1/2026

1. Authenticate as Harrison Xu at the same sign in URL. Giant Food, store 233, Asset Protection for Giant District 104, group AP Level 2 Ahold.
2. Read the error returned at sign in.

Expected: session opens with Asset Protection permissions.
Actual: sign in fails with an error. The error text is not transcribed anywhere in this ticket. It exists only inside the attachments `LPMS SSO Issue.png` and `LPMS SSO Issue pt 2.docx`, both from 9/1/2026 09:51. Transcribe it into this ticket.

## 3. Findings

Two defects run in opposite directions in one ticket. Defect A over grants. Defect B under grants. A group membership problem on the Ahold side explains B. It does not explain A, because Paula Dotson belongs to no LPMS group at all.

Ahold verified the Azure state for Paula Dotson themselves and attached the evidence. That verification came from the client administrator, not from Appriss.

Both defects surfaced against the new sign in URL. That endpoint change is the one variable common to both and no one has tested either behaviour against the previous URL.

Ahold supplied Kyle Moses as a control user holding the same permissions as Harrison Xu.

| Item | Defect A | Defect B |
|---|---|---|
| User | Paula Dotson | Harrison Xu |
| Azure provisioning to LPMS | none, and never any | present, per the client |
| Result | session opens, Store Reporter granted | sign in fails |
| Reproducible from what is written | yes, with any unprovisioned user | no, error text missing |
| Severity dimension | access control | availability for one user |

## 4. Troubleshooting performed, and the limits of support access

Support asked Ahold for a control user with matching permissions so the sign in claims could be compared, and asked Ahold to check group membership on their side. Ahold answered with Kyle Moses.

No claim dump has been captured. No sign in logs have been pulled. The claim comparison is requested and not executed.

AI assistance: this note was drafted with AI assistance. Every ticket state, timestamp, attachment name and quoted comment in it was read directly from Jira on 1 September 2026. No finding here is inferred.

Conversations outside the ticket: the ADUSA escalation call on 1 September 2026 covered the open ticket list. Neither defect in this ticket was discussed on that call. Nothing else has happened outside the ticket.

Support cannot read the identity provider configuration or the role resolution path. That is the piece this needs from Engineering.

## 5. Ruled out. Do not repeat

| Hypothesis | Why it is dead |
|---|---|
| Ahold side group membership explains both | Paula Dotson holds no LPMS group. Client administrator verified it and attached proof |
| Same root as the hierarchy thread in RCS-28415, RCS-28519 and RCS-28667 | Those three fail after authentication with an empty store picker. Both defects here occur at authentication |
| Stale session or cache on the user machine | Paula Dotson had never signed in to LPMS before this test |

## 6. Still open

1. Confirm the routing for defect A. It grants a role to an identity that should be refused, which reads as an access control defect rather than a functional one. Give me the review queue to send it to.
2. Confirm whether the role resolution path applies a default role when the identity carries no LPMS entitlement, and whether that path is reachable only through the new sign in URL.
3. Compare the sign in claims for Harrison Xu against Kyle Moses and post the delta here.
4. Confirm whether defect A reproduces against the previous sign in URL.

Ticket opened 1 September 2026. Priority Medium. Reporter leighann.stubbs@adusa.com. Currently assigned to Vlad Bogus.
