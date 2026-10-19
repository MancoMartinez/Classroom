# Reunión con Kiran, 28 ago 2026. Qué puede absorber soporte

Evidencia: 18 tickets ENG con Kiran como asignado, tocados entre el 7 y el 28 de agosto,
más los RCS enlazados. Todo verificado en Jira en vivo. Cierre de la evidencia: 28 ago 2026.

---

## El hallazgo que abre la reunión

Kiran es asignado en 9 de los 10 tickets del cluster de permisos y en los 8 del cluster de
identidad. El cuello de botella de ingeniería para todo el dominio Incident es una persona.
Ese es el argumento, y no hay que decirlo como reclamo. Hay que decirlo como oferta.

El segundo hallazgo contradice lo que todos asumen. **Cuatro tickets se reportaron como
problema de permisos y ninguno lo era.**

| Ticket | Se reportó como | Causa real |
|---|---|---|
| ENG-6492 Sportsman's | Rol con acceso indebido | Config correcta en cuatro capas, la app no la aplica en Active Audits ni en el workbench |
| ENG-7824 Tailored Brands | Permisos SSO mal asignados | Falta la fila en incident.LPUser2 para 267 usuarios del tenant |
| RCS-28307 Smart & Final | Acceso a tiendas | Nivel correcto, faltaba usar Change Location. Cerrado como training |
| ENG-7401 Boot Barn | Tiendas sin acceso a auditorías | Plantilla inactiva más desajuste entre contador del tile y grilla |

En los cuatro casos soporte verificó nivel de seguridad, grupos y asignaciones antes de
encontrar la causa en otro sitio. Ese trabajo de descarte ya lo hacemos. La conclusión
operativa es dura: cuando soporte revisa permisos en el Control Panel y todo se ve bien,
eso no prueba nada. Hay que ir a SQL.

---

## Cluster 1, identidad de usuarios y migración ADUSA

Ocho tickets, todos de Kiran. Los ocho en Done.

### Lo que soporte podía haber hecho sin ingeniería

**ENG-7189, comparación de permisos pre y post migración. SÍ, sin condición.**
Es un SELECT puro sobre `incident.LPUser2`, `membership.Users` e `incident.LPSecurity`,
con una columna calculada que marca OK o MISMATCH sobre el SecurityID. Un L2 con lectura
en producción lo corre hoy mismo. Kiran lo entregó el 14 ago a las 10:15, un día después
de que Matt se lo pidiera.

Matthew Kamminga, 13 ago 13:26:
> "@Kiran Vadday this is the ticket for you to create an supply a select statement to
> compare security ID before/after migration"

J.R. Teagle escribió la razón de negocio en la descripción, 12 ago:
> "Every one of them was resolved by assertion rather than evidence. Without a comparison,
> Support argues rather than answers, and a genuine permission defect would be
> indistinguishable from a misremembering user."

Ese ticket es literalmente una herramienta para soporte. Lo construyó ingeniería.
RCS enlazados: RCS-28094 Vallarta, RCS-28122 Blain's, RCS-28141 Smart and Final,
RCS-28211 Skechers, RCS-28217 Smart & Final.

**ENG-7178, correos reescritos por la migración. SÍ, sin condición.**
Dos consultas. Una detecta el desajuste LoginID contra UserName. La otra es el UPDATE de
dedupe sobre una sola columna de una sola tabla. Ambas dentro del alcance de un L2.
J.R. Teagle lo dijo con todas las letras, 12 ago:
> "Before telling a customer they are entering credentials incorrectly, Support has to
> establish whether we changed that user's address first. Today there is no way to check."

Excepción real: hubo un comentario con `DELETE FROM membership.Users WHERE Email LIKE
'%[0-9]@%'` que Kiran publicó y luego borró el 19 ago. Ese patrón alcanza direcciones
legítimas que contienen un dígito, que es exactamente el defecto que el ticket describe.
Ese sí exige aprobación y backup verificado.

**ENG-6555, mapeo LoginID contra UserName. SÍ CON CONDICIÓN.**
Todo es DML sobre dos tablas, sin ALTER. Kiran, 13 ago 06:11:
> "Ran the updates on PROD at 5:45 AM EST today."

Faltan tres cosas: ventana de mantenimiento aprobada, acceso simultáneo a los dos
servidores porque la generación ocurre en uno y la ejecución en otro, y un runbook que
fije cuál dirección aplica. El ticket documenta dos direcciones opuestas del mismo UPDATE
y no dice cuál se corrió.

**ENG-7366, migración en bloque de 491 usuarios inactivos ADUSA. SÍ CON CONDICIÓN pesada.**
Script de siete pasos en una transacción. Toca `membership.Users`,
`incident.LPUser2`, `secure.LocationHierarchyUserAssignments`, `membership.GroupMembers`,
`membership.UserExtensionData`. Todo DML. Kiran lo abrió y lo cerró en un día.

Cuatro bloqueos concretos: aprobación firmada para el Step 4, porque insertar en
`membership.GroupMembers` con el grupo Administrators es concesión de privilegio
administrativo. El hash de contraseña literal, que soporte no debería estar eligiendo a
mano. El criterio que decide cuáles de los 491 IDs entran, que hoy vive como lista pegada
en un comentario. Y la resolución manual de 4 IDs cruzando `incident.CaseChanges`.

### Lo que no es de soporte y hay que reconocerlo de entrada

**ENG-6556** modifica el stored procedure `MigrateUsersToLocationHierarchy` y siembra
Arpfiles. **ENG-6562** es refactor de VB.NET en `LPUser.vb`, `Common.vb` y `LPSConstants.vb`
más redefinición de vista. **ENG-7000** es un cambio de una línea en
`Attachments.ascx.vb:792`. Los tres viajaron dentro de la release de agosto.

Dato de ENG-6562 que sirve para la reunión: los dos índices de cobertura propuestos,
`IX_LHUA_HierarchyID_UserId` e `IX_UserExtData_UserId_AttrName`, exigen CREATE INDEX y
nunca se hicieron. Ese es el único punto de los 18 tickets donde hace falta DDL de verdad.

### El ticket que no se puede juzgar

**ENG-7319** agrupa RCS-28177, RCS-28342, RCS-28364 y RCS-28379. Kiran lo abrió y lo cerró
en dos minutos y cinco segundos, sin descripción. Único comentario:
> "Fixed the linked issues."

Cuatro tickets de cliente colgados de ahí. Nadie puede reproducir ni verificar qué se hizo.

---

## Cluster 2, permisos, accesos y defectos de Incident

Diez tickets. Ninguno se resolvió otorgando un rol. **Ninguna acción de todo el barrido
fue una concesión de permiso por parte de soporte.**

La única acción de autorización en 18 tickets fue un DELETE, no una concesión: la fila de
override manual de Beverly Wright en `sso.SecurityLevelAssignments`, borrada el 24 jul en
`sqldb-prd-wus2-arp-production-209-tbi-platform`, con aprobación previa de Zackary Graas
como dueño de SSO. Lo hizo Juan. Funcionó. Y esa aprobación fue verbal y ad hoc, no existe
como flujo escrito.

Las concesiones y quitas de grupo las ejecuta el cliente. Colton Neal quitó a Beverly y
Francesca del grupo `TMW-APP-OKTA-SSO-Appriss-EBR-CorporateUser` el 13 ago desde el Okta
del cliente. En tenants con SSO federado el punto de control está fuera de nuestro alcance
por diseño.

### Los casos donde soporte cerró solo, sin ingeniería

**ENG-5372 Boot Barn.** Juan encontró la contención: volver a guardar Audit Date y End Date
vía Modify Audit Date/Times y después Mark Audit Completed guarda sin error. Aimee lo
entregó al cliente el 8 jul, Debbie De La Cruz lo aceptó el 10 jul. Cero ingeniería.

**ENG-6507 Spartan Nash.** BJ Probert corrigió la plantilla de auditoría en producción el
3 abr y cerró la iteración. Precedente ejecutado de corrección de datos por soporte.

Esos dos son la munición. Son la prueba de que ya lo hacemos cuando el camino está claro.

### Los casos donde soporte hizo el 100% del diagnóstico y el arreglo era código

**ENG-6492 Sportsman's.** Tyrone Whitney entregó causa raíz, replicación en producción con
la cuenta `supervisortest` y matriz completa de rutas de acceso, entre el 14 y el 23 jul.
El ENG no tiene un solo comentario. Tyrone, 20 jul:
> "This is a permissions enforcement bug, not a configuration issue. The configuration is
> correct at every layer — LPSECURITY, SECURITYDETAIL, base audit security levels, and
> audit assignment."

Y el 23 jul:
> "The only audits visible to this Regional LP Manager are ATF Compliance Store Audits —
> the exact type they are denied access to in SECURITYDETAIL"

Cinco semanas de trabajo de soporte, y el arreglo estaba en el code-behind. Ese es el
límite duro y hay que decirlo en la reunión: no queremos absorber esto, queremos entregarlo
mejor clasificado.

**ENG-7193.** Gina Pilato cerró la pregunta decisiva con dos palabras el 13 ago:
> "Truncated in legacy too"

Eso descartó regresión de cutover y descartó corrección de datos. Un triage de un día.

### Los que están parados

**ENG-7782 Smart & Final.** Creado el 25 ago, en Backlog, cero comentarios. Nadie ha mirado
qué consulta alimenta el autocompletado de aprobadores. Si el destinatario debe ser un
usuario del sistema y Mark Flores no tiene cuenta, es alta de usuario y es de soporte.
Si la consulta ignora los contactos creados en User Tool, es código. Nadie lo ha
determinado. Ese es un caso concreto que se puede ofrecer en la reunión hoy mismo.

**ENG-7824 Tailored Brands.** Creado el 26 ago, cero comentarios. Todo el trabajo lo hizo
Juan entre el 24 jul y el 25 ago. Hallazgo del 25 ago:
`membership.Users.IncidentUserID` apunta a un UserID inexistente en `incident.LPUser2`.
267 usuarios del tenant tienen el mismo puntero roto, bloque 50000 a 50406, y 82 son
cuentas de Appriss. Matt Gladden, 26 ago:
> "analysis seems correct. Those two users appear to be missing from the LPUser2 table.
> Possibly a migration miss"

Defecto latente que Juan identificó y que no tiene ticket ENG propio:
`sso.GetUserSecurityLevel` hace `SELECT TOP 1 ... ORDER BY Persistent DESC` sin desempate
secundario. Matthew Sincic tenía dos filas con Persistent NULL y resolvía arbitrariamente.

**ENG-7205, AuditCompletionDate reseteado a 1900-01-01.** Afecta a Walmart. Ryan Barlow,
12 ago:
> "They have a report that pulls daily from audit and they have raised several issues
> during calls regarding 'missing audits' from their internal reporting system only to
> find the missing audit listed in Secure Audit."

El backfill sobre `AuditMasterStore` desde el change log `AUDIT.COMPLETED` lo puede correr
soporte. Está bloqueado por tres cosas: el arreglo de código tiene que ir primero o las
filas se vuelven a corromper, hace falta una regla de qué entrada usar cuando hay
duplicados, y hace falta autorización explícita para escribir en la tabla que alimenta un
reporte diario de Walmart.

---

## El ticket que nadie enlazó y que explica la mitad de los casos de permisos

**ENG-7312**, creado por Ryan Barlow el 14 ago, asignado a Matthew Kamminga, en Backlog.
No está enlazado a ninguno de los 18 tickets. Documenta cuatro cosas:

- `LPSecurity.DeleteSecurity` corre `DELETE FROM LPSecurity WHERE SecurityID=@Param1` sin
  FK y sin validar referencias. Deja huérfanas en `sso.SecurityLevelAssignments`,
  `incident.LPUser`, `incident.LPUser2`, `incident.SecurityDetail`,
  `incident.AnnouncementSecurity` y `membership.Users`.
- `sso.GetUserSecurityLevel` lee esas filas huérfanas en el login y pisa el SecurityID
  mapeado por SAML sin escribir línea de log.
- `sso.SecurityLevelView` hace INNER JOIN contra `incident.LpSecurity`, así que la fila
  huérfana desaparece de la grilla de administración. El override queda activo e invisible.
- `sso.SsoUsers.sql` nunca referencia `sso.SecurityLevelAssignments`. Un usuario cuyo único
  rastro SSO sea una asignación de nivel no aparece en la grilla de búsqueda.

Traducción para la reunión: la superficie de permisos es parcialmente invisible desde el
front. Soporte no puede diagnosticar permisos con el Control Panel. Este ticket es la
petición más concreta que se le puede hacer a Kiran hoy.

---

## Los tres bloqueos reales, en orden de frecuencia

**1. Falta de script parametrizado y runbook. Cuatro apariciones.**
ENG-6555 documenta dos direcciones opuestas del mismo UPDATE sin decir cuál se corrió.
ENG-7366 lleva 491 IDs literales y cinco nombres corregidos a mano dentro de un CASE.
ENG-7178 y ENG-7189 entregan consultas pegadas en comentarios de Jira.

Ningún ticket apunta a un script en repositorio. Para reejecutar cualquiera de estos,
alguien copia texto desde el navegador. **Este bloqueo no es de permisos. Es de forma del
entregable, y es el más barato de arreglar.** Es la petición principal de la reunión.

**2. El pipeline de release. Tres apariciones en el cluster de identidad, ocho de diez en
el de permisos.** Ocho de diez tickets del segundo cluster terminan en un `.vb`, `.ascx` o
`.aspx`. Ese es el techo duro y ningún nivel de acceso a base de datos lo levanta.

**3. Falta un flujo escrito de autorización para escribir en producción. Tres apariciones.**
El DELETE de `sso.SecurityLevelAssignments` que Juan hizo con aprobación verbal de Zack.
El backfill de ENG-7205 sobre la tabla que alimenta el reporte de Walmart. La creación de
`ACCIDENTEQUIPMENT` para Tahoe Donner. Ninguno está bloqueado por capacidad técnica.

**El permiso ALTER aparece una sola vez en los 18 tickets**, en los dos CREATE INDEX de
ENG-6562 que nunca se ejecutaron. La hipótesis de que a soporte le falta ALTER no se
sostiene. Lo que falta es empaquetado y firma, no privilegio de esquema.

---

## El conteo, para decirlo en una frase

De los 18 tickets ENG revisados en tres semanas:

- **2 caían íntegros dentro del perfil de un L2 sin ninguna condición**: ENG-7189 y ENG-7178.
  Los dos son consultas de diagnóstico. Uno de ellos, ENG-7189, se creó explícitamente
  para dárselo a soporte.
- **7 más eran alcanzables con condiciones satisfacibles**: ENG-6555, ENG-7366, ENG-7824
  en su parte ejecutada, ENG-7401 en diagnóstico y datos, ENG-5372 en contención,
  ENG-7205 en el backfill, ENG-6507 en la plantilla.
- **8 son ingeniería genuina**, código VB.NET compilado del monolito Incident.
- **1 no se puede juzgar** porque nadie escribió qué se hizo.

La frase para la reunión: en tres semanas, la mitad del trabajo que hizo ingeniería en el
dominio Incident era alcanzable desde soporte, y el bloqueo dominante no es el permiso,
es que el entregable llega como texto pegado en un comentario en lugar de un script con
parámetros.

---

## Dos cosas que hay que reconocer de frente

Soporte se equivocó dos veces en la ventana, y decirlo primero compra credibilidad para
todo lo demás.

**David Vargas** atribuyó ENG-7401 a un registro faltante de clave de cifrado en la tabla
Options para `/bootbarn`. Kiran lo descartó doce días después. Kiran, 24 ago:
> "Hi @David Vargas I do not believe this is a code issue. Could you please replicate the
> problem and share the reproduction steps with me."

**Juan** atribuyó el fallo de búsqueda de Beverly Wright al nivel 11 sin acceso a búsqueda
en la RCA del 28 jul, y lo retractó por escrito el 25 ago:
> "Our 2026-07-28 RCA attributed the failure to Level 11 lacking search access. That
> attribution does not hold and should not be carried forward."

Los dos casos comparten forma: soporte encontró una anomalía real y la promovió a causa
raíz sin contrafactual. Eso es lo que hay que corregir del lado nuestro, y es el precio
de entrada para pedir más terreno.

---

Fuente: Jira en vivo, cloudId 7eb600cf-c7e0-43ed-acc4-90b277d43514, consultado el 28 ago 2026.
Guion de preguntas en `inbox/2026-08-28-meet-kiran-preguntas.md`.
