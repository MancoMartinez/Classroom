RTS-207372. Verificado en Jira el 21 sep 2026.

Qué pasa: Closed, resolución Resolved, Rajith Suvarna. Último comentario: 10 sep, 12:21 EDT, confirma que la alerta despejó tras cancelar consultas.

Causa: evidencia operativa de consultas largas de work items de THD en secure_WH, otras consultas en cola y timeouts multicliente. El hilo citado cuestiona la cancelación automática tras una hora. No confirma que errores de columna o reintentos originaran esa carga.

Evidencia: comentario 3337373 del 10 sep reproduce el intercambio técnico sobre secure_WH, THD, cancelación manual y falta de compute para otros clientes. Comentarios 3337404 y 3337411 confirman alerta despejada. RTS no muestra enlaces; búsqueda adicional encuentra ENG-8650, vinculado a RCS-28799.
Fuente: https://trebuco.atlassian.net/browse/RTS-207372

Qué hago hoy: confirmar con Gabor Remenyi despliegue y validación de ENG-8650. Está Development Complete; versión Secure September 2026 Release 2/2, fecha 24 sep, released=false. Relacionar QueryIds con SNR1/SNR3 de RTS-206667. Comprobar warehouse y ventanas de carga antes de vincularlo a RCS-28968. El cierre de la alerta acredita mitigación, no corrección permanente.

Precedentes: RTS-206667, comentario de Vlad del 18 sep. Historia: python3 bin/buscar RTS-207372. Teams aparece citado dentro del comentario; no se leyó el hilo original completo.

Compromisos: el intercambio plantea investigar tras cancelar y abrir un bug prioritario. ENG-8650 existe. Gabor dijo el 18 sep que probablemente QA no puede probarlo directamente y sugirió tests automáticos. No consta resultado de esos tests ni despliegue. Fecha de versión no equivale a compromiso de entrega.

Texto interno propuesto:
The September 10 incident cleared after the long running THD work item queries were cancelled. ENG-8650 is Development Complete and targets the unreleased September 24 version. Gabor, please confirm deployment timing and the automated test results or production validation planned for the one hour timeout. Vlad reported SNR1 and SNR3 blocking other work items on September 18 in RTS-206667. Please correlate the QueryIds before treating these as the same defect. We have no evidence yet connecting this incident to the detail or derived amount discrepancies in RCS-28968.
