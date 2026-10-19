# RCS-27765 · El SQL del Composer no mide transacciones · 14 sep 2026

Juan saco el SQL real con el boton Query. Motor confirmado Snowflake: sintaxis `set var` con `$var`
y `TABLE(SECURE_SQUAREHIERARCHY...)`. No hay CTE de Greenplum.

## Cinco defectos del SQL generado, para contar transacciones

1. `COUNT(1)` sobre el join a `ardm_Item` cuenta LINEAS DE ARTICULO, no transacciones. Cada header se
   multiplica por sus items. Para transacciones va `COUNT(DISTINCT T1.TransactionID)`.
2. El filtro de fecha es `T2.OrigTradingDay`, columna de `ardm_Item`. Por el nombre y su uso en
   devoluciones, apunta al trading day ORIGINAL de la venta, no al dia en que ocurrio la transaccion.
   HIPOTESIS, no verificada contra el diccionario. El dia real vive en `T1.TradingDay`.
3. `T3.LocationID IS NOT NULL` convierte el LEFT JOIN de jerarquia en INNER. Filtra por las tiendas
   visibles del UserId. Si tu usuario pierde acceso a la 358 el resultado cae a cero sin error.
4. La ventana `2025-08-15` a `2026-09-14` es condicion fija inyectada por el Composer, la misma
   familia del indicador naranja de Walmart en RCS-28618.
5. `GROUP BY CashierNo, StoreNo` sin dia. Los tres dias salen mezclados y hay que sumar filas.

Conclusion: este SQL no reproduce los 773 / 2,323 / 2,421 del 27 jul. Ese numero salio por otra via.

## Consulta de conteo, limpia

```sql
USE DATABASE ARDMPROD;
USE SCHEMA ARDM_121;          -- confirmar el 121 antes de correr

SELECT T1.TradingDay                    AS "trading_day",
       COUNT(DISTINCT T1.TransactionID) AS "transacciones"
FROM ardm_Header AS T1
WHERE T1.StoreNo = 358
  AND T1.TradingDay BETWEEN CAST('2026-06-24' AS DATE) AND CAST('2026-06-26' AS DATE)
GROUP BY T1.TradingDay
ORDER BY T1.TradingDay;
```

El `USE SCHEMA` explicito no es adorno. RCS-28671 midio comandos generados sin calificador de base ni
de esquema y sin `USE` delante, y dos ejecuciones identicas dieron resultados distintos.

## La consulta que cierra el ticket sin pasar por logs ni SnowTime

`ardm_Header` lleva `inserteddatetime` y `filename`. Verificado de rebote: el join de
`GetTransactionJson` con `REFERENCE_LOCATION` excluye `_row_created, inserteddatetime, updateddatetime,
filename` por nombre duplicado, o sea las dos tablas las tienen.

```sql
SELECT T1.TradingDay                    AS "trading_day",
       DATE(T1.inserteddatetime)        AS "dia_de_carga",
       T1.filename                      AS "archivo",
       COUNT(DISTINCT T1.TransactionID) AS "transacciones"
FROM ardm_Header AS T1
WHERE T1.StoreNo = 358
  AND T1.TradingDay = CAST('2026-06-25' AS DATE)
GROUP BY 1, 2, 3
ORDER BY 2;
```

Lectura directa:
- Filas con `dia_de_carga` del 9 o 10 sep: el reenvio SI entro. El problema es aguas abajo del ARDM.
- Solo filas cargadas en junio: el reenvio nunca aterrizo. La falla es del cliente o del inbound.
- `filename` nombra el archivo real con el que entro cada lote, y desmiente o confirma de una vez el
  `TL358_20260625999999999.tlg` que el cliente dice que era interno.

Corre `DESCRIBE TABLE ardm_Header` primero. Si los nombres de columna difieren, ajusta y no asumas.

Este par de consultas reemplaza los pasos 3 y 4 de la guia si la columna de carga existe.
