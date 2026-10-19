# RCS-28482. Verificar el fix de Mohammed y cerrar con Jim

Verificado en vivo en Jira, 4 sep 2026. Cronología real, no la de la ficha del cerebro que decía
"comentario no pegado", ya está pegado desde ayer 16:34.

Ayer pegaste el internal note y el update a Jim. Jim agradeció a las 17:19. Shandana asignó a
Mohammed Mutahhar hoy a las 4:06 am como SRE de turno. Mohammed respondió hoy 8:30 am con causa
técnica y un fix propuesto, y te etiquetó pidiendo que confirmes y avises al cliente. Estado actual
en Jira: Under Support Review, tú de assignee otra vez.

Lo que dijo Mohammed, verbatim: la pestaña sale en gris porque el join hacia el datasource Store no
está completo. En Data Sources, la fila que compara `incident.Employee.EmployeeID` contra
`StoreManagerID` tiene el lado derecho del igual vacío, muestra "..." en vez de "Store". Si
reconstruyes esa condición, cambiando el datasource lejos de Store y volviendo a ponerlo, el
desplegable debería ofrecer "Store" como opción. Al seleccionarlo, todas las pestañas vuelven,
incluida MISC.

No lo dio por probado él mismo. Dijo "I don't know how it got into this state". Te toca confirmarlo
en el reporte real antes de decirle a Jim que está resuelto.

## Paso 1. Entra a Izenda

Mismo camino de ayer. Si la sesión sigue activa, ve directo a
`https://apps.apprissretail.com/adusa/nettrack/AdHoc/reportlist.aspx`. Si pide login otra vez,
repite Control Panel, Customers in USPROD, ADUSA, Click logo to sign in.

## Paso 2. Abre PBI - Current Location Listing en Report Designer

Categoría Jim Cosseboom Test. Ábrelo con el lápiz para entrar al Report Designer, no solo al viewer.

## Paso 3. Ve a Data Sources y busca la fila del join a Store

Busca la fila con `incident.Employee` y `EmployeeID` en la izquierda, y a la derecha del signo
igual el campo que debería decir `Store` y en cambio muestra "...". Esa es la fila que describió
Mohammed.

## Paso 4. Reconstruye la condición

Haz clic en el desplegable vacío del lado derecho. Cambia la tabla a cualquier otra opción
temporalmente, y vuelve a abrir el desplegable. Si "Store" aparece ahora como opción, selecciónalo.

## Paso 5. Confirma que las pestañas volvieron

Mira la fila de arriba. Deberían estar todas otra vez: Data Sources, Fields, Summary, Chart, Gauge,
Map, MISC, Style, Filters. Haz clic directo en MISC y confirma que abre el panel de distribución,
no que se queda en gris como ayer.

## Paso 6. Guarda

Save, no Save As. Confirma que no crea una copia duplicada del reporte.

## Paso 7. Repite exactamente lo mismo en Outlook Export (Jim Cosseboom Test)

Misma categoría Jim Cosseboom Test. Mismos pasos 3 a 6.

## Paso 8. Según lo que encuentres

Si MISC responde en los dos después del fix, pega la respuesta a Mohammed y el aviso a Jim, los dos
archivos de abajo, en ese orden.

Si en alguno no funciona, o si "Store" nunca aparece en el desplegable, no pegues ninguno de los dos
todavía. Vuelve a Mohammed con lo que pasó exactamente, sin decir que funcionó si no funcionó.

---

## Si funcionó: respuesta a Mohammed, en el hilo de RCS-28482

```
Hi Mohammed,

Confirmed on both reports. Rebuilding the Store join and reselecting Store restored the full tab set on PBI - Current Location Listing and Outlook Export, MISC included.

Updating the client now. Thank you for the fix.
```

## Si funcionó: aviso a Jim, en el hilo de RCS-28482

```
Hi Jim,

This one is resolved. The MISC tab is available again on both PBI - Current Location Listing and Outlook Export, and you should be able to change the report distribution as before.

Please confirm on your end when you get a chance.

Thank you.
```

## Si NO funcionó: respuesta a Mohammed

Reemplaza [DESCRIBE QUE PASO] con lo que viste realmente, paso por paso, antes de pegar.

```
Hi Mohammed,

Tried the rebuild on both reports. [DESCRIBE QUE PASO]

Have not updated the client yet. Let me know how you want to proceed.
```
