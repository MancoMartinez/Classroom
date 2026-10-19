# Verificacion de transicion Jira: Work in progress -> Under Customer Review
18 ago 2026

## Pregunta
Los 4 tickets marcados "Resolved" en el tracker pero con status Jira "Work in progress"
(RCS-28177, RCS-28364, RCS-28365, RCS-28415): se pueden mover a "Under Customer Review"
en vez de dejarlos quietos o cerrarlos directo?

## Verificacion (solo lectura, getTransitionsForJiraIssue)
Se consulto el listado de transiciones disponibles para los 4 tickets. Los 4 comparten el
mismo workflow y los 4 tienen la transicion "Under Customer Review" (id 571) disponible:
isAvailable: true, isConditional: false, hasScreen: false (no pide campos obligatorios).

Confirmado en: RCS-28177, RCS-28364, RCS-28365, RCS-28415.

## Recomendacion
Si, moverlos a Under Customer Review es correcto y mejor que mi sugerencia inicial de
esperar sin tocar nada. Esa transicion no afirma que el cliente confirmo por escrito
(eso seria Completed/Closed), solo dice "Appriss ya hizo su parte, esperando que el
cliente lo verifique", que es exactamente el estado real segun la llamada de hoy.

## Como hacerlo (Juan lo ejecuta manualmente, Claude no transiciona ni comenta)
Transicion a usar: "Under Customer Review" (id 571), en cada uno de los 4 tickets.
No pide campos obligatorios (hasScreen: false), asi que es solo click y confirmar.

Comentario sugerido para pegar al transicionar (en ingles, mismo texto para los 4,
ajustando el ticket si se quiere mencionar el contexto puntual):

> Appriss considers this resolved based on today's call. Moving to Under Customer Review
> pending written confirmation from ADUSA.

## Nota aparte (ya senalada en el informe de verificacion del 18 ago)
El borrador de correo a Jim lista como "cuatro para cerrar" a RCS-28177, RCS-28364,
RCS-28378 y RCS-28415, pero RCS-28378 ya tiene status distinto de Work in progress
(no es parte de este grupo de 4), mientras que RCS-28365 si lo es y no aparece en esa
lista del correo. Vale la pena revisar esa lista antes de enviar.
