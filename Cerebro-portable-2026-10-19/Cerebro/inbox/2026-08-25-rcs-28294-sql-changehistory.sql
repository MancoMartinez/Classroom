/* ============================================================================
   RCS-28294 Vallarta, Smart Alerts. Consultas de Change History y timezone.
   Fecha: 2026-08-25
   Acceso: Azure Bastion > SSMS > Managed Instance sqlmi-prd-wus2-arp-001
   Login: jmartinez@trebu.co

   TODO ESTO ES SOLO LECTURA. Ni un UPDATE, ni un INSERT, ni un DELETE.

   OJO. incident.Audit* NO es esto. Ese es el modulo de Audits de Incident,
   auditorias de tienda: AuditMaster, AuditConfig, AuditMasterQuestion,
   AuditMasterStore, AuditKPIHistory. La traza de SAVE.CASE y VIEW.PAGE vive
   en la tabla ChangeHistory.
   ============================================================================ */


/* ---------------------------------------------------------------------------
   PASO 1. Encontrar la base de Vallarta
   Las bases se llaman sqldb-prd-wus2-arp-production-NNN-xxx-platform, donde
   NNN es el Client ID y xxx el codigo corto. El Client ID de Vallarta no esta
   registrado en el cerebro. Se saca de la URL de la app, que trae el patron
   /nettrack/LPMS/screens/incident/NNN/lpms/...
   --------------------------------------------------------------------------- */
SELECT name, database_id, state_desc
FROM sys.databases
WHERE state = 0
  AND database_id > 4
  AND name LIKE '%platform'
ORDER BY name;
GO


/* ---------------------------------------------------------------------------
   PASO 2. Ubicar la tabla y decidir el esquema
   Gotcha documentado por BJ Probert sobre AutoZone: los datos reales vivian en
   el esquema dbo y el esquema incident estaba vacio. No asumas cual es.
   Cuenta filas y deja que el numero decida.
   --------------------------------------------------------------------------- */
USE [sqldb-prd-wus2-arp-production-NNN-xxx-platform];
GO

SELECT  s.name                AS SchemaName,
        t.name                AS TableName,
        SUM(p.rows)           AS [RowCount]
FROM sys.tables t
JOIN sys.schemas s    ON s.schema_id = t.schema_id
JOIN sys.partitions p ON p.object_id = t.object_id AND p.index_id IN (0,1)
WHERE t.name IN ('ChangeHistory','CaseChanges','ActivityLog',
                 'WorkFlowHistory','WorkFlowTracking','UserSession','MasterCase')
GROUP BY s.name, t.name
ORDER BY [RowCount] DESC;
GO


/* ---------------------------------------------------------------------------
   PASO 3. Ver las columnas reales de ChangeHistory
   El modal muestra Operation, Date Changed, User Name, Case No y Case Data.
   Los nombres en base pueden no coincidir. Mapealos antes de escribir el WHERE.
   --------------------------------------------------------------------------- */
SELECT  c.column_id,
        c.name           AS ColumnName,
        ty.name          AS DataType,
        c.max_length,
        c.is_nullable
FROM sys.columns c
JOIN sys.types ty ON ty.user_type_id = c.user_type_id
WHERE c.object_id = OBJECT_ID('dbo.ChangeHistory')
ORDER BY c.column_id;
GO

SELECT TOP 20 * FROM dbo.ChangeHistory ORDER BY 1 DESC;
GO


/* ---------------------------------------------------------------------------
   PASO 4. El reloj del servidor
   Azure SQL Managed Instance corre en UTC. Si Local y Utc dan lo mismo, todo
   lo que se escribio con GETDATE() esta en UTC y la conversion la hace la app.
   Corre esto antes que nada, es la linea base de todo el analisis.
   --------------------------------------------------------------------------- */
SELECT  SYSDATETIMEOFFSET() AS ServerOffset,
        GETDATE()           AS ServerLocal,
        GETUTCDATE()        AS ServerUtc,
        DATEDIFF(MINUTE, GETUTCDATE(), GETDATE()) AS DeltaMinutos;
GO


/* ---------------------------------------------------------------------------
   PASO 5. El caso reportado
   --------------------------------------------------------------------------- */
SELECT  MasterCaseID,
        CaseNumber,
        CaseStage,
        CreatedBy,
        CreateDate,
        CaseOwnerID,
        CaseLastSavedByID,
        ApprovedByID
FROM dbo.MasterCase
WHERE CaseNumber = '2026-ADUP-40-96';
GO


/* ---------------------------------------------------------------------------
   PASO 6. La traza completa, ascendente
   La captura del modal trae 23 eventos y el mas viejo es un SAVE.CASE del
   8/11/2026 a las 12:23 AM. Confirma aca que sean 23 y que el primero coincida.
   Ajusta el nombre de la columna de caso segun lo que devolvio el paso 3.
   --------------------------------------------------------------------------- */
SELECT  Operation,
        DateChanged,
        UserName,
        CaseNo,
        CaseData
FROM dbo.ChangeHistory
WHERE CaseNo = '2026-ADUP-40-96'
ORDER BY DateChanged ASC;
GO


/* ---------------------------------------------------------------------------
   PASO 7. LA CONSULTA QUE RESUELVE EL TICKET
   Compara el valor crudo contra las dos conversiones posibles.
   AT TIME ZONE 'Pacific Standard Time' usa el ID de Windows, que SI aplica
   DST, asi que en agosto devuelve PDT, UTC menos 7.

   Como se lee el resultado:
   - Si Raw sale 2026-08-11 00:23, el modal pinta UTC crudo sin convertir y el
     reporte con su 8/10 es el que esta bien. Defecto en Change History.
   - Si Raw sale 2026-08-10 17:23, el modal esta sumando horas de mas.
   - Si ComoPacifico da 8/10 5:23 PM, esa es la hora real de reloj de pared y
     confirma que el guardado cruzo medianoche UTC.
   --------------------------------------------------------------------------- */
SELECT  ch.Operation,
        ch.UserName,
        ch.DateChanged                                          AS Raw,
        CAST(ch.DateChanged AS datetime2) AT TIME ZONE 'UTC'
             AT TIME ZONE 'Pacific Standard Time'               AS ComoPacifico,
        DATEPART(HOUR, ch.DateChanged)                          AS HoraCruda,
        ch.CaseData
FROM dbo.ChangeHistory ch
WHERE ch.CaseNo = '2026-ADUP-40-96'
ORDER BY ch.DateChanged ASC;
GO


/* ---------------------------------------------------------------------------
   PASO 8. Timezone de los dos usuarios
   Vianney Valdez guarda el caso y es quien renderiza el modal.
   Fernando Torres es el sujeto y David lo midio con TimeZone UTC y
   LastLoginDate NULL. Verificalo tu mismo, no lo des por bueno.
   --------------------------------------------------------------------------- */
SELECT  UserId,
        UserName,
        TimeZone,
        LastLoginDate,
        CreateDate
FROM membership.Users
WHERE UserName LIKE '%valdez%'
   OR UserName LIKE '%torres%';
GO


/* ---------------------------------------------------------------------------
   PASO 9. Reproducir el conteo de David
   El reporto 419 cuentas, 308 en UTC todas con LastLoginDate NULL, y una tanda
   de migracion con CreateDate 2026-07-30 17:41:06.613. Si los numeros no dan,
   su analisis parte de otra base y hay que revisarlo antes de citarlo.
   --------------------------------------------------------------------------- */
SELECT  TimeZone,
        COUNT(*)                                                   AS Cuentas,
        SUM(CASE WHEN LastLoginDate IS NULL THEN 1 ELSE 0 END)     AS SinLoginNunca,
        MIN(CreateDate)                                            AS PrimerAlta,
        MAX(CreateDate)                                            AS UltimaAlta
FROM membership.Users
GROUP BY TimeZone
ORDER BY Cuentas DESC;
GO


/* ---------------------------------------------------------------------------
   PASO 10. Guardados contra alertas, la evidencia del defecto A
   Saca todos los SAVE.CASE del ultimo mes con su hora UTC y su hora Pacifico.
   Marca los que cayeron despues de las 5 PM PT, que son los que cruzan
   medianoche UTC. Si las quejas de Tatiana se concentran ahi, la frontera de
   fecha UTC explica el retraso.
   --------------------------------------------------------------------------- */
SELECT  ch.CaseNo,
        ch.UserName,
        ch.DateChanged                                          AS UtcCrudo,
        CAST(ch.DateChanged AS datetime2) AT TIME ZONE 'UTC'
             AT TIME ZONE 'Pacific Standard Time'               AS HoraPacifico,
        CASE WHEN CAST(ch.DateChanged AS date)
                  <> CAST(CAST(ch.DateChanged AS datetime2) AT TIME ZONE 'UTC'
                          AT TIME ZONE 'Pacific Standard Time' AS date)
             THEN 'CRUZA MEDIANOCHE UTC' ELSE '' END            AS Frontera
FROM dbo.ChangeHistory ch
WHERE ch.Operation = 'SAVE.CASE'
  AND ch.DateChanged >= DATEADD(DAY, -30, GETUTCDATE())
ORDER BY ch.DateChanged DESC;
GO


/* ---------------------------------------------------------------------------
   PASO 11. Si no aparece log de envio de la alerta
   Busca cualquier tabla que huela a alerta antes de pedirsela a Engineering.
   --------------------------------------------------------------------------- */
SELECT  s.name AS SchemaName, t.name AS TableName, SUM(p.rows) AS [RowCount]
FROM sys.tables t
JOIN sys.schemas s    ON s.schema_id = t.schema_id
JOIN sys.partitions p ON p.object_id = t.object_id AND p.index_id IN (0,1)
WHERE t.name LIKE '%Alert%'
   OR t.name LIKE '%Notif%'
   OR t.name LIKE '%Email%'
   OR t.name LIKE '%Queue%'
GROUP BY s.name, t.name
ORDER BY [RowCount] DESC;
GO
