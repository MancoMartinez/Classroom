RCS-29361 Urban c044_urb, queries de solo lectura. TRANSACTIONID devolucion 2609079422895513998, venta original 2609075943847627398, TRADINGDAY 2026-09-07.

1. Lineas de las dos transacciones.
SELECT * FROM ARDM_PRODUCTION.C044_URB.ARDM_ITEM WHERE TRANSACTIONID IN (2609079422895513998, 2609075943847627398) AND TRADINGDAY = '2026-09-07';

2. Tender de la devolucion.
SELECT * FROM ARDM_PRODUCTION.C044_URB.ARDM_TENDER WHERE TRANSACTIONID = 2609079422895513998 AND TRADINGDAY = '2026-09-07';

3. Vinculo con la venta original.
SELECT * FROM ARDM_PRODUCTION.C044_URB.ARDM_LINKEDORDER WHERE TRANSACTIONID = 2609079422895513998 AND TRADINGDAY = '2026-09-07';

Si una tabla no existe, corre SHOW TABLES IN SCHEMA ARDM_PRODUCTION.C044_URB; y ajusta el nombre.

4. Alcance. Tickets con una devolucion con recibo y una linea de venta anulada, desde el 5 ago.
SELECT TRADINGDAY, COUNT(DISTINCT TRANSACTIONID) AS tickets FROM ARDM_PRODUCTION.C044_URB.ARDM_ITEM WHERE TRADINGDAY >= '2026-08-05' AND VOIDEDFLG = TRUE AND SALEFLG = TRUE AND TRANSACTIONID IN (SELECT TRANSACTIONID FROM ARDM_PRODUCTION.C044_URB.ARDM_ITEM WHERE TRADINGDAY >= '2026-08-05' AND RETURNFLG = TRUE AND REFUNDWITHRECEIPTFLG = TRUE) GROUP BY 1 ORDER BY 1 DESC;

5. Codigo de la funcion del recibo. Solo las lineas con receipt o void.
SELECT f.index + 1 AS linea, f.value::string AS texto FROM ARDM_PRODUCTION.INFORMATION_SCHEMA.FUNCTIONS fn, LATERAL FLATTEN(input => SPLIT(fn.function_definition, CHR(10))) f WHERE fn.function_schema = 'C044_URB' AND fn.function_name ILIKE '%TRANSACTION_JSON%' AND (f.value::string ILIKE '%receipt%' OR f.value::string ILIKE '%void%') ORDER BY 1;

5b. Si la 5 devuelve cero filas, lista las funciones del schema.
SELECT function_name, argument_signature FROM ARDM_PRODUCTION.INFORMATION_SCHEMA.FUNCTIONS WHERE function_schema = 'C044_URB' ORDER BY 1;

6. Las queries 5 y 5b no dan resultado porque la funcion vive en el schema Secure del cliente, no en ARDM_PRODUCTION.C044_URB. Busca en toda la cuenta.
SHOW USER FUNCTIONS LIKE '%JSON%' IN ACCOUNT;
SELECT * FROM TABLE(RESULT_SCAN(LAST_QUERY_ID())) WHERE "schema_name" ILIKE '%044%' OR "schema_name" ILIKE '%URB%';
Para clientes migrados a SnowTime la funcion puede llamarse GET_ARDM_JSON(TRANSACTIONIDS VARCHAR) en vez de GET_TRANSACTION_JSON(TXN_ID NUMBER).

7. Con la base y el schema del paso 6, lee el JSON que recibe el visor del recibo.
SELECT <base>.<schema>.GET_TRANSACTION_JSON(2609079422895513998);
o, si es la funcion nueva:
SELECT <base>.<schema>.GET_ARDM_JSON('2609079422895513998');

8. SHOW USER FUNCTIONS IN ACCOUNT agota los 180 s. Usa SHOW acotado.
SHOW SCHEMAS LIKE '%C044%' IN ACCOUNT;
Con cada base y schema que salga:
SHOW USER FUNCTIONS LIKE '%JSON%' IN SCHEMA <base>.<schema>;

9. Schemas de c044 encontrados: ARDM_PRODUCTION (C044_URB, C044_URB_SNOWTIME) y ARP_PRODUCTION (C044_URB, C044_URB_PLATFORM). El schema Secure es probablemente ARP_PRODUCTION.C044_URB.
SELECT function_name, argument_signature FROM ARP_PRODUCTION.INFORMATION_SCHEMA.FUNCTIONS WHERE function_schema IN ('C044_URB', 'C044_URB_PLATFORM') ORDER BY 1;
SELECT f.index + 1 AS linea, f.value::string AS texto FROM ARP_PRODUCTION.INFORMATION_SCHEMA.FUNCTIONS fn, LATERAL FLATTEN(input => SPLIT(fn.function_definition, CHR(10))) f WHERE fn.function_schema IN ('C044_URB', 'C044_URB_PLATFORM') AND fn.function_name ILIKE '%JSON%' AND (f.value::string ILIKE '%receipt%' OR f.value::string ILIKE '%void%') ORDER BY 1;

10. Eventsource GenericEventProvider, Eventinfo ardm_json (fetch+resolve), pos-data. Busca la tabla ardm_json.
SHOW TABLES LIKE '%JSON%' IN SCHEMA ARDM_PRODUCTION.C044_URB;
SHOW TABLES LIKE '%JSON%' IN SCHEMA ARDM_PRODUCTION.C044_URB_SNOWTIME;

11. Con el nombre de la tabla, lee el documento de la devolucion.
SELECT * FROM ARDM_PRODUCTION.C044_URB.<tabla_json> WHERE TRANSACTIONID = 2609079422895513998;

12. Control. Devoluciones con recibo del 14 sep, con el tipo de linea extra de cada ticket. Abre en Secure una de cada grupo y compara la etiqueta.
SELECT TRANSACTIONID, ANY_VALUE(STORENO) AS storeno, ANY_VALUE(POSNO) AS posno, ANY_VALUE(TICKETNO) AS ticketno, ANY_VALUE(TRADINGDAY) AS tradingday, MAX(IFF(SALEFLG AND VOIDEDFLG, 1, 0)) AS venta_anulada, MAX(IFF(SALEFLG AND NOT VOIDEDFLG, 1, 0)) AS venta_activa FROM ARDM_PRODUCTION.C044_URB.ARDM_ITEM WHERE TRADINGDAY = '2026-09-14' GROUP BY TRANSACTIONID HAVING MAX(IFF(RETURNFLG AND REFUNDWITHRECEIPTFLG, 1, 0)) = 1 ORDER BY venta_anulada DESC, venta_activa DESC LIMIT 30;
