# RCS-28631 — instructivo

Runbook para decidir y ejecutar el siguiente paso. El ticket es de Luis Hernandez, Juan no es el assignee. Los pasos de escritura en Jira los ejecuta Luis o quien tenga el ticket asignado, nunca Claude.

## Paso 1. Confirmar el estado real antes de mover nada

Donde se ejecuta: Jira, lectura.

El comando o la accion:

Abrir RCS-28631 y verificar en el campo Status y en el campo Assignee.

Que se espera ver: Status = Under Delivery Review, Assignee = Luis Hernandez. El ultimo cambio de Status fue Shandana Khan devolviendolo desde Under Engineering Review, no un evento nuevo. El ultimo cambio de Assignee, a las 17:19 del 3 sep, fue Juan Martinez reasignando a Luis, sin tocar el Status. Esto ya paso por Engineering una vez y volvio.

Si falla: si el status ya cambio a otra cosa, para aqui y avisa a Juan antes de seguir con los pasos siguientes, la base de este instructivo no aplica.

## Paso 2. Verificar que los cuatro requisitos previos de escalacion esten cubiertos

Donde se ejecuta: Jira, lectura, contra el propio ticket.

Que se espera ver, uno por uno:

Entorno de la reproduccion. Cubierto, USPROD, control panel, cliente 138 nordstrom.com.

Pasos de reproduccion con capturas. Cubierto, seis capturas adjuntas y descripcion paso a paso del lightbox de Permissions en el comentario de Luis del 3 sep.

Notas de troubleshooting con el detalle tecnico. Cubierto, el comentario de Luis del 3 sep cita archivos y numeros de linea especificos de ApiController.cs, FileMappingService.cs y VirtualFilePathModule.cs.

Aviso al cliente de que el ticket cambia de cola. No cubierto todavia. Sara Beaty no tiene ningun mensaje que le diga que el ticket se mueve de Delivery a Engineering.

Si falla: si falta el aviso al cliente, redactalo antes de transicionar. Usa la skill cerebro-respuesta-cliente para ese texto, no lo improvises aqui.

## Paso 3. Publicar el comentario de re escalacion antes de transicionar

Donde se ejecuta: Jira, escritura. Autoriza Luis Hernandez.

Que hace este paso: esta es la segunda vez que el ticket va a Engineering. La primera vez Shandana lo rechazo sin que existiera todavia el analisis de codigo. Repetir la transicion sin mencionarla a ella directamente arriesga que lo rebote otra vez sin abrir el hilo. El comentario tiene que citar su propia condicion para que quede claro que se esta respondiendo a eso, no insistiendo a ciegas.

El comando o la accion, bloque listo para pegar, en ingles:

Re-routing back to Engineering per your note above: "feel free to send back to Engineering with supporting details if it's felt this is a platform-level bug though." The supporting details are the code trace in the previous comment, the asymmetric .fti suffix handling between Get and Save in ApiController.cs, which matches the empty Permissions panel on every newly-created FTI item. This is not a team or user permission gap, 900, 901, 902 and 118 fail for every user regardless of team while 116 and 117 do not. Moving to Under Engineering Review, reassigning to you per the escalation procedure. Precedent RCS-28283, same Product Type Secure 5 - EBR, followed the same path once the reproduction pointed to code rather than configuration.

Que se espera ver: el comentario queda visible en el ticket y menciona a Shandana Khan.

Si falla: si el comentario no permite mencionar usuarios de Nordstrom, quita la mencion y deja el texto igual, el contenido ya la nombra.

## Paso 4. Transicionar de Under Delivery Review a Under Engineering Review

Donde se ejecuta: Jira, escritura. Autoriza Luis Hernandez, es su ticket.

Que hace este paso: mueve RCS-28631 con la transicion "Waiting for Engineering" y reasigna a Shandana Khan, exactamente lo mismo que Luis ya hizo una vez el 3 sep antes de que ella lo devolviera. Esta transicion esta disponible ahora mismo sobre el ticket, verificado por API.

El comando o la accion: en la vista del ticket, boton de estado, elegir Waiting for Engineering. Despues cambiar el campo Assignee a Shandana Khan.

Que se espera ver: Status pasa a Under Engineering Review. Se autocrea un ticket ENG vinculado, issuelinks deja de estar vacio esta vez. No hace falta crear el ENG a mano.

Si falla: si ella lo vuelve a devolver a Delivery, no repitas el ciclo sin mas. Pide que conteste puntualmente por que el analisis de codigo no alcanza, y escala esa respuesta a Juan antes de intentar una tercera vez.

## Paso 5. Avisar a Sara Beaty que el ticket cambia de cola

Donde se ejecuta: Jira, escritura, comentario visible al cliente. Autoriza Luis Hernandez.

El comando o la accion: pedir el texto a la skill cerebro-respuesta-cliente antes de pegar nada. Esa skill fija el tono y evita compartir hallazgos internos o fechas no confirmadas. No hay texto listo en este instructivo porque redactarlo aqui saltaria esa regla.

Que se espera ver: el cliente recibe confirmacion de que el ticket avanzo, sin fecha de resolucion prometida.

Si falla: si Luis prefiere no avisar todavia, documentalo en la bitacora como decision explicita, no como omision.

## Paso 6. Cerrar el ciclo en el cerebro

Donde se ejecuta: terminal, dentro de la carpeta Cerebro. Solo Juan o quien tenga acceso a bin/anotar.

El comando o la accion:

bin/anotar RCS-28631 "Ticket de Luis. Analisis de Luis del 3 sep ya documenta bug de codigo en el Save endpoint de FTI. Recomendado pasar de Under Delivery Review a Under Engineering Review con Shandana Khan, precedente RCS-28283."

Que se espera ver: la linea aparece en bitacora/RCS-28631.md con fecha de hoy.

Si falla: si el comando no corre, escribe la nota a mano en bitacora/RCS-28631.md con el mismo texto.

## Transicion sugerida

Waiting for Engineering (id 231), lleva a Under Engineering Review, reasignar a Shandana Khan. Es la segunda vez que se hace esta transicion en este ticket, la primera la revirtio ella misma.

## Comentario interno sugerido, bloque para pegar en Jira

Re-routing back to Engineering per your note above: "feel free to send back to Engineering with supporting details if it's felt this is a platform-level bug though." The supporting details are the code trace in the previous comment, the asymmetric .fti suffix handling between Get and Save in ApiController.cs, which matches the empty Permissions panel on every newly-created FTI item. This is not a team or user permission gap, 900, 901, 902 and 118 fail for every user regardless of team while 116 and 117 do not. Moving to Under Engineering Review, reassigning to you per the escalation procedure. Precedent RCS-28283, same Product Type Secure 5 - EBR, followed the same path once the reproduction pointed to code rather than configuration.
