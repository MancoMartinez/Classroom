BOARD EQUIPO COLOMBIA V2 (9 oct 2026). REEMPLAZA EL ALCANCE DEL PASO 1.

ALCANCE
Solo los tickets asignados a los 6 del equipo (Luis Hernandez, Sebastian Garces, Diego Buelvas, Edwin Garzon, Sebastian Rueda, Enrique Jimenez) mas el Supp Backlog, la cola sin asignar (JQL: project = RCS AND assignee IS EMPTY AND statusCategory != Done). Los tickets de Juan quedan fuera.
Supp Backlog hoy: 0 tickets.

LECTURA DE HOY 10:11 Bogota (100 tickets abiertos del equipo)
Esperando al cliente 57. El equipo trabaja 31. El cliente respondio y debe el equipo 12. Con alguna bandera 28.
Prioridad: 81 Medium, 16 High, 3 Low, 0 Critical.

BANDERAS DE HOY
Sin ownership del asignado (11 tickets, ningun comentario de nadie del equipo):
Luis RCS-29367, RCS-29366, RCS-29365 (Chanel), RCS-27407 (PPG, ya en Work in progress)
Enrique RCS-29363, RCS-29351, RCS-29233 (Home Depot, 141h desde que se creo)
Edwin RCS-29355, RCS-29353
Garces RCS-29352
Rueda RCS-29360
Nueve llegaron el 8 oct despues de las 11:00. RCS-29233 y RCS-27407 son los que ya pasaron cualquier plazo razonable.
High atrasados: RCS-29331 Home Depot (Garces, el cliente respondio hace 27h, limite 24h). RCS-29332 Nordstrom (Diego, Waiting for Software Release, 42h sin comentario del equipo).
Medium sin comentario del equipo mas de 4 dias: RCS-28814 (Diego 285h), RCS-28744 (Edwin 241h), RCS-29122 (Enrique 236h), RCS-28508 (Edwin 193h), RCS-29126 (Enrique 159h), RCS-28274 (Edwin 145h), RCS-26420 (Garces 144h).
Seguimiento al cliente vencido (Under Customer Review, mas de 3 dias habiles): RCS-28591 (Edwin 10d), RCS-28866 (Rueda 7d), RCS-28956 (Garces 5d), RCS-28976 (Edwin 4d), RCS-29230 High, RCS-29020, RCS-28863 (Garces 3d), RCS-29147 (Enrique 3d).

DISENO DE ALERTAS
1. Jira Automation, evento inmediato, sin depender del Mac: ticket creado o reasignado con prioridad Critical o High, y ticket que queda sin asignar mas de 15 min en el Supp Backlog. Accion: Send web request al Workflow de Teams.
2. Script local, cada 15 min dentro de turno: calcula atrasos por persona. Cada alerta lleva ticket, dueno, prioridad, cliente y motivo. Guarda estado para no repetir la misma alerta antes de 2 h.
3. Lectura diaria de Claude a las 8:30: por cada ticket abierto, clasifica si el equipo puede avanzar, debe investigar, espera al cliente o espera a Engineering. Eso es juicio de contenido y no sale de una regla.

FORMATO DE LA ALERTA EN TEAMS
RCS-29331 | Sebastian Garces | High | The Home Depot | El cliente respondio hace 27h y no hay respuesta del equipo (limite 24h)

SUPUESTOS A CONFIRMAR
Plazo de triage: Critical 15 min, High 1 h, Medium 4 h de turno desde la asignacion.
Los estados Waiting for Software Release, Under Delivery Review y Under Product Mgmt Review corren el limite de comentario igual que los demas.
Seguimiento al cliente a los 3 dias habiles. Jira ya envia un correo al asignado a los 7 dias.
High cuenta 24 h sin sabados ni domingos. Critical cuenta 30 min dentro del turno de cada persona.

LIMITE CONOCIDO
El plazo de triage necesita la hora de asignacion, que sale del changelog. El script la lee con expand=changelog.
