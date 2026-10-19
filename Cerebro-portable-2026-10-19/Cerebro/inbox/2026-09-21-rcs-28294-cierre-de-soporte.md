# RCS-28294, cierre de la parte de soporte

Las capturas de Client ID 432 confirman los dos logs que Matt Kamminga describio en su
diagnostico del 18 de septiembre. Log 0, 2:14:12pm, "Quit ProcessSmartAlert because the smart
alert for the case is still on processing, pSystemType=HR, pSystemID=48786", es el flag
incident.Shoplifting.inprocess pegado en 1. Log 16, 2:17:52pm, BlobNotFound 404 en
Printing.CreateDocument, es el segundo problema, el documento de impresion de la alerta que no
existe en Azure Blob Storage.

Matt ya aplico un workaround para el segundo problema tambien, actualizo la ubicacion de los
print docs de Vallarta para que las alertas ERMS de HR sigan saliendo, y le pidio a Shandana Khan
que le reasigne el ticket a el cuando el fix de codigo real quede listo para el proximo sprint.

No queda nada de soporte por investigar aca. La unica accion de Juan es un comentario corto de
cierre confirmando el estado y dejando en registro que support espera la reasignacion. Texto
sugerido, listo para pegar:

Root cause confirmed. ShopliftingID 48786 had incident.Shoplifting.inprocess stuck at 1, likely
from an August issue, which made the smart alert engine abort with Quit ProcessSmartAlert because
the smart alert for the case is still on processing. Matt Kamminga cleared the flag and relaunched
the process, which surfaced a second issue, a 404 BlobNotFound error from Printing.CreateDocument
when generating the alert print document. Matt applied a temporary workaround updating the print
doc location so ERMS alerts keep firing while the permanent code fix is scheduled for next sprint
under his ownership. No action pending on support for this ticket. Following up once the
reassignment to Matt goes through to track the code fix separately.

Bitacora actualizada con la confirmacion de los logs.
