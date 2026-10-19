# Cola de la mañana, 2 sep 2026

Refresco automatico previo al turno. 18 tickets abiertos asignados a Juan.
Niveles: 1 = 2 tickets, 2 = 0, 3 = 5, 4 = 11.

## Aviso del clasificador

`bin/eval_cola.py` da 7 de 13 = 54 por ciento. La caida no viene del lexico.
Las etiquetas de `cola/EVAL-clasificador.json` se fijaron el 24 ago y los seis tickets que fallan
son exactamente los seis cuyo ultimo comentario cambio despues de esa fecha.

| Ticket | Etiqueta fijada 24 ago | Realidad hoy |
|---|---|---|
| RCS-27941 | 1, Colton Neal reporto | Juan publico causa raiz el 1 sep |
| RCS-27765 | 1, Heaven escribio el 24 | Juan contesto |
| RCS-28289 | 1, Joe Austin: Scot vuelve | Juan contesto |
| RCS-28123 | 2, Kamminga prometio seguir | Kamminga publico hallazgos el 1 sep, sin promesa nueva |
| RCS-28256 | 2, prometio update | Juan mando recordatorio el 1 sep |
| RCS-28327 | 2, promesa de 11 dias | Juan publico el update el 28 ago, promesa cumplida |

Accion pendiente: refijar las etiquetas del eval contra el volcado de hoy. Hasta entonces el
numero no mide el clasificador, mide la antiguedad del set.

## Cambios desde ayer

Entra RCS-27791, Guess, nivel 1, 48 dias de silencio hacia el cliente.
Sale RCS-28638, Myer Australia, reasignado a Sebastian Garces, sigue abierto en Under Support Review.
Comentarios nuevos: RCS-28671 por Valerie Cerezo, RCS-27941 por Juan.
Ningun ticket subio de nivel. Ningun cliente escribio durante la noche.

## Nivel 1, te toca responder

### RCS-27791 Guess, Audit Question not appearing correctly in Grid Style
Under Support Review, Medium, reporta Stephanie Benedetti, 50 dias de edad.
Alerta: el cliente no oye nada de Appriss hace 48 dias.
Ultimo humano de cara al cliente: Stephanie Benedetti, "Thank you!".
Lo que el clasificador no marca: el 27 ago Matthew Kamminga escribio en el ticket interno de
ingenieria, relevado por Automation for Jira, "This should now be working as expected. Please
validate and then let the client know". El fix esta listo desde hace 6 dias y nadie se lo dijo a
Stephanie.

### RCS-28294 Vallarta, Smart Alerts no Triggering
Under Support Review, Medium, reporta Tatiana Barcenas, 21 dias de edad, silencio de 5 dias.
Tatiana escribio hace 1 dia. No puede entregar mas case numbers porque no logra entrar al sistema,
le pidio cambio de contraseña y le salio un mensaje de error.
Bitacora del 25 ago: el caso 2026-ADUP-40-96 nunca se completo, contraste PDF contra Change History.

## Nivel 2, promesa sin cumplir

Vacio.

## Nivel 3, esperando al cliente

- RCS-27676 RLC SFTP IP/Hostname Change, Tyler Aken, 28 dias sin respuesta, pediste las IP publicas.
- RCS-27959 PACSUN MuleSoft whitelisting, 20 dias, pediste que corran las pruebas.
- RCS-28122 Blain's cambios de usuarios, James Check, 13 dias, pediste confirmacion de cierre.
- RCS-28282 Co-op acceso bloqueado, Michelle Welsh, 11 dias, pediste la lista de paises.
- RCS-28496 PVH fallas de login, 11 dias, esperas la respuesta a lo que pidio Rajith.

Los cinco pasaron los siete dias. Todos tocan perseguir.

## Nivel 4

- RCS-28153 BYF errores y cierre de sesion, High, trabajado sin pegar en Jira desde el 27 ago, cliente en silencio hace 21 dias.
- RCS-28099 CWH item discount logic, movimiento interno, cliente en silencio hace 14 dias.
- RCS-28289 Vitamin Shoppe blocked users, esperando a que Scott vuelva, 7 dias.
- RCS-27765 Winn-Dixie data file check, hilo movido a correo, 7 dias.
- RCS-28482 AHL/DLZ campos grises en Izenda, trabajado sin pegar desde el 27 ago, 6 dias.
- RCS-28327 Delhaize loyalty discounts, update publicado, investigacion activa, 5 dias.
- RCS-28581 CWH POS number regresion, trabajado sin pegar desde el 31 ago, 5 dias.
- RCS-28123 ADUSA case assignment, Kamminga publico hallazgos ayer, 1 dia.
- RCS-28256 Appriss Incident timeouts, High, recordatorio enviado ayer, 1 dia.
- RCS-28671 THD searches producing errors, High, Escalated, Valerie Cerezo pide alcance e impacto, 0 dias.
- RCS-27941 Tailored Brands SSO, causa raiz publicada ayer, 0 dias.

## Por donde empezar

RCS-27791. El fix de ingenieria esta confirmado desde el 27 ago y la unica persona que falta por
enterarse es la clienta. Cierras 48 dias de silencio con un mensaje de validacion y probablemente
cierras el ticket. Ningun otro de la cola se resuelve con tan poco trabajo.

## Riesgo aparte

RCS-28638 cambio de dueño a Sebastian Garces. La bitacora del 31 ago con el refresco de
enumeraciones nunca se pego en Jira. Sebastian arranca sin ese contexto.
