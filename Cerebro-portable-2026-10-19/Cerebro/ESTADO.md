# Cerebro. Estado verificado, 14 octubre 2026, noche

Entrega y cifras en inbox/2026-10-14-cerebro-v2-1.md. Abajo sigue el estado de la tarde.

## Qué cambió

buscar_conocimiento acepta variantes. Claude pasa la consulta en el otro idioma y con el término técnico; cada variante aporta sus canales BM25 y E5 y RRF los fusiona. El reranker vota como un canal más contra ese orden, en vez de reemplazarlo.

Los adjuntos entran al índice. xlsx, csv, docx, har y texto se extraen solos en cada búsqueda. PDF necesita pypdf en .venv-cerebro. Las imágenes pasan por OCR con Vision de macOS cuando Juan corre python3 bin/adjuntos.py extraer.

consultar_relaciones es la sexta herramienta MCP. El grafo une ticket, cliente, sistema, familia de causa y persona, cada arista con confianza documentada, inferida o mención y su evidencia.

bin/ediciones.py registra 19 pares reales. 12 de los 13 textos pegados en Jira coinciden en 98 % o más con su borrador final de inbox: la corrección de Juan ocurre entre versiones del borrador, y ahí se mide.

.claude/settings.json niega a Claude Code ejecutar guardar, ingerir_inbox.py y cerrar, y las herramientas de escritura de Jira.

## Qué se midió

158 consultas. Hit@5 de 0.342 a 0.589 con variantes; intervalo de 95 % de la mejora entre 0.171 y 0.323. Partición test: 0.286 a 0.536. Precedentes: 0.158 a 0.316. Anclas: 0.446 a 0.743, cifra optimista porque las reformulaciones se escribieron conociendo el vocabulario del dominio. Reranker sobre variantes: hit@5 0.601 y MRR 0.449 contra 0.589 y 0.427, con intervalo que incluye el cero.

Fine-tuning de E5 con 197 consultas y 495 pares, lote 4 por memoria de la VM: hit@5 con variantes cae de 0.589 a 0.475. Rechazado. El modelo base sigue.

Familia inferida contra la documentada: precisión 0.73 con cobertura 0.42 al umbral elegido. Optimista, porque las descripciones de familia se escribieron mirando esos casos.

## Qué falta

Probar bge-reranker-v2-m3 en el Mac con eval_cerebro.py --reranker. Instalar pypdf y correr la extracción con OCR una vez. Dos skills ordenaban ejecutar bin/guardar; las propuestas de corrección están en la entrega.

# Estado verificado, 14 octubre 2026, tarde

Entrega completa y cifras en inbox/2026-10-14-cerebro-v2-implementacion.md. El estado del 28 de septiembre sigue abajo como historia.

## Qué cambió

El motor indexa cada fuente redactada por bin/secretos.py. Ningún token, PAT, JWT, contraseña ni cadena de conexión con formato conocido llega al índice ni sale por MCP. La fuente original queda intacta. cerrar e ingerir-aplicar corren la compuerta sobre inbox/*.md y se detienen ante un hallazgo de severidad alta.

La capa epistémica vive en .cerebro/retrieval.sqlite. Extrae afirmaciones por oración con tipo confirmada, hipótesis, descartada, corrección, compromiso o estado. Guarda fecha observada, fecha de registro y vigencia. Un estado de Jira vence a los tres días de la fecha del documento. Doce documentos con marca explícita de versión quedan reemplazados por su versión nueva y pierden la mitad de su puntaje.

Un cross-encoder multilingüe, cross-encoder/mmarco-mMiniLMv2-L12-H384-v1, reordena los 30 primeros candidatos del híbrido. Queda activado en .cerebro/config.json. Hasta que Juan lo descargue con bin/cerebro index --reranker, la búsqueda cae al orden híbrido y lo avisa.

MCP suma verificar_borrador y el parámetro solo_hechos. contexto_ticket devuelve las afirmaciones del ticket agrupadas, con hipótesis posiblemente superadas marcadas.

## Qué se midió

158 consultas: 101 anclas heredadas y 57 títulos de Jira con precedentes escritos en Cerebro. Particiones fijas dev y test por hash. Medición en la VM, CPU de 4 núcleos.

Híbrido: hit@5 0.342, MRR@10 0.257, nDCG@10 0.135. Con reranker: hit@5 0.437, MRR 0.320, nDCG 0.175. Intervalo de 95 % por bootstrap pareado de la mejora en hit@5: de 0.025 a 0.158. La mejora en MRR y nDCG también excluye el cero. En la partición test sola, 56 consultas, el intervalo incluye el cero. La mejora en hit@5 fue de 9.5 puntos, medio punto bajo el criterio de 10 fijado antes de medir. Latencia p50 en la VM: 0.07 s híbrido, 2.4 s con reranker. Falta medirla en el Mac.

El verificador de grounding se calibró con 283 oraciones de 10 borradores, con y sin la evidencia de su ticket. AUC del coseno E5: 0.535. Del cross-encoder: 0.629. De la cobertura de entidades: 0.68. El soporte semántico es una señal débil. Las alertas deterministas son la parte fuerte: entidad inexistente en el índice, hipótesis hacia el cliente, fecha futura y estado volátil.

## Qué falta

bge-reranker-v2-m3 no cupo en la VM de 3 GB. Se evalúa en el Mac cambiando el modelo en .cerebro/config.json y corriendo evaluar-busqueda. El fine-tuning de embeddings tiene el script listo y se niega a entrenar con 32 consultas distintas; exige 300. El bucle de ediciones empieza a registrar desde hoy con bin/ediciones.py. db:knowledge_chunks/555 contiene un secreto dentro de sessions.db; el índice lo redacta y la base solo la corrige Juan desde la terminal.

# Historia: estado verificado, 28 septiembre 2026

Cerebro tiene ahora un motor local común para consola, Codex y Claude Desktop. El motor recupera evidencia; el modelo de la aplicación la interpreta. No se entrenaron sus pesos con las notas.

La auditoría y sus fuentes están en inbox/2026-09-28-cerebro-auditoria.md. Guía operativa en inbox/2026-09-28-cerebro-guia-uso.md. Informe actual de los 19 tickets en inbox/2026-09-28-cola-prioridades-auditoria.md. Jira decide el estado actual.

## Qué funciona

BM25 de SQLite FTS5, embeddings multilingües locales E5 y fusión de posiciones. Modelo fijado a revisión 614241f622f53c4eeff9890bdc4f31cfecc418b3. Texto fragmentado con título, ruta y líneas; lectura de contexto completo; búsqueda exacta de IDs; bitácora y notas nuevas junto a ficha; relaciones registradas de items y menciones entre tickets.

Índice separado y reconstruible en .cerebro/retrieval.sqlite. La siguiente búsqueda detecta cambios, eliminaciones y notas nuevas, y genera sus vectores localmente. No requiere ingerir inbox para encontrarlo. brain/sessions.db conserva 1776 knowledge_chunks, sin escrituras del agente.

Prueba del 28 sep: 3373 fuentes y 15823 fragmentos cubiertos con vector. Son documentos/registros y segmentos, no 3373 hechos independientes. El número crece con nuevas notas. Consultar python3 bin/cerebro status para inventario actual.

Cobertura: knowledge_chunks, items y sus relaciones, 99 reuniones con transcripción, 16 conversaciones, 6 sesiones, Q&A si existe; notas completas de inbox, bitácora, memorias, investigaciones, flujos, triage y Claude outputs. Las fichas y el espejo son vistas duplicadas, disponibles para lectura. No se indexan backups ni adjuntos binarios.

## Qué se midió y qué falta

101 preguntas heredadas, hit-rate@5 por ancla regex: BM25 36/101, híbrido E5 48/101, en el mismo corpus. Mediana de búsqueda caliente sin sincronización: 0.003 y 0.096 segundos respectivamente. No es exactitud de respuestas, no es recall y no es evaluación independiente. Persisten 53 consultas sin el ancla en los cinco primeros resultados. No declarar memoria perfecta.

El experimento anterior llamado BM25 era TF-IDF; LSA no evaluaba embeddings neuronales. Se corrigió la nomenclatura. Las conclusiones del estado del 8 sep sobre descartar vectores no estaban justificadas. Copia previa en .cerebro/ESTADO.md.antes-20260928.

MCP probado por stdio y configurado en ambos clientes, cuatro herramientas de lectura. Hace falta reiniciar las aplicaciones o recargar servidores para que aparezcan en una nueva sesión. Esto no se puede dar por activado en una conversación ya abierta solo porque el archivo de configuración existe.

PDF, Excel, imágenes y otros adjuntos requieren extracción/lectura específica. El motor no actualiza Jira solo: se consulta el conector en vivo. No hay razonador autónomo local, sincronización en segundo plano ni garantía de que el modelo respete siempre el protocolo. La entrada en AGENTS.md/CLAUDE.md guía su uso; la evidencia debe verificarse.

## Seguridad y recuperación

Jira y producción continúan de solo lectura. No se ejecutaron bin/guardar, bin/ingerir_inbox.py ni cerrar. Juan sigue ingiriendo desde su terminal. El modelo de embeddings se descarga, pero los textos se vectorizan en el Mac. Al usar MCP, las fuentes devueltas sí entran en el contexto de la aplicación elegida.

Copias previas de buscar, cola, AGENTS, CLAUDE, MAPA y ESTADO en .cerebro. Copias de las configuraciones MCP junto a cada configuración original. bin/test_cerebro_motor.py, bin/test_cerebro_mcp.py y bin/test_cola.py son pruebas reproducibles. bin/eval_cerebro.py mide recuperación real; cola/eval histórico no tiene cobertura suficiente para certificar la priorización completa.
