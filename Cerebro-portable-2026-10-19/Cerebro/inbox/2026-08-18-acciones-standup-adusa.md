# Acciones del standup ADUSA — 18 ago 2026

## Tuyos, del tracker

**RCS-28123 Asignación de casos.** El fix llegó a producción el 17. Está en verificación, pero
para verificarlo hay que aprobar un registro real en producción y eso necesita permiso de ADUSA.
Confirma si ya lo dieron antes de intentar la prueba.

**RCS-28124 Adjuntos.** Pasa a staging hoy, con dos despliegues porque el release branch trae
cosas extra. No lo cierres hasta que salga el segundo.

**RCS-28021 Izenda.** Confirmado que el scheduler corre, el correo llegó a las 8:12 a.m. Lo que
sigue roto es que algunos CSV llegan sin datos. Ese es el síntoma que hay que aislar ahora, no
el scheduler.

**RCS-28353 Editar location data, 502.** Los fixes de rendimiento de Ripp llegaron a producción
la noche del 17. Toca retest del update de perfil de tienda con ADUSA.

**RCS-28364 Brian Somsky.** Registro actualizado el 14. Esperando el retest del usuario.
Ojo: Anthony Powell se reportó el 14 con el mismo síntoma y no está en ningún lado todavía.

## Sin dueño, hay que asignarlos hoy

**RCS-28413 Izenda con datos incorrectos.** El más urgente por reputación: el reporte Interview
by Source de Food Lion Central Division pasó de más de 270 casos a 66, y los managers ya
recibieron la versión de 66. Verifica el conteo real de Central Division contra el reporte antes
de que alguien tome una decisión con ese dato.

**RCS-28415 Usuarios nuevos no pueden crear casos.** Ryan Cummings de Stop & Shop. Chris se lo
pidió a Gina en la llamada. Confirma que Gina lo tomó o queda huérfano.

## Dependencias de otros que conviene vigilar

- Kiran: los 3 usuarios restantes del remapeo, prometidos para hoy en la tarde.
- RCS-28196: bloqueado en permisos de ALTER, depende de una llamada con John.
- RCS-28161: probado en test, todavía no está en el release branch.

## Punto de proceso que quedó abierto

Nadie resolvió si el "Resolved" del tracker lo escribe el cliente o debe salir del estado de
Jira. Hoy pueden contradecirse. Vale la pena cerrarlo con Chris.
