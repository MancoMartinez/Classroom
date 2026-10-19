# SBX work items, estado 5 oct 2026

RCS-29207. Ryan DeVries, 2 oct 13:15: contactar a Carl Costelow, el search se rompio cuando alguien de su equipo cambio el tipo del campo. Borrar y volver a agregar la columna no lo arreglo. Juan escribio a Carl el 2 oct 13:42. Carl, 5 oct 5:24: "Hey, sure. Please post things like this in the Delivery Chat going forward". Ruta: Carl Costelow, Delivery Secure 5, Under Delivery Review. Si Carl dice que es codigo, Engineering con Shandana Khan.
RCS-29205. Ryan, 2 oct 15:59: "they either forgot or didn't migrate some fields to Snowtime". Propone reunion con el equipo de soporte para trabajar el ticket y repasar el flujo de backend issues. Antes dijo que campos o feeds faltantes necesitan al equipo de SnowTime. Ticket sigue a nombre de Juan.
Regla nueva: pedidos a Delivery van por el canal "Delivery Chat" de Teams, no por chat directo. Carl Costelow, 5 oct.
Archivos 5 oct: comentario interno y respuesta a Manish por ticket, Teams a Carl y a Ryan.
Pendiente: Juan crea el invite de la reunion con Ryan.

Ryan, 5 oct 9:28: Juan agenda con el Scheduling Assistant de Outlook. Ryan trabaja de 9 a 5 PM EST, flexible. Reunion con el equipo de soporte para trabajar RCS-29205 y repasar el flujo de backend issues.

RCS-29207, 5 oct: Carl Costelow "It's fixed now. Do you want to go back to customer?". Pendiente: verificar en Snowflake y Executive Workbench que el periodo 24 ago a 27 sep tiene items antes de avisar a Manish. El fix no toca RCS-29205, causa distinta, campo no migrado a SnowTime. RCS-29206 sin defecto, cero real, esperando a Manish.

Plan 5 oct para no esperar la reunion. RCS-29205: Juan corre la comparacion de columnas X_ antes y despues del cutover para tener la lista de campos no migrados, y le pregunta a Ryan quien del equipo SnowTime entra. Respuesta a Manish del dia ya redactada. RCS-29206: Under Customer Review desde el 1 oct, seguimiento amable a Manish. La lista de campos sirve de control cruzado: si aparece un campo de la regla de 29206, se reabre esa conclusion.

RCS-29205: nadie tiene asignado el arreglo. Ryan solo corrige errores de mapeo; campos no migrados requieren al equipo de SnowTime (Ryan, 2 oct 12:34). Se le pregunta a Ryan si el los suma o Juan contacta, y a quien.

Ruta SnowTime nueva, anuncio al equipo de soporte 5 oct: todo ticket que se escale a SnowTime va primero a Adarsh Kumar por Teams, el asigna un recurso. Responder rapido a sus pedidos de informacion. Guia de troubleshooting de SnowTime prometida para el fin de esa semana; migraciones SnowTime deben cerrar a fin de octubre.
RCS-29205: Teams a Adarsh pidiendo recurso. Aviso a Ryan. El mensaje a Ryan preguntando quien de SnowTime queda obsoleto.

Resultado comparacion de campos C166_SBX, 5 oct, semana 17 a 23 ago contra 31 ago a 6 sep:
En cero despues del cutover: ARDM_TENDER.X_PARTNEROWNEDTOKEN 631190 a 0, X_PARTNERIDONTOKEN 631190 a 0, ARDM_HEADER.X_PAIDINPAIDOUTREASONCODE 10253 a 0, X_PAIDINPAIDOUTREASONENUM 10253 a 0, ARDM_TENDER.X_REFUNDTOOWN 6 a 0. Los otros 32 X_ estables.
Dato aparte: ARDM_HEADER.X_POSTVOIDNOTRERUNG paso de 10.9M a 57.2M filas con dato, cambio de comportamiento, no faltante.
Columnas legacy sin equivalente en SnowTime: CHECKPOINTID en todas, ARDM_HEADER COMPLETEDNONVOIDCUSTTXNFLG NEXTTRANSAMOUNT PREVIOUSTRANSAMOUNT, ARDM_ITEMDISCOUNT CARDTOKEN STAFFID VALUECHANGEREASON, ARDM_TENDER TENDERTYPEGROUP. CARDNUMBERMASKED es falso positivo, existe como X_CARDNUMBERMASK.
RCS-29206 se sostiene: X_RECEIVINGPARTNERID estable, y la trigger search corre sin error, asi que no usa columnas inexistentes.
