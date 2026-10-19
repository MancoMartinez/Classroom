Facteus, las tres preguntas que dejó L1 en la llamada

Fecha 2026-10-07. Separadas por a quién le corresponde contestarlas.

Pregunta 1, es para Chris, no para Support

Si un cliente deja de enviar datos por un problema de su lado, ¿ese cliente sigue generando alerta a través de Facteus?

La plantilla del ticket de Missing Clients sí trae una variable por cliente, {{ $labels.customer }}, además de staleness_hours y drop_ratio, así que el mecanismo está pensado para alertar por cliente individual, no solo de forma agregada. Pero el umbral exacto que dispara la alerta, el valor de drop_ratio y cuántas horas de staleness por encima de las 26 ya cuentan como problema, nunca quedó confirmado por Chris. Esto se señaló en la revisión del 22 de septiembre y quedó pendiente, no se volvió a preguntar en los correos del 26 ni del 29, que se enfocaron en SLA, horario, escalación y dashboards. Sin ese número, no se puede responder con certeza si el caso que describe L1 dispara la alerta o no. Hay que devolverle esto a Chris.

Preguntas 2 y 3, son decisión de Support, no de Chris

Si llega un correo o alerta de Facteus por un problema de cliente, ¿se debe escalar siempre primero a L2? Y si el cliente reporta el problema directamente como urgente, ¿también se escala a L2?

El árbol de decisión que ya documentó Data Engineering no tiene ningún paso de L2, las alertas internas y los correos externos van directo a Data Engineering por la ruta de Jira Operations. Meter a L2 en el medio sería una capa nueva que Support decide agregar, no algo que Chris tenga que aprobar ni definir. La pregunta real para resolver con Camila y Viraj es si L1 triagea y manda directo a Data Engineering como está documentado hoy, o si quieren que L2 revise primero antes de escalar, y si la urgencia reportada directamente por el cliente cambia esa regla.

Qué hacer con esto

La pregunta 1 se suma a la lista de cosas por confirmar con Chris, junto con el umbral de drop_ratio que ya estaba pendiente desde el 22 de septiembre. Las preguntas 2 y 3 hay que resolverlas internamente antes de decirle nada a L1, no tiene sentido devolverles una respuesta a medias.
