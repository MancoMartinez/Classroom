---
fecha: 2026-09-02
origen: sesion local_cb6e90fd, "Cerebro cola manana", 2 sep 2026
tipo: correccion de proceso
estado: sin aprobar para la base
---

# El clasificador de cola cayo a 54% y la causa no es el lexico

## Lo medido

`bin/eval_cola.py` marca 7 de 13. Exactitud 54%.

Los seis fallos son exactamente los seis tickets cuyo ultimo comentario cambio despues del 24 de
agosto, la fecha en que se fijaron las etiquetas de referencia a mano:

RCS-27941, RCS-27765, RCS-28289, RCS-28327, RCS-28123, RCS-28256.

Cada uno tiene explicacion:

- RCS-27941, RCS-27765 y RCS-28289: Juan ya los contesto.
- RCS-28327: Juan cumplio la promesa el 28 de agosto.
- RCS-28123: Matthew Kamminga lo movio el 1 de septiembre.
- RCS-28256: Juan mando recordatorio el 1 de septiembre.

El orden de la cola quedo bien. Solo el set de referencia esta viejo.

## La correccion al contrato

`CLAUDE.md` dice hoy: "Si la exactitud baja de 100%, el lexico se desactualizo y la cola puede estar
mal ordenada."

Eso es falso en este caso y ya se midio. La exactitud bajo porque el set de referencia envejecio,
no porque el lexico fallara. Un set de etiquetas fijado a mano el 24 de agosto caduca cada vez que
Juan responde un ticket del set.

Redaccion propuesta para `CLAUDE.md`:

Si la exactitud baja de 100%, revisa primero la fecha del ultimo comentario de cada ticket que
fallo. Si el comentario cambio despues de la fecha en que se fijaron las etiquetas, el set de
referencia caduco y hay que refijarlo contra el volcado de hoy. Solo si los fallos son de tickets
sin movimiento, el lexico se desactualizo.

## Accion pendiente

Refijar el set de referencia de `bin/eval_cola.py` contra el volcado del 2 de septiembre. Sin eso,
cada corrida diaria va a reportar una degradacion que no existe.

## Dato de reasignacion

RCS-28638 Myer Australia salio de la cola de Juan hacia Sebastian Garces. Sigue abierto. La bitacora
del 31 de agosto con el refresco de enumeraciones nunca se pego en Jira, asi que Garces arranca sin
ese contexto. Esa reasignacion es una de las dos razones por las que Garces amanece en 7 abiertos
contra un techo de 5.
