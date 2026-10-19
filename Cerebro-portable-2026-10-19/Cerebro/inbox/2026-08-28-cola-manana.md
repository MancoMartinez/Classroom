# Cola de la mañana, viernes 28 ago 2026

Generado 2026-08-28T10:09 -04:00 desde Jira en vivo. 16 tickets abiertos.
Niveles: 1=1, 2=3, 3=6, 4=6.

## Aviso primero: el clasificador dio 67%

`bin/eval_cola.py` reporta 8 de 12, exactitud 67%. Revisé las cuatro fallas contra el volcado.
Tres son etiquetas vencidas, no léxico roto. El set de referencia se fijó el 24 ago y en esos
tres tickets Juan comentó después de esa fecha.

- RCS-28327, Juan publicó update el 27 ago. La etiqueta esperaba nivel 2 por una promesa del 12 ago que ya cumplió.
- RCS-28289, Juan respondió a Joe Austin el 25 ago. La etiqueta esperaba nivel 1.
- RCS-27765, Juan respondió a Heaven Poirot el 25 ago. La etiqueta esperaba nivel 1.

La cuarta es real. RCS-28256 lleva señal doble en el mismo comentario: Juan pide confirmación
a Colton y además promete seguimiento sobre el login de Vincent Fortner. `cola.py` lo mandó a
nivel 3. Cabe en nivel 2. Trátalo como si estuviera arriba.

Acción pendiente: refijar `cola/EVAL-clasificador.json` con lectura del 28 ago. Mientras siga
con etiquetas del 24, el porcentaje no mide el léxico.

## Qué cambió desde ayer

Entró uno. RCS-28638, Myer Australia, mapping de Proof Type, Order No y Financial Statement Date
perdido desde el 09/08/26. Prioridad High. Christine Piacentini reporta. Juan ya tomó ownership.

Salieron dos de la cola. RCS-28223 y RCS-28294.

Subió de nivel uno. RCS-28093 pasó de nivel 4 a nivel 1 y de Under Support Review a Work in
progress. Leigh Ann Stubbs escribió y nadie de Appriss contestó.

Escribió un cliente en la noche. Leigh Ann Stubbs en RCS-28093. Es el único movimiento de
cliente desde el corte de ayer.

## Nivel 1, te toca responder

### RCS-28093, Ahold, Employees not restricted by Store location
Work in progress. Low. 27 días de edad. Reporta leighann.stubbs@adusa.com.
Motivo: Leigh Ann escribió hace 0 días y nadie de Appriss contestó.
Alertas: ninguna.
Último movimiento, Leigh Ann Stubbs: "I am not sure what it will take to do that but I have
copied April on this message to see if it's a possibility."
https://trebuco.atlassian.net/browse/RCS-28093

## Nivel 2, promesa sin cumplir

### RCS-28638, Myer Australia, Mapping of Proof Type, Order No y Financial Statement Date
Under Support Review. High. 0 días de edad. Reporta Christine Piacentini. Entró hoy.
Motivo: prometiste un update hace 0 días y no llegó.
Alertas: ninguna.
Último movimiento, Juan Martinez: "I have taken ownership of this ticket and will be
investigating it for you. Please allow some time for me to research the issue and I will get
back with you just as soon as I have any information."
https://trebuco.atlassian.net/browse/RCS-28638

### RCS-28581, CWH, POS Number has regressed to previous mapping
Under Support Review. Medium. 2 días de edad. Reporta James McKenna.
Motivo: prometiste un update hace 0 días y no llegó.
Alertas: ninguna.
Último movimiento, Juan Martinez: "I have taken ownership of this ticket and will be
investigating it for you. Please allow some time for me to research the issue and I will get
back with you just as soon as I have any information."
https://trebuco.atlassian.net/browse/RCS-28581

### RCS-28123, ADUSA, Case assignment issues
Work in progress. Medium. 25 días de edad. Reporta leighann.stubbs@adusa.com.
Motivo: prometiste un update hace 1 día y no llegó. Silencio de cliente 1 día.
Alertas: ninguna.
Último movimiento, Juan Martinez: "The missing confirmation and print option is a separate
issue. I have logged it, and engineering is reviewing it now. I will update you as soon as
possible."
https://trebuco.atlassian.net/browse/RCS-28123

### RCS-28256, Appriss Incident Time Out(s) and Slow Load times (clasificado 3, cabe en 2)
Under Customer Review. High. 18 días de edad. Reporta Colton Neal.
Motivo del script: pediste algo hace 2 días y no hay respuesta. El mismo comentario promete
seguimiento sobre el login de Vincent Fortner, y esa promesa no se ha cumplido.
Alertas: ninguna.
Último movimiento, Juan Martinez: "Vincent Fortner's login is a separate issue on our side.
We are aware of it and I will follow up with you on that. Fixes have been deployed for the save
errors and for reporting. Before I close either of these, I would prefer to get your confirmation."
https://trebuco.atlassian.net/browse/RCS-28256

## Nivel 3, esperando al cliente

- RCS-27676, RLC, SFTP IP/Hostname Change, Low, 23 días sin respuesta, alerta: el cliente no oye nada de Appriss hace 23 días. Pasó los 7 días, toca perseguir.
- RCS-27959, PACSUN, IP Whitelisting para MuleSoft, Medium, 15 días sin respuesta, alerta: el cliente no oye nada de Appriss hace 15 días. Pasó los 7 días, toca perseguir.
- RCS-28122, Blain's, Not able to make changes to users, Medium, 8 días sin respuesta, alerta: el cliente no oye nada de Appriss hace 8 días. Pasó los 7 días, toca perseguir.
- RCS-28282, Co-op, Intermittent blocked access notification, Medium, 6 días sin respuesta, sin alertas.
- RCS-28496, PVH, multiple stores reporting issues logging in, Medium, 6 días sin respuesta, sin alertas.

## Nivel 4, en movimiento interno o trabajado sin pegar

- RCS-28153, BYF, Errors and logging users out, High, alerta: el cliente no oye nada de Appriss hace 16 días. Trabajado sin pegar en Jira. Fix liberado, ENG-7184 Done, fixVersion Secure August 2026 Release 2/2.
- RCS-28099, CWH, HYP to RCS Item Discount Logic, Medium, alerta: el cliente no oye nada de Appriss hace 9 días. Último autor David Vargas.
- RCS-28327, Delhaize, Loyalty Discounts not Specified, Medium, sin alertas. Update publicado el 27 ago. Plan de validación en inbox/2026-08-24-rcs-28327-validacion-composer.md.
- RCS-27765, Winn-Dixie, Data file check, Medium, sin alertas. Respondido el 25 ago, hilo de correo reconectado.
- RCS-28289, Vitamin Shoppe, Blocked Users, Medium, sin alertas. Esperando a que Scott vuelva de vacaciones.
- RCS-28482, AHL/DLZ, Greyed out fields en Izenda, Low, sin alertas. Jim confirmó que el reporte corre y solo falla la edición. Sin hallazgo técnico. No escribirle sin hallazgo.

## Por dónde empezar

RCS-28093. Es el único nivel 1 y es el único movimiento de cliente de la noche. Leigh Ann
Stubbs copió a April y dejó la pregunta abierta sobre qué hace falta para restringir empleados
por tienda. El reloj arranca hoy en cero y ahí se corta más barato. Los tres nivel 2 son
acuses de ownership de menos de 48 horas, todavía no queman.

Si sobra tiempo antes del bloque de nivel 2, RCS-27676 lleva 23 días de silencio hacia el
cliente y es el número más alto de la cola.
