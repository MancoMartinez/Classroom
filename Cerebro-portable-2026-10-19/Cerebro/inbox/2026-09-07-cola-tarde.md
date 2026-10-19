# Cola del 2026-09-07, refresco de la tarde

Comparado contra el corte de la manana del mismo dia, generado a las 10:22.

## Exactitud del clasificador

El eval dio 87 por ciento, 13 de 15. Bajo del 93 por ciento de la manana. El lexico sigue desactualizado.

Falla en RCS-28753. Esperaba nivel 2 y dio nivel 4. La etiqueta a mano se baso en el triage automatico de Akshaya Purappemane que promete seguimiento. El ticket ya tiene una respuesta real de Juan a Nike sobre Peyman, asi que el nivel 4 puede ser el correcto ahora y la etiqueta a mano quedo vieja. Revisa antes de confiar ciegamente en cualquiera de los dos.

Falla en RCS-27765, misma que en la manana. Esperaba nivel 4 y dio nivel 3. El comentario "the email has been replied to and we will be monitoring the thread" no lo reconoce el lexico de cierre.

## Que cambio desde la manana

RCS-28281 entro nuevo a la cola. Ahold, Transaction Data Load For August 10 Incomplete, prioridad High. Bitacora de hoy dice que el estancamiento viene de un traspaso a Nikita del 27 de agosto que no se completo y una pregunta de Ayesha sin responder. Pendiente escalar a Viraj y actualizar al cliente con el chequeo de bloques de 10 minutos para las fechas 8/11, 8/12, 8/19, 8/20, 8/22 y 8/25.

RCS-28671 reaparecio. THD, Searches Producing only Errors, prioridad High, label Escalated. Estaba ausente en el corte de la manana. Mohammed Mutahhar, SRE, confirmo la causa del work item atascado y que los datos ya existen en el sistema fuente. Falta remover el work item afectado y regenerarlo.

RCS-28482 bajo de nivel 1 a nivel 4. Juan ya le respondio a Jim Cosseboom pidiendo confirmacion para cerrar el ticket o seguir investigando. Queda en espera de esa confirmacion.

RCS-28753 bajo de nivel 2 a nivel 4. Juan ya le respondio a Nike sobre la disponibilidad de Peyman para confirmar la informacion pedida.

RCS-28294 y RCS-27941 siguen en nivel 1 sin respuesta, ahora con un dia mas de silencio cada uno, 5 y 4 dias.

Nivel 2 quedo vacio.

## Nivel 1, te toca responder (2)

RCS-28294, Vallarta, Smart Alerts no Triggering, prioridad Medium.
Motivo: Tatiana Barcenas escribio hace 5 dias y nadie de Appriss contesto.
Ultimo movimiento: "Hi Juan, Thank you, we will continue to use Internet Explorer. Regards, Tatiana Barcenas"
Alertas: ninguna.

RCS-27941, Tailored Brands, SSO/Permissions Issues in Incident, prioridad Medium.
Motivo: Colton Neal escribio hace 4 dias y nadie de Appriss contesto.
Ultimo movimiento: "Thanks Juan, I will work on this and get back to you next week sometime. Thanks again,"
Alertas: ninguna.

## Nivel 2, promesa sin cumplir

Ninguno.

## Nivel 3, esperando al cliente (7)

RCS-27676, RLC, SFTP IP/Hostname Change, 34 dias sin respuesta. Alerta: 34 dias.
RCS-27959, PACSUN, IP Whitelisting MuleSoft, 26 dias sin respuesta. Alerta: 26 dias.
RCS-28122, Blain's, Not able to make changes to users, 19 dias sin respuesta. Alerta: 19 dias.
RCS-28282, Co-op, Intermittent blocked access notification, 17 dias sin respuesta. Alerta: 17 dias.
RCS-28496, PVH, login issues desktop e ipads, 17 dias sin respuesta. Alerta: 17 dias.
RCS-28289, Vitamin Shoppe, Blocked Users, 13 dias sin respuesta. Alerta: 13 dias.
RCS-27765, Winn-Dixie, Data file check, 3 dias sin respuesta, cliente prometio reenvio de datos el 9 de septiembre. Sin alerta. Nivel dudoso, ver seccion de exactitud arriba.

## Nivel 4, movimiento interno o trabajado sin pegar (9)

RCS-28099, CWH, HYP to RCS Item Discount Logic, sin pendiente de cara al cliente, silencio de 20 dias. Alerta: 20 dias.
RCS-27791, Guess, Audit Question en Grid Style, sin pendiente de cara al cliente, silencio de 5 dias. Sin alerta.
RCS-28342, Ahold-Delhaize, Employee data missing from profile, sin pendiente de cara al cliente, silencio de 3 dias. Sin alerta.
RCS-28581, CWH, POS Number regresado a mapeo anterior, sin pendiente de cara al cliente, silencio de 3 dias. Sin alerta.
RCS-28756, Appriss Internal, Nike ECOM Load issue, trabajado, revisar si ya quedo pegado en Jira. Sin alerta.
RCS-28281, Ahold, Transaction Data Load Incomplete, nuevo hoy, trabajado, pendiente escalar a Viraj. Sin alerta.
RCS-28671, THD, Searches Producing only Errors, reaparecio, causa confirmada por Mohammed Mutahhar, falta regenerar el work item. Sin alerta.
RCS-28482, AHL/DLZ, Greyed out fields in Izenda, ya respondiste, esperando confirmacion de Jim Cosseboom. Sin alerta.
RCS-28753, Nike, Logic for Manual Discount Amount field, ya respondiste sobre disponibilidad de Peyman. Sin alerta.

## Recomendacion

Sigue con RCS-28294 y RCS-27941, los unicos dos en nivel 1 y los dos llevan mas de un dia de silencio sin que nadie de Appriss conteste. Empieza por RCS-28294 porque tiene un dia mas de silencio.
