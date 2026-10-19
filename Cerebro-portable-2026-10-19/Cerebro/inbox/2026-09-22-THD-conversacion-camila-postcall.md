# THD. Para hablar con Camila después de la llamada

22 de septiembre de 2026. Base principal: grabación 15 completa, 20:24. Complemento: grabación 14 completa, 35:01. Transcripción automática local; tiempos relativos a cada archivo. Jira verificado durante este análisis. Las afirmaciones del cliente y de Camila conservan su atribución; no sustituyen pruebas de Ingeniería.

[Qué decirle](#conversacion) · [Qué cambió](#hallazgos) · [Qué confirmar](#acciones) · [Correcciones](#correcciones) · [Otros pendientes](#otros) · [Fuentes](#fuentes)

<a id="conversacion"></a>
## Para abrir la conversación

Camila, me quedé con que Matt necesita volver a confiar en el reporte para identificar faltantes reales. Hoy puede encontrar todos los artículos en el recibo y seguir viendo una discrepancia en el total calculado. Además, reportó lo mismo con Total Item Quantity. Yo pondría esos dos campos en la validación de cada recarga y pediría confirmar qué fechas quedaron conciliadas, especialmente el 22, que durante la llamada todavía estaba pendiente de confirmación.

Lo de las tres y cuatro horas tiene otro sentido al que inicialmente interpretamos con la captura. Matt considera rápida la carga y quiere confirmar que esperamos el marker file, que indica que THD terminó de entregar el lote. Él mismo dijo que es una teoría. Podemos revisar esa secuencia con Infraestructura sin dar por hecho que ahí está la causa.

Para el correo de mañana, alinearía contigo qué podemos respaldar sobre la expectativa de fin de semana, quién queda a cargo del monitoreo diario y qué respuesta nos falta de Ingeniería. También separaría la recuperación de los work items del arreglo del timeout, porque hoy tienen estados diferentes.

<a id="hallazgos"></a>
## Lo que cambió con las grabaciones

| Tema | Qué sabemos ahora | Qué significa para nosotros |
| --- | --- | --- |
| Total Item Sale Amount | Matt observa recibos completos e importe calculado discrepante. Sospecha que la recarga no actualiza el campo. Audio 15, 00:00 a 01:55. | RCS-28968 sigue siendo el caso principal. Camila también describe esa falta de recálculo en audio 14, 14:47 a 16:33, y menciona a Andres haciendo el rebuild. Falta respaldo técnico del mecanismo y del despliegue. |
| Total Item Quantity | Matt reporta cantidad 1 con 3 artículos visibles en recibo. Dice que en ese momento ya no ve discrepancias tras la recarga. Audio 15, 05:07 a 07:04. | Añadir este campo al alcance de revisión. Validar cantidades según su definición, sin asumir que número de líneas siempre equivale a unidades. |
| Otros calculados | Menciona campos de transacción anterior y siguiente como candidatos. Camila prioriza los dos anteriores y revisará el resto después. Audio 15, 07:04 a 09:17 y 13:03 a 13:57. | No decir que todos esos campos fallan. Acordar inventario y pruebas posteriores a recarga. |
| Tres y cuatro horas | THD envía lotes cada 4 h. Matt observa unos 3 a 3,5 h de atraso y recuerda 5 a 8 h antes. Pregunta si extraemos antes de terminar el lote. Audio 15, 09:17 a 17:49. | Corrige nuestra lectura provisional de la captura. No estaba pidiendo simplemente cargar más rápido. |
| Marker file | Según Matt, THD publica este archivo cuando termina el lote en GCS. Estima unos 30 min para prepararlo. Audio 15, 11:53 a 12:34 y 14:03 a 15:55. | Revisar marcador, extracción e ingestión del mismo lote. Matt reconoce expresamente que su explicación es una teoría. |
| Compromiso siguiente | Camila promete correo mañana 23 sep con resumen y novedades disponibles. Audio 15, 18:52 a 19:59. | Es compromiso de actualización. No prometió resolver todo mañana. |

Un lote cada 4 h puede contener transacciones mucho más recientes. Matt lo aclara a 14:03. El promedio de atraso, la antigüedad de la última transacción y la frecuencia de envío miden cosas distintas. Ninguno demuestra por sí solo que ignoremos el marcador.

<a id="acciones"></a>
## Lo que conviene concretar con ella

| Con quién coordinar | Pregunta concreta | Evidencia que necesitamos |
| --- | --- | --- |
| Bikash, Andres y Datos, RCS-28968 | ¿Qué fechas y campos quedaron corregidos? ¿Quién confirma el 22? | Misma transacción antes y después: Subtotal, detalle, recibo, Total Item Sale Amount y Total Item Quantity. Usar el ejemplo 4909, tienda 8918, registro 51, ID 2609210101525048961. |
| Responsable del arreglo permanente | ¿Qué mecanismo falla, cuál es el ticket técnico y qué respalda la expectativa de esta semana? | Dueño, alcance, pruebas, despliegue previsto y validación de una carga nueva sin intervención. Separar del arreglo de suspendidas. |
| Datos e Infraestructura | ¿La extracción espera el marker file del lote correcto? | Horas con zona de publicación del último archivo, marcador, extracción, carga y recálculo; archivos esperados frente a recibidos. No retrasar cargas a ciegas. |
| Responsable de la contención | ¿Quién revisa cada día y cuándo avisa a Camila? | Horario, resultado, recarga si hace falta y conciliación de todos los campos dependientes. Revisar el SOP de recarga y recibos ya prometido en RCS-28649. |
| Shandana e Ingeniería | ¿Podemos recuperar el work item señalado antes del arreglo general? | Plan de ENG-8659, responsable y preservación de notas/asignaciones. Verificar los 17 históricos; no mezclarlos con 25 trabajos de cola. |
| Mohammed y responsable de ENG-8650 | ¿Qué falta para publicar y validar el timeout? | Fecha efectiva, prueba y alcance. La versión 24 sep sigue sin publicar. No es ETA del datafeed. |

<a id="correcciones"></a>
## Precisiones para el próximo mensaje

1. Fin de semana. Camila lo expresó como expectativa a 02:55 y 03:11 del audio 15. Hasta obtener respaldo de Ingeniería, mantener esa diferencia frente a una ETA confirmada. El cliente ya escuchó esa expectativa.
2. Recarga del 22. El correo previo daba por recargado 20 a 22; a 03:11 del audio 15 Camila aún esperaba confirmación del 22. Puede tratarse de etapas distintas. Confirmar si falta carga, recálculo o validación antes de repetir que todo quedó correcto.
3. Work items. En audio 14, 03:03 a 04:20, la explicación de Accepted into Development sugirió arreglo listo esperando publicación. ENG-8659 sigue Backlog, sin asignado ni versión. ENG-8650 sí está Development Complete. Corregir la explicación para cada caso.
4. Causa única. La llamada no demuestra que marcador, faltantes, calculados, suspendidas y búsquedas lentas compartan causa. Tampoco demuestra que Snowflake explique por sí solo la mejora de tiempos.
5. Validación completa. Un recibo completo resuelve una parte del problema. Matt necesita que los campos de búsqueda y monitoreo también concilien para distinguir errores reales.

<a id="otros"></a>
## Otros pendientes de la primera grabación

Comunicación y SOP, audio 14, 16:33 a 26:52. Ericka pide instrucciones para que cada corrección incluya todas las salidas afectadas; recuerda problemas de marzo. Camila ofrece revisar esa historia con Valerie y reforzar el SOP. Corey valora la respuesta de Soporte y pide avisos antes de que sus usuarios descubran el impacto. Ericka señala interrupciones en los avisos; Corey también reconoce mejora reciente. Acordar una próxima actualización incluso cuando siga pendiente la ETA. Esto afecta la confianza del cliente y merece espacio en la conversación.

RCS-28008, audio 14, 00:13 a 02:27. Corey dice que Transaction ID sigue vacío al cruzar Work View con Secure pese a la conversión a entero. Jira confirma Completed para el cambio original, con despliegue anunciado 13 ago. Valerie pidió un ticket nuevo con capturas y ofreció vincularlo. Falta identificar ese nuevo número. No mezclarlo con RCS-28968.

Engage, audio 14, 05:25 a 10:36. Ericka quiere incluir a su equipo en la sesión de feedback. También plantea cómo explicar campos vacíos de los recibos. Quedó abierta la actualización de su guía de campos y una conexión entre equipos legales si la necesitan. No hay cambio de plantilla acordado.

Reporte antiguo, audio 14, 11:45 en adelante. Ericka propone desactivar el reporte de faltantes que considera poco fiable. En el segmento revisado no identifican al responsable ni ejecutan la desactivación. Confirmar alcance antes de actuar. No confundir retirar una notificación con resolver el problema de datos.

Otros seguimientos, audio 14, 27:13 a 33:14. Corey coordinará con Denver información de CIT y horarios de la visita/SBR. También preguntan por watchlist de tarjetas en el roadmap de Engage y por precios de Sidekick; Valerie consultará a Joe sobre estos últimos. No hay fecha de producto ni precio confirmados. Mencionan tickets antiguos para limpieza; los números no quedan suficientemente claros en la transcripción para recomendar cierres. Confirmarlos con Ericka.

<a id="fuentes"></a>
## Fuentes para volver al detalle

[Audio principal 15](</Users/MancoMenStudio/Downloads/Carrera 73 15.m4a>) · [Transcripción 15](/Users/MancoMenStudio/Cerebro/adjuntos/THD-2026-09-22/Carrera-73-15.srt) · [Audio 14](</Users/MancoMenStudio/Downloads/Carrera 73 14.m4a>) · [Transcripción 14](/Users/MancoMenStudio/Cerebro/adjuntos/THD-2026-09-22/Carrera-73-14.srt).

[RCS-28968](https://trebuco.atlassian.net/browse/RCS-28968), Under Customer Review. [ENG-8659](https://trebuco.atlassian.net/browse/ENG-8659), Backlog. [ENG-8650](https://trebuco.atlassian.net/browse/ENG-8650), Development Complete, versión 24 sep sin publicar. [RCS-28008](https://trebuco.atlassian.net/browse/RCS-28008), Completed. Estados consultados directamente durante este análisis.

[Guía previa](/Users/MancoMenStudio/Cerebro/inbox/2026-09-22-THD-guia-reunion.md) · [Correcciones del Excel](/Users/MancoMenStudio/Cerebro/inbox/2026-09-22-THD-correcciones-excel.md).
