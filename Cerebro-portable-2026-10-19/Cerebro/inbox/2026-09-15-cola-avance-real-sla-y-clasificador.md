# Cola 15 sep 2026, ajustes al clasificador y estado del dia

## Cambios en bin/cola.py hoy

1. avance_real / primera_toma / dias_desde_toma: recorre TODOS los comentarios de Juan en
   cada ticket, no solo el ultimo. Si ninguno trae una marca de sustancia (root cause, found,
   identified, reproduced, fix, deploy, query, attached log/screenshot, etc), avance_real
   queda False aunque el ticket lleve dias moviendose. dias_desde_toma cuenta desde el primer
   comentario de Juan en el ticket.
2. SLA_DIAS / sla_umbral(): techo de trabajo interno por prioridad, no contractual:
   critical/highest 1 dia, high 3, medium 7, low 14. Si avance_real es False y dias_desde_toma
   supera el techo, se agrega la alerta "SLA en riesgo". A confirmar con Juan si estos numeros
   sirven o hay que ajustarlos.
3. causa_de(): lee la seccion "## Causa" de tickets/<ticket>.md y reporta si esta confirmada,
   es hipotesis, esta registrada sin marca, o no existe. De los 19 tickets activos hoy, ninguno
   tiene esa seccion escrita en su ficha (aunque en el hilo de Jira si haya diagnostico, como el
   Kafka bridge de RCS-28756, que todavia no esta pasado a la ficha).
4. cliente_devuelve_pelota() corregido: agradecimientos con nombre propio en el saludo o la
   firma ("Hello Juan, Thank you for your assistance and updates. Regards, Tatiana Barcenas")
   inflaban el conteo de sustancia y no se reconocian como cierre puro. RCS-28294 fue el caso
   real. Se recorta el nombre del saludo y de la firma por posicion antes de medir.
5. pedido_tapado: si el ultimo comentario publico es un cierre puro del cliente, se revisa el
   comentario publico inmediatamente anterior. Si es de otra persona, te menciona por nombre y
   trae un pedido, ese pedido manda, no el cierre. Cubre el caso donde alguien te pregunta algo
   y despues el cliente cierra con un agradecimiento generico que no responde nada.

## Eval

exactitud 11/12 = 92%, un solo caso fallado y documentado: RCS-28294. Shandana Khan (Appriss)
escribio el 15 sep 02:58 "Please clarify how the Claude analysis provided is related to the
issue the client is now reporting... please ensure any new issues are raised as separate
tickets", sin mencionar a Juan por nombre en ese comentario puntual. pedido_tapado exige mencion
directa por nombre para no generar falsos positivos, y aqui no la hay, asi que el clasificador
sigue viendo el cierre de Tatiana como la ultima palabra y da nivel 3. Gold quedo en nivel 1
porque la realidad es que Juan le debe esa aclaracion a Shandana. Hueco conocido, no bloqueante.

## Cola de hoy, 19 tickets: nivel1=1 nivel2=1 nivel3=9 nivel4=8

Ver cola/estado.json y cola/COLA.md para el detalle fila por fila. Resumen de la respuesta dada
en el chat: accion hoy (RCS-28911, RCS-28871, RCS-28294 por hallazgo manual, mas los TRABAJADO
SIN PEGAR), cluster de escalamiento (RCS-27676, RCS-28122, RCS-28282, RCS-28496, cuatro Under
Customer Review de 24 a 48 dias sin diagnostico propio nunca escrito), cluster por cliente
Blain's (RCS-28122 + RCS-28351), cluster por cliente Ahold-Delhaize (RCS-28911 + RCS-28281 +
RCS-28342), cluster por cliente CWH (RCS-28581 + RCS-28099), y el bloque under customer sano sin
accion (RCS-28289, RCS-28240, RCS-28351, RCS-27941).
