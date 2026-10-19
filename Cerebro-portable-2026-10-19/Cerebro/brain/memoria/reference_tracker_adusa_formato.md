---
name: reference_tracker_adusa_formato
description: "Cómo se arma el tracker de ADUSA para el cliente y el método de correo de J.R. Teagle, deducidos de sus archivos reales"
metadata: 
  node_type: memory
  type: reference
  originSessionId: a8293f75-ab64-479b-971f-f586abf0f63b
  modified: 2026-08-18T22:18:31.729Z
---

**Dos documentos distintos, no confundirlos.**

| | Versión al cliente (J.R.) | Interna (Chris) |
|---|---|---|
| Columnas | 10 | 14 |
| Hojas | 2 (la 2ª son casos de ejemplo) | 1 |
| Columna D | `Action with` | `Status` duplicado |
| Extra | — | `Engineer assigned`, `Cause`, `Priority`, `Appriss Notes` |

`Appriss Notes` es la peligrosa: lleva texto interno crudo ("QA not passed", "Gina: unable to
reproduce in test demo7", nombres de ingenieros, ambientes). **Se elimina antes de enviar.**

**Estructura de la hoja del cliente**: título, fecha de corte, línea de cadencia (llamadas
martes 2:30 PM ET y jueves 3:30 PM ET), tabla resumen por tema con 5 columnas de conteo, la
nota que define las categorías, y el detalle agrupado por tema con banda alterna. Las cuatro
categorías de `Action with` y sus colores: Resolved, Pending Ahold verification (arreglo
entregado, esperando que Ahold pruebe), Awaiting Ahold input (Appriss necesita info o acción
de Ahold), Active with Appriss.

**Escritura de J.R. en las celdas**: tercera persona ("Appriss will..."), causa cuando se
conoce, el pedido concreto al final ("Please have those users sign out, sign back in and
confirm"), honesto sin flagelarse ("Appriss is not calling it resolved on the strength of
those fixes"), nunca culpa al cliente, nunca menciona otros clientes ni tickets ENG.

---

## El método de correo de J.R.

El correo **no es el reporte de estado**, el adjunto lo es. El correo trae solo lo que necesita
respuesta del cliente. Línea puente literal que usa: *"A few things I need from you directly,
separate from the tracker, because these are the ones that move fastest with an answer from
your side."*

Reglas que se leen de su texto:
1. Cada punto pide **una sola cosa concreta**: un nombre de reporte, una cifra, una prueba, un
   contacto. Nunca "por favor revisen".
2. Explica por qué está trabado del lado de ellos: *"That one is waiting on a test rather than
   on us."* Quita el tono de reclamo.
3. Separa lo que espera una prueba, lo que espera una decisión y lo que espera información.
4. Corrige errores del cliente sin fricción y ya aplicados: *"RCS-28047 is not one of your
   tickets. I believe you meant RCS-28407, and I have made that swap in the attached version."*
5. Explica el retraso con la razón real, sin excusas largas.
6. Cero jerga interna, ningún ingeniero por nombre, ningún ENG, ninguna rama, ningún ambiente.
7. Ofrece rutas, no promesas ni fechas comprometidas.

**Longitud: ~430 palabras, ítems de 2 a 4 frases.** Un correo largo con párrafos de 6 frases
no es su estilo y se vuelve ilegible. La prueba de que el formato funciona: James Cosseboom
respondió los once puntos, en orden, uno por uno, con capturas y adjuntos.

**Regla de higiene**: no repetir una pregunta que el cliente ya contestó. Es el error más
visible posible en este flujo.

Ver [[project_adusa_tracker_cliente_18ago]], [[project_adusa_ficha_y_tickets]].
