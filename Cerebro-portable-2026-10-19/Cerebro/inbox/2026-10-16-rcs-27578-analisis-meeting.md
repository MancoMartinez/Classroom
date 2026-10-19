Qué pasa
Jira en vivo: Closed, Matthew Everett. Cliente confirmó resolución el 8 jul.
Causa
Defecto histórico: sso.GetUserSecurityLevel filtraba Persistent=1 e ignoraba niveles de archivo. La explicación inicial de timing fue insuficiente para Jonathan Thompson, cuyos datos existían antes de su ingreso.
Evidencia
Nota interna 3205066 del 1 jul: 3917 usuarios con fila válida ignorada y 19 sin asignación. Resolución 3217064 del 8 jul: fix activo desde 2 jul, PR 54159 y referencia permanente 54149. https://trebuco.atlassian.net/browse/RCS-27578
Capturas de Jonathan adjuntas; archivos y dos MSG descargados. Esta sesión abrió los correos y extrajo sus imágenes. Los PR solo se leyeron como referencias del expediente.
Qué hago hoy
Explicar la diferencia con Rachel: procedimiento actual devuelve 5 y datos llegaron antes del alta. No reutilizar la espera de 24 horas como diagnóstico del caso actual.
Precedentes
RCS-26519 y RCS-27269. Historia por bin/buscar; análisis en investigaciones/2026-10-16-tailored-incident-id-analisis.md.
Compromisos
Matthew aclaró públicamente el 6 jul que usuario correctamente incluido no debe iniciar sesión y esperar después. Los 19 sin fila y roster completo frente a delta quedaron como pendientes históricos, sin asumir vigencia actual.
