# PLAN. Escalación a ENG y tracker interno

Martes 1 de septiembre de 2026, verificado con `date`. Estados leídos de Jira en vivo hoy.
Jira quedó en solo lectura. Aquí no se escribió nada.

Criterio de Matt, que J.R. dejó por escrito dentro de RCS-28683 el 1 sep: defecto más pasos de
reproducción escritos en el ticket. Sin las dos cosas no escala.

## Los nueve, y de quién son hoy

| Ticket | Dueño hoy | Status | Qué toca |
|---|---|---|---|
| RCS-28693 | Vlad Bogus | Work in progress | Pega el comentario. Pregúntale a J.R. la ruta |
| RCS-28123 | **Juan** | Work in progress | Pega el comentario. Decide la ruta con J.R. |
| RCS-28589 | Matthew Kamminga | Under Engineering Review | Pega el comentario. Coordina con Ron antes de mover estado |
| RCS-28683 | Megha Rathi | Work in progress | Frenado. Faltan pasos de reproducción |
| RCS-28482 | **Juan** | Work in progress | Frenado. Appriss nunca lo reprodujo |
| RCS-28667 | Megha Rathi | Work in progress | Frenado. Falta contestar la pregunta de diseño |
| RCS-28596 | Shandana Khan | Accepted into Development | Ya arriba. Jim lleva seis días sin respuesta |
| RCS-28519 | Diego Buelvas | Closed | Cerrado |
| RCS-28533 | Diego Buelvas | Closed | Cerrado |

## Bloques para pegar

Cada archivo trae solo el texto. Abres, seleccionas todo, pegas.

- `inbox/2026-09-01-rcs-28693-comentario-interno.md`
- `inbox/2026-09-01-rcs-28123-comentario-interno.md`
- `inbox/2026-09-01-rcs-28589-comentario-interno.md`

Los tres llevan los cuatro requisitos de Aimee: entorno, pasos numerados con adjuntos nombrados,
notas de troubleshooting con la declaración de uso de IA, y las conversaciones que ocurrieron fuera
del ticket. Donde falta un dato el comentario dice que falta y pide que lo escribas. No lo inventé.

## Antes de pegar, tres datos que solo tienes tú

1. **RCS-28693.** El entorno y la URL literal del nuevo sign in. Y transcribe el mensaje de error de
   Harrison Xu, que vive solo dentro de `LPMS SSO Issue.png` y `LPMS SSO Issue pt 2.docx`. Ábrelos.
2. **RCS-28123.** El entorno.
3. **RCS-28589.** El entorno.

## La ruta, y lo que no puedes decidir solo

**RCS-28693.** El caso de Paula Dotson entrega rol a una identidad sin aprovisionar en Azure. Eso es
control de acceso, no permisos de tienda. La tabla de Aimee manda Secure e Incident Engineering a
Under Engineering Review con Shandana Khan. Para acceso hay otra ruta, Under Security Review, que se
queda a tu nombre y auto crea INFOSEC. **No hay precedente del mismo defecto en Jira para decidirlo
por analogía. Pregúntale a J.R. hoy.**

**RCS-28123.** No es defecto. La ruta al popup desde reassign se cerró en código hace tres años y
medio a propósito. Restaurarla cambia el producto. Va al Feedback Portal, o va a ENG con
justificación de negocio. La decisión es de J.R.

**RCS-28589.** Ya está arriba. Ron acordó en la llamada etiquetar a Ryan de Delivery y devolverlo a
la lista. Habla con él antes de mover el estado o se cruzan las dos rutas.

## Sobre el ENG que no aparece solo

El doc de Aimee dice que la transición auto crea el ENG. El changelog dice otra cosa. RCS-28596
entró a Under Engineering Review el 27 ago 17:07 y ENG-7904 nació quince horas después, clonado a
mano por Shandana Khan. RCS-28589 entró hoy 11:32 y sigue sin ENG. Transiciona, asigna a Shandana, y
persigue el ENG a las 24 horas si no existe.

## Dos deudas con Jim que no son de escalación

**RCS-28596.** Seis días sin respuesta desde el acuse del 26 de agosto, sobre el único ticket del
lote con causa raíz confirmada en código. Es el que peor se ve.

**RCS-28482.** Seis días con una promesa sin fecha. Es tuyo.

Los dos necesitan respuesta al cliente, que va por `cerebro-respuesta-cliente` y en formato
distinto: sin markdown, sin hallazgos de investigación, sin fecha futura. Pídemelos cuando quieras.

---

# Tracker interno

`adusa-envio-hoy/Appriss ADUSA-Support-Tracker - INTERNO 09012026 v2.xlsx`

**Solo se tocaron las filas 61 a 69.** Verificado celda por celda contra el original de J.R.: filas
1 a 60 sin un solo cambio, resumen sin tocar, hoja `Support tracker_old` sin tocar.

Las nueve quedan con las quince columnas llenas, en el formato del bloque de J.R.: columna B el
título, columna C la descripción del reporter, y de D a O el resto. La prosa sale de tu D11 y los
estados, assignees y fechas de Jira de hoy.

| Fila | Ticket | Status | Action with | Assignee |
|---|---|---|---|---|
| 61 | RCS-28482 | Work in progress | Active with Appriss | Juan Martinez |
| 62 | RCS-28519 | Closed | Closed | Diego Buelvas |
| 63 | RCS-28533 | Closed | Closed | Diego Buelvas |
| 64 | RCS-28667 | Work in progress | Active with Appriss | Megha Rathi |
| 65 | RCS-28123 | Work in progress | Active with Appriss | Juan Martinez |
| 66 | RCS-28693 | Work in progress | Active with Appriss | Vlad Bogus |
| 67 | RCS-28683 | Work in progress | Active with Appriss | Megha Rathi |
| 68 | RCS-28596 | Accepted into Development | Active with Appriss | Shandana Khan |
| 69 | RCS-28589 | Under Engineering Review | Active with Appriss | Matthew Kamminga |

`Engineer assigned` va vacío en seis de las nueve porque esos tickets no tienen ingeniero. Lleva
Matt el 28123, el 28596 y el 28589. Ese vacío es el dato que J.R. está buscando.

## Lenguaje, lo que se revisó

Auditadas las columnas que escribí, `Issue summary`, `Next steps`, `Cause` y `Appriss Notes`. Cero
guiones largos, cero guiones medios, cero guiones como conector, cero paréntesis explicativos, cero
adversativas de compensación, cero muletillas de IA. Voz activa en todas. Ritmo roto a propósito con
frases cortas.

Las columnas `Issue summary` y `Next steps` van en tercera persona Appriss y quedaron limpias de
nombres de ingenieros, de tickets ENG y de otros clientes. Es la forma que tienen esas columnas en
el documento del cliente, así que si alguna fila se copia al D-series no arrastra nada interno. Los
nombres, los ENG y el precedente de Lux quedaron en `Appriss Notes`, que nunca sale.

**Lo que conserva guiones a propósito, y por qué.** Los prefijos de fecha `8/26/2026 - texto` en
`ADUSA Comments` y `Appriss Notes`, porque es el formato que usan las otras 37 filas del documento y
romperlo en nueve filas se vería peor. Las citas textuales del reporter, incluidos su `however` y su
`in order to` y sus paréntesis, porque son sus palabras. Los valores literales de Jira `Support
Resolved, Fixed Configuration` y `Customer Resolved, Customer Requested Ticket to be Closed`. Y los
nombres de reporte que dio Jim.

Los títulos de la columna B quedaron sin el prefijo de cliente y sin guiones. J.R. tenía `AHL/DLZ -
Greyed out fields in Izenda` y `Delhaize - Screen Not Rendering Correctly`. Los dejé como `Greyed
out fields in Izenda` y `Screen not rendering correctly`, que es como escriben las filas 23 a 59.
Dime si prefieres los originales de él.

## Tres cosas que dejé sin tocar

1. La fila 60 duplica RCS-28482, escondida, solo con el número y el título. La 61 ya está completa.
2. La fila 38 duplica RCS-28123, escondida, con la versión del 19 de agosto. La 65 ya está completa.
3. El resumen sigue diciendo Total 37. Las fórmulas son COUNTIF sobre rangos que terminan en la fila
   59, así que las filas 60 a 69 quedan fuera de todo conteo. Con las nueve dentro serían 46.

Sigue faltando **RCS-28588**, el único de tu D11 que no existe en el interno.

## Deudas que crean estos textos

Los tres comentarios internos prometen escribir datos en el ticket. Ninguno promete fecha al
cliente. El de RCS-28589 pide dos cosas a Ahold y el de RCS-28123 pide dos. Cuando los pegues,
esas cuatro peticiones quedan abiertas a tu nombre.
