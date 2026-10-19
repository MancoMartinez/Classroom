# Mapa del cerebro

Punto de entrada único. Empieza aquí y salta a lo que necesites. Rutas revisadas el 28 sep 2026. Las cifras históricas de capas de abajo no son inventario vigente; consultar ESTADO.md.

## Elige la ruta según lo que vas a hacer

| Lo que necesitas | Abre esto |
|---|---|
| Por dónde empiezo hoy, qué debo responder | `inbox/2026-09-28-cola-prioridades-auditoria.md`; verificar cambios posteriores en Jira |
| Ver todos mis tickets de un vistazo | `tickets/INDICE.md` |
| Trabajar un ticket específico | `python3 bin/buscar RCS-28535`, seguido de las fuentes recientes |
| Registrar que ya trabajé algo | `bin/anotar RCS-28535 "lo que hice"` |
| Ejecutar un proceso: cerrar, escalar, comentar, armar un RCA | `flujos/INDICE.md` |
| Retomar una investigación técnica o buscar una causa raíz conocida | `investigaciones/INDICE.md` |
| Ver si otro analista ya resolvió este síntoma en otro cliente | `confluence/RTS-triage/INDICE.md` |
| Buscar por palabras y significado | `bin/buscar "lo que sea"` |
| Ver el estado de la cuenta ADUSA día por día | `brain/markdown/26-adusa-estado-tickets-reuniones.md` |
| Lo que aún no está clasificado | `inbox/` |

## Las cuatro capas

**Capa 1, memorias.** `brain/memoria/` con índice en `MEMORY.md`. Hechos verificados y reglas de
trabajo, un archivo por hecho. Es lo primero que se lee y lo último que se contradice.

**Capa 2, conocimiento.** `brain/sessions.db` con FTS5, y el mismo contenido en texto plano en
`brain/markdown/`, un archivo por carpeta. 1647 fragmentos en 27 carpetas: KT de Aimee y Kristin,
onboarding, procesos RCS, soluciones, reuniones, docs de ingeniería, ADUSA.

**Capa 3, vistas de trabajo.** Generadas o curadas sobre las dos capas de abajo. No contienen
verdad nueva, solo la ordenan para el modo en que estás trabajando.

- `tickets/` — 298 fichas, una por ticket, más `INDICE.md`. Generadas por `bin/indexar_tickets.py`.
- `flujos/INDICE.md` — cómo se hace cada cosa. Curado a mano.
- `investigaciones/INDICE.md` — causas raíz y mapas de sistema. Curado a mano.
- `confluence/RTS-triage/` — 46 fichas de triage por ticket del espacio RTS de Confluence, una por
  ticket, con causa raíz, evidencia y fix. Son precedentes de otros analistas, no procesos propios.
  El índice se rehace con `python3 bin/traer_confluence.py indice` y se refresca desde Confluence
  con `python3 bin/traer_confluence.py bajar`.

**Capa 4, la cola viva.** `cola/estado.json` y `cola/COLA.md` ordenan los tickets abiertos por
urgencia real, traídos de Jira en vivo. Cuatro niveles: te toca responder, promesa sin cumplir,
esperando al cliente, en movimiento interno. Dentro de cada nivel manda el tiempo callado.

`bitacora/RCS-XXXXX.md` guarda lo que reportas haber trabajado antes de que llegue a Jira, y baja
ese ticket de la cola sin borrarlo. `adjuntos/RCS-XXXXX/` guarda tus archivos por ticket.

**Capa 5, inbox.** `inbox/AAAA-MM-DD-tema.md`. Todo entregable cae aquí en el momento. Después se
ingiere a la base con `bin/guardar` y queda en las capas de abajo.

## Cómo se busca

FTS5 sobre los 1648 fragmentos, cobertura completa, más el razonamiento de Claude al leer.

```bash
bin/buscar "izenda export"      # conocimiento + mesa + memorias + tickets + bitacora + inbox + triage de Confluence
bin/buscar RCS-28535            # atajo: imprime la ficha del ticket
```

El índice estaba corrupto y se reconstruyó el 24 ago 2026. Antes fallaban 25 de 28 consultas de dos
palabras y el script se tragaba el error. Si vuelve a fallar, `bin/buscar` ahora lo dice en pantalla.

Si los vectores hacen falta o no, está medido y sin resolver. `cola/INFORME-recuperacion.md` tiene
el número y la razón por la que 31 preguntas no alcanzan para decidir.

## Las tres skills

| Skill | Para qué |
|---|---|
| `cerebro-cola` | El panorama del día, ordenado por urgencia real |
| `cerebro-ticket` | Un solo ticket, con el contexto aislado del resto |
| `appriss-jira-support` | Redactar comentarios y transiciones, releerla siempre |

Un chat de Cowork por ticket. Empieza el chat invocando `cerebro-ticket` con el ID y la
investigación de ese ticket no se mezcla con la de ningún otro.

## Verificar que nada se rompió

```bash
python3 bin/eval_cola.py            # el clasificador de urgencia contra etiquetas fijas
python3 bin/eval_recuperacion.py    # la recuperación contra el set de preguntas
```

## Qué es fuente de verdad y qué no

Jira es la fuente de verdad del estado de un ticket. Siempre. Las fichas de `tickets/` dicen qué se
escribió y cuándo, no en qué estado está el ticket ahora. Sirven para no investigar de cero, no para
reportar estado.

La base y las memorias son fuente de verdad de lo que se aprendió: causas raíz, procesos, quién sabe
qué. Eso no caduca por sí solo.

## Regenerar las vistas

```bash
python3 bin/indexar_tickets.py     # rehace tickets/ desde todo el cerebro
bin/exportar.sh                    # base a markdown, reindexa, arma el zip portable
```

`flujos/INDICE.md` e `investigaciones/INDICE.md` se editan a mano. Ningún script los pisa.
