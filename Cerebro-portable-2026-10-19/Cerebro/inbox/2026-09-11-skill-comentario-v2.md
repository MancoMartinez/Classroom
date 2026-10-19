---
name: cerebro-comentario
description: "Redacta comentarios de Jira para Juan Martinez, internos de escalacion a ingenieria y respuestas a cliente, con el formato y el tono fijados por el. Usala cuando Juan pida redactar un comentario, una nota interna, una escalacion a Eng, una respuesta al cliente, o cuando termine la investigacion de un ticket y toque escribir. Tambien cuando pida revisar un borrador de comentario. Nunca escribe en Jira, solo entrega el texto para que Juan lo pegue."
---

# Comentarios de Jira

Dos formatos. Ingenieria y cliente. Mismas reglas de escritura, formato visual distinto.

Jira nunca se escribe desde aca. Redacta, Juan pega. Nada de `addComment`, `transition`, `edit`
ni `create`.

## 0. Carpeta

Busca `MAPA.md` y `tickets/`. Si el comentario es sobre un ticket concreto y la carpeta falta,
detente y pidela con `mcp__cowork__request_cowork_directory`. Sin `tickets/RCS-XXXXX.md` no sabes
que ya se le dijo al cliente y vas a repetirlo o a contradecirlo.

Sigue sin ella solo si Juan lo ordena, o si te pide revisar un borrador que el pego en el chat.

## 0.1 Verifica la ruta antes de escribir una linea

Una escalacion bien redactada al equipo equivocado rebota y cuesta dias.

Lee `brain/memoria/reference_escalacion_l3_procedimiento.md` y saca destino, estado y assignee.
Nunca los cites de memoria.

El nombre del producto no decide la ruta. Decide donde vive el componente. Engage Analytics va a
Secure Engineering con Shandana Khan, no a Engage Engineering con Ian Williams. RCS-23643 lo dice
literal: "Note: Even though this is related to Engage, the ticket is for the Secure team." El bug
que salio de ahi, ADO 66220, quedo como Secure EBR.

Antes de nombrar a un ingeniero, busca dos cosas: un ticket anterior con el mismo defecto y a quien
se asigno, y el mismo defecto abierto hoy en otro ticket y quien lo tiene. Si los dos apuntan a la
misma persona, esa es la ruta. Si contradicen la tabla, mandan los precedentes, y lo dices con la
cita.

Busca ese precedente con `bin/buscar "sintoma"`, que cubre tickets, bitacora, memorias y el corpus
de triage de Confluence en `confluence/RTS-triage/`. Ese corpus dice a que equipo se mando cada
defecto y con que argumento. Varias fichas concluyen Delivery donde el instinto dice Engineering.

El ENG se auto crea con la transicion. Nunca lo crees a mano.

## 0.2 Si el defecto ya golpeo a varios clientes, escalalo agrupado

Antes de escribir la nota interna, mira si el mismo defecto aparece en otras fichas de
`confluence/RTS-triage/`. Las familias vivas estan al final de `investigaciones/INDICE.md`.

Con tres o mas clientes afectados por la misma causa, el comentario pide un arreglo de raiz y lo
sustenta con la lista, en vez de pedir un parche para este tenant. Es el argumento que ya usaron
RCS-28606, RTS-206610, RTS-206268 y RTS-206667 con el catalogo de campos desincronizado.

Cita ticket y cliente de cada precedente. Una tabla de cuatro filas convence mas que un parrafo.

Esto vale solo para el comentario interno. Al cliente nunca se le nombra otro tenant.

## 0.3 Nada entra al ticket sin que Juan lo haya corrido

Es la regla nueva y es la que mas duele. Origen: JR, EoW del 11 sep 2026. Tres ingenieros distintos
se le quejaron esa semana, cada uno con un ticket de ejemplo. Lo que devuelven, textual: "this is AI
slop, the answer here is wrong".

La IA es un ingeniero junior que triaga. Quiza era muy bueno en su empresa anterior. No entiende
como se conectan nuestras herramientas ni las sutilezas que no estan escritas en ningun lado.

El flujo que JR exige, en orden: usala, mirala, corre tu mismo lo que dijo, verificalo, y solo
entonces escribe el comentario.

Consecuencia operativa para esta skill. Antes de redactar, separa cada afirmacion en tres cajones y
marca el cajon en el texto:

| Cajon | Como entra al comentario |
|---|---|
| Verificado por Juan | Como hecho, con el comando, el ID o el timestamp que lo prueba |
| Hipotesis de IA sin correr | Como hipotesis declarada, con la peticion de revision |
| Sin verificar y sin valor | No entra |

Si Juan no corrio nada todavia, dilo en el chat y no entregues el comentario. Un borrador
construido solo con salida de IA es exactamente el ticket que rebota.

## 0.4 El test de Camila

Antes de escribir un bloque grande, preguntate si a ti te serviria recibirlo. Si tu heredaras este
ticket de otra persona, esa nota te da informacion util para actuar.

Si la respuesta es no, no la escribas. Borra el bloque, no lo reescribas mas corto.

## 0.5 No nombres un defecto antes de que ingenieria lo confirme

En la nota interna puedes proponerlo como hipotesis, siempre marcada.

En el texto al cliente esta prohibido. Un ticket de Lewis anuncio dos defectos. Ingenieria dijo
despues que era configuracion y que quiza no habia ninguno. Eso creo la expectativa de dos
correcciones gratis sobre algo que podia ser un change request facturable.

Si el mismo comentario interno alimenta un texto al cliente, revisa que la hipotesis no se filtre.

## Reglas de escritura, en los dos formatos

Prohibido el guion largo y el guion medio. Ni en titulos, ni en el cuerpo, ni para separar
clausulas. Punto seguido, coma o dos puntos. Es la regla que mas se rompe, revisala al final.

Prohibidos los incisos entre parentesis o entre guiones. El dato subordinado que valga va en
oracion propia. El resto se descarta.

Prohibidas las adversativas de compensacion. Nada de "sin embargo", "no obstante", "aunque",
"si bien", "however", "although", "that said". La contradiccion va como correccion directa, en
oracion nueva.

Imperativo y voz activa en la nota interna. "Pull that case in the logs", no "that case should be
pulled". Nada de "cabe destacar" ni "es importante señalar". Esta regla no cruza al texto de
cliente, donde una peticion en imperativo pelado esta prohibida.

Asimetria sintactica. Una oracion de cuatro palabras despues de una de cuarenta. "She was right."
vale mas que un parrafo de matices.

Sin adjetivos vacios. Nada de "robusto", "significativo", "critico" sin numero detras.

Ingles para todo bloque que se pegue en Jira, Confluence o Teams. Español solo para hablar con Juan.

No concluyas mas alla de la evidencia. Sin verificar, se dice. Si es hipotesis, se marca. Un
precedente de otro cliente sostiene una hipotesis, no una confirmacion.

## Privacidad

Nunca pegues contenido de casos de RRHH en Jira. Campos como `HRDetail.HR1` traen nombres de
empleados y acusaciones. Identifica por `CaseNo` y por ID interno, nada mas.

En SQL que toque narrativa, cambia la columna por una prueba de presencia:

```sql
CASE WHEN HD.HR1 IS NULL THEN 'vacio' ELSE 'con dato' END
```

## Formato 1. Escalacion interna a ingenieria

Markdown completo, Jira Cloud lo convierte al pegar. Encabezados, negritas, tablas y bloques de
codigo. Objetivo: un ingeniero lo lee en dos minutos y sabe que hacer.

Negrita solo en lo que cambia una decision. Tabla siempre que haya tres o mas datos comparables.
Bloque de codigo para filtros, SQL, nombres de tabla y mensajes de error literales.

### El techo. Un ingeniero lo lee en dos minutos o no lo lee

Un comentario interno largo no demuestra trabajo. Demuestra que nadie filtro.

| Bloque | Techo |
|---|---|
| Findings | Seis lineas. Cada una con su prueba |
| Salida de consulta o de log | Diez lineas, y solo si esa salida decide algo |
| Casos concretos | Uno, completo, que Eng pueda abrir. No una lista de veinte |
| Ruled out | Cuatro filas |
| Still open | Cuatro peticiones numeradas |

Pasos de reproduccion y tablas de precedentes no cuentan contra el techo. Son lo que Eng si usa.

Lo que sobra no se resume. Se borra, o se va a `investigaciones/RCS-XXXXX-tema.md` y el comentario
la cita por ruta.

### Los cuatro requisitos que hacen rebotar el ticket

Del doc de Aimee Wadsworth, Confluence RTS `478006902856`. No son opcionales.

| Requisito | En concreto |
|---|---|
| Entorno | Test, QA o Prod. Escrito, no implicito |
| Pasos de reproduccion con capturas | Numerados, uno por tenant, con expected y actual |
| Notas de troubleshooting, incluida la IA | Que probaste, en que orden, contra que fuente. Declara el uso de IA |
| Conversaciones fuera del ticket | Teams, correo, llamadas. Si no hubo, escribe que no hubo |

El 13 ago 2026 Aimee devolvio cuatro tickets de Vedant Shirude por no traerlos. RCS-28007 tenia la
investigacion completa de Tyrone Whitney y aun asi no paso, porque el assignee solo habia escrito
"CC: Matthew Kamminga". Un ticket se atasca semanas no por falta de investigacion sino porque la
investigacion nunca se escribio en el ticket.

El quinto requisito, avisarle al cliente que el ticket se mueve, lo cubre el Formato 2.

### Como se declara el uso de IA

JR dicto la forma. Usala casi textual:

```
Claude flagged this as the likely root cause. I checked A, B and C myself, and here is what I
found. This is what I think is happening. Could someone else evaluate this and give me your
thoughts?
```

Tres partes obligatorias. Lo que la IA propuso. Lo que Juan verifico, enumerado, con el comando o
el ID. La peticion de revision.

Esta forma no esconde el uso de IA y por eso no rebota. Lo que rebota es pegar la salida como si
fuera investigacion propia.

Si una hipotesis de IA no se verifico, entra asi: "unverified, from AI triage, listed so it is not
re-explored". Nunca como hallazgo.

### Pasos de reproduccion

Nunca los resumas en prosa. Nunca los des por obvios porque el sintoma se ve en la captura. Uno por
tenant, con encabezado propio:

```
### Nombre del tenant (ABBR), fecha del reporte

1. Accion de entrada. Portal, ambiente, usuario.
2. Navegacion exacta. Nombre literal de la pestaña o el menu.
3. Parametros aplicados. Rango de fechas, filtros, seleccion.
4. Donde mirar.

Expected: que deberia verse.
Actual: que se ve. Nombre del adjunto y fecha de captura.
```

Si un dato no lo tienes, escribe que no lo tienes. No lo rellenes con el valor de otro tenant. Asi
se marca: "Leave the default date range applied".

Tres reproducciones independientes valen mas que una repetida. Si el defecto aparece en tickets de
otros clientes, incluye esos pasos y di de que ticket salen. Las fichas de `confluence/RTS-triage/`
traen esos pasos ya escritos, con su cliente y su fecha.

### Estructura

Las secciones 2 y 4 no se quitan nunca, cargan los requisitos de Aimee.

```
# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Correction
Si soporte dijo algo incorrecto, o el ticket arrastra una premisa falsa, va aqui y va
primero. Sin suavizar. Sin justificar el error.

## 2. Environment and steps to reproduce
Entorno explicito. Pasos numerados por tenant. Expected contra Actual.

## 3. Findings
Lo que establece la evidencia, seis lineas. Cada linea marcada verified o unverified.
Precedentes con su numero de bug. Configuracion leida en produccion, con fecha de lectura.

## 4. Troubleshooting performed, and the limits of support access
Que probaste, en orden. La declaracion de uso de IA en la forma de arriba. Conversaciones
fuera del ticket, o constancia de que no hubo. Que necesita Eng que soporte no puede ver.

## 5. Ruled out. Do not repeat
Una linea por hipotesis caida, con la refutacion. Maximo cuatro filas.

## 6. Still open
Que necesitas de Eng, numerado. Tickets relacionados. Prioridad y edad.
```

Abre con la correccion si la hay. Un ingeniero que lee tres parrafos antes de enterarse de que la
premisa era falsa pierde el tiempo dos veces.

En Findings, separa lo que probaste en este tenant de lo que viene de un precedente. El precedente
va con su ticket, su cliente y la ruta de la ficha. Un ingeniero que no puede distinguir las dos
cosas trata todo el comentario como opinion.

Declara tus salvedades metodologicas antes de que las encuentre Eng. Cuesta menos.

Distingue proceso ejecutado de efecto entregado. `RunStatus = Success` significa que el proceso
corrio. No significa que llego el correo.

Da al menos un caso concreto que Eng pueda abrir. Un `CaseNo` con fecha vale mas que tres parrafos.

Cierra pidiendo cosas numeradas. "Confirm whether X covers Y" sirve. "Please advise" no.

La peticion de revision del bloque de IA cuenta como una de esas peticiones. No la repitas al final.

## Formato 2. Respuesta al cliente

Sin markdown, sin tablas, sin encabezados, sin negritas. Parrafos cortos, ocho como techo. El
detalle completo esta en `cerebro-respuesta-cliente`, y ahi vive el banco de frases. Lo esencial:

Dos capas. La social se acolcha, la tecnica se recorta. Mas palabras alrededor, menos adentro.

Ninguna frase que niegue una necesidad en seco. "I don't need anything else from you" se lee como
go away. Va "I appreciate everything you have sent over so far. I do not think I need anything else
at the moment, and I will come back to you if that changes."

Ninguna peticion en imperativo pelado. Could you, whenever you have a moment.

Toda conclusion no confirmada por ingenieria va con atenuante. It looks like, that may point to.

Solo hechos observados en el sistema. Nunca determinaciones de perdida ni culpa a una tienda o a un
empleado. Sin especulacion.

Sin fecha de arreglo mientras ingenieria no la confirme. Promete el proximo contacto, no el arreglo.

Sin la palabra defect mientras ingenieria no lo confirme por escrito.

Sin jerga interna, sin nombres de tabla, sin claves ENG, sin nombres de ingenieros o de equipos.

Sin hallazgos de investigacion. Que componente carga y cual no es hallazgo. Fuera.

Sin salida de IA, en ningun tamaño.

Sin precedentes de otros clientes. Nunca nombres otro tenant, ni digas que el mismo defecto le pasa
a alguien mas. Eso vive en la nota interna.

Si soporte se equivoco, corrigelo en el primer parrafo, absorbiendo con I. Una vez, sin disculpas
encadenadas.

El reporter interno no relaja ninguna regla. Lo que le des viaja al cliente sin control de Juan.

## Antes de entregar, los diez

1. Guiones largos o medios. Elimina todos.
2. "Sin embargo", "aunque", "however", "although". Reescribe en oracion nueva.
3. Parentesis explicativos. Sacalos a oracion propia o borralos.
4. Parrafos de longitud pareja. Rompe uno.
5. Adjetivos sin numero detras. Pon el numero o quita el adjetivo.
6. Cada afirmacion contra su cajon. Verificado, hipotesis marcada, o fuera.
7. El test de Camila sobre cada bloque de mas de seis lineas. Si no te serviria recibirlo, borralo.
8. Los techos de la tabla. Findings seis lineas, salida diez, un caso concreto.
9. Los cuatro requisitos de Aimee en el comentario interno. Si falta uno, el ticket rebota.
10. Destino y assignee, contrastados contra un precedente del mismo defecto, no solo contra la
    tabla.

Y tres mas, si el texto va al cliente: ningun otro tenant nombrado, ninguna ficha citada, ninguna
frase que suene a go away leida en voz de lector americano.

## Entrega

Un archivo por bloque pegable, con solo el texto pegable adentro. Sin titulo en español arriba, sin
notas de contexto. Juan abre, selecciona todo y pega.

    inbox/AAAA-MM-DD-rcs-XXXXX-comentario-interno.md
    inbox/AAAA-MM-DD-rcs-XXXXX-respuesta-<reporter>.md
    inbox/AAAA-MM-DD-rcs-XXXXX-teams-<destinatario>.md

El marco en español, el analisis y el orden de ejecucion van en el entregable del ticket, no aqui.

Si la ruta cambia despues de escribir el Teams, renombra el archivo al destinatario correcto y avisa
que el anterior quedo obsoleto. Un archivo con el nombre equivocado se pega equivocado.
