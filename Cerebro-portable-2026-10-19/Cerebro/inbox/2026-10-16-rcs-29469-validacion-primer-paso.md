# RCS-29469: validación actual de cuentas aportada por Juan

16 octubre. Resultado de los SELECT que Juan ejecutó en el tenant. Datos completos: adjuntos/RCS-29469/2026-10-16-validacion-cuentas-juan.tsv. El agente no ejecutó SQL contra producción. No se aportó todavía SelectedDatabase/CheckedAtUTC del primer SELECT; conservar esa referencia si está disponible.

Hecho: los cinco usuarios existen, todos con AccountSecurityID NULL. Todos tienen una fila nivel 5, Persistent NULL, insertada 15 octubre 10:34:36. El último login de cada uno es anterior a esa inserción. Estas filas no demuestran disponibilidad del nivel en el login pasado, ni prueban un nuevo fallo de primer login. Tampoco excluyen que una carga anterior ya tuviera el mismo nivel; falta historial del lote o login.

Christi tiene además nivel 5 Persistent 1 desde 17 abril 01:12:29.873 y último login 14 julio 19:36:12. Es el ejemplo prioritario para investigar disponibilidad histórica y aplicación al login. Dos filas con el mismo ID no demuestran conflicto ni explican por sí solas la cuenta vacía. Falta revisar cómo el código vigente entonces resolvía esas asignaciones. No reactivar la hipótesis histórica descartada del filtro Persistent como causa actual sin nueva evidencia.

Corrección de vigencia: hay asignaciones insertadas el 15 octubre. El supuesto de feed detenido desde el 13 no es vigente. No se demuestra con este resultado que todos los archivos llegaron o que una carga del 16 esté completa.

Columnas reales de sso.teams aportadas: UserName nvarchar, TeamName nvarchar, InsertedDateTime datetime, Persistent bit, UtcDateFrom datetime, UtcDateTo datetime.

Hoy: ejecutar el SELECT de sso.teams para los cinco, con todas sus filas, fechas y Persistent. No pedir todavía otro login ni cambiar niveles antes de conservar evidencia. Siguiente consulta: inbox/2026-10-16-rcs-29469-validacion-teams.sql.

Notas publicadas 3398422 y 3398439 permanecen como historia. El límite de que no se había ejecutado validación fresca queda actualizado por estos resultados. Ningún comentario nuevo se preparó o publicó. El resto del seguimiento de carga, alcance de ENG-10069 y Chris sigue abierto.
