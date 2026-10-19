# Cola de Juan, refresco de la manana, 31 ago 2026

Generado 2026-08-31T10:02 desde Jira en vivo. Comparado contra el estado del 28 ago 17:05.

## Alerta de clasificador

Exactitud del clasificador 8/12 = 67 por ciento contra las etiquetas fijadas el 24 ago. Bajo de 100.
El lexico de promesas quedo corto en una frase nueva. Detalle abajo, en Verificacion.

## Que cambio desde el viernes

Nadie escribio de ningun lado durante el fin de semana. Cero tickets nuevos, cero cerrados, cero
cambios de nivel por actividad real. Los 16 tickets de la cola son los mismos del 28 ago. Todos
envejecieron dos o tres dias por el fin de semana, eso es lo unico que se movio.

Conteo: nivel 1 = 1, nivel 2 = 3, nivel 3 = 6, nivel 4 = 6.

Nivel 2 incluye RCS-28327 por correccion manual. El clasificador lo puso en nivel 4, la etiqueta de
referencia y la lectura directa del comentario en Jira dicen nivel 2. Ver Verificacion.

## Nivel 1, te toca responder

RCS-28093, Ahold, Employees not restricted by Store location. leighann.stubbs@adusa.com escribio
hace 3 dias, nadie de Appriss contesto. Ultimo texto de ella: "I am not sure what it will take to do
that but I have copied April on this message to see if it's a possibility."

## Nivel 2, promesa sin cumplir

RCS-28123, ADUSA, Case assignment issues. Prometiste un update hace 4 dias, no llego. Ultimo texto
tuyo: "The missing confirmation and print option is a separate issue. I have logged it, and
engineering is reviewing it now. I will update you as soon as possible."

RCS-28581, CWH, POS Number has regressed to previous mapping. Prometiste un update hace 3 dias, no
llego. Ultimo texto tuyo: "I have taken ownership of this ticket and will be investigating it for
you. Please allow some time for me to research the issue and I will get back with you."

RCS-28327, Delhaize, Loyalty Discounts not Specified. Correccion manual, ver Verificacion. Ultimo
texto tuyo, 27 ago: "I have nothing confirmed yet on the cause and I am not going to give you one
until I do. I will come back to you when I have it. I need nothing from you at this point."
Prometiste, y llevas 4 dias sin volver.

## Nivel 3, esperando al cliente, una linea cada uno

RCS-27676, RLC SFTP IP change, 26 dias esperando. Alerta: el cliente no oye nada de Appriss hace 26
dias.

RCS-27959, PACSUN IP whitelisting, 18 dias esperando. Alerta: el cliente no oye nada de Appriss hace
18 dias.

RCS-28122, Blain's, cambios de usuario, 11 dias esperando. Alerta: el cliente no oye nada de Appriss
hace 11 dias.

RCS-28282, Co-op, notificacion de acceso bloqueado, 9 dias esperando. Alerta: el cliente no oye nada
de Appriss hace 9 dias.

RCS-28496, PVH, fallas de login, 9 dias esperando. Alerta: el cliente no oye nada de Appriss hace 9
dias.

RCS-28256, Appriss Incident, timeouts y carga lenta, 5 dias esperando. Sin alerta de silencio.
Verificado en Jira, el comentario mezcla un pedido al cliente con una promesa de avisar cuando salga
un fix. Revisalo cuando llegues a nivel 3, puede subir a nivel 2 si el fix ya salio.

## Nivel 4, en movimiento interno o trabajado sin pegar, una linea cada uno

RCS-28153, BYF, errores y logout de usuarios, trabajado sin pegar en Jira. Alerta: el cliente no oye
nada de Appriss hace 19 dias.

RCS-28099, CWH, HYP a RCS logica de descuento, en movimiento interno. Alerta: el cliente no oye nada
de Appriss hace 12 dias.

RCS-28289, Vitamin Shoppe, usuarios bloqueados, en movimiento interno, esperando que Scott vuelva de
vacaciones. Sin alerta.

RCS-27765, Winn-Dixie, chequeo de archivo de datos, en movimiento interno. Sin alerta.

RCS-28482, AHL/DLZ, campos en gris en Izenda, trabajado sin pegar en Jira. Sin alerta.

RCS-28638, Myer Australia, mapeo de Proof Type ausente, trabajado sin pegar en Jira. Sin alerta.

## Verificacion del clasificador

`bin/eval_cola.py` dio 8 de 12 contra el fixture del 24 ago. Fui a Jira a leer los cuatro casos
completos antes de mostrar la cola.

RCS-28327 es un hueco real del lexico. Tu comentario del 27 ago dice "I will come back to you when
I have it." El lexico de promesas no reconoce esa frase, solo variantes de "I will update you".
Movi este ticket a nivel 2 a mano. Hay que sumar la frase al lexico de `bin/cola.py`.

RCS-28256 es senal mixta, no error del lexico. El comentario pide al cliente que pruebe algo y
tambien promete avisar cuando salga un fix. El clasificador eligio esperando al cliente, la
etiqueta de referencia esperaba promesa. Ambas lecturas son defendibles, lo deje en nivel 3 y lo
marque para revision.

RCS-28289 y RCS-27765 no son errores del lexico. La etiqueta del 24 ago se fijo antes de que
contestaras esos tickets. Ya contestaste los dos el 25 ago, el ultimo humano de cara al cliente
ahora eres tu, nivel 1 ya no aplica a ninguno de los dos. El fixture quedo desactualizado por el
paso del tiempo, no por un lexico roto.

Neto, un solo caso pide cambio de codigo en `bin/cola.py`. Los otros tres son ruido esperado de un
fixture fijo contra tickets que se mueven.

## Recomendacion

Empieza por RCS-28093. Es el unico ticket donde el cliente esta esperando tu respuesta directa, sin
nadie de Appriss de por medio, y ya lleva 3 dias. Los de nivel 2 son promesas atrasadas y pueden
esperar unas horas mas. Los de nivel 3 dependen del cliente, no de vos.
