# VisualCron: conectar el cliente y sacar el employee feed de ADUSA

Fecha: 27 ago 2026
Contexto: Matt Kamminga pregunta por Teams si Juan tiene acceso a la maquina de VisualCron.
La pregunta viene de la peticion de Juan del 26 ago: un archivo reciente del employee feed de
ADUSA para mapear que campo aterriza en `incident.Employee.MISC1`.
Ticket de fondo: RCS-28093. MISC1 es lo que LPMS llama *division* y lleva la marca. Llega
intermitente. Mismo comportamiento en el ambiente viejo, no es regresion.

## Estado observado en pantalla

VisualCron Client 12.2.2, abierto en QA-LPMS-RDP-001 via Bastion.

- Perfil de servidor: `[AD] jmartinez@QA-LPMS-VC`
- Barra de estado: `Server: QA-LPMS-VC-001:16444 | Server time: N/A | Jobs: N/A`
- Boton `Server [Off]` en gris, grid de servidores vacio
- Failed Jobs, Running Jobs, Log, Server info y License en gris

Lectura: el cliente arranco sin sesion contra el servidor. Los iconos grises son consecuencia de
no haber conectado, no evidencia de que falten permisos.

## Discrepancia con el runbook

El runbook oficial define el servidor US como `visualcron.lpguys.net`, no `QA-LPMS-VC-001`.
El perfil actual apunta al nombre de maquina. Puede resolver igual, puede quedarse colgado en el
handshake Kerberos si el SPN no coincide.

Valores exactos que exige el runbook para el servidor US:

```
Auto connect at startup: Checked
Is a local server: Unchecked
Server: visualcron.lpguys.net
Port: 16444
Timeout: 60
Credentials: Use Active Directory logon
IdentityType: SPN identity
Principle name: HOST/qa-lpms-rdp-001.lpguys.net
```

Servidor EU, se agrega como segundo perfil con Add. ADUSA es US, para esto no hace falta.

```
Server: PE-LPMS-VC-001
Port: 16444
Principle name: HOST/qa-lpms-rdp-001.lpguys.net
```

El runbook esta escrito para el Client 9. En 12.2.2 el boton vive en la pestana Servers o en el
icono contiguo al dropdown de servidor. Los campos son los mismos.

## Pasos

1. Abre Manage Servers desde la pestana Servers o el icono junto al dropdown.
2. Selecciona el perfil, Edit, corrige los ocho campos de arriba, Update.
3. Cierra Manage Servers y pulsa Connect.
4. Con sesion viva, Server time y Jobs dejan de decir N/A y el grid se llena.

Si Connect falla por credenciales o permisos, la cuenta AD no esta en User permissions del
servidor VisualCron. El acceso a Azure y el acceso a VisualCron son dos aprobaciones distintas.
Juan ya tiene la primera, esta en el Bastion. Pide la segunda a Matt o a IT.

## Donde esta el archivo del feed

Tres rutas, de mas directa a menos.

**WinSCP contra `root@192.168.3.8`, carpeta `/uploads/`.** Ahi dejan los clientes los archivos de
import antes de que corra nada. Es el feed crudo de ADUSA, que es exactamente lo que sirve para
mapear campos. Sube con Parent Directory hasta `/uploads/` para ver todos los clientes.

**Share `\\qa-lpms-vc-001.lpguys.net`, carpeta VC-Clients.** Guarda los ejecutables programados por
cliente. VisualCron transfiere ahi el archivo, llama a LPImport desde la carpeta del cliente, corre
la aplicacion, actualiza el log y archiva el import. La carpeta de archive del cliente tiene los
ultimos dias.

**VisualCron ya conectado.** Ubica el job del employee import de ADUSA, abre el task y lee la ruta
de archive configurada. Esta ruta confirma cual de las dos anteriores es la buena.

## Respuesta a Matt, para pegar en Teams

Ver bloque en la conversacion. Resumen: Juan tiene Bastion y cliente, le falta la sesion al
servidor VisualCron.

## Fuentes

- Visual Cron Azure Access, espacio RTS, pagina 475025145857
- Azure Bastion, espacio AALPS, pagina 474713391122
- brain/markdown/26-adusa-estado-tickets-reuniones.md, RCS-28093 y MISC1

## Avance 27 ago, 19:20

Conexion resuelta. QA-LPMS-VC-001 arriba, 145 jobs, uptime 100%, latencia 31 ms, 4 failed jobs.

Matt indico buscar por Delhaize y menciono una carpeta clients con subcarpeta de Delhaize donde
viven todos sus jobs.

Filtro Name = `Delhaize` devuelve dos jobs, ninguno es el employee feed:

| Grupo | Job | Ultima corrida | Duracion |
|---|---|---|---|
| Platform - Refloaders | Refloader Prod Delhaize | 27 ago 15:09 | 00:00:00.3 |
| Platform - SQL Jobs | Delhaize Noggin Export RCS16448 | 27 ago 08:30 | 00:00:14.2 |

`Refloader Prod Delhaize` declara "Uses Job Variables" en la descripcion. Esas variables deberian
contener la ruta base del cliente. Es la via mas corta a la carpeta que describe Matt.

Pendiente: filtrar por `employee` para listar todos los jobs de employee import y ver bajo que
marca esta ADUSA. Candidatos de nombre: Food Lion, Stop and Shop, Giant, Hannaford, Ahold, Peapod.

Hipotesis viva: el feed de empleados de ADUSA puede no ser un import programado. En la reunion del
21 ago quedo que Jim copio a April Valerio "por el feed automatico de empleados". Si es automatico
via API, el job estaria en el grupo LPGuys - API Integration y no en Imports.

## Rutas encontradas, 27 ago 21:35

Job `Refloader Prod Delhaize`, grupo Platform - Refloaders, servidor QA-LPMS-VC-001.

Job Variables:

```
WorkingDirectory  F:\Clients\Delhaize\Refloader_PROD
DownloadFolder    /uploads/DelhaizeFTP/imports
```

`F:\Clients\Delhaize` es la carpeta clients que describio Matt. La unidad F es local de
QA-LPMS-VC-001. Desde el RDP se llega por el acceso directo VC-Clients del escritorio o por
`\\qa-lpms-vc-001.lpguys.net`.

`/uploads/DelhaizeFTP/imports` es la carpeta del SFTP `root@192.168.3.8` donde ADUSA deposita.

Trigger: lunes a viernes 10:00 AM, activo desde el 10 jul 2025.

Cadena de cinco tasks, en orden:

| # | Task | Que hace |
|---|---|---|
| 1 | FTP/FTPS/SFTP/SCP | Baja los archivos de /uploads/DelhaizeFTP/imports |
| 2 | Decrypt File(s) | Descifra con las llaves de Kleopatra |
| 3 | Execute Refloader | Corre el ejecutable del cliente |
| 4 | Archive File(s) | Copia a la carpeta de archive |
| 5 | Delete file(s) | Borra el original |

El task 5 borra el archivo de origen. La unica copia recuperable esta en la ruta del task 4.
Abrir el task 4 para leer la ruta exacta de archive. Abrir el task 1 para leer la mascara de
nombres de archivo, que identifica cual de los archivos es el de empleados.

## Detalle de los tasks 1 y 4

Task 1, FTP/FTPS/SFTP/SCP. Command type Download, conexion `lpms@files.lpguys.net:22`.
Corrige el dato del runbook viejo, que citaba `root@192.168.3.8`.

Task 4, Archive File(s), tipo Copy files:

```
Source folder       F:\Clients\Delhaize\Refloader_PROD\data
File mask           pgp*
Destination folder  F:\Clients\Delhaize\Refloader_PROD\archive
```

Consecuencia operativa: la carpeta archive guarda los archivos cifrados, no los descifrados.
El task 2 descifra en `\data`, el task 5 borra lo que queda ahi. Cualquier archivo recuperado de
`\archive` hay que descifrarlo con Kleopatra siguiendo el runbook LPMS - Decrypt client file.

## Como llegar al mapeo de MISC1

Cuatro vias, ordenadas por costo.

1. Task 3, Execute Refloader. Declara el ejecutable y sus argumentos, incluido el archivo de
   configuracion. Ese config es el que mapea campo del feed contra campo de LPMS. Responde la
   pregunta original sin descifrar nada.
2. Listar `F:\Clients\Delhaize\` completo. Refloader_PROD es una subcarpeta. Puede existir otra
   carpeta dedicada al employee feed con su propio job.
3. Copiar un `.pgp` de `\archive` a carpeta de trabajo y descifrarlo con Kleopatra. Nunca tocar
   el original.
4. SSMS contra `pd-lpms-uswest2-sqldb-001.database.windows.net`, solo SELECT. Contar filas del
   tenant ADUSA con MISC1 nulo o vacio. Ese conteo es el que Matt se comprometio a sacar en
   RCS-28093.

Duda abierta: el job se llama Refloader, que recarga datos. Falta confirmar que sea el mismo
proceso que alimenta employee. La via 2 lo resuelve.

## Confirmado, 27 ago 22:10. El feed de empleados existe y esta identificado

Output estandar del task 1, corrida programada del 27 ago 10:00:00 AM, resultado Success,
duracion 00:00:02.1. Descargo dos archivos:

```
F:\Clients\Delhaize\RefLoader_PROD\data\pgp-DA_Employee_Info.dat
F:\Clients\Delhaize\RefLoader_PROD\data\pgp-DA_Store_info.dat.pgp
```

`DA_Employee_Info.dat` es el employee feed de ADUSA. DA es Delhaize America. Queda cerrada la duda
abierta: el job Refloader Prod Delhaize si es el proceso que alimenta employee. No existe un job
de employee aparte.

El prefijo `pgp-` indica que ambos llegan cifrados. La mascara del task 4 es `pgp*`, asi que los
dos terminan en la carpeta archive.

## El share correcto

`F$` falla con 0x80004005 por ser share administrativo. El share publicado es **VC-Clients**:

```
\\qa-lpms-vc-001.lpguys.net\VC-Clients\Delhaize
```

Contenido, tres carpetas:

| Carpeta | Modificada |
|---|---|
| Exports | 2 oct 2024 |
| RefLoader_Prod | 10 jul 2025 |
| RefLoader_Test | 9 jul 2025 |

No hay carpeta dedicada a empleados. Todo el feed pasa por RefLoader_Prod.

## Correccion sobre la duracion del job

El Job Result Output de la corrida de las 15:09 dice Start reason `By User`, disparada por
Ryan Barlow, duracion 0.3 segundos. Esa fue una ejecucion manual sin archivos nuevos que procesar.
La corrida real es la programada de las 10:00 AM, donde el task 3 tomo 32.8 segundos. El job
acumula 316 ejecuciones desde el 9 jul 2025. Descarta la lectura anterior de que 0.3 segundos
fuera senal de fallo.

## Siguiente paso

Ruta de trabajo: `\\qa-lpms-vc-001.lpguys.net\VC-Clients\Delhaize\RefLoader_Prod`

1. Abrir `Custom_Load_ReferenceLPMS.cmd` con Bloc de notas por clic derecho, Abrir con.
   Nunca doble clic, eso lo ejecuta en produccion.
2. Del .cmd sale la ruta del archivo de configuracion del Refloader. Ese config declara el mapeo
   de columnas contra MISC1.
3. La carpeta `archive` guarda los `pgp-DA_Employee_Info.dat` de dias anteriores. Copiar uno a
   `C:\Temp` y descifrarlo con Kleopatra si hace falta ver los encabezados reales.

## Contenido de Custom_Load_ReferenceLPMS.cmd, 27 ago

Version 10.24.2024.0. Rutas que declara:

```
ROOTFOLDER           F:\Clients\Delhaize\RefLoader_Prod
CORE_CODE            F:\Clients\_CoreCode_Prod\RefLoader
JOBLOG               F:\Clients\Delhaize\RefLoader_Prod\logs\JobLog.log
CUSTOMER_CONFIG_FILE F:\Clients\Delhaize\RefLoader_Prod\RefLoader_DB.config
```

Bloque EMPLOYEE:

```
ANC_LOAD_TYPE      EMPLOYEE
ANC_SOURCE         F:\Clients\Delhaize\RefLoader_Prod\data
ANC_DAILY_FILEMASK pii-pgp-DA_Employee_Info.dat
ANC_FORMAT_FILE    \fmt\employee.xml
ANC_EXPECTEDDAILY  FALSE
```

Llamada al motor:

```
ReferenceSupplementalLoad.exe RefLoader_DB.config \fmt\employee.xml
```

### Donde vive el mapeo de MISC1

`employee.xml` es el format file que pasa como segundo argumento. Ese archivo declara la
correspondencia entre columna del feed y campo de LPMS. Ahi esta MISC1.
Ruta probable: `F:\Clients\Delhaize\RefLoader_Prod\fmt\employee.xml`.
El argumento empieza con backslash, asi que puede resolver contra la raiz de F o contra CORE_CODE.
Verificar cual de las dos existe.

### Hallazgo de causa raiz para RCS-28093

`ANC_EXPECTEDDAILY=FALSE` en el bloque EMPLOYEE. Cuando el archivo no llega, el script salta a
`:LOAD_NOSOURCEFILE`, escribe una linea en el JobLog y deja el exit code en 0. La alerta a
VisualCron solo se dispara con EXPECTEDDAILY en TRUE, que fija exit code 3.

Consecuencia: si ADUSA deja de enviar el feed de empleados un dia, el job reporta Success y nadie
se entera. Esto explica de forma mecanica la intermitencia que el cliente reporta en la marca.
El comportamiento es identico en el ambiente viejo, coherente con lo que dijo Chris el 21 ago
sobre que no es regresion.

Para medirlo, abrir `F:\Clients\Delhaize\RefLoader_Prod\logs\JobLog.log` y contar las lineas:

```
-EMPLOYEE- Source file not found to load
-EMPLOYEE- Reference files found in data folder
```

La razon entre ambas da el porcentaje de dias sin feed. Es evidencia directa, con fecha y hora.

### Discrepancia de nombres, pendiente de confirmar

El FTP descargo `pgp-DA_Employee_Info.dat`. El .cmd busca `pii-pgp-DA_Employee_Info.dat`.
Igual con store: descargado `pgp-DA_Store_info.dat.pgp`, buscado `pii-pgp-DA_Store_info.dat.pgp`.
La diferencia es el prefijo `pii-` en ambos casos.

Hipotesis: el task 2, Decrypt File(s), escribe la salida anteponiendo `pii-`. Confirmar abriendo
ese task. Si la hipotesis falla, el `if exist` nunca encuentra el archivo y el load de employee
no corre nunca, que seria un hallazgo mayor.

### Otros archivos utiles en la carpeta

| Archivo | Para que sirve |
|---|---|
| `logs\JobLog.log` | Historial de si el feed llego o no, por dia |
| `logs\EMPLOYEE_Import_Log.log` | Registros rechazados cuando el exit code es 2 |
| `RefLoader_DB.config` | Cadena de conexion a la base de LPMS |
| `fmt\employee.xml` | Mapeo campo del feed contra campo de LPMS |

Codigos de salida del script: 0 todo bien, 2 cargo con errores de datos, 3 falta un archivo
esperado a diario, 99 error critico.
