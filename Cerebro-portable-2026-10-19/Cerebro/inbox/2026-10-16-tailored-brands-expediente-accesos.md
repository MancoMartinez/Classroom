# Tailored Brands 209: expediente de accesos a Incident

Estado al 16 oct 2026. Jira consultado en vivo hoy. Todas las horas son UTC salvo que diga ET o Bogotá. Bogotá es UTC-5 y ET es UTC-4.

## 1. Tickets y estado en vivo

| Ticket | Tema | Estado hoy | Dueño |
|---|---|---|---|
| [RCS-29451](https://trebuco.atlassian.net/browse/RCS-29451) | Incident Security ID vacío y jerarquía vacía | Accepted into Development | Shandana Khan |
| [ENG-10069](https://trebuco.atlassian.net/browse/ENG-10069) | Usuarios creados por SSO no reciben nivel en su primer login | Backlog, sin asignar, sin comentarios | |
| [RCS-28256](https://trebuco.atlassian.net/browse/RCS-28256) | Lentitud Secure a Incident | Under Customer Review, High | Juan Martinez |
| [ENG-9990](https://trebuco.atlassian.net/browse/ENG-9990) | Lentitud Incident TBI | Backlog, sin asignar, sin comentarios | |

Enlaces en Jira: RCS-29451 relates to RCS-28256 y lo clona ENG-10069. RCS-28256 lo clona ENG-9990 y está duplicado por RCS-29060.

Hay tres problemas abiertos y son independientes:

1. **Nivel vacío en el primer login.** Es un defecto de código y está en RCS-29451 y ENG-10069.
2. **Jerarquía vacía por LocationID 9000xxxx.** Es un problema de datos o de carga. Va por DataOps en el canal Data Issues y todavía no tiene ticket propio.
3. **Feed SSO+ sin cargar desde el 13 oct.** El problema está antes de la tarea Hatr. Va por DataOps en Data Issues.

Aparte sigue la lentitud, que está en RCS-28256 y ENG-9990.

## 2. Línea de tiempo

### Antecedentes

| Fecha | Hecho | Fuente |
|---|---|---|
| 2026-04-17 01:12 | Kiran inserta una fila Persistent 1 de nivel 5 para Christi Winters. | [RCS-26519](https://trebuco.atlassian.net/browse/RCS-26519) |
| 2026-06-04 | Se construye la carga del nivel de Incident desde el archivo diario hacia Secure. | [RCS-27269](https://trebuco.atlassian.net/browse/RCS-27269) |
| 2026-06-26 a 07-02 | Secure ignoraba los niveles en el login. Se corrige el 2 jul con el hotfix PR 54159. El permanente, PR 54149, quedó "tested locally only". | [RCS-27578](https://trebuco.atlassian.net/browse/RCS-27578) |
| 2026-06-29 | Un despliegue de release pisa un fix ya mergeado. | RCS-26519 |
| 2026-07-14 19:36 | Christi Winters entra y su cuenta queda NULL aunque tiene la fila Persistent 1 desde abril. | SQL del 14 oct |
| 2026-07-22 a 09-16 | Configuración de seguridad por Case Type, resuelta. | [RCS-27941](https://trebuco.atlassian.net/browse/RCS-27941) |
| 2026-08-06 | Las consultas de LPUser pasan de 0,5 s a 57 s. El release reseteó dos feature flags. | RCS-28256 |
| 2026-08-10 | Se abre RCS-28256 por lentitud. | Jira |
| 2026-08-27 | Sale ENG-7168 y los tiempos del cliente no cambian. | [ENG-7168](https://trebuco.atlassian.net/browse/ENG-7168) |
| 2026-09-08 y 09-28 | Colton reporta a Chaz Hyman y Nancy Bolhoff, y después a Paul Bubelnik Jr, sin nivel. | RCS-28256 |
| 2026-09-25 | Nota de escalación por lentitud. Matt está fuera hasta el 5 oct. | Comentario 3364709 |
| ~2026-10-08 | Ola de corte a SnowTime con TBI incluido. ENG-7326 figura Live, pero no hay fecha confirmada del cambio de fuente de Secure. | [ENG-7326](https://trebuco.atlassian.net/browse/ENG-7326) |
| 2026-10-09 09:11 | Se redespliega `sso.GetUserSecurityLevel`, con modify_date en esa hora. | sys.objects |

### 12 al 13 de octubre

| Fecha | Hecho | Fuente |
|---|---|---|
| 10-12 19:21 | La cuenta de Chris Orth se crea por SSO. A las 19:24:52 hay una CryptographicException en Saml2Verification.cs línea 55. No está confirmado que sea de Chris. | Grafana |
| 10-12 15:35 ET | Colton le aplica Location Manager a Chris a mano. Chris entra a las 19:50 UTC y sigue sin poder crear incidentes. | Comentarios 3393401 y 3393474 |
| 10-13 09:00 a 11:00 | ReferenceDataBackLoad corre y carga el feed SSO+. Las filas quedan a las 10:42:27. Es la última carga. | Control Panel Logs |
| 10-13 9:55 ET | Colton avisa que la jerarquía de Chris está vacía y que su SSO+ muestra la ubicación correcta. | Comentario 3394253 |
| 10-13 15:57 ET | Matt pide separar el ticket, que Shandana cree un ENG para la lentitud y que los accesos los resuelva Soporte. | Comentario 3394822 |
| 10-13 19:23:49 | Primer login de Rachel Dill, que crea la cuenta con SecurityID NULL. Su fila de nivel 5 ya existía desde las 10:42. | Grafana, ResponseLog 30893 |

### 14 de octubre

| Hora | Hecho | Fuente |
|---|---|---|
| 05:22 ET | Shandana crea ENG-9990 para la lentitud. | Comentario 3395369 |
| 09:00 a 09:03 | ReferenceDataBackLoad termina en 3 minutos sin filas nuevas. | Control Panel Logs |
| 09:02 ET | La automatización avisa que el ticket pasa de 60 días y pide revisión con Support management. | Comentario 3395484 |
| Durante el día | Revisión profunda. Juan pone nivel 5 a mano a Paul, Nancy y Rachel. | inbox/2026-10-14-rcs-28256-revision-profunda.md |
| 14:15 ET | Respuesta pública con el estado por usuario. | Comentario 3395988 |
| 15:30 ET | Nota interna con hallazgos y propuesta de separar. | Comentario 3396090 |
| 15:39 ET | Colton confirma que la tienda de Chris es 40002005, #2005 MW TUX DC, y pregunta si el 90002005 viene del archivo. | Comentario 3396106 |
| 18:59 ET | Juan agrega 40002005 persistente a la jerarquía de Chris. En la base queda como 22:57:46 UTC. | Comentario 3396285 |
| 19:58 UTC | Rachel vuelve a entrar y el nivel manual se mantiene. | membership.Users y UserActivityLogins |
| Durante el día | Correo de J.R. Teagle, "Secure Incident ID, Choose a Value", pide revisar RCS-27269, 27578, 27941 y 28256. | Correo |

### 15 de octubre

| Hora | Hecho | Fuente |
|---|---|---|
| 09:00 a 09:13 | ReferenceDataBackLoad termina en 13 minutos sin filas nuevas. | Control Panel Logs |
| Durante el día | Matt responde por Teams Q1 a Q3: LPUser2 no es requisito, basta la vista LPUser. Pide un solo RCS nuevo para accesos. Pide validar con Ryan que la carga llene Secure e Incident. | inbox/2026-10-15-rcs-28256-respuesta-matt.md |
| Durante el día | Grafana: patrón de primer login en 9 de 9 casos. | Sección 4 |
| Durante el día | Matt: "Should work when the user is created as well as any subsequent attempts... please send to shan to create a new ENG ticket". | Teams |
| 13:57 ET | Juan crea RCS-29451 con prioridad Medium. | Jira |
| 13:58 ET | Aviso público de la separación en RCS-28256. | Comentario 3396997 |
| 14:03 ET | Triage de Talos, que es IA. Su lectura, no verificada, es que el nivel sale de la pantalla SSO admin, de un nivel enviado en SAML o de un default. Dice que TBI no tiene default y que mapea niveles por team. | Comentario 3397002 |
| 15:02 ET | Nota interna de escalación. | Comentario 3397050 |
| 15:03 ET | Respuesta pública: Engineering revisa y Soporte pone el nivel a mano si aparecen nuevos casos. | Comentario 3397054 |
| Después | Se crea ENG-10069 y RCS-29451 pasa a Accepted into Development con Shandana. | Jira |
| 16:06, 16:17 y 16:57 Bogotá | Respuestas de Ryan Barlow, en la sección 5. | Teams |
| 19:45:11 | Se crea por SSO la cuenta de David.Loza@mooresclothing.com, caso de prueba nuevo. | Grafana |

### 16 de octubre, llamada con Tailored

Participantes: J.R., Mike DiTommaso, Christopher Dyess, Colton Neal y Camila Cortes.

- **Acceso a archivos:** Colton no tiene acceso directo a los archivos diarios y tiene que pedírselos a otra persona. No se sabe todavía quién es el responsable.
- **Reintentos:** según Colton, algunos usuarios entran al reintentar. Es una observación sin tiempos ni secuencia.
- **Jacinta Titus y Emeldia Pryor:** tienen el nivel vacío, con ApprissCase Users y Location Manager en el archivo. Su último login fue en junio, según Colton, sin verificar en logs. No se puede asumir que sean casos de primer ingreso.
- **Christi Winters y Rahim Mehdiyev:** aparecen con el nivel vacío en el libro "Appriss Incident Security ID Examples".
- **Uso esporádico (Mike):** algunos usuarios de tienda entran una o dos veces al año. Un login viejo no significa abandono. El criterio de validación tiene que cubrir a quien vuelve después de meses.
- **Archivo appriss_sso_locations_20261014024505:** muestra Company, Brand y Location separados. Varias filas corporativas traen Brand SSU, otras MSP o TMW, y Location 2005 aparece en filas SSU. Colton sugiere que el problema puede ser de todos los SSU. Es una hipótesis del cliente.
- **Archivo del 14 oct:** el nombre del archivo indica que TBI generó un archivo de ubicaciones el 14 oct a las 02:45. No se sabe si llegó a SnowTime.
- **Chris Orth:** muestra su jerarquía con 40002005, #2005 MW TUX DC. Eso prueba que la asignación se ve, no que haya creado un incidente.
- **Pedido de J.R.:** consultar con Matt, en el ticket y en Teams, si conviene seguir derivando el nivel del archivo de teams o recibir el Security ID explícito junto con la ubicación. No hay decisión.

## 3. Hallazgos por problema

### 3.1 Nivel vacío en el primer login, confirmado con logs

- **Rachel Dill:** tenía fila de nivel 5 a las 10:42 y el proc devolvía 5. Su primer login a las 19:23:49 creó la cuenta con `"SecurityID":null`. En el log aparecen los grupos y el team que se aplicaron desde SSO Extra, y ninguna línea de nivel.
- **Patrón en 9 de 9 usuarios creados entre el 9 y el 15 oct:** los que volvieron a entrar tienen 5. Los que solo hicieron el login de creación siguen en NULL.
- **El nivel manual se mantiene:** a Rachel le duró después de su login del 14 oct.
- **Christi Winters no encaja con el patrón:** tenía Persistent 1 desde abril, entró en julio y quedó NULL. Sigue sin explicación.
- **Alcance:** 49 usuarios con login desde el 2 jul, nivel mayor que 0 en el feed y NULL tanto en membership.Users como en la vista incident.LPUser. Falta medir cuántos tienen un solo login.
- **Descartado:**
  - El feed, porque las filas existen.
  - `sso.GetUserSecurityLevel`, porque devuelve 5 y no filtra Persistent = 1.
  - La vista LPUser, porque todos los afectados están en ella.
  - LPUser2, porque es solo correlación. Matt dice que no es requisito: con fila tienen nivel 79 de 79, sin fila 101 tienen nivel y 46 no.
  - Las claims SAML, porque no traen ni team ni nivel.
- **Hipótesis descartada:** que una regresión del proc al filtro Persistent = 1 explicara los casos.

### 3.2 Jerarquía vacía por LocationID 9000xxxx

- **Alcance:** 266 usuarios @tailoredbrands.com con 32 LocationID 9000xxxx que no existen en place.Location. Son DCs, hubs, oficinas y corporativo. Los más grandes son #1099 CORPORATE con 40, #5075 JOSEPH ABBOUD MFG con 22, #5013 PDC TUX HUB con 21, #4001 AURORA DC con 19, #1091 RETAIL DC BVDC con 19 y #2005 MW TUX DC con 16.
- **Gemelos:** cada 9000xxxx tiene un gemelo 4000xxxx en place.Location, a una distancia de 50000000.
- **Total:** 287 ApprissCase Users tienen alguna ubicación inválida. Los 21 que no están en el rango 9000xxxx no se han revisado.
- **El prefijo es de marca:** en incident.Store la tienda 2005 existe como 10002005 JAB, 20002005 KNG, 30002005 MSP y 40002005 TMW. El prefijo 9 no existe ni en Incident ni en Secure.
- **Claims SAML:** las de los corporativos traen company SSU y UniqueLocID tipo SSU1099.
- **Ryan:** "It does appear that we add the 9", dicho con cautela. Después dijo "I don't think adding a 4 is correct", y en su opinión las oficinas y DC deberían venir como ubicaciones en el archivo del cliente. Deja abierto si el 9 es correcto.
- **Chris Orth:** tiene un parche individual, 40002005 persistente. No sirve como regla para todos.

### 3.3 Feed SSO+ sin carga desde el 13 oct

| Día | ReferenceDataBackLoad | Filas nuevas |
|---|---|---|
| 13 oct | 09:00:00 a 11:00:35 | sí, a las 10:42 |
| 14 oct | 09:00:21 a 09:03:46 | no |
| 15 oct | 09:00:28 a 09:13:21 | no |

- Ryan revisó la tarea y no vio errores: "The issue, if any, would be up stream. Any changes to that type of load process go through data ops most likely."
- Desde el corte a SnowTime, Ryan no conoce el proceso de cambios.
- La tarea está Enabled en Hatr Scheduled Tasks. Su Sleeping Until dice 04:00 UTC, pero arranca de verdad a las 09:00.

## 4. Consultas útiles

Todas son de solo lectura. Las SQL se corren en SSMS dentro del bastion, base `sqldb-prd-wus2-arp-production-209-tbi-platform`. No funcionan en Snowflake.

### Frescura del feed

```sql
SELECT 'level' AS tabla, MAX(InsertedDateTime) AS ultima_carga FROM sso.SecurityLevelAssignments
UNION ALL SELECT 'location', MAX(InsertedDateTime) FROM sso.LocationHierarchyMembers;
```

### Proc de nivel: fecha y definición

```sql
SELECT name, create_date, modify_date FROM sys.objects WHERE object_id = OBJECT_ID('sso.GetUserSecurityLevel');
SELECT OBJECT_DEFINITION(OBJECT_ID('sso.GetUserSecurityLevel')) AS Definicion;
EXEC sso.GetUserSecurityLevel @userName = 'rachel.dill@menswearhouse.com';
```

### Usuarios con nivel en el feed y cuenta NULL desde el 2 jul

```sql
SELECT COUNT(*) n, STRING_AGG(CONCAT(u.UserName,'|',CONVERT(date,u.LastLoginDate),'|',s.SecurityID),'; ') x
FROM membership.Users u
JOIN sso.SecurityLevelAssignments s ON s.UserName = u.UserName AND s.SecurityID > 0
WHERE u.SecurityID IS NULL AND u.LastLoginDate >= '2026-07-02';
```

### Feed, team y grupo de usuarios concretos

```sql
SELECT 'level' AS src, UserName, CONVERT(varchar(20),SecurityID) AS value, CONVERT(varchar(10),Persistent) AS persistent, CONVERT(varchar(30),InsertedDateTime) AS inserted
FROM sso.SecurityLevelAssignments WHERE UserName LIKE '%rachel.dill%' OR UserName LIKE '%chris.orth%'
UNION ALL SELECT 'team', UserName, TeamName, CONVERT(varchar(10),Persistent), NULL
FROM sso.Teams WHERE UserName LIKE '%rachel.dill%' OR UserName LIKE '%chris.orth%'
UNION ALL SELECT 'perm', UserName, GroupName, NULL, NULL
FROM sso.PermissionGroups WHERE UserName LIKE '%rachel.dill%' OR UserName LIKE '%chris.orth%'
ORDER BY UserName, src;
```

### Cuenta y último login de un usuario

```sql
SELECT UserID, UserName, SecurityID, LastLoginDate FROM membership.Users WHERE UserName = 'David.Loza@mooresclothing.com';
```

### Nivel en la capa de Incident

En la vista incident.LPUser la columna es `EmailAddr`. No existe `Email`.

```sql
SELECT LoginID, EmailAddr, UserID, SecurityId, StoreIdent, LastLoginDate FROM incident.LPUser WHERE LoginID = 'rachel.dill@menswearhouse.com';
```

### Ubicaciones del feed que no existen en place.Location

```sql
SELECT m.LocationID, COUNT(*) n, STRING_AGG(m.UserName,'; ') x
FROM sso.LocationHierarchyMembers m
WHERE NOT EXISTS (SELECT 1 FROM place.Location l WHERE l.LocationID = m.LocationID)
GROUP BY m.LocationID;
```

### Gemelos 9000xxxx a 4000xxxx

Esta consulta está reconstruida. Revísala antes de correrla.

```sql
SELECT m.LocationID, m.LocationID - 50000000 AS gemelo, COUNT(DISTINCT m.UserName) AS usuarios,
       CASE WHEN l.LocationID IS NULL THEN 'no existe' ELSE 'existe' END AS gemelo_en_place
FROM sso.LocationHierarchyMembers m
LEFT JOIN place.Location l ON l.LocationID = m.LocationID - 50000000
WHERE m.LocationID BETWEEN 90000000 AND 90009999
GROUP BY m.LocationID, l.LocationID ORDER BY usuarios DESC;
```

### Tienda por número de marca

StoreIdent es un ID corto interno. La búsqueda se hace por StoreNo.

```sql
SELECT StoreIdent, StoreNo FROM incident.Store WHERE StoreNo IN (10002005, 20002005, 30002005, 40002005, 90002005);
```

### Jerarquía efectiva de un usuario

```sql
SELECT * FROM secure.LocationHierarchyUserAssignments WHERE UserId = (SELECT UserID FROM membership.Users WHERE UserName = 'chris.orth@tailoredbrands.com');
```

### Claims SAML de un login

```sql
SELECT Id, InsertedDateTime, Summary, Response FROM sso.ResponseLog WHERE Id = 30893;
```

### Grafana

Se usa Explore con el datasource `grafanacloud-apprissretail-logs`. Grafana muestra la hora de Bogotá.

Usuarios creados por SSO:

```
{service_name=~".+", deployment_environment="usprod"} | clientId="209" |= "Sso user created"
```

Login de un usuario. Usa backticks. El GUID va en minúscula porque `|=` distingue mayúsculas:

```
{service_name=~".+", deployment_environment="usprod"} | clientId="209" |~ `(?i)rachel\.dill`
{service_name=~".+", deployment_environment="usprod"} | clientId="209" |= "19ca9f1a-88c3-48dd-8457-26aba1331fa0"
```

### Control Panel

**Carga del feed:** en Logs, con Log Source Grafana y cliente 209, pon el Message filter en `ReferenceDataBackLoad`. La L va en mayúscula y el campo Instance ID tiene que quedar vacío.

**Programación de la tarea:** en Hatr Scheduled Tasks, cliente 209, filtra por Reference. Para revisar no se toca Run Now ni Cleaning Locks.

## 5. Respuestas de personas, textuales

**Matt Kamminga**

- Teams, 13 oct en Jira: "these individual user access issues they should not need further engineering review".
- Teams, 15 oct, Q1 a Q3: la vista LPUser alcanza, sin LPUser2. Un RCS nuevo para accesos. "Toda ubicación de incident debería estar también en secure", validar con Ryan.
- Teams, 15 oct: "do you see anything in the logs as to why the securityId is not being sent? as long as they have the row in SSO+ it should really be set from there".
- Teams, 15 oct: "Should work when the user is created as well as any subsequent attempts really if its actually failing on creation then please send to shan to create a new ENG ticket to resolve".

**Ryan Barlow, Teams 15 oct**

- "TBI sends a file specifically for SSO. This file loads everything into the SSO+ tables. TBI has moved to snowtime." Los scripts viejos de ARDM están en el repo DataOps c209tbi, ruta ardm/sql/load_ardm_scripts/ARDM_sso_.
- "It does appear that we add the 9 . . ."
- "ReferenceDataBackload is the hatr task that performs the replication. You can see logs in Control Panel. I don't believe any error messaging goes out if it fails."
- "Looks like 10/14 data should have loaded around 9am UTC on 10/14.... perhaps customer file didn't make it in time so it reloaded the day prior".
- "The hatr task ran and I didn't see any errors. The issue, if any, would be up stream."
- "I don't think adding a 4 is correct. In my opinion the 9 outliers need to be a location included in the customer's file... Whether or not the 9 is correct would need work."
- "With snowtime in play now, I haven't had any exposure into the process for changes".

**Shandana Khan, Jira 14 oct:** crea ENG-9990 y desenlaza ENG-7182 porque no lo ve relacionado.

**Colton Neal**

- Jira, 14 oct: la tienda de Chris es 40002005 y pregunta "Do you know the 90002005 coming from the file directly?".
- Llamada, 16 oct: no tiene acceso a los archivos diarios.

**Mike DiTommaso, llamada 16 oct:** los usuarios de tienda entran una o dos veces al año.

**J.R. Teagle, llamada 16 oct:** pide consultar con Matt si conviene derivar el nivel o recibirlo explícito.

## 6. Otros tickets abiertos de Tailored Brands

| Ticket | Tema | Estado y dueño | Relación con este caso |
|---|---|---|---|
| [RCS-29445](https://trebuco.atlassian.net/browse/RCS-29445) | Izenda lento, timeouts y errores de servidor | Work in progress, Vedant Shirude | Mismo tenant y síntoma de lentitud. Duplica a RCS-29060, que a su vez está enlazado a RCS-28256. Hipótesis: comparte la causa de rendimiento de ENG-9990. Sin verificar. |
| [RCS-29430](https://trebuco.atlassian.net/browse/RCS-29430) | Faltan nombre, dirección y ID de cliente en recibos desde principios de oct | Under Support Review, Sebastian Rueda | Empieza en las mismas fechas que la ola de corte a SnowTime del ~8 oct y que el feed SSO detenido el 14. Hipótesis: problema aguas arriba en SnowTime. Sin verificar. Conviene cruzarlo con Sebastian. |
| [RCS-27097](https://trebuco.atlassian.net/browse/RCS-27097) | Review Data, clonado a [ENG-4230](https://trebuco.atlassian.net/browse/ENG-4230), redondeo en Snowflake | Accepted into Development, Shandana Khan | Datos Snowflake. No se relaciona con accesos. |
| [RCS-27237](https://trebuco.atlassian.net/browse/RCS-27237) | Tender Types, Other Credit Card | Under Customer Review, Rae Hatfield | Sin relación. |
| [RCS-26881](https://trebuco.atlassian.net/browse/RCS-26881) | Campo Staff Discount Amount por línea | Under Customer Review, Rae Hatfield | Sin relación. |
| [ENG-7326](https://trebuco.atlassian.net/browse/ENG-7326) | Corte a SnowTime | Live | Contexto del feed. No hay fecha confirmada del cambio de fuente de Secure. Edwin la pidió el 14 oct. |

## 7. Pendientes

1. **ENG-10069:** sin asignar. Hay que confirmar con Shandana quién lo toma y que lea la nota 3397050.
2. **Data Issues:** publicar el post sobre el feed del 14 y el 15 y sobre el origen del 9, que está en inbox/2026-10-15-rcs-28256-data-issues-tbi-sso.md. Ryan no tiene un nombre de contacto. Daniel Endersby contesta los hilos de SnowTime en ese canal, pero no está confirmado como dueño de TBI.
3. **Matt:** pedido de J.R. sobre derivar el nivel o recibirlo explícito. No se ha enviado.
4. **Los 49:** medir cuántos tienen un solo login, comparando EntryDate de LPUser con LastLoginDate. Revisar Christi, Jacinta y Emeldia, que no encajan con el primer ingreso.
5. **David Loza:** revisar su SecurityID antes y después de su segundo login.
6. **Chris Orth:** confirmar que puede crear un incidente.
7. **J.R.:** el correo del 14 está obsoleto en la parte de ubicaciones, porque decía "missing on our side".
8. **Cliente:** identificar quién tiene acceso a los archivos diarios de TBI.
9. **RCS-28256:** está a más de 60 días y pide revisión con Support management.
10. **El 9 y SSU:** no reemplazar 9 por 4 de forma masiva ni pedir a HR que cambie datos hasta que DataOps defina el mapeo.
