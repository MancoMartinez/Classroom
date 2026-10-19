# Confluence: runbook de Smart Alerts en borrador, 30 sep

Borrador privado, sin publicar. RTS, padre "Troubleshooting articles - Incident" (474924187736).
Titulo: Smart Alerts Runbook: Filter, Database, Logs and Manual Re-trigger. ID 478259937303.
Editar: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/edit-v2/478259937303

## Lo que ya existia en Confluence
RTS 475519582363 Smart Alerts not generating, 2024. Build Filters, ejemplo con narrativa "Threat".
RTS 476537552897 Alert Not Triggered, 2025. Auditoria, log debug completo con paso 4 (query de elegibilidad) y paso 15 "No matching criteria found. Alert Skipped".
RTS 475461517316 Smart Alert Config, abr 2026. Todos los campos de configuracion y Special Alerts.
RTS 476886695937 Accessing Incident/Audit Error and Debug Logs. Control Panel, Support, Incident Logs.
RTS 474930053190 Known Issues - Smart Alert Configuration. BOLO a managers equivocados.
RTS 478257446931 RCS-28534 Stater Bros triage, Diego, 29 sep. InProcess, 242 casos, hipotesis de adjuntos.
AALPS 474658701551 Classic to NetTrack Smart Alert. Llaves UseSmartAlert y UseSmartAlertDebug.
RCS 475407482883 Smart Alert Administration, y guias de 2022 y 2023 para clientes.
Ninguna pagina cubre Grafana, el reset de InProcess ni ProcessCaseAlert.aspx.

## Dato nuevo del log de la pagina Alert Not Triggered
Paso 4 del motor filtra: StatusID distinto de 0, BeginDate hasta hoy, AlertGroup distinto de Special, tipo de caso en SmartAlertCaseTypes o Any, y sin fila previa en SmartAlertProcess para esa alerta. Tablas SmartAlertConfig, AlertConfig, SmartAlertCaseTypes.

## Pendiente antes de publicar
Nombres de columna de SmartAlertConfig en un tenant Cohesion. Ruta ProcessCaseAlert igual al slug. Ruta de menu en LPMS para buscar caso. Validar con RCS-29195.
