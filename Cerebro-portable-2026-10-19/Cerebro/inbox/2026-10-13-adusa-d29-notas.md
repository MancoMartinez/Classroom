# D29, martes 13 oct 2026

Tracker fuera de cadencia. Lo pidio J.R. Teagle en Teams para compartir con
Carl G de Sales, antes de una reunion de nivel alto sobre Engage.

Archivo: inbox/adusa-envio-hoy/Appriss ADUSA-Support-Tracker - 10132026 D29.xlsx
Script:  inbox/adusa-envio-hoy/generar_d29.py
78 tickets, 59 resueltos, 19 abiertos, 14 con Appriss, 5 esperando a Ahold,
0 en Pending Ahold verification.

## Lo que se movio desde el D28

RCS-29315 pasa a Under Engineering Review el 10/13. Megha confirmo que el SAML de
Alexis Henderson llega con rol y ubicacion y no se crea cuenta. Escalado a Kiran.
RCS-29376 pasa a Under Delivery Review el 10/12 y cambia de Shandana a David Parraga.
Shandana lo mando a delivery por si es configuracion y no bug de plataforma.
RCS-28667 pasa a Accepted into Development. La transicion fue el 10/2.
RCS-29108 pasa a Under Customer Review y a Awaiting Ahold input. Vedant confirmo
EmailonReassign en YES, ENG-8714 en produccion y correo cargado para Stephanie
Jenkins, y pidio a Leighann que confirme si sigue sin recibir.
RCS-27077 pasa a Under Customer Review y a Awaiting Ahold input. Nikita cargo los
76 archivos TLOG de Ahold, 12,758 transacciones, ninguno rechazado.
RCS-29300 sube a 10/13 por el seguimiento de Megha. Sigue esperando a Becky.
RCS-28281 sube de 9/24 a 10/6 por el seguimiento real de Juan.
RCS-29399 entra nuevo en el bloque de transacciones.

## Sin movimiento real

RCS-29000, el 10/12 es espejo de Automation for Jira del ticket de ingenieria con
los prerequisitos de prueba de Kiran. Fecha queda en 9/22.
RCS-28281, el 10/11 es el aviso automatico de 60 dias.
RCS-28667, el 10/13 tambien es espejo de automation.
Diez tickets sin tocar: 28693, 28683, 28849, 29131, 29164, 29234, 28824, 29026,
29063, 29355.

## Lo que hay que mirar

El D28 reporto RCS-28667 como Under Engineering Review. Jira lo habia movido a
Accepted into Development el 10/2, siete dias antes del envio. Corregido en el D29.
Ese error nace de verificar estado solo con los tickets que tuvieron comentario
nuevo. La transicion no dejo comentario.

Matthew Kamminga escribio el 10/13 en el ENG de RCS-28667 que hay que montar las
pruebas con el cliente para recorrer todos los detalles. Eso se vuelve una llamada
con Leighann. No lo puse en el texto al cliente porque todavia no es un compromiso
dado por escrito a ADUSA.

RCS-29399 trae un pedido de Rodney para entrar a Secure por un link sin SSO
mientras dura el problema de acceso. Shaun Callow lo subio al equipo el 10/13 y
nadie ha contestado. Es una decision, no una tarea de soporte.

RCS-28693 sigue abierto en Under Engineering Review con Matthew, sin tocar desde
el 9/15. Kiran escribio el 9/11 que el RCS se puede cerrar y Gina lo confirmo el
9/15. Van 28 dias.

Carl separa Secure de Incident y el tracker esta organizado por tema, no por
producto. El corte por producto se puede sacar del campo RCS: Issue Type en Jira.
No lo etiquete a mano para no equivocarme delante de Sales.
