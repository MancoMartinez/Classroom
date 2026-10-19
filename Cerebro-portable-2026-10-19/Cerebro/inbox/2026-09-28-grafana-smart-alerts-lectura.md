# Grafana para Smart Alerts: acceso, consultas que funcionan y como leer

## Acceso
Explore en apprissretail.grafana.net, datasource grafanacloud-apprissretail-logs. Tambien Control Panel, Support, Logs, elegir cliente y fuente Grafana. Staging: usstaging.apprissretailcloud.com/control/#/logs, app web-stg-wus2-arp-nettrack.
Produccion: AzureAppName web-prd-wus2-arp-nettrack, deployment_environment usprod, logger LPSBO.SmartAlert.
clientId: ADUSA 441, Vitamin Shoppe 433, Vallarta 432.

## Horas
Explore muestra hora Bogota, UTC-5. Verificado: 14:36:46 en Grafana = RunDate 19:36:46 UTC en SmartAlertProcess. El Control Panel mostro UTC. La base guarda UTC. ET = UTC-4 en septiembre.

## Consultas que funcionan, en Code
Todo de un caso, la mejor para diagnosticar:
{service_name=~".+", deployment_environment="usprod"} | clientId="441" |= "<ShopliftingID>"
Corridas que terminaron:
{service_name=~".+", deployment_environment="usprod"} | clientId="441" |= "End of SmartAlert.ProcessSmartAlert"
Envios confirmados de una alerta:
{service_name=~".+", deployment_environment="usprod"} | clientId="441" |= "13b" |= "External Case"
Casos atascados:
{service_name=~".+", deployment_environment="usprod"} | clientId="441" |= "still on processing"
La consulta con {AzureAppName="..."} como selector no devuelve nada. Usar el selector de arriba.

## Trampas
1. Limite de 1000 lineas, direccion Backward: el export se corta por el final mas viejo. Rango corto o filtro por ID.
2. Filtrar por una palabra de negocio trae las lineas 6 y 6a de otras alertas cuyo SQL la menciona. Ejemplo: "Impersonation" trajo 1000 lineas de otras alertas. Filtrar por ShopliftingID.
3. La linea 13a no trae SystemID. Se asocia al caso por el asunto o por la hora.
4. Las lineas salen desordenadas porque las alertas se evaluan en paralelo.

## Pasos del log
Begin of SmartAlert.ProcessSmartAlert. pSystemType=Case o Audit o HR, pSystemID = ShopliftingID en casos.
1 Inside ProcessSmartAlert. 2 y 2a consulta del tipo de caso. 3 SystemID y tSystemCaseType. 4 carga las alertas configuradas.
6 Ready to run AlertName. 6a Ran AlertName con el SQL del filtro y Rows Returned=N. 1 = la alerta aplica, 0 = no aplica.
8 Getting ready to merge doc, DocName. 8a Merging Completed.
13a Ready to send email, Total Attachment count/size y SubjectLine.
13b EMAIL SENT, AlertName, EmailGroup y cc.
14 Inserting into SmartAlertProcess.
16 Warning, por ejemplo archivo o blob no encontrado. La corrida sigue con otras alertas.
End of SmartAlert.ProcessSmartAlert: SystemID.
0. Quit ProcessSmartAlert ... still on processing: InProcess estaba en 1.
ProcessAlertQueue 1. dt.Rows.Count: tamano de la cola.

## Patrones
Sano: 6a con Rows Returned=1, 8, 8a, 13a, 13b, 14, End.
Deadlock sep 2026: 13a sin 13b ni End, luego Quit en cada guardado.
Filtro no aplica: 6a Rows Returned=0 y End sin 13a. Es configuracion.
Los filtros se leen completos en la linea 6a: division, fecha de creacion, CaseStatus, narrativa, CaseTier.

## SQL de apoyo, solo SELECT
SELECT ShopliftingID, InProcess FROM incident.Shoplifting WHERE ShopliftingID = <ID>;
SELECT * FROM incident.SmartAlertProcess WHERE ShopliftingID = <ID>;
SELECT TOP 20 * FROM incident.SmartAlertProcess ORDER BY RunDate DESC;
SELECT AlertConfigID, EmailGroup FROM incident.AlertConfig WHERE EmailGroup LIKE '%' + CHAR(13) + '%' OR EmailGroup LIKE '%' + CHAR(10) + '%';
Base de Incident en el servidor de produccion del tenant. DEVWUS2 es desarrollo.
