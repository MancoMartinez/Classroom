RCS-28968. Verificado en Jira el 21 sep 2026.

Qué pasa: Work in progress, Bikash Kumar. THD escaló hoy por recurrencia en hora 20 del 19 y 20 sep. A las 09:28 EDT Matthew precisó que recibos y otros datos aparecen correctos; Total Item Sale Amount no coincide con Subtotal y ya no sirve para detectar faltantes.

Causa: pendiente. Separar detalle ausente, imágenes y agregado derivado desactualizado. La saturación por búsquedas es hipótesis sin prueba de warehouse compartido ni correlación de consultas y jobs.

Evidencia: 3350872, 18 sep, Bikash confirma recuperación y 77.92 para Secure ID 2609167613983099252. 3358182, 21 sep, Matthew aclara síntoma actual y pregunta por recarga de fin de semana. 3358462, 21 sep 11:24 EDT, Bikash informa investigación de Engineering.
Fuente: https://trebuco.atlassian.net/browse/RCS-28968

Qué hago hoy: revisar las transacciones de las capturas actuales; conciliar Subtotal, suma de items persistidos, Total Item Sale Amount y recibo por ID. Obtener jobs de recarga, transformación y recálculo con tiempos/warehouse; confirmar ejecución e invalidación de caché solo si aplica. Pedir dueño técnico, ticket y siguiente checkpoint. No repetir el acuse enviado hoy.

Precedentes: RCS-28649: orphan-delete corregido y recibos reconstruidos; SOP pendiente el 10 sep; RCS-28671, work items sin eventos. Consultar python3 bin/buscar para su historia.

Compromisos: Bikash prometió investigar recurrencia y avisar al progresar. No consta ETA ni nueva validación tras la aclaración del cliente.

Texto interno propuesto:
Bikash, Matthew's September 21 clarification changes the validation target: receipts and other data look correct, while Total Item Sale Amount remains inconsistent with Subtotal. Please reconcile the current sample IDs against the persisted item sum and both subtotal fields, and confirm whether weekend reloads reran the derived field calculation. Please share the engineering owner, tracking issue and next checkpoint. Validate the September 19 and 20 hour 20 samples before requesting closure. The September 18 sample passed, but that does not establish recovery of the current cases.
