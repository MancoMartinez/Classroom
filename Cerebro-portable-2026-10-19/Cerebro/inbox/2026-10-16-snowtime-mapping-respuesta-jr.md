# Respuesta solicitada para J.R., 16 octubre 2026

Hallazgo confirmado: el precedente RCS-29205 separa investigación de Support, cambio del mapping por ingeniería SnowTime y rebuild con rol admin. No se confirmó un permiso general de L2 para editar y desplegar mappings. El FAQ confirma lectura de monitoreo para SNOWTIME_SUPPORT. El proceso Support Data Team admite L2 con formación en datos y escalación cuando no puede resolver; no acredita permisos de repositorio o despliegue.

Fuentes consultadas en vivo: RCS-29205, 19 comentarios de 19. Nota interna del 7 oct, 3384023, documenta la ruta Adarsh a Anushka. Nota interna del 9 oct, 3386643, documenta rama de Ryan, PR de Anushka y rol admin para rebuild. Son notas publicadas en Jira por Juan, no comentarios directos de los ingenieros.
https://trebuco.atlassian.net/browse/RCS-29205
https://trebuco.atlassian.net/wiki/spaces/RTS/pages/477555982355
https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/477664444418
Antecedente Cerebro: inbox/2026-10-02-sbx-work-items-escalacion-estado.md, resolución de ruta, líneas 51 a 60. Delivery ofreció ayuda con mappings.

Borrador v1 obsoleto por la captura adicional aportada por Juan. Sustituido por v2 abajo. Destino Teams interno. verificar_borrador: sin bloqueantes. Evidencia adicional comprobada directamente en Jira y Confluence para las alertas de respaldo del índice. No enviado.

I haven't confirmed that L2 has permission to edit and deploy SnowTime mappings. Our documented monitoring access is read-only. Ryan has offered to walk the support team through the workflow for backend issues, and I'll arrange a session with him for next week, subject to calendar availability.

Evidencia nueva: captura de Teams con Ryan DeVries aportada el 16 oct. El 2 oct a las 15:59 propone reunir a Support para trabajar el ticket y explicar el workflow de backend. El 5 oct a las 09:28 pide usar el calendario de Outlook para buscar disponibilidad. La captura no confirma una reunión agendada. Juan expresa hoy intención de coordinarla para la semana del 19 oct. El nombre visible es Ryan, no Bryan. La frase de próxima semana es un compromiso nuevo de Juan, no una fecha acordada con Ryan. El FAQ leído en vivo respalda lectura de monitoreo, no una limitación universal de todos los permisos de Support.

Actualización, captura de Teams del 16 oct, 09:25: J.R. pregunta directamente si Support tiene permisos para hacer cambios de mapping en SnowTime. La captura confirma que Juan publicó a las 09:24 el precedente RCS-29205. El borrador v2 pendiente queda sustituido por v3 para responder a la pregunta concreta. No se ha confirmado el permiso; no afirmar que todo el acceso de Support es de solo lectura.

Borrador v3, no enviado:
I haven't confirmed that yet, J.R. I’ll check with Ryan whether Support has the permissions needed to make SnowTime mapping changes.

Actualización 16 oct, captura Teams: Juan preguntó a Ryan a las 09:26 si tenemos permisos para cambiar mappings. Ryan respondió a las 09:28: "I believe you should? What are you trying to do?" Es una expectativa de Ryan, no una comprobación de permisos efectivos. El borrador v3 para J.R. queda desactualizado en su promesa de consultar: Juan ya consultó. La respuesta definitiva de permisos sigue pendiente.

Borrador solicitado por continuidad para Ryan, v1, no enviado. Verificado sin bloqueantes:
J.R. asked whether Support can correct existing SnowTime mappings when something stops working. I'm checking our permissions and the expected workflow, rather than requesting a specific change right now. Would we make those changes through the SnowTime repo and a PR, and would deployment require someone else's approval?

Siguiente paso: Ryan, aclarar la ruta de cambio por repositorio y PR y quién aprueba el despliegue. J.R., informar del permiso solo cuando se confirme su alcance.
