# INTERNAL NOTE. NOT FOR CUSTOMER

Hi Kiran, the customer pushed back on the admin process. Bringing it back to you with what she described.

## 1. Environment and customer follow up

Environment: **Production**, ADUSA tenant, Secure platform after the July unification.

Leigh Ann Stubbs replied on 9/24 at 15:49 ET:

| Point | What the customer says |
|---|---|
| Provisioning path | The manager requests an LPMS role through ADUSA IT. Leigh Ann approves and tells IT which role to assign |
| Scope | Users are provisioned by **Brand/Division**, never by single location or district |
| Sync | Access email arrives, then a 4 to 6 hour sync window |
| Symptom | The user finds out at first login that they cannot create a case |
| History | "This has not been an issue until now." |

## 2. Steps to reproduce

### ADUSA, reported 8/29

1. ADUSA IT provisions a new user with a Brand/Division role. Nobody adds a hierarchy by hand.
2. The user signs in after the sync window.
3. The user tries to select a store to start a case.

Expected: the stores of the user's Brand/Division are available.
Actual: the location selector is empty. Case: Gabriel Quist, attachments Gabriel Quist.JPG and Gabriel Quist Hierarchies.JPG from 8/29.

## 3. Findings

1. Verified 9/24: Settings > Users > Gabriel Quist > Hierarchies holds one row. Standard Location Hierarchy, level 0 Location, 8369 Hannaford District 10 General Office. That is the manual row Leigh Ann added on 8/29.
2. Verified 9/24: Select Locations lists stores for Standard Location Hierarchy at District level.
3. From internal Secure docs, not tested on this tenant: at SSO sign-in, IDP claims carry a level and a value that map to hierarchy members, and Secure writes the user's location rows from them. SSO Master File and SSO+ feed the same tables.
4. Unverified: which claims ADUSA's IDP sends today, and whether LPMS derived store access from the Brand/Division role before unification.
5. Same symptom, fixed by hand on the account: RCS-28415 https://trebuco.atlassian.net/browse/RCS-28415 and RCS-28519 https://trebuco.atlassian.net/browse/RCS-28519

## 4. Troubleshooting performed

I read the Hierarchies tab in the production UI on 9/24. No data changes.

Claude flagged the SSO claim mapping as a possible way to assign the hierarchy from the Brand/Division role. I checked the Hierarchies tab for Gabriel Quist and the store list myself. I have not confirmed which claims ADUSA sends. Could someone evaluate whether this path applies here?

No conversations happened outside this ticket.

## 5. Still open

1. Before unification, did LPMS give store access from the Brand/Division role alone, with no per user hierarchy step? That would explain the customer's "not an issue until now".
2. Could ADUSA's Brand/Division claim, or an SSO Master File entry, map to a Division level member so new users arrive with their stores?
3. If neither applies, does this belong to Product as a change request?

Priority Medium. Open since 8/29.
