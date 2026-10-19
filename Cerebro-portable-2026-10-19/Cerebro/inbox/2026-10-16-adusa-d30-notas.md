# D30, viernes 16 oct 2026

Semanal. Periodo que ve Jim: 9 al 16 oct.

Archivo: inbox/adusa-envio-hoy/Appriss ADUSA-Support-Tracker - 10162026 D30.xlsx
Script:  inbox/adusa-envio-hoy/generar_d30.py
78 tickets, 61 resueltos, 17 abiertos. 9 con Appriss, 6 esperando a Ahold,
2 en Pending Ahold verification.

## El hecho que ordena la semana

ADUSA esta con un incidente de seguridad desde el fin de semana del 10/10 que les
corta el SSO a aplicaciones externas. Aparece escrito en cuatro tickets: Jim en
RCS-29234 el 10/16 y en RCS-29164 el 10/15, Rodney en RCS-27077 el 10/15 y en
RCS-29399 el 10/13, Becky en RCS-29300 el 10/14. Jim espera recuperar acceso a
comienzos de la semana.

Eso explica por que seis tickets quedan esperando a Ahold y por que los dos fixes
liberados esta semana no se pueden verificar todavia.

## Cierres

RCS-29026 el 10/13. Leigh Ann confirmo que se podia cerrar.
RCS-29399 el 10/14. Luis entrego el detalle hora por hora del 10/11 al 10/13 de las
dos instancias. Delhaize: los archivos llegaron bien, la carga se freno por un error
en el paso del recall extract, se reinicio y hay correccion preparada sin desplegar.
Ahold: todos los archivos se procesaron sin error, lo que cambio fue el contenido,
mucho menos volumen del 10/12 hasta la tarde del 10/13. Rodney consiguio acceso
alterno y cerro el ticket.

## Fixes liberados en la release de esta semana

RCS-29234 a produccion el 10/16. Sebastian Garces pidio verificacion a Jim el mismo
dia. Jim no puede probar por el incidente. Pasa a Pending Ahold verification.
RCS-28667 a produccion el 10/16. Matthew Kamminga dejo escrito que hay que montar
las pruebas con el cliente. Lo dejo en Active with Appriss porque Appriss todavia no
le ha dicho nada al cliente, no es verificacion pendiente mientras no se pida.
RCS-28693 se desbloqueo por fin. J.R. pidio el 10/13 que Harrison Xu reintentara,
Kiran confirmo que el fix salio en ENG-8701, Leigh Ann contesto que no puede ahora.
Pasa a Pending Ahold verification con Vlad Bogus. Llevaba sin tocar desde el 9/15.

## Lo que hay que mirar

RCS-29376 esta resuelto en el analisis y no se le ha dicho al cliente. Juan Ramirez
valido el 10/13 en produccion que el boton Reset Password solo sale en cuentas con
UserType Normal, o sea las que nunca han entrado por SSO. Leigh Ann tiene cuatro
cuentas y las dos que usa no muestran el boton. Falta redactar esa respuesta.

RCS-29300 se puso serio. Becky dijo el 10/14 que el orden en el recibo importa para
la investigacion, que un AP specialist sospecho robo por video que no cuadraba con
Secure, y que esto puede generar falsos positivos. Pidio no tratarlo como feedback
de roadmap. Rodney pidio el 10/15 un ejemplo reciente para el equipo POS EX. Eso lo
debe Appriss.

RCS-29355 tiene una correccion de rumbo. Edwin confirmo el 10/16 que la entrega de
ADUSA si esta bien y que el problema es que esas entregas de QA no se estan cargando
en el ambiente de QA. Sin fecha comprometida. En el texto al cliente lo deje como
hallazgo actual, sin marcarlo como correccion de nadie.

RCS-28281 cambia de naturaleza. Rodney dijo el 10/13 que no tienen proceso para
recuperar datos de mas de 10 dias y que construir uno toma tiempo. Juan confirmo que
el ticket queda abierto. Dejo de ser un reenvio pendiente y pasa a ser un desarrollo
en el lado del cliente.

No mueven fecha por ser espejo de Automation for Jira: RCS-28683 el 10/13 con la
evidencia de QA de Nicolas Garcia, RCS-29000 el 10/16 con el borrador de casos de
prueba de Gina Pilato.

Barrido de RCS creados del 10/13 al 10/16: 75 tickets, ninguno con reporter de
dominio adusa.com. Cero nuevos en el tracker.
