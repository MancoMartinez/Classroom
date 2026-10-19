Facteus, correo final para Chris, con la llamada de ayer con Viraj

Fecha 2026-09-26. Se te quedó pendiente ayer, este es el texto listo para enviar hoy. Asunto que dio Viraj en la llamada: "Facteus - Support handover - doc review".

Qué cambió con la llamada frente al borrador del 24

ITHD-9247 y RETAILDB-2972 quedaron confirmados como el mismo ticket, Viraj lo verificó cruzando el historial. Ya no es una pregunta abierta para Chris.

Viraj va a abrir hoy un ticket de IT nuevo para pedir acceso de lectura para todo el equipo de Support, no solo para los dos, a los esquemas PRODDATACLOUD.FACTEUS_CONFIG, PRODDATACLOUD.FACTEUS y FACTEUS_DATASHARE.

El punto de Product type y Problem en los tickets de Jira ya no es una pregunta para Chris, es algo que ustedes crean del lado de Support con ayuda de Camila. Se saca del correo.

Se agrega un punto nuevo, si el equipo L1 debería monitorear las alertas de Facteus igual que monitorea todo lo demás, y proponer meter a alguien de L1 en la siguiente llamada.

Sigue abierto, sin cambios de la llamada: el SLA de 1 hora o 24 horas contra 1 día hábil, la cobertura de fin de semana, un punto de escalación con nombre y su backup, y el choque de horario 00:00 contra 01:00 UTC.

Texto para el correo:

```
Hi Chris,

Thanks again for putting this together, the team found the documents genuinely useful. Viraj and I
went through everything together, including a call yesterday, and here is where we landed.

The access request, RETAILDB-2972, is the same request as ITHD-9247, we confirmed it against the
ticket history. Viraj is opening a new IT ticket today to extend read access to the full support
team for PRODDATACLOUD.FACTEUS_CONFIG, PRODDATACLOUD.FACTEUS and FACTEUS_DATASHARE, so this should
move forward from our side this week.

A few open points we would like to align on before the October handover.

Requirements section 5.3 sets a 1 hour notification and a 24 hour fix or update commitment. The
operational pages set the expectation at 1 business day. Could you confirm which one is the actual
commitment in force, and whether there is weekend coverage for Facteus specifically, or only for the
general Data Issues category?

We would like a named escalation point of contact on your side, plus a backup for when that person
is not available, including who covers on call over the weekend if an urgent Facteus ticket comes in.

Small one, the Requirements Specification says the process runs at 01:00 UTC, the Process Not Run
Within 24 Hours page says 00:00 UTC. Probably just needs one of the two updated.

Last thing, we found two dashboards you mentioned in comments on ENG-6450 that were never linked
from Confluence, the Grafana one and the console view Saddam built. We are also looking into whether
our L1 team, who already monitors alerts for every other product, should pick up Facteus monitoring
as well. We would like to bring one of the L1 leads into a follow up call next week to align on this,
along with the SLA and escalation points above.

Happy to walk through any of this on a call if that's easier than the thread.

Thanks,
Juan
```
