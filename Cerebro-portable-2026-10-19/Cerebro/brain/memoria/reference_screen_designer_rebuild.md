---
name: reference_screen_designer_rebuild
description: "Truco de Kiran Vadday para arreglar pantallas rotas / 404 en un tenant: rebuild vía Screen Designer con ?ADMIN=9QQP"
metadata: 
  node_type: memory
  type: reference
---

Cuando un cliente reporta que una pantalla del sistema no carga (404, "Page Not Found", error genérico al abrir un tipo de incidente/reporte), este es el atajo que usa Kiran Vadday (Engineering) para reconstruir las pantallas del tenant:

1. Admin > Screen Designer, dentro del nettrack del cliente afectado
2. Editar la URL a mano agregando `?ADMIN=9QQP` al final, Enter. Ese parámetro desbloquea una vista de admin que no aparece por default
3. Al fondo de la pantalla aparece el botón **"Build All Screens"**, click ahí
4. Volver a probar usando el **mismo link** del caso/incidente que daba error, no hace falta crear uno nuevo

**Confirmado funcionando el 3 ago 2026** en Tahoe Donner (RCS-27573): after rebuild, Guest Incident Injury Report - Summer volvió a cargar en location 010.

**Advertencia, no ejecutar a ciegas:** en el caso de Santikos (RCS-28022, 31 jul 2026), el mismo Build All Screens coincidió con que la lista de Incident Types del tenant quedó en cero después. No está probada la causalidad, pero después de cada rebuild hay que revisar también que los Incident Types del cliente sigan poblados, no solo que la pantalla cargue.

Ver [[project_flujo_tickets]].
