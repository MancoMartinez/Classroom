-- Solo lectura. Base 209-tbi. Versiones cortas, salida compacta.
-- A. Usuarios con nivel en feed y cuenta en NULL desde el 2 jul (una fila)
SELECT COUNT(*) n,STRING_AGG(CONCAT(u.UserName,'|',CONVERT(date,u.LastLoginDate),'|',s.SecurityID),'; ') x FROM membership.Users u JOIN sso.SecurityLevelAssignments s ON s.UserName=u.UserName AND s.SecurityID>0 WHERE u.SecurityID IS NULL AND u.LastLoginDate>='2026-07-02';
-- B. Ubicaciones del feed que no existen en place.Location
SELECT m.LocationID,COUNT(*) n,STRING_AGG(m.UserName,'; ') x FROM sso.LocationHierarchyMembers m WHERE NOT EXISTS(SELECT 1 FROM place.Location l WHERE l.LocationID=m.LocationID) GROUP BY m.LocationID;
-- C. Columnas de sso.ResponseLog (una fila)
SELECT STRING_AGG(name,', ') FROM sys.columns WHERE object_id=OBJECT_ID('sso.ResponseLog');
