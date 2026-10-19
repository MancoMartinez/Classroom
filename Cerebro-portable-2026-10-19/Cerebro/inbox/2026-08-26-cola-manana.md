# Cola de Juan, 26 ago 2026, 15:26 hora Colombia

18 tickets abiertos asignados. Niveles: 1=2, 2=1, 3=7, 4=8.

## Aviso primero. El clasificador dio 64%, no 100%

`bin/eval_cola.py` reporta exactitud 9 de 14. Cuatro de las cinco fallas salen de etiquetas
vencidas, no del lexico. `cola/EVAL-clasificador.json` se fijo el 24 de agosto leyendo el ultimo
comentario de cada ticket ese dia. Juan respondio el 25 en RCS-27765, RCS-28289 y RCS-28482, y el
cliente escribio de nuevo el 26 en RCS-28123. El clasificador esta leyendo el estado real y las
etiquetas quedaron atras. Toca refijar el set de etiquetas contra el volcado de hoy.

La unica falla que merece juicio humano es RCS-28256. El comentario de Juan del 25 de agosto
contiene una promesa, "I will follow up with you on that", y tambien un pedido al cliente. El
lexico coloca el pedido mas cerca del final y manda el ticket a nivel 3. La etiqueta esperaba
nivel 2. Decide tu de quien es la pelota ahi.

## Que cambio desde ayer

Salieron de la cola tres tickets: RCS-28032, RCS-28342 y RCS-27941.

Entraron tres:

- RCS-28223, McDonald's, Restaurant Manager and Crew Cash Audit Questions. Nivel 3.
- RCS-28099, CWH, HYP to RCS Item Discount Logic. Nivel 4.
- RCS-28294, Vallarta, Smart Alerts no Triggering. Nivel 4.

Subio de nivel uno solo: RCS-28123 paso de 2 a 1. Jim Cosseboom escribio hoy.

Bajaron dos: RCS-28289 de 1 a 4 y RCS-28256 de 2 a 3. En ambos Juan respondio el 25 de agosto.

Clientes que escribieron desde ayer: Jim Cosseboom en RCS-28123, hoy 26 de agosto.

## Nivel 1. Te toca responder

### RCS-28123 · ADUSA - Case assignment issues
`Work in progress` · Medium · reporta leighann.stubbs@adusa.com · abierto hace 23 dias

Jim Cosseboom escribio hoy y nadie de Appriss contesto.

Aviso: el cliente no oye nada de Appriss hace 7 dias.

Ultimo movimiento, Jim Cosseboom: "Leigh Ann tested and while it is working, the box that used to
pop-up that confirmed that the case had been assigned and giving the user the option to view/print
report is not appearing instead bringing the user to the workbench."

### RCS-28093 · Ahold - Employees not restricted by Store location
`Under Customer Review` · Low · reporta leighann.stubbs@adusa.com · abierto hace 26 dias

Leigh Ann Stubbs escribio hace 2 dias y nadie de Appriss contesto. Silencio de cara al cliente,
4 dias.

Ultimo movimiento, leighann.stubbs@adusa.com: "Do you have the equivalent of what field or
placement that is on the Employee feed that you receive?"

## Nivel 2. Promesa sin cumplir

### RCS-27991 · Engage Analytics Not Populating Sections
`Work in progress` · High · reporta Paul Marderosian · abierto hace 29 dias

Prometiste un update hace 6 dias y no llego.

Ultimo movimiento, Juan Martinez: "Hi @Paul Marderosian Thank you for the quick responses. To
confirm what I'm working with: You were originally signed in under Harbor Freight, which has since
been migrated to Engage Insights. You're now logged in under F…"

## Nivel 3. Esperando al cliente

- RCS-27676 · RLC - SFTP IP/Hostname Change · pediste algo hace 22 dias · aviso: el cliente no oye nada de Appriss hace 22 dias.
- RCS-27959 · PACSUN - IP Whitelisting para MuleSoft · pediste algo hace 13 dias · aviso: el cliente no oye nada de Appriss hace 13 dias.
- RCS-28122 · Blain's - Not able to make changes to users · pediste algo hace 7 dias · aviso: el cliente no oye nada de Appriss hace 7 dias.
- RCS-28496 · PVH - stores reporting issues logging in · pediste algo hace 4 dias.
- RCS-28282 · Co-op - Intermittent blocked access notification · pediste algo hace 4 dias.
- RCS-28223 · McDonald's - Crew Cash Audit Questions · Matthew Kamminga pidio algo hace 1 dia.
- RCS-28256 · Appriss Incident Time Out(s) and Slow Load times · High · pediste algo hace 0 dias. Nivel en disputa, ver el aviso de arriba.

Los tres primeros pasaron los siete dias. Toca perseguir.

## Nivel 4. En movimiento interno o trabajado sin pegar

- RCS-28153 · BYF - Errors and logging users out · High · aviso: el cliente no oye nada de Appriss hace 15 dias.
- RCS-28327 · Delhaize - Loyalty Discounts not Specified · trabajado sin pegar, lo reportaste el 24 ago · aviso: el cliente no oye nada de Appriss hace 13 dias.
- RCS-28099 · CWH - HYP to RCS Item Discount Logic · aviso: el cliente no oye nada de Appriss hace 8 dias.
- RCS-28021 · Ahold - Unable to use Izenda · silencio de cara al cliente 6 dias.
- RCS-27765 · Winn-Dixie - Data file check · respondido el 25 ago.
- RCS-28482 · AHL/DLZ - Greyed out fields in Izenda · trabajado sin pegar, lo reportaste el 24 ago.
- RCS-28294 · Vallarta - Smart Alerts no Triggering · trabajado el 25 ago, plan de reproduccion en inbox/2026-08-25-rcs-28294-repro-smart-alerts.md.
- RCS-28289 · Vitamin Shoppe - Blocked Users · esperando que Scott vuelva de vacaciones.

## Empieza por RCS-28123

El cliente escribio hoy, el ticket subio a nivel 1, y arrastra siete dias sin oir nada de Appriss.
Es el unico ticket de la cola donde coinciden las tres señales. Jim reporta que la asignacion ya
funciona y que se perdio el pop-up de confirmacion con la opcion de ver o imprimir el reporte. Eso
es un hallazgo nuevo sobre el mismo ticket, no el bug original.

Segundo en fila, RCS-28482 y RCS-28327. Los dos tienen el texto redactado desde el 24 de agosto y
siguen sin pegar en Jira. Cerrar esos dos cuesta minutos y baja dos avisos de silencio.
