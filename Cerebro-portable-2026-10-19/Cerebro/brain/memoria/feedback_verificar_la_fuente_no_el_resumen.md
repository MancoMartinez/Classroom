---
name: feedback_verificar_la_fuente_no_el_resumen
description: "Leer el PR, el ticket o el documento original, nunca el resumen que alguien hizo de él en Teams"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a8293f75-ab64-479b-971f-f586abf0f63b
  modified: 2026-08-14T19:30:01.793Z
---

Cuando alguien comparte un enlace con una descripción, la descripción puede estar mal. Abrir la fuente antes de razonar sobre ella.

**El caso, 13 ago 2026.** Chris Rippingale pegó en el chat de la Unificación los PR 55858 y 55859 llamándolos *"This caching optimisation"*. Los dos son en realidad **ENG-6975, Platform Cohesion - Self service incident user migration**, rama `ripp/rnd/incident-user-emails`: migración autoservicio de usuarios de Incident, no caché. Además el 55858 estaba **Active, con un conflicto de merge en `Program.cs`**, sin aprobación de los revisores requeridos y con 3 de 4 checks sin correr, o sea ni cerca de producción. Haberle creído al mensaje habría dejado todo el análisis del trabajo de caché apuntando al lugar equivocado.

**Why:** un mensaje de chat es la interpretación de una persona apurada, no el artefacto. En Appriss los PR, los changelogs de Jira y las páginas de Confluence dicen quién hizo qué y en qué estado está; el chat dice lo que alguien recuerda.

**How to apply:** si hay enlace, abrirlo y leer título, rama, estado, checks y archivos tocados antes de sacar conclusiones. Lo mismo con "ya está desplegado", "ya se cerró" o "es el mismo problema". Y decirlo explícitamente cuando la fuente contradice al mensaje, sin dramatizarlo.

**Segundo caso, 14 ago 2026, RCS-28021.** Se mandó a probar el visor interactivo de Izenda sin leer el comentario que la clienta había dejado esa misma mañana a las 09:29, donde decía *"users are receiving the same report daily"* y nombraba los dos reportes afectados. "Receiving" significaba entrega programada por correo, no correr un reporte en la aplicación. Matt lo señaló horas después. Se probó el reporte equivocado y por la ruta equivocada. **Antes de tocar la aplicación, leer los comentarios del ticket del día, no solo la descripción ni el resumen de la hoja de seguimiento.** Y el resumen de Rovo que aparece arriba del ticket lleva la etiqueta "Uses AI. Verify results", así que no cuenta como fuente.

**Restricción de acceso:** en Azure DevOps y en cualquier sistema ajeno, **solo consultar y leer, nunca modificar ni accionar**. Dicho textual por Juan el 13 ago: *"CONSULAR o LEER NUNCA MODIFICAR NI ACCINAR NADA"*. Nada de aprobar, comentar, hacer merge ni hacer clic en botones de acción.

Relacionado: [[feedback_leer_teams_antes_de_investigar]] (leer el chat es el primer paso, no el último), [[feedback_agrupar_no_es_causa_raiz]], [[feedback_jira_read_only]].
