# Prompt para la consola con Atlassian

Copiar y pegar tal cual. Pide **solo lectura**, y pide el resultado en un formato que puedo
consumir directo.

---

```
Necesito que consultes Jira (instancia trebuco.atlassian.net, cloudId
7eb600cf-c7e0-43ed-acc4-90b277d43514) en MODO SOLO LECTURA y me devuelvas un reporte.

REGLA DURA: no escribas nada en Jira. No uses addCommentToJiraIssue, editJiraIssue,
transitionJiraIssue, createJiraIssue, createIssueLink, addWorklogToJiraIssue ni ninguna
operación de escritura. Solo getJiraIssue y searchJiraIssuesUsingJql.

Contexto: son los 35 tickets del cliente Ahold Delhaize USA (ADUSA, Client ID 441). Hoy 18
de agosto hubo una reunión con el cliente y hay que enviarle un tracker actualizado. Necesito
el estado real de Jira para no publicar nada que se contradiga con el sistema.

PARTE 1 — Tabla base de los 35 tickets

Corre este JQL:

key in (RCS-28014,RCS-28021,RCS-28023,RCS-28025,RCS-28030,RCS-28041,RCS-28042,RCS-28043,
RCS-28053,RCS-28059,RCS-28075,RCS-28093,RCS-28109,RCS-28115,RCS-28123,RCS-28124,RCS-28125,
RCS-28135,RCS-28161,RCS-28177,RCS-28196,RCS-28281,RCS-28292,RCS-28304,RCS-28342,RCS-28353,
RCS-28356,RCS-28364,RCS-28365,RCS-28369,RCS-28378,RCS-28379,RCS-28407,RCS-28413,RCS-28415)
ORDER BY key ASC

Campos: key, summary, status, assignee, reporter, priority, created, updated, resolution,
resolutiondate, issuelinks, labels.

Devuélvelo como una tabla markdown con una fila por ticket y estas columnas exactas:
KEY | STATUS | RESOLUTION | ASSIGNEE | PRIORITY | CREATED (dd/mm/yyyy) | UPDATED (dd/mm/yyyy)

PARTE 2 — Último comentario real de cada ticket

Para cada uno de los 35, dame el ÚLTIMO comentario que no sea de "Automation for Jira" ni un
acuse automático. Formato, una línea por ticket:

KEY | fecha y hora del comentario | autor | primeras 200 palabras del comentario

Si el último comentario real tiene más de 4 días, márcalo con [SIN MOVIMIENTO].

PARTE 3 — Verificación puntual, esto es lo que más necesito

Contéstame estas preguntas concretas, cada una con la evidencia (campo o comentario) que la
respalda:

1. RCS-28177, RCS-28364, RCS-28378 y RCS-28379: ¿el status y la resolución de Jira son
   coherentes con darlos por resueltos? ¿Alguno sigue abierto o sin resolución puesta?
2. RCS-28342: ¿quién es el assignee HOY? ¿Hay algún comentario del 18 de agosto? ¿Está
   enlazado a algún ticket de ingeniería (ENG)?
3. RCS-28415 y RCS-28413: ¿tienen assignee o siguen sin dueño? ¿Cuándo se les asignó?
4. RCS-28356 y RCS-28353: ¿están enlazados entre sí en Jira? ¿Alguno está marcado como
   duplicado del otro? Necesito saberlo porque en la reunión se dijo que 28356 es duplicado
   pero en la hoja sigue como ticket independiente de alta prioridad.
5. RCS-28196: ¿el status sigue siendo "Waiting for Software Release"? ¿Hay comentario del 18?
6. RCS-28124: ¿el status es "Under Customer Review"? ¿Cuál es el último comentario de
   Leigh Ann Stubbs?
7. RCS-28021 y RCS-28161: ¿están enlazados a ENG-5649 o a cualquier otro ticket ENG?
8. RCS-28281: ¿sigue asignado a Edwin Garzon? ¿Hay comentarios después del 11 de agosto?
9. ¿Alguno de los 35 cambió de status HOY, 18 de agosto? Lista cuáles y a qué status.
10. ¿Existe algún ticket RCS nuevo de ADUSA creado el 17 o el 18 de agosto que NO esté en la
    lista de 35 de arriba? Corre:
    project = RCS AND created >= "2026-08-17" AND (text ~ "ADUSA" OR text ~ "Ahold" OR
    text ~ "Food Lion" OR text ~ "Hannaford" OR text ~ "Stop & Shop" OR text ~ "Giant")
    ORDER BY created DESC

PARTE 4 — Contradicciones

Compara lo que encuentres contra esta tabla, que es lo que estoy a punto de enviarle al
cliente. Dime SOLO las filas donde Jira diga algo distinto:

RCS-28014 Closed / Resolved          RCS-28021 Work in progress / Active
RCS-28023 Closed / Resolved          RCS-28025 Closed / Resolved
RCS-28030 Closed / Resolved          RCS-28041 Closed / Resolved
RCS-28042 Closed / Resolved          RCS-28043 Closed / Resolved
RCS-28053 Completed / Resolved       RCS-28059 Closed / Resolved
RCS-28075 Closed / Resolved          RCS-28093 Work in progress / Active
RCS-28109 Completed / Resolved       RCS-28115 Completed / Resolved
RCS-28123 Work in progress / Active  RCS-28124 Under Customer Review / Pending Ahold verification
RCS-28125 Completed / Resolved       RCS-28135 Closed / Resolved
RCS-28161 Accepted into Development / Active
RCS-28177 Under Customer Review / Resolved
RCS-28196 Waiting for Software Release / Active
RCS-28281 Under Support Review / Active
RCS-28292 Work in progress / Active  RCS-28304 Work in progress / Active
RCS-28342 Under Customer Review / Active
RCS-28353 Work in progress / Active  RCS-28356 Work in progress / Active
RCS-28364 Under Customer Review / Resolved
RCS-28365 Under Customer Review / Resolved
RCS-28369 Under Customer Review / Resolved
RCS-28378 Under Support Review / Resolved
RCS-28379 Under Customer Review / Resolved
RCS-28407 Under Support Review / Active
RCS-28413 Under Support Review / Active
RCS-28415 Under Support Review / Active

(El primer valor es el status de Jira, el segundo es la categoría que le pongo yo al cliente.
"Resolved" de mi lado significa que el cliente lo dio por bueno, no que Jira esté cerrado, así
que no lo marques como contradicción salvo que el ticket esté claramente activo o reabierto.)

PARTE 5 — Formato de salida

Escribe todo a un archivo:
~/Desktop/Cerebro/inbox/2026-08-18-jira-verificacion.md

No resumas ni interpretes de más. Quiero los datos crudos con su evidencia. Si algo no lo
puedes obtener, dilo explícitamente en vez de rellenarlo.
```

---

## Por qué está pedido así

- **Solo lectura, explícito y con la lista de herramientas prohibidas.** La regla del proyecto
  es no escribir nunca en Jira, y un prompt que solo diga "consulta" puede terminar en un
  comentario publicado por accidente.
- **Parte 2 pide el último comentario real, no el campo `updated`.** El `updated` se mueve por
  automatizaciones y no sirve para medir silencio.
- **Parte 3 son las diez preguntas que hoy no puedo responder** y que afectan directamente lo
  que va en el correo y en la hoja.
- **Parte 4 le da la tabla contra la cual comparar**, así devuelve solo diferencias en vez de
  35 filas que ya tengo.
- **Parte 5 escribe a `inbox/`** para que quede en el Cerebro y yo lo pueda leer sin que me lo
  pegues.
