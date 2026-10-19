# SBX RCS-29205/06/07, plan del 1 oct

Estado en Jira, leido 1 oct: los tres en Under Support Review. Nota interna y respuesta a Manish pegadas el 30 sep 23:55 a 23:58 EDT.
Links puestos: 29205 relates 29206 y 29207, 29207 relates RCS-28873. Manish no ha respondido.
Proxima actualizacion diaria por SLA High: antes de las 22:55 Bogota del 1 oct.

## Paso 1. Fallos en la corrida mensual, Snowflake
SELECT start_time, execution_status, error_code, error_message, LEFT(query_text, 500) AS sql_inicio
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
WHERE user_name = 'SVC_ARP_PRODUCTION_166_USER'
  AND start_time BETWEEN '2026-09-29' AND '2026-10-01'
  AND execution_status <> 'SUCCESS'
ORDER BY start_time;

## Paso 2. Todas las trigger searches de la corrida, exportar CSV completo
SELECT start_time, rows_produced, execution_status, query_parameterized_hash, query_text
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
WHERE user_name = 'SVC_ARP_PRODUCTION_166_USER'
  AND start_time BETWEEN '2026-09-29' AND '2026-10-01'
  AND query_text ILIKE '%MetricQueryResults%'
ORDER BY start_time;

## Paso 3. Con el CSV: identificar el SQL de cada definicion, ver rows_produced, y medir por semana las columnas de su condicion.
## Paso 4. Ruta: si la causa es columna o catalogo tras el cutover, Delivery con Sebastian Rueda como contexto de PR 57459.
##         Si hay error de binding de MemberID, se suma a RCS-28873.

## Resultado paso 1, 1 oct 16:03 Bogota. Fallos de SVC_ARP_PRODUCTION_166_USER, 29 sep a 1 oct 00:00 PT
291 fallos:
- 280 con 100038 "Numeric value '<n>' is not recognized". 276 son la misma consulta:
  WITH T6AsCte ... T9.x_MemberID AS loyalty_card_ext_memberid, SUM(CAST(T9.Points AS BIGINT)) AS SumofRewardStarsRedeemed,
  MAX(T9.x_TotalStarsAccrued) AS MaxofRewardStarsAccrued, T7.TradingDay ... COUNT(DISTINCT CASE WHEN ...
  Primera 30 sep 00:08 PT, ultima 23:57 PT. Cuatro por hora todo el dia: el generador reintenta cada 15 minutos y falla siempre.
  Los otros 4 son una busqueda de gift card.
- 3 con 000904 invalid identifier 'T1.WEEKLYPERIODOFTRANSACTIONDATE': 29 sep 00:40 y 30 sep 04:37:28 y 04:37:29 PT. SQL redactado.
  Cae en medio de corridas de metricas, no se puede atribuir a una definicion todavia.
- 8 con 000604 canceladas, consultas interactivas sin relacion.
Lectura: RCS-29207 casi seguro es la consulta de estrellas que falla con el error de MemberID numerico, familia RCS-28873.
Falta el texto completo para atar la consulta a la definicion SFE Star Farming.
Paso 2: el CSV filtrado por MetricQueryResults trae el job de metricas, no las trigger searches de work items. No sirve para 29205 y 29206.

## Resultados A, B y C, 1 oct 16:10 Bogota

### RCS-29207 CONFIRMADA
Consulta A: la consulta que falla trae alias "Topic_-_SFE_-_Star_Farming_same_day_high_volume". Es la definicion del ticket.
Condicion que rompe: T9.x_MemberID <> 70267962874. x_MemberID es TEXT en SnowTime y el literal va sin comillas.
Ultima falla: 1 oct 14:05 PT, query ID 01c77251-0109-d5e7-0120-d20111b67fc7, Numeric value '1867074335977200' is not recognized.
Consulta B, por dia: 26 ago SUCCESS 35, 28 ago FAIL 4, 9 sep FAIL 4, 30 sep FAIL 276, 1 oct FAIL 180. Reintenta cada 15 min.
Ruta segun reference_escalacion_l3_procedimiento: configuracion en produccion va a Delivery Secure 5, Peyman Motlagh, sprint RCS Support Team.
Codigo va a Engineering con Shandana Khan. Pregunta abierta a Sebastian Rueda: si PR 57459 cubrio esta definicion.

### RCS-29206 PROBABLE
Consulta C, 30 sep 01:01:44 PT, SUCCESS sin filas: StaffDiscountFlg, ardm_ItemDiscount DiscountCode IN lista y NOT IN lista,
reference_product.ProductHierarchy1 IN dos listas, HAVING transacciones, fechas y SUM(Amount). Calza con la regla de serveware.
Elemento distinto a las demas busquedas de partner que si corrieron: INNER JOIN a reference_Employee con x_EmploymentStatus = 1,
por x_receivingpartnerid = operatorid. Sospecha: ese join o ProductHierarchy1 quedaron sin coincidencias tras el cutover.

### RCS-29205 SIN UBICAR
Ninguna de las 9 consultas de C usa x_partneridontoken ni refund. Falta buscar por cero filas con tender o gift card.

## Resultados D, E y F, 1 oct 16:19 Bogota

### D. Historial de la busqueda con reference_Employee y ProductHierarchy1
29 jul 4 ejecuciones SUCCESS: 3, 2, 4, 6 filas. 26 ago 3 SUCCESS: 2, 4, 3. 28 ago 4 FAIL, dia del cutover.
30 sep 01:01:44 PT SUCCESS sin filas, corrida programada. 30 sep 12:58 a 12:59 PT: sin filas, luego 2, 4 y 4.
1 oct 10:20 PT: 51 filas. Las corridas de la tarde y de hoy las lanzo alguien en la app con otros parametros.
Lectura: la corrida programada dio cero. Con otros parametros si trae filas. No esta probado que sea la definicion de serve ware.

### E. Join con empleados activos
Entre 88% y 96% de las transacciones de partner encuentran empleado activo, todas las semanas, sin quiebre en el cutover.
El join con reference_Employee queda DESCARTADO como causa.

### F. RCS-29205 ubicada, PROBABLE
30 sep 02:08:49 PT, SUCCESS sin filas. TransactionType = 2, refund. T3.x_partnerownedtoken = parametro. Cuatro banderas de partner
del header igual a parametro: x_partnerbeanmarkoutflag, x_partnerbeverageflag, x_partnerfoodmarkoutflag, x_partnersaleflag.
Agrupa por AccountNumber, gift_card x_cardclass y x_partnerownedtoken. Calza con refund a SVC o tarjeta de partner sin partner discount.
Siguiente: distribucion de x_partnerownedtoken y las cuatro banderas en refunds antes y despues del 27 ago.

## Resultados G y H, 1 oct 16:22 Bogota

### RCS-29205: columna vacia desde el cutover, CONFIRMADO en datos
Refunds, TransactionType 2, ARDM_PRODUCTION.C166_SBX, 27 jul a 27 sep:
antes del 27 ago: x_partnerownedtoken TRUE 3927, NULL 169878. Desde el 27 ago: TRUE 0, NULL 204745.
La trigger search filtra T3.x_partnerownedtoken = parametro. Cero filas el 30 sep 02:08:49 PT.
Pregunta abierta: mapeo de x_partnerownedtoken en el modelo de tender de SnowTime para c166_sbx y quien es el dueño.
Precedente de mapeo SnowTime por cliente: RCS-28638 MYR, dbt/clients/us/<cliente>/models/mapping/map_ardm_tender.sql.

### RCS-29206: misma busqueda corrida por periodo el 30 sep 12:58 a 12:59 PT
29 jun a 26 jul: 4 filas. 27 jul a 23 ago: 2 filas. 24 ago a 27 sep: 0 filas. Corrida programada 01:01:44 PT: 0 filas.
Antes del cutover la misma busqueda usaba ardm_header_ext.receivingpartnerid y reference_Employee_Ext; ahora columnas x_.
Lectura: la busqueda funciona sobre SnowTime para periodos viejos. El cero esta en los dias posteriores al cutover.
Siguiente: DiscountCode y ProductHierarchy1 antes y despues del 27 ago.

Entregables del 1 oct en inbox: rcs-29205/06/07 comentario-interno y respuesta-manish, rcs-29207 teams-sebastian.

## Resultados I y J, 1 oct 16:26 Bogota, RCS-29206
J: joins de descuento a item y producto completos antes y despues, 3858918 y 4160371 descuentos, faltan 3 en cada tramo. DESCARTADO.
I: mezcla de DiscountCode en transacciones de partner. Solo antes del 27 ago: 4563 649, 4567 171, 4569 16, 2647 1.
Solo despues: 4575 113, 4554 80, 4282 69, 4576 24, 4287 11, 4552 1, 4229 1. 4571 sube de 786 a 3803, 4574 de 101 a 1132.
Hipotesis nueva, PROBABLE: la definicion tiene una lista fija de codigos controlables. Si lista los codigos retirados,
el cero viene de la lista y no del cutover. Seria configuracion del cliente o de Delivery, no defecto.
Siguiente: codigos que la definicion uso en agosto, desde Events del work item 156176, y conteo semanal de esos codigos.

## K, L y M, 1 oct 16:37 Bogota. RCS-29206 CERRADA en investigacion: cero real, sin defecto
K: transacciones de agosto de los items 156176 y 156175 usan codigo 6 Partner Discount, 3 Amount off, 4 Percent off,
y 4563 Merch Sum Sale en una sola. Jerarquia 085, vasos y tumblers.
L: codigos 3 y 4 siguen sobre jerarquia 085 despues del cutover con volumen parecido. 4563 desaparece y no hace falta.
La hipotesis de lista de codigos desactualizada CAE.
M: regla reconstruida, codigos 3 y 4, jerarquia 085, minimo 2 tx, 2 fechas, monto <= -30:
P1 29 jun a 26 jul: 131 partners, 3 califican. Busqueda real: 4 filas, falta la segunda lista de jerarquias.
P2 27 jul a 23 ago: 48 partners, 2 califican. Busqueda real: 2 filas. Coincide exacto, partner 37210022 con -47.92.
P3 24 ago a 27 sep: 103 partners, 0 califican. Busqueda real: 0 filas.
Conclusion: el periodo tuvo actividad y nadie llego a los tres umbrales. Sin defecto.
Entregables reemplazados: inbox/2026-10-01-rcs-29206-comentario-interno.md y -respuesta-manish.md, ahora con explicacion de causa.

## Respuesta de Sebastian Rueda, 1 oct
"Member ID paso de Int64 a String". No sabe quien es dueño del mapeo de tender de SnowTime.
Decision RCS-29207: escalar a Delivery Secure 5, Under Delivery Review, Peyman Motlagh, Team Ownership Support (Delivery Dep.), Sprint RCS Support Team.
Nota: inbox/2026-10-01-rcs-29207-escalacion-delivery.md, reemplaza la nota interna anterior.
Decision RCS-29205: preguntar a Matthew Everett, que trabajo los mapeos SnowTime vacios de Myer, RCS-28518/28536/28559.
Teams: inbox/2026-10-01-rcs-29205-teams-matthew-everett.md. Ticket en Work in Progress hasta tener dueño.
Advertencia de Matthew en RCS-28518: no correr rebuild antes de desplegar el fix de mapeo.

## 2 oct. Decision: escalar 29207 y 29205 a Delivery Secure 5
Estado leido en Jira el 2 oct: 29205 y 29207 en Work in progress con nota y respuesta del 1 oct pegadas. 29206 Under Customer Review.
Sebastian Rueda no sabe el dueño del mapeo SnowTime. Regla del procedimiento: dato o configuracion en produccion va a Delivery.
Entregables: inbox/2026-10-02-rcs-29207-escalacion-delivery.md, -respuesta-manish.md, y los mismos de 29205.
Estado destino: Under Delivery Review, Peyman Motlagh, Team Ownership Support (Delivery Dep.), Sprint RCS Support Team.
