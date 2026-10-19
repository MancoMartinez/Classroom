# RCS-29026 Incident Logs del Control Panel, 9/25

Archivo de Juan, 530 líneas, 9/25 00:08 a 19:06, solo ERROR. Ningún error de SmartAlert ni SendGrid.
Pista: AdditionalProcessing.btnSave_Click, ThreadAbortException en Response.Redirect, AdditionalProcessing.aspx.vb línea 1071. Tres entradas: 16:40:58, 17:49:55, 17:59:24.
Horas del log en UTC, deducido. La pantalla de Juan muestra UTC+1: 9:20 PM suyo = 4:20 PM de Leigh. Su caso 9998-13 dice 6:52 PM = 17:52 UTC = 12:52 PM Bogotá, hora de su captura.
17:49:55 y 17:59:24 coinciden con las dos pruebas de Juan, con y sin filtro. HIPOTESIS: si la Smart Alert se dispara en btnSave_Click después de la línea 1071, el Redirect corta el hilo y la alerta nunca corre.
Pendiente: Incident Logs del 9/24 hacia 20:20 UTC, para ver si el error empieza ahí. Kiran revisa el código.
