# RCS-28032 · lo que muestra la sesion de Juan del 24 ago · frena la transicion

> **RESUELTO por el HAR del 25 ago 00:36 UTC.** La tienda 1016 es OpsDistrict **501**, StoreIdent 946, dato
> devuelto por la propia aplicacion. La pregunta del hallazgo 1 queda contestada y el SELECT ya no decide
> nada. El hallazgo 2 tiene ahora un mecanismo medido: el StoreIdent no se persiste en el formulario y el
> clic en Next no genera request. Ver `inbox/2026-08-24-rcs-28032-har-newaudit-causa.md`.

Fecha: 2026-08-24, 7:35 y 7:37 PM
Fuente: dos capturas de la sesion propia de Juan en `apps.apprissretail.com/vitaminshoppe/nettrack/`,
pestanas NewAudit.aspx y AuditLog.aspx. Juan entra con menu Admin visible, o sea alcance completo.

Esto cambia el plan del entregable anterior. **No mover el ticket a Under Engineering Review todavia.**

## Hallazgo 1. La tienda 1016 si resuelve, y eso cuestiona la evidencia de Dayna

En la sesion de Juan el campo Select Location devuelve:

    1016 -  Federal Way WA Store,  Federal Way,  WA,  3

La tienda existe, resuelve, y el ultimo campo del string es 3, que coincide con el Ops Region 3 que
mostraba la pantalla de Dayna.

Dayna escribio: *"If I choose a store in D504, it won't load the location number"*, y la captura que
adjunto para probarlo es justamente la de la tienda 1016.

Federal Way queda en Washington. Las tiendas conocidas de Dayna son la 249 Tanasbourne OR en el distrito
504 y la 500 Everett WA en el distrito 501. El patron de los datos que ya se levantaron pone Oregon en 504
y Washington en 501.

**Si 1016 pertenece al distrito 501, la captura no prueba lo que Dayna dice que prueba.** Estaria fallando
una tienda dentro del distrito que ella si tiene activo, y la explicacion de alcance de distrito no cubre
ese caso. Si 1016 pertenece al 504, la evidencia queda en pie y ademas se explica el contraste: no resuelve
para ella porque esta fuera de su alcance, si resuelve para Juan porque Juan ve todo.

Esta consulta decide si la escalacion se sostiene:

    SELECT StoreIdent, StoreNo, Region, District, DistrictManagerID
    FROM incident.Store
    WHERE StoreNo IN (1016, 249, 500);

Solo SELECT. Correrla antes de cualquier transicion.

## Hallazgo 2. La tabla de Screen Labels no resuelve en la sesion de Juan

Las dos pantallas salen plagadas de literales de fallback. Claves que faltan, tal cual aparecen:

NewAudit.aspx: `mnu_BackToMenu`, `mnu_UserTools`, `sys_PleaseFindStore`, `title_SelectAuditName`,
`title_AuditName`, `btn_Next`.

AuditLog.aspx: `mnu_BackToMenu`, `mnu_UserTools`, `mnu_BulkReassign`, `sys_DateRange`, `sys_To`,
`sys_ClickFindToSearchGeneric` (dos veces), `sys_PleaseFindStore`, `btn_Search`.

**El dato que importa: el 11 de agosto esas mismas etiquetas se veian bien.** En las capturas de Dayna
aparecen resueltas como "Back to Menu", "User Tools", "STEP 1: Please click in the field above...",
"Select Audit Name", "Audit Name", "Next", "Date Range:", "To", "Click Find button to Search" y "Search".
El 24 de agosto, en la misma URL y el mismo tenant, ninguna resuelve.

Entre esas dos fechas hay al menos un despliegue conocido, el release de la manana del 13 de agosto.

No resuelven las etiquetas y tampoco funciona el boton. Juan reporta que Next no hace nada con la ubicacion
ya cargada. Para Dayna el 11 de agosto ese mismo boton si respondia, devolvia "Please select a location and
try again". Son dos comportamientos distintos del mismo control.

## Como se relacionan los dos hallazgos

Interpretacion, no hecho establecido. Son dos fallas distintas que conviven en la misma pantalla. La de
Dayna es alcance de ubicacion. La de Juan es render y comportamiento del formulario. Nada de lo que hay
hoy permite decir que una causa la otra.

Lo que si cambia: Juan acaba de reproducir en su propia sesion una falla funcional en NewAudit.aspx que
no depende del distrito. Eso hay que separarlo y documentarlo antes de escalar, porque si el ticket entra
a Engineering describiendo solo el problema de distrito, la pantalla rota se pierde.

## Que hay escrito en el cerebro sobre screen labels

| Que | Donde | Aplica |
|---|---|---|
| `GetScreenLabelByFormField` hace cientos de llamadas a base por recurso, sin cache. PR `55972` de Chris Rippingale, estaba en PR en USDEV al 12 ago | `brain/memoria/project_teams_unificacion_2026_08_12.md` | Es el mecanismo que resuelve estas mismas etiquetas. Candidato, no confirmado como causa de ningun ticket |
| "Changed screen labels that do not show up need a label cache reset" | `brain/markdown/21-kt-kristin-sign-off-procesos-rts.md`, KT de Kristin | Ojo, ese punto esta en la seccion de APIS. No esta verificado que el mismo reset exista en nettrack |
| Screen Designer con `?ADMIN=9QQP` y "Build All Screens" | `brain/memoria/reference_screen_designer_rebuild.md` | Es para pantallas que no cargan o dan 404, no para entradas faltantes de la tabla de labels. Y trae advertencia: en Santikos, RCS-28022, los Incident Types del tenant quedaron en cero despues de correrlo |

**No ejecutar Build All Screens en 433 para probar suerte.** No esta establecido que repare la tabla de
Screen Labels, y el antecedente de Santikos es un tenant con datos perdidos.

## Verificaciones antes de tocar nada, en orden

1. **A quien le pasa.** Abrir NewAudit.aspx en una ventana de incognito o con otro usuario del tenant. Si
   las etiquetas resuelven, es de la sesion o del perfil de Juan y no del tenant.
2. **Alcance.** Navegar a otra pantalla de nettrack en 433 que no sea del modulo Audit. Si tambien salen
   los fallback, es global del tenant. Si no, es del modulo.
3. **Otro tenant.** Abrir la misma pantalla Audit en otro cliente. Si se ve bien, apunta al tenant 433.
4. **Por que Next no hace nada.** F12, pestana Console por error de JavaScript, y pestana Network por el
   postback al pulsar Next. Estado HTTP y respuesta. Sin esto no se puede afirmar si el boton no dispara o
   si dispara y el servidor rechaza.
5. **La tabla.** SELECT sobre la tabla de screen labels del tenant buscando las claves listadas arriba.
   Establece si las filas no existen o si existen y no se estan leyendo. Son dos problemas distintos con
   arreglos distintos. El nombre exacto de la tabla no esta documentado en el cerebro, hay que ubicarlo.
6. **La tienda 1016.** El SELECT del hallazgo 1.
7. **Si hubo release.** Confirmar que se desplego en 433 entre el 11 y el 24 de agosto.

## Que se le dice al cliente hoy

Nada todavia. El borrador de cliente del entregable anterior decia que confirmamos el comportamiento y que
movemos a ingenieria. Con la tienda 1016 sin verificar, esa afirmacion no se sostiene. Joe volvio de PTO el
17 de agosto y lleva seis dias esperando, asi que si hace falta acusar recibo, va sin conclusiones:

> Hi Joe and Brandon,
>
> Thank you for sending Dayna's screenshots. We are working through them now and I have a few checks
> running on our side. I will come back to you here with something concrete shortly.
>
> Thank you.

## Estado del entregable anterior

`inbox/2026-08-24-rcs-28032-evidencia-dayna-y-escalacion.md` queda en pie para el analisis de LHUA y para
el borrador interno. Su seccion de transicion queda suspendida hasta que cierren los puntos 1 y 6.
