# Facteus, guía para hablar con Viraj mañana

Fecha 2026-09-24. Complementa inbox/2026-09-22-facteus-documentacion-review.md. Todo lo de abajo se verificó hoy directo en Jira, no se copió del review del 22.

## Por qué habla esto con Viraj y no solo con Camila

El 4 de junio de 2026, en la reunión de shadowing, Camila dejó a Viraj y a Juan como responsables de dar seguimiento al acceso de Snowflake mientras ella estaba fuera. Camila dijo ese día que ya existía un ticket de IT abierto para gestionar el acceso, y puso fecha límite el 19 de junio si no se resolvía antes. Fuente: brain/markdown/08-appriss-kt-topic-1-customer-consumer-support.md, reunión 2026-06-04.

Hoy 24 de septiembre, más de tres meses después de esa fecha límite, el acceso de Support a Snowflake sigue sin aparecer concedido para ninguno de los dos en la matriz de accesos del equipo. El bloqueo de Facteus del punto 6 del correo de Chris no es un problema nuevo, es la misma tarea de junio que nunca cerró. Viraj tiene el mismo contexto de origen que tú, por eso conviene alinear con él antes de responder a Chris, no reabrir la historia desde cero con Camila.

## Estado verificado hoy en Jira, línea por línea

**ENG-6450**, "Create Support Process Surrounding Facteus Daily Processing", estado Done. https://trebuco.atlassian.net/browse/ENG-6450

Es el ticket donde Chris fue documentando todo el trabajo desde julio. Su comentario del 15 de septiembre trae la misma lista del correo que llegó al equipo, con checkboxes:

- Marcados listos: triage en el ticket, detalle de datos faltantes, árbol de decisión, definir INTERNAL, definir EXTERNAL, contactos de Facteus, dashboard enlazado.
- Sin marcar todavía: accesos de Support antes del handover, lectura a PRODDATACLOUD, lectura a FACTEUS_DATASHARE, y enviar el correo de feedback de vuelta al hilo.

Ese último punto sin marcar es exactamente lo que Camila está pidiendo con su recordatorio de hoy.

**ENG-9367**, "Handover Support Process", creado hoy mismo por Chris, en Backlog, depende de ENG-6450. https://trebuco.atlassian.net/browse/ENG-9367. Su descripción dice que el handover completo se espera para el sprint de octubre. Este ticket es nuevo, todavía no tiene comentarios.

**RETAILDB-2972**, "Facteus Access For Support Team", estado Open, sin assignee, sin comentarios, creado el 16 de septiembre por Chris. https://trebuco.atlassian.net/browse/RETAILDB-2972. Pide lectura a PRODDATACLOUD.FACTEUS_CONFIG, PRODDATACLOUD.FACTEUS y FACTEUS_DATASHARE completo, más ARDM_PRODUCTION y ARDMPROD si faltan.

**ITHD-9247**, mencionado por Chris el 16 de septiembre en ENG-6450 como el ticket de acceso ya creado. Enlace que dio: https://trebuco.atlassian.net/servicedesk/customer/portal/6/ITHD-9247. Esta cuenta no tiene permiso para abrirlo, Jira responde que no existe o no hay acceso. No se pudo confirmar si ITHD-9247 y RETAILDB-2972 son el mismo ticket con dos numeraciones o dos solicitudes distintas. Viraj puede tener acceso al portal de IT Help Desk donde Juan no lo tiene, pídele que lo abra en la llamada.

**Cronología de la presión de Chris sobre este mismo punto**, todo dentro de ENG-6450:

- 23 de septiembre, comentario de Chris: "Support still need to go over the details. If I do not have an update by today I will chase this up."
- 24 de septiembre, comentario de Chris: "JR and team have been chased today for a response."

Chris ya escaló a JR hoy mismo por el mismo bloqueo. El mensaje de Camila de hoy pidiendo respuesta para mañana llega el mismo día que Chris escala. No es una coincidencia, es la misma presión bajando por dos canales distintos.

**Dashboards que ya existen y responden el punto 8 del correo original.** Chris los dejó en comentarios de ENG-6450 el 28 de agosto, y no estaban visibles desde las páginas de Confluence que se revisaron el 22:

- Dashboard Grafana: https://apprissretail.grafana.net/goto/svsg2j
- Condición de alerta en Grafana: https://apprissretail.grafana.net/alerting/grafana/ffwj8zpezwc1sb/view
- Dashboard de consola, obra de Saddam: https://prd-datacloud-console-app-wus2.azurewebsites.net/

Confirma con Viraj si alguno de los dos ya lo probó, antes de decirle a Chris que el punto sigue abierto.

## Preguntas para dejar resueltas con Viraj, no para corregirle nada a Chris

Pregúntale a Viraj, dejando abierta la posibilidad de que alguno de los dos esté leyendo mal el estado real:

¿Tiene él acceso al portal de IT Help Desk para abrir ITHD-9247 y ver si es el mismo ticket que RETAILDB-2972 o uno distinto?

¿Sabe si alguien de nuestro lado ya respondió algo sobre RETAILDB-2972 fuera de Jira, por Teams o por correo, que no quedó registrado ahí?

Dado que la decisión de junio los dejó a los dos como responsables de este seguimiento, ¿quiere que uno de los dos tome el RETAILDB-2972 como propio esta semana, o prefiere seguir compartiéndolo?

¿Ya probó el dashboard de Grafana o el de Saddam para alguna alerta real de Facteus, o seguimos sin ninguna prueba en vivo del proceso completo?

Con esto resuelto, la respuesta a Chris puede decir con precisión en qué estado está cada pieza, en vez de repetir que el acceso está pendiente sin más contexto.

## Enlaces para tener a mano en la llamada

- Revisión completa del 22 de septiembre: inbox/2026-09-22-facteus-documentacion-review.md
- ENG-6450: https://trebuco.atlassian.net/browse/ENG-6450
- ENG-9367: https://trebuco.atlassian.net/browse/ENG-9367
- RETAILDB-2972: https://trebuco.atlassian.net/browse/RETAILDB-2972
- ITHD-9247 (Juan sin acceso, probar con la cuenta de Viraj): https://trebuco.atlassian.net/servicedesk/customer/portal/6/ITHD-9247
- Matriz de accesos del equipo L2: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/477936910361/
- Requirements Specification, sección 5.3, el SLA: https://trebuco.atlassian.net/wiki/spaces/DS/pages/477211557894/
