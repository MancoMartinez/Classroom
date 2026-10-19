# ADUSA, 1 de septiembre. Las dos reuniones, los dos trackers y qué te pidió J.R.

Fuentes: `2026-09-01-reunion-ahold.md`, `2026-09-01-reunion-corta-jr.md`, `jr-corta-crudo.txt`,
el hilo de Teams con J.R. de las 9:07 a 9:12, `Appriss ADUSA-Support-Tracker (2).xlsx` que él
te mandó, y tu `Appriss ADUSA-Support-Tracker - 08312026 D11.xlsx`.
Estados de Jira verificados en vivo el 1 sep. Contenido revisado contra las fuentes por un
segundo pase.

---

## 1. La respuesta a tu pregunta: qué son las filas 66 a 69

J.R. dijo esto, limpiando las muletillas del audio: *"rows 66 through 69 are already in the list
but hidden, so just go through, find them in the list. If they're already on this spreadsheet
just unhide it and update it and delete this wrong. Otherwise just try to add in the formatting
and stuff so it looks like these, please."*

Abre el interno que él te mandó y baja al final del detalle. Las filas 66 a 69 no son filas de
tracker, son cuatro pegotes que él dejó ahí mientras cruzaba tu D11 contra el interno:

| Fila | Qué hay literalmente en la celda A |
|---|---|
| 66 | `RCS-28693` |
| 67 | `RCS-28683` |
| 68 | `[RCS-28596] Ahold-Delhaize - Employees Duplicated in a View - The Retail Equation, Inc` |
| 69 | `https://trebuco.atlassian.net/browse/RCS-28589`, más la nota en la columna M *"This one just came back from Jim w/ apostraphe issues."* |

Las 66 y 67 son el número pelado. La 68 es el título pegado del navegador. La 69 es la URL. Las
cuatro van sin tema, sin status, sin assignee y sin fechas.

**Reconstrucción de lo que hizo J.R.** Tomó tu D11, fue metiendo al fondo del interno todo lo
que le faltaba, y a la mitad se quedó sin tiempo. Las filas 60 a 65 alcanzó a llenarlas o a
esconderlas. Las 66 a 69 quedaron crudas.

**Su frase "already in the list but hidden" es una advertencia, no un dato.** Está avisando que
pegó rápido y que alguno de esos cuatro podría estar ya arriba, escondido, y que hay que
deduplicar antes de crear la fila.

**Lo verifiqué. Se equivocó en los cuatro, y acertó en otros dos que no nombró.**

Ninguno de los cuatro de las filas 66 a 69 existe en ningún otro lugar del interno. Los cuatro
hay que construirlos completos, con el formato de las filas de arriba, y borrar el pegote.

Los duplicados reales están en otro lado:

- **RCS-28482.** Fila 60 escondida con solo el número y el título. Fila 61 visible con 6 de las
  15 columnas llenas, sin assignee, sin fechas, sin next steps, sin priority. Borra la 60,
  completa la 61.
- **RCS-28123.** Fila 38 escondida con la fila del 19 de agosto completa. Fila 65 visible con
  media fila del 1 de septiembre. Funde las dos en una y borra la otra.

Eso es exactamente lo que él pidió, aplicado donde de verdad pasa.

### La convención de ocultar, y dónde se rompe

Contra Jira de hoy funciona: escondida significa cerrada, visible significa abierta. La única
excepción es RCS-28281, escondido y abierto.

Contra la propia columna Status del interno se rompe ocho veces. Estas ocho filas están
escondidas y marcadas *Active with Appriss*: 28124, 28161, 28177, 28196, 28281, 28353, 28356 y
28407. Siete ya cerraron en Jira y la hoja no se enteró. Quien lea el interno sin Jira al lado
ve ocho contradicciones.

Las cuatro filas nuevas van visibles, porque los cuatro tickets están abiertos hoy.

### El resumen del interno está roto

La tabla de las filas 6 a 17 dice Total 37 y la cabecera dice *Status as of Wednesday, August
19, 2026*. El detalle ya tiene 45 tickets únicos. J.R. pegó ocho filas nuevas debajo y nunca
tocó el resumen. Cuando termines de limpiar, recalcula esa tabla y cambia la fecha, o el
documento sigue diciendo una cifra que ninguna fila respalda.

---

## 2. El diff exacto entre los dos trackers

Tu D11 tiene 43 tickets. El interno tiene 45 filas únicas.

**Solo un ticket tuyo no está en el interno: RCS-28588**, *Store numbers should be 4 digits*,
Ryan Barlow, Completed y Resolved.

**Tres del interno no están en el tuyo:**

| Ticket | Situación |
|---|---|
| RCS-28447 | Izenda Access, cerrado el 19 de agosto. Nunca entró al tracker del cliente, igual que en el D5. Registrado en `inbox/2026-08-24-adusa-d6-llamada-lunes.md`. Está Closed y Resolved, no mueve el conteo de abiertos. |
| RCS-28683 | Nació ayer 31 de agosto a las 15:40. El D11 cerró antes. |
| RCS-28693 | Nació hoy 1 de septiembre a las 09:55. |

Nada más difiere. Los otros 42 coinciden.

---

## 3. El ticket de Secure que J.R. menciona, y por qué no cuadra

J.R. te escribió en Teams: *"I met with Matt about them already and added the missing ones from
your sheet, other than the Secure ticket."*

Consulté el campo Product Type en Jira:

| Ticket | Product Type | ¿Está en el interno? |
|---|---|---|
| RCS-28281 | **Secure 5 - EBR** | Sí, fila 57, escondida, y está Work in progress |
| RCS-28125 | Secure 3 or 4 - EBR | Sí, fila 58, escondida, Closed |
| RCS-28588 | **Incident, antes LPMS** | **No** |

El único que falta es RCS-28588 y no es de Secure. El de Secure de verdad es RCS-28281, ya está
en el interno, y está escondido pese a estar abierto.

Hay dos lecturas y las dos te obligan a lo mismo:

1. J.R. confundió 28588 con un ticket de Secure porque cae junto a 28589 en el tema de archivo
   de tiendas. Entonces falta meterlo.
2. J.R. quiso decir que deja 28281 fuera del alcance del interno por ser Secure. Entonces hay
   que sacarlo del interno o dejarlo escondido a propósito, y 28588 sigue faltando igual.

Pregúntale cuál de las dos. Es una línea en Teams y evita que el conteo de abiertos quede mal
en el documento que él usa para decidir cuándo pasar la llamada a async.

**Ojo con el efecto en el conteo.** Si 28281 sale del interno por ser Secure, los abiertos de la
escalación bajan de diez a nueve sin que nadie arregle nada. Eso ayuda a justificar el async que
J.R. quiere. Que la baja quede explicada como cambio de alcance y no como cierre, o Jim lo va a
leer como progreso que no ocurrió.

---

## 4. Cómo se conecta con el informe diario de Jim

Son dos documentos distintos con dos públicos distintos y J.R. lo dijo explícito: *"this is not
the spreadsheet you're sending out to Jim. I still expect you to generate your Jim spreadsheet
the way that you have been."*

| | Tuyo, para Jim | Interno, de J.R. y Matt |
|---|---|---|
| Nombre | `Appriss ADUSA-Support-Tracker - MMDDAAAA D##.xlsx` | `Appriss ADUSA-Support-Tracker.xlsx` |
| Columnas | 10 | 15 |
| Última versión | D11, estado del 31 de agosto | cabecera del 19 de agosto, detalle parcheado a mano |
| Cadencia | correo diario más llamadas martes y jueves | cuando J.R. lo toca |
| Métrica de quien lo lee | Jim: menos amarillo, mejor | J.R.: conteo de abiertos para decidir el async |

Las cinco columnas del interno que nunca salen al cliente: `Theme`, `Engineer assigned`,
`Cause`, `Appriss Notes`, `Priority`.

**La relación real es que el interno se alimenta de tu D-series y va nueve días hábiles
atrasado.** Su cabecera es del 19 de agosto, que en la numeración D es el D3. Hoy sale el D12.
Tu tracker es la fuente. El de J.R. es la copia que él mantiene a mano y que hoy está sucia. Por
eso te pidió a ti que lo limpies.

### Lo que entra al D12 de hoy

El D11 quedó en 43 tickets, 36 resueltos, 7 activos. Hoy pasan tres cosas y ningún cierre:

- **RCS-28683**, *Adding additional associate to case*, creado ayer 15:40, Megha Rathi, Work in
  progress. Error 404 al agregar una persona al caso. La persona sí queda agregada. Hay que
  desplegar hacia ella para verla en el workbench.
- **RCS-28693**, *User not provisioned to system unable to log in, SSO error should have
  defaulted to Store Reporter Role*, creado hoy 09:55, Vlad Bogus, Work in progress.
- **RCS-28589 se reabrió.** En el D11 lo mandaste como Completed y Resolved, que era correcto el
  31 de agosto. Hoy Jira lo tiene en Under Engineering Review con resolution vacía, actualizado
  a las 11:43. Leanne lo dijo en la llamada: lo cerraron como resuelto y ella lo considera
  resuelto solo en parte.

**D12 sale en 45 tickets, 35 resueltos, 10 activos.** Jim va a ver tres amarillos más que ayer,
y uno de ellos es un amarillo que ayer estaba verde. Su métrica es el amarillo. El correo tiene
que abrir explicando los tres, y en especial por qué 28589 volvió, o el número habla solo y
habla mal.

Los diez abiertos, confirmados con `resolution IS EMPTY` en Jira: 28093, 28123, 28281, 28482,
28535, 28589, 28596, 28667, 28683, 28693.

**RCS-28693 conviene agruparlo con el hilo de provisioning** de RCS-28415, RCS-28519 y
RCS-28667. La agrupación es defendible, no es un hecho establecido. Los tres anteriores son
usuario nuevo sin jerarquía que no puede seleccionar tienda. El 28693 es usuario no provisionado
que no puede entrar, con un error de SSO que debió caer a Store Reporter Role. El denominador
común es el provisioning por SSO y esa verificación lleva abierta desde el 17 de agosto. Escribe
la fila señalando el patrón y marcando que falta confirmarlo, y el conteo deja de parecer una
cadena de casos sueltos.

---

## 5. Los nueve tickets abiertos y su enlace a ENG

J.R. pidió, limpiando el audio: *"each one of these nine tickets, make sure we have steps to
reproduce in the ticket. And if we do, we can validate it, then link it to an ENG ticket. Create
an ENG ticket and link it, please."*

Los nueve que Ron contó en la llamada son estos. RCS-28693 nació después y hace el décimo.

| # | Ticket | Status | Assignee | Enlace ENG |
|---|---|---|---|---|
| 1 | RCS-28535 attachments, **el grande** | Work in progress | Edwin Garzon | **ENG-7181, In Development** |
| 2 | RCS-28093 employees not restricted | Accepted into Development | Matthew Kamminga | **ENG-6744, Ready for Development** |
| 3 | RCS-28596 employees duplicated | Accepted into Development | Shandana Khan | **ENG-7904, Backlog** |
| 4 | RCS-28123 case assignment | Work in progress | **Juan Martinez** | ENG-7192, **Done** |
| 5 | RCS-28482 greyed out fields Izenda | Work in progress | **Juan Martinez** | **ninguno** |
| 6 | RCS-28589 store file apóstrofe | Under Engineering Review | Matthew Kamminga | **ninguno** |
| 7 | RCS-28667 users sin jerarquía | Work in progress | Megha Rathi | **ninguno** |
| 8 | RCS-28683 404 al agregar persona | Work in progress | Megha Rathi | **ninguno** |
| 9 | RCS-28281 transaction data load | Work in progress | Nikita Rathore | ninguno, es Secure |
| 10 | RCS-28693 SSO sin provisionar | Work in progress | Vlad Bogus | **ninguno** |

### Corrección importante al encargo de J.R.

**El ticket ENG no se crea a mano.** Lo auto-crea la transición de estado. Según el
procedimiento de Aimee Wadsworth, para Secure e Incident Engineering se mueve el ticket a
**Under Engineering Review** y se asigna a **Shandana Khan**, y el ENG se genera solo con los
comentarios sincronizando en ambos sentidos. Ver
`brain/memoria/reference_escalacion_l3_procedimiento.md`.

Si creas ENGs a mano quedan huérfanos, sin sincronización de comentarios, y duplicados cuando
alguien haga la transición correcta después.

**Hay una prueba de esto delante tuyo.** RCS-28589 ya está en Under Engineering Review y sigue
sin ENG. Está asignado a Matthew Kamminga, no a Shandana Khan. La transición se hizo con el
assignee equivocado y el auto-create no disparó. Eso es lo que hay que arreglar en ese ticket,
no crear un ENG nuevo.

### Lo que Aimee exige antes de escalar, sin excepción

Entorno, pasos completos de reproducción con capturas, las notas de troubleshooting, y toda
conversación con otros ingenieros que ocurrió fuera del ticket. El 13 de agosto comentó cuatro
tickets de Vedant en cuatro minutos por saltarse esto. Ibas en copia.

### RCS-28123 merece atención aparte

ENG-7192 está **Done** y el RCS sigue abierto. Eso coincide con lo que Matt encontró en la
llamada: el popup de confirmación con ver e imprimir está atado a approve y a mark case
completed, no a reassign. El arreglo entregado no toca lo que el usuario reporta.

El problema real que planteó Leanne es otro y ninguno de los dos tickets lo cubre: reasignar no
devuelve confirmación. El usuario tiene que mirar el panel izquierdo, que tarda uno o dos
minutos en refrescar, para saber que el caso se movió. Eso es una petición de feature, no un
defecto. Matt habla con Kelly de Hannaford y trae notas el jueves.

Este es tu ticket. Nadie más lo va a mover.

---

## 6. Pasos, en orden de urgencia

**Hoy, antes de mandarle nada a Jim**

1. **Confirma con J.R. lo del ticket de Secure.** Una línea en Teams. El interno no puede quedar
   con el conteo de abiertos ambiguo. Bloquea el punto 2.
2. **Limpia el interno.** Cuatro filas nuevas completas para 28693, 28683, 28596 y 28589,
   visibles, con el formato de las de arriba. Borra los pegotes de 66 a 69. Borra la fila 60,
   que duplica 28482, y completa la 61. Funde 38 con 65 en una sola fila de 28123. Decide 28588
   y 28281 según lo que conteste J.R. Recalcula el resumen de las filas 6 a 17 y cambia la fecha
   de la cabecera. Revisa las ocho filas escondidas que dicen *Active with Appriss* y alinéalas
   con Jira.
3. **Genera y envía el D12 a Jim.** 45 tickets, 35 resueltos, 10 activos. El correo abre
   explicando los tres cambios, con 28589 primero por ser el que retrocede. Sigue el método de
   J.R.: el adjunto es el reporte, el correo solo pide lo que necesita respuesta del cliente.
   Formato en `brain/memoria/reference_tracker_adusa_formato.md`, generador en
   `adusa-envio-hoy/generador/`.
4. **Avísale a J.R. cuando el interno esté limpio.** Te lo pidió explícito y él está esperando
   para asignar.

**Mañana y miércoles, antes de la llamada del jueves**

5. **RCS-28589.** Está en Under Engineering Review sin ENG. Reasigna a Shandana Khan para que
   dispare el auto-create. Ron va a etiquetar a Ryan de Delivery y devolverlo a la lista, así
   que coordina antes de mover el estado o se cruzan las dos rutas. Leanne dio el detalle
   exacto: el apóstrofe no aparece en el registro de tienda de Food Lion Store 1, sí aparece al
   exportar el CSV de ubicaciones en la columna 8c, y no aparece en los reportes de Izenda que
   alimentan Power BI. Lo mete el export, y ese export alimenta otro sistema del cliente. Eso
   son pasos de reproducción listos.
6. **RCS-28482 y RCS-28667.** Verifica que tengan pasos de reproducción escritos en el ticket.
   Si los tienen, transición a Under Engineering Review con Shandana Khan. El 28482 es tuyo. El
   28667 es de Megha, coordina antes de tocarlo o quedan dos voces en el mismo ticket.
7. **RCS-28683 y RCS-28693.** El 28683 ya lo están reproduciendo. Cuando la reproducción quede
   escrita en el ticket, escala igual. El 28693 acaba de nacer, primero triage.
8. **RCS-28535, el de attachments.** Es la palanca completa. J.R. dijo que con dos o tres de los
   grandes tumbados la llamada pasa a async y nombró este. ENG-7181 está In Development. No lo
   escales, empújalo. Pide fecha a Matt y ponla en la fila del D12, porque Jim dijo que es el
   único que causa consternación real y que lo escuchó fuerte de una de las marcas el viernes.
9. **RCS-28123.** Cierra el hilo de Matt con Kelly de Hannaford el jueves. Decide si la falta de
   confirmación al reasignar se abre como feature request separado o se documenta en el mismo
   ticket. Aclara por qué ENG-7192 está Done con el RCS abierto.

**Pendiente que viene arrastrado y nadie ha cerrado**

10. **RCS-28093.** Verifica hoy la posición 20 del empleado 5701349746 en la tienda 0001 antes de
    contestarle a Jim. El ejemplo que tienes escrito es del 21 de agosto y April pudo haber
    corregido el feed. Detalle en `inbox/2026-08-31-cambios-desde-el-D10-y-dos-correos.md`.
11. **RCS-28327**, *Delhaize (DHZ): Loyalty Discounts not Specified*, Work in progress, está
    **asignado a ti** y no aparece en ninguno de los dos trackers. Decide si entra al alcance de
    la escalación o se trabaja aparte.

---

## 7. Otros abiertos de ADUSA fuera de los dos trackers

Salieron del barrido de Jira. Ninguno está en el D11 ni en el interno. Confirma si es
deliberado:

| Ticket | Resumen | Status | Assignee |
|---|---|---|---|
| RCS-28327 | Delhaize (DHZ): Loyalty Discounts not Specified | Work in progress | **Juan Martinez** |
| RCS-28368 | Add Tender Types for Evermore and FIS Insurance Cards | Under Customer Review | Nikita Rathore |
| RCS-28456 | Add / Display Price Checked Items (AHL) | Work in progress | Gulshan Kumar |
| RCS-28472 | Delhaize (DHZ): Unable to see expanded results when Tender Type is in summary | Accepted into Development | Shandana Khan |
| RCS-28547 | Ahold's Sunday Morning Data Sent but Not Loaded | Work in progress | Bikash Kumar |

Sobre RCS-28456 hay historia sucia y conviene cerrarla. El 18 de agosto se marcó como ticket de
ADUSA fuera de los 35. El 19 una nota afirmó que no existía y que no era de ADUSA, y eso es
falso. Jira de hoy confirma que existe, que es de ADUSA y que está abierto. No hay decisión
registrada de excluirlo. Decídelo ahora.

---

## Enlaces

- `2026-09-01-reunion-ahold.md` y `2026-09-01-reunion-corta-jr.md`
- `inbox/2026-08-31-cambios-desde-el-D10-y-dos-correos.md`
- `inbox/2026-08-24-adusa-d6-llamada-lunes.md`
- `brain/memoria/reference_escalacion_l3_procedimiento.md`
- `brain/memoria/reference_tracker_adusa_formato.md`
- `brain/markdown/26-adusa-estado-tickets-reuniones.md`
- `adusa-envio-hoy/0-LEEME-PRIMERO.md`
