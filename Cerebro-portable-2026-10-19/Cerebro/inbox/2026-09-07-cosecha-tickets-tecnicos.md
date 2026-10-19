# Cosecha 7 sep 2026. Hallazgos técnicos por ticket

Resumen de causas raíz y decisiones pendientes de sesiones de tickets individuales no cosechadas antes de hoy. El detalle completo, con evidencia e instructivo, vive en los archivos de `inbox/` que cada sesión ya escribió.

## RCS-28281

Causa raíz confirmada solo para el hueco del 10 de agosto, archivos duplicados. Las demás fechas con hueco, 11, 12, 19, 20, 22 y 25 de agosto, siguen como hipótesis sin verificar. El traspaso a Nikita del 27 de agosto no se completó en la práctica, todos los comentarios desde esa fecha los publica Ayesha Mehar. La pregunta de Ayesha del 27 de agosto sobre revisar la data en bloques de 10 minutos, dirigida a Juan y Nikita con copia a Viraj Kansara, sigue sin contestar y es lo que bloquea cualquier update nuevo al cliente.

## RCS-27407, PPG

Causa raíz confirmada por Tyrone Whitney: `ManageSmartAlerts.aspx` no regenera `FiltersSQL` al guardar cambios de tipo de auditoría. Afecta las ocho alertas SSVR, IDs 33 a 40, casi cuatro meses sin disparar para PPG. Engineering no toma el desarrollo, Support ejecuta el código bajo ENG-8117 en Backlog. Pendiente confirmar con Engineering el repo y pipeline exactos porque la app corre en netTrack legado y la guía de code change está escrita sobre la plataforma moderna.

## RCS-28756, Nike

Causa raíz confirmada: Nike dejó de mandar archivos ECOM el 28 de agosto. No es un problema de Appriss. El asunto real vive en RTS-206999. Ticket movido a Under Customer Review, seguimiento agendado para el 8 de septiembre.

## RCS-28709, Stater Bros

El estado real en Jira es Work in progress, la ficha vieja decía Under Customer Review. El ticket gemelo RCS-28742, donde se documentó la reproducción, se cerró el 4 de septiembre sin que nadie creara el ENG que Shandana Khan había condicionado a aceptar el síntoma como bug real. Tres tiendas distintas en cuatro días con el mismo patrón, incluidas dos nuevas hoy, tienda 139 y 208. Decisión pendiente de Juan: quién cubre este ticket High el fin de semana porque Viraj sale, y si empuja ahora la aceptación del bug con Shandana dado que su condición ya se cumplió.

## RCS-28465 y RCS-28534, Stater Bros Smart Alerts

Causa raíz confirmada por Sebastian Rueda: `incident.Shoplifting.InProcess` queda atascado en 1 y bloquea silenciosamente toda evaluación de Smart Alert para ese caso, sin dejar rastro de error. Precedente exacto: ENG-2819, mismo síntoma, cerrado por Kiran Vadday. La escalación va directo a ella, no a Shandana genérica. Los dos tickets se enlazan por Relates a un ENG común, no Duplicate, porque cada uno tiene su propio ShoplitingID atascado y necesita su propio UPDATE.

## RCS-28671

Comentario 3327605 ya pegado con la pregunta de reconciliación a Andres Marciales y Dan. Dan todavía no contesta ahí.

## THD, Daniel Ketchum, título vacío

El campo Title de Daniel en LPUser2 está vacío porque el claim de SSO no lo pobló, mismo patrón del hallazgo del 18 de agosto con Jonathan Wright, Stacie Whetzel y Melanie Engelman, que Matthew Kamminga corrigió el 19 de agosto para ese lote. Daniel es el mismo síntoma repitiéndose tres semanas después. Pregunta corta ya enviada a Matt para confirmar si su fix cubre todos los tenants.

## RCS-28631

La secuencia de timestamps en Jira confirma que Shandana respondió al aviso vacío de Luis de las 12:05, no al análisis con capturas de las 12:19, que todavía no existía cuando ella escribió. No está ignorando evidencia que ya tenía.

## RCS-28482, ADUSA

La pantalla de permisos ViewReports no está en Permission Groups del Platform nuevo. Está en nettrack legacy, ruta `ManageSecuritySettings.aspx`, un grid con un security level por fila. Documentado en `brain/memoria/reference_viewreports_nettrack_legacy.md`.

## Informe de equipo, últimas 3 semanas

Ya generado y guardado en inbox por su propia sesión. Cubre la escalación de ADUSA completa, otros nueve incidentes mayores con estado verificado en Jira, estado de la cola, cambios de personal, documentación nueva en Confluence y estado del clasificador. Cierra con cinco puntos que necesitan decisión directa de Juan, entre ellos tres comentarios ya redactados que nunca se pegaron en Jira.
