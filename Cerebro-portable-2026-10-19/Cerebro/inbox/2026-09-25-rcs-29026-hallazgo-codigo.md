# RCS-29026 hallazgo de código con Vedant Shirude, 9/25

CONFIRMADO por Vedant Shirude en SmartAlert.vb: el Insert a SmartAlertProcess escribe 'Success' fijo. sendResult de SendEmailAsync no se revisa. Success solo significa que no hubo excepción.
DESCARTADO: la coma. LPSBO SendGridEmail.vb parte toEmail y ccEmail por ",".
El ";" del log sale de tEmailGroup & ";" & tcc. Los managers de la tienda viajan como CC.
HIPOTESIS NUEVA: correo duplicado entre TO y CC. kimberly.WILLIAMS@FoodLion.com está en el Email Group y Kimberly.WILLIAMS@FoodLion.com en el bloque de managers del envío de 10:12 de 0619-27. SendGrid rechaza con 400 una personalization con el mismo correo en to y cc. La alerta de un solo destinatario no tiene CC y sí llegó. Verificar en el log de SendGridEmail la respuesta del 9/20 14:12 UTC.
Aparte y sin explicar: desde el 9/24 hacia las 4:20 PM hora de Leigh no corre ninguna alerta.
Vedant 9/25 1:37 PM: los Warn tampoco se guardan. No hay forma de ver la respuesta de SendGrid del 9/20.
Juan compartió con Vedant RCS-29123, "no alerts today". Posible mismo corte del 9/24, ticket aparte, no mezclar.
