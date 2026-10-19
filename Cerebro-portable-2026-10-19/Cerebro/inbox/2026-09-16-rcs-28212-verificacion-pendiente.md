# RCS-28212: corrección de Corporate y validación del cliente

Qué pasa: Juan decide comunicar que la configuración de Corporate quedó corregida de nuestra parte y solicitar revisión del cliente.

Causa confirmada: incident.event_type usa COR y case.event_type tenía CORP. Se agregó COR con label Corporate. Fuente: autorización de Matt en bitacora/RCS-28212.md y capturas de Juan del 16 sep.

Evidencia: el caso CA-44541-COR-2026-0001 ya muestra Corporate sin * COR. La copia 5511 devuelve casos COR; el caso objetivo aparece al retirar el filtro de subtipo. Esto confirma la corrección del tipo, pero no demuestra que el reporte 5165 con sus filtros originales incluya el caso. El mensaje se limita a la configuración corregida y pide validación.

Qué hago hoy: entregar respuesta breve en inglés. Juan la publica; el agente no escribe en Jira.

Precedentes: bitacora/RCS-28212.md. Compromisos: sin fecha adicional ni afirmación de validación final de 5165; pendiente revisión del cliente.

Texto para el cliente:
Hi Vinh, we’ve corrected the Corporate case type configuration on our side. Could you please check the affected cases and report and let us know if you’re seeing the expected results? Thank you.
