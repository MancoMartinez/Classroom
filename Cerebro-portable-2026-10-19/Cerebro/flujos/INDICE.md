# Flujos y procesos

Cómo se hace cada cosa. Si vas a ejecutar un procedimiento, la respuesta ya está escrita aquí.
Curado a mano el 24 ago 2026, actualizado el 8 sep 2026. No lo regenera ningún script, se edita
cuando aparece un proceso nuevo.

## Reglas de trabajo que no se negocian

| Regla | Dónde |
|---|---|
| Jira es solo lectura. Juan ejecuta, Claude redacta | `brain/memoria/feedback_jira_read_only.md` |
| Todo entregable se escribe a `inbox/` en el momento | `brain/memoria/feedback_nada_solo_en_consola.md` |
| Los borradores se escriben al final, con la evidencia cerrada | `brain/memoria/feedback_borradores_al_final.md` |
| Leer el hilo de Teams completo antes de proponer hipótesis | `brain/memoria/feedback_leer_teams_antes_de_investigar.md` |
| Leer la fuente original, nunca el resumen que alguien hizo | `brain/memoria/feedback_verificar_la_fuente_no_el_resumen.md` |
| Agrupar por metadata no autoriza a afirmar causa raíz común | `brain/memoria/feedback_agrupar_no_es_causa_raiz.md` |
| No usar `created` ni `updated` de Jira como fecha de actividad | `brain/memoria/feedback_fechas_jira_updated.md` |
| Estilo de todo mensaje que Juan envía | `brain/memoria/feedback_estilo_mensajes.md` |

## Ciclo de vida de un ticket RCS

| Paso | Dónde |
|---|---|
| Flujo obligatorio para arrancar cualquier ticket | `brain/memoria/project_flujo_tickets.md` |
| Acuse de primer contacto: 3 o 4 frases, nada técnico | `brain/memoria/feedback_ack_primer_contacto.md` |
| Reglas de todo comentario de Jira y de asignación | `brain/memoria/feedback_comentarios_reglas.md` |
| Cómo se cierra de verdad: Resolve a Completed, después Close | `brain/memoria/reference_jira_rcs_workflow.md` |
| No comentar al cliente antes de Under Support Review | `brain/markdown/19-rcs-procesos-playbook.md` § regla de Shandana |
| Transición Work in progress a Under Customer Review, verificada | `brain/markdown/19-rcs-procesos-playbook.md` § verificación de la transición |
| Escalación a L3: estado, asignado y ticket que se autocrea | `brain/memoria/reference_escalacion_l3_procedimiento.md` |
| L2 a L3, revisión 13 octubre: diagrama transcrito, Peter Just para Solutions Experts y corrección de Ryan sobre Teams en Delivery | `inbox/2026-10-13-l2-l3-rcs-ticket-management.md` |
| A quién asignar al escalar un RTS: Engineering Review contra Support Data Team Review | `brain/markdown/19-rcs-procesos-playbook.md` § a quién asignar al escalar un RTS |
| Qué puede absorber soporte sin pasar por ingeniería, según Kiran el 28 ago | `brain/markdown/19-rcs-procesos-playbook.md` § ENG-6492 reunión con Kiran |
| Revisión de tickets en Completed antes de cerrarlos | `brain/markdown/19-rcs-procesos-playbook.md` § RCS-28334 |
| Reglas de asignación al equipo, cosecha del 28 ago | `brain/markdown/19-rcs-procesos-playbook.md` § cosecha asignación reglas |
| Feature requests: proceso Pendo e Ideas Portal, no ticket de ingeniería | `brain/markdown/16-rcs-soluciones.md` § proceso Pendo / Ideas Portal |
| Separar Incident de Secure 5 con Product Type cf[15196] | `brain/memoria/reference_jira_product_type_field.md` |
| On-call, operación y escalación en JSM | `brain/markdown/25-on-call-operación-escalación-jsm.md` |
| Dev workflow para un code change | `brain/markdown/24-appriss-dev-workflow-code-change.md` |
| Desbloquear una cuenta: la UI no escribe, va por base y exige reset de contraseña | `flujos/desbloquear-usuario-bloqueado.md` |
| SecurityLevel NULL, permisos o Session Error post migración: SELECT de Kiran en ENG-7189 compara SecurityID | `flujos/verificar-securityid-post-migracion.md` |

## RCA y comunicación con el cliente

| Paso | Dónde |
|---|---|
| Proceso oficial de RCA: Shorthand vs Report, SLA, ticket OUTM previo | `brain/memoria/reference_proceso_rca_appriss.md` |
| Guía completa para armar un RCA | `brain/markdown/19-rcs-procesos-playbook.md` § guía proceso RCA |
| Formato del tracker ADUSA y método de correo de J.R. Teagle | `brain/memoria/reference_tracker_adusa_formato.md` |
| Ciclo D1 a D6 del tracker ADUSA, día por día | `brain/markdown/26-adusa-estado-tickets-reuniones.md` |
| Dónde vive la ficha de cada cliente (CSM, PM, client ID) | `brain/memoria/reference_ficha_clientes_onboarding.md` |

## Diagnóstico: cómo medir antes de concluir

| Procedimiento | Dónde |
|---|---|
| Qué significa cada código de error y a qué memoria ir | `flujos/diagnostico-por-codigo-de-error.md` |
| Medir una queja de lentitud web con DevTools | `brain/memoria/reference_medir_lentitud_web_devtools.md` |
| Arreglar un problema de datos en ARDM | `brain/memoria/reference_ardm_playbook_peyman.md` |
| Acceso a bases de tenant por Bastion y SSMS, barrido cross database | `brain/memoria/reference_acceso_sql_tenants.md` |
| Jump servers US: nuevo VMPWUS2SHRDJUMP, ocho hosts con retiro anunciado el 14 octubre y archivos por recuperar | `inbox/2026-10-13-jump-server-us-consolidacion.md` |
| Retrospective de la Unificación y los labels pendientes | `brain/memoria/reference_confluence_unificacion_bucket_review.md` |

## Familias de fallas con mapa propio

Antes de investigar un síntoma que suena conocido, mira si ya tiene mapa.

| Familia | Dónde |
|---|---|
| Smart Alerts, siete mecanismos bajo el mismo síntoma | `investigaciones/smart-alerts-familia-de-fallas.md` |
| SSO, cuatro capas donde falla el login | `investigaciones/sso-cuatro-capas-donde-falla-el-login.md` |
| Timeout, 502, 524 y 499: qué es cada uno | `flujos/diagnostico-por-codigo-de-error.md` |
| Izenda en tenants migrados, dos rutas distintas | `brain/memoria/reference_izenda_adusa_dos_rutas.md` |
| Causas raíz recurrentes de la Unificación de julio | `brain/memoria/reference_unificacion_patrones.md` |

## El propio cerebro

| Qué | Dónde |
|---|---|
| Cómo se trabaja sobre esta carpeta | `MAPA.md` y `CLAUDE.md` |
| Origen del flujo buscar / guardar / exportar | `brain/memoria/project_flujo_trabajo_cerebro.md` |
| Por qué Moscú ya no razona y Claude es el motor | `brain/memoria/project_moscu_sin_gpt.md` |
| Costo real de mover Moscú a la API de Claude | `brain/markdown/27-cerebro-sistema-decisiones.md` |
| Rutina diaria y atajos de terminal en el Mac | `PASOS.md` § paso 9, y `cerebro.sh` |
| Por qué Cowork no puede escribir en la base, y qué hace en su lugar | `ESTADO.md` § dónde vive Cerebro |
| Clasificador de urgencia: cómo se mide y por qué caducan las etiquetas | `brain/markdown/27-cerebro-sistema-decisiones.md` § clasificador de urgencia |
