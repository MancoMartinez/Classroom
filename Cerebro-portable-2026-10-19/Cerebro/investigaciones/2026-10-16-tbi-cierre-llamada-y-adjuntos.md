# TBI: conclusiones de llamada y cruce de adjuntos, 16 octubre 2026

Fuente de la llamada: transcripción automática de 36 minutos aportada por Juan. Hablantes inferidos y posibles errores de nombres y cifras. No se dispone aquí del audio original para verificarlos. Se usa el cuerpo de la transcripción, no se toman sus puntos útiles como conclusiones comprobadas.

## Decisiones y compromisos de la llamada

1. 01:22 a 02:53, 18:05 a 19:03: Matt rechaza agregar el Security ID al archivo de ubicaciones como arreglo simple. Describe el diseño basado en teams: carga de teams en SSO+ y réplica al nivel de seguridad, con nombres de team y nivel exactamente iguales. No afirma haber verificado el código actual de esa réplica. J.R. descarta rehacer toda la implementación. Matt se compromete a poner en el chat la explicación del requisito y funcionamiento, con la salvedad de que es según su conocimiento. No se confirmó que ya la publicara.
2. 08:20 a 10:34: si el nivel existe y no se recoge al crear o al volver a entrar, Matt lo considera investigación de Ingeniería. Hay que revisar ambos escenarios. El primer frente ya tiene ENG-10069; no se confirmó que cubra Christi ni una causa de código exacta.
3. 10:41: J.R. pide a Juan poner en el chat enlaces RCS y descripción breve de los tres o cuatro tickets abiertos, incluidos los separados del original. La transcripción no prueba que Juan ya lo haya hecho.
4. 12:36 a 15:46: el ticket mostrado es el de Izenda, RCS-29445. Se ven errores de servidor y Cloudflare 524, con Open Investigations. Matt considera suficiente la evidencia si se limita a Izenda. J.R. pide llevarlo a Waiting for Engineering, asignarlo a Shandana y dejar clara la prioridad del cliente. La consulta posterior sigue mostrando Work in progress y Vedant, sin nuevo comentario de escalación: el pedido no consta ejecutado. El agente no modifica Jira.
5. 15:49 a 17:58 y 34:40: Matt observa TBI más lento que otros clientes. La narración de J.R. de esperar veinte minutos, y hasta una hora, sigue la referencia a Ahold; no asignar esa medida a TBI. Tampoco adjudicar a TBI la llamada Lunar React pendiente de Jim: ese bloque parece continuar sobre Ahold. Los treinta minutos de 11:11 son un reporte verbal introducido al hablar de TBI, no una medición técnica.
6. 19:37 a 20:38: J.R. describe criterio de ownership: Delivery implementa, Support atiende correcciones pequeñas de una o dos horas; trabajos mayores requieren Ingeniería o Delivery. Es criterio operativo expresado en la llamada, no acceso técnico concedido ni aprobación para escribir SQL.
7. 29:03 a 34:18: Juan muestra sso.LocationHierarchyMembers con 90002005 y 40002005. La persistente 4000 es la corrección manual; la otra se interpreta como carga. Matt dice que esa tabla no valida existencia del código y pide archivo original. Su atribución al cliente no está demostrada y debe reconciliarse con Ryan y los CSV.

## Qué añade RCS-29469

Jira consultado en vivo: Work in progress, Juan Martinez, High. Cinco comentarios de cinco leídos. Colton presentó el ticket el 16 octubre como seguimiento explícito de la llamada. Cuatro adjuntos descargados e inspeccionados. No había relaciones Jira en la consulta. El triage Talos interno no pudo leer adjuntos ni recuperar el expediente anterior; su ausencia de precedente no refuta el hallazgo de Rachel.

CSV de ubicaciones: 4094 filas y usuarios únicos; columnas Username, Company, Brand, DeptDescrShort, Zone, Region, District, Location.
CSV de teams: 4094 filas y usuarios únicos, mismo conjunto de usuarios de ubicaciones; cinco nombres de team, todos sin espacios extra detectados en los ejemplos.
CSV de permissions: 4241 filas, 4075 usuarios únicos, un duplicado exacto. 51 usuarios del CSV de ubicaciones no tienen fila en permissions; falta clasificar si es intencional. No es causa demostrada de los cinco ejemplos, que sí están en permissions.

### Contraste determinante para Chris

Archivo appriss_sso_locations_20261014024505.csv, línea 301: Username Chris.Orth@tailoredbrands.com, Company vacío, Brand SSU, Zone CORPORATE, Location 2005. No hay ningún Location que empiece con 9000 en ese archivo. Teams línea 301: Location Manager. Permissions línea 319: ApprissCase Users.

Conclusión estricta: en el archivo aportado del día 14 no viene 90002005 literal para Chris. La investigación previa observó ese valor en la salida sso.LocationHierarchyMembers con fecha de carga del 13. Los lotes son diferentes; hay que obtener el archivo realmente consumido y la transformación para probar de dónde sale el prefijo. No se justifica pedir a HR que cambie Brand, pues SSU ya existe, ni sustituir 9 por 4 para todos. El maestro tiene la tienda 2005 bajo varias marcas según la investigación anterior.

### Location vacío no equivale a ubicación inválida

337 filas tienen Brand SSU. De ellas, 92 tienen Location vacío y 245 informado; hay 32 valores de Location no vacíos. En todo el archivo hay 111 Location vacíos. Todos corresponden a teams de District Manager, Regional Manager, Field Loss Prevention o Administrators; ninguno es Location Manager. 19 de los vacíos tienen ApprissCase Users. Por tanto, vacío puede representar alcance superior a tienda: hay que comprobar jerarquía efectiva antes de declararlo error o pedir una tienda individual. Las cifras del archivo no son comparables directamente con los 266 usuarios y 32 códigos de la consulta histórica: distinta fecha y población.

### Excel: evidencia visual real, no celdas de datos

Libro con hojas No Security Incident ID y Emails; no hay valores de celdas que permitan sustituir la lectura visual. Se extrajeron e inspeccionaron 29 PNG incorporados.

Cinco perfiles muestran Incident Security ID sin selección: Jacinta Titus, Emeldia Pryor, Christi Winters, Rahim Mehdiyev y Cheneria Chevalier. Todos aparecen en los tres CSV con Team Location Manager y Group ApprissCase Users. Brand/Location respectivamente KNG/314, KNG/706, TMW/1604, TMW/4151 y JAB/761. Esto demuestra presencia en el archivo, no recepción o asignación posterior.

Las capturas de última sesión muestran Jacinta 3 junio, Emeldia 15 mayo, Christi 14 julio, Rahim 16 septiembre y Cheneria 2 enero de 2026. No se deduce fecha de creación ni primer login; Cheneria tiene un historial antiguo que hay que clasificar antes de incluirlo en el defecto de alta. No se convierte la hora mostrada a UTC sin validar la pantalla.

Cuatro correos: Jennifer Alba-Faust 14 octubre, aplicación no carga y errores; Johnny Hernandez 14 septiembre, no puede entrar tras usuario corto y contraseña; Nuri Ceylan 8 septiembre, acceso denegado; Rachel Dill 13 octubre, error al completar un incidente y login. Los tres primeros no tienen prueba de Security ID vacío en el correo. El de Rachel se cruza con su evidencia previa; no demuestra automáticamente la misma causa en los demás.

## Estados y pendientes comprobados

RCS-29469: Work in progress, Juan. RCS-29451: Accepted into Development, Shandana. ENG-10069: Backlog, sin asignar, cero comentarios. RCS-29445: Work in progress, Vedant; tres comentarios, último humano público 15 octubre 04:30 EDT. ENG-9990: Backlog, sin asignar. Consulta nueva de RCS-28256 agotó tiempo; no se afirma estado actual.

RCS-29451 tiene cuatro comentarios completos: el interno de Juan 3397050 del 15 octubre contiene la cronología de Rachel y la hipótesis de alta; el público 3397054 comunica revisión por Ingeniería y ofrece ajuste manual a nuevos casos. Esa oferta sí es compromiso publicado. RCS-29469 solo tiene ownership público de Juan 3398341 a las 13:40 EDT, sin fecha concreta de resultado.

## Plan de validación

Hoy, rendimiento: Juan debe coordinar con Vedant y Shandana la escalación solicitada por J.R., conservando screenshots, 524 y alcance Izenda. El compromiso de J.R. era entrada a revisión de Ingeniería el 16 octubre, no solución ese día. Si se desea medir navegación general de TBI, tratarla por separado de Izenda y de los tiempos narrados sobre Ahold.

Hoy, accesos: usar RCS-29469 como recepción de archivos y validación de cinco ejemplos; RCS-29451/ENG-10069 como expediente técnico ya existente. Proponer vincular, no cerrar automáticamente ni crear otro ENG por el mismo síntoma. Para cada ejemplo, comprobar entrada en teams, catálogo de nivel con nombre exacto, salida SSO+ efectiva, cuenta actual, fecha de login y jerarquía. El nivel disponible antes del login es discriminante para Ingeniería.

Hoy, datos: con responsable actual de SnowTime/DataOps aún por identificar, trazar Chris SSU+2005 desde archivo consumido a código generado y registro SSO+. Usar archivo del mismo lote; las copias del 14 adjuntas no prueban recepción del 13 ni del 15. Pedir tabla y consulta exactas de la observación de Matt de inserciones el 15. No atribuir upstream ni retraso del feed por MAX solamente.

Siguiente control: obtener escrito de Matt, dueño de ENG-10069 y resultado de revisión de Ingeniería para rendimiento; registrar fecha real de próxima comunicación. No consta aprobación de corrección masiva ni de cambios del formato del cliente.

## Fuentes

- Transcripción: /Users/MancoMenStudio/.codex/attachments/e41225b0-672e-4b96-92b5-98e7b94f92de/Texto pegado.txt.
- Jira RCS-29469 y adjuntos: adjuntos/RCS-29469/jira-evidencia-2026-10-16.json; CSV originales y Excel en la misma carpeta.
- Inspección de cinco usuarios y Chris/Rachel: adjuntos/RCS-29469/csv-crosscheck.json. PNG originales del Excel: adjuntos/RCS-29469/excel-images/.
- Rachel: https://trebuco.atlassian.net/browse/RCS-29451?focusedCommentId=3397050.
- Compromiso de ajustes manuales: https://trebuco.atlassian.net/browse/RCS-29451?focusedCommentId=3397054.
- Tickets: https://trebuco.atlassian.net/browse/RCS-29469, https://trebuco.atlassian.net/browse/RCS-29445, https://trebuco.atlassian.net/browse/ENG-10069 y https://trebuco.atlassian.net/browse/ENG-9990.
