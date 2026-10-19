RCS-28256. Resultado de la consulta al feed, 14 oct 2026.

Que pasa
Los seis usuarios (Paul Bubelnik Jr, Chris Orth, Chaz Hyman, Nancy Bolhoff, Vincent Fortner, Rachel Dill) tienen en sso.SecurityLevelAssignments SecurityID 5, Persistent NULL, InsertedDateTime Oct 13 2026 10:42AM. Los seis tienen team Location Manager y permission group ApprissCase Users.

Causa
Descartado para estos seis: no estan fuera del feed. Persistent NULL en todos: ninguno tiene override manual en SSO+. Chris Orth tiene Location Manager aplicado a mano en el Portal el 12 oct y no aparece como override aqui, asi que el Portal escribe en otra tabla. HIPOTESIS: el nivel esta en el feed pero no se copio a la cuenta del usuario (membership.Users.SecurityID e incident.LPUser2). Sin verificar.

Limite
InsertedDateTime es la hora de la carga diaria, que reemplaza todo, no la primera vez que llego el usuario. Esta consulta no dice si la fila existia cuando fallaron.

Que hago hoy
Corre el SELECT de ENG-7189 filtrado a los seis (esta en el chat) y comparo OldSystem_SecurityID, NewSystem_SecurityID y SecurityLevel_Name.

Precedentes
flujos/verificar-securityid-post-migracion.md

Actualizacion. SELECT de ENG-7189 filtrado a los seis dio 0 filas. Ese SELECT parte de incident.LPUser2, asi que 0 filas es compatible con que los seis no tengan fila en LPUser2 (puntero colgando, como Beverly y Francesca el 25 ago, ver bitacora/RCS-27941.md). HIPOTESIS, o base equivocada. Siguiente: mismo SELECT invertido, partiendo de membership.Users con DB_NAME() en la salida.

Resultado del SELECT invertido desde membership.Users, base sqldb-prd-wus2-arp-production-209-tbi-platform.
Los seis existen, Enabled, no borrados, con IncidentUserID 50405 a 50473, y NINGUNO tiene fila en incident.LPUser2.
membership.Users.SecurityID: Chaz Hyman 5, Chris Orth 5, Vincent Fortner 5. Nancy Bolhoff NULL, Paul Bubelnik Jr NULL, Rachel Dill NULL.
Lectura: la fila de LPUser2 faltante es comun a unos 267 usuarios, la mayoria sin reclamo (RCS-27941, 1 sep), asi que no discrimina. Lo que separa a los tres con Incident Security ID en blanco es SecurityID NULL en la cuenta, con nivel 5 presente en el feed. Chris Orth tiene 5 y igual falla: su bloqueo es la Hierarchy en blanco. HIPOTESIS sin verificar: por que el nivel del feed no se copio a la cuenta de Nancy, Paul y Rachel.
Pendiente: Hierarchy de Chris Orth en secure.LocationHierarchyUserAssignments. Si Juan aplico Location Manager a Paul el 28 sep y hoy esta NULL, el login lo revirtio.
