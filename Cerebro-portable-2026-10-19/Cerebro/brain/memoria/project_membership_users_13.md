---
name: project-membership-users-13
description: Investigación de los 13 usuarios migrados ausentes de membership.Users (jul 2026) y por qué Kiran Vadday vio resultados distintos.
metadata: 
  node_type: memory
  type: project
  originSessionId: 9fc04b4a-14c1-4cb0-b5b5-97ac10fcabe5
  modified: 2026-07-30T15:58:37.476Z
---

Investigación de Juan (29–30 jul 2026) sobre la ola de migración del 7/27: **13 usuarios con UserID del bloque nuevo de unificación que no aparecían en `membership.Users`** — Chanel 7, Vallarta 4, Sportsman's 2.

Descartado como causa: el campo `Active`. En sportsmans, un usuario funcional (`anewton@sportsmans.com`) también tiene `Active = NULL` y sí está en membership. Lo que comparten los afectados es estar en el bloque de IDs nuevo y faltar en membership → apunta al **camino de creación**, no al campo active.

Falso positivo descartado: ADUSA devolvió 2.300+ usuarios porque sus UserID nativos ya empiezan en el rango de 1.800 millones, así que un umbral numérico simple capturó toda su base. **Los umbrales numéricos no sirven para delimitar el bloque nuevo.**

**Kiran Vadday reportó lo contrario** (Chanel: todos existen en ambas tablas). La discrepancia no es de datos, es de **clave de join**: Juan unía por `membership.Users.incidentUserID = incident.LPUser2.UserID`, Kiran buscaba por email/UserName. Un usuario puede tener fila en membership pero con `incidentUserID` sin poblar → "falta" por join, "existe" por email. Son **≥3 clases distintas de fallo** metidas en un solo bucket: fila ausente, fila presente con vínculo roto, y fila solo en membership. El vínculo roto es lo que rompe `GetSSOPermissionGroupsByUserName` (el `@userName` no resuelve).

Cualquier query de reconciliación debe **mostrar las dos rutas de join en columnas separadas** y anclarse a la lista de emails conocidos, no a un umbral de UserID.

Relacionado: [[project-appriss-support-role]]
