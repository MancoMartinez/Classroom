RCS-29451. Matt, 15 oct: "do you see anything in the logs as to why the securityId is not being sent? as long as they have the row in SSO+ it should really be set from there"

Dato que no encaja con "deberia ponerse desde ahi": Christi Winters tiene fila Persistent 1 nivel 5 desde 2026-04-17, entro 2026-07-14 19:36 UTC y su SecurityID sigue NULL.
Caso para logs: Shak Feaster, en los 49, login 2026-10-07 22:00:47 UTC (sso.ResponseLog Id 30759), cuenta NULL.

Plan de logs, solo lectura:
1. Fila de nivel de Shak y salida del proc.
2. Tablas de log en la base (sso.GetUserSecurityLevel escribe errores con secure.LogExceptionInsert).
3. Grafana, cliente 209, 7 oct 16:55 a 17:05 hora Bogota (22:00 UTC), usuario shak.feaster.

Resultado 15 oct: Shak Feaster fila nivel 5, Persistent NULL, carga 2026-10-13 10:42; proc devuelve 5 hoy. Su login (7 oct) fue antes del redespliegue del proc (9 oct 09:11 UTC) y no se sabe si su fila existia ese dia. No sirve como caso limpio.
Caso limpio: Rachel Dill, login 2026-10-13 19:23:49 UTC (ResponseLog 30893), despues de la carga del 13 y del redespliegue, proc devolvia 5, cuenta quedo NULL. Grafana: 13 oct 2:23 PM Bogota.
Tablas de log en la base: secure.Log, secure.UserActivityLogins, dbo.CommandLog, ops.RunLog, sdl.BatchInterfaceLog, incident.ActivityLog. Siguiente: columnas de secure.Log y secure.UserActivityLogins.

15 oct: secure.UserActivityLogins para Rachel solo trae 2026-10-14 19:58:29 (TimeZone America/New_York). Su login del 13 oct no aparece ahi; la tabla parece guardar solo el ultimo. Rachel volvio a entrar el 14, despues del arreglo manual: sirve para ver si el 5 se sostuvo.
secure.Log vacia en las dos ventanas del 13 oct con filtros rachel, Security, SSO.
Grafana (preferido por Juan, son los mismos logs que Control Panel): Explore, datasource grafanacloud-apprissretail-logs,
{service_name=~".+", deployment_environment="usprod"} | clientId="209" |~ "(?i)rachel\.dill"
Rango 13 oct 2:15 a 2:35 PM Bogota y 14 oct alrededor del login de las 19:58.

15 oct 13:40 Bogota: membership.Users despues del arreglo manual: Rachel 5 con LastLoginDate 2026-10-14 19:58:28.900; Paul 5 y Nancy 5 sin login nuevo. CONFIRMADO: el nivel manual se sostiene despues de un login (Rachel). LastLoginDate coincide con UserActivityLogins.LoginTime 19:58:29: las dos en UTC.
Grafana: mi consulta original tenia \. dentro de comillas dobles, error de LogQL. Correcta con backticks: ... |~ `(?i)rachel\.dill`. Corrida en la ultima hora, sin resultados. Falta correrla en 13 oct 14:20 a 14:28 Bogota.

Grafana export de Juan, 15 oct: las lineas son de 2026-10-15 18:25 a 18:39 UTC, no de la ventana del 13 oct; el rango de tiempo no se cambio. Nada de login. Contenido: tareas Hatr NotificationEmail, NettrackSmartAlert, RecommendationIndexing; errores 404 "index '209-recommendations' / '209-search' for service 'vss-prd-wus2-arp' was not found" (AzureVectorSearchRepository, otro tema, no se persigue aqui); SSR con NULL VirtualFilePath.
Formato util: las lineas secure-logs traen {clientId}, {component}, {sender}, {userToken}, {userId}, {message}; userId es el GUID de membership.Users.UserID. Buscar por GUID, no por email.

Grafana 15 oct, segundo export (13 oct 19:50 a 20:40 UTC, line limit 20): secuencia de login SSO para cada usuario (David Jackson II, Erin Molloy, Sam Fuentes, Alexis Post):
SsoService "Identified N SSO Extra permission groups to assign to the user ..." ; "Identified 1 SSO Extra teams to assign ..." ; "was added to user groups ..." ; "was added to teams ..." ; Saml2 "<user> logged on at ... UTC".
No aparece ninguna linea de security level / Incident Security ID en el flujo de login. HIPOTESIS: el paso que asigna el nivel no registra nada, o no corre.
Busqueda por GUID de Rachel (19CA9F1A-88C3-48DD-8457-26ABA1331FA0) sin resultados: los logs traen el GUID en minuscula y |= distingue mayusculas. Ademas el login de Rachel (19:23 UTC) quedo fuera del export por el line limit 20.

HALLAZGO 15 oct, Grafana login de Rachel Dill 2026-10-13 19:23:49 UTC (fue su PRIMER login, la cuenta se creo ahi):
19:23:49.582 SsoService Identified 1 SSO Extra permission groups
19:23:49.586 SsoService Identified 1 SSO Extra teams
19:23:49.641 MembershipService UserCreate: User Rachel Dill has been created
19:23:49.660 SsoService "Sso user created. User Data": SecurityID null, Groups [], Teams [], LocationHierarchyMembers [], PrimaryLocationID null
19:23:49.684 MembershipService added to ApprissCase Users, Basic Users
19:23:49.698 MembershipService added to Location Manager user team(s)
19:23:56.732 Saml2 logged on
Ninguna linea de security level. Su fila en sso.SecurityLevelAssignments (5) ya estaba desde la carga de 10:42 UTC. CONFIRMADO por log: en el alta por SSO se aplican grupos y team desde SSO Extra y el nivel no. HIPOTESIS: el paso de nivel no corre en el alta (creacion de usuario).
Otros usuarios creados por SSO segun Grafana: Theresa.Veasley@kgstores.com 10-15 17:17, Tamieko.Jones@kgstores.com 10-15 14:00, Doris.Mays@kgstores.com 10-14 20:00, Brett.Virtue@menswearhouse.com 10-14 19:47, Alexis.Post@menswearhouse.com 10-13 19:22, Chris.Orth@tailoredbrands.com 10-12 19:21, Jordan.Shields@menswearhouse.com 10-11 20:44, Teegan.Baker@kgstores.com 10-10 17:58, Ashley.N.Carter@kgstores.com 10-09 20:24.
Chris Orth se creo el 12 oct 19:21 UTC. A las 19:24:52 UTC hay CryptographicException en Saml2Verification.Execute (Saml2Verification.cs linea 55): posible intento fallido de Chris, sin confirmar.

PATRON 15 oct, usuarios creados por SSO del 9 al 15 oct (alta segun Grafana vs LastLoginDate):
Con nivel 5 (volvieron a entrar despues del alta): Alexis Post alta 10-13 19:22:23, ultimo 19:50:47; Ashley N Carter 10-09 20:24:16 / 20:27:23; Jordan Shields 10-11 20:44:20 / 20:50:28; Teegan Baker 10-10 17:58:30 / 18:00:39; Theresa Veasley 10-15 17:17:42 / 17:46:18.
NULL (su unico login fue el del alta): Brett Virtue 10-14 19:47:05 / 19:47:05; Doris Mays 10-14 20:00:25 / 20:00:25; Tamieko Jones 10-15 14:00:02 / 14:00:02. Rachel Dill igual hasta el arreglo manual.
Los 8 con nivel 5 en el feed. 9 de 9 consistentes: el login que crea la cuenta no aplica el nivel de SSO+; el siguiente login si. CONFIRMADO en 9 casos, falta medirlo en los 49.
Consecuencia practica: un segundo login deberia resolverlo sin arreglo manual. Sin probar en los 49.
Borrador inbox/2026-10-15-rcs-29451-teams-matt-logs.md queda OBSOLETO, reemplazado por -v2.
15 oct: Matt confirma que el nivel debe aplicarse en el alta y en logins siguientes; pide mandar a Shandana para ENG nuevo. Borradores: comentario-interno, teams-shandana, respuesta-colton de RCS-29451.
