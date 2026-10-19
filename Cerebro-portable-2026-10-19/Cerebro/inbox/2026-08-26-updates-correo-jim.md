# Updates para el correo de Jim, verificados contra Jira

Fecha: miércoles 26 ago 2026, 17:20 ET aprox.
Baseline: tracker enviado el lunes 24 ago (Appriss ADUSA-Support-Tracker - 08242026 D6.xlsx).
Verificación: JQL sobre los 39 tickets del tracker, estados y comentarios posteriores al 24 ago.

Nota sobre los archivos adjuntos. El archivo llamado "tracker actual" (Appriss ADUSA-Support-Tracker (1).xlsx)
tiene fecha de estado 19 ago y es anterior al que se envió el lunes. La comparación se hizo contra el D6 del 24 ago,
que es el último enviado.

## Sí, hay material para el correo. Cinco cierres nuevos y cuatro movimientos.

### Cierres confirmados por el cliente desde el lunes

RCS-28342, Anthony Lopez, job title faltante.
Jim confirmó el 26 ago 10:30: "Testing shows that this appears to have been corrected. Ticket can be closed".
Cerrado el 26 ago 10:47 como Customer Resolved.
Atención: el tracker del lunes prometía un cambio de código para el release del jueves 27 ago, para que los
usuarios nuevos hereden el título. El cierre del ticket no cubre eso. Decide si se le informa que el ticket cierra
y el cambio de código sigue programado.

RCS-28196, Law Enforcement Notified y Vehicle Involved con default No.
Leigh Ann confirmó el 24 ago 11:17 que los dos campos abren en blanco y la lógica condicional funciona.
Cerrado el 24 ago. El tracker del lunes decía "Ahold to check them and confirm", así que esto ya está cumplido.
Dato interno que no va al cliente: el arreglo está manual en producción y en main, no en la release branch.
Gina confirmó el 26 ago 10:54 que el release del jueves no sobrescribe el arreglo manual. No hace falta revalidar
después del jueves.

RCS-28519, Deborah Jean y Sammy Rivera sin tiendas para crear casos.
Jim confirmó el 26 ago 16:36 que ambos probaron y funciona. Cerrado el 26 ago 16:37 como Support Resolved,
Fixed Configuration.

RCS-28533, pantalla mal renderizada para Ralph Valentine.
Leigh Ann trabajó con el usuario el 26 ago 12:43. Cerró sesión, limpió historial, verificó zoom al 100% y
resolución de pantalla. El usuario resolvió el problema de su lado y verificó que LPMS despliega correcto.
Cerrado como Customer Resolved.

RCS-28292, migración del servidor del store file.
April Valerio confirmó el 25 ago 10:08: "There have been no issues with the file server migration. Please close
this case". Cerrado el 26 ago 01:52.

### Movimientos sin cierre

RCS-28123, case assignment.
Leigh Ann probó y la asignación funciona. Aparece un tema nuevo: el pop-up de confirmación que daba la opción
de ver e imprimir el reporte ya no aparece y el usuario cae directo al workbench. Es el mismo punto que el
tracker traía desde el 14 ago sin respuesta. Juan lo registró hoy 17:06 y engineering lo revisa. El ticket
retrocedió de Under Customer Review a Work in progress.

RCS-28093, employee search cruza marcas.
Pasó a Under Customer Review. El cambio del filtro de marca sigue apuntado al release del jueves 27 ago.
Hay un compromiso abierto de Appriss: Leigh Ann preguntó el 24 ago 08:35 cuál es el campo equivalente en el
feed de empleados que recibe Appriss. Juan respondió hoy 17:06 que lo confirma con el equipo de datos.
Ese dato hay que entregarlo mañana.

RCS-28021, export de Izenda.
Sigue en Work in progress con movimiento interno todo el día. El dato que importa: Gina probó en demo7 el
26 ago 16:02 y exportó los cuatro tipos de archivo, recibió solo el XML. El fix no pasa QA todavía.
El compromiso del lunes fue release del jueves 27 sujeto a QA. El riesgo de que no entre es real.
Avisa mañana, no el viernes.

RCS-28304, case tier truncado.
Sin movimiento en Jira desde el 21 ago 19:19, sigue en Under Engineering Review. El lunes se dijo que Appriss
confirmaría antes del release si entraba o no. Esa confirmación no se ha dado.

### Lo que no se movió y expone a Appriss

RCS-28535, Forbidden al subir adjuntos.
Sin movimiento en Jira desde el lunes 24 ago 20:22. El dato de Leigh Ann del 24 ago 14:11 acota el problema:
clips de unos 2 minutos suben bien, archivos de 11 minutos o más fallan alrededor del 60% y devuelven Forbidden.
Eso apunta a límite de tamaño o timeout en la ruta de upload, no a permisos. No hay avance visible de ingeniería
en dos días sobre un tema que el cliente ya diagnosticó por su cuenta. Es el item más expuesto del correo.

RCS-28281, carga de transacciones de Secure.
Sin movimiento en Jira desde el 19 ago 18:45. El tracker prometió backfill el viernes 21 ago y prometió publicar
los conteos por día de operación en el ticket. Cinco días sin publicar nada. Compromiso incumplido por escrito.

RCS-28482, tab MISC gris en Izenda.
Sin movimiento desde el lunes 24 ago 20:22.

### Higiene del tracker

RCS-28447, Izenda Access Issue, abierto y cerrado el 18 ago, aparece en la versión del 19 ago y desapareció del
tracker del lunes. Si se cuenta, el total pasa de 39 a 40 tickets.

RCS-28407 pasó de Completed a Closed el 25 ago. Solo higiene de Jira, sin cambio para el cliente.

### Conteos nuevos para el resumen por tema

Resueltos: 32, contra 27 el lunes.
Pending Ahold verification: 0, contra 3 el lunes.
Awaiting Ahold input: 0.
Active with Appriss: 7, contra 9 el lunes.
Total: 39.

Los siete activos: RCS-28021, RCS-28093, RCS-28123, RCS-28281, RCS-28304, RCS-28482, RCS-28535.
RCS-28093 figura en Jira como Under Customer Review. No hay nada que el cliente pueda verificar hasta que el
cambio salga el jueves, así que en el tracker cuenta como Active with Appriss.

## Bloque en inglés para pegar en el correo

Good afternoon Jim,

Update since Monday's summary. Five tickets closed on your team's confirmation.

RCS-28342, Anthony Lopez job title. Closed 8/26 on your confirmation that testing shows the data corrected.
The code change that keeps newly created users from dropping the title stays scheduled for the 8/27 release.

RCS-28196, Law Enforcement Notified and Vehicle Involved. Closed 8/24 after Leigh Ann confirmed both fields
open blank and the conditional items appear. No revalidation is needed after Thursday's release.

RCS-28519, Deborah Jean and Sammy Rivera unable to select a store. Closed 8/26 after both tested successfully.

RCS-28533, screen rendering for Ralph Valentine. Closed 8/26 after the user resolved it on his side and
Leigh Ann verified the screen displays correctly.

RCS-28292, LPMS store file server migration. Closed 8/26 on April Valerio's confirmation that the migration
ran with no issues.

Open items and where they stand.

RCS-28123, case assignment. Assignment itself is working. The confirmation window with the view and print
option no longer appears and users land on the workbench instead. Logged as a separate item and under
engineering review now. We will come back with a timeline.

RCS-28093, employee search returning more than one brand. The brand filter change is built and scheduled for
the 8/27 release. We owe Leigh Ann the equivalent field on the employee feed. We are confirming it with our
data team and will send it tomorrow.

RCS-28021, Izenda export. Still failing in our own testing as of this afternoon. Of the four export formats
tested, only XML returned a file. We are working it today. We will confirm tomorrow whether it makes the
8/27 release.

RCS-28304, case tier display width. Still in testing. We will confirm before Thursday either way.

RCS-28535, Forbidden error on attachment upload. Leigh Ann's detail on 8/24 narrows this usefully. Clips of
around two minutes upload fine, files of eleven minutes or more fail at roughly 60 percent. We are working the
size and timeout limits on the upload path rather than permissions. We will come back with a finding.

RCS-28281, transaction data load. This one sits on the Secure side. We owe you updated counts per trading day
and have not posted them since 8/19. We will post current counts on the ticket tomorrow.

Regards,
Juan
