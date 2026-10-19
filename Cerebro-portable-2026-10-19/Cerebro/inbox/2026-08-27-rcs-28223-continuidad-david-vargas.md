# RCS-28223 McDonald's Cash Audit, continuidad tras la salida de David Vargas

Fecha: 2026-08-27
Ticket: https://trebuco.atlassian.net/browse/RCS-28223
Estado verificado en Jira hoy: Under Support Review, Medium, assignee Juan Martinez.
Labels: Escalated, Uni_Jul_26_SSOMapping.
Reporter: Hugo Cortez, hugo.cortez@us.mcd.com, Field Security Manager US Security.
Abierto el 6 ago 2026. Ultimo comentario: Matthew Kamminga, 25 ago 10:35, sin responder.

## Que verifique y contra que fuente

Jira en vivo via getJiraIssue, 19 comentarios completos. Ficha `tickets/RCS-28223.md` casi vacia,
sin bitacora, sin adjuntos locales. Cerebro barrido por FieldType, AuditSection, cash audit,
McDonald, Audit Workbench.

## El bloqueo exacto

Matthew Kamminga, 25 ago 2026, 10:35:

    @David Vargas , are the affected questions all grid style questions?
    Are you able to provide reproduction steps on how to recreate this error?

David Vargas ya salio de la empresa. Nadie contesto. La escalacion a Engineering esta frenada en
esas dos preguntas. Sin repro, AALPS no toma el caso.

## Que dejo David, con cita

Comentario interno del 24 ago, 18:43:

    Confirmed FieldType 35 (the compound "identify top two managers, dollar amount, action taken"
    control) is the common factor across every reported broken question.
    Manager audit: Q2 (AuditConfigQuestionID Q57), Q4 (Q60), Q6 (Q61) - all FieldType 35.
    Working questions (Q116, Q117, Q118) are FieldType 11 (simple Yes/No).
    ScreenDetail shows no permission/readonly/hidden flag differences between the two field types.
    AuditMasterQuestion (the answer storage table) is generic - one shared Answer/Comments column
    for all question types regardless of FieldType, so there's no schema drift to correct.

Pidio a Engineering reproducir en Test sobre `AuditSection_V24_S4.aspx`, tenant `mcdonalds`.

Comentario al cliente del 24 ago, 18:44: le dijo a Hugo que use el campo Comments como workaround
y que actualizaria con un timeline de fix.

## Los tres huecos que dejo el analisis

1. David nunca reprodujo el defecto. Todo su trabajo es lectura de tablas. No hay URL de una
   auditoria real, no hay usuario de prueba, no hay captura del comportamiento al escribir y
   guardar. Kamminga esta pidiendo justo lo que falta.

2. David solo mapeo las preguntas del Manager audit. La descripcion original de Hugo tambien
   reporta el Crew audit, preguntas 2, 4, 5, 7 y 8. Esas nunca se mapearon a AuditConfigQuestionID
   ni se les verifico el FieldType. Kamminga pregunta si son todas grid. La respuesta no se puede
   dar completa sin cerrar el lado Crew.

3. David nunca dijo que sean grid en el sentido de la UI. Dijo FieldType 35, control compuesto.
   Traducir eso a "grid style question" es una afirmacion sobre el render, no sobre la tabla.
   Confirmar contra la pantalla o contra el PDF adjunto antes de responderle a Matt.

## Errores de estado que hay que corregir en el ticket

El label `Uni_Jul_26_SSOMapping` corresponde al problema de login, no al de audit. El login se
separo a RCS-28486. En 28223 ese label apunta a la causa equivocada.

La primera hipotesis de David, del 13 ago, culpaba el cookie handoff de Platform Cohesion y
vinculaba ENG-6198. Shandana Khan lo desmonto el 19 ago: "reviewed the linked ENG ticket with
@Matthew Kamminga, this and ENG-6198 are not related". Ese vinculo ya se quito. No lo revivas.

## Insumo que resuelve la pregunta de Matt sin acceso a la app

Adjunto en el ticket, subido por Hugo el 13 ago 21:56:
`McDonald's Manager and Crew Cash Audit.pdf`, 599 KB, attachment id 1404097.

Ese PDF es la auditoria completa, Manager y Crew. Sirve para dos cosas a la vez: decir si las
preguntas rotas se renderizan como grilla, y numerar las preguntas de Crew que David nunca mapeo.

## Camino propuesto

1. Bajar el PDF y leer las preguntas rotas de ambas auditorias.
2. Confirmar el FieldType de las preguntas de Crew 2, 4, 5, 7 y 8 en AuditConfigQuestion, tenant
   mcdonalds. Solo SELECT.
3. Reproducir en Test sobre AuditSection_V24_S4.aspx: abrir una auditoria, escribir en una pregunta
   FieldType 35, guardar, capturar el resultado.
4. Redactar la respuesta a Kamminga con la tabla de preguntas, el si o el no sobre grid, y los pasos
   numerados. Usar `cerebro-comentario`.
5. Quitar el label Uni_Jul_26_SSOMapping.

## Pendiente de decision

Reproducir primero y contestarle a Matt con repro completo, o contestarle hoy con lo que hay y
declarar que el repro va aparte. Sin repro el ticket puede volver a rebotar.
