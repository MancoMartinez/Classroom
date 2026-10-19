# RCS-28535. Forbidden al subir adjuntos en ADUSA

Abierta el 26 ago 2026. Estado: sin causa confirmada.
Ticket: RCS-28535, reporter Jim Cosseboom, abierto el 23 ago 07:16, prioridad Medium, Work in progress,
assignee Edwin Garzon, sin labels.

## Lo que el sistema y el cliente muestran

Ian Jordan recibe Forbidden al subir adjuntos. Video de body worn camera en MP4.

El 24 ago 11:43 Leigh Ann agregó dos usuarias más de Hannaford, Kayla De Jesus-Morales y Erica Shrader, con
tres casos donde falló la subida de video: 2026-HANNAFORD BROS. CO., LLC-8327-51, 2026-HANNAFORD BROS. CO.,
LLC-8109-161 y 2026-HANNAFORD BROS. CO., LLC-8109-164.

El 24 ago 14:11 Leigh Ann acotó el comportamiento. Clips de unos 2 minutos suben bien. Archivos de 11 minutos
o más fallan alrededor del 60% y devuelven Forbidden.

Ese 60% es la barra de progreso del navegador, que cuenta bytes enviados y no acuse del servidor. Un 60%
estable entre usuarios distintos apunta a un límite determinista y no a una red inestable.

Falta el dato que decide todo. El tamaño en MB de uno de los archivos que falla. La duración es un proxy del
tamaño, no el tamaño.

## Lo que ya está establecido en la base y aplica acá

El tope de subida a blob era de 4 MB antes del release del 13 ago. Ese release lo levantó. Nadie escribió a
cuánto quedó. Ver `brain/memoria/project_bucket_review_sesion2.md`.

Juan validó el 13 ago txt, pdf y video en Stater Bros y Sportsman's, lo más pesado 150 MB, sin error. Matt
Kamminga probó 5 GB en test y pidió "as big as you have got". El objetivo real es 1 GB. Ver
`brain/memoria/project_uni_jul_26_attachments.md`.

Producción tiene Cloudflare en el camino y test no. Cloudflare corta a los 100 segundos. Eso ya explica por qué
150 MB pasó la validación interna y el cliente sigue fallando.

Un 524 es timeout del origen, no un bloqueo. Un bloqueo de WAF muestra la página de Cloudflare con el Ray ID al
pie. Un 502 sin Ray ID lo genera YARP, nuestro propio reverse proxy. Ver
`brain/memoria/reference_waf_cloudflare_bloqueos.md`.

Ruta de la subida en la app: `.../nettrack/LPMS/ManageAttachments.aspx?SuspectID=&MasterCaseID=&ShopliftingID=&StoreIdent=`.
Flujo: Browse, Upload, Save All Changes. Convención de nombre para archivos de prueba: número de caso más
`-testfile`.

No le pidas un HAR a Leigh Ann. Su equipo le bloquea F12 y lo dijo el 14 ago. Pídele fecha, hora y zona
horaria. Las trazas de App Insights traen URL, código y duración: `appi-prd-wus2-arp`, rol `web-prd-wus2-arp-yarp`.

## Hipótesis, ordenadas por fuerza

### H1. La credencial de escritura al blob expira en medio de la transferencia

Azure Storage responde 403 Forbidden a un SAS vencido o fuera de ventana. La palabra que ven los usuarios
coincide literal. Un corte estable cerca del 60% en transferencias largas, con éxito limpio en clips de 2
minutos, encaja con una ventana de tiempo fija y no con un límite de tamaño.

Discriminador: lee el cuerpo de la respuesta que falla. Un SAS vencido devuelve AuthenticationFailed con
"Signature not valid in the specified time frame". Después busca la vigencia del SAS en el código de la ruta de
subida y compárala contra el tiempo medido hasta el 60%.

La mata: que la respuesta que falla no traiga código de error de Azure Storage y salga de nuestro propio host.

### H2. Cloudflare corta el POST de la subida

Producción carga Cloudflare, test no.

Discriminador: `Cf-Ray` en la respuesta que falla. Si está, Cloudflare está en el camino. Si no está, no lo
está, por el contraste medido el 14 ago en este mismo tenant adusa.

Actualización del 28 ago 2026. Cloudflare sí está delante de LPMS en adusa. Un HAR de 122 peticiones tomado
durante la reproducción de RCS-28123 trae `Server: cloudflare` y Cf-Ray en 111 de las 122 respuestas, incluido
el POST de guardado con `Cf-Ray: a327093dc9252a96-IAD`. Queda por medir si la ruta de subida corta a los 100
segundos. La presencia de Cloudflare ya no está en duda.

Corrección técnica sobre esta hipótesis. Un corte de Cloudflare a los 100 segundos devuelve 524. Un bloqueo de
WAF devuelve la página de bloqueo. Ninguno de los dos dice Forbidden a secas. Esta hipótesis no avanza sin Ray ID.

### H3. Queda un tope de tamaño de request después del cambio del 13 ago

Discriminador: busca `maxAllowedContentLength` y `maxRequestLength` efectivos para el host de LPMS. Después
sube una escalera de tamaños hasta que rompa.

### H4. Es el mismo defecto de plataforma de RCS-28331

Sportsman's Warehouse se congela cerca del 49% con archivos de 488 MB y 686 MB. ADUSA falla cerca del 60% con
video de 11 minutos. Dos tenants, misma forma, falla porcentual a mitad de transferencia. RCS-28305 de Stater
Bros también es error al subir video. RCS-28167 no aplica, ese es de abrir ZIP ya adjuntos, no de subir.

Discriminador: el tamaño del archivo de ADUSA. Si cae en cientos de MB, trata los dos como un solo defecto y
deja de trabajarlos por separado.

No los enlaces en Jira hasta que llegue el tamaño. Agrupar sin una medición compartida no es causa raíz.

## Siguientes pasos, en orden

1. Pídele a Leigh Ann el tamaño en MB de uno de los archivos que falla, más fecha, hora y zona horaria de una
   falla concreta. Nada de HAR.
2. Saca App Insights para ese timestamp contra ManageAttachments.aspx en adusa. Registra código, duración y si
   viene `Cf-Ray`.
3. Corre la escalera de tamaños en producción sobre adusa. Nombra los archivos con el número de caso más
   `-testfile`. Cronometra cada subida y anota el porcentaje donde muere.
4. Lee la vigencia del SAS en la ruta de subida. Compárala contra el tiempo medido hasta la falla.
5. Agrega el label `Uni_Jul_26_Attachments` si el tamaño confirma que pertenece al bucket. Solo agregar.

## Pregunta abierta para ingeniería

¿A cuánto quedó el tope de subida después del release del 13 ago?

## Qué NO va al cliente

Todo lo de arriba. El cliente recibe estado y una petición de tamaño de archivo. Nada de hipótesis, nada de
otros tenants, nada de RCS-28331.

Relacionado: `brain/memoria/project_uni_jul_26_attachments.md`,
`brain/memoria/reference_waf_cloudflare_bloqueos.md`, `brain/memoria/project_bucket_review_sesion2.md`,
`tickets/RCS-28124.md`.
