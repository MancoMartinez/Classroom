Bug real encontrado al revisar la cola del 21 sep. bin/cola.py comparaba la fecha de la bitacora contra la fecha del ultimo comentario de Jira usando solo el dia, sin hora. Cuando Juan anotaba en bitacora el mismo dia que el ultimo comentario, el override de TRABAJADO SIN PEGAR EN JIRA se disparaba sin importar si ese comentario llego antes o despues de la nota.

Caso real de hoy: RCS-28294. Juan le respondio a Tatiana Barcenas a las 13:00 confirmando el fix. Tatiana contesto a las 15:36 con una pregunta directa, si el fix aplica a todas las smart alerts. La bitacora tenia una entrada del mismo 21 sep, escrita antes de esa respuesta, y el clasificador la usaba para tapar la pregunta de Tatiana como si ya estuviera resuelta. El ticket aparecia en nivel 4 cuando en realidad es nivel 1, pregunta de cliente sin contestar.

Mismo problema al reves con RCS-28871, tapaba una promesa real de Juan a Shreedhar sobre stress testing, abierta desde el 15 sep y todavia sin contestar por Infra.

Arreglo en bin/cola.py: bitacora_de ahora lee la hora que bin/anotar deja entre parentesis al final de cada nota, por ejemplo (16:25). clasificar_final compara fecha y hora completas contra el ultimo comentario, no solo la fecha. Si una nota no tiene hora porque se escribio a mano sin pasar por bin/anotar, se asume 00:00 de ese dia en vez de fin de dia, para no tapar de mas.

Efecto en la cola de hoy: RCS-28294 subio a nivel 1 correcto. RCS-28871 subio a nivel 2, promesa sin cumplir, correcto. Eval quedo en 100 por ciento, 6 de 6, con las dos etiquetas de RCS-28294 y RCS-28756 actualizadas a lo que paso hoy.

Backup del archivo anterior en bin/cola.py.bak-20260921 por si algo se rompe.
