# Appriss — Dev Workflow (Code Change)

Carpeta 24 de la base de Moscú. 6 fragmentos.

## Code change 1/6 — Tickets: RCS vs ENG, clone y estados
_chunk 1157 · 2026-07-14 · fuente: ingesta-2026-07-14_

Guía "Making a Code Change - High Level Guide for Support" (sesión Chris Rippingale 2026-07-10; doc oficial publicado en Confluence ARPDT: https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/478006870071/Making+a+Code+Change+-+High+Level+Guide+for+Support). El equipo nuaav ejecutará el paso que Engineering hacía internamente. NOTA del doc: el proceso de clonar RCS→ENG está pendiente de confirmación de Shandana Khan (scrum leader).

Dos espacios Jira con roles distintos:
- RCS = interacción con el cliente. NUNCA se hacen cambios de código bajo tickets RCS.
- ENG = todos los cambios de código. Estados propios: In Development, Ready for Approval, Ready for Test, Tested…

Flujo: ticket RCS que requiere código → clonarlo a ticket ENG (Jira clone o link); quedan enlazados; el RCS sigue siendo la cara al cliente. Luego REFINAR el ticket ENG: ¿está claro? ¿hay ambigüedad/preguntas antes de empezar? (aplica también a tickets ENG que te manda un ingeniero).
Mantra de toda la guía: en CADA paso preguntarse "¿esto lo puede hacer Claude por mí?".
Al final del ciclo, en cada etapa hay que mantener el RCS actualizado con el cliente: "entendido, trabajando en ello" → "va en el release X" → "desplegado".
Se trabaja en dos boards en paralelo: Support (RCS) y Engineering (ENG).

## Code change 2/6 — Acceptance criteria temprano (desbloquea a QA) y arranque de código
_chunk 1158 · 2026-07-14 · fuente: ingesta-2026-07-14_

ACCEPTANCE CRITERIA: todos los tickets ENG tienen campo de acceptance criteria y es crítico ponerlo LO ANTES POSIBLE (Claude puede redactarlo). En cuanto existe, las automations del equipo QA empiezan a generar test plans, test cases y scripts ANTES de que el código esté listo. Dejarlo para cuando el PR está arriba = esperar más por QA. Si llega a Ready for Test sin acceptance criteria, QA no hace nada o lo devuelve Declined.

ARRANQUE DE CÓDIGO:
1. main actualizado (git pull) en el repo correcto.
2. Branch con convención: <nombre>/eng-<número>/<descripción> — ejemplo canónico del doc: `ripp/eng-1234/js-bug-on-explorer` (minúsculas). El número es del ticket ENG, no del RCS. (En SnowTime, mismo patrón con RCS: nombre/ticket/descripción.)
3. Cambiar el ticket ENG a In Development al empezar a codear.
4. Levantar la app local y REPLICAR el issue antes de tocar nada (sin replicar no hay fix verificable). Guía: página "Development Environment" en Confluence (ARPDT 475172667455).
5. Arrancar Claude CLI en la RAÍZ del repo (ej. C:\git\Secure) — si lo abres en un subdirectorio pierde docs, skills y contexto del repo. Pegar el ticket ENG a Claude: "go fix this". Para tareas grandes: plan mode y trabajar el plan juntos, o considerar mandarlo a Ratchet.
[Fuente: call Chris Rippingale / Juan Martinez 2026-07-10]

## Code change 3/6 — Developer checklist antes del PR (calidad, seguridad, UX)
_chunk 1159 · 2026-07-14 · fuente: ingesta-2026-07-14_

Checklist del desarrollador (página PR checklist en Confluence; el PR pide marcar conformidad). Lo esencial:
- Network tab (F12) abierta: sin cientos de requests Ajax, sin payloads gigantes, sin re-descargas (revisar caching; probar sin bypass de caché).
- Console JS abierta siempre: cero errores/warnings nuevos.
- Unit tests: responsabilidad del ingeniero (integration es más de QA). Decirle a Claude "escribe unit tests apuntando a 100% coverage" — lee los docs y tests existentes y lo hace bien. Arrange-Act-Assert estándar.
- Code style: reglas de naming, excepciones, performance, SQL en el wiki — Claude ya las lee. Rider las autocorrige (equipo migró de ReSharper/CodeMaid a Rider; muy recomendado sobre Visual Studio).
- Impersonation/personas: probar como investigator, analyst, etc. — tu login es "God mode", los clientes ven la app con permisos recortados. SSO local disponible (alt-click login).
- .NET trace mientras usas la feature: detecta LINQ ineficiente. OJO con queries LINQ malas (ToList temprano + order + where): funcionan local y explotan con 1M de filas — revisar especialmente las que mete Claude.
- ¿Tocaste cookies/SSO/seguridad? Justificar por qué y avisar a quién corresponda.
- Resourcing: NINGÚN texto hardcodeado en UI; magic strings resX. La app soporta ~260 idiomas (Azure AI traduce on-the-fly y persiste).
- Input validation: SIEMPRE client-side Y server-side (bypass trivial de UI = hallazgo de pentest).
- Estilos: nada inline fuera de Tailwind/Bootstrap utilities; todo en CSS files.
- Feature flags nuevos: documentarlos en el wiki.
[Fuente: call Chris Rippingale / Juan Martinez 2026-07-10]

## Code change 4/6 — UI bloopers: expectativas UX que QA sí revisa
_chunk 1160 · 2026-07-14 · fuente: ingesta-2026-07-14_

Lista "UI bloopers" (Claude también la lee para hacer QA — por eso es tan explícita):
- Back button del browser debe funcionar (no romperlo con estado).
- Links reales, no ng-click+window.open: el usuario debe poder right-click/middle-click → nueva pestaña.
- Escape cierra modales/lightboxes.
- Tab order correcto en formularios; Enter hace submit.
- Help bubbles donde la feature no sea 100% obvia.
- HTML titles y breadcrumb correctos (los usuarios navegan con el breadcrumb; se configura en los function components de React).
- Vernacular consistente: "OK" (no "Okay"); acciones de creación siempre "New" (nunca mezclar Add/Insert/Create).
- Widths razonables: inputs no estiran el ancho completo de la página; tamaños consistentes entre inputs.
- Disabled buttons sin outline.
- Responsive: la app se usa en móvil/tablet/desktop — no romper.
El look & feel importa: "funcionalmente correcto pero horrible de ver" no pasa.
[Fuente: call Chris Rippingale / Juan Martinez 2026-07-10]

## Code change 5/6 — Build en Azure DevOps y deploy a dev + defence testing
_chunk 1161 · 2026-07-14 · fuente: ingesta-2026-07-14_

BUILD (antes del PR, para probar fuera del laptop): Azure DevOps → Pipelines → carpeta "Azure builds" (las demás carpetas son legacy/ruido). URL: https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_build?definitionScope=\Azure\Builds — Deployments: definitionScope=\Azure\Deployments.
- Pipelines: Platform (cubre casi todo), Control Panel (propio), ARP files (config); edge cases: Python API, Returns. Cambio de código + config = 2 builds.
- Run pipeline → elegir TU branch → destildar los componentes que no cambiaste (ej. solo secure) → produce un artifact publicable.

DEPLOY a dev: Pipelines → Deployments → carpeta del componente → release pipeline del ambiente (US dev o EU dev; importa solo si el cliente es US/EU — ahí viven sus tenants).
- ANTES de deployar: mirar cuándo fue el último deploy; si fue hace minutos, IM directo en Teams a esa persona ("¿sigues usando US dev?"). No pisar el branch de un colega.
- En el wizard: el primer dropdown es el YAML del pipeline (ignorar); elegir el ARTIFACT de tu build (quitar el filtro para encontrar tu branch); en "stages to run" destildar todo salvo dev.
- CICD: cuando un PR completa a main, los non-prod (QA, showcase, CICD, dev) se actualizan solos (Control Panel; Platform es más complejo). Branching: todo sale de main y vuelve a main; release branch solo para prod, se actualiza desde main al final de la semana. "Keep it simple".

DEFENCE TESTING: probar tu cambio en dev (Control Panel → US Dev → login con AstroMart o cliente real) NO basta. Un peer debe revisarlo (5 min) antes de QA: hay campo en el ticket para registrar quién fue el defence tester (se asigna en sprint planning). Razón: QA son ~6 personas vs ~100 devs — respetar su tiempo llegando con calidad.
Existen skills de Claude para todo esto (ej. "Q build") pero hay que entender qué hacen por debajo.
[Fuente: call Chris Rippingale / Juan Martinez 2026-07-10]

## Code change 6/6 — PR, gates automáticos, QA, release y hotfix
_chunk 1162 · 2026-07-14 · fuente: ingesta-2026-07-14_

PR (Azure DevOps, template default):
- Título DEBE empezar "ENG-<número>" — un pipeline lo valida y rechaza el PR si falta.
- Contenido: respeto por el tiempo del reviewer. Issue en bullets, Solution en bullets, screenshot si hay cambio de UI, PRs relacionados linkeados con "!" (ej. cambio en ARP files + código), feature flags declarados (QA los necesita), notas extra en bullets. NO pegar paredes de texto generadas por Claude ("nadie las lee").
- Checklists del template: conformidad con developer checklist, probado localmente, probado en EU/US dev, defence tested. Checkboxes vacíos = nadie revisa tu PR.

GATES AUTOMÁTICOS al abrir el PR: (1) Codeant (reviewer AI; en el transcript sonaba 'Codan') comenta — se le puede decir a Claude "este es el PR, arregla los comentarios de Codeant"; (2) corre TODOS los unit tests — fallo = rechazo (decidir: ¿rompí el código o el test quedó obsoleto?); (3) code coverage — si tu cambio la baja, rechazo; (4) code style/análisis; (5) linting JS. Playwright corre nightly (plan futuro: por PR en contenedor). Cycle time actual de PR ≈ 15h; entre pares del equipo puede ser mucho menor.

ESTADOS: In Development → (PR arriba) Ready for Approval → completar PR con todos los comentarios resueltos (Codeant, Jira, StyleCop, lint, code coverage) → Ready for Test (entra a cola QA) → QA genera test cases + playwright scripts → Tested.
RELEASE: semanas 2 y 4; release branch se actualiza desde main y auto-deploya a STAGING. En release week: ir a staging y probar TUS cambios ("cradle to grave" — si explota en prod es tu problema; nadie quiere la llamada a las 2 AM). Fix en release week: PR a main (entra solo), o cherry-pick a release (deploya al completar el PR — lo más rápido), o branch desde release.
HOTFIX: solo P0 (moviliza a mucha gente). ARP files sí se pueden deployar en cualquier momento. Criterio de Chris: si algo que SIEMPRE funcionó se rompió (ej. Back button → 403), es incidente y se arregla ya; si nunca funcionó, puede esperar al release. Si encuentras un bug tras el approve de QA, regresar el estado y avisar.
[Fuente: call Chris Rippingale / Juan Martinez 2026-07-10]
