# RCS-27941 · Tailored Brands · SSO/Permissions en Incident
## Plan de verificación y escalamiento · 2026-08-25

Estado verificado en Jira hoy: **Work in progress**, assignee Juan Martinez, prioridad Medium,
creado 2026-07-22, último update 2026-08-20 12:42 EDT. Edad 34 días. Último comentario es de Colton
Neal pidiendo revisión de Engineering. **La acción está del lado de Juan y lleva 5 días sin respuesta.**

---

## 1. Lo que la evidencia del 20 de agosto derriba

El RCA del 28 de julio sostiene dos cosas. Las dos quedan sin respaldo con las capturas nuevas.

**Afirmación 1 del RCA:** "Beverly resolves to Security Level 11 (Corporate User), which does not have
Incident search access", y el nivel 5 Location Manager sí la tiene.

**Lo que muestra la evidencia:** Francesca Ramos tiene Incident Security ID **Location Manager** y su
búsqueda de "Peters" devuelve el mismo "No data to display" que la de Beverly, que está en
**Corporate User**. Dos niveles distintos, el mismo síntoma exacto. El nivel de seguridad no separa el
caso que funciona del que falla. Escalar cargando esta premisa le entrega a Engineering un
diagnóstico ya falsificado.

**Afirmación 2 del RCA:** los claims de Okta re-derivan el nivel 11 en cada login y por eso el DELETE
no persiste.

**Lo que muestra la evidencia:** Colton sacó a Beverly y a Francesca del grupo
TMW-APP-OKTA-SSO-Appriss-EBR-CorporateUser del archivo diario el 13 de agosto. El RCA predice que con
eso el nivel del feed gana. Siete días después Beverly sigue apareciendo como Corporate User en la UI
y la búsqueda sigue vacía. O el cambio del feed no propagó, o el nivel no es la variable que manda.
El caso de Francesca inclina la balanza hacia lo segundo.

Corrige el RCA antes de escalar. No lo cites como está.

---

## 2. Lo que sí separa al usuario que funciona de los que fallan

Dexter Monroe es el único control con el que contamos, y funciona.

| | Dexter (funciona) | Beverly (falla) | Francesca (falla) |
|---|---|---|---|
| Permission groups | 6 en SSO+, 7 en Control Panel: Administrators, ApprissCase Search Users, ApprissCase Users, Basic Users, EBR Analysts, EBR Investigators, Over Short Analysts | ApprissCase Search Users x2, Basic Users | ApprissCase Search Users x2 |
| User Teams | Administrators, Field Loss Prevention | no aparece en las capturas | no aparece en las capturas |
| Security Level | Administrators (Persistent True) | Corporate User | Location Manager |
| Location Hierarchy | pestaña existe, nunca se abrió | **nunca se revisó** | **nunca se revisó** |

Quedan dos variables sin tocar en 34 días de ticket: **User Team** y **Location Hierarchy**. La
pestaña Location Hierarchy aparece en el menú lateral de SSO+ en todas las capturas del cliente y
nadie la abrió.

El cerebro ya tiene este modo de falla escrito, en `brain/memoria/reference_esquema_usuarios_incident.md`:

> "Sin ninguna fila en `lhua`: el usuario no tiene asignación de ubicación. Síntoma: entra bien pero
> no ve tiendas y no puede crear caso."

> "Permission groups define qué puede hacer, Hierarchies define sobre qué ubicaciones. Un usuario con
> los grupos completos y Hierarchies vacío entra y no ve nada."

Eso describe el síntoma actual con precisión. El usuario entra, la app carga, el menú abre, la
búsqueda corre, y devuelve cero filas. Un problema de autorización daría un error. Cero filas con
un minuto de espera es una consulta que sí se ejecuta contra un alcance vacío.

Advertencia del propio cerebro, en `brain/markdown/19-rcs-procesos-playbook.md`: "la vista
`incident.lpuser` es lo que maneja toda la app. Para síntomas funcionales, la vista primero."

---

## 3. La prueba de control que nadie corrió

Una captura del cliente muestra un caso con Last Name y First Name en blanco, el
2026-TMW-40004406-INT-6. Otra muestra un caso con nombre, Michael Harvey. Tailored Brands tiene casos
sin registro de persona asociado. Una búsqueda por Suspect con apellido no devuelve esos casos para
nadie.

Nadie ha confirmado que exista un suspect apellidado Peters en un caso visible por cualquier usuario.
Pídele a Dexter Monroe que corra exactamente la misma búsqueda: Search On Suspect, Last Name Peters.
Toma cinco minutos y decide todo el ticket.

Si Dexter también recibe cero filas, esto no es permisos. Es un dato que no existe, y el ticket se
resuelve con el cliente en vez de escalarse.

Si Dexter recibe filas y Beverly no, el alcance por usuario queda confirmado como causa y la
escalación va con evidencia sólida.

---

## 4. Paso a paso

**Paso 0. Prueba de control, hoy.** Pídele a Colton que Dexter corra la búsqueda idéntica. Bloquea
todo lo demás hasta tener el resultado. El borrador está en la sección 6.

**Paso 1. SQL de solo lectura en 209-tbi, los tres usuarios lado a lado.** El bloque está en la
sección 5. Salen cuatro cosas: nivel efectivo, grupos, teams y filas de jerarquía.

**Paso 2. Abre la pestaña Location Hierarchy en SSO+ para Beverly y Francesca.** Compárala contra la
de Dexter. Captura las tres. Esta es la variable que falta.

**Paso 3. Confirma que Peters existe.** Consulta directa por el apellido y anota en qué tienda y
distrito cae el caso, para cruzarlo contra la jerarquía de cada usuario.

**Paso 4. Decide la ruta con lo que salga.**

- Jerarquía vacía o mal asignada, y se corrige desde Control Panel: es configuración. Arregla, verifica
  con `sso.GetUserSecurityLevel` y la vista `incident.lpuser`, y pasa a Under Customer Review.
- Jerarquía correcta y la búsqueda sigue vacía: es código. Escala a Engineering.
- Peters no existe para nadie: es dato del cliente. Respuesta al cliente y Under Customer Review.

**Paso 5. Escala hoy o mañana, sin dejar pasar más.** Detalle en la sección 7.

---

## 5. Bloque SQL, solo SELECT

Servidor `sqldb-prd-wus2-arp-production-209-tbi-platform`.

```sql
-- Nivel de seguridad efectivo, los tres usuarios
EXEC sso.GetUserSecurityLevel @userName = 'Beverly.Wright@tailoredbrands.com';
EXEC sso.GetUserSecurityLevel @userName = 'francesca.ramos@tailoredbrands.com';
EXEC sso.GetUserSecurityLevel @userName = 'Dexter.Monroe@tailoredbrands.com';

-- Filas crudas de asignacion, para ver duplicados y casing
SELECT UserName, SecurityID, Persistent, InsertedDateTime, UtcDateFrom, UtcDateTo
FROM sso.SecurityLevelAssignments
WHERE UserName LIKE '%wright%' OR UserName LIKE '%ramos%' OR UserName LIKE '%monroe%'
ORDER BY UserName, Persistent DESC, InsertedDateTime DESC;

-- Grupos por usuario
EXEC sso.GetSSOPermissionGroupsByUserName @userName = 'Beverly.Wright@tailoredbrands.com';
EXEC sso.GetSSOPermissionGroupsByUserName @userName = 'francesca.ramos@tailoredbrands.com';
EXEC sso.GetSSOPermissionGroupsByUserName @userName = 'Dexter.Monroe@tailoredbrands.com';

-- Jerarquia de ubicaciones, la variable que falta
SELECT lhua.*
FROM secure.LocationHierarchyUserAssignments lhua
JOIN membership.Users u ON u.UserID = lhua.UserID
WHERE u.UserName LIKE '%wright%' OR u.UserName LIKE '%ramos%' OR u.UserName LIKE '%monroe%';

-- CORREGIDO 2026-08-25. La vista no tiene columna UserName, tiene email y loginid.
SELECT TOP 1 * FROM incident.lpuser;   -- mira la forma primero
SELECT * FROM incident.lpuser
WHERE email IN ('beverly.wright@tailoredbrands.com',
                'francesca.ramos@tailoredbrands.com',
                'dexter.monroe@tailoredbrands.com');

-- Puntero colgante hacia incident.LPUser2
SELECT u.UserName, u.IncidentUserID, lp.UserID AS lpuser2_match
FROM membership.Users u
LEFT JOIN incident.LPUser2 lp ON lp.UserID = u.IncidentUserID
WHERE u.UserName LIKE '%wright%' OR u.UserName LIKE '%ramos%' OR u.UserName LIKE '%monroe%';

-- CORREGIDO 2026-08-25. incident.CaseSubject no existe, me la inventé.
-- Las tablas reales documentadas son MasterCase y Shoplifting, y en algunos
-- tenants viven en el esquema dbo y no en incident. Descubre antes de consultar.
SELECT TABLE_SCHEMA, TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME LIKE '%MasterCase%' OR TABLE_NAME LIKE '%Shoplift%'
   OR TABLE_NAME LIKE '%Suspect%'   OR TABLE_NAME LIKE '%Subject%'
ORDER BY TABLE_SCHEMA, TABLE_NAME;
```

---

## 6. Borrador para el cliente, pégalo hoy

Rompe los 5 días de silencio y pide la prueba de control. Bloque limpio, sin markdown.

```
Hi Colton,

Thank you for the detail and the screenshots, they narrow this down considerably.

One observation changes our working theory. Beverly resolves to Corporate User and Francesca resolves
to Location Manager, two different security levels, and both return the same empty result. That tells
us the security level is not what separates a working account from a failing one, so we are widening
the review to location hierarchy and team assignment, which we have not yet examined for either user.

Before we take this to Engineering I need one control test from your side, and it should take five
minutes. Please ask Dexter Monroe to run the exact same search that Beverly and Francesca ran: Search
On set to Suspect, Last Name Peters, no other filters. Send me a screenshot of his result either way,
including an empty one.

Dexter has full Administrator access and his Edit action already works, so his result tells us whether
a suspect record named Peters is reachable at all. If his search also comes back empty, the records
are not in scope for anyone and this is not a permissions problem. If his search returns rows and
Beverly's does not, we have isolated the difference to her account scope and we escalate with that
evidence.

I am running a parallel review of both accounts on our side today, comparing security level,
permission groups, user teams and location hierarchy against Dexter as the working reference. I will
come back with what we find regardless of when your test lands.

Thank you,
Juan
```

---

## 7. Escalamiento

**Escala.** Los argumentos, en orden de peso:

1. El cliente lo pidió explícitamente el 20 de agosto: "Can we have engineering review what may be
   causing the issue of these specific users not being able to Search".
2. Hay un defecto de código ya documentado y sin ticket. El RCA del 28 de julio dice que
   `sso.GetUserSecurityLevel` hace `SELECT TOP 1 ... ORDER BY Persistent DESC` sin desempate
   secundario, que la selección es arbitraria cuando dos filas comparten el valor, y que es un
   "latent defect that can affect any user with multiple feed assignments". Prometió un ticket ENG.
   **Ese ticket ENG nunca se creó.** No aparece en ninguna parte de la base. Un defecto latente
   confirmado que puede afectar a cualquier cliente lleva 28 días sin registrar.
3. Support ya intentó arreglarlo dos veces, el DELETE del 24 de julio y el cambio de grupo Okta del
   13 de agosto, y ninguno sostuvo el resultado.
4. 34 días, SLA corriendo, cliente con go live de 800 tiendas ya pasado el 3 de agosto.

**Ruta.** Transición **231 Waiting for Engineering**, destino **Under Engineering Review**. Confirmada
como disponible en Jira hoy. El ticket se reasigna, el ENG lo auto crea la transición y los
comentarios sincronizan en ambos sentidos. Para Secure e Incident el destinatario es Shandana Khan.
No crees el ENG a mano.

**Requisito antes de mover.** El procedimiento L3 exige entorno, pasos completos de reproducción con
capturas, notas de triage con lo que se descartó, conversaciones fuera del ticket, y aviso al cliente.
Aimee devolvió cuatro tickets de Vedant el 13 de agosto por faltar exactamente eso. Por eso el paso 0
va primero. Escalar hoy sin la prueba de control te devuelve el ticket.

**Comentario interno para pegar al momento de la transición:**

```
Escalating to Incident Engineering.

Environment: Production, tenant 209-tbi, sqldb-prd-wus2-arp-production-209-tbi-platform.

Symptom. Two users, Beverly Wright and Francesca Ramos, authenticate successfully, load the Incident
main menu, and run an Incident search with Search On set to Suspect and Last Name Peters. The search
executes, delays roughly one minute, and returns No data to display. No error is raised. A third
user, Dexter Monroe, performs equivalent actions successfully.

What Support ruled out.

1. SSO group data. sso.GetSSOPermissionGroupsByUserName returns the complete group set for the
working user. Group retrieval is not failing.

2. Security level as the discriminator. Beverly resolves to Security Level 11 Corporate User and
Francesca resolves to Security Level 5 Location Manager. Both produce the identical empty result.
Two different levels, one symptom. Our earlier RCA attributed the failure to Level 11 lacking search
access. That attribution does not hold and should not be carried forward.

3. Manual override conflict. On 2026-07-24 we removed Beverly's manual SSO+ override row from
sso.SecurityLevelAssignments with SSO owner approval. sso.GetUserSecurityLevel returned Level 5
immediately afterward. The result did not persist across logins.

4. Okta group claim. On 2026-08-13 the customer removed both users from
TMW-APP-OKTA-SSO-Appriss-EBR-CorporateUser in the daily feed. Beverly still displayed as Corporate
User on 2026-08-20 and the search still returned zero rows.

What Support needs from Engineering.

A. Confirm what row level scope the Incident suspect search applies per user, and which table or view
supplies it. Our reading points to location hierarchy assignment rather than security level, because
the query executes and returns zero rows rather than raising an authorization error.

B. Confirm the defect already identified in sso.GetUserSecurityLevel. The procedure performs
SELECT TOP 1 with ORDER BY Persistent DESC and no secondary tiebreaker. When two rows share the same
Persistent value the selection is arbitrary. This was observed on Matthew Sincic, who held two feed
rows at Level 13 and Level 2 with Persistent NULL on both and resolved to Level 2. This is a latent
defect affecting any user with multiple feed assignments and it needs a deterministic tiebreak. No
ENG ticket was raised for it at the time.

C. Confirm whether duplicate permission group rows for the same group, one Persistent True and one
Persistent False, are expected. Both failing users carry two ApprissCase Search Users rows.

Business context. Tailored Brands completed an 800 store go live on 2026-08-03. The ticket has been
open 34 days. The customer requested Engineering review on 2026-08-20.

Evidence. Customer screenshots in the ticket. SQL evidence in sso.SecurityLevelAssignments,
sso.GetUserSecurityLevel and sso.ResponseLog IDs 18781 and 18782. Prior investigation notes and RCA
in the comment history of this ticket, with the Level 11 attribution corrected as noted above.
```

Rellena las secciones A y el resultado de la prueba de control antes de mover el ticket.

---

## 8. Huecos que quedan abiertos

- El ticket ENG del desempate en `sso.GetUserSecurityLevel` no existe. Créalo o exígelo en la
  escalación. Es el hallazgo con más alcance de todo el ticket.
- RCS-27578 aparece una sola vez en toda la base, como referencia suelta en un comentario de este
  mismo ticket. No hay ficha ni conclusión. Si importa, hay que traerlo de Jira.
- RCS-27269 es de Tailored Brands y es de mapeo de Security Levels, mismo dominio, cerrado, de Peyman.
  Su conclusión técnica no está escrita en ninguna parte. Vale pedírsela a Peyman antes de escalar.
- El significado de la bandera `Persistent` se contradice entre fuentes.
  `brain/memoria/reference_sso_incident_diagnostico.md` dice que TRUE viene de import de archivo y
  FALSE se puso a mano. La evidencia de este ticket dice lo contrario, feed igual a NULL y override
  manual igual a 1. Sin resolver. No lo afirmes en ninguna dirección hasta verificarlo.
- Toda la evidencia de niveles de seguridad de este ticket vive solo en `cola/jira-dump.json`. Nunca
  se promovió a `brain/memoria/`. `bin/buscar` no la encuentra. Guárdala.

---

# ADENDA · 2026-08-25 tarde · Resultados del SQL

Juan corrió el bloque. Cinco consultas devolvieron datos, dos fallaron por error mío. Lo que salió
reemplaza el diagnóstico de las secciones 2 y 3.

## A. El hallazgo

```
SELECT u.UserName, u.IncidentUserID, lp.UserID AS lpuser2_match
FROM membership.Users u
LEFT JOIN incident.LPUser2 lp ON lp.UserID = u.IncidentUserID
```

| UserName | IncidentUserID | lpuser2_match |
|---|---|---|
| dexter.monroe@tailoredbrands.com | 22 | **22** |
| beverly.wright@tailoredbrands.com | 50267 | **NULL** |
| francesca.ramos@tailoredbrands.com | 50268 | **NULL** |

**Beverly y Francesca no tienen fila en `incident.LPUser2`.** Su `IncidentUserID` apunta a un
`UserID` que no existe. Dexter, el único que funciona, resuelve limpio.

Esto es el **puntero colgando**, clase 3 del esquema de usuarios de Incident, ya documentado en
`brain/memoria/reference_esquema_usuarios_incident.md`:

> "Puntero colgando: `membership.Users.IncidentUserID` apunta a un `UserID` que no existe en
> `incident.LPUser2`. 77 usuarios activos así en ADUSA el 10 ago. Este es el vínculo roto que rompe
> `GetSSOPermissionGroupsByUserName`. **Soporte no lo puede arreglar.**"

Y el mecanismo, del mismo archivo, describe el síntoma de este ticket palabra por palabra:

> "El proceso de alta escribe en `membership.Users` y se salta las dos tablas de abajo. Autenticar
> solo necesita `membership.Users`, así que **el usuario entra sin problema y después no ve tiendas
> ni puede crear caso**."

Beverly y Francesca autentican, cargan el menú, corren la búsqueda, esperan un minuto y reciben cero
filas sin error. Es exactamente eso.

El rango de IDs confirma el origen. El mismo archivo dice que los punteros colgantes caen en el rango
bajo de cinco dígitos y que eso "apunta al proceso que crea filas nuevas, no a la carga original de
la migración". Dexter es 22, de la carga vieja. Beverly y Francesca son 50267 y 50268, consecutivos,
del proceso nuevo.

## B. Lo que esto entierra

**El nivel de seguridad.** `GetUserSecurityLevel` devolvió 11 para Beverly, 13 para Dexter y
**conjunto vacío para Francesca**. En `sso.SecurityLevelAssignments` no existe ninguna fila para
`francesca.ramos@tailoredbrands.com`. Beverly tiene nivel, Francesca no tiene ninguno, y las dos
fallan igual. La variable no discrimina. Cierra esa línea.

Dato aparte que hay que reportar igual: la UI de SSO+ muestra a Francesca como Location Manager y la
base no tiene fila que lo respalde. La UI está mostrando algo que el procedimiento no devuelve.

**Los permission groups.** Beverly tiene `ApprissCase Search Users` y `Basic Users`. Francesca tiene
solo `ApprissCase Search Users`. Distinto entre ellas, mismo fallo. Y ya estaba escrito en
`brain/markdown/16-rcs-soluciones.md`: "Permission groups no es el diferenciador." Cierra esa línea
también.

**Mi hipótesis de Location Hierarchy: sin confirmar, y probablemente equivocada.** La consulta
devolvió tres filas, todas con `HierarchyId` 1, `LocationHierarchy1` igual a TBI y `LocationHierarchy2`
a `6` y `LocationId` en NULL. No seleccioné el UserName, así que no sé de quién es cada fila. Si las
tres son nuestros tres usuarios, tienen alcance idéntico y la jerarquía tampoco discrimina. Repite la
consulta con el nombre antes de afirmar nada. La consulta corregida está abajo.

**El defecto del `ORDER BY Persistent DESC` sigue vivo y sigue sin ticket ENG.** Dexter tiene dos
filas, 13 con Persistent 1 y 2 con Persistent NULL. Resuelve a 13. No es la causa de este ticket. Es
un defecto latente real que hay que reportar de todos modos.

## C. Los dos que fallaron, y por qué

**`incident.lpuser`** dio `Invalid column name 'UserName'`. La vista existe, el error es de columna.
La vista no tiene `UserName`. Sus columnas de identidad son `email` y `loginid`, según
`brain/memoria/reference_esquema_usuarios_incident.md` y `brain/markdown/16-rcs-soluciones.md`.
`UserName` pertenece a `membership.Users`. Yo mezclé las dos.

**`incident.CaseSubject`** dio `Invalid object name`. Esa tabla no existe. La inventé, y el archivo
original lo advertía. Las tablas reales documentadas son `MasterCase` y `Shoplifting`. Advertencia
adicional de `brain/markdown/16-rcs-soluciones.md`: en al menos un tenant "los datos reales viven en
schema dbo, NO en schema incident (vacío)". Descubre el esquema en vez de asumirlo.

## D. Consultas corregidas

```sql
-- 1. La vista, por email
SELECT TOP 1 * FROM incident.lpuser;
SELECT * FROM incident.lpuser
WHERE email IN ('beverly.wright@tailoredbrands.com',
                'francesca.ramos@tailoredbrands.com',
                'dexter.monroe@tailoredbrands.com');

-- 2. LA CONSULTA QUE DECIDE LA RUTA DEL FIX.
-- Distingue "no tiene fila en LPUser2" de "tiene fila pero el puntero no le apunta".
-- El script de Kiran del 14 ago une por UserName = LoginID dentro de LPUser2,
-- asi que a quien no tenga fila no lo alcanza. Ese punto ciego esta documentado.
SELECT mu.UserName, mu.Email, mu.IncidentUserID,
       lp_id.UserID    AS match_por_incidentuserid,
       lp_login.UserID AS match_por_loginid,
       lp_login.LoginID, lp_login.EmailAddr, lp_login.StoreIdent, lp_login.Inactive
FROM membership.Users mu
LEFT JOIN incident.LPUser2 lp_id
       ON lp_id.UserID = mu.IncidentUserID
LEFT JOIN incident.LPUser2 lp_login
       ON CAST(lp_login.LoginID AS NVARCHAR(100)) = CAST(mu.UserName AS NVARCHAR(100))
WHERE mu.Email IN ('beverly.wright@tailoredbrands.com',
                   'francesca.ramos@tailoredbrands.com',
                   'dexter.monroe@tailoredbrands.com');

-- 3. Cuantos usuarios mas de Tailored Brands estan rotos igual.
-- En ADUSA esto dio 77 y solo unos pocos habian reclamado.
SELECT COUNT(*) AS punteros_colgando
FROM membership.Users mu
WHERE mu.IncidentUserID IS NOT NULL
  AND NOT EXISTS (SELECT 1 FROM incident.LPUser2 lp WHERE lp.UserID = mu.IncidentUserID);

SELECT mu.UserName, mu.Email, mu.IncidentUserID, mu.FirstName, mu.LastName
FROM membership.Users mu
WHERE mu.IncidentUserID IS NOT NULL
  AND NOT EXISTS (SELECT 1 FROM incident.LPUser2 lp WHERE lp.UserID = mu.IncidentUserID)
ORDER BY mu.IncidentUserID DESC;

-- 4. LHUA con el nombre, para saber de quien es cada fila
SELECT mu.UserName, mu.Email, lhua.*
FROM secure.LocationHierarchyUserAssignments lhua
JOIN membership.Users mu ON mu.UserID = lhua.UserId
WHERE mu.Email IN ('beverly.wright@tailoredbrands.com',
                   'francesca.ramos@tailoredbrands.com',
                   'dexter.monroe@tailoredbrands.com');

-- 5. Descubrir el esquema de casos antes de buscar a Peters
SELECT TABLE_SCHEMA, TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME LIKE '%MasterCase%' OR TABLE_NAME LIKE '%Shoplift%'
   OR TABLE_NAME LIKE '%Suspect%'   OR TABLE_NAME LIKE '%Subject%'
ORDER BY TABLE_SCHEMA, TABLE_NAME;
```

## E. Qué cambia en el plan

La prueba de control con Dexter deja de ser bloqueante. Ya tenemos el discriminador en base, y es más
fuerte que una captura del cliente. Pídela igual, cuesta cinco minutos y descarta el caso de que
Peters no exista.

La consulta 3 es la que puede cambiar el tamaño del ticket. Si Tailored Brands tiene decenas de
usuarios con el puntero roto y solo dos reclamaron, esto deja de ser un ticket de dos personas.

**Escala.** Soporte no puede arreglar esto, está escrito. El fix es un script en producción sobre
`incident.LPUser2` y lo ejecuta Kiran Vadday. Reemplaza las secciones A, B y C del comentario interno
de escalación de la sección 7 por el hallazgo del puntero colgante, con la tabla de tres filas como
evidencia. Los 77 de ADUSA nunca se reportaron como ticket propio. Este es el momento de que ese
defecto tenga uno.

---

# ADENDA 2 · 2026-08-25 · Contraste contra la tasa base

Juan pidió verificar antes de escalar. Tenía razón en desconfiar. La consulta 3 devolvió **267
usuarios** sin fila en `incident.LPUser2`. Declarar 267 usuarios rotos a partir de una muestra de dos
es un salto que no da la evidencia.

## A. Lo que la lista dice de verdad

267 usuarios, dominios así:

| Dominio | Usuarios | Qué es |
|---|---|---|
| kgstores.com | 86 | K&G, banner de Tailored Brands |
| trebu.co | 82 | **personal de Appriss** |
| menswearhouse.com | 59 | Men's Wearhouse, banner |
| tailoredbrands.com | 20 | corporativo |
| josabank.com | 16 | Jos. A. Bank, banner |
| mooresclothing.com | 4 | Moores, banner |

Entre los 82 de Appriss están Kiran Vadday, Zackary Graas, Peyman Motlagh, Ryan Barlow, Matt
Kamminga, Shelley Cameron y el propio Juan. Kiran es quien ejecuta el fix de este defecto y aparece
en la lista de rotos. Eso solo ya obliga a frenar.

## B. El dato que decide, y que no estaba a la vista

Todos los IDs de la lista caen entre 50000 y 50406. Ese bloque tiene 407 posiciones. Solo 267
aparecen como colgantes.

**140 IDs del mismo bloque no están en la lista, o sea que sí tienen fila válida en `LPUser2`.**

Y no están agrupados. Están intercalados uno a uno con los rotos: 50003, 50005, 50007, 50012, 50018,
50019, 50022, 50025. Vecinos inmediatos, unos con fila y otros sin ella.

Eso descarta las dos explicaciones cómodas. No es que el bloque 50xxx sea "usuarios que por diseño no
tienen registro en Incident", porque un tercio sí lo tiene. Y no es una carga que falló completa,
porque habría cortado en bloque, no salteado.

**Es un alta que falla de forma intermitente**, aproximadamente 2 de cada 3. El cerebro ya describió
esa misma firma en ADUSA, en `brain/memoria/reference_esquema_usuarios_incident.md`:

> "Contraejemplo del mismo lote: dos usuarios creados el 29 jul en el mismo segundo sí tienen las dos
> filas, así que **el alta falla de forma intermitente, no siempre**."

Misma firma, otro cliente, y Tailored Brands no está en las olas de migración. Refuerza que el
defecto está en el proceso de alta de usuarios, no en la migración.

## C. Lo que sigue sin estar probado

Que la fila faltante **cause** la búsqueda vacía. Es correlación con cuatro casos y cero
contraejemplos, no causalidad demostrada.

| Usuario | Fila en LPUser2 | Búsqueda en Incident |
|---|---|---|
| Dexter Monroe | sí, UserID 22 | funciona |
| Matthew Sincic | sí, no aparece en la lista de colgantes | funciona, su Edit se resolvió |
| Beverly Wright | no | falla |
| Francesca Ramos | no | falla |

Cuatro de cuatro consistentes. Con 267 colgantes y solo tres quejas, la pregunta que falta es por qué
los otros 264 no reclaman. La respuesta probable es que no usan la búsqueda de Incident, y hay que
demostrarlo, no suponerlo.

## D. Lo que sí quedó resuelto

**Location Hierarchy queda descartada, ahora con el nombre en la fila.** Los tres usuarios tienen fila
en `secure.LocationHierarchyUserAssignments`, `HierarchyId` 1, `LocationHierarchy1` igual a TBI,
niveles 2 a 6 y `LocationId` en NULL. Alcance idéntico entre el que funciona y las que fallan. Mi
hipótesis de la adenda 1 estaba equivocada y queda cerrada.

Nota adicional: en ADUSA 75 de los 77 colgantes tampoco tenían fila en LHUA. Beverly y Francesca sí
la tienen. El patrón de Tailored Brands **no es idéntico** al de ADUSA. No los presentes como el
mismo caso.

**Los nombres reales de las tablas ya están.** `incident.MasterCase`, `incident.Suspect`,
`incident.Shoplifting`, `incident.ShopliftingExtra`, `incident.SuspectAgeSummary`. Todas en el esquema
`incident`, así que en este tenant no aplica la trampa del esquema `dbo`.

## E. Ronda final de verificación, solo SELECT

```sql
-- 1. LA PRUEBA QUE PUEDE TUMBAR TODO. Existe Peters?
SELECT COUNT(*) AS suspects_totales FROM incident.Suspect;
SELECT TOP 50 * FROM incident.Suspect WHERE LastName LIKE 'Peters%';

-- Si esto da cero filas, la busqueda vacia es comportamiento correcto
-- y los permisos no tienen nada que ver.

-- 2. Tasa base dura. Cuantos usuarios hay y que proporcion cuelga.
SELECT
  (SELECT COUNT(*) FROM membership.Users)  AS usuarios_membership,
  (SELECT COUNT(*) FROM incident.LPUser2)  AS filas_lpuser2,
  (SELECT MIN(UserID) FROM incident.LPUser2) AS min_id,
  (SELECT MAX(UserID) FROM incident.LPUser2) AS max_id;

-- 3. Separar las tres clases de fallo en un solo conteo
SELECT
  SUM(CASE WHEN lp_id.UserID IS NOT NULL THEN 1 ELSE 0 END) AS sano,
  SUM(CASE WHEN lp_id.UserID IS NULL AND lp_login.UserID IS NOT NULL THEN 1 ELSE 0 END) AS puntero_mal_pero_existe,
  SUM(CASE WHEN lp_id.UserID IS NULL AND lp_login.UserID IS NULL THEN 1 ELSE 0 END) AS sin_ninguna_fila
FROM membership.Users mu
LEFT JOIN incident.LPUser2 lp_id
       ON lp_id.UserID = mu.IncidentUserID
LEFT JOIN incident.LPUser2 lp_login
       ON CAST(lp_login.LoginID AS NVARCHAR(100)) = CAST(mu.UserName AS NVARCHAR(100));

-- Esto decide el fix. "Puntero mal pero existe" lo arregla un UPDATE.
-- "Sin ninguna fila" exige crear el usuario de Incident, que es otro trabajo.

-- 4. El control que falta. Usuarios que SI tienen fila, para comparar contra los que fallan.
SELECT TOP 30 mu.UserName, mu.Email, mu.IncidentUserID,
       lp.UserID, lp.LoginID, lp.StoreIdent, lp.Inactive
FROM membership.Users mu
JOIN incident.LPUser2 lp ON lp.UserID = mu.IncidentUserID
WHERE mu.IncidentUserID BETWEEN 50000 AND 50406
ORDER BY mu.IncidentUserID;

-- 5. Matthew Sincic, segundo control conocido que funciona
SELECT mu.UserName, mu.Email, mu.IncidentUserID,
       lp.UserID, lp.LoginID, lp.StoreIdent, lp.Inactive
FROM membership.Users mu
LEFT JOIN incident.LPUser2 lp ON lp.UserID = mu.IncidentUserID
WHERE mu.Email LIKE '%sincic%';

-- 6. Cuantos de los colgantes han iniciado sesion alguna vez.
-- En ADUSA 76 de 77 ya habian entrado. Si aca casi ninguno entro,
-- el hallazgo es mucho menos grave de lo que parece.
SELECT TOP 1 * FROM membership.Users;   -- ver si hay LastLoginDate o equivalente
```

La consulta 6 necesita que primero mires qué columna de última sesión existe. Si la mayoría de los
267 nunca entró, el problema es de provisión silenciosa y no de servicio degradado.

## F. Qué le pasa al plan

**No escales todavía.** Corre la consulta 1 primero. Si Peters no existe en `incident.Suspect`, el
ticket se cierra con el cliente y las 34 días de investigación de permisos fueron por el camino
equivocado desde el principio.

Si Peters existe, corre la 3 y la 5. Con eso el comentario de escalación deja de decir "dos usuarios
tienen un puntero roto" y pasa a decir cuántos usuarios del tenant están en cada clase de fallo y qué
tipo de fix necesita cada una. Esa versión no la devuelve Engineering.

**Corrige la adenda 1 antes de reusarla.** La afirmación "es el puntero colgando, mismo defecto que
los 77 de ADUSA" está de más. Lo que hay es un patrón consistente en cuatro usuarios, un bloque de
IDs con fallo intermitente de 2 en 3, y una firma parecida a la de ADUSA con una diferencia clara en
LHUA.

---

# ADENDA 3 · 2026-08-25 · Peters existe, y aparece el alcance por tienda

## A. La prueba decisiva pasó

`incident.Suspect` tiene 20.278 filas. `LastName LIKE 'Peters%'` devuelve coincidencias exactas de
Peters, más Peterson y Peterson Hanes.

| SuspectID | StoreIdent | MasterCaseID | Nombre | EmployeeID | Puesto |
|---|---|---|---|---|---|
| 671 | 5361 | 671 | Eli Peters | 324542 | Store Lead |
| 11990 | 6665 | 11990 | Cory Peters | vacío | vacío |
| 15353 | 3902 | 15353 | MILA Peters | LTP11 | Consultant |
| 20549 | 5076 | 20549 | Alijah Peters | 340150 | Store Lead |

**El dato existe.** La búsqueda de Beverly y Francesca debería devolver filas. El "No data to display"
no es comportamiento correcto. La hipótesis del usuario sin registro en Incident sigue en pie y el
ticket es real.

Dos observaciones de estructura. `SuspectID` es igual a `MasterCaseID` en las ocho filas, así que la
relación es uno a uno. Y los registros traen `EmployeeID` y `EmployeePosition` poblados, consistente
con el caso de uso que Beverly declaró en el ticket: bajar documentación de casos de empleados para
reclamos de desempleo.

## B. El dato que obliga a rediseñar la prueba de control

Los cuatro Peters están en las tiendas **5361, 6665, 3902 y 5076**.

La fila de `LPUser2` de Dexter tiene `StoreIdent` **4825**.

**Ningún caso de Peters está en la tienda de Dexter.** Si la búsqueda filtra por tienda, Dexter
también recibe cero filas, y ese cero no prueba nada sobre permisos. La prueba que propuse en la
sección 3 tiene ese punto ciego y hay que corregirla antes de pedírsela al cliente.

Predicción, para que quede escrita antes de correrla. Si Dexter busca Peters y recibe filas, el
alcance es de compañía y la tienda no filtra, y entonces la diferencia está en el usuario. Si recibe
cero, el alcance por tienda manda y hay que rehacer todo el análisis con esa variable.

## C. La prueba pareada, que aísla la variable de verdad

En vez de buscar un apellido cualquiera, busca uno que exista **en la tienda de Dexter**, y que lo
corran los tres usuarios.

```sql
-- Elegir el apellido para la prueba pareada
SELECT TOP 20 SuspectID, StoreIdent, MasterCaseID, LastName, FirstName,
       SubjectType, EmployeeID, EmployeePosition
FROM incident.Suspect
WHERE StoreIdent = 4825
ORDER BY SuspectID DESC;
```

Con ese apellido en la mano, tres búsquedas idénticas, Search On Suspect, mismo Last Name, sin más
filtros. Dexter, Beverly y Francesca. Misma data, mismo alcance de tienda, tres usuarios. Lo único
que varía es el usuario, que es exactamente lo que hay que medir.

Resultados posibles y qué significa cada uno:

- Dexter encuentra, las dos no: la diferencia es del usuario. Escala con eso.
- Los tres encuentran: el problema es solo con los datos fuera de la tienda de Dexter, o sea alcance,
  no identidad. Cambia la ruta del fix.
- Ninguno encuentra: la búsqueda por Suspect está rota para todos y es un bug de aplicación, con lo
  cual el ticket cambia de naturaleza y de prioridad.

## D. Lo que falta consultar antes de escribirle al cliente

```sql
-- 1. Columnas de MasterCase, para no volver a adivinar
SELECT COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'incident' AND TABLE_NAME = 'MasterCase'
ORDER BY ORDINAL_POSITION;

-- 2. Los casos de Peters con su estado, por si estan cerrados, borrados o privados
SELECT s.SuspectID, s.StoreIdent, s.MasterCaseID, s.LastName, s.FirstName,
       s.SubjectType, s.PrivateRecord, s.Deleted
FROM incident.Suspect s
WHERE s.LastName = 'Peters';

-- 3. Hay una vista que se llama ViewFilteredSuspects. Mirar que filtra.
SELECT TOP 1 * FROM recommendation.ViewFilteredSuspects;

-- 4. Las tiendas de los Peters y la de Dexter, en la misma jerarquia?
SELECT LocationId, StoreIdent, LocationHierarchy1, LocationHierarchy2,
       LocationHierarchy3, LocationHierarchy4
FROM place.Location
WHERE StoreIdent IN (4825, 5361, 6665, 3902, 5076);
```

La consulta 4 vale por sí sola. Si la tienda de Dexter y las de los Peters cuelgan de ramas distintas,
el alcance por jerarquía vuelve a la mesa y mi descarte de la adenda 2 queda incompleto.

## E. Estado del diagnóstico

Confirmado: el dato existe, el síntoma es real, LHUA es idéntica entre los tres usuarios, el nivel de
seguridad y los permission groups no discriminan, y 267 de 407 usuarios del bloque nuevo no tienen
fila en `incident.LPUser2` por un alta que falla de forma intermitente.

Sin probar: que la fila faltante cause la búsqueda vacía. Cuatro casos consistentes, cero
contraejemplos, ninguna prueba pareada todavía.

Sin mirar: si la búsqueda filtra por tienda. Es la variable que puede tumbar el análisis entero y
recién aparece ahora, en la columna `StoreIdent` de los suspects.

Sigue sin escalar hasta cerrar la prueba pareada de la sección C.

---

# ADENDA 4 · 2026-08-25 · El alcance por tienda queda descartado

## A. Resultado

`incident.Suspect` con `StoreIdent = 4825` devuelve **cero filas**. La tienda de Dexter no tiene
suspects. La prueba pareada de la adenda 3 no se puede armar.

`place.Location` no tiene columna `StoreIdent`. Adiviné el nombre por segunda vez. Introspecciona.

## B. Lo que el cero prueba

Dexter tiene `StoreIdent` 4825 en `LPUser2`. Su tienda no tiene suspects. La captura del cliente lo
muestra encontrando a Michael Harvey en el caso 2026-TMW-40003407-INT-6.

**Dexter encuentra casos fuera de su tienda. El `StoreIdent` del usuario no filtra la búsqueda.**

Descarto el alcance por tienda. La predicción de la adenda 3 queda resuelta sin necesidad de correr
la prueba. La búsqueda de Peters recupera validez como control.

## C. Siguiente consulta

```sql
SELECT COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'place' AND TABLE_NAME = 'Location'
ORDER BY ORDINAL_POSITION;
```

## D. Prueba de control, versión final

Colton le pide a Dexter: Search On Suspect, Last Name Peters, sin más filtros. Captura del resultado.

Dexter encuentra y las dos no: la diferencia es del usuario. Escala.
Dexter tampoco encuentra: la búsqueda por Suspect está rota para todos. Cambia la prioridad.

## E. Variables descartadas hasta aquí

Nivel de seguridad. Permission groups. Location hierarchy. StoreIdent del usuario.

Queda en pie: la fila ausente en `incident.LPUser2`. Cuatro casos consistentes, cero contraejemplos.
