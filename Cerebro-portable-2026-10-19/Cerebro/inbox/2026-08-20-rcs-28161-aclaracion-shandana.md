# RCS-28161, aclaración de Shandana Khan, 20 ago 2026

## El ticket

Delhaize, Stores.csv no exportaba desde Manage Stores. Bug de plataforma, no de Izenda.
Confirmado por Matt Kamminga el 19 ago a las 16:31. Fix desplegado a producción hoy 20 ago
a las 09:55, confirmado por Matt y por Viraj.

## Lo que pasó

El 19 ago a las 19:37 Juan comentó directo a la clienta (Leigh Ann Stubbs) confirmando que
ingeniería estaba terminando el fix. En ese momento el ticket seguía asignado a Shandana Khan,
con estado Waiting for Software Release, sin transicionar a Under Support Review.

## La aclaración de Shandana, 20 ago 04:51

Cita textual: "our usual process is for Engineering to internally comment, and update from
Accepted into Development → Under Support Review for Support to communicate/confirm with the
Customer once a given fix is in Prod. Leaving this assigned to me with a status of Waiting for
Software Release has confused this. I'll assign to you to manage comms once the fix is in Prod."

## Qué hizo mal Juan

Juan comunicó al cliente el estado del fix de ingeniería antes de que el ticket transicionara
a Under Support Review. Ese paso marca el traspaso formal de Engineering a Support y evita que
dos personas comuniquen el mismo estado desde dos roles distintos. Comentar mientras el ticket
seguía asignado a Shandana con status Waiting for Software Release generó la confusión que ella
señaló.

## Regla para aplicar

Antes de comentarle a un cliente sobre un fix en desarrollo, verificar el status del ticket.
Si sigue en Accepted into Development o Waiting for Software Release y el assignee es de
Engineering, esperar el comentario interno de Engineering y la transición a Under Support Review.
Comentar recién ahí. Se puede escalar o preguntar por el avance sin ser assignee, pero la
comunicación con el cliente sobre el estado del fix es del que tiene el ticket en Under Support
Review.

Relacionado: reference_escalacion_l3_procedimiento (Secure/Incident Engineering, assignee
Shandana Khan, Under Engineering Review).
