# RCS-29026 / RCS-29123 Llamada con Kiran 9/28, fix de Smart Alerts

## Transcripcion limpia (ingles, audio 5 min)
Kiran: You create a smart alert and they won't receive an email. Russ confirmed yesterday they received the email, but we don't have any update in the Smart Alert History.
This code fix allows the second part to happen. In the Grafana logs it comes to 13 and 13a and we don't see 13b. Smart Alert History reads from incident.SmartAlertProcess, so the insert does not happen and the email sent notification does not happen on our side.
The test in staging works. We should see step 13b and the email sent notifications. The biggest thing: select * from incident.SmartAlertProcess should have data. The last two days I could not see any data after 9/24.
After the deployment you should see records at least for today, for new cases. Logs should not be cut off.
There is also a network 500 on the SmartTrack call that tracks smart alert activity, throwing 500 / not found. That should go away.
So: no more 500 errors, SmartAlertProcess populated, Smart Alert History showing it. Smart Alert History in the UI is SmartAlertProcess behind the scenes. Logs, table and UI all in sync.
The fix: it tries to do things in parallel, and there was a deadlock because there is so much traffic on ADUSA, it does not happen on other sites. The change says wait, let the process complete, rather than forming a deadlock. One line change. Cherry pick to release branch, QA. Europe deployment is done, US must be done by now, so we should be able to test it.

## Evidencia staging (capturas)
Control Panel staging, client 441, web-stg-wus2-arp-nettrack, 9/27 11:56:46 PM: 13b. *** EMAIL SENT, AlertName Appriss Test Incident Burglary Food Lion, EmailGroup bvadday@trebu.co.
SELECT SmartAlertProcess ShopliftingID 1119654: SmartAlertProcessID 148886, config 364, RunDate 2026-09-27 23:56:46, Success.
PR: https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/Secure/pullrequest/58273

## Que verificar tras deploy US
1. Grafana client 441: aparece 13b y End en casos nuevos.
2. SELECT * FROM incident.SmartAlertProcess WHERE RunDate >= hoy: filas nuevas.
3. Smart Alert History en UI con registros de hoy.
4. Sin 500 en la llamada de SmartTrack de actividad de smart alert.
5. Aparte y no cubierto por el PR: direcciones con CRLF (drops Invalid) e Impersonation 0143-14 sin evento en SendGrid.

## Para Vitamin Shoppe (tenant 433)
Mismo sintoma posible: 13a sin 13b, SmartAlertProcess sin filas recientes, InProcess pegado en 1. Kiran dice que el deadlock se da por trafico alto de ADUSA, el fix es de codigo comun. Validar si Vitamin Shoppe tiene el mismo patron en Grafana antes de asumir la misma causa.
