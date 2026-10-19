**Escalating to Secure Engineering.** The Incident security level from SSO+ is not applied on the sign in that creates the user. Matthew Kamminga confirmed on Teams on 2026-10-15 that it should apply on creation and on later sign ins, and asked to route this to a new ENG ticket.

## 1. Environment and steps to reproduce

Production, tenant 209 tbi, `sqldb-prd-wus2-arp-production-209-tbi-platform`. Logs from Grafana Explore, `grafanacloud-apprissretail-logs`, clientId 209. Every query was read only.

### Rachel Dill, 2026-10-13

1. Her row exists in `sso.SecurityLevelAssignments`: SecurityID 5, Persistent NULL, loaded 2026-10-13 10:42 UTC. `EXEC sso.GetUserSecurityLevel` returns 5 for her.
2. Her first SSO sign in, 2026-10-13 19:23:49 UTC, creates the account.
3. Check `membership.Users.SecurityID`, or Portal, Settings, Users, Rachel Dill, Secure Incident tab.

Expected: Location Manager, SecurityID 5.
Actual: NULL. I set it manually on 2026-10-14. It held after her next sign in on 2026-10-14 19:58 UTC.

Grafana sequence for that sign in:

| UTC | Sender | Message |
|---|---|---|
| 19:23:49.582 | SsoService | Identified 1 SSO Extra permission groups to assign |
| 19:23:49.586 | SsoService | Identified 1 SSO Extra teams to assign |
| 19:23:49.641 | MembershipService | User Rachel Dill has been created |
| 19:23:49.660 | SsoService | Sso user created, User Data with `"SecurityID":null` |
| 19:23:49.684 | MembershipService | Added to ApprissCase Users, Basic Users |
| 19:23:49.698 | MembershipService | Added to Location Manager user team |
| 19:23:56.732 | Saml2 | Logged on |

No line about the security level.

## 2. Findings

Users created through SSO between 2026-10-09 and 2026-10-15, all with level 5 in `sso.SecurityLevelAssignments`:

| User | Created UTC | Last sign in UTC | Account level |
|---|---|---|---|
| Ashley N Carter | 10-09 20:24:16 | 10-09 20:27:23 | 5 |
| Teegan Baker | 10-10 17:58:30 | 10-10 18:00:39 | 5 |
| Jordan Shields | 10-11 20:44:20 | 10-11 20:50:28 | 5 |
| Alexis Post | 10-13 19:22:23 | 10-13 19:50:47 | 5 |
| Theresa Veasley | 10-15 17:17:42 | 10-15 17:46:18 | 5 |
| Brett Virtue | 10-14 19:47:05 | same | NULL |
| Doris Mays | 10-14 20:00:25 | same | NULL |
| Tamieko Jones | 10-15 14:00:02 | same | NULL |

Every user who signed in again has the level. Every user whose only sign in created the account does not. Verified.

49 users who signed in since 2026-07-02 have a feed level above 0 and a NULL SecurityID in `membership.Users` and in the lpuser view. Verified. How many of them signed in only once is not checked yet.

**My reading, unverified:** the security level step is skipped on user creation and runs on later sign ins.

## 3. Troubleshooting performed

Ruled out so far: the feed, the rows are present; `sso.GetUserSecurityLevel`, its current definition orders by Persistent with no Persistent = 1 filter and returns 5; the lpuser view, every affected user is in it. Detail in my internal note of 2026-10-14 on https://trebuco.atlassian.net/browse/RCS-28256.

Outside the ticket: Teams with Matthew Kamminga on 2026-10-15, and an email thread with J.R. Teagle on the same reports. Workaround in use: setting Incident Security ID manually in the Portal.

## 4. Still open

1. Does the SSO user creation path call the security level assignment, and is that the step that is skipped?
2. Once confirmed, could the affected accounts be corrected in one pass, or should Support set them one by one?

Related: https://trebuco.atlassian.net/browse/RCS-28256 and https://trebuco.atlassian.net/browse/RCS-27578.
