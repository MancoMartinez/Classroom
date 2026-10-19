Mensaje corto para pedirlo:

Could you run these against Snowflake for THD, C085_THD and C085_THD_SNOWTIME? I don't have access
to either database. Trying to confirm whether a transaction exists in one, both, or neither.

Consultas, en orden. Las primeras dos ubican el esquema, la tercera es la que responde la pregunta.

-- 1. Esquema de la tabla en la base original
SELECT TABLE_SCHEMA, TABLE_NAME
FROM C085_THD.INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME ILIKE '%HEADER%' OR TABLE_NAME ILIKE '%TRANSACTION%'
ORDER BY TABLE_SCHEMA, TABLE_NAME;

-- 2. Lo mismo en la base migrada a SnowTime
SELECT TABLE_SCHEMA, TABLE_NAME
FROM C085_THD_SNOWTIME.INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME ILIKE '%HEADER%' OR TABLE_NAME ILIKE '%TRANSACTION%'
ORDER BY TABLE_SCHEMA, TABLE_NAME;

-- 3. La transaccion en la base original. Sustituir <esquema> por lo que salga del paso 1.
SELECT *
FROM C085_THD.<esquema>.ARDM_HEADER
WHERE TRADINGDAY = '2026-08-27'
  AND STORENO = 7135
LIMIT 20;

-- 4. La misma transaccion en la base SnowTime. Sustituir <esquema> por lo que salga del paso 2,
-- y el nombre de tabla si difiere de ARDM_HEADER.
SELECT *
FROM C085_THD_SNOWTIME.<esquema>.ARDM_HEADER
WHERE TRADINGDAY = '2026-08-27'
  AND STORENO = 7135
LIMIT 20;

Que responde cada resultado:

Aparece en las dos: el dato fuente esta bien en ambos lados, el problema esta en otro punto del
proceso que genera fti.Transactions.

Aparece solo en la original y no en la SnowTime: la migracion no trajo esa transaccion. Apunta
directo al cutover del 28 de agosto.

No aparece en ninguna: el dato nunca llego a Snowflake para esa tienda y ese dia. Es un problema mas
arriba en el pipeline, antes de cualquiera de las dos bases.

No aparece en la original y si en la SnowTime: la transaccion migro bien pero algo la excluyo antes
de la migracion o quedo huerfana. Es el caso menos probable.
