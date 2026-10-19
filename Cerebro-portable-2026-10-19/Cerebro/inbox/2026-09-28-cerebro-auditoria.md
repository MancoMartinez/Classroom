# Auditoría e implementación de Cerebro, 28 septiembre 2026

La insatisfacción tiene fundamento. Había conocimiento almacenado que el buscador no consultaba, conocimiento reciente fuera de SQLite, fichas que ocultaban novedades y métricas que no demostraban lo que sus conclusiones afirmaban. No es principalmente una limitación inevitable de Claude Desktop o Codex: faltaba un recuperador común, actualizado y verificable.

## Qué estaba fallando

1. bin/buscar devolvía solo los primeros 4000 caracteres de una ficha existente y terminaba. Así omitía inbox y bitácora aun cuando contenían correcciones recientes. Un ID inexistente caía en búsqueda genérica y podía traer otros tickets por la palabra RCS.
2. La búsqueda por archivos contaba subcadenas, con cupos por carpeta y desempates por recorrido. No había un ranking global, deduplicación ni fragmentos con referencias precisas. investigaciones/ y flujos/ quedaban fuera.
3. SQLite tenía 1776 knowledge_chunks, con novedades solo hasta el 15 sep; las notas llegaban al 28. Había 758 notas en inbox al inicio y 1455 embeddings antiguos de otro modelo que el buscador no usaba. Tener vectores guardados no significaba buscar con ellos.
4. El ingestor filtra notas por nombre y comprime secciones a 1200 caracteres o primeras frases a 600. Esto puede omitir una corrección al final o asumir que un borrador ya fue enviado. Se leyó el código, no se ejecutó ni se modificó la base.
5. El experimento etiquetado BM25 era TF-IDF con producto de vectores. LSA no era un modelo neural. Su recall@5 era hit-rate@5: un acierto si aparecía al menos un documento relevante. No encontrar significancia estadística no demuestra equivalencia ni permite descartar la búsqueda como cuello de botella. Se corrigieron nombres y conclusiones en el evaluador.
6. ESTADO.md estaba fechado el 8 sep y MAPA conservaba cifras de agosto. Ninguno de los dos clientes tenía un servidor Cerebro configurado. Cada aplicación terminaba improvisando su propia manera de consultar.
7. La cola automática no usaba jsdPublic para visibilidad ni accountType para bots, dependía del orden recibido y podía rebajar un pendiente porque existía una nota local posterior. Carlo de NEXCOM tampoco entraba en su identificación de clientes. Una investigación o un borrador no cumple una promesa al cliente.

## Qué quedó implementado

Motor único en bin/cerebro_motor.py, accesible mediante bin/buscar, bin/cerebro y bin/cerebro_mcp.py. Índice local reconstruible en .cerebro/retrieval.sqlite, separado de la base original. Usa BM25 real, embeddings multilingües E5 locales y fusión de rangos. Segmenta sin desechar texto, conserva títulos/ruta/líneas y limita duplicados al recuperar.

Cada búsqueda detecta cambios y eliminaciones. Las notas nuevas obtienen vector automáticamente. El acceso exacto por ticket combina bitácora, notas recientes, ficha y referencias; no confunde IDs parciales. Conserva las relaciones de items y muestra coapariciones entre tickets como pistas explícitamente no causales.

También se incorporaron las transcripciones y resúmenes de 99 reuniones, 16 conversaciones y 6 sesiones guardadas en SQLite, además de knowledge_chunks, items, Q&A y carpetas de texto. En la evaluación hubo 3373 fuentes y 15823 fragmentos vectorizados. No son 3373 hechos independientes: hay historias, borradores y repeticiones que todavía deben interpretarse.

Codex y Claude Desktop quedaron configurados para llamar al mismo servidor por stdio. Cuatro herramientas, todas de lectura: búsqueda, contexto de ticket, lectura de fuente y estado. El protocolo MCP se probó con un cliente real. La aparición de esas herramientas en las aplicaciones requiere reiniciar o recargar; no se afirma que esta conversación ya las tenga cargadas.

Se actualizaron AGENTS, CLAUDE, MAPA y ESTADO para obligar a consultar fuentes recientes, distinguir borradores de comunicaciones y validar estados en Jira. Las ocho reglas permanentes siguen intactas. La cola automática ahora respeta visibilidad, bots, orden cronológico y no cancela deuda por una bitácora. Sigue siendo una heurística, por lo que el informe de prioridades combina lectura humana y evidencia.

## Resultados medidos y sus límites

En el corpus ampliado, con las mismas 101 preguntas y anclas heredadas: BM25 obtuvo 36/101 y el híbrido E5 48/101 en hit-rate@5. Son 12 consultas adicionales con ancla en los cinco primeros resultados. El primer modelo de paráfrasis probado no mejoró el resultado y se sustituyó por uno entrenado para recuperación.

Mediana caliente sin sincronizar fuentes: BM25 0.003 s; híbrido 0.096 s. Estos tiempos excluyen arranque, carga inicial del modelo y generación de nuevos vectores. No se deben presentar como latencia total desde la aplicación.

Quedan 53 preguntas sin el ancla en top 5. El set no es independiente, no hubo juicio humano ciego y una regex no certifica una respuesta correcta. La comparación no es directamente comparable con el antiguo 33%, medido sobre otro corpus. No hay base para afirmar que Cerebro recuerda todo o que sus respuestas tienen 48% de exactitud.

Pruebas ejecutadas: IDs exactos/desconocidos, notas nuevas pese a ficha vieja, cobertura de investigaciones, actualización y borrado, vectorización incremental, lectura restringida al corpus, base fuente intacta en prueba, MCP real por stdio y clasificación pública/interna/bots/borradores. El evaluador histórico de cola pasó sus cuatro casos presentes; cuatro no certifican los 19 tickets actuales.

## Cola completa

Se leyeron en Jira los 19 abiertos asignados a Juan, todos los proyectos, con comentarios completos al corte 17:35 Bogotá. RCS-29145 ya estaba Completed. Guardados panorama y 19 notas de menos de 2500 caracteres en inbox/2026-09-28-cola-prioridades-auditoria.md y los archivos individuales vinculados allí.

Primero: verificar coordinación NEXCOM y responder el nuevo acceso de McDonald’s. Trabajo técnico: THD por la ventana histórica demostrada y GPC por recuperación de datos sin dueño confirmado. Casos cercanos a cierre: 7-Eleven RCS-28212, ADUSA RCS-29026/RCS-29123 y Winn-Dixie RCS-29130, siempre con validación.

## Qué todavía no está cubierto

PDF, Excel, imágenes y otros adjuntos no se indexan automáticamente. Jira se consulta en vivo a través del conector, no mediante un servicio de sincronización nuevo. El modelo del escritorio sigue siendo quien razona; no se entrenaron sus pesos ni se instaló un LLM autónomo. La búsqueda proporciona evidencia, no convierte contradicciones históricas en conocimiento validado.

Las próximas mejoras deben salir de fallos concretos registrados: consultas nuevas con fuentes esperadas para evaluación independiente, extracción de adjuntos cuando aporten evidencia ausente, y reordenamiento neural si demuestra mejorar ese set. No se añadieron entrenamiento propio, base de grafos separada ni infraestructura de servidores sin evidencia de que resuelvan el siguiente cuello de botella.

## Preservación y fuentes

Jira y producción permanecieron en solo lectura. sessions.db no se escribió y los ingestores prohibidos no se ejecutaron. Las descargas fueron de modelos/dependencias; la vectorización de notas ocurre en el Mac. Las fuentes que el agente pide por MCP sí pasan al contexto de Codex/Claude, igual que al leer un archivo en una conversación.

Fuentes locales: versiones previas guardadas en .cerebro, bin/buscar, bin/eval_recuperacion.py, bin/cola.py, esquemas/conteos SQLite en mode=ro y .cerebro/evaluacion-2026-09-28.json. Modelo fijado a revisión 614241f622f53c4eeff9890bdc4f31cfecc418b3. Copias de configuraciones junto a los originales.

Referencias oficiales: [MCP en Codex](https://learn.chatgpt.com/docs/extend/mcp?surface=cli), [MCP de Anthropic](https://www.anthropic.com/news/model-context-protocol), [recuperación contextual](https://www.anthropic.com/engineering/contextual-retrieval), [SQLite FTS5/BM25](https://www.sqlite.org/fts5.html), [multilingual E5](https://huggingface.co/intfloat/multilingual-e5-small?hardware=rtx-4060). Se usa contexto de título/encabezado, no se afirma haber implementado íntegramente el método de contextualización generativa de Anthropic.

Verificación final: el SHA-256 de brain/sessions.db coincide con el de inicio. Las cuatro herramientas MCP respondieron; la búsqueda híbrida por MCP devolvió evidencia sin avisos de degradación.
