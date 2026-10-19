# Appriss Onboarding — Examen Knowledge Check (justificaciones)

Carpeta 15 de la base de Moscú. 31 fragmentos.

## Knowledge Check — resumen del examen y dominios
_chunk 619 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check del onboarding de Appriss Retail (30 preguntas, multiple choice), respondido y justificado el 2026-06-10. Cubre tres dominios: Plataforma & Productos (Q1-Q10: Secure, Engage, Incident, ARDM, Astromart, Azure, SnowTime, Work Items, LPMS), Ingeniería (Q11-Q20: patrón Director Controller→Director→Service→DAL, React con JavaScript, coverage 90%, Lunar, Azure SQL Managed Instance, docs/ por aplicación, feature flags en positivo, Azure DevOps Pipelines, Moq) y Soporte (Q21-Q30: RTS, RCS, Quick Entry, ticket grooming, SLA, incidents, Jira, Knowledge Base, CAMS/Secure Audit, Support como primer contacto). Cada chunk de este folder contiene una pregunta con su respuesta correcta, la justificación y la fuente documental. Documento interactivo: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html

## Knowledge Check Q1 — ¿Cuáles son los tres productos principales de Appriss Retail?
_chunk 620 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 1 (Plataforma & Productos).
Pregunta: ¿Cuáles son los tres productos principales de Appriss Retail?
Respuesta correcta: Engage, Secure and Incident
Justificación: El mapa de producto lista Secure 5/EBR, Engage (Return Auth) e Incident/Audit (netTrack) como familias principales. Las otras opciones mezclan herramientas internas (Hatr, Lunar, Control Panel) o tecnologías (SnowTime, SFTP) que no son productos.
Fuente: Base Conocimiento HTML — mindmap «Productos»; DOCX «Secure 5 es el producto central…»

## Knowledge Check Q2 — ¿Cuál es el propósito principal de la plataforma Secure?
_chunk 621 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 2 (Plataforma & Productos).
Pregunta: ¿Cuál es el propósito principal de la plataforma Secure?
Respuesta correcta: Retail loss prevention, incident management and investigations
Justificación: Secure es una plataforma SaaS multi-tenant de prevención de pérdidas (EBR): los analistas consultan datos transaccionales, surgen excepciones y los investigadores hacen seguimiento. No procesa pagos ni gestiona RR.HH.
Fuente: Engineer OnB secure.md: «Secure is an omnichannel exception-based reporting (EBR) and loss prevention platform»

## Knowledge Check Q3 — ¿Qué significa ARDM?
_chunk 622 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 3 (Plataforma & Productos).
Pregunta: ¿Qué significa ARDM?
Respuesta correcta: Appriss Retail Data Model
Justificación: Es la base analítica central: cada data area del search builder corresponde a tablas del ARDM. Multi-tenant por schema, normalizado para cualquier formato POS.
Fuente: DOCX: «El ARDM (Appriss Retail Data Model) es la base analítica central de la plataforma»

## Knowledge Check Q4 — ¿Cuál es el tenant demo/test usado por todos los equipos?
_chunk 623 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 4 (Plataforma & Productos).
Pregunta: ¿Cuál es el tenant demo/test usado por todos los equipos?
Respuesta correcta: Astromart
Justificación: Astromart es el tenant de prueba estándar para desarrollo local, con ClientID = 1. La app local corre vía Yarp en localhost:5001/astromart/signin.
Fuente: Glosario Onboarding: «Astromart. El tenant de prueba estándar para desarrollo local, con ClientID 1»

## Knowledge Check Q5 — ¿Qué es Engage?
_chunk 624 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 5 (Plataforma & Productos).
Pregunta: ¿Qué es Engage?
Respuesta correcta: A customer returns management platform at the point of sale and online
Justificación: Engage autoriza o niega devoluciones y reclamos en el punto de venta en milisegundos, usando modelos de riesgo sobre el historial del consumidor (Return Authorization/Verify, Claims, Order Protection, Incent).
Fuente: DOCX: «Engage, que autoriza o niega devoluciones y reclamos en el punto de venta en milisegundos»

## Knowledge Check Q6 — ¿Quiénes son los usuarios principales de Secure?
_chunk 625 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 6 (Plataforma & Productos).
Pregunta: ¿Quiénes son los usuarios principales de Secure?
Respuesta correcta: Loss prevention analysts, investigators, and store managers
Justificación: «Analysts build searches… Investigators follow up on the exceptions. Store managers see dashboards relevant to their location.» No son ingenieros, cajeros ni finanzas.
Fuente: Engineer OnB overview.md

## Knowledge Check Q7 — ¿Qué cloud provider usa Appriss Retail principalmente?
_chunk 626 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 7 (Plataforma & Productos).
Pregunta: ¿Qué cloud provider usa Appriss Retail principalmente?
Respuesta correcta: Azure
Justificación: Todo el stack es Microsoft Azure: Azure SQL Managed Instance, Azure Blob Storage (landing de archivos), Azure DevOps, Azure Functions, Azure Key Vault, Azure AI Search.
Fuente: DOCX stack: «…Microsoft Azure como nube»

## Knowledge Check Q8 — ¿Qué es SnowTime?
_chunk 627 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 8 (Plataforma & Productos).
Pregunta: ¿Qué es SnowTime?
Respuesta correcta: A data pipeline that moves raw files through DBT Core into Snowflake ARDM
Justificación: SnowTime es el pipeline de ingesta estándar de seis pasos sobre Azure + Snowflake + DBT: los archivos del cliente aterrizan cifrados en Blob Storage y se validan, descifran y normalizan al modelo ARDM con DBT Core.
Fuente: DOCX: «El estándar es SnowTime, un pipeline de seis pasos sobre Azure, Snowflake y DBT»; «ARDM schemas, cargados por el pipeline SnowTime con DBT Core»

## Knowledge Check Q9 — ¿Qué es un Work Item en Secure?
_chunk 628 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 9 (Plataforma & Productos).
Pregunta: ¿Qué es un Work Item en Secure?
Respuesta correcta: A flagged result from a search, assigned to an investigator's queue
Justificación: Las searches programadas generan work items que aterrizan en la cola de los investigadores; son listas de investigación para el personal de Loss Prevention, no tickets de Jira ni de soporte.
Fuente: DOCX flujo EBR: «las searches programadas generan work items que aterrizan en la cola de los investigadores»

## Knowledge Check Q10 — ¿Qué significa LPMS?
_chunk 629 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 10 (Plataforma & Productos).
Pregunta: ¿Qué significa LPMS?
Respuesta correcta: Loss Prevention Management System — the legacy name for Secure Incident
Justificación: Glosario: «LPMS. Loss Prevention Management System: el nombre legacy de Secure Incident en netTrack». Secure Incident (ex-LPMS) gestiona casos e incidentes confirmados.
Fuente: Glosario Onboarding + sección módulos de Secure

## Knowledge Check Q11 — ¿Cuál es el rol principal de un Director en la arquitectura backend?
_chunk 630 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 11 (Ingeniería).
Pregunta: ¿Cuál es el rol principal de un Director en la arquitectura backend?
Respuesta correcta: Orchestrate the business flow by calling services
Justificación: En el patrón de capas «Director/Service/DAL», el Director está entre el Controller y los Services: coordina el flujo de negocio llamando servicios. El Controller maneja HTTP, el DAL habla con la base; el Director no hace ninguna de las dos.
Fuente: Engineer OnB databases.md: «the Director/Service/DAL layers map closely to the underlying tables»
Nota: Matiz: en Secure 5, IDirector es además el objeto de contexto central (clientID, config, recursos, permisos) que se inyecta en todo el backend.

## Knowledge Check Q12 — ¿Cuál es el orden correcto de capas en el patrón Director?
_chunk 631 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 12 (Ingeniería).
Pregunta: ¿Cuál es el orden correcto de capas en el patrón Director?
Respuesta correcta: Controller → Director → Service → DAL
Justificación: El request entra por el Controller (HTTP), pasa al Director (orquestación), que llama Services (lógica), que usan el DAL (acceso a datos). Coincide con la mención «Director/Service/DAL» con el Controller por encima.
Fuente: Engineer OnB databases.md (orden Director/Service/DAL) + CLAUDE.md (Controllers reciben IDirector)

## Knowledge Check Q13 — ¿Qué framework frontend se usa para todo el trabajo nuevo de UI?
_chunk 632 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 13 (Ingeniería).
Pregunta: ¿Qué framework frontend se usa para todo el trabajo nuevo de UI?
Respuesta correcta: React with JavaScript
Justificación: React 18 + React Router 6, sin TypeScript: el type checking en runtime es por PropTypes. Angular es legacy en retirada; jQuery/Razor y Blazor no son el estándar.
Fuente: Engineer OnB CLAUDE.md: «PropTypes for runtime type checking (no TypeScript)»

## Knowledge Check Q14 — ¿Cuál es el coverage mínimo requerido de unit tests?
_chunk 633 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 14 (Ingeniería).
Pregunta: ¿Cuál es el coverage mínimo requerido de unit tests?
Respuesta correcta: 90%
Justificación: El estándar de unit testing fija 90% como mínimo en .NET. (El checklist de code review pide apuntar a 100% como objetivo y el frontend React opera con threshold del 53% — el «mínimo requerido» documentado es 90%.)
Fuente: Base Conocimiento HTML: «Coverage mínimo 90% en .NET»

## Knowledge Check Q15 — ¿Qué herramienta instala y hace seed de las bases de datos localmente?
_chunk 634 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 15 (Ingeniería).
Pregunta: ¿Qué herramienta instala y hace seed de las bases de datos localmente?
Respuesta correcta: Lunar
Justificación: Lunar (.NET 8) crea las bases, corre migrations de EF y aplica los seeds en cinco capas desde arpfiles, registrando en __SeedHistory. «El instalador es Lunar.»
Fuente: DOCX sección 3.7 + Engineer OnB lunar.md

## Knowledge Check Q16 — ¿Qué base de datos se usa para los datos core de la aplicación?
_chunk 635 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 16 (Ingeniería).
Pregunta: ¿Qué base de datos se usa para los datos core de la aplicación?
Respuesta correcta: SQL Server (Azure SQL Managed Instance)
Justificación: Las Application Databases (estado operacional: configuración, investigaciones, work items, usuarios) corren sobre SQL Server en Azure SQL MI. Snowflake es el warehouse analítico (ARDM), no el operacional.
Fuente: Engineer OnB databases.md: «Application databases (SQL Server on Azure SQL Managed Instance)»

## Knowledge Check Q17 — ¿Dónde deben colocarse los nuevos archivos markdown de documentación?
_chunk 636 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 17 (Ingeniería).
Pregunta: ¿Dónde deben colocarse los nuevos archivos markdown de documentación?
Respuesta correcta: In a docs/ folder at the root of the relevant application
Justificación: La convención observada en el repo: Sources/UI/ControlPanel/docs/architecture.md, Pipelines/docs/database-deployments.md, docs/04-development/yarp.md — cada aplicación lleva su carpeta docs/.
Fuente: Engineer OnB control-panel.md, snowflake.md, cache.md

## Knowledge Check Q18 — ¿Cuál es la convención correcta para feature flags?
_chunk 637 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 18 (Ingeniería).
Pregunta: ¿Cuál es la convención correcta para feature flags?
Respuesta correcta: enableFeature = true
Justificación: «La regla de diseño más importante: los flags se nombran siempre en positivo (enableWidget = true), nunca en negativo (disableWidget = false).» Ejemplos reales: Feature.EnableEmailSending, Feature.SsoEverywhere.Enabled.
Fuente: DOCX Parte IV 4.3 Feature Flags

## Knowledge Check Q19 — ¿Qué plataforma CI/CD se usa para builds y deployments?
_chunk 638 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 19 (Ingeniería).
Pregunta: ¿Qué plataforma CI/CD se usa para builds y deployments?
Respuesta correcta: Azure DevOps Pipelines
Justificación: Todo el build/deploy corre en ADO (dev.azure.com/apprissdevops): pipelines por cliente (ARDM Daily/Trickle), build-engagedatabase-production, FileTransform en deploys de Engage, etc.
Fuente: Engineer OnB README.md + docs DataOps

## Knowledge Check Q20 — ¿Qué librería de mocking se usa en los unit tests de C#?
_chunk 639 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 20 (Ingeniería).
Pregunta: ¿Qué librería de mocking se usa en los unit tests de C#?
Respuesta correcta: Moq
Justificación: «El framework preferido es Moq, con project mocks como alternativa.» Los tests de controllers mockean IDirector con new Mock<IDirector>().
Fuente: DOCX estándar de testing + Engineer OnB CLAUDE (1).md

## Knowledge Check Q21 — ¿Qué significa RTS en el contexto de soporte?
_chunk 640 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 21 (Soporte).
Pregunta: ¿Qué significa RTS en el contexto de soporte?
Respuesta correcta: Retail Technical Support
Justificación: RTS es el proyecto Jira / espacio Confluence hermano de RCS, asociado a alertas técnicas de infraestructura/data (ej. errores de GreenPlum). De las cuatro opciones, esta es la única plausible.
Fuente: Topic 1 KB glosario; KT Notes
Nota: ⚠️ En el glosario interno real, RTS = «Retail Tenant Support». Esa opción no aparece en el examen; la esperada es «Retail Technical Support».

## Knowledge Check Q22 — ¿Qué significa RCS?
_chunk 641 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 22 (Soporte).
Pregunta: ¿Qué significa RCS?
Respuesta correcta: Retail Customer Support
Justificación: «RCS — Retail Customer Support. El proyecto Jira principal donde aterrizan todos los tickets de soporte de clientes» (prefijo RCS-#####).
Fuente: Topic 1 KB glosario

## Knowledge Check Q23 — ¿Para qué se usa Quick Entry?
_chunk 642 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 23 (Soporte).
Pregunta: ¿Para qué se usa Quick Entry?
Respuesta correcta: A stripped-down interface for store staff to submit incidents without full Secure access
Justificación: «Quick Entry es la interfaz mobile para que el staff de tienda registre incidentes y complete auditorías sin acceso completo a Secure.» Los analistas configuran qué formularios están habilitados para Quick Entry.
Fuente: DOCX módulos de Secure

## Knowledge Check Q24 — ¿Qué es el «ticket grooming» en el workflow de soporte?
_chunk 643 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 24 (Soporte).
Pregunta: ¿Qué es el «ticket grooming» en el workflow de soporte?
Respuesta correcta: The process of reviewing support tickets and moving relevant ones to the Engineering backlog
Justificación: El grooming es la revisión periódica de la cola (cadencia diaria/semanal, prep de Kanban): se evalúan los tickets abiertos y los que requieren trabajo de producto pasan al Engineering Backlog. No es cierre automático ni asignación de severidad.
Fuente: Topic 1 KB — «Queue grooming & Kanban prep»; flujo «All Open — To be moved to Backlog»

## Knowledge Check Q25 — ¿Qué significa SLA?
_chunk 644 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 25 (Soporte).
Pregunta: ¿Qué significa SLA?
Respuesta correcta: Service Level Agreement
Justificación: Acuerdo de nivel de servicio: define los tiempos de respuesta/resolución comprometidos por prioridad. Los dashboards de soporte (Support Metrics) miden cumplimiento de SLA, CSAT y escalaciones.
Fuente: Topic 1 KB — Reports de SLA, Support Metrics Dashboard

## Knowledge Check Q26 — ¿Qué es un «incident» en el contexto de retail loss prevention?
_chunk 645 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 26 (Soporte).
Pregunta: ¿Qué es un «incident» en el contexto de retail loss prevention?
Respuesta correcta: A recorded event such as theft, fraud, or policy violation managed in the Incident module
Justificación: «Cuando una investigación confirma un evento de pérdida, se crea un incidente categorizado y rastreable» (theft, fraud, policy violation, training issue) en Secure Incident. No confundir con incidentes de producción/outages.
Fuente: Engineer OnB secure.md — Secure Incident (formerly LPMS)

## Knowledge Check Q27 — ¿Qué plataforma se usa para gestionar tickets de soporte?
_chunk 646 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 27 (Soporte).
Pregunta: ¿Qué plataforma se usa para gestionar tickets de soporte?
Respuesta correcta: Jira
Justificación: Todo el soporte vive en Jira (trebuco.atlassian.net): proyectos RCS, ENG, INT, DO; el portal de clientes es JSM (Jira Service Management) y la automatización sincroniza ENG → RCS.
Fuente: Topic 1 KB — flujo de tickets y dashboards Jira

## Knowledge Check Q28 — ¿Cuál es el propósito de la Knowledge Base del equipo de soporte?
_chunk 647 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 28 (Soporte).
Pregunta: ¿Cuál es el propósito de la Knowledge Base del equipo de soporte?
Respuesta correcta: A repository of known issues, solutions, and guides to help resolve support tickets consistently
Justificación: La KB (Confluence RCS + portal público) reúne known issues, troubleshooting, user guides y release notes para resolver tickets de forma consistente sin redescubrir soluciones.
Fuente: Base Conocimiento HTML: «Knowledge base pública: user guides, how-to, troubleshooting, release notes»

## Knowledge Check Q29 — ¿Qué módulo maneja los workflows de auditoría dentro de Secure?
_chunk 648 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 29 (Soporte).
Pregunta: ¿Qué módulo maneja los workflows de auditoría dentro de Secure?
Respuesta correcta: CAMS (the Audit module)
Justificación: «Secure Audit (nombre legacy: CAMS, Compliance Audit Management System) programa y puntúa auditorías de tiendas y distritos.» HATR es el job scheduler, Lunar el instalador — no módulos de auditoría.
Fuente: DOCX módulos de Secure + glosario

## Knowledge Check Q30 — Cuando un cliente reporta un problema de datos, ¿cuál es el primer punto de cont
_chunk 649 · 2026-06-10 · fuente: /Users/MancoMenStudio/Downloads/Justificacion_Examen_KnowledgeCheck_Appriss.html_

Examen Knowledge Check Appriss Retail — Pregunta 30 (Soporte).
Pregunta: Cuando un cliente reporta un problema de datos, ¿cuál es el primer punto de contacto?
Respuesta correcta: The Support team
Justificación: Los tickets de clientes entran siempre por Support (L1 triage → L2 investigación). Para data issues, Support hace el diagnóstico inicial (revisar el Azure Pipeline del cliente) y solo escala al Support Data Team o a Engineering (L3) si corresponde.
Fuente: Topic 1 KB — modelo L1/L2/L3 y diagnóstico «mis datos no cargaron»
