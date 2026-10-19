---
name: reference_hosts_pu_vs_clasico
description: "Qué host es Platform Unification y cuál es la plataforma clásica, y por qué eso decide quién administra los permisos de un usuario"
metadata: 
  node_type: memory
  type: reference
  originSessionId: a8293f75-ab64-479b-971f-f586abf0f63b
  modified: 2026-08-18T22:55:57.375Z
---

Aclarado por **Kiran Vadday** el 18 ago 2026, resolviendo el caso de David Vargas sin acceso a
dashboards de Nordstrom (RCS-28219).

| Host | Qué es |
|---|---|
| `app.apprissretail.com` | **Es PU** (Platform Unification). La plataforma unificada. |
| `usprod.apprissretailcloud.com` | **NO es PU todavía.** Plataforma clásica, US Producción. Aquí vive Control Panel (`/control`). |
| `euprod.apprissretailcloud.com` | Equivalente europeo, clásico. |
| `<tenant>.apprissretailcloud.com` | Host con nombre del cliente sobre la misma pila clásica. |

**Por qué importa.** El host decide **quién y dónde** se administran los permisos:

- Si el usuario entra por **usprod**, está en la plataforma clásica y sus permisos se
  administran desde **Control Panel USPROD**, a lo que Juan ya tiene acceso
  (`SupportL2` + `Engineers`). No hace falta escalar a nadie. Ver
  [[reference_control_panel_admin]] y [[project_juan_accesos]].
- Si entra por **app.apprissretail.com**, está en PU y ahí sí entra el equipo de Kiran.

**Antes de escalar un problema de permisos, mirar la barra de direcciones.** El host en la
URL del error dice de qué lado está el usuario, y por lo tanto si el caso es tuyo o de otro
equipo.

**Vocabulario de Kiran**: cuando pide *"the signing url"* quiere la URL de **inicio de
sesión**, no un enlace profundo a un dashboard o a un search. Con la URL de login identifica
plataforma y tenant; con un `#/dashboard/...` no puede.

Ver [[reference_control_panel_admin]], [[project_juan_accesos]],
[[reference_unificacion_patrones]].
