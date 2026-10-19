# RCS-29146 queries de verificacion en la Platform DB de J Crew. Solo SELECT.

1. Contexto
SELECT DB_NAME() AS db, @@SERVERNAME AS server;

2. Forma de la tabla
SELECT TOP 5 * FROM workview.Workview ORDER BY ID DESC;

3. Abiertos por estado y asignacion
SELECT StatusID, CASE WHEN AssignedToUserID IS NULL THEN 'sin asignar' ELSE 'asignado' END AS asignacion, COUNT(*) AS Cnt, MIN(CreatedDateTime) AS Mas_viejo, MAX(CreatedDateTime) AS Mas_nuevo FROM workview.Workview WHERE StatusID <> 3 GROUP BY StatusID, CASE WHEN AssignedToUserID IS NULL THEN 'sin asignar' ELSE 'asignado' END ORDER BY StatusID;

4. Que son esos items
SELECT Headline, Category, StatusID, COUNT(*) AS Cnt FROM workview.Workview WHERE StatusID <> 3 GROUP BY Headline, Category, StatusID ORDER BY Cnt DESC;

5. Razones de abandono del tenant
SELECT DISTINCT EnumerationType, [Key], Value FROM secure.EnumerationReferenceData WHERE EnumerationType = 'WorkviewAbandonReason' ORDER BY [Key];
SELECT * FROM workview.AbandonReason ORDER BY ID;

6. Razones que J Crew ya uso
SELECT AbandonReasonID, AbandonReasonNotes, COUNT(*) AS Cnt FROM workview.Workview WHERE StatusID = 3 GROUP BY AbandonReasonID, AbandonReasonNotes ORDER BY Cnt DESC;

7. Existe algo llamado case item
SELECT TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE '%Case%';
SELECT TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE COLUMN_NAME LIKE '%Case%' ORDER BY TABLE_SCHEMA, TABLE_NAME;

Decision
Solo StatusID 0 y 1 en query 3: la hipotesis Work Items se sostiene. Avanza con el runbook sin preguntar al cliente.
Filas con StatusID 2 (AttachedToCase) o 4 (Investigating): no las toques sin avisar. Son las que podrian llamarse case items de verdad.
Query 7 devuelve una tabla tipo CaseItem: la hipotesis falla. Para y revisa antes de actuar.
Reason ID: usa uno que exista en las dos consultas de query 5. Un ID ausente de workview.AbandonReason rompio la generacion en H&M, RCS-28870.

RONDA 2 (tras resultados del 6 oct)

A. Alcance seguro, items con caso o factboard
SELECT StatusID, CASE WHEN CaseID IS NULL THEN 0 ELSE 1 END AS conCaso, CASE WHEN FactboardID IS NULL THEN 0 ELSE 1 END AS conFactboard, COUNT(*) AS Cnt FROM workview.Workview WHERE StatusID <> 3 GROUP BY StatusID, CASE WHEN CaseID IS NULL THEN 0 ELSE 1 END, CASE WHEN FactboardID IS NULL THEN 0 ELSE 1 END ORDER BY StatusID;

B. Como cierran los items desde el release del 16 jul
SELECT AbandonReasonID, StandardCompleteReasonID, COUNT(*) AS Cnt, MIN(AbandonedDateTime) AS Primero, MAX(AbandonedDateTime) AS Ultimo FROM workview.Workview WHERE StatusID = 3 AND AbandonedDateTime >= '2026-07-16' GROUP BY AbandonReasonID, StandardCompleteReasonID ORDER BY Cnt DESC;

C. A quien estan asignados los 61 abiertos con dueno
SELECT AssignedToUserID, StatusID, COUNT(*) AS Cnt, MAX(AssignedToDateTime) AS Ultima_asignacion FROM workview.Workview WHERE StatusID IN (1,4) GROUP BY AssignedToUserID, StatusID ORDER BY Cnt DESC;

RONDA 3 (6 oct 19:12, correccion)
Error Msg 156 en el backup: backup es palabra reservada de T-SQL, no sirve como alias. Error de compilacion, el batch entero no corrio. Usa el alias copia.

Resultados ronda 2: A confirma 699 (StatusID 0) y 52 (StatusID 1) sin caso ni factboard, y 9 (StatusID 4) con factboard. B vacia, ningun cierre desde el 16 jul. C: 61 items repartidos en 12 usuarios, ultima asignacion reciente el 10 sep (1 item).

1. Backup, idempotente
IF OBJECT_ID('workview.Workview_backup_20261006') IS NULL
    SELECT * INTO workview.Workview_backup_20261006 FROM workview.Workview;

SELECT (SELECT COUNT(*) FROM workview.Workview) AS origen,
       (SELECT COUNT(*) FROM workview.Workview_backup_20261006) AS copia;

2. Query D, si StandardCompleteReasonID se usa alguna vez
SELECT AbandonReasonID, StandardCompleteReasonID, COUNT(*) AS Cnt FROM workview.Workview WHERE StatusID = 3 GROUP BY AbandonReasonID, StandardCompleteReasonID ORDER BY Cnt DESC;

SELECT TOP 20 ID, AbandonReasonID, StandardCompleteReasonID, AbandonedDateTime, ActionedDateTime FROM workview.Workview WHERE StatusID = 3 ORDER BY ActionedDateTime DESC;

3. UPDATE, solo si el backup cuadra. Un solo batch. Esperas 751 filas.
BEGIN TRANSACTION;

SELECT ID
INTO workview.Workview_abandoned_20261006
FROM workview.Workview
WHERE StatusID IN (0,1) AND CaseID IS NULL AND FactboardID IS NULL;

UPDATE wv
SET wv.StatusID = 3,
    wv.AbandonReasonID = 8,
    wv.AbandonReasonNotes = N'Mass completed per customer request (RCS-29146).',
    wv.AbandonedDateTime = GETUTCDATE()
FROM workview.Workview AS wv
INNER JOIN workview.Workview_abandoned_20261006 AS a ON a.ID = wv.ID
WHERE wv.StatusID IN (0,1) AND wv.CaseID IS NULL AND wv.FactboardID IS NULL;

SELECT @@ROWCOUNT AS filas_actualizadas;
-- 751: COMMIT TRANSACTION;
-- otro numero: ROLLBACK TRANSACTION;

Si la query D muestra StandardCompleteReasonID poblado para AbandonReasonID 8, agrega la linea wv.StandardCompleteReasonID = <valor> al SET.

RONDA 4 (6 oct 19:16, sustituye el script de la ronda 3)
Hallazgos. El login no puede CREATE TABLE (Msg 262), asi que SELECT INTO a tabla de usuario falla. Query B vacia no significaba sin cierres: los cierres dejan AbandonedDateTime NULL y llenan ActionedDateTime. Query D: reason 8 siempre con StandardCompleteReasonID 3.

0. Transaccion colgada tras el Msg 262
SELECT @@TRANCOUNT AS abiertas;
-- si es 1 o mas: ROLLBACK TRANSACTION;

1. Permiso de UPDATE
SELECT HAS_PERMS_BY_NAME('workview.Workview', 'OBJECT', 'UPDATE') AS puede_update;

2. Backup como CSV, 751 filas. Guardar en adjuntos/RCS-29146/backup-pre-update-20261006.csv
SELECT ID, StatusID, AssignedToUserID, AbandonReasonID, AbandonReasonNotes, AbandonedDateTime, ActionedDateTime, StandardCompleteReasonID FROM workview.Workview WHERE StatusID IN (0,1) AND CaseID IS NULL AND FactboardID IS NULL ORDER BY ID;

3. UPDATE
BEGIN TRANSACTION;
UPDATE workview.Workview
SET StatusID = 3,
    AbandonReasonID = 8,
    AbandonReasonNotes = N'Mass completed per customer request (RCS-29146).',
    ActionedDateTime = GETUTCDATE(),
    StandardCompleteReasonID = 3
WHERE StatusID IN (0,1) AND CaseID IS NULL AND FactboardID IS NULL;
SELECT @@ROWCOUNT AS filas_actualizadas;
-- 751: COMMIT TRANSACTION;
-- otro numero: ROLLBACK TRANSACTION;

4. Verificacion
SELECT StatusID, COUNT(*) AS Cnt FROM workview.Workview WHERE StatusID <> 3 GROUP BY StatusID;
SELECT COUNT(*) AS marcados FROM workview.Workview WHERE AbandonReasonNotes = N'Mass completed per customer request (RCS-29146).';

Revert, si hiciera falta: filtra por esa nota y restaura StatusID, AbandonReasonID, notas y fechas desde el CSV.
