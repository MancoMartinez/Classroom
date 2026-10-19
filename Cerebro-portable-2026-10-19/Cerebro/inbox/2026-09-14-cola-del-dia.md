# Cola del 14 sep 2026, con diff contra el 11 sep y contexto de conversaciones previas

19 tickets abiertos, los mismos 19 del viernes. Niveles 1=2, 2=3, 3=9, 4=5. Clasificador en
13/13 tras corregir un bug de fondo: el 14 por ciento de los comentarios de Jira traen
apostrofe curvo, Outlook o iOS lo autocorrigen, y todo el lexico de contracciones usaba
apostrofe recto. RCS-28753 se colo asi el 14 sep, "I'll reach out" con comilla curva no
se veia como cierre del cliente. Corregido en bin/cola.py normalizando comillas y guiones
antes de aplicar el lexico. Backup en bin/cola.py.bak-20260911.

## Cambios desde el viernes 11

Tres tickets con comentario nuevo durante el fin de semana o el lunes.

    RCS-27765  4 -> 1. Winn-Dixie. Shireesh reenvio el 12 sep la pregunta del cliente:
               dejaron el archivo en la cola el 11 sep y piden confirmar si llego
    RCS-28756  4 -> 1. Nike ECOM. Ayesha volvio a insistir hoy pidiendo update
    RCS-28753  4 -> 3. Nike Manual Discount. Damir dijo que por ahora cierran y que
               el escribe si sale algo mas. Pelota del cliente

Los otros 16 no tuvieron actividad nueva.

## Lo que quema hoy, con el contexto que ya existe en la base

**RCS-27765, Winn-Dixie.** Verificar en el servidor si el archivo que el cliente dijo que
reenviaba el 9 sep llego. Shireesh ya reenvio la pregunta dos veces. Respuesta corta y cierra.

**RCS-28756, Nike ECOM.** No responder a Nike todavia. El 11 sep aparecio evidencia de que la
respuesta que ya se le envio a Nike el 10 sep esta mal en tres de cinco puntos. ENG-4235
documenta un consumer Kafka de Appriss, prd-datacloud-kafka-ingest-wus2, entre Nike y el
Event Hub. El corte pudo ser del lado de Appriss, no de Nike. Hay un mensaje de Teams a
Nichols Turner esperando respuesta desde el 9 sep, listo en
inbox/2026-09-11-rcs-28756-kafka-bridge.md. Tu ultima palabra a Ayesha, el 11 sep, fue que
sigues esperando al equipo responsable. Eso sigue siendo cierto hoy. Si Nichols no ha
contestado, la accion es insistirle a el, no a Ayesha.

**RCS-28342, Ahold-Delhaize.** 9 dias de promesa sin cumplir, la mas vieja de las tres.
Sin comentario nuevo desde el viernes.

**RCS-27676, RLC.** 41 dias sin que el cliente oiga nada de Appriss. Sigue siendo el mas
expuesto de toda la cola. Sin movimiento.

## Cola completa

    1  RCS-27765  Winn-Dixie          Shireesh te pidio, 2 dias
    1  RCS-28756  Nike ECOM           Ayesha te pidio, 0 dias
    2  RCS-28342  Ahold-Delhaize      prometiste, 9 dias
    2  RCS-28294  Vallarta            prometiste, 3 dias
    2  RCS-28871  Walgreens           prometiste, 3 dias
    3  RCS-27676  RLC                 41 dias sin respuesta
    3  RCS-28122  Blain's             25 dias
    3  RCS-28282  Co-op               23 dias
    3  RCS-28496  PVH                 23 dias
    3  RCS-28289  Vitamin Shoppe      19 dias, Joe Austin no volvio
    3  RCS-28240  United Supermarkets 5 dias
    3  RCS-28351  Blain's             5 dias
    3  RCS-27941  Tailored Brands     3 dias
    3  RCS-28753  Nike                cliente cerro, 3 dias
    4  RCS-28099  CWH                 27 dias, muerto
    4  RCS-27791  Guess               11 dias
    4  RCS-28581  CWH                 10 dias
    4  RCS-28281  Ahold               6 dias
    4  RCS-28256  Appriss Incident    5 dias

## Compromisos

Verificar si Nichols Turner respondio el mensaje de Teams del 9 sep sobre RCS-28756.
Sigue abierta la decision sobre partir el nivel 4 y sobre el override de bitacora.
