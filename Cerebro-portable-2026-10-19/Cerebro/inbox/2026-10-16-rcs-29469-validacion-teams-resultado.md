# RCS-29469: resultado del cruce con sso.teams

Datos aportados por Juan tras ejecutar SELECT en el tenant. Resultado íntegro: adjuntos/RCS-29469/2026-10-16-validacion-teams-juan.tsv. No son consultas ejecutadas por el agente.

Los cinco usuarios tienen exactamente una fila devuelta en sso.teams: TeamName Location Manager, Persistent NULL, InsertedDateTime 15 octubre 10:34:36 y UtcDateFrom/UtcDateTo NULL. Coincide con el team del CSV. En el SELECT previo, cada uno tiene una fila de nivel 5 con esa misma fecha, y la cuenta tiene SecurityID NULL.

Interpretación: CSV, teams y filas de nivel son consistentes en la foto actual. No se demuestra que este archivo específico sea el consumido ni se descarta una incidencia histórica del loader. Los cinco últimos logins preceden a la inserción del 15. No hay un nuevo login posterior a esa carga en el resultado aportado; por tanto, estos cinco no reproducen por sí solos el caso limpio de Rachel.

Christi tiene además una asignación de nivel 5 Persistent 1 desde abril, anterior a su login de julio. Las dos filas tienen el mismo nivel. No atribuirles conflicto ni borrar una fila. El comportamiento esperado de una fila de salida de carga descrito por Matt no decide por sí solo la convivencia con overrides persistentes.

Siguiente comprobación: leer la definición actual de sso.GetUserSecurityLevel con SELECT OBJECT_DEFINITION para confirmar filtros y precedencia. Esto no reconstruye el código que corrió en julio. Después decidir prueba controlada de SSO con captura antes/después y logs, o ampliar el ENG con el caso histórico de Christi. No pedir al cliente que reenvíe archivos, no prometer que otro login resolverá ni corregir las cuentas antes de guardar evidencia.

Las notas públicas e internas ya publicadas no requieren un comentario nuevo por cada SELECT. Se prepara una actualización consolidada cuando termine esta validación.
