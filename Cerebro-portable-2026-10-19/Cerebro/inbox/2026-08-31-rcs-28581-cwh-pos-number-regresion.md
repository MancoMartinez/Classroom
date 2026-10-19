# RCS-28581 · CWH · POS Number regreso al mapeo anterior

Fecha: 2026-08-31. Cliente: Chemist Warehouse, CWH, cliente 248. Reporter: James McKenna.
Producto: Secure 5 Core EBR. Feed ARDM por API en tiempo real, storage prddatastoreneu,
carpetas c248_rawdata_*.

## Estado verificado en Jira, no en la ficha

Consultado el 2026-08-31 con getJiraIssue.

Status: Under Support Review.
Assignee: Juan Martinez.
Priority: Medium.
Creado: 2026-08-25 19:03 -0400. Actualizado: 2026-08-27 15:36 -0400.
Labels: ninguno. Issuelinks: ninguno. Sin ENG enlazado.
Comentarios: 5. El ultimo es el ownership de Juan del 2026-08-27.

Deuda: Juan prometio un update el 2026-08-27 y no lo entrego. Van 4 dias.

## Lo que dice el cliente, verbatim

Descripcion, 2026-08-25:
"The POS number for the reciepts has regressed and no longer displays the till number. Our tills
generally are TILL02, TILL03 or DISPENSE01 or the like. Until this week that was what was
displaying. It has revered back to a number that is not relevant to the users. Can we please remap
back to the second screenshot? First screenshot shows current issue"

Comentario 2026-08-26 18:17:
"Hi team, it appears the till number has reverted or you have completed a fix? Now working as
expected and ticket can be closed"

Comentario 2026-08-26 19:25, se retracta:
"Hi team please disregard last comment. I have found the issue in other transaction outside what I
had tested. Appears it may be in a data period, I will update when I know more"

## Evidencia de los adjuntos

Guardados en adjuntos/RCS-28581/ con descripcion textual en DESCRIPCION.md.

Captura 1, comportamiento actual, el defecto:
Store 036, Chemist Warehouse Coburg Market, Coburg, Victoria. Pos 863485. Cashier 37463 Meysam
Noorifar. Order No 5739233443017590. RETAIL SALE.

Captura 2, comportamiento esperado:
Store 803, Chemist Warehouse Sydney Park Street, Sydney, NSW. Pos TILLD04. Cashier 114493 Tasmia
Ahmed. Order No 12789024214068481. RETAIL SALE.

Limite duro de esta evidencia. Las dos capturas son de tiendas distintas, 036 contra 803, y no
traen fecha de transaccion visible. El cliente afirma que el corte parece ser por periodo de datos.
La evidencia entregada no separa discriminador por fecha de discriminador por tienda. Resolver eso
es el primer paso, no una nota al pie.

## Historia del mapeo. Aqui esta el hallazgo

DO-9495, "CW - UAT - Wrong POS number for transactions". Closed, Resolved el 2026-04-29 18:11 -0400.
Reporter Slade Jordan. Assignee final Daniel Ortquist. Padre DO-4921. Label clientproject.

Tomasz Sutkowski diagnostico la causa, verbatim:
"The value '71' is taken from ardm_event_vw.pos_number, while I can see requested 'TILL11' is
available in ardm_header_vw.machine name."

Bartosz Bereski confirmo el fix, verbatim:
"Since the fix is already implemented in the production code, the POS number will now be correctly
retrieved from the machine name."

Bartosz recargo a mano el archivo c248_rawdata_postransactions/2026/02/17/17/data_6_5_0.json.gz para
materializar el fix.

DO-7534, "CWH 248 - QA - Secure POS NO and Ticket No", Waiting on 3rd Party, creado 2025-10-15. Es
el requisito de negocio original. Slade Jordan sobre por que el valor tiene que ser alfanumerico:
"if we have to use the number only we may not have uniqueness needed to determine till01 from
dispense01."

## Dos senales del changelog de DO-9495 que cambian la lectura

Primera. El ticket toco el estado "Reload Required" el 2026-03-06 y Tomasz comento "Should be
resolved after reload". Cerro el 2026-04-29 con fixVersions vacio. Un cierre sin fixVersion y con
recarga manual de un archivo puntual admite la lectura de que la correccion nunca quedo persistida
en el modelo del pipeline. Si el mapeo a machine_name vive solo en el resultado de esa recarga y no
en map_ardm_header.sql, las transacciones nuevas resuelven pos_number otra vez. Eso encaja con el
"data period" que reporto el cliente.

Segunda. DO-9495 aparece con updated 2026-08-19, dentro de la ventana del incidente. El changelog
descarta que sea trabajo tecnico. La unica entrada de ese dia es Austin Flannery agregando el label
clientproject, verbatim del JSON: field labels, fromString "", toString "clientproject". No hubo
reapertura, ni cambio de estado, ni comentario, ni adjunto. Es un bulk edit administrativo. No lo
uses como pista.

## Como se puebla el campo, segun Confluence

"v2 / Rules / dbt-mapping.md", ARPDT, pageId 477834641411:
"get_transaction_id() computation, 19-digit INT PK from (storeno, posno, ticketno,
endtransdatetime)."
"Mapping owns column rename + cast + seed lookup. Nothing else."

"How SnowTime Turns Raw Files into the Production Database", PD, pageId 477966893068:
"Mapping, rename, cast, look up codes, and filter (map_*). This is the heart of turning source
columns into ARDM columns."

Traduccion operativa. posno es columna estandar ARDM. Sale de un rename directo desde la capa flat.
Se configura en models/flat/flat_*.sql y models/mapping/map_ardm_header.sql del repo dbt del
cliente, en Azure DevOps. No hay UI. El cambio va por PR.

Riesgo que hay que declarar antes de proponer cualquier correccion. posno entra en
get_transaction_id(). Cambiar el mapeo de posno cambia el transactionid de 19 digitos de las
transacciones nuevas. Un remapeo de POS number no es cosmetico.

Precedente del tenant australiano hermano, "Customer Profile: Myer", RTS, pageId 477951524865:
"Changes are usually applied going-forward only. Fixes take effect from a stated tradingday onward,
and historical reloads are a separate request."

No existe perfil de Confluence para CWH. La plantilla es pageId 477951262722.

## Hipotesis, sin confirmar

H1, la fuerte. El mapeo a machine_name nunca quedo en el modelo dbt. Vivio en el resultado de la
recarga manual de febrero. Las transacciones nuevas volvieron a pos_number. Predice corte por
fecha, no por tienda.

H2. El mapeo esta en el modelo y se aplico going-forward desde un tradingday, y hay tiendas o tipos
de till que machine_name no resuelve. Predice corte por tienda o por tipo de till, no por fecha.

H3, debil. Una migracion de cliente 248 fallida dejo el mapeo en estado anterior. ENG-7413,
"US - Automated Deploy - QA pipeline failing to install several clients", creado 2026-08-19, lista
"85, 225, 248, 281, 300, 310, 353, 500, 505". El pipeline afectado es USQA, no produccion. Es lead
indirecto.

Dato que ninguna hipotesis explica todavia. El valor malo del recibo es 863485, seis digitos. En
DO-9495 el valor malo era 71, dos digitos, y era un numero de register. 863485 no tiene forma de
register. Verifica si 863485 es realmente ardm_event_vw.pos_number o si es un tercer valor. No
afirmes reversion limpia a DO-9495 hasta comprobarlo.

## Descartados, con razon

ENG-7898, "Gold Layer - Fix IS_ECOM false-positive on 'WAREHOUSE'-named stores (clients 248, 442)".
Afecta IS_ECOM, no el campo POS. El propio ticket dice "Not a new failure mode".

ENG-7610, "Snowflake Shares - Add supplementary export for CWH Till Drawer Open control actions
(ACTIVITYID 55)", creado 2026-08-24. Esta en Backlog, sin codigo mergeado. No es la causa. Si
identifica el pipeline exacto, cwh_ecom, donde hay que verificar si machine_name sigue mapeado.

RCS-28661, "Wal-Mart - POS 84 Showing instead of actual register". Sintoma identico, pipeline
BigQuery de Walmart, sin relacion tecnica.

RCS-28099, "CWH - HYP to RCS - Item Discount Logic", Under Customer Review. Mismo tenant y mismo
canal de ingesta. Causa distinta. Ruchi Vora, verbatim: "This ticket is waiting on customer to
provide us with the data as its missing from their data source." No afirmes causa comun.

## Proximos pasos, en orden

1. Consigue el SQL del search. Corre el reporte con parametros dummy para ver el query. Es la
   leccion de RCS-27644 en H&M, brain/markdown/16-rcs-soluciones.md:177-188.
2. Con el query, corre un SELECT sobre transacciones de CWH y resuelve la pregunta que la evidencia
   dejo abierta. Agrupa por tienda y por tradingday. Si el corte es por fecha, es H1. Si es por
   tienda o por tipo de till, es H2.
3. Comprueba si 863485 sale de ardm_event_vw.pos_number o de otra columna.
4. Verifica en el repo dbt de cliente 248 si map_ardm_header.sql mapea posno desde machine_name.
   Solo lectura en Azure DevOps.
5. Con la ventana cerrada y el archivo verificado, escala. La ruta para mapeo de datos en produccion
   es DELIVERY, brain/markdown/19-rcs-procesos-playbook.md:961. Para loaders y mapeo ARDM de CWH el
   orden es primero el PM Ruchi Vora, despues Peyman Motlagh de pyARDM y Data Ops. Enlaza DO-9495
   como antecedente.

## Correccion de datos del cerebro

tickets/RCS-28581.md dice "Cliente: CWH, Camping World". Es CWH, Chemist Warehouse. El error viene
de inbox/2026-08-27-cola-completa-por-sla.md:268, que lo titulo "Camping World".
tickets/INDICE.md:217 etiqueta RCS-28099 como "Ahold, ADUSA, Delhaize". Es CWH.

## Texto para el cliente. Ingles, para pegar en Jira

Destinatario: James McKenna, reporter verificado en el campo reporter de Jira.
Cero peticiones. La deuda del 27 se corrige de frente, una oracion. Proximo contacto anclado a
condicion, sin fecha.

```
Hi James,

I owe you the update I committed to on the 27th. Here it is.

Your correction on the 26th holds. The POS number is not resolving the till on all transactions, and I am treating it as an open defect on our side.

I need nothing from you on this one. The transactions you attached are enough for me to work from.

I will come back to you on this ticket once I have the cause identified.

Kind regards,
Juan
```

Version anterior descartada, y por que. Pedia dos Order Numbers y una confirmacion sobre store 036.
Las dos peticiones se resuelven con un SELECT propio. La skill lo prohibe: borra toda peticion que
puedas resolver tu. Ademas justificaba la peticion citando que las capturas eran de tiendas
distintas, y eso es un hallazgo de investigacion. Fuera.

## Compromisos que crea este texto

Uno. Volver a James en este ticket con la causa identificada. Sin fecha, la condicion es tener la
causa. No cumplirlo repite la deuda del 27.

## Transicion sugerida en Jira

Ninguna. Queda en Under Support Review. El comentario no pide nada, asi que la pelota es tuya y el
estado tiene que decir eso. Mover a Under Customer Review sin haber pedido nada falsea la cola.

## Ruta de acceso para el paso 1. Verificado contra el cerebro y Confluence

Las dos vias existen y tienes las dos. El orden que ahorra tiempo es Composer primero, Snowflake
despues.

### Composer vive en el tenant del cliente, no en Control Panel

"Secure EBR - Application Topology (Current State, April 2026)", RTS, pageId 477571317762:
"The Secure EBR Client Website connects to two primary data layers via the Secure Store and Search
Composer." "Search Composer, Routes client transaction queries to either Green Plum or Snowflake
depending on migration status."

"Control Panel - Start Here", ARPDT, pageId 475169095710:
"Control Panel is internal to Appriss Retail only. Customers do not have access to the Control
Panel."

Control Panel es el salto, no el destino.

### Pasos concretos

1. Entra a https://usprod.apprissretailcloud.com/control. Tus roles son SupportL2 y Engineers,
   registrados en brain/memoria/project_juan_accesos.md:13.
2. Tabla "Customers in USPROD", busca Chemist Warehouse.
3. Primera columna, "Click logo to sign in". No uses /<slug>/signin. Redirige al SSO del cliente,
   donde tu usuario de Appriss no existe. brain/memoria/project_juan_accesos.md:18.
4. En el tenant: All Apps, Secure Store, Explorer, Composer.
5. Barra de Composer: Parameters, Columns & Filters, Query. El boton Query imprime el SQL generado.

El boton Query esta verificado por ti mismo hoy en otro ticket.
inbox/2026-08-31-rcs-28618-comentario-interno.md:95-98: "Reproduced the failure in Production with a
Support account. Pulled the generated SQL from the Composer Query button. Ran four read only queries
against Snowflake."

Nota de discrepancia documental. Confluence no documenta ningun procedimiento para extraer el SQL
generado por Composer. El boton Query no aparece en RTS ni en ARPDT. Tu experiencia del 31 de agosto
manda sobre la ausencia en Confluence. Vale documentarlo despues.

### Gotchas de Composer

inbox/2026-08-31-rcs-28618-analisis.md:355: "El search que corre no es el del path publico. Al abrir
el quick link, Composer materializa una copia efimera bajo unsaved searches en el espacio del
usuario."

inbox/2026-08-31-rcs-28671-thd-searches-snowtime.md:23: "Abrir, correr, leer. No toques Composer."
Editar el campo por Composer ya empeoro un conteo de fallos en otro ticket.

### Snowflake, para el paso 2

"Using Snowflake for Support Investigations", RTS, pageId 477651730444:
"you can use Snowflake to directly query client data, confirming whether data is present, finding
the exact date a data gap started, without waiting on Engineering."
"You are logged in as the PUBLIC role by default. This role has read access to ARDMPROD."
Warehouse sugerido: SUPPORTDATA_XS_WH, X-Small. Login US: https://app.snowflake.com/okb13541/jn80103/

"Support Team Snowflake Access", ARPDT, pageId 477731028995:
"Support access is strictly read-only. No write or execute privileges are required."

Tres nombres de base circulan en la documentacion y no coinciden: ARDMPROD.ARDM_<clientid>,
ARDM_PRODUCTION.<CLIENTID>_SNOWTIME, y arp_production.c<###>_<clientname>. No adivines cual aplica a
CWH. El SQL que salga del boton Query te lo dice.

### El motor de CWH no esta confirmado, y esto importa

brain/markdown/05-appriss-kt-topic-1-nucleo-escalacion.md:434 registra CWH asi:
"248 | chemistwarehouse.com | CWH | GP11 | GP1 | Azure".

GP11 y GP1 son instancias Greenplum. Si CWH no migro a SnowTime, el query de Composer va a Greenplum
y no a Snowflake, y la ruta del paso 2 cambia. Greenplum se alcanza por salto al jump server LA4,
10.22.0.220 por RDP, credenciales trebu.co, llave gp5newnew.ppk.
brain/memoria/reference_ardm_instancias_clientes.md.

El boton Query resuelve esto de un tiro. La sintaxis del SQL delata el motor. La leccion esta en
inbox/2026-08-31-rcs-28618-analisis.md:435: "El motor es Snowflake, no Greenplum. La sintaxis
set var = valor; con referencias $var es de Snowflake."

Corre Composer primero. No pidas acceso a nada hasta saber que motor responde.
