# SBX RCS-29205/06/07, hallazgos del paso 2, 30 sep 21:51 Bogota

Fuente: Executive Workbench del tenant starbucks-us, filtro Workview Monitor con las tres definiciones,
Date Range 01/07/2026 a 01/10/2026. Capturas de Juan en el chat.

1. Sin filtro de monitor, 25 sep a 1 oct: 3723 work items, 3155 C1 y 568 Unassigned. El tenant genera.
2. Las tres definiciones juntas, 1 jul a 1 oct: 199 work items. Avg open days 68 C1 y 57 Unassigned.
3. Result Count por Calendar Date muestra solo tres corridas: 01/07, 29/07 y 26/08.
   Aproximado por corrida: 72, 61 y 54 items sumando estados.
4. No hay punto para la corrida esperada del 29 o 30 sep, periodo 24 ago a 27 sep.

Lectura: la cadencia es cada 28 dias, unos 3 dias despues del cierre de periodo. Coincide con la
espera de 2 dias 7 horas. El cero que reporta el cliente queda CONFIRMADO en la app para las tres.
Falta separar si la corrida mensual no ocurrio para nadie o si ocurrio y estas tres dieron cero.
Siguiente: mismo grafico con una definicion mensual de control, fiscal period, que no este en los tickets.

## Control, 30 sep 21:55 Bogota
Definiciones mensuales de control, fiscal period, fuera de los tickets. Result Count muestra cuatro
corridas: 01/07, 29/07, 26/08 y 30/09. La del 30/09 trae 3 items Open.
Lectura: la corrida mensual del periodo 24 ago a 27 sep si ocurrio, el 30 sep. Las tres de los
tickets no tienen punto en 30/09. H3, espera de datos o rollover, queda descartada como explicacion
del estado actual. El cliente miro el 29 sep, antes de la corrida, y eso no cambia el resultado de hoy.
Reserva: la generacion corre una definicion a la vez. Revisar el 1 oct en la manana que las tres
sigan sin punto, o leer sus runs en la Platform DB, antes de marcar CONFIRMADO.
Siguiente: paso 3, busqueda origen a mano en Composer.

## Work View, 30 sep 22:15 Bogota
Categoria Discounts-All, texto "serve ware", 1 jul a 1 oct: 15 resultados.
- Partner Discount ... serve ware: items 156176 y 156175, periodo 27/07 a 23/08, creados hace un mes.
  Tag de agrupacion: Receiving Partner, 3721... y 3719... Ningun item del periodo 24/08 a 27/09.
- Store - Merch Item discounted - fiscal period: items 158884, 158885, 158887 del periodo 24/08 a 27/09, creados ayer.
- Controllable Discounting - Multiple Items Disc on the Same Trans by Cashier: items 160219, 160216,
  160274, 160242 del periodo 24/08 a 27/09, creados ayer.
Lectura: los descuentos sin partner corrieron el 29 sep con resultados. Lo que falla tiene un campo de partner o miembro:
Receiving Partner en 29206, Partners SVC en 29205, estrellas y MemberID en 29207.
Hipotesis nueva H1b: arpfiles PR 57459, desplegado el 24 sep, retipo MemberID de Int64 a String en
loyalty_card_ext e item_discount_ext y quito los operadores numericos. Si Receiving Partner es ese
campo y la definicion lo filtra con un operador numerico o lo compara como numero, la corrida del 29 sep da cero.
La corrida del 26/08 fue antes del cutover y antes del PR. No distingue entre las dos causas.

## SQL de la busqueda de soporte, 30 sep 22:25 Bogota
"1-Benefits - Partner Purchases Summary by Receiving Partner" genera SQL contra ardm_header:
T1.x_receivingpartnerid, comparado como texto con LOWER y FLATTEN de un arreglo JSON, y T1.StaffDiscountFlg = true.
Corrio sin error para 27/07 a 23/08 y para el segundo rango. Partner 37210022 con filas en los dos.
Lectura: Receiving Partner sale de ardm_header.x_receivingpartnerid, columna de texto con prefijo x_.
No es MemberID de item_discount_ext. H1b pierde fuerza para RCS-29206.
Siguiente: medir por semana StaffDiscountFlg y x_receivingpartnerid en ARDM_PRODUCTION.C166_SBX.ARDM_HEADER,
y sacar de stats.Search el SQL real de la trigger search de la definicion.

## Snowflake, partner discount por semana, 30 sep 22:28 Bogota
ARDM_PRODUCTION.C166_SBX.ARDM_HEADER, 27 jul a 27 sep. Resultado de Juan:
semana      transacciones  staffdiscount  receivingpartner  ambos
2026-07-27  52893492       341118         1765134           340587
2026-08-03  52798754       333622         1751240           333100
2026-08-10  54820017       342863         1779660           342334
2026-08-17  52882493       327574         1729524           327120
2026-08-24  59913739       403112         1889641           402643
2026-08-31  57188999       364834         1829530           364390
2026-09-07  55267345       350272         1812870           349876
2026-09-14  57288409       378577         1838164           378241
2026-09-21  55822950       349638         1794227           349227
Lectura: sin caida en la semana del cutover ni despues. StaffDiscountFlg y x_receivingpartnerid llegan completos.
El lado partner de RCS-29206 esta sano. La sospecha pasa a la condicion de serveware o descuento controlable de la definicion.
La consulta a stats.Search se corrio por error en Snowflake. Es T-SQL y va en SSMS contra la Platform DB 166.

## Snowflake query history, 30 sep 22:41 Bogota
SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY, filtro x_receivingpartnerid y staffdiscountflg, sin AutoCreated_ArrayParam, LIMIT 50.
Las 50 filas son del 30 sep. 49 de SVC_ARP_PRODUCTION_166_USER y 1 de Juan. 50 de 50 SUCCESS, sin error_message.
Ventana de generacion mensual: 01:50 a 04:37 PT del 30 sep. Corrieron definiciones de partner contra ardm_header:
CashierNo = x_receivingpartnerid, metricas por receiving partner con 520138 y 190223 filas, gift card con receiving partner.
Ninguna de las 50 trae condicion de serveware ni de descuento controlable. La trigger search de 29206 no aparece en ese tope.
Lectura: la generacion de definiciones de partner corrio el 30 sep sin errores. No confirma ni descarta la condicion de serveware.
Siguiente: query history filtrando por texto de serveware o de item discount, y para 29207 por memberid con error_message.
Entregables pegables de esta noche: inbox/2026-09-30-rcs-2920X-comentario-interno.md y -respuesta-manish.md.
Links Jira recomendados, los pone Juan: 29205, 29206 y 29207 relates entre si; 29207 relates RCS-28873.
