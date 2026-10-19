---
name: reference_jerarquia_ubicaciones_incident
description: "Cómo se resuelve el alcance de distrito de un usuario en Incident: LHUA asigna tiendas, el distrito se hereda del StoreIdent primario"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 8b73134e-5723-4d74-be14-e59eb99f9e25
  modified: 2026-08-11T16:26:43.303Z
---

Modelo verificado con SQL en el tenant 433 (Vitamin Shoppe) el 10 ago 2026.

**Las tablas**
- `structure.LocationHierarchyMaster` define la forma de la jerarquía. En 433 son 4 niveles: Company, Division, Region y **District en el nivel 4**.
- `place.Location` lleva columnas planas `LocationHierarchy1..6` más sus Descriptions, una fila por tienda.
- `secure.LocationHierarchyUserAssignments` (LHUA) guarda el alcance por usuario. Cada fila puede apuntar a un `LocationId` concreto o a un valor de nivel de jerarquía.
- `incident.Store` lleva `StoreIdent`, `StoreNo`, `Region`, `District` y `DistrictManagerID`.
- `incident.LPUser` es una VIEW sobre `incident.LPUser2`. El puente desde Secure es `membership.Users.IncidentUserID` (int) → `incident.LPUser2.UserID` (int).

**El hallazgo que importa**
En 433 las 884 filas de LHUA están asignadas por `LocationId`. Cero usan las columnas de distrito, región o división. Es decir, **el alcance de distrito no se asigna, se hereda del distrito de la tienda asignada**.

Y solo se hereda del `StoreIdent` primario. Verificado en cuatro usuarios: cada uno ve el distrito de su StoreIdent primario y nada del secundario, incluso cuando el secundario está en otro distrito y la persona figura como `DistrictManagerID` de ese otro distrito.

**Consecuencia práctica**
Un usuario que gestiona dos distritos no se puede resolver desde Support. Agregar una segunda fila en LHUA a mano desde Control Panel no le da el segundo distrito, solo la tienda. La pestaña Hierarchies de Control Panel no es el mecanismo de distrito.

**Cómo distinguir migración de edición manual**
La migración creó una sola fila LHUA por usuario. Si un usuario tiene dos filas y la segunda tiene un `HierarchyUserAssignmentId` igual o cercano al total de filas de la tabla, esa fila se agregó a mano después.

**Qué se descartó buscando esto**, para no repetir el trabajo: grupos de permisos, estado de cuenta (Locked/Disabled/Deleted), el mapeo Secure a Incident, cuentas duplicadas de la unificación, los feature flags de sesión, los datos maestros de distrito, y `SupervisorFlag` / `SecurityID`. Ninguno era la causa.

El comportamiento observable del caso está en [[reference_multidistrito_lhua]]. Esta memoria es el modelo de datos que lo explica.

Relacionado: [[reference_esquema_usuarios_incident]], [[reference_acceso_sql_tenants]].
