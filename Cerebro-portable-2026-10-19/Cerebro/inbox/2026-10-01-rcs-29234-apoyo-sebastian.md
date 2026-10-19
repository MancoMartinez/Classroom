# RCS-29234, ADUSA, LPMS no guarda casos. Apoyo a Sebastian

Fecha: 2026-10-01
Origen: Teams J.R. Teagle 2:54 p.m. y Jira en vivo 15:37 EDT.

## Qué pasa
Critical de Jim Cosseboom, creado 14:58 EDT. Al dar SAVE el sistema se queda pensando, vuelve a la pantalla del caso y borra lo digitado. Jim escribió a las 15:06 que puede ser solo la página Central Station Master porque Shoplifting sí guarda. Asignado a Sebastian Rueda, Under Support Review. Lo único que ha recibido Jim es el acuse automático de Rajith. Jim escribió también por correo a Juan, Ripp, J.R., Kara y otros.

## Lo que pide J.R.
Que Juan respalde a Sebastian. Que la comunicación en el ticket sea constante, además de resolver.

## Causa
Sin determinar. Talos, triage de Nick Hawkins 15:10: falta un ejemplo concreto, el save es código común, cada pantalla de caso tiene límite de dos minutos por request. Hipótesis sin verificar: mismo día que ENG-9699, donde Kiran reprodujo fallas en páginas dinámicas.

## Qué hago hoy
1. Responder a J.R.
2. Escribirle a Sebastian.
3. Que Sebastian publique el primer comentario humano en RCS-29234.
4. Con el ejemplo de Jim, pedir a ingeniería errores y tiempos de request en esa ventana.

## Precedentes
RCS-28115, ADUSA, SAVE sin respuesta por error de script en narrative, hotfix 8/1, solo se validó Shoplifting.
RCS-28075, ADUSA, 524 de Cloudflare en ShopliftingEntrypage.

## Pregunta de Sebastian: dónde está la base de Incident de ADUSA
Base: sqldb-prd-wus2-arp-production-441-dai-platform, Client ID 441, código dai. Managed Instance sqlmi-prd-wus2-arp-001 por Azure Bastion y SSMS. Fuente brain/memoria/reference_acceso_sql_tenants.md. Solo SELECT.
Los errores de la app no viven en la base. Están en Control Panel USPROD, Support, Incident Logs, View by Client, archivo AAAAMMDD_error_log.txt, y en Grafana con clientId 441. La base sirve para ver si el caso alcanzó a escribirse.
Grafana: {service_name=~".+", deployment_environment="usprod"} | clientId="441" |~ "(?i)exception|error|timeout"
