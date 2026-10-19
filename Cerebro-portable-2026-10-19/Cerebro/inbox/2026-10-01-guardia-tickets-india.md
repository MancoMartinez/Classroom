# Guardia Colombia sobre tickets de India, 1 oct 2026

Fuente: Jira en vivo, leído 1 oct 9:16 Bogotá. Viraj los pidió en Nuaav Leadership Support el 30 sep. Horas en Bogotá.

## Orden por urgencia

1. RCS-29135 Ross Stores, Aspect Step03 deadlock. Megha Rathi. HOY.
Ross reprocesaba el batch 3685 hoy a las 7:00 Bogotá (5 AM PT). Megha se ofreció como POC y está fuera. Sin comentario de Arvie Antenor desde entonces. Causa confirmada en logs: Custom_Purge.cmd (5:00 a 6:40) se cruzó con Step03 (5:14 a 5:25), deadlock 1205. Segunda vez en 5 semanas, precedente RCS-28538. Megha escaló a Kathryn Scheldberg dos preguntas de Madel Prades sobre reprogramar el Historical Purge, sin respuesta.
Acción: alguien de Colombia toma el POC, vigila respuesta de Arvie y valida conteos. No cerrar hasta confirmación del cliente.

2. RCS-28770 Tailored Brands, montos duplicados en Markdown, Clearance y Employee Discount. Megha Rathi. HOY.
Ya se perdió la llamada del 28 sep porque la invitación nunca salió. Rae Hatfield lo pidió el 29. Colton Neal propuso el 30: viernes 2 oct 10:00 CST (preferido, igual a 10:00 Bogotá) o miércoles 7 oct 10:00 CST. Nadie respondió.
Acción: confirmar el viernes y enviar la invitación hoy, con Rae como opcional. Segunda invitación fallida sería grave. Nota interna de Megha del 29 sep tiene los dos hallazgos en hipótesis, sin confirmar en código.

3. RCS-28756 Nike ECOM sin data desde 28 ago. Bikash Kumar. Te nombran a ti.
Bryant McAnnally escaló el 29 sep pidiendo timeline, cerca de un mes sin causa. Bikash revisó el archive el 30 sep: no hay archivos ECOM entre 28 ago y 17 sep en c67_rawdata_order, hay que pedir reenvío a Nike. Rajith Suvarna pidió que se coordine contigo por el hilo de correo con Nike (RTS-206999).
Contradicción a resolver: Rajith dice que el backlog sí llegó tras el arreglo; Bikash dice que el archive está vacío en ese rango. Acción: cruzar ambas versiones y redactar la solicitud de reenvío a Nike.

4. RCS-28566 TGJ Secure 5, transacción anulada muestra venta. Nikita Rathore.
Esperando al equipo Snowtime desde 16 sep. Kelly Murray preguntó el 29 sep porque el cliente lo sacó en la llamada semanal. Última respuesta al cliente, 24 sep, genérica. Acción: si el cliente o Kelly escriben, contestar con estado; no hay acción técnica de soporte pendiente.

5. RCS-28935 Bass Pro, todas las transacciones XML desde oct 2024. Nikita Rathore.
Último mensaje al cliente 22 sep, genérico. Motivo dado por Paul Marderosian: integración con tercero para devoluciones en POS. Peyman advirtió que los raw están cifrados. Pendiente decisión interna de qué entregar. Riesgo: 9 días sin update al cliente.

6. RCS-28543 Kinney Drugs (KNY/179) alerta Grafana. Nikita Rathore. Interno.
Alerta sigue disparando: RTS de acción enlazados a diario del 24 al 30 sep. Fix en PR 57431 de arpfiles (Simon Smith), Nikita pidió ajuste en c138 el 11 sep. Sin comentarios desde entonces. Acción: verificar si el PR se mergeó; solo vigilar.

## Compromisos abiertos que quedan sin dueño mientras India está fuera
POC de Ross hoy. Invitación a Tailored Brands hoy. Respuesta de Aspect Eng a Madel.

## Corte 15:20 Bogotá

RCS-28756 Nike. Damir Demirovic (Nike) pidió a las 10:20 aclarar si Appriss tiene o no los archivos. Sin respuesta. Borrador:

Hi Damir, thank you for flagging that, the wording was unclear. Appriss does not have the ECOM order files for August 28 through September 17. Our archive shows no files received from Nike for those dates, so there is nothing on our side to reload. Could your team resend the ECOM order files for that window? Once they arrive, our system will process them automatically. Days since September 19 are processing normally.

RCS-29135 Ross. Kathryn Scheldberg respondió a las 11:19: Custom_Purge.cmd es independiente, detenerlo a mitad no daña nada, se sugiere una vez por semana fuera de horario y sin cruzarse con custom_loadlp.cmd. Arvie no ha confirmado el reproceso. Borrador para Madel y Arvie:

Hello Madel and Arvie, Aspect engineering confirmed the following about the Historical Purge job. Custom_Purge.cmd is a standalone scheduled job that deletes reporting data older than the configured number of days. Stopping it mid run does not cause harm, the next run starts fresh. Recommended setup is once a week during off business hours, scheduled so it does not overlap with Custom_LoadLP.cmd. Running it during business hours can cause slowness and locked records for users. Your team can move the scheduled task, run it more often so each run is shorter, or stop it before the load starts. Disabling it entirely keeps historical data and lets the database grow. Arvie, could you confirm whether the reprocessing of batch 3685 completed and the record counts look correct?

RCS-28770 Tailored Brands. Sigue sin respuesta a Colton. La llamada preferida es mañana 2 oct 10:00 Bogotá.

RCS-28543 Kinney. Ayesha Mehar a las 9:26: Stock Count Adjustments sigue fallando a diario, incluido hoy.

RCS-28566 y RCS-28935. Sin movimiento desde el 29 sep.
