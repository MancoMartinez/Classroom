# Plan de revisión de la cola, verificado ticket por ticket contra Jira

Generado 2026-09-04 14:00 aprox. Los 19 tickets abiertos se leyeron en vivo con getJiraIssue, comentario por comentario, no por el clasificador de bin/cola.py. El clasificador se equivocó en varios. Quedan marcados abajo.

Orden de barrido: prioridad de Jira primero, Critical arriba, después High, Medium, Low. Dentro de cada prioridad, primero lo que tú debes, después lo que el cliente te debe ordenado por antigüedad del silencio, al final lo que está en trámite interno sin nadie esperando.

No hay tickets Critical hoy. Jira no trae fecha de vencimiento cargada en ninguno de los 19 tickets, el campo duedate está vacío en todos. El único proxy real de SLA es la automatización de Jira Service Management, que manda aviso al asignado a los 7 días de silencio del cliente y a los 14 días con advertencia de cierre automático. Ese aviso aparece como comentario y se usa abajo como el dato de antigüedad real.

## HIGH, 3 tickets

### RCS-28153, BYF, errors and logging users out
Lo que debo: contarle a Ashley que el fix real, ENG-7184, se liberó el 27 de agosto. Ella nunca lo supo, el último mensaje tuyo a ella es del 11 de agosto.
Lo que me deben: nada pendiente de su parte en el sentido estricto, el estado Under Customer Review es correcto, Ashley nunca confirmó si el timeout de 240 minutos resolvió el problema original.
Pendiente real: Jira ya mandó dos avisos automáticos de inactividad del cliente, 7 y 14 días, el segundo el 25 de agosto advirtiendo cierre automático. El riesgo es que el ticket se cierre solo sin que Ashley sepa que hay un fix nuevo. Publica el update hoy.

### RCS-28671, THD, Searches Producing only Errors
Lo que debo: terminar de verificar el repoblado del lado de fti.Transactions y publicar el cierre. Se lo dijiste a Ericka Smith hace 20 minutos, "I need nothing further from you on this one."
Lo que me deben: nada, la conversación está en tu cancha por decisión tuya.
Pendiente real: cerrar el loop de verificación y comentar. Sin riesgo de cierre automático, prioridad alta real.

### RCS-28753, Nike, Manual Discount Amount field
Corrección sobre lo que reporté antes. Esta mañana marqué este ticket como promesa sin cumplir. Ya no es así. Damir de Nike y Peyman Motlagh de Ingeniería tuvieron un intercambio técnico completo hoy mismo, 11:18, 11:55 y 13:41. Peyman ya respondió la última pregunta de Damir con el detalle exacto.
Lo que debo: nada urgente. Verifica que la respuesta de Peyman cierre el tema para Nike, sin acción tuya inmediata.
Lo que me deben: la siguiente pregunta de Damir si la tiene, no hay debt tuyo activo ahora mismo.

## MEDIUM, 14 tickets

### Lo que debo, atender primero

RCS-28342, Ahold-Delhaize, employee data missing from profile. Un segundo usuario reportó el mismo problema de título faltante hoy a las 18:12 de ayer. Solo respondió la automatización, ningún humano. Aplica el mismo fix de Kiran del caso anterior y contesta a leighann.

RCS-28327, Delhaize, Loyalty Discounts not Specified. Corrección: el sistema lo marca en movimiento interno sano, no lo es del todo. Edwin Garzon encontró la causa raíz el 20 de agosto, falta el workbook de enumeraciones CRDM 2.0 para el cliente 46. Nadie escaló ese hallazgo a quien administra el contenido de Secure para ese cliente. Quince días sin movimiento sobre un root cause ya identificado. Escala eso, no es que falte investigar, falta empujar la corrección.

RCS-28756, Appriss Internal, Nike ECOM Load issue. Ganesh Nayak creó el ticket el 3 de septiembre a pedido de Peyman Motlagh y nadie lo ha tocado desde entonces. Cero triage. Asígnalo o comienza la investigación.

### Lo que me deben, ordenado por antigüedad del silencio

RCS-27959, PACSUN, IP whitelisting MuleSoft. Pediste que probaran ambas conexiones el 12 de agosto. Aviso de cierre automático por 14 días de silencio el 26 de agosto. 22 días sin respuesta.

RCS-28122, Blain's, cambios a usuarios. Pediste confirmar si Admin Tools y el problema de Compliance Audit quedaron resueltos el 19 de agosto. Aviso de cierre automático el 2 de septiembre. 15 días sin respuesta real a esa pregunta puntual, aunque James escribió un mensaje vago el 13 de agosto.

RCS-28282, Co-op, notificación de acceso bloqueado. Pediste la lista de países a permitir o bloquear el 21 de agosto. Dos avisos automáticos, el más reciente hoy mismo advirtiendo cierre en 14 días. 13 días sin la lista.

RCS-28496, PVH, login en desktop e iPads. Tu colega Rajith pidió screenshots y detalles el 20 de agosto, tú confirmaste que esperabas esa respuesta el 21. Aviso de cierre automático el 3 de septiembre. 13 días sin la información.

RCS-28289, Vitamin Shoppe, Blocked Users. Joe Austin avisó que Scott vuelve de vacaciones y le daría seguimiento, el 24 de agosto. Aviso de 7 días el 1 de septiembre. 9 días esperando ese seguimiento.

RCS-27791, Guess, Audit Question en Grid Style. El fix de ingeniería ya se aplicó, tú le pediste a Stephanie confirmar el 2 de septiembre. 2 días, todavía sin aviso automático, sin urgencia real.

RCS-28099, CWH, Item Discount Logic. James McKenna avisó el 17 de agosto que siguen reuniendo datos y que tomará tiempo. Tú acusaste recibo. Cliente trabajando, no hay pregunta abierta de tu parte.

RCS-27765, Winn-Dixie, data file check. El cliente confirmó hoy mismo, vía Shireesh, que reenvían el archivo faltante el miércoles 9 de septiembre a las 10 am. No hay nada que perseguir hasta esa fecha. Corrección sobre el reporte de esta mañana, este no es un ticket de deuda tuya ni suya, es una fecha en el calendario.

### En movimiento interno, nadie espera

RCS-28294, Vallarta, Smart Alerts no Triggering. Corrección importante. Este ticket no es una deuda tuya urgente. El último mensaje de Tatiana es un agradecimiento por lo del navegador, no una pregunta sin contestar. El problema real de fondo, las Smart Alerts, está escalado a Ingeniería con Shandana Khan desde el 27 de agosto, con un candidato de causa raíz identificado, ENG-7359. Dale seguimiento a la escalación de ingeniería, no lo trates como si el cliente estuviera esperando tu respuesta.

RCS-27941, Tailored Brands, SSO/Permissions. Corrección importante. Colton Neal dijo explícitamente el 3 de septiembre "I will work on this and get back to you next week." La pelota está en su cancha, no en la tuya. No es nivel de urgencia alta hoy.

RCS-28581, CWH, POS Number regresó a mapeo previo. James McKenna mandó un mensaje de cortesía el 3 de septiembre, sin pregunta pendiente. Tu investigación sobre DO-9495 sigue activa. Continúa cuando puedas, sin presión de cliente.

## LOW, 2 tickets

RCS-28482, AHL/DLZ, campos grises en Izenda. Esto no es esperar al cliente pese a lo que decía la cola de esta mañana. Mohammed Mutahhar es de Ingeniería, no es el cliente. Shandana Khan lo asignó hoy a las 4 am como SRE de turno. Mohammed dio una hipótesis técnica a las 8:30 am y te pidió textualmente "could you confirm above and let the client know please." La prioridad en Jira es Low, la urgencia real no lo es, J.R. Teagle pidió esta escalación en la llamada del 3 de septiembre. Verifica la hipótesis de Mohammed hoy y comunícasela a Jim Cosseboom.

RCS-27676, RLC, SFTP IP/Hostname Change. Pediste el Public IP view de Azure o confirmación de NAT Gateway el 4 de agosto. 31 días sin respuesta, es el silencio más largo de toda la cola. Prioridad Low en Jira, pero por antigüedad vale la pena un último empujón antes de dejarlo morir.

## Orden de barrido sugerido para hoy

1. RCS-28342, nivel 1 real, cliente nuevo sin contestar.
2. RCS-28153, High, comunicar el fix antes del cierre automático.
3. RCS-28671, High, cerrar la verificación que ya está en curso.
4. RCS-28482, Low en Jira pero con Ingeniería esperando que tú actúes desde esta mañana.
5. RCS-28327, escalar el root cause de Edwin que lleva quince días parado.
6. RCS-28756, triage del ticket interno sin dueño.
7. De ahí en adelante, los que están esperando al cliente por antigüedad: 27959, 28122, 28282, 28496, 28289, 27676.
8. Los que están bien como están, sin acción hoy: 28753, 27941, 28294, 27791, 28099, 27765, 28581.
