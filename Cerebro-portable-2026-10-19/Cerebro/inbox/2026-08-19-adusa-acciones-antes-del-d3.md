# ADUSA · acciones antes de armar el D3 · 19 ago 2026

Todo verificado contra Jira en vivo (7eb600cf-c7e0-43ed-acc4-90b277d43514, cloudId trebuco) entre
las 19:00 y 19:40 ET del 19 de agosto. El tracker interno "(2).xlsx" que compartiste (36 tickets,
encabezado "verified directly against Jira") coincide con esto salvo lo señalado abajo. No se
tocó Jira, solo lectura (getJiraIssue, searchJiraIssuesUsingJql, getTransitionsForJiraIssue).

Regla aplicada para mover a Under Customer Review: solo cuando el trabajo de Appriss ya está
hecho y lo único pendiente es la confirmación del cliente. Si sigue habiendo trabajo real de
nuestro lado, se queda en Work in progress aunque haya un comentario nuevo.

---

## 0. Housekeeping urgente, no es un comentario

**RCS-28177.** Jim confirmó por escrito en el ticket ("That is correct. I just updated the ticket
in JIRA") y hoy Jim además puso "Testing by users shows that the issue appears to have been
resolved". El ticket quedó en Closed, pero la automatización de Jira dejó esta nota hoy a las
12:11pm:

"@Viraj Kansara, your work item has been set to in 'Needs Attention - Add Resolution' because the
Resolution Details cascading field second dropdown value was left empty. Please transition this
issue back to Completed and select a value. THIS MAY HAVE BEEN BECAUSE THE REQUEST WAS INCORRECTLY
TRANSITIONED DIRECTLY TO CLOSED - PLEASE USE COMPLETED STATUS TO RESOLVE"

No hace falta comentario nuevo al cliente, esto ya está resuelto de cara a Jim. Sí hace falta que
alguien (Viraj o quien tenga permiso) entre y llene el segundo dropdown de Resolution Details en
Completed. Avisa si quieres que redacte algo para Viraj sobre esto, pero no es un comentario de
cliente.

---

## 1. Tickets que necesitan comentario al cliente hoy

### RCS-28342 — Anthony Lopez / títulos SSO (Janai, Stacie, Melanie)

Estado real en Jira: Under Customer Review, dueño Juan Martinez. Evidencia de hoy que aún no está
en el ticket: en el correo de Jim (11:34am) y las capturas que compartiste, después de cerrar
sesión y volver a entrar, los títulos siguen sin aparecer. Encontré algo concreto en las capturas:
Janai tiene dos cuentas, janai.harrison@adusa.com (activa, sin título) y
Janai.Harrison1@adusa.com (deshabilitada, con el título "Analyst Claims Adjuster"). Stacie Whetzel
solo tiene una cuenta y sigue sin título. Melanie Engelman sigue sin título. Jonathan Wright sí
tiene título (ese es otro ticket, ya cerrado).

Comentario sugerido (pegar como respuesta al cliente):

```
Hi Jim,

Thanks for testing. We found Janai's title is sitting on a second, disabled account
(Janai.Harrison1@adusa.com), not on her active one, and Stacie's and Melanie's active
accounts still show no title. Should the disabled account become the one in use for
Janai, or is there a different account we should treat as primary?

Thanks.
```

Transición: mover de Under Customer Review a Work in progress. El trabajo volvió a nuestro lado,
no es solo esperar confirmación.

Evidencia para adjuntar como nota interna (no al cliente): las capturas de Janai Harrison (las dos
cuentas), la lista de Users con las dos Janai, Stacie Whetzel, y Melanie Engelman. La de Jonathan
Wright sirve de contraste pero va mejor como referencia en el texto, no hace falta adjuntarla aquí.

### RCS-28093 — Employee search cruza marcas (Food Lion / Stop & Shop)

Estado real: Accepted into Development, dueño Matthew Kamminga (el tracker que me pasaste todavía
dice Edwin Garzon, está desactualizado en esa columna). Matthew reprodujo hoy a las 15:55 que el
entorno viejo se comporta igual, así que no es una regresión de la migración, y va a priorizar el
cambio. Por separado, en el correo de Jim (11:34am) llegó el ejemplo concreto que pedían: Tahj
Stone aparece en la búsqueda de Food Lion tienda 0001 siendo empleado de Stop & Shop. Ese ejemplo
todavía no está en Jira.

Comentario sugerido:

```
Hi Jim,

Thanks for the Tahj Stone example, that's exactly what we needed. We confirmed the same
cross brand result exists in the legacy environment too, so this isn't something the
platform move introduced. We're prioritizing a fix for the search filter now.

Thanks.
```

Transición: ninguna, se queda en Accepted into Development.

Evidencia interna: la captura de Manage Associates (Food Lion 0001, Tahj Stone) y la de Associate
Lookup.

### RCS-28196 — Campos NULL en AD Shoplifting Entry

Estado real: Work in progress, dueño Vedant Shirude. Esto sigue igual que lo que ya habíamos
concluido con la transcripción de la reunión: null y en gris es un estado intermedio aceptado,
el objetivo real sigue siendo blanco y ese trabajo no está terminado, así que no se mueve de
Work in progress. Pendiente real: Leigh Ann preguntó hoy a las 10:43am si hay otras páginas con
el mismo problema y quiere que se revisen si las hay.

Comentario sugerido:

```
Hi Leigh Ann,

Good question. Do you already have specific pages in mind where the same default might
show up, or would you like us to check the other incident entry pages for the same
pattern?

Thanks.
```

Transición: ninguna.

### RCS-28292 — Migración de servidor (archivo LPMS store file)

Estado real: Work in progress, dueño Gulshan Kumar. April respondió hoy a las 12:26pm la pregunta
sobre la IP pública: el archivo se transfiere por SFTP, no hace falta poner nada en whitelist.
Esto cierra la pregunta que Gulshan había dejado abierta el 18.

Comentario sugerido:

```
Hi April,

Thanks, that clarifies it. Since the transfer is SFTP based, no allow list change is
needed on our side. We'll have support monitoring the feed during the migration window
Thursday night into Friday morning as planned.

Thanks.
```

Transición: ninguna, ya estaba en Work in progress (no había pasado a Under Customer Review).

### RCS-28407 — 502 frecuente en LPMS

Estado real: Work in progress, dueño Edwin Garzon, vinculado a ENG-7344. J.R. comentó hoy 9:39am
que la frecuencia bajó pero no está eliminado. Leigh Ann reportó un caso nuevo y concreto hoy a
las 9:47am (después del comentario de J.R.): en Locations, al entrar a una tienda individual el
502 aparece en gris de fondo y la pantalla la regresa al listado. Referencia también RCS-28353.
Esto no tiene respuesta todavía.

Comentario sugerido:

```
Hi Leigh Ann,

Thanks for the detail on this morning's case. That symptom, the 502 in the background
and the drop back to the location listing, is being tracked under the same engineering
work (ENG-7344). We'll pass your example directly to that effort.

Thanks.
```

Transición: ninguna.

### RCS-28378 — Botones Save/Next, Hannaford

Estado real: Under Customer Review, dueño Vedant Shirude (el tracker decía sin asignar, está
desactualizado). Leigh Ann dijo el 18 a las 10:36am "confirming if working as intended, will
let you know", y no volvió a escribir. Ya pasaron más de 24 horas sin respuesta.

Comentario sugerido:

```
Hi Leigh Ann,

Following up, were you able to confirm with your team whether the Save and Next buttons
are working now?

Thanks.
```

Transición: ninguna, se queda en Under Customer Review.

### RCS-28161 — Export de Stores.csv

Estado real: Accepted into Development, dueño Shandana Khan. Matthew aclaró hoy a las 16:31 que
esto es el export a CSV de Manage Stores, un camino separado del de Izenda, no que ya esté
desplegado. Última actualización al cliente fue J.R. el 17 ("fix en test, actualizamos mañana").
Van más de 24 horas sin novedad para Leigh Ann.

Comentario sugerido:

```
Hi Leigh Ann,

Quick update, we traced this to the Manage Stores export specifically rather than the
Izenda side, and engineering is finishing that fix now. We'll confirm here once it's
live.

Thanks.
```

Transición: ninguna.

---

## 2. Tickets que ya quedaron cubiertos hoy, sin acción pendiente

- **RCS-28021** (Izenda export/502): ya tiene dos comentarios tuyos de hoy (18:14), completos y
  con los nombres de reporte correctos. Sin acción. Si quieres, se puede adjuntar como nota interna
  la captura de PBI Merchandise Export Q3-2026 y la de PBI Current Location Listing como evidencia,
  pero tu comentario ya las describe con suficiente detalle.
- **RCS-28413** (Central Division count): ya está en Completed en Jira (actualizado 18:37 de hoy),
  coincide con "client confirmed working as expected". Sin acción. Vale la pena confirmar que el
  segundo dropdown de Resolution Details quedó lleno, dado lo que pasó en el 28177.
- **RCS-28281** (transacciones 8/10 Secure): ya tiene tu comentario de hoy (18:45) con las cifras
  de backfill. Sin acción.
- **RCS-28304** (Case tier abreviado): Viraj ya le dijo al cliente ayer que está escalado a
  Engineering. La nota de Matthew de hoy (16:22) es interna, no cambia nada de cara al cliente.
  Sin acción.
- **RCS-28356** (latencia/502 Hannaford): tu pregunta de ayer (20:36) sigue sin respuesta de Leigh
  Ann, pero no llevamos ni 24 horas todavía. Sin acción por ahora.

---

## 3. Tickets nuevos: no existen los que aparecían en la nota que me compartiste

Revisé Jira en vivo (JQL `project = RCS AND created >= -3d`) y no hay ningún RCS-28433, RCS-28445,
RCS-28456 ni RCS-28472. Esos números no corresponden a ADUSA, esa lista viene de otra sesión que
se equivocó. Lo único nuevo de ADUSA fuera de los 35/36 tickets ya trackeados es:

| Ticket | Qué es | Estado | Dueño | Incluir en tracker cliente |
|---|---|---|---|---|
| RCS-28447 | Ahold-Delhaize - Izenda Access Issue (Application Error 404) | Closed, resuelto el mismo día 18 ago | Madhuraj Gujaran | Sí, ya está contado en el tracker interno (2).xlsx que subiste, dentro de los 36 |

No hay ningún ticket ADUSA huérfano ni sin dueño en este momento.

---

## 4. Resumen para pegar y actuar

| Ticket | Acción | Nota |
|---|---|---|
| RCS-28177 | Arreglo de Resolution Details en Jira, no comentario | urgente, mecánico |
| RCS-28342 | Comentario + mover a Work in progress | |
| RCS-28093 | Comentario, sin cambio de estado | |
| RCS-28196 | Comentario, sin cambio de estado | |
| RCS-28292 | Comentario, sin cambio de estado | |
| RCS-28407 | Comentario, sin cambio de estado | |
| RCS-28378 | Comentario, sin cambio de estado | check-in por 24h+ |
| RCS-28161 | Comentario, sin cambio de estado | check-in por 24h+ |
| RCS-28021 | Sin acción | ya cubierto hoy |
| RCS-28413 | Sin acción | ya Completed |
| RCS-28281 | Sin acción | ya cubierto hoy |
| RCS-28304 | Sin acción | ya cubierto por Viraj |
| RCS-28356 | Sin acción por ahora | menos de 24h |

El D3 para el cliente se arma después de que pegues estos comentarios y hagas la transición de
RCS-28342. Avísame cuando estén puestos y regenero el tracker cliente sobre el mismo D2 que ya
tienes, sin tocar el tracker interno.
