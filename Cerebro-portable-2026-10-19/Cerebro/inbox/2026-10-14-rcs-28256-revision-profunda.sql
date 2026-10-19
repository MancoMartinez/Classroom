-- Solo lectura. Base sqldb-prd-wus2-arp-production-209-tbi-platform
-- 1. Cuando se modifico el proc y que dice hoy
SELECT name, create_date, modify_date FROM sys.objects WHERE object_id = OBJECT_ID('sso.GetUserSecurityLevel');
SELECT OBJECT_DEFINITION(OBJECT_ID('sso.GetUserSecurityLevel')) AS Definicion;
-- 2. Que devuelve el proc hoy para los tres
EXEC sso.GetUserSecurityLevel @userName = 'paul.bubelnikjr@menswearhouse.com';
EXEC sso.GetUserSecurityLevel @userName = 'nancy.bolhoff@menswearhouse.com';
EXEC sso.GetUserSecurityLevel @userName = 'rachel.dill@menswearhouse.com';
-- 3. Ultimo login de los seis (UTC)
SELECT UserName, LastLoginDate, SecurityID FROM membership.Users
WHERE UserName IN ('chaz.hyman@menswearhouse.com','chris.orth@tailoredbrands.com','nancy.bolhoff@menswearhouse.com',
                   'paul.bubelnikjr@menswearhouse.com','rachel.dill@menswearhouse.com','vincent.fortner@menswearhouse.com')
ORDER BY LastLoginDate;
-- 4. Alcance: usuarios con nivel en el feed y sin nivel en su cuenta, por mes del ultimo login
SELECT CONVERT(char(7), u.LastLoginDate, 120) AS MesUltimoLogin, COUNT(*) AS Usuarios,
       SUM(CASE WHEN u.SecurityID IS NULL THEN 1 ELSE 0 END) AS SinNivelEnCuenta
FROM membership.Users AS u
WHERE u.LastLoginDate IS NOT NULL
  AND EXISTS (SELECT 1 FROM sso.SecurityLevelAssignments AS s WHERE s.UserName = u.UserName AND s.SecurityID > 0)
GROUP BY CONVERT(char(7), u.LastLoginDate, 120)
ORDER BY MesUltimoLogin;
-- 5. Frescura del feed
SELECT 'level' AS tabla, MAX(InsertedDateTime) AS ultima_carga FROM sso.SecurityLevelAssignments
UNION ALL SELECT 'location', MAX(InsertedDateTime) FROM sso.LocationHierarchyMembers;
-- 6. Existe la ubicacion de Chris (comparada con la de Vincent)
SELECT * FROM place.Location WHERE LocationID IN (90002005, 40001405);
