Facteus, qué respondió Chris y qué falta confirmar

Fecha 2026-09-29. Chris contestó dos veces en el hilo después del correo del 26.

Qué quedó resuelto

El choque de horario quedó resuelto a favor de 00:00 UTC, actualizó la Requirements Specification para que coincida con la página operativa.

Los dashboards, Grafana y el de Saddam, ya tienen link en cada sección de triage de los documentos.

El punto de contacto con nombre quedó resuelto distinto a como se pidió, en vez de una persona más un backup, Chris documentó una ruta de escalación por Jira Operations, antes OpsGenie, hacia todo el equipo de Data Engineering, con instrucciones de cómo crear la alerta bajo Sample Ticket, Escalate To Data Engineering. Es mejor que un solo nombre, si alguien no está, la ruta sigue llegando al equipo.

Qué no contestó

Ninguno de los dos correos confirma cuál SLA aplica, el 1 hora / 24 horas de la Requirements 5.3 o el 1 día hábil de las páginas operativas, ni la cobertura de fin de semana específica para Facteus. El primer correo menciona actualizar el documento "en términos de expectations" pero probablemente se refería al horario, no al SLA. Vale la pena preguntarlo otra vez, sin dar por hecho que ya quedó cubierto.

Qué pide Chris ahora

Que confirmes que revisaste los cambios y que le avises cuándo los líderes senior de L1 están listos para revisar esto con él, para poner fecha al handover completo hacia el resto del equipo de Support.

Texto para el hilo:

```
Hi Chris,

Thanks for turning these around so quickly, everything looks good. The midnight UTC fix matches the
operational pages now, and having the dashboard links directly in each triage section is going to
save people time during an actual incident. The OpsGenie / Jira Operations route to the whole Data
Engineering team is a cleaner answer than a single named contact too, that solves the backup question
on its own.

One thing I don't think either of us confirmed yet, which SLA is the one actually in force for
Facteus, the 1 hour / 24 hour commitment in Requirements 5.3 or the 1 business day in the operational
pages, and whether there's weekend coverage specifically for Facteus or only for the general Data
Issues category. Want to make sure we're not missing that before we bring L1 into this.

We're getting our L1 leads up to speed on our side now. I'll reach back out once they're ready and we
can pick a date for the full handover.

Thanks,
Juan
```
