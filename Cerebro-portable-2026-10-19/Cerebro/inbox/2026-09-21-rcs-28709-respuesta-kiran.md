RCS-28709. Respuesta breve para Kiran. Verificado en Jira el 21 de septiembre de 2026.

Estado actual: Under Support Review, asignado a Viraj Kansara. ENG-8656 existe y está en Backlog, sin asignado. La ficha local que indicaba ausencia de ENG quedó obsoleta. Causa raíz sin confirmar.

Texto para Teams:

Hi Kiran, this is an intermittent Save/Submit issue in Stater Bros LPMS. Users reported a blank screen and cases becoming inaccessible or retaining no entered data. Viraj reproduced it on case 2026-083-STORE SHOPLIFT-220 on September 3 and attached a recording. We rebuilt the screens that day, and my seven retests passed, but Angie reported further affected cases at stores 139 and 208 on September 4, so we could not confirm it was resolved.

ENG-8656 is linked and currently in Backlog. The root cause is still unconfirmed. I saw your note today that you could not reproduce it. The next step is to retry the affected flow and collect the corresponding Incident error logs from Control Panel.

Evidencia: https://trebuco.atlassian.net/browse/RCS-28709
Viraj, 3 sep, comentario 3325907: reproducción y grabación adjunta. Angie, 4 sep, 3327596: recurrencia en tiendas 139 y 208, esta última sin error visible pero sin datos guardados. Juan, 4 sep, 3327899: dos rebuilds y siete pruebas correctas. Kiran, 21 sep, 3358957: no reproduce y solicita reintento y archivos fechados error_log desde Incident Logs.

Compromiso existente: Shandana, 14 sep, 3345015, alta prioridad para una de las próximas releases y actualización cuando el fix llegue a producción. No hay fecha firme ni fix confirmado. https://trebuco.atlassian.net/browse/ENG-8656

Hoy: entregar este resumen a Juan. Siguiente acción sugerida para Juan y Viraj: repetir el flujo con autorización para la prueba y recopilar logs del entorno y hora correspondientes. No se ejecutaron pruebas ni se obtuvieron logs en esta sesión.

Precedente: RCS-28742, relacionado cerrado. Historia: bin/buscar RCS-28709 y ficha local.

Adjunto de Kiran revisado visualmente: adjuntos/RCS-28709/image-20260921-194758.png. Muestra EUDEV, cliente apprisscommerce3.com (7), Support > Incident Logs > View by Client > logs, archivos YYYYMMDD_error_log.txt. Es una guía de navegación, no evidencia del error de Stater Bros; el visor está vacío. Seleccionar el entorno real de Stater Bros y su cliente antes de buscar los logs de la fecha del fallo.

Pendiente de ingestión por Juan desde su terminal con cerrar.
