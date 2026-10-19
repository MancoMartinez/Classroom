RCS-28671. Platform DB THD, sqldb-prd-wus2-arp-production-085-thd-platform. Solo SELECT.
Columnas confirmadas en sesiones previas: ID, Headline, LocationID, CreatedDateTime, CountOfEvents, PotentialValue, StatusID. fti.AnalysisResults se une por WorkViewID. Lo demas va con * para no adivinar nombres.

Q1. Los 17 originales ya no deberian existir.

SELECT ID, Headline, LocationID, CreatedDateTime
FROM workview.Workview
WHERE ID IN (248114,248116,248117,248118,248119,248132,248133,248138,248142,248144,248148,248154,248158,248159,248160,248161,248162);

Q2. Los reemplazos, creados desde el viernes en las 17 tiendas.

SELECT w.*, ar.*
FROM workview.Workview w
LEFT JOIN fti.AnalysisResults ar ON ar.WorkViewID = w.ID
WHERE w.CreatedDateTime >= '2026-09-25'
  AND w.LocationID IN ('2023','3615','6541','664','721','6616','2507','629','1258','201','6344','207','1104','7135','7161','1861','635')
ORDER BY w.LocationID, w.CreatedDateTime;

Q3. Eventos del reemplazo de 248159. Cambia el FtiID por el que devolvio Q2.

SELECT COUNT(*) AS eventos
FROM fti.Transactions
WHERE FtiID = 'FTI_NUEVO';

Q4. A quien quedo asignado. Primero mira las columnas, despues filtra por el ID nuevo.

SELECT TOP 5 * FROM workview.Teams;
SELECT * FROM workview.Teams WHERE <columna de workview id> = ID_NUEVO;

Q5. Audit trail de la regeneracion, confirma RunId y tipo de evento.

SELECT TOP 50 *
FROM workview.WorkItemGenerationEvent
WHERE WorkviewId = ID_NUEVO;

---
Resultado 28 sep 19:03 UTC, corrido por Juan.
Q1: 0 filas. Los 17 originales ya no existen.
Q2: la unica fila con periodo 2026-08-27 es 252329, MKD2 Denver, store 3615, cajero SMV3495, creada 2026-09-25 16:55:36, CountOfEvents 3, StatusID 1, AssignedToUserID 33029E1A-E954-4D0C-9A2E-9F70C4248FD9, FtiID 67677FB5-BD46-4192-A8AB-D66352C48E64. Reemplaza a 248116. En 7135 no aparece ningun MD03 con periodo 27 ago. El resto de filas son generacion normal del 26 y 27 sep.
Q3 a Q5 fallaron por correrse con los marcadores literales.

Segunda ronda:

R1. Todo lo regenerado con periodo 27 ago, cualquier tienda.
SELECT ID, Headline, LocationID, CountOfEvents, PotentialValue, StatusID, AssignedToUserID, CreatedDateTime, PeriodFromDateTime, PeriodToDateTime, VirtualFilePath
FROM workview.Workview
WHERE PeriodFromDateTime = '2026-08-27' AND PeriodToDateTime = '2026-08-27'
  AND CreatedDateTime >= '2026-09-01'
ORDER BY CreatedDateTime;

R2. Ultimos MD03 de 7135 y 7161.
SELECT TOP 20 ID, Headline, LocationID, Section2Value, CountOfEvents, PotentialValue, StatusID, AssignedToUserID, CreatedDateTime, PeriodFromDateTime, PeriodToDateTime
FROM workview.Workview
WHERE VirtualFilePath LIKE '%md03%' AND LocationID IN (7135, 7161)
ORDER BY CreatedDateTime DESC;

R3. Control de eventos sobre 252329.
SELECT COUNT(*) AS eventos
FROM fti.Transactions
WHERE FtiID = '67677FB5-BD46-4192-A8AB-D66352C48E64';

R4. Run de la regeneracion y todo lo que ese run genero.
SELECT * FROM workview.WorkItemGenerationEvent WHERE WorkviewId = 252329;

SELECT e.RunId, e.RowId, e.EventType, e.WorkviewId, w.Headline, w.LocationID
FROM workview.WorkItemGenerationEvent e
LEFT JOIN workview.Workview w ON w.ID = e.WorkviewId
WHERE e.RunId IN (SELECT RunId FROM workview.WorkItemGenerationEvent WHERE WorkviewId = 252329)
ORDER BY e.RowId;

R5. Columnas de Teams.
SELECT TOP 5 * FROM workview.Teams;

---
Resultado segunda ronda, 28 sep 19:08 UTC.
R1: solo 2 WI con periodo 27 ago creados desde septiembre. 252328 COM1 store 865, 16:55:23, 1 evento, StatusID 3. 252329 MKD2 store 3615, 16:55:36, 3 eventos. Ambos el 25 sep.
R2: el MD03 mas reciente en 7135 es 186824 de oct 2025, en 7161 es 217484 de mar 2026. No existe reemplazo de 248159 ni de 248160.
R3: 3 eventos para 252329. Ese reemplazo esta sano.
R4: RunId F163CC7D-6822-4E19-A768-3260B3A7CFBB tiene una sola fila, 252329. Un run por definicion.
R5: workview.Teams no existe en esta base.
Nota: el COM1 original 248162 era store 635. 252328 es store 865. Verificar si es el reemplazo o un WI distinto.

R6. Todos los runs de la ventana de regeneracion, por tipo de evento.
SELECT e.RunId, e.EventType, COUNT(*) AS n, MIN(e.EventDateTime) AS desde, MAX(e.EventDateTime) AS hasta
FROM workview.WorkItemGenerationEvent e
WHERE e.EventDateTime >= '2026-09-25 12:00' AND e.EventDateTime < '2026-09-26 12:00'
GROUP BY e.RunId, e.EventType
ORDER BY desde;
