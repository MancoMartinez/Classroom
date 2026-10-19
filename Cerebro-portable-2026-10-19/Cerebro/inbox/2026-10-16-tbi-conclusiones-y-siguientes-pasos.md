Actualización posterior: Matt ya publicó la explicación de SSO+. Consulta la [versión operativa actualizada](/Users/MancoMenStudio/Cerebro/inbox/2026-10-16-tbi-paso-a-paso-post-llamada.md). Los pendientes de obtener ese escrito que aparecen abajo son historia de la lectura anterior.

# TBI: qué sabemos después de la llamada y de RCS-29469

Sí hay contexto suficiente para continuar sin reiniciar el diagnóstico. [RCS-29469](https://trebuco.atlassian.net/browse/RCS-29469) es el seguimiento de Colton con archivos y ejemplos. Su triage automático no leyó los adjuntos ni recuperó la investigación previa. Los archivos ya se descargaron y se revisaron, incluidas 29 imágenes del Excel.

## Conclusiones

1. Security ID: Matt descartó agregarlo al archivo de ubicaciones como arreglo simple. Según el diseño que describió, se deriva del archivo de teams y los nombres de team y nivel deben coincidir exactamente. No verificó en la llamada el código de réplica actual. Aceptó explicar el requisito por escrito en el chat; falta constancia de publicación.
2. Ingeniería: si el nivel está disponible y no llega a la cuenta, Matt pide investigar tanto alta como logins posteriores. Rachel ya tiene evidencia en [RCS-29451, comentario interno](https://trebuco.atlassian.net/browse/RCS-29451?focusedCommentId=3397050) y [ENG-10069](https://trebuco.atlassian.net/browse/ENG-10069). Christi y los demás ejemplos no deben darse por explicados solo por el patrón de primer login.
3. Origen del 9: el CSV adjunto de Chris trae Brand SSU y Location 2005, línea 301, no 90002005. Ese código se observó en SSO+ con carga del día 13; el CSV es del día 14. Falta seguir el mismo lote hasta la transformación. La atribución al cliente de Matt sigue sin demostrarse. No pedir a HR que agregue una marca que ya viene ni cambiar 9 por 4 masivamente.
4. Ejemplos: el Excel muestra cinco perfiles sin nivel: Jacinta, Emeldia, Christi, Rahim y Cheneria. Los cinco vienen en los CSV con Location Manager y ApprissCase Users. Eso descarta ausencia en estos archivos, pero no prueba recepción o aplicación. Los correos de acceso y lentitud requieren clasificación, no una causa única asumida.
5. Location vacío: hay 111 filas sin tienda, 92 con SSU; todas pertenecen a roles superiores a Location Manager. Puede ser alcance jerárquico intencional. No son 111 fallos confirmados; hay que validar la jerarquía correspondiente.
6. Vigencia del feed: Matt mencionó inserciones del 15 sin identificar tabla. MAX del 13 y una tarea sin errores no permiten concluir que todo el feed esté detenido. Hace falta tabla, archivo consumido y lote.
7. Rendimiento: el ticket revisado fue [RCS-29445](https://trebuco.atlassian.net/browse/RCS-29445), Izenda, errores de servidor y 524. Matt consideró suficiente lo mostrado para Ingeniería si el alcance es Izenda. J.R. pidió pasarlo a Shandana y Waiting for Engineering como prioritario. La narración de veinte minutos de espera pertenece al bloque de Ahold, no a una medición de TBI.

## Qué sigue hoy

| Frente | Acción y resultado necesario |
| --- | --- |
| Rendimiento | Coordinar con Vedant y Shandana el pedido de J.R. RCS-29445 sigue Work in progress con Vedant en la consulta. Confirmar recepción de Ingeniería hoy y próximo update. El compromiso de la llamada no era resolverlo hoy. |
| Security ID | Confirmar con Shandana quién toma ENG-10069, que sigue Backlog y sin asignar. Validar cobertura de usuarios existentes y usar los cinco ejemplos nuevos con datos de archivo, salida de carga y cuenta. |
| Datos | Identificar con Ryan al responsable actual de SnowTime/DataOps. Revisar el mismo lote de Chris, transformación SSU+2005 y salida 90002005. Identificar la tabla donde Matt vio inserciones del 15. |
| Cliente y evidencia | Conservar RCS-29469 como recepción de archivos y proponer su relación con RCS-29451. No cerrarlo como duplicado automáticamente ni abrir otro ENG por el mismo síntoma. |
| Registro de llamada | Preparar para aprobación de Juan la lista RCS y tema pedida por J.R. Obtener el escrito de Matt; no consta publicado. |

Estados consultados en vivo el 16 octubre: RCS-29469 Work in progress, Juan; RCS-29451 Accepted into Development, Shandana; RCS-29445 Work in progress, Vedant; ENG-10069 y ENG-9990 Backlog, sin asignar. La nueva consulta a RCS-28256 agotó tiempo; no se afirma estado actual.

## Qué material previo queda superado

El HTML de preguntas era preparación anterior a la llamada. La opción de Security ID en ubicaciones ya tiene respuesta negativa como arreglo simple. Atribuir 90002005 literal al archivo del cliente no se sostiene con el CSV aportado. Presentar el feed entero como detenido desde el 13 o atribuir a TBI los veinte minutos narrados sobre Ahold queda corregido por esta lectura. Los guiones anteriores no son conclusiones actuales.

[Detalle, fuentes, minutos y alcance de cada observación](/Users/MancoMenStudio/Cerebro/investigaciones/2026-10-16-tbi-cierre-llamada-y-adjuntos.md).

## Siguiente paso

Shandana y Vedant: concretar la escalación de RCS-29445 y el responsable de ENG-10069, con fecha del próximo resultado.
Matt: obtener la explicación de teams y niveles que ofreció, y precisar la tabla y consulta de las inserciones del 15.
Ryan y responsable de SnowTime por identificar: contrastar CSV original, transformación y lote de Chris antes de atribuir el prefijo al cliente.
