---
name: project_reparto_cola_2026_08_11
description: "Resultado del reparto de la cola RCS del 11 ago 2026: qué se aplicó, quién quedó sin nada, y los dueños por bucket que quedaron establecidos"
metadata: 
  node_type: memory
  type: project
  originSessionId: 8b73134e-5723-4d74-be14-e59eb99f9e25
  modified: 2026-08-12T00:15:03.542Z
---

Documento del reparto: https://claude.ai/code/artifact/2de558bd-f5aa-450c-9a81-7dc202f9064e

**La cola pasó de 46 sin asignar a 24** el mismo día. De 25 asignaciones propuestas se aplicaron 23 tal cual.

**Las dos que se desviaron eran las dos de Bikash Kumar**: RCS-28271 (Alshaya SBX) terminó con Nikita y RCS-28299 (PACSUN) con Aimee Wadsworth, cerrado como Duplicate. Bikash quedó sin un solo ticket del reparto.

**El hallazgo que hay que repetir en cada reparto**: la capacidad real del equipo con dos personas fuera eran unos 22 tickets contra 45 esperando. Repartir todo no es un plan, mueve el atasco de la cola a las colas individuales, que es lo que pasó el 3 de agosto. Ver [[project_backlog_triage_2026_08_03]].

**Dueños por bucket, la propuesta de J.R. que quedó funcionando** (derivada de lo que cada uno ya tenía, no inventada):

| Bucket | Dueño |
|---|---|
| Login, acceso, permisos, WAF | Juan |
| Attachments y print docs | Diego |
| Reports, exports, Izenda | Vedant |
| Alerts y notifications | David Vargas |
| Data integrity y feeds | Viraj y Bikash |
| Location hierarchy | Edwin |
| Timeouts y latencia | Gulshan |
| UI behavior | Nikita |

**El filtro 29803 se queda corto.** Devuelve menos que la consulta directa porque no indexa lo que entra el mismo día. Para un barrido completo: `project = RCS AND assignee IS EMPTY AND statusCategory != Done`.

**Cobertura de los que están fuera**: los tickets de una persona ausente nunca aparecen en la cola sin asignar, así que ningún reparto los toca. Hay que sacarlos a mano. Sebastián Rueda tenía 13 abiertos con dos High al irse, ver [[project_rcs_28077_28003]].

Relacionado: [[project_appriss_support_team]], [[reference_confluence_unificacion_bucket_review]].
