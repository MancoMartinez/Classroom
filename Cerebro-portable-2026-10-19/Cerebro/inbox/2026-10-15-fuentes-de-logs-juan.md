Fuentes de logs que Juan tiene disponibles. 15 oct 2026. Dicho por Juan.

1. Control Panel del tenant: seccion Incident Logs y seccion Logs.
2. Grafana.
3. Base del tenant por SSMS en bastion: secure.Log (UpdatedDateTime, LogID, MachineName, Component, Sender, MessageType, Message, UserID, UserToken, LogCount, MessageHash, InsertedDateTime), secure.UserActivityLogins (UserID, LoginTime, TimeZone), sso.ResponseLog (Id, InsertedDateTime UTC, ProviderID, Summary, Response con el XML SAML). Tambien existen dbo.CommandLog, ops.RunLog, sdl.BatchInterfaceLog, incident.ActivityLog, incident.EvidenceLog.
Ojo: las consultas de base de tenant se corren en SSMS dentro del bastion, no en Snowflake. En Snowflake falla con "session does not have a current database" porque sys.columns y OBJECT_ID son sintaxis de SQL Server.
Grafana muestra hora Bogota; la base guarda UTC, cinco horas mas (flujos/smart-alert-disparo-manual.md).
