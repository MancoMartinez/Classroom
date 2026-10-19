# Flujo de debug para Smart Alerts que nunca disparan, via debug logs en control panel

Origen. RCS-28294, Vallarta. Comentario de Matthew Kamminga, 18 sep 2026, 11:51am.

## El metodo

1. Los debug logs del control panel de netTrack se disparan cada vez que se guarda un incidente.
   No hace falta esperar un batch ni buscar en Application Insights primero.
2. Guardar el incidente sospechoso una vez y revisar los debug logs en el control panel.
3. Buscar el ShopliftingID del caso en el log. Si el motor de Smart Alerts lo esta descartando
   antes de evaluar el filtro, aparece un log tipo "Quit ProcessSmartAlert because the smart alert
   for the case is still on processing", con pSystemType y pSystemID.
4. Ese mensaje apunta al flag `incident.Shoplifting.inprocess`. Si quedo en 1 y nunca volvio a 0,
   el motor asume que ya hay un proceso corriendo sobre ese caso y aborta sin evaluar nada. Cero
   filas en `incident.SmartAlertProcess` no es el filtro fallando, es el motor nunca invocado.
5. Liberar el flag en produccion, un solo UPDATE dirigido por ShopliftingID:
   `update incident.shoplifting set inprocess = 0 where shopliftingid = <ID>`
6. Volver a guardar el incidente para relanzar el proceso.
7. Revisar los debug logs otra vez. Si aparece un log tipo "SmartAlert.ProcessSmartAlert.Warning"
   con "Printing.CreateDocument" y un 404 BlobNotFound de Azure Blob Storage, el motor si evaluo
   el filtro y si intento generar el documento de impresion de la alerta, pero el blob del
   documento no existe. Es una falla distinta, en la generacion del documento, no en el flag.

## Caso de referencia, RCS-28294

ShopliftingID 48786, CaseNo 2026-ADUP-45-79, el mismo que quedo con cero filas en la
investigacion de agosto.

Log 1, 18 sep 2:14:12pm, ClientID 432:
"0. Quit ProcessSmartAlert because the smart alert for the case is still on processing.
pSystemType=HR, pSystemID=48786"

Matt corrio `update incident.shoplifting set inprocess = 0 where shopliftingid = 48786` y volvio
a guardar el incidente.

Log 2, 18 sep 2:17:52pm, ClientID 432:
"16. SmartAlert.ProcessSmartAlert.Warning: ID=48786|AlertName=HR Alert 1|Going back to process
other alerts|Printing.CreateDocument: The specified blob does not exist. ErrorCode: BlobNotFound"
AzureAppName web-prd-wus2-arp-nettrack, AzureDeploymentSlot production, deployment_environment
usprod.

Capturas de ambos logs en `investigaciones/evidencia-smart-alerts-inprocess-2026-09-18/`.

## Conclusion de Matt

Dos fallas separadas bajo el mismo sintoma de "la alerta no llego".

Falla A, el flag inprocess trabado. Explica por que el motor nunca se invoca para un caso que
cumple el filtro. Glitch de agosto, sin causa raiz identificada del porque se trabo, solo el
sintoma y el fix manual.

Falla B, BlobNotFound al generar el documento de impresion de la alerta. Nueva, descubierta al
forzar el reproceso de 48786. Matt dijo que hay que abrir un bug nuevo para esto. Todavia no
existe ese ticket.

## Para promover a la base

Este metodo de debug sirve para cualquier caso donde el cliente reporta que una alerta no llego
y `incident.SmartAlertProcess` muestra cero filas para el ShopliftingID en cuestion. Encaja como
mecanismo nuevo en `investigaciones/smart-alerts-familia-de-fallas.md`, que ya documenta siete
mecanismos bajo el mismo sintoma, o como entrada de diagnostico en `flujos/INDICE.md` junto a
`flujos/diagnostico-por-codigo-de-error.md`.

Juan decide donde queda y lo cura a mano, `flujos/` e `investigaciones/` no se pisan por script.
