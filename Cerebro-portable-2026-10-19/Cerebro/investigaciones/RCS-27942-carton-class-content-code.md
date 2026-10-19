# VS&Co, CartonClass y CartonContentCode vacios tras Reload Cartons

Ticket origen: RCS-27942. Tenant VSCoCorpAP, ClientID 123634. Abierto el 22 jul 2026.
Estado de la investigacion al 10 sep 2026: HIPOTESIS con dos ramas y discriminador definido.

## El sistema, como esta armado

ENG-1071 es el SOW del carton import de VS&Co, Done, release Secure February 2026 2/2. Define el
flujo completo.

Punto 2, el archivo de import entra por SFTP y crea casos mas registros de merchandise. El archivo
del cliente trae ocho columnas: Destination, Origin, Carrier, BOL #, Carton #, Tracking #, Ship
Date, Carton Claim Type. CartonClass y CartonContentCode no estan en esa lista.

Punto 3, "Carton content code is numeric and needs descriptive text mapping for business users.
This should be managed via application category/lookup for ease of maintenance going forward.
Initial mapping will come from DC teams."

Punto 4, "Uploads will batch call the API to enrich the cartons with Class (or Contents Category),
Units, Total Retail $". El enriquecimiento lo hace Appriss, no el cliente.

Punto 5, "Call API from the merchandise screen to process cartons entered manually or where the
lookup failed initially". Ese es el boton Reload Cartons.

ENG-4225, Done, release Secure June 2026 2/2 del 25 jun 2026, autor Matthew Kamminga, QA Gina
Pilato. Cambio las columnas CartonContentCode y CartonClass de GridViewDataTextColumn a
GridViewDataComboBoxColumn ligadas a ListMaster, TextField=Description ValueField=ID. Agrego el
campo Code (txtCodeValue) en ManageCategories que se guarda como MasterValue. El SQL 60_26_006.sql
siembra las categorias Merchandise_CartonContentCode y Merchandise_CartonClass, crea el config
CategoryCodeFields vacio por defecto, y para VSCoCorpAP lo setea a
'Merchandise_CartonContentCode,Merchandise_CartonClass'. La feature esta apagada para todos los
demas clientes.

## Las dos ramas

Rama 1, la resolucion contra ListMaster. Desde el 25 jun 2026 el grid ya no muestra texto libre,
resuelve un ID de categoria. Si las categorias sembradas no tienen entradas cargadas, o las tienen
sin MasterValue igual al codigo que devuelve el API, el combo no encuentra match y el valor no se
persiste. El SOW dejo el mapeo inicial a cargo de los equipos DC del cliente. Si nunca se cargo,
esto explica el sintoma completo y es configuracion, no codigo.

Rama 2, el parseo de la respuesta del API. Total Retail se pobla, Class y Content Code no. Si la
categoria esta bien cargada, el mapeo de esos dos campos en la respuesta es el que falla.

## El discriminador

La respuesta cruda del API para uno de los cuatro cartones que el cliente listo el 11 ago. Con
valor en la respuesta del API y NULL en dbo.Merchandise despues de Reload Cartons, el fallo esta
del lado de Appriss en todos los casos, y la rama la decide el paso 3 de abajo.

## Verificaciones, en orden

1. Control Panel, Engineering, Config Items o Global Config del tenant VSCoCorpAP. CategoryCodeFields
   debe valer Merchandise_CartonContentCode,Merchandise_CartonClass. Vacio cierra el caso.

2. Categorias cargadas.
   SELECT ID, Description, MasterValue, FormFieldName FROM dbo.ListMaster
   WHERE FormFieldName IN ('Merchandise_CartonContentCode','Merchandise_CartonClass');
   Se espera una fila por codigo, con MasterValue igual al codigo del API. Cero filas confirma
   la rama 1.

3. Dato crudo de los cartones del cliente.
   SELECT Carton, CartonClass, CartonContentCode, CartonType, TrackingNo, TotalRetail
   FROM dbo.Merchandise WHERE Carton IN ('00006372933919964476','00006372933919695018',
   '00006372933918485149','00006675230517557807');
   Retail poblado con Class y ContentCode NULL confirma que el corte esta despues del API.

Acceso: Azure Bastion y SSMS segun brain/memoria/reference_acceso_sql_tenants.md. VSCoCorpAP es
tenant clasico de nettrack, no platform, la ruta es QA-LPMS-RDP-001. Solo lectura.

## Verificado el 10 sep 2026

CategoryCodeFields no existe en Control Panel USPROD para victoriassecretandco.com, cliente 74.
Juan filtro por nombre y por Config Item, cero resultados en los 927 items del tenant. Control Panel
USPROD administra la plataforma clasica de usprod.apprissretailcloud.com. VS&Co corre en
apps.apprissretail.com/vss, otro host. El config que sembro 60_26_006.sql vive en la base de ese
tenant, no en Control Panel.

Las pantallas del sintoma son de nettrack legacy, no del Platform nuevo. ENG-4225 modifico
Merchandise.ascx y ManageCategories.aspx, archivos WebForms. ENG-1071 probo contra
test.lpguys.net/vscocorpap/nettrack. La ruta a mirar es apps.apprissretail.com/vss/nettrack, con el
patron de acceso de reference_viewreports_nettrack_legacy.md: entrar al tenant por el logo en
Control Panel y despues cambiar la ruta a nettrack.

## nettrack devuelve 500 al entrar por URL directa, 10 sep 2026

Tanto /nettrack/systemselect.aspx como /nettrack/Admin/ManageCategories.aspx, slug /vss, host
web-prd-wus2-arp-nettrack.azurewebsites.net, devuelven HTTP 500 con la misma excepcion:

  System.ApplicationException
  COMMON.GetConfigurationItem: DAL.ExecuteSimpleStringWithParms: Invalid object name
  'Secure.ConfigurationItem'. | SELECT value FROM [Secure].[ConfigurationItem] WHERE Name= @Param0

Revienta en LPSBO.Common.GetConfigurationItem, llamado desde LPSConstants.GetPublicBaseUrl dentro de
InitializeCulture. Es decir, falla en el arranque de la pagina, antes de cualquier logica de
Merchandise. La firma es GetConfigurationItem(String Name, Int32 PlatformID).

Dos lecturas, sin resolver.
Lectura A, falta contexto de sesion. Al escribir la URL a mano no hay tenant ni PlatformID
resueltos, la conexion cae a una base sin ese esquema y el objeto no existe. Prueba barata: entrar
al tenant por el logo en Control Panel y navegar a nettrack desde ahi. Precedente del mismo patron
en RCS-28482, reference_viewreports_nettrack_legacy.md, donde la entrada directa fallaba y la
entrada por Control Panel funcionaba.
Lectura B, el esquema no existe en la base del tenant. Si el objeto Secure.ConfigurationItem falta
de verdad, ningun script de la serie que incluye 60_26_006.sql pudo sembrar CategoryCodeFields ahi,
y eso explicaria por si solo los campos vacios. Esto es escalacion, no configuracion.

Discriminador: repetir la misma URL directa con otro tenant. Si otro tenant abre, gana B. Si todos
fallan igual, gana A.

Dato que no cuadra y hay que cerrar: Control Panel USPROD lista victoriassecretandco.com como
cliente 74, y usprod es la plataforma clasica. El host de nettrack es
web-prd-wus2-arp-nettrack, nomenclatura ARP, la misma de las bases platform. Falta establecer en
que base vive de verdad este tenant antes de correr las queries del entregable.

## La base existe, las tablas no estan en dbo, 10 sep 2026

sys.databases devuelve sqldb-prd-wus2-arp-production-074-vss-platform. El Client ID del tenant es
074, coincide con el cliente 74 de Control Panel. El 123634 de ENG-4225 es otra numeracion.

Las dos queries fallan igual:
  Msg 208, Level 16, State 1. Invalid object name 'dbo.ListMaster'.
  Msg 208, Level 16, State 1. Invalid object name 'dbo.Merchandise'.

Resuelto. El esquema no es dbo, es incident. sys.tables sobre la base 074 devuelve:

  incident.ConfigurationItem
  incident.EquipmentListMaster
  incident.ListMaster
  incident.Merchandise
  secure.ConfigurationItem

501 tablas en la base. Los nombres dbo.Merchandise y dbo.ListMaster salieron de la descripcion de
ENG-4225, que describe archivos de codigo de nettrack, no el esquema de la base del tenant migrado.

Esto cierra el 500 de nettrack a favor de la lectura A. secure.ConfigurationItem SI existe en la
base 074. La peticion que fallo no estaba mirando esta base, le faltaba el contexto de tenant por
haber entrado escribiendo la URL a mano. La base del tenant no esta rota y no hay nada que escalar
por ese lado.

## ENG-4225 no esta en el tenant 074, 10 sep 2026

Tres medidas sobre sqldb-prd-wus2-arp-production-074-vss-platform.

CategoryCodeFields no existe. incident.ConfigurationItem filtrado por Name LIKE '%CategoryCode%'
devuelve cero filas.

incident.ListMaster no tiene columna MasterValue. El barrido de INFORMATION_SCHEMA.COLUMNS con
patron '%Master%' entre otros devolvio solo Description y FormFieldName para esa tabla. ENG-4225
agrego el campo Code que se persiste como MasterValue. Sin esa columna, el cambio no esta aplicado
en esta base.

incident.Merchandise si tiene Carton, CartonClass, CartonContentCode, CartonType y TrackingNo. No
tiene TotalRetail, el nombre de la columna de retail es otro.

Lectura. ENG-4225 dice textualmente "For VSCoCorpAP (ClientID 123634)". VS&Co tiene dos entornos y
el script 60_26_006.sql se sembro en el clasico 123634. El tenant migrado 074, que es donde entra
Angie por apps.apprissretail.com/vss, no recibio ni la columna ni el config item. Eso explica por si
solo que CartonClass y CartonContentCode queden vacios mientras el retail si se pobla.

Confirmado sin depender de filtros. incident.ListMaster tiene exactamente cinco columnas:
Description, PerDivision, FieldLength, FormFieldName, ID. No existe MasterValue. El barrido de
ConfigurationItem por Name LIKE '%Carton%' o '%Category%' devuelve cero filas. Las dos cosas que
introduce ENG-4225, la columna MasterValue y el config item CategoryCodeFields, no existen en el
tenant 074.

CONCLUSION RETIRADA. Se dio por confirmado que ENG-4225 no estaba instalado en el entorno del
cliente. Estaba mal. La medicion siguiente lo tumba.

SELECT COUNT(*) FROM incident.Merchandise en la base 074 devuelve 0. La tabla esta vacia. La base
sqldb-prd-wus2-arp-production-074-vss-platform no contiene la operacion de VS&Co, es un cascaron.
Que le falte la columna MasterValue o el config CategoryCodeFields a una base sin datos no prueba
nada sobre el entorno donde trabaja Angie. Todo lo medido entre el schema y esta linea se midio en
la base equivocada.

Lo unico que queda en pie de esa tanda: la base 074 existe, esta vacia, y el 500 de nettrack
probablemente sea consecuencia de lo mismo y no de una configuracion rota.

Donde estan los datos, sin resolver. El candidato es el tenant clasico VSCoCorpAP, ClientID 123634,
que es el que nombra ENG-4225 y donde ENG-1071 hizo sus pruebas. Bikash si encontro datos reales el
6 ago 2026: su query devolvio ShopliftingID 5333930 con TrackingNo 1ZH4E0790301911717, Carton
00006675230520384636, CartonClass y CartonContentCode en NULL, CartonType Carton Not Received. El
tenia la base correcta. Preguntarle por que ruta la consulto es mas barato que seguir barriendo.

Falta un solo dato para cerrar el caso de punta a punta: los cuatro cartones que listo Angie el 11
ago, para medir el sintoma en la misma base donde falta el cambio.

Nota de metodo. Cinco queries murieron por nombres de objeto y de columna tomados de la descripcion
de ENG-4225 en vez de leerlos del esquema. ENG-4225 describe archivos de codigo de nettrack. El
esquema de la base de un tenant migrado es otro. Leer INFORMATION_SCHEMA antes de escribir la
primera query habria ahorrado cinco intentos.

El 6 y el 11 ago se le pidio al cliente confirmar con su IT si CartonClass y CartonContentCode
venian en el archivo de import. El SOW dice que esos campos no vienen del archivo, los llena
Appriss por API. La pregunta costo cinco dias y el cliente respondio el 11 ago con evidencia de
que su API si devuelve los valores. Desde el 19 ago el ticket no se mueve.

## El otro reclamo del mismo ticket

Tracking #. El SOW mapea Tracking # a Shipment.TrackingNo, campo nuevo, nivel shipment. La
respuesta que se le dio al cliente el 4 ago es correcta en el diseño. Queda una contradiccion
abierta: la query de Bikash del 6 ago sobre dbo.Merchandise con ShopliftingID 5333930 devolvio
TrackingNo 1ZH4E0790301911717. Si esa columna existe en Merchandise y a veces se puebla, hay que
saber cual columna lee el grid antes de repetir el argumento del diseño. El pedido del cliente de
tener el tracking uno a uno con el carton es enhancement, no defecto.

## Pruebas que nunca corrieron

ENG-5055 (TC_70212_I, los dropdowns guardan correctamente) y ENG-5056 (TC_70212_II, los valores
persisten al reabrir) siguen en Backlog. Gina Pilato dejo escrito el 22 jun 2026 "Confirmed
manually and automated tests created", los casos Xray quedaron sin ejecutar.## El API del cliente responde con valores, 10 sep 2026

Llamada directa a POST vscologisticsprod.eastus2.vsazure.com/logisticsinfo/v1/cartonretailvalue,
el mismo endpoint que describe ENG-1071 punto 4, con los cuatro cartonNumbers del ticket. Respuesta
200 OK:

  00006372933918485149  retailValue 4807.25  cartonClass 98  cartonContentCode PP
  00006372933919964476  retailValue 599.40   cartonClass 16  cartonContentCode GW
  00006675230517557807  retailValue 2461.20  cartonClass 98  cartonContentCode PT

Confirma de primera mano lo que el cliente ya afirmo el 11 ago con su propia validacion. El API
devuelve Class y Content Code para los cuatro cartones. El problema no esta en el dato de origen,
esta en el tramo entre la respuesta del API y la fila que queda en Merchandise. Eso es lectura de
codigo de ingesta, no exploracion de SQL.

Nota: 98/PP, 16/GW, 98/PT son codigos crudos. ENG-4225 resuelve CartonClass y CartonContentCode
contra categorias ListMaster via el config CategoryCodeFields. Si el codigo persiste crudo en la
tabla y el codigo mapea a un ID de categoria que no existe, la resolucion falla silenciosa y el
campo queda vacio en la UI aunque el dato haya llegado. Sigue sin descartarse porque no se ubico la
base de produccion real del tenant.

## Pista clave: el clasico es multi tenant compartido, no una base por cliente

Kiran confirma via chat, 10 sep 2026: VSCoCorpAP es client 74, VSCoCorpBP es client 434. El 434 no
esta en la misma base donde esta el 74 dentro de sqlmi-prd-wus2-arp-001. Ese servidor es el Platform
nuevo, una base por tenant, no el LPMS clasico.

Releyendo el stack trace del 500 de nettrack: LPSBO.Common.GetConfigurationItem(String Name, Int32
PlatformID). El parametro PlatformID es la marca de un esquema multi tenant compartido. El LPMS
clasico no tiene una base por cliente, tiene pocas bases (o una) con todos los tenants adentro,
discriminados por PlatformID o ClientID en cada fila. Eso explica por que 434 y 74 no comparten base
con nombre de tenant: ninguno tiene una base con su nombre en el clasico, ambos viven en la base
compartida filtrados por esa columna.

Servidor a probar: pd-lpms-uswest2-sqldb-001.database.windows.net, US Production, listado por Kiran.
Pendiente: listar sys.databases ahi, confirmar el nombre de la columna discriminadora en Merchandise,
y repetir las queries de siempre con el filtro de tenant agregado.


