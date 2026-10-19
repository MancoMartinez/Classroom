---
name: reference_control_panel_admin
description: "Dónde vive cada cosa en Control Panel para administrar usuarios, según Kiran Vadday en llamada, incluido dónde NO está el flag Disabled"
metadata: 
  node_type: memory
  type: reference
  originSessionId: f1250f28-e367-4743-9ca8-90b661b376fc
  modified: 2026-08-04T23:27:17.136Z
---

Recorrido en vivo con **Kiran Vadday** (llamada agosto 2026, transcripción de Moscú). Antes de mandar a alguien a buscar en Control Panel, usar esto.

**El flag Disabled está en `User details`, arriba del todo, junto al email.** Textual de Kiran: *"it's like the very top, e-mail, user details and Disabled"*.

**Dónde NO está.** Kiran las revisó todas en vivo antes de encontrarlo y perdió tiempo: *"Permission groups, not hierarchies is also not the place. User teams, nope. Secure incident, nope. Advanced properties, nope. Yeah, there is nothing. Oh, I hate this."* Después: *"We wasted time, I'm sorry. There is Disabled."*

Debajo es la columna `Disabled` en `membership.Users`, se pone en 1. *"if I change that to one. This won't come up in the view."*

**Un usuario sin last login nunca entró.** Eso apunta a que el email en el registro está mal, no a una cuenta bloqueada. Verificado el 4 ago 2026 con Dillon Wadsworth (Big Y, RCS-28033): sin last login, y la solución fue corregirle el email y el LoginID, no desbloquearlo. Es el chequeo rápido antes de asumir bloqueo.

**Para verificar o dar accesos de admin:** entrar al sitio de producción, `All apps`, `Settings`, `Users`, buscar el usuario, `User details`, después `Permission groups`, agregar los que falten y **guardar**. Kiran: *"Try add as many as you want and save at the end. Don't forget to save."* Es más rápido que ir a la base por Bastion.

**La línea base de grupos para cualquier usuario** son tres: `ApprissCase Search Users`, `ApprissCase Users`, `Basic Users`. Kiran: *"that's basic for everybody"*. Si a alguien le faltan, agregarlos aunque no sea lo que vino a pedir.

**Manage Associates no existe con ese nombre.** En el nivel de admin la pantalla se llama **Manage Employees** (`manageemployees.aspx`). Kiran: *"we are so bad at naming our stuff"*. Al cliente y a los tickets llega como Manage Associates, así que traducir antes de buscar.

**Pestaña Hierarchies:** tres selectores, Select Hierarchy, Select Level y Select Locations. En los tenants vistos, Level 0 es Location (tienda) y Level 1 es District. El código de un nodo District viene calificado con sufijo, por ejemplo `501_2639`.

**Botón Reset Password** está en la misma ficha del usuario, arriba junto a Save.

Ver [[reference_screen_designer_rebuild]] para el truco de pantallas rotas y [[reference_esquema_usuarios_incident]] para las llaves de join correctas.
