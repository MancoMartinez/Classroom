Freeze de despliegues y hotfixes de L2. Revisión 14 octubre 2026.

Qué preguntaron y por qué
La pregunta busca aclarar si L2 puede desplegar hotfixes durante noviembre y diciembre por iniciativa propia o necesita aprobación. Interpretación de la intención, no motivo confirmado por el autor. Surge de la tensión entre mantener estabilidad en temporada comercial y corregir fallos que impiden usar el producto.

Qué aporta cada enlace
Freeze Periods es la política interna. Define freeze como restricción de despliegues en determinados entornos, explica el objetivo de estabilidad y admite excepciones para parches críticos de seguridad y hotfixes de bugs que afectan el uso del producto. Añade expresamente coordinación y aprobación de los clientes.
Release Calendar es el calendario destinado a clientes, según Freeze Periods. Sirve para consultar fechas de releases y freezes. No pude abrir su contenido con la herramienta web; no verifiqué las fechas exactas de 2026.

Evaluación de la respuesta
La respuesta reconoce una excepción válida. Omite la condición de aprobación del cliente que aparece en la oración siguiente del documento. También omite los parches críticos de seguridad. La frase may still be deployed expresa posibilidad condicionada, no autorización automática para L2.

Distinción operativa
Crear un PR, aprobarlo y desplegarlo son acciones distintas. Freeze Periods regula despliegues; no documenta una prohibición de preparar PRs, ni otorga a L2 autoridad especial para desplegar. La aprobación técnica del PR no acredita aprobación del cliente para una excepción al freeze. La página no identifica quién tramita la excepción interna ni el procedimiento para obtener autorización.

Qué aclarar
Confirmar quién autoriza internamente las excepciones para L2 y cómo registrar la coordinación y aprobación del cliente antes de desplegar.

Fuentes
https://trebuco.atlassian.net/wiki/spaces/RTS/pages/474677477544/Freeze+Periods
Versión 11, publicada 6 octubre 2026; leída completa hoy.
https://docs.apprissretail.com/products/product-docs/general/release-calendar
Referencia verificada en Freeze Periods; contenido no accesible en esta revisión.
Antecedente privado leído: db:meetings/64, líneas 75 a 249. Formación del 14 julio sobre pruebas, revisión y aprobación de PR. No equivale a política de excepción al freeze.
