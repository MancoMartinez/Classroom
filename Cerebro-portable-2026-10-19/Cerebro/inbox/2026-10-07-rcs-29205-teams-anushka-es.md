Hola Anushka, ¡mucho gusto! Adarsh me contó que eres la ingeniera de SBX, así que abro este chat con él incluido. Gracias por ayudar con este caso.

El ticket es RCS-29205, un High de Starbucks NA: https://trebuco.atlassian.net/browse/RCS-29205

Un work item mensual de refunds de c166_sbx no devuelve resultados desde el cutover a SnowTime del 27 ago. Comparé una semana antes del cutover con una semana después en ARDM_PRODUCTION.C166_SBX, y estos campos tenían dato antes y están vacíos después:

ARDM_TENDER.X_PARTNEROWNEDTOKEN: 631,190 filas antes, 0 después
ARDM_TENDER.X_PARTNERIDONTOKEN: 631,190 filas antes, 0 después
ARDM_HEADER.X_PAIDINPAIDOUTREASONCODE: 10,253 filas antes, 0 después
ARDM_HEADER.X_PAIDINPAIDOUTREASONENUM: 10,253 filas antes, 0 después
ARDM_TENDER.X_REFUNDTOOWN: 6 filas antes, 0 después

Los otros 32 campos X_ de esas tablas mantuvieron su volumen. El work item filtra por X_PARTNEROWNEDTOKEN, así que su búsqueda devuelve 0 filas sin error.

¿Podrías revisar el mapeo de estos campos? Cuando vuelvan a llenarse, también necesitaríamos recargarlos desde el 27 ago para poder regenerar el periodo del 24 ago al 27 sep. ¿Quieres que te asigne el ticket? La consulta que usé y las notas completas están en el ticket, y con gusto hacemos una llamada cuando quieras. ¡Muchas gracias!
