# El estado Escalated en RCS

Verificado el 31 ago 2026 sobre RCS-28671, que estaba en Escalated en ese momento. Antes de esta
fecha el cerebro nunca corrio `getTransitionsForJiraIssue` sobre un ticket en Escalated, asi que
todo lo que se decia de las salidas era deduccion.

## Que es

Del RCS Ticket Status Guide de Kristin, 15 jul 2026, en
`brain/markdown/21-kt-kristin-sign-off-procesos-rts.md`:

> **Escalated.** The ticket has been flagged as requiring elevated attention, typically due to
> urgency, complexity, or customer impact.

Step 7 del Workflow Guide, mismo archivo:

> This is used by the client when the issue is urgent, has high customer impact, or has been stuck
> without resolution for too long. This flags the ticket for senior attention.
>
> CHANGE STATUS WHEN: Escalation is resolved and work resumes --> WORK IN PROGRESS

**El doc oficial documenta una sola salida: Work in Progress, cuando la escalacion se resuelve.**
No contempla el caso de responderle al cliente y quedar esperando.

## Escalated tambien es label, y no es lo mismo

El estado tiene id 10022, statusCategory `indeterminate`, color amarillo. Existe ademas un label
`Escalated`. RCS-28223 tiene el label con estado Under Support Review. RCS-28075 tiene los dos a la
vez. No los confundas al reportar.

## Salidas reales, medidas

Consulta por API sobre RCS-28671 el 31 ago 2026, estado Escalated, tipo Incident:

| Transicion | id | Lleva a | Disponible |
|---|---|---|---|
| Work in progress | 551 | Work in progress | si |
| Under Customer Review | 571 | Under Customer Review | si, sin pantalla |
| Resolution Suggested | 661 | Resolution Suggested | si |
| Waiting for Support | 641 | Under Support Review | si |
| Waiting for Engineering | 231 | Under Engineering Review | si |
| Waiting for Delivery | 601 | Under Delivery Review | si |
| Resolve | 111 | Completed | si, con pantalla |
| Close Ticket | 581 | Closed | **no**, condicional |

Estan tambien las demas rutas a `Under X Review`, todas globales y disponibles. La unica bloqueada
es Close Ticket, igual que desde cualquier otro estado. Cerrar sigue siendo Resolve y despues Close
desde Completed.

**Escalated no es un estado terminal ni bloquea nada.** Tecnicamente sale a donde sea.

## Que hacer despues de responderle al cliente

El principio rector del doc de Kristin manda:

> Key principle: the ticket status must always show who owns the next action.

Por ahi, si le respondiste al cliente y esperas su respuesta, corresponde Under Customer Review.

Hay dos razones para no moverlo apenas comentas:

1. **La escalacion no se resuelve porque tu contestes.** Se resuelve cuando el motivo por el que el
   cliente escalo deja de existir. Si el trabajo de fondo sigue abierto, bajar la bandera el mismo
   dia en que el cliente escalo deja el ticket fuera del radar con el problema vivo.
2. **Under Customer Review pausa todos los SLA y arranca el reloj de auto cierre.** Recordatorios a
   los dias 7, 14 y 28, y cierre automatico pasado el 28. Ver
   `brain/markdown/19-rcs-procesos-playbook.md`. Un ticket escalado que se auto cierra por silencio
   del cliente es un problema que vuelve peor.

Escalated ademas alimenta el Kanban del SCRUM semanal. Olive igual a Escalated, se discute
inmediatamente. Sacarlo del estado lo saca de esa lista.

**Comentar sin cambiar el estado es una accion valida y registrada.** El tracker de ADUSA la anota
asi para RCS-28161: "Comentario, sin cambio de estado".

## Regla practica

Mientras el motivo de la escalacion siga abierto, comenta y deja el estado quieto.

Mueve a Under Customer Review cuando lo unico que falte sea la confirmacion del cliente y el trabajo
interno este cerrado.

Mueve a Work in Progress cuando la escalacion se resuelva y el trabajo siga de tu lado. Esa es la
unica salida que documenta el doc oficial.

## Lo que sigue sin estar escrito

No hay nada escrito sobre si mover un ticket fuera de Escalated requiere aprobacion de leadership, ni
sobre quien aplica el estado en la practica del equipo. El doc dice "used by the client". Preguntalo
antes de bajar la bandera de un ticket que escalo el cliente.

No hay ningun caso previo documentado de Escalated a Under Customer Review. El unico movimiento
fuera de Escalated que aparece es RCS-28022, Santikos, que despues figura en Work in progress, sin
nota de quien lo movio.
