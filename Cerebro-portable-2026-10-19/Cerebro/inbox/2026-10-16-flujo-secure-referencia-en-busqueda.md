# Flujo: agregar una búsqueda de referencia a una búsqueda guardada en Secure

Creado el 16 oct 2026 a partir de RCS-29465, Williams-Sonoma. Úsalo cuando un cliente pida enlazar una referencia a su búsqueda o cuando una búsqueda con referencia dé filas vacías, filas repetidas o sumas raras. Las cifras son del 16 oct 2026. Vuelve a medir antes de citarlas.

## Orden correcto, de menor a mayor costo
1. Busca en Cerebro el síntoma y el nombre de la referencia, en español y en inglés, antes de abrir nada. En RCS-29465 el traspaso decía que no había precedente y existía RCS-29363.
2. Abre la búsqueda del cliente en el Composer. Lee Conditions, Display Fields y Expanded Display Fields. Anota la hora de la captura, porque el cliente puede editarla mientras trabajas.
3. Haz clic en References. Vacío significa que la versión guardada no usa ninguna referencia.
4. Prueba en memoria, sin Save: agrega la referencia con Add search..., elige la unión, arma el enlace y haz clic en Run.
5. Haz clic en Query en la pantalla de resultados y copia el SQL. Léelo antes de medir nada.
6. Mide en Snowflake replicando ese SQL con los mismos filtros y la misma ventana, con y sin la referencia.
7. Escribe el entregable v2 en inbox y pregunta a quien corresponda.

## Qué enseña la pantalla de Secure
- El selector de campo del enlace ofrece solo Display Fields. Expanded Display Fields no aparecen. Sum y Count tampoco, porque son agregados. Una búsqueda resumen necesita el campo llave en Display Fields, y eso cambia el agrupamiento.
- Opciones de unión: Only in la búsqueda, Only in la referencia, and, or. And genera INNER JOIN. Or genera FULL OUTER JOIN, que con filtros sobre HEADER actúa como LEFT JOIN. Si el cliente quiere conservar todas las filas, usa or.
- Los campos de la referencia salen de Add Display Field, sección Referenced Searches. La etiqueta debe llevar el nombre de la referencia. Una etiqueta EMPLOYEE es el campo base de la tabla y sale vacío.
- Los parámetros opcionales con el interruptor apagado no se aplican. La corrida cubre la ventana externa del SQL, que en WSGC fue de 13 meses.
- Una fila vacía en el enlace puede dar error o ignorarse. Bórrala antes de Accept.
- El aviso "search is referenced by the following assets" y el candado naranja con un número indican que la búsqueda se usa en otros lugares. No guardes encima.

## Snowflake
- Identifica la copia antes de medir con MIN y MAX de TRADINGDAY en ARDM_HEADER de cada copia. En WSGC, cliente 139, ARDMPROD.ARDM_139 quedó congelada el 2026-08-11 y ARDM_PRODUCTION.C139_WIL es la actual.
- En la copia SnowTime no existen las tablas _EXT. Las columnas X_ viven dentro de ARDM_HEADER y REFERENCE_EMPLOYEE. Verifica con DESC TABLE y descarga el CSV. INFORMATION_SCHEMA devolvió vacío varias veces para el mismo rol.
- Los nombres lógicos de Secure, como ardm_Header y reference_Employee, no son los físicos.
- No uses SELECT * sobre tablas de empleados o clientes. DESC TABLE y conteos bastan.
- Compara filas y suma con y sin la CTE de la referencia. Si con referencia supera, hay inflado.

## Riesgo conocido en 1b - Emp HR Info with User ID V2
La CTE hace auto join de reference_Employee por EmployeeID. Hay 609 User ID repetidos, y un reembolso de esos cajeros entra de 2 a 9 veces. Medido el 16 oct 2026 sobre 13 meses: sin referencia 4297884 filas y suma -80458795.81, con la CTE 4444633 filas y suma -123035024.88. Quien la use en un resumen con Sum o Count recibe totales inflados. El origen del auto join está sin confirmar. Se preguntó a Enrique por RCS-29363 y el PR 59321.

## Detalle
inbox/2026-10-16-rcs-29465-pasos.md y inbox/2026-10-16-rcs-29465-v2.md.
