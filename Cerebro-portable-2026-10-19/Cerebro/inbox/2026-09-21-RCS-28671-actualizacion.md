RCS-28671. Verificado en Jira el 21 sep 2026.

Qué pasa: Accepted into Development, Shandana Khan. ENG-8659, vinculado directamente, está Backlog, sin asignado, sin versión y sin comentarios. No hay evidencia de ejecución del arreglo. Último comentario RCS: Mohammed, 8 sep. Último público: Juan, 7 sep. Silencio documental de 13 y 14 días respectivamente.

Causa: error T3.TENDERTYPEGROUP confirmado en búsquedas originales. Simon reparó 278 el 31 ago; Corey confirmó el 1 sep que seguían arregladas. Fase actual: 17 work items sin filas en fti.Transactions, ventana del cutover del 28 ago. El mecanismo preciso de provider/contexto de sesión no quedó probado. SQL sin esquema y filtros distintos no demuestran por sí solos una carrera de conexiones.

Evidencia: 3322645, reparación y seis búsquedas aún bloqueadas por otro bug. 3324086, cliente confirma búsquedas y reporta work items. 3333850, Mohammed propone borrar/regenerar; 3334895, pide ticket Blue Team. ENG-8659 acredita ese seguimiento.
Fuentes: https://trebuco.atlassian.net/browse/RCS-28671
https://trebuco.atlassian.net/browse/ENG-8659

Qué hago hoy: pedir a Shandana/Jon dueño y fecha de ejecución del ENG existente, preservar asignaciones/notas y validar los 17 IDs tras reparación. No abrir duplicado ni repetir WISC: pruebas previas deduplicaron sin recuperar eventos. Pedir a Simon estado de las seis búsquedas restantes como pendiente separado.

Precedentes: bitacora/RCS-28671.md, ENG-8334 confirma fuente ARDM completa y reparación de plataforma. Historia: python3 bin/buscar RCS-28671.

Compromisos: Juan prometió actualizar al confirmar vía de regeneración. Existe ticket, todavía sin ejecución ni ETA.

Texto interno propuesto:
Shandana, ENG-8659 is still unassigned in Backlog, with no target version or execution update. Please confirm the Blue Team owner and a remediation date for the 17 affected work items, including preservation of existing assignments and notes and validation of their transaction links afterward. The customer last received an update on September 7. Please also separate Simon's six remaining search failures from this recovery task.

Texto al cliente:
The recovery of the 17 affected work items is tracked with Engineering and is awaiting scheduling. We do not yet have a confirmed completion date. The original search repair and this work item recovery are separate steps. We will update this ticket when the recovery schedule is confirmed.
