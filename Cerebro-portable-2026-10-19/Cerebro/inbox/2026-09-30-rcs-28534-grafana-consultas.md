# RCS-28534 Stater Bros, consultas de Grafana antes de la llamada con Diego, 30 sep

Explore en apprissretail.grafana.net, datasource grafanacloud-apprissretail-logs, modo Code. Hora en pantalla Bogota, base en UTC mas cinco horas. Limite 1000 lineas.

## 0. Confirmar que clientId 423 trae lineas. Ultimas 24 h
{service_name=~".+", deployment_environment="usprod"} | clientId="423" |= "SmartAlert"
Si sale vacio: {service_name=~".+", deployment_environment="usprod"} |= "staterbros" |= "SmartAlert"

## 1. Salud del cliente, 7 dias, vista Time series. Responde si el atasco sigue despues del fix del 9/28
Corridas terminadas por hora:
sum(count_over_time({service_name=~".+", deployment_environment="usprod"} | clientId="423" |= "End of SmartAlert.ProcessSmartAlert" [1h]))
Guardados rechazados por InProcess por hora:
sum(count_over_time({service_name=~".+", deployment_environment="usprod"} | clientId="423" |= "still on processing" [1h]))
Listos para enviar contra enviados por hora:
sum(count_over_time({service_name=~".+", deployment_environment="usprod"} | clientId="423" |= "Ready to send email" [1h]))
sum(count_over_time({service_name=~".+", deployment_environment="usprod"} | clientId="423" |= "EMAIL SENT" [1h]))
Lectura: End sigue despues del 9/28 = el motor corre. Brecha 13a contra 13b = corridas colgadas. Quit creciendo despues del 9/28 = casos nuevos quedando atascados.

## 2. Lista de casos bloqueados hoy, ultimas 24 h
{service_name=~".+", deployment_environment="usprod"} | clientId="423" |= "still on processing"
Anota los SystemID que salen. Esos son atascos con prueba, no solo InProcess = 1.

## 3. Caso por caso, 7 dias. Repetir con 205148, 205157, 205211, 205367, 205395, 202901
{service_name=~".+", deployment_environment="usprod"} | clientId="423" |= "205148"
Por cada ID anota la ultima linea de cada corrida:
6a Rows Returned=0 y End: filtro no aplica, configuracion.
6a=1, 8, 8a, 13a, 13b, 14, End: sano.
13a sin 13b ni End, luego Quit: atasco en el envio, mecanismo 8.
Muere en 8 u 8a sin llegar a 13a: apoya la hipotesis de adjuntos de Diego.
Solo Quit: InProcess ya estaba en 1 desde antes de la ventana.
En 13a copia Total Attachment count y size.

## 4. Filtros de las alertas, sobre 205148
{service_name=~".+", deployment_environment="usprod"} | clientId="423" |= "205148" |= "6a"
Lee el SQL de Legal Follow Up y de Discipline Request. Busca CaseStatus, RootCause o Disposition en el WHERE.

## 5. Errores y avisos, 7 dias
{service_name=~".+", deployment_environment="usprod"} | clientId="423" |= "SmartAlert" |~ "(?i)exception|error|warning"
{service_name=~".+", deployment_environment="usprod"} | clientId="423" |~ "(?i)BlobNotFound|GetBlobAttachment|timeout"

## Llevar a Diego
Grafica de End y Quit por hora con el 9/28 marcado. Tabla de seis IDs con su ultima linea. Filtro 6a de las dos alertas.

## Rangos, hora Bogota, absolutos
0: Last 1 hour. Si vacio, Last 24 hours.
1: 2026-09-21 00:00 a now. Cubre antes del pico 9/24, el pico y despues del fix. Metrica, sin limite de 1000.
2: 2026-09-28 14:00 a now. Jim confirmo alertas desde 2:30 PM EDT 9/28, 13:30 Bogota.
3: 205148 y 205157: 2026-09-20 00:00 a now. 205211, 205367, 205395: primero 2026-09-29 15:00 a 17:00, luego 2026-09-29 00:00 a now. 202901: Last 7 days, solo se esperan Quit.
4: el mismo rango de 205148.
5: 2026-09-28 14:00 a now. Si pega 1000 lineas, partir por dia.
