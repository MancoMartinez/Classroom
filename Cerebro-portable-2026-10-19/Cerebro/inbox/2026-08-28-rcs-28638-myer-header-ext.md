---
ticket: RCS-28638
cliente: Myer Australia (client 109, MYR, Greenplum GP3, Azure)
prioridad: High
tipo: Incident
estado_jira_verificado: Under Support Review (28 ago 2026)
assignee: Juan Martinez
reporter: Christine Piacentini
creado: 2026-08-27T20:49:03-0400
---

# RCS-28638 Myer, mapeo de Proof Type, Order No y Financial Statement Date

## Lo que reporta el cliente

Cita textual de la descripcion:

> The mapping of the Header Ext fields of Proof Type, Order No and Financial Statement date is
> missing from Transactions since 09/08/26
> The search I have created associated with this defect can be located in the Validation Folder
> Transaction ID: 2608273342446971618

## Que se verifico y contra que fuente

Jira vivo, getJiraIssue RCS-28638, 28 ago 2026. Estado Under Support Review, prioridad High,
assignee Juan Martinez. Dos comentarios: acuse de Akshaya Purappemane y toma de propiedad de Juan
el 27 ago 21:18. Ningun comentario tecnico todavia.

Tres adjuntos del reporter, guardados en `adjuntos/RCS-28638/`:

image-20260828-004653.png. Fila de resultados del search. Transaction ID 2608273342446971618,
Store No 219, Cashier No 1077380, End Trans Date Time 27/08/2026 12:11:49 PM, Transaction Amount
-500.00, Register 618, Transaction 44, Transaction Type Return/Exchange With Proof Of Purchase.
Las columnas Financial Statement Date, Order Number y Proof Type salen vacias.

image-20260828-004816.png. Retail Transaction Details de la misma transaccion. Store ID 219,
Transaction ID RT2196182708260044, Total Amount -500.00, Team Member Name Aravinda (1077380),
Training Mode N, Authorized by Team Member 1148897, Register ID 219618, Transaction Status
Finished, begin 27/08/2026 12:07:36 GMT+10, end 12:11:49 GMT+10. Card Number 627804******0812.
Bloque RETURN/EXCHANGE WITH PROOF OF PURCHASE con dos lineas resaltadas por el cliente:
`Proof Type : CUSTOMER ORDER RETURN` y `Customer Order Number : 2002504903`. Ambas POBLADAS.
Linea de item: RETURN, DE'LONGHI EC9255WI ARTE METAL PRO COLD B 4717, article 187370800,
-500.00 GST, `Reason ID:RC19`, `Reason Description:$lineItemDomainSpecific.returns.returnNotes`.

image-20260828-004849.png. Receipt view de Myer Group Sydney City, misma transaccion.
Los labels `Financial Statement Date:` y `Proof Type:` aparecen sin valor. La linea de item dice
`RETURN REASON: OTHER REASON`. Tender Visa -500.00.

## Hallazgo central

El dato llego a Appriss. La misma transaccion 2608273342446971618 muestra Proof Type
CUSTOMER ORDER RETURN y Customer Order Number 2002504903 en Retail Transaction Details, y los
muestra vacios en las columnas del search y en el receipt view. La perdida no esta en el envio del
cliente. Esta entre el detalle de la transaccion y los campos Header Ext que alimentan las columnas
del search y la plantilla del recibo.

Segundo defecto en la misma evidencia, no reportado por el cliente.
`Reason Description:$lineItemDomainSpecific.returns.returnNotes` es un token de plantilla sin
resolver. El render esta pidiendo una propiedad que el payload ya no expone con ese nombre. El
receipt view cae a `OTHER REASON` mientras el detalle guarda `RC19`. Firma de cambio de nombre de
propiedad en el origen o en la plantilla de mapeo, no de dato ausente.

## Contradiccion en la fecha de corte, hay que cerrarla con el cliente

El cliente afirma "missing since 09/08/26". RCS-28640, mismo cliente, misma fecha de corte
declarada, aporta como transaccion CORRECTA la 2608098315964575603. El prefijo del Transaction ID
es AAMMDD, asi que esa transaccion es del 09/08/2026 y esta bien. El corte cae despues del 9 de
agosto, no el 9. La ventana exacta sigue abierta.

## Contexto de cuenta, esto no es un ticket suelto

Doce tickets Myer creados en agosto 2026. Nueve son defectos de mapeo o datos faltantes. Cuatro
entraron el 27 de agosto, tres de ellos en dos horas de la noche, todos desde la misma sesion de
validacion del cliente.

Los cuatro del 27 de agosto:

    RCS-28638  High    Juan Martinez   Proof Type, Order No, Financial Statement Date, desde 09/08/26
    RCS-28612  Medium  sin asignar     Delivery Fee en Point of Sale, desde 29/06/2026
    RCS-28639  Low     Vlad Bogus      Manager ID volvio de Authorising TM al nombre Appriss
    RCS-28640  Medium  sin asignar     Auto Reference, desde 09/08/26

Los cuatro previos, todos Work in progress y todos con Matthew Everett:

    RCS-28518  High    Gift y Return Cards, Auth No en recibos, 21 ago
    RCS-28536  Medium  Mapping Defect Paid In/Out, desde 15/07/2026, 23 ago
    RCS-28537  Medium  Credit card Tender Type y POS Hash en Paid In, 23 ago
    RCS-28559  High    Missing POS Hash Credit Card Numbers, 78.439 el 22/08/26, 24 ago

Cuatro ventanas de corte distintas declaradas por el cliente: 29/06, 15/07, 09/08 y el
comportamiento nuevo del 21 ago. No es un evento unico.

## Causa candidata que ya nombro el cliente

RCS-28518, cita textual:

> This changed seems to have occurred at the same time as the recent implementation of the payments
> project. When testing the gift card payments in QA the mapping was correct on the receipt.
> Note: This defect did not occur in the test environment. The logic seems to be correct in the QA
> environment.

Rastro del payments project: RCS-26437 del 12 abr 2026 y RCS-26537 del 19 abr 2026, ambos cargas a
QA para ese proyecto, ambos Resolved. Y RCS-27978 del 27 jul 2026,
"Request to load data into the QA Environment OMNI store August Release Sprint".

Hipotesis a medir, no confirmada. El mapeo especifico de Myer se pierde o se sobrescribe cuando
entra un release, y cada release se lleva otro grupo de campos. QA queda correcto porque ahi el
mapeo se rehace a mano al cargar los archivos de prueba. Esto explicaria las cuatro ventanas de
corte y explicaria por que el cliente insiste en que en QA todo estaba bien.

## Precedentes utiles

RCS-26403, Completed. Request to map Return With Proof of Purchase Type: Receipt. Es el ticket que
mapeo Proof Type originalmente. Sirve para saber donde se configuro y quien lo hizo:
Chenuka Ratwatte.

RCS-26010, Customer Resolved. Mapeo de informacion de cliente en Return With Proof of Purchase,
hacia las Customer Extension Tables. Mismo tipo de transaccion, misma familia de tablas de
extension.

RCS-25061, Resolved. Delivery Fee Details Missing en Point of Sale. Antecedente exacto de
RCS-28612. Ya paso una vez y volvio.

RCS-27262, Resolved. POS Hash del 29 y 30 mayo 2026. Antecedente exacto de RCS-28559. Se resolvio
recargando los archivos. Ya volvio.

RCS-22051, Resolved. Velocity Tender Account Number no mapeado, el numero de referencia ocupaba el
lugar del numero real. Mismo patron que RCS-28518.

RCS-27644 H&M, del cerebro, `brain/markdown/16-rcs-soluciones.md:177-188`. Leccion procedimental:

> pedir/conseguir siempre el SQL del search (correr el report con parametros dummy para ver el
> query), fue lo que destrabo la causa raiz

Y el dato de donde viven los overrides de mapeo por cliente: `secure_Resource.json`.

## Ruta de escalacion

Data mapping va a DELIVERY, no a Engineering. Fuente:
`brain/markdown/19-rcs-procesos-playbook.md:961`

> DELIVERY: problemas de DATA y CONFIGURACION ya en produccion, incluido DATA MAPPING de menor
> alcance y setup/config. Contactos: Matt Kamminga (LPMS/CAMS), Ian Williams/Kenny Vu (Engage),
> Tomasz Mikunda/Carl Costelow (Secure 3/4/5).

Myer es Secure Store, asi que Tomasz Mikunda o Carl Costelow.

No existe ticket ENG de Myer sobre mapeo. Verificado con JQL sobre ENG y DATASCI desde el 1 jun
2026. El unico Myer es ENG-6976, transferir caso a Incident, Ready for Development, Matthew
Kamminga. No tiene relacion con este defecto.

## Vacio de conocimiento confirmado

El cerebro no tiene una sola entrada sobre Header Ext, Proof Type, Financial Statement Date ni Auto
Reference. Cero hits. Myer no tiene ficha de cuenta ni entrada en investigaciones.

El runbook que este ticket necesita esta sin escribir. `brain/markdown/03-documentation-trackertracker.md:203-215`,
entrada T-012:

> Runbook for the most common Data Ops fire: customer changes columns / schema drift / mapping
> breaks. Recurring in Peyman's RCS queue.
> Status: Not Started. Appriss partner: Peyman Motlagh. Nuaav assignee: Sebastian Rueda.

## Datos tecnicos de la cuenta

Client ID 109, codigo MYR, Greenplum GP3 y GP1, hosting Azure. Fuente
`brain/markdown/05-appriss-kt-topic-1-nucleo-escalacion.md:388`.
GP3 es on premise, acceso SSH con credenciales gpadmin del password book, salto por jump server LA4
10.22.0.220. Fuente `brain/memoria/reference_ardm_instancias_clientes.md:32`.
Archivos crudos en `p-ingest-<region>/109_MYR/Archive/Prod/<fecha>`.

## Transicion sugerida

Ninguna todavia. El ticket esta en Under Support Review y ahi debe quedarse hasta cerrar la
evidencia interna. No comentar al cliente antes de tener la ventana de fechas confirmada.
