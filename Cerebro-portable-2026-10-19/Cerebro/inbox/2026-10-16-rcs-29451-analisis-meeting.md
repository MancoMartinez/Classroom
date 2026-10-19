Qué pasa
Jira: Accepted into Development, Shandana Khan. ENG-10069: Backlog sin asignar. Nivel vacío en primer ingreso y jerarquías comparten el RCS.
Causa
Falla observable confirmada para Rachel: nivel 5 disponible antes del alta, cuenta creada con NULL. Hipótesis: diferencia entre flujo de creación y actualización. Falta confirmación del código.
Evidencia
Jira en vivo, nota interna 3397050 del 15 oct: https://trebuco.atlassian.net/browse/RCS-29451?focusedCommentId=3397050
49 cuentas con nivel en feed y NULL en cuenta es corte histórico; no se probó primer ingreso para todas. ENG-10069 no trae comentarios ni la secuencia técnica en su descripción.
Qué hago hoy
Para la reunión, proponer responsable de Engineering, revisión de la nota del RCS y criterio de validación de primer ingreso. Juan ya preservó la evidencia; esta sesión no consultó producción.
Precedentes
RCS-27578 corrigió Persistent en julio; no explica por sí solo Rachel en octubre. Consultar bin/buscar e investigaciones/2026-10-16-tailored-incident-id-analisis.md.
Compromisos
Público 3397054 del 15 oct: Engineering revisa; Soporte ofrece nivel manual para nuevos reportes. Sin ETA publicada. El guion completo queda pendiente de revisar el análisis.
