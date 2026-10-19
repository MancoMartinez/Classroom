-- Paso 1. Genera la consulta. Corre esto y copia el valor de la columna SQL_GENERADO.
-- Mide cada columna X_ de C166_SBX: filas con dato antes del cutover (27 jul a 26 ago)
-- contra despues (27 ago a 27 sep). Solo tablas que tienen TRADINGDAY.
SELECT LISTAGG(
         'SELECT ''' || c.table_name || ''' AS tabla, ''' || c.column_name || ''' AS columna, '
         || 'COUNT_IF(TRADINGDAY <  ''2026-08-27'' AND "' || c.column_name || '" IS NOT NULL) AS con_dato_antes, '
         || 'COUNT_IF(TRADINGDAY >= ''2026-08-27'' AND "' || c.column_name || '" IS NOT NULL) AS con_dato_despues '
         || 'FROM ARDM_PRODUCTION.C166_SBX."' || c.table_name || '" '
         || 'WHERE TRADINGDAY BETWEEN ''2026-07-27'' AND ''2026-09-27''',
         ' UNION ALL ')
       WITHIN GROUP (ORDER BY c.table_name, c.column_name)
       || ' ORDER BY con_dato_despues, con_dato_antes DESC;' AS sql_generado
FROM ARDM_PRODUCTION.INFORMATION_SCHEMA.COLUMNS c
WHERE c.table_schema = 'C166_SBX'
  AND STARTSWITH(UPPER(c.column_name), 'X_')
  -- Si tarda mucho, descomenta la linea siguiente y limita a las tablas principales:
  -- AND c.table_name IN ('ARDM_TENDER', 'ARDM_HEADER')
  AND EXISTS (SELECT 1 FROM ARDM_PRODUCTION.INFORMATION_SCHEMA.COLUMNS t
              WHERE t.table_schema = c.table_schema
                AND t.table_name = c.table_name
                AND t.column_name = 'TRADINGDAY');

-- Paso 2. Pega el texto copiado en un worksheet nuevo y correlo.
-- Lectura: con_dato_antes mayor que 0 y con_dato_despues en 0 es un campo que dejo de llegar
-- en el cutover. x_partnerownedtoken debe salir en esa lista. Si sale tambien un campo que
-- usa RCS-29206, avisame: cambiaria la conclusion de ese ticket.

-- Paso 3. Columnas que existian en legacy y no existen en SnowTime.
-- Cruza ARDMPROD.ARDM_166 contra ARDM_PRODUCTION.C166_SBX por nombre, con y sin prefijo X_.
-- Un renombre distinto a ese patron puede salir como falso positivo, revisalo a mano.
SELECT l.table_name, l.column_name, l.data_type
FROM ARDMPROD.INFORMATION_SCHEMA.COLUMNS l
LEFT JOIN ARDM_PRODUCTION.INFORMATION_SCHEMA.COLUMNS s
  ON s.table_schema = 'C166_SBX'
 AND UPPER(s.table_name) = UPPER(l.table_name)
 AND (UPPER(s.column_name) = UPPER(l.column_name)
      OR UPPER(s.column_name) = 'X_' || UPPER(l.column_name))
WHERE l.table_schema = 'ARDM_166'
  AND s.column_name IS NULL
ORDER BY 1, 2;
