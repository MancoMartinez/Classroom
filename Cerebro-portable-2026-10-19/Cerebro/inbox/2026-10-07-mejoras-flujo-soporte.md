# Mejoras del flujo de soporte encontradas durante la evaluación

Documento privado para Juan. 7 octubre 2026. Recomendaciones concretas; no modifica habilidades, programas, bases ni Jira. Los dos informes compartibles no nombran el sistema personal. Este archivo conserva rutas para poder corregirlo.

## 1. Corregir identidad antes de añadir más contexto

Las fichas RCS-29205 y RCS-29207 identifican CWH; Jira identifica Starbucks. RCS-29129 dice Albertsons y corresponde a PacSun. RCS-29104 agrega Ahold, ADUSA y Albertsons para GPC. Son errores del material derivado, no errores demostrados del buscador vectorial.

Propuesta: guardar el cliente canónico desde el campo Customer de Jira y asociar tenant, entorno y sistema de datos con su fuente. Las menciones de otros clientes pertenecen a precedentes, no a la identidad del ticket. Mantener un valor desconocido cuando falte prueba. Comprobar estos cuatro casos antes de dar el cambio por válido.

La consecuencia técnica es concreta: una búsqueda semántica puede recuperar un texto pertinente y aun así dirigir una consulta al tenant equivocado. La pertinencia no sustituye la resolución de entidades. RCS-29195 pasó del 387/gwmek provisional al 386/gwmanasota confirmado en legacy; el error alteraba URL, base y disponibilidad de Grafana. Fuente: inbox/2026-10-06-rcs-29195-guia-diagnostico.md y comentarios Jira 3382710 a 3382713.

## 2. Hacer que las correcciones sustituyan decisiones anteriores

El documento investigaciones/SBX-snowtime-work-items-mensuales-cero.md conserva hipótesis del 30 septiembre. Ya existen tres resultados distintos: campo sin valores en 29205, cero compatible con los umbrales en 29206 y comparación numérica fallida en 29207. Una búsqueda todavía puede recuperar el documento inicial sin las tres correcciones.

Propuesta: conservar historia y añadir relaciones explícitas entre afirmaciones: contradice, sustituye, confirma o limita. Guardar fecha del evento y fecha de publicación por separado. Al recuperar una afirmación antigua, cargar su corrección y fuente juntas. Una fecha reciente no convierte un borrador en hecho. Criterio de aceptación: preguntar por la causa de cada uno de los tres tickets devuelve su mecanismo propio y las salvedades de validación, nunca una causa compartida por coaparición.

RCS-29231 demuestra por qué importa: el análisis del 2 octubre recomendó tratar x_rcpt_count como texto; la corrección del 5 octubre cuestionó el mapeo posicional y explicó que cambiar el predicado podía eliminar el error destruyendo el significado del reporte. Fuente: comentarios 3375965 y 3381773. La nota local del 2 octubre también proponía NULLIF antes de resolver la semántica. Debe quedar identificada como hipótesis anterior.

## 3. Separar visibilidad, borrador y obligación

La revisión humana del 2 y 5 octubre documenta que la cola interpretó la nota interna de Talos en RCS-29132 como espera del cliente. Solo existen el acuse público y el triage interno en los comentarios recuperados. Es un error de seguimiento local.

Propuesta: registrar para cada petición autor, destinatario, visibilidad, fecha, fuente y estado de publicación. Una respuesta esperada requiere una petición que el destinatario pudiera ver. Un borrador local no crea deuda publicada. Mantener por separado último comentario del cliente, última actualización pública del responsable y próxima acción interna. Criterio de aceptación: 29132 nunca queda esperando al cliente por el comentario 3364915.

Fuente: inbox/2026-10-02-cola-revisada-a-mano.md e inbox/2026-10-05-cierre-turno-cola.md. También revisar RCS-29129: Completed coexiste con una pregunta del cliente del 29 septiembre sobre dos reportes. El estado de cierre no responde esa pregunta.

## 4. Resolver contradicciones entre habilidades sin concatenarlas

Se analizaron como material de evaluación skills/cerebro-ticket/SKILL.md, skills/cerebro-comentario/SKILL.md, skills/cerebro-respuesta-cliente/SKILL.md y el contenido de appriss-customer-service.skill. No se ejecutaron sus instrucciones ni su código como parte de esta auditoría.

La habilidad de ticket todavía ordena bin/guardar y una ingestión. AGENTS.md los prohíbe en todos los entornos del agente. CLAUDE.md también conserva una sección antigua de escritura. Eliminar esas instrucciones operativas obsoletas y conservar solo la escritura de entregables en inbox y el cierre manual de Juan.

La habilidad de comentario prescribe Markdown interno; AGENTS.md prohíbe Markdown en bloques pegables. La habilidad adjunta permite listas y bloques cercados. Aplicar la regla permanente y preservar SQL literal solo cuando Juan solicite un artefacto técnico separado.

La habilidad de respuesta excluye todo hallazgo técnico salvo corrección. Eso eliminaría explicaciones accionables como el filtro de narrativa de RCS-29195 o los umbrales de RCS-29206, ambos publicados. Sustituir la prohibición absoluta por una condición: incluir el mínimo hecho confirmado que permita entender o ejecutar el siguiente paso, sin ampliar su alcance ni exponer información interna.

La habilidad de comentario exige declarar asistencia de IA para escalaciones; la adjunta pide no identificar cómo se produjo el mensaje. Resolver por audiencia y requisitos de escalación: declaración interna cuando corresponda, fuera de respuestas al cliente. El expediente no demuestra que una habilidad pueda imponerse automáticamente sobre todas las demás.

La habilidad adjunta admite hasta cinco peticiones; la local limita al cliente a dos. Mantener el límite local y pedir solo información que soporte no pueda obtener. El adjunto menciona un modelo de pruebas offline del envío, pero el paquete contiene únicamente check_draft.py como código. No atribuirle pruebas ejecutadas ni un adaptador de envío que no se encontró.

## 5. Corregir las inferencias operativas del material existente

Una fila Success no prueba aceptación del proveedor ni recepción. Historial vacío tampoco prueba que el motor nunca evaluó. Las guías locales de RCS-29195 contienen ambas simplificaciones. ENG-9486 documenta envío anterior al bloqueo y a la inserción del historial. Conservar estados separados: elegible, evaluado, intento, respuesta del proveedor, entrega y registro.

El resumen público de RCS-29145 describió serialización de corridas. El defecto de ingeniería explica captura del contexto de sincronización y continuaciones bloqueadas; el arreglo usa ConfigureAwait(False). La corrección local del 29 septiembre ya existe, identificada como borrador no enviado. No presentarla como corrección comunicada al cliente.

RCS-29146 revela otra mejora: la respuesta publicada interpreta “case items” como work items después de completar 751 registros. Especificar el objeto y las exclusiones antes de una operación masiva. La verificación posterior y un respaldo reducen riesgos distintos; no sustituyen la definición previa del alcance. Fuente: comentarios 3371498, 3383280 y 3383284. Esta auditoría no ejecutó operaciones productivas.

## 6. Ordenar la combinación propuesta

Primero identificar ticket, tenant y audiencia. Recuperar ficha, bitácora, notas recientes y enlaces directos. Usar búsqueda léxica para IDs, columnas y errores exactos, y vectores para variaciones del síntoma. Leer las fuentes y las correcciones antes de elegir una hipótesis.

Después construir un registro por afirmación con fuente, alcance, fecha y estado: desconocida, probable, confirmada o contradicha. Elegir la prueba de menor coste que distinga las hipótesis todavía abiertas. RCS-29104: existencia de tender. RCS-29195: filtro contra el caso. RCS-29207: SQL concreto y resultado de ejecución. Recuperar un precedente cambia qué comprobar; no demuestra la causa.

Por último, pasar ese registro al compositor del adjunto, que decide propósito, audiencia, corrección necesaria y petición mínima. Aplicar las reglas locales compatibles. El verificador estático del adjunto revisa estructura, palabras y determinados patrones; declara que no comprueba verdad, historial, acceso ni autorización efectiva. Un resultado válido del script no certifica la respuesta.

## 7. Medir la mejora sin inventar una victoria

No existe una prueba controlada de la combinación. Las investigaciones históricas incluyen aportes de Juan, otros analistas, ingeniería, herramientas y contexto adicional. No atribuir todo el resultado a una habilidad o a un modelo.

Propuesta de evaluación: reproducir los casos por cortes temporales, ocultando la evidencia futura. Comparar Talos visible, flujo local y flujo local más compositor con igual evidencia, permisos y presupuesto de herramientas. Separar evaluación retrospectiva de mejoras futuras de Talos que no se pueden ejecutar aquí. Si no existe acceso al sistema, comparar salidas archivadas y declarar la asimetría.

Agrupar los tickets del mismo incidente en la misma partición para evitar que una solución de un caso hermano filtre la respuesta a la evaluación. Separar clasificación, diagnóstico, comunicación y seguimiento. Medir afirmaciones sin respaldo, precedentes pertinentes utilizados, elección de pruebas discriminantes, preguntas evitables, tiempo activo humano y demora desde evidencia contradictoria hasta corrección. Revisión ciega por dos ingenieros con adjudicación de discrepancias.

Las 15 etiquetas observadas de Talos son 12 medium y 3 high. No son probabilidades calibradas. Esta muestra no permite estimar una tasa general de exactitud ni horas ahorradas. Tampoco el hit-rate@5 local de 48/101 demuestra exactitud de respuestas: ESTADO.md lo define como presencia de un ancla en recuperación, con 53 preguntas sin esa ancla entre los cinco primeros resultados.

Prioridad recomendada: identidad, sustitución de afirmaciones y visibilidad antes de ampliar el índice o cambiar de modelo. Son fallos observados que ya cambian decisiones. La actualización de pesos del LLM no forma parte del flujo documentado; la mejora propuesta procede del contexto recuperado, las comprobaciones y el control de afirmaciones.
