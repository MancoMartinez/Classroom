# RCS-28671. Que puede hacer soporte en Control Panel y que no

## Lo que dijo Shandana, contra la evidencia
Cierto para la informacion. WISC, en Control Panel USPROD, lista cada Run con Total results, Generated, Duplicate, Failure y State. Ahi se ve si Mohammed corrio las 17 definiciones y que devolvio cada una. Juan tiene rol SupportL2 y Engineers, brain/memoria/project_juan_accesos.md.
Probable tambien para la regeneracion. Soporte ya relanza WI desde WISC: RCS-28170 TJX, Diego Buelvas, "re-run via the WISC Control Panel"; RCS-28352 Floor & Decor, "Manual Rerun" contra control/api/wisc/run. Precedentes de otros clientes, no un SOP escrito.
Lo unico que soporte no podia hacer era borrar WI. Eso ya lo hizo Mohammed. Lo que falta es un rerun por definicion y periodo.

## Por que la SQL no bastaba
WorkItemGenerationEvent solo registra WI creados. Un run que devolvio 0 filas o solo duplicados no deja rastro ahi. R6 no prueba que los otros 15 no corrieron.

## Proceso
1. Control Panel USPROD, WISC, cliente 85. Filtra la definicion. Para 248159 es canada work items/md03-cit-d.
2. Busca Runs con Period 2026-08-27 encolados desde el 25 sep. Anota RunId, Total results, Generated, Duplicate, Failure, State.
3. Lee el resultado:
   Sin Run: la definicion nunca se relanzo. Siguiente paso, New Run con periodo 2026-08-27.
   Total 0: la busqueda ya no devuelve ese grupo. Revisar con Mohammed.
   Duplicate mayor que 0 y Generated 0: la deduplicacion lo bloqueo. Revisar con Mohammed.
   Failure mayor que 0: Logs de Control Panel con el RunId.
4. Antes del New Run, espera la respuesta de Mohammed. El pudo haber corrido algo que WISC mostrara distinto.
5. Tras el New Run, repite R1 de -sql-regenerados.md y abre el WI nuevo como cliente.
6. Repite con las otras 14 definiciones de inbox/RCS-28671-affected-work-items.csv.

## Riesgo del New Run
Los originales ya estan borrados, asi que no hay WI previo que choque. El borrado quito la asignacion a DAPM Sean y las notas. El nuevo sale con la asignacion por defecto de la definicion.

## Pendiente de verificar
Nombres exactos de columnas y el flujo del boton New Run salen de la bitacora del 7 sep, no de un documento. Confirmalos en pantalla.

---
Lectura de WISC, 28 sep 14:29, capturas de Juan.
md03-cit-d periodo 2026/08/27, Run 92b446fe-85d1-4463-ac8f-03ee9acd1164. Queued 9/24 18:53:30 UTC, Ended 20:59:05. Success, 0 results, 0 gen. MD03 si se relanzo y la busqueda disparadora no devolvio ningun grupo.
com1 periodo 8/27, Run 8c9da172: 2 results, 1 gen, 1 dupe. Queued 9/25 21:41 UTC.
denver mkd2 periodo 8/27, Run f163cc7d: 1 result, 1 gen. Queued 9/25 21:20 UTC.
Failed en la ventana: snr4, sls1, ref3. Otra familia, rendimiento, no es de este ticket.
La vista recorta por cantidad de runs. Con To 28 sep el filtro md03 perdio el run del 9/24. Usa rangos cortos.
Conclusion: un New Run de md03-cit-d para 8/27 probablemente devuelve 0 otra vez. El bloqueo no es de permisos sino de que la busqueda no encuentra el grupo de 7135 y 7161 hoy.
Siguiente: Logs del run 92b446fe. Abrir el .fti y correr su busqueda en el Portal para 8/27, store 7135, cajero DXM6269.

Teams de seguimiento a Mohammed:
Hi Mohammed Mutahhar, one more data point on RCS-28671. In WISC, md03-cit-d for period 8/27 ran on 9/24 as run 92b446fe-85d1-4463-ac8f-03ee9acd1164 and returned 0 results, so nothing was generated for 248159 and 248160. The original run on 8/28 found both groups. Would you expect the trigger search to come back empty for 8/27 now, or am I looking at the wrong run?

---
Show Query del run 92b446fe, 28 sep. Causa del 0 encontrada en el SQL.
La busqueda externa filtra TradingDay entre calendarStartDate y calendarEndDate, ambos 2026-08-27.
La subbusqueda T4AsCte, que decide que transacciones califican, filtra T5.TradingDay BETWEEN 2026-09-23 AND 2026-09-24. Esa ventana movil se ancla a la fecha de ejecucion del run, no al periodo.
El join T4 exige que la transaccion del 27 ago este en el CTE. Nunca esta. Resultado 0 siempre que se relance un periodo viejo de md03-cit-d.
Estado: CONFIRMADO por lectura del SQL. Falta la prueba en Snowflake con la ventana del CTE cambiada a 2026-08-27.
Hipotesis: las otras definiciones de los 15 sin reemplazo tambien usan ventana movil. COM1 y MKD2 regeneraron, quiza porque no la usan.
Implicacion: un New Run de soporte en WISC para 8/27 va a dar 0 otra vez. La regeneracion de estos WI necesita anclar la ventana al periodo, y eso no se hace desde WISC.

---
CONFIRMADO 28 sep. Query del run con la ventana del CTE en 2026-08-27, ARDM_PRODUCTION.C085_THD: 2 filas. 7135 DXM6269 cuenta 1262034041293206, 3 transacciones. 7161 GXH3486 cuenta 1222026206381307, 3 transacciones. Los datos estan. El 0 del rerun lo causa la ventana movil anclada a la fecha de ejecucion.
Nota: el esquema correcto es C085_THD, no C085_THD_SNOWTIME. ARDMPROD.ARDM_085 no tiene StdTenderTypeGrp.
Textos: -comentario-interno-ventana.md, -teams-mohammed-ventana.md.
