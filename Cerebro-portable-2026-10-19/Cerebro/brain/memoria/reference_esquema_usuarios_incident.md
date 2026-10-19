---
name: reference-esquema-usuarios-incident
description: "Mapa de tablas de usuarios y jerarquías en la plataforma Incident, explicado por Kiran Vadday el 30 jul 2026, y cómo compararlas sin equivocarse."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 9fc04b4a-14c1-4cb0-b5b5-97ac10fcabe5
  modified: 2026-08-14T23:15:02.418Z
---

Explicado por **Kiran Vadday** (bvadday@apprissretail.com) el 30 jul 2026, tras dos discrepancias donde ella y Juan miraban capas distintas.

**Llaves de comparación correctas, nunca por ID numérico:**

| Tabla o vista | Columna de identidad |
|---|---|
| `membership.Users` | `username` |
| `incident.lpuser` (vista) | `loginid` o `email` |
| `incident.lpuser2` | `loginid` y `emailaddress` |

**Ruta de la migración:** `incident.lpuser2` → `membership.Users` **y** `secure.LocationHierarchyUserAssignments` (lhua). Los usuarios que originalmente vivían en el esquema `incident` se migran al lado `secure`.

**Fuente de verdad:** para clientes que son solo Incident, sigue estando en el esquema `incident`, **principalmente la vista `lpuser`**. Pero esa vista está construida a partir de `membership.Users` más `incident.lpuser2`.

**Regla operativa, textual de Kiran:** *"Secure.lhua y lpuser view both must be checked"*. Las dos, no una.

**Los dos errores que causaron las discrepancias:**

1. **Umbral numérico de UserID** para delimitar el bloque nuevo de unificación. No sirve: hay clientes cuyos IDs nativos ya están en ese rango (ADUSA arranca en 1.800 millones, y por eso una query devolvió 2.300 falsos positivos).
2. **Reportar una sola ruta de join.** Unir por `incidentUserID` y unir por email dan respuestas distintas y las dos son ciertas: la fila puede existir por email con el vínculo vacío. Siempre sacar las dos rutas en columnas separadas.

**Tres clases de fallo distintas, verificadas en ADUSA el 10 ago 2026.** No son el mismo bucket y no se arreglan igual:

1. **Fila mal apuntada en `lhua`**: el `place.Location` asignado tiene `LocationHierarchy2Description` distinto de `incident.Store.Division`. Es lo que corrigió Kiran el 31 jul con su script de DELETE + INSERT.
2. **Sin ninguna fila en `lhua`**: el usuario no tiene asignación de ubicación. **El script de Kiran nunca los toca**, porque solo reinserta para los usuarios que él mismo acaba de borrar (`#FixedUsers`). Por eso alguien puede seguir roto después de un arreglo "across the board". Síntoma: entra bien pero no ve tiendas y no puede crear caso. Se arregla **desde Control Panel**, pestaña **Hierarchies** del usuario, Select Hierarchy → Standard Location Hierarchy, nivel **Location**, y la ubicación es el `place.Location.LocationID` de su tienda. La columna "Location Code" de esa pantalla **es el LocationId**. No hace falta tocar la base.
3. **Puntero colgando**: `membership.Users.IncidentUserID` apunta a un `UserID` que no existe en `incident.LPUser2`. **77 usuarios activos así en ADUSA** el 10 ago. Este es el vínculo roto que rompe `GetSSOPermissionGroupsByUserName`. Soporte no lo puede arreglar.

**Las clases 2 y 3 son en realidad el mismo defecto.** En ADUSA, **75 de esos 77 tampoco tienen fila en `lhua`**. El proceso de alta escribe en `membership.Users` y se salta las dos tablas de abajo. Autenticar solo necesita `membership.Users`, así que el usuario entra sin problema y después no ve tiendas ni puede crear caso. **76 de los 77 ya habían iniciado sesión.** Todos creados el 27 jul o después, la fecha del corte, a razón de 5 a 15 por día y todavía sumando el 10 de agosto. Contraejemplo del mismo lote: dos usuarios creados el 29 jul en el mismo segundo sí tienen las dos filas, así que el alta falla de forma intermitente, no siempre. Síntoma confirmado en un solo usuario (Edward Colo); los demás están en el mismo estado en base, que no es lo mismo que probados.

Pista sobre el origen del #3: en ADUSA los usuarios migrados tienen `UserID` de 578xxxxxx o 1816xxxxxx con `Active = -1` y correo @ahold.com, mientras que los creados después traen IDs bajos de 5 dígitos con `Active = NULL` y correo de la marca (@stopandshop.com). Los punteros colgando caen en ese rango bajo, así que apunta al proceso que crea filas nuevas, no a la carga original de la migración.

**Ojo con el dominio al buscar.** `LPUser2` guarda @ahold.com y `membership.Users` guarda el de la marca. Buscar por un solo dominio da falso negativo.

**Ojo con el join por nombre.** El script de Kiran une por `FirstName` + `LastName`. En Control Panel hay gente con nombre legal distinto del de Incident (Anthony Harris aparece como Jerry Harris) y filas con nombre y apellido invertidos. Esos usuarios son invisibles tanto para el diagnóstico como para el arreglo.

**Pestañas de Control Panel que no son lo mismo**: *Permission groups* define qué puede hacer (en ADUSA la base son tres: ApprissCase Search Users, ApprissCase Users, Basic Users), *Hierarchies* define sobre qué ubicaciones. Un usuario con los grupos completos y Hierarchies vacío entra y no ve nada.

**Actualización del 14 ago 2026, verificada en ADUSA.** El detalle completo con conteos y consultas está en [[reference_lpuser_lpuser2_membership]]. Lo que confirma o corrige esta ficha:

- La pista del final de arriba quedó **confirmada con nombres**. Los migrados con `UserID` 578xxxxxx o 1816xxxxxx y correo @ahold.com llevan además el `LoginID` con prefijo **AA** o **US** más el número de empleado. Duane Masimore, `AA00503189` / UserID 578353135, contra `00503189` / duane.masimore@giantfood.com en membership. Jesse Trimbach, `US00065002` / UserID 1816868828, contra `00065002` / jesse.trimbach@stopandshop.com.
- **`membership.Users` se sembró desde `incident.LPUser`, no desde LPUser2.** Los conteos lo prueban: LPUser 11.073, membership 11.073, LPUser2 12.370. Kiran dice que la verdad para nettrack es LPUser2, así que membership quedó apuntando a la tabla que no manda.
- **La bandera de aprobador es `membership.Users.SupervisorFlag`.** No está en LPUser2 ni en LpSecurity.
- El umbral numérico sigue sin servir, ahora por otra razón más: el rango 50000-59999 parece sintético y son `UserID` reales de `incident.LPUser`, con gente válida dentro.

Ver también [[project-membership-users-13]] y [[project-juan-accesos]].
