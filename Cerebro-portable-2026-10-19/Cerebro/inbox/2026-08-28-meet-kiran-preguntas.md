# Guion de preguntas para Kiran, 28 ago 2026

Orden de prioridad. Si la reunión se corta a la mitad, las cinco primeras son las que
mueven la aguja. Todas en inglés, listas para leer.

---

## Cómo abrir, 30 segundos

No abras con una petición. Abre con el conteo y con el error propio.

> "I went through everything Engineering touched on Incident in the last three weeks,
> eighteen ENG tickets. Two of them were pure SELECT statements that my team should have
> run ourselves. Seven more we could have taken with some conditions. I also found two
> cases where Support called a root cause without a counterfactual, mine included, and I
> retracted one in writing last week. So I'm not here to say give us more. I'm here to
> figure out what shape the handoff needs so you stop being the bottleneck."

---

## Bloque 1, el bloqueo real. Prioridad máxima

**1.** Five of the tickets I reviewed delivered SQL as a comment pasted into Jira, not as a
script in a repo. ENG-6555 documents two opposite directions of the same UPDATE and
doesn't say which one ran in production. What would it take to get these into a
parameterized script somewhere my team can pull them from?

**2.** ENG-7189 is a SELECT that compares SecurityID before and after migration. Matt asked
you for it explicitly so Support could stop arguing with customers. That's our tool and
Engineering built it. How many more of these exist that we don't know about?

**3.** When you hand us a query, what do you need back from us so you trust the result?
Row counts, a screenshot, the execution plan? I want to define that once instead of
guessing per ticket.

---

## Bloque 2, autorizaciones. Es el eje que Juan quiere resolver

**4.** In July I deleted a row from `sso.SecurityLevelAssignments` in production for
Beverly Wright, with Zack Graas approving as SSO owner. It worked. But that approval was
verbal and ad hoc. Who signs off on a production write, and does the approver change
depending on the table?

**5.** ENG-7366 step 4 inserts into `membership.GroupMembers` for the Administrators group.
That's granting admin privilege. Is that something Support can ever execute with a written
approval, or is it engineering-only by policy?

**6.** ENG-7205 needs a backfill on `AuditMasterStore` for rows with
`AuditCompletionDate = 1900-01-01`. Walmart pulls a daily report off that table. Can my
team run that backfill once your code fix is deployed, and who authorizes it?

**7.** In the eighteen tickets I reviewed, Support never once granted a permission. Not a
role, not a group, not a membership. Is that by design, or is it just that nobody told us
we could?

---

## Bloque 3, la caja negra de los permisos

**8.** ENG-7312 says `sso.GetUserSecurityLevel` reads orphaned rows and overrides the
SAML-mapped SecurityID with no log line, and `sso.SecurityLevelView` inner-joins so that
same row disappears from the admin grid. It's been in Backlog since August 14 and it's not
linked to any of the tickets it explains. Can we get that prioritized, or at least get a
query that shows us the invisible overrides?

**9.** Four tickets in three weeks were reported as permission problems and none of them
were. Sportsman's, Tailored Brands, Smart & Final, Boot Barn. Every time, someone on my
team burned days verifying security levels first. What's the fastest way to rule permissions
in or out so we stop starting there?

**10.** When Support checks permissions in Control Panel and everything looks correct, what
does that actually prove? Because based on ENG-7312, my read is: nothing.

---

## Bloque 4, base de datos. Qué puede tocar soporte

**11.** Across all eighteen tickets, ALTER came up exactly once, the two covering indexes
proposed in ENG-6562 that never got created. So my working theory is that Support isn't
blocked by schema privilege, we're blocked by not having a signed-off procedure. Does that
match how you see it?

**12.** Tahoe Donner is missing the `ACCIDENTEQUIPMENT` table entirely, it's a
database-only migration tenant. Can Support create a missing table in a tenant DB if you
give us the schema, or does that always come back to you?

**13.** Which tables are off limits to Support writes, no exceptions? I'd rather have a
short blacklist than ask you every time.

**14.** ENG-7824: 267 users in the Tailored Brands tenant have
`membership.Users.IncidentUserID` pointing at a UserID that doesn't exist in
`incident.LPUser2`, block 50000 to 50406, and 82 of them are Appriss accounts. Your August
14 script joins on UserName equals LoginID inside LPUser2, so it can't reach users who have
no row at all. Do you want my team to build the reconciliation for the ones with no row?

---

## Bloque 5, código. Dónde está el techo

**15.** Eight of ten tickets in the permissions cluster end in a `.vb`, `.ascx` or `.aspx`
file. I'm not asking for repo access. I'm asking: what do you want in the ticket when we
hand you one of those, so you don't have to re-derive it?

**16.** Tyrone spent five weeks on ENG-6492 and produced the root cause, a production
replication, and the full enforcement map. The ENG ticket has zero comments. Did that work
reach you in a usable form, or did it get re-done?

**17.** ENG-7782 has been in Backlog since August 25 with no comments. Nobody has looked at
what query feeds the approver autocomplete. If it's a missing user account, that's ours
today. Can my team take the diagnosis on that one this week and report back?

---

## Bloque 6, proceso. Para cerrar

**18.** ENG-7319 was opened and closed in two minutes with "Fixed the linked issues" and
four customer RCS hanging off it. When that happens, Support can't verify or explain
anything to the customer. What's a realistic minimum for a close note?

**19.** You're the assignee on nine of the ten tickets in the permissions cluster. What are
the two or three categories where handing them to my team would actually give you time
back, rather than just creating review work for you?

**20.** If we get one thing right in the next month, what should it be?

---

## Tres cosas que debe llevarse Juan de la reunión

1. Una respuesta a la pregunta 1 y 3. Formato del entregable y criterio de verificación.
   Ese es el cambio más barato y el de mayor retorno.
2. Un nombre de aprobador para escrituras en producción, o el compromiso de definirlo.
3. Un caso concreto asignado a soporte esta semana. ENG-7782 es el candidato: está parado,
   nadie lo ha mirado, y el diagnóstico es un SELECT.

---

## Datos duros para tener a mano si te los piden

- 18 tickets ENG revisados, ventana 7 a 28 ago 2026, Kiran asignado en 17.
- 2 caían íntegros en el perfil L2 sin condición: ENG-7189, ENG-7178.
- 7 más alcanzables con condición: ENG-6555, ENG-7366, ENG-7824, ENG-7401, ENG-5372,
  ENG-7205, ENG-6507.
- 8 son código VB.NET compilado. 1 no documentado.
- 5 de 18 entregaron SQL pegado en un comentario, ninguno en repositorio.
- ALTER apareció 1 vez. Nunca se ejecutó.
- Soporte concedió permisos 0 veces. Ejecutó 1 DELETE con aprobación verbal.
- Casos cerrados por soporte sin ingeniería: ENG-5372 contención Boot Barn, aceptada por
  el cliente el 10 jul. ENG-6507 plantilla Spartan Nash corregida en producción el 3 abr.
