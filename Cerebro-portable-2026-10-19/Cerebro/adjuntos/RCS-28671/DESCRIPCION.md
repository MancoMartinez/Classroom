# Adjuntos RCS-28671, descritos

Las tres capturas las subio Corey Wood a Jira el 31 ago 2026 09:31 EDT. Juan las paso al chat.

## image-20260831-132933.png
Pantalla Results del Composer de Secure Store, tema oscuro, breadcrumb
Portal > Secure Store > Explorer > Composer. Logo de The Home Depot arriba a la izquierda junto al
de Appriss Retail. Barra con Composer, Run, Columns & Filters y un candado con el numero 1.
Mensaje de error: "Sorry but we couldn't process your search". Tracking code
b7441dab-23a8-5798-b875-e5d63e194565. Boton Try again a la derecha. Pestanas Tabular y Chart, con
Tabular activa.

## image-20260831-132901.png
Pantalla Results con los parametros de la busqueda que fallo. Titulo
"Line Item Void - General Search", subtitulo "All line item voids by a selected parameters".
Parametros activos:
  HEADER Transaction Date Between June 01 2026 And August 31 2026  (REQ)
  HEADER Store Number Equal to 2605  (REQ)
  HEADER Cashier LDAP Equal to UBMKVT7
Parametros apagados: Transaction Total, Total Line Item Void Amount, Account Number XREF, SKU,
Tender Type Group.

## image-20260831-132917.png
Pantalla Results en tema claro, breadcrumb Portal > Secure Store. Mismo mensaje
"Sorry but we couldn't process your search". Tracking code 7f39278d-ebfd-5af1-9a85-131fc3dff2cb.
Ese codigo es el mismo UserToken que aparece en el log que pego Manisha Naik, asi que esta captura
y el stack trace de RunAsyncSearchActivity corresponden al mismo evento.

---

# Adjuntos de Ericka Smith, 01 sep 2026 15:20 EDT

Reportados por el Canada Field Team. Work Item 248159.

## 2026-09-01-ericka-wi-248159-cabecera.png
Cabecera del Work Item en Secure Store - Markdowns. Definicion
"MD03-APS-D - Consecutive Markdowns for Same Payment Card". Rango 08/27/2026 a 08/27/2026.
Prioridad High. ID 248159.
Metricas: Value Potential $0.00, Store Number 7135, Cashier LDAP DXM6269,
Unique Count of Appriss Secure ID 3.
Filtros: Region 0032-CANADA, District 0157-CHARL..., Store Number 7135, y "3 more".
Botones View y History, etiqueta "last week".
El Value Potential en cero con 3 IDs unicos es el sintoma: el work item existe y no trae
transacciones.

## 2026-09-01-ericka-wi-248159-events-error.png
Pantalla Portal > Work Item > Events. Tres paneles: Transactions con pestañas Investigation y
Journal, Selected con "Nothing selected.", y Pinned (0/4) con "Pin some items to see them here."
El panel de Transactions esta vacio. Abajo a la derecha, banner rojo:
"There has been a system error. Please contact support." con boton "Show Me Details".

## 2026-09-01-ericka-wi-248159-error-detalle.png
Modal "Error Information". Texto: "Something went wrong while trying to get the information you
requested." Tracking code del error: 774fbb98-fc34-4cd0-8ee8-538f85d2967d.

---

# Capturas que Juan paso al chat el 28 sep 2026

## wi-248159-events-url-fti.png
Pantalla Events del WI 248159 con la URL completa: homedepot.apprissretailcloud.com/platform/viewer#/store/live/fti/d1d505d6-9285-46f2-a115-497a48878d92?wi=248159. El FtiID de la URL coincide con el FtiID viejo que tenia 0 filas en fti.Transactions. Toast "There has been a system error. Please contact support."

## log-774fbb98-instantanalytics.png
Control Panel USPROD > Logs, Grafana, cliente homedepot.com (85), filtro User token 774fbb98-fc34-4cd0-8ee8-538f85d2967d. Una fila 2026-09-01 19:17:56, Error, Core.InstantAnalytics.InstantAnalyticsService, sender GetInstantAnalyticsEvents, "The Events relating to this instant analytics result could not be found", InstantAnalyticsService.cs linea 306, ApiController.cs linea 156.

## viewer-trans-8989.png
Viewer de Secure Store, transaccion 8989, store 7135, POS 51, cajero DXM6269, 08/27/2026 8:37:17 AM, total $73.07, DEBIT contactless, tarjeta 1262034041293206. Dos MANUAL PRICE OVERRIDE sobre HENRY MAGIC JOINTING SAND con RSN AMT OFF MKDN al 50%, cinco items anulados.

## canada01-markdowns-by-ldap-7135.png
Busqueda CANADA01 - Markdowns by LDAP, 5 resultados para DXM6269 Donna McLure en 7135. En rojo las tres transacciones del WI 248159: 8989 ($73.07, markdown 99.59), 8990 ($50.01, 44.26), 8991 ($25.00, 22.14), todas DEBIT con la misma cuenta 1262034041293206, entre 8:37 y 8:50 AM del 27 ago.
