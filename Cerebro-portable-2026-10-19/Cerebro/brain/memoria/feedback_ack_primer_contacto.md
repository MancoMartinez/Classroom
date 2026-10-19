---
name: feedback_ack_primer_contacto
description: "Un acuse de primer contacto son 3 o 4 frases sin nada técnico; y hay que releer la skill appriss-jira-support antes de escribir, no citarla de memoria"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a8293f75-ab64-479b-971f-f586abf0f63b
  modified: 2026-08-12T22:05:36.320Z
---

**Un acuse de primer contacto lleva tres cosas y nada más:** quién soy, que ya lo estoy revisando, y que vuelvo con novedades. Tres o cuatro frases. Cierra con nombre y `Appriss Retail Support`.

**Lo que NO lleva un acuse:** hallazgos, causas, lo que vi por dentro, nombres de campo, URLs, códigos de error, ni preguntas de alcance. Las preguntas al cliente van **después** de correr las verificaciones propias, nunca en el primer mensaje ([[feedback_borradores_al_final]]).

**Por qué:** en RCS-28327 y RCS-28342, el 12 de agosto de 2026, Juan pidió acuses básicos de presentación y le entregué dos mensajes largos con hallazgos técnicos y preguntas de scoping. Es un error que ya había cometido en el mismo día con RCS-28033 y con Nikita. Su reclamo textual: *"siempre siempre hacer lo mismo... jamás consultas"*.

**La causa real del error:** cargué la skill `appriss-jira-support` al inicio de la sesión y después escribí de memoria en vez de volver a leerla. La memoria de la skill se degrada; el archivo no.

**Cómo aplicarlo:** antes de redactar cualquier comentario de Jira, releer la sección de tono y la estructura del tipo de comentario en `appriss-jira-support`. Contar las frases antes de entregar. Si un acuse pasa de cuatro, está mal.

Ojo con la confusión de skills: `appriss-hr-question` es la de recursos humanos y no sirve para esto. La que gobierna comentarios, notas internas, Teams y escalaciones es **`appriss-jira-support`**.

Relacionado: [[feedback_comentarios_reglas]], [[feedback_estilo_mensajes]], [[feedback_borradores_al_final]].
