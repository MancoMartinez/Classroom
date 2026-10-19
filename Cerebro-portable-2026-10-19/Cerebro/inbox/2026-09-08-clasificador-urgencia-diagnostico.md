# Clasificador de urgencia de la cola, de 73% a 100%

Nota de sistema del Cerebro. No es la ficha de ningun ticket.

## Que pasa

`bin/eval_cola.py` marcaba 11 de 15 desde hacia semanas. `ESTADO.md` lo tenia escrito como deuda
tecnica del lexico de promesas y pedia dos decisiones de Juan antes de arreglarlo. El diagnostico
estaba equivocado en dos de los cuatro casos, y la causa de fondo no era el lexico.

## Causa

El set de etiquetas de `cola/EVAL-clasificador.json` caduca solo y nadie lo estaba mirando. Se fija
leyendo el ultimo comentario de cada ticket un dia concreto. Cada comentario nuevo que llega despues
deja esa etiqueta describiendo un momento que ya paso, y el medidor lo cuenta como fallo del codigo.

Las etiquetas se fijaron el 3 de septiembre. El volcado de Jira llegaba al 8. Seis tickets
recibieron comentarios en medio, y los cuatro fallos eran cuatro de esos seis. El propio archivo lo
advertia en su campo descripcion. Refrescar dos etiquetas subio la exactitud de 73% a 87% sin tocar
una linea de codigo.

## Que se hizo

Tres arreglos en `bin/cola.py`, cada uno medido contra el volcado real:

1. `cliente_devuelve_pelota()`. Si el ultimo mensaje del cliente trae compromiso propio o solo acuse
   de recibo, sin pregunta ni pedido, el ticket baja de nivel 1 a nivel 3. Antes cualquier palabra
   del cliente subia el ticket a "te toca responder". Decision de Juan del 8 de septiembre.
2. `sin_citas()`. Recorta el comentario en el primer bloque citado, cabecera de Outlook, firma o pie
   de portal. El lexico de promesas y pedidos se aplica solo a lo que Appriss escribio de su puño.
   Antes, un correo del cliente pegado dentro de un comentario se leia como palabras de Appriss.
3. `es_cliente()` por tres vias: cuenta de Jira Service Management, dominio del correo en el nombre
   visible, y lista manual para el resto. De los 33 autores sin cuenta de servicio en el volcado,
   uno solo era cliente real. Los otros 32 eran Appriss e ingenieria.

Resultado 15 de 15. La cola cambio de orden: el nivel uno bajo de dos tickets a uno, y el nivel
cuatro subio de nueve a diez.

## Lo que faltaba, y es lo que mas vale

Se agrego `bin/refrescar_eval.py`. Compara la fecha de fijado contra el ultimo comentario de cada
ticket y nombra las etiquetas vencidas antes de que nadie culpe al codigo. `bin/eval_cola.py` ahora
avisa solo y marca cada fallo que cae sobre una etiqueta vencida. El atajo de terminal es
`refrescar`. Sin esto, el mismo diagnostico equivocado vuelve en cuanto el volcado se actualice.

## Evidencia por caso

Lo que decia el documento contra lo que mostraba el volcado.

RCS-27941. Decia que Colton Neal no tiene cuenta de servicio y que su promesa se leia como promesa
de Appriss. Falso, si la tiene y el modelo lo leia bien. El 7 de septiembre Juan le pregunto y no ha
contestado, asi que nivel 3 es correcto y la etiqueta 1 estaba vencida.

RCS-28753. Decia que el unico comentario era un triage automatico descartado por interno. Falso, hay
once comentarios y el triage no se marca interno. Peyman respondio la pregunta del cliente el 8 de
septiembre, asi que nivel 4 es correcto y la etiqueta 2 estaba vencida. Este caso si expuso un
hueco real: el cliente Damir tiene cuenta ordinaria, no de servicio.

RCS-28289. Decia que el nivel 1 no tiene filtro lexico. Correcto. Joe Austin escribio el 8 de
septiembre que sigue trabajando de su lado y que avisa cuando sepa de IT. Se comprometio el, y el
ticket subia a nivel 1 igual.

RCS-27765. Decia que "we will be monitoring the thread" se leia como pedido al cliente. Otra causa.
Lo que disparaba era "do you have" dentro de "Do you have a request or problem", el pie de pagina
del portal de IT del cliente, pegado dentro del comentario de Appriss.

## Trampa de nombres, anotada

Este archivo se llamo primero con la palabra cola y un guion en el nombre, y el ingestor lo descarto
como foto de cola efimera. La regla acierta en 16 de 16 casos reales, asi que no se toco. Al nombrar
una nota sobre el sistema de cola, evita esa palabra seguida de guion en el nombre del archivo.
