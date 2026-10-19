# RCS-27941 · Bloques para pegar · 2026-08-25

Orden: comentario interno primero, comentario al cliente segundo, transición 231 tercero.

Estado verificado en Jira hoy: Work in progress, assignee Juan Martinez, Medium, creado 2026-07-22.
Transición 231 Waiting for Engineering disponible, destino Under Engineering Review.

---

## 1. Comentario interno

```
Escalating to Incident Engineering.

Environment: Production, tenant 209-tbi, sqldb-prd-wus2-arp-production-209-tbi-platform.

Symptom. Beverly Wright and Francesca Ramos authenticate, load the Incident main menu, and run a
suspect search. The search executes, delays roughly one minute, and returns No data to display. No
error is raised. Dexter Monroe performs the equivalent search successfully.

Reproduction. Search For Incident, People Filters tab, Search On set to Suspect, Last Name Peters,
all other fields empty. Customer screenshots for both users are attached to this ticket, dated
2026-08-20.

The data exists. incident.Suspect holds 20278 rows. LastName LIKE 'Peters%' returns four exact
Peters records, SuspectID 671, 11990, 15353 and 20549. The empty result is not correct behavior.

Discriminator found. membership.Users.IncidentUserID points to a UserID that does not exist in
incident.LPUser2 for both failing users.

  dexter.monroe@tailoredbrands.com     IncidentUserID 22      LPUser2 match 22
  beverly.wright@tailoredbrands.com    IncidentUserID 50267   LPUser2 match NULL
  francesca.ramos@tailoredbrands.com   IncidentUserID 50268   LPUser2 match NULL

Neither user matches by LoginID either, so they have no LPUser2 row at all.

Scale. 267 users in this tenant have the same broken pointer. All fall in the IncidentUserID block
50000 to 50406. The block holds 407 positions and 140 of them resolve correctly, interleaved one by
one with the broken ones. The provisioning path fails intermittently, roughly two out of three, and
it is not limited to customer accounts. 82 of the 267 are Appriss staff accounts.

What Support ruled out, each with evidence.

1. Security level. sso.GetUserSecurityLevel returns 11 for Beverly, 13 for Dexter, and an empty set
for Francesca. Francesca has no row in sso.SecurityLevelAssignments. One user has a level, the other
has none, and both fail identically. Our 2026-07-28 RCA attributed the failure to Level 11 lacking
search access. That attribution does not hold and should not be carried forward.

2. Permission groups. Beverly holds ApprissCase Search Users and Basic Users. Francesca holds
ApprissCase Search Users only. Different sets, same failure.

3. Location hierarchy. All three users hold one row in
secure.LocationHierarchyUserAssignments with HierarchyId 1, LocationHierarchy1 TBI, levels 2 through
6 and LocationId NULL. Identical scope between the working user and the failing users.

4. Store scope. Dexter's LPUser2 row carries StoreIdent 4825. incident.Suspect holds zero rows for
that store, and Dexter still retrieves case 2026-TMW-40003407-INT-6. The user's store does not
filter the search.

5. Manual override and Okta claim. We removed Beverly's manual SSO+ override row on 2026-07-24 with
SSO owner approval, and the customer removed both users from
TMW-APP-OKTA-SSO-Appriss-EBR-CorporateUser in the daily feed on 2026-08-13. Neither change resolved
the search.

What Support needs from Engineering.

A. Confirm whether the Incident suspect search requires an incident.LPUser2 row for the requesting
user, and what the search returns when that row is absent. Our evidence is four users with no
counterexample. Dexter and Matthew Sincic hold rows and search successfully. Beverly and Francesca
hold none and fail.

B. Repair the 267 broken pointers in this tenant and fix the provisioning path that creates them.
Kiran Vadday's 2026-08-14 script joins on UserName equal to LoginID inside LPUser2, so it does not
reach users who have no row at all. Both users in this ticket fall in that blind spot.

C. Raise a defect for sso.GetUserSecurityLevel. The procedure performs SELECT TOP 1 with ORDER BY
Persistent DESC and no secondary tiebreaker. When two rows share the same Persistent value the
selection is arbitrary. Matthew Sincic held two feed rows at Level 13 and Level 2, both with
Persistent NULL, and resolved to Level 2. This affects any user with multiple feed assignments. It
was identified on 2026-07-28 and no ENG ticket was raised.

Business context. Tailored Brands completed an 800 store go live on 2026-08-03. The ticket has been
open 34 days. The customer requested Engineering review on 2026-08-20.
```

---

## 2. Comentario al cliente

```
Hi Colton,

Thanks for the screenshots, they gave us what we needed.

The Peters records do exist, so the empty result Beverly and Francesca are getting is on our side.
We've traced it to a difference in how their accounts were set up, and it isn't something the
permission screens show. That's why everything looked correct when you checked.

We're escalating to Engineering today.

One thing that would help confirm it: could you have Dexter Monroe run the same search, Search On set
to Suspect, Last Name Peters, everything else blank? A screenshot either way works.

Leave the Okta group change as is, that part was right.

I'll come back as soon as Engineering weighs in.

Thanks,
Juan
```

---

## 3. Transición

Después de pegar los dos comentarios, aplicá la transición 231 Waiting for Engineering. Destino
Under Engineering Review. El ENG lo auto crea la transición y los comentarios sincronizan en ambos
sentidos. El ticket se reasigna, para Secure e Incident el destinatario es Shandana Khan.

---

## 4. Pendiente después de escalar

El defecto del desempate en `sso.GetUserSecurityLevel` lleva 28 días identificado sin ticket ENG.
Va en el punto C del comentario interno. Verificá que Engineering lo abra como ítem separado, porque
afecta a cualquier cliente con doble asignación de feed y no solo a este ticket.
