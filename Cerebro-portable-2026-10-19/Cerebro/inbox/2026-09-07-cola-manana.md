# Cola del 2026-09-07, refresco de la mañana

Comparado contra el corte anterior del 2026-09-04.

## Exactitud del clasificador

El eval dio 93 por ciento, 13 de 14. El lexico se desactualizo. La cola puede estar mal ordenada en el margen.

Falla puntual en RCS-27765. El clasificador lo puso en nivel 3, esperando al cliente. El caso etiquetado a mano espera nivel 4, movimiento interno. El comentario relevante dice "the email has been replied to and we will be monitoring the thread". El lexico de promesas y de cierre no reconoce esa frase como respuesta ya dada. Revisa RCS-27765 a mano antes de confiar en su nivel.

## Que cambio desde el corte anterior

La cola bajo de 18 a 16 tickets. Dos salieron por cierre o resolucion, RCS-28327 y RCS-28671. Ninguno de los 16 tickets actuales es nuevo, todos venian del corte anterior.

RCS-28482 subio de nivel 4 a nivel 1. Jim Cosseboom escribio de vuelta durante el fin de semana. Confirma que los tabs quedaron corregidos y avisa que los campos se borraron, va a reconstruir los dos reportes el mismo. Te toca responder.

RCS-28756 tiene ahora a Juan Martinez como ultimo autor en Jira, con el comentario interno que la bitacora del 4 sep dice que redactaste. El clasificador lo sigue marcando TRABAJADO SIN PEGAR EN JIRA. Verifica si ese comentario ya quedo pegado. Si es asi, corre bin/anotar o confirma para que el proximo corte lo reclasifique en base a Jira solamente.

Ningun otro ticket recibio comentario nuevo de cliente. El resto de los movimientos son solo envejecimiento de silencio.

## Nivel 1, te toca responder (3)

RCS-28294, Vallarta, Smart Alerts no Triggering, prioridad Medium.
Motivo: Tatiana Barcenas escribio hace 4 dias y nadie de Appriss contesto.
Ultimo movimiento: "Hi Juan, Thank you, we will continue to use Internet Explorer. Regards, Tatiana Barcenas"
Alertas: ninguna.

RCS-27941, Tailored Brands, SSO/Permissions Issues in Incident, prioridad Medium.
Motivo: Colton Neal escribio hace 3 dias y nadie de Appriss contesto.
Ultimo movimiento: "Thanks Juan, I will work on this and get back to you next week sometime. Thanks again,"
Alertas: ninguna.

RCS-28482, AHL/DLZ, Greyed out fields in Izenda, prioridad Low.
Motivo: Jim Cosseboom escribio hace 1 dia y nadie de Appriss contesto.
Ultimo movimiento: "It looks like the greyed out tabs are corrected but the fields have mostly been deleted so I will rebuild both reports"
Alertas: ninguna. Subio de nivel 4 a nivel 1 en este corte.

## Nivel 2, promesa sin cumplir (1)

RCS-28753, Nike, Logic for Manual Discount Amount field, prioridad High.
Motivo: Ayesha Mehar prometio un update hace 2 dias y no llego.
Ultimo movimiento: "Hello @damir.demirovic@nike.com , Thank you for your communication. The engineer assigned to this ticket, or another team member, will get back to you just as quickly as possible"
Alertas: ninguna.

## Nivel 3, esperando al cliente (7)

RCS-27676, RLC, SFTP IP/Hostname Change, 33 dias sin respuesta. Alerta: el cliente no oye nada de Appriss hace 33 dias.
RCS-27959, PACSUN, IP Whitelisting MuleSoft, 25 dias sin respuesta. Alerta: el cliente no oye nada de Appriss hace 25 dias.
RCS-28122, Blain's, Not able to make changes to users, 18 dias sin respuesta. Alerta: el cliente no oye nada de Appriss hace 18 dias.
RCS-28282, Co-op, Intermittent blocked access notification, 16 dias sin respuesta. Alerta: el cliente no oye nada de Appriss hace 16 dias.
RCS-28496, PVH, login issues desktop e ipads, 16 dias sin respuesta. Alerta: el cliente no oye nada de Appriss hace 16 dias.
RCS-28289, Vitamin Shoppe, Blocked Users, 12 dias sin respuesta. Alerta: el cliente no oye nada de Appriss hace 12 dias.
RCS-27765, Winn-Dixie, Data file check, 2 dias sin respuesta, cliente prometio reenvio de datos el 9 de septiembre. Sin alerta. Nivel dudoso, ver seccion de exactitud arriba.

## Nivel 4, movimiento interno o trabajado sin pegar (5)

RCS-28099, CWH, HYP to RCS Item Discount Logic, sin pendiente de cara al cliente, cliente sin noticias hace 19 dias. Alerta: el cliente no oye nada de Appriss hace 19 dias.
RCS-27791, Guess, Audit Question en Grid Style, sin pendiente de cara al cliente, silencio de 4 dias. Sin alerta.
RCS-28581, CWH, POS Number regresado a mapeo anterior, sin pendiente de cara al cliente, silencio de 3 dias. Sin alerta.
RCS-28756, Appriss Internal, Nike ECOM Load issue, trabajado, posible ya pegado en Jira, revisar bitacora. Sin alerta.
RCS-28342, Ahold-Delhaize, Employee data missing from profile, sin pendiente de cara al cliente, silencio de 2 dias. Sin alerta.

## Recomendacion

Empieza por RCS-28294. Es el ticket con mas dias de silencio dentro del nivel mas urgente, cuatro dias sin que nadie de Appriss conteste a Tatiana Barcenas. RCS-28482 pide una respuesta mas corta y quedo con menos dias de silencio, resuelvelo enseguida despues de RCS-28294 porque el cliente ya anuncio su proximo paso y solo falta confirmar.
