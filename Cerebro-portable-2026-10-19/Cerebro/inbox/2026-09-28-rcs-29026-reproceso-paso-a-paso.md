# Reproceso de Smart Alert atascada, paso a paso. Primer caso ADUSA 1599977

Base: procedimiento Kiran 9/27 y llamada 9/28. De a un caso. UPDATE en produccion con visto bueno de Kiran.

Paso 0. Kiran: "Starting now with one ADUSA case (ShopliftingID 1599977). Is the fix already live in US prod?"
Paso 1. SQL, base ADUSA 441. Confirmar que esta atascado:
SELECT ShopliftingID, InProcess FROM incident.Shoplifting WHERE ShopliftingID = 1599977;
SELECT * FROM incident.SmartAlertProcess WHERE ShopliftingID = 1599977 AND RunDate >= '2026-09-24';
Atascado = InProcess 1 y cero filas. Si ya tiene fila, pasar al siguiente candidato.
Paso 2. Destrabar:
UPDATE incident.Shoplifting SET InProcess = 0 WHERE ShopliftingID = 1599977;
Paso 3. Disparar, con sesion ADUSA abierta:
https://apps.apprissretail.com/adusa/nettrack/ProcessCaseAlert.aspx?ShopliftingID=1599977
Paso 4. Grafana, rango ultima hora:
{service_name=~".+"} | clientId="441" |= "1599977"
Esperado: Begin, 13a, 13b EMAIL SENT, End. Sin Quit.
Paso 5. Confirmar:
SELECT * FROM incident.SmartAlertProcess WHERE ShopliftingID = 1599977;
Fila con RunDate de hoy y Success. Revisar Smart Alert History del caso en el UI.
Paso 6. OK: siguiente candidato (1598412, 1597868, 1599976, 1597500, 1599974). Falla: parar y mandar a Kiran captura de Grafana.
Vitamin Shoppe 433: mismo flujo con 2026-09-28-rcs-29145-reproceso-casos.md cuando Kiran confirme la URL del tenant.
