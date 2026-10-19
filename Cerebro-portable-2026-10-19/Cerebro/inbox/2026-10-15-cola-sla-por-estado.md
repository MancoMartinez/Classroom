# Cola y SLA por estado, 15 octubre 2026

Origen: el resumen de la mañana marcó RCS-28671 y RCS-28881 como SLA en riesgo y RCS-28240 como respuesta pendiente. Juan corrigió: Under Customer Review pausa el SLA; 5 a 7 días sin respuesta del cliente es seguimiento; la prioridad es el cliente con el último mensaje y el reloj activo, o la deuda de update tras el ownership con el SLA cerca o vencido.

Cambios
1. bin/cola.py: reloj pausado o activo por estado; cadencia en horas hábiles sin comentario público de Appriss (Critical 30 min, High 24 h, Medium 4 a 5 días, Low 7 a 10 por defecto); fecha comprometida reemplaza el techo; lectura de los ciclos SLA de Jira; nivel 2 UPDATE VENCIDO; aviso cuando la pelota está en el cliente con el estado activo; fuera la alerta de días corridos desde la toma. Léxico: "still trying to get help internally" cede la pelota. Respaldo en .cerebro/cola.py.antes-20261015.
2. bin/test_cola.py: test_sla_por_estado. Pasa.
3. AGENTS.md: sección Cola y SLA.
4. Tarea programada Resumen de la mañana: prompt reescrito con las mismas reglas y los customfield SLA.
5. Skill cerebro-cola: propuesta con ruta ~/Cerebro, reglas de SLA y Siguiente paso.

Resultado sobre Jira en vivo del 15 oct, 11:00
RCS-28240 nivel 3, pausado: Emma sigue gestionando internamente.
RCS-28671 nivel 3, pausado: Viraj hizo seguimiento el 12 oct.
RCS-28881 nivel 2 UPDATE VENCIDO: sesión del 13 oct sin resultado público, último update 9 oct.
RCS-29205 nivel 2, High, 24 h hábiles sin update tras el comentario del 14 oct.
RCS-28256 nivel 3 con reloj activo en Work in progress.

Medido: los Medium solo traen ciclos SLA de primera respuesta ya cerrados; la cadencia es la que decide. eval_cola.py tiene las 17 etiquetas vencidas desde el 1 oct; los niveles no cambiaron frente a la versión anterior en los cuatro casos etiquetados. Refrescar con bin/refrescar_eval.py.
