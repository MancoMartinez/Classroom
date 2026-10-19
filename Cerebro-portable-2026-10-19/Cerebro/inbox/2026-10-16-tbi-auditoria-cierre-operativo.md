# TBI: auditoría después de las actualizaciones de Juan

16 octubre 2026. Juan confirma que publicó la lista de tickets en el chat y respondió a Matt. Se aceptan ambas acciones como realizadas. No se consultó Teams.

## Completado

RCS-29445: Under Engineering Review, Shandana Khan. Nota interna de Juan 3398413 publicada el 16 octubre; contiene reproducción, evidencia, límites, conversación y preguntas. Respuesta pública 3398421 publicada: confirma escalación y promete update cuando llegue feedback. Leídos cinco comentarios de cinco.

[RCS-29445: nota interna](https://trebuco.atlassian.net/browse/RCS-29445?focusedCommentId=3398413)
[Respuesta a Colton](https://trebuco.atlassian.net/browse/RCS-29445?focusedCommentId=3398421)

RCS-29469: Work in progress, Juan. Nota interna 3398422 publicada con los cinco ejemplos, Matt, archivos y pendientes técnicos. Respuesta pública 3398439 publicada: archivos revisados, investigación en curso, sin más peticiones al cliente por ahora. Leídos siete comentarios de siete.

[RCS-29469: nota interna](https://trebuco.atlassian.net/browse/RCS-29469?focusedCommentId=3398422)
[Respuesta a Colton](https://trebuco.atlassian.net/browse/RCS-29469?focusedCommentId=3398439)

Completado por declaración de Juan: lista de RCS en chat y respuesta a Matt. Explicación escrita de Matt recibida previamente. Quedan resueltos los pendientes de comunicación y la escalación específica que pidió J.R. No se necesita repetir comentarios ni adjuntar obligatoriamente el anexo.

Estados complementarios verificados: RCS-29451 Accepted into Development, Shandana. ENG-10069 y ENG-9990 Backlog, sin asignar. El estado del RCS no prueba que un desarrollador ya haya tomado su ENG.

## Qué sigue de Juan

1. Validación técnica de RCS-29469. Comparar los cinco usuarios con sso.teams, nivel efectivo de SSO+, cuenta y momento del login. El SELECT del anexo no se ejecutó en esta sesión. Sin esos resultados no consta resuelto el caso ni se debe cerrar.
2. Con los resultados, aportar al expediente existente RCS-29451/ENG-10069 los casos con nivel disponible antes del login y cuenta vacía. Separar los que no tienen nivel de salida de carga y los que requieren alcance de jerarquía superior. No crear otro ENG por el mismo síntoma automáticamente.
3. Continuar la pregunta de Chris. El CSV del 14 trae SSU y 2005; falta archivo consumido y transformación del lote histórico del 13, y confirmación de que puede crear incidentes. No atribuir el prefijo al cliente sin esa trazabilidad.
4. Dar seguimiento a las respuestas de Matt que Juan ya solicitó. No reenviar preguntas iguales. Incorporar cada respuesta nueva cuando llegue.
5. Seguimiento de rendimiento: verificar con Shandana quién toma la revisión y cuándo será el próximo update. La lectura de enlaces de RCS-29445 solo muestra Duplicate hacia RCS-29060; no aparece un ENG nuevo enlazado. No demuestra que no exista un ENG en otro lugar. Aclarar cobertura y vínculo con Shandana, sin repetir transiciones ni crear ENG manualmente.

RCS-29469 continúa bajo responsabilidad de Juan y tiene trabajo técnico pendiente. RCS-29445 ya se entregó a Ingeniería; a Juan le queda seguimiento y comunicación del feedback.

El tipo Relates existe en Jira; RCS-29469 todavía no tiene relaciones formales. Su nota ya contiene referencias a RCS-29451/ENG-10069. Enlazar formalmente es orden documental, no un bloqueo que obligue a rehacer lo publicado.

## Siguiente paso

Juan: ejecutar la comparación de los cinco usuarios y guardar resultados con fecha; después elegir qué tramo requiere investigación.
Shandana: confirmar owner, vínculo ENG y próximo update de rendimiento; evitar otro ENG si ya está cubierto.
Matt y responsable actual del cargador por identificar: incorporar respuestas pendientes y seguir la transformación de Chris.
