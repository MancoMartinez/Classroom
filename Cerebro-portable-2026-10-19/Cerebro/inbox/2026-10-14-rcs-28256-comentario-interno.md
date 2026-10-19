**Update on the user access part, with a proposal to split this ticket.** The blank Incident Security ID and blank Hierarchy reports trace to two causes. Neither is limited to the six users reported here.

## 1. Environment and steps to reproduce

Production, tenant 209 tbi, `sqldb-prd-wus2-arp-production-209-tbi-platform`. Every query below is read only and was run on 2026-10-14.

### Rachel Dill, reported 2026-10-13

1. Rachel signs in through Okta SSO. `sso.ResponseLog` Id 30893, 2026-10-13 19:23:49 UTC.
2. Portal, Settings, Users, Rachel Dill, Secure Incident tab.

Expected: Incident Security ID Location Manager. `sso.SecurityLevelAssignments` has SecurityID 5 from the 2026-10-13 10:42 load, and `EXEC sso.GetUserSecurityLevel` returns 5 for her.
Actual: Incident Security ID blank. `membership.Users.SecurityID` was NULL after that sign in. I set it to Location Manager manually on 2026-10-14.

### Chris Orth, reported 2026-10-12

1. Chris signs in on 2026-10-12 19:50 UTC, after Location Manager was applied to him manually.
2. He tries to create an incident.

Expected: he can select his store.
Actual: error, and his Hierarchy page is blank. The feed sends him LocationID 90002005. That ID does not exist in `place.Location`, and he has no row in `secure.LocationHierarchyUserAssignments`.

## 2. Findings

| # | Finding | Status |
|---|---|---|
| 1 | 46 users who signed in since 2026-07-02 have a feed level above 0 and `membership.Users.SecurityID` NULL | verified |
| 2 | None of the 46 has a row in `incident.LPUser2`, by IncidentUserID or by LoginID and email | verified |
| 3 | With an LPUser2 row, 79 of 79 users have the level. Without one, 101 have it and 46 do not | verified |
| 4 | Christi Winters has a Persistent 1 level row from 2026-04-17, signed in 2026-07-14, and her account is still NULL | verified |
| 5 | 287 ApprissCase Users get a 9000xxxx LocationID in `sso.LocationHierarchyMembers` that is not in `place.Location` | verified |
| 6 | Latest rows in both SSO tables are from 2026-10-13 10:42. No 2026-10-14 load as of 18:57 UTC | verified |

`sso.GetUserSecurityLevel` shows modify_date 2026-10-09 09:11. The current definition orders by Persistent and has no Persistent = 1 filter. The SAML claims in `sso.ResponseLog` carry location and Okta group, with no team or level.

**My reading, unverified:** the step that copies the level to the account at sign in does not apply it for part of the users without an LPUser2 row. I do not know what separates the 101 from the 46. Some of the 101 were set manually.

## 3. Troubleshooting performed

In order: feed rows for the six users, account level against `incident.LPUser2` by both join routes as in https://trebuco.atlassian.net/browse/ENG-7189, the definition and output of `sso.GetUserSecurityLevel`, LastLoginDate, SAML claims, and LHUA plus `sso.LocationHierarchyMembers` against `place.Location`.

Applied today: Location Manager for Paul Bubelnik Jr, Nancy Bolhoff and Rachel Dill. Chaz Hyman, Vincent Fortner and Chris Orth already had level 5.

Outside the ticket: J.R. Teagle's email thread "Secure Incident ID, Choose a Value" asked for a review of https://trebuco.atlassian.net/browse/RCS-27269, https://trebuco.atlassian.net/browse/RCS-27578, https://trebuco.atlassian.net/browse/RCS-27941 and this ticket. I sent a Teams message to Matthew Kamminga on 2026-10-14.

```sql
SELECT ruta,nivel,COUNT(*) n FROM (SELECT CASE WHEN a.UserID IS NOT NULL THEN 'por ID' WHEN b.UserID IS NOT NULL THEN 'solo por email o login' ELSE 'ninguna' END ruta,CASE WHEN u.SecurityID IS NULL THEN 'cuenta NULL' ELSE 'con nivel' END nivel FROM membership.Users u LEFT JOIN incident.LPUser2 a ON a.UserID=u.IncidentUserID OUTER APPLY (SELECT TOP 1 x.UserID FROM incident.LPUser2 x WHERE x.LoginID=u.UserName OR x.EmailAddr=u.Email) b WHERE u.LastLoginDate>='2026-07-02' AND u.Email NOT LIKE '%@trebu.co' AND EXISTS(SELECT 1 FROM sso.SecurityLevelAssignments s WHERE s.UserName=u.UserName AND s.SecurityID>0)) t GROUP BY ruta,nivel;

SELECT COUNT(DISTINCT m.UserName) FROM sso.LocationHierarchyMembers m JOIN sso.PermissionGroups p ON p.UserName=m.UserName AND p.GroupName='ApprissCase Users' WHERE NOT EXISTS(SELECT 1 FROM place.Location l WHERE l.LocationID=m.LocationID);
```

## 4. Proposed split

| Issue | Type | Where it would live |
|---|---|---|
| Slow load from Secure to Incident | performance | https://trebuco.atlassian.net/browse/ENG-9990, stays on this ticket |
| Level not applied at sign in, 46 users | sign in code | new RCS, Under Engineering Review |
| Office locations 9000xxxx missing, 287 users, plus the missing 2026-10-14 load | data | new RCS, Under Delivery Review |

## 5. Still open

1. Does finding 1 need an ENG ticket, or is there a support side fix for users without an LPUser2 row?
2. Is one RCS per cause the split you had in mind?
3. Should the 9000xxxx office locations load into `place.Location` for TBI, or should those users get a store assigned?

Ticket priority High, open since 2026-08-10.
