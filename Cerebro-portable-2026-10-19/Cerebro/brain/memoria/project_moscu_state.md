---
name: project-moscu-state
description: "Estado actual de Moscú — segundo cerebro macOS local-first en ~/Desktop/InterviewApp/antigravity. Pases completados, stack, cómo construir."
metadata: 
  node_type: memory
  type: project
  originSessionId: c86c8d24-b93a-48cd-9cb8-1c79cbfd9e3e
---

**Moscú** (antes InterviewApp/Jarvis) es un asistente personal macOS-only (arm64, macOS 14+) con dos modos coexistentes:

- **Overlay (Meeting)**: ventana flotante `sharingType=.none`, invisible a screen-capture. ScreenCaptureKit + whisper.cpp (Metal) + GPT-4o streaming. Para reuniones en Zoom/Meet/Teams. (Renombrado de "Live Interview" a "Meeting" en `WorkbenchSection.live` rawValue y header.)
- **Workbench / Chat**: ventana principal NavigationSplitView con perfil, contextos, knowledge folders (RAG BM25+vector+RRF), items, chat conversacional, modos Código/Ejemplo/Visión.

**Bundle ID**: `com.interviewapp.moscu`
**Ruta del proyecto**: `~/Desktop/InterviewApp/antigravity/`
**Estado a 2026-05-27**: Pases 1–26 + F1–F6 + Ruta A + Ruta B (B1/B2/B3) completados + fixes recientes. 85 tests, 0 failures. Score 91/100 producción-ready.

**Why:** Cumple reglas no negociables: free, local-first, no-telemetry, invisible a capture, ≤2s latency, no SIP violations, ad-hoc signed.

**How to apply:** Antes de proponer cambios, verificar que no rompen estas reglas. El estado actual es muy avanzado — evitar refactoring innecesario.

**Preferencia idioma**: El usuario prefiere respuestas en español.

## Cómo construir y ejecutar

```bash
cd ~/Desktop/InterviewApp/antigravity
./scripts/run-app.sh release          # build + open
./scripts/run-app.sh release --reset  # + reset TCC permisos
```

**NO usar `swift run`** — produce binario sin Info.plist y macOS niega permisos de mic/screen.

## Schema actual: v9
Tablas: `contexts`, `categories`, `items`, `knowledge_folders`, `knowledge_chunks` (con `embedding BLOB`, `contextualized_body`), `files`, `chat_conversations`, `chat_messages`, `proactive_suggestions`, `user_profile`, `routing_rewards`, `item_links`, `schema_meta`.

## Fixes recientes (2026-05-27)

**STT streaming fix (crítico)**:
- Reemplazado `single_segment=true` + `await result` por `single_segment=false` + `new_segment_callback`.
- Cada frase decodificada se emite inmediatamente vía `SegmentYielder` C bridge.
- Sentinel `windowResetMarker` (U+FFF0) resetea el acumulador `livePartial` entre ventanas de audio.
- `captionTask` ahora acumula segmentos (append) en lugar de reemplazar — `livePartial` crece frase a frase.

**UI fixes**:
- Auto-scroll al final del transcript card via `ScrollViewReader`.
- Bug post-stop analysis corregido: `lastSavedDecisions` es `@Published`, `saveAnalysisToKB()` usa folder/contexto sugerido por IA.

## Visión del usuario — features solicitadas (pendientes de implementar)

- **Pre-meeting brief**: antes de iniciar grabación, el panel derecho muestra chunks relevantes de KB, decisiones recientes y tareas abiertas relacionadas al contexto activo.
- **Clipboard paste para screenshots**: Cmd+V en chat y Meeting para pegar imágenes de NSPasteboard en modo visión.
- **Meeting history**: lista de reuniones pasadas con resúmenes; el contenido de cada reunión se auto-categoriza en KB/items.
- **Agent-style knowledge synergy**: surface de información context-aware sin prompting explícito del usuario; todo sincroniza en base a lo que ocurre en la reunión.
- **Categories/files siempre disponibles** para análisis detallado.
- **Meeting summaries auto-routed** a la categoría/folder correcta vía IA.

## Pases pendientes
- Pase 20: WhisperKit/ANE eval (opcional, depende de feedback de uso real)
- Fase 4: deprecar overlay separado (esperando validación del usuario)
- Features de visión del usuario (ver sección anterior)

## Problemas conocidos
- Transcripción ES "traduce a medias" — usuario decidió esperar. Opciones: forzar `language="es"`, ampliar WhisperFilter, cambiar a ggml-medium, o WhisperKit.
- Build warnings no críticos: `ChatMessage.Role` no Sendable, `mlModelClass` AnyClass?.
- TCC puede revocar permisos si cambia hash del bundle → usar `--reset`.

## Logs en vivo
```bash
/usr/bin/log stream --predicate 'subsystem == "com.interviewapp"' --level info
```
