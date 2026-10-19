# HATR Scheduled Tasks y Durable Functions Monitor, rutas en USPROD

Verificado por Juan el 9 oct 2026 con su usuario.

Scheduled Tasks por cliente: https://usprod.apprissretailcloud.com/control/#/hatr/scheduled
Menu lateral, seccion Hatr: Hatr Stats, Hatr Scheduled Tasks, Hatr Trigger Task, Hatr Lock Diagnostics, Monitor.
Botones de la pagina: Cleaning Scheduled Tasks Locks, Cleaning User Tasks Locks. Por fila: Run Now, View Monitor, View Logs.
Columnas: Enabled, Sleeping, Sleeping Until UTC y en zona del cliente.

Durable Functions Monitor: https://usprod.apprissretailcloud.com/monitor
Task hubs: productionSystemTasks para lo programado, NotificationEmail_Scheduled vive ahi. productionUserTasks para exports y busquedas que dispara un usuario.
Instancia: https://usprod.apprissretailcloud.com/monitor/productionSystemTasks/durable-instances/<clientId>x<guid>
El monitor muestra los botones de accion deshabilitados. Solo lectura.

Uso: RCS-29021 Claire's 439 y RCS-29350 Wild Fork 354.
