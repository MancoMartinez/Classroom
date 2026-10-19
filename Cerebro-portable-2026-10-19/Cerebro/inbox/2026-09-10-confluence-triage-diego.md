# Corpus de triage de Confluence bajado a Cerebro

Fecha: 10 sep 2026. Origen: carpeta Triage del espacio RTS en Confluence, id 478142038021,
mantenida por Diego Buelvas. https://trebuco.atlassian.net/wiki/spaces/RTS/folder/478142038021

## Qué se trajo

46 fichas, 412KB, a `confluence/RTS-triage/`. Una por ticket, no son procesos genéricos. Cada una
sigue el mismo formato de 10 secciones: detalles del ticket, problema, perfil del cliente,
investigación paso a paso marcando PASS y POINT OF FAILURE, causa raíz en tabla, hallazgos
adicionales, fix recomendado con opciones y cuál se aplicó, preguntas abiertas, queries corridas
con su resultado, extras.

Cada archivo lleva frontmatter con ticket, cliente, analista, estado, síntoma en una línea, causa
en una línea, fix, familia de falla cuando aplica, tickets relacionados, id de Confluence y fecha.
El frontmatter es lo que alimenta el índice.

Autores: 42 de Diego Buelvas, 1 de Sebastian Rueda (RCS-28873), 1 de Matthew Kamminga (RCS-28105),
1 de Vismaya Thottada (RTS-206639), 1 de Ayesha Mehar (RTS-205543).

Dos tickets tienen dos versiones de ficha, las dos se guardaron: RCS-28510 (v1 del 21 ago con el fix
propuesto, v2 del 28 ago con el fix ya aplicado y validado) y RCS-28105 (v1 de Diego el 4 ago, v2 de
Kamminga el 5 ago).

## Qué se agregó al proyecto

- `confluence/RTS-triage/` con las 46 fichas más `INDICE.md`.
- `bin/traer_confluence.py` con dos modos. `indice` rehace INDICE.md leyendo el frontmatter de los
  archivos locales, sin red. `bajar` refresca desde la API de Confluence y solo reescribe la ficha
  si la versión en Confluence subió; necesita CONFLUENCE_BASE, CONFLUENCE_USER y CONFLUENCE_TOKEN
  en el entorno, y html2text instalado para una conversión limpia a markdown.
- Sección nueva al final de `investigaciones/INDICE.md` apuntando al corpus y a las familias.

## Familias de falla que ya se repiten entre clientes

Rename de columnas ARDM v1 a v2 sin resync del catálogo de campos de Secure. Cuatro clientes:
RCS-28606 Williams Sonoma con TENDERTYPEGROUP, RTS-206667 Home Depot con el mismo campo, RTS-206610
Floor&Decor con CUSTOMERNUMBER a X_CUSTOMERNUMBER, RTS-206268 Kinney con POS_ARTICLEID. La conclusión
de Diego es que se escale agrupado como un solo resync de metadata, no parche por parche. En
RTS-206268 editar el campo desde Composer empeoró el fallo de 3 de 30 a 11 de 30.

Binding de campo por posición o etiqueta que queda obsoleto al editar. RCS-28843 Nordstrom pinpointea
la línea que revienta, ChartFormatter.GetDescriptionValue sin manejo defensivo. RCS-28841 Casey's y
RTS-206261 WinCo son el mismo mecanismo. El workaround estable es borrar y recrear el campo calculado.

Campo del Synopsis ausente de los Display Fields. RTS-205361 Walmart y RTS-205224 Burlington. El motor
valida contra los Display Fields, agregar el campo oculto basta y no se puede volver a quitar.

Duplicados por join sin dedup aguas arriba. RCS-28077 AHL con REFERENCE_PRODUCT 6 veces por ArticleID,
RCS-28751 Loblaw con el export en 5 partes sin collapse, RCS-28746 TG Jones sin protección
anti cartesiana al sumar un campo de tender.

## Notas sueltas que sirven para cualquier ticket

El chequeo Go No Go de Work Items avanza día por día y se traba en el primer día sin marcador de carga
(RCS-28632 NAPA), o cuando el conteo del día queda bajo el mínimo configurado (RCS-28170 TJX).

Los códigos de abandon reason de Work View no son tabla SQL, salen de un Excel por tenant; hay que
resolver el ID antes de ejecutar (RCS-28750 Starbucks).

Las búsquedas del Composer sobre datos ARDM son federadas, Snowflake más SQL Server; el SQL de
preview no corre tal cual contra un solo motor (RCS-28834 ICA).

En RAW_DATA de raw_receipt el POSLog viene Base64 dentro del JSON; un CONTAINS directo da falso
negativo (RCS-28838 ICA).

Snowflake guarda un hijo XML único como OBJECT, y LATERAL FLATTEN sobre OBJECT expande pares clave
valor, no hijos, así que el filtro nunca hace match (RCS-28052 TJXEU).

Nunca agregar una DEFAULT partition a una tabla de Greenplum manejada por generate_*_partitions()
(RTS-205543 Lululemon).

## Qué falta decidir

Si se ingiere todo el corpus a la base o solo este resumen. Son 412KB de texto; ingerir las 46 fichas
completas mete mucho detalle de un solo cliente a la base general. La recomendación es ingerir esta
nota y dejar las fichas como corpus buscable con grep, que ya es lo que hace bin/buscar sobre
markdown.

## Enganches para que el corpus se consulte solo

Hecho el mismo día, después de bajar las fichas:

- `bin/buscar` ahora incluye `confluence/RTS-triage` como sexta fuente, sección TRIAGE CONFLUENCE.
  Backup del original en `bin/buscar.bak-20260910`. Probado con `bin/buscar tendertypegroup`.
- `MAPA.md` tiene la ruta en la tabla de entrada y en la capa 3. Backup en `MAPA.md.bak-20260910`.
- `CLAUDE.md` tiene la ruta en "por dónde entrar" y en "dónde está cada cosa", más la regla de uso:
  el corpus se cita como precedente, no reemplaza la evidencia del ticket propio.
  Backup en `CLAUDE.md.bak-20260910`.
- `investigaciones/INDICE.md` cierra con la sección del corpus y las cuatro familias.

Lo que no quedó automático: las skills `cerebro-ticket`, `cerebro-comentario` y
`cerebro-respuesta-cliente` no nombran la carpeta. Alcanzan el corpus igual porque ya mandan a
`investigaciones/INDICE.md` y a `bin/buscar`, que ahora lo cubren. Si se quiere que lo nombren
explícito hay que editar las skills, no los archivos de la carpeta.

## Actualización de skills, propuesta el mismo día

Dos skills se propusieron con el corpus adentro. Juan las revisa y guarda desde la tarjeta.

`cerebro-ticket`. El corpus entra en tres puntos. En la carpeta obligatoria, como tercera cosa que
se pierde si falta. En el orden de búsqueda, después de flujos y antes de bin/buscar, con una
sección nueva que fija la regla: la ficha ajena es hipótesis con buen antecedente, no evidencia, y
la causa no se marca CONFIRMADA sin verificar en el ticket propio. En el bloque Precedentes del
entregable, con formato de cita que incluye ticket original y cliente. Se agregó también el paso de
sumar el ticket a su familia en investigaciones/INDICE.md cuando la confirme.

`cerebro-comentario`. El corpus entra como fuente para verificar la ruta de escalación, porque las
fichas dicen a qué equipo se mandó cada defecto y con qué argumento, y varias concluyen Delivery
donde el instinto dice Engineering. Se agregó una sección para escalar agrupado cuando el mismo
defecto ya tocó a tres o más clientes, con el ejemplo de las cuatro fichas del catálogo
desincronizado. En Findings, separar lo probado en el tenant propio de lo que viene de precedente.
En el formato al cliente, prohibición explícita de nombrar otro tenant o citar una ficha.

Sin tocar: `cerebro-respuesta-cliente` no necesita el corpus, el cliente nunca recibe hallazgos de
investigación ni precedentes de otros tenants. `cerebro-cola` y `cerebro-asignacion` trabajan sobre
la cola, no investigan síntomas.
