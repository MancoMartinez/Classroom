# RCS-28671. Plan de Mohammed para regenerar MD03, 29 sep

Propuesta de Mohammed Mutahhar por Teams: el job ancla el periodo de la busqueda principal y no actualiza las condiciones de la busqueda de referencia. Cambiar temporalmente la condicion de fecha de la busqueda de referencia al 27 ago, relanzar md03-cit-d para 8/27 en WISC, revertir la busqueda.

## Antes de tocar nada
1. Ubica la busqueda de referencia. En el SQL aparece como RefSearch2, SubSearchParam_1. Desde Consecutive Markdowns, ubica la condicion que referencia otra busqueda.
2. Captura la condicion original tal como esta. Es la unica forma de revertir exacto.
3. Mira si otras definiciones usan esa misma busqueda de referencia. md03-aps-d es candidata. Mientras dure el cambio, todas corren con la fecha fija.
4. Hazlo lejos de la corrida diaria de md03. WISC la muestra encolada entre 18:11 y 22:40 UTC. En hora Bogota, antes de las 13:00.
5. Pregunta a Mohammed si guardar la busqueda sube SearchVersion y si eso dispara reintentos automaticos de periodos recientes.

## Ejecucion
1. Cambia la condicion de la busqueda de referencia a Between 08/27/2026 y 08/27/2026. Save.
2. WISC, New Run, md03-cit-d, periodo 2026-08-27.
3. Espera 2 results y 2 gen. Anota el RunId.
4. Revierte la condicion exacta de la captura. Save.
5. Show Query en el siguiente run diario de md03. La ventana del CTE debe volver a ser relativa a la fecha del run.

## Validacion
Nuevos WI de 7135 DXM6269 y 7161 GXH3486 con periodo 27 ago. Events abre las transacciones 8989, 8990 y 8991. Value Potential distinto de 0.00.

## Pendiente
Aplicar lo mismo a las otras definiciones de los 17 sin reemplazo que usen ventana movil. Cada una con su busqueda de referencia.

## Teams a Mohammed
Thanks Mohammed Mutahhar, that makes sense. Before I change it, two quick checks. Does saving the reference search bump its version and trigger any automatic reruns of recent periods? And do you know if md03-aps-d or any other definition uses the same reference search? I'll do it outside the daily md03 window, capture the original condition first, and revert right after the rerun.

## Nota interna
Agreed approach with Mohammed Mutahhar on Teams, 2026-09-29. The work item job anchors the period on the main search but not on the reference search conditions. Plan: temporarily set the reference search date condition in Consecutive Markdowns to 2026-08-27, rerun md03-cit-d for period 2026-08-27 in WISC, then revert the condition. Original condition captured before the change. Result and new work item IDs to follow in this ticket.

---
Respuestas de Mohammed, 29 sep.
1. Guardar sube la version de la busqueda.
2. No dispara reruns automaticos. El rerun se lanza a mano.
3. Las definiciones que dependen de la busqueda se ven con el boton Dependencies de la barra, y tambien al hacer Save.
Riesgo que queda: la corrida diaria de cualquier definicion dependiente mientras dure el cambio. Mitigacion: fuera de 18:00 a 23:00 UTC y revertir de inmediato.

---
EJECUTADO 29 sep. Subbusqueda Consecutive Markdowns subsearch cambiada a Between 08/27/2026 y 08/27/2026, run 32afd25e-39f2-4de2-aede-3fd2edb1cf14 (Rerun desde 92b446fe), Success, 2 results, 2 gen. Subbusqueda revertida a Within the last 1 Days.
Reemplazos:
253175 MD03-APS-D store 7135 DXM6269, 3 eventos, PotentialValue 148.08, sin asignar, FtiID 96CF4B17-2C2D-4461-9EC8-DC73AE9A853C. Reemplaza 248159.
253176 MD03-APS-D store 7161 GXH3486, 3 eventos, PotentialValue 129.87, sin asignar, FtiID 5FCDBF86-AE1C-4157-AB60-F2CDC07833EC. Reemplaza 248160.
Nota: New Run no genero nada visible; Rerun sobre el run existente del periodo si.
