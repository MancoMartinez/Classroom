# Correo del 18 ago (post-reunión) + diff exacto del tracker

Archivo: `~/Downloads/Appriss ADUSA-Support-Tracker - 08182026 PM.xlsx`
Construido sobre la plantilla de J.R.: mismos estilos, mismas 10 columnas, mismos colores de
"Action with", mismas 2 hojas, misma agrupación por tema, mismo orden de filas.

---

## 1. Correo para Jim

```
Jim,

Thank you for the detailed answers this morning and for the time on the call.  I've updated
the tracker on our side with everything that came out of both and it's attached.  Four items
closed today, which takes us from sixteen resolved to twenty.

A few things I need from you directly, separate from the tracker, because these are the ones
that move fastest with an answer from your side.

Performance, RCS-28356 and RCS-28407.  You saw latency but no 502s this morning, and Leigh Ann
logged one with detail.  The read we still don't have is from the Hannaford team who reported
the longest page open times.  Have they seen a difference since Monday evening?

Attachments, RCS-28124.  The upload fix went into this morning's release, so this one is
waiting on a test rather than on us.  Could someone try a video upload and tell us either way?
Separately, .txt was the only format that didn't behave in our testing.  Is that a format your
teams actually use?

The Central Division report, RCS-28413.  We have the name and the expected count now, thank
you.  Before we send a correction out, who received the 66 case version, and do you want us to
reissue to that list or send you the file to distribute?

Scheduled reports.  You offered to look at which ones run during business hours.  If you send
us the list and the time you need each report by, we'll move them and confirm.

RCS-28196, the two Shoplifting fields.  They no longer default to No.  The question for your
side is whether cases entered between cutover and the fix need reviewing for those two fields.
If so we can pull the list.

New user provisioning, RCS-28415 and RCS-28365.  Both users are corrected.  Matt offered to
walk your team through assigning locations in the new application, since that screen differs
from the one they were trained on.  Is that useful, and who should be on it?

On the Secure side, RCS-28281.  Understood that it sits outside this workstream, and we'll
take it up with Lauren Linsenbach and Jacquelyn Wunders directly.  The original question still
stands for them: do you need the missing volume backfilled, or is a corrected figure for that
date enough?

Four to close: RCS-28177, RCS-28364, RCS-28378 and RCS-28379.  All show resolved on both
sides.  Confirm and we'll close them in Jira today.

One note on the attached.  RCS-28342 has moved back to active rather than waiting on you.  The
individual records were corrected, but your examples show the job title is missing on other
accounts too, so we're looking at how the claim is mapped rather than fixing them one at a
time.


Thanks,
```

~400 palabras, igual que el de J.R. (~430). Ocho pedidos más una nota, contra diez más una
corrección en el suyo.

---

## 2. Por qué cada pregunta, y por qué NO están las otras

| Pregunta | Justificación |
|---|---|
| Hannaford, 502 y lentitud | J.R. la pidió ayer y **nadie la contestó**. James dio su propia experiencia, no la de Hannaford, que es el equipo que reportó los tiempos más largos. Sin esa lectura no se sabe si el fix del 17 sirvió donde más dolía. |
| Prueba de subir video (28124) | El fix salió en el release de esta mañana. Appriss ya probó de su lado. Leigh Ann dijo tener tres mensajes pendientes de respuesta. **El ticket no avanza sin la prueba de ellos.** |
| ¿Usan .txt? (28124) | Hallazgo nuevo de las pruebas de hoy. Es el único formato que falla. Si no lo usan, no vale la pena retener el ticket por eso; si lo usan, cambia la prioridad. **Sin la respuesta se decide a ciegas.** |
| Quién recibió el reporte de 66 casos (28413) | James pidió corregirlo. Para reemitir hace falta saber a quién le llegó la versión mala. **Es el único dato que falta para cerrar el ciclo**, y él no lo dio. |
| Lista y horarios de reportes programados | **Jim se ofreció él mismo** al final de la llamada a revisar cuáles corren en horario laboral. Es un compromiso suyo, no un pedido nuestro. Pedir la lista es darle continuidad, no cargarle trabajo. |
| Casos entre el cutover y el fix (28196) | J.R. ya lo había señalado en su versión: *"ADUSA may want to decide whether cases entered since cutover need reviewing"*. **Sigue sin decidirse** y solo ellos pueden decidirlo, es su dato. |
| Llamada de acompañamiento (28415/28365) | **Matt la ofreció en la reunión** y nadie la agendó. La causa real fue que Leigh Ann asignó la jerarquía al nivel de arriba porque la pantalla cambió. Sin la llamada se repite con cada usuario nuevo. |
| Backfill o cifra corregida (28281) | Es **la pregunta original de J.R. que quedó sin responder**. James dijo que él no maneja el tema y nombró a Lauren y Jacquelyn. La pregunta no se cae, cambia de destinatario. |
| Confirmación para cerrar 4 tickets | ADUSA dijo verbalmente que los cierra. Chris fue explícito: **Appriss no marca nada resuelto por su cuenta.** Sin el sí por escrito no se pueden cerrar en Jira. |

**Preguntas de J.R. que NO repito, porque James ya las contestó hoy:**

| Pregunta de ayer | Respuesta de James |
|---|---|
| Un reporte con nombre que falle (28021) | Dio dos: *PBI - Incident Export 2026 Q3* y *PBI - Current Location Listing*, con el patrón exacto de CSV/XLS. |
| Qué esperan de la búsqueda de empleados (28093) | Lo demostró con el ejemplo de Tahj Stone. Ahora **nosotros les debemos** el conteo de registros con Misc 1, no al revés. |
| Contacto y validación de la migración (28292) | April Valerio, y él valida la mañana del 21. |
| Qué página y qué usuarios (28378) | La página de shoplifting de Hannaford, y ya está resuelto. |
| ¿Levanto el Feature Request? (28304) | Sí, pero prioridad baja, se puede archivar. |
| Confirmación de 28177 y 28364 | Confirmados. Solo falta el sí formal para cerrar. |

Volver a preguntar cualquiera de estas sería el error más visible del correo.

---

## 3. Diff exacto contra la versión de J.R.

### Resumen por tema

| Tema | Cambio |
|---|---|
| Login and access | sin cambio |
| **User accounts and duplicates** | Resolved **1 → 4**, Pending **3 → 0** |
| Store and brand restrictions | sin cambio |
| **Case entry and assignment** | Resolved **2 → 3**, Awaiting **2 → 0**, Active **2 → 3** |
| Attachments and file handling | sin cambio |
| Reporting and exports | sin cambio |
| Performance and timeouts | sin cambio |
| Platform configuration and notifications | sin cambio |
| Transaction, tender and POS data | sin cambio |
| Change requests and scoping | sin cambio |
| **Total** | Resolved **16 → 20**, Pending **4 → 1**, Awaiting **2 → 0**, Active **13 → 14** |

Solo se movieron dos temas. Los otros ocho quedaron idénticos porque en ellos no cambió ningún
estado, solo texto. Verificado: los diez temas suman exacto al total, y el total coincide con el
conteo real de las 35 filas de detalle.

### Cambios de estado (6 tickets)

| Ticket | De → A | Motivo |
|---|---|---|
| RCS-28177 | Pending Ahold verification → **Resolved** | Christina Cordero confirmó en vivo antes de la llamada; Jonathan Wright ya veía sus casos |
| RCS-28364 | Pending Ahold verification → **Resolved** | Búsqueda hecha durante la llamada devuelve casos hasta enero |
| RCS-28378 | Awaiting Ahold input → **Resolved** | Era la página de shoplifting de Hannaford, ya resuelta |
| RCS-28379 | Active with Appriss → **Resolved** | Muestra de la hoja 2 tomada en vivo, todos con owner |
| RCS-28304 | Awaiting Ahold input → **Active with Appriss** | James decidió: sí levantar el FR. Ya no espera input de ellos, ahora nos toca |
| RCS-28342 | Pending Ahold verification → **Active with Appriss** | Retrocede: ejemplos nuevos siguen fallando |

### Texto actualizado sin cambio de estado (13 tickets)

`28093` `28365` `28415` `28123` `28196` `28124` `28021` `28161` `28413` `28353` `28356`
`28407` `28281` `28292`

### Sin tocar, ni una letra (13 tickets)

`28014` `28042` `28059` `28053` `28135` `28023` `28043` `28115` `28369` `28025` `28075`
`28030` `28041` `28109` `28125`

**Por qué**: son los cerrados hace días que nadie mencionó hoy ni en la reunión ni en el correo
de James. Tocarlos sería inventar movimiento donde no lo hubo, y el cliente compara versiones.

---

## 4. Qué fuentes usé y cuáles NO

**Sí, completas:**
- **Audio de la reunión**, 55 minutos, transcrito local con whisper. Fuente principal; donde
  contradecía notas previas, mandó el audio.
- **Transcript de Moscú**, como segunda pasada para tramos donde el audio quedó confuso.
- **Tracker-3 de Chris**, parseado celda por celda y comparado contra Tracker-2 para aislar
  exactamente qué editó él durante la llamada.
- **Correo de James** del 18 a las 11:51 a.m., con las nueve capturas.
- **Correo de J.R.** del 17 con los once puntos.
- **Nota de voz de J.R.** del 18.

**No, y conviene que lo sepas:**
- **Jira: no verificado.** El conector de Atlassian está caído desde antes de armar el archivo y
  sigue caído. Los estados de la columna C salen del Tracker-3 y de la reunión, no de Jira.
  Concretamente sin confirmar: si RCS-28177, 28364, 28378 y 28379 ya están en un estado de Jira
  coherente con "Resolved", y si 28342 y 28415 tienen dueño asignado hoy.
- **El video de pantalla de 7 GB: no procesado.** Es la grabación de Chris compartiendo el
  tracker. Su contenido debería ser el mismo Tracker-3 que ya tengo exacto al byte, así que el
  riesgo es bajo, pero si quieres lo extraigo por frames y lo confirmo.

---

## 5. Dos decisiones que tomé y conviene que revises

**RCS-28124 quedó como "Pending Ahold verification"**, igual que en la versión de J.R. Chris lo
había puesto como "Awaiting Ahold input" en su hoja interna. Me quedé con el de J.R. porque la
definición que el propio documento trae en la fila 18 dice que esa categoría es *"se entregó un
arreglo y se espera que Ahold pruebe y confirme"*, que es exactamente donde está. Si prefieres
respetar la edición de Chris, es un solo cambio.

**RCS-28356 sigue como ticket propio.** Chris lo declaró duplicado en la llamada y lo saltó,
pero es el que carga la explicación de arquitectura para el cliente y el que J.R. venía marcando
como el de mayor prioridad. Si se consolida con RCS-28353 hay que hacerlo en Jira primero y
recalcular el resumen, si no la hoja y Jira se contradicen.
