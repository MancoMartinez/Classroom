# Cosecha 4 sep 2026 — Proceso Pendo / Ideas Portal para feature requests

Sesión fuente: "Pendo definition inquiry" (local_ae0af428), transcripción del 3 sep 2026.

## Hallazgo verificado, proceso

Un ticket de feature request no se desarrolla dentro de RCS. Se mueve a Pendo/Ideas Portal y el RCS se cierra. Es support quien registra el feature request en Pendo/Ideas Portal, el cliente no llena ningún formulario.

Existe un canned response fijo llamado "Ideas Portal Ticket" o "Feature Request Response". Le avisa al cliente que su ticket se movió del RCS al Ideas Portal, que sigue en evaluación aunque el RCS aparezca cerrado, y que recibirá notificaciones si avanza o se convierte en Idea votable.

No existe una transición de Jira separada para Pendo. El cierre usa la transición normal Resolve a Completado. Al poner Complete, dos dropdowns de Resolution Details son obligatorios. Uno de los valores fijos de ese dropdown es exactamente "Feature Request - Pendo Referred". Si algún dropdown queda en "none", el sistema regresa el ticket solo a "additional info needed" y le manda email al assignee.

Proceso completo, en orden: enviar el canned response de Ideas Portal Ticket al cliente, pasar el ticket a Complete, llenar los dos dropdowns con "Feature Request - Pendo Referred" en el que corresponde, y escribir en las notas de resolución qué se registró y dónde quedó. El ticket pasa a Closed después de que el cliente verifica.

## Caso aplicado

RCS-28646, Stephanie confirmó avanzar con dos de tres ítems solicitados, auto populate en No y help text de campos HTML box. Ambos gaps de producto, van a Pendo/Ideas Portal por Luis Hernandez.

No existe un canned response distinto con la palabra "roadmap" en la base de conocimiento. El único es "Ideas Portal Ticket / Feature Request Response".

Fuentes citadas en la sesión: [RCS-28646](https://trebuco.atlassian.net/browse/RCS-28646), [RICED: Scoring Feedback in the Ideas Portal](https://trebuco.atlassian.net/wiki/spaces/PTO/pages/477860069383/RICED+Scoring+Feedback+in+the+Ideas+Portal), [Pendo Requests](https://trebuco.atlassian.net/wiki/spaces/PTO/pages/477476093954/Pendo+Requests).
