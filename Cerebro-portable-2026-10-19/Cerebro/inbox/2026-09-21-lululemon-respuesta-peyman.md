Lululemon | 2026-09-21 | Confirmación de Peyman Motlagh

Fuente: respuesta de Teams copiada por Juan, hora no proporcionada.

Peyman confirma que las licencias SAS vencieron el 21 de agosto y provocaron fallos en los procesos que usaban SAS. Todos los scripts SAS han sido retirados del código actual. La licencia deja de ser solo una hipótesis para esos fallos.

Identifica además el traslado de clientes desde LA4 hacia Azure por Infrastructure. Considera que ambos problemas contribuyeron a la demora y afirma que ya fueron atendidos y no deberían repetirse hasta mover este cliente a Snow Time. Esto expresa su expectativa para esos problemas en el entorno actual; no confirma una fecha para Snow Time ni demuestra que esa migración vaya a causar fallos.

Contraste: Ryan DeVries ya confirmó que su corrección SQL aplica a cada ejecución posterior. Su explicación también menciona el traslado a Azure. No sumar ambas explicaciones como incidentes independientes sin correlación adicional.

Alcance pendiente: Peyman no menciona explícitamente el timeout de get_exchange_rates a openexchangerates.org de RTS-206998 ni la caída de segmentos GP3 de RTS-207848. No asumir que están cubiertos por su afirmación. SAS queda aclarado; no repetir preguntas sobre licencia o necesidad del paso. Consulta mínima: si RTS-206998 fue efecto del traslado o requiere una acción separada. Mantener GP3 con Christopher Beck/Brandon Kays.
https://trebuco.atlassian.net/browse/RTS-206998
https://trebuco.atlassian.net/browse/RTS-207848

Respuesta propuesta, no enviada:
Thanks, Peyman, that clarifies it. I’ll reflect that the SAS scripts have been removed and the move to Azure has been addressed. One remaining point: was the exchange-rate connection timeout in RTS-206998 also related to the move, or does it need a separate follow-up? I’m checking the GP3 incident with Chris and Brandon separately.
https://trebuco.atlassian.net/browse/RTS-206998

Sin nuevo ETA ni compromiso global de ausencia de fallas. Juan ingiere con cerrar.
