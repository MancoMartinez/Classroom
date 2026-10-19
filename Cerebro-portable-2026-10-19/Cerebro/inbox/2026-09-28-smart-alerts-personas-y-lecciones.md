# Smart Alerts sep 2026: quien es quien y lecciones de proceso

## Personas
Kiran Vadday: dev de Nettrack. Encontro el deadlock, hizo el PR 58273, enseno el disparo manual. Escribe corto; mensajes cortos y en forma de pregunta.
Vedant Shirude: dev, reviso SendGridEmail.vb con Juan el 9/25.
Russ Harmon: Infra. SMTP, SendGrid, logs de entrega. SendGrid 7 dias. Limito SMTP a 25MB.
Chris Rippingale: acceso a SendGrid, reviso el 9/25.
Ryan Barlow: participo en el hilo AALPS de RCS-29123.
J.R. Teagle: lead. Pidio on call el 9/27, aprobo solo hacia adelante.
Camila Cortes: pide updates en espanol y ETA para el hilo de correo.
Luis Hernandez: equipo, usa la guia de disparo manual en Vitamin Shoppe.
Vlad Bogus: seguimiento con Russ sobre alertas futuras de tamano.
Ayesha Mehar: levanto alerta a Russ en Jira Ops.
Matthew Kamminga: metodo InProcess del 18 sep en RCS-28294.
Cliente ADUSA: Jim Cosseboom, Director AP, escribe por correo. Leigh Ann Stubbs, reporter de ambos tickets. Dawn Hendry, storepayments.
Cliente Vitamin Shoppe: Joe Austin, RCS-29145.

## Lecciones
1. Buscar en inbox antes de preguntar de nuevo. El procedimiento de Kiran ya estaba escrito y se volvio a pedir.
2. Consultar Jira antes de concluir. RETAILIT ya estaba Closed y el plan decia pedir cerrarlo.
3. No inventar URLs ni servidores. La URL de test de ADUSA no existia. DEVWUS2 no es produccion.
4. Convertir horas: Grafana Bogota, base UTC, cliente ET.
5. Filtrar Grafana por ShopliftingID, no por palabras de negocio.
6. No confundir asunto con alerta: el asunto trae el tipo de caso.
7. Mientras el ticket esta en Infra no se crea ENG. RETAILIT se crea solo y su estado cambia solo.
8. No dar ETA al cliente aunque ingenieria lo de; el deploy se atraso dos veces.
9. El cliente decide si se reenvian alertas perdidas.
10. Con companeros, preguntar en vez de corregir; dejar abierta la posibilidad de estar leyendo mal.
