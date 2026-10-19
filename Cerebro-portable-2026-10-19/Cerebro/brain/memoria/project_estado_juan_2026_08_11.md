---
name: project_estado_juan_2026_08_11
description: Estado de los 17 tickets de Juan al cierre del 11 ago 2026 y lo que quedó pendiente en cada uno
metadata: 
  node_type: memory
  type: project
  originSessionId: 8b73134e-5723-4d74-be14-e59eb99f9e25
  modified: 2026-08-12T00:16:43.593Z
---

**Pendientes concretos al cierre del 11 ago:**

- **RCS-28021, ADUSA Izenda.** Leigh Ann confirmó que la usuaria limpió caché y probó en incógnito, Edge y Chrome, y sigue sin poder exportar, sin mensaje de error. Ya no es arrastre del timeout corregido: es el mismo Izenda que Colton reporta en Tailored Brands (RCS-28256), donde hay Ray ID `a299728c9ee465e3`. Son un solo problema.
- **RCS-28033, Big Y.** Kevin probó el Add Person él mismo y le salió error, con captura. Regresión confirmada por el cliente.
- **RCS-27959, PACSUN.** Jongki confirmó que las IPs de producción son las mismas de staging y avisó que **son adicionales, no reemplazo**. RETAILIT-20648 dice que ya actualizaron el allow list, pero el aviso de Jongki llegó 49 minutos antes del cambio, así que hay que confirmar que no quitaron las viejas.
- **RCS-28153, Big Y.** Ashley pidió el timeout en **240 minutos**. El cambio sigue sin aplicar.
- **RCS-27991, Engage Analytics.** Sin moverse desde el 3 de agosto. Es el High más viejo y el empujón a Amy Tsushima nunca salió. Ruta formal si no contesta: Under Engineering Review con Ian Williams y mensaje de Teams obligatorio, porque no ve la asignación solo.

**Cambios de interlocutor:** en RCS-28032, Joe Austin salió de PTO el 11 de agosto al mediodía y dejó a **Brandon Bigelow** en el ticket. Lo que se escriba de ahora en adelante va para Brandon.

**Estado de RCS-28032**: Dayna ahora ve el distrito 501 y perdió el 504, después de que el 4 de agosto le agregaran los dos. Confirma el modelo de [[reference_jerarquia_ubicaciones_incident]]: solo se hereda el distrito del StoreIdent primario.

**RCS-28256** quedó resuelto en la parte de sign in y creación de incidentes, confirmado por Colton el 11. Izenda sigue abierto y sin dueño; el detalle completo está en [[project_rcs_28256_tailored_brands]]. Ojo con lo de arriba: que RCS-28021 y RCS-28256 sean el mismo Izenda es **hipótesis**, no está confirmado. Lo que hay es que Matt enlazó ENG-6777 al fallo de export de Izenda de Vitamin Shoppe. Hasta que alguien lo confirme se deja escrito como hipótesis, no como hallazgo ([[feedback_agrupar_no_es_causa_raiz]]).

**Lo primero al día siguiente: la llamada con Peyman.** Guion en `~/Desktop/guion-llamada-peyman-2026-08-11.md`, **no ha ocurrido**. Antes de marcar, correr la línea 1 de `1.sql` para dejar el 40 de 994 en pantalla. Dos decisiones a la salida: si se le escribe a Joe, y quién toma Ahold. Los paquetes de RCS-28003 (Nike) y RCS-28077 (Ahold) se escriben después de la llamada, no antes. En RCS-28003 el defecto del `null` literal dentro de la dirección, 390 de 994, se rutea por Support Data Team, primero John Morgan y Peyman si no está. En RCS-28077 va comentario interno con la duplicación diaria, asignar a Peyman, sprint `RCS Support Team` y comentario corto a Jacquelyn; **el DELETE no se ejecuta**. Ver [[project_rcs_28077_28003]].

**Borradores ya escritos y sin publicar**, todos en `~/Downloads/RESPUESTAS-NUEVAS-2026-08-11.md`: los dos comentarios de RCS-28153 Big Y (falta aplicar el timeout de 240 y verificar que no quedó solo en `CustomerEditedValue`) y los dos de RCS-28032 Vitamin Shoppe. Pendientes de trámite: RCS-28123 ADUSA a Under Customer Review, RCS-27978 Myer con comentario de cierre y los dos pasos Resolve a Completed y luego Close, RCS-28055 Gen Parts sin respuesta humana en 12 días, y RCS-28152 a Manisha Naik.

**Arrastre viejo:** los 77 punteros colgando de ADUSA sin enviar a Kiran, y RCS-27959 PACSUN a Under Security Review después de revisar el CASD del 23 jul.

Relacionado: [[project_reparto_cola_2026_08_11]], [[reference_waf_cloudflare_bloqueos]], [[project_estado_abierto_2026_08_05]].
