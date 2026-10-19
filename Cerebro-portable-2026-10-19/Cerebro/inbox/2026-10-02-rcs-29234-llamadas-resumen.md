# RCS-29234 ADUSA, llamadas del 2 oct. Resumen

Que pasa: Leigh Ann agrego campos en Medical911 con Save and Build. El primer guardado funciono y el segundo quedo girando. Central Station Master guarda bien. Tras reiniciar NetTrack, Medical Incident guarda en Stop & Shop 9999. Servicio restaurado.

Causa, hipotesis: Save and Build deja un estado compilado obsoleto que solo limpia el reinicio. J.R. cree que bastaba reiniciar sin reconstruir pantallas. Kiran apunta a un campo borrado que la pantalla sigue pidiendo. Sin reproducir en test.

Evidencia:
Llamada 2, 00:29. Jim narra el Save and Build y el spinner.
Llamada 2, 02:31. El impacto va por pantalla de entrada de caso, no por case type.
Llamada 3, 12:13 a 17:11. Restart apps de NetTrack en 3 segundos y dos casos de prueba guardados.

Que hago hoy:
1. En un ambiente de test, nunca en el de Jim, guarda un caso para fijar la linea base.
2. En Screen Designer agrega un campo, Save and Build, y guarda un caso dos veces. Repite borrando el campo y agregando otro.
3. Graba la sesion y anota que campo aparece en el error.
4. Arregla la VPN antes del proximo incidente. Hoy Sebastian tuvo que compartir pantalla.

Precedentes: inbox/2026-10-01-rcs-29234-apoyo-sebastian.md e inbox/2026-10-02-rcs-29234-investigacion-teams.md. Transcripciones: inbox/2026-10-02-rcs-29234-llamadas-transcripcion.md y llamada3-transcripcion.md. Procedimiento de reinicio en inbox/2026-10-02-flujo-reinicio-nettrack.md.

Compromisos: ADUSA no hace Save ni Save and Build hasta nuevo aviso. J.R. manda grabacion, transcripcion y pasos de Leigh Ann a ingenieria y llama a Jim. Matt Kamminga vuelve el lunes 5 oct. J.R. baja la prioridad de Critical a High cuando todo este estable. J.R. pide a seguridad el lunes permiso de aprobacion de pipelines para soporte.

## Observaciones

La nota anterior decia no atribuir el origen a Jim. Ahora hay una secuencia reportada que dispara la falla. Falta reproducirla.
J.R. dijo ayer que fallaban todos los case types. Jim lo corrigio: Central Station Master sirve a muchos.
Que otros clientes no se quejen no prueba que el defecto no exista. Casi nadie edita formularios despues de configurarlos.
Solo Kiran, Matt y Chris aprueban pipelines de produccion. Con Matt de vacaciones y Chris en Londres, el reinicio dependio de Kiran.
Queda abierta la pregunta de Ryan sobre el timeout.
