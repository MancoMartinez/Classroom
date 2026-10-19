# ADUSA · reunión del viernes, respuesta de Jim, D5 y correo · 21 ago 2026

Verifiqué los 37 tickets del tracker de Chris contra Jira en vivo, antes y después de tus cambios de esta noche. Los archivos (4) y (5) son idénticos, cero celdas distintas, el filtro no recortó nada. La respuesta de Jim al correo del D4 cerró dos tickets. Cada ticket queda completo abajo, sin remitir a otra sección.

## 1. Verificación de tus cambios de esta noche

Revisé en vivo lo que ejecutaste entre las 19:19 y las 19:42. Todo quedó bien, con un detalle.

RCS-28124 quedó Closed con Resolution en Resolved. Pasó una hora y la automatización no levantó la bandera de "Needs Attention", así que el segundo nivel de Resolution Details quedó lleno. Limpio, no repitió lo de RCS-28177.

RCS-28353 quedó Completed con Resolution en Resolved. Exacto.

RCS-28482 lo tomaste, comentaste el acuse a las 19:24 y la explicación de Data Sources a las 19:42, y lo pasaste a Under Customer Review. Esa transición es mejor que la que yo había sugerido, Appriss ya entregó su parte y lo que falta es la prueba de Jim.

RCS-28304 lo dejaste sin comentar, correcto. La actualización de las 19:19 en ese ticket no fue tuya, fue Kiran publicando una URL de prueba y una captura en el ticket de ingeniería. Ya está trabajando el ancho del campo.

El único detalle es tu nota interna del 28124 a las 19:38, dice que el cliente confirmó en una reunión. Jim lo confirmó por correo, no en reunión. Es nota interna, no afecta al cliente, pero si alguien reconstruye el hilo después no va a encontrar esa reunión.

## 2. Lo que cerró la respuesta de Jim

RCS-28124, adjuntos no visibles. Jim contestó textual, "We have no new reports of issues and .txt is unlikely a type of an attachment". Eso respondió las dos preguntas abiertas del ticket de una sola vez, el error Forbidden no volvió y .txt no es un formato que usen. Cerrado hoy a las 19:38, Closed con Resolution en Resolved, sin bandera de automatización.

RCS-28353, error 502 al actualizar la tienda. Jim contestó textual, "As mentioned on the call yesterday this seems to be working fine". Cerrado hoy a las 19:41, Completed con Resolution en Resolved.

RCS-28482, campos grises en Izenda. Jim lo abrió el 19 a las 15:17 y estuvo 48 horas sin dueño y sin respuesta real, con solo el acuse automático. Eso ya se corrigió, lo tomaste hoy y comentaste la ruta de Data Sources que Kiran encontró en la reunión. Under Customer Review, esperando la prueba de Jim.

RCS-28196, páginas adicionales. Jim contestó "We will look". Eso es respuesta, no resolución. Estado Work in progress, dueño Vedant Shirude. No lo toques y no lo vuelvas a preguntar, contestó ayer.

## 3. Lo que la reunión aporta y no está en Jira

RCS-28342, títulos de puesto. Estado Work in progress, dueño tú, último comentario tuyo del 20 a las 19:41 prometiéndole a Jim actualizar el registro de Janai. Matt confirmó hoy que el script ya corrigió a los usuarios existentes. Kiran aclaró el punto que faltaba, el cambio de código para que los usuarios nuevos hereden el título entra como ticket del próximo sprint, no ahora. Antes de comentar necesito un dato tuyo, ¿ya aplicaste el cambio en el registro de Janai que prometiste ayer? Si sí, redacto el comentario de confirmación con el detalle del próximo sprint. Si no, se queda sin comentario hoy.

RCS-28304, ancho del campo Case tier. Estado Under Engineering Review, dueño Matthew Kamminga. La reunión resolvió la pregunta que Leigh Ann hizo el 13 de agosto, si el campo se puede ensanchar o si toca enhancement request. Respuesta real de hoy, Appriss lo mete junto con los PRs de Matt y Kiran lo toma, descrito como trabajo de dos minutos. Ahold no tiene que levantar ningún enhancement request. **No lo comentes todavía.** Aplica la regla que Shandana marcó el 20 de agosto, el ticket sigue en Engineering y el comentario al cliente sale cuando transicione a Under Support Review. Comentar antes repite exactamente el error de RCS-28161.

RCS-28021, Izenda. Estado Work in progress, dueño tú. En la reunión Chris dijo que esto se puede cerrar. Jira lo contradice. Leigh Ann escribió el 17 a las 14:35 textual, "No, it is not ok. I still do not have the ability to export results into a usable report." Tus dos preguntas del 19 a las 18:14, si el fallo es en un reporte o en todos y si el mismo reporte sí exporta en CSV, siguen sin respuesta. Leigh Ann está fuera hasta el 23. No se cierra. Se queda en Work in progress.

RCS-28356 y RCS-28407, rendimiento. La reunión decidió mantener Izenda en su propio app service plan dedicado en vez de devolverlo al plan principal, con esta razón textual de Chris, no arriesgarse a que los 502 vuelvan. Jose analiza el autoscale la semana entrante. Ese es el estado real del monitoreo. RCS-28356 lleva desde el 18 a las 20:36 sin respuesta de Leigh Ann. RCS-28407 sigue en Under Engineering Review con Edwin.

RCS-28292, migración del servidor. Estado Work in progress, dueño Gulshan Kumar. La ventana corrió anoche, 20 a las 23:00 hasta hoy a las 06:00, y ya cerró hace horas. April creó el caso como aviso y Appriss se comprometió a monitorear el feed. En la reunión Chris dijo que no ha escuchado nada y que asume que salió bien. Asumir no es verificar y en Jira no hay ni un comentario posterior al tuyo del 19. Confirma internamente con Support o Infra si el archivo de tiendas de esta mañana llegó completo. Con ese dato redacto el cierre para April. Sin ese dato no lo toco.

## 4. Los tickets que ya quedaron cubiertos, sin acción

RCS-28093, búsqueda de empleados entre marcas. Cerrado del todo hoy. Jie Chen pidió el dato de MISC1 a las 12:50, tú se lo pediste a Leigh Ann a las 13:21, Jim contestó que ese empleado es Food Lion y copió a April Valerio por el feed automático de empleados, y tú lo devolviste a Jie Chen a las 18:01. Estado Accepted into Development, dueño Matthew Kamminga. El tracker de Chris dice Work in progress y dueño Edwin Garzon, las dos cosas están desactualizadas, el D5 las corrige.

RCS-28378, botones Save y Next. Ya transicionó a Completed. La transición que faltaba ayer quedó hecha.

RCS-28123, asignación de casos. Estado Work in progress, dueño tú. Sin comentario desde el 19 a las 14:52, cuando Matthew reportó lentitud real en el lookup de usuarios. Lleva 47 horas. El pendiente es interno, no del cliente.

RCS-28281, transacciones Secure. Estado Work in progress, dueño Nikita Rathore. Tu comentario del 19 a las 18:45 le prometió a Jacquelyn el backfill alineado con el viernes, o sea hoy. Verifica si cerró antes de que termine el día.

## 5. D5 generado

Archivo: Appriss ADUSA-Support-Tracker - 08212026 D5.xlsx, construido sobre el D4.

Verifiqué los 36 tickets uno por uno contra Jira después de tus cambios. Cero desviaciones, la columna de estado es espejo exacto.

Ticket nuevo: RCS-28482, campos grises en Izenda, Under Customer Review, Pending Ahold verification, dueño tú.

Estados alineados con Jira: RCS-28124 a Closed, RCS-28353 a Completed, RCS-28378 a Completed, RCS-28161 a Closed, RCS-28413 a Closed, RCS-28415 a Closed, RCS-28125 a Closed, RCS-28281 a Work in progress, RCS-28292 a Work in progress.

Dueños corregidos, los dos venían mal desde el D4: RCS-28304 pasa de Vedant Shirude a Matthew Kamminga, RCS-28161 de Shandana Khan a Viraj Kansara.

Total 36 tickets. Resolved 25, Pending Ahold verification 2, Awaiting Ahold input 0, Active with Appriss 9.

## 6. Correo para Jim

Descarté todo lo que Jim ya sabe o ya quedó comentado en los tickets. Los cierres de RCS-28124 y RCS-28353 salen de su propia respuesta. RCS-28196 lo contestó ayer. RCS-28021 espera a Leigh Ann y él no puede accionar nada.

Queda una sola cosa que Appriss necesita, la prueba de RCS-28482. Ya la pediste en el ticket a las 19:42, así que en el correo va como señalamiento, sin repetir la explicación completa de Data Sources.

RCS-28304 lo dejé fuera a propósito. Es el único avance nuevo frente al D4 que Jim todavía no conoce, y sigue en Engineering con Kiran trabajándolo. Va en la columna del tracker y no en el correo, por la misma razón por la que no se comenta en Jira todavía.

```
Hi Jim,

Tracker attached, updated through today.

One thing we need from your side, on RCS-28482. I left you the route into those greyed out fields on the ticket. If you can try it on both reports and tell us whether you get to the attributes you need, we will take it from there.

Thanks,
```
