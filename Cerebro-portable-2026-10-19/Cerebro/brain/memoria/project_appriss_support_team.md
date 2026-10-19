---
name: project_appriss_support_team
description: "Roster real del equipo Support Appriss (Teams) con puestos y país, fuente de verdad para asignar tickets RCS"
metadata: 
  node_type: memory
  type: project
  originSessionId: f3876df8-4a71-4754-9550-62264ecd309a
  modified: 2026-09-25T00:00:00.000Z
---

Roster real del equipo **Support Appriss**. Base original tomada de Teams el 3 ago 2026, corregida
el 25 sep 2026 contra `inbox/2026-09-04-cosecha-carga-equipo-completo.md` y
`inbox/2026-09-22-informe-tickets-equipo-ago-sep.md`. **Esta es la única fuente válida para decidir
asignaciones.** No deducir el equipo de quién tiene tickets en Jira, eso trae gente de otros equipos.

**Propietario del equipo**
- Camila Cortes, Support Manager (contractor). Hace seguimiento a clientes, no es asignataria técnica.

**Miembros (14)**

| Nombre | Puesto | Grupo | Nota |
|---|---|---|---|
| Juan Martinez | Lead Support Engineer | Colombia (es el usuario) | |
| Viraj Kansara | Lead Data Engineer (contractor) | India, es el otro lead, par de Juan | |
| Diego Buelvas | Full Stack Engineer (contractor) | Colombia | |
| Sebastian Rueda | Senior Data Engineer (contractor) | Colombia | |
| Edwin Garzon | Data Engineer (contractor) | Colombia | |
| Luis Hernandez | Senior Full Stack Engineer | Colombia | |
| Sebastian Garces | (rol no confirmado) | Colombia | entro despues del 3 ago, confirmado equipo Colombia en feedback_estilo_mensajes.md |
| Enrique Jimenez | (rol no confirmado) | Colombia | entro despues del 3 ago, sin tickets abiertos al 4 sep, activo desde entonces |
| Nikita Rathore | Full Stack Engineer (contractor) | India | |
| Vedant Shirude | Senior Full Stack Engineer | India | |
| Bikash Kumar | Data Engineer (contractor) | India | |
| Gulshan Kumar | DevOps / SRE (contractor) | India | |
| Megha Rathi | (rol no confirmado) | India | aparecio en Teams el 4 sep sin rol confirmado, tratada como India desde el informe del 22 sep |
| Harini Shankarakrishnan | (rol no confirmado) | India | aparecio despues del 3 ago, tratada como India desde el informe del 22 sep |

**David Vargas salio del equipo.** Estaba en la version anterior de este roster como Colombia. Cero
tickets propios y cero actividad en los ultimos 60 dias al 25 sep 2026. Ver
`inbox/2026-08-27-cosecha-salida-david-vargas.md`, "los tickets de quien sale del equipo nunca
aparecen en la cola sin asignar, hay que sacarlos por accountId".

Las cargas por persona ya no se guardan aqui porque envejecen en horas. Para carga actual, consulta
Jira en vivo o el informe mas reciente en inbox. **Regla que se mantiene:** los numeros crudos
enganan, hay que mirar cuantos estan en `Under Customer Review`, porque esperar no es trabajar.

Desambiguaciones que ya causaron errores:
- "Sebastian" en los mensajes de Peyman es **Sebastian Rueda**, no Sebastian Garces.
- "David" del equipo era **David Vargas**, ya no esta. David Beck y David Parraga **no** son del equipo.
- Charly Correa, Camilo Baquero, David Parraga y Andres Esteban **no** son del equipo, aunque aparezcan como asignatarios en RCS.

Ya salieron de la empresa: Tyrone Whitney, Carlos Jacinto (cuenta de Jira desactivada, ver [[project_flujo_tickets]]) y David Vargas.

Ver también [[project_appriss_support_role]] y [[feedback_comentarios_reglas]].
