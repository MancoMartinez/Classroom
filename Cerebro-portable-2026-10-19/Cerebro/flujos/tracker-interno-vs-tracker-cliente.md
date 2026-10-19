# Tracker interno contra tracker del cliente. Qué cambia y por qué

Escrito el 1 sep 2026 comparando las filas 61 a 69 del tracker interno contra el D12 que va a Jim.

## La regla de fondo

El tracker interno responde una pregunta: qué le falta a este ticket para moverse.
El tracker del cliente responde otra: en qué va lo que reporté.

Son documentos distintos porque tienen lectores distintos. El interno lo leen Appriss y J.R. El del cliente lo
leen los directivos de Appriss y de Ahold al mismo tiempo. Todo lo que sirve para presionar hacia adentro
lastima hacia afuera.

## Columnas que existen solo en el interno

Engineer assigned, Cause, Appriss Notes y Priority.

El del cliente tiene diez columnas y ninguna de esas cuatro. Además no lleva columna Theme, porque el tema va
como banda de sección sobre las filas.

Esas cuatro columnas son el filtro entero. Casi todo lo que no puede salir vive ahí.

## Fila por fila, qué se quedó adentro

### RCS-28482, fila 61

Interno: "Not escalated. Nobody at Appriss has opened these reports." Y la promesa a Jim del 26 sin fecha,
seis días sin actividad. Cause dice "Izenda report type, unverified".

Cliente: Appriss trabaja el tab MISC, ambos reportes siguen corriendo, solo la edición está bloqueada, nada se
necesita de Ahold.

Por qué. Nadie escribe en un documento que va a la sala que su propio equipo no abrió el reporte en seis días.
Y una causa marcada como no verificada no se comunica, porque el cliente la va a citar como si lo fuera.

### RCS-28667, fila 64

Interno: sin pasos de reproducción, sin ambiente, sin troubleshooting, nota de espera sin hallazgo, y la
pregunta de Ahold tres días sin responder.

Cliente: se responde la pregunta. Asignar la jerarquía en el perfil es hoy una acción de administrador, y lo
que Appriss revisa es si el provisioning puede traerla. Más el patrón de tres reportes.

Por qué. Que Appriss lleve tres días sin responder es un problema de gestión interna. Lo que el cliente
necesita es la respuesta, no el reproche.

### RCS-28123, fila 65

Interno: la ruta al popup se cerró en código hace tres años y medio a propósito. Restaurarla cambia el
producto y necesita justificación de negocio, no arreglo de defecto. ENG-7192 está Done y cubre otra cosa.
ENG-557 está en Backlog. Y lo más duro: soporte le dijo a Ahold el 26 que el tema estaba registrado y bajo
revisión de ingeniería, y ese registro no existe.

Cliente: Appriss recorrió la ruta de asignación y no encuentra ventana de confirmación en ella. Marcar un caso
completo sí lleva a una pantalla de ese tipo. Y dos peticiones concretas.

Por qué. Lo de los tres años y medio convierte un defecto en una decisión de producto delante del cliente, y
esa conversación la tiene el account team, no un tracker de soporte. Las claves ENG nunca salen. Y que soporte
haya dicho algo que no existe se corrige haciendo el registro, no confesándolo en un adjunto que leen J.R. y Rip.

### RCS-28693, fila 66

Interno: dos defectos en direcciones opuestas. Paula Dotson no tiene provisioning en Azure y autenticó con rol
Store Reporter. El interno lo llama defecto de control de acceso en producción y dice que espera decisión de
ruta de J.R.

Cliente: solo Harrison Xu y la comparación de claims contra Kyle Moses.

Por qué. Leigh Ann reportó lo de Paula Dotson ella misma, así que el cliente ya lo sabe. Lo que no puede salir
es que Appriss lo califique por escrito como defecto de control de acceso en producción antes de tener ruta
decidida. Esa frase, en una lista de distribución, se convierte en un hallazgo de seguridad citable.

### RCS-28683, fila 67

Interno: la lista de lo que falta antes de mover, la condición que puso J.R. de levantar el ENG y enlazarlo, y
la observación de que la segunda queja es fricción de flujo y hay que separarla.

Cliente: Appriss está reproduciendo, el caso sí se crea así que nada se pierde, y volverá con la reproducción.

Por qué. La lista de lo que falta es gestión. Lo que le sirve al usuario es saber que no perdió el trabajo.

### RCS-28596, filas 68 y 69

Interno: ENG-7904 clonado el 28, en Backlog sin sprint ni fix version. Peyman y Ryan por nombre. El archivo
Popups/EELookupList.aspx.vb. El precedente de Lux. Y seis días sin responderle a Jim.

Cliente: la causa está en código y no en datos, ingeniería aceptó el trabajo el 28.

Por qué. Nombre de archivo, clave ENG, otro cliente y ausencia de fix version son todo material interno. Que
un ENG esté en Backlog sin fix version le dice al cliente que no hay compromiso, y eso se maneja hablando, no
en una celda.

## Lo que sí cruza en los dos sentidos

Estado, assignee, fechas, resumen del problema y comentarios del cliente. Eso es idéntico a propósito, porque
si difiere alguien lo va a notar.

## Cuatro cosas del archivo interno que conviene arreglar

**RCS-28596 está duplicado en las filas 68 y 69**, idénticas. Es el mismo error que tenía RCS-28482 en las
filas 60 y 61 del tracker de Chris, que se corrigió al armar el D6 el 24 de agosto. La fila 60 sigue siendo un
resto de ese duplicado.

**La columna Theme dejó de tener temas desde la fila 61.** Hasta la 59 dice "Platform configuration and
notifications" o "Transaction, tender and POS data". De la 61 en adelante dice el título del ticket. Cualquier
agrupación o tabla dinámica por tema queda rota.

**El vocabulario de Action with se soltó.** Las filas 59, 62 y 63 dicen "Closed" donde el resto del documento
dice "Resolved". La leyenda solo define cuatro valores y "Closed" no es uno.

**La tabla resumen de arriba quedó congelada.** Dice 37 tickets y 21 resueltos, que es la foto del 19 de
agosto, mientras el detalle ya llega al 1 de septiembre. El encabezado también sigue diciendo "Status as of
Wednesday, August 19".

## Regla práctica para el futuro

Antes de mover un texto del interno al del cliente, pregúntate si contiene alguna de estas seis cosas. Si
contiene una, no sale.

Una clave ENG o RCS de otro cliente. Un nombre de ingeniero fuera de la columna Assignee. Un nombre de archivo,
tabla, query o ambiente. Una causa marcada como no verificada. Una crítica al desempeño de Appriss. Una fecha
futura o un nombre de día.
