# Backlog sin asignar, 15 octubre 2026, 14:25 Bogotá
Consulta Jira: project = RCS AND assignee is EMPTY AND statusCategory != Done. Devuelve 3, isLast=true. No se verificó la definición exacta de la cola visual custom/82. Dos están Under Support Review y uno Under Customer Review. No aparece un cuarto abierto sin asignar. RCS-29450 ya tiene a Diego y pasó a Under Customer Review durante esta revisión; no prueba que fuera el cuarto visto por Juan.

Reparto propuesto, sin ejecutar
Juan: RCS-29452 Big 5. El más acotado y con precedente del mismo cliente. La solución previa tiene evidencia publicada del lado soporte; el cliente aún no confirmó cierre. Falta confirmar campo y procedimiento.
Diego: RCS-29448 Sainsbury’s. Validación de recibo con muestra definida, decisiones de negocio y acceso a Test pendientes. Coordinar con Shaun Callow.
Edwin: RCS-29449 DSW Engage. Investigación de alimentación y mapeo, sin solución confirmada.

Carga Jira actual, todas las páginas recibidas
Persona | Abiertos | Espera cliente | Otros estados
Diego Buelvas | 14 | 12 | 2
Sebastian Garces | 12 | 7 | 5
Edwin Garzon | 13 | 8 | 5
Luis Hernandez | 17 | 14 | 3
Sebastian Rueda | 17 | 5 | 12
Otros estados no equivale a trabajo activo inmediato: incluye esperas internas y release. Luis y Rueda superan el techo operativo de 16 recogido en bin/asignar.py. No recomendar más para ellos. Garces queda como alternativa si Diego carece de acceso a Test.

Consultar los tres entregables individuales de triage-backlog de hoy. Fuentes: Jira en vivo y roster brain/memoria/project_appriss_support_team.md. Jira permanece solo lectura. No hay borradores pegables nuevos ni borradores pendientes invalidados identificados para estos tres tickets.

Siguiente paso
Edwin: obtener para Juan el procedimiento y pantalla usados en RCS-29049, incluidos caché y verificación posterior.
Shaun Callow y Diego: confirmar acceso a Test y quién valida implicaciones de alertas y ProductStop.
Valerie Cerezo y Edwin: confirmar Engage ID DSW y un SKU con descripción esperada.
