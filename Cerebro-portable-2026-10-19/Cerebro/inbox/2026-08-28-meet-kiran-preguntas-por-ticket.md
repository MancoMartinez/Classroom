# Preguntas por ticket, Kiran, 28 ago 2026

Inglés para leer en la llamada. Español para que sepas qué estás preguntando y por qué.

---

## PRIORIDAD 1. Los que abren la conversación

### ENG-7189, comparación de SecurityID pre y post migración

**EN**
> "Matt asked you for this SELECT so Support could stop resolving permission complaints by
> assertion. You delivered it in one day. Where does that query live now, and are there
> others like it that my team doesn't know about?"

**ES**
Matt te pidió este SELECT para que soporte dejara de resolver quejas de permisos por
afirmación. Lo entregaste en un día. ¿Dónde vive esa consulta ahora, y hay más como esa que
mi equipo no conoce?

**Por qué preguntas esto:** es el mejor ejemplo de la reunión. Ingeniería construyó una
herramienta de soporte. Está pegada en un comentario de Jira, no en ningún repositorio.

---

### ENG-6555, mapeo LoginID contra UserName

**EN**
> "This ticket has two opposite directions of the same UPDATE and it doesn't say which one
> ran. You ran it in production at 5:45 AM on August 13. If the same mismatch shows up next
> week, which direction do we apply?"

**ES**
Este ticket tiene dos direcciones opuestas del mismo UPDATE y no dice cuál se corrió. Tú lo
ejecutaste en producción el 13 de agosto a las 5:45 AM. Si el mismo desajuste aparece la
semana que viene, ¿cuál dirección aplicamos?

**Por qué:** es DML puro sobre dos tablas, sin ALTER. Soporte lo puede correr. Lo único que
falta es que alguien decida cuál de las dos versiones es la buena.

---

### ENG-7366, migración de 491 usuarios inactivos ADUSA

**EN**
> "Step 4 inserts into `membership.GroupMembers` for the Administrators group. That's
> granting admin privilege from a script. Can Support ever execute that with a written
> approval, or is it engineering-only by policy? And the password hash is a literal in the
> script — should Support be picking that by hand?"

**ES**
El paso 4 inserta en `membership.GroupMembers` para el grupo Administrators. Eso es conceder
privilegio de administrador desde un script. ¿Puede soporte ejecutarlo alguna vez con
aprobación escrita, o es exclusivo de ingeniería por política? Y el hash de contraseña es un
literal dentro del script, ¿debería soporte estar eligiendo eso a mano?

**Por qué:** todo el script es DML, sin ALTER. Solo dos piezas necesitan firma. Si las
aíslas, el resto lo absorbe soporte.

---

### ENG-7312, la caja negra de permisos

**EN**
> "This says `sso.GetUserSecurityLevel` reads orphaned rows and overrides the SAML-mapped
> SecurityID with no log line, and `sso.SecurityLevelView` inner-joins so that same row
> disappears from the admin grid. It's been in Backlog since August 14 and it's not linked
> to a single one of the tickets it explains. When Support checks permissions in Control
> Panel and everything looks correct, what does that actually prove?"

**ES**
Este dice que `sso.GetUserSecurityLevel` lee filas huérfanas y pisa el SecurityID mapeado
por SAML sin dejar log, y que `sso.SecurityLevelView` hace INNER JOIN así que esa misma fila
desaparece de la grilla de administración. Lleva en Backlog desde el 14 de agosto y no está
enlazado a ninguno de los tickets que explica. Cuando soporte revisa permisos en el Control
Panel y todo se ve correcto, ¿qué prueba eso realmente?

**Por qué:** la respuesta honesta es "nada". Esta es la petición más concreta que le puedes
hacer hoy. Pide al menos una consulta que muestre los overrides invisibles.

---

## PRIORIDAD 2. Autorizaciones, el eje de tu misión

### ENG-7824, Tailored Brands

**EN**
> "In July I deleted the override row in `sso.SecurityLevelAssignments` for Beverly Wright,
> with Zack Graas approving as SSO owner. It worked, but that approval was verbal. Who signs
> off on a production write, and does the approver change by table? Also: 267 users in that
> tenant have `membership.Users.IncidentUserID` pointing at a UserID that doesn't exist in
> `incident.LPUser2`, block 50000 to 50406, 82 of them Appriss accounts. Your August 14
> script joins UserName to LoginID inside LPUser2, so it can't reach users with no row at
> all. Do you want my team to build the reconciliation for those?"

**ES**
En julio borré la fila de override en `sso.SecurityLevelAssignments` para Beverly Wright, con
Zack Graas aprobando como dueño de SSO. Funcionó, pero esa aprobación fue verbal. ¿Quién
firma una escritura en producción, y cambia el aprobador según la tabla? Además: 267 usuarios
de ese tenant tienen `membership.Users.IncidentUserID` apuntando a un UserID que no existe en
`incident.LPUser2`, bloque 50000 a 50406, 82 de ellos cuentas de Appriss. Tu script del 14 de
agosto une UserName con LoginID dentro de LPUser2, así que no alcanza a los usuarios que no
tienen fila. ¿Quieres que mi equipo arme la reconciliación para esos?

**Por qué:** es tu caso, lo trabajaste tú, y estás ofreciendo trabajo, no pidiéndolo.

---

### ENG-7205, AuditCompletionDate a 1900-01-01, Walmart

**EN**
> "Once your code fix is deployed, the backfill on `AuditMasterStore` from the
> `AUDIT.COMPLETED` change log is a plain UPDATE. Can my team run it? Two things I'd need
> from you: a rule for which `AUDIT.COMPLETED` entry to use when there are duplicates, since
> duplicates are the expected state in exactly those rows, and someone authorizing a write
> to the table Walmart pulls a daily report from."

**ES**
Una vez desplegado tu arreglo de código, el backfill sobre `AuditMasterStore` desde el change
log `AUDIT.COMPLETED` es un UPDATE plano. ¿Lo puede correr mi equipo? Necesitaría dos cosas
de ti: una regla de qué entrada `AUDIT.COMPLETED` usar cuando hay duplicados, porque los
duplicados son el estado esperado justo en esas filas, y alguien que autorice escribir en la
tabla de la que Walmart saca un reporte diario.

**Por qué:** caso perfecto de handoff. Bloqueado por criterio y firma, no por capacidad.

---

### ENG-5372, Tahoe Donner

**EN**
> "Tahoe Donner is missing the `ACCIDENTEQUIPMENT` table entirely — it's a database-only
> migration tenant. If you give me the schema, can Support create a missing table in a tenant
> DB, or does that always come back to Engineering?"

**ES**
A Tahoe Donner le falta la tabla `ACCIDENTEQUIPMENT` completa, es un tenant de migración solo
de base de datos. Si me das el esquema, ¿puede soporte crear una tabla faltante en la base de
un tenant, o eso siempre vuelve a ingeniería?

**Por qué:** es el único caso real de DDL en tu lado. Sirve para probar dónde está el límite.

---

## PRIORIDAD 3. Casos concretos para salir con trabajo asignado

### ENG-7782, Smart & Final, búsqueda de aprobador

**EN**
> "This has been in Backlog since August 25 with zero comments. Nobody has looked at what
> query feeds the approver autocomplete. If the recipient has to be a system user and Mark
> Flores has no account, that's a user creation and it's ours today. If the query ignores
> contacts created in User Tool, it's code and it's yours. Can my team take the diagnosis
> this week and report back?"

**ES**
Lleva en Backlog desde el 25 de agosto sin un solo comentario. Nadie ha mirado qué consulta
alimenta el autocompletado de aprobadores. Si el destinatario tiene que ser un usuario del
sistema y Mark Flores no tiene cuenta, eso es alta de usuario y es nuestro hoy. Si la consulta
ignora los contactos creados en User Tool, es código y es tuyo. ¿Puede mi equipo tomar el
diagnóstico esta semana y reportar?

**Por qué:** esta es la que te hace salir con algo. Pídela explícitamente.

---

### ENG-7401, Boot Barn, auditorías programadas

**EN**
> "David called this a missing encryption key record in the Options table and you dismissed
> it twelve days later. Fair. But the other half — audits sitting In Progress on a template
> that's no longer active, AuditConfigID 68 — who decides whether we reactivate the template
> or close the live audits? That changes what the customer reports as store compliance."

**ES**
David dijo que era un registro faltante de clave de cifrado en la tabla Options y tú lo
descartaste doce días después. Correcto. La otra mitad: auditorías In Progress sobre una
plantilla que ya no está activa, AuditConfigID 68. ¿Quién decide si reactivamos la plantilla
o cerramos las auditorías vivas? Eso cambia lo que el cliente reporta como cumplimiento.

**Por qué:** reconoces el error de David de frente y giras hacia la parte que sí es de soporte.

---

### ENG-6507, Spartan Nash, plantilla de auditoría

**EN**
> "BJ Probert already fixed the production template for this back in April and closed it.
> It came back. Support can check whether they're still on a non-standard template with a
> SELECT against `AuditConfig` and `AuditMaster` today. What we don't have is a deterministic
> repro — what combination of text length and question type triggers the page break? Without
> that, every template fix is a per-customer patch that recurs."

**ES**
BJ Probert ya arregló la plantilla de producción para esto en abril y lo cerró. Volvió.
Soporte puede verificar hoy si siguen en plantilla no estándar con un SELECT contra
`AuditConfig` y `AuditMaster`. Lo que no tenemos es una reproducción determinista: ¿qué
combinación de largo de texto y tipo de pregunta dispara el corte de página? Sin eso, cada
corrección de plantilla es un parche por cliente que reincide.

**Por qué:** demuestras que soporte ya cerró esto una vez. Es tu precedente más fuerte.

---

## PRIORIDAD 4. Proceso, para cerrar la reunión

### ENG-7319, el que se abrió y cerró en dos minutos

**EN**
> "This was opened and closed in two minutes and five seconds with 'Fixed the linked issues'
> as the entire record, and four customer RCS hanging off it. When that happens, Support
> can't verify anything or explain anything to the customer. What's a realistic minimum for
> a close note?"

**ES**
Este se abrió y cerró en dos minutos y cinco segundos con "Fixed the linked issues" como todo
el registro, y cuatro RCS de cliente colgados. Cuando eso pasa, soporte no puede verificar
nada ni explicarle nada al cliente. ¿Cuál es un mínimo realista para una nota de cierre?

---

### ENG-6492, Sportsman's

**EN**
> "Tyrone spent five weeks on this and produced the root cause, a production replication with
> the `supervisortest` account, and the full enforcement map. The ENG ticket has zero
> comments. Did that work reach you in a usable form, or did somebody re-derive it?"

**ES**
Tyrone pasó cinco semanas en esto y produjo la causa raíz, una replicación en producción con
la cuenta `supervisortest` y el mapa completo de enforcement. El ticket ENG tiene cero
comentarios. ¿Ese trabajo te llegó en forma usable, o alguien lo volvió a derivar?

**Por qué:** pregunta incómoda pero necesaria. Define qué formato de entrega sirve.

---

### La de cierre

**EN**
> "You're the assignee on seventeen of the eighteen tickets I reviewed. What are the two or
> three categories where handing them to my team actually gives you time back, instead of
> just creating review work for you?"

**ES**
Eres el asignado en diecisiete de los dieciocho tickets que revisé. ¿Cuáles son las dos o
tres categorías donde pasárselos a mi equipo realmente te devuelve tiempo, en lugar de
solo crearte trabajo de revisión?

---

## Los tres compromisos que debes sacar

1. Dónde viven los scripts a partir de ahora, y en qué formato. Sale de ENG-7189 y ENG-6555.
2. Un nombre de aprobador para escrituras en producción. Sale de ENG-7824 y ENG-7205.
3. ENG-7782 asignado a tu equipo esta semana.
