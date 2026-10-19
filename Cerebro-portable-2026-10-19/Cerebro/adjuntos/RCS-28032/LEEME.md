# Adjuntos RCS-28032

Subidos por Juan el 24 ago 2026. Origen: correo reenviado por Joe Austin al ticket el 18 ago.

## Re__D501_LPMS.eml

Hilo interno de Vitamin Shoppe, asunto "Re: D501 LPMS".
De Dayna Rivera a Joe Austin, con copia a Brandon Bigelow y Danielle Watts, 11 ago 2026 16:22 UTC.
Firma de Dayna: District Sales Manager, S Wa and Oregon, dayna.rivera@vitaminshoppe.com, 832-858-7817.

Texto de Dayna, literal:

> Previously before the last update, on this screen it would show the two districts and allow me to
> choose one before it asked me to pick a store. These screen shots are from 9:15 AM PST on 8/11.
> But this is what I have been seeing since the last update with the only difference being I could
> only see D504 and not D501 and after yesterday, it's the opposite.
>
> After yesterday, I now only have D501 access. If I choose a store in D504, it won't load the
> location number
>
> If I try to continue anyway, I get this error message about selecting a location number
>
> Additionally, I tried to search to see what stores had completed the Store Loss Audit and only D501
> now shows up. I'm also not getting alerts for anything D504 does anymore, audits, incident reports, etc.

Cadena previa del mismo hilo, en orden:

- 3 ago, Dayna: "I still do not have access to D501. I tried several stores"
- 4 ago 10:10, Joe: "I was informed that you should have access now. Can you verify?"
- 10 ago 08:47, Dayna: seguimiento pidiendo acceso a las auditorias de D501
- 10 ago 18:05, Dayna: "I have access to D501 now, but have lost access to D504"
- 11 ago 05:33, Joe: traslada el pedido de capturas de Juan y avisa que suma a Brandon por su PTO

## Capturas extraidas del correo, en `eml_extract/`

| Archivo | Que muestra |
|---|---|
| `att26_image.png` | Chrome en `https://apps.apprissretail.com/vitaminshoppe/nettrack/Audit/NewAudit.aspx`. Pantalla New Audit, tarjeta Select Location vacia, texto "STEP 1: Please click in the field above to enter a store number, address, city, etc. to find a store". Boton Next deshabilitado. Es la pantalla donde antes del update aparecian los dos distritos. |
| `att27_image.png` | Misma pantalla New Audit con "1016" escrito en Select Location. El numero de tienda no resuelve. |
| `att28_image.png` | Misma URL NewAudit.aspx. Select Audit Class con "District Manager SVS" seleccionado, Audit Name "Customer Experience Summary", y banda roja al pie: "Please select a location and try again." |
| `att29_image.png` | `https://apps.apprissretail.com/vitaminshoppe/nettrack/Audit/AuditLog.aspx`. General Filters, rango 6/28/2026 a 8/10/2026, Audit Description "Store Manager Store Loss Review". Al pie el alcance efectivo de la usuaria: Division "The Vitamin Shoppe", Ops Region "3", Ops District "501". Solo 501, no aparece 504. |
| `att30_image.png` | Misma AuditLog.aspx ya ejecutada, Default Audit View con resultados. Audit Case Number 1011-114855 del 08/10/2026, 90.72 por ciento, 88 de 97 puntos. Audit Case Number 1015-114807 del 08/07/2026, 88.66 por ciento, 86 de 97 puntos. |
| `att17_image017.png` | Control Panel, User details de Dayna. Email dayna.rivera@vitaminshoppe.com, First name Dayna, Last name Rivera, Title "DSM D504 & D501". |
| `att16_image016.jpg` | Foto de firma o imagen del pie de correo, sin valor diagnostico. |
| `att01` a `att15`, `att18` a `att25` | Iconos de firma de correo y repeticiones de las mismas capturas. Sin valor diagnostico. |

## Capturas sueltas subidas junto al .eml

Corresponden al tramo del 29 jul, la parte de Brandon Bigelow, ya cerrada.

| Archivo | Que muestra |
|---|---|
| `image-20260729-161147.png` | Correo original de Brandon a support@apprissretail.com, 29 jul, asunto "Access Issues", con la captura del Session Error embebida. |
| `image-20260729-161311.png` | Jira Service Management, espacio Retail Customer Support, pestana Customers. Busqueda de `Brandon.Bigelow@vitaminshoppe.com` sin resultados, "No matches for your search". |
| `image-20260729-161351.png` | Misma pantalla Customers. Busqueda de `joseph.austin@vitaminshoppe.com` con resultado: Joe Austin, 4 open requests, 70 closed requests, Active. |
| `image-20260729-163104.png` | Correo de acuse de Appriss Retail Support a Brandon, asunto "[RCS-28032] - Vitamin Shoppe - Access Issues", con Joe Austin en copia como reporter. |
| `image-20260729-163131.png` y `image (7).png` | Pantalla "Session Error": "Your Incident session could not be established. This is usually caused by a temporary account configuration issue. Please return to the Secure portal and sign in again. If the problem persists, contact your administrator." |
| `image (8).png` | Recorte del correo de Dayna a Joe: "Hey Joe / I still do NOT have access to D501", firmado Dayna Rivera. |
| `image001.png` y `image (1)` a `image (6)` | Logo de The Vitamin Shoppe e iconos de firma. Sin valor diagnostico. |
