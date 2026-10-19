---
ticket: RCS-28612
cliente: Myer Australia, client 109, MYR, Secure 5, Snowflake ARDM_PRODUCTION.C109_MYR
prioridad: High, subio de Medium el 29 ago
estado_jira_verificado: Work in progress, 1 sep 2026
assignee_jira_verificado: Sebastian Garces, NO Juan Martinez
reporter: Christine Piacentini
creado: 2026-08-27T01:59:43-0400
ultimo_movimiento: 2026-08-29T01:09:50-0400
tipo: plan de ejecucion
relacionado: RCS-28638, RCS-25061, RCS-28518, RCS-28559, RCS-28536, RCS-28640
---

# RCS-28612, Delivery Fee ausente en transacciones de Point of Sale

## Lo primero, porque cambia quien ejecuta

El ticket no es tuyo. Assignee verificado en Jira vivo hoy: Sebastian Garces, tomo propiedad el
28 ago 14:58. Estado Work in progress. Bryant McAnnally subio la prioridad a High el 29 ago con
este comentario:

> This seems to be tied to several other issues related to the Showtime migration and needs to be
> immediately corrected for this customer. Please have someone review it as soon as possible.
> There are 5+ tickets in progress.

Nadie ha comentado desde el 29 ago. Van tres dias de silencio en un ticket High con un sponsor de
negocio encima.

Decide antes del paso 1. O te lo reasignas y ejecutas tu, o le entregas este plan a Garces y
supervisas. El plan sirve igual. Lo que no sirve es que los dos escriban en el ticket.

Nota de contexto: `inbox/2026-08-31-flag-roster-garces.md` deja abierta la verificacion de si
Garces pertenece a tu equipo Colombia. RCS-28612 esta en esa lista de siete tickets pendientes de
revision.

## Lo que reporta el cliente

Cita textual de la descripcion:

> The mapping of the delivery fee and delivery details are missing from transactions since
> 29/06/2026.
> Example: Transaction ID with correct mapping: 2606280085108544965
> Example where the delivery fee details are missing: 2608267428125472187 and 2608264200321847850

Dos comentarios mas del reporter el 27 ago:

> I think it is also affecting transactions where the delivery fee is tied to a wrap fee and
> Gift Registry

> I have created a search which can be saved in the validation folder

El search existe y esta guardado. Nombre exacto, visto en la captura del dialogo Open Search:
`RCS-28612_Mapping of Missing Delivery Fee from Point of Sale transactions`, tipo search, owner
Christine Piacentini, ruta `public > validation`, descripcion
`Delivery Fee details are empty, not including E-Comm Orders`, ultimo cambio 27/08/26 16:03:51.

## Que se verifico y contra que fuente

Jira vivo, getJiraIssue RCS-28612, RCS-28638 y RCS-25061, 1 sep 2026. Diez adjuntos del reporter,
guardados en `adjuntos/RCS-28612/` y descritos abajo. Cerebro completo, busqueda sobre
brain, flujos, investigaciones, tickets, inbox y bitacora.

## Los adjuntos, descritos

Los diez son del 27 ago 2026, todos de Christine Piacentini.

`image-20260827-053414.png`. Recibo Myer Group, Garden City, store 47, pos 123, trans 41,
26/08/2026 11:59:37 AM, team member Johanna, cashier 1221615. Cuatro lineas SUNGLASS HUT CONCESSION
ITEM, article 827829740, class group 1327. Una a 0.00 marcada C, una a -1 y 0.00 marcada V, una a
473.00, una a 473.00 con 40% OFF ITEM de -189.20 que deja 283.80. TOTAL 756.80. Mastercard 756.80.
Customer JAMES MORRIS. ITEMS SOLD 2, ITEMS RETURNED 0. **No hay linea DELIVERY FEE en el recibo.**

`image-20260827-053513.png`. Fila del search, transaction 2606280085108544965, store 204, cashier
1109207, 28/06/2026 6:00:34 PM, register 411, transaction 77, amount 3059.60, void False,
Item Receipt Description DELIVERY FEE, Amount Charged 75.00, Delivery Carrier OTHER, Delivery
Comments `DISPOSE 1 DOUBLE MATTRESS CAPITAL 02 8832 5181 9 JULY 2026`. **Este es el caso correcto.**

`image-20260827-054907.png`. Recibo Myer Group, Chatswood, store 204, pos 411, trans 77,
28/06/2026 6:00:34 PM, MYER one 6278041276926017. SEALY EXQUISITE MARRAKESH LUX PL MAT DB, article
157705960, 7649.00 con 60% off Sealy sel stores de -4589.40 y Bonus Delivery Sealy de -75.00, queda
2984.60. Linea propia **DELIVERY FEE, DeliveryFee 1, 75.00, Delivery Carrier OTHER.** TOTAL 3059.60.
Es el recibo del caso correcto.

`2608267428125472187-20260827-054700.jpg` y `image-20260827-055538.png`. Fila del search,
transaction 2608267428125472187, store 47, cashier 1221615, 26/08/2026 11:59:37 AM, register 123,
transaction 41, amount 756.80, Customer Full Name JAMES MORRIS, Keycode 827829740, Item Receipt
Description SUNGLASS HUT CONCESSION ITEM. **Delivery Carrier, Delivery Comments, Delivery Contact y
Delivery Free Reason salen vacias. No hay fila con Item Receipt Description DELIVERY FEE.**

`image-20260827-055554.png`. Recibo Myer Group, North Lakes, store 56, pos 207, trans 45,
26/08/2026 2:01:49 PM, MYER one 6278041053428518. VAN HEUSEN VTSB103Q_PNVB TAILORED PRINT, article
218683600, 79.95 con `$59 Van Heusen business shirts (4010...)` de -20.95, queda 59.00.
TOTAL 68.95. Mastercard 68.95. **No hay linea DELIVERY FEE en el recibo.**

`image-20260827-055643.png`. Fila del search, transaction 2608264200321847850, store 56, cashier
1080038, 26/08/2026 2:01:49 PM, register 207, transaction 45, amount 68.95, Customer Full Name
SHIRLEY-ANN CANTON, Keycode 218683600, Item Receipt Description VAN HEUSEN VTSB103Q_PNVB TAILORED
PRINT. **Columnas Delivery vacias.**

`image-20260827-055735.png`. Retail Transaction Details, store 56, Transaction ID
RT0562072608260045, register 056207, total 68.95, team member Suzanne 1080038, training mode N,
status Finished, begin 26/08/2026 13:58:48 GMT+10, end 14:01:49. Card 627804******8518. Linea
resaltada por el cliente en amarillo: `SALE / Delivery Carrier Type: AUSTRALIA POST /
Delivery Instructions: LEAVE AT FRONT DOOR IF NOONE HOME / DELIVERY FEE / 987654320 / $9.95 GST`.
Debajo la linea de mercancia VAN HEUSEN 218683600 $79.95 GST con promo -$20.95. Item Count 1.
Subtotal 68.95, GST 6.27, Grand Total 68.95, Paid Card 68.95, auth 21067, reference 480045056207,
tender entry Keyed.

`image-20260827-055538.png` par de arriba y `image-20260827-060716.png` no confundir.
`image-20260827-055538.png` es la fila del search de store 47. La Retail Transaction Details de
store 47 muestra Transaction ID RT0471232608260041, total 756.80, team member Johanna 1221615,
begin 26/08/2026 11:54:46 GMT+08, end 11:59:37. Linea resaltada:
`SALE / Delivery Carrier Type: AUSTRALIA POST / DELIVERY FEE / 987654320 / $0.00 GST`.
Debajo VOIDED SUNGLASS HUT -$0.00, SALE $473.00, SALE $473.00 con 40 % OFF ITEM BRAND PARTNER OFFER
-$189.20. Item Count 2. Subtotal 756.80.

`image-20260827-060716.png`. Fila del search, transaction 2606283871873023324, store 1, cashier
1149767, 28/06/2026 5:04:05 PM, register 501, transaction 120, amount 7.95, Item Receipt Description
DELIVERY FEE, Amount Charged 7.95, Delivery Carrier GIFT REGISTRY, Delivery Comments WRAP FEE,
Delivery Type WRAP ONLY. Es el adjunto del comentario sobre wrap fee y Gift Registry.

`image-20260827-061018.png`. Dialogo Open Search con el search guardado, ya descrito arriba.

## Hallazgo 1. El dato llega a Appriss y se pierde despues. Igual que RCS-28638

Las dos transacciones que el cliente declara rotas muestran la informacion de delivery completa en
Retail Transaction Details. Store 56: `Delivery Carrier Type: AUSTRALIA POST`, instrucciones de
entrega, `DELIVERY FEE`, article 987654320, $9.95. Store 47: mismo bloque, $0.00.

Las mismas dos transacciones salen sin ninguna columna de delivery en el search, y sin linea de
delivery en el recibo. El envio del cliente no es el problema. La perdida esta aguas abajo del
detalle de la transaccion.

## Hallazgo 2. Aritmetica que prueba el defecto. El cliente no lo escribio

Recibo de store 56, transaction 2608264200321847850:

    VAN HEUSEN                     79.95
    promo Van Heusen shirts       -20.95
    subtotal mercancia             59.00
    TOTAL impreso                  68.95
    diferencia                      9.95

Los 9.95 son exactamente el DELIVERY FEE que aparece en Retail Transaction Details. El monto esta
cobrado y esta dentro del total. La linea no esta impresa. El recibo no cuadra contra sus propias
lineas.

Ese es literalmente el sintoma con el que Christine abrio RCS-25061 en enero:

> As the Delivery Fee is missing the total transaction amount is not adding up correctly.

Usa la de store 56 como transaccion de ejemplo, no la de store 47. La de store 47 tiene delivery
fee $0.00, asi que 473.00 mas 283.80 da 756.80 y el total cuadra. Esa transaccion no demuestra
nada aritmeticamente y debilita el caso si la pones primero.

## Hallazgo 3. RCS-25061 no es un antecedente vago. Es el fix exacto que se perdio

La ficha del cerebro solo dice "Antecedente exacto de RCS-28612. Ya paso una vez y volvio". Jira
tiene el detalle completo y cambia el diagnostico.

RCS-25061, abierto por la misma Christine Piacentini el 18 ene 2026, mismo titulo de sintoma,
Delivery Fee Details Missing en Point of Sale, misma queja de que el total no cuadra. Lo trabajo
Mohammad Sheikh, hoy inactivo en Atlassian. El 21 ene publico la logica SQL vigente entonces:

    substring(replace(replace(coalesce(sale_description, return_description,
      cancelforlayaway_description, layaway_description, saleforpickup_description, null),
      '"',''),'|',''),1,60) as itemreceiptdescription

    where upper(COALESCE(tri_ct_tri_ntd_tri_applicationid, tri_at_tri_ntd_tri_applicationid,
                         tri_rt_tri_ntd_tri_applicationid, tri_tct_tri_ntd_tri_applicationid)) = 'ONLINE'
    OR LOWER(REPLACE(coalesce(cancelforlayaway_posidentity_positemid, layaway_posidentity_positemid,
             priceadjustmentforlayaway_posidentity_positemid, return_posidentity_positemid,
             saleforpickup_posidentity_positemid, sale_posidentity_positemid, ''), ' ', '')) != 'deliveryfee'

Esa condicion es el corazon del defecto. La linea de delivery fee solo se emite si la transaccion es
ONLINE, o si el positemid no es deliveryfee. Para una venta de tienda fisica con una linea
deliveryfee, ninguna de las dos se cumple y la linea no se emite. Por eso desaparece del search y
del recibo, y por eso el total no cuadra.

Christine lo corrigio en el ticket:

> our TLOGS have not changed since 2024. The delivery fee issue that we were experiencing was the
> discount calculations on Online Transactions. POS transactions were not affected.

Appriss cambio la logica, la probo en test, y el 4 feb 2026 Mohammad escribio:

> As per the latest update, the fix has been deployed in Production.

Resolucion registrada: `Support Data Team Resolved - Models Updated`. Christine valido el 5 feb:

> validation completed on the most recent transactions. Mapping looks correct.

Ese fix vive en el stack legacy. Myer paso de Greenplum legacy a SnowTime, go live ENG-6418 cerrado
el 17 ago 2026. La hipotesis es directa y es la misma clase que Matthew Everett ya probo en
RCS-28518 con `map_ardm_tender.sql:333`: el cambio de febrero de 2026 sobre la logica de
`itemreceiptdescription` no se porto a la reimplementacion dbt de SnowTime. Medela, no la afirmes.

## Hallazgo 4. La fecha de corte del cliente no esta probada, y aqui importa mas que en 28638

Christine declara 29/06/2026. Decodifica los IDs, el prefijo es AAMMDD:

    2606280085108544965    28/06/2026    correcto
    2606283871873023324    28/06/2026    correcto
    2608267428125472187    26/08/2026    roto
    2608264200321847850    26/08/2026    roto

Lo unico probado es que el 28/06 estaba bien y el 26/08 esta roto. Los cincuenta y nueve dias
intermedios estan sin medir. El 29/06 es la fecha del dia siguiente a su ultimo ejemplo bueno, no
una fecha observada. Es el mismo error de razonamiento que ya aparecio en RCS-28638 y que RCS-28640
contradijo con datos.

Y aqui hay una deduccion que sirve para separar mecanismos. Christine lee la transaccion del 28/06
hoy, en produccion, y sale poblada. Si el rewrite del 14 ago hubiera arrastrado tradingdays
historicos hasta junio, esa fila estaria en NULL ahora. No lo esta. Eso apunta a un hueco hacia
adelante y no a destruccion de datos historicos. RCS-28518 fue destruccion. Este parece no serlo.
La cross tab del paso 2 lo confirma o lo tumba en una consulta.

## Hallazgo 5. El adjunto de wrap fee y Gift Registry no prueba lo que el cliente cree

`image-20260827-060716.png`, la transaccion 2606283871873023324, es del 28/06/2026 y sale
**poblada**: Delivery Carrier GIFT REGISTRY, Delivery Comments WRAP FEE, Delivery Type WRAP ONLY,
7.95. Es anterior al corte que ella misma declara y esta correcta. El comentario dice "I think it
is also affecting", y el adjunto que soporta la afirmacion es un caso bueno.

Hay que pedirle una transaccion de wrap fee o Gift Registry posterior al corte. Sin eso, el alcance
del ticket cubre delivery fee unicamente.

Ojo con un detalle ya cerrado en RCS-25061, para no reabrirlo. En enero Christine pregunto si el
carrier deberia decir Wrap Fee en vez de Gift Registry, y Mohammad respondio con la evidencia:

> IN TLOG, we can see the "DELIVERY_CARRIER" as "GIFT REGISTRY"

El valor viene del TLOG del cliente. No es un defecto de mapeo.

## Hallazgo 6. Esta rota la emision de la fila, no solo el llenado de columnas

Diferencia importante contra RCS-28638, y es la razon tecnica por la que no son el mismo defecto.

En RCS-28638 la fila de la transaccion existe en el search y las columnas Proof Type, Order Number
y Financial Statement Date salen vacias. El registro esta, los campos no.

En RCS-28612 el caso correcto del 28/06 devuelve una fila cuyo Item Receipt Description es
`DELIVERY FEE` con Amount Charged 75.00. Los dos casos rotos del 26/08 no devuelven ninguna fila de
delivery fee. Devuelven la fila de mercancia con las columnas de delivery vacias. La linea de
delivery fee no se esta emitiendo.

Eso encaja exactamente con el predicado de RCS-25061, que decide si la linea se emite. No encaja
con un campo de extension que se quedo en NULL.

## Sobre relacionar RCS-28612 con RCS-28638

Relacionalos, con link `relates to`. No `duplicates`, no `is caused by`.

A favor de relacionar: mismo cliente 109 MYR, mismo reporter, misma sesion de validacion del 27 ago,
misma familia de migracion SnowTime, mismo sponsor presionando, y Bryant ya los trata como un solo
frente cuando escribe "5+ tickets in progress". Relacionarlos hace visible el patron de cuenta y
evita que dos ingenieros corran la misma cross tab dos veces.

En contra de fusionarlos: son defectos distintos con tablas distintas y con evidencia distinta.
28638 es Header Ext, campos en NULL sobre una fila que existe, sin antecedente documentado.
28612 es emision de linea de item, sin fila, con un fix previo identificado al detalle y con la
consulta SQL exacta en el historico. Las fechas de corte declaradas tampoco coinciden, 29/06 contra
09/08. Si los fusionas pierdes el hallazgo de RCS-25061, que es lo que le da ventaja a este ticket
sobre los otros cuatro de Myer.

Recomendacion concreta, cinco links:

    RCS-28612 relates to RCS-28638    misma cuenta, misma familia SnowTime
    RCS-28612 relates to RCS-25061    antecedente con el fix y el SQL exacto
    RCS-28612 relates to RCS-28518    mecanismo probado de omision de rama en el port
    RCS-28612 relates to RCS-28559    misma cuenta, mismo sponsor, mismo frente
    RCS-28612 relates to RCS-28536    misma cuenta, defecto de mapeo, ventana 15/07

---

# Paso a paso

Datos fijos para todos los pasos:

    Cliente                109, MYR, Myer Australia, Secure 5
    Schema SnowTime        ARDM_PRODUCTION.C109_MYR
    Repo                   dev.azure.com/apprissdevops/Sysrepublic Secure/_git/SnowTime
    Ruta de mapeo          dbt/clients/us/c109_myr/models/mapping/
    Pipeline               Deploy - SnowTime DBT / US - C109_MYR
    Go live SnowTime       17 ago 2026, ENG-6418. Validacion cutover ENG-3795
    Transaccion buena      2606280085108544965, store 204, 28/06/2026, delivery fee 75.00
    Transaccion mala A     2608264200321847850, store 56, RT0562072608260045, 26/08/2026,
                           delivery fee 9.95, usar esta, la aritmetica prueba el defecto
    Transaccion mala B     2608267428125472187, store 47, RT0471232608260041, 26/08/2026,
                           delivery fee 0.00, secundaria
    Article delivery fee   987654320
    Search del cliente     public > validation, RCS-28612_Mapping of Missing Delivery Fee from
                           Point of Sale transactions
    Fix perdido            RCS-25061, desplegado a produccion 4 feb 2026

## Paso 0. Resolver la propiedad del ticket. Hoy

Habla con Garces antes de tocar Jira. Dos salidas validas.

Si te lo quedas, reasignate el ticket y publica el paso 1. Si se lo dejas, pasale este archivo
completo y que el publique el paso 1 firmado por el. En ese caso tu papel es revisar la cross tab
del paso 3 antes de que salga cualquier conclusion al cliente.

No dejes pasar hoy sin decidir. Es High, tiene sponsor, y lleva tres dias sin movimiento.

## Paso 1. Romper el silencio

Texto listo para pegar en `inbox/2026-09-01-rcs-28612-respuesta-piacentini.md`. Cero peticiones.
Todo lo que el borrador anterior le pedia a Christine lo resuelves tu en los pasos 2 y 3. La fecha
de corte sale de la consulta. El filtro del search sale del boton Query. El caso de wrap fee sale
del mismo conteo por dia. Pedirselo a ella traslada trabajo y alarga el ticket.

No transiciones el ticket. Queda en Work in progress.

Deuda que crea ese comentario: publicar los hallazgos en RCS-28612. Sin fecha, anclado a tenerlos.

## Paso 2. Reproducir el search del cliente y sacarle el SQL

Leccion de RCS-27644 H&M, `brain/markdown/19-rcs-procesos-playbook.md:922-934`, call con Daniel
Endersby del 10 jul 2026:

> Cuando un ticket dice "mi report no muestra datos" sin mas info (muy comun), la palanca mas
> poderosa es obtener el SQL real que corre el report

En ese caso el SQL mostro que el filtro `ActionType NOT IN` descartaba el 94% de los headers,
porque SnowTime V2 dejo de emitir las filas sinteticas con ActionType 99 que pyARDM si emitia. Sin
el SQL la investigacion llevaba dias atascada en el filtro de fechas.

### Donde se abre eso, paso por paso

Esto es Secure, la aplicacion del cliente. No es Jira ni Snowflake. Ruta verificada por ti mismo el
31 ago en RCS-28581, `inbox/2026-08-31-rcs-28581-cwh-pos-number-regresion.md:226-232`:

    1. Entra a https://usprod.apprissretailcloud.com/control
       Tus roles ahi son SupportL2 y Engineers. brain/memoria/project_juan_accesos.md:13
    2. Tabla "Customers in USPROD". Busca Myer.
    3. Primera columna, "Click logo to sign in". Esa es la via de soporte.
       No uses /<slug>/signin, porque redirige al SSO de Myer donde tu usuario no existe.
       Alternativa non SAML: ?admin=true al final de la URL de signin.
    4. Ya dentro del tenant: All Apps, Secure Store, Explorer, Composer.
    5. Barra de Composer: Parameters, Columns & Filters, Query.
       El boton Query imprime el SQL generado.

Myer es australiano y corre en US. No lo busques en la region europea. El pipeline se llama
`Deploy - SnowTime DBT / US - C109_MYR` y el repo lo tiene bajo `us`, no bajo `au`.

### Como encuentras el search de Christine

El dialogo Open Search de tu captura `image-20260827-061018.png` muestra la ruta `public >
validation` con un breadcrumb y un filtro. Esa carpeta es del cliente. El cerebro no tiene una
definicion nuestra de "Validation Folder", solo el nombre tal como lo escribio Christine, asi que no
asumas que es una carpeta estandar del producto.

Si no das con el dialogo, usa el metodo de Daniel Endersby, `brain/markdown/19-rcs-procesos-playbook.md:941-946`:

    Make a search, cambiar area a repo/support, filtro display name contains delivery, Run.
    Devuelve coincidencias en searches privados, publicos y de sistema.

    Como leer el prefijo del file path:
      system...   search de sistema
      <GUID>...   search privado de un usuario
      public...   carpeta publica

El nombre exacto a buscar es `RCS-28612_Mapping of Missing Delivery Fee from Point of Sale
transactions`, owner Christine Piacentini.

### Corre, no edites

Abre el search, correlo con los parametros que traiga o con un rango dummy, y dale al boton Query.
Que devuelva cero filas no importa. Lo que quieres es el texto del SQL.

Gotcha de Composer, `inbox/2026-08-31-rcs-28618-analisis.md:352-358`: al abrir el search, Composer
materializa una copia efimera bajo `unsaved searches` en tu espacio de usuario. El que corre no es
el del path publico. Abrir, correr, leer, sin editar nada. No guardes.

### Que sacas del SQL

    que tabla o vista alimenta la columna Item Receipt Description
    que tabla alimenta Delivery Carrier, Delivery Comments, Delivery Contact, Delivery Type
    si hay un join y de que lado se pierde la fila de delivery fee
    como excluye E-Comm, porque ese filtro es la mitad del predicado de RCS-25061
    si el motor es Snowflake o Greenplum

Lo ultimo se lee por sintaxis. Composer rutea a uno o a otro segun el estado de migracion del
cliente, Confluence pageId 477571317762. En RCS-28618 la sintaxis `set var =` con `$var` confirmo
Snowflake, `inbox/2026-09-01-cosecha-rcs-28618.md:24`. Myer ya migro el 17 ago, asi que espera
Snowflake. Confirmalo igual.

El SQL tambien resuelve el nombre de la base, que es la trampa del paso 3. Tres nombres circulan en
la documentacion y no coinciden: `ARDMPROD.ARDM_<clientid>`,
`ARDM_PRODUCTION.<CLIENTID>_SNOWTIME` y `arp_production.c<###>_<clientname>`. No adivines.

Guarda el query en `adjuntos/RCS-28612/query-composer.sql`. Es la pieza que le entregas a quien
reciba la escalacion.

Orden que ahorra tiempo, de `inbox/2026-09-01-cosecha-rcs-28581.md:35`: corre Composer primero. El
boton Query resuelve motor y nombre de base de un tiro. No pidas acceso a nada hasta saber que
motor responde.

## Paso 3. La cross tab. Esta decide si es SnowTime o no

### Donde corres estas consultas

Dos caminos, los dos documentados y los dos tuyos.

Camino A, consola web. Para Myer es la cuenta **US**: `https://app.snowflake.com/okb13541/jn80103/`.
Auth por AzureAD. Entras con rol `PUBLIC`, que ya tiene lectura sobre ARDMPROD. Warehouse
`SUPPORTDATA_XS_WH`, X Small. Guia RTS, Confluence pageId 477651730444. Cita textual:

> Support access is strictly read only. No write or execute privileges are required.

Camino B, MCP desde Claude Code. Regla critica, `brain/markdown/20-snowtime-monitoring-migración.md:88`:
los MCP de Snowflake solo cargan si Claude Code arranca **desde** `C:\git\SnowTime`. Arrancar en
otro directorio y hacer cd dentro de la sesion no sirve. El MCP correcto para Myer es
`snowflake-us`, no `snowflake-eu`. Si `snowflake-eu` devuelve vacio para C109_MYR no es permisos,
es region equivocada. Role `SNOWTIME_ENGINEERING_ROLE`, warehouse `SNOWTIME_ENGINEERING_XS_WH`.

Usa siempre warehouse XS. Un XL corriendo un SELECT descuidado cuesta una fortuna.

Solo SELECT, SHOW y DESCRIBE. Nada de INSERT, UPDATE, DELETE, MERGE, CREATE ni DROP.

Si te falta un grant de rol, el contacto es Christopher Beck, tambien Daniel Endersby segun el
Quick Reference. `brain/markdown/20-snowtime-monitoring-migración.md:31`.

Las dos cuentas, para referencia. Myer va por la de arriba.

    US   OKB13541-JN80103   OKB13541-JN80103.snowflakecomputing.com
         consola  https://app.snowflake.com/okb13541/jn80103/
    EU   OKB13541-NEUAZ     OKB13541-NEUAZ.snowflakecomputing.com
         consola  https://app.snowflake.com/okb13541/neuaz/

La URL de consola EU no esta escrita en el cerebro. Se deriva del link de Streamlit EU,
`app.snowflake.com/streamlit/okb13541/neuaz/#/apps/az3znzw6tli65q5uxotf`, que trae el mismo par
`okb13541/neuaz`. Lo documentado literal es entrar a `https://app.snowflake.com/` y elegir JN80103
o NEUAZ. `brain/markdown/14-appriss-ingeniería-docs-fuente.md:4286-4294`,
`brain/markdown/20-snowtime-monitoring-migración.md:27`.

### Ubica la tabla y las columnas reales

El nombre de base sale del SQL del paso 2. Si el paso 2 no salio, no adivines. No asumas nombres de
columna tampoco.

    SHOW TABLES LIKE '%DELIVERY%' IN SCHEMA ARDM_PRODUCTION.C109_MYR;
    SHOW TABLES LIKE '%ITEM%' IN SCHEMA ARDM_PRODUCTION.C109_MYR;
    SHOW COLUMNS LIKE '%DELIVERY%' IN SCHEMA ARDM_PRODUCTION.C109_MYR;
    SHOW COLUMNS LIKE '%RECEIPTDESCRIPTION%' IN SCHEMA ARDM_PRODUCTION.C109_MYR;

`itemreceiptdescription` es el nombre que uso Mohammad en enero. Busca donde vive hoy. La familia de
tablas conocida del schema es ARDM_HEADER, ARDM_HEADER_EXT, ARDM_TENDER, ARDM_PAIDIN_PAIDOUT,
ARDM_PAIDIN_PAIDOUT_EXT, ARDM_GIFTCARD, REFERENCE_CARD.

Criterio de decision. Si no existe ninguna columna de delivery en el schema, el defecto es de
esquema y no de poblacion. Eso ya es el hallazgo y el paso 4 sobra.

Con los nombres reales, la cross tab. Fija el tradingday, varia el escritor. Sustituye
`<tabla>` y los nombres de columna por los del bloque anterior.

    SELECT
        DATE_TRUNC('month', tradingday)    AS tradingday_month,
        DATE_TRUNC('month', _ROW_CREATED)  AS writer_month,
        COUNT(*)                           AS rows_total,
        COUNT(deliverycarrier)             AS carrier_pop,
        COUNT(deliverycomments)            AS comments_pop,
        ROUND(100.0 * COUNT(deliverycarrier) / NULLIF(COUNT(*),0), 2) AS pct_carrier
    FROM ARDM_PRODUCTION.C109_MYR.<tabla>
    WHERE tradingday >= '2026-05-01'
    GROUP BY 1, 2
    ORDER BY 1, 2;

Como se lee.

Poblado cuando el escritor es el mismo mes, en cero cuando el escritor es agosto. Es el rewrite del
14 ago. Mismo dato de origen, distinto escritor, distinto resultado. Caso RCS-28518.

Cero desde el corte y sin fila previa poblada por un escritor de agosto. La rama no se
reimplemento en SnowTime. Caso RCS-28536. **Esta es la que predice el hallazgo 3.**

Poblado en todos los escritores y el cliente igual ve vacio. El dato esta y el problema es el render
o el search. Salta al paso 5.

Despues el conteo de lineas de delivery fee por dia, que es el test especifico de este ticket
porque aqui lo que falta es la fila entera:

    SELECT
        tradingday,
        COUNT(*) AS delivery_fee_lines
    FROM ARDM_PRODUCTION.C109_MYR.<tabla>
    WHERE tradingday BETWEEN '2026-06-01' AND '2026-08-31'
      AND UPPER(itemreceiptdescription) = 'DELIVERY FEE'
    GROUP BY 1
    ORDER BY 1;

El dia en que la cuenta cae a cero es la fecha de corte real. Esa cifra es la que va al comentario
interno y la que corrige o confirma el 29/06 del cliente. Si el corte cae el 13 o el 17 de agosto,
SnowTime es la causa y el 29/06 del cliente esta mal. Si cae el 29/06, SnowTime no explica nada y
hay que buscar un cambio de junio.

Y el test a nivel de fila, sobre las tres transacciones que ya tienes. Este es el que Christine
puede reconocer:

    SELECT transactionid, tradingday, _ROW_CREATED, itemreceiptdescription,
           deliverycarrier, deliverycomments, amountcharged
    FROM ARDM_PRODUCTION.C109_MYR.<tabla>
    WHERE transactionid IN ('2606280085108544965',
                            '2608264200321847850',
                            '2608267428125472187');

Solo SELECT. No corras ningun rebuild. Matthew lo dejo por escrito en RCS-28518:

> REBUILD CAUTION: do not run a repair rebuild before the mapping fix is deployed. A rebuild is
> what caused this damage, and rebuilding again with the current mapping would re-null anything
> still intact.

## Paso 4. Buscar el predicado de RCS-25061 en el codigo de SnowTime

Ahora sabes que buscar exactamente, que es la ventaja de este ticket sobre los otros cuatro de Myer.
Busca en `dbt/clients/us/c109_myr/models/mapping/` la cadena literal:

    deliveryfee
    itemreceiptdescription
    applicationid

Lo que tienes que responder es una sola pregunta. El predicado que decide si la linea de delivery
fee se emite, incluye la excepcion para transacciones que no son ONLINE, o quedo con la version de
enero de 2026.

El patron a reconocer es el de RCS-28518:

> map_ardm_tender.sql:333 emits null::VARCHAR as accountnumber. Legacy pyardm
> ARDM_1_Tender.sql:128-132 populated it via a four-branch CASE; SnowTime implements only branch 4

Aqui el equivalente seria un predicado que quedo en la forma
`applicationid = 'ONLINE' OR positemid != 'deliveryfee'` sin la correccion de febrero.

Revisa tambien `ArdmProdParity.md` y `models/ardm_mapping.md` por los campos de delivery. Matthew
encontro su columna marcada BLOCKED con 19.68% de match en la linea 748. Advertencia suya: ese
reporte tiene entradas obsoletas en las dos direcciones, un BLOCKED no es prueba por si solo,
confirmalo contra el paso 3.

Si no tienes lectura en Azure DevOps, no pidas permisos por este ticket. Pidele el grep a Matthew
Everett, que ya tiene cuatro tickets de Myer y el contexto entero. Azure DevOps es de solo lectura,
nada de comentar, aprobar ni mergear.

## Paso 5. Revisar el render del recibo

Independiente del paso 4, porque el recibo y el search son dos consumidores distintos.

El recibo de store 56 imprime un total que incluye 9.95 de delivery fee y no imprime la linea. Si el
paso 3 devuelve la fila poblada en la tabla, el defecto es de plantilla y no de mapeo. Los overrides
de mapeo por cliente viven en `secure_Resource.json`, referencia en
`brain/markdown/16-rcs-soluciones.md:186`. El cerebro no tiene la ruta en disco de ese archivo, hay
que preguntarla.

Referencia de plantilla de recibo en el repo, del trabajo de RCS-28638: `detail-panel.html`,
lineas 130-137 y 303-305.

## Paso 6. Escribir el comentario interno y escalar

El comentario interno no se escribe todavia. Hoy no tienes entorno reproducido, ni pasos de
reproduccion propios, ni una sola cifra contra produccion. Los cuatro requisitos de Aimee no se
cumplen y el ticket rebota. Ese es el error que devolvio cuatro tickets de Vedant Shirude el 13 ago.

Cuando el paso 3 devuelva numeros, escribelo a
`inbox/AAAA-MM-DD-rcs-28612-comentario-interno.md`, con la estructura que ya funciono en RCS-28618:

    # INTERNAL NOTE. NOT FOR CUSTOMER
    1. Correction
    2. Environment and steps to reproduce
    3. Findings
    4. Troubleshooting performed, and the limits of support access
    5. Ruled out. Do not repeat
    6. Still open
    Related
    Routing

Las secciones 2 y 4 no se quitan nunca. Los pasos de reproduccion van numerados, con Expected y
Actual, nombrando el adjunto y su fecha. Client ID 109 en el comentario, siempre. Declara el uso de
IA y aclara que cada cifra sale de una consulta contra produccion, no del modelo.

Lo que ya tienes listo para la seccion 1, Correction: el ticket no menciona RCS-25061 y Bryant lo
enmarco entero como Showtime. Existe un fix previo del mismo sintoma, desplegado a produccion el 4
feb 2026 con resolucion `Support Data Team Resolved - Models Updated`. Eso cambia la pregunta que
tiene que responder ingenieria.

Lo que ya tienes listo para la seccion 5, Ruled out: el carrier GIFT REGISTRY no es defecto de
mapeo, viene del TLOG del cliente, probado por Mohammad Sheikh en RCS-25061 el 29 ene 2026.

Ruteo. Aqui hay una bifurcacion real y depende del paso 4.

Si el paso 4 encuentra que el predicado quedo mal portado en dbt, es codigo y va a Engineering, y en
la practica va consolidado con la familia Myer de Matthew Everett, no como ticket suelto. Regla de
frontera del cerebro: codigo o bug a Engineering, dato o configuracion ya en produccion a Delivery.

Si el paso 4 encuentra que el mapeo es configuracion de cliente en `secure_Resource.json`, va a
Delivery, y los campos son estos:

    Team Ownership     Support (Delivery dep.)
    Sprint             RCS Support Team
    Status             Under Delivery Review
    Assignee           Peyman Motlagh, el reasigna
    Label              Support_Data_Team
    Tipo               Incident
    Campo Problem      Data, no Other

Antes de mover, verifica que el ticket lleve entorno, pasos de reproduccion con capturas, las notas
de troubleshooting y cualquier conversacion que ocurrio fuera del ticket. Aimee bloqueo cuatro
tickets de Vedant Shirude el 13 ago por no tenerlas. Y avisa al cliente que el ticket se mueve.

Riesgo conocido del handoff, `asignaciones/2026-08-28.md:223-225`: mover el estado sin poner
assignee deja el ticket huerfano en la cola unassigned.

## Paso 7. Cerrar en el cerebro

    bin/anotar RCS-28612 "lo que se hizo"
    cat inbox/2026-09-01-rcs-28612-delivery-fee-pos.md | bin/guardar 16 "RCS-28612 Delivery Fee POS Myer, fix de RCS-25061 perdido en el port a SnowTime"
    python3 bin/indexar_tickets.py

---

## Lo que no esta probado y no debe afirmarse

La perdida del fix de RCS-25061 en el port a SnowTime es hipotesis. Tiene el mecanismo probado en
otra columna, RCS-28518, y tiene el SQL exacto del fix original. No tiene todavia una linea de
codigo de SnowTime que lo confirme. Eso lo entrega el paso 4.

La fecha de corte real no se conoce. 29/06 es la declaracion del cliente y esta sin respaldo. La
consulta del paso 3 la fija.

El alcance sobre wrap fee y Gift Registry no esta demostrado. El unico adjunto que lo sustenta es un
caso correcto anterior al corte.

## Limpieza pendiente

`adjuntos/RCS-28612/` quedo con diez archivos duplicados con prefijo de UUID truncado. El sandbox no
los pudo borrar. Los diez con nombre limpio son los buenos. Borra los que empiezan por cuatro
caracteres y guion.
