---
name: project_adusa_ficha_y_tickets
description: Ficha de Ahold Delhaize USA (Client ID 441) y estado de los tickets de Juan al 14 ago 2026
metadata: 
  node_type: memory
  type: project
  originSessionId: a8293f75-ab64-479b-971f-f586abf0f63b
  modified: 2026-08-14T23:15:23.599Z
---

**Ficha.** Ahold Delhaize USA. Organización en Jira: `Ahold-Delhaize`. Tenant `adusa`. **Client ID 441.** Marcas: Food Lion, Giant Food, Giant/Martins (Giant Food Stores LLC), Hannaford, Stop & Shop, Delhaize. Base, siguiendo nomenclatura: `sqldb-prd-wus2-arp-production-441-adusa-platform`.

App: `https://apps.apprissretail.com/adusa/nettrack/`
Menú Incident: `/LPMS/Menu.aspx?System=LPMS` · Búsqueda: `/LPMS/CaseLog.aspx` · Izenda: `/AdHoc/reportlist.aspx` · Renumerar caso: `/admin/RecreateCaseNo.aspx`

**Contacto principal:** Leigh Ann Stubbs, `leighann.stubbs@adusa.com`, Administrator Corporate Asset Protection, T 704-310-2008. Reporta casi todos los tickets. **Escalación:** James Cosseboom y Tom Blackburn (VP de IT). Ver [[project_adusa_escalacion_2026_08_14]].

**Nombres de usuarios que salieron como ejemplos:** Nicholas Wilson `nicholas.wilson2@stopnshop.com` (RCS-28177), Brian Somsky (RCS-28364), Anthony Lopez (RCS-28342), Patrick Barnes (RCS-28123).

---

## Tickets de Juan al 14 ago 2026

**RCS-28369, número de caso no siguió al cambio de tienda. Verificado.** Matt lo corrigió con RecreateCaseNo, quedó `2026-GIANT/MARTINS (GIANT FOOD STORES, LLC)-6314-30`. Juan verificó en la UI: coincide en fecha 7/31/2026 6:29 PM, tipo, estado OPEN, valor $91.22 y owner Stefani Belanger; el número viejo no devuelve nada; los 9 casos de la tienda 6510 con esa owner son anteriores y cerrados. Sin duplicado. ENG-7270 en Backlog. Procedimiento en [[reference_recreate_caseno_changelocation]].

**RCS-28342, Anthony Lopez. Resuelto lo reportado, reencuadrado el resto.** El título que faltaba ya aparece (11139 = FT Lead Asset Protection Coordinator), verificado en producción el 14 ago en las dos pantallas. **Leigh Ann confirmó que sí hay más de un Anthony Lopez**, o sea que nunca fue un duplicado de migración, son dos personas reales. Lo que queda es que el desplegable de aprobadores no permite distinguirlas: en la plataforma anterior había un botón en User Details que marcaba a alguien como aprobador, y Matt cree que **el dato existe pero no se muestra en el front end**, y no está seguro de si el desplegable lista solo aprobadores o a todos. Eso quedó a cargo de Matt. Ella dejó un segundo ejemplo similar en el chat, ya agregado al ticket.

**RCS-28342, cierre de la noche del 14 ago.** Kiran intervino a las 5:56 p.m. sobre el ticket de Juan y encontró un **tercer UserID**: el correcto de la base vieja es **1194761**, ni 11139 ni 1789032. Detalle revelador, el login de la entrada 11139 era `5701194761`, con el UserID bueno embebido. Su fix corrigió el correo en LPUser2, apuntó `membership.Users` al IncidentUserID correcto poniendo `UserName` y `SupervisorFlag = 1`, e insertó la fila que faltaba en `secure.LocationHierarchyUserAssignments` (LocationId 8031). **Contradicción sin resolver:** en la llamada Leigh Ann dijo que hay más de un Anthony Lopez, personas distintas; Kiran lo trata como una sola persona con varios correos (*"Due to multiple email addresses, the UserID that was matched was erroneous"*). Se resuelve contando filas de `membership.Users` para ese nombre. Camila dejó pedido aparte: revisar otros casos iguales y validar quién es aprobador y quién no, que ahora se puede porque la bandera es `SupervisorFlag`. Detalle de esquema en [[reference_lpuser_lpuser2_membership]].

**RCS-28177, búsquedas con número en el correo. Verificado por Juan la noche del 14 ago.** Kiran alineó 44 filas y Jonathan Wright quedó bien, las dos llaves cuadran y el correo con el `2` es consistente a ambos lados. **Pero ADUSA no quedó limpio:** quedan 20 usuarios reales del cliente sin contraparte en LPUser2, 18 sin rastro por ninguna llave y 2 con la identidad vieja de Ahold. El update de Kiran no los podía alcanzar. Asignado a Viraj Kansara, no a Juan. Ver [[reference_lpuser_lpuser2_membership]].

**RCS-28021, Izenda.** Ver [[reference_izenda_adusa_dos_rutas]]. Tres problemas distintos apilados en un ticket; conviene separarlo.

**RCS-28124, adjuntos.** El tope real era 4 MB de subida a blob, fix en producción el 13 ago, Juan validó hasta 3 GB. Cerrable. La confirmación del cliente está bloqueada porque les pega el 502 antes.

**RCS-28123, asignación de casos.** Pedido el número de caso el 3 y el 10 de agosto, nunca llegó. Creció dos veces: 13 ago 19:52, Send to Approver devuelve pantalla en blanco y el nombre solo aparece tras refrescar; 14 ago 11:36, ya no se puede imprimir el PDF desde esa pantalla. **ENG-7192 no cubre ninguna de las dos.** Línea: la asignación sí se guarda, falla la respuesta que devuelve la página, misma forma que ChangeLocation. Falta un caso de prueba sancionado para reproducir sin mandar una aprobación real.

**RCS-28353, 502 al actualizar tienda.** Asignado el 14 ago. Prioridad uno tras la escalación.

**RCS-28379, Case Owner, Creator y Assigned To en blanco.** Dato de Leigh Ann en la llamada: **antes los casos no aparecían del todo, ahora aparecen sin nombre.** Juan encontró casos con las tres columnas vacías tanto de **2021** como del **4 ago 2026**, o sea antes y después del corte, y en esos mismos casos **Last Saved By sí resuelve**. Eso descarta que la resolución de usuarios esté rota en general y descarta que sea solo residuo de migración. Falta la consulta que separa las dos hipótesis: si la columna del owner trae un ID y la pantalla lo muestra vacío es problema de resolución; si está en NULL, el dato nunca se escribió.

**RCS-28378, botones Save y Next de Hannaford.** Sin dueño. Es exactamente lo que describió James al abrir la escalación, gente que mete datos y los pierde al dar Next.

**RCS-28327, loyalty discounts.** Salió del documento de revisión de Camila pero sigue abierto y sigue siendo de Juan.

Ver [[reference_unificacion_patrones]], [[project_estado_abierto_2026_08_13]].
