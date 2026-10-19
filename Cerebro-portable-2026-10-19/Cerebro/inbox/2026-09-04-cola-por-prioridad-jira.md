# Cola reordenada por prioridad de Jira, 2026-09-04 14:44

## Exactitud del clasificador

La evaluación cayó a 88 por ciento, 15 de 17 casos correctos. Dos fallas.

RCS-28753 quedó en nivel 4. Corresponde a nivel 2, promesa sin cumplir. El único comentario es el triage automático de Akshaya Purappemane, el léxico no lo lee como respuesta de Appriss.

RCS-27765 quedó en nivel 3. Corresponde a nivel 4. Juan ya contestó, "the email has been replied to and we will be monitoring the thread". El comentario más reciente es de Shireesh Ramdas reenviando un correo del cliente, el léxico lo lee como pregunta sin responder cuando ya se respondió antes.

Corrige estos dos manualmente en tu cabeza al leer la lista de abajo. RCS-28753 pesa más de lo que muestra su nivel. RCS-27765 pesa menos.

## Criterio de orden

Jira no trae SLA por ticket en los campos que se leen hoy. El proxy de urgencia es prioridad de Jira primero, nivel de deuda con el cliente segundo, días de silencio de Appriss tercero.

## HIGH, 3 tickets

RCS-28753. Nike, Manual Discount Amount field. Etiqueta del sistema EN MOVIMIENTO INTERNO, corrige a PROMESA SIN CUMPLIR por la falla de arriba. Peyman ya mandó a Nike la explicación técnica del cálculo hoy, revisa si falta cerrar el hilo con el cliente antes de darlo por resuelto.

RCS-28671. THD, Searches Producing only Errors. TRABAJADO SIN PEGAR EN JIRA. Causa raíz cerrada hoy, Juan ya le dijo al cliente que no necesita nada más de su parte. Pendiente exclusivo, pegar el comentario en Jira.

RCS-28153. BYF, errors and logging users out. TRABAJADO SIN PEGAR EN JIRA desde el 27 de agosto. El cliente lleva 24 días sin oír nada de Appriss y el fix ya está liberado en producción, ENG-7184 Done desde el 27 de agosto. Es la deuda más vieja de todo High, pégalo hoy.

## MEDIUM, 14 tickets

Te toca responder.

RCS-28294. Vallarta, Smart Alerts no Triggering. Tatiana Barcenas escribió hace 1 día, nadie de Appriss contestó.

RCS-27941. Tailored Brands, SSO/Permissions Issues in Incident. Colton Neal escribió hoy, nadie de Appriss contestó.

RCS-28342. Ahold-Delhaize, employee data missing from profile. leighann.stubbs escribió hoy. El cliente lleva 9 días sin oír nada de Appriss, alerta activa.

Esperando al cliente, ordenado por días de silencio.

RCS-27959. PACSUN, IP whitelisting MuleSoft. 22 días sin respuesta del cliente.
RCS-28122. Blain's, cambios a usuarios. 15 días sin respuesta.
RCS-28496. PVH, login en desktop e iPads. 13 días sin respuesta.
RCS-28282. Co-op, notificación de acceso bloqueado. 13 días sin respuesta.
RCS-28289. Vitamin Shoppe, Blocked Users. 9 días sin respuesta.
RCS-27765. Winn-Dixie, data file check. El sistema lo marca esperando al cliente, la falla de arriba dice que ya está resuelto de tu lado. Shireesh reenvió hoy la fecha que dio el cliente, 9 de septiembre, para el reenvío de datos. No hay acción tuya pendiente, solo seguimiento a esa fecha.

En movimiento interno.

RCS-28099. CWH, Item Discount Logic. 17 días sin contacto al cliente, sin nada pendiente de tu lado.
RCS-28327. Delhaize, Loyalty Discounts not Specified. 7 días, investigación activa.
RCS-27791. Guess, Audit Question en Grid Style. 2 días, sin pendientes.
RCS-28756. Appriss Internal, Nike ECOM Load issue. 1 día, sin pendientes.
RCS-28581. CWH, POS Number regresó a mapeo previo. Sin pendientes de cara al cliente.

## LOW, 2 tickets

RCS-28482. AHL/DLZ, campos grises en Izenda. Mohammed Mutahhar te mencionó directo hoy con la causa técnica. Baja prioridad en Jira, pero la mención directa pide respuesta tuya para armar el comentario y escalar como quedó acordado con J.R.

RCS-27676. RLC, SFTP IP/Hostname Change. 31 días sin respuesta del cliente, la deuda más vieja de toda la cola. Baja prioridad en Jira, considera perseguir de todos modos por la antigüedad.

## Recomendación

Empieza por RCS-28153. Es High, el cliente lleva 24 días sin saber que el fix ya está liberado, y la única acción pendiente es pegar el comentario. Cierra esa deuda antes de tocar cualquier ticket Medium.
