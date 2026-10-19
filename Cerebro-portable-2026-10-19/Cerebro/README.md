# Segundo cerebro — Juan Martínez

Exportado el 2026-08-24. 1648 fragmentos de conocimiento, 491 items de la mesa de trabajo, 67 memorias.

## Si eres Claude y acabas de abrir esto

Lee `MAPA.md` primero, elige la ruta y salta. Si quieres el orden largo:

1. `CLAUDE.md` — el contrato: reglas que no se negocian y por dónde entrar.
2. `brain/memoria/MEMORY.md` — el índice de memorias. Cada línea apunta a un hecho verificado.
3. `tickets/INDICE.md`, `flujos/INDICE.md`, `investigaciones/INDICE.md` — las tres vistas de trabajo.
4. `brain/markdown/` — la base de conocimiento entera en texto plano, un archivo por carpeta.
5. `brain/sessions.db` — la misma información en SQLite con FTS5.

Para buscar rápido sin abrir nada:

```bash
bin/buscar "lo que busques"
bin/buscar RCS-28535
grep -ril "lo que busques" brain/markdown/ tickets/
```

## Qué hay en la base

| # | Carpeta | Fragmentos |
|---|---|---|
| 14 | Appriss — Ingeniería (docs fuente) | 244 |
| 4 | Appriss KT — Proceso & Tracker | 166 |
| 11 | Appriss KT — Topic 1: Roster & Pendientes | 123 |
| 8 | Appriss KT — Topic 1: Customer & Consumer Support | 120 |
| 7 | Appriss KT — Topic 1: Fundamentos & Triage | 105 |
| 5 | Appriss KT — Topic 1: Núcleo & Escalación | 95 |
| 9 | Appriss KT — Topic 1: Data Pipeline & DevOps | 95 |
| 13 | Appriss Onboarding — Base de Conocimiento | 95 |
| 3 | Documentation tracker(Tracker) | 83 |
| 10 | Appriss KT — Topic 1: Dashboards & Métricas | 80 |
| 19 | RCS — Procesos & Playbook | 67 |
| 26 | ADUSA — Estado, Tickets & Reuniones | 62 |
| 21 | KT Kristin — Sign-off & Procesos RTS | 55 |
| 17 | Reuniones — Prep | 52 |
| 16 | RCS — Soluciones | 48 |
| 6 | Customer service | 32 |
| 15 | Appriss Onboarding — Examen Knowledge Check (justificaciones) | 31 |
| 1 | Onboarding Nuaav | 19 |
| 2 | Hoja de vida | 19 |
| 12 | KT — Preguntas para Aimee (Prep) | 15 |
| 18 | Appriss Secure — EBR | 11 |
| 20 | SnowTime — Monitoring & Migración | 10 |
| 25 | On-call — Operación & Escalación (JSM) | 7 |
| 24 | Appriss — Dev Workflow (Code Change) | 6 |
| 23 | Appriss — Organigrama (Chris Rippingale) | 4 |
| 27 | Cerebro — Sistema & Decisiones | 3 |
| 22 | Diseño — Sistema & Estilo | 1 |

## Memorias

- `feedback_ack_primer_contacto.md` — Un acuse de primer contacto son 3 o 4 frases sin nada técnico; y hay que releer la skill appriss-jira-support antes de escribir, no citarla de memoria
- `feedback_agrupar_no_es_causa_raiz.md` — Agrupar tickets por metadata de intake no autoriza a afirmar que comparten causa raíz; verificar comentarios antes de pasarle un patrón a otra persona
- `feedback_borradores_al_final.md` — No redactar comentarios ni mensajes mientras la investigación sigue abierta; primero cerrar la evidencia, después escribir
- `feedback_comentarios_reglas.md` — Todo comentario de Jira y todo análisis de asignación se redacta ya cumpliendo el skill appriss-jira-support, sin que Juan lo pida
- `feedback_estilo_mensajes.md` — Estilo para los mensajes que Juan envía (Teams, Jira, correo): sin guiones, humano y conciso, sin concluir más allá de la evidencia.
- `feedback_fechas_jira_updated.md` — No usar created ni updated de la API de Jira como fecha de silencio o de actividad; contar desde el último comentario real
- `feedback_jira_read_only.md` — Nunca escribir en Jira — solo leer. Juan ejecuta todos los cambios manualmente con un paso a paso que yo redacto.
- `feedback_leer_teams_antes_de_investigar.md` — Antes de proponer una consulta o una hipótesis, leer el hilo de Teams completo; el equipo suele haberlo hecho ya
- `feedback_nada_solo_en_consola.md` — Todo entregable se escribe a un archivo en el momento; Juan pierde respuestas buenas cuando se va a verificar algo y vuelve al scroll
- `feedback_verificar_la_fuente_no_el_resumen.md` — Leer el PR, el ticket o el documento original, nunca el resumen que alguien hizo de él en Teams
- `project_adusa_escalacion_2026_08_14.md` — La escalación ejecutiva de Ahold Delhaize del 14 ago 2026: quién la convocó, qué se comprometió, y qué quedó mal dicho
- `project_adusa_ficha_y_tickets.md` — Ficha de Ahold Delhaize USA (Client ID 441) y estado de los tickets de Juan al 14 ago 2026
- `project_adusa_standup_2026_08_18.md` — Standup ADUSA del 18 ago 2026 con Chris Rippingale, la causa raíz completa de la migración de usuarios y los compromisos con fecha
- `project_adusa_tracker_cliente_18ago.md` — Tracker del cliente ADUSA del 18 ago 2026 construido y validado, correo redactado, pendiente solo verificar 10 puntos contra Jira
- `project_appriss_support_role.md` — Juan es L2 Support Engineer en Appriss Retail (cola RCS en trebuco.atlassian.net); contexto de la migración/unificación de Incident en curso desde julio 2026.
- `project_appriss_support_team.md` — Roster real del equipo Support Appriss (Teams) con puestos y país, fuente de verdad para asignar tickets RCS
- `project_backlog_triage_2026_08_03.md` — Estado del triage de backlog del 3 ago 2026, reparto propuesto y qué quedó pendiente de verificar
- `project_bucket_review_sesion2.md` — Bucket review de la Unificación al 13 ago 2026: 88 tickets etiquetados / 50 abiertos, lo que la reunión agregó a la página de JR y las decisiones abiertas
- `project_estado_abierto_2026_08_05.md` — Estado del trabajo abierto al 5 ago 2026: RCS-28075, pedido de la próxima ola de unificación, y dónde están los documentos nuevos
- `project_estado_abierto_2026_08_11.md` — Corte del 11 ago 2026: qué queda pendiente ticket por ticket al cerrar el día
- `project_estado_abierto_2026_08_13.md` — Cola y pendientes de Juan al 13 ago 2026: lo que salió a PROD hoy, lo que le toca y las tres preguntas sin responder
- `project_estado_abierto_2026_08_18.md` — Estado abierto al 18 ago 2026 tarde — RCS-28379/Izenda global (ENG-5649), Stater Bros RCA (RCS-28431 sigue activo), tracker ADUSA del día
- `project_estado_juan_2026_08_11.md` — Estado de los 17 tickets de Juan al cierre del 11 ago 2026 y lo que quedó pendiente en cada uno
- `project_flujo_tickets.md` — Flujo obligatorio para trabajar cualquier ticket de Juan — arrancar siempre desde la base de conocimiento, no desde cero.
- `project_flujo_trabajo_cerebro.md` — La carpeta ~/Desktop/Cerebro es la raíz única del segundo cerebro desde el 18 ago 2026, con buscar/guardar/exportar como herramientas de terminal
- `project_interviewapp.md` — Overview of the InterviewApp project — a macOS interview assistant at ~/Desktop/InterviewApp; currently at Phase 0 (context only, no code).
- `project_juan_accesos.md` — Accesos y herramientas que Juan ya tiene en Appriss — no asumir que le faltan ni sugerir pedirle permisos a otros.
- `project_membership_users_13.md` — Investigación de los 13 usuarios migrados ausentes de membership.Users (jul 2026) y por qué Kiran Vadday vio resultados distintos.
- `project_moscu_second_brain.md` — Moscú second-brain vision + Phase 1-3 roadmap and the Microsoft Graph decision that overrides a CLAUDE.md non-negotiable
- `project_moscu_sin_gpt.md` — La key de Azure de Moscú murió (401 en chat y embeddings); Claude Code pasa a ser el motor de inteligencia y Moscú queda como almacén
- `project_moscu_state.md` — Estado actual de Moscú — segundo cerebro macOS local-first en ~/Desktop/InterviewApp/antigravity. Pases completados, stack, cómo construir.
- `project_rcs_27973_28283.md` — RCS-27973 GAP canceladas en Identify y RCS-28283 TG Jones SSO+ duplicado, estado al 12 ago 2026
- `project_rcs_28077_28003.md` — Estado al 11 ago 2026 de los dos tickets de Sebastián Rueda que cubrió Juan: Ahold refund searches y Nike receipt address
- `project_rcs_28240_united_supermarkets.md` — RCS-28240 United Supermarkets: el SSO del entorno de test lleva parado desde abril de 2026 esperando que Albertsons actualice su IdP
- `project_rcs_28256_tailored_brands.md` — RCS-28256 Tailored Brands al 13 ago 2026: sign in resuelto, quedan el salto lento a Incident y el timeout de Izenda (dueño: Jack), y cómo remedirlo
- `project_reparto_cola_2026_08_11.md` — Resultado del reparto de la cola RCS del 11 ago 2026: qué se aplicó, quién quedó sin nada, y los dueños por bucket que quedaron establecidos
- `project_teams_unificacion_2026_08_12.md` — Chat de Unificación, 12 ago 2026: performance de Chris, PRs 55640 y 55972, AutoZone P1 no es unificación, flags de Walmart 300
- `project_uni_jul_26_attachments.md` — El bucket Uni_Jul_26_Attachments al 13 ago 2026: los tres tickets, qué validó Juan del release y por qué esa validación todavía no alcanza
- `reference_acceso_sql_tenants.md` — Ruta de acceso a las bases de tenant por Bastion + SSMS, nomenclatura de las DB, mapa de Client IDs y el patrón de barrido cross-database
- `reference_ardm_instancias_clientes.md` — En qué instancia de Greenplum vive cada cliente, dónde está el Product Delivery Client Matrix y cómo se accede a los clusters
- `reference_ardm_playbook_peyman.md` — Procedimiento para arreglar un problema de datos en ARDM: rastrear el campo hasta su tabla de referencia, confirmar si la pantalla pega a Greenplum o Snowflake, respaldar y deduplicar
- `reference_configuration_items_features.md` — Los feature flags viven en secure.ConfigurationItem y el valor efectivo puede ser CustomerEditedValue, no Value
- `reference_confluence_unificacion_bucket_review.md` — La página de Confluence que es la base del retrospective de la Unificación: dónde está, qué contiene y los 3 labels que faltan aplicar en Jira
- `reference_control_panel_admin.md` — Dónde vive cada cosa en Control Panel para administrar usuarios, según Kiran Vadday en llamada, incluido dónde NO está el flag Disabled
- `reference_erms_lpms_descarga_pdf.md` — Causa raíz de las fallas de descarga de PDF: el módulo ERMS sube los archivos al directorio lpms
- `reference_escalacion_l3_procedimiento.md` — Procedimiento real de escalación de RCS a L3: estado, a quién se asigna y qué ticket se auto-crea, según el doc de Aimee
- `reference_esquema_usuarios_incident.md` — Mapa de tablas de usuarios y jerarquías en la plataforma Incident, explicado por Kiran Vadday el 30 jul 2026, y cómo compararlas sin equivocarse.
- `reference_ficha_clientes_onboarding.md` — Dónde vive la ficha de cada cliente (CSM, PM, dev engineers, client ID): los tickets RCS de Set Up System Monitoring. Incluye la de CWH cliente 248
- `reference_hosts_pu_vs_clasico.md` — Qué host es Platform Unification y cuál es la plataforma clásica, y por qué eso decide quién administra los permisos de un usuario
- `reference_izenda_adusa_dos_rutas.md` — Izenda en tenants migrados: el visor y la entrega programada leen fuentes distintas, y cómo distinguir cuál falla
- `reference_jerarquia_ubicaciones_incident.md` — Cómo se resuelve el alcance de distrito de un usuario en Incident: LHUA asigna tiendas, el distrito se hereda del StoreIdent primario
- `reference_jira_product_type_field.md` — El campo Product Type en Jira (cf[15196]) es el filtro correcto para separar Incident de Secure 5; verificado 6 ago 2026
- `reference_jira_rcs_workflow.md` — Cómo se cierra de verdad un ticket RCS: Resolve a Completed y después Close, y por qué el botón Close Ticket nunca aparece
- `reference_lpuser_lpuser2_membership.md` — Las tres tablas de identidad tras la Unificación: membership.Users se sembró de LPUser pero nettrack lee LPUser2, y ahí nacen los usuarios rotos
- `reference_medir_lentitud_web_devtools.md` — Protocolo para medir una queja de lentitud web con DevTools y decidir si el tiempo se va en el servidor o en el cliente
- `reference_multidistrito_lhua.md` — Un usuario con dos distritos asignados en LHUA solo ve uno a la vez; confirmado en Vitamin Shoppe el 11 ago 2026
- `reference_peyman_motlagh.md` — Peyman Motlagh, 13 años en Appriss, es la fuente de ARDM y pyardm, prefiere llamadas a chat, y se va en diciembre de 2026
- `reference_proceso_rca_appriss.md` — Proceso oficial de RCA en Appriss (Shorthand vs Report, SLA desde resolución, ticket OUTM previo, tres Claude Skills existentes) verificado en Confluence el 18 ago 2026
- `reference_query_store_regresion_plan.md` — Detectar una regresión de plan de ejecución en SQL Server con Query Store: el estimador de cardinalidad 140 vs 160
- `reference_recreate_caseno_changelocation.md` — El bug de ChangeLocation que deja el case number viejo, la herramienta RecreateCaseNo.aspx que lo arregla, y cómo verificar que no se duplicó el caso
- `reference_screen_designer_rebuild.md` — Truco de Kiran Vadday para arreglar pantallas rotas / 404 en un tenant: rebuild vía Screen Designer con ?ADMIN=9QQP
- `reference_sso_incident_diagnostico.md` — Cómo diagnosticar un fallo de SSO/SAML en un tenant de Incident: el SSO Response Log es el discriminador que dice de qué lado está el problema
- `reference_tracker_adusa_formato.md` — Cómo se arma el tracker de ADUSA para el cliente y el método de correo de J.R. Teagle, deducidos de sus archivos reales
- `reference_unificacion_patrones.md` — Causas raíz recurrentes de la Unificación de julio 2026, explicadas por Kiran Vadday, que deben guiar el diagnóstico antes de investigar desde cero
- `reference_waf_cloudflare_bloqueos.md` — Cómo se triagea un bloqueo de Cloudflare: la página de bloqueo dice si el disparador es contenido o país, y sin Ray ID no se agrupa con nada
- `user_profile.md` — The user is a Spanish-speaking macOS developer on a MacBook Air M4 who prefers free/local-first, privacy-respecting stacks.

## Cómo se regenera

```bash
./bin/exportar.sh
```

Cierra Moscú, copia la base con VACUUM, vuelca todo a markdown, reindexa los tickets, copia las memorias y comprime el bundle.

## Estructura

```
Cerebro/
├── MAPA.md            punto de entrada, elige la ruta según lo que vas a hacer
├── CLAUDE.md          el contrato para cualquier sesión de Claude
├── README.md          este archivo, generado
├── inbox/             todo lo nuevo cae aquí sin pensarlo
├── tickets/           una ficha por ticket, más INDICE.md (generado)
├── flujos/            procesos y cómo se hace cada cosa (curado a mano)
├── investigaciones/   causas raíz y mapas de sistema (curado a mano)
├── brain/
│   ├── sessions.db    la base de Moscú
│   ├── markdown/      la base en texto plano
│   └── memoria/       las memorias de Claude Code
├── bin/               los scripts
└── archivo/           lo viejo, guardado no borrado
```