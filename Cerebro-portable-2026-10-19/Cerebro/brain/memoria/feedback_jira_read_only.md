---
name: feedback-jira-read-only
description: Nunca escribir en Jira — solo leer. Juan ejecuta todos los cambios manualmente con un paso a paso que yo redacto.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9fc04b4a-14c1-4cb0-b5b5-97ac10fcabe5
  modified: 2026-08-13T18:20:42.971Z
---

Nunca ejecutar acciones de escritura en Jira (comentarios, transiciones, cambios de campo, labels, links). Solo lectura: `getJiraIssue`, `searchJiraIssuesUsingJql`, `getTransitions...`. Sitio: `trebuco.atlassian.net`.

**Why:** solo Juan tiene autoridad para escribir o cambiar cosas en los tickets; es su cola y su responsabilidad ante el cliente. Dicho explícitamente el 30 jul 2026.

**How to apply:** entregar siempre un paso a paso en el chat — campos a cambiar, status destino, y los comentarios (interno y de cliente) redactados completos y listos para copiar y pegar. Él los revisa y los aplica manualmente. No ofrecer publicarlos ni preguntar si los aplico yo.

**Excepción autorizada el 12 ago 2026: los labels `Uni_Jul_26_*`.** Juan pidió explícitamente "rompiendo la regla agrega todas las etiquetas... pero asignalas porfavor" para el barrido previo al bucket review. Es una excepción acotada: **solo labels de la Unificación, solo agregar, nunca quitar.** Quitar un label es una decisión de quien lo puso y se propone, no se ejecuta. Los comentarios, transiciones y prioridades siguen siendo suyos. Reasignar un ticket solo cuando hay una base clara (la misma persona ya trabaja el defecto gemelo); repartir carga entre el equipo se propone, no se aplica.

**Confirmado en la práctica el 13 ago 2026:** quité `Uni_Jul_26_ReportsExports` de RCS-28247 y J.R. Teagle lo volvió a poner tres horas después. No se re-quitó. Quitar el label de otro es su decisión, se le pregunta y ya.

Relacionado: [[project_appriss_support_role]], [[user_profile]], [[feedback_verificar_la_fuente_no_el_resumen]]
