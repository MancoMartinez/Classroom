# Cerebro — contrato para cualquier sesión de Claude

Lee primero AGENTS.md. Sus ocho reglas permanentes aplican a todo el proyecto y sustituyen cualquier instrucción histórica contradictoria. El agente nunca escribe en brain/sessions.db ni ejecuta bin/guardar, bin/ingerir_inbox.py o cerrar. Juan ingiere inbox desde su terminal con cerrar.

Accesos de Juan, ya concedidos: SQL de producción por Bastion y SSMS en `sqlmi-prd-wus2-arp-001`, Control Panel USPROD con WISC, Snowflake y SnowTime. Nunca escribas "acceso sin verificar" ni sugieras pedir permisos o delegar. Detalle y límites en la sección Accesos de Juan de AGENTS.md.

Esta carpeta es el segundo cerebro de Juan Martínez, Lead Support Engineer en Appriss Retail
(contratado vía Nuaav, Colombia, UTC-5). Todo lo que importa vive aquí o se exporta aquí.

El estado real del proyecto, con cifras medidas y lo que sigue roto, está en
`ESTADO.md`, en la raíz de esta carpeta. Léelo antes de opinar sobre el sistema.

El servidor MCP local `cerebro` comparte la búsqueda con Codex y consola. Usar sus herramientas de lectura cuando estén disponibles; de lo contrario, los comandos siguientes. Consultar el protocolo añadido en AGENTS.md.

## Antes de responder cualquier cosa de trabajo

Busca primero. Nunca arranques de cero, casi siempre ya hay algo escrito:

```bash
bin/buscar "lo que sea"      # motor híbrido compartido con MCP
bin/buscar RCS-28535         # ficha, bitácora, notas nuevas y referencias
```

Si no tienes el comando, el equivalente crudo:

```bash
grep -ril "término" brain/markdown/ brain/memoria/ tickets/
```

## Por dónde entrar según lo que pide Juan

`MAPA.md` es el punto de entrada. Estas son las cuatro rutas, elige la que corresponde antes de
tocar nada:

| Juan pide | Entra por |
|---|---|
| Todos mis tickets, la cola, el panorama | `tickets/INDICE.md` |
| Un ticket concreto | `bin/buscar RCS-XXXXX`, luego ficha, bitácora y fuentes recientes del paquete |
| Cómo se hace algo: cerrar, escalar, comentar, armar un RCA, un tracker | `flujos/INDICE.md` |
| Una investigación, una causa raíz, un mapa de sistema | `investigaciones/INDICE.md` |
| Un síntoma que quizá otro analista ya cerró en otro cliente | `confluence/RTS-triage/INDICE.md` |

Las fichas de `tickets/` dicen qué se escribió y cuándo. **Jira es la fuente de verdad del estado.**
Nunca reportes un estado desde una ficha sin verificarlo en Jira primero.

Cuando el síntoma que investigas se parezca a uno del corpus de Confluence, cítalo como precedente
y sigue con tu propia evidencia. Ese corpus es trabajo de otros analistas sobre otros clientes: sirve
para no partir de cero y para reconocer una familia de falla, no para dar por confirmada una causa en
el ticket que tienes enfrente. Cuatro familias ya se repiten, están al final de `investigaciones/INDICE.md`.

`tickets/` se regenera con `python3 bin/indexar_tickets.py`. `flujos/` e `investigaciones/` se
editan a mano, ningún script los pisa.

## Reglas que no se negocian

1. **Jira es de solo lectura.** Nunca `addComment`, `transition`, `edit` ni `create`. Redacta el
   texto, Juan lo pega. No hay excepción para etiquetas.
2. **Azure DevOps y sistemas de terceros: leer, nunca accionar.** Nada de aprobar, comentar,
   mergear ni pulsar botones.
3. **SQL contra producción: solo SELECT.**
4. **Nada que valga se queda solo en el scroll de la consola.** Todo entregable se escribe a
   `inbox/AAAA-MM-DD-tema.md` en el momento, antes de seguir. Juan pierde respuestas buenas
   cuando se va a verificar algo y vuelve; escribir el archivo lo evita.
4b. **Un entregable por ticket, techo 2500 caracteres.** Seis bloques: qué pasa, causa marcada como
   confirmada o hipótesis, evidencia en tres líneas con su cita, qué hago hoy en pasos ejecutables,
   precedentes con ruta, compromisos. No se narra el recorrido y no se recrea la historia del
   ticket. La historia se consulta con `bin/buscar`, no se copia al archivo. Si el hallazgo pasa el
   techo, la causa raíz se va a `investigaciones/` con su propia entrada y el entregable la cita.
   Medición del 8 sep 2026: los informes anteriores promediaban 10.3KB más un instructivo de 6.4KB.
4c. **Juan ingiere inbox desde su terminal con cerrar.** El agente nunca ejecuta
   `bin/guardar` ni `bin/ingerir_inbox.py`, tampoco en modo de ensayo.
5. **Español para hablar con Juan. Inglés para todo lo que se pega en Jira, Confluence o Teams.**
6. **Sin guiones como conectores, sin markdown en bloques pegables, sin negritas ahí.**
7. **Regla de estilo, aplica a todo texto que Claude escriba, no solo bloques pegables.**
   Prohibida la construcción adversativa correctiva. Elimina "sin embargo", "no obstante",
   "aunque", "pero" usado para suavizar una contradicción. Presenta la corrección como
   corrección técnica directa, en oración nueva, con punto seguido.
   Prohibido el inciso explicativo entre paréntesis o entre guiones largos. El dato
   subordinado que valga va en oración propia. El resto se descarta.
   Exige asimetría de ritmo. Una oración larga y densa seguida de una oración corta rompe
   la monotonía. No repitas el mismo largo de oración en cadena.
   Modo imperativo y voz activa siempre. Nada de voz pasiva ni fórmulas impersonales para
   evadir quién hizo qué. Prohibidas las muletillas "cabe destacar", "es importante señalar"
   y equivalentes.
   Prohibido el adjetivo calificativo vacío. Si el dato no es verificable o medible, no va.

## Dónde está cada cosa

| Qué | Dónde |
|---|---|
| Punto de entrada, el mapa completo | `MAPA.md` |
| Base de conocimiento en SQLite con FTS5, 1744 fragmentos en 27 carpetas | `brain/sessions.db` |
| La misma base en texto plano | `brain/markdown/` |
| Memorias de Claude Code | `brain/memoria/` (índice en `MEMORY.md`) |
| Ficha por ticket, 530 fichas | `tickets/` |
| Procesos y cómo se hace cada cosa | `flujos/INDICE.md` |
| Causas raíz y mapas de sistema | `investigaciones/INDICE.md` |
| Fichas de triage de Confluence, 46 precedentes por ticket | `confluence/RTS-triage/INDICE.md` |
| Lo nuevo sin clasificar | `inbox/` |
| Regenerar el bundle portable | `./bin/exportar.sh` |
| Atajos de terminal, Mac y Linux | `cerebro.sh` |
| Atajos de terminal, Windows | `cerebro.ps1` |

La base del bundle es la base de trabajo. `bin/buscar` y `bin/guardar` resuelven rutas relativas a
esta carpeta y funcionan igual en el Mac, en Cowork y en cualquier copia. Para apuntar a otra base,
`CEREBRO_DB=/ruta/sessions.db`.

## Escribir en la base

Moscú tiene que estar cerrada. `bin/guardar` hace el backup solo antes de escribir, y desde el 8 sep
2026 rota y deja las dos copias más recientes. Sin rotación, ocho copias de 31MB se comieron 250MB
de los 294MB de la carpeta.

```bash
bin/guardar --carpetas                              # ver los IDs de carpeta
echo "cuerpo de la nota" | bin/guardar 26 "Título"  # guardar
python3 bin/ingerir_inbox.py --aplicar              # volcar inbox consolidado
python3 bin/indexar_tickets.py                      # rehacer tickets/ después
```

**En el sandbox de Cowork la base no acepta escritura.** La carpeta se monta por FUSE y SQLite no
puede tomar el bloqueo. Medido el 8 sep 2026: lectura normal funciona, escritura da `disk I/O error`
siempre, y un journal caliente al lado también rompe la lectura normal. `bin/buscar` cae a
`immutable=1` y lee igual. `bin/guardar` y `bin/ingerir_inbox.py` solo corren en terminal. Si
`guardar` falla con `disk I/O error`, deja la nota en `inbox/` y dile a Juan que la ingiera desde su
terminal. Ese fue el motivo real por el que la base se congeló dos semanas.

**Cowork trabaja en modo consulta.** Decisión de Juan del 8 sep 2026. Desde Cowork se busca, se
leen fichas, se redactan comentarios y se arman entregables de Office. Todo lo que Cowork produzca
se escribe a `inbox/AAAA-MM-DD-tema.md` y entra a la base después, desde terminal, con
`ingerir-aplicar`. Cowork nunca corre `bin/guardar` ni `bin/ingerir_inbox.py`. Si te ves tentado a
escribir en la base desde ahí, la respuesta es el archivo en `inbox/`.

Los triggers de FTS5 indexan solos en insert, update y delete. No toques `chunks_fts` a mano.

El 24 ago 2026 se encontró el índice corrupto: 25 de 28 consultas OR devolvían
`database disk image is malformed`. La causa eran los triggers de la tabla de contenido externo, que
borraban usando `old.body` mientras el insert indexaba `contextualized_body`. `chunks_fts` e
`items_fts` se reconstruyeron como FTS5 autónomo y los seis triggers se reescribieron. Ya se puede
hacer UPDATE y DELETE sobre `knowledge_chunks` sin romper nada. Detalle en
`cola/INFORME-recuperacion.md`.

## Estado del motor de IA

La key de Azure murió el 18 ago 2026 (401 en chat y embeddings). **La app Moscú ya no razona,
solo almacena y busca.** El motor de inteligencia eres tú, Claude Code. Transcribir en Moscú,
procesar aquí, guardar de vuelta. Ver `brain/memoria/project_moscu_sin_gpt.md`.

Sobre los vectores, la posición está medida, no supuesta. 168 de los 1623 fragmentos de entonces
nunca recibieron embedding. La búsqueda hoy es FTS5 sobre el 100% del contenido más tu razonamiento
al leer.

`bin/eval_recuperacion.py` mide FTS5 sobre `cola/EVAL-recuperacion.json`. **El set se llevó a 101
preguntas el 8 sep 2026 y FTS5 da 33% de recall@5.** El 48% anterior estaba inflado: diez de los 32
casos tenían anclas que apuntaban a más de treinta fragmentos y se acertaban por azar.

Regla del set: un ancla debe apuntar a entre 1 y 30 fragmentos. Fuera de ese rango la pregunta no
mide nada y hay que apretarla.

**La comparación contra el canal semántico ya corrió.** Cinco brazos sobre 101 preguntas: FTS5 33%,
BM25 38%, LSA 38%, RRF 39%, BM25 más LSA 39%. Ninguna pareja se separa, McNemar da p entre 0.26 y
1.00. El contraste que decide es BM25 contra BM25 más semántica: mueve cinco preguntas, p igual a
1.00. **Los vectores no son el cuello de botella.** El techo lo pone algo aguas arriba del ranking.

No propongas embeddings como arreglo del recall sin releer `cola/INFORME-recuperacion.md`. Y ten
presente que el evaluador mide solo el canal de `knowledge_chunks`, mientras `bin/buscar` busca
además en memorias, fichas, mesa e inbox.

No pidas una key de Azure nueva. Si se prueban embeddings, van locales y en el Mac, porque torch no
entra en el sandbox de Cowork.

## La cola de tickets

`cola/COLA.md` y `cola/estado.json` ordenan los tickets abiertos por urgencia real en cuatro
niveles: te toca responder, promesa sin cumplir, esperando al cliente, en movimiento interno. El
clasificador vive en `bin/cola.py` y se mide con `bin/eval_cola.py` contra etiquetas fijadas a mano.
Está en 100% desde el 8 sep 2026.

**Si la exactitud baja, corre `python3 bin/refrescar_eval.py` antes de tocar el léxico.** Las
etiquetas caducan solas: se fijan leyendo el último comentario de cada ticket un día concreto, y
cada comentario nuevo las deja describiendo un momento que ya pasó. El 8 sep 2026 el sistema marcaba
73% y dos de los cuatro fallos eran etiquetas vencidas, no defectos del código. Ese diagnóstico
equivocado estuvo semanas escrito en `ESTADO.md` como deuda técnica. `eval_cola.py` ahora marca solo
los fallos que caen sobre etiquetas vencidas. Si no hay vencidas, el léxico sí se movió y la cola
puede estar mal ordenada.

`bitacora/RCS-XXXXX.md` guarda lo que Juan reporta haber trabajado antes de que llegue a Jira.
`adjuntos/RCS-XXXXX/` guarda sus archivos. Ambos alimentan la ficha del ticket.

Skills: `cerebro-cola` para el panorama, `cerebro-ticket` para trabajar uno solo con el contexto
aislado.
