---
name: reference_viewreports_nettrack_legacy
description: "Unauthorized Access al entrar directo a Izenda/AdHoc en nettrack, y dónde vive el flag ViewReports que lo arregla"
metadata:
  node_type: memory
  type: reference
  modified: 2026-09-03
---

Entrar directo a `https://apps.apprissretail.com/<slug>/nettrack/AdHoc/reportlist.aspx`, incluso ya con sesión de tenant abierta vía Control Panel, puede devolver "Unauthorized Access, Could not Find entry in Screen Label table (sys_UnauthorizedAccess)". No es session cookie, es permiso.

El flag que lo desbloquea es `ViewReports`, asignado por security level, no por usuario individual. Confirmado por Kiran Vadday el 3 sep 2026, caso RCS-28482, ADUSA: "Goto Admin, make ViewReports = Yes for your security level."

Dónde NO está: `Permission Groups` del Platform nuevo, ruta `apps.apprissretail.com/<slug>/platform/cpf/usergroup`. Esa pantalla solo tiene Name, Description y Users por grupo. No expone flags legacy.

Dónde SÍ está: nettrack legacy, `https://apps.apprissretail.com/<slug>/nettrack/Admin/ManageSecuritySettings.aspx`. Es un grid con un security level por fila, ejemplo visto en Tahoe Donner: Support, Admin, Risk Management, Safety Coordinator, TDA Manager, TDA Employee, TDA Operations, TDA Mechanics. Columnas Yes/No/(not set) para varios permisos, entre ellas ViewReports, más columnas de scope como Case, Database. El grid tiene scroll horizontal, hay columnas fuera de la vista inicial. Editar con el lápiz de la fila, guardar con Save y después Save All Changes al fondo de la pantalla.

El botón "Case Type/Audit Settings" al fondo de esa misma pantalla abre un detalle distinto, checkboxes de Case Types, Case Types Allowed For Completion, Equipment Types, Audits, Action Plans, Search Audits. No es donde vive ViewReports, no confundir los dos.

Corrección del mismo caso, 3 sep 2026: en ADUSA la fila Support ya tenía View Reports en All, no en None. La única fila en None era ITSupport. Al final no hizo falta cambiar nada en `ManageSecuritySettings.aspx`, el Unauthorized Access era cache del navegador. Recargar o abrir en pestaña nueva resolvió el acceso a `AdHoc/reportlist.aspx` sin tocar ningún security level. Antes de editar una fila compartida, vale la pena descartar cache primero, es más barato y no afecta a otros usuarios del mismo nivel.

Precedente relacionado, mismo tenant Tahoe Donner: `reference_screen_designer_rebuild.md`, otro ajuste de Admin en nettrack legacy, distinto síntoma (404 por screens sin build), mismo patrón de que el arreglo vive en Admin del propio nettrack y no en el Platform nuevo.
