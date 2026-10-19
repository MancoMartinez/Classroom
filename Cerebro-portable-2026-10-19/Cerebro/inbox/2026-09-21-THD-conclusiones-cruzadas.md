THD. Revisión cruzada al 21 de septiembre de 2026

Conclusión
Hay avances verificables y tres frentes abiertos: recuperar 17 work items, validar/publicar el arreglo del timeout y resolver la inconsistencia recurrente de detalle/agregados. La cadena rename → reintentos → saturación → dataload incompleto no está demostrada. No comunicarla como RCA.

Correcciones de la hipótesis original
1. RTS-206667 confirma el rename de TenderTypeGroup a StdTenderTypeGrp para SNR4. El error original era NonRetryableException y el mensaje condicionaba reintento a actualizar búsqueda/definición. Eso no demuestra un bucle automático de reintentos. Sus comentarios más recientes hablan de cancelación y de SNR1/SNR3 lentos. RCS-28799, comentario 3325670 del 2 sep, registra SNR4 succeeded: ya no es válido afirmar que falla en cada corrida desde agosto. No atribuir todos esos fallos al rename original.
2. RCS-28671 confirma el mismo identificador roto, no solo una clase de síntoma similar. Simon reparó 278 búsquedas y el cliente confirmó esa reparación. Quedaron seis bloqueadas por otro bug, sin cierre documentado en ese hilo. El ticket reabrió por 17 work items sin eventos. Tratar esas dos fases separadamente.
3. RTS-207372 documenta consultas largas de THD en secure_WH, colas y timeouts de otros clientes; la cancelación manual despejó la alerta. Hay un defecto específico de timeout, ENG-8650. RCS-28799 documenta mejora de una búsqueda de más de cuatro horas a 80 segundos el 7 sep, nuevos timeouts el 8 sep y 18 búsquedas dependientes por actualizar el 10 sep. Falta confirmar adopción completa de la optimización. Falta demostrar que los errores de compilación originaron las consultas largas. ENG-8650 enlaza RCS-28799, no RTS-207372 directamente; la relación temática y temporal es fuerte, sin sustituir correlación por QueryId.
4. RCS-28968 tiene una aclaración del cliente hoy: recibos y otros datos completos, Total Item Sale Amount incorrecto. No basta describirlo como carga faltante. Verificar primero suma real de items, Subtotal, derivado y recibo por la misma transacción.
5. Compartir Snowflake no prueba compartir warehouse ni competir por el mismo compute. No se recuperó evidencia de que los jobs de dataload corrieran en secure_WH durante los timeouts. Se necesitan warehouse, job/query IDs, intervalos y espera en cola antes de atribuirles inanición de recursos.

Precedente que faltaba en el planteamiento
RCS-28649 explica la recurrencia de detalle desde agosto con evidencia distinta de los timeouts. Su triage del 30 ago encontró task suspendida. La investigación de septiembre evolucionó: Andres corrigió la hipótesis de archivos tardíos el 9 sep y explicó una limpieza que eliminaba detalle repartido entre archivos. ENG-8334 confirma orphan-delete deshabilitado y reconstrucción de aproximadamente 1,31 millones de recibos ardm_json. La comprobación de 0 recibos desactualizados corresponde al corte histórico del 10 sep; no prueba que hoy todo esté bien. Camila cerró RCS-28649 tras confirmación del cliente y dejó pendiente un SOP para recargas y recibos. La recurrencia del 17 al 21 sep requiere comprobar la vigencia y alcance del fix y del SOP; no asumir que comparten exactamente la causa anterior.

Otro exceso de certeza en la investigación histórica
La nota local del 4 sep calificó la carrera de sesión como confirmada al comparar comandos del mismo template con filtros distintos. Ese contraste no aísla el contexto de sesión como única variable: cambian tienda y datos. Mohammed mantuvo el 7 sep dos alternativas, disponibilidad al ejecutar o configuración del event provider; Andres había documentado fuente completa antes del corte. El punto firme es fuente ARDM completa en la revisión y ausencia de eventos de plataforma para los 17 items. El mecanismo del fallo requiere más evidencia. La remediación propuesta por Engineering sí quedó clara: borrar los afectados y regenerar con control.

Prioridad de acción
Primero: RCS-28968 con Bikash. Ya respondió hoy 11:24 EDT, 10:24 Bogotá. El siguiente contacto debe aportar conciliación o plan técnico, no otro acuse. Pedir dueño técnico, ticket, recálculo y validación de horas 20 del 19/20 sep. No pedir nuevamente ejemplos que ya están en capturas sin revisarlos.
Segundo: RCS-28671 con Shandana/Jon. ENG-8659 existe en Backlog, sin asignado, comentarios ni versión. Accepted into Development no significa trabajo en ejecución. Pedir dueño y fecha para recuperar los 17 y preservar su información. El cliente no recibe actualización desde el 7 sep.
Tercero: RTS-206667 con Vlad y ENG-8650 con Gabor. Separar optimización de SNR1/SNR3 del timeout. ENG-8650 está Development Complete y apunta a Secure September 2026 Release 2/2, releaseDate 24 sep, released=false. Confirmar fecha efectiva, pruebas y validación antes de decir desplegado. El 18 sep Gabor indicó que probablemente QA no puede probarlo directamente y propuso depender de pruebas automáticas; no publicó sus resultados.
Cuarto: recuperar con Camila/Andres el SOP prometido en RCS-28649 e incluir validación de detalle, derivado y recibo. Un reload exitoso no acredita consistencia entre las tres salidas.

Comunicación
Sí podemos comunicar que las búsquedas originales recibieron reparación y la recuperación de los 17 items tiene un ENG concreto pendiente de programación. Podemos informar internamente que el fix del timeout tiene desarrollo terminado y versión prevista, todavía sin release publicada. No anunciar solución permanente de RCS-28968, ETA garantizada ni causa común.
Los textos ingleses para pegar están en cada entregable por ticket. Son borradores, no enviados. Cada archivo queda bajo 2500 caracteres.

Cobertura y límites
Consulta directa de Jira: cuatro tickets originales, RCS-28799, RCS-28649, DO-12041, ENG-8334, ENG-8650 y ENG-8659. Revisión de 43 comentarios de RCS-28671, 25 de RTS-206667, 9 de RTS-207372 y 16 de RCS-28968. Fechas de actividad tomadas de comentarios. DO-12041 figura Closed y no tiene comentarios; no aporta prueba individual de recuperación de estos defectos.
No se ejecutaron pruebas en producción, consultas a Snowflake ni lectura directa del hilo completo de Teams. El diálogo de Teams de los timeouts se leyó reproducido en Jira. La búsqueda semántica avisó cobertura parcial; búsquedas JQL específicas permitieron localizar los ENG relevantes. Ninguna ausencia de resultado demuestra que no exista otro ticket.

Fuentes
https://trebuco.atlassian.net/browse/RTS-206667?focusedCommentId=3351092
https://trebuco.atlassian.net/browse/RCS-28671?focusedCommentId=3334895
https://trebuco.atlassian.net/browse/ENG-8659
https://trebuco.atlassian.net/browse/RTS-207372?focusedCommentId=3337373
https://trebuco.atlassian.net/browse/ENG-8650
https://trebuco.atlassian.net/browse/RCS-28968?focusedCommentId=3358182
https://trebuco.atlassian.net/browse/RCS-28649?focusedCommentId=3336400
https://trebuco.atlassian.net/browse/RCS-28649?focusedCommentId=3337469
https://trebuco.atlassian.net/browse/ENG-8334?focusedCommentId=3338722

https://trebuco.atlassian.net/browse/RCS-28799?focusedCommentId=3337429
https://trebuco.atlassian.net/browse/RCS-28799?focusedCommentId=3325670
