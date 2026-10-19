# Explicación escrita de Matt en el chat, aportada por Juan

16 octubre 2026. Juan confirma que Matt publicó el siguiente texto. No se dispone de enlace o identificador del mensaje. Es evidencia aportada por Juan, no lectura independiente del chat.

ok, so SSO+ process works in this way.
Customer sends over a files for teams. This file contains the team and the user (email address)
We truncate and load this file into sso.teams table
We then replicate the data from the file into the sso.SecurityLevelAssignments table doing a look up on the teams text to the securityid number and save the number into the table.
this should only ever produce one row per user in this table.
this value should then be used on a user whenever they log in via sso

Cambio del plan: Matt cumplió el escrito que ofreció. Ya no pedirle que lo redacte. Validar CSV de teams, tabla sso.teams, lookup textual a ID, fila de SecurityLevelAssignments y uso al iniciar sesión. Una fila por usuario es comportamiento esperado descrito, no una cardinalidad comprobada en producción. Revisar cómo trata asignaciones manuales Persistent sin suponer que cualquier fila adicional es un defecto.

El mensaje no explica el prefijo 9, no prueba recepción de un archivo concreto ni cambia la escalación Izenda. No es una instrucción de ejecutar TRUNCATE: ese es el comportamiento del cargador descrito por Matt. El agente y las consultas propuestas permanecen en solo lectura.

Borradores afectados: la nota interna de RCS-29469 anterior queda obsoleta, sustituida por comentario-interno-v2. Se actualizan anexo y paso a paso para retirar el escrito de Matt de pendientes. La nota de RCS-29445 conserva su alcance.
