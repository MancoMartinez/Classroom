# Qué cambió desde el D8, verificado contra Jira

Fecha: jueves 27 ago 2026, 17:50 ET aprox. Verificada con `date`.
Baseline: Appriss ADUSA-Support-Tracker - 08262026 D8.xlsx, estado del 26 ago 19:10.
Barrido: los 39 tickets del D8, más búsqueda de tickets nuevos por reporter @adusa.com.

## Primero, lo que se me pasó ayer

Tres tickets ADUSA creados el 26 de agosto por la mañana no entraron al D8.

RCS-28588, Store numbers should be 4 digits. Leigh Ann, 26 ago 07:06.
RCS-28589, Store file showing invalid characters before numeric value. Leigh Ann, 26 ago 08:23.
RCS-28596, Employees Duplicated in a View. Jim, 26 ago 11:34.

Los tres existían horas antes de que armara el documento. Verifiqué solo las 39 filas del tracker del lunes y
nunca barrí tickets nuevos del cliente. El barrido de hoy ya incluye búsqueda por reporter, así que no se repite.

## Cerrados hoy por el release de la mañana

RCS-28021, Izenda export. J.R. avisó del release a las 09:30. Jim confirmó a las 10:37 que varios usuarios
probaron y funciona correctamente. Cerrado 11:22 como Customer Resolved.

RCS-28304, case tier truncado. El cambio llegó a producción, Leigh Ann confirmó a las 10:39 que ve el tier
completo y lo llamó cosmético. Cerrado 12:47 como Engineer Resolved, Hot Fix Provided.

Hay una nota interna de Jack Chen en 28021 que vale una decisión tuya. En producción los exports a CSV, Excel,
DOC y XML corren más rápido que PDF, los reportes grandes pueden pasar de 30 segundos en Excel, el PDF de un
reporte grande puede dar timeout, y si algún export pasa de 3 minutos hay que pasarlo a Appriss para tratarlo
uno por uno. Eso es guía operativa que le sirve al usuario. Decide si se la comunicas o si se queda interna.

## Retroceso de estado sin comentario

RCS-28093 pasó de Under Customer Review a Under Support Review hoy a las 09:32. Sin ningún comentario.

Eso deja tres problemas. El D8 le dijo a Jim que estaba Pending Ahold verification. J.R. anunció el release en
28021 y en 28304 y no en este. Y le sigues debiendo a Leigh Ann el campo equivalente del employee feed desde el
26. Resuelve el estado y el comentario antes de generar el D9.

## RCS-28281. El que más se movió y el que peor está

Contacto nuevo del lado ADUSA, Rodney Cummings. Jacquelyn Wunders está de vacaciones esta semana.

Rodney escribió a las 17:44. ADUSA sostiene que los faltantes del 8/22 y del 8/27 son internos de Appriss, con
RTS-205639 y RTS-206582 como referencia. El del 8/27 ya se resolvió.

Becky revisó el 20 de agosto entre 6 y 8 PM y encontró al menos una transacción por minuto en esos intervalos.
ADUSA pide revisar la data en bloques de 10 minutos para ubicar los huecos y decidir qué lotes reenviar. Ayesha
Mehar lo escaló al equipo L2 a las 18:08 y te mencionó.

Ayer prometiste publicar los conteos por día de operación hoy. No se publicaron. Es la segunda promesa
incumplida en ese ticket y ahora el cliente llega con datos propios y con una petición técnica concreta. Ese es
el ticket que hay que atender antes de cualquier otra cosa.

## Confirmación del cliente sin respuesta

RCS-28482. Jim respondió ayer 19:29: "You are correct, the report is running correctly, it just isn't editable."
Veintidós horas sin respuesta. Todavía dentro de las 24 y por poco.

## Sin movimiento

RCS-28535. Nada desde ayer 19:06. La investigación del upload sigue sin avance registrado en Jira.

RCS-28196 solo tuvo ruido interno de ingeniería. Sigue cerrado y no cambia nada para el cliente.

## Los tres nuevos, qué dicen

RCS-28588. 899 ubicaciones de tres dígitos entraron por el archivo de ubicaciones del 26 de agosto. Ryan Barlow
las inactivó y las renombró a DELETE, pidió mover cuatro casos que colgaban de ellas, Leigh Ann los movió, y
Ryan cambió el job de carga a UPDATEONLY. La automatización ya no crea ubicaciones nuevas. Eso responde también
el pedido de Jim de restaurar el comportamiento previo. Completed 11:16.

RCS-28589. El archivo de ubicaciones traía apóstrofes antes del valor numérico de Longitude, campo que aparece
como EASFrequency en el archivo. Ryan quitó los apóstrofes de 432 registros y agregó una regla que los ignora en
EASFrequency y CCTVIPAddress. Los apóstrofes llegan en el archivo que ADUSA envía. Completed 12:14.

RCS-28596. La búsqueda de empleado dentro del caso devuelve cada empleado dos veces. La tabla de administración
los muestra una sola vez. Causa confirmada en código y no en datos. El query hace LEFT JOIN de Employee a Store
por StoreNo, y en Delhaize la tienda solo es única por Division más StoreNo, así que un empleado cruza con varias
filas de Store. El mismo problema se arregló para Lux quitando el join. Archivo Popups/EELookupList.aspx.vb.
Under Engineering Review, Shandana Khan.

Atención al parentesco. RCS-28596 y RCS-28093 son el mismo problema de fondo, la numeración de tienda que solo
es única por división, visto desde dos pantallas. Decide si el D9 los presenta juntos o si el hallazgo de 28596
te sirve para cerrar 28093.

## Conteos que mostraría el D9

Total 42, contra 39 en el D8. Resueltos 36. Pending Ahold verification 0. Awaiting Ahold input 0.
Active with Appriss 6.

Los seis activos: RCS-28093, RCS-28123, RCS-28281, RCS-28482, RCS-28535, RCS-28596.

Propongo un tema nuevo, Store file and location data, para RCS-28588 y RCS-28589. RCS-28596 entra en Store and
brand restrictions junto a RCS-28093, que es el mismo problema.

## Qué hay que resolver antes de generar el D9

1. RCS-28281. Publicar los conteos y responder la petición de bloques de 10 minutos.
2. RCS-28093. Corregir el estado y entregarle a Leigh Ann el campo del employee feed.
3. RCS-28482. Contestarle a Jim su confirmación de ayer.
4. RCS-28535. Registrar avance de la investigación o decir que no hay.
5. Decidir si 28596 y 28093 se trabajan como uno.

Avísame cuáles vas a atender y redacto los comentarios con las reglas de cerebro-respuesta-cliente.
