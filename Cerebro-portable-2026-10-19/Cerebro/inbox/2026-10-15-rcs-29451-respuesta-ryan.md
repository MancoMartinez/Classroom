RCS-29451. Respuesta de Ryan Barlow por Teams, 15 oct 2026.
TBI manda un archivo propio para SSO que carga las tablas SSO+. TBI paso a Snowtime; los scripts viejos de ARDM (repo DataOps c209tbi, ardm/sql/load_ardm_scripts/ARDM_sso_...) pueden no aplicar ya.
"It does appear that we add the 9": el prefijo 9 lo agrega nuestra carga, no el cliente. CONFIRMADO por Ryan.
La replicacion la hace la tarea Hatr ReferenceDataBackload; logs en Control Panel; no avisa si falla.
La carga del 14 oct debio correr hacia las 9:00 UTC; quiza el archivo del cliente llego tarde y se recargo el dia anterior. Sin verificar.
Pendiente: confirmar en Grafana la corrida de ReferenceDataBackload del 14 y 15 oct; preguntar a Ryan como corregir el prefijo y donde se rastrea.

15 oct 16:39 Bogota: MAX(InsertedDateTime) sso.SecurityLevelAssignments 2026-10-13 10:42:27; sso.LocationHierarchyMembers 2026-10-14 22:57:46, que es la entrada manual de Chris Orth (5:57:46 PM Bogota). CONFIRMADO: ninguna carga del feed el 14 ni el 15 oct en ninguna de las dos tablas. No es solo un archivo tardio de un dia.
La busqueda de Grafana que pego Juan trae lineas "Sso user created", no ReferenceDataBackload: falta correr la busqueda correcta. Nuevo usuario creado: David.Loza@mooresclothing.com 2026-10-15 19:45:11 UTC (caso para probar el patron).

15 oct, ruta para ver la corrida: la busqueda de Grafana por ReferenceDataBackload no sirve, en RCS-28911 dio cero lineas en tres dias. Hatr Trigger Task no tiene historial y el Durable Monitor borra su historial en cada ciclo. Lo que si sirve es Control Panel, Hatr, Hatr Scheduled Tasks, cliente 209, fila ReferenceDataBackLoad: Enabled, Sleeping Until UTC y View Logs. No tocar Run Now ni los botones de Cleaning Locks.

15 oct 16:50 Bogota, captura de Hatr Scheduled Tasks, cliente tailoredbrands.com 209, filtro Reference. CONFIRMADO: ReferenceDataBackLoad Enabled, Sleeping, proxima corrida 2026-10-16 04:00 UTC, 00:00 hora del cliente. CctvReferenceDataLoad Enabled, proxima 2026-10-16 01:00 UTC. ReferenceDataBackLoadIncidentOnly y ReferenceDataCacheTask deshabilitadas.
La tarea no esta caida ni trabada. Corre a las 04:00 UTC, no a las 9:00 UTC que se habia supuesto. La ultima carga del feed tiene InsertedDateTime 2026-10-13 10:42 UTC, seis horas despues de la corrida de las 04:00. HIPOTESIS: la tarea corrio el 14 y el 15 sin archivo nuevo del cliente, o con un archivo que no inserto filas. Falta View Logs del 14 y 15.

15 oct 16:59 Bogota, Control Panel Logs, fuente Grafana, cliente 209, filtro ReferenceDataBackLoad con L mayuscula. CONFIRMADO, horas en UTC:
13 oct Starting 09:00:00, Executed 11:00:35, dos horas. Las filas del feed quedaron a las 10:42, dentro de esa corrida.
14 oct Starting 09:00:21, Executed 09:03:46, tres minutos, sin filas nuevas.
15 oct Starting 09:00:28, Executed 09:13:21, trece minutos, sin filas nuevas.
CORRECCION: la tarea corre a las 09:00 UTC como dijo Ryan. El 04:00 UTC de Sleeping Until no es la hora de arranque real.
La tarea corre y termina sin error. HIPOTESIS: no llego archivo de TBI el 14 y 15, o la carga lo salto. Leccion: el filtro de Message distingue mayusculas, ReferenceDataBackload con l minuscula da cero resultados.

15 oct 16:57 Bogota, segunda respuesta de Ryan por Teams, a la version 1 del mensaje:
"The hatr task ran and I didn't see any errors. The issue, if any, would be up stream. Any changes to that type of load process go through data ops most likely."
"I don't think adding a 4 is correct. In my opinion the 9 outliers need to be a location included in the customer's file. For example, if a user is assigned to a DC, then that DC needs to be included as a location. Whether or not the 9 is correct would need work."
Lectura: feed del 14 y 15, la tarea Hatr esta bien, la falla seria aguas arriba, archivo de TBI o SnowTime. Dueno: DataOps, canal Data Issues segun directriz del 15 oct. Ruta de autoservicio por verificar: SnowTime FAQ NO DATA FEED, Client Summary, Observability, Feed Health, Azure Function Loader.
Ubicaciones 9000xxxx: Ryan descarta el prefijo 4. Su opinion, no confirmada: TBI debe incluir oficinas y DC como ubicaciones en su archivo. Si el 9 es correcto queda abierto. La entrada manual de Chris Orth con 40002005 es un parche y la tienda real depende de Colton.
teams-ryan-2-v2 queda OBSOLETO, Juan envio la version 1 y Ryan ya contesto.

15 oct, tercera respuesta de Ryan: "With snowtime in play now, I haven't had any exposure into the process for changes". No tiene nombre en DataOps para TBI. La ruta queda en el canal Data Issues sin etiqueta. En ese canal, los hilos de SnowTime del 14 y 15 oct los contesta Daniel Endersby: WMT, 202 MKS y ICA. Es una observacion del canal, no un dueno confirmado de TBI.
