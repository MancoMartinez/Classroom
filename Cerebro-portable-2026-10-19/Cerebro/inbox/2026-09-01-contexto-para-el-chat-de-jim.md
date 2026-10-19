Contexto de hoy para armar el D12. Martes 1 de septiembre de 2026. Estados leídos de Jira en vivo hoy. Baseline el D11, que salió con el estado del 31 de agosto.

REUNIONES DE HOY

Llamada ADUSA, repaso ticket por ticket. Ron condujo. Estuvieron Matt Kamminga, Leigh Ann Stubbs, Jim Cosseboom y yo. Ron contó nueve tickets abiertos en voz alta y yo lo confirmé contra el tracker.

Llamada corta después, con J.R. Teagle y Matt. J.R. quiere cerrar tickets para pasar la cadencia de llamadas a asíncrona. Su palanca declarada: si se tumban dos o tres de los grandes, empezando por el de attachments, la llamada se vuelve async.

Hilo de Teams con J.R. por la mañana. Él cruzó mi D11 contra el tracker interno y metió lo que faltaba. Eso no toca el documento de Jim.

CIERRE DE JIM EN LA LLAMADA

Dijo que los tickets que quedan son más menores y que el único que causa consternación real afuera es el de attachments uploads. Lo escuchó fuerte y claro el viernes de una de las marcas. Agradeció el progreso y dijo que las notas que Ron manda con las actualizaciones le han servido.

Su métrica, literal: en el spreadsheet tiene los tickets abiertos resaltados en amarillo, y entre menos amarillo vea, mejor.

Eso importa para el D12, porque hoy va a ver tres amarillos más que ayer y uno de ellos ayer estaba verde.

LO QUE CAMBIA RESPECTO AL D11

Dos tickets nuevos y una reapertura. Ningún cierre.

RCS-28683, Adding additional associate to case. Creado el 31 de agosto a las 15:40 por Leigh Ann. Work in progress, assignee Megha Rathi. El usuario agrega una persona nueva al caso, sale un error 404, y al volver a la pantalla la persona sí quedó agregada. Hay que desplegar hacia esa persona para verla en el workbench. Soporte ya lo está reproduciendo. ADUSA confirmó que usan múltiples sospechosos en el mismo caso con frecuencia.

RCS-28693, User not provisioned to system unable to log in. Creado hoy a las 09:55 por Leigh Ann. Work in progress, assignee Vlad Bogus. Harrison Xu, Giant Food tienda 233, Asset Protection para Giant District 104, no puede entrar. Aparte, Leigh Ann reportó que una usuaria sin acceso a LPMS logró autenticar con rol Store Reporter. Los dos casos salieron contra la URL nueva de acceso.

RCS-28589, Store file showing invalid characters, se reabrió. En el D11 salió como Completed y Resolved, correcto al 31 de agosto. Hoy Jira lo tiene en Under Engineering Review con resolution vacía. Estuvo Completed desde el 27 de agosto a las 12:13 hasta que la automatización lo reabrió hoy a las 10:29 contra un comentario de Jim. Jim escribió que los apóstrofes siguen apareciendo al exportar el location listing, y que ese export alimenta otro sistema de ellos.

CONTEOS QUE DEBE MOSTRAR EL D12

45 tickets. 35 resueltos. 0 Pending Ahold verification. 0 Awaiting Ahold input. 10 Active with Appriss.

El D11 cerró en 43, 36 y 7.

Los diez activos: RCS-28093, RCS-28123, RCS-28281, RCS-28482, RCS-28535, RCS-28589, RCS-28596, RCS-28667, RCS-28683, RCS-28693.

RCS-28683 entra en Case entry and assignment. RCS-28693 entra en Login and access. RCS-28589 se queda donde está, en Store file and location data, y cambia de resuelto a activo.

QUÉ DECIR EN CADA FILA QUE SE MUEVE

RCS-28589. La capa de carga está arreglada. Appriss quitó los apóstrofes de los 432 registros afectados y añadió una regla que los ignora al cargar. La capa de export sigue abierta. Appriss verificó que los valores guardados no traen apóstrofe, así que el carácter entra al exportar o al abrir el archivo. Appriss necesita dos cosas de Ahold: con qué aplicación abrieron el listado exportado, y el archivo exportado adjunto sin guardarlo antes desde una hoja de cálculo. Nada de fecha.

RCS-28683. Appriss está reproduciendo el error 404. Sin fecha, sin causa técnica. El próximo contacto se ancla a la reproducción, no a un día.

RCS-28693. Appriss está comparando los datos de inicio de sesión del usuario afectado contra el usuario de control que dio Ahold, y pidió a Ahold revisar la pertenencia de grupo de su lado. Sin fecha. No menciones el segundo caso como hallazgo de seguridad en el documento del cliente.

RCS-28123. La asignación funciona y Ahold lo verificó el 26 de agosto. Sigue abierta la ventana de confirmación que aparecía después de asignar y ofrecía ver e imprimir. Appriss necesita dos cosas de Ahold: confirmación de si la pantalla que recuerdan es la de Mark Case Completed, y una captura del comportamiento anterior. No escribas que la ruta se cerró en código hace tres años y medio. Eso es interno.

RCS-28596. Jim lo reportó el 26 de agosto y no ha recibido nada desde el acuse. Seis días. Appriss identificó el cambio necesario y desarrollo aceptó el trabajo el 28 de agosto. No hay fecha comprometible. Vale la pena confirmar si el workaround es seleccionar cualquiera de las dos filas duplicadas y decírselo.

RCS-28482. Seis días sin actividad. El 26 de agosto Appriss prometió volver sin fecha. La pestaña bloqueada es MISC, la que cambia la distribución del reporte. Ambos reportes siguen corriendo, solo la edición está bloqueada. Appriss no necesita nada de Ahold en este.

RCS-28535, attachments. Es el que Jim nombró como el único que causa consternación afuera. Pídele fecha a Matt antes de generar el documento y pon el estado real en la fila. Si no hay fecha, ancla el próximo contacto a que salga de pruebas.

RCS-28667. Ahold preguntó si armar la jerarquía de cada usuario nuevo es función del administrador del cliente o si debería resolverse en la configuración de provisioning. Esa pregunta lleva tres días sin respuesta y es lo único abierto del ticket, porque el usuario afectado ya trabaja. Contéstala en la fila.

COMPROMISOS QUE SALIERON DE LA LLAMADA

Yo actualizo el spreadsheet compartido con los tickets nuevos y le envío mi copia a Jim esta tarde. Ron pone nota para Ryan en el 28589 y lo devuelve a la lista. Matt confirma con Kelly, una de las gerentes de Hannaford, lo del 28123 y trae notas. Próxima llamada el jueves a la misma hora. Se mencionó que el viernes mucha gente toma puente.

PENDIENTE ARRASTRADO QUE SIGUE SIN CERRAR

RCS-28093. Jim escribió que April confirmó que la posición 20 de DA_Employee_Info.dat viene poblada para todos los registros, y preguntó si tengo ejemplos donde no. El ejemplo que tengo escrito es del 21 de agosto, el empleado 5701349746 en la tienda 0001 con MISC1 vacío. Verifica el estado de hoy antes de reenviarlo. Si April ya corrigió el feed, reportaríamos un problema que el cliente resolvió.

QUÉ NO ENTRA AL DOCUMENTO DEL CLIENTE

Nada de esto va en el tracker ni en el correo. Se dijo hoy y se queda adentro:

Que la ruta al popup del 28123 se cerró en código hace tres años y medio a propósito.
Que una usuaria sin aprovisionar en Azure obtuvo sesión con rol Store Reporter. Es un hallazgo de control de acceso y todavía no tiene ruta decidida.
Que la causa del 28596 está en un left join y en el archivo de código afectado.
Que el apóstrofe del 28589 lo puede estar metiendo Excel al abrir.
Cualquier clave ENG, cualquier nombre de ingeniero fuera de la columna Assignee, cualquier ambiente, cualquier otro cliente.
Cualquier fecha futura, nombre de día o referencia relativa de tiempo.

TICKETS DE ADUSA QUE SIGUEN EXCLUIDOS DEL DOCUMENTO DEL CLIENTE

RCS-28447, abierto y cerrado el mismo día, nunca entró a la serie D. RCS-28327, RCS-28368, RCS-28456, RCS-28472 y RCS-28547 están abiertos en Jira y no están en el tracker. RCS-28327 está asignado a mí. Ninguno se agregó todavía y esa decisión sigue pendiente. No los metas sin confirmarlo conmigo.

DOS COSAS QUE SE DIJERON EN LA LLAMADA Y NO TIENEN RESPALDO EN JIRA

Que el popup del 28123 esté atado a approve. Matt nombró Complete case y dejó el resto en otras acciones. Approve nunca se nombró.
Que el 28693 pertenezca al hilo de provisioning del 28415, el 28519 y el 28667. Esos tres fallan después de autenticar con el selector de tienda vacío. El 28693 falla en la autenticación y en dirección contraria.

Una corrección de grafía. En la transcripción de la llamada aparece Leanne. El nombre en Jira es Leigh Ann Stubbs.
