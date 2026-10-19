RCS-29234. Talos assessment / Evaluación Talos. 7 Oct 2026.

Issue / Qué pasa
Case save failure / Fallo al guardar casos. Jira: Accepted into Development.

Cause and assessment / Causa y evaluación
Useful evidence request, insufficient runtime model / Petición útil, modelo runtime incompleto. Talos requested a concrete case, timestamp and error record. Shared save code cannot exclude tenant-specific generated-screen state. Later recurrence followed Screen Designer changes; restart restored service without proving a permanent repair. / Pedir trazas ayudaba; compartir código no descarta estado específico del tenant.

Evidence / Evidencia
Talos 2026-10-01: https://trebuco.atlassian.net/browse/RCS-29234?focusedCommentId=3374675
Later evidence 2026-10-02: https://trebuco.atlassian.net/browse/RCS-29234?focusedCommentId=3375939
Sebastian records successful baseline cases and failures after adding/building a field in staging. Matthew accepted sprint work on 6 Oct, 3382480. The first stale-assembly explanation is not independently proven by a restart.

Today / Qué hago hoy
Distinguish observed trigger, temporary restoration and confirmed mechanism. / Separar disparador, recuperación y mecanismo.

Precedents / Precedentes
investigaciones/2026-10-02-adusa-save-y-fechas-screen-designer.md; ENG-9281 is analogous, not confirmed same cause.

Commitments and evolution / Compromisos y evolución
Public 3382583 commits to the next confirmed engineering step. No later Talos note.

