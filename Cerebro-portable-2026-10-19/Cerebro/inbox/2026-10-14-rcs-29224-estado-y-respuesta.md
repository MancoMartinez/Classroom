RCS-29224 AAP, decisión al 14 octubre 2026

Jira verificado: Escalated, Enrique asignado, prioridad Medium. Leídos los 16 comentarios. Hoy 09:33 EDT Shaun pide urgencia: el cliente ha insistido tres veces. Última respuesta pública nuestra: Juan, 8 oct; Rocky pidió confirmación el 12. No consta respuesta con el aval de Daniel.
Fuente: https://trebuco.atlassian.net/browse/RCS-29224?focusedCommentId=3395549

Daniel hoy 08:54 (zona no visible) confirma que retrasar todos los archivos de inventario juntos está bien. La captura compartida condiciona mantener lo demás igual y enumera 14 APPRISS: CCNDET, CCNTHS, GLPSUB, IITDSC, IITFIL, IITHDS, IITHST, IITVIT, MSTPOG, SHKDTL, SKUFIL, STRINVDT, STRMST, STRPHYINV. Fuente: adjuntos/RCS-29224/2026-10-14-teams/01.png y 04.png. No equivale a aprobar mover POS/tlog.

Rocky dijo “all the files”, no enumeró cuáles. Fecha más temprana 21 oct, pendiente aprobación. Fuente: https://trebuco.atlassian.net/browse/RCS-29224?focusedCommentId=3386223

Hoy: responder con el aval condicionado y precisar alcance, fecha y zona horaria. No volver a pedir a Daniel el mismo aval de inventario. Si incluye POS/tlog, pedirle solo esa ampliación. Coordinar con Raman alertas activas y con el dueño de searches/work items los horarios que consumen inventario; no asumir que la página de abril sigue vigente.

Precedentes: leer inbox/2026-10-13-rcs-29224-hallazgos-repo.md y hallazgos-snowflake.md. Son reportes de Claude, sin salidas crudas verificadas aquí. Describen totales de inventario en cero y dependencia de POS; causa y regresión no probadas. PR 58891 no demuestra reparación de inventory_itemposition. Validar este hallazgo por separado, sin afirmar que bloquea el cambio autorizado. La conversación sobre URL/timeouts requiere Kenny y no acredita una decisión sobre inventario.

Mantener Escalated mientras siga el motivo. UCR solo cuando el trabajo interno termine y quede una acción del cliente. Compromiso publicado: Juan prometió volver con novedades el 8 oct. Lo siguiente es borrador, no enviado.

Hi Rocky, engineering has confirmed that the inventory files can move together to the later send time, provided everything else remains unchanged. This means inventory data will be available later. When you say all files, does this include POS/TRE or tlog files as well as the APPRISS inventory feeds? Please confirm the approved change date and whether 9:30 AM means local Eastern time. This confirmation currently covers the inventory feeds only.
