# Cosecha rcs-28671-escalated — 2026-09-01
Fuente: sesión local_bb507016-362f-48fa-9351-2ae2badef68d, "Ticket RCS-28671 review"

## Hallazgos verificados

Juan preguntó qué hacer con un ticket en Escalated después de responderle al cliente. Nunca había
trabajado uno en ese estado. La sesión midió las transiciones reales en vez de deducirlas.

### El doc oficial documenta una sola salida

El RCS Ticket Status Guide de Kristin, 15 jul 2026, vive en
`brain/markdown/21-kt-kristin-sign-off-procesos-rts.md`. Define Escalated como bandera de atención
elevada por urgencia, complejidad o impacto al cliente. Step 7 del Workflow Guide fija el cambio de
estado: "Escalation is resolved and work resumes --> WORK IN PROGRESS". El doc no contempla el caso
de responderle al cliente y quedar esperando.

### Salidas reales, medidas por API

`getTransitionsForJiraIssue` sobre RCS-28671 el 31 ago 2026, estado Escalated, tipo Incident:

| Transición | id | Lleva a | Disponible |
|---|---|---|---|
| Work in progress | 551 | Work in progress | sí |
| Under Customer Review | 571 | Under Customer Review | sí, sin pantalla |
| Resolution Suggested | 661 | Resolution Suggested | sí |
| Waiting for Support | 641 | Under Support Review | sí |
| Waiting for Engineering | 231 | Under Engineering Review | sí |
| Waiting for Delivery | 601 | Under Delivery Review | sí |
| Resolve | 111 | Completed | sí, con pantalla |
| Close Ticket | 581 | Closed | no, condicional |

Escalated no es terminal y no bloquea nada. La única bloqueada es Close Ticket, igual que desde
cualquier otro estado.

El estado tiene id 10022 y statusCategory `indeterminate`. Existe además un label `Escalated` que no
es lo mismo. RCS-28223 trae el label con estado Under Support Review. RCS-28075 trae los dos a la
vez.

### Por qué no se mueve apenas comentas

Under Customer Review pausa todos los SLA y arranca el reloj de auto cierre. Recordatorios a los
días 7, 14 y 28, cierre automático pasado el 28. Fuente `brain/markdown/19-rcs-procesos-playbook.md`.
Un ticket escalado que se auto cierra por silencio del cliente vuelve peor.

Escalated alimenta el Kanban del SCRUM semanal. Olive igual a Escalated, se discute de inmediato.
Sacarlo del estado lo saca de esa lista.

Comentar sin cambiar el estado es acción válida y registrada. El tracker de ADUSA la anota así para
RCS-28161: "Comentario, sin cambio de estado".

### Regla práctica fijada

Mientras el motivo de la escalación siga abierto, comenta y deja el estado quieto. Mueve a Under
Customer Review cuando lo único que falte sea la confirmación del cliente y el trabajo interno esté
cerrado. Mueve a Work in Progress cuando la escalación se resuelva y el trabajo siga de tu lado. Esa
última es la única salida que documenta el doc oficial.

Todo esto quedó escrito en `flujos/estado-escalated.md`.

### Corrección registrada

La sesión afirmó primero que el ticket "se queda en Escalated". Esa afirmación no venía de la
documentación. Salió del archivo del ticket que la misma sesión escribió ese día. Se corrigió
después de correr las transiciones. Regla que deja el caso: no cites una salida de estado de memoria
ni de un archivo propio del mismo día. Mídela.

### Alcance del retest de RCS-28671

Se retesteó 1 búsqueda de las cerca de 150 que Simon Smith reparó. Simon escribió el 31 ago 12:26
que quedan 50 búsquedas públicas sin investigar y que las de usuario siguen sin tocar. Corey Wood
escribió a las 11:54 que el problema puede estar creciendo. La causa raíz la trabaja Simon en
DO-12041.

Precedente que bloquea la edición: en Kinney Drugs, editar el campo por Composer subió los fallos de
3 de 30 a 11 de 30. No toques Composer mientras Simon repara.

Detalle completo del retest en `inbox/2026-08-31-rcs-28671-thd-searches-snowtime.md`. Textos
pegables en `inbox/2026-08-31-rcs-28671-comentario-interno.md` y
`inbox/2026-08-31-rcs-28671-respuesta-corey.md`.

## Pendiente de verificar

No hay nada escrito sobre si bajar la bandera de un ticket que escaló el cliente requiere aprobación
de leadership. El doc dice "used by the client". Peyman fue quien pidió avanzar. Pregúntaselo a él
antes de mover el estado.

No existe caso previo documentado de Escalated a Under Customer Review. El único movimiento fuera de
Escalated que aparece en la base es RCS-28022, Santikos, que después figura en Work in progress sin
nota de quién lo movió.

Compromisos vivos: Juan le debe a Corey una respuesta cuando sus usuarios reconfirmen, y le debe a
Simon retestear lo que le mande.
