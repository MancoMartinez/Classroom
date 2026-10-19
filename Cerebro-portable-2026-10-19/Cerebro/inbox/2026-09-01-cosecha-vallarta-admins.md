# Cosecha Vallarta administradores — 2026-09-01
Fuente: sesion local_9d03ced8-75ba-4b99-8e9c-b3331ad76a4e, "Administradores de tickets Vallarta"

## Hallazgos verificados

- La promesa del jueves nacio en RCS-28165, no en el correo. Viraj Kansara escribio el 26 ago 03:12: "expected to be available on your Vallarta instance by Thursday". El 27 ago declaro "the fix has now been released to production". El 28 ago 04:16 el ticket paso a Resolution Suggested sin comentario. Noemi lo contradice hoy.
- RCS-28165 arrastra dos defectos distintos. Filtros que se resetean. Export que devuelve un stub HTML de 20 B.
- El reporte de Noemi, "not showing reports", admite tres lecturas: visor sin datos, export roto, lista de reportes vacia por permisos. La tercera es lo que RCS-28572 dejo abierto. Hay que preguntarle que ve en pantalla antes de reabrir por el motivo equivocado.
- El export de Vallarta es ENG-5649, el Izenda global. Al 24 ago el cerebro registra que el sintoma A, export que no descarga, no tenia evidencia de fix. Solo el B.
- El Admin group de Noemi cae en el patron de unificacion de `reference_unificacion_patrones`. Se resuelve a mano y no se escala. RCS-28094 ya la habia restituido el 31 jul. Es reincidencia.
- Dos usuarias de Vallarta quedaron bloqueadas hoy despues de resetear contraseña. Noemi en RCS-28676 y Tatiana en RCS-28294 a las 10:38. En incognito si entran, asi que el fallo esta en la cookie de sesion y no en las credenciales. Sintoma nuevo.
- RCS-28676 esta sin assignee. Es el unico ticket de Vallarta sin dueño.
- RCS-28572 hay que devolverlo a Work in progress. Edwin lo dio por resuelto el 26 limpiando cache y hoy el cliente reporta lo mismo con dos casos nuevos.

## Sin ticket todavia

Tres temas del hilo de Vallarta no tienen ticket abierto:
- El Admin group de Noemi.
- Los auditores que no crean audits.
- La cuenta de Christian Torres.

Los dos ultimos caben dentro de RCS-28572.

## Tickets tocados

RCS-28165, RCS-28572, RCS-28637, RCS-28676, RCS-28294, RCS-28094, ENG-5649.
