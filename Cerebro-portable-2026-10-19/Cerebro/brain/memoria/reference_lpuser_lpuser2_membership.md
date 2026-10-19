---
name: reference_lpuser_lpuser2_membership
description: "Las tres tablas de identidad tras la Unificación: membership.Users se sembró de LPUser pero nettrack lee LPUser2, y ahí nacen los usuarios rotos"
metadata: 
  node_type: memory
  type: reference
  originSessionId: a8293f75-ab64-479b-971f-f586abf0f63b
  modified: 2026-08-14T23:12:30.988Z
---

Verificado el 14 ago 2026 en ADUSA (cliente 441, `sqldb-prd-wus2-arp-production-441-dai-platform`), investigando RCS-28177.

**Las tres tablas y cuál manda.** Kiran Vadday, textual en el chat de la Unificación: *"LPUser2 UserID is the truth, at least for nettrack, that has to match in membership.Users.IncidentUserID"*. Pero los conteos de ADUSA dicen otra cosa sobre cómo se construyó:

```
incident.LPUser    11,073
incident.LPUser2   12,370
membership.Users   11,073
```

`membership.Users` tiene **exactamente** las mismas filas que `incident.LPUser`. Se sembró desde LPUser, no desde LPUser2. Por eso `IncidentUserID` apunta a `LPUser.UserID`. Cuando las dos tablas de incident coinciden en el UserID de una persona, todo funciona; cuando no, esa persona no puede buscar ni aparece como propietaria de caso, porque nettrack lee LPUser2.

**Las dos llaves que tienen que cuadrar**, y son distintas:
- `membership.Users.UserName` = `incident.LPUser2.LoginID` (identidad)
- `membership.Users.IncidentUserID` = `incident.LPUser2.UserID` (join)

**El punto ciego del fix de Kiran.** Su `UPDATE` del 14 ago (44 filas en ADUSA) une por `UserName = LoginID` **dentro de LPUser2**. Quien no tenga fila en LPUser2, o cuyo UserName no sea igual a ningún LoginID, no entra en ese update aunque esté roto. La misma consulta se iba a replicar en los 20 clientes migrados, así que el punto ciego se replica con ella. Para encontrar a los que quedan fuera hay que buscarlos con `NOT EXISTS` por las dos llaves a la vez, y después intentar cruzarlos por correo, por nombre en los dos órdenes, y por `LoginID LIKE '%' + UserName`.

**Dos convenciones de UserName conviven en el mismo tenant.** Unos lo tienen numérico (Jonathan Wright: UserName 1680764 = LoginID 1680764) y otros lo tienen como correo (Leigh Ann Stubbs: UserName leighann.stubbs@adusa.com, LoginID 1037716). `UserName <> LoginID` por sí solo **no es defecto**, depende de la convención. No declararlo roto sin más.

**Patrón de identidad vieja de Ahold.** Algunos usuarios sí están en LPUser2 pero con la identidad anterior: `AA` o `US` más el número, en @ahold.com, y con otro `UserID`. La unificación los recreó con el correo de la marca (giantfood, stopandshop, foodlion, hannaford, giantmartins) y el número pelado, sin enlazar las dos identidades. Ejemplos confirmados: Duane Masimore, membership `00503189`/giantfood contra LPUser2 `AA00503189`/`Duane.Masimore@ahold.com`/UserID 578353135; Jesse Trimbach, `00065002`/stopandshop contra `US00065002`/`JESSE.TRIMBACH@ahold.com`/UserID 1816868828. Es el mismo cuadro de [[reference_unificacion_patrones]].

**Las cuentas @trebu.co ensucian cualquier barrido.** Unas 21 filas de `membership.Users` son cuentas nuestras (Matt, Kiran, Chris, Jie, Juan, etc.) más `Anonymous`. No tienen fila en LPUser2 y eso es normal. Filtrar siempre con `Email NOT LIKE '%@trebu.co' AND Email NOT LIKE '%noreply-sysrepublic%'`.

**Rangos de UserID: no significan nada.** El bloque 50000-59999 parece sintético a primera vista y no lo es; son UserID reales de `incident.LPUser`, y hay gente en ese rango que sí tiene contraparte válida en LPUser2. No sacar conclusiones del rango numérico. Ver [[feedback_verificar_la_fuente_no_el_resumen]].

**Las 1,297 filas de más en LPUser2** son gente en nettrack sin cuenta en membership. Pregunta abierta, nadie la ha mirado.

**La bandera de aprobador es `membership.Users.SupervisorFlag`.** No está en LPUser2 ni en LpSecurity. Confirmado por el fix de Kiran en RCS-28342 el 14 ago: `UPDATE membership.Users SET IncidentUserID=..., UserName=..., SupervisorFlag=1`. Es la respuesta a "quién es aprobador y quién no".

**La jerarquía de tienda vive en `secure.LocationHierarchyUserAssignments`** (HierarchyId, UserId, LocationId), y `UserId` es el **GUID de membership.Users**, no el UserID numérico de incident. Es la tabla detrás del "home store hierarchy setup" que Jie Chen arregló para Nicholas Wilson y Shamar Anderson en RCS-28177. Un usuario sin fila ahí no puede seleccionar tienda al crear un caso.

**Causa raíz del bucket DuplicateEmail, en palabras de Kiran** (RCS-28342, 14 ago): *"Due to multiple email addresses, the UserID that was matched was erroneous."* La migración cruzó por correo y con varias direcciones por persona escogió el UserID equivocado.

**Un UserID equivocado deja rastro en ~50 tablas de `incident`, no solo en el perfil.** Solo `incident.MasterCase` tiene seis columnas de usuario: CreatedBy, AssignedToID, CaseOwnerID, CaseLastSavedByID, CheckOutUserID, ApprovedByID. Más CaseChanges, CaseJournal, CaseLink, las Audit*, Shoplifting, RestitutionList, RestitutionPayment, VendorPayments, WorkFlowHistory, WorkFlowTracking, ActivityLog, ChangeHistory, UserSession y otras. Kiran publicó el script de cascada completo en RCS-28342 (tabla temporal `#UserIDFix` con pares WrongUserID/CorrectUserID). Para verificar que corrió, contar filas que sigan apuntando al UserID viejo en MasterCase y CaseJournal.

**Cuidado con `LEFT(email, CHARINDEX('@', email) - 1)`**: revienta con "Invalid length parameter" si hay un correo sin arroba. Usar `SUBSTRING(email, 1, NULLIF(CHARINDEX('@', email), 0) - 1)`.

Relacionado: [[reference_esquema_usuarios_incident]], [[project_membership_users_13]], [[reference_acceso_sql_tenants]], [[reference_jerarquia_ubicaciones_incident]].
