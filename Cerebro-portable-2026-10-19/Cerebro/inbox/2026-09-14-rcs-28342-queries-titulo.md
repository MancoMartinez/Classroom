# RCS-28342, queries para corregir titulo de usuario nuevo y detectar otros

Usuario nuevo identificado por adjunto de Jira: Daniel Ketchum, daniel.ketchum@giantfood.com.

## Paso 1, ubicar al usuario y confirmar el sintoma

```sql
SELECT u.UserId, u.UserName, lp2.Title AS Lp2Title, u.JobDescription,
       ued.AttributeValue AS UedTitle
FROM membership.Users u
LEFT JOIN incident.LPUser2 lp2 ON lp2.LoginID = u.UserName
LEFT JOIN membership.UserExtensionData ued
    ON ued.UserId = u.UserId AND ued.AttributeName = 'Title'
WHERE u.UserName LIKE '%daniel.ketchum%' OR u.UserName LIKE '%Ketchum%';
```

Anota el UserName que devuelva. Si Lp2Title trae valor y UedTitle y JobDescription estan
vacios, es el mismo defecto de siempre.

## Paso 2, confirmar si ya corrio el cambio del 15 sep

```sql
SELECT UserId, UserName, JobDescription
FROM membership.Users
WHERE UserName = '1194761';
```

Ese es Anthony Lopez, ya corregido el 14 ago con el MERGE viejo hacia UserExtensionData.
Si JobDescription aparece vacio, el cambio de Kiran no entro todavia, usa el Paso 3A.
Si JobDescription ya trae "FT Lead Asset Protection Coordinator" sin que nadie lo haya
escrito a mano, el cambio ya esta activo, usa el Paso 3B.

## Paso 3A, fix viejo, MERGE hacia UserExtensionData

```sql
WITH Candidates AS (
    SELECT u.UserId, MAX(lp2.Title) AS Lp2Title
    FROM membership.Users u
    JOIN incident.LPUser2 lp2 ON lp2.LoginID = u.UserName
    LEFT JOIN membership.UserExtensionData ued
        ON ued.UserId = u.UserId AND ued.AttributeName = 'Title'
    WHERE u.UserName = '<UserName del Paso 1>'
      AND lp2.Title IS NOT NULL AND LTRIM(RTRIM(lp2.Title)) <> ''
    GROUP BY u.UserId
)
MERGE membership.UserExtensionData AS target
USING Candidates AS source
    ON target.UserId = source.UserId AND target.AttributeName = 'Title'
WHEN MATCHED AND (target.AttributeValue IS NULL OR LTRIM(RTRIM(target.AttributeValue)) = '')
    THEN UPDATE SET target.AttributeValue = source.Lp2Title
WHEN NOT MATCHED BY TARGET
    THEN INSERT (UserId, AttributeName, AttributeValue)
    VALUES (source.UserId, 'Title', source.Lp2Title);
```

## Paso 3B, fix nuevo, directo a JobDescription

```sql
-- primero revisa que no pises un dato real del cliente
SELECT UserId, UserName, JobDescription FROM membership.Users
WHERE UserName = '<UserName del Paso 1>';

-- si JobDescription viene vacio, aplica
UPDATE membership.Users
SET JobDescription = (
    SELECT MAX(Title) FROM incident.LPUser2 WHERE LoginID = membership.Users.UserName
)
WHERE UserName = '<UserName del Paso 1>'
  AND (JobDescription IS NULL OR LTRIM(RTRIM(JobDescription)) = '');
```

## Paso 4, cerrar

Pide a Leigh Ann que Daniel salga y vuelva a entrar. El titulo aparece tras el refresco de
sesion, no antes.

## Paso 5, detectar otros usuarios nuevos con el mismo sintoma

```sql
SELECT
    lu.EmployeeId, lu.FirstName, lu.UserID, lu.LoginID,
    lp2.Title AS Lp2Title, ued.AttributeValue AS UedTitle, u.JobDescription,
    CASE
        WHEN lp2.LoginID IS NULL THEN 'No LPUser2 row, LoginID no matcheo'
        WHEN lp2.Title IS NULL OR LTRIM(RTRIM(lp2.Title)) = '' THEN 'LPUser2 sin titulo'
        WHEN ued.UserId IS NULL AND (u.JobDescription IS NULL OR LTRIM(RTRIM(u.JobDescription)) = '')
            THEN 'LPUser2 tiene titulo, falta escribirlo'
        ELSE 'Revisar a mano'
    END AS Diagnostico
FROM incident.LPUser lu
JOIN membership.Users u ON u.UserName = lu.LoginID
LEFT JOIN incident.LPUser2 lp2 ON lp2.LoginID = lu.LoginID
LEFT JOIN membership.UserExtensionData ued
    ON ued.UserId = u.UserId AND ued.AttributeName = 'Title'
WHERE lu.Title IS NULL OR LTRIM(RTRIM(lu.Title)) = ''
ORDER BY Diagnostico, lu.UserName;
```

Este es el query original de Kiran, sin cambios. Cada fila con Diagnostico distinto de vacio
es un usuario mas con el mismo defecto. Repite el Paso 3A o 3B para cada uno.
