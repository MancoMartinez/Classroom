RCS-29234. Investigación actualizada2 oct2026. Corte Teams14:26 Colombia.

Qué pasa: recuperación1 oct con rebuild/reinicio NetTrack; recurrencia2 oct tras cambios Medical911. Hoy CentralStationMaster funciona según Jim. Segundo reinicio: validación interna13:58, confirmación Jim vía J.R.14:10. Jira sigue Critical, Work in progress, Sebastian Garces;16 comentarios completos,14 públicos/2 internos, sin issues vinculados.

Causa: mitigación confirmada, origen pendiente. Hipótesis caché/configuración/runtime incoherente. Ryan propone pestañas de sesión anterior. CPF.Core.LogOnTimeoutMinutes=60 según Ryan13:49, distinto de timeoutSQL120s. Juan14:15 aún sin reproducción.

Evidencia: https://trebuco.atlassian.net/browse/RCS-29234 comentario público3375792 de Jim12:52; grupo Camila, Chris, J.R., +6; cuatro transcripciones. J.R.13:38: añadir Accident_AccidentTimeReported y ShopliftingExtra_AssociateReportedEmail, Save and Build, renombrar; caso Food Lion9988-47 funciona; hacer campos obligatorios y9988-48 queda procesando. Probar secuencia completa.

Qué hago hoy: entregar cronología, evidencias, hipótesis y prueba propuesta sin cambios. Support conserva ticket según Kiran14:04. Falta actualización pública de segunda recuperación, reproducción e ID del Defect LastSavedDate.

Precedentes: ENG-9281 caché, no duplicado confirmado; ENG-556 zona horaria BuildDate. Informe y fuentes en investigaciones/2026-10-02-adusa-save-y-fechas-screen-designer.md. Borrador en inbox/2026-10-02-defect-last-saved-date-borrador.md.

Compromisos: Juan/Garces reproducen solo en test; cliente pausa diseñador; J.R. pregunta pestañas y revisará con Matt lunes5 oct. LastSave es trazabilidadDB, no columnaGUI ni causa probada del bloqueo. No afirmar fix permanente. Liderazgo analizado separadamente en informe. Juan ingiere con cerrar; agente no ingiere ni modifica Jira.
