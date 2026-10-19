---
name: feedback_agrupar_no_es_causa_raiz
description: Agrupar tickets por metadata de intake no autoriza a afirmar que comparten causa raíz; verificar comentarios antes de pasarle un patrón a otra persona
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 3f56fb32-9062-4251-8c49-5c2b2da4c07c
  modified: 2026-08-06T20:34:48.802Z
---

En el triage del 3 ago 2026 los 5 tickets de Chemist Warehouse quedaron en un solo grupo (G1) con la frase *"los cinco son iguales por dentro"*. Esa agrupación era por **metadata de intake**: mismo reporter interno (James McKenna), label `clientproject`, título "CWH - HYP to RCS", prioridad sin poner, y todos preguntas de descubrimiento de datos. No era por causa raíz.

El 5 ago Juan le pasó esa agrupación a Edwin Garzón como si fuera técnica: *"RCS-28100 de till openings es el mismo patrón, revisaría si es otro ActivityID que el loader no consume"*. Era falso. RCS-28100 ya tenía dos comentarios de Ruchi Vora (29 y 31 jul) diciendo que el dato **falta en la fuente del cliente**, que está en `Under Customer Review` y asignado a Viraj Kansara. Nada que ver con el loader ni con ActivityID. Edwin perdió tiempo y lo devolvió con un *"según Claude está a la espera de información del cliente"*.

**Why:** un grupo de triage sirve para repartir trabajo, no para diagnosticar. Cuando ese grupo sale del documento y se le entrega a un compañero como pista técnica, se convierte en una afirmación de causa raíz que nadie verificó.

**How to apply:** antes de decirle a alguien "es el mismo patrón que X", leer los comentarios de X. Si el ticket ya tiene status o comentarios que contradigan la hipótesis, eso manda sobre cualquier agrupación previa. Y en los documentos de triage, marcar explícito qué agrupa por metadata y qué por causa raíz verificada.

Ver [[project_backlog_triage_2026_08_03]], [[reference_ficha_clientes_onboarding]], [[feedback_comentarios_reglas]].
