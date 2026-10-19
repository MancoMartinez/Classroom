# RCS-29126 Pasos para Enrique

Actualizado 30 sep 2026 con la lectura del PDF de Manage Attachments del caso 2026-150020-1.

## Lo que ya revisamos del PDF

Archivo: `2026-150020-1-Investigation Notes-Ray Nichols.pdf`, 6 páginas.

1. El sistema no generó ese PDF. Los metadatos dicen Author Mike Croze, Creator Microsoft Word. Mike escribió sus notas en Word y pegó capturas.
2. Adentro hay capturas de resultados de búsqueda de Secure. Una grilla por tarjeta con Store No, Tender Card Number, Sum of Tender Amount y Unique Count of Transaction ID. Otra lista de 7 refunds de la tarjeta 6509 en la tienda 150020. También trae recibos, frames de CCTV y una tabla de empleados.
3. Son imágenes. No son los resultados guardados en la investigación. Por eso Enrique ve "información parcial".
4. Ryan Yakow aparece en la tabla de empleados. Es el empleado 874122, Support IV, en la misma tienda TNF 20. Un caso "Ryan Yakow" sería otro caso de empleado de esa tienda, distinto al de Nichols.
5. La CreationDate del PDF, 30 sep 16:13, sale de la conversión al descargarlo. El original es un .docx subido el 26 ago.

## Corrección con el inventario de Manage Attachments de 2026-150020-1

Seis archivos. Uno llegó solo y cinco los subió Mike a mano:

| Archivo | Subida |
|---|---|
| 2026-150020-1-exported_pdf_5.pdf | 8/26/2026 11:53 AM |
| Investigation Notes-Ray Nichols.docx | 8/26/2026 1:52 PM |
| Ray Nichols Ecom.pdf | 8/26/2026 1:52 PM |
| Ray Nichols Possible POS.xlsx | 8/26/2026 1:52 PM |
| Statement Roderick Wilburn - TNF 20 - 8.25.2026.pdf | 8/26/2026 1:52 PM |
| Croze Investigators Statement for Nichols.pdf | 8/26/2026 1:52 PM |

1. `exported_pdf_5.pdf` tiene toda la pinta de ser el PDF que Secure deja al convertir. Llegó solo, a las 11:53, dos horas antes que el lote manual. El caso tiene Case Age 35, así que se creó el 26 ago por conversión. HIPÓTESIS: el "5" sería el ID de la investigación o un consecutivo.
2. El PDF que revisamos antes es el .docx de notas, convertido al descargarlo. Por eso sale Creator Microsoft Word y la fecha de hoy. Se descarta la idea de que Mike lo subió hoy.
3. La conversión del caso de Nichols del 26 ago sí dejó su PDF. Ese es el "antes" que Mike menciona. Lo que reporta es sobre las dos conversiones posteriores, alrededor del 25 sep.

## Hallazgo del 30 sep: exported_pdf_5.pdf está en blanco

Enrique lo abrió y solo trae un "#" y el logo. Es el mismo síntoma reportado en otros dos clientes:

- **ENG-6676 / RCS-28006, Casey's:** "the PDF just shows a # symbol and nothing else". ENG-6676 está Reopened desde el 29 sep, asignado a Matt Kamminga. El log del 28 sep muestra que falla la tarea Hatr `ExportGenericPageToPdfTask`. La actividad `ExportGenericPageToPdfPreCacheEventsActivity` cae por timeout de Snowflake sobre ARDM_JSON, SqlState 57014.
- **ENG-7440 / ARPP-644, Bunnings:** combined PDF en blanco en Incident tras transferir la investigación. Se cerró como duplicado de ENG-6676.

Qué significa: la conversión sí crea el caso y sí adjunta el PDF, pero el PDF sale vacío. Por eso Mike no encuentra los resultados de búsqueda. No es un error de uso. VF Corp sería el tercer cliente. HIPOTESIS fuerte hasta ver el log de VF Corp. El caso de Casey's tenía más de 900 recibos, y Mike probablemente tiene menos, así que la causa puntual podría variar.

## Paso 1. Comparar el caso de agosto con los nuevos

1. Abre `2026-150020-1-exported_pdf_5.pdf` y revisa si trae los resultados de búsqueda como tabla. Ese archivo es la referencia de una conversión que funcionó.
2. Encuentra los dos casos nuevos. Filtra Active Incidents por Created By Mike Croze y Source of Info Secure, con fecha de creación entre el 20 y el 26 sep, en todas las tiendas. 2026-150020-3 es del 28 ago, así que probablemente no es uno de ellos.
3. En cada caso nuevo abre Manage Attachments y busca un `exported_pdf_N.pdf`.

Cómo leer el resultado:

- Existe `exported_pdf_N` y trae las búsquedas: es un tema de uso. Se le muestra a Mike que los resultados quedan en ese adjunto y no en la grilla Items.
- Existe `exported_pdf_N` pero sin búsquedas, y el de Nichols sí las trae: la exportación cambió entre el 26 ago y el 25 sep. Es un defecto. Escala con los dos PDF lado a lado.
- No existe `exported_pdf_N`: la exportación no llegó al caso. Es el patrón de Bug 65080. Sigue al paso 2.

## Paso 1b. Inventario del resto de casos

Hazlo en los casos 2026-150020-3 y en los casos nuevos, impersonando a Mike.
Anota de cada archivo el nombre, quién lo subió y la fecha.
Busca un archivo que no haya subido Mike a mano, con el nombre de la investigación o del factboard y la fecha de conversión.

Si existe, ábrelo y revisa si trae las grillas de búsqueda. Si trae las grillas, es un tema de uso: se le muestra a Mike dónde quedaron.
Si no existe, la exportación de la investigación no llegó al caso. Sigue al paso 2.

## Paso 2. La investigación en Secure

1. Entra a Secure EBR impersonando a Mike desde Control Panel. Entra a Secure, no a Incident.
2. Ve a Investigator, Investigations. Cambia el filtro de estado a In Case o Completed. La lista por defecto oculta las investigaciones convertidas.
3. Ubica la de Ray Nichols y la segunda que convirtió. Anota el Factboard ID de la URL de cada una.
4. Pestaña de resultados o transacciones: confirma que las búsquedas guardadas siguen ahí con filas. Toma captura.
5. History o Activity: busca la línea de conversión a caso con número de caso y hora. Busca también "Failed to upload attachments to case". Ese es el texto de RCS-22180 y RCS-22023, Bug 65080.
6. Genera el PDF desde la investigación, con la opción de exportar o imprimir a PDF. Si también sale en blanco con "#", el defecto queda reproducido por fuera de la conversión, igual que en Casey's. Toma captura y anota la hora exacta, porque ingeniería la necesita para buscar el log.
7. Si tienes a mano la URL que genera el PDF, pruébala. En Casey's era `.../platform/factboard/<ClientID>/pdfInvestigation/<FactboardID>`. Si carga lento o da timeout, anótalo.

## Paso 3. El caso Ryan Yakow

1. En Incident, en Active Incidents, limpia todos los filtros. Tu captura muestra 22 items, así que hay un filtro o scope aplicado.
2. Busca "Yakow" en Case Name, en Subject y por número de empleado 874122. Repite en los casos cerrados y sin filtro de tienda.
3. En Secure, con el filtro In Case o Completed, busca la investigación "Ryan Yakow". Su History da el número de caso. Abre el caso por número, no por título.
4. Si la investigación dice In Case y el caso no existe en Incident, es el patrón de RCS-26453 y RCS-28898, Urban Outfitters. Escalamos con el Factboard ID y la hora.

## Paso 4. SQL, solo SELECT, si los pasos 1 a 3 no alcanzan

Primero confirma los nombres reales de columnas. El esquema legacy de lpguys puede estar en dbo y no en incident.

    SELECT TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME IN ('MasterCase','Shoplifting','Suspect')
      AND (COLUMN_NAME LIKE '%Name%' OR COLUMN_NAME LIKE '%Case%' OR COLUMN_NAME LIKE '%Created%' OR COLUMN_NAME LIKE '%Employee%');

Después, con los nombres ya ajustados, lista lo que Mike creó en septiembre:

    SELECT m.MasterCaseID, m.CaseNo, m.StoreIdent, m.CreatedDate
    FROM incident.MasterCase m
    WHERE m.CreatedBy = <UserID de Mike> AND m.CreatedDate >= '2026-09-01'
    ORDER BY m.CreatedDate;

Si no tienes acceso a la base, pásale a Juan los Factboard ID y la hora de conversión.

## Pregúntale a Mike

1. El nombre exacto de las dos investigaciones que convirtió y cuál es "el caso nuevo". ¿Es 2026-150020-3, Datta Aarya?
2. Si el PDF de notas lo subió él y cuándo.
3. Si después de convertir recibió un correo o aviso de fallo.
4. Por "search results", ¿se refiere a las búsquedas guardadas dentro de la investigación en Secure? Por ejemplo, la grilla de tarjetas con refunds.

## Qué mandarle a Juan

1. Inventario de Manage Attachments de los dos casos.
2. Factboard ID, estado y captura del History de cada investigación.
3. Si existe o no un PDF generado por Secure en el caso.
4. Resultado de la búsqueda "Yakow" y 874122.

Con eso decidimos si se lo explicamos a Mike como tema de uso o si lo escalamos como defecto de la conversión.
