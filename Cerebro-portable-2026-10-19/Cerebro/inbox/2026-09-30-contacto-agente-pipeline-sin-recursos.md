# A quien escalar un agente de pipeline sin RAM o CPU

## Que pasa
Un equipo donde corre un pipeline ARDM de Azure DevOps se cuelga, con sospecha de falta de RAM o CPU.

## Respuesta
Confirmado. Contacto: Mike Tasch (Michael Tasch), Infra & Cloud Engineer, equipo de Peter Tuttle.
Es dueno de los agent pools de DataOps (prod_ardm1, prod_nonsas) y de las cajas DSPROD-LA01 a LA12.
Ruta formal desde un RCS: Under Infrastructure Review. El ticket queda a tu nombre y auto crea RETAILIT.

## Evidencia
1. RETAILIT-20895, 20721, 20713, 20425, 20777: todos asignados a Mike Tasch sobre agent pools y DSPROD.
2. Confluence RTS 478234214401, runbook de pipelines, patrones 3 y 8: lentitud por contencion de recursos y agente que abandona el job. Escalar a infra si se repite en la misma caja.
3. Confluence on-call: Infrastructure cubre CPU, memoria y disco. brain/memoria/reference_escalacion_l3_procedimiento.md.

## Que hago hoy
1. Del log del build, anota el nombre del agente (DSPROD-LAxx o VM Azure), build ID y hora de la ultima linea.
2. Revisa config_control por un STARTED huerfano antes de relanzar (patron 6).
3. Escribe a Mike por Teams. Si hay RCS, transiciona a Under Infrastructure Review.
4. Peyman Motlagh en copia si el pipeline es de Secure 5, el runbook lo nombra como destinatario del estado.

## Contexto que cambia el diagnostico
RETAILIT-20721 mueve prod_ardm1 de agentes SAS on prem a VMs Azure. RETAILIT-20713 decomisiona DSPROD-LA01 a LA12, en hold hasta 09-28. Menos agentes o VMs mas chicas pueden explicar la contencion.
Si la maquina es VisualCron o LPMS, el dueno tambien es Infra (RETAILIT-20742, Mike Tasch con Matt K).

## Borrador Teams
Hi Mike, quick question. The agent running <pipeline name> (build <ID>) seems to be hanging, and it looks like it may be running out of memory or CPU. Last log line was at <time> on <agent name>. Is this something your team can take a look at, or should I route it somewhere else? Could it be related to the prod_ardm1 agent pool changes, or am I reading this wrong?

## Compromisos
Ninguno abierto.
