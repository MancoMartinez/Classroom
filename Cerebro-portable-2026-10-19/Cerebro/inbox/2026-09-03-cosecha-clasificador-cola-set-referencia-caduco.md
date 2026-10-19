---
fecha: 2026-09-03
fuente: cosecha de sesiones locales, cerebro-asignacion-diaria
sesiones: local_163435f0-f1b9-4578-a268-6b8e0c17a2bd, local_b0e30963-ebac-4f46-a165-1db9db4a9b79
---

# Clasificador de cola, exactitud cayo y el set de referencia envejecio

Dos corridas independientes del 2 de septiembre midieron el clasificador de `bin/cola.py` por
debajo del 100% esperado. La corrida de la asignacion diaria marco 54%. La corrida de "cerebro cola
manana" marco 58% en otra medicion el mismo dia. Los dos numeros vienen de conjuntos de prueba
distintos, no se promedian.

La causa medida no es el lexico desactualizado. Los seis fallos de la corrida de 54% son los seis
tickets cuyo ultimo comentario cambio despues del 24 de agosto. El set de referencia fijado a mano
quedo viejo, no el lexico de promesas.

`CLAUDE.md` dice hoy: "Si la exactitud baja de 100%, el lexico se desactualizo y la cola puede estar
mal ordenada." Esa frase queda contradicha por la medicion de hoy. Hace falta corregirla para que
diga que la primera sospecha es el set de referencia, no el lexico, y confirmar el lexico aparte.

Corregir esto en `CLAUDE.md` necesita la aprobacion de Juan antes de tocar el archivo.

## Cambios de estado que la corrida de cola manana encontro y no pudo cerrar del todo

Total de la cola bajo de 18 a 17 tickets. La sesion no pudo confirmar cual ticket salio porque el
estado de ayer se sobreescribio antes de guardar copia. Vale corregir el script para que guarde
respaldo del estado anterior antes de sobreescribir.

Movimientos verificados ese dia:

RCS-27791 bajo de nivel 1 a nivel 4, Juan ya le respondio a Stephanie.
RCS-27941 quedo resuelto de cara al cliente con la causa raiz enviada.
RCS-28123 volvio a subir a nivel 1, Leighann de ADUSA pregunto algo puntual el 2 de septiembre a las
08:38.
RCS-28294 sigue en nivel 1, Tatiana escribio la tarde del 1 de septiembre.
RCS-28671 tiene mencion directa de Manisha Naik la mañana del 2 de septiembre.

La corrida tambien senalo que el limite entre nivel 1 y nivel 2 no es confiable ese dia. Nivel 2
salio vacio pero RCS-28123 y RCS-28327 traian promesas sin fecha que deberian caer ahi.
