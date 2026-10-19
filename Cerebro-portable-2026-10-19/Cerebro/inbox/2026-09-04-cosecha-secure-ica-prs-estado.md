# Cosecha 4 sep 2026 — Secure ICA, estado de los cuatro tickets y PRs

Sesión fuente: "ICA receipt viewer issues analysis" (local_04925369), transcripción del 3 sep 2026.

## Hallazgo verificado

PRs 55913 y 56235, que cubren RCS-28254 y el fix original de RCS-28253, están mergeados en producción desde el 29 de agosto.

La regresión que ICA reportó el 2 de septiembre se está atendiendo en un PR nuevo, 57002, que también cubre el problema de descuento de RCS-28717. Ese PR seguía en draft sin reviewers asignados al 3 de septiembre, no había llegado a staging ni a producción.

RCS-28716, causa raíz confirmada: falta un guard en el banner de la sección Audit. Sin PR abierto todavía.

RCS-28719 sigue sin causa raíz identificada. Cita textual de Nikita en su resumen de investigación: "We need an actual example of a missing row/transaction from the customer to investigate further, nothing in the data we can access points to a mechanism."

## Carga verificada en Jira al 3 sep, usada para decidir quién cubre

Diego Buelvas: 7 abiertos, 0 en Work in progress, la mayoría esperando cliente o release.
Edwin Garzon: 16 abiertos, 5 en Work in progress, 2 High.
Sebastian Rueda: 15 abiertos, 6 en Work in progress, uno escalado.

## Decisión

Con Nikita fuera el 4 de septiembre, Diego Buelvas queda cubriendo PR 57002 y los tickets RCS-28716, RCS-28717 y RCS-28719 mientras ella no está. Aviso enviado a Diego en español pidiendo que reporte si el PR avanza o si ICA manda la transacción faltante para RCS-28719.
