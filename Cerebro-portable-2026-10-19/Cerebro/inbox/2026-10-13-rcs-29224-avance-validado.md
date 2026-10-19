RCS-29224, corrección del plan, 13 octubre 2026

Sustituye el avance anterior. Jira hoy: Escalated, Enrique. Rocky espera desde el 12 oct; el 9 oct confirmó TODOS los archivos.

Capturas de Juan, jueves 8 oct: adjuntos/RCS-29224/2026-10-08-teams/01.png a 05.png.
Jenny: inventory_itemposition usa cantidades e importes de ventas/devoluciones de ardm_item. El diseño anterior esperaba todo el inventario y POS procesado. Advierte valores incorrectos si POS no está listo; no certifica SnowTime.
Daniel: anunció fix y limpieza nocturna, con incertidumbre. El anuncio no prueba ejecución.

PR 58891: Completed, main, Daniel, 8 oct 16:32 Bogotá, e98fffb9. Deploy dbt Project y Setup Raw seleccionados; éxito del despliegue AAP y limpieza no verificados.
https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/SnowTime/pullrequest/58891

El diff AAP enrich_ardm_item.sql conserva Verify y recupera department, descripción e impuesto desde su gemelo XBR/TLOG; actualiza updateddatetime. Atiende ventanas separadas. El fragmento no demuestra recálculo de inventory_itemposition.
Claude, sin mediciones verificadas aquí, avala retrasar solo inventario mirando costes. No cubre la dependencia de Jenny ni todos los archivos. Se retira la conclusión general “sin defecto”.

Hoy Enrique:
1. Pedir a Daniel resultado del despliegue, limpieza y fechas reparadas; validación de llegadas separadas y totales de inventario.
2. Validar con Jenny/Viraj POS completo antes del cálculo o recálculo al llegar tarde. Comparar cantidades/importes por tienda, SKU y día; contar filas no basta.
3. Luego coordinar monitoreo con Raman y horarios consumidores. Confirmar zona horaria y fecha aprobada, no antes del 21 oct.
Mover todos ocho horas no garantiza que coincidan sus ventanas.
Mantener Escalated mientras siga abierta la validación interna.

Precedentes: RCS-29244, recuperación visible sin validar integridad; RCS-27837, llegada frente a procesamiento. Compromiso publicado: Juan volvería con actualización; sin fecha. Hoy dar avance a Rocky, sin aprobación final. Nada enviado.

Borrador para Daniel:
Hi Daniel, for AAP (021), RCS-29224, PR 58891 is merged. Did the AAP deployment and overnight cleanup complete, and which dates were repaired? Does the fix also ensure inventory_itemposition sales and return totals are refreshed when POS arrives later? The client now proposes moving all files to 9:30 AM, no earlier than October 21. What validation or adjustment is still needed before we confirm this?
