---
name: feedback_comentarios_reglas
description: "Todo comentario de Jira y todo análisis de asignación se redacta ya cumpliendo el skill appriss-jira-support, sin que Juan lo pida"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f3876df8-4a71-4754-9550-62264ecd309a
  modified: 2026-08-11T16:25:12.396Z
---

Juan no debe tener que pedir en cada turno que los comentarios cumplan las reglas. **Se aplican por defecto, siempre, desde el primer borrador.**

Checklist obligatorio antes de mostrar cualquier comentario:

- **Cliente**: neutral, conciso, orientado a la solución. Sin nombres de empleados internos, sin nombres de equipos internos que el cliente no haya visto ya en ese mismo ticket, sin mencionar on-call, sin mencionar problemas de otros clientes.
- **Cliente = CERO detalle técnico.** No se mencionan queries, planes de ejecución, Cloudflare, códigos de error, timeouts de aplicación, nombres de infraestructura, ni qué está haciendo ingeniería por dentro. Se dice qué se probó y qué resultado dio, en lenguaje de usuario. Si hace falta pedir datos, se pide directo: "ya que el error persiste, puedes compartirme los siguientes datos para validar". Nada de explicar el porqué del pedido. Un comentario de cliente bien hecho cabe en pantalla sin scroll. Todo lo técnico va al comentario interno.
- **Interno**: directo, técnico, corto. Ahí sí se nombra gente y equipos.
- **Hechos y solo hechos.** Lo que sea interpretación va marcado como interpretación en el propio texto. Si no se sabe, se dice que no se sabe.
- **Nunca** determinaciones de LP ni atribución de culpa a tienda o empleado.
- **Nada de guiones** como conector, ni em dash. Comas y puntos.
- **Teams**: un párrafo, corto y directo. No repetirle a la persona las instrucciones que ella acaba de dar.
- **No afirmar un resultado que Juan aún no ha verificado.** Si el comentario depende de correr una consulta, avisarlo arriba del borrador.
- **Client ID en el comentario interno, siempre.** Kiran lo pidió expresamente en la llamada del 3 ago 2026 y se lo propuso a Matt como obligatorio: *"if you know say Adusa Delhaize, I have to go to the Excel sheet, find out their client ID 420 and then go to 420"*. Las bases de datos ya no llevan nombre de compañía, solo número de cliente. Juan ya lo venía haciendo y Kiran lo felicitó por eso.
- **Antes de escalar o investigar un reporte funcional, pedir el caso concreto.** Kiran: *"can you please give us the URL of the incident you're trying, the link to the workbench. All we need is this."* URL, usuario y captura. Sin eso se pierden horas reproduciendo a ciegas, y así pasó con RCS-28093.
- **El hallazgo interno nunca se le cuenta al cliente, ni siquiera en resumen.** La forma correcta del comentario de cliente cuando se necesita evidencia es literal: saludo, "based on what we have so far we need a bit more to keep moving", la lista de lo que se pide, gracias. Punto. Juan lo dijo así: *"solo necesito que lo saludes, le digas que en base a la informacion necesitamos lo siguiente para tener mas evidencia y avanzar con el caso"*.
- **Nada se escribe en Jira.** Yo redacto, Juan pega. Ver [[feedback_jira_read_only]].

**Why:** cada vez que se salta el checklist, Juan tiene que devolver el trabajo, y ya pasó con clientes reales (se filtraron problemas de otros clientes en un comentario de Big Y, se nombró a J.R. en un comentario de cliente, se afirmaron cosas que eran interpretación). El 10 ago 2026, en RCS-28256, el borrador al cliente llevaba el 524 de Cloudflare, la regresión de planes y el CommandTimeout. Ese mismo día, en RCS-28032, el borrador le explicaba al cliente que su usuaria era la única configurada en dos distritos y que solo uno tomaba efecto: eso es análisis interno y Juan lo devolvió por segunda vez en el día.

**How to apply:** antes de mostrar el borrador, correr el checklist mentalmente y decir en una línea qué se verificó. Lo mismo aplica al análisis de asignación de tickets: el equipo se toma de [[project_appriss_support_team]], nunca se deduce de quién aparece como asignatario en Jira.
