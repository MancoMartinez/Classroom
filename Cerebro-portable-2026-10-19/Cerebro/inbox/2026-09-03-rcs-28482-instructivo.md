# RCS-28482. Reproducir, documentar y pasar a Ingeniería

## Paso 1. Entrar al tenant

1. Entra a `https://usprod.apprissretailcloud.com/control`.
2. Tabla *Customers in USPROD*, busca Ahold Delhaize USA / ADUSA, Client ID 441.
3. Primera columna, Click logo to sign in. No uses `/adusa/signin`, eso manda al SSO del cliente y tu usuario de Appriss no existe ahí. Si el logo falla, agrega `?admin=true` al final de la URL de signin.

## Paso 2. Si el link de Izenda da Unauthorized Access

Primero recarga la página o ábrela en una pestaña nueva. En este ticket fue cache del navegador, no permiso, ViewReports en Support ya estaba en All.

Si sigue sin cargar después de recargar, ahí sí revisa el security level en `https://apps.apprissretail.com/adusa/nettrack/Admin/ManageSecuritySettings.aspx`, columna View Reports de tu fila.

## Paso 3. Entrar a Izenda y reproducir

7. Ya con `ViewReports` habilitado, ve a `https://apps.apprissretail.com/adusa/nettrack/AdHoc/reportlist.aspx`.
8. En la lista de reportes busca PBI - Current Location Listing (Jim Cosseboom Test), ábrelo. Mira la fila de pestañas arriba: Data Sources, Fields, Preview. Confirma que MISC no aparece o aparece en gris, sin poder hacer clic.
9. Repite con Outlook Export (Jim Cosseboom Test).
10. En la misma lista, abre un tercer reporte que no sea clon de estos dos y que sí tenga MISC habilitado. Cualquier reporte activo del tenant que uses de referencia sirve.
11. En cada uno de los tres, abre la pestaña Data Sources y anota qué tipo de reporte es. Ese dato es el que falta para confirmar o descartar la hipótesis de Juan del 24 de agosto.

## Paso 4. Escribir el internal note con esa evidencia

El texto pegable vive aparte, en `inbox/2026-09-03-rcs-28482-comentario-interno.md`. Es formato de escalación a ingeniería de `cerebro-comentario`, markdown completo, las seis secciones. Abre ese archivo, selecciona todo, pégalo en RCS-28482. No copies desde acá.

## Paso 5. Transicionar y asignar

Status a Under Engineering Review. Assignee a Shandana Khan.
