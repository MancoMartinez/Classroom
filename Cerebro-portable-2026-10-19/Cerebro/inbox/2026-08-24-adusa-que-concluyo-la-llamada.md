# ADUSA · qué concluyó realmente la llamada del lunes · 24 ago 2026

## 1. Sobre el informe diario, la llamada no lo pidió

Revisé el transcript completo buscando cualquier mención al tracker o al informe. No hay ninguna. Los únicos dos compromisos de comunicación que se acordaron son estos, ambos al final de la llamada.

Appriss avisa por correo cuáles items pasaron QA, antes del release del jueves. Jim eligió correo cuando le dieron a elegir entre correo y comentarios en los tickets, cita textual: "I think if you email us, let us know, and then we can test Thursday morning".

Check-in el jueves a media mañana para validar juntos, ticket por ticket. Jim: "Why don't we set up a check-in late morning on Thursday and just walk through them together and check them off that way". Quien condujo la llamada del lunes no estará el jueves. Matt confirmó que sí.

La cadencia diaria del tracker nunca vino del cliente. Viene de la instrucción de J.R. del 18 de agosto, cuando el objetivo era recuperar la confianza de una cuenta que amenazaba con irse. Ese objetivo ya se cumplió, Jim abrió la llamada del lunes diciendo que el feedback es positivo y que los 502 se resolvieron. La llamada del lunes reemplazó la cadencia diaria por una cadencia por evento.

Nadie dijo que se dejara de enviar. Nadie lo pidió tampoco.

## 2. Estado real, verificado en vivo esta noche

El tracker que subió Chris es idéntico al anterior, cero celdas distintas. No lo tocó desde el viernes.

El D6 que armé hoy sigue correcto contra Jira. Ningún estado cambió desde que lo generé. No hay que rehacerlo.

## 3. Lo que sí cambió y hay que atender

Tres tickets siguen sin dueño y sin una sola respuesta de Appriss. RCS-28519 desde el 21, cuatro días. RCS-28533 desde el 22, tres días. RCS-28535 desde el 23.

RCS-28535 recibió dos comentarios de Leigh Ann hoy, ninguno contestado. El primero a las 11:43 agregó dos usuarias de Hannaford y tres números de caso. **El segundo, a las 14:11, cambia el diagnóstico por completo.** Cita textual:

"Regarding uploading video, small video clips of 2 minutes or so actually work. The files they have are 11 plus minutes and the system is timing out on uploading the file. The users get to about 60% and then they are receiving the error message of Forbidden."

Esto no es un problema de permisos. Es un timeout de carga en archivos grandes que se manifiesta como error Forbidden alrededor del 60%. Explica por qué el arreglo de RCS-28124 pareció funcionar, los archivos de prueba eran chicos, y por qué el síntoma vuelve con video de body worn camera de once minutos. Es el dato más útil de todo el set y está en un ticket sin dueño.

RCS-28482 sigue sin respuesta desde que Jim corrigió el malentendido el 22 a las 10:33. Hoy además te reenvió las capturas por correo. Las capturas confirman lo que dijo en la llamada: en el reporte roto solo quedan activas DATA SOURCES, FIELDS y PREVIEW, en el reporte que funciona están todas incluida MISC. Un detalle que se ve en las imágenes y que vale como pista, el reporte roto muestra un check "Distinct" y "Results 100", el que funciona muestra "Records". Los dos reportes no son del mismo tipo en Izenda, y el conjunto de pestañas disponibles depende del tipo. Eso es hipótesis mía leyendo las capturas, no está verificado.

## 4. Lo que ya se cerró y no hay que tocar

RCS-28353, RCS-28356 y RCS-28407 quedaron cerrados con la confirmación de Jim en la llamada. RCS-28292 quedó en Under Customer Review con la validación del archivo de tiendas que Jim hizo en vivo a las 16:11. RCS-28123 quedó en Under Customer Review esperando a Leigh Ann.

RCS-28196 sigue en Work in progress. En la llamada quedó en el mismo grupo que RCS-28123, esperando verificación de Leigh Ann. Los dos deberían estar parejos.

## 5. Lo que sale el jueves 27

RCS-28342 el cambio de sync, RCS-28093 el filtro por marca, RCS-28021 el export de Izenda, y tentativamente RCS-28304 el ancho del campo. Todo sujeto a QA. Appriss avisa por correo antes.

## 6. Decisión tomada sobre la cadencia

Se deja de enviar tracker todos los días. A partir de ahora sale solo cuando haya cambio real que reportar, un ticket que cambie de estado o uno nuevo que entre.

Hoy sí hubo cambio real y grande, entraron tres tickets nuevos al tracker y se cerraron cuatro. El D6 ya está generado y refleja la llamada. Enviarlo hoy deja por escrito lo que se acordó en la reunión, que es justo lo que Jim usa para seguir.

Después de hoy, el próximo envío obligado es el correo de QA, miércoles o jueves temprano, con la lista de qué entra al release. Ese sí es compromiso adquirido en la llamada.

Los tres tickets sin dueño se reparten al equipo, RCS-28535 a Edwin Garzon y RCS-28519 y RCS-28533 a Diego Buelvas. Comentarios redactados en `2026-08-24-adusa-traspaso-diego-edwin.md`.
