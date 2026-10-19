# RCS-28671. Comparacion de NativeCommandParameters, RunId 2706EDE9

Fecha: 2026-09-04. Trabajo solo, fin de semana, sin acceso a Dan ni a Andres.

## Lo que se comparo

Dos filas del mismo RunId, ejecutadas en el mismo segundo de inicio, 12:17:26.

| | RowId 0, Ericka, store 7135 | RowId 1, store 7161 |
|---|---|---|
| Resultado | Sin eventos | Con eventos |
| ExecutionStartDateTime | 12:17:26.4033333 | 12:17:26.4033333 |
| ExecutionEndDateTime | 12:17:46.8 | 12:17:48.2266667 |
| Failed | 0 | 0 |

El texto de NativeCommandParameters es identico entre las dos filas. Solo cambian los valores de
filtro, tienda, cajero, cuenta, descripcion de jerarquia. La estructura del set de variables es
byte por byte la misma.

## Lo que dice el comando en si

DeaggregationNativeCommand, sacado de WorkItemDefinitionGenerationRequest para este RunId, es la
query que trae las transacciones puntuales:

    FROM ardm_Header AS T3
    LEFT JOIN reference_location AS T4 ...
    LEFT JOIN ardm_Tender AS T5 ...

Nombres de tabla sueltos. Sin prefijo de base de datos, sin prefijo de esquema. La query resuelve
contra lo que la sesion de Snowflake tenga activo en el USE DATABASE o el search path al momento de
ejecutar, no contra un objetivo fijo en el texto del comando.

## La conclusion

Dos ejecuciones del mismo comando, con el mismo template de parametros, en el mismo segundo de
inicio, dan resultados distintos. La unica variable que puede producir eso sin que el comando
cambie es el contexto de sesion. Si una de las dos conexiones del pool enganho el esquema previo al
corte y la otra enganho el esquema posterior, cada una ve un ARDM distinto en el mismo instante,
aunque el dato final ya estuviera completo en los dos lados segun confirmo Andres.

No es dato faltante. Es una carrera de conexion durante la ventana viva del cutover, 12:05 a 13:07
del 28 de agosto.

## Que descarta esto

**La hipotesis de Dan.** Ninguna definicion guardada esta atada a un binding viejo. El comando es
SQL generado en el momento, identico en la fila que fallo y en la que no. Resavear una busqueda no
toca esto.

**WISC como via de reparacion.** Antes de llegar a este comando, WISC revisa si el work item ya
existe para esa tienda y ese periodo. Como los 17 ya existen, WISC los salta por deduplicacion y
nunca vuelve a correr la deaggregacion que llenaria fti.Transactions. Confirmado en la prueba del
02 sep sobre el 248158, dos corridas, mismo resultado, cero cambios.

## Lo que hace falta

Una re-ejecucion de la deaggregacion, no de la generacion completa del work item. Punto a punto,
para los RunId y RowId exactos de los 17, ahora que la sesion ya no esta en la ventana del cutover.
Ese mecanismo no esta expuesto en la UI de soporte ni en WISC. Es pregunta para Engineering o para
quien administre el pool de conexiones de Snowflake durante un cutover en vivo.

## Que no se pudo hacer esta noche

Confirmar esto contra un segundo caso, EXT1, que trajo 26 work items en el mismo minuto con 19
buenos y 7 vacios. Un contraste ahi seria mas fuerte por el volumen. Pendiente para cuando haya
acceso de nuevo.

## Aviso sobre este mismo analisis, verificado

Vuelto a revisar contra el transcript crudo de la sesion anterior al corte de contexto, RunId
2706EDE9 completo. Los cuatro comandos NativeCommandParameters muestreados ahi, incluidos los de
RowId 0 y RowId 1, dicen todos FROM ardm_Header AS T#, LEFT JOIN reference_location, LEFT JOIN
ardm_Tender, sin un solo calificador de base o esquema delante del nombre de tabla. Tampoco aparece
un USE DATABASE ni un USE SCHEMA antes del comando en ese texto. DeaggregationSql sigue en NULL en
las dos filas, lo que coincide con la medicion del 02 sep sobre este mismo RunId.

La hipotesis de la carrera de sesion queda confirmada como lectura de los datos disponibles. No
queda probada contra el pool de conexiones de Snowflake mismo, eso nadie lo instrumento en el
instante del corte. Lo que si queda firme es que el comando no lleva ningun binding a una
definicion guardada, y que dos ejecuciones identicas en el mismo segundo dieron resultados
distintos. Alcanza para descartar la hipotesis de Dan con evidencia, no solo con logica.

Comentario listo para pegar el lunes en
inbox/2026-09-04-rcs-28671-comentario-mecanismo-monday.md.
