# RCS-28032 · cierre de evidencia · la hipotesis del multidistrito se cae · listo para escalar

Fecha: 2026-08-25
Client ID 433. Estado en Jira: Work in progress, assignee Juan, Medium, labels FromEmail, L1, Uni_Jul_26_WAFAccess.
Ultimo movimiento del cliente: Joe Austin, 18 ago, con las capturas. Siete dias sin respuesta nuestra.

## 1. La query derriba la explicacion que llevabamos

Resultado de `incident.Store`:

| StoreIdent | StoreNo | StoreName | Region | District | DistrictManagerID |
|---|---|---|---|---|---|
| 946 | 1016 | Federal Way WA Store | 3 | **501** | 10419 |
| 617 | 249 | Tanasbourne OR Store | 3 | **501** | 10419 |
| 466 | 500 | Everett WA Store | 3 | **501** | 10419 |

**Las tres tiendas de Dayna estan en el distrito 501.** Ninguna esta en el 504.

El analisis del 10 de agosto que quedo escrito en el ticket decia: *"Dayna 617, store 249 Tanasbourne OR,
district 504. She sees 504."* Hoy esa misma tienda devuelve District 501.

Consecuencia directa: Dayna ve 501 porque todas sus tiendas estan en 501. No ve 504 porque no tiene ninguna
tienda en 504. Eso no es un fallo de asignacion multiple. Es que el 504 no existe en su alcance.

**La hipotesis de que un usuario con dos filas en LHUA solo ve un distrito a la vez no se sostiene con este
caso.** Nunca hubo dos distritos que resolver.

Queda una contradiccion sin cerrar y hay que decirla asi: o los datos de distrito de la tienda 249 cambiaron
entre el 10 y el 25 de agosto, o la lectura del 10 de agosto fue incorrecta. No se puede decidir con lo que
hay.

## 1b. El distrito 504 existe, tiene 9 tiendas, y Dayna figura como manager de una de ellas

    SELECT StoreIdent, StoreNo, StoreName, Region, District, DistrictManagerID
    FROM incident.Store
    WHERE District = '504';

| StoreIdent | StoreNo | StoreName | Region | District | DistrictManagerID |
|---|---|---|---|---|---|
| 377 | 541 | Puyallup WA Store | 3 | 504 | 49781 |
| 618 | 250 | Redmond WA Store | 3 | 504 | 80288 |
| 700 | 313 | Tukwila WA Store | 3 | 504 | 49781 |
| 764 | 393 | Issaquah WA Store | 3 | 504 | 49781 |
| 895 | 589 | Tacoma WA Store | 3 | 504 | 49781 |
| 938 | 1026 | South Lake Union WA Store | 3 | 504 | 80288 |
| 948 | 1018 | Bremerton WA Store | 3 | 504 | **10419** |
| 956 | 1023 | Clackamas OR Store | 3 | 504 | 49781 |
| 1292 | 1033 | Issaquah WA Store | 3 | 504 | 49781 |

Tres cosas salen de aca.

**El 504 no se desarmo.** Tiene nueve tiendas activas. Descartada esa via.

**La tienda 948, Bremerton WA, StoreNo 1018, lleva DistrictManagerID 10419**, el mismo valor que llevan las
tres tiendas de Dayna en el 501. Esa tienda esta en el 504 y no esta en su alcance de LHUA. Falta confirmar
que 10419 es ella:

    SELECT UserID, FirstName, LastName, EmailAddr FROM incident.LPUser WHERE UserID = 10419;

**El distrito 504 tiene tres district managers distintos.** 49781 en seis tiendas, 80288 en dos, 10419 en
una. Eso es inconsistencia de datos maestros del cliente y hay que reportarlo, con independencia del resto.

## 1c. Esto reabre el caso A, y lo vuelve barato de cerrar

La lectura mas simple que explica todo lo observado: el alcance de distrito se hereda de las tiendas
asignadas en LHUA, y hoy las tres tiendas de Dayna estan en el 501. Ve el 501 por eso. No ve el 504 porque no
tiene ninguna tienda del 504 asignada.

Encaja con lo que paso el 4 de agosto. Antes de ese cambio veia 504. Despues del cambio vio 501 y perdio 504.
Si el cambio le movio la tienda primaria de una del 504 a una del 501, el resultado es exactamente ese.

**El experimento que decide, y cuesta un cambio reversible en Control Panel:** asignarle en LHUA la tienda
948, Bremerton WA, que es del 504 y de la que ella ya figura como manager. Tres resultados posibles:

- Ve 501 y 504. El multidistrito funciona y el problema era que le faltaba una tienda del 504.
- Gana 504 y pierde 501. El multidistrito no se honra. Ahi si es bug y va a ingenieria con evidencia limpia.
- No cambia nada. El alcance no se resuelve por tienda asignada y hay que volver al modelo.

**Coordinar con Joe antes de correrlo.** Si pierde el 501, Dayna queda peor que hoy y no puede trabajar. El
4 de agosto ya paso algo asi sin avisarle.

## 2. La consola descarta el crash de JavaScript

Los dos mensajes son de carga inicial de la pagina, ninguno se dispara al pulsar Next:

- `[Violation] Permissions policy violation: unload is not allowed in this document`, desde `DXR.axd`. Es un
  aviso del navegador sobre el evento unload de DevExpress. No es excepcion.
- `Bootstrap doesn't allow more than one instance per element. Bound instance: bs.tooltip.`, desde
  `data.js:26`, con la pila `cpf.ui.js:8944 → bootstrap → popover → getOrCreateInstance`. Ocurre dentro del
  ready de jQuery. Se intenta montar un popover sobre un elemento que ya tiene un tooltip.

El indicador de la barra dice "No Issues found".

Entonces: al pulsar Next no se lanza excepcion y no sale ningun request. **El boton no falla, el codigo
decide no enviar.** `btnSave_Click` valida y retorna sin avisar, porque el hidden del StoreIdent sigue en 0.
Esto refuerza el hallazgo del HAR y descarta la via del error de script.

El error de Bootstrap queda como observacion secundaria. Ocurre durante `AfterInitialize` de los controles
DevExpress. Vale mencionarlo a ingenieria por si esa excepcion corta la inicializacion de controles
posteriores. No hay evidencia de que lo haga.

## 3. Clientes para comparar NewAudit.aspx

Barrido con `cf[15196] = "Audit (f.k.a. CAMS)"` en RCS.

**Comparacion primaria, tenants con Audit sano.** Ninguno tiene tickets abiertos de pantallas de Audit rotas,
solo pedidos funcionales:

| Cliente | Por que sirve | Referencia |
|---|---|---|
| **Loomis** | El que mas usa el modulo. Tickets de comentarios, action plans y smart alerts, ninguno de acceso roto | RCS-27828, RCS-28318, RCS-27654 |
| **SpartanNash** | Audits en produccion, temas de contenido del reporte, no de la pantalla | RCS-27794, RCS-27315, RCS-28457 |

Si en cualquiera de esos dos el store lookup si persiste el StoreIdent y Next avanza, el defecto es de 433 o
de su configuracion. Si falla igual, es de la build 6.26.8 y afecta a todos.

**Segundo caso roto, y este es el que mas conviene mirar. Boot Barn, RCS-28321.**

Sigue Under Support Review, assignee Shandana Khan. David Vargas encontro el 12 de agosto:
`SystemSelect.aspx` 500, `LPSConstants: SetPlatformCohesionModeCookies Error: GetEncryptionKey: Record
missing in Options Table`, slug `/bootbarn`. Misma clase de excepcion que RCS-27509 en Guess y ENG-6198 en
Bunnings, cada uno con un valor de configuracion distinto faltante.

Shandana levanto un ENG nuevo el 19 de agosto y lo marco alta prioridad. **Y hoy, 24 de agosto a las 14:32,
Kiran comento ahi: "I do not believe this is a code issue. Could you please replicate the problem and share
the reproduction steps with me."**

Kiran esta pidiendo en Boot Barn exactamente lo que este HAR ya entrega para 433. Si el mecanismo resulta
ser el mismo, un valor de configuracion faltante en la tabla Options del slug que rompe el handoff de sesion
a Nettrack, explicaria de una sola vez los Screen Labels sin resolver y el StoreIdent que no persiste. Es una
hipotesis. Comprobarla cuesta un SELECT sobre la tabla Options del slug `/vitaminshoppe` buscando el registro
de encryption key.

**El slug de cada tenant** sale del Customer Server Profile, Confluence `474658570288`, mantenido por Ryan
Barlow y Matt Kamminga. No lo deduzcas del nombre.

## 4. Antecedente del propio cliente que hay que leer antes de escalar

**RCS-28005, Vitamin Shoppe, Secure Audit not working.** Under Engineering Review, assignee Matthew Kamminga,
label `Uni_Jul_26_UIBehavior`.

El 28 de julio las pantallas de Audit de 433 daban 404 en
`/nettrack/Audit/screens/incident/433/audit/screens/AuditSection_V268_S212.aspx`. Tyrone lo resolvio ese
mismo dia: *"The audit screens have been rebuilt and should now be accessible."*

El 13 de agosto, Matt Kamminga comento en el ENG vinculado: *"Add additional validation to confirm screens
are rebuilt as part of the migration path."*

**Las pantallas de Audit de 433 ya fueron reconstruidas el 28 de julio.** Ese rebuild es candidato a explicar
por que hoy faltan 30 entradas en la tabla de Screen Labels, y encaja con la advertencia de Santikos, donde
Build All Screens coincidio con datos del tenant que quedaron vacios. Es hipotesis, no esta probado.

Queda sin explicar por que Dayna veia las etiquetas resueltas el 11 de agosto, dos semanas despues de ese
rebuild. La cultura `en-GB` del bundle de la sesion de Juan sigue siendo la mejor explicacion de esa
diferencia.

## 5. Como queda el ticket

| | Que es | Evidencia | Estado |
|---|---|---|---|
| **A. Distrito 504** | Dayna no ve el 504. Sus tres tiendas estan en el 501. El 504 tiene 9 tiendas y ella figura como manager de una, la 948 Bremerton, sin tenerla asignada | Queries de `incident.Store` del 25 ago | No escalar todavia. Se cierra con el experimento de asignarle la 948, coordinado con Joe |
| **B. New Audit** | El StoreIdent no persiste, Next no dispara. Cualquiera lo reproduce | HAR del 25 ago y consola | Listo para Engineering |
| **C. Screen Labels** | 30 etiquetas sin resolver, bundle en `en-GB` | HTML de la pagina | Va con B, misma pantalla, posible misma causa |

## 6. Borrador de comentario interno

**El texto listo para pegar vive en `inbox/2026-08-25-rcs-28032-PEGAR-interno.md`.** Abrilo, Ctrl+A, Ctrl+C,
pegalo en Jira. Ese archivo no lleva prefijos de cita ni sangria, asi que el formato entra limpio. La copia de
abajo queda como respaldo de lectura.

Cubre el ciclo completo, del reporte original al estado de hoy. Cumple lo que Aimee exige: entorno, pasos de
reproduccion, lo que se descarto, las conversaciones con ingenieria que ocurrieron fuera del ticket, y que
necesitamos de Engineering.

> Client ID 433. Environment: Production, https://apps.apprissretail.com/vitaminshoppe/nettrack/, build 6.26.8.
> Full history and current state of this ticket.
>
> 1. ORIGINAL REPORT, RESOLVED
> Brandon Bigelow hit a Session Error on 29 July after a forced password change. The error cleared on its own
> within 24 hours. Joe Austin confirmed recovery on 31 July. Brandon's account is healthy. Close that thread.
>
> 2. SECOND PROBLEM, RAISED 31 JULY
> Joe reported that Dayna Rivera covers districts 501 and 504 and reaches only 504.
>
> 3. WHAT SUPPORT CHANGED, 4 AUGUST
> I added both districts to her profile through Control Panel Hierarchies. On 10 August Dayna reported the
> inverse result. She gained 501 and lost 504. That flip drove the working hypothesis that multi district
> assignment is not honoured.
>
> 4. RULED OUT WITH EVIDENCE, 4 TO 11 AUGUST
> Permission groups. She carries the same three groups as Journey Armstrong, Daniel Garza and Gisele Pohl.
> Account state. Locked, Disabled and Deleted all false, last sign in 10 August.
> Secure to Incident user mapping. All four users resolve to a valid active LPUser.
> Duplicate accounts from the platform update. No duplicate email addresses on the tenant.
> Feature flags EnableAdHocInitCaching and EnableAdHocPerRequestUserScope. Both True on this database.
> District master data, SupervisorFlag and SecurityID. None of them drives the behaviour.
>
> 5. DATA MODEL, VERIFIED WITH SQL 10 AUGUST
> structure.LocationHierarchyMaster defines four levels on this tenant: Company, Division, Region, District at
> level 4. All 884 rows in secure.LocationHierarchyUserAssignments are assigned by LocationId. Zero rows use
> the district, region or division columns. District scope is inherited from the assigned store.
>
> 6. ENGINEERING CONTACT OUTSIDE THE TICKET
> Kiran Vadday reviewed the analysis above on 10 and 11 August and asked for the exact page and URL where
> Dayna expects 501 and does not see it. Joe forwarded her screenshots to the ticket on 18 August.
>
> 7. NEW SQL EVIDENCE, 25 AUGUST. THIS CORRECTS ITEM 3
> incident.Store returns her three stores:
> StoreIdent 946, StoreNo 1016, Federal Way WA Store, Region 3, District 501, DistrictManagerID 10419
> StoreIdent 617, StoreNo 249, Tanasbourne OR Store, Region 3, District 501, DistrictManagerID 10419
> StoreIdent 466, StoreNo 500, Everett WA Store, Region 3, District 501, DistrictManagerID 10419
>
> My 10 August note on this ticket recorded store 249 in district 504. It returns 501 today. All three of her
> stores sit in 501. She sees 501 because every store she holds is in 501. She holds no store in 504.
>
> District 504 returns nine stores:
> 377 / 541 Puyallup WA, DM 49781
> 618 / 250 Redmond WA, DM 80288
> 700 / 313 Tukwila WA, DM 49781
> 764 / 393 Issaquah WA, DM 49781
> 895 / 589 Tacoma WA, DM 49781
> 938 / 1026 South Lake Union WA, DM 80288
> 948 / 1018 Bremerton WA, DM 10419
> 956 / 1023 Clackamas OR, DM 49781
> 1292 / 1033 Issaquah WA, DM 49781
>
> Store 948 carries DistrictManagerID 10419, the same value as her three stores. It sits in 504 and is absent
> from her LHUA scope. Confirm 10419 maps to her with SELECT UserID, FirstName, LastName, EmailAddr FROM
> incident.LPUser WHERE UserID = 10419.
>
> District 504 also carries three district managers across nine stores. 49781 on six, 80288 on two, 10419 on
> one. Flag that to the customer as master data to review.
>
> 8. NEXT STEP ON THE DISTRICT QUESTION. DO NOT ESCALATE THIS PART YET
> Assign store 948 to her in LHUA and observe the result. Three outcomes decide it. She gains both districts,
> which means she only lacked a store in 504 and no defect exists. She swaps 501 for 504, which proves multi
> district assignment is not honoured and sends this part to Engineering. Nothing changes, which invalidates
> the inheritance model in item 5. Coordinate the window with Joe first. A swap leaves her unable to work.
>
> 9. SEPARATE DEFECT. REPRODUCIBLE BY ANY USER. THIS IS WHAT NEEDS ENGINEERING
> New Audit cannot hold a selected location. I reproduced it with full admin scope, so permissions play no
> part. HAR attached.
>
> Steps to reproduce:
> a. Open /vitaminshoppe/nettrack/Audit/NewAudit.aspx.
> b. Type a store number into Select Location. The typeahead resolves. For 1016 the server returns StoreNo
> 1016, StoreName Federal Way WA Store, StoreIdent 946, City Federal Way, State WA, OpsRegion 3,
> OpsDistrict 501, Zip 98003, Inactive 0.
> c. Select the store. The browser posts the StoreIdent to fld_storeident$cpStoreLookupCallbackPanel as c0:946.
> d. The server returns hfStoreLookup re-rendered with value="". Every later postback still carries
> fld_storeident$fld_storeident 0, fld_storeident$fld_storeno 0, screentypecode 0 and clientid 0, while the
> combo displays 1016 - Federal Way WA Store, Federal Way, WA, 3.
> e. Click Next. No HTTP request leaves the browser. Console shows no exception. The button declares
> autoPostBack true, serverEvents Click, and routes through btnSave_Click. That function validates against the
> empty hidden and returns without rendering a message.
>
> The form never holds a location. That produces the "Please select a location and try again" message the
> customer reported on 11 August.
>
> Console output at load, neither triggered by the click:
> Permissions policy violation, unload is not allowed in this document, from DXR.axd.
> Bootstrap doesn't allow more than one instance per element, bound instance bs.tooltip, from data.js:26 with
> the stack cpf.ui.js:8944, popover.js, base-component.js, inside the jQuery ready handler. Check whether that
> exception cuts DevExpress control initialisation short.
>
> 10. SCREEN LABELS ON THE SAME PAGE
> The page renders 30 Screen Label fallbacks. The list includes the store lookup's own column headers:
> Store_StoreNo, Store_StoreName, Store_City, Store_State, Store_OpsRegion, Store_OpsDistrict, Store_Address1,
> Store_Zip, Store_Country. It also includes btn_Next, sys_PleaseFindStore, title_storelookup,
> title_SelectAuditName, title_AuditName, LPUser_Language and the mnu_ navigation entries. The store lookup
> runs with dxpDisplayColumns true and dxpValueField StoreIdent. Check whether it maps the value column by
> name. If it does, the missing labels break the mapping and explain item 9.
>
> The React bundle loads as allApps___v6.26.8_433en-GB. This tenant resolves culture as en-GB. Check whether
> the label rows exist for en-US only. Dayna's 11 August screenshots show these same labels resolving
> correctly, so the failure varies by session rather than by tenant.
>
> 11. RELATED TICKETS TO READ BEFORE PICKING THIS UP
> RCS-28005, same client. Audit screens for 433 were rebuilt on 28 July to clear a 404 on
> AuditSection_V268_S212.aspx. Matt Kamminga's note on the linked ENG asks to add validation confirming
> screens are rebuilt as part of the migration path. That rebuild is a candidate for the missing label rows.
> RCS-28321, Boot Barn. SystemSelect.aspx 500 with GetEncryptionKey Record missing in Options Table for slug
> /bootbarn, breaking the cohesion mode session handoff into Nettrack. Same exception class as RCS-27509 and
> ENG-6198. Kiran asked for reproduction steps there on 24 August. If the mechanism matches, one missing
> config value per slug explains both the labels and the lost StoreIdent here. Run a SELECT on the Options
> table for /vitaminshoppe to check.
>
> 12. WHAT WE NEED FROM ENGINEERING
> Confirm why the server returns hfStoreLookup empty after receiving a valid StoreIdent. Confirm whether the
> store lookup resolves its value column by label name. Confirm whether the missing Screen Label rows are a
> culture mismatch or a side effect of the 28 July screen rebuild.

## 7. Borrador de comentario al cliente

**Listo para pegar en `inbox/2026-08-25-rcs-28032-PEGAR-cliente.md`.** Va despues de mover el ticket. No pide
nada. Sin formato, texto plano.

> Hi Joe and Brandon,
>
> Thank you for sending Dayna's screenshots. They pointed us to the right place.
>
> We found a defect in the New Audit screen that blocks store selection, and it affects any user, not just
> Dayna. That part is now with our engineering team.
>
> We are still working on her District 504 access and will keep you posted here.
>
> Thank you.

## 8. Transicion

Codigo, por lo tanto Engineering. Transicion `231` "Waiting for Engineering", destino Under Engineering
Review, reasignar a **Shandana Khan**, el ENG se auto crea.

Antes de mover, adjuntar `HARVit1.har` al ticket. El procedimiento de Aimee exige entorno, pasos de
reproduccion con evidencia y las notas de troubleshooting dentro del ticket. Con el comentario interno de
arriba mas el HAR, se cumple.

Orden: adjuntar HAR, comentario interno, transicion, reasignar a Shandana, comentario al cliente.

## 9. Correcciones al cerebro, pendientes

`brain/memoria/reference_multidistrito_lhua.md` afirma que un usuario con dos distritos solo ve uno a la vez,
y usa este caso como confirmacion. Hoy no hay evidencia de que Dayna tenga dos distritos asignados, tiene tres
tiendas y las tres estan en el 501. La memoria queda sin respaldo hasta que corra el experimento de la tienda
948. No la borres todavia, marcala como en verificacion.

`brain/memoria/reference_jerarquia_ubicaciones_incident.md` dice que el distrito se hereda del StoreIdent
primario, verificado en cuatro usuarios el 10 de agosto. Esa parte del modelo no la toca la evidencia de hoy.
El ejemplo de Dayna que usa como prueba si queda invalidado.
