BOARD EQUIPO COLOMBIA, PASO 1: DATOS Y FILTROS (8 oct 2026)

HALLAZGOS EN JIRA (RCS, cloudId 7eb600cf-c7e0-43ed-acc4-90b277d43514)
Equipo: Luis Hernandez, Sebastian Garces, Diego Buelvas, Edwin Garzon, Sebastian Rueda, Enrique Jimenez (accountId 712020:153a3fea-8720-4528-b10f-5196a5d5fb21, 14 abiertos). Juan va aparte con 12.
Abiertos sin Enrique: 97. Under Customer Review 60, Work in progress 21, Under Support Review 11, Waiting for Software Release 2, Under Delivery Review 2, Under Product Mgmt Review 1. Existe tambien el estado Escalated (Enrique, 1 ticket).
Prioridades: Critical, High, Medium, Low. Hoy 79 Medium, 16 High, 2 Low en el grupo de 97.
SLA de Jira (JSM): Target Assignment Time (customfield_18575), Target First Response (customfield_18672), Assigned Team First Response (customfield_18673), Time to resolution (customfield_15187). Hay variantes TJX 74 a 78.
Solo 15 de 97 tienen Time to resolution corriendo. RCS-28281 marca 665h vencido con el reloj pausado. El SLA de Jira no mide tu regla de comentarios. Calcula la edad del ultimo comentario en el script.
La frase "taken ownership" aparece en 12 de 111 tickets. Detecta el triage por autor del primer comentario, no por texto.

REGLAS ACORDADAS
Horario Bogota: equipo 8 a 17, Juan 9 a 18, Garces y Enrique 10 a 19. Alertas solo dentro del turno de cada persona.
Triage hecho: primer mensaje de ownership del asignado mas el ticket con lo necesario para avanzar, en Under Support Review o Work in progress.
Maximo sin comentario del equipo: Critical 30 min, High 24 h, Medium 4 a 5 dias. Si el equipo prometio algo, manda la promesa.

FILTROS JQL (validados contra Jira el 8 oct)
Filtro 1, nombre "Colombia abiertos" (base):
project = RCS AND statusCategory != Done AND assignee in ("712020:7cb67354-171b-4f4b-b5f6-46a5c57cbd4d","712020:239d8bd1-42fb-47ac-8e49-8698e657fbba","712020:20065f69-a041-443a-8b58-b79b1649d0b4","712020:9e64bce4-462c-48d2-887a-2d2e3dee5936","712020:ae769ae6-4093-403d-847f-a3a13075b642","712020:153a3fea-8720-4528-b10f-5196a5d5fb21")

Filtro 2, "Colombia estado fuera de flujo" (hoy 1 ticket, RCS-29224 en Escalated):
filter = "Colombia abiertos" AND status not in ("Work in progress","Under Support Review","Under Customer Review","Waiting for Software Release","Under Delivery Review","Under Product Mgmt Review")

Filtro 3, "Colombia sin movimiento por prioridad" (hoy 10 tickets):
filter = "Colombia abiertos" AND status != "Under Customer Review" AND ((priority = Critical AND updated <= -30m) OR (priority = High AND updated <= -24h) OR (priority in (Medium, Low) AND updated <= -4d))

Filtro 4, "Colombia SLA Jira vencido" (hoy 25 tickets):
filter = "Colombia abiertos" AND ("Target First Response" = breached() OR "Target Assignment Time" = breached() OR "Time to resolution" = breached())

LIMITES DE LOS FILTROS
updated cambia con cualquier edicion, no solo con comentarios. Cuenta horas corridas, no horas de turno. El script del paso 3 corrige las dos cosas.

HORARIO DE VERANO
Jira Automation programa el cron en la zona horaria del sitio. EE.UU. sale de horario de verano el 1 nov 2026 y el cron se corre una hora respecto a Bogota. El script usa America/Bogota explicito.

PENDIENTE DE JUAN
1. Crear los 4 filtros en Jira, guardarlos y compartirlos contigo.
2. Crear el Workflow de Teams en tu canal: "Post to a channel when a webhook request is received". Guarda la URL, no la pegues en chats.
3. Crear un API token en id.atlassian.com/manage-profile/security/api-tokens y guardarlo en el Keychain del Mac.
