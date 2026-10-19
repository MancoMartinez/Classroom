RTS-206667. Verificado en Jira el 21 sep 2026.

Qué pasa: Under L2 Support Review, Vlad Bogus. El título dice Active Alerts: 0; no acredita reparación. El 18 sep Vlad confirmó SNR3 y SNR1 lentos, bloqueando los demás work items, e inició revisión de rendimiento.

Causa: rename TenderTypeGroup a StdTenderTypeGrp confirmado para SNR4 el 28 ago. SNR4 tuvo un run exitoso el 2 sep, documentado en RCS-28799, comentario 3325670. Causa del rendimiento actual pendiente. El error original es NonRetryableException; no prueba reintentos continuos.

Evidencia: comentario 3315650, 28 ago, confirma columna inexistente y carga completa de 5.185.741 transacciones. Comentario 3338878, 11 sep, documenta cancelación de SNR3 y SNR4 pendiente. Comentario 3351092, 18 sep, identifica SNR1/SNR3 como bloqueadores.
Fuente: https://trebuco.atlassian.net/browse/RTS-206667

Qué hago hoy: pedir a Vlad QueryIds, duración, periodos, warehouse y resultado de optimización de SNR1/SNR3. Contrastar la ejecución exitosa de SNR4 del 2 sep con su estado actual. Cruzar las consultas con RTS-207372 antes de declarar causa común.

Precedentes: confluence/RTS-triage/RTS-206667-home-depot-snr4-tendertypegroup.md. Consultar historia con python3 bin/buscar RTS-206667.

Compromisos: Vlad investiga mejora de rendimiento. No consta ETA ni validación final en los comentarios recuperados.

Texto interno propuesto:
Vlad, your September 18 update identifies SNR1 and SNR3 as blocking the remaining work items. Please share the affected QueryIds, warehouse, execution periods and optimization outcome, and confirm whether they match the workload cancelled under RTS-207372. RCS-28799 records a successful SNR4 run on September 2; please confirm its current stability. This will separate the confirmed metadata defect from the current performance issue. What is the next validation checkpoint?
