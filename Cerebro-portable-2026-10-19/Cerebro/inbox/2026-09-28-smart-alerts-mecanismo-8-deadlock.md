# Smart Alerts, mecanismo 8: deadlock en ProcessSmartAlert (sep 2026)

Para agregar a investigaciones/smart-alerts-familia-de-fallas.md como mecanismo 8. Fuente: RCS-29026, RCS-29123 (ADUSA 441) y RCS-29145 (Vitamin Shoppe 433), 24 al 28 sep 2026.

## Sintoma
El cliente reporta que no sale ninguna alerta desde una fecha. Smart Alert History vacio para casos nuevos. incident.SmartAlertProcess sin filas nuevas. Varios tenants a la vez: Kiran encontro varios clientes con ultimo registro el 9/24.

## Firma en Grafana
Corridas que llegan a "13a. Ready to send email" y nunca a 13b, 14 ni End. InProcess queda en 1. Cada guardado posterior del caso sale con "0. Quit ProcessSmartAlert because the smart alert for the case is still on processing". ProcessAlertQueue crece. ADUSA: ultimo End 9/24 11:06:43 UTC. Vitamin Shoppe: el cliente lo ubica el 9/23.

## Causa, confirmada por Kiran Vadday
Deadlock cuando varias corridas procesan en paralelo bajo carga. Aparecio primero en ADUSA por volumen, pero Vitamin Shoppe mostro lo mismo con menos trafico.
Segundo sintoma que menciono Kiran: la llamada de SmartTrack que registra actividad de la alerta devolvia 500.

## Fix
PR 58273 (https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/Secure/pullrequest/58273), una linea: la corrida espera a que termine la anterior. Cherry pick a release. Staging validado 9/27 23:56 UTC, ShopliftingID 1119654, config 364. Europa primero, US prod 9/28. Jim confirmo alertas desde 2:30 PM EDT 9/28.

## Reglas que dejo
1. El fix es solo hacia adelante. No sabe que casos quedaron atascados ni los reprocesa.
2. Guardar un caso con InProcess = 1 no dispara nada. Hay que poner InProcess en 0 primero.
3. InProcess = 1 solo no prueba atasco. El flag vale 1 cada vez que una corrida esta en curso. Atasco = 13a sin End en Grafana, sin fila en SmartAlertProcess y Quit posteriores.
4. Reenviar alertas perdidas es manual y decision del cliente. ADUSA pidio solo hacia adelante (Jim, avalado por J.R.). Vitamin Shoppe: se ofrecio reenvio por numero de caso.

## Pistas falsas que costaron tiempo
1. Direcciones duplicadas en la lista. Kiran quito Silvana.Baxter y bj.robinson de AlertConfig 218 el 9/27. No era la causa.
2. Limite de 30MB de SendGrid. Real pero aparte: rebote por tamano a Jim el 9/21 08:24 UTC. Russ limito SMTP a 25MB el 9/27. En el bloqueo los adjuntos eran 0/0.
3. Frontera de medianoche UTC. Descartada: 9:20 PM en pantalla de Juan eran 4:20 PM ET.
4. Caso de prueba abierto. Las alertas de ADUSA exigen caso Closed. Un caso de prueba Open da Quit o 6a sin match y no prueba nada.

## Hallazgos colaterales, verdaderos y fuera de este mecanismo
1. SmartAlert.vb escribe Success en SmartAlertProcess sin revisar el resultado de SendGrid. Success no prueba entrega.
2. SendGrid descarta como Invalid direcciones con salto de linea CRLF dentro: jamie.holl\r\nand, johnna.krac\r\nhinski, bj.robin\r\nson, retflassetprotectiondivisio\r\nnalmgrsall en Security Deficiency #0513 y Medical Incident #2213. Limpieza con Kiran.
3. Bounced reales: tuckner.francois@giantfood.com, ghosmer@adusa.com.
4. Los campos Email Manager 1 a 15 de la tienda entran como CC. De ahi vienen duplicados y personas que el cliente no ve en la lista de la alerta, como btatum en 0619-27.
5. En Food Lion, Impersonation/Social Engineering sale por la alerta Defrauded Customer-Food Lion, que cubre los dos tipos. La alerta TGC - Impersonation/Social Engineering filtra STORE.DIVISION = GIANT/MARTINS, Rows Returned=0 en Food Lion por configuracion.
6. El asunto del correo toma el tipo de caso: una linea 13a con "Impersonation/Social Engineering - Food Lion #2569" era la alerta Defrauded.
7. SendGrid guarda 7 dias moviles. Pedir logs a Russ dentro de esa ventana.
8. Relacion con el metodo del 18 sep (Matt, RCS-28294): mismo flag InProcess, alli sin causa. Tambien Warning 16 BlobNotFound o PDF temporal no encontrado en auditorias, falla distinta.
