# Cerebro v2: implementación del roadmap, 14 octubre 2026

## Punto de partida corregido

El análisis previo describía la copia vieja .cerebro/buscar-antes-20260928.py. El bin/buscar vigente ya delegaba en cerebro_motor.py: BM25 de FTS5, embeddings multilingual-e5-small y fusión RRF k=60 sobre .cerebro/retrieval.sqlite. El paso de recuperación híbrida ya existía. Esta entrega construye encima.

## Qué quedó hecho

| Pieza | Archivo | Estado |
|---|---|---|
| Escáner y redacción de secretos | bin/secretos.py, cerebro.sh compuerta | Activo. Índice y leer_fuente redactados; cerrar e ingerir-aplicar se detienen ante severidad alta |
| Afirmaciones por oración con vigencia | bin/afirmaciones.py, tablas claims, claims_done y superseded | Activo. Se rellena solo en la primera búsqueda, unos 10 s |
| Versiones reemplazadas | afirmaciones.versiones | Activo. 12 documentos, penalización 0.5 |
| Filtro de hechos | search(hechos=True), MCP solo_hechos | Activo |
| Reranker cross-encoder | cerebro_motor.reranker, .cerebro/config.json | Activado. Requiere una descarga en el Mac |
| Evaluación con MRR, nDCG, recall, IC 95 % y partición test | bin/eval_cerebro.py, cola/EVAL-precedentes.json | Activo |
| Golden set de precedentes | bin/golden_precedentes.py, cola/titulos-jira.json | 57 consultas, 152 pares |
| Matriz de vectores en memoria y caché de consultas | cerebro_motor.dense_matrix | Activo |
| Verificador de grounding | bin/grounding.py, MCP verificar_borrador | Activo, calibrado |
| Bucle de ediciones | bin/ediciones.py | Listo, sin pares todavía |
| Fine-tuning de embeddings | bin/entrenar_embeddings.py | Bloqueado por datos: 32 de 300 consultas |
| Pruebas | bin/test_capa_epistemica.py, test_cerebro_motor.py, test_cerebro_mcp.py | Las tres pasan en la VM |

## Cifras

158 consultas, corpus de 3976 fuentes y 18398 fragmentos.

| Modo | hit@1 | hit@5 | MRR@10 | nDCG@10 | p50 VM |
|---|---|---|---|---|---|
| BM25 | 0.165 | 0.317 | 0.223 | 0.109 | 0.004 s |
| Híbrido | 0.171 | 0.342 | 0.257 | 0.135 | 0.069 s |
| Híbrido más reranker | 0.228 | 0.437 | 0.320 | 0.175 | 2.4 s |

Mejora del reranker sobre el híbrido, IC 95 % bootstrap pareado: hit@5 de 0.025 a 0.158, MRR de 0.018 a 0.108, nDCG de 0.018 a 0.062. Anclas: 0.446 a 0.495 en hit@5. Precedentes: 0.158 a 0.333. Partición test sola, 56 consultas: 0.286 a 0.357, con un intervalo que incluye el cero. Detalle en .cerebro/evaluacion-20261014-reranker-todo.json y -test.json.

Grounding, 283 oraciones de 10 borradores verificadas con y sin la evidencia de su ticket: AUC coseno 0.535, cross-encoder 0.629, cobertura de entidades 0.68. Umbrales en .cerebro/grounding-calibracion.json. Usa el verificador como triage. Sus alertas deterministas pesan más que el puntaje de soporte.

Afirmaciones extraídas: 1957 confirmadas, 1293 hipótesis, 259 descartadas, 730 correcciones, 386 compromisos, 5351 estados de Jira.

## Hallazgos de seguridad

Severidad alta en el corpus: 8 JWT dentro de inbox/2026-10-07-talos-evidencia/RCS-28256.json, inbox/2026-10-07-talos-evidencia/RCS-28881.json e investigaciones/evidencia-excel-urban-2026-09-17/RCS-12040.json. El motor no indexa .json. db:knowledge_chunks/555 guarda una credencial por asignación dentro de sessions.db; el índice la redacta y la base sigue con el valor. inbox/*.md está limpio.

## Lo que haces tú en la terminal del Mac

1. Reinicia Claude Desktop y Codex para que el servidor MCP cargue el código nuevo.
2. Descarga el reranker una vez: bin/cerebro index --reranker
3. Corre las pruebas: .venv-cerebro/bin/python bin/test_capa_epistemica.py, luego bin/test_cerebro_motor.py y bin/test_cerebro_mcp.py con el mismo intérprete.
4. Mide la latencia real: time bin/buscar "smart alerts no se disparan". Si pasa de 1.5 s y te estorba, pon "enabled": false en .cerebro/config.json.
5. Revisa db:knowledge_chunks/555 y los tres .json con JWT. Rota la credencial si sigue viva.

## Siguiente nivel

1. Evalúa bge-reranker-v2-m3 en el Mac: cambia "model" en .cerebro/config.json y corre evaluar-busqueda después de source cerebro.sh. Quédate con el que gane en la partición test.
2. Amplía cola/titulos-jira.json con títulos de tickets cerrados para llegar a 300 consultas y desbloquear el fine-tuning.
3. Registra cada texto que pegues con bin/ediciones.py, o pásale a Claude el JSON de comentarios de Jira para emparejar. Con 20 pares por skill, ediciones.py ejemplos produce los few-shot.
4. Tareas programadas para la cola y el SLA, pendientes de tu horario.

## Respaldos

.cerebro/*.antes-20261014: cerebro_motor.py, cerebro_mcp.py, eval_cerebro.py, test_cerebro_mcp.py, requirements-cerebro.txt, cerebro.sh, ESTADO.md y AGENTS.md. Para revertir, copia cada uno a su ruta original y borra .cerebro/config.json. brain/sessions.db no se tocó.
