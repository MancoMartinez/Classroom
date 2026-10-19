Facteus, respuesta final a Chris, alineada con Viraj

Fecha 2026-09-25. Viraj respondió al mensaje del 24 y confirmó los seis puntos, agregó uno nuevo, Product type y Problem selection en los tickets, un campo que ningún documento de Chris especifica para Facteus. Con eso Support queda alineado, este es el texto listo para pegar en el hilo de Chris.

Puntos que cubre, los seis de Viraj más el suyo propio:

1. Cuál SLA aplica, el 1hr/24h de la Requirements Specification o el 1 día hábil de las páginas operativas.
2. Cobertura de fin de semana.
3. Qué puede cerrar Support sin escalar.
4. Un technical owner y un backup con nombre.
5. El choque de horario, 00:00 contra 01:00 UTC.
6. Product type y Problem selection en los tickets de Facteus.
7. Acceso, RETAILDB-2972 sigue abierto, con la duda de si ITHD-9247 es el mismo ticket.

Texto para el hilo:

```
Hi Chris,

Thanks again for putting this together, the team found the documents genuinely useful. Viraj and I
went through everything together and here's where we landed.

The access request, RETAILDB-2972, is still Open and unassigned on our side. We're also trying to
confirm whether ITHD-9247, the one you mentioned creating on the 16th, is the same request or a
separate one, we'll follow up on that directly so it doesn't stay blocked.

A few open points we'd like to align on before the October handover.

Requirements section 5.3 sets a 1 hour notification and a 24 hour fix or update commitment. The
operational pages set the expectation at 1 business day. Could you confirm which one is the actual
commitment in force, and whether there's weekend coverage for Facteus specifically, or only for the
general Data Issues category?

The decision tree currently routes every ticket, internal or external, to Data Engineering. Is there
any category Support is expected to resolve and close on its own? If not, that's fine, we'd just like
it documented that way. Either way, having a named technical owner and backup on your side would help
us know who to follow up with.

Small one, the Requirements Specification says the process runs at 01:00 UTC, the Process Not Run
Within 24 Hours page says 00:00 UTC. Probably just needs one of the two updated.

Last thing, when a Facteus ticket gets created or triaged, what Product type and Problem selection
should we be using? Neither the internal nor the external process page specifies it, and we'd like
to keep these consistent from the start.

Happy to walk through any of this on a call if that's easier than the thread.

Thanks,
Juan
```
