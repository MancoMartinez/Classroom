# RCS-29145 Reproceso de casos atascados, Vitamin Shoppe 433. Llamada con Kiran 9/28

## Lo que dijo Kiran (transcripcion resumida, ingles)
The code fix only fixes going forward. It won't know which cases are stuck. Don't go only by InProcess = 1: the flag is set to 1 every time a smart alert is processing, and if you set it to 0 it becomes 1 again. Get the case number, get the ShopliftingID, check InProcess, set it to 0, trigger ProcessCaseAlert.aspx, watch Grafana and Smart Alert History. One by one: make sure the first is good before the second. Only trigger the ones you are sure are stuck.
Sobre el borrador para Chris Ripp: correcto. El PR 58273 explica la causa raiz.

## Mismo procedimiento del 9/27 (2026-09-27-rcs-29026-proceso-prueba-smart-alert.md), adaptado a 433
Candidatos: casos con 13a y sin End en Grafana (ver 2026-09-28-rcs-29145.md). pSystemID de tipo Case es el ShopliftingID.

1. Confirmar cuales no tienen alerta registrada desde el 9/23 (SELECT, se puede sin Kiran):
SELECT s.ShopliftingID, s.InProcess
FROM incident.Shoplifting s
WHERE s.ShopliftingID IN (147176,147184,147185,147186,147187,147188,147189,147190,147191,147192,147193,147194,147195,147196,147197,147198,147199,147200,147201,147202,147203,147204,147205,147206,147208,147209,147210,147212,147213,147215)
AND NOT EXISTS (SELECT 1 FROM incident.SmartAlertProcess p WHERE p.ShopliftingID = s.ShopliftingID AND p.RunDate >= '2026-09-23');
Resultado = lista segura de atascados.
2. Por cada uno, de a uno:
UPDATE incident.Shoplifting SET InProcess = 0 WHERE ShopliftingID = <id>;
Es UPDATE en produccion. Con autorizacion de Kiran.
3. Abrir en el navegador con sesion de Vitamin Shoppe: <url del tenant>/nettrack/ProcessCaseAlert.aspx?ShopliftingID=<id>. La ruta de ADUSA es apps.apprissretail.com/adusa/...; confirmar la de 433 con Kiran, no adivinar.
4. Grafana client 433: esperar 13a, 13b EMAIL SENT y End.
5. SELECT * FROM incident.SmartAlertProcess WHERE ShopliftingID = <id>; debe aparecer fila. Revisar Smart Alert History del caso en el UI.
6. Si todo bien, siguiente caso. Si falla, parar y avisar a Kiran.
Pendiente: el fix PR 58273 tiene que estar en US antes, si no el caso vuelve a atascarse.
