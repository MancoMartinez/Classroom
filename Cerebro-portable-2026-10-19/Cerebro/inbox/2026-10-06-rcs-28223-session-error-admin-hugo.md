# RCS-28223 6 oct: 14283 entra, el admin de Hugo sale con Session Error

Comentario de Hugo: NSN 14283 ya puede entrar. Su cuenta de administrador no.
Captura: apps.apprissretail.com/mcdonalds/nettrack/?id=L, "Session Error. Your Incident session could not be established. This is usually caused by a temporary account configuration issue."

Lectura
14283, reportado por el cliente. Entra tras el reset. Consistente con Password NULL como causa, pendiente de confirmar con LastLoginDate en la fila.
Admin de Hugo, distinto sintoma. El Session Error sale despues del handoff con Secure, es decir la autenticacion paso y falla la sesion de Incident. No es el "system error" al enviar password de las tiendas.
No resetear a ciegas. En RCS-28486 (McDonald's, 19 ago) un reset nuevo disparo el mismo error y complico el diagnostico.

Precedentes: RCS-28486 McDonald's (reset forzado, segundo login entra), RCS-28061 Stater Bros (ENG-7000, configuracion), RCS-29147 Prada (SecurityID, flujos/verificar-securityid-post-migracion.md), RCS-28977 Vallarta.

Bloque 1, solo SELECT. Falta el usuario exacto de Hugo, por eso filtra por nombre.
SELECT mu.UserName, mu.Email, mu.Locked, mu.Disabled, mu.Deleted, mu.ChangePassword, CASE WHEN mu.Password IS NULL THEN 1 ELSE 0 END AS PasswordNull, mu.LastPasswordReset, mu.LastLoginDate, mu.IncidentUserID, mu.SecurityID AS mu_securityid, lp.UserID AS lp2_userid, lp.LoginID AS lp2_loginid, lp.SecurityID AS lp2_securityid, lp.Inactive AS lp2_inactive, sec.SecurityLevel FROM membership.Users mu LEFT JOIN incident.LPUser2 lp ON lp.UserID = mu.IncidentUserID LEFT JOIN incident.LPSecurity sec ON sec.SecurityID = mu.SecurityID WHERE mu.LastName LIKE 'Cortez%' AND mu.FirstName LIKE 'Hug%';

Confirmar 14283:
SELECT UserName, CASE WHEN Password IS NULL THEN 1 ELSE 0 END AS PasswordNull, LastPasswordReset, LastLoginDate FROM membership.Users WHERE UserName = 'sca.14283@us.stores.mcd.com';

Lo que mira el resultado: PasswordNull, mu_securityid y lp2_securityid iguales y no NULL, SecurityLevel con nombre, lp2_userid igual a IncidentUserID, Deleted 0. OK con SecurityID NULL o SecurityLevel NULL es falso negativo (ENG-7312).

Pendiente tras el resultado: actualizar a Kiran y Matt (14283 confirmado, 19 cuentas con el mismo perfil, pregunta si se crearon sin password a proposito) y decidir el reset de Hugo.

## Actualizacion 6 oct
Juan confirma que la captura es de Hugo, la subio 1 min antes de su comentario de las 6:12 PM. Reloj de la captura 3:11 PM, zona de Hugo sin confirmar. El comentario ya no pide la hora, pide usuario y zona horaria.

## Correccion 6 oct, Control Panel de Hugo
Control Panel, Settings, Users: hugo.cortez@us.mcd.com, Locked False, Disabled False, Time Zone America/Los_Angeles, Last Login 10/6/2026 11:09:47 PM, Last Login Local 3:09:47 PM. La captura de Hugo marca 3:11 PM, 1 min despues del login. Login a Secure registrado, el Session Error sale despues. Usuario y zona ya conocidos, el comentario a Hugo no pide nada.
Nota: Last Login a Last Login Local son 8 horas, y el 6 oct Los Angeles esta en PDT (7 horas). Sin explicar, relevante si se cruza con una traza.

Bloque 1 corregido, filtro exacto:
SELECT mu.UserName, mu.Email, mu.Locked, mu.Disabled, mu.Deleted, mu.ChangePassword, CASE WHEN mu.Password IS NULL THEN 1 ELSE 0 END AS PasswordNull, mu.LastPasswordReset, mu.LastLoginDate, mu.IncidentUserID, mu.SecurityID AS mu_securityid, lp.UserID AS lp2_userid, lp.LoginID AS lp2_loginid, lp.SecurityID AS lp2_securityid, lp.Inactive AS lp2_inactive, sec.SecurityLevel FROM membership.Users mu LEFT JOIN incident.LPUser2 lp ON lp.UserID = mu.IncidentUserID LEFT JOIN incident.LPSecurity sec ON sec.SecurityID = mu.SecurityID WHERE mu.Email = 'hugo.cortez@us.mcd.com' OR mu.UserName = 'hugo.cortez@us.mcd.com';

## Resultado bloque 1, Hugo (6 oct)
UserName y Email hugo.cortez@us.mcd.com. Locked 0, Disabled 0, Deleted 0, ChangePassword 0, PasswordNull 0.
IncidentUserID 1000999 igual a lp2_userid 1000999. lp2_loginid igual a UserName. lp2_inactive 0.
mu_securityid 1, lp2_securityid 1, SecurityLevel 7 con nombre. Sin falso negativo.
LastLoginDate 2026-10-06 22:09:47.577. LastPasswordReset 2026-10-06 22:10:40.997, 53 s despues del login y antes de la captura de las 3:11 PM de Hugo (22:11 UTC).
Conclusion confirmada: todo lo de membership y LPUser2 esta sano. Descarta password, bloqueo, deshabilitado, llaves y SecurityID.
Conclusion confirmada: LastLoginDate se guarda en UTC. 22:09:47 UTC es 3:09:47 PM en Los Angeles (PDT), igual que Last Login Local de Control Panel. La columna Last Login de Control Panel suma una hora de mas (23:09). Resuelve la duda de 930: 2026-10-03 20:11:00 UTC.
Sin verificar: quien reseteo el password a las 22:10:40. Si no fue Juan, lo hizo Hugo o un flujo de Secure. LastLoginDate no cambio despues, asi que no ha vuelto a entrar desde el reset.
Patron cercano: RCS-28486 McDonald's, reset forzado, primer login con Session Error, segundo login entra.

Bloque 2, solo SELECT, patron RCS-29147:
SELECT UserName, SecurityID, Persistent, InsertedDateTime, UtcDateFrom, UtcDateTo FROM sso.SecurityLevelAssignments WHERE UserName = 'hugo.cortez@us.mcd.com' ORDER BY Persistent DESC, InsertedDateTime DESC;
EXEC sso.GetUserSecurityLevel @userName = 'hugo.cortez@us.mcd.com';

Si Hugo repite el login y sigue el Session Error, pasa a Under Engineering Review con comentario interno estilo RCS-29147 y aviso a Kiran por Teams, hora del fallo en UTC.

## Resultado bloque 2, Hugo (6 oct)
sso.SecurityLevelAssignments y sso.GetUserSecurityLevel devuelven vacio para hugo.cortez@us.mcd.com.
Confirmado: no hay nivel forzado que pise al entrar. Mismo resultado que RCS-29147. Vacio no discrimina, en RCS-27941 Francesca tambien daba vacio y fallaba igual que quien tenia nivel.
Estado: nada de lo medible desde SQL explica el Session Error. Siguiente es el reintento limpio de Hugo (comentario ya redactado). Si falla, Under Engineering Review con comentario interno estilo RCS-29147 y Teams a Kiran con la hora en UTC (22:09:47 del 6 oct para el login, mas la del reintento).

## Precedente para el reintento (6 oct)
No hay flujo escrito para Session Error en flujos/INDICE.md, solo el de SecurityID (ya corrido). Lo que hay en el cerebro:
RCS-28676 y RCS-28294, Vallarta 31 ago: tras resetear password sale Session Error y en incognito si entran. Apunta a cookie de sesion y no a credenciales.
RCS-28984 (17 sep), paso 2: probar en otro navegador, limpiar cookies, copiar la URL completa, sin pedir un reset nuevo.
RCS-28486 McDonald's: reset forzado, segundo login entra.
RCS-29147 (Enrique): cerrar sesion en Secure y entrar una vez mas, si falla pasa a Engineering.
El comentario a Hugo ahora pide incognito y, si repite, otro navegador. La URL ya esta en su captura (apps.apprissretail.com/mcdonalds/nettrack/?id=L).

## Decision 6 oct: no resetear a Hugo todavia
Primero el reintento en incognito y otro navegador (comentario ya redactado). Razones: el password existe y la cuenta no esta bloqueada, un reset no ataca el sintoma; RCS-28486 y RCS-28984 registran que un reset disparo el mismo Session Error; ya hay un reset a las 22:10:40 UTC y otro mas borra la evidencia de LastPasswordReset. El reset queda como opcion si incognito y otro navegador fallan y Engineering lo pide.
