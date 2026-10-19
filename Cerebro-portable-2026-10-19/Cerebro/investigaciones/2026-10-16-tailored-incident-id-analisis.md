# Tailored Brands: análisis para Secure Incident ID Meeting

Preparación privada para Juan. Corte: 16 octubre 2026. Jira y Confluence consultados en vivo; observaciones SQL y Grafana proceden de evidencia publicada por Juan y de notas previas de Cerebro. Esta sesión no consultó producción directamente.

## Lectura principal

La reunión probablemente trata de la confiabilidad del aprovisionamiento de usuarios de Incident. El hilo “Secure Incident ID, Choose a Value” citado en la nota interna de RCS-28256 del 14 de octubre vincula RCS-27269, RCS-27578, RCS-27941 y RCS-28256. “Incident Security ID” es el nivel del usuario, por ejemplo Location Manager. El número de un caso es otro dato; RCS-28157 trató ese segundo asunto y no explica el problema actual.

Hay cuatro planos distintos: recepción y transformación de archivos SSO+, aplicación del nivel a la cuenta durante el ingreso, resolución de ubicaciones y autorización por tipo de caso. La lentitud y los errores de Izenda tienen seguimiento separado. Reunirlos bajo una causa única borraría las pruebas que permiten distinguirlos.

Juan confirmó como posibles participantes a J.R. Teagle, Mike DiTommaso, Christopher Dyess, Colton Neal y Camila Cortes. Identificó tres representantes del cliente. Falta invitación original, horario y agenda formal. Su lista no confirma que Matthew Kamminga, Shandana Khan, DataOps o un desarrollador asistan.

El papel propuesto para Juan es presentar evidencia, impacto, separación de causas, contención aplicada y preguntas pendientes. Esto deriva de su trabajo y de sus comentarios publicados. La reunión necesita acordar responsables y próximo hito. El expediente no otorga a Juan autoridad para comprometer una fecha de desarrollo.

## Mapa actual verificado

| Asunto | Registro | Estado y responsable al consultar | Lectura |
| --- | --- | --- | --- |
| Nivel vacío y jerarquía | [RCS-29451](https://trebuco.atlassian.net/browse/RCS-29451) | Accepted into Development, Shandana Khan | Caso principal de accesos |
| Nivel en primer ingreso | [ENG-10069](https://trebuco.atlassian.net/browse/ENG-10069) | Backlog, sin asignar | Defecto registrado; no equivale a corrección programada |
| Transición lenta a Incident | [RCS-28256](https://trebuco.atlassian.net/browse/RCS-28256) | Under Customer Review, Juan Martinez | Accesos separados públicamente el 15 de octubre |
| Desarrollo de lentitud | [ENG-9990](https://trebuco.atlassian.net/browse/ENG-9990) | Backlog, sin asignar | Sin comentarios en el ENG al consultar |
| Reportes Izenda | [RCS-29445](https://trebuco.atlassian.net/browse/RCS-29445) | Work in progress, Vedant Shirude | Descripción con esperas de minutos y errores |
| Cadencia SSO+ | [RCS-28973](https://trebuco.atlassian.net/browse/RCS-28973) | Closed, Bikash Kumar | Precedente que requiere reconciliar evidencia y cierre |
| Búsquedas HR | [RCS-27941](https://trebuco.atlassian.net/browse/RCS-27941) y [ENG-7824](https://trebuco.atlassian.net/browse/ENG-7824) | Closed y Done | Validación del cliente el 15 de septiembre; sin cambio de código |
| Aprovisionamiento histórico | [RCS-26519](https://trebuco.atlassian.net/browse/RCS-26519), [RCS-27269](https://trebuco.atlassian.net/browse/RCS-27269), [RCS-27578](https://trebuco.atlassian.net/browse/RCS-27578) | Closed | Resolvieron fallas anteriores, con mecanismos diferentes |

RCS-28256 está en espera del cliente y su SLA queda pausado por ese estado. Su antigüedad no demuestra riesgo de reloj. Este análisis no calcula SLA para el resto de los tickets.

## 1. Nivel vacío: la evidencia más fuerte

[Nota interna 3397050, RCS-29451, 15 octubre](https://trebuco.atlassian.net/browse/RCS-29451?focusedCommentId=3397050). Juan publicó la escalación y dejó explícita la diferencia entre datos observados y su interpretación del flujo.

Rachel Dill sirve como caso discriminante. Su fila en sso.SecurityLevelAssignments tenía SecurityID 5 desde el 13 de octubre a las 10:42 UTC. El procedimiento actual devuelve 5. Su ingreso de las 19:23:49 UTC creó la cuenta y el log registró SecurityID null. Luego agregó grupos y equipo Location Manager. El dato había llegado antes de la creación.

La secuencia publicada registra SsoService identificando grupos y equipos a las 19:23:49.582 y .586, MembershipService creando la cuenta a .641, User Data con SecurityID null a .660, grupos a .684 y equipo a .698. Saml2 registra el ingreso a las 19:23:56.732. La ausencia de una línea de nivel no basta para probar qué método omitió el código. El estado NULL resultante y el nivel disponible en el feed sí documentan la falla observable.

Juan aplicó Location Manager manualmente el 14 de octubre. El nivel se sostuvo después del ingreso posterior de Rachel. Eso demuestra estabilidad del parche en ese caso. Su segundo ingreso no prueba una autocorrección, porque ocurrió después del ajuste manual.

Ocho cuentas adicionales creadas entre el 9 y el 15 de octubre tienen nivel 5 en el feed. Ashley Carter, Teegan Baker, Jordan Shields, Alexis Post y Theresa Veasley tenían nivel tras ingresos posteriores. Brett Virtue, Doris Mays y Tamieko Jones tenían NULL y su último ingreso coincidía con la creación. Este patrón apoya la hipótesis de una diferencia entre creación y actualización de cuenta. No constituye una prueba controlada de que cerrar y volver a entrar resuelva todos los casos.

La cifra de 49 corresponde a cuentas que habían ingresado desde el 2 de julio, con nivel positivo en el feed y NULL en membership.Users y en la vista incident.LPUser. No equivale a 49 usuarios bloqueados simultáneamente ni a 49 primeros ingresos comprobados. Tampoco se debe sumar a los otros conteos de jerarquía.

Hipótesis vigente: el alta por SSO no aplica el nivel de la misma forma que un ingreso posterior. Falta identificar y confirmar la rama concreta del código y determinar el alcance actual. El título de ENG-10069 recoge ese defecto. Su descripción conserva el resumen de accesos y jerarquías del RCS y no incorpora la secuencia técnica; no tenía comentarios. El vínculo al RCS existe. Conviene que el responsable de Engineering confirme que leyó la nota 3397050 antes de estimar.

## 2. Chris Orth: nivel correcto y ubicación sin resolver

[Nota interna 3396090](https://trebuco.atlassian.net/browse/RCS-28256?focusedCommentId=3396090), [reporte del cliente 3394253](https://trebuco.atlassian.net/browse/RCS-28256?focusedCommentId=3394253) y [respuesta pública 3396285](https://trebuco.atlassian.net/browse/RCS-28256?focusedCommentId=3396285).

Las capturas del 12 y 13 de octubre muestran a Chris con Location Manager, un error genérico al intentar continuar, jerarquía del usuario con cero resultados y una fila SSO+ para 90002005. La combinación demuestra que aplicar el nivel no bastó para restituirle la capacidad de crear incidentes.

Las consultas documentadas por Juan no encontraron 90002005 en place.Location. Colton confirmó #2005 MW TUX DC, Bakersfield, cuyo identificador es 40002005. Juan comunicó públicamente que agregó una entrada persistente para Chris y pidió probar de nuevo. En los comentarios consultados no aparece una confirmación posterior de Chris creando correctamente el incidente.

La revisión local identificó 266 usuarios con 32 identificadores 9000xxxx y encontró equivalentes 4000xxxx. Otro conteo, 287 usuarios ApprissCase Users con ubicación sin correspondencia, incluye 21 fuera de ese subconjunto. Son poblaciones diferentes y observaciones del 14 de octubre. No afirman 287 usuarios con el mismo defecto de prefijo.

Ryan escribió el 15 de octubre que parece que la carga agrega el 9. También cuestionó reemplazarlo por 4 como arreglo general y propuso revisar si oficinas y DC deben existir como ubicaciones en el archivo del cliente. Son observaciones preservadas en Cerebro, no lectura directa del chat de Teams en esta sesión. La regla de transformación y su corrección permanecen abiertas. Cada tienda 2005 existe bajo varias marcas; el número corto no determina la marca correcta.

Hay un matiz de comunicación: la respuesta pública del 14 de octubre pidió revisar si el 90002005 venía en el archivo. El dato posterior de Ryan exige rastrear la transformación de Appriss antes de atribuirlo al cliente. No se debe presentar la opinión sobre oficinas y DC como requisito ya confirmado para TBI.

## 3. Archivos diarios: ejecución y frescura son pruebas diferentes

[RCS-28973, nota 3382222 del 6 octubre](https://trebuco.atlassian.net/browse/RCS-28973?focusedCommentId=3382222) documenta tareas exitosas y archivos recibidos diariamente, junto con un máximo de InsertedDateTime congelado en el 4 de octubre. La nota considera que el dato podría estar atascado. El comentario público 3387261 del 10 de octubre comunica procesamiento saludable, ausencia de impacto funcional observado y cierre con seguimiento.

El expediente no muestra en esos comentarios una reconciliación completa entre el máximo congelado y la conclusión de cierre. Tampoco prueba una interrupción continua desde septiembre hasta hoy. El cliente declaró el 23 de septiembre que no conocía usuarios afectados en ese momento y explicó que su preocupación incluía altas, bajas y transferencias.

Las notas de Juan del 15 de octubre registran filas del feed con máximo 13 octubre 10:42 UTC y ninguna fila nueva atribuida a la carga del 14 o 15. ReferenceDataBackLoad arrancó a las 09:00 UTC cada día y terminó sin error; el 13 duró dos horas, el 14 tres minutos y el 15 trece. Es evidencia local fechada. No se consultaron hoy ni SnowTime ni archivos originales de esos días.

Conclusión limitada: terminar sin error no demuestra que el archivo nuevo se consumió ni que una baja o traslado concreto se aplicó. Falta comparar nombre y fecha del archivo recibido, procesamiento en SnowTime, salida replicada y resultado para un cambio conocido. Un máximo sin movimiento tampoco prueba por sí solo ausencia de archivo si la transformación admite actualizaciones diferenciales.

El precedente RCS-27325 aporta una prueba más concreta de junio: la captura 1368905 muestra cero filas de origen para LocationHierarchyMembers mientras Teams y PermissionGroups sí cargaban miles. El cliente validó el 10 de julio que veía la tienda correcta. Es un antecedente de carga parcial, no evidencia de que ese mismo mecanismo opere en octubre.

## 4. Qué resolvieron junio y julio

RCS-26519 y RCS-27269 completaron el recorrido que deriva niveles desde el archivo de equipos y los replica a sso.SecurityLevelAssignments. La resolución interna de RCS-26519 del 29 de junio menciona tabla y mapeo YADL incompletos, una configuración de Snowflake y un cambio sobrescrito por un despliegue. Eso acredita historia de despliegues; no prueba que el defecto actual sea una regresión del mismo cambio.

RCS-27578 empezó con Adam Barkhouse y una explicación de timing. El 1 de julio, la investigación documentó 3.917 usuarios con nivel válido en el feed que el procedimiento ignoraba al filtrar Persistent = 1. La corrección quitó el filtro y priorizó excepciones persistentes. Soporte comunicó el despliegue el 3 de julio como activo desde el día 2. Colton confirmó resolución el día 8.

La lectura de octubre descartó que el procedimiento actual conserve ese filtro. Rachel ingresó después de su carga y del despliegue registrado el 9 de octubre. Repetir “solo debe esperar al archivo” no explica su caso.

El correo del 6 de julio de Matthew Everett ya había aclarado al cliente que un usuario incluido correctamente en el archivo no debe iniciar sesión y esperar después 24 horas. El archivo llega primero y el siguiente ingreso debe aplicar la asignación. La reunión debe respetar esa expectativa publicada.

Los pendientes históricos fueron 19 usuarios sin fila de asignación, confirmar roster completo frente a delta y revisar excepciones manuales. La nota de Shelley del 21 de julio dice que TBI decidió conservar las excepciones porque algunos usuarios no llegan por SailPoint. No existe autorización general para eliminarlas.

## 5. HR y búsquedas: permisos completos requieren más de una capa

RCS-26584 documenta que el 5 de mayo Colton renombró Risk Management a HR Corporate User, habilitó tipos de registro y validó búsquedas para Beverly y Francesca. Las capturas de mayo muestran ese nombre y las asignaciones SSO+.

En RCS-27941, las capturas del 20 de agosto muestran Corporate User para Beverly y Location Manager para Francesca, con búsqueda Peters vacía. Las capturas del 1 de septiembre muestran que esos niveles no estaban habilitados en los tipos relevantes. Kiran también agregó permisos faltantes para Ramos. El 10 de septiembre, Francesca aparecía HR Corporate User y Beverly seguía Corporate User; tras el ajuste, Colton confirmó el 15 que ambas buscaban bien.

Resultado confirmado: Soporte y cliente corrigieron configuración y asignación; Engineering cerró sin cambio de código. Pregunta abierta histórica: por qué el estado de mayo no coincidía con agosto. Los comentarios no prueban quién lo cambió ni qué proceso lo revirtió. No atribuirlo al primer ingreso actual.

La hipótesis de que una fila ausente en LPUser2 explique por sí sola el fallo quedó corregida. Para cuentas nuevas, Matthew indica revisar la vista LPUser. Las 49 cuentas actuales aparecen en esa vista. Insertar filas LPUser2 sin demostrar necesidad repetiría una investigación descartada.

## 6. Rendimiento e Izenda

RCS-28256 conserva el reporte de transición de 35 a 40 segundos del 16 de septiembre. Es medición del cliente, no cronometraje independiente de esta sesión. ENG-9990 está en Backlog sin asignar. El 14 de octubre Shandana lo creó y desvinculó ENG-7182 por no tener relación demostrada.

RCS-29445 describe lista de reportes de 2 a 5 minutos, aperturas de 2 a 4 minutos, errores de servidor y timeouts. Las capturas del expediente de RCS-28256 muestran errores de Izenda en septiembre y octubre, incluido 524 el 14 de octubre a las 16:07:16 UTC. El RCS dedicado no trae adjuntos propios. Los originales siguen disponibles en RCS-28256.

La nota automática de Talos en RCS-29445 sugiere revisar flags. Las lecturas de Juan del 8 de septiembre ya tenían ambos flags AdHoc en True; no prueban su valor actual. Tampoco prueban que volver a encenderlos resuelva el problema. La atribución del tiempo restante requiere trazas del entorno y un dueño técnico.

## 7. Confluence y sus límites

[Setting up SSO](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/475190689809) describe alta automática en primer ingreso y aprovisionamiento combinado desde claims y archivos. [Setting up Secure Incident](https://trebuco.atlassian.net/wiki/spaces/PD/pages/475269201922) separa permisos y pertenencia a ubicaciones como requisitos. Estas páginas ayudan a explicar las capas; no diagnostican TBI.

[Universal SSO](https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/1175654815) documenta configuración de mapeo y diferencias entre Secure e Incident. Es diseño histórico, no inspección de la configuración efectiva de octubre.

[Runbook Tailored Brands](https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478007361549) cita RCS-27578 y ofrece diagnóstico general. Su versión de julio no recoge el defecto actual. [Gateway Pull Support Guide](https://trebuco.atlassian.net/wiki/spaces/PD/pages/477497557009) describe S3 y pipelines; su tabla no enumera los tres archivos SSO. No acredita la ruta completa actual de SSO después de SnowTime.

[SSO Troubleshooting](https://trebuco.atlassian.net/wiki/spaces/RTS/pages/475709046806) aconseja contrastar SSO+ y usuario. Su afirmación general sobre VPN no trae evidencia específica de TBI. No se usa como explicación del incidente.

[Triage Urban RCS-28909](https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478212325381) muestra que ubicaciones en Incident y en Secure pueden divergir. Solo aporta precedente de arquitectura. Sus propuestas de escritura y supuestos sobre no purgar filas no se trasladan a TBI.

## 8. Qué puede aportar Juan a la reunión

El cliente lleva meses esperando automatización consistente. Mike cuestionó el 6 de julio una explicación que trasladaba el problema a tiempos de espera; Colton pidió el 12 de junio evitar ajustes manuales habituales para transferencias. La conversación necesita demostrar qué evidencia explica cada síntoma y cómo se validará el resultado.

Papel propuesto: explicar el caso limpio de Rachel, separar Chris, reconocer las correcciones previas y confirmar el seguimiento actual en RCS-29451 y ENG-10069. Las cifras corresponden a cortes históricos y requieren medir alcance actual. Evitar prometer que un segundo ingreso o el cambio masivo de prefijo resolverá a toda la población.

Decisiones a buscar: responsable técnico de ENG-10069; responsable de DataOps para la carga y las ubicaciones; un criterio de éxito observable; responsable y fecha del próximo update. No hay ETA publicada para el arreglo.

Criterios propuestos para acordar, sin ejecución autorizada en producción: cuenta nueva con fila previa en el feed recibe nivel correcto desde primer ingreso; usuario con ubicación confirmada puede crear un incidente; excepción persistente intencional se conserva; traslado y baja conocidos se reflejan según el comportamiento pactado. Cada prueba necesita entorno, propietario y usuario aprobados por quienes administran el sistema.

Preguntas para el cliente: si Chris pudo crear tras el ajuste; si Paul, Nancy y Rachel accedieron después de la solicitud del 14 de octubre; qué usuarios siguen afectados hoy; qué ubicaciones y excepciones manuales son intencionales. Las preguntas sobre archivos van por nombres y cambios concretos, no por atribución anticipada de culpa.

## 9. Compromisos publicados y cautelas

RCS-29451, público 15 octubre 15:03 EDT: revisión por Engineering y asignación manual para nuevos reportes de nivel vacío. No incluye plazo de corrección. RCS-28256, público 15 octubre: accesos pasan a RCS-29451 y lentitud permanece allí. RCS-28973, público 10 octubre: cierre con monitoreo y seguimiento proactivo si aparecen hallazgos. Distinguir esos compromisos del texto local preparado para Data Issues, cuyo envío no quedó confirmado en esta sesión.

Las notas del 14 de octubre que afirman LPUser2 como causa, que recomiendan prefijo 4 para todos o que consideran 04:00 UTC como arranque real están superadas por fuentes del 15. Los borradores para crear el RCS y pedir un ENG ya no reflejan el estado actual. No reenviar. No se modificaron borradores anteriores ni se prepararon mensajes nuevos.

## 10. Evidencia y cobertura

El paquete conserva respuestas de Jira, comentarios con fecha y visibilidad, inventario de adjuntos y originales descargados. Las descripciones y comentarios de los tickets se recuperaron completos según sus contadores; el registro técnico permite verificar total y cantidad recibida. Se consultaron fuentes recientes de Cerebro, fichas y bitácora con sus correcciones. Las fichas derivadas tienen errores de asociación de cliente; Jira manda.

Se descargaron 137 archivos representativos del inventario seleccionado, deduplicando copias por nombre y tamaño antes de descargar; incluye 135 imágenes y dos MSG. La galería permite revisar todas las imágenes y abrir originales. Los MSG de junio se abrieron y sus nueve imágenes internas se extrajeron; algunas son duplicadas. Incluyen firmas, publicidad y un comentario de abril ya presente en Jira. La clasificación por tamaño y nombre evita muchas copias, sin garantizar identidad binaria.

No se afirma cobertura de todos los tickets históricos de TBI. La búsqueda incluyó Jira por cliente y títulos, con antecedentes adicionales de permisos y transferencias. RCS-24442 se revisó como antecedente remoto de archivos; sus adjuntos no se incluyeron en la descarga principal. No se accedió a la invitación, correo actual, Teams en vivo, código fuente, Azure DevOps, SnowTime ni producción. Los enlaces a PR son referencias del expediente, sin verificación directa de su contenido o despliegue actual.

Archivos de apoyo: 2026-10-16-tailored-meeting-evidencia.json, 2026-10-16-tailored-extra-evidencia.json, 2026-10-16-tailored-29451-evidencia.json, 2026-10-16-tailored-confluence.json, 2026-10-16-tailored-confluence-sso.json y 2026-10-16-tailored-adjuntos-manifest.json en investigaciones. El primer archivo de Confluence conserva el timeout inicial de Universal SSO; la lectura posterior completa está en confluence-sso.json. La carpeta de galería incluye inventario con hash de cada archivo: 137 archivos, 132 contenidos distintos. Cinco copias adicionales compartían contenido con otro archivo de distinto nombre.

## Capturas para recorrer la evidencia

Chris tiene Location Manager, jerarquía vacía y una asignación SSO+ 90002005. La misma hoja conserva errores Izenda del 14 de octubre. Cada captura es evidencia de su momento, no del estado actual.

![Chris y los frentes separados](/Users/MancoMenStudio/Cerebro/investigaciones/2026-10-16-tailored-galeria/RCS-28256-8.jpg)

El 1 de septiembre, las pantallas de Manage Case Type muestran niveles permitidos por tipo y las filas consultadas por Kiran.

![Autorización por tipo de caso](/Users/MancoMenStudio/Cerebro/investigaciones/2026-10-16-tailored-galeria/RCS-27941-4.jpg)

El 10 de septiembre, Francesca muestra HR Corporate User y Beverly Corporate User. El expediente conserva además las capturas de pertenencia a los grupos AD y el ajuste posterior de Beverly.

![Diferencia entre niveles efectivos](/Users/MancoMenStudio/Cerebro/investigaciones/2026-10-16-tailored-galeria/RCS-27941-5.jpg)

Jonathan tenía datos en archivos antes del ingreso fallido de julio. La hoja muestra permisos, equipo y ubicación del archivo, además del error. Es el antecedente que impidió sostener timing como explicación general.

![Jonathan y los archivos anteriores a su ingreso](/Users/MancoMenStudio/Cerebro/investigaciones/2026-10-16-tailored-galeria/RCS-27578-2.jpg)

En junio, la captura de carga de RCS-27325 muestra cero filas del origen de jerarquías mientras sí carga equipos y permisos. Es precedente de carga parcial.

![Carga parcial de junio](/Users/MancoMenStudio/Cerebro/investigaciones/2026-10-16-tailored-galeria/RCS-27325-1.jpg)

Galería completa: [abrir índice de originales](/Users/MancoMenStudio/Cerebro/investigaciones/2026-10-16-tailored-galeria/index.html) o [hojas de revisión](/Users/MancoMenStudio/Cerebro/investigaciones/2026-10-16-tailored-galeria/galeria.md).

Siguiente paso:
J.R. y Camila: acordar quién presenta cada frente y quién comunica el próximo hito; confirmar presencia de Engineering y DataOps.
Shandana y Engineering: confirmar lectura de 3397050, responsable de ENG-10069 y prueba que separa alta de actualización.
Mike, Colton y Christopher: validar usuarios aún afectados y resultado de Chris; acordar qué mejora concreta cierra el problema.
