-- RCS-28915 Goodwill Sacramento (382). SOLO SELECT.
-- Base de plataforma confirmada: sqldb-prd-wus2-arp-production-382-gos-platform
-- Ultima fila de SmartAlertProcess: 2026-08-31 17:43:49 UTC. Filas 7380, 7126 con goodwillsacto.org.
-- Si incident. falla: SELECT TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME IN ('SmartAlertProcess','Shoplifting','MasterCase');

-- 1. Filas por dia desde agosto
SELECT CAST(RunDate AS date) AS dia, COUNT(*) AS filas
FROM incident.SmartAlertProcess WHERE RunDate >= '2026-08-01'
GROUP BY CAST(RunDate AS date) ORDER BY dia;

-- 2. Ultimas 20 filas
SELECT TOP 20 * FROM incident.SmartAlertProcess ORDER BY RunDate DESC;

-- 3. Ultimos 60 casos con fecha y corridas de alerta
SELECT s.ShopliftingID, s.CaseNo, s.InProcess, m.CreatedDate,
       (SELECT COUNT(*) FROM incident.SmartAlertProcess p WHERE p.ShopliftingID = s.ShopliftingID) AS corridas
FROM (SELECT TOP 60 ShopliftingID, MasterCaseID, CaseNo, InProcess FROM incident.Shoplifting ORDER BY ShopliftingID DESC) s
JOIN incident.MasterCase m ON m.MasterCaseID = s.MasterCaseID
ORDER BY s.ShopliftingID DESC;

-- 4. Casos atascados
SELECT ShopliftingID, CaseNo, InProcess FROM incident.Shoplifting WHERE InProcess = 1;

-- 5. Estados de las corridas desde mediados de agosto
SELECT RunStatus, COUNT(*) AS filas FROM incident.SmartAlertProcess WHERE RunDate >= '2026-08-15' GROUP BY RunStatus;

-- 6. Alertas y filtro real, para comparar con la base legacy
SELECT ac.AlertConfigID, ac.StatusID, sac.AlertGroup, sac.BeginDate, sac.LPSystem, sac.Runquery
FROM incident.AlertConfig ac JOIN incident.SmartAlertConfig sac ON ac.AlertConfigID = sac.AlertConfigID;

-- 7. Alertas activas completas: Filters, FiltersSQL, fechas de modificacion si existen
SELECT * FROM incident.AlertConfig WHERE AlertConfigID IN (10,12,13,14,16);
SELECT * FROM incident.SmartAlertConfig WHERE AlertConfigID IN (10,12,13,14,16);

-- 8. En una base de plataforma de un cliente que SI recibe alertas (Vitamin Shoppe 433, ADUSA 441 o Vallarta 432):
--    SELECT name FROM sys.databases WHERE name LIKE '%-433-%';
--    Luego sobre esa base (si incident. falla, prueba dbo.):
SELECT TOP 5 ac.AlertConfigID, ac.StatusID, sac.AlertGroup, LEFT(sac.Runquery, 150) AS inicio_runquery
FROM incident.AlertConfig ac JOIN incident.SmartAlertConfig sac ON ac.AlertConfigID = sac.AlertConfigID
WHERE ac.StatusID = 1 AND sac.AlertGroup = 'Standard';

-- 9. Opcional. Operaciones registradas alrededor del corte (puede no cubrir cambios de alertas)
SELECT Operation, COUNT(*) AS filas FROM dbo.ChangeHistory
WHERE DateChanged >= '2026-08-28' AND DateChanged < '2026-09-03' GROUP BY Operation ORDER BY filas DESC;
