---
name: reference_multidistrito_lhua
description: Un usuario con dos distritos asignados en LHUA solo ve uno a la vez; confirmado en Vitamin Shoppe el 11 ago 2026
metadata: 
  node_type: memory
  type: reference
  originSessionId: 254b4d73-4509-4741-99d1-56c88cb6d56c
  modified: 2026-08-11T15:15:58.798Z
---

En la plataforma unificada, un usuario con **dos filas en `secure.LocationHierarchyUserAssignments`** a nivel de distrito **solo ve un distrito a la vez**. La asignación múltiple no se honra.

**Evidencia (Vitamin Shoppe, Client ID 433, RCS-28032):** Dayna Rivera cubre los distritos 501 y 504. Antes del cambio veía solo 504. El 4 ago se le agregaron ambos en Control Panel. El 11 ago la clienta reportó que ahora ve 501 y **perdió 504**. Mismo usuario, mismo perfil, dos estados observados: el distrito visible cambió al agregar la segunda fila.

Es la única usuaria del tenant con dos distritos, y por eso ningún otro District Manager lo reporta. Su segunda fila es el ID 884 en una tabla de 884, o sea agregada a mano después de la migración, no creada por ella.

**Ya descartados con evidencia, no son la causa:** permission groups (idénticos a tres DMs que funcionan), estado de cuenta, el mapeo Secure a Incident, cuentas duplicadas, y los flags `EnableAdHocInitCaching` / `EnableAdHocPerRequestUserScope` (ambos True en esa base).

**Cómo usarlo:** ante un reporte de "no veo uno de mis distritos", primero preguntar si la persona cubre más de uno. Si es así, no es configuración y no se arregla desde Control Panel: agregar la fila solo cambia cuál de los dos se ve. Va a ingeniería.

Ver también [[reference_esquema_usuarios_incident]] y [[reference_unificacion_patrones]].
