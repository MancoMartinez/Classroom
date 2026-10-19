# RCS-29026 caso 1353-15: redisparo omitido por SmartAlertProcess (2026-10-05)

## Resultado del redisparo
Link abierto a las 23:47:42 UTC (18:47 Bogota), ShopliftingID 1603659. Pagina en blanco es normal.
Grafana: corrida completa Begin a End en 0.3 s. El paso 4 trae la clausula
"1 Not In (Select 1 From SmartAlertProcess Where ShopliftingID = 1603659 And SmartAlertConfigID=SAC.SmartAlertConfigID And SystemType='C')".
Solo evaluo Harassment - Hannaford, TGC - Incident With Injury, Invalid Location Selected y JC Alert for Incident with Weapon, todas RR=0.
Harassment - Food Lion (config 209) no aparece: la excluye la fila 371425 de SmartAlertProcess.
Leccion: si la alerta ya tiene fila en SmartAlertProcess, redisparar no reenvia. Hay que quitar esa fila primero. El runbook no cubre este caso.

## Mensaje para Kiran (Teams)
Triggered 1603659 but Harassment - Food Lion was skipped. Step 4 excludes configs already in SmartAlertProcess, and row 371425 exists for config 209. Can you remove that row, or is it ok if I do it? Then I'll trigger again.

## Despues de quitar la fila
1. Abrir https://apps.apprissretail.com/adusa/nettrack/ProcessCaseAlert.aspx?ShopliftingID=1603659
2. Grafana: {service_name=~".+", deployment_environment="usprod"} | clientId="441" |= "1603659" y buscar 6a de Harassment - Food Lion con Rows Returned 1, luego 13b, 14 y End.
3. SQL: SELECT * FROM SmartAlertProcess WHERE ShopliftingID = 1603659 (fila nueva, Success).
4. SendGrid: Activity, Email Logs, destinatario de Jamie Holland, fecha de hoy, estado Delivered.

## Kiran pregunto si se puso InProcess = 0 antes de redisparar
InProcess ya estaba en 0 (consulta previa al disparo), no hizo falta cambiarlo. El bloqueo es la fila 371425.
Respuesta:
InProcess was already 0 when I checked before triggering, so I didn't need to change it. The run did start (Begin to End in Grafana), it just didn't pick up Harassment - Food Lion. I think row 371425 in SmartAlertProcess is what excludes it, but please let me know if I'm missing something.

## Kiran: "Nothing jumps out from my end"
InProcess sigue en 0 despues del play: es normal. Nettrack lo pone en 1 al empezar y lo devuelve a 0 al terminar, y la corrida duro 0.3 s.
Siguiente mensaje (pedir decision concreta):
Thanks Kiran. Maybe I'm reading it wrong, but the step 4 query in the log has "1 Not In (Select 1 From SmartAlertProcess Where ShopliftingID = 1603659 And SmartAlertConfigID=SAC.SmartAlertConfigID ...)", and row 371425 exists for config 209. Would it be ok to delete that row and trigger again so it resends?

## Kiran: "Did you use the same url I gave and updated the shopliftingiD?"
Si. Misma URL que uso el 9/28 (1599977, 1599980), solo cambio el ID. Grafana confirma la corrida para 1603659.
Respuesta:
Yes, same URL, only changed the ID: https://apps.apprissretail.com/adusa/nettrack/ProcessCaseAlert.aspx?ShopliftingID=1603659. Grafana shows the run for 1603659 at 23:47:42 UTC, it evaluated 4 alerts with 0 rows and ended, and Harassment - Food Lion wasn't in the list. I can share the log if it helps.

## Kiran: "Did you check the filters and see if the record in shoplifting satisfies them all?"
Si cumple: en la corrida original del 10/4, 6a de config 209 dio RR=1 a las 16:20:10 UTC y llego a 13b. Hoy la 209 no llego al paso 6, la saco el paso 4.
Respuesta:
Yes, on the original run on 10/4 the filter for config 209 returned 1 row at 16:20:10 UTC and it went to EMAIL SENT, so the case meets the filters. Today's run didn't reach the filter step for 209, it wasn't in the list from step 4. That's why I suspect row 371425.

## Kiran: "371425?"
Respuesta:
Sorry, that's the SmartAlertProcessID. SELECT * FROM SmartAlertProcess WHERE ShopliftingID = 1603659 returns one row: SmartAlertProcessID 371425, SmartAlertConfigID 209, Success, from the 10/4 16:20 UTC send that never reached SendGrid. Since that row exists, step 4 excludes config 209 when I retrigger.

## Kiran: "Yea, that's the last time it triggered"
Confirma que la 371425 es el ultimo disparo. Falta que diga si se borra para reenviar.
Respuesta:
Right. Since that send never reached SendGrid, the customer never got it. To resend, should we delete row 371425 and trigger again? Can you do it, or is it ok if I run the delete?
