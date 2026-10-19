# Pase de guardia ADUSA, corte martes 22 sep 2026, 22:19 Bogota

Tracker vigente: inbox/adusa-envio-hoy/Appriss ADUSA-Support-Tracker - 09222026 D26.xlsx
Correo: inbox/2026-09-22-correo-D26-para-jim.md
Cadencia: un tracker por dia habil trabajado. D23 jueves 17, D24 viernes 18, D25 lunes 21, D26 martes 22.

Total 60 tickets historicos. 48 resueltos, 12 abiertos. Cero en Pending Ahold verification,
2 en Awaiting Ahold input, 10 Active with Appriss.

Todo lo de abajo esta verificado contra Jira en vivo hoy. Los dias quietos se cuentan desde el
ultimo comentario real, sin contar automaticos ni espejos del ticket interno de ingenieria.

---

## Lo que hay que mirar primero

### 1. RCS-28693 lleva once dias pudiendo cerrarse

Kiran Vadday escribio el 11 sep, replicado al RCS desde el ticket interno de ingenieria:
"The RCS can be closed. The tied ENG ticket will continue to go as usual and the fix goes to
everyone." Gina Pilato confirmo el 15 sep: "Assigned myself to 852 S&S and was able to
create/save an incident."

Ingenieria dio luz verde hace once dias y el ticket sigue en Under Engineering Review con Matthew
Kamminga. El cliente no ha recibido nada desde el 9/10. Accion: redactar el cierre con Leigh Ann y
Jim, recordando que el cambio de codigo mas amplio continua por separado, y transicionar. Es el
cierre mas barato que hay en la lista.

### 2. RCS-29059 esta sin asignar y toca dos instancias

Abierto hoy 16:27 por Teresa Coughenour, levantado por la SE Kristen Dyer en una llamada con
Delhaize. El indicador Associated del quick receipt no marca transacciones que ya estan en una
investigacion, lo que hace que los work items se sientan duplicados. Lo probaron tambien en la
instancia Ahold y tampoco funciona, con captura de agosto mostrando que si funcionaba antes.

Nadie lo tiene. Es el unico sin dueno de los doce.

### 3. RCS-28281 tiene reloj de auto cierre corriendo

El aviso automatico del 21 sep dice que el ticket se cierra solo si el cliente no responde en los
proximos catorce dias. Ahold no escribe desde el 31 de agosto, veintidos dias. Juan puso
seguimiento el 17 y otra vez hoy 22 a las 20:29.

Decision pendiente de Juan, no del cliente: o se consigue el chequeo de diez minutos por otra via,
o se deja cerrar, o se pide extension interna. Aparte hay una deuda propia sin saldar: los conteos
por dia de trading que Juan se comprometio a postear el 26 de agosto nunca se pegaron.

---

## Los doce abiertos, uno por uno

### RCS-28281, Ahold, carga de transacciones del 10 ago
Under Customer Review, Awaiting Ahold input, Juan Martinez, High.
Ultimo movimiento real: hoy 22 sep 20:29, seguimiento de Juan. Cliente callado desde el 31 ago.
Falta: que Becky corra el chequeo de diez minutos sobre 8/11, 8/12, 8/19, 8/20, 8/22 y 8/25.
Siguiente: decidir que hacer con el reloj de auto cierre. Pegar los conteos por dia pendientes
desde el 26 ago.

### RCS-28589, Ahold, apostrofes en el store file
Accepted into Development, Active with Appriss, Matthew Kamminga.
Ultimo movimiento real: 9 sep, Kamminga pidiendo a Shandana abrir ticket ENG. Trece dias.
El espejo del 21 sep dice que el ticket interno esta en Ready for Test y Gina pregunta si hay algo
para QA. Eso no entra al tracker, es resultado de QA.
Falta: que ingenieria termine y libere.
Siguiente: preguntar internamente por el estado real del ENG antes de que el cliente pregunte.

### RCS-28667, Ahold, usuarios nuevos en la plataforma
Under Engineering Review, Active with Appriss, Matthew Kamminga.
Ultimo movimiento real: 3 sep. Diecinueve dias. El mas frio de la lista.
Falta: respuesta de ingenieria. No hay nada escrito desde hace casi tres semanas.
Siguiente: empujon a Kamminga. Si no hay avance, escalar a Shandana para planificacion.

### RCS-28683, Ahold, agregar asociado a un caso
Under Engineering Review, Active with Appriss, Matthew Kamminga.
Ultimo movimiento real: 9 sep. Trece dias.
Diego Buelvas reprodujo el 404 al agregar un asociado. Ademas absorbio el item que venia de
RCS-28910, el mensaje de error que Leigh Ann vio al agregar una persona al caso.
Falta: ingenieria.
Siguiente: mismo empujon que RCS-28667, van con el mismo dueno.

### RCS-28693, Ahold Delhaize, SSO y rol Store Reporter por defecto
Under Engineering Review, Active with Appriss, Matthew Kamminga.
Ver el punto uno de arriba. Cerrable desde el 11 sep.

### RCS-28824, Delhaize, store y cashier profiles
Work in progress, Active with Appriss, Sebastian Rueda.
Ultimo avance real: 17 sep, respuesta de Becky. Hoy 22 sep solo hubo acuse sin contenido.
Estado: store profile corregido, las cuatro pestanas devuelven graficos. Quedan dos frentes, los
dos de datos. El cashier profile no devuelve graficos y el area map no tiene coordenadas.
Dato que ordena el caso, de Becky el 17 sep: ADUSA si envia archivo de tiendas y ubicacion, no
envia archivo de empleados, y lo que necesita en cashier no es detalle de empleado sino que los
graficos de refunds, voids y coupon history devuelvan datos. Apunta a que otra instancia de su
organizacion tampoco envia archivo de empleados y ahi si le pintan.
Falta: que el equipo de datos confirme que llega en cada feed.
Siguiente: pedirle a Sebastian una respuesta con contenido. El acuse de hoy dice "will came back
to you with some updates soon", que ademas usa una referencia de tiempo que la regla prohibe.

### RCS-28849, Ahold, pantalla de confirmacion al asignar un caso
Accepted into Development, Active with Appriss, Shandana Khan.
Ultimo movimiento real: 14 sep. Ocho dias.
Aceptado como change request, no como defecto. El trabajo va por producto.
Falta: nada del lado de soporte. Es seguimiento pasivo.
Siguiente: nada urgente.

### RCS-29000, Delhaize, redondeo inconsistente en columnas de porcentaje
Accepted into Development, Active with Appriss, Shandana Khan.
Movimiento hoy 22 sep 11:14, ingenieria lo acepto para desarrollo. Sin comentario escrito de
ingenieria, solo la transicion de estado.
Sebastian escalo el 21 sep con el analisis completo: una o dos de las cuatro columnas calculadas
pierden la designacion de dos decimales en cada corrida y cual es cambia entre corridas.
Verificado sobre un export de 321 filas.
Ojo con la regla: ingenieria no ha confirmado defecto por escrito. En texto al cliente no se
nombra defecto todavia, solo el estado.
Siguiente: cuando ingenieria escriba algo, actualizar al cliente. Becky esta bloqueada para
publicar su reporte mientras tanto.

### RCS-29026, Ahold Food Lion, Smart Alert que no disparo
Under Support Review, Active with Appriss, Juan Martinez desde el 21 sep 20:51.
El cliente no ha recibido nada mas que el acuse de L1. Un dia sin respuesta de fondo.
Caso 2026-FOOD LION,LLC-0619-27, digitado el 20 sep 10:12. Asset Protection no recibio la alerta,
Dawn Hendry de Store Payments tampoco, y BTatum aparece en la lista sin deber estar.
Pregunta abierta del cliente que es la que mas pesa: hay mas alertas que no dispararon.
Plan ya escrito, paso a paso, en inbox/2026-09-22-planes-28581-28099-28984-29026.md.
Metodo de referencia en inbox/2026-09-18-flujo-debug-smart-alerts-inprocess.md, de Kamminga sobre
RCS-28294. Dos fallas distintas bajo el mismo sintoma: flag incident.Shoplifting.inprocess pegado
en 1, y BlobNotFound de Azure al generar el documento. Los debug logs disparan al guardar el
incidente, no hay que esperar batch.
Siguiente: ejecutar ese plan. Es el ticket con mas impacto de negocio de los doce.

### RCS-29042, Ahold Delhaize, error en la pestana de adjuntos
Under Support Review, Active with Appriss, Vedant Shirude.
Abierto hoy 07:44 por Leigh Ann. Vedant lo tiene desde hoy.
Caso 2026-FOOD LION,LLC-1586-2. La pestana de adjuntos da error en ese caso y funciona en otro.
Ella pregunta si hay que borrar el caso y rehacerlo.
Siguiente: mirar ese caso concreto antes de que ella lo borre por su cuenta.

### RCS-29057, Ahold Delhaize, narrative ausente en el LP External Doc
Under Customer Review, Awaiting Ahold input, Juan Martinez.
Abierto hoy 15:25 por Leigh Ann. Juan lo tomo a las 18:13 y pidio el numero de caso a las 19:57.
Ficha completa en inbox/2026-09-22-rcs-29057.md.
Lo relevante: la hipotesis directa del precedente RCS-22886 quedo descartada. Dos casos de prueba
de tipos distintos generan el LP External Doc con el narrative completo. La causa esta en otro
factor que ninguna prueba nueva reproduce.
Falta: el numero de caso puntual. Sin eso no hay mas terreno propio que cubrir.
Siguiente: esperar el dato. Si el narrative del caso real tampoco esta guardado en Incident, el
problema no es el documento y hay que redirigir la conversacion.

### RCS-29059, Delhaize, indicador Associated ausente en el quick receipt
Under Support Review, Active with Appriss, sin asignar.
Abierto hoy 16:27 por Teresa Coughenour, en nombre de Kristen Dyer.
Ver el punto dos de arriba. Es el unico sin dueno.

---

## Relojes y riesgos

RCS-28281, auto cierre por silencio del cliente. Aviso de catorce dias emitido el 21 sep.
RCS-29026, la pregunta de si hay mas alertas silenciosas sigue sin responder y el caso era de
perdida grande.
RCS-28667, diecinueve dias sin movimiento en ingenieria. Es el candidato natural a que el cliente
pregunte en la proxima llamada.
RCS-29000, Becky bloqueada para publicar su reporte mientras ingenieria no entregue.
RCS-29042, riesgo de que el cliente borre y rehaga el caso por su cuenta antes de que alguien lo
mire.

## Tres tickets nuevos en un solo dia

22 sep trajo RCS-29042, RCS-29057 y RCS-29059. Es el dia con mas entradas de la serie. Los tres
vienen de dos personas de ADUSA, Leigh Ann Stubbs dos y Teresa Coughenour uno. Dos ya tienen dueno,
uno no.

## Lo que no entro al tracker y por que

El analisis de escalacion de RCS-29000 completo, con Search Composer, ARDM_Header, int8, numero de
cliente y la palabra defect. Ingenieria no ha confirmado nada por escrito.
Los espejos automaticos del ticket interno de ingenieria en RCS-28589 y RCS-28693, que ademas
traen resultados de QA.
El aviso automatico de catorce dias de RCS-28281, que es fecha futura y presiona al cliente.
Lo interno de RCS-28824 sobre Snowflake, Greenplum, cliente 46, GP11 y PyARDM.

## Metodo, para quien reciba esto

Cada dia: reconfirmar los abiertos contra Jira en vivo, barrer los RCS creados desde el ultimo
tracker filtrando por reporter de dominio adusa.com y no por palabra clave en el titulo, generar
el nuevo desde el anterior con generar_dNN.py, y correr el diff celda por celda contra el anterior
antes de enviar. Abrir el archivo en Excel una vez para que recalcule la fila 18.
El correo va bajo la skill cerebro-respuesta-cliente: cero peticiones, sin fechas futuras, sin
nombres de personas del cliente salvo el saludo, sin nombrar defecto sin confirmacion escrita de
ingenieria.
