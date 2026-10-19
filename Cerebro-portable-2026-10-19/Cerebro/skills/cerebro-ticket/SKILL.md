---
name: "cerebro-ticket"
description: "Abre una sesion aislada para trabajar un solo ticket RCS de Juan Martinez. Usala cuando Juan nombre un ticket concreto y quiera investigarlo, redactar un comentario, entender su historia, o cuando suba adjuntos de un ticket. Carga solo el contexto de ese ticket, nunca mezcla la investigacion de varios. Entrega un archivo corto con causa y accion, y devuelve el hallazgo a la base. Para ver la cola completa usa cerebro-cola."
---

# Un ticket, un hilo

Un ticket, un contexto, un entregable. La sesion de un ticket no arrastra la investigacion de otro.

## 0. Carpeta obligatoria

Busca `MAPA.md` y `brain/sessions.db`. Si falta, detente y pidela con
`mcp__cowork__request_cowork_directory`. Se llama `Cerebro-AAAA-MM-DD`.

Sin `tickets/RCS-XXXXX.md` no sabes que ya se escribio. Sin `investigaciones/INDICE.md` vas a
reinvestigar una causa raiz ya cerrada. Sigue sin la carpeta solo si Juan lo ordena, y ahi marca
cada conclusion afectada.

Rutas relativas a esa carpeta. Estilo y prohibiciones de escritura: su `CLAUDE.md`.

## 1. Cargar solo este ticket

    tickets/RCS-XXXXX.md      lo que ya se escribio
    bitacora/RCS-XXXXX.md     lo que Juan trabajo y aun no esta en Jira
    adjuntos/RCS-XXXXX/       lo que Juan subio

Sin ficha, corre `python3 bin/indexar_tickets.py` y vuelve a mirar.

El estado real sale de `getJiraIssue`, cloudId `trebuco.atlassian.net`, con
`fields: ["summary","description","status","priority","assignee","reporter","created","updated","labels","comment","attachment"]`.
Nunca de la ficha.

## 2. Buscar sin quemar contexto

No leas archivos completos. Lanza un subagente con la pregunta concreta:

    Agent, subagent_type: Explore
    "Busca en Cerebro que se sabe de <sintoma>. Devuelve solo el hallazgo con la cita textual
     y la ruta. No pegues archivos completos."

Antes de investigar de cero: `investigaciones/INDICE.md`, `flujos/INDICE.md`,
`bin/buscar "sintoma"`.

La Unificacion de julio 2026 explica gran parte de los sintomas de identidad, permisos y SSO. Tres
tablas: `membership.Users`, `LPUser`, `LPUser2`. Empieza ahi antes de proponer hipotesis nueva.

## 3. Adjuntos

No descargues por adelantado. Lista nombre, autor y fecha desde Jira, di cuales parecen relevantes,
Juan elige.

Lo que suba va a `adjuntos/RCS-XXXXX/` con el nombre original. De cada captura escribe en la
bitacora que muestra. El texto queda buscable, la imagen no. Nunca los dejes en `uploads` ni en la
carpeta temporal.

## 4. Un entregable. Techo 2500 caracteres

Un archivo por ticket: `inbox/AAAA-MM-DD-rcs-XXXXX.md`. Seis bloques, en este orden:

| Bloque | Contenido |
|---|---|
| Que pasa | Dos frases. A quien afecta y en que estado esta |
| Causa | Marcada `CONFIRMADA` o `HIPOTESIS`. Nunca ambiguo |
| Evidencia | Tres lineas maximo. Cada una con su cita, ID, timestamp o ruta |
| Que hago hoy | Pasos numerados. Comando completo listo para pegar, que se espera ver, si falla a quien |
| Precedentes | Una linea por ticket o investigacion, con la ruta |
| Compromisos | Que promete este ticket, a quien, y anclado a que condicion |

No narres el recorrido. No recrees la historia del ticket. La historia se consulta con `bin/buscar`
y con la ficha, no se copia al archivo. La cronologia entra solo si cambia una decision.

Si el hallazgo pasa el techo, no alargues el archivo. La causa raiz se va a
`investigaciones/RCS-XXXXX-tema.md` con su propia entrada en el indice, y el entregable la cita.

Los bloques pegables van en archivos aparte, uno por bloque, con solo el texto pegable adentro.
Los redacta `cerebro-comentario` para ingenieria o `cerebro-respuesta-cliente` para el cliente.

## 5. Orden de trabajo

Cierra la evidencia antes de redactar. No escribas el comentario con la investigacion abierta.

Antes de comentarle al cliente un fix de ingenieria, verifica el estado. En `Accepted into
Development` o `Waiting for Software Release` con assignee de Engineering, espera la transicion a
`Under Support Review`. Comentar antes repite el error de RCS-28161.

## 6. Devolver a la base. No es opcional

    bin/anotar RCS-XXXXX "que hizo, una frase"
    cat inbox/AAAA-MM-DD-rcs-XXXXX.md | bin/guardar 16 "Titulo del hallazgo"
    python3 bin/indexar_tickets.py

Carpetas: 16 RCS Soluciones, 19 RCS Procesos, 26 ADUSA, 17 Reuniones, 27 Cerebro.

Entre el 25 ago y el 8 sep 2026 se escribieron 289 notas en `inbox/` y entro un solo chunk a la
base. Un caso que no vuelve a la base no existe la semana que viene.

En el sandbox de Cowork la base no acepta escritura. Si `bin/guardar` responde `disk I/O error`,
deja la nota en `inbox/` y dile a Juan que corra en su terminal:

    python3 bin/ingerir_inbox.py --aplicar

## En el chat. Techo diez lineas

Causa, que hago hoy, que necesito de Juan. El archivo con `mcp__cowork__present_files`. Nunca
pegues el entregable completo en la respuesta.

## Prohibido

Jira, Azure DevOps y terceros: leer, nunca accionar. SQL contra produccion: solo `SELECT`.

Concluir mas alla de la evidencia. Sin cita es hipotesis, y se marca como hipotesis.

Mezclar dos tickets en el mismo hilo.

