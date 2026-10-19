# Cosecha jim-tracker — 2026-08-28
Fuente: sesiones local_be10f332-b636-4ec8-bce8-dfc4d6b17038 y local_37fde903-51c4-4862-87ff-a65e7bf71621

## Hallazgos verificados

El tracker D9 quedó generado y verificado contra Jira. Los 42 estados coinciden uno a uno.

Conteos D8 contra D9:

| Categoría | D8 | D9 |
|---|---|---|
| Total | 39 | 42 |
| Resolved | 32 | 36 |
| Pending Ahold verification | 1 | 0 |
| Awaiting Ahold input | 0 | 1 |
| Active with Appriss | 6 | 5 |

Los cinco activos son RCS-28123, RCS-28281, RCS-28482, RCS-28535 y RCS-28596.

Tres tickets ADUSA faltaron en el D8. RCS-28588, RCS-28589 y RCS-28596 se crearon el 26 por la mañana, antes de armar el D8. El barrido del D8 solo revisó las 39 filas del tracker del lunes y nunca buscó tickets nuevos del cliente. El barrido de hoy ya filtra por reporter de dominio adusa.com.

El release de la mañana cerró dos. RCS-28021 con Jim Cosseboom confirmando el export a las 10:37, cerrado 11:22. RCS-28304 con Leigh Ann Stubbs viendo el tier completo a las 10:39, cerrado 12:47.

RCS-28093 retrocedió a Under Support Review hoy a las 09:32 sin comentario. El D8 le había dicho a Jim que estaba Pending Ahold verification. J.R. anunció el release en RCS-28021 y RCS-28304 y no lo anunció en este.

RCS-28596 tiene causa confirmada en código. El query de búsqueda de empleado hace LEFT JOIN a Store por StoreNo. En Delhaize la tienda solo es única por Division más StoreNo. El mismo arreglo ya se aplicó para Lux, quitando el join en `EELookupList.aspx.vb`.

RCS-28093 comparte esa raíz y no comparte el arreglo. RCS-28596 es código del lado de Appriss. RCS-28093 depende de que ADUSA pueble la posición 20 de `DA_Employee_Info.dat`.

RCS-28281 cambió de contenido sin cambiar de categoría. Entró un contacto nuevo, Rodney Cummings, porque Jacquelyn está de vacaciones. ADUSA sostiene que los faltantes del 8/22 y del 8/27 son internos de Appriss y trae referencias RTS. Piden revisar la data en bloques de 10 minutos para decidir qué lotes reenviar. Ayesha lo escaló a L2 mencionando a Juan.

Los conteos prometidos en RCS-28281 no se publicaron. Es la segunda vez en ese ticket. Las promesas del 19 y del 26 de agosto las hizo Juan en su nombre.

RCS-28281 contradice por escrito lo que Appriss afirmó el 19 de agosto, cuando se le dijo a Jacquelyn que el faltante restante era data que nunca llegó a Appriss.

## Decisiones y compromisos

RCS-28093 va al tracker como Awaiting Ahold input, no como Active with Appriss. La leyenda define esa categoría como Appriss necesita información o acción de Ahold para continuar. El estado correcto en Jira es Under Customer Review, no Under Support Review.

Tratar RCS-28093 y RCS-28596 por separado. Juntarlos amarra el que está listo para arreglarse al que espera datos del cliente.

RCS-28482 no necesita respuesta. Jim solo acusó recibo.

RCS-28535 no lleva registro de avance. No se ha probado y el cliente no responde.

RCS-28281 lo trabaja Nikita. Se entregaron dos piezas: el comentario al cliente para que lo publique ella y el traspaso interno. El saludo va dirigido a Rodney. El comentario abre con la corrección de lo afirmado el 19 de agosto.

El comentario de RCS-28281 no sale sin los conteos pegados. Es el tercer mensaje sobre el mismo tema y los dos anteriores prometieron conteos sin traerlos.

Tema nuevo en el tracker, "Store file and location data", para RCS-28588 y RCS-28589.

Awaiting Ahold input recibe color propio en el D9, un morado. La categoría existía en la leyenda desde el D6 y nunca se había usado.

## Pendiente de verificar

Estado real de RTS-205639 y RTS-206582. Que el del 8/27 esté resuelto viene de la lectura de Rodney, no de una lectura de Appriss.

Conteos con Anil P. Los produjo el 11 de agosto.

Si los conteos no salen hoy, decirle al cliente quién los va a publicar.

La fila de RCS-28021 en el D9 lleva notas de export de producción tomadas del comentario interno de ingeniería: los reportes grandes pueden pasar de 30 segundos a Excel, el PDF de un reporte grande puede dar timeout, y un export de más de tres minutos hay que enviarlo a Appriss. Decidir si va al cliente.

La sesión local_37fde903 se detuvo antes de analizar el tracker adjunto y el correo del lunes. No aportó hallazgos.
