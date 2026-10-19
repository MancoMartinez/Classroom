# Correo para Jim y acciones previas en Jira

Fecha: miércoles 26 ago 2026, 17:20 ET aprox.
Verificación: comentarios de Jira leídos hasta las 17:13 de hoy. Ese es el corte real, no el del tracker.
Baseline de comparación: tracker D6 enviado el lunes 24 ago.

## Respuesta a tu pregunta

Sí, verifiqué los comentarios más recientes. El último movimiento que entró en la revisión es de hoy 17:13
en RCS-28021, un comentario interno de ingeniería replicado por automatización.

Tus dos respuestas de hoy 17:06 quedaron registradas. RCS-28093 y RCS-28123. Ambas cubren el acuse sin
entregar hallazgo, que es lo correcto ahí. Una advertencia sobre RCS-28093. Le prometiste a Leigh Ann el campo
equivalente del employee feed hoy mismo. Ese compromiso arranca un reloj de 24 horas. Si mañana no tienes el
campo del equipo de datos, entra un comentario de avance igual.

## Paso 1. Ajustes de Jira antes de generar el documento

Ejecuta tú. Yo no escribo en Jira.

### Cambio de estado

RCS-28093. Figura en Under Customer Review. El cliente no tiene nada que verificar hasta que salga el release
del jueves 27. Bájalo a Work in progress. Si lo dejas en Under Customer Review, el documento va a contar un
Pending Ahold verification que no existe y Jim va a preguntar qué debe probar.

### Comentarios con más de 24 horas

RCS-28281. Última actividad 19 ago 18:45. Siete días. El tracker prometió por escrito publicar los conteos por
día de operación en el ticket. Publica los conteos actuales de 8/10 en adelante.

RCS-28304. Último comentario 21 ago 19:19. Cinco días. Se prometió confirmar antes del release del jueves si
el cambio entra. Confirma o niega hoy.

RCS-28021. Último comentario visible al cliente anterior al 24 ago. Todo el movimiento de hoy es interno de
ingeniería. Entra un comentario al cliente con el resultado de QA de esta tarde.

RCS-28482. Último comentario tuyo 24 ago 20:22. Cuarenta y cinco horas. Entra avance del diagnóstico del tab MISC.

RCS-28535. Último comentario tuyo 24 ago 20:18. Cuarenta y cinco horas. El cliente entregó el diagnóstico de
duración el 24 ago 14:11 y sigue sin respuesta técnica. Es el ticket más expuesto.

### Higiene menor

RCS-28356, RCS-28378, RCS-28364, RCS-28115, RCS-28053 y RCS-28109 están en Completed y no en Closed. El
documento los mapea igual a Resolved, así que no bloquea nada. Ciérralos cuando tengas espacio.

RCS-28447 no aparece en el tracker del lunes y sí en la versión del 19 ago. Decide si vuelve. Si vuelve, el
total pasa de 39 a 40.

## Paso 2. Documento

Cuando cierres los ajustes de arriba, avísame y genero el D6 nuevo con el mismo formato y las mismas reglas de
lenguaje. Conteos que va a mostrar con el estado de hoy: 32 resueltos, 0 pending Ahold verification,
0 awaiting Ahold input, 7 active with Appriss, total 39.

## Paso 3. Correo para Jim

Adjunta el documento. No repitas el contenido del documento en el cuerpo.

Subject: ADUSA support tracker, 8/26 status

Jim,

Tracker attached. I verified every ticket state against Jira this afternoon.

Five closed since Monday on your team's confirmation. RCS-28342, RCS-28196, RCS-28519, RCS-28533, RCS-28292.

Seven remain open with Appriss. RCS-28021, RCS-28093, RCS-28123, RCS-28281, RCS-28304, RCS-28482, RCS-28535.

Read four of those in detail. RCS-28021 failed our own export test this afternoon and I will confirm tomorrow
whether it makes the Thursday release. RCS-28123 now carries a separate item. The confirmation window with the
view and print option no longer appears after assignment. RCS-28535 moved to the upload size and timeout path
after Leigh Ann established that files of eleven minutes or more fail at 60 percent. RCS-28281 needs current
transaction counts from us and I will post them on the ticket tomorrow.

Two things from your side.

Confirm whether the automated employee feed carries Company for every employee record. April Valerio was
checking this for RCS-28093.

Send one of the failing video files or its exact size for RCS-28535. I want to reproduce the timeout against a
real file.

Regards,
Juan

## Compromisos que crea este correo

Tres, todos con fecha de mañana jueves 27.

Confirmar si RCS-28021 entra en el release.
Publicar los conteos de transacciones en RCS-28281.
Entregar el campo del employee feed en RCS-28093.

Si alguno no lo vas a cumplir mañana, sácalo del correo ahora.
