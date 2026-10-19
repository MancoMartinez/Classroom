# D15, 4 sep 2026. Verificación completa, correo y una respuesta que faltaba

Archivo: `adusa-envio-hoy/Appriss ADUSA-Support-Tracker - 09042026 D15.xlsx`. 50 tickets, 38 resueltos, 1 pendiente de verificación de Ahold, 2 esperando información de Ahold, 9 activos con Appriss. Cero duplicados, cero hipervínculos sueltos.

Nota técnica. LibreOffice no recalculó hoy, el proceso murió con SIGKILL en cada intento incluso convirtiendo un CSV vacío, así que no es un problema del archivo. Verifiqué a mano en Python que cada fórmula de la tabla resumen suma exactamente igual que el conteo real de la tabla de detalle, línea por línea. Excel recalcula solo al abrir el archivo, así que esto no debería notarse, pero avísame si ves algún número raro al abrirlo.

## Barrido completo contra Jira, los 11 tickets de ayer más el ticket nuevo

**RCS-28784, nuevo, sin asignar.** Delhaize, un paquete de 12 sodas marcó precio original de 21.98 por unidad, el cajero aplicó un descuento manual a 4.00. El recibo POS muestra el precio original como 2 por 21.98, que da 10.99 por unidad. Reporta Becky LaPierre, contacto conocido de Delhaize, ya tiene dos tickets previos con nosotros. Pregunta directa, si el problema está en el tlog de Appriss o en los tlogs del cliente. Cero horas de atención humana todavía, solo el acuse automático.

**RCS-28482, cambió dos veces en un día.** A las 4:06 AM Shandana Khan lo pasó a Mohammed Mutahhar como SRE de turno. Mohammed encontró a las 8:30 que el join hacia Store estaba incompleto en ambos reportes. A las 19:10 yo mismo reconstruí los joins, en Outlook Export hicieron falta dos adicionales a los que Mohammed había detectado, y a las 19:11 le avisé a Jim que ambos reportes ya muestran MISC otra vez. Falta que Jim confirme que se ve bien de su lado y que Mohammed valide un mapeo que usé por analogía, Misc1 contra StoreManagerID, sin confirmar todavía. El tracker ya quedó en Under Customer Review, con la fila coloreada como pendiente de verificación de Ahold.

**RCS-28535, cambió de estado.** El tracker de ayer decía Work in progress, Jira ya lo tiene en Under Customer Review desde el 26 de agosto, quedó desactualizado. Jim le pidió a Leigh Ann seguimiento el 3 de septiembre, ella escribió a dos gerentes de Hannaford y sigue esperando respuesta. Por separado, una prueba interna de hoy subió un archivo de 5 MB, falló una vez y funcionó al reintentar, sin nada en el log de errores. Actualicé el tracker a Under Customer Review, Awaiting Ahold input.

**RCS-28766, avance real.** Diego Buelvas encontró la causa exacta a nivel de commit. Un pull request del 14 de agosto, ENG-7192-Part2, borró el bloque que dispara la alerta de reasignación en la página de reasignar caso. Diego recomienda restaurar ese bloque o construir deduplicación real en el servicio de alertas. Esta mañana devolvió el ticket a Shandana Khan para abrir el ticket formal de ingeniería, que todavía no existe. Actualicé estado y asignado en el tracker.

**RCS-28667, sin cambio de estado, un dato desactualizado.** El tracker traía a Megha Rathi como asignada. Jira ya lo tiene en Matthew Kamminga desde que Juan documentó la reproducción completa el 3 de septiembre. Corregido.

**Sin cambios, verificados y correctos en el tracker: RCS-28093, RCS-28281, RCS-28589, RCS-28596, RCS-28683, RCS-28693, RCS-28752.**

## Un hallazgo que no es para el tracker

RCS-28596 lleva desde el 26 de agosto sin que Jim reciba un solo comentario dirigido a él. Todo lo que pasó, ingeniería confirmó la causa el 27 de agosto, aceptó el trabajo, el fix ya está en QA, se quedó entre soporte e ingeniería. Jim nunca se enteró de nada de esto en el ticket.

Esto no se soluciona en el tracker ni en el correo de estado, se soluciona respondiendo el ticket. Aquí tienes el texto listo para pegar, con saludo a Jim, mismo tono que los demás:

---

Hi Jim,

Update on this one.

Appriss confirmed the duplicate rows come from the employee search query joining to the Store table on store number alone. Delhaize store numbers repeat across brands, so the join matches more than one store and returns each employee twice.

The fix removes that join for Delhaize, the same approach already used for Lux. Engineering accepted the fix and it is now in QA.

Appriss is holding release for a window that avoids a weekend deployment.

I need nothing from you on this one.

Thank you.

---

## Correo de estado para Jim, con la sala en copia

Subject: ADUSA support tracker, 9/4 status

Jim, all,

Attached is today's tracker, verified directly against Jira.

One new ticket opened today, RCS-28784.

Twelve tickets remain open: RCS-28093, RCS-28281, RCS-28482, RCS-28535, RCS-28589, RCS-28596, RCS-28667, RCS-28683, RCS-28693, RCS-28752, RCS-28766 and RCS-28784.

Three of those are worth a look in the tracker. RCS-28482 is fixed on both Izenda reports. Please confirm they look right on your end. RCS-28535 is waiting on your own Hannaford managers to respond to Leigh Ann's outreach. RCS-28766 has a confirmed root cause at the code level.

Thank you.
