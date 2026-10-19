Hola Adarsh, ¡feliz lunes! Siguiendo el nuevo proceso para escalaciones de SnowTime, te escribo por un ticket High de Starbucks NA, RCS-29205: https://trebuco.atlassian.net/browse/RCS-29205

Un work item mensual de c166_sbx no devuelve resultados desde el cutover a SnowTime del 27 ago. Ryan DeVries lo revisó y cree que algunos campos no se migraron. Comparé una semana antes del cutover con una semana después en ARDM_PRODUCTION.C166_SBX, y estos campos tenían dato antes y están vacíos después:

ARDM_TENDER.X_PARTNEROWNEDTOKEN: 631,190 filas antes, 0 después
ARDM_TENDER.X_PARTNERIDONTOKEN: 631,190 filas antes, 0 después
ARDM_HEADER.X_PAIDINPAIDOUTREASONCODE: 10,253 filas antes, 0 después
ARDM_HEADER.X_PAIDINPAIDOUTREASONENUM: 10,253 filas antes, 0 después
ARDM_TENDER.X_REFUNDTOOWN: 6 filas antes, 0 después

El work item filtra por X_PARTNEROWNEDTOKEN. ¿Podrías asignar a alguien de tu equipo para que lo revise? Cuando los campos vuelvan a llenarse, también necesitaríamos recargarlos desde el 27 ago para poder regenerar el periodo del 24 ago al 27 sep. Quedo atento a cualquier pregunta. ¡Muchas gracias!
