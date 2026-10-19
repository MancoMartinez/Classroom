-- Solo lectura. Base: sqldb-prd-wus2-arp-production-209-tbi-platform
SELECT 'level' AS src, UserName, CONVERT(varchar(20),SecurityID) AS value,
       CONVERT(varchar(10),Persistent) AS persistent, CONVERT(varchar(30),InsertedDateTime) AS inserted
FROM sso.SecurityLevelAssignments
WHERE UserName LIKE '%paul.bubelnik%' OR UserName LIKE '%chris.orth%' OR UserName LIKE '%chaz.hyman%'
   OR UserName LIKE '%nancy.bolhoff%' OR UserName LIKE '%vincent.fortner%' OR UserName LIKE '%rachel.dill%'
UNION ALL
SELECT 'team', UserName, TeamName, CONVERT(varchar(10),Persistent), NULL
FROM sso.Teams
WHERE UserName LIKE '%paul.bubelnik%' OR UserName LIKE '%chris.orth%' OR UserName LIKE '%chaz.hyman%'
   OR UserName LIKE '%nancy.bolhoff%' OR UserName LIKE '%vincent.fortner%' OR UserName LIKE '%rachel.dill%'
UNION ALL
SELECT 'perm', UserName, GroupName, NULL, NULL
FROM sso.PermissionGroups
WHERE UserName LIKE '%paul.bubelnik%' OR UserName LIKE '%chris.orth%' OR UserName LIKE '%chaz.hyman%'
   OR UserName LIKE '%nancy.bolhoff%' OR UserName LIKE '%vincent.fortner%' OR UserName LIKE '%rachel.dill%'
ORDER BY UserName, src;
