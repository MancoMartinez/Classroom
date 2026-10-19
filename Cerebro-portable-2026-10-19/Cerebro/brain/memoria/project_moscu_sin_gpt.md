---
name: project_moscu_sin_gpt
description: La key de Azure de Moscú murió (401 en chat y embeddings); Claude Code pasa a ser el motor de inteligencia y Moscú queda como almacén
metadata:
  type: project
---

Verificado el **18 ago 2026**: la API key de Azure guardada en el Keychain (`com.interviewapp.azure.apiKey`) devuelve **401 en todos los endpoints**, tanto el de chat (`.../deployments/gpt-4o/chat/completions`) como el de embeddings (`.../deployments/Moscu/embeddings`), en los tres hosts posibles. La key rotó o la suscripción se cerró. No es un problema de configuración.

**Consecuencia:** dentro de la app Moscú están muertos el chat, la contextualización de chunks, el resumen de conversaciones, la restauración de puntuación, el Quick Capture classifier, el DecisionDetector, el WeeklyDigest y los pulsos de reunión. Todo eso llamaba a GPT-4o.

**Lo que sigue vivo sin ninguna key:** whisper.cpp local para transcribir, SQLite con FTS5 para buscar, y toda la base de 1.500+ chunks ya escrita.

**El replanteo, y es la decisión de fondo:** Moscú deja de ser "app con IA adentro" y pasa a ser **el almacén y el índice**. La inteligencia la pone **Claude Code**, que lee y escribe la misma base con scripts. Transcribir en Moscú, procesar en Claude Code, guardar de vuelta en Moscú.

**Ruta de escritura directa a la base** (la app debe estar cerrada):
`~/Library/Application Support/InterviewApp/sessions.db`, tabla `knowledge_chunks(folder_id,title,body,source_path,ord,created_at)`. Los triggers de FTS5 indexan solos al insertar. Backup siempre con `VACUUM INTO` antes de tocar.

**Embeddings**: Ollama local funciona (`nomic-embed-text` ya descargado, 768 dims). Los 1.455 vectores existentes son `text-embedding-3-small` de 1536 dims y **no se pueden mezclar** con los de Ollama, el coseno da 0. O se renueva la key de Azure, o se re-indexa todo a 768. Decisión pendiente.

**Bug corregido el mismo día:** el botón "Vectorizar" fallaba en silencio porque `EmbeddingClient.isAvailable()` solo comprobaba que existiera una URL y una key, nunca que funcionaran. Se agregó `probeError()` con petición real y `vectorizationError` visible en la UI.

Ver [[project_moscu_state]].
