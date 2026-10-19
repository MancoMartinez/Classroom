# RCS-28294 reset masivo de InProcess, Vallarta (2026-10-09)

Matt 10/9: "yes bulk reset back to 0 would fix. there is currently no way to set them back to 0 so if the process flops for any reason they get stuck"
Riesgo que queda: sin reseteo automatico, cualquier corrida que falle vuelve a dejar el caso pegado. Va al ENG.

## SQL (base 432)
USE [sqldb-prd-wus2-arp-production-432-vsa-platform];
-- 1. Respaldo, guardar como CSV. Esperado 305 filas
SELECT s.ShopliftingID, s.CaseNo, s.CaseStatus, m.CreatedDate
FROM incident.Shoplifting s JOIN incident.MasterCase m ON m.MasterCaseID = s.MasterCaseID
WHERE s.InProcess = 1 AND m.CreatedDate < '2026-10-01'
ORDER BY s.ShopliftingID;
-- 2. Reset
BEGIN TRAN;
UPDATE s SET s.InProcess = 0
FROM incident.Shoplifting s JOIN incident.MasterCase m ON m.MasterCaseID = s.MasterCaseID
WHERE s.InProcess = 1 AND m.CreatedDate < '2026-10-01';
SELECT @@ROWCOUNT AS Actualizadas;
-- 305: COMMIT;  otro numero: ROLLBACK;
-- 3. Verificar
SELECT COUNT(*) AS Pegados FROM incident.Shoplifting WHERE InProcess = 1;

## Teams Matt
Thanks Matt. I'll run the reset for the 305 Vallarta cases created before 10/1 with InProcess = 1, keeping a list of the IDs first. Ok if I go ahead? I'll also note in the ticket that there's no automatic reset, so a failed run leaves the case stuck.

## Cliente (Tatiana), despues del reset
Hello Tatiana,

Thank you for the two examples, they helped us find the issue. Some older cases were blocked from sending their smart alerts, including 2026-ADUP-65-52 and 2026-ADUP-66-15. We have cleared that, so alerts on those cases will go out normally the next time they are saved.

The alerts for those two closures were not sent at the time. Would you like us to send them now? I wanted to check with you first, since they would go to the full distribution list.

Kind regards,
Juan
