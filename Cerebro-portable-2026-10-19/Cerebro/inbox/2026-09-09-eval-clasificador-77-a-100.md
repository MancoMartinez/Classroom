# Clasificador de cola: de 77% a 100%, tres causas distintas

Fecha: 2026-09-09. Disparador: `bin/eval_cola.py` marco 10/13 y el diagnostico automatico
atribuyo dos de los tres fallos a etiquetas vencidas. Solo uno lo era.

## Que pasa

La exactitud cayo a 77% con tres fallos: RCS-28753, RCS-27941, RCS-28294. Ninguno tenia la
misma causa. Tratarlos como un solo problema de lexico habria roto casos que funcionaban.

## Causas, confirmadas las tres

1. Etiqueta vencida real, RCS-28753. Gold 4 fijado el 8 sep sobre la respuesta de Peyman
   Motlagh. El 9 sep Madhuraj Gujaran acuso recibo a Damir y prometio que un ingeniero
   vuelve. Nivel real hoy: 2. El modelo ya daba 2.

2. Bug de borde en `bin/refrescar_eval.py`. Comparaba `fecha > fijado` sobre la fecha sola.
   Un comentario que llega el mismo dia del sellado, despues de sellar, quedaba invisible.
   RCS-28294 se colo por ahi: gold 1 del 8 sep, comentario de Juan del 8 sep sin detectar.

3. Fallo real del lexico `PREGUNTA` en `bin/cola.py`. Dos peticiones al cliente sin formula
   de cortesia no matcheaban ningun patron y los tickets caian a nivel 4 con la pelota del
   cliente encima.
   RCS-27941: "You can ask Beverly to close and log in again, also clear browser data".
   RCS-28294: "I wanted to confirm if you could try clearing all Chrome browsing data".

## Evidencia

    exactitud 10/13 = 77%   antes
    exactitud 13/13 = 100%  despues
    niveles antes:   1=0 2=3 3=5 4=11
    niveles despues: 1=0 2=3 3=6 4=10

## Que se cambio

`bin/cola.py`, lexico PREGUNTA, cuatro patrones nuevos:
`if you (could|can)`, `you can (ask|try|clear|close|check|log|have)`,
`try (clearing|again|once more|logging)`, `retry`.

Descartado en la misma sesion: `i wanted to confirm`. Subio RCS-27791 a nivel 3 siendo un
cierre, no un pedido. La distincion que importa es "wanted to confirm THAT everything works"
contra "wanted to confirm IF you could try". El patron `if you could` separa las dos.

`bin/refrescar_eval.py`, tres cambios: compara timestamp completo con `cola.parse_fecha`,
no la fecha sola; el sello `--fijar` guarda hora con zona, no solo el dia; acepta sellos
viejos de 10 caracteres.

`cola/EVAL-clasificador.json`, tres golds corregidos y resellado en 2026-09-09T17:36:45-04:00.

Backups: `bin/cola.py.bak-20260909`, `bin/refrescar_eval.py.bak-20260909`,
`cola/EVAL-clasificador.json.bak-20260909`.

## Precedente

El 8 sep 2026 paso lo contrario: 73% con dos de cuatro fallos por etiquetas vencidas, y el
diagnostico equivocado vivio semanas en ESTADO.md como deuda tecnica. La leccion no es que
las caidas sean siempre calendario. Es que hay que separar los fallos uno por uno antes de
tocar el lexico.

## Compromisos

Actualizar ESTADO.md con la exactitud del 9 sep y la nota del sello con hora.
