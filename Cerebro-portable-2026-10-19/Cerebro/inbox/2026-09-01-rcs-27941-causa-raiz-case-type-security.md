# RCS-27941 · Causa raíz encontrada · martes 1 de septiembre de 2026

Kiran cruzó `incident.Suspect` contra `incident.Shoplifting` y `incident.MasterCase`, y sacó el
`CaseType` de cada Peters. Después abrió Manage Case Type, pestaña Security, en
`apps.apprissretail.com/tailoredbrands/nettrack/Admin/CaseTypeConfig.aspx`.

## 1. El cruce

| MasterCaseId | StoreIdent | CaseType |
|---|---|---|
| 671 | 5361 | Refund Fraud |
| 11990 | 6665 | Recovery - Legacy ThinkLP |
| 15353 | 3902 | Employee Work Injury |
| 20549 | 5076 | Refund Fraud |

## 2. Los security levels habilitados por tipo

**Refund Fraud:** Field Loss Prevention, Support, Administrators, Risk Management.

**Recovery - Legacy ThinkLP:** Support.

**Employee Work Injury:** Support, Administrators, Risk Management.

**Corporate User y Location Manager no aparecen en ninguno de los tres.**

## 3. Por qué cierra el caso

Beverly resuelve a Corporate User. Francesca resuelve a Location Manager. Los cuatro registros de
Peters viven en tipos de caso que no habilitan ninguno de esos dos niveles. La búsqueda corre, aplica
el filtro de Case Type Security y devuelve cero filas. Sin error, porque no hay error.

Dexter resuelve a Administrators, que sí está habilitado en Refund Fraud y en Employee Work Injury.
Por eso encuentra.

Esto explica todo lo que quedaba suelto. Los dos niveles distintos fallan igual porque ninguno está
habilitado. Los 267 usuarios sin fila en LPUser2 no reclaman porque LPUser2 nunca fue la causa. La app
no arroja error porque el filtro es de negocio, no de autorización.

**Es configuración, no defecto.** El ticket sale de Engineering.

Yo nunca miré esta capa. Perseguí identidad y alcance de ubicación, y el filtro estaba en el tipo de
caso.

## 4. La decisión es del cliente

Appriss no define qué roles ven qué tipos de incidente. Tailored Brands sí. Beverly usa Incident para
bajar documentación de casos de empleados para reclamos de desempleo, así que Employee Work Injury y
Refund Fraud encajan con su función. Confirmalo con ellos antes de tocar nada.

Preguntale a Kiran quién aplica el cambio, si el admin del cliente desde esa pantalla o Delivery.

---

## 5. Comentario interno para el ticket

```
Root cause identified. This is a configuration matter, not a defect.

Kiran Vadday traced the four Peters records from incident.Suspect through incident.Shoplifting to
incident.MasterCase and pulled the CaseType on each.

  MasterCaseId 671    store 5361   Refund Fraud
  MasterCaseId 11990  store 6665   Recovery - Legacy ThinkLP
  MasterCaseId 15353  store 3902   Employee Work Injury
  MasterCaseId 20549  store 5076   Refund Fraud

Manage Case Type, Security tab, shows the security levels enabled per incident type.

  Refund Fraud                Field Loss Prevention, Support, Administrators, Risk Management
  Recovery - Legacy ThinkLP   Support
  Employee Work Injury        Support, Administrators, Risk Management

Corporate User and Location Manager are enabled on none of the three.

Beverly Wright resolves to Corporate User. Francesca Ramos resolves to Location Manager. Every Peters
record sits in a case type that excludes both levels, so the search runs, applies the case type
security filter and returns zero rows. No error is raised because none occurs.

Dexter Monroe resolves to Administrators, which is enabled on Refund Fraud and Employee Work Injury.
That is why his search returns results.

This supersedes my 2026-08-25 escalation comment. The scale figure in that comment is also wrong. I
stated that 140 of the 407 positions in the 50000 to 50406 IncidentUserID block resolve against
incident.LPUser2. The correct count is zero, confirmed by query. Every account in that block lacks an
LPUser2 row, which Kiran confirms is expected for accounts added directly in platform. The missing
LPUser2 row is not the cause and item B of that escalation is withdrawn.

Next step sits with the customer. They own which security levels can access each incident type.
Support is asking Tailored Brands to confirm the intended access for Beverly and Francesca.
```

---

## 6. Comentario al cliente

```
Hi Colton,

We found what is driving this.

Access to those records is governed by incident type, not by the permission groups you were looking
at. The records Beverly and Francesca searched for sit in incident types that their current profile
does not cover, so the search returns nothing rather than an error.

This one is a decision on your side. Which incident types should Beverly and Francesca be able to
see? Refund Fraud and Employee Work Injury are the two that hold the records they were after.

Send me the list and we will get it configured.

Thank you,
Juan
```

---

## 7. Mensaje para Kiran, formato chat

```
That's it, thank you

Corporate User and Location Manager aren't on any of those three case types, and Beverly is Corporate
User, Francesca is Location Manager

Dexter is Administrators, which is why he sees them

I never looked at case type security, I was stuck on identity and location scope

Going back to the customer to confirm which incident types they should have

Who applies the change, their admin from that screen or Delivery?
```

---

## 8. Compromisos

Comentario al cliente: configurar una vez que Tailored Brands mande la lista de tipos. Sin fecha.

Pendiente tuyo: preguntarle a Kiran quién aplica el cambio, y sacar el ticket de Engineering una vez
pegado el comentario interno.
