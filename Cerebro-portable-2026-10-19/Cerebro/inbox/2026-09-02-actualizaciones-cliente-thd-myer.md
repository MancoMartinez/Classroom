# Actualizaciones cliente, THD y Myer

Fecha 2026-09-02. Mision recibida por Juan, asegurar actualizacion de cara al cliente hoy en cinco
tickets. Investigacion contra Jira en vivo, cerebro completo, bitacoras, informes previos y las
transcripciones de Teams de hoy sobre RCS-28671.

## Resultado en una linea

Revision en vivo contra Jira, corrida de nuevo despues de la primera entrega. Cuatro de los cinco ya
tienen el ultimo comentario de nuestro lado, no del cliente. Sebastian se adelanto y publico en
RCS-28612 y en RCS-28638 mientras se escribia este archivo, asi que los dos borradores que traia
preparados quedaron sin uso. Solo RCS-28702 sigue sin su comentario sustantivo. Texto listo mas
abajo, verificado contra el checklist de doce puntos de cerebro-respuesta-cliente y contra una
segunda pasada de un agente independiente. No se pego desde aca.

## RCS-28671. THD, Searches Producing only Errors. Tuyo. YA RESUELTO HOY

Estado verificado en Jira, Work in progress. Reporter Corey Wood. Organizacion The Home Depot.

La ficha de `tickets/RCS-28671.md` y el `INDICE.md` marcan el cliente como Tailored Brands. Es un
error del indexador. Corey Wood tiene dominio homedepot.com y el campo organizacion en Jira dice The
Home Depot sin ambiguedad. Revisa `bin/indexar_tickets.py` cuando tengas espacio, no hoy.

Publicaste el comentario a las 16:29 de hoy. Responde exactamente lo que pedia tu jefe. Diecisiete
work items, generados el 28 de agosto entre las 12:05 y las 13:07, lista cerrada con tienda y dueño
de cada uno. Ninguna fecha prometida. Probaste la regeneracion via WISC y confirmaste que no repara
nada. Enrutaste la causa al equipo que dirigio el corte de SnowTime. No hace falta redactar nada
nuevo en este ticket.

Quedan tres deudas tuyas, todavia no de cara al cliente.

Confirmacion de Dan Endersby sobre quien reescribe las filas de evento. Sigue sin respuesta en el
hilo de Teams.

El defecto de snr4 no tiene ticket propio. Cuatro de quince fallos reales de deaggregacion el 27 y
28 de agosto, y nadie lo ha levantado todavia.

Le prometiste a Corey un plan de remediacion. Esa promesa vive sin fecha. Cumplela cuando el equipo
de SnowTime conteste.

## RCS-28649. THD, EBR Secure, Recent Transaction Receipt. Edwin. YA RESUELTO HOY

Estado en Jira, Under Customer Review. Edwin publico a las 16:47 de hoy la explicacion completa a
Matthew Crider. Confirma el hueco del 8/28 corregido y pide al cliente volver a correr su reporte de
discrepancias.

Un riesgo antes de dar esto por cerrado del todo. El informe de ayer, 1 de septiembre, advirtio de
frente no confirmarle al cliente que el problema de visualizacion de recibos quedo resuelto. La
transaccion 1123 de la tienda 7109 mostraba comportamiento inconsistente entre dos vistas del mismo
dato. El comentario de Edwin de hoy confirma que la recarga no dejo recibos obsoletos. No toca esa
transaccion puntual.

Verifica la 1123 antes de que el cliente la encuentre primero. Si renderiza bien hoy, no hace falta
decir nada. Si no, mejor saberlo ahora que despues de cerrar.

## RCS-28702. THD, EBR Secure, Investigations Folder Not Filtering. Edwin. FALTA EL COMENTARIO PUBLICO

Estado en Jira, Under Support Review. Reporter Ericka Smith.

Edwin encontro la causa esta mañana y la escribio en una nota interna con nombre de archivo, commit
y numero de PR. Lo unico que llego a Ericka fue el acuse generico de "ya estamos revisando". Falta
el comentario publico que tu jefe dice que ya tiene material de sobra para escribir.

El texto de abajo no nombra archivos, commit ni PR. Tampoco dice que el mismo defecto puede tocar a
otros clientes con el mismo permiso. Nada de eso le pertenece a Ericka.

## RCS-28612. Myer, Delivery Fee ausente en POS. Sebastian G. YA RESUELTO, SE ADELANTO SEBASTIAN

Estado en Jira, Under Customer Review. Reporter Christine Piacentini.

Sebastian encontro la causa esta mañana, dejo una nota tecnica interna con nombres de tabla y rama,
y a las 17:33 de hoy publico el comentario que faltaba, cita textual, "We deployed a fix for this
issue. Could you please review it?". Es corto y no repite el detalle tecnico. El ultimo comentario
del ticket es nuestro.

El borrador que traia preparado para esta ticket, mas abajo bajo referencia, ya no hace falta
pegarlo. Quedo aqui solo como registro de lo que se habria dicho si Sebastian no llega primero.

## RCS-28638. Myer, Proof Type, Order No, Financial Statement Date. Sebastian G. YA RESUELTO, SE ADELANTO SEBASTIAN

Estado en Jira, Under Customer Review. Reporter Christine Piacentini.

Sebastian tenia el PR 57041 en revision desde las 13:31. A las 17:34 de hoy publico, cita textual,
"We deployed a fix for this issue. Could you please review it?". No repite la frase "soon" de las
10:11. El ultimo comentario del ticket es nuestro.

El borrador que traia preparado para esta ticket, mas abajo bajo referencia, ya no hace falta
pegarlo. Quedo aqui solo como registro de lo que se habria dicho si Sebastian no llega primero.

## El texto que falta pegar, mas dos de referencia ya innecesarios

### RCS-28702, lo pega Edwin, saludo a Ericka Smith. PENDIENTE, es el unico que falta hoy

```
Hi Ericka,

Thank you for the detailed screenshots showing the toggle behavior.

We found the cause. A recent change to how investigation permissions are checked left the
Investigations folder toggle not filtering the way it should, so it shows every investigator's
saved investigations instead of just your own regardless of the toggle position.

The fix is with engineering now.

I need nothing further from you on this one.

I will update this ticket once the fix is released.

Kind regards,
```

### RCS-28612, de referencia. Sebastian ya publico el suyo a las 17:33, no pegar esto

```
Hi Christine,

Thank you for the transaction examples and for the search you saved. Both let us reproduce the gap
directly.

We found the cause. The delivery fee line was not being generated for the in-store transactions you
flagged.

A fix is built and is now waiting to be deployed to production.

I need nothing further from you on this one.

I will confirm on this ticket once the fix is live.

Kind regards,
```

### RCS-28638, de referencia. Sebastian ya publico el suyo a las 17:34, no pegar esto

```
Hi Christine,

Thank you for your patience.

We found the cause. Proof Type, Order Number and Financial Statement Date were not populating
correctly for the transactions you flagged.

A fix is written and is in code review now.

I need nothing further from you on this one.

I will confirm on this ticket once the fix is deployed.

Kind regards,
```

## Compromiso que el texto de RCS-28702 crea

RCS-28702 debe avisar cuando el fix salga a produccion. Sin fecha, anclado a ese evento.

## Quien pega que

Edwin pega el de RCS-28702. Ya es su ticket y ya escribio la causa.
No se pega desde aca. Jira es de solo lectura para Claude.

## Verificacion aplicada

Los tres textos originales pasaron el checklist de doce puntos de cerebro-respuesta-cliente antes de
saber que Sebastian se adelantaria en dos de los tres. Cero peticiones, cero fechas futuras, cero
guiones, cero parentesis, cero adversativas, voz activa. Saludo contra el reporter real verificado
en Jira, no contra la ficha. Una segunda pasada con un agente independiente confirmo el resultado
sin encontrar violaciones. Esta revision, la de ahora, se hizo releyendo los cinco tickets en vivo
otra vez para confirmar de quien es el ultimo comentario.
