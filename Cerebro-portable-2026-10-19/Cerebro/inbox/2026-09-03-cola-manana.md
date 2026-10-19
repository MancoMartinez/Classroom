# Cola de la mañana, 2026-09-03

## Aviso primero

La exactitud del clasificador cayo a 58%, 7 de 12 casos etiquetados. El lexico de promesas y de
preguntas se desactualizo. La cola de abajo puede estar mal ordenada, sobre todo en el limite entre
nivel 1 y nivel 2. Fallas concretas del eval:

RCS-28123 esperaba nivel 2, dio nivel 1. Evidencia: Matthew Kamminga prometio seguir investigando
sin fecha.
RCS-28327 esperaba nivel 2, dio nivel 4. Misma causa, promesa de update sin fecha.
RCS-27941 esperaba nivel 1, dio nivel 4. RCS-28289 esperaba nivel 1, dio nivel 4. RCS-27765
esperaba nivel 1, dio nivel 4. Estos tres ya tienen respuesta de Juan mas reciente que la del
cliente segun Jira. Revisalos a mano antes de confiar en el nivel 4.

## Que cambio desde ayer

RCS-27791 bajo de nivel 1 a nivel 4. Juan le respondio a Stephanie Benedetti ayer a las 13:44.

RCS-27941 quedo en nivel 4. Juan le respondio a Colton Neal ayer a las 17:55 con la causa raiz
completa del problema de permisos.

RCS-28123 volvio a subir. Juan comento de madrugada hoy a las 00:55. Leighann Stubbs, la cliente de
ADUSA, respondio hoy a las 08:38 con una pregunta puntual sobre las notificaciones de asignacion de
casos. El ticket lleva 31 dias abiertos y Matthew Kamminga dejo una promesa sin fecha el 1 de
septiembre.

RCS-28294 sigue en nivel 1. Tatiana Barcenas escribio ayer a las 16:55 confirmando que van a seguir
usando Internet Explorer.

RCS-28671 se mantiene en nivel 4 pero con alerta activa. Manisha Naik, ingenieria interna, escribio
hoy a las 06:24 con la consulta de logs que pediste. Te menciono por nombre.

El total bajo de 18 tickets a 17. El respaldo completo del estado de ayer no quedo guardado antes
de correr el clasificador de hoy, asi que no puedo decir con certeza cual ticket salio de la cola.
Verifica el conteo en Jira si te hace falta ese dato.

## Nivel 1, te toca responder (2)

RCS-28123, ADUSA, Case assignment issues. Motivo: Leighann Stubbs escribio hace 0 dias y nadie de
Appriss contesto. Edad del ticket 31 dias. Ultimo movimiento: "I was informed that as of late
Monday afternoon, the notification to the newly assigned person to a case is not receiving the
notification email. I did attach an email that they used to receive, dated back from 8/14. I am
still looking into this but wanted to see if you knew anything about this."

RCS-28294, Vallarta, Smart Alerts no Triggering. Motivo: Tatiana Barcenas escribio hace 0 dias y
nadie de Appriss contesto. Edad del ticket 22 dias. Ultimo movimiento: "Hi Juan, Thank you, we will
continue to use Internet Explorer. Regards, Tatiana Barcenas."

## Nivel 2, promesa sin cumplir (0)

Vacio segun el clasificador. El eval marca esto como sospechoso. RCS-28123 y RCS-28327 traen
promesas de update sin fecha y el clasificador los movio a otros niveles. Tratalos como nivel 2 en
la practica hasta que se corrija el lexico.

## Nivel 3, esperando al cliente (5)

RCS-27676, RLC, SFTP IP/Hostname Change, 29 dias sin respuesta. Alerta: el cliente no oye nada de
Appriss hace 29 dias.
RCS-27959, PACSUN, IP Whitelisting para MuleSoft, 21 dias sin respuesta. Alerta: 21 dias.
RCS-28122, Blain's, cambios de usuario bloqueados, 14 dias sin respuesta. Alerta: 14 dias.
RCS-28496, PVH, fallas de login en tiendas, 12 dias sin respuesta. Alerta: 12 dias.
RCS-28282, Co-op, bloqueo intermitente al ver transacciones, 12 dias sin respuesta. Alerta: 12 dias.

## Nivel 4, movimiento interno o trabajado sin pegar (10)

RCS-28153, BYF, errores y logout forzado, fix confirmado y liberado en ENG-7184, falta pegar en
Jira. Alerta: 22 dias.
RCS-28099, CWH, logica de descuento Item Discount, sin nada pendiente de cara al cliente. Alerta:
15 dias.
RCS-28289, Vitamin Shoppe, usuarios bloqueados, esperando a que Scott vuelva de vacaciones. Alerta:
8 dias.
RCS-27765, Winn-Dixie, revision de archivo de datos, hilo de correo se partio, ya corregido con IT.
Alerta: 8 dias.
RCS-28482, AHL/DLZ, campos en gris en Izenda, reporte corre bien y solo falla la edicion, sin
hallazgo tecnico nuevo. Alerta: 7 dias.
RCS-28327, Delhaize, descuentos de lealtad no especificados, causa raiz propuesta es el workbook de
enumeraciones CRDM 2.0 faltante para el cliente 46. Sin alerta.
RCS-28581, CWH, numero de POS regreso al mapeo anterior, investigacion arrancada sobre DO-9495. Sin
alerta.
RCS-28671, THD, busquedas solo dan error, reabierto por Corey Wood tras el cierre del 1 de
septiembre, Manisha aporto el WI 248159 hoy. Alerta: Manisha Naik te menciono directo.
RCS-27941, Tailored Brands, permisos de SSO en Incident, causa raiz entregada, falta que el cliente
ajuste el CaseType. Sin alerta.
RCS-27791, Guess, pregunta de auditoria en Grid Style, Juan confirmo el cambio y espera
confirmacion del cliente. Sin alerta.

## Recomendacion

Empieza por RCS-28123. Es el ticket mas viejo de los dos en nivel 1, arrastra una promesa sin fecha
de Matthew Kamminga y Leighann acaba de preguntar algo puntual sobre las notificaciones de
asignacion. RCS-28294 solo necesita un acuse de recibo breve, resuelvelo despues.
