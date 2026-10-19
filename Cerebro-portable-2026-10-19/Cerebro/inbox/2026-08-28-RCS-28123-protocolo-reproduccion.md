# RCS-28123. Protocolo para reproducir la ventana de confirmación perdida

Fecha: viernes 28 ago 2026, 18:40 ET.
Objetivo: confirmar si la ventana de confirmación con ver e imprimir desapareció, y decidir si es defecto o
diferencia de configuración.

## Antes de correrlo, dos cosas que cambian el cuadro

No es nuevo. Leigh Ann lo reportó el 14 de agosto a las 11:36: antes se imprimía el PDF del caso desde esa
misma pantalla y ahora hay que salir al workbench y usar print o view. Lo volvió a reportar el 26. Doce días
sin respuesta en medio.

ENG-7192 no lo cubre. Ese ticket, en Backlog, se titula "Incident Case Assignment: assigned case absent from
search by assignee and emails duplicate". Cubre la búsqueda por asignatario y los correos duplicados. La
pantalla en blanco al enviar al aprobador y la pérdida del PDF quedaron fuera. Eso ya estaba anotado en la base
desde el trabajo del D6 y nadie lo agregó.

Por eso el ticket lleva 49 horas quieto. No se olvidó, cayó en el hueco entre lo que ENG-7192 cubre y lo que el
cliente reporta.

## Permiso que ya tienes

ADUSA acordó por escrito el 18 de agosto, en este mismo ticket, que Appriss puede crear, asignar y aprobar un
caso de prueba en Stop & Shop location 9999 en producción, sin tocar datos reales.

No lo corras sobre un caso real. La asignación se guarda de verdad y el correo de asignación se envía de
verdad.

## El protocolo. Quince minutos

1. Crea un caso en Stop & Shop location 9999. Nombra el adjunto o la referencia con el número de caso más
   `-testfile` si necesitas subir algo.

2. Asígnalo a un usuario. Mira qué pasa al guardar. Anota cuál de los tres casos ocurre: aparece la ventana de
   confirmación completa, aparece sin los botones de ver e imprimir, o el usuario cae directo al workbench.

3. Sobre el mismo caso de prueba, usa Send to Approver. Anota si la pantalla se queda en blanco y hay que
   refrescar para que aparezca el nombre. Ese fue el síntoma del 13 de agosto y nadie confirmó si el release
   del 17 lo cerró.

4. Desde el workbench, usa print o view sobre ese mismo caso. Confirma que el PDF sí sale por esa vía, que es
   el rodeo que Leigh Ann describe.

5. Captura pantalla en cada paso, el número de caso, y la hora exacta con zona horaria. La hora te sirve para
   buscar la petición en App Insights si necesitas ir al servidor.

## La comparación que decide el ticket

Corre los pasos 2 y 3 en el ambiente legacy que Matt Kamminga levantó en lpguys. Lo usó el 19 de agosto para
RCS-28093 y sirvió para probar que el cruce de marcas ya existía antes de la Unificación.

Esa comparación responde la única pregunta que Jim va a hacer. Si la ventana estaba antes y no está ahora, es
defecto de la migración. Si nunca estuvo, es una diferencia de configuración de pantalla y la conversación es
otra.

## Si necesitas mirar la configuración

Admin, Screen Designer dentro del nettrack de adusa, agregando `?ADMIN=9QQP` a la URL. Ahí ves si la pantalla
de confirmación sigue configurada.

Solo inspecciona. No pulses Build All Screens. En Santikos, RCS-28022, ese botón coincidió con que la lista de
Incident Types del tenant quedó en cero.

## Qué resuelve la reproducción

Si la ventana no aparece en producción y sí aparecía en legacy, tienes evidencia para levantar el ítem que le
dijiste a Jim el 26 que ya habías levantado. Búsqueda en Jira de todo lo creado desde el 26 con confirmation,
print o workbench en el asunto no devuelve ningún ítem de ADUSA. Confírmalo antes de que Jim pregunte por el
número.

Si aparece bien en producción, entonces es específico de un usuario o de una marca, y el siguiente paso es
pedirle a Leigh Ann el usuario y el caso concreto donde falla.

En los dos escenarios sales del ticket con algo que decir, que es lo que no tienes desde el 26.

## Resultado de la reproducción. 28 ago 2026, 18:18 COT

Reproducido. Caso de prueba 2026-THE STOP & SHOP SUPERMARKET COMPANY LLC-9999-55, Unusual Incident,
tier Loitering, location 9999.

Lo que muestra el HAR, 122 peticiones, ninguna 4xx ni 5xx.

23:18:26 UTC abre `LPMS/ReAssignCase.aspx`.
23:18:36.166 POST con `__EVENTTARGET=btn_Save`, `__EVENTARGUMENT=Click`, responde 200.
23:18:36.769 el navegador carga `LPMS/LPMSEditMenu.aspx`, que es el workbench. Seiscientos milisegundos después.

El guardado ocurrió. Case Last Saved avanzó de 12:12 a 12:17 AM. La asignación funciona, igual que dijo
Leigh Ann.

**El hallazgo que sirve para ingeniería.** No hay ninguna petición a una pantalla de confirmación. La aplicación
no intenta cargarla y fallar. Navega directo al workbench. Entonces no es una pantalla rota ni un render que se
cae, es el destino de la navegación después de guardar. Eso acota el trabajo a una línea de código o a una
configuración, y ingeniería lo puede responder rápido.

**Descartado, y hay que decirlo porque parecía otra cosa.** Al `ReAssignCase.aspx` entraron cinco POST en cuatro
segundos. Cuatro son callbacks de autocompletado del combo de DevExpress mientras se escribía el nombre, con
valores `j`, `juan`, `Juan Martinez`, `Juan Martinez`. Solo el quinto lleva `btn_Save`. No hubo doble envío y
esta corrida no aporta nada al síntoma de correos de asignación duplicados.

**Límite de esta corrida.** Se reasignó a Juan Martinez, que ya era el asignado. El guardado pudo ser un no-op
sobre el valor. Una corrida más reasignando a un usuario distinto lo dejaría cerrado sin dudas.

El HAR se exportó sin cuerpos de respuesta en esa entrada, así que no se puede leer qué devolvió la página.
Si hace falta, reexportar con response bodies activado.

## Dato colateral que cierra una duda de RCS-28535

Cloudflare está delante de LPMS en adusa. Confirmado. El POST del guardado trae
`Cf-Ray: a327093dc9252a96-IAD` y `Server: cloudflare`, y 111 de las 122 respuestas del HAR traen Cf-Ray.

Eso resuelve la duda que quedó abierta en `investigaciones/RCS-28535-upload-forbidden.md` sobre si Cloudflare
está en el camino. Está. No prueba que Cloudflare cause la falla de subida.

## Referencias de la base

`brain/memoria/reference_screen_designer_rebuild.md` para el truco de Screen Designer y su advertencia.
`brain/memoria/reference_erms_lpms_descarga_pdf.md` por si el botón aparece y el PDF falla. Ahí la primera
pregunta es qué módulo subió el archivo, porque ERMS los deja en el directorio de lpms.
Chunk 1531 en la base para la cronología completa del ticket y el hueco de ENG-7192.
