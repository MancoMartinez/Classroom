# Plan de salida de David Vargas y reparto — 25 ago 2026

David trabaja hasta hoy. Tiene **14 tickets abiertos** y ninguno aparece en la cola sin asignar,
porque los tickets de una persona que sale nunca entran ahí. Hay que sacarlos a mano. Eso ya está
escrito en `brain/memoria/project_reparto_cola_2026_08_11.md`.

Nada pasa a Juan. Todo va al equipo, agrupado por cliente y por subsistema.

## 1. La foto completa

| Origen | Cantidad |
|---|---|
| Abiertos de David Vargas | **14** |
| Sin asignar en RCS | **25** |
| **Total a colocar** | **39** |

| Persona | Abiertos | Techo | Margen | Cupo hoy |
|---|---|---|---|---|
| Luis Hernandez | 0 | 5 | 5 | **2** |
| Sebastian Garces | 0 | 5 | 5 | **2** |
| Sebastian Rueda | 10 | 16 | 6 | **3** |
| Edwin Garzon | 12 | 16 | 4 | **3** |
| Diego Buelvas | 13 | 16 | 3 | **3** |
| | | | **23** | **13** |

Margen total 23 contra 39 esperando. El cupo de hoy es 13 porque el techo no se llena de golpe.

## 2. Los 14 de David, agrupados

Tres son High y los tres se colocan hoy.

| Cliente | Tickets | Subsistema |
|---|---|---|
| Nordstrom | 28219, 28270, 28300 | Workview, dashboards, fórmulas. Sara Beaty reporta los tres |
| Ollie's | 28085, 28484, 28485 | Acceso, filtros guardados, opciones de tipo y ubicación |
| McDonald's | 28158, 28223 | Alignment Report y Cash Audit. 28223 lleva `Escalated` y `Uni_Jul_26_SSOMapping` |
| Smart Alerts | 28465 Stater Bros, 28452 SpartanNash | Alertas y PDF adjunto |
| Sueltos | 28321 Boot Barn **High**, 28358 Wegmans **High**, 28531 Kohl's **High**, 28099 CWH | |

## 3. Día 1, hoy. Trece movimientos

### Diego Buelvas, +3, queda en 16

| Ticket | Cliente | Por qué |
|---|---|---|
| **RCS-28531** | Kohl's | Receipt Images Not Loading, **High**. Attachments y print docs es su bucket. Repite su **RCS-28510**, recibos de refund sin transacción original |
| **RCS-28358** | Wegmans | Something unexpected happened en pantalla de IMS, **High**. Rendering y UI. Callado 11 días, es el más abandonado de los tres High |
| **RCS-28219** | Nordstrom | Location ID Parameter en Workview. **La investigación ya está hecha**, en `tickets/RCS-28219.md`, por qué dan 403 los links y cómo reproducir. Arranca leyendo eso |

### Edwin Garzon, +3, queda en 15

| Ticket | Cliente | Por qué |
|---|---|---|
| **RCS-28321** | Boot Barn | Stores no pueden acceder a scheduled audits, **High**. Es su bucket de location hierarchy. Precedente exacto en `brain/memoria/reference_esquema_usuarios_incident.md`: *"Sin ninguna fila en `lhua`: el usuario no tiene asignación de ubicación. Síntoma: entra bien pero no ve tiendas"* |
| **RCS-28485** | Ollie's | Type y Location Options desaparecidas. Mismo modo de falla que Boot Barn, jerarquía de ubicaciones. Los dos juntos se resuelven de una |
| **RCS-28085** | Ollie's | User Access Incorrect. Está en `Under Customer Review`, cuesta poco, y mantiene Ollie's con un solo dueño |

### Sebastian Rueda, +3, queda en 13

| Ticket | Cliente | Por qué |
|---|---|---|
| **RCS-28465** | Stater Bros | Smart Alert Not Working. Precedente medido: en el análisis de RCS-28112, **248 de 255 errores HTTP 500** del app service de nettrack estaban en `POST /nettrack/api/internal/SendSmartAlert.aspx`. Rueda llevó el RCS-28106 de Santikos, mismo endpoint |
| **RCS-28534** | Stater Bros | Legal Follow Up Smart Alert not working. Sale de la cola sin asignar. **Mismo cliente y mismo subsistema que 28465.** Separarlos duplica el trabajo |
| **RCS-28158** | McDonald's | Alignment Report de agosto. Alineación de datos es su bucket. Está en `Under Customer Review`, cuesta poco |

### Luis Hernandez, +2, queda en 2

| Ticket | Cliente | Precedente que tiene que leer antes de tocar el ticket |
|---|---|---|
| **RCS-28557** | Smart & Final | Time out too short. `brain/markdown/16-rcs-soluciones.md` § RESPUESTAS-NUEVAS-2026-08-11: *"The session timeout for your users is now set to 240 minutes"*. Y `SYNC-L2-L3-RESUMEN-BILINGUE-2026-08-05`: *"Session timeout going from 300 to 30 minutes isn't a bug"*. Es config, no bug |
| **RCS-28524** | Rack Room | New User Login Issue. `brain/markdown/17-reuniones-prep.md`, llamada con Kiran Vadday del 3 ago: *"there is nothing called a new login. Any new login is a new email address"* |

### Sebastian Garces, +2, queda en 2

| Ticket | Cliente | Precedente que tiene que leer antes de tocar el ticket |
|---|---|---|
| **RCS-28556** | Vitamin Shoppe | User Blocked. `brain/memoria/reference_waf_cloudflare_bloqueos.md`. Sin Ray ID no se agrupa con nada. Pedir el Ray ID es el trabajo completo del primer turno |
| **RCS-28552** | Smart & Final | No puede reenviar casos a su manager. `brain/markdown/08-appriss-kt-topic-1-customer-consumer-support.md` § Reunión 22 jul, Access issues for Kimberly Baney, forwarding puesto a mano |

**Luis y Garces comparten cliente.** Mark Flores y Daniel Rodriguez son los dos de Smart & Final.
Tienen que hablarse antes de comentar. Smart & Final no puede recibir dos voces el mismo día. Esto
ya pasó con Leigh Ann en el reparto del 3 de agosto.

## 4. Estadística de limpieza

| Métrica | Antes | Después día 1 | Delta |
|---|---|---|---|
| Sin asignar en RCS | 25 | **20** | -5 |
| ADUSA sin asignar | 1 | **1** | 0 |
| Abiertos de David | 14 | **6** | -8 |
| Huérfanos totales | 39 | **26** | **-13** |
| High sin dueño | 3 | **0** | -3 |

**RCS-28547 de Ahold no entró hoy.** Es el único ADUSA sin asignar y su dueño natural es Rueda,
porque repite su **RCS-28523**, "Nordstrom Velocity Data 0 Loads". Los tres cupos de Rueda se
fueron a los dos Stater Bros y al McDonald's. Decide tú: si ADUSA pesa más que los Smart Alerts de
Stater Bros, saca 28158 de la lista de Rueda y mete 28547.

## 5. Día 2, mañana

Margen que queda después de hoy: Diego 0, Edwin 1, Rueda 3, Luis 3, Garces 3.

Lo que sigue pendiente de David, seis tickets:

| Ticket | Cliente | Dueño natural | Bloqueo |
|---|---|---|---|
| RCS-28484 | Ollie's | Edwin | Entra en su único cupo libre |
| RCS-28270 | Nordstrom | Diego | **Diego queda en techo** |
| RCS-28300 | Nordstrom | Diego | **Diego queda en techo** |
| RCS-28223 | McDonald's | Rueda | `Escalated` y `Uni_Jul_26_SSOMapping`. Necesita el contexto de la Unificación, ver `reference_sso_incident_diagnostico.md` |
| RCS-28452 | SpartanNash | Diego | PDF con TempArea, attachments. **Diego queda en techo**. Prioridad Low |
| RCS-28099 | CWH | Rueda | `Under Customer Review`, cuesta poco |

**El cuello de botella tiene nombre: Diego.** Queda en 16 con tres tickets de Nordstrom y
SpartanNash esperándolo. Tiene **5 en `Under Customer Review`**, y cada uno que cierre le abre un
espacio. Ese es el desbloqueo, no subirle el techo.

## 6. Lo que no cuadra y hay que decidir

**Margen 23 contra 39 huérfanos.** Faltan 16 espacios y entran tickets nuevos todos los días. Hoy
entraron seis. Con el techo en 16 y sin nadie que reemplace a David, la cola sin asignar no baja de
20. Ese es el número para J.R. y Camila, no una opinión.

**David reportó dos de sus propios tickets**, RCS-28484 y RCS-28485 de Ollie's. Los abrió el 19 de
agosto. Antes de repartirlos, alguien tiene que leer qué encontró él, porque el contexto se va con
él hoy.

**Pendiente de David antes de que se vaya:** un comentario interno en cada uno de los 14 con dónde
quedó. Sin eso, quien herede arranca de cero en catorce hilos.
