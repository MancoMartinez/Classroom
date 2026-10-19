RCS-29231. Talos assessment / Evaluación Talos. 7 Oct 2026.

Issue / Qué pasa
Reprint report numeric error / Error numérico de reimpresiones. Jira: Under Delivery Review.

Cause and assessment / Causa y evaluación
Useful log request; evolving disputed cause / Logs útiles; causa en revisión. Talos correctly requested the recorded error and generated SQL. Subsequent human analysis first blamed Secure typing, then Juan Ramirez argued a positional mapping regression using legacy values. / El error SQL quedó demostrado; la primera explicación humana también requirió revisión.

Evidence / Evidencia
Talos 2026-10-01: https://trebuco.atlassian.net/browse/RCS-29231?focusedCommentId=3374539
Later evidence 2026-10-05: https://trebuco.atlassian.net/browse/RCS-29231?focusedCommentId=3381773
2 Oct note 3375965 proposed text predicates. The 5 Oct correction says that would select unrelated values and break the employee join. Correct field presence alone proves neither lineage nor semantics.

Today / Qué hago hoy
Resolve mapping ownership and business meaning before making the error disappear. / Verificar semántica y linaje antes de cambiar tipos.

Precedents / Precedentes
RCS-29028; RTS-208663; inbox/2026-10-02-rcs-29231.md contains an earlier hypothesis, not final truth.

Commitments and evolution / Compromisos y evolución
Assigned to Delivery; Data team review requested in 3381968. No verified deployed fix or Talos update.

