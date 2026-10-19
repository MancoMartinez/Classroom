# Investigaciones y hallazgos técnicos

Causas raíz ya establecidas y mapas de sistema. Antes de investigar de cero, mira si el patrón ya está aquí.
Curado a mano el 24 ago 2026, actualizado el 17 sep 2026. Se edita cuando cierra una investigación nueva.

## Excel de Urban: campos vacíos y exportaciones de cero filas

| Hallazgo | Dónde |
|---|---|
| RCS-26238: tipos Double en dos campos de texto, fix confirmado en PR 51987/52242. RCS-23141: mismo defecto con alta confianza histórica. RCS-28339: otra búsqueda, ocho filas frente a aviso de cero, causa pendiente; matriz de filtros, contexto y tareas, SQL de lectura y precedentes. | [Investigación y pruebas](excel-urban-root-cause-2026-09-17.md) |

## La Unificación de julio 2026, el hilo que explica casi todo

| Hallazgo | Dónde |
|---|---|
| Causas raíz recurrentes que deben guiar el diagnóstico | `brain/memoria/reference_unificacion_patrones.md` |
| Las tres tablas de identidad: membership.Users, LPUser, LPUser2 | `brain/memoria/reference_lpuser_lpuser2_membership.md` |
| Los 13 usuarios migrados ausentes de membership.Users | `brain/memoria/project_membership_users_13.md` |
| Qué host es Platform Unification y cuál el clásico | `brain/memoria/reference_hosts_pu_vs_clasico.md` |
| Bucket Uni_Jul_26_Attachments y por qué la validación no alcanzaba | `brain/memoria/project_uni_jul_26_attachments.md` |
| RCS-28535 ADUSA: Forbidden al subir video largo, cuatro hipótesis con discriminador | `investigaciones/RCS-28535-upload-forbidden.md` |
| Bucket review al 13 ago: 88 etiquetados, 50 abiertos | `brain/memoria/project_bucket_review_sesion2.md` |
| Chat de Unificación del 12 ago: PRs 55640 y 55972, AutoZone P1 | `brain/memoria/project_teams_unificacion_2026_08_12.md` |

## SSO y acceso: cuatro capas donde falla el login

Tocan 82 de las 443 fichas, el 18%. El cliente siempre reporta que los usuarios no pueden entrar, y
el fallo puede estar en el borde, en una dependencia interna, en el handshake o en lo que el propio
login reescribe. Empieza por el discriminador de cuatro preguntas.

| Hallazgo | Dónde |
|---|---|
| Las cuatro capas, con discriminador y cómo se separan entre sí | `investigaciones/sso-cuatro-capas-donde-falla-el-login.md` |
| Handshake y mapeo de claims en Incident: el SSO Response Log manda | `brain/memoria/reference_sso_incident_diagnostico.md` |
| Cloudflare bloqueando el egress de Zscaler Toronto, dos IP en el mismo /24 | `tickets/RCS-28556.md` |
| Key Vault 429 tumbando el SAML de Secure EBR, cuota compartida | `tickets/RCS-28779.md` |
| El login pisa la asignación de equipo: Mandatory Teams | `tickets/RCS-28631.md` |

## Identidad, permisos y alcance de usuario

| Hallazgo | Dónde |
|---|---|
| Mapa de tablas de usuarios y jerarquías en Incident | `brain/memoria/reference_esquema_usuarios_incident.md` |
| Cómo se resuelve el distrito: LHUA asigna tiendas, el distrito se hereda | `brain/memoria/reference_jerarquia_ubicaciones_incident.md` |
| Un usuario con dos distritos solo ve uno a la vez | `brain/memoria/reference_multidistrito_lhua.md` |
| Dónde vive cada cosa en Control Panel, y dónde NO está el flag Disabled | `brain/memoria/reference_control_panel_admin.md` |
| Diagnóstico de SSO/SAML: el SSO Response Log es el discriminador | `brain/memoria/reference_sso_incident_diagnostico.md` |
| RCS-28442 Torrid: por qué la premisa del ticket estaba mal | `tickets/RCS-28442.md` |
| RCS-28219 Nordstrom: por qué dan 403 los links y cómo reproducir | `tickets/RCS-28219.md` |

## Izenda, reportes y rendimiento

| Hallazgo | Dónde |
|---|---|
| Izenda en tenants migrados: el visor y la entrega leen fuentes distintas | `brain/memoria/reference_izenda_adusa_dos_rutas.md` |
| Izenda a 502 en Incident: causa raíz confirmada en vivo con el cliente | `brain/markdown/26-adusa-estado-tickets-reuniones.md` § reunión cliente 18 ago |
| Regresión de plan en SQL Server: estimador de cardinalidad 140 vs 160 | `brain/memoria/reference_query_store_regresion_plan.md` |
| Bloqueos de Cloudflare: sin Ray ID no se agrupa con nada | `brain/memoria/reference_waf_cloudflare_bloqueos.md` |
| Unauthorized Access al entrar directo a Izenda/AdHoc en nettrack, y el flag ViewReports | `brain/memoria/reference_viewreports_nettrack_legacy.md` |

## Smart Alerts y notificaciones

Tocan 46 de las 443 fichas de ticket, el 10%. El cliente siempre reporta "las alertas no llegan" y
debajo hay siete mecanismos que no comparten causa ni arreglo. Empieza por el discriminador.

| Hallazgo | Dónde |
|---|---|
| Los siete mecanismos, con discriminador de cuatro preguntas | `investigaciones/smart-alerts-familia-de-fallas.md` |
| `ManageSmartAlerts.aspx` no regenera `FiltersSQL` al editar tipos de auditoría | `tickets/RCS-27407.md` |
| 248 de 255 errores 500 en `POST SendSmartAlert.aspx`, medición del 31 jul | `brain/markdown/16-rcs-soluciones.md` |
| Los dos bugs de `SmartAlert.vb` en Platform Cohesion, y el precedente TempArea | `tickets/RCS-28452.md` |
| Frontera de fecha UTC: la alerta sale al día siguiente | `tickets/RCS-28294.md` |
| El PR que borró la alerta REASSIGN de `ReAssignCase.aspx.vb` | `tickets/RCS-28795.md` |

## Bugs de plataforma con arreglo conocido

| Hallazgo | Dónde |
|---|---|
| ChangeLocation deja el case number viejo, y RecreateCaseNo.aspx lo arregla | `brain/memoria/reference_recreate_caseno_changelocation.md` |
| Fallas de descarga de PDF: ERMS sube los archivos al directorio lpms | `brain/memoria/reference_erms_lpms_descarga_pdf.md` |
| Pantallas rotas o 404: rebuild vía Screen Designer con ?ADMIN=9QQP | `brain/memoria/reference_screen_designer_rebuild.md` |
| Feature flags: el valor efectivo puede ser CustomerEditedValue, no Value | `brain/memoria/reference_configuration_items_features.md` |

## Datos y plataforma

| Hallazgo | Dónde |
|---|---|
| En qué instancia de Greenplum vive cada cliente | `brain/memoria/reference_ardm_instancias_clientes.md` |
| SnowTime, monitoring y migración | `brain/markdown/20-snowtime-monitoring-migración.md` |
| RCS-27942 VS&Co: CartonClass y CartonContentCode vacios, dos ramas con discriminador | `investigaciones/RCS-27942-carton-class-content-code.md` |

## Personas y quién sabe qué

| Quién | Dónde |
|---|---|
| Roster real del equipo Support, fuente de verdad para asignar | `brain/memoria/project_appriss_support_team.md` |
| Peyman Motlagh: fuente de ARDM y pyardm, se va en diciembre 2026 | `brain/memoria/reference_peyman_motlagh.md` |
| Organigrama bajo Chris Rippingale | `brain/markdown/23-appriss-organigrama-chris-rippingale.md` |
| Accesos y herramientas que Juan ya tiene | `brain/memoria/project_juan_accesos.md` |
| Reparto de la cola RCS y dueños por bucket | `brain/memoria/project_reparto_cola_2026_08_11.md` |

## Cuentas con historia propia

| Cuenta | Dónde |
|---|---|
| Ahold Delhaize USA, Client ID 441: ficha y tickets | `brain/memoria/project_adusa_ficha_y_tickets.md` |
| ADUSA, escalación ejecutiva del 14 ago | `brain/memoria/project_adusa_escalacion_2026_08_14.md` |
| ADUSA, standup del 18 ago con Chris Rippingale y la causa raíz de la migración | `brain/memoria/project_adusa_standup_2026_08_18.md` |
| ADUSA, tracker de cliente del 18 ago construido y validado | `brain/memoria/project_adusa_tracker_cliente_18ago.md` |
| Tailored Brands RCS-28256 | `tickets/RCS-28256.md` y `brain/memoria/project_rcs_28256_tailored_brands.md` |
| United Supermarkets RCS-28240, SSO parado desde abril | `tickets/RCS-28240.md` y `brain/memoria/project_rcs_28240_united_supermarkets.md` |
| Ahold refund searches y Nike receipt address | `brain/memoria/project_rcs_28077_28003.md` |
| GAP canceladas en Identify y TG Jones SSO duplicado | `brain/memoria/project_rcs_27973_28283.md` |

## Fichas de triage de Confluence, el corpus de Diego

46 fichas del espacio RTS de Confluence, bajadas el 10 sep 2026 a `confluence/RTS-triage/`. Una por
ticket, formato fijo de 10 secciones, con causa raíz, evidencia y fix aplicado u opciones. Sirven de
precedente cuando llega un ticket con síntoma o requisitos parecidos.

| Qué | Dónde |
|---|---|
| Índice con ticket, cliente, síntoma, causa y familia | `confluence/RTS-triage/INDICE.md` |
| Refrescar el índice después de bajar fichas nuevas | `python3 bin/traer_confluence.py indice` |
| Bajar o actualizar desde Confluence, con credenciales | `python3 bin/traer_confluence.py bajar --carpeta 478142038021` |

Cuatro familias ya se repiten entre clientes. Antes de investigar de cero, revisa la familia:

| Familia | Fichas |
|---|---|
| Rename de columnas ARDM v1 a v2 sin resync del catálogo de campos de Secure | RCS-28606, RTS-206610, RTS-206268, RTS-206667 |
| Binding de campo por posición o por etiqueta que queda obsoleto al editar | RCS-28843, RCS-28841, RTS-206261 |
| Campo usado en el Synopsis que falta en los Display Fields de la búsqueda | RTS-205361, RTS-205224 |
| Duplicados por join a una tabla de referencia sin dedup aguas arriba | RCS-28077, RCS-28751, RCS-28746 |
| Job HATR NotificationEmail_Scheduled detenido por tenant, la notificacion queda en la app y no sale el correo. Arreglo: Run Now en Control Panel #/hatr/scheduled | RCS-29021 Claire's, RCS-29350 Wild Fork |

- `ingestion-api-como-entra-la-data.md`. Como entra la data del cliente: POST a la Ingestion API,
  routing por tamaño a Event Hub o Blob, las tres validaciones que rebotan con 401 y 400, y que es
  seguro compartir con el cliente. Usado en RCS-28756.
- `SBX-snowtime-work-items-mensuales-cero.md`. Starbucks c166, tres work items mensuales en cero en
  el periodo que cruza el cutover a SnowTime del 27 ago. Hipotesis de campos _EXT con placeholder
  X_, discriminadores y consultas. Corrige la ficha de Confluence de RCS-28873. RCS-29205/06/07.
