Actualización: Juan completó la comunicación en Teams y las notas y respuestas públicas de ambos tickets. RCS-29445 ya está con Shandana en Under Engineering Review. Usa la [auditoría de lo completado y pendiente](/Users/MancoMenStudio/Cerebro/inbox/2026-10-16-tbi-auditoria-cierre-operativo.md) antes de repetir pasos de esta guía.

# TBI: orden de ejecución después de la llamada

Las notas están listas para revisión y copia. El agente no publicó comentarios, no cambió asignados y no movió estados. El HTML anterior es el guion previo, no el registro de acuerdos.

## Archivos que vas a usar

[Nota interna para RCS-29445, Izenda y rendimiento](/Users/MancoMenStudio/Cerebro/inbox/2026-10-16-rcs-29445-comentario-interno-v2.md)

[Nota interna para RCS-29469, archivos y ejemplos de acceso](/Users/MancoMenStudio/Cerebro/inbox/2026-10-16-rcs-29469-comentario-interno-v3.md)

[Anexo técnico completo en inglés](/Users/MancoMenStudio/Cerebro/investigaciones/2026-10-16-tbi-engineering-evidence.md)

Juan pidió después el formato ampliado con títulos, tablas y negritas. Las versiones actuales incorporan el contexto necesario en cada nota. El anexo queda como respaldo opcional, no como requisito adicional para esta entrega. Incluye consultas SELECT pendientes, no resultados inventados. Las notas anteriores de análisis no eran comentarios listos para pegar; estas son las versiones vigentes para este destinatario y propósito.

## Lo que J.R. te pidió realmente

| Pedido | Fuente de la llamada | Responsable y estado conocido |
| --- | --- | --- |
| Poner en el chat los enlaces y de qué tratan los tres o cuatro RCS abiertos, incluidos los separados del original | 10:41 a 10:56 | Juan. No hay prueba en esta sesión de que ya lo publicaras. |
| Llevar el ticket de Izenda a la cola de Ingeniería, asignado a Shandana y dejando clara la prioridad del cliente | 15:32 a 15:46 | Juan, coordinado con Vedant. La última consulta sigue con Vedant, Work in progress. |
| Explicar por escrito el requisito del archivo de teams y cómo llega a nivel de seguridad | 02:40 a 02:53, 21:11 | Cumplido: Juan aportó el texto que Matt publicó. Tu parte es conservarlo y usarlo para validar el flujo. |
| Reunir información adicional si Matt la necesitaba para rendimiento | 15:01 a 15:25 | Matt dijo que los screenshots ya daban bastante información para el alcance Izenda. No bloquees el traslado pidiendo otra vez toda la evidencia al cliente. |

No hubo una orden nueva de crear otro ENG de Security ID. ENG-10069 ya existe. El requerimiento de ver el archivo original de Chris lo hizo Matt después de que J.R. saliera. Ahora tienes una copia del 14 octubre en RCS-29469; aún falta el lote realmente consumido de la fila histórica.

La conversación de Lunar React y horarios de Jim sigue el bloque de Ahold. No se asignó a Juan organizar una llamada nueva de TBI. El criterio de una o dos horas de Support es orientación de ownership, no una tarea de cambiar datos masivamente.

## Paso 1. Deja el registro corto que pidió J.R.

Abre el chat de la llamada y deja los enlaces RCS con una línea de tema. Usa estos cuatro:

1. [RCS-28256](https://trebuco.atlassian.net/browse/RCS-28256): caso original, lentitud al pasar de Secure a Incident. ENG-9990 es el seguimiento de Ingeniería.
2. [RCS-29445](https://trebuco.atlassian.net/browse/RCS-29445): reportes Izenda, tiempos de carga, errores de servidor, exportaciones y timeout 524.
3. [RCS-29451](https://trebuco.atlassian.net/browse/RCS-29451): accesos, Security ID vacío y jerarquía de tiendas; ENG-10069 sigue el fallo de asignación en el alta.
4. [RCS-29469](https://trebuco.atlassian.net/browse/RCS-29469): seguimiento de Colton después de la llamada, con tres CSV y el Excel de ejemplos.

El borrador ampliado ya está en inglés y separado por ticket. Usa la versión v2 enlazada al final. No uses los ENG como sustitutos de los enlaces RCS que J.R. pidió. No puedo comprobar desde aquí que ya publicaste la lista.

## Paso 2. Escala RCS-29445 con la evidencia que ya existe

1. Abre [RCS-29445](https://trebuco.atlassian.net/browse/RCS-29445). La consulta actual: Work in progress, Vedant Shirude, prioridad Medium. La prioridad verbal del cliente no cambió automáticamente ese campo.
2. Coordina con Vedant el traspaso que pidió J.R. Usa la nota preparada en ese ticket como comentario interno. Es la nota de rendimiento, no la de accesos.
3. La nota ampliada contiene la evidencia necesaria. El anexo técnico queda disponible si el investigador pide más detalle. Las capturas originales están en [RCS-29060, reporte del 14 octubre](https://trebuco.atlassian.net/browse/RCS-29060?focusedCommentId=3396117) y están enlazadas en la nota. RCS-29445 no tiene adjuntos propios; conserva esos enlaces y, si incorporas copias, usa los archivos originales, no solo la miniatura del guion.
4. Avisa al cliente del traslado con un update breve antes de moverlo. No prometas una fecha de solución ni copies las hipótesis del anexo. La guía de escalación exige ese aviso. No redacté una respuesta al cliente adicional porque pediste las notas internas.
5. En el menú de estado, la transición comprobada es Waiting for Engineering. El estado de llegada es Under Engineering Review. No son dos colas diferentes. Se verificó disponibilidad por lectura para la cuenta conectada.
6. Asigna a Shandana Khan según el pedido de J.R. y el [procedimiento de escalación](https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478006902856). Revisa después de la transición que el asignado siga correcto.
7. Comprueba que aparezca el ENG creado por la automatización. No lo crees manualmente. Si no aparece, pide a Shandana que revise el vínculo y evita repetir la transición a ciegas.
8. Confirma recepción y próxima fecha de actualización. El compromiso del 16 octubre era entrar a revisión de Ingeniería, no que el arreglo quedara listo hoy. Comprueba con Shandana el alcance frente a ENG-9990; no asumas que cubre todos los reportes.

Resultado esperado de este paso: nota y evidencia accesibles, estado Under Engineering Review, Shandana como responsable y seguimiento ENG identificable.

## Paso 3. Avanza RCS-29469 sin abrir otra investigación desde cero

1. Pega la nota interna de RCS-29469 en [ese ticket](https://trebuco.atlassian.net/browse/RCS-29469). Documenta que los cuatro adjuntos ya fueron leídos y corrige la falta de contexto del triage automático. No afirmes que corregiste las cinco cuentas.
2. Conserva sus adjuntos originales. Como referencia textual, la nota ya nombra RCS-29451 y ENG-10069. El tipo de enlace Relates existe en Jira; si tu pantalla permite enlazar, relaciónalo con RCS-29451. No lo marques Duplicate ni lo pases a Ingeniería solo por haber llegado un nuevo correo.
3. Mantén de momento el trabajo de validación bajo tu seguimiento. Work in progress no pausa el reloj. Ya publicaste ownership a las 13:40 EDT del 16 octubre, sin fecha concreta de resultado; el próximo update debe reflejar lo que compruebes después.
4. Abre la sección C del anexo. Con tu acceso SSMS/Bastion previamente usado, corre solo los SELECT para los cinco ejemplos. Guarda hora de lectura y resultado, incluidos ceros o ausencia de filas. No ejecutes correcciones desde ese bloque.
5. Para cada uno registra: usuario; team del CSV; presencia y team en sso.teams; lookup a securityid; fila de sso.SecurityLevelAssignments y su vigencia; nivel actual de cuenta; último login y jerarquía efectiva. Matt describió una fila por usuario como resultado esperado. Distingue filas históricas y manuales Persistent antes de llamar defecto a una duplicidad. Revisa primero las columnas reales de sso.teams con el SELECT de la sección E del anexo. No ejecutes TRUNCATE: Matt describió lo que hace el cargador, no una acción para ti.
6. Clasifica el resultado. CSV presente y sso.teams ausente: recepción o carga pendiente de trazar. Team presente y nivel ausente o incorrecto: lookup o réplica pendiente de investigar. Nivel disponible antes del login y cuenta vacía: aporta ese ejemplo a RCS-29451/ENG-10069. Nivel actual correcto: busca la secuencia de cambios antes de concluir reparación automática. Jerarquía vacía: comprueba si el usuario requiere tienda o un alcance superior.
7. Los cinco usuarios son Jacinta Titus, Emeldia Pryor, Christi Winters, Rahim Mehdiyev y Cheneria Chevalier. Los cinco sí vienen en los tres archivos. Sus capturas de última sesión van de enero a septiembre; no los clasifiques a todos como primer login.
8. Separa los cuatro correos incluidos en el Excel: aplicación que no carga, fallo al entrar y acceso denegado no demuestran automáticamente Security ID vacío. No pidas otra copia de los archivos ya recibidos.
9. Cuando tengas la validación, actualiza a Colton sin detalles internos y acuerda dónde continuará el seguimiento del acceso. Cierra o consolida el ticket solamente cuando la evidencia y la comunicación queden preservadas y haya una decisión explícita.

Resultado esperado: cinco cuentas clasificadas y ejemplos verificables para el ENG existente, en lugar de otra escalación genérica duplicada.

## Paso 4. Resuelve la pregunta de Chris con el dueño del cargador

1. Usa la línea 301 de appriss_sso_locations_20261014024505.csv: Chris.Orth, Brand SSU, Location 2005. Compárala con la asignación histórica 90002005 de SSO+ del 13 octubre y la 40002005 persistente agregada manualmente.
2. La copia del 14 no prueba qué cargó el 13. Pide al responsable actual de SnowTime el archivo consumido y el identificador de lote de esa fila, además de la regla que combina Brand y Location. Ryan dijo que no conoce el proceso actual de cambios; primero hay que identificar a ese responsable, no asumir que Ryan puede modificarlo.
3. No atribuyas el 9 al cliente ni a un componente preciso hasta ver la transformación del mismo lote. No reemplaces todo por 4. SSU ya viene como marca, por lo que pedir a HR agregar una marca no responde a la evidencia.
4. Verifica con Colton si Chris puede crear un incidente después del ajuste individual. Ver una fila 40002005 en la jerarquía no prueba el flujo completo.
5. Las 111 filas de Location vacío pertenecen a roles distintos de Location Manager. Valida alcance regional, distrital o administrativo antes de pedir tiendas individuales. Son una población distinta de los códigos inválidos 9000xxxx.

Resultado esperado: archivo, regla y salida conectados; responsable identificado; sin un cambio de datos basado solo en una interpretación.

## Paso 5. Cierra los compromisos de seguimiento

1. El escrito de Matt ya está cumplido: Juan aportó el mensaje publicado. Consérvalo junto a la nota y usa la cadena CSV → sso.teams → lookup de texto a ID → sso.SecurityLevelAssignments → cuenta al iniciar sesión. La explicación documenta el diseño esperado; todavía no comprueba cómo se comporta cada cuenta en producción.
2. Pide a Matt la tabla y consulta exactas donde vio inserciones del día 15. No repitas que todo el feed está detenido desde el 13 por un MAX histórico.
3. Confirma con Shandana quién toma ENG-10069. El RCS padre está Accepted into Development; el ENG estaba Backlog y sin asignar. Son estados de expedientes distintos, no prueba de que alguien ya empezó a programar.
4. Pide cobertura explícita para los usuarios existentes. Rachel demuestra un alta concreta; Christi tenía una asignación persistente antigua y necesita revisión. Un segundo login no es una recuperación universal comprobada.
5. Acuerda un próximo punto de control con fecha y responsable. No declares cumplidas las tareas hasta ver el comentario, transición, archivo o respuesta real.

## Siguiente paso

Shandana y Vedant: concretar RCS-29445, confirmar el ENG y el próximo update; obtener dueño de ENG-10069.
Matt: precisar la tabla donde observó carga del día 15 y cómo se aplica la expectativa de una fila por usuario cuando existen asignaciones manuales Persistent.
Ryan y responsable actual de SnowTime por identificar: seguir el lote de Chris y la regla SSU+2005 antes de decidir una corrección.

Texto listo para el chat que pidió J.R.: [Lista de los cuatro RCS en inglés](/Users/MancoMenStudio/Cerebro/inbox/2026-10-16-tbi-teams-lista-tickets-jr-v2.md). Borrador, no publicado.

Verificación de borradores: las dos notas internas y la lista de Teams pasaron verificar_borrador destino interno sin bloqueantes. La alerta sobre otros reportes de RCS-29445 se contrastó con la descripción vigente y el comentario 3396117 de RCS-29060, leídos en Jira en esta preparación. No se publicó ningún texto.
