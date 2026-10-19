# RCS-28032 · Vitamin Shoppe · evidencia de Dayna y escalacion a Engineering

> **SUSPENDIDO el 24 ago por la tarde.** Juan reprodujo en su propia sesion y encontro dos cosas que este
> documento no contempla: la tienda 1016 si resuelve para el, "1016 - Federal Way WA Store, Federal Way, WA, 3",
> y las dos pantallas salen con la tabla de Screen Labels sin resolver. La transicion a Under Engineering
> Review queda frenada. El analisis de LHUA y el borrador interno siguen validos.
> Ver `inbox/2026-08-24-rcs-28032-screen-labels-y-repro-juan.md`.

Fecha: 2026-08-24
Ticket: https://trebuco.atlassian.net/browse/RCS-28032
Client ID: 433
Estado en Jira al momento de escribir: **Work in progress**, assignee Juan Martinez, prioridad Medium,
labels FromEmail, L1, Uni_Jul_26_WAFAccess.
Ultimo movimiento: comentario de Joe Austin del 18 ago con las capturas adjuntas. Seis dias sin respuesta nuestra.

## Que se verifico y contra que fuente

| Que | Fuente |
|---|---|
| Estado, assignee, labels y los 30 comentarios | `getJiraIssue` RCS-28032, lectura del 24 ago |
| Correo de Dayna del 11 ago y sus cinco capturas | `adjuntos/RCS-28032/Re__D501_LPMS.eml`, parseado y descrito en `adjuntos/RCS-28032/LEEME.md` |
| Modelo de datos de jerarquia de ubicaciones en el tenant 433 | `brain/memoria/reference_jerarquia_ubicaciones_incident.md`, SQL corrido el 10 ago |
| Comportamiento observable del multidistrito | `brain/memoria/reference_multidistrito_lhua.md` |
| Procedimiento de escalacion y transiciones disponibles | `brain/memoria/reference_escalacion_l3_procedimiento.md` y `getTransitionsForJiraIssue` |

No se escribio nada en Jira. Juan pega.

## Lo que aporta la evidencia nueva

Las capturas del 11 ago a las 9:15 AM PST cierran el pedido que quedo abierto el 10 y el 11 de agosto.
Entorno: Produccion, `https://apps.apprissretail.com/vitaminshoppe/nettrack/`.

Pasos de reproduccion, tal como los documenta la usuaria:

1. Entrar a `/vitaminshoppe/nettrack/Audit/NewAudit.aspx`. La tarjeta Select Location aparece vacia y pide
   escribir un numero de tienda. Antes del update esta pantalla presentaba los dos distritos y permitia
   elegir uno antes de pedir la tienda.
2. Escribir el numero de tienda 1016, que la usuaria identifica como tienda de District 504. El numero no
   resuelve a una ubicacion.
3. Seleccionar Audit Class "District Manager SVS" y Audit Name "Customer Experience Summary", pulsar Next.
   La pagina devuelve "Please select a location and try again."
4. Entrar a `/vitaminshoppe/nettrack/Audit/AuditLog.aspx`. El alcance efectivo que muestra la pagina es
   Division "The Vitamin Shoppe", Ops Region "3", Ops District "501". District 504 no aparece.
5. La usuaria reporta ademas que dejo de recibir alertas de todo lo de D504, auditorias e incident reports.

Dos cosas nuevas que no estaban en el ticket:

- **Declaracion de regresion.** Dayna dice, textual: *"Previously before the last update, on this screen it
  would show the two districts and allow me to choose one before it asked me to pick a store."* Es la primera
  vez que alguien situa el comportamiento anterior. Interpretacion, no hecho verificado por nosotros: el paso
  de seleccion de distrito existia antes del update y ya no esta.
- **Alcance visible desde la propia UI.** AuditLog.aspx imprime Ops District 501 como alcance efectivo. Ya no
  depende solo de leer LHUA, la aplicacion lo muestra.

Esto confirma desde el lado de la aplicacion lo que ya estaba confirmado desde el lado de la asignacion el
11 de agosto: la asignacion multiple de distrito no se honra, y agregar la segunda fila en LHUA solo cambia
cual de los dos distritos toma efecto.

## Lo que ya esta descartado, para no repetirlo

Grupos de permisos, estado de cuenta, mapeo Secure a Incident, cuentas duplicadas de la unificacion, los
flags `EnableAdHocInitCaching` y `EnableAdHocPerRequestUserScope`, datos maestros de distrito, `SupervisorFlag`
y `SecurityID`. Detalle en `reference_jerarquia_ubicaciones_incident.md`.

## Pendiente de verificar antes de afirmarlo

- La tienda 1016 no figura en los datos que se levantaron el 10 ago. Las tiendas conocidas de Dayna son el
  StoreIdent 617, tienda 249 Tanasbourne OR, distrito 504, y el StoreIdent 466, tienda 500 Everett WA,
  distrito 501. Confirmar en `incident.Store` a que distrito pertenece la tienda 1016 antes de usarla como
  ejemplo ante ingenieria.
- Si quitar la segunda fila de LHUA devuelve el distrito original. No se probo. De ahi depende que se pueda
  ofrecer un workaround de "cual de los dos quiere activo".
- El label del ticket es `Uni_Jul_26_WAFAccess`. El playbook lo clasifica en `Uni_Jul_26_SSOMapping` por el
  sintoma original de Brandon. Ninguno de los dos describe el tema abierto hoy, que es alcance de ubicacion.
  Revisar con J.R. si corresponde reetiquetar.

## Borrador de comentario interno

> Client ID 433.
>
> Dayna Rivera sent the screens on 11 Aug at 9:15 AM PST. Joe forwarded them to the ticket on 18 Aug. They
> close the request that was open since 10 Aug.
>
> Environment: Production, https://apps.apprissretail.com/vitaminshoppe/nettrack/
>
> Steps to reproduce, as documented by the user:
> 1. Open /vitaminshoppe/nettrack/Audit/NewAudit.aspx. Select Location is empty and asks for a store number.
> 2. Enter store number 1016, a District 504 store. The store number does not resolve to a location.
> 3. Select Audit Class District Manager SVS and Audit Name Customer Experience Summary, then Next. The page
>    returns "Please select a location and try again."
> 4. Open /vitaminshoppe/nettrack/Audit/AuditLog.aspx. The effective scope printed on the filter page is
>    Division The Vitamin Shoppe, Ops Region 3, Ops District 501. District 504 is absent.
> 5. The user also stopped receiving alerts for District 504, both audits and incident reports.
>
> User statement on the prior behavior, verbatim: "Previously before the last update, on this screen it would
> show the two districts and allow me to choose one before it asked me to pick a store." Reading this as a
> regression introduced by the update. We have not verified the pre update behavior ourselves.
>
> This matches what the assignment side already showed on 11 Aug. Both districts 501 and 504 were added to her
> profile on 4 Aug. Before that she saw only 504. After that she sees only 501. Same user, same profile, the
> visible district changed when the second row was added. Multi district assignment is not honored.
>
> Data model, verified with SQL on tenant 433 on 10 Aug: all 884 rows in secure.LocationHierarchyUserAssignments
> are assigned by LocationId. Zero use the district, region or division columns. District scope is inherited
> from the primary StoreIdent, not assigned. Confirmed across four users. Adding a second LHUA row from Control
> Panel grants the store, not the district.
>
> Already ruled out with evidence: permission groups, account state, Secure to Incident user mapping, duplicate
> accounts from the platform update, EnableAdHocInitCaching and EnableAdHocPerRequestUserScope, district master
> data, SupervisorFlag and SecurityID.
>
> Kiran reviewed the assignment side analysis on 10 and 11 Aug and asked for the exact page and URL. That is
> now supplied above.
>
> This cannot be corrected from Support. Moving to Engineering.
>
> The original report on this ticket, Brandon Bigelow's Session Error of 29 Jul, resolved on its own after 24
> hours and his account is healthy. The open item is the location scope only.

## Borrador de comentario al cliente

Va despues de mover el ticket, no antes. El procedimiento de escalacion exige avisarle al cliente que el
ticket se esta moviendo.

> Hi Joe and Brandon,
>
> Thank you for sending Dayna's screenshots. They gave us what we needed.
>
> We have confirmed the behavior on our side. Her account cannot be corrected from the configuration side, so
> we are moving this ticket to our engineering team for a permanent fix.
>
> Dayna currently has District 501. I will let you know as soon as engineering comes back with the fix and the
> release it lands in.
>
> Thank you.

Si Juan verifica primero que se puede alternar el distrito activo, se le puede agregar esta linea antes del
cierre, y solo entonces:

> If she needs District 504 instead while we work on this, let me know and we can switch which one is active.

## Transicion sugerida

Es un bug de codigo, por lo tanto Engineering. Del procedimiento de Aimee: destino Secure / Incident
Engineering, estado **Under Engineering Review**, se reasigna a **Shandana Khan**, el ENG se auto crea con la
transicion y los comentarios sincronizan en ambos sentidos.

Transicion disponible en el ticket: id `231`, nombre "Waiting for Engineering", destino Under Engineering Review.

Orden: comentario interno, transicion, reasignar a Shandana, comentario al cliente.

## Aparte

RCS-28054, Genuine Parts Co., es el mismo sintoma de alcance de ubicacion despues de un cambio de
configuracion. Si el ENG confirma la causa, vale linkearlos.
