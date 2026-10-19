# HANDOFF — ADUSA, 18 de agosto 2026, cierre de sesión

**Leer esto primero.** Resume dónde quedó todo antes de reiniciar la sesión de Claude para
recuperar el acceso a Atlassian.

---

## Estado en una línea

El tracker para el cliente **ya está construido y validado**, el correo **ya está redactado**,
y falta **una sola cosa**: verificar 10 puntos contra Jira, que no se pudo hacer porque el
conector de Atlassian está caído (`HTTP 404 at https://mcp.atlassian.com/v1/mcp`).

---

## Entregables listos

| Archivo | Qué es |
|---|---|
| `~/Downloads/Appriss ADUSA-Support-Tracker - 08182026 PM.xlsx` | **El tracker para enviar al cliente.** Construido sobre la plantilla exacta de J.R. |
| `2026-08-18-correo-y-cambios-tracker-pm.md` | El correo para Jim + diff exacto + justificación de cada pregunta |
| `2026-08-18-post-reunion-adusa.html` | Análisis de la reunión ticket por ticket, agrupado por quién debe el siguiente paso |
| `2026-08-18-prompt-atlassian-verificacion.md` | **Prompt listo** para la consola que sí tiene Atlassian |
| `2026-08-18-cheatsheet-adusa-tracker2.html` | Cheat sheet bilingüe de los 35 tickets |
| `adusa-18ago-fuentes/` | Todas las fuentes crudas, transcripts, JSONs, frames del video y el generador |

---

## El tracker: cómo está hecho y cómo modificarlo

No está escrito a mano. Se genera con dos archivos en
`adusa-18ago-fuentes/generador-tracker/`:

- **`content.py`** — solo el contenido que cambia (encabezado, tabla resumen, y un dict
  `CELLS` con fila → columna → texto).
- **`build.py`** — toma el .xlsx de J.R. como plantilla, convierte las celdas a inline
  strings, aplica los cambios, recalcula el color de la columna D según el valor, recalcula
  las alturas de fila, y escribe el archivo nuevo. **Preserva estilos, anchos, merges, la
  hoja 2 y todo lo demás byte a byte.**

Para regenerar tras la verificación de Jira: editar `content.py` y correr `python3 build.py`.

### Validaciones que pasa el archivo actual
- 35 tickets, mismo orden y mismas filas que J.R.
- Tabla resumen suma exacto al total, y el total coincide con el conteo real del detalle:
  **20 Resolved · 1 Pending Ahold verification · 0 Awaiting Ahold input · 14 Active with Appriss**
- Columna Status idéntica a la hoja de Chris en los 35 (cero discrepancias)
- Colores de "Action with" coherentes con el valor en los 35
- Zip íntegro, 2 hojas, hoja 2 "Cases missing owners" intacta con sus 35 filas

---

## Error cometido y corregido, para que no se repita

Inventé 5 valores de la columna **Status** (el estado real de Jira) deduciéndolos del contexto
en vez de copiarlos de la fuente. Los detectó el video al mostrar la pantalla de Chris.

| Ticket | Puse | Real |
|---|---|---|
| RCS-28342 | Work in progress | Under Customer Review |
| RCS-28415 | Work in progress | Under Support Review |
| RCS-28196 | Work in progress | **Waiting for Software Release** |
| RCS-28378 | Under Customer Review | Under Support Review |
| RCS-28413 | Work in progress | Under Support Review |

Ya revertidos. **Regla que sale de esto: la columna Status no se deduce nunca, se copia de
Jira o de la hoja de Chris.**

---

## Lo que cambió respecto a la versión de J.R. del 17

**Resumen por tema**: solo se movieron dos temas.
- User accounts and duplicates: Resolved 1→4, Pending 3→0
- Case entry and assignment: Resolved 2→3, Awaiting 2→0, Active 2→3
- Total: Resolved 16→20, Pending 4→1, Awaiting 2→0, Active 13→14

**Cambios de estado (6)**
| Ticket | De → A | Motivo |
|---|---|---|
| RCS-28177 | Pending → **Resolved** | Christina Cordero confirmó en vivo; Jonathan Wright ya veía sus casos |
| RCS-28364 | Pending → **Resolved** | Búsqueda en la llamada devuelve casos hasta enero |
| RCS-28378 | Awaiting → **Resolved** | Era la página de shoplifting de Hannaford |
| RCS-28379 | Active → **Resolved** | Muestra de la hoja 2 tomada en vivo |
| RCS-28304 | Awaiting → **Active** | James decidió levantar el FR, prioridad baja |
| RCS-28342 | Pending → **Active** | Retrocede, ejemplos nuevos siguen fallando |

**Texto actualizado sin cambio de estado (14)**: 28093, 28365, 28415, 28123, 28196, 28124,
28021, 28161, 28413, 28353, 28356, 28407, 28281, 28292.

**Sin tocar (15)**: 28014, 28042, 28059, 28053, 28135, 28023, 28043, 28115, 28369, 28025,
28075, 28030, 28041, 28109, 28125. Son cerrados de días atrás que nadie mencionó hoy.

---

## Lo pendiente: verificación contra Jira

Correr el prompt de `2026-08-18-prompt-atlassian-verificacion.md`. Las diez preguntas:

1. ¿28177, 28364, 28378, 28379 tienen status y resolución coherentes con darlos por resueltos?
2. 28342: assignee hoy, comentario del 18, ¿enlazado a algún ENG?
3. 28415 y 28413: ¿siguen sin dueño?
4. 28356 y 28353: ¿están enlazados o marcados como duplicados? (en la reunión se dijo que
   28356 es duplicado, pero en la hoja sigue como ticket independiente de alta prioridad)
5. 28196: ¿sigue en "Waiting for Software Release"?
6. 28124: status y último comentario de Leigh Ann
7. 28021 y 28161: ¿enlazados a ENG-5649?
8. 28281: ¿sigue con Edwin Garzon? ¿comentarios después del 11?
9. ¿Alguno cambió de status hoy?
10. ¿Hay tickets nuevos de ADUSA del 17-18 que no estén en los 35?

El resultado debe quedar en `inbox/2026-08-18-jira-verificacion.md`.

---

## Hechos de la reunión que sostienen el documento

Fuente: audio completo de 55 min transcrito local (`transcript-audio-reunion-completo.txt`).

- **Causa raíz admitida por Appriss**: los reportes/Izenda disparan el conteo de threads y
  arrastran a Incident. Los 502 vienen de ahí. Secure y Engage: cero impacto.
- **Compromiso con fecha**: separación ya en staging, QA esta semana, despliegue el fin de
  semana, visible el lunes. Advertencia de Chris: eso arregla Incident, no los reportes.
- **Jim abrió dudando del progreso**: "veo 16 abiertos, salimos del viernes con 13 o 14".
- **Chris es CTO** y le anunció al cliente que Juan enviaría el correo y el tracker nuevo.
- **Chris no marca nada resuelto por su cuenta**: lo deja para que el cliente lo firme.
- **RCS-28093**: ~300 números de tienda existen en más de una marca. La marca viaja en MISC1
  (que LPMS llama *division*) pero llega intermitente. Igual en el ambiente viejo, no es
  regresión. Matt va a sacar el conteo.
- **RCS-28342**: ADUSA verificó que el título SÍ está en su Active Directory. El fallo es de
  nuestra ingesta del claim. Ejemplos: Janai Harrison, Stacie Whetzel, Jonathan Wright y
  Melanie Engleman (esta última con último inicio de sesión conocido).
- **RCS-28161 no es Izenda**: es la exportación de la app, `Locations → Search → Export`, la
  que usan para carga masiva por FTP.
- **RCS-28123**: permiso concedido para validar de punta a punta en la ubicación **9999** de
  Stop & Shop, que es viva pero ficticia.
- **RCS-28356**: Chris lo declaró duplicado en la llamada y lo saltó.
- **Reunión siguiente**: jueves 20, temprano en la tarde ET (J.R. vuela a las 3:30). Choca con
  la ventana de migración de RCS-28292 (20 ago 11 p.m. → 21 ago 6 a.m. ET, April Valerio POC).
- **Jim se comprometió** a revisar qué reportes programados corren en horario laboral para
  moverlos a horas de baja carga.

---

## Verificación con el video

Se procesaron los 52 minutos de `~/Desktop/Grabación de pantalla...mov` (7 GB). Es la
grabación de la pantalla de Juan, no de la reunión.

- Confirmado que el archivo que Chris compartió es el mismo Tracker-3 que ya se tenía: barra
  de título `Appriss ADUSA-Support-Tracker.xlsx`, celda activa `A50 = RCS-28365`, que coincide
  con la fila 50 de Tracker-2 y Tracker-3.
- Leídas en pantalla, con el resaltado amarillo de Chris: RCS-28364 Resolved, RCS-28378
  Resolved, RCS-28379 Resolved, RCS-28407 Active with Appriss.
- Aparecen pantallas de Jira. En RCS-28365, comentario de Leigh Ann: *"Per the user Melanie
  Engleman, she is able to utilize the system as intended, verified 8/15 through an email
  received"*, y J.R. preguntando si es el mismo caso que RCS-28415 para enlazarlos.

---

## Dos decisiones abiertas

**RCS-28124** quedó como "Pending Ahold verification", igual que en la versión de J.R. Chris lo
había puesto como "Awaiting Ahold input" en su hoja interna. Se mantuvo el de J.R. porque la
definición de la fila 18 del propio documento dice que esa categoría es "se entregó un arreglo
y se espera que Ahold pruebe y confirme", que es donde está.

**RCS-28356** sigue como ticket propio pese a que Chris lo llamó duplicado, porque es el que
carga la explicación de arquitectura para el cliente y el que J.R. venía marcando como el de
mayor prioridad. Si se consolida, hay que hacerlo en Jira primero y recalcular el resumen.
