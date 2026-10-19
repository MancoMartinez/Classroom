# SBX work items, 8 oct 2026

Ryan DeVries compartio su branch rdevries-rcs29205 en el repo SnowTime (ADO apprissdevops / Sysrepublic Secure / SnowTime) para analisis. Desde la sesion no hay credenciales de ADO; para analizarlo hace falta el diff pegado o los archivos.
Riesgo de duplicar: Ryan con branch propio y Anushka revisando el mapeo. Se le pregunta a Ryan si comparte el branch con Anushka o hablan directo.

Para cerrar RCS-29205 hace falta: un solo enfoque Ryan/Anushka, deploy del forward fix, seed historico corrido, REBUILD_RANGE de ARDM_TENDER desde el 27 ago, regenerar work items del 24 ago al 27 sep, verificacion de Juan en Snowflake y Executive Workbench, y confirmacion de Manish. x_refundtoown y paid in/paid out no bloquean este ticket; seguimiento aparte.

Respuestas de Ryan, 8 oct: 1) cuanto recargar depende; hizo historia completa, pero Starbucks tiene 1 anio de retencion. 2) ambos schemas tienen historia completa antes del cutover; lo malo es desde la conversion. 3) rebuild desde la fecha de conversion para llenar bien. 4) no cree que FALSE vs NULL afecte, ambos boolean. 5) paid in/out probablemente mismo problema, no lo reviso. Pregunta si el equipo SnowTime ayuda: si, Anushka.
Accion: confirmar a Ryan y pasar branch y notas a Anushka y Adarsh en el chat grupal; preguntar si asignarle el ticket.
