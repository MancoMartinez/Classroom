# Qué cambió desde el D9, y estado de la cola completa

Fecha: viernes 28 ago 2026, 12:05 ET aprox. Verificada con `date`.
Baseline: Appriss ADUSA-Support-Tracker - 08272026 D9.xlsx, estado del 27 ago 19:10.
Barrido: los 42 tickets del D9, más búsqueda de tickets nuevos por los cuatro reporters de ADUSA y por
palabra clave en el asunto.

## Sobre los tres tickets de la llamada

RCS-28588, RCS-28589 y RCS-28596 sí están en el informe. Faltaron en el D8 del miércoles y entraron al D9 del
jueves, que es el que enviaste. Los dos primeros bajo el tema nuevo Store file and location data, y RCS-28596
en Store and brand restrictions junto a RCS-28093.

Para la reunión, la respuesta es que ya están y que el hueco fue del método de barrido, no de los tickets. El
barrido del miércoles solo revisó las 39 filas del tracker del lunes. Desde el jueves busca tickets nuevos por
reporter de ADUSA, y hoy además por palabra clave en el asunto.

## Tickets nuevos desde el 27

Ninguno. La búsqueda por los cuatro reporters de ADUSA y por asunto no devuelve nada creado después del 26.

## Cambios desde el D9. Tres, ninguno de categoría

RCS-28596 pasó de Under Engineering Review a Accepted into Development hoy 08:25. Sigue Active with Appriss.
Ingeniería aceptó el trabajo con el diagnóstico de Ryan Barlow, quitar el join a Store en
Popups/EELookupList.aspx.vb como ya se hizo para Lux.

RCS-28093 pasó de Under Support Review a Work in progress hoy 06:46. Sigue Awaiting Ahold input. Leigh Ann
respondió a las 06:46: no sabe qué implica poblar la posición 20 y copió a April Valerio para ver si es
posible. La pelota sigue del lado de ADUSA.

RCS-28281 es el cambio que importa, y es a favor.

## RCS-28281. Los conteos que debías ya salieron

Appriss Retail Support envió la tabla completa por día de operación al cliente el 27 de agosto a la 1:00 PM,
por el hilo de RTS-205639. Ayesha Mehar la citó dentro de RCS-28281 a las 18:08. La deuda que arrastrabas desde
el 19 está saldada, y no la saldaste tú.

Lo que muestra la tabla. 8/10 quedó en 2,021,502 transacciones sobre 727 tiendas, contra el 1,066,691 del
reporte original. Ese día ya está normal. Los días que siguen bajos son 8/11, 8/12, 8/19, 8/20, 8/22 y 8/25.
El más bajo es 8/22 con 1,479,909.

Lo que trae Rodney Cummings el 28 a las 02:27. Los conteos por file mask van a salir bajos en los días con
problemas de transmisión, porque esa data se envía en días posteriores y esos días quedan con conteo más alto
de lo normal. Becky revisó el 20 de agosto de 6 a 8 PM y encontró al menos una transacción por minuto.

La petición abierta. Escanear en bloques de 10 minutos donde haya huecos, para que ADUSA determine qué lotes
reenviar. Ayesha lo escaló al equipo L2, te mencionó a ti y a Nikita, y acusó recibo al cliente el 27 a las
18:45. Nadie de L2 ha respondido si ese análisis se puede correr.

Esa es la única acción viva del ticket. Ya no son los conteos.

## Estado de la cola y quién responde

Seis abiertos. Cuarenta y dos en total.

RCS-28093, Juan Martinez, Awaiting Ahold input. April Valerio evalúa si el feed puede poblar la posición 20.
Nada que hacer de tu lado hasta que respondan.

RCS-28123, Juan Martinez, Active with Appriss. Le dijiste a Jim el 26 que ingeniería estaba revisando la
ventana de confirmación y que lo actualizarías. Dos días sin movimiento en el ticket.

RCS-28281, Nikita Rathore, Active with Appriss. Comunica Ayesha Mehar. Contacto del cliente, Rodney Cummings.
Pendiente que L2 diga si el análisis por bloques de 10 minutos se puede hacer.

RCS-28482, Juan Martinez, Active with Appriss. Tab MISC. Dos días sin movimiento.

RCS-28535, Edwin Garzon, Active with Appriss. Forbidden al subir. Dos días sin movimiento y con un cliente que
ya entregó el diagnóstico de duración el 24.

RCS-28596, Shandana Khan, Active with Appriss. Aceptado a desarrollo hoy.

## Conteos del D10

Idénticos a los del D9. Total 42, resueltos 36, pending Ahold verification 0, awaiting Ahold input 1,
active with Appriss 5.

Ningún ticket cambió de categoría, así que la tabla resumen no se mueve. Lo que cambia es el contenido de tres
filas: RCS-28281, RCS-28093 y RCS-28596.

## Antes de enviar

Nada bloquea la generación del documento. Los estados de Jira y las categorías del tracker son coherentes.

Dos tickets llevan dos días en silencio y los dos son tuyos, RCS-28123 y RCS-28482. RCS-28535 lleva dos días y
es de Edwin. Si el documento sale así, esas tres filas le dicen a la sala que Appriss no reporta nada desde el
miércoles.

## Conocimiento

El anuncio de p-ingest y GP11 ya está en la base, chunk 1706 en Appriss KT Topic 1. No hay que volver a
guardarlo. Para tus tickets de ADUSA el punto práctico es que Delhaize es 046 DHZ en GP11 y sus archivos van al
share nuevo, mientras Ahold es 112 AHL en GP9 y sigue en p-ingest.
