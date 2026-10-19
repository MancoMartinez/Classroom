# RCS-29026 reenvio caso 1353-15 paso a paso (2026-10-07)

Runbook https://trebuco.atlassian.net/wiki/x/F4CDWm8 no cubre este caso. Paso 4 es para casos atascados (InProcess=1). Este es "Sent but not received" (13b presente, SendGrid sin registro). Tabla 3.2: "run exists but no 6 line for the alert = already sent". Para reenviar falta un paso que el runbook no tiene: quitar la fila de SmartAlertProcess.

Datos: ShopliftingID 1603659, SmartAlertProcessID 371425, config 209 Harassment - Food Lion, tenant 441 slug adusa, base sqldb-prd-wus2-arp-production-441-dai-platform.

0. Requisitos: OK explicito de Kiran para el DELETE (el "Sure go ahead" fue para redisparar), login de escritura.
1. Bastion, SSMS, sqlmi-prd-wus2-arp-001 con login de escritura.
2. Antes:
USE [sqldb-prd-wus2-arp-production-441-dai-platform];
SELECT * FROM incident.SmartAlertProcess WHERE ShopliftingID = 1603659 ORDER BY RunDate DESC;
SELECT ShopliftingID, InProcess FROM incident.Shoplifting WHERE ShopliftingID = 1603659;
Esperado: una fila 371425 config 209 Success. InProcess 0. Captura del resultado (respaldo).
3. Borrar:
BEGIN TRAN;
DELETE FROM incident.SmartAlertProcess WHERE SmartAlertProcessID = 371425 AND ShopliftingID = 1603659;
SELECT @@ROWCOUNT AS Borradas;
Si Borradas = 1: COMMIT;  Si otro numero: ROLLBACK; y parar.
4. Confirmar: el SELECT de SmartAlertProcess devuelve 0 filas.
5. Control Panel, adusa, entrar por logo. Mismo navegador:
https://apps.apprissretail.com/adusa/nettrack/ProcessCaseAlert.aspx?ShopliftingID=1603659
Pagina en blanco es normal. Anotar hora.
6. Grafana, ultimos 15 min:
{service_name=~".+", deployment_environment="usprod"} | clientId="441" |= "1603659"
Bien: 6a de Harassment - Food Lion con Rows Returned=1, 14, End. 13a/13b no traen ID:
{service_name=~".+", deployment_environment="usprod"} | clientId="441" |= "#1353"
Bien: 13b EMAIL SENT con la lista.
7. SQL: SELECT de SmartAlertProcess, fila nueva config 209 Success con RunDate de hoy (UTC).
8. SendGrid, Activity, Email Logs, destinatario jamie.holland@adusa.com, Subject starts with "Harassment - Food Lion #1353", fecha hoy. Bien: Delivered. Repetir con Kim Woods y Crystal Sweatt o el grupo. Horas en UTC.
9. Si a los 10 min no aparece en SendGrid: misma falla silenciosa. No redisparar otra vez. Avisar a Kiran con hora y lineas.
10. Si Delivered: respuesta al cliente (2026-10-07-rcs-29026-avance.md) y nota interna con hora, fila nueva y SendGrid.

Mensaje Kiran para el OK:
Hi Kiran, to resend the 1353-15 alert I plan to delete row 371425 from SmartAlertProcess (ShopliftingID 1603659, config 209) and trigger ProcessCaseAlert again. Is it ok if I run the delete with the write login?

Pendiente runbook: agregar escenario "Sent but not received, resend" con este DELETE.

## Paso 2 ejecutado (10/7)
Fila 371425, config 209, ShopliftingID 1603659, RunDate 2026-10-04 16:20:19.000, Success, SystemType C, EmailAddresses empieza Grant.Thomas@FoodLion.com,Linda.Stiller@foodlion... InProcess 0. Coincide con Grafana (13b 16:20:19.405).
Antes del DELETE: respaldar EmailAddresses completo y confirmar que estan Kim Woods, Jamie Holland y el grupo de Crystal:
SELECT SmartAlertProcessID, RunDate, EmailAddresses,
 CASE WHEN EmailAddresses LIKE '%jamie.holland%' THEN 'si' ELSE 'no' END AS Jamie,
 CASE WHEN EmailAddresses LIKE '%woods%' THEN 'si' ELSE 'no' END AS Kim,
 CASE WHEN EmailAddresses LIKE '%sweatt%' OR EmailAddresses LIKE '%RETFL%' THEN 'si' ELSE 'no' END AS Crystal_o_grupo
FROM incident.SmartAlertProcess WHERE SmartAlertProcessID = 371425;

## Respaldo EmailAddresses 371425 (10/7)
Grant.Thomas@FoodLion.com,Linda.Stiller@foodlion.com,Valarie.Wallace@foodlion.com,Neal.Cope@adusa.com,GAFinchum@FoodLion.com,CPhillips-Brown@adusa.Com,Kim.Lyda@adusa.com,James.Cosseboom@adusa.com,CentralStation@adusa.com,Brandi.Langford@FoodLion.com,troy.leshko@foodlion.com,Katherine.Kirby@foodlion.com,RETFLAssetProtectionDivisionalMgrsALL@retail.foodlion.com,DWalker@foodlion.com,Tommy.Postek@adusa.com,Brian.Tanner@FoodLIon.com,Silvana.Baxter@foodlion.com,Jamie.Holland@adusa.com,Carmine.Willis@FoodLion.com,bj.robinson@foodlion.com,Kimberly.WILLIAMS@FoodLion.com,Keith.Gouldman@FoodLion.com,Craig.Arcamone@foodlion.com;BDWilliams@foodlion.com,Brian.Tanner@FoodLion.com,Madelina.Fordham@foodlion.com,kim.woods@foodlion.com,Daniel.Analoro@foodlion.com
Jamie si, Kim si, Crystal via RETFL si.

HALLAZGO (hipotesis, sin verificar): "Craig.Arcamone@foodlion.com;BDWilliams@foodlion.com" usa punto y coma. SendGridEmail.vb separa solo por comas, asi que queda una direccion invalida. Si el envio la rechaza entera, no hay registro en SendGrid y SmartAlert.vb igual escribe Success. Lo que va despues del ; parece la parte de Email Managers de la tienda 1353 (kim.woods incluido). Si es la causa, reenviar fallaria igual.
Tambien: Brian.Tanner duplicado (FoodLIon y FoodLion).
NO borrar todavia. Verificar:
SELECT SmartAlertProcessID, SmartAlertConfigID, ShopliftingID, RunDate, EmailAddresses
FROM incident.SmartAlertProcess
WHERE RunDate >= '2026-09-27' AND EmailAddresses LIKE '%;%'
ORDER BY RunDate DESC;
SELECT SmartAlertProcessID, SmartAlertConfigID, RunDate, EmailAddresses
FROM incident.SmartAlertProcess WHERE ShopliftingID = 1596525;
Si las filas con ; no llegaron a SendGrid y las otras si: causa. Si alguna con ; llego: hipotesis descartada.

Teams Kiran:
Before deleting 371425 I looked at its EmailAddresses and found "Craig.Arcamone@foodlion.com;BDWilliams@foodlion.com", with a semicolon instead of a comma. If the code splits only on commas, that becomes one invalid address. Could that make the whole send fail before SendGrid? If so, a resend would fail the same way. I'm checking other sends with a semicolon to compare.

## Resultado consulta punto y coma (10/7)
Muchas filas de hoy con ; (configs 358, 361, 345, 235, 333, 207, 270, 400), p.ej. 371877 18:27:14 UTC "Lauren.linsenbach@adusa.com;paul.ullrich@stopandshop..." y 357 del 9/20 "james.cosseboom@adusa.com;" (Jim confirmo recibir las de >$1k). El ; es comun, casi seguro no es la causa.
Prueba final en SendGrid: lauren.linsenbach@adusa.com, hoy, cerca de 18:27 UTC. Si Delivered: hipotesis descartada, seguir con el DELETE (con OK de Kiran). No mandar el mensaje del punto y coma a Kiran.

## SendGrid lauren.linsenbach 10/7 (hipotesis ; DESCARTADA)
Horas de SendGrid coinciden exacto con RunDate (UTC): 17:40:05 (371868), 17:35:12 (371866), 17:31:47 (371864), 17:27:51 (371862), 17:25:49 (371860), 17:23:07 (371859). 371860 config 358 lleva "Lauren.linsenbach@adusa.com;jonathan.peck@..." y salio Delivered. El ; no rompe el envio.
Fechas: #1353 se envio 10/4 16:20 UTC, Leigh Ann reporto 10/5, la consulta de ; uso envios de hoy 10/7 solo como control.
SendGrid guarda 7 dias: la ausencia del 10/4 se pierde hacia el 10/11. Capturar ya la busqueda de jamie.holland 10/4.
Siguiente: OK de Kiran y DELETE (pasos 3 a 10).

## Juan: tiene DELETE en la base, no necesita OK de Kiran. Lo resuelve el.
Captura de evidencia SendGrid (antes del 10/11):
Email Logs, destinatario Jamie.Holland@adusa.com, Date October 4, 2026 (todo el dia, UTC), Subject starts with "Harassment - Food Lion".
Esperado: 2 Delivered, 03:49:35 (#2829) y 23:33:46 (#2560). Nada a las 16:20 (#1353). Repetir con kim.woods@foodlion.com.
Busqueda con "Jamie.Holland@adusa.com" (mayusculas) dio 0 resultados el 10/7. El 10/5 se encontraron 2 filas buscando en minusculas. Repetir con jamie.holland@adusa.com. Si sigue en 0, quitar el filtro de asunto.
Evidencia capturada 10/7: jamie.holland@adusa.com, Oct 4 2026 UTC, "Harassment - Food Lion": 2 Delivered (03:49:35 y 23:33:46), nada a las 16:20. Leccion: la busqueda de SendGrid distingue mayusculas, usar siempre minusculas.
10/7: DELETE de 371425 hecho (Borradas=1, COMMIT). SELECT por 1603659 devuelve 0 filas.

## Reenvio 10/7
Nueva fila 371880, config 209, RunDate 2026-10-07 18:49:34 UTC, Success, misma lista.
SendGrid jamie.holland 10/7 sin filtro de asunto: ultimo envio 18:40:41 (Medical Incident). Nada a las 18:49 al momento de revisar.
Pendiente: esperar 15 min y refrescar (posible demora de indexado), revisar Grafana 13b. Si sigue sin aparecer: la falla se REPRODUCE para este caso (2 de 2), mientras otros envios a la misma lista llegan. Apunta a algo del contenido de este correo, no a algo intermitente.
Teams Kiran (si se confirma):
Hi Kiran, I removed row 371425 and triggered 1603659 again. Nettrack wrote a new SmartAlertProcess row (371880, config 209, Success, 10/7 18:49:34 UTC), but SendGrid has nothing for it, same as on 10/4. Other alerts to the same recipients today were delivered. Since it failed twice for the same case, could it be something in this specific email? Happy to share the Grafana lines.
Grafana |= "#1353" 10/7: 7a 18:49:25.503 y 13a 18:49:34.394 (0 adjuntos, asunto "Harassment - Food Lion #1353 in Pfafftown, NC"). 13b no sale con ese filtro porque no trae el asunto. Buscar |= "13b" entre 13:49:30 y 13:50:00 Bogota.

## HALLAZGO 10/7: correo duplicado entre To y CC
13b Harassment - Food Lion 18:49:34.534 UTC. El ; en EmailAddresses es la frontera To|cc, no un error.
To incluye Brian.Tanner@FoodLIon.com. CC (Email Managers tienda 1353) incluye Brian.Tanner@FoodLion.com. Misma direccion con distinta capitalizacion.
La API v3 de SendGrid rechaza el mensaje entero (400) si una direccion se repite entre to, cc y bcc, y compara sin mayusculas. Rechazado = sin registro en Email Logs. SmartAlert.vb no revisa la respuesta y escribe Success.
Coincide con 0619-27 del 9/20 (Silvana.Baxter y bj.robinson en To y CC, Kimberly Williams dos veces) y con que Defrauded volvio a llegar cuando Kiran quito duplicados de la 218 el 9/27.
Coincide con 2 de 2 fallas del #1353 y con que los otros Harassment del 10/4 (otras tiendas) si llegaron. Mike no vio nada en el relay: consistente con envio por API.
Estado: HIPOTESIS fuerte. Falta confirmar.
Confirmar: duplicados en envios recientes y cruzar con SendGrid.
SELECT p.SmartAlertProcessID, p.SmartAlertConfigID, p.ShopliftingID, p.RunDate,
 LOWER(LTRIM(RTRIM(s.value))) AS Repetida, COUNT(*) AS Veces
FROM incident.SmartAlertProcess p
CROSS APPLY STRING_SPLIT(REPLACE(p.EmailAddresses, ';', ','), ',') s
WHERE p.RunDate >= '2026-09-15' AND LTRIM(RTRIM(s.value)) <> ''
GROUP BY p.SmartAlertProcessID, p.SmartAlertConfigID, p.ShopliftingID, p.RunDate, LOWER(LTRIM(RTRIM(s.value)))
HAVING COUNT(*) > 1
ORDER BY p.RunDate DESC;
Si las filas con duplicados son las que no aparecen en SendGrid: confirmado.
Arreglo inmediato del #1353: quitar el duplicado (Brian.Tanner de la lista de la 209 o de Email Managers de la tienda 1353) con Kiran, borrar 371880 y redisparar. Arreglo de fondo: deduplicar en codigo sin distinguir mayusculas y revisar el resultado de SendGrid.

Teams Kiran:
Hi Kiran, I resent 1603659 (row 371880, 18:49:34 UTC) and it's missing in SendGrid again. Looking at the 13b line, Brian.Tanner is in To as Brian.Tanner@FoodLIon.com and in CC (store managers) as Brian.Tanner@FoodLion.com. I think SendGrid rejects the whole message when the same address is in To and CC, even with different case, and SmartAlert.vb still writes Success. 0619-27 on 9/20 also had duplicates (Silvana and BJ). Does that sound right to you? If so, could we remove Brian from the 209 list so I can resend?

## Duplicados desde 9/15: 31 envios (10/7)
Incluye 368924 (0619-27, 9/20, kimberly.williams) = falla original del ticket. Y 371880 (#1353 hoy, brian.tanner).
Repetidas recurrentes: mark.sens (config 199 y 361), kimberly.williams (197 Defrauded FL), brian.tanner (209), erica.booth/peter.voronin/alexander.martin1 (264), nicholas.oakes (340), edward.king1 (267, 358), joseph.hammer (358).
Confirmacion en SendGrid (dentro de 7 dias):
1. mark.sens@adusa.com, Oct 7: NO debe haber nada a 02:13:05 ni 18:00:05. Control: SI debe haber Delivered a 18:40:41 (Medical Incident Hannaford, sin duplicado).
2. kimberly.williams@foodlion.com, Oct 4: NO debe haber nada a 00:20:46.
Si se cumple: causa confirmada.

## Prueba SendGrid de duplicados (10/7): resultado MIXTO
mark.sens Oct 7: 02:13:05 Delivered (371801, config 199, CON duplicado, "Fire - Food Lion #0..."). 18:00:05 NO aparece (371874, config 361, con duplicado). Control 18:40:41 Delivered.
kimberly.williams Oct 4: nada a 00:20:46 (371350, config 197, con duplicado).
Un duplicado no basta para perder el correo (371801 llego). Hipotesis debilitada. No mandar mensaje de Brian a Kiran todavia.
Siguiente: comparar donde esta el duplicado (To/CC) y su capitalizacion en 371801 (llego) vs 371874, 371350, 371880, 368924 (no llegaron).
WITH x AS (
 SELECT p.SmartAlertProcessID, p.RunDate,
  CASE WHEN CHARINDEX(';', p.EmailAddresses) > 0 THEN LEFT(p.EmailAddresses, CHARINDEX(';', p.EmailAddresses) - 1) ELSE p.EmailAddresses END AS ToPart,
  CASE WHEN CHARINDEX(';', p.EmailAddresses) > 0 THEN SUBSTRING(p.EmailAddresses, CHARINDEX(';', p.EmailAddresses) + 1, 4000) ELSE '' END AS CcPart
 FROM incident.SmartAlertProcess p
 WHERE p.SmartAlertProcessID IN (371801, 371874, 371350, 371880, 368924)
)
SELECT x.SmartAlertProcessID, x.RunDate, 'To' AS Parte, LTRIM(RTRIM(s.value)) AS Direccion
FROM x CROSS APPLY STRING_SPLIT(x.ToPart, ',') s
WHERE s.value LIKE '%mark.sens%' OR s.value LIKE '%kimberly.williams%' OR s.value LIKE '%brian.tanner%'
UNION ALL
SELECT x.SmartAlertProcessID, x.RunDate, 'Cc', LTRIM(RTRIM(s.value))
FROM x CROSS APPLY STRING_SPLIT(x.CcPart, ',') s
WHERE s.value LIKE '%mark.sens%' OR s.value LIKE '%kimberly.williams%' OR s.value LIKE '%brian.tanner%'
ORDER BY 1, 3;

## PATRON CONFIRMADO 5 de 5 (10/7)
Perdidos (no en SendGrid), duplicado entre To y CC:
368924 9/20 kimberly.williams (0619-27, falla original del ticket)
371350 10/4 kimberly.williams
371874 10/7 mark.sens
371880 10/7 brian.tanner (#1353 reenvio)
(371425 10/4 #1353 original: misma lista que 371880)
Entregado: 371801 10/7, mark.sens dos veces pero ambas en To.
Causa: cuando la misma direccion (sin importar mayusculas) esta en To (lista de la alerta) y en CC (Email Managers de la tienda), el correo completo no llega a SendGrid. SmartAlert.vb escribe Success igual.
Alcance: consulta de duplicados To/CC desde 9/15:
WITH x AS (
 SELECT p.SmartAlertProcessID, p.SmartAlertConfigID, p.ShopliftingID, p.RunDate,
  LEFT(p.EmailAddresses, CHARINDEX(';', p.EmailAddresses) - 1) AS ToPart,
  SUBSTRING(p.EmailAddresses, CHARINDEX(';', p.EmailAddresses) + 1, 4000) AS CcPart
 FROM incident.SmartAlertProcess p
 WHERE p.RunDate >= '2026-09-15' AND CHARINDEX(';', p.EmailAddresses) > 0
)
SELECT DISTINCT x.SmartAlertProcessID, x.SmartAlertConfigID, x.ShopliftingID, x.RunDate, LOWER(LTRIM(RTRIM(t.value))) AS Duplicada
FROM x
CROSS APPLY STRING_SPLIT(x.ToPart, ',') t
CROSS APPLY STRING_SPLIT(x.CcPart, ',') c
WHERE LOWER(LTRIM(RTRIM(t.value))) = LOWER(LTRIM(RTRIM(c.value))) AND LTRIM(RTRIM(t.value)) <> ''
ORDER BY x.RunDate DESC;

Teams Kiran:
Hi Kiran, I think I found why some Smart Alerts never reach SendGrid even though SmartAlertProcess says Success. In every lost send I checked, the same address is in To (alert email group) and in CC (store managers), sometimes with different case: 0619-27 on 9/20 and 10/4 00:20 (Kimberly Williams), 1353-15 on 10/4 and on today's resend (Brian Tanner), and 10/7 18:00 (Mark Sens). A send with Mark Sens twice but both in To was delivered. Does that make sense with how SendGridEmail.vb builds the message? If so, could we dedupe To and CC ignoring case? For 1353-15 I'd like to resend once Brian is only in one of the two.
Verificado 10/7: jamie.holland Oct 7 sin filtro de asunto, 18:40:41 y 19:02:15 Delivered, nada a 18:49:34. El reenvio (371880) no llego. No es demora: un correo posterior si llego.
