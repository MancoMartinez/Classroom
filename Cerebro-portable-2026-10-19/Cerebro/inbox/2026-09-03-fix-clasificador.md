# Arreglo del clasificador de cola, 2026-09-03

Se hicieron tres cambios en bin/cola.py y bin/eval_cola.py, los tres ya corridos y verificados
contra el volcado de hoy.

## 1. Hueco real de lexico

RCS-28289 traia el comentario "I'll be waiting for the update once Scott is back" y el clasificador
lo mandaba a nivel 4 en vez de nivel 3. El patron `i'?ll wait for` no cubria la forma progresiva
con "be" en medio. Se agregaron a PREGUNTA: `i'?ll be waiting`, `i will be waiting`,
`we'?ll be waiting`, `we will be waiting`, `still waiting (to hear|for|on)`. RCS-28289 ya clasifica
nivel 3.

## 2. El eval no probaba el pipeline completo

eval_cola.py llamaba a clasificar() directo, sin pasar por el override de bitacora que main()
si aplica. RCS-28581 tiene bitacora del 31 de agosto posterior a su ultimo comentario en Jira, asi
que el pipeline real lo manda a nivel 4, TRABAJADO SIN PEGAR. El eval, saltandose el override,
media un nivel 2 que nunca sale en la cola real. Se extrajo clasificar_final() en cola.py, que
junta clasificar() mas el override de bitacora, y main() y eval_cola.py usan la misma funcion
ahora. No hay forma de que el eval y la cola real diverjan de nuevo por esto.

## 3. EVAL-clasificador.json refrescado

Las 19 etiquetas venian fijadas el 24 de agosto. De los 19 tickets, dos ya cerraron y el resto
llevaba en promedio mas de una semana de comentarios nuevos que el eval no reflejaba. Se releyeron
a mano, desde el volcado crudo, los ultimos comentarios publicos, no bot y no internos, de los 17
tickets abiertos hoy, y se fijaron 17 etiquetas nuevas con fecha 2026-09-03.

Exactitud despues del refresco y los dos arreglos: 17 de 17, 100 por ciento.

## Como sigue esto envejeciendo

El eval vuelve a caer solo con el paso de los dias, a medida que lleguen comentarios nuevos sobre
los 17 tickets de hoy. Eso es lo esperado, no una alarma de lexico roto. Antes de tocar el lexico
por una falla del eval, lee el comentario real del ticket en Jira. Si Juan ya respondio despues de
la fecha de la etiqueta, refresca la etiqueta. Si el comentario sigue siendo el mismo y el nivel
esta mal, ahi si es lexico.
