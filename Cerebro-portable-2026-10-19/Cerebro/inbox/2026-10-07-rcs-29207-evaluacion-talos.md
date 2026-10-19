RCS-29207. Talos assessment / Evaluación Talos. 7 Oct 2026.

Issue / Qué pasa
Star Farming failures / Fallos Star Farming. Jira: Completed.

Cause and assessment / Causa y evaluación
Useful test, missed explicit precedent / Prueba útil, precedente explícito omitido. Talos requested actual run outcomes and saved SQL, which was useful. It did not exploit RCS-28873, already linked in the description and documenting MemberID type/binding defects before triage. / La omisión reduce especificidad; no demuestra qué componente interno de recuperación falló.

Evidence / Evidencia
Talos 2026-09-30: https://trebuco.atlassian.net/browse/RCS-29207?focusedCommentId=3373376
Later evidence 2026-10-01: https://trebuco.atlassian.net/browse/RCS-29207?focusedCommentId=3374851
The named query failed on x_MemberID compared with an unquoted number. 3374851 records repeated failures. Restored results: 3381525 on 5 Oct; customer confirmation: 3382815 on 6 Oct.

Today / Qué hago hoy
Retrieve explicit links and verify the exact failing definition before applying a precedent. / Leer enlaces y probar el mecanismo concreto.

Precedents / Precedentes
RCS-28873 comments 3337746 and 3364681; no claim that all MemberID issues require the same fix.

Commitments and evolution / Compromisos y evolución
Completed, customer verified. No later Talos note; resolution belongs to the documented human/engineering sequence.

