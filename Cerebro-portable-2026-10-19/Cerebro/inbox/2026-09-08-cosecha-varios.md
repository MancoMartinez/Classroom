# Cosecha de transcripciones — 8 sep 2026

Hallazgos verificados de cuatro sesiones sin cosechar. Pendiente de aprobación de Juan antes de entrar a la base con `bin/guardar`.

## 1. Exactitud del clasificador de cola bajó a 73%

Sesión "Cerebro cola manana", local_33961b4e-8d59-41d9-af19-d513e1547167.

El clasificador de `bin/cola.py` acertó 11 de 15 casos contra el set etiquetado a mano el 8 de septiembre, 73% de exactitud. Falla en tres tickets con cambio de nivel: RCS-28289, RCS-27941 y RCS-28753. Un cambio de nivel en esos tres no cuenta como movimiento real sin revisar Jira directamente. `CLAUDE.md` marca 100% como el piso aceptable, la caída confirma que el léxico envejeció y hay que revisar `bin/cola.py` contra estos tres casos.

## 2. Azure DevOps, reviewer requerido para el fix de SnowflakeSqlExpressionFieldWriter

Sesión "Securee developer addition", local_c606f340-6b12-4e85-b136-482f6b9954f1.

El grupo Approval All Developers en el PR exige un reviewer de Secure Developers, Secure Managers o Secure Senior Managers. Juan Martinez no cuenta para ese requisito. El fix toca `SnowflakeSqlExpressionFieldWriter`, la capa de generación SQL de Snowflake en Secure, dominio del equipo Blue de Jon Morgan, Platform and Database Services.

Miembros actuales de Secure Developers verificados en Azure DevOps: Brad Nguyen, Brandon Kays, Christopher Beck, Diego Gomez, Gabor Remenyi, Manasa Chennoju, Mohammed Abdul-Mutahhar, Neil Abrahams, Santiago Forero.

Candidatos recomendados para el reviewer: Brad Nguyen o Neil Abrahams, los dos DB Engineers con conocimiento del generador de expresiones SQL. Gabor Remenyi también sirve, está en Blue y en Cyan a la vez. Ningún cambio se hizo en el PR ni en los grupos, la revisión fue de solo lectura.

## 3. Sesión "Cerebro asignacion diaria" del 7 de septiembre, sin hallazgo nuevo

Sesión local_50a6cc50-f9e7-4445-9fb8-3906b5e82d38.

El contenido completo de esta sesión ya vive en `asignaciones/2026-09-07.md`, secciones 3 y 6bis. No hay hallazgo adicional que capturar aquí, se marca cosechada para no repetir la lectura.

## 4. Migración New Relic a Grafana, estado y acceso de Sebastian Rueda

Sesión "New Relic project overview", local_27f8f29b-1781-4b55-a1cc-a9fe82203e88.

El proyecto de infraestructura del equipo Support migra todo el monitoreo de New Relic a Grafana dentro del 2026 Support Plan, espacio RTS de Confluence. Cuatro fases en el año: Q1 planeación previa a la compra, Q2 migración con alertas y configuración, Q3 optimización de dashboards y alertas ya migrados, Q4 mejora continua.

Trabajo técnico completado: whitelisting de IPs con InfoSec, monitores de ping, script, SSL y work items movidos a Grafana, logs de LPMS, Secure y Engage enviados vía Alloy, ocho dashboards replicados en Grafana (Ingest de archivos, HTTP Ping, Greenplum Dataload, Verify SQL, Snowflake Sync, Work Items PROD, Returns Portal, Application Uptime), alertas de archivos, GP, work items, sintéticos y logs al 100%. Un solo paso queda sin marcar completo, desinstalar el agente de infraestructura de New Relic.

RTS-206268 y RTS-206515 son alertas sintéticas etiquetadas Grafana, monitores que salieron de esta migración.

El dashboard que se busca por "New Relic" para carga de archivos y Greenplum es "Greenplum Dataload Status", vive en la página Confluence "New Relic Monitoring", con cuatro flujos de ticket según el tipo de error: errores, conteo de transacciones o tiendas por debajo de lo esperado, procesos que se pasan de tiempo, y procesos que no corrieron en 24h o una semana. Es un dashboard onenr.io, entra con el login corporativo normal, no requiere cuenta separada.

Matriz de acceso de onboarding L2 confirma con check para Sebastian Rueda: Jira RTS/RCS, VPN, Snowflake, Key Vault, 1Password, Remote Desktop. Jump US y Jump EU aparecen sin confirmar. No existe fila de acceso separada para New Relic o Grafana en esa matriz. Si el login corporativo no funciona en el dashboard, el camino es un ticket de Access Change en el IT Help Desk con aprobación del lead, no una credencial de New Relic aparte.

Para llevar a alguien nuevo a leer el proceso completo, el orden de lectura en Confluence es 2026 Support Plan, después Migration Steps, después New Relic Monitoring.

Fuentes: 2026 Support Plan (https://trebuco.atlassian.net/wiki/spaces/RTS/pages/477135994882/2026+Support+Plan), Migration Steps (https://trebuco.atlassian.net/wiki/spaces/RTS/pages/477838770180/Migration+Steps), New Relic Monitoring (https://trebuco.atlassian.net/wiki/spaces/RTS/pages/474743046149/New+Relic+Monitoring), L2 Support Onboarding (https://trebuco.atlassian.net/wiki/spaces/RTS/pages/477936910361/L2+Support+Onboarding+Essential+Links+Resources+and+Access+Information).
