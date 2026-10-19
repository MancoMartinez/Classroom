-- CONSULTA 1. Campos X_ que tenian dato antes del cutover y quedaron vacios despues.
-- Compara una semana antes (17 a 23 ago) contra una semana despues (31 ago a 6 sep).
EXECUTE IMMEDIATE $$
DECLARE
  consulta STRING;
  resultado RESULTSET;
BEGIN
  SELECT LISTAGG(
           'SELECT ''' || table_name || ''' AS tabla, ''' || column_name || ''' AS columna, '
           || 'COUNT_IF(TRADINGDAY BETWEEN ''2026-08-17'' AND ''2026-08-23'' AND "' || column_name || '" IS NOT NULL) AS con_dato_antes, '
           || 'COUNT_IF(TRADINGDAY BETWEEN ''2026-08-31'' AND ''2026-09-06'' AND "' || column_name || '" IS NOT NULL) AS con_dato_despues '
           || 'FROM ARDM_PRODUCTION.C166_SBX."' || table_name || '" '
           || 'WHERE TRADINGDAY BETWEEN ''2026-08-17'' AND ''2026-09-06''',
           ' UNION ALL ')
    INTO :consulta
  FROM ARDM_PRODUCTION.INFORMATION_SCHEMA.COLUMNS
  WHERE table_schema = 'C166_SBX'
    AND table_name IN ('ARDM_HEADER', 'ARDM_TENDER', 'ARDM_ITEM', 'ARDM_ITEMDISCOUNT')
    AND STARTSWITH(UPPER(column_name), 'X_');
  consulta := consulta || ' ORDER BY con_dato_despues, con_dato_antes DESC';
  resultado := (EXECUTE IMMEDIATE :consulta);
  RETURN TABLE(resultado);
END;
$$;

-- CONSULTA 2. Columnas que existian en legacy y no existen en SnowTime.
SELECT l.table_name AS tabla_legacy, l.column_name AS columna_legacy, l.data_type
FROM ARDMPROD.INFORMATION_SCHEMA.COLUMNS l
LEFT JOIN ARDM_PRODUCTION.INFORMATION_SCHEMA.COLUMNS s
  ON s.table_schema = 'C166_SBX'
 AND UPPER(s.table_name) = REPLACE(UPPER(l.table_name), '_EXT', '')
 AND (UPPER(s.column_name) = UPPER(l.column_name)
      OR UPPER(s.column_name) = 'X_' || UPPER(l.column_name))
WHERE l.table_schema = 'ARDM_166'
  AND REPLACE(UPPER(l.table_name), '_EXT', '') IN ('ARDM_HEADER', 'ARDM_TENDER', 'ARDM_ITEM', 'ARDM_ITEMDISCOUNT')
  AND s.column_name IS NULL
ORDER BY 1, 2;
