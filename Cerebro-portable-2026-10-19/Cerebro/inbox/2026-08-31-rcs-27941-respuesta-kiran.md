# RCS-27941 · Respuesta a Kiran · 2026-08-31

Estado en Jira hoy: **Under Support Review**, assignee **Shandana Khan**. Ya no es de Juan.
Último comentario: Kiran, 31 ago 15:45.

---

## 1. Qué pasó desde el 25 de agosto

**25 ago 16:37.** Juan pegó la escalación. 16:42, el comentario a Colton.

**25 ago 16:52.** Colton respondió con "Here is the screenshot that Dexter provided me". La imagen
mide 200x183. La firma corporativa de Colton en sus comentarios anteriores mide 200x183. **Colton
pegó su firma en vez del resultado.** La prueba de control nunca llegó.

**26 ago 08:13.** Shandana asignó a Matt Gladden para validar.

**26 ago 11:11. Matt Gladden validó el análisis:**

> "analysis seems correct. Those two users appear to be missing from the LPUser2 table. Possibly a
> migration miss"

**31 ago 15:45. Kiran:**

> "I see that Dexter can now access the Edit button for People records when searching for the last
> name 'Peters'. Regarding Beverly's experience, could you please confirm if she is still encountering
> this issue?"

---

## 2. Análisis de la posición de Kiran

**Kiran contradice a Gladden.** Gladden llamó a la ausencia en LPUser2 "a migration miss". Kiran dice
que para una usuaria nueva la ausencia está bien. Los dos revisaron el mismo dato. Nombrá la
diferencia sin discutirla.

**Kiran cerró la prueba de control sin saberlo.** Dice que Dexter encuentra Peters con el botón Edit.
Dexter tiene fila en LPUser2 y encuentra. Beverly y Francesca no tienen fila y no encuentran. La
correlación queda en cinco casos, sin contraejemplo. El screenshot que Colton no mandó ya no hace
falta.

**Kiran está mirando al usuario equivocado.** Dexter dejó de ser el caso abierto el 28 de julio. Los
casos abiertos son Beverly y Francesca.

**Los screenshots que pide ya están en el ticket**, del 20 de agosto, con los campos exactos:
Search On Suspect, Last Name Peters, resto vacío.

**Nadie aplicó un fix.** Ningún comentario reporta un cambio en LPUser2. Kiran describe a Dexter, que
funciona desde julio. Verificá antes de responderle.

---

## 3. Verificado hoy, 31 ago

```
UserName                             IncidentUserID   UserID   LoginID
beverly.wright@tailoredbrands.com    50267            NULL     NULL
francesca.ramos@tailoredbrands.com   50268            NULL     NULL
```

Ningún fix aplicado. Las dos siguen sin fila en `incident.LPUser2`.

---

## 4. Mensaje para Kiran, formato chat

Líneas cortas, una idea por línea, como escribe ella.

```
Hi Kiran

Dexter is my control, not the open case, his Edit got fixed back on July 28

The open ones are Beverly and Francesca, both still return empty on the same search

Their screenshots are in the ticket from Aug 20, Search On Suspect, Last Name Peters, rest blank

Just re-ran the join, both still NULL on LPUser2

On the new user part, that's what I wanted to ask you

If missing the row is fine at first, what creates it later?

These two have been active 40 days and it never showed up

267 users in the tenant are in the same state

Matt Gladden looked at it on the 26th and read it as a migration miss

Easier on a quick call?
```

---

## 4b. Segunda ronda · Kiran responde el bloque 50000

Kiran:

> "the LPUser2 might be empty because they might be directly added in platform and they might not
> have been there in LPUser2, that is fine. Another clue is incidentuserid starting with 50000 etc.
> and if they don't exist in LPUser2, that is fine"

**Kiran explica el origen. No explica el síntoma.** Aceptá su explicación y devolvé la pregunta que
queda abierta: Beverly sigue sin poder buscar.

**El dato que no encaja con su hipótesis.** Si el bloque 50000 se agrega directo en platform y por eso
no está en LPUser2, ningún ID de ese bloque debería tener fila. 140 posiciones del rango 50000 a
50406 no aparecen entre los 267 colgantes, y están intercaladas una a una con los rotos. El bloque no
decide.

**Confirmá el 140 antes de citarlo.** Mi número salió de restar 267 de 407 y asume que el rango está
poblado sin huecos. Consulta directa:

```sql
SELECT COUNT(*) AS con_fila
FROM membership.Users mu
JOIN incident.LPUser2 lp ON lp.UserID = mu.IncidentUserID
WHERE mu.IncidentUserID BETWEEN 50000 AND 50406;
```

Mensaje, formato chat. Reemplazá el número con el que devuelva la consulta.

```
Got it, that explains how they ended up without the row

Still stuck on the search though, Beverly is still empty as of today

One thing that doesn't fit for me: in the 50000 to 50406 block, [N] of them do have LPUser2 rows

And they're interleaved one by one with the ones that don't

So the block itself doesn't seem to be what decides it

If LPUser2 isn't what breaks the search, what should I look at next?

Security level, groups, hierarchy and store all match between Dexter and Beverly, I checked each one

Can send you the query results if that helps
```

---

## 4c. Tercera ronda · Kiran tenía razón

`con_fila` devolvió **0**. Ningún usuario del bloque 50000 a 50406 tiene fila en `incident.LPUser2`.

**Mi 140 estaba mal.** Lo saqué restando 267 de las 407 posiciones del rango, asumiendo que el bloque
estaba poblado sin huecos. Los 140 que conté como sanos no existen en `membership.Users`. Nunca
consulté, deduje.

**Consecuencia.** El bloque completo carece de fila en LPUser2, tal como Kiran describió para las
altas directas en platform. No es intermitente. No es un defecto. Los 267 están en el mismo estado y
solo dos reportaron el problema, así que la ausencia de LPUser2 no explica el síntoma.

**Corregí también la adenda 2 del otro archivo.** La lectura de "alta intermitente 2 de cada 3" queda
sin respaldo.

### Acción obligatoria: corregir el comentario en Jira

El comentario de escalación del 25 de agosto afirma:

> "The block holds 407 positions and 140 of them resolve correctly, interleaved one by one with the
> broken ones. The provisioning path fails intermittently, roughly two out of three"

Eso es falso. Shandana y Engineering lo están leyendo. Pegá esta corrección en el ticket.

```
Correction to my 2026-08-25 escalation comment.

The scale figure in that comment is wrong. I stated that 140 of the 407 positions in the 50000 to
50406 IncidentUserID block resolve correctly against incident.LPUser2. The correct count is zero.

SELECT COUNT(*) FROM membership.Users mu JOIN incident.LPUser2 lp ON lp.UserID = mu.IncidentUserID
WHERE mu.IncidentUserID BETWEEN 50000 AND 50406 returns 0.

My original figure came from subtracting the 267 dangling users from the 407 positions in the range,
which assumed the block was fully populated. It is not. The 140 I counted as healthy do not exist in
membership.Users.

The corrected reading. Every user in this ID block lacks an incident.LPUser2 row. Kiran Vadday
confirms this is expected for accounts added directly in platform. The provisioning path is not
failing intermittently. Since all 267 accounts are in the same state and only two reported the
search failure, the missing LPUser2 row does not explain the symptom and should not be treated as
the root cause.

Item B of my escalation is withdrawn. Items A and C stand.

Still open. Beverly Wright and Francesca Ramos return No data to display on a suspect search for
Peters, which returns four records in incident.Suspect. Security level, permission groups, location
hierarchy and store scope all match between them and a user who searches successfully.
```

### Mensaje para Kiran, formato chat

```
You're right, I ran it properly this time

Zero users in the 50000 to 50406 block have LPUser2 rows, not a subset

My earlier number was wrong, I subtracted instead of querying

So LPUser2 is out, all 267 are in the same state and only these two reported it

Noted on Matt, I'll drop that from the ticket

Since you asked what to check, two things would help most

What does the suspect search resolve the requesting user against? If I know the table or proc that
decides the result set I can stop guessing

And do you know anyone in that same 50000 block who searches fine? That's the control I never had

Correcting my comment in the ticket now
```

---

## 5. Comentario para el ticket

Pegalo también en RCS-27941, para que quede el registro. Shandana es la assignee.

```
Clarification on the open scope.

Dexter Monroe is the control, not the open case. His Edit access was resolved on 2026-07-28. He holds
a row in incident.LPUser2 and his suspect search returns the Peters records.

The open cases are Beverly Wright and Francesca Ramos. Neither holds a row in incident.LPUser2 and
both return No data to display on the same search. Their screenshots are in this ticket, dated
2026-08-20, with Search On set to Suspect, Last Name Peters and all other fields empty.

Five users now, no counterexample. Users with an LPUser2 row search successfully. Users without one
return empty.

Open question for Engineering. If a missing LPUser2 row is expected for a newly provisioned account,
confirm what creates the row afterward and why it has not been created for these two accounts after
40 days of active use. 267 accounts in this tenant are in the same state.

No change has been applied to incident.LPUser2 for either user as of today.
```

---

## 6. Ojo con esto

Colton cree que mandó el resultado de Dexter y mandó su firma. Si en algún momento necesitás ese
screenshot formalmente, pedíselo de nuevo. Para el argumento técnico ya no hace falta, porque Kiran
confirmó por su cuenta que Dexter encuentra a Peters.
