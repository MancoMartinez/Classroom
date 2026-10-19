# Cola de Juan: cierres, respuestas y SLA

Corte: 16 de septiembre de 2026, 12:57 Bogotá. Jira en vivo, assignee=currentUser() AND statusCategory != Done, paginación completa. 21 tickets: 12 Under Customer Review, 7 Work in progress, 1 Under Support Review, 1 Under Infrastructure Review. Prioridades: 2 High, 18 Medium y 1 Low. Se revisaron los comentarios de los 21; los seis hilos con más de 20 comentarios se consultaron completos. No se modificó Jira ni SQLite.

## Cierres

RCS-27941 sí permite cierre por confirmación expresa. Colton confirmó el 15 sep a las 12:23 Bogotá que ambos usuarios buscan correctamente y pidió cerrar. Fuente: https://trebuco.atlassian.net/browse/RCS-27941?focusedCommentId=3347270

Ningún ticket tiene acreditada una secuencia completa vigente para cierre por silencio hoy.

RCS-28496 PVH: UCR desde 20 ago. Avisos de 7 días el 27 ago y de 14 días el 3 sep. El aviso anuncia otros 14 días. Próxima comprobación del aviso final: 17 sep. No anticipar el cierre. Fuente: https://trebuco.atlassian.net/browse/RCS-28496?focusedCommentId=3326061

RCS-28282 Co-op: UCR desde 21 ago. Avisos el 28 ago y 4 sep. Próxima comprobación del aviso final: 18 sep. No anticipar el cierre. Fuente: https://trebuco.atlassian.net/browse/RCS-28282?focusedCommentId=3327262

RCS-27676 Ralph Lauren: 43 días desde UCR del 4 ago. El aviso final del 22 jul anunciaba cierre el 29 jul; el cliente respondió después, el 30 jul. Ese aviso perdió vigencia. No aparecen nuevos avisos tras la petición de IP públicas del 4 ago. Revisar automatización y tipo SOW con el responsable, retomar seguimiento. No cerrar usando el aviso de julio.

RCS-27791 Guess: aviso de 14 días hoy; la comprobación de día 28 corresponde al 30 sep si sigue sin respuesta. La automatización del 12 sep también pide revisión con Support Management por superar 60 días, salvo que ya conozcan el caso.

## Respuestas y trabajo que debes priorizar

1. RCS-28256 High: actualizar al cliente y obtener avance técnico sobre la lentitud. Último público tuyo: 8 sep, 20:46 Bogotá. El cliente pidió mantener abierto. SLA de resolución activo vencido.
2. RCS-28881 NEXCOM: responder al comentario nuevo de Carlo de hoy. Pantalla blanca inmediata y aviso del navegador tras 8 a 10 minutos; el formulario afectado es 576. Dividieron la auditoría en Retail y Services para trabajar este año. No dar por confirmado un timeout de 100 segundos.
3. RCS-28342 ADUSA: responder a Leigh Ann del 15 sep, 11:35. No confirmó todavía el título de Daniel y reportó bloqueo del Agent List Report. Separar la comprobación del perfil del nuevo problema de reportes.
4. RCS-2 Vallarta: responder internamente a Shandana del 15 sep, 01:58. Pide explicar la relación entre timestamps y el nuevo reporte de login/session timeout. El agradecimiento posterior de Tatiana no responde esa pregunta ni autoriza cierre.
5. RCS-28581 CWH: retomar investigación y dar actualización sustantiva. Tu último mensaje del 27 ago fue un acuse. James retiró expresamente su petición de cierre del 26 ago y volvió a escribir el 3 sep.
6. RCS-27765 Winn-Dixie: acusar el correo de Matthew remitido por Rajith el 15 sep. Leí la imagen: Matthew afirma que el archivo solo contenía 25 jun y que investigarán si el proceso genera el formato correcto. Contrastar esa afirmación con el lote observado por Juan. No concluir que enviaron fechas equivocadas. Adjuntos: adjuntos/RCS-27765/image-20260915-164240.png. La captura no identifica zona horaria; usar la fecha del comentario para incorporación al ticket.
7. RCS-28099 CWH: acusar la respuesta del 14 sep, 17:17, y acordar seguimiento. James pide más tiempo para combinar seis conjuntos de datos. No cerrar por silencio.

## Compromisos abiertos

RCS-28212: actualización sustantiva el 15 sep, 18:59. Falta confirmación de Ingeniería y plazo del arreglo prometido el 11 sep. Bryant lo calificó crítico en el hilo; Jira mantiene Medium. Revisar prioridad con Support. No afirmar que cambió oficialmente.

RCS-28871: actualización el 15 sep, 16:08. Falta stress testing. Escalar internamente esa respuesta y concretar próxima fecha. Infraestructura no exime de la cadencia sin plazo explícito documentado.

RCS-28756: actualización el 15 sep, 13:08. Falta causa y arreglo del conector Kafka; continuar con Data Engineering. Tu última instrucción pide mantener en espera el contacto con Nike.

RCS-28281 High: UCR desde 7 sep. Espera cifras solicitadas a Becky y conserva revisión interna pendiente. Seguimiento del aviso de 14 días previsto para 21 sep. No cerrar por silencio hoy.

## Resto de la cola

| Ticket | Estado | Próximo paso |
| --- | --- | --- |
| RCS-28558 | UCR | Esperar retest solicitado por J.R. el 15 sep y correo de Dexter. Matt documentó arreglo de numeración. |
| RCS-28351 | UCR | Esperar validación de adjuntos pedida el 8 sep; aviso de 7 días el 15 sep. |
| RCS-28289 | UCR | Joe respondió el 8 sep: su IT sigue investigando el túnel de IP. El aviso anterior no justifica cierre. |
| RCS-28240 | UCR | Esperar confirmación del tenant Azure y nueva prueba; aviso de 7 días el 15 sep. |
| RCS-28223 | UCR | Esperar retest de los grid columns solicitado el 14 sep. |

Los otros 16 tickets figuran en los bloques anteriores. RCS-28122 y RCS-28911 no aparecen en la cola actual de Juan; no inferir su estado desde informes anteriores.

## Comentarios nuevos hoy

RCS-28881: Carlo, 06:38 Bogotá, comentario público 3348131. Es la única respuesta humana nueva entre estos 21 tickets al corte.
RCS-27791: Automation for Jira, 08:10 Bogotá, comentario interno 3348277. Es un recordatorio de 14 días, no una respuesta del cliente.

## SLA de Jira y cadencia

RCS-28256: Time to resolution, meta 14h, reloj activo, breached=true, remainingTime=-176h 48m al corte. Es el SLA activo más urgente observado.
RCS-28281: Time to resolution, meta 14h, breached=true, remainingTime=-629h 30m. Reloj pausado en UCR. El incumplimiento ya ocurrió y la pausa no lo elimina.
Los otros 19 tickets no devuelven un ciclo de resolución activo en este campo. No equivale a cumplimiento ni ausencia de obligaciones. Los ciclos completados de primera respuesta y asignación representan incumplimientos históricos, no plazos nuevos por vencer.

Cadencia oficial de comunicación: Critical cada hora, High diario, Medium cada 48h, Low semanal. UCR pausa la cadencia. RCS-28256 y RCS-28581 requieren atención inmediata por antigüedad de comunicación sustantiva. RCS-28294 alcanza 48h desde tu último público el 16 sep a las 18:19 Bogotá. RCS-28342 necesita respuesta al cliente desde ayer. No se usaron umbrales orientativos de bin/cola.py como SLA contractual.

## Fuentes normativas y discrepancias

RCS Ticket Update Cadence, versión 3, 17 jul: seguimiento manual a las 48h, otro a las 48h, aviso final a las 48h y cierre siete días después sin respuesta. Una respuesta reinicia la secuencia.
https://trebuco.atlassian.net/wiki/spaces/RTS/pages/477946314758

RCS Ticket 7/14/28 Day Process, versión 1, 12 jun: automatización exclusiva UCR, avisos días 7, 14 y 28, cierre después del aviso final. Días calendario. Registro de avisos como comentarios internos.
https://trebuco.atlassian.net/wiki/spaces/RTS/pages/477913776130

RCS Ticket Workflow Inception to Closure, versión 1, 2 sep: reafirma automatización 7/14/28 y propiedad de Support sobre comunicación. También menciona actualizaciones semanales; para priorización se usó la guía específica por prioridad. No declara que sustituya la guía de julio ni resuelve explícitamente ambas cadencias de seguimiento.
https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478170087431

Por esa coexistencia no se mezclaron avisos automáticos con la secuencia manual para adelantar cierres. Las fechas 17, 18 y 30 sep se deducen de los avisos reales de 14 días y requieren comprobar aviso final y ausencia de respuesta en ese momento.

Ingerir este archivo desde la terminal con cerrar. No se ejecutó ingesta desde el agente.

Cada ticket tiene además una ficha de acción breve en inbox/2026-09-16-rcs-NUMERO-revision-cola.md, con los seis bloques y menos de 2500 caracteres.
