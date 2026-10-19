---
name: "cerebro-cola"
description: "Refresca y muestra la cola de tickets RCS de Juan Martinez ordenada por urgencia real, desde Jira en vivo. Usala cuando Juan pida su cola, sus tickets, el panorama, que hay pendiente, por donde empiezo, que debo responder hoy, a quien le debo respuesta, o el avance de la semana. Para trabajar un ticket concreto usa cerebro-ticket."
---

# Cola de Juan, por urgencia real

Salida corta. La cola es una lista de decisiones, no un informe.

## 0. Carpeta obligatoria

Busca `MAPA.md` y `brain/sessions.db`. Si falta, detente y pidela con
`mcp__cowork__request_cowork_directory`. Se llama `Cerebro-AAAA-MM-DD`.

Sin `bitacora/` le vas a decir que debe una respuesta que ya dio. Sin `brain/memoria/` no tienes
las reglas. Un resultado incompleto que parece completo es peor que ninguno. Sigue sin la carpeta
solo si Juan lo ordena explicito.

Rutas relativas a esa carpeta. Las reglas de estilo y las prohibiciones estan en su `CLAUDE.md`.

## 1. Jira en vivo

    searchJiraIssuesUsingJql
    cloudId: trebuco.atlassian.net
    jql: project = RCS AND assignee = currentUser() AND statusCategory != Done ORDER BY updated DESC
    maxResults: 50
    fields: ["summary","status","priority","assignee","reporter","created","updated","labels","duedate","comment"]

La respuesta pasa de doscientos mil caracteres y se derrama a disco. No la leas, te quema el
contexto. Localiza el derrame y copialo:

    F=$(ls -t <ruta>/tool-results/*searchJiraIssuesUsingJql* | head -1)
    cat "$F" > cola/jira-dump.json

## 2. Clasificar y medir

    python3 bin/cola.py cola/jira-dump.json
    python3 bin/eval_cola.py

Si la exactitud baja de 100 por ciento, dilo antes de mostrar nada. El lexico de promesas o de
preguntas se desactualizo y el orden puede estar mal.

## 3. Mostrar. Techo quince lineas

Lee `cola/estado.json`, no el markdown. No pegues `cola/COLA.md` en el chat, Juan lo abre si quiere.

Primero el conteo por nivel. Niveles 1 y 2, una linea por ticket: key, cliente, dias callado,
motivo en cinco palabras. Niveles 3 y 4, solo conteo y los keys.

| Nivel | Que significa |
|---|---|
| 1 | Te toca responder. El ultimo humano de cara al cliente fue el cliente |
| 2 | Promesa sin cumplir. Appriss prometio un update que no llego |
| 3 | Esperando al cliente. A los siete dias toca perseguir |
| 4 | Movimiento interno, o ya trabajado y sin pegar en Jira |

Dentro del nivel manda el tiempo callado. Mas dias, mas arriba.

Dos alertas van siempre visibles, incluso en nivel 4: `el cliente no oye nada de Appriss hace N
dias` y `te menciono directo`, que significa que alguien de Appriss te pregunto algo por nombre en
el ultimo comentario.

## 4. Cerrar el ciclo

    bin/anotar RCS-28482 "que hizo, una o dos frases"

Baja a `TRABAJADO, SIN PEGAR EN JIRA`. No desaparece, deja de quemar. Si Juan ya lo pego en Jira,
repite el paso 1 completo.

## Prohibido

Escribir en Jira. Nada de `addComment`, `transition`, `edit` ni `create`. Redacta, Juan pega.

Usar `updated` de Jira como señal de actividad. El reloj cuenta desde el ultimo comentario real.

Inventar estados. Si el dato no esta en `cola/estado.json`, vuelve a Jira y verificalo.

Mezclar la investigacion de un ticket con la vista de cola. Para eso esta `cerebro-ticket`.

Escribir un informe de la cola. La cola se dice, no se documenta.

