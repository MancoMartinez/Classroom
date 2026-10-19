# Cosecha visual-cron — 2026-08-28
Fuente: sesion local_7cfc3365-2457-4fcb-b097-3583e6c4fd25, "Visual Cron"

Ticket asociado: RCS-28093, ADUSA / Delhaize. Verificado en Jira durante la sesion: estado Under
Support Review, asignado a Juan Martinez, prioridad Low. ENG-6744 ya existe, no hay transicion
pendiente.

## Hallazgos verificados

Job y ejecutable. El Refloader de Delhaize corre `Custom_Load_ReferenceLPMS.cmd`, que invoca
`ReferenceSupplementalLoad.exe` con dos argumentos: `RefLoader_DB.config` y `\fmt\employee.xml`.

Descarga diaria. El job baja dos archivos a las 10 AM, `DA_Employee_Info.dat` y
`DA_Store_info.dat`, ambos cifrados con PGP, hacia
`VC-Clients\Delhaize\RefLoader_Prod\data`.

Rutas confirmadas:
- Mapeo: `F:\Clients\Delhaize\RefLoader_Prod\fmt\employee.xml`
- Log del job: `F:\Clients\Delhaize\RefLoader_Prod\logs\JobLog.log`
- Log de rechazos declarado en el XML: `logs\employee_import_log.log`

Prefijo `pii-` confirmado. El task 2 del job, `Decrypt File(s)`, renombra la salida anteponiendo
`pii-`. El JobLog registra `Source file name: pii-pgp-DA_Employee_Info.dat`, seguido de
`App return code = 0` y `Load completed successfully`. Queda descartado el escenario de que el
`if exist` nunca encontrara el archivo.

Mapeo de `incident.Employee`, leido en `fmt\employee.xml`:
- `Misc1` toma la posicion 20 del archivo.
- `EmployeeID` toma la posicion 19 y es la unica columna con `key="true"`.
- `StoreNumber` toma la posicion 27.
- Operacion `upsert`, `Truncate` en false.
- Separador coma, calificador de texto comilla doble, `DataStartsAt` 2, `BatchSize` 5000,
  `BulkInsert` true.
- El mapeo salta las posiciones 5, 13, 21, 22 y 47.

`Misc1` no declara `default` ni `rule`. `Weight` si trae `default="0"` y las columnas de fecha
traen `rule="validdate"`.

Bandera de alerta. El bloque EMPLOYEE del .cmd trae `ANC_EXPECTEDDAILY=FALSE`. Con el archivo
ausente el script salta a `:LOAD_NOSOURCEFILE`, escribe una linea en el log y deja exit code 0.
La alerta hacia VisualCron solo se dispara con `EXPECTEDDAILY=TRUE`, que fuerza exit code 3. Un
dia sin feed de empleados reporta Success.

Medicion disponible y todavia sin correr. Contar en `JobLog.log` las lineas
`-EMPLOYEE- Source file not found to load` contra
`-EMPLOYEE- Reference files found in data folder`. La razon entre ambas da el porcentaje de dias
sin feed con fecha y hora de cada caso. Los tramos abiertos en la sesion son de julio 2025 y todos
salen exitosos.

Correcciones sobre afirmaciones previas de la misma sesion. El log de rechazos se llama
`logs\employee_import_log.log`, no `EMPLOYEE_Import_Log.log`. El archive no guarda solo cifrados.
La mascara `pgp*` captura tanto `pgp-` como `pii-pgp-`.

Hipotesis abierta, marcada como inferencia. Una fila con la columna 20 en blanco sobrescribe el
valor de `Misc1` guardado para ese empleado, porque el upsert usa `EmployeeID` como unica llave y
el mapeo no define default. Eso explicaria la intermitencia de la marca de division que reporta el
cliente. No esta verificado contra el ejecutable.

## Decisiones

Juan responde a Leigh Ann Stubbs con la posicion 20, el nombre del archivo y el formato. Nada mas.
Cierra la pregunta que ella hizo el 24 de agosto y el compromiso que Juan tomo el 26.

La respuesta al cliente perdio tres bloques por incumplir `cerebro-respuesta-cliente`: el parrafo
de causa, el ejemplo del empleado 5701349746 y la peticion del file layout. Quedaron tres
parrafos, una peticion y cero fechas. La peticion del layout salio porque Juan ya tiene el mapeo.

La nota interna lleva el mapeo completo, la fuente del XML, la hipotesis del upsert, las
posiciones 21 y 22 que el loader descarta y `ANC_EXPECTEDDAILY=FALSE`. Menciona a Jie Chen, que
pidio el dato el 21, y a Matthew Kamminga. Declara el uso de IA y la conversacion de Teams.

El ticket se queda en Under Support Review a nombre de Juan. Juan decide y pega, Jira no se toca
desde la sesion.

## Pendiente de verificar

Medir el conteo de `Misc1` vacio en `incident.Employee` antes de que ADUSA toque el feed. Sin esa
linea base no se demuestra que el cambio funciono ni se distingue entre feed y upsert si el
problema persiste.

Contar las lineas `-EMPLOYEE- Source file not found to load` al final de `JobLog.log` para medir
la intermitencia real del archivo.

Pedir a ADUSA el layout del archivo para saber si la marca de division viajo alguna vez en las
posiciones 21 o 22.

Confirmar la hipotesis del upsert contra el comportamiento del ejecutable.
