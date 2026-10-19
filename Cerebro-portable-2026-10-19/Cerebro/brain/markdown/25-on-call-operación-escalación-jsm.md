# On-call — Operación & Escalación (JSM)

Carpeta 25 de la base de Moscú. 7 fragmentos.

## On-call JSM — Qué es y capacidades
_chunk 1381 · 2026-07-27 · fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478025515011/On-Call+Operation+Guide+Support+L2+L3_

Guia oficial On-Call Operation Guide (Support L2/L3). Espacio Confluence RTS, autora Camila Cortes, actualizada 2026-07-22.

Jira Service Management (JSM) es la plataforma ITSM y de alerting de Atlassian. Para los equipos de soporte e ingenieria de Appriss Retail, JSM es la espina dorsal del sistema de on-call: rutea pages, gestiona escalaciones y trackea la respuesta a incidentes desde la primera alerta hasta la resolucion.

Capacidades que usa el equipo:
- On-call schedules: turnos rotativos que definen quien es primario y secundario en cada momento.
- Alert routing: los incidentes se rutean automaticamente al responder on-call correcto segun el schedule.
- Escalation policies: reglas por tiempo que paginan al siguiente nivel si el responder actual no hace acknowledge.
- Mobile push notifications: paging instantaneo via la app movil de JSM en iOS y Android.
- Incident/ticket management: el ticket trackea todo el ciclo open, acknowledged, in progress, resolved.

Nota de contexto: esta guia (JSM nativo, schedules en Jira Operations) reemplaza el modelo previo basado en OpsGenie que aparece en KB antigua de Moscu.

## On-call — Instalacion JSM en el movil (iOS)
_chunk 1382 · 2026-07-27 · fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478025515011/On-Call+Operation+Guide+Support+L2+L3_

Obligatorio antes del primer turno: todos los miembros on-call deben tener la app movil de JSM instalada y configurada.

iOS:
Paso 1 - Instalar: App Store, buscar "Jira Cloud by Atlassian" (publisher Atlassian), Get e instalar.
Paso 2 - Sign in: abrir la app, Log in, usar la cuenta Atlassian de Appriss Retail (email corporativo).
Paso 3 - Activar push: seleccionar Direct notifications, Next (Allow). Si te saltaste el prompt: Ajustes del iPhone, Notificaciones, Jira Cloud by Atlassian, activar Allow Notifications, Sounds y Badges.
Paso 4 - Critical Alerts (recomendado): en la app, tu nombre arriba a la izquierda, Notifications settings, Critical Alerts, activar. Los Critical Alerts saltan el modo No molestar y el modo silencio, esencial para turnos de madrugada.
Tip iOS: prueba la configuracion en Notification settings, Alert rules, Contact methods, Test push notification.

## On-call — Instalacion JSM en el movil (Android)
_chunk 1383 · 2026-07-27 · fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478025515011/On-Call+Operation+Guide+Support+L2+L3_

Android:
Paso 1 - Instalar: Google Play Store, buscar "Jira Cloud by Atlassian" (publisher Atlassian), Install.
Paso 2 - Sign in: abrir la app, Sign in with Atlassian, usar email corporativo de Appriss Retail y credenciales SSO. Organization URL si la pide: apprissretail.atlassian.net.
Paso 3 - Notificaciones: cuando pregunte, Allow all notifications. Si te la saltaste: Settings de Android, Apps, Jira, Notifications, activar todas las categorias.
Paso 4 - Desactivar optimizacion de bateria para la app: Settings, Apps, Jira Service Management, Battery, seleccionar Unrestricted. Esto evita que Android mate la app en background y retrase los pages.
Paso 5 - Canal de notificacion en alta prioridad: en la app, tu nombre arriba a la izquierda, Notifications settings, Critical Alerts, activar.
Tip Android: equipos Samsung y Pixel pueden tener "sleep mode" o "focus mode" que bloquean notificaciones. Revisa Digital Wellbeing o Focus y agrega JSM a la whitelist explicitamente.

## On-call — Como hacer Acknowledge de un page
_chunk 1384 · 2026-07-27 · fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478025515011/On-Call+Operation+Guide+Support+L2+L3_

Cuando JSM te pagina es critico hacer acknowledge lo mas rapido posible. El acknowledge detiene el timer de escalacion y le señala al equipo que alguien esta activamente en ello.

Desde la app movil (metodo mas rapido): abrir la push notification de JSM, tocar la alerta para abrir el incidente, seleccionar Acknowledged. El timer se detiene de inmediato.
Desde el portal web de JSM: ir a Alerts (Operations), navegar a las alertas asignadas a ti, abrir el incidente y click en Acknowledged.
Desde email (ultimo recurso): JSM envia un email de alerta, click en View Alert, redirige al incidente, click Acknowledged.

Importante: solo leer la push notification NO cuenta como acknowledge. Debes entrar y hacer click en Acknowledge dentro de la app o el portal.

## On-call — Politica de escalacion por tiempo
_chunk 1385 · 2026-07-27 · fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478025515011/On-Call+Operation+Guide+Support+L2+L3_

La politica de escalacion del on-call de Appriss Retail es por tiempo y automatica. Si un page no recibe acknowledge dentro de la ventana definida, JSM escala automaticamente al siguiente nivel sin intervencion manual.

0:00 - Alert Fired - Primary On-Call: una alerta se dispara (monitoreo, ticket de cliente, o trigger manual). JSM pagina al ingeniero primario on-call via push, SMS y email.
+5 min - No Ack - Secondary On-Call: si el primario no hizo acknowledge, JSM pagina automaticamente al secundario.
+10 min - Still No Ack - Manager / Team Lead: si el secundario no hizo acknowledge, JSM pagina al Manager o Team Lead.
+15 min - Unresolved - VP: si sigue sin acknowledge, se pagina al VP como nivel final de escalacion.

La escalacion es automatica e inmediata, no requiere que nadie dispare manualmente el siguiente nivel. Manten tu schedule y tu info de contacto en JSM siempre al dia.

## On-call — Expectativas de respuesta, triage y comunicacion
_chunk 1386 · 2026-07-27 · fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478025515011/On-Call+Operation+Guide+Support+L2+L3_

Recibir un page es solo el comienzo. Una vez que haces acknowledge, tomas ownership del ticket hasta la resolucion o un handoff apropiado.

Framework de triage:
P1 High/Critical (rojo): sistema caido, o datos de alto impacto que no cargan o no funcionan para el cliente. Es critico, arreglalo ya. Escala a Infrastructure si involucra CPU, red o certificados. Escala a Professional Services o CSM si es configuracion de cara al cliente.
P2 Medium (amarillo): el sistema funciona pero hay un problema de datos. Los datos se recolectan bien; el sistema opera. Puede esperar al siguiente dia habil. Documenta el issue y setea expectativas con el cliente.
P3 Low (verde): issue de ingenieria o codigo (no critico). Los bugs son normales y arreglables, mantente calmado. Apunta a resolver en 1-2 horas. Si se necesita un release completo, comparte el timeline claramente. Escala a Delivery para deployments o releases.
Importante: baja la prioridad si el triage revela que es menos severo de lo reportado (ej. delay de datos vs outage). Siempre agrega una nota de triage explicando tu decision de prioridad en los comentarios del ticket.

Estandares de comunicacion con el cliente:
- Reconoce primero su sentimiento: "Entiendo que esto impacta tus operaciones y lo estoy tratando como prioridad".
- Se transparente, no solo tecnico: el cliente necesita saber que esta roto, que estas haciendo y cuando esperar resolucion.
- Setea expectativas realistas: da un estimado aunque sea un rango. Under-promise, over-deliver.
- Actualiza proactivamente: no esperes a que el cliente pregunte. Envia updates al menos cada 30 minutos en P1/P2 activos.
- Nunca prometas una causa raiz antes de investigar.

## On-call — Rutas de escalacion, cierre y Quick Reference
_chunk 1387 · 2026-07-27 · fuente: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478025515011/On-Call+Operation+Guide+Support+L2+L3_

Rutas de escalacion por tipo de issue (no te quedes con un ticket que necesita atencion especializada):
- Professional Services: configuracion del cliente, temas de onboarding, setup de politicas.
- CSM Team: relacion con el cliente, comunicacion a nivel de cuenta, impacto en renovacion. Si se requiere, setea expectativas con el cliente y avisa al CSM. Recuerda: el CSM NO tiene rotacion on-call, lo tomaran en horario laboral.
- Delivery Team: issues de deployment, coordinacion de releases, promociones de ambiente.
- Infrastructure: recursos de servidor (CPU, memoria, disco), red, expiracion de certificados SSL/TLS, load balancer.
Al escalar, siempre deja una nota de handoff clara en el ticket JSM: que investigaste, que descartaste y que necesita saber el siguiente equipo.

Opciones de escalacion (links JSM, ver All On-Call Teams en Jira Operations):
- Secure/Incident: pagina segun hora UTC. 5:00-20:00 UTC pagina SRE Europe; 20:00-5:00 UTC pagina SRE Americas.
- Engage: schedule propio.
- Infrastructure (excepto RTI) y Infrastructure RTI: schedules separados.

Cierre de ticket / handoff:
- Actualiza el ticket con lo encontrado y lo que lo arreglo (causa raiz + nota de resolucion).
- Confirma con el cliente antes de cerrar, no autocierres sin confirmacion.
- Estado del ticket a Resolved.
- No estas solo: trae al secundario on-call antes de estrellarte, temprano si el issue es complejo. Si el secundario tampoco resuelve, escala al product expert del area.
- Deja una nota de handoff completa, taggea explicitamente al siguiente owner y dale un brief por Teams, no solo reasignes y desaparezcas.

Quick Reference Card:
- JSM Portal: Incidents (Operations, Jira).
- Trade on-call request: formulario Office (On-Call Shift Trade Request).
- Ack window primario: 5 min desde el page.
- Ack window secundario: 5 min tras escalacion del primario (+10 total).
- Ack window Manager/Lead: 5 min tras el secundario (+15 total).
- Escalacion final: VP, paginado a +15 min si sigue sin ack.
- Resolucion objetivo: 1-2 horas para la mayoria de issues de ingenieria.
- Issues solo de datos: pueden diferirse al siguiente dia habil si el sistema esta operativo.
