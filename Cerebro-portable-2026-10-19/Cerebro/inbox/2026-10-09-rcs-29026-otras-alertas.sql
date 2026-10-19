-- RCS-29026: direcciones de las listas de alertas activas que coinciden con un gerente de tienda
-- pero con otras mayusculas. Gerentes = direcciones que aparecieron en CC de algun envio desde 2026-01-01.
USE [sqldb-prd-wus2-arp-production-441-dai-platform];
WITH cc AS (
 SELECT DISTINCT LTRIM(RTRIM(c.value)) AS Addr
 FROM incident.SmartAlertProcess p
 CROSS APPLY STRING_SPLIT(SUBSTRING(p.EmailAddresses, CHARINDEX(';', p.EmailAddresses) + 1, LEN(p.EmailAddresses)), ',') c
 WHERE CHARINDEX(';', p.EmailAddresses) > 0 AND p.RunDate >= '2026-01-01' AND LTRIM(RTRIM(c.value)) <> ''
), grp AS (
 SELECT sac.SmartAlertConfigID, sac.SmartAlertName, LTRIM(RTRIM(g.value)) AS Addr
 FROM incident.SmartAlertConfig sac
 JOIN incident.AlertConfig ac ON ac.AlertConfigID = sac.AlertConfigID
 CROSS APPLY STRING_SPLIT(ac.EmailGroup, ',') g
 WHERE ac.StatusID <> 0 AND LTRIM(RTRIM(g.value)) <> ''
)
SELECT DISTINCT grp.SmartAlertConfigID, grp.SmartAlertName,
 grp.Addr AS EnLaAlerta, cc.Addr AS ComoGerente
FROM grp
JOIN cc ON LOWER(grp.Addr) = LOWER(cc.Addr)
 AND grp.Addr COLLATE Latin1_General_CS_AS <> cc.Addr COLLATE Latin1_General_CS_AS
ORDER BY grp.SmartAlertName, grp.Addr;
