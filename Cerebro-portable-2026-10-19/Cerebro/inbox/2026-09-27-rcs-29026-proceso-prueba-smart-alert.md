# RCS-29026 Cómo probar una Smart Alert, explicado por Kiran Vadday en llamada 9/27

Caso de prueba: 2026-FOOD LION ,LLC-0513-25, ShopliftingID 1599980, alerta Security Deficiency - Food Lion.

1. SELECT ShopliftingID, InProcess FROM incident.Shoplifting WHERE ShopliftingID = 1599980
2. Si InProcess = 1: UPDATE incident.Shoplifting SET InProcess = 0 WHERE ShopliftingID = 1599980
   Es UPDATE en producción. Solo con Kiran o Infra en la llamada.
3. Con sesión ADUSA abierta, abrir https://apps.apprissretail.com/adusa/nettrack/ProcessCaseAlert.aspx?ShopliftingID=1599980 y dar Enter. Dispara la alerta sin guardar el caso. Ruta solo para desarrollo.
4. Control Panel, Support, Logs, cliente adusa.com 441, Grafana. Recargar la página y volver a elegir el cliente para ver lo último. Hora del log en UTC, 4 horas adelante de ET.
5. Lectura: la corrida llega a "13a. Ready to send email". Falta "13b. Email sent". Después vendría el insert en SmartAlertProcess con Success. Los pasos salen desordenados porque corren en paralelo.
6. Confirmación: SELECT * FROM incident.SmartAlertProcess WHERE ShopliftingID = 1599980. Con fila, el correo salió.

Con Infra en la llamada: repetir en 2 o 3 casos más con InProcess = 1, por ejemplo 1599977, 1598412, 1597868, 1599976, 1597500, 1599974, y confirmar que les llega el correo antes de cerrar.
Estado 9/27: Ayesha Mehar levantó alerta a Russ en Jira Ops. RETAILIT-20901 asignado a Russell Harmon, estado Waiting on Customer Response.
