RCS-28256. Respuesta de Matthew Kamminga por Teams, 15 oct 2026.

Q1: no hace falta fila en incident.LPUser2 para usuarios nuevos; basta con que aparezcan en la vista incident.LPUser. Corrige mi lectura: el cruce correcto es contra la vista LPUser, no LPUser2. Coincide con la regla de Kiran (lhua y lpuser view, las dos).
Q2: separar lentitud en un RCS y accesos en otro. Los accesos probablemente estan todos relacionados. Un solo RCS nuevo para accesos, no dos.
Q3: de donde vienen los 9000xxxx. Toda ubicacion de incident deberia estar tambien en secure. Validar con Delivery, Ryan Barlow, que la carga llene bien las dos tablas.

Pendiente verificar:
A. Los 46 usuarios sin nivel, estan o no en la vista incident.LPUser.
B. Si 90002005 existe en incident.Store y 40002005 no, o al reves.

15 oct 17:44 UTC. incident.LPUser vista: columnas EmailAddr (no Email), LoginID, UserID, SecurityId, StoreIdent a StoreIdent5, Inactive, Active, LastLoginDate. Ejemplo Shanese Browne UserID 50455, SecurityId 5, StoreIdent 4567.
incident.Store sin filas para StoreIdent 90002005 ni 40002005: StoreIdent en Incident es un ID interno corto (4567), no el LocationID de Secure. Falta buscar la tienda 2005 por StoreNo.

RESULTADOS 15 oct
A. Vista incident.LPUser, usuarios con nivel en feed y login desde 2 jul, sin @trebu.co: en LPUser con nivel 181; en LPUser con cuenta NULL 49. Nadie fuera de la vista. CONFIRMADO: la vista no discrimina; el criterio de Matt (aparecer en LPUser) se cumple y aun asi 49 quedaron sin nivel. La causa del nivel sigue sin conocerse. LPUser2 queda como correlacion, Matt dice que no es requisito.
B. incident.Store para la tienda 2005: StoreNo 10002005 JAB (StoreIdent 4442), 20002005 KNG (4634), 30002005 MSP (4835), 40002005 TMW-CAL-CALB (5193). El primer digito es la marca: 1 JAB, 2 KNG, 3 MSP, 4 TMW. No existe prefijo 9 ni en Incident ni en Secure. Los usuarios corporativos llegan con company SSU en el SAML. HIPOTESIS: el 9 sale de la compania del empleado (SSU) en lugar de la marca de la ubicacion. Pregunta para Ryan Barlow.
15 oct: vista incident.LPUser SecurityId NULL en los 49 (n 49, vista_null 49). CONFIRMADO en las dos capas.
