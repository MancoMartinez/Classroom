# Cola actualizada, tarde 2026-09-03

Generado 18:00 hora Colombia. 17 tickets. Niveles 1=2, 2=1, 3=5, 4=9.

## Que cambio desde la corrida de la manana

RCS-28123 y RCS-28482 salieron de la cola, ya no estan abiertos en RCS.
RCS-27941 volvio a nivel 1. Colton Neal escribio hoy: "I will work on this and get back to you
next week sometime." Tecnicamente hablo el cliente de ultimo, aunque el mismo dijo que va a
tardar en volver.
RCS-28753 entro nuevo, Nike, logica del campo Manual Discount Amount, prioridad alta. Nivel 2
porque el ultimo comentario es la respuesta automatica de triage, que el clasificador lee como
promesa de seguimiento.
RCS-28756 entro nuevo, Nike, ECOM Load issue desde el 28 de agosto, reportado por Ganesh Nayak
desde Teams.

## Nivel 1, te toca responder (2)

RCS-28294, Vallarta, Smart Alerts. Tatiana Barcenas escribio hace 1 dia, "we will continue to use
Internet Explorer".
RCS-27941, Tailored Brands, permisos SSO. Colton Neal escribio hoy diciendo que el va a trabajar en
esto y vuelve la semana entrante. Un acuse corto cierra el ciclo aunque la pelota quedo del lado
de el.

## Nivel 2, promesa sin cumplir (1)

RCS-28753, Nike, Manual Discount Amount, prioridad alta, ticket de hoy. Lo unico que hay es la
respuesta automatica de triage. No es una promesa incumplida real todavia, es un ticket nuevo sin
asignar de fondo.

## Nivel 3, esperando al cliente (5)

RCS-27676 RLC, 30 dias. RCS-27959 PACSUN, 22 dias. RCS-28122 Blain's, 15 dias. RCS-28282 Co-op, 13
dias. RCS-28496 PVH, 12 dias.

## Nivel 4, movimiento interno o trabajado sin pegar (9)

RCS-28153 BYF fix liberado, falta pegar. RCS-28099 CWH sin deuda. RCS-27765 Winn-Dixie hilo
corregido. RCS-28289 Vitamin Shoppe esperando a Scott. RCS-28581 CWH investigacion activa. RCS-28327
Delhaize causa raiz en validacion. RCS-27791 Guess a la espera de confirmacion. RCS-28756 Nike ECOM
recien llegado. RCS-28671 THD reabierto, Manisha te menciono hoy con el WI 248159.

## Diagnostico del eval, no arreglar el lexico todavia

Las tres fallas de hoy, RCS-28289, RCS-28327 y RCS-27765, no son lexico desactualizado. Son
etiquetas de EVAL-clasificador.json congeladas el 24 de agosto. En los tres, Juan respondio despues
de esa fecha y el nivel de hoy es el correcto. El eval compara contra un estado que ya no existe.

Hallazgo real sobre el lexico, aparte del eval: RCS-28289 tiene el comentario "I'll be waiting for
the update once Scott is back", que deberia caer en nivel 3, esperando al cliente. El patron
`i'?ll wait for` no matchea "I'll be waiting for" por el "be" en medio. Es un hueco chico y real,
no el que senala el eval.

Dos caminos para avanzar, no excluyentes:
1. Refrescar EVAL-clasificador.json con el estado de hoy, para que el eval vuelva a medir algo
   real.
2. Ampliar el patron de espera en bin/cola.py para cubrir "will be waiting", "still waiting to
   hear", y variantes con "be" en medio del verbo.
