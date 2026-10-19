# Cosecha: a quién se asigna un RTS al escalarlo

Fecha: 2026-08-27. Sesión de origen: local_c3f3a283-f4b8-42d7-a140-4976e98ec0c5,
"RTS escalation team assignments". Medido contra Confluence y Jira en vivo.

## Hallazgo central

La matriz de assignees de L3 es de RCS, no de RTS. La página 478006902856 lo dice literal: "when
moving RCS tickets to different L3 departments". No existe matriz publicada de assignees para RTS.

En RTS el status enruta el ticket. El assignee se queda con el ingeniero de L1 que tiene el alert.

## Mediciones en Jira, 27 ago 2026

RTS con assignee Shandana Khan, Peyman Motlagh o Ian Williams, creados en los últimos 365 días: 1
ticket en total entre los tres.

Los 15 RTS más recientes que pasaron por `Under Engineering Review` en 180 días conservan su
assignee de L1 y llevan el label `L1`. Ninguno se reasignó.

RTS abiertos hoy en `Under Engineering Review`: 2. Uno sin asignar, uno con Matthew Kamminga.

En `Under Support Data Team Review`, sobre los 50 RTS que pasaron por ese status en 60 días, los 13
assignees distintos son todos del equipo L1 de India. Se agrega el label `Support_Data_Team` y el
assignee no cambia.

El equipo Support de Colombia ha tocado 12 RTS en toda la historia del proyecto. Uno solo pasó por
`Under Engineering Review`.

## El único precedente del equipo: RTS-206268

Grafana, Kinney Drugs (KNY/179), Active Alerts: 1. Reporter svc rts. Timeline del changelog:

| Fecha y hora | Quién | Qué hizo |
|---|---|---|
| 20-ago 20:49 | Madhuraj Gujaran (L1) | Se quita el assignee, pasa a `Under L2 Support Review` |
| 21-ago 10:19 | Diego Buelvas | Se asigna, pasa a Work in progress |
| 21-ago 12:34:06 | Diego Buelvas | Publica el informe de triage completo |
| 21-ago 12:34:17 | Diego Buelvas | Pasa a `Under Engineering Review` |
| 21-ago 12:34:34 | Diego Buelvas | Se quita el assignee, queda sin asignar |
| 22, 23 y 24-ago | svc rts | El alert sigue firing, nadie de engineering lo toca |
| 24-ago 06:13 | Vlad Bogus | Comenta "Ticket Moved to RCS: RCS-28543" |
| 24-ago 06:14 | Vlad Bogus | Under Engineering Review → Completed |

Diego lo dejó sin asignar. Nadie de engineering lo recogió en tres días. Vlad Bogus resolvió el caso
convirtiéndolo en RCS-28543.

La causa raíz no llegó por el status. Llegó por Teams. Shireesh Ramdas de L1 pegó el 21-ago a las
05:30 el link al canal R&D > 2026 SnowTime con el mensaje de Daniel Endersby. Causa raíz de ese
alert: la migración SnowTime, error de compilación de Snowflake, invalid identifier `T2.POS_ARTICL`.

## Procedimiento para el equipo

Al pasar un RTS a `Under Engineering Review`, dejarlo sin asignar. Misma regla que RTI/RTIaaS.

El status por sí solo no consigue que nadie actúe. Postear en el canal de Teams del dominio. Secure
5 Issues si es Secure 5.

Si hay impacto en cliente, convertirlo en RCS. Ahí sí aplica la matriz de L3 con Shandana Khan o
Peyman Motlagh.

## Camino de escalación a Data Engineering

Fuente: "Process - Internal Alerts", espacio DS, página 478102126595, Chris Howard, 12-ago-2026. Si
el retry del task en Snowflake no lo arregla, escalar a Data Engineering por Teams y OpsGenie, y
avisar en el canal Data Engineering > Alerts. Miembros al 12-ago-2026: Chris Howard, Nicholas Turner
y Saddam Hussain como manager.

## Matriz de L3 para RCS, referencia

| Producto | Assignee |
|---|---|
| Secure / Incident Engineering | Shandana Khan. Se auto crea un ENG y los comentarios sincronizan en ambos sentidos |
| Engage Engineering | Ian Williams. Mensaje obligatorio por Teams. Backups Shruti Golwalker y Kenny Vu |
| RTI / RTIaaS | Dejar sin asignar. Los engineers lo toman de su cola |
| Support Data Team | Peyman Motlagh. Label `Support_Data_Team`, Team Ownership "Support (Delivery dep.)", Sprint "RCS Support Team". Alcance solo Secure 5 |

## Fuentes

- https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478006902856
- https://trebuco.atlassian.net/wiki/spaces/DS/pages/478102126595
- https://trebuco.atlassian.net/browse/RTS-206268
- https://trebuco.atlassian.net/browse/RCS-28543

El detalle completo de esta sesión quedó en `inbox/2026-08-27-rts-escalacion-a-quien-asignar.md`.
