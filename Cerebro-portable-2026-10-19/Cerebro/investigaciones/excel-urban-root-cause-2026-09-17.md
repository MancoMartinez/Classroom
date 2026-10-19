# Exportación Excel de Urban: causas y plan de verificación

Investigación del 17 de septiembre de 2026. Cliente 44, Urban Outfitters, Secure 5 EBR. Jira marca los tres tickets Closed. Consulta Jira, Confluence, Cerebro, adjuntos originales y Azure DevOps. Todas las operaciones externas fueron de lectura.

## Dictamen

| Ticket | Conclusión técnica | Grado de evidencia |
| --- | --- | --- |
| RCS-26238 | Dos DisplayField de texto declarados System.Double provocan celdas vacías al escribir Excel. El fix cambia ambos a System.String. | Confirmado por diagnóstico de SRE, diff de PR y validación del cliente en QA. Producción comunicada, sin confirmación posterior del cliente. |
| RCS-23141 | Mismos campos y búsqueda que RCS-26238. El repositorio conserva esos tipos incorrectos durante septiembre de 2025. | Hipótesis causal de alta confianza, respaldada por captura y cadena de commits. Falta snapshot de configuración efectiva de aquella ejecución para cerrar la atribución histórica. |
| RCS-28339 | Otra búsqueda muestra ocho filas y notifica exportación terminada con cero resultados. | Síntoma confirmado. Causa no determinada. Investigar equivalencia entre request interactivo y export asíncrono antes de cambiar datos o configuración. |

La agrupación “Excel export intermittently failing or missing fields” mezcla dos mecanismos. Los campos vacíos tienen un defecto de configuración reproducible; la exportación de cero filas requiere investigación propia. No hay evidencia de una causa común para los tres.

## 1. Campos vacíos: mecanismo, origen y corrección

Archivo: `repo/44/system/ebr/smarttracksearches/sametendercard.search`.

| Campo | Tipo defectuoso | Tipo correcto | Línea del diff 51987 |
| --- | --- | --- | --- |
| tender_accountnumber | System.Double | System.String | 77 |
| customer_customerfullname | System.Double | System.String | 82 |

Mulrenan explica que la grilla renderiza los valores como texto y el escritor Excel usa el tipo declarado para convertirlos. Tokens alfanuméricos y nombres no se convierten a Double, por lo que el export deja celdas vacías. El dato existe aguas arriba. El [comentario 3075525 del 6 de abril](https://trebuco.atlassian.net/browse/RCS-26238?focusedCommentId=3075525) identifica el archivo y compara con clientes 57 y 138. El [PR 51987](https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/arpfiles/pullrequest/51987?_a=files) confirma exactamente ese cambio, sin modificación de SQL ni de carga de datos.

Inspeccioné el Excel original, adjunto 1315787. Hoja SearchResults: 348 filas de datos, diez columnas. I1 y J1 contienen Account Number y Customer Full Name; I2:J349 está vacío. Las columnas existen. La formulación de BJ sobre columnas faltantes describe el síntoma de manera imprecisa. El archivo y el conteo están en `evidencia-excel-urban-2026-09-17/1315787.xlsx` y `excel-inspeccion.json`.

La captura 1184025 de RCS-23141 muestra Same Tender Card con seis resultados. Excel conserva las seis filas y los encabezados; pierde el token de cuenta de las filas y el nombre que sí aparece en una fila de la grilla. No exigir nombres en todas las filas: varias ya estaban vacías en pantalla. La prueba correcta compara por transacción y conserva los nulos de origen.

### Cadena de cambios comprobada

| Cambio leído directamente | Qué demuestra |
| --- | --- |
| [PR 40748](https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/arpfiles/pullrequest/40748?_a=files), 14 mayo 2025; commit b66d94712b0b48d445532317401646bf29329c4f | Agrega el archivo de Urban con ambos DisplayField como Double. Su objetivo era corregir el paso del número de cuenta desde el recibo. |
| [PR 43459](https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/arpfiles/pullrequest/43459?_a=files), 11 agosto 2025; commit 07400fc5fe89ca7e5292e2b930315b7bb69ca424 | Revierte nombre de parámetro y variable a cardno y ajusta el enlace del recibo. Deja intactos los tipos defectuosos. |
| [Historial del archivo en main](https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/arpfiles?path=/repo/44/system/ebr/smarttracksearches/sametendercard.search&version=GBmain&_a=history) | Muestra esas dos entradas y la corrección de mayo de 2026. El repositorio conservó el defecto durante los dos reportes. |
| [PR 51987](https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/arpfiles/pullrequest/51987), 10 mayo 2026; commit b9e76df95c3c08c6a175dc818f435584a2173ffa | Cambia dos líneas a String en main. |
| [PR 52242](https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/arpfiles/pullrequest/52242), 13 mayo 2026 | Lleva ese commit a release como hotfix y registra prueba en Staging y aprobación de QA. |

No atribuir la introducción en producción al 14 de mayo de 2025. El [comentario 2685220 de RCS-19380](https://trebuco.atlassian.net/browse/RCS-19380?focusedCommentId=2685220), del 2 de mayo, ya documenta diferencias entre QA y producción, incluidos los campos personalizados. El primer commit visible podría haber incorporado una definición que ya existía en producción. El origen exacto exige auditoría de la definición previa y del despliegue.

### Por qué pudo escapar

Inferencia respaldada por el alcance del PR: el arreglo original y su validación se centraban en abrir SmartTrack con la cuenta precargada. Su descripción enumera pruebas en Delivery y Event Viewer, sin evidenciar una comparación del archivo Excel. En agosto el equipo corrigió otra ruta del enlace. El [comentario 2801308 de RCS-19380](https://trebuco.atlassian.net/browse/RCS-19380?focusedCommentId=2801308) reconoce que el primer arreglo cubría receipt view y faltaba links view. La matriz futura debe cubrir ambos accesos y validar el contenido descargado.

El [comentario 2850522 de RCS-23141](https://trebuco.atlassian.net/browse/RCS-23141?focusedCommentId=2850522), del 22 de septiembre de 2025, informa purga de caché y actualización de versión. No identifica un cambio del XML ni una validación exitosa del cliente. Purgar caché vuelve a cargar una definición; no corrige su tipo. No presentar esa intervención como causa raíz ni como arreglo probado.

En RCS-26238 el cliente confirma QA el [7 de mayo, comentario 3122195](https://trebuco.atlassian.net/browse/RCS-26238?focusedCommentId=3122195). Smeet comunica producción el [15 de mayo, comentario 3133476](https://trebuco.atlassian.net/browse/RCS-26238?focusedCommentId=3133476). Los campos administrativos Data Load y Load Job Modified contradicen el mecanismo que describe el análisis y corrige el PR. Conservar la explicación técnica como fuente principal.

### Acción para los dos tickets

1. En Control Panel seleccionar USPROD y cliente 44. Abrir Engineering → Arp Files y resolver `/system/ebr/smarttracksearches/sametendercard.search`. Guardar evidencia del origen efectivo, revisión y ambos tipos. Comparar con release y con cualquier personalización de la búsqueda. La rama main por sí sola no prueba producción.
2. Revisar que los accesos desde Receipt y Links usan el mismo archivo y pasan cardno. Comparar también la entrada directa y una copia guardada por el usuario. Registrar rutas reales; no sobreescribir búsquedas para probar.
3. En QA preparar datos sintéticos: token alfanumérico, token con ceros iniciales, nombre con espacios y acentos, nombre nulo y varias transacciones del mismo token. Probar export normal y Override limit and export all results.
4. Comparar pantalla y Excel por TransactionID y, si la búsqueda devuelve varias filas por transacción, por la combinación estable correspondiente. Exigir mismo conjunto de filas y valores de texto exactos. No convertir identificadores a número ni rellenar nombres nulos.
5. Si la definición efectiva sigue en Double, investigar despliegue, personalización o caché obsoleta del archivo. El fix ya existe. Reutilizar 51987/52242; no abrir un PR idéntico. Si la definición es String y el fallo persiste, capturar request y tipo real entregado al escritor antes de proponer código nuevo.
6. Para confirmar retrospectivamente RCS-23141, recuperar auditoría o snapshot de la búsqueda efectiva del 18 septiembre 2025. El repositorio y la captura sustentan alta confianza; no sustituyen ese artefacto.

## 2. Cero filas: RCS-28339

Las tres capturas del 12 agosto aportan información que no aparece en la descripción:

| Adjunto | Observación directa |
| --- | --- |
| 1403034 | Secure Store → Explorer → Composer. Búsqueda Email Only Lookup 2025-09-03. Ocho resultados. El filtro rápido visible contiene 338553. El valor coincide con Cashier No en las filas visibles. |
| 1403035 | Notificaciones de exportación completada a las 15:31, 15:34 y 15:50; notificación de email enviado a las 15:49. Hora mostrada en la captura, zona sin verificar. |
| 1403036 | Notificación para esa búsqueda: Number of results: 0 y Size of file: 3kb. Ofrece enlace de descarga. |

No consta el XLSX de ese intento ni su task ID. La notificación acredita conteo cero reportado por el sistema; no inspeccioné sus filas. Los tres avisos tampoco prueban duplicación: podrían representar tres exportaciones iniciadas por el usuario. El texto “2025-09-03” pertenece al nombre de la búsqueda; no demuestra su fecha de última edición ni el rango de datos.

El cliente comunica recuperación el [26 agosto, comentario 3312599](https://trebuco.atlassian.net/browse/RCS-28339?focusedCommentId=3312599). No hay fix, excepción, SQL ni correlación de tareas en los ocho comentarios. El cierre es operativo.

### Discriminadores en orden

| Hipótesis | Prueba concreta | Resultado que la sostiene | Decisión |
| --- | --- | --- | --- |
| Diferencia en filtros o parámetros entre grilla y export | Misma búsqueda y usuario; comparar sin filtro, 338553 sin comillas, con comillas y condición explícita Cashier No = valor. Capturar ambos requests. | Pantalla devuelve datos y solo falla determinada forma de filtro; payload o SQL cambian entre rutas. | Rastrear serialización del filtro y el PR de ENG-4066. Revisar versión antes de declarar regresión. |
| La tarea vuelve a leer la búsqueda guardada y pierde parámetros o usa otra revisión | Comparar ruta/ID/revisión de la búsqueda guardada con SSR interactivo y entrada de la tarea. | La tarea recibe parámetros por defecto, vacíos o definición distinta. | Corregir paso de parámetros o resolución de definición en la capa que diverge. |
| Contexto de usuario, cliente o jerarquía diferente | Mismo usuario afectado frente a soporte; comparar ClientID, UserID, roles y condiciones obligatorias de ambos requests. | La tarea ejecuta para otro contexto o añade restricciones diferentes. | Corregir propagación del contexto. No ampliar permisos como prueba. |
| Caché interactiva frente a consulta nueva | Comparar search hash, parámetros, revisión, search.from_cache y resultados del proveedor. | La pantalla lee caché con filas y el export ejecuta consulta distinta o sin filas. | Resolver invalidación o discrepancia de contexto. No purgar globalmente antes de conservar evidencia. |
| Búsqueda referenciada o join en memoria | Leer definición completa y ReferencedSearchServiceRequests; comparar conteos antes y después de cada fase. | La consulta principal devuelve filas y la fase de referencia/filtro las elimina solo en export. | Revisar SearchAccess, SearchJoinHelper y Evaluation Engine según la conexión efectiva. |
| Error/reintento convertido en resultado vacío o aviso incorrecto | Correlacionar task ID, intentos, errores, número de filas y blob de salida. | Excepción o fallo de proveedor seguido de estado Complete con cero, o conteo del aviso distinto del XLSX. | Corregir propagación de fallo o metadatos de resultado con prueba de regresión. |
| Fallo exclusivo de descarga | Descargar el artefacto ya generado y observar respuesta HTTP y redirecciones. | El archivo del servidor contiene filas y falla entrega HTTP, MIME, cookie o ruta. | Revisar endpoint de descarga. No explica por sí solo el cero en la notificación. |

El filtro rápido es la primera prueba por su presencia en la captura y el precedente ENG-4066. No hay comillas visibles en la captura de Urban. Esa diferencia impide dar el bug de comillas por confirmado.

### Secuencia de reproducción

1. Recuperar la ruta real de Email Only Lookup 2025-09-03 del usuario afectado. Guardar XML o SSR, filtros, parámetros y definición de display. No asumir que vive en arpfiles; una búsqueda personal puede residir en el repositorio del usuario.
2. Fijar el mismo usuario, tenant, rango y datos durante la prueba. Registrar URL, revisión y hora con zona. Guardar HAR de pantalla/export con credenciales y cookies retiradas, IDs de correlación, task ID y archivo descargado.
3. Ejecutar las cuatro variantes de filtro de la matriz. Comparar grilla, consulta del proveedor, filas entregadas al escritor, conteo de notificación y XLSX. Registrar cada etapa; un aviso Complete no prueba integridad del contenido.
4. Si alguna variante falla, repetirla tres veces con los mismos parámetros y luego con sesión nueva. Separar cada intento por ID. Esto busca el patrón; tres pases no prueban ausencia universal de intermitencia.
5. En Control Panel, Search Stats y Logs, filtrar por cliente 44, usuario y ventana del intento. Anotar conexión, hash, caché, duración y conteo si la versión expone esas métricas.
6. En HATR Monitor, inspeccionar la tarea de usuario correspondiente, entradas, estado, intentos, excepciones y salida. No usar Trigger Task, cancelar, reintentar manualmente ni cambiar estados en producción.
7. Verificar la definición de pos-data antes de abrir la base. Cerebro explica que DataAreaConnection decide entre Platform SQL, Snowflake y Greenplum. No usar la instancia de otro cliente ni asumir el esquema por el ID.
8. Si los logs de agosto ya expiraron, registrar la retención como límite y reproducir con datos actuales acotados. No inventar correlación entre una recuperación y un despliegue cercano.

## 3. Consultas de lectura preparadas

No ejecuté SQL contra producción. Estas consultas son plantillas de diagnóstico. Sustituir los parámetros en el cliente SQL elegido y comprobar el motor y esquema reales primero. Mantener el mismo contexto de acceso que la aplicación; una consulta administrativa sin sus restricciones solo prueba existencia de datos.

### Platform SQL: comprobar metadatos antes de consultar AsyncSearch

Ejecutar en la base de plataforma de Urban, con credencial de lectura:

```sql
SELECT TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'secure' AND TABLE_NAME = 'AsyncSearch'
ORDER BY ORDINAL_POSITION;
```

Si confirma StartDateTime y EndDateTime, acotar a una ventana de reproducción. Usar parámetros datetime del cliente SQL y verificar la zona almacenada:

```sql
SELECT TOP (100) *
FROM [secure].[AsyncSearch]
WHERE StartDateTime >= @inicio
  AND StartDateTime < @fin
ORDER BY StartDateTime DESC;
```

Inspeccionar columnas de usuario, identificador y request que realmente existan; no suponer nombres. La [guía de búsquedas pendientes](https://trebuco.atlassian.net/wiki/spaces/RTS/pages/476754640949) documenta esa tabla y Status=1 con EndDateTime nulo como candidato pendiente. Su ejemplo es Nordstrom. No ejecutar sus UPDATE ni trasladar su nombre de base a Urban. Un export Complete con cero no equivale a una búsqueda Pending.

### Datos de Same Tender Card

El [comentario 3072494](https://trebuco.atlassian.net/browse/RCS-26238?focusedCommentId=3072494) contiene SQL de ardm_Header, ardm_Tender y ardm_Customer unidos por TransactionID y TradingDay. Una vez verificados esos objetos en la conexión efectiva, usar una ventana pequeña y parámetros vinculados por el driver:

```sql
SELECT h.TransactionID, h.TradingDay,
       t.AccountNumber, c.CustomerFullName
FROM ardm_Header h
LEFT JOIN ardm_Tender t
  ON t.TransactionID = h.TransactionID AND t.TradingDay = h.TradingDay
LEFT JOIN ardm_Customer c
  ON c.TransactionID = h.TransactionID AND c.TradingDay = h.TradingDay
WHERE h.TradingDay >= :fecha_inicio
  AND h.TradingDay < :fecha_fin
  AND t.AccountNumber = :token
ORDER BY h.TradingDay, h.TransactionID
LIMIT 100;
```

Adaptar únicamente el marcador de parámetros y el límite al motor confirmado. Conservar account/token como texto. No copiar el SET ni el barrido anual del ejemplo histórico. Esta consulta acredita valores de origen y puede devolver varias filas por transacción; comparar la granularidad real del SSR antes de concluir duplicados.

Para Email Only Lookup, capturar primero el SQL generado y los parámetros del intento. Su definición no se recuperó. Inventar ahora tablas de email, joins o un WHERE equivalente escondería precisamente la diferencia que buscamos.

## 4. Precedentes y límites de analogía

| Fuente consultada | Hallazgo aprovechable | Límite |
| --- | --- | --- |
| [ENG-4066](https://trebuco.atlassian.net/browse/ENG-4066), Done; [RCS-26650](https://trebuco.atlassian.net/browse/RCS-26650), Closed | Jim reprodujo el 18 mayo 2026 cero resultados al exportar filtros con comillas. QA confirmó 10 junio y Shandana informó producción 12 junio. | Probar filtros en Urban. El release antecede al incidente de agosto; verificar regresión o despliegue, no asumir fix aplicable. |
| [RCS-14740](https://trebuco.atlassian.net/browse/RCS-14740), Closed | Export de drilldown podía dar cero y luego funcionar. Mohammed refiere fix previo el 30 abril 2024. Enlaza [bug 58821](https://dev.azure.com/apprissdevops/missioncontrol/_workitems/edit/58821). | No consta mecanismo preciso en Jira. No atribuirlo a caché ni a fechas por el primer diagnóstico tentativo. No inspeccioné ese work item. |
| [RTS-49747](https://trebuco.atlassian.net/browse/RTS-49747), Closed | Export con Reference Search daba cero en Secure 5.3. Comentario de 3 febrero 2020 indica corrección en 5.4. | Precedente arquitectónico antiguo. Urban necesita confirmar referencias y versión efectiva. |
| [RCS-19401](https://trebuco.atlassian.net/browse/RCS-19401), Closed | El 5 febrero 2025 el analista encontró tareas equivalentes en TJX US y CA; una generaba cero. | La primera sospecha de timeout fue reemplazada por evidencia de ClientID distinto. No concluir reintentos por ver varios avisos. |
| [ENG-4070](https://trebuco.atlassian.net/browse/ENG-4070), Done | URL de descarga con host distinto y cookie host-only; config corregida, cliente valida 2 junio 2026. | Síntoma de login/descarga. Urban ya recibe aviso de cero antes de descargar. |
| [RCS-28105, triage Confluence](https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478143283209) | Traza ResultsController.ExportSearchAsync, HATR, AzureExcelFileWriter y TaskExportController. Plantea MIME y ruta blob. | La ficha admite falta de logs de producción. No tratar sus hipótesis como causa verificada en Urban. Consulté copia de Cerebro del 25 agosto; no usé su estado histórico como estado actual. |
| [ENG-6777](https://trebuco.atlassian.net/browse/ENG-6777), Backlog; [ENG-5649](https://trebuco.atlassian.net/browse/ENG-5649), Reopened | El test enlazado a Urban cubre Izenda y extensión de descarga. Comentarios de 26 agosto reconocen que el PR estaba asociado al test en vez del bug. | Las capturas de Urban son Secure Store Search. Este enlace no prueba causa ni cobertura de conteo/celdas. |
| [RCS-20774](https://trebuco.atlassian.net/browse/RCS-20774), Closed | Urban tuvo error Microsoft.ACE.OLEDB.12.0 al exportar diccionario Searchable as Excel y problema de alias. Kristen informa funcionamiento 26 junio 2025. | Exporta metadatos de Developer Mode, ruta distinta del export de resultados. |
| [Permisos de System Search](https://trebuco.atlassian.net/wiki/spaces/RTS/pages/475391033346), [RCS-12040](https://trebuco.atlassian.net/browse/RCS-12040), Closed | Usuarios con Edit System Search pueden guardar sobre SmartTrack y dejar parámetros fijos. | Revisar personalizaciones y auditoría. No demuestra que un usuario causara los defectos de Urban. |

Documentación adicional: [HATR](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/474696646657), versión de 2023, describe trabajo asíncrono de exportación; [release junio 2026](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/477911482370) incluye ENG-4066 y ENG-4070. Cerebro `brain/markdown/14-appriss-ingeniería-docs-fuente.md`, secciones Search Service y HATR, conserva documentación técnica de junio 2026. Sus originales locales ya no existen en la ruta Downloads/Engineer OnB. Tratar esa copia como guía de navegación hasta verificar el código desplegado.

## 5. Criterios para actuar

| Evidencia obtenida | Acción concreta y responsable funcional propuesto |
| --- | --- |
| Double en definición efectiva | Delivery compara con 51987/52242 y corrige la divergencia mediante proceso de cambio. Conservar snapshot antes de cualquier purga. |
| String efectivo, datos correctos y escritor deja vacío | Ingeniería reproduce con fixture y corrige conversión/serialización. Verificar todos los callers del escritor antes de elegir el lugar del cambio. |
| Filtros distintos entre pantalla y tarea | Ingeniería corrige construcción o serialización del SSR. Una prueba debe comparar valores y filas del XLSX, además del evento de descarga. |
| Parámetros guardados o personalización obsoleta | Delivery determina el origen efectivo y prepara corrección mínima de esa definición. |
| ClientID/UserID/jerarquía distintos | Ingeniería/SRE corrige propagación. No cambiar acceso para ocultar el síntoma. |
| SQL correcto devuelve cero de forma legítima | Soporte explica el filtro/rango verificado; Data Team interviene solo si demuestra datos faltantes aguas arriba. |
| Excepción tratada como Complete/zero | Ingeniería conserva error como fallo de tarea y añade regresión específica. |
| Artefacto correcto y descarga falla | SRE/Ingeniería revisa URL, cookies, MIME y blob con HTTP y logs. |

No hace falta un nuevo PR para volver a aplicar una corrección ya fusionada sin demostrar regresión. Tampoco hay fundamento para recargar datos, modificar tablas o tocar permisos con la evidencia actual.

## 6. Qué quedó probado y qué falta ejecutar

Completado: lectura de los tres tickets y sus comentarios; búsqueda de antecedentes en Cerebro, Jira y Confluence; inspección de cuatro capturas originales y un XLSX; revisión de cuatro PR, sus diffs pertinentes y del historial del archivo; planes y consultas acotadas de lectura. Evidencia y notas están en `investigaciones/evidencia-excel-urban-2026-09-17/`.

Limitaciones: Rovo advirtió cobertura parcial en algunas búsquedas. La lectura de How to Export Reports for Quick Access or Troubleshooting devolvió restricción por IP y no se usó como evidencia. Control Panel bloqueó esta sesión con Cloudflare Ray ID `a3c941032b7b1e0e`. No ejecuté reproducciones en QA/producción, no consulté sus bases ni recuperé el XML efectivo de Email Only Lookup. Tampoco inspeccioné el código interno del escritor; su comportamiento está documentado por SRE y por la descripción del PR, y el diff confirma el arreglo de tipos.

Primera sesión operativa: revisar definición efectiva de Same Tender Card en cliente 44 y recoger un export actual; luego ejecutar la matriz de filtro de Email Only Lookup con IDs y archivo. Esas dos verificaciones separan validación de un fix conocido de investigación del incidente sin causa.

Compromisos históricos: RCS-23141 quedó con pruebas prometidas y validación solicitada, sin resultado registrado. RCS-26238 quedó con producción comunicada y validación solicitada, sin respuesta explícita del cliente en producción. En RCS-28339 Tim dijo que continuaría monitoreando. No se encontró un compromiso abierto con fecha concreta para esta investigación nueva.
