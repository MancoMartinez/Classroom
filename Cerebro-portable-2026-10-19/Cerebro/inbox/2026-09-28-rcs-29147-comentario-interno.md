Internal note, RCS-29147

Symptom. The Prada user cannot open Incident after signing in to Secure. Exact message: "Session Error. Your Incident session could not be established. This is usually caused by a temporary account configuration issue. Please return to the Secure portal and sign in again. If the problem persists, contact your administrator."

Checked by Support, all clean.
1. ENG-7189 comparison query: OldSystem_SecurityID 1, NewSystem_SecurityID 1, SecurityID_Status OK, SecurityLevel_Name 10. The level exists in incident.LPSecurity.
2. membership.Users: Enabled, not deleted.
3. sso.SecurityLevelAssignments: no rows for this user, so no override applies at login.
4. The user retried sign in from the Secure portal and the error persists.

Precedent. RCS-28061, Stater Bros, same message. Resolved by Engineering as a configuration update, linked to ENG-7000.

Request. Could Engineering check the Secure to Incident session handoff for this tenant, and confirm whether the RCS-28061 configuration fix applies to Prada.
