# RCS-27765 · Guia de ejecucion con puntos de control · 14 sep 2026

Cada paso trae que debes ver para saber que vas bien, y que cambia si no lo ves.

## Paso 0. Confirmar cliente y esquema. Dos minutos

Winn-Dixie aparece en la captura de Shireesh como `\\p-ingest-fsla4\121_SEG\Archive`. De ahi sale
cliente 121, codigo SEG, esquema esperado `ardm_121`, en Snowflake `ARDMPROD.ARDM_121`.

Ese 121 es inferido del path, no confirmado. Verificalo en el Product Delivery Client Matrix, hoja
Clients, buscando 121 o SEG. Te da instancia de Greenplum y esquema.

CONTROL: si el matrix te da otro ID para Winn-Dixie, todo lo que sigue cambia de esquema. Para aqui.
FRENO: el matrix se actualiza a mano y tiene filas viejas. Si sale vacio o dice CRDM, confirma por
Control Panel USPROD, tabla Customers in USPROD.

## Paso 1. El conteo. Via A, por la aplicacion

Esta via reproduce el numero que ya le diste al cliente, sin adivinar SQL.

1. Control Panel USPROD, columna "Click logo to sign in", elige Winn-Dixie. No uses `/<slug>/signin`,
   redirige al SSO del cliente donde tu usuario no existe.
2. Busqueda de transacciones, filtro tienda 358, TradingDay del 24 al 26 jun 2026, agrupado por dia.
3. Boton Query del Composer para ver el SQL real. Copialo. Es tu evidencia auditable y te dice el
   motor: si abre con WITH es Greenplum, si no hay CTE es Snowflake.

CONTROL, este es el que te protege: deben salir tres filas. El 24/06 tiene que dar 2,323 y el 26/06
tiene que dar 2,421. Si esos dos no cuadran con lo que reportaste el 27 jul, no mires el 25/06.
Estas en otro tenant, en otra columna de tienda o en otro motor. Vuelve al paso 0.

Los dias vecinos son el testigo. Sin ellos el numero del 25/06 no prueba nada.

## Paso 1 bis. Via B, SQL directo

Solo si prefieres la base o la via A no te deja entrar al tenant.

Motor: `ARDMPROD.ARDM_121` en Snowflake, o el cluster GP que diga el matrix. Acceso por jump server
LA4, `10.22.0.220` por RDP con credenciales trebu.co.

Tabla verificada: `ardm_Header`, una fila por transaccion, columnas `TransactionID` y `TradingDay`.
La tienda entra por LEFT JOIN a `reference_location`, como aparece en el SQL generado de THD y de
Walmart.

El nombre exacto de la columna de tienda no esta escrito en el Cerebro. No lo adivines. Sacalo del
SQL del boton Query de la via A, o con un DESCRIBE sobre las dos tablas.

Solo SELECT contra produccion. Y verifica con que rol estas conectado si una query sale vacia sin
razon: tienes credencial de lectura y de escritura separadas.

## Paso 2. Leer el 25/06. Tres desenlaces y cada uno cambia el resto

A. Da 2,300 o mas. Entro. Salta al paso 5.
B. Sigue en 773. El reenvio no aterrizo. Sigue al paso 3.
C. Da un intermedio, por ejemplo 1,400. Entro parcial. Es peor que B porque no es un fallo limpio.
   Sigue al paso 3 y anota el delta exacto, Eng lo va a pedir.

## Paso 3. De quien es la falla. Logs del inbound de la Ingestion API

Ventana 9 sep 08:00 a 11 sep 23:59 ET. Cliente 121 SEG.

Campos: ClientID, ClientScope, CustomerID, CustomerHubName, DocId, DataSize, BlobLocation y el
codigo de respuesta.

Como se lee:
- 200 registrados y sin data en produccion. La falla es de Appriss. Escala a Eng con los DocId.
- 401 o 400. Es credencial o dataType del lado del cliente. El resultCode dice cual de las tres
  validaciones rebotó: 10 nombre de cliente, 12 identidad, 11 tipo de dato.
- Nada registrado. El cliente no envio. Vuelve a Matthew.

FRENO REAL: donde se consultan esos logs no esta escrito en el Cerebro. El precedente mas cercano es
App Insights, recurso `appi-prd-wus2-arp`, usado en RCS-28535 para ARP. El recurso del gateway es
otro y tu RBAC de Azure solo te muestra unas 14 VMs. Si ahi te frenas, no se detiene el ticket.
Pide el log en paralelo y pasa al paso 4, que si esta a tu alcance.

## Paso 4. SnowTime, Winn-Dixie, 9 y 10 sep

Mira volume trends y trading day distribution.

Buscas un pico de trading day 25/06 en la carga del 9 o del 10 sep. El patron normal del pipeline es
98% del dia anterior, asi que un trading day de 76 dias se ve solo.

- Aparece el pico y el conteo sigue en 773. La data entro al pipeline y se perdio aguas abajo. Eso
  es Eng con evidencia dura, no con sospecha.
- No aparece. La data nunca llego al loader. Vuelve a Matthew.

## Paso 5. Escribir. Solo aqui

Un texto al ticket y el mismo al correo, reply all sobre el hilo de Matthew. Sin fechas futuras al
cliente. Pideme el borrador cuando tengas el numero.

## Nota de ventana, aplica al Transaction Vault y no al conteo

`DataApi.CutOffDate` sin configurar toma por default tres meses antes de hoy. Hoy eso cae el 14 jun y
el 25/06 todavia queda del lado bueno. Alrededor del 25 sep cruza el umbral y los drill down de
recibos del 25/06 empiezan a servirse por el fallback de Greenplum en vez del Data API. El conteo
agregado no se mueve. Lo que ve el cliente al abrir un recibo, si.
