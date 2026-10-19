RCS-29123. Talos assessment / Evaluación Talos. 7 Oct 2026.

Issue / Qué pasa
Smart Alerts stopped / Smart Alerts detenidas. Jira: Under Customer Review.

Cause and assessment / Causa y evaluación
Material inference error / Error de inferencia material. Talos equated empty history with no evaluation. ENG-9486 documents a path that sends email and deadlocks before inserting history. Missing telemetry is not proof of non-execution. / Historial vacío no prueba ausencia de ejecución; el bloqueo precedía al registro.

Evidence / Evidencia
Talos 2026-09-25: https://trebuco.atlassian.net/browse/RCS-29123?focusedCommentId=3364532
Later evidence 2026-09-28: https://trebuco.atlassian.net/browse/RCS-29123?focusedCommentId=3370892
Use ENG-9486 description and Solution as the mechanism: ConfigureAwait(False), not the older support explanation of one run waiting for another. Talos was not expected to know the later fix, but its original implication was too strong.

Today / Qué hago hoy
Separate evaluation, provider handoff, delivery and history persistence. / Separar evaluación, entrega y persistencia.

Precedents / Precedentes
ENG-9486; inbox/2026-09-29-rcs-29145-respuesta-teams.md explicitly supersedes serialisation.

Commitments and evolution / Compromisos y evolución
Customer update 3370890: go-forward recovery; no automatic resend of the missed interval. No Talos revision.

