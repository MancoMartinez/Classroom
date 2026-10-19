# Carga completa del equipo Support Appriss, verificada en Jira, 4 sep 2026

Origen: captura de la pestaña Members de Teams que Juan compartió en el chat, 14 personas.
Cruce contra `brain/memoria/project_appriss_support_team.md` y `bin/asignar.py`, más consulta en
vivo a Jira para los 13 que sí tienen accountId confirmado.

## Tabla de carga por persona

| Persona | Total abiertos | Activa | Under Customer Review | High | Critical | Estados |
|---|---|---|---|---|---|---|
| Diego Buelvas | 12 | 6 | 6 | 2 | 0 | Under Customer Review 6, Work in progress 3, Under Engineering Review 1, Resolution Suggested 1, Waiting for Software Release 1 |
| Edwin Garzon | 16 | 11 | 5 | 3 | 0 | Work in progress 5, Under Customer Review 5, Under Support Review 3, Under Delivery Review 2, Escalated 1 |
| Sebastian Rueda | 16 | 15 | 1 | 0 | 0 | Work in progress 7, Under Support Review 6, Under Customer Review 1, Escalated 1, Waiting for Software Release 1 |
| Luis Hernandez | 6 | 5 | 1 | 0 | 0 | Work in progress 3, Under Delivery Review 1, Under Customer Review 1, Under Support Review 1 |
| Sebastian Garces | 8 | 4 | 4 | 1 | 0 | Work in progress 4, Under Customer Review 4 |
| Viraj Kansara | 17 | 15 | 2 | 2 | 0 | Resolution Suggested 8, Work in progress 3, Waiting for Software Release 3, Under Customer Review 2, Accepted into Development 1 |
| Nikita Rathore | 22 | 17 | 5 | 2 | 0 | Work in progress 16, Under Customer Review 5, Waiting for Software Release 1 |
| Vedant Shirude | 14 | 7 | 7 | 4 | 1 | Under Customer Review 7, Work in progress 4, Waiting for Software Release 2, Resolution Suggested 1 |
| Bikash Kumar | 24 | 20 | 4 | 0 | 0 | Work in progress 17, Under Customer Review 4, Resolution Suggested 3 |
| Gulshan Kumar | 20 | 15 | 5 | 2 | 0 | Work in progress 12, Under Customer Review 5, Under Support Review 1, Under Engineering Review 1, Resolution Suggested 1 |
| Megha Rathi | 7 | 5 | 2 | 0 | 0 | Work in progress 4, Under Customer Review 2, Under Support Review 1 |
| Enrique Jimenez | 0 | 0 | 0 | 0 | 0 | sin tickets abiertos en RCS |
| Camila Cortes | 2 | 2 | 0 | 0 | 0 | Work in progress 1, Under Support Review 1 |

Total general en RCS, statusCategory distinto de Done, entre las 13 personas: 164.

## Techo de Colombia contra la carga de ahora mismo

Sebastian Garces subió de 6 a 8 desde la corrida de reparto de esta mañana. RCS-28772 y RCS-28773,
los dos de Myer, entraron hoy y quedaron asignados a él fuera del reparto propuesto. Estaba un punto
sobre el techo de 5, ahora está tres puntos sobre el techo.

Diego, Edwin, Rueda y Luis se mantienen en los mismos números de la corrida de esta mañana, sin
cambios adicionales detectados.

## Dos nombres en la captura de Teams sin rol confirmado en el cerebro

Megha Rathi y Enrique Jimenez aparecen como Members en la pestaña de Teams. Ninguno de los dos
está en `brain/memoria/project_appriss_support_team.md` ni en el diccionario EQUIPO de
`bin/asignar.py`.

Megha Rathi ya sostiene 7 tickets RCS activos, incluidos RCS-28667 y RCS-28683, donde coordina
reproducción para ingeniería. No hay evidencia en el cerebro de si su rol es Colombia o India, ni si
cuenta para el reparto diario de la cola sin asignar.

Enrique Jimenez no tiene ningún ticket RCS abierto. Sin actividad registrada en el cerebro bajo ese
nombre antes de hoy.

Ninguno de los dos entra al diccionario EQUIPO ni a la lógica de techo hasta que Juan confirme rol,
país y si aplica el mismo tratamiento de nuevo que se le dio a Luis Hernandez y a Sebastian Garces
cuando entraron. Deducir esto de Jira sin esa confirmación es el mismo error que ya sacó cuatro
personas ajenas al equipo el 3 de agosto.

Camila Cortes tiene 2 tickets viejos a su nombre, RCS-28351 del 13 de agosto y RCS-28240 del 7 de
agosto. El roster la marca como no asignataria técnica. Vale confirmar si esos dos deben
reasignarse.
