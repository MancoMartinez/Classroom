# RCS-29417: relación con RCS-29205

Qué pasa
Jira en vivo, 15 octubre 2026. RCS-29417: Under Support Review, Edwin Garzon, Medium; faltan Paid-In/Paid-Out en tiendas 10111, 910647 y 9375 desde fechas de agosto. El título dice después del 19 agosto. RCS-29205: Work in progress, Juan Martinez, High; work item de refunds sin resultados del 24 agosto al 27 septiembre.

Causa
Relación técnica sustentada. Duplicidad sin confirmar. En 29205, SnowTime dejó sin poblar campos de tokens y Paid-In/Paid-Out. El comentario interno 3384023 del 7 octubre confirma que pyardm generaba headers tipo 50/51 desde paidin_paidout; SnowTime necesita un modelo nuevo y filas históricas. Falta comprobar ese mecanismo en las tiendas y fechas concretas de 29417. El 19 agosto antecede al corte del 27 agosto.

Evidencia
29205, comentario interno 3381601 del 5 octubre: X_PAIDINPAIDOUTREASONCODE y ENUM pasan de 10.253 filas con datos en 17 a 23 agosto a cero en 31 agosto a 6 septiembre. Comentario interno 3386643 del 9 octubre: PR 58962 incluye ambos campos.
29417, descripción y sus 2 comentarios completos: sin diagnóstico confirmado ni enlace de duplicado. Talos, interno 3394922 del 13 octubre, declara que no pudo consultar datos ni distinguir filas ausentes de filas que no aparecen en pantalla. 29205: 19 comentarios completos; sin enlace a 29417.
Fuentes: https://trebuco.atlassian.net/browse/RCS-29205 y https://trebuco.atlassian.net/browse/RCS-29417. Notas locales: inbox/2026-10-14-sbx-work-items-estado.md e inbox/2026-10-14-rcs-29205-verificacion-resultado.md. Registran deploy y recarga pendiente; no prueban ejecución posterior.

Qué hago hoy
Mantener la relación como hipótesis de cobertura del mismo arreglo. Verificar ejemplos exactos y cobertura de recarga antes de proponer duplicado. Ningún cambio en Jira.

Precedentes
db:knowledge_chunks/1918: coaparición no demuestra causa común.

Compromisos
Juan publicó el 14 octubre en 29205 que comprobará el periodo fiscal y publicará el resultado. Ningún compromiso nuevo.

Siguiente paso
Edwin: pedir fechas y transacciones concretas de esas tiendas, especialmente del 19 al 26 agosto.
Anushka: confirmar si el arreglo y la recarga Paid-In/Paid-Out cubren esos ejemplos y si ya se ejecutaron.
