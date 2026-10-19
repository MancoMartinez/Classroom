# A quién asignar al escalar un RTS: Under Engineering Review vs Under Support Data Team Review

Fecha: 2026-08-27. Fuente: Confluence RTS en vivo más Jira en vivo.

## 1. Under Engineering Review

Fuente: "Escalating Tickets to L3 Departments: Procedures and Responsibilities", RTS 478006902856,
Aimee Wadsworth. La página se modificó hace una hora, así que está vigente.

| Producto | Assignee | Extra |
|---|---|---|
| Secure / Incident Engineering | Shandana Khan | Se auto crea un ENG y los comentarios sincronizan en ambos sentidos |
| Engage Engineering | Ian Williams | Mensaje obligatorio por Teams. Backups: Shruti Golwalker, Kenny Vu |
| RTI / RTIaaS | Dejar sin asignar | Los engineers lo toman de su cola |

Kevin Woo y Shruti manejan cambios de POS en Engage. Kevin también trickle transactions.

## 2. Under Support Data Team Review

Fuente: "Support Data Team Ticket Triage", RTS 477555982355, Aimee Wadsworth, 05-jul-2026.

Assignee: **Peyman Motlagh**. Él monitorea la cola del Support Data Team y reasigna al engineer que
corresponde. El engineer recibe correo del assignment.

Campos que van con la escalación:

- Label `Support_Data_Team`
- Team Ownership: "Support (Delivery dep.)"
- Sprint: "RCS Support Team"

Alcance del equipo: solo Secure 5. Ingest de data del retailer, data incorrecta en receipts o
reportes. No monitorea ningún otro producto.

## 3. Detalle que hay que tener presente

La página oficial de escalación L3 no lista el Support Data Team entre sus destinos. Para el camino
L2 documentado usa `Under Delivery Review` con Peyman Motlagh y Sprint "RCS Support Team". El status
`Under Support Data Team Review` sí existe en el workflow de RTS y hoy tiene 7 tickets abiertos.

Evidencia de cómo se usa hoy en RTS, tomada de RTS-206598 el 27-ago-2026. Anil P de L1 toma el
ticket, lo pasa a Work in progress, lo mueve a Under Support Data Team Review con el label
`Support_Data_Team`, y lo reasigna dentro de L1 a Ayesha Mehar. El status enruta, el assignee se
queda en L1. En los 50 tickets RTS que pasaron por ese status en los últimos 60 días, los 13
assignees distintos son todos del equipo L1 de India.

Los assignees reales del Support Data Team aparecen en los tickets viejos de esa cola:
Peyman Motlagh en RTS-177546, Luke Du en RTS-172310 y RTS-172317, Hao T Nguyen en RTS-168877.

Conclusión operativa: asigna a Peyman Motlagh y él distribuye. Si el ticket lo trabaja L1 y no L2,
el status solo enruta y el assignee no cambia.

## 3b. La matriz es de RCS, no de RTS

La página 478006902856 lo dice literal: "Please note the following status and/or assignee processes
when moving **RCS** tickets to different L3 departments". No hay matriz publicada de assignees para
RTS.

Medición en Jira, 27-ago-2026:

- RTS con assignee Shandana Khan, Peyman Motlagh o Ian Williams, creados en los últimos 365 días: 1
  ticket en total entre los tres.
- Los 15 RTS más recientes que pasaron por `Under Engineering Review` en 180 días conservan su
  assignee de L1 y llevan el label `L1`. Ninguno se reasignó a Shandana.
- RTS abiertos hoy en `Under Engineering Review`: 2. Uno sin asignar, uno con Matthew Kamminga.

En RTS el status enruta y el assignee se queda con el ingeniero de L1 que tiene el alert.

Camino que sí mueve a alguien en RTS, según "Process - Internal Alerts", espacio DS, Chris Howard,
12-ago-2026. Si el retry en Snowflake no lo arregla, escalar a Data Engineering por Teams y OpsGenie
y avisar en el canal Data Engineering > Alerts. Miembros al 12-ago-2026: Chris Howard,
Nicholas Turner, Saddam Hussain como manager.

Si el problema necesita comunicación con el cliente, L1 crea un RCS. Ahí sí aplica la matriz con
Shandana Khan o Peyman Motlagh.

## 3c. El único precedente del equipo: RTS-206268

Consulta en Jira el 27-ago-2026. Los 11 miembros del equipo Support solo han tocado 12 RTS en toda
la historia del proyecto. De esos, uno solo pasó por `Under Engineering Review`. Ese es el caso
completo.

RTS-206268, "[Grafana] - Kinney Drugs (KNY/179) - Active Alerts: 1". Reporter svc rts. Labels
Grafana, L1, cat-GR-Secure, grafana-cid-179, subcat-Work-Item.

Timeline medido del changelog:

| Fecha y hora | Quién | Qué hizo |
|---|---|---|
| 20-ago 20:22 | Automation | Initiate → Open |
| 20-ago 20:23 | Madhuraj Gujaran (L1) | Se asigna, pasa a Work in progress |
| 20-ago 20:49 | Madhuraj Gujaran | Se quita el assignee, pasa a `Under L2 Support Review` |
| 21-ago 10:19 | Diego Buelvas | Se asigna, pasa a Work in progress |
| 21-ago 12:34:06 | Diego Buelvas | Publica el informe de triage completo |
| 21-ago 12:34:17 | Diego Buelvas | Work in progress → `Under Engineering Review` |
| 21-ago 12:34:34 | Diego Buelvas | Se quita el assignee, queda sin asignar |
| 22, 23 y 24-ago | svc rts | El alert sigue firing, nadie de engineering lo toca |
| 24-ago 06:13 | Vlad Bogus | Comenta "Ticket Moved to RCS: RCS-28543" |
| 24-ago 06:14 | Vlad Bogus | Under Engineering Review → Completed, y Automation lo cierra |

Lo que hizo Diego: dejarlo sin asignar. Nadie de engineering lo recogió en tres días. El ticket se
resolvió convirtiéndolo en RCS-28543, y Vlad Bogus hizo esa conversión.

Lo que sí movió la aguja fue Teams. Shireesh Ramdas de L1 pegó el 21-ago a las 05:30 el link al
canal R&D > 2026 SnowTime con el mensaje de Daniel Endersby, y ahí quedó la causa raíz: la migración
SnowTime, error de compilación de Snowflake, invalid identifier `T2.POS_ARTICL...`. El diagnóstico
llegó por el canal, no por el status.

Conclusión operativa para el equipo. Al pasar un RTS a `Under Engineering Review` se deja sin
asignar, igual que la regla de RTI/RTIaaS. El status por sí solo no consigue que nadie actúe. Hay
que postear en el canal de Teams del dominio, Secure 5 Issues para Secure 5, y si hay impacto en
cliente hay que convertirlo en RCS, que es donde la matriz con Shandana Khan aplica de verdad.

## 4. Pregunta abierta para Aimee o Kristin

Pedir que la página 478006902856 agregue la fila del Support Data Team, con el status exacto y el
assignee. Hoy hay dos caminos, `Under Delivery Review` documentado y `Under Support Data Team
Review` en uso, y la página no los distingue.

## Fuentes

- https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478006902856
- https://trebuco.atlassian.net/wiki/spaces/RTS/pages/477555982355
- https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478022959146 (Queue Process)
- https://trebuco.atlassian.net/browse/RTS-206598
