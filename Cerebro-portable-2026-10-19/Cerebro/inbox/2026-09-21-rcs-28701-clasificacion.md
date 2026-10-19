RCS-28701. Clasificación al 21 de septiembre de 2026

Qué pasa
Recomiendo mantener Incident por el fallo pendiente de uco_Merchandise. Jira: Incident, Work in progress, Sebastian Garces. Autopoblado confirmado funcional el 18 sep; Merchandise funciona en Loss según Stephanie el 21 sep.

Causa: hipótesis
Validar Hide/Display por tipo de caso y los campos Merchandise_%. La documentación de Sebastian compara Screen Designer, Web Flow y Security, sin registrar esa validación. La causa de DHL sigue sin confirmar.

Evidencia
Jira y comentarios 16, 18 y 21 sep: https://trebuco.atlassian.net/browse/RCS-28701
Confluence define Incident como break/fix: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478007263240
KB del control exige habilitar Merchandise_% en Hide/Display: https://trebuco.atlassian.net/wiki/spaces/RTS/pages/474931036165

Qué hago hoy
Recomendar a Sebastian comparar Admin > Hide/Display > Illegal Goods > Merchandise_% contra el caso funcional. Si persiste con configuración correcta, escalar a Engineering como defecto con reproducción. Necesitar código no convierte un defecto en New Feature. Permisos configurables: SOW. Capacidad inexistente: New Feature.

Precedentes
RCS-17168, Michaels: mismo control falla en formulario nuevo y funciona en otro; comentario 29 ago 2024 documenta corrección Hide/Display; cliente confirma 11 sep. Incident, Closed. https://trebuco.atlassian.net/browse/RCS-17168
RCS-18755, Guess: misma tabla incompleta por tipo de caso; ajuste y confirmación 18 dic 2024. Incident, Closed. https://trebuco.atlassian.net/browse/RCS-18755


Compromisos
No cambié Jira ni configuración. No hay fecha de solución comprometida. Documento cuestionado: https://trebuco.atlassian.net/wiki/spaces/AALPS/pages/478221434892. Juan ingiere esta nota desde su terminal con cerrar.

Kiran, chat aportado por Juan
Indica que las páginas dinámicas viven en Azure Blob y pide el síntoma para valorar una solución sin revisar código.

Respuesta propuesta, pendiente de enviar
The issue is with uco_Merchandise on DHL's Illegal Goods case type. Clicking Add Merchandise creates a row with edit/delete icons but no editable fields, so users cannot enter or save merchandise details. The same control works in Property Crimes. Sebastian also tested the working Merchandise.aspx page under Illegal Goods and reproduced the same issue. What configuration should we check first?
https://trebuco.atlassian.net/browse/RCS-28701
