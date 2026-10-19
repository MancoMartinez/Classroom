Hola Ryan, gracias de nuevo por compartir el branch. Lo revisé y el enfoque del acumulador tiene mucho sentido, siguiendo el precedente de c179_kny. Tengo algunas preguntas, y puede que esté leyendo mal algo:

1. Anushka mencionó que una reconstrucción desde el historial de ardm_customer llegaba a cerca del 44% a 6 meses. Tu seed va desde 2020. ¿Valdría la pena comparar notas con ella para quedar en un solo enfoque?
2. El seed lee ARDM_PRODUCTION.C166_SBX desde 2020, mientras que las notas describen el historial completo en ARDMPROD.ARDM_166. ¿C166_SBX tiene ese historial completo, o los años anteriores saldrían de ARDM_166?
3. Las filas de ARDM_TENDER ya cargadas desde el 27 ago seguirían en NULL. ¿Un REBUILD_RANGE desde el 27 ago después del seed sería la forma de llenarlas, para poder regenerar los work items del 24 ago al 27 sep?
4. El enrichment devuelve FALSE para tokens sin coincidencia, donde pyardm los dejaba en NULL. ¿Ese cambio podría afectar otras búsquedas?
5. El branch cubre los dos campos de token. ¿Los campos de razón de paid in y paid out irían en un cambio aparte?

¡Muchas gracias por todo el trabajo en esto!
