---
name: "cerebro-asignacion"
description: "Propone el reparto diario de la cola unassigned de RCS entre el equipo Colombia de Juan Martinez, con estadistica de limpieza de backlog antes y despues, y cosecha las transcripciones de los otros chats del proyecto hacia inbox. Usala cuando Juan pida a quien asignar, el reparto del dia, que le doy a mi equipo, la limpieza del backlog, o el estado de la cola sin asignar. Juan ejecuta la asignacion en Jira, la skill nunca asigna. Para su propia cola usa cerebro-cola, para un ticket suyo usa cerebro-ticket."
---

# Reparto diario de la cola unassigned de RCS

La carpeta Cerebro es la raiz, vive en `~/Downloads/Cerebro-AAAA-MM-DD`. Si no esta montada,
pidesela a Juan antes de seguir. Rutas relativas a ella. Estilo y prohibiciones: su `CLAUDE.md`.

Juan reparte trabajo al equipo Colombia. Esta skill propone. Juan asigna.

## Reglas que mandan

Jira es solo lectura. Nunca `editJiraIssue`, `transitionJiraIssue` ni `addComment`. La skill entrega
una tabla y Juan la ejecuta a mano.

El roster sale de `brain/memoria/project_appriss_support_team.md`. Nunca se deduce de quien aparece
asignado en Jira. Ese error ya saco cuatro personas ajenas al equipo.

El orden de decision es roster, cargas, perfil. Invertirlo ya le dio el bloque mas grande a la
segunda persona mas cargada.

Nada se le asigna a Juan.

El techo no se llena de golpe. El cupo del dia es el menor de dos frenos, el margen al techo y el
incremento diario, y los calcula el script.

Un ticket en `Under Customer Review` cuenta contra el techo y no consume tiempo. Cuando alguien
queda en techo con trabajo esperando, el desbloqueo es cerrar lo que tiene en espera, no subirle el
techo. Dilo asi cuando pase.

ADUSA es critical. Si hay un ADUSA sin asignar y el cupo no alcanza, nombra el ticket, di quien es
el dueño natural y pide a Juan que decida el intercambio.

## 1. Jira en vivo

Tres consultas. Todas derraman a disco. No leas las respuestas, te queman el contexto.

Cola sin asignar. El filtro guardado 29803 no indexa lo que entra el mismo dia, usa la consulta
directa:

    searchJiraIssuesUsingJql
    cloudId: trebuco.atlassian.net
    jql: project = RCS AND assignee IS EMPTY AND statusCategory != Done ORDER BY created ASC
    maxResults: 100
    searchResultMode: all
    fields: ["summary","status","priority","created","updated","labels","reporter","issuetype"]

Carga abierta del equipo:

    jql: project = RCS AND statusCategory != Done AND assignee IN ("712020:7cb67354-171b-4f4b-b5f6-46a5c57cbd4d","712020:239d8bd1-42fb-47ac-8e49-8698e657fbba","712020:20065f69-a041-443a-8b58-b79b1649d0b4","712020:9e64bce4-462c-48d2-887a-2d2e3dee5936","712020:ae769ae6-4093-403d-847f-a3a13075b642") ORDER BY assignee ASC
    fields: ["assignee","status","priority","summary","updated"]

Los tickets de alguien que sale del equipo nunca aparecen en la cola sin asignar. Hay que sacarlos a
mano. El diccionario `SALIENTES` de `bin/asignar.py` lleva los accountId.

    jql: project = RCS AND statusCategory != Done AND assignee = "<accountId>" ORDER BY priority DESC, created ASC

Copia los derrames a `asignaciones/unassigned.json` y `asignaciones/carga.json`.

## 2. Medir y clasificar

    python3 bin/asignar.py asignaciones/unassigned.json asignaciones/carga.json

Escribe `asignaciones/estado-reparto.json`. El script mide y clasifica, no decide. Leelo con `jq`,
nunca los dumps completos:

    jq -r '.antes, .cupo_total' asignaciones/estado-reparto.json
    jq -r '.equipo | to_entries[] | [.key, .value.nivel, .value.cruda, .value.techo_abiertos, .value.margen_techo, .value.cupo] | @tsv' asignaciones/estado-reparto.json
    jq -r '.tickets[] | [.key, .dificultad, (.buckets|join("/")), .adusa, .edad_dias, (.summary|.[0:60])] | @tsv' asignaciones/estado-reparto.json

## 3. El equipo

Techos fijados por Juan el 25 ago 2026.

| Persona | Nivel | Techo | Incremento | A que le pega |
|---|---|---|---|---|
| Luis Hernandez | nuevo | 5 | 2 | Senior Full Stack, React y .NET. Sin contexto de producto. Solo basicos con precedente |
| Sebastian Garces | nuevo | 5 | 2 | Sin historial RCS. Solo basicos con precedente |
| Diego Buelvas | normal | 16 | 3 | Attachments y print docs. Exports e Izenda. Rendering y UI. Recibos. Lleva Delhaize |
| Edwin Garzon | normal | 16 | 3 | Location hierarchy y LHUA. Cargas de datos y feeds. Campos faltantes en transacciones |
| Sebastian Rueda | normal | 16 | 3 | Data integrity. Duplicacion de filas. Mapeo de campos. Feeds y loads. Smart Alerts |

Hay dos Sebastianes y confundirlos ya causo errores. Garces es el nuevo. Rueda es el Senior Data
Engineer. "Sebastian" a secas en mensajes de otros significa Rueda.

Los buckets tecnicos son la propuesta de J.R. Teagle, en
`brain/memoria/project_reparto_cola_2026_08_11.md`. Cruza el bucket del script con la tabla y con lo
que la persona tiene abierto hoy en `.equipo[nombre].abiertos`. Un ticket que repite un patron que
ya lleva abierto vale doble, y lo dices con el numero del ticket que repite, nunca con "coincide con
su perfil".

Un cliente, un dueño. Dos tickets del mismo cliente y del mismo subsistema van a la misma persona o
el trabajo se duplica. Si por cupo hay que partir un cliente, avisalo y di quien lo completa mañana.

## 4. La regla de los nuevos

El script marca `dificultad: basico` por lexico. Eso es un candidato, no una decision.

Antes de proponerle un ticket a un nuevo, busca el precedente:

    bin/buscar "sintoma concreto del ticket"

Con precedente, el ticket va y en el entregable va la cita textual y la ruta, para que arranque
leyendo. Sin precedente, el ticket no va para un nuevo aunque el lexico lo marque basico. Un nuevo
sin precedente pregunta, y preguntar consume tiempo de Juan, de Diego, de Edwin y de Rueda.

El lexico falla en un caso conocido. "Access level" y "user profile" suenan basicos y muchas veces
son identidad de la Unificacion de julio 2026, las tres tablas `membership.Users`, `LPUser` y
`LPUser2`. Verifica en `investigaciones/INDICE.md` antes de darselo a un nuevo.

Nunca le des a un nuevo un Critical, un High, un RCA, una migracion, un ticket ADUSA, un ticket con
label `Escalated`, ni un sintoma que toque varias tiendas o varios articulos.

## 5. El entregable

Escribe `asignaciones/AAAA-MM-DD.md` antes de mostrar nada. Seis bloques, sin narrar el recorrido:

1. Antes. Total sin asignar, cuantos ADUSA, mezcla de prioridad, edad media, edad maxima, cuantos
   pasan de 7 dias. Suma los abiertos de quien este saliendo.
2. Cupo del equipo. Abiertos, techo, margen y cupo del dia por persona.
3. Reparto propuesto. Una fila por ticket: key, cliente, persona, el por que con cita o numero de
   ticket, y el precedente cuando exista.
4. Estadistica de limpieza. Antes, despues, delta. Incluye High sin dueño antes y despues.
5. Mañana. Margen que queda por persona y que sigue pendiente, con el bloqueo nombrado.
6. Lo que no cuadra. Margen total contra huerfanos totales. Ese numero es el argumento de capacidad
   que Juan lleva a J.R. Teagle y a Camila Cortes. Va como cifra, no como adjetivo.

Cierra el historial:

    echo "AAAA-MM-DD,<antes>,<despues>,<delta>,<propuestos>,<adusa_antes>,<adusa_asignados>,<edad_antes>,<edad_despues>" >> asignaciones/estadistica.csv

Con tres lineas o mas, muestra la tendencia del delta junto con la foto del dia.

## 6. Cosechar los chats del proyecto

Las transcripciones no se leen por archivo, se leen por herramienta:

    mcp__session_info__list_sessions
    mcp__session_info__read_transcript   session_id, format: auto, limit: 20

Que falta:

    echo '<json de list_sessions>' | python3 bin/cosechar.py pendientes
    python3 bin/cosechar.py estado

Por cada sesion sin cosechar extrae solo hallazgos verificados: causas raiz, procedimientos,
decisiones de cliente, numeros medidos. Descarta el ida y vuelta, los borradores caidos y las
hipotesis que no cerraron. Techo de 1500 caracteres por cosecha.

    python3 bin/cosechar.py marcar <session_id> "<titulo>" inbox/AAAA-MM-DD-cosecha-tema.md

Juan aprueba antes de que entre a la base. Cuando lo apruebe:

    cat inbox/archivo.md | bin/guardar <id> "Titulo del hallazgo"
    python3 bin/indexar_tickets.py

Carpetas: 16 RCS Soluciones, 19 RCS Procesos, 26 ADUSA, 17 Reuniones, 27 Cerebro.

Si `bin/guardar` responde `disk I/O error`, estas en el sandbox de Cowork y la base no acepta
escritura. Deja la nota en `inbox/` y dile a Juan que corra `python3 bin/ingerir_inbox.py --aplicar`
en su terminal.

Si una sesion sigue corriendo, saltala. No la coseches a medias.

## 7. Mostrar. Techo veinte lineas

Cifras del antes y cupo total. Reparto ticket por ticket, una linea cada uno. Cierra con el despues
y lo que queda fuera. El archivo con `present_files`. No repitas el archivo en el chat.

## 8. Cerrar el ciclo al dia siguiente

Juan aplica el reparto a mano y no siempre queda igual. El paso 1 del dia siguiente trae la
realidad. Compara lo propuesto ayer contra quien quedo asignado hoy y anota las desviaciones. El 11
ago 2026 se aplicaron 23 de 25 propuestas. Medir la desviacion es lo que corrige el clasificador.

## Prohibido

Proponer repartir todo el backlog. Mueve el atasco de la cola general a las colas individuales, y ya
paso el 3 ago 2026.

Usar `updated` de Jira como señal de actividad. Leer los dumps completos. Inventar un precedente que
no verificaste con `bin/buscar`. Meter a alguien que no este en el roster. Asignarle algo a Juan.

Si aparece un nombre nuevo, o alguien sale, actualiza
`brain/memoria/project_appriss_support_team.md` y los diccionarios `EQUIPO` y `SALIENTES` de
`bin/asignar.py` con el accountId verificado por `lookupJiraAccountId`. El roster envejece y es la
primera fuente de error.

