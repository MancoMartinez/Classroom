# Ajuste del rol de Lead: matriz, JR y Camila. 5 oct 2026

Fuentes: Support Role Matrix.xlsx (hojas Team Charter, Support Engineering columna Lead, Data Engineering, SRE), inbox/2026-10-02-reunion-jr-camila-resumen.md y su transcripción, inbox/2026-08-18-brief-reunion-adusa.md, brain/memoria/project_appriss_support_team.md. La transcripción es automática y tiene nombres mal escritos. Lo que dicen JR y Camila sobre terceros es su relato, no una observación independiente.

## Diagnóstico

Hoy trabajas como tech lead: asignas, tomas los tickets más complejos y ayudas cuando te piden. La columna Lead de la matriz y JR piden otro rol. Tú respondes por el desempeño y la cultura del equipo, y repartes el tiempo en 50% tickets y 50% gestión. El ajuste central: asigna, supervisa y desbloquea. Toma un ticket propio solo cuando nadie más del equipo puede resolverlo, y deja escrito por qué.

## Lo que la matriz ya te exige (columna Lead)

| Fila | Texto de la matriz | Qué implica desde la reunión |
|---|---|---|
| Ownership, D14 | Responsable del desempeño, la salud y la cultura de todo el equipo L2 | JR: cuando el equipo falla, falla el lead |
| Mentorship, D17 | Feedback estructurado, sesiones de transferencia de conocimiento, desarrollo deliberado | Busca la respuesta que el equipo no encuentra y documéntala |
| Communication, D16 | Maneja expectativas con Product, Business e Infra y traduce complejidad técnica a impacto de negocio | Transmite al equipo qué clientes escalan rápido y cuáles son críticos |
| Pressure, D15 | Guía al equipo en incidentes de alta severidad sin crear pánico | Check-ins en críticos hasta recuperar confianza |
| Problem-solving, D13 | Dirección técnica y resolución de desacuerdos | Respaldo explícito de JR cuando alguien no sigue tus instrucciones |
| .NET D9 y React D10 | Revisa los fixes del equipo y es dueño del code review | Tu trabajo técnico principal es revisar, no resolver |
| AI, D18 | Fija el estándar de uso de IA y exige al equipo aplicarlo | JR: la IA apoya, no reemplaza el troubleshooting |
| DevOps, D11 | Dueño del manejo de incidentes de despliegue y enlace con DevOps | Mantén el enlace, delega la ejecución |

La matriz ya trae el patrón de lo que falló el 1 oct. Fullstack B14 y Sr. Data Engineer C13 piden comunicar progreso sin que nadie lo pida. Cita esas filas en los one-on-ones. Convierten el feedback en un criterio escrito y quitan lo personal.

## Brechas entre tu rutina y lo esperado

| Hoy | Esperado | Ajuste |
|---|---|---|
| Tomas lo complejo | Asignar y supervisar | Delega el ticket complejo con contexto y revísalo. Si lo tomas tú, escribe en la bitácora por qué nadie más podía |
| Asignas por carga | Asignas por capa y criticidad | Cruza el ticket con la matriz. LPMS, .NET y React van a fullstack. SQL profundo, pipelines y Snowflake van a data. Infra va a SRE |
| Ayudas cuando te piden | Revisión diaria de la cola del equipo | Bloquea tiempo fijo en el calendario |
| El contexto de cliente vive en tu cabeza | El equipo sabe qué cliente escala | Escribe un mapa de criticidad |
| Disponibilidad implícita | Avisas cuando no estás | Nombra un respaldo (Viraj o Camila) y avísales antes |
| Instrucciones sin seguimiento | Autoridad de manager de facto | Verifica cumplimiento y escala a Camila o JR cuando falle dos veces |

La asignación fuera de capa merece atención propia. Camila describió a Sebastian Rueda como data engineer con una brecha en LPMS. La matriz define a Data Engineering con Snowflake, SQL Server y pipelines, y a Fullstack con .NET, React y DevOps. Si asignas un crítico fuera de capa, nombra en el mensaje a un compañero de fullstack como pareja.

## Rutina diaria propuesta

Inicio del turno, 30 a 45 minutos. Abre la cola del equipo con cerebro-cola y cerebro-asignacion. Busca tickets sin dueño activo, SLA corriendo y críticos sin comentario al cliente. Asigna con el mensaje de contexto de abajo.

Mediodía. Haz check-in en cada crítico. Pregunta qué evidencia hay (logs, base de datos, reproducción) y cuándo toca el siguiente comentario al cliente. Si el ticket tiene a un líder en el hilo, el intervalo baja a 15 minutos hasta que haya comentario al cliente y avance verificable.

Antes de que el equipo cierre su turno. Confirma que cada crítico tiene dueño que sigue disponible o un relevo nombrado. Este chequeo habría evitado el caso del 1 oct, donde nadie supo a tiempo que el ticket no tenía dueño.

Semanal. One-on-one por persona con la matriz como criterio. Sesión corta de transferencia de conocimiento con lo que documentaste esa semana. Reporte semanal que ya tienes comprometido.

Plantilla de asignación para Teams, en inglés y sin formato:

Assigning RCS-XXXXX to you. Customer: NAME. Why it is critical: leader in the thread, escalation history, SLA. Next customer update is due at TIME ET. If you are blocked or have a higher priority, tell me in this thread before TIME and I will reprioritize. Backup: NAME. I will check in at TIME.

Con el equipo directo, JR pidió firmeza. Mantén tu estilo de preguntar para entender, y cierra cada conversación con un compromiso escrito y una fecha.

## Dónde la matriz contradice lo que piden: lleva esto a Camila y JR

1. La columna Lead mezcla tech lead y team lead. D8 a D10 te piden resolver lo más complejo. D14 y D17 y JR te piden gestionar. JR separa los dos roles y ve a Diego como tech lead natural en Colombia. Pregunta a JR cuál es tu columna y si habrá track de tech lead. Propón reescribir D9 y D10 como "reviews and unblocks the most complex production issues".
2. Data Engineering no tiene columna Lead. Viraj es Lead Data Engineer y par tuyo, y la matriz no lo refleja.
3. El charter pone "Small Enhancements that change product behavior or scope" dentro del alcance y "Stay in your lane on features" como principio. Pide una frase que trace la línea.
4. La descripción de Support Engineering dice "first-line technical responder". El charter lo llama L2 y deja el triage a L1. Data Engineering menciona "L3 incidents". Alinea los niveles con el modelo de Confluence: L1 triage, L2 Support, L3 Engineering y Delivery.
5. El charter exige cero bugs hacia Product Engineering y fix en código local. La guía de escalación L3 de Confluence manda los bugs de código a Engineering. Pide criterio explícito de cuándo un bug sube.
6. Las métricas no miden comunicación. Falló la comunicación. Propón tres: tiempo hasta el primer comentario al cliente en críticos, tickets sin dueño activo por más de un turno, y tickets que el lead resuelve frente a tickets que revisa. Define los umbrales con Camila.
7. El charter no incluye la regla de urgencia de Camila: un líder en el hilo, o una asignación de Juan, Camila o Viraj, es prioridad, y el conflicto se sube levantando la mano. Agrégala a Operating Principles.
8. D18 y JR chocan en el tono sobre IA. Agrega un principio: toda entrada en Confluence o Jira generada con IA lleva la evidencia de logs, base de datos y reproducción que la respalda.
9. Typos para corregir: "Jon title", "L3incidents", "Terraformtemplates".

## Mapa de criticidad de clientes (por construir)

JR pide que transmitas al equipo qué clientes escalan rápido. Arma una tabla con cliente, contacto que escala, historial de escalaciones, tickets abiertos y quién del equipo lo conoce. Arranca con Jim (historial de Smart Alerts y unificación) y los clientes que Camila mencionó. Toma los datos de las fichas en tickets/ y verifica el estado en Jira antes de escribir nada.

## Esta semana

1. Bloquea el espacio diario de revisión de cola en tu calendario.
2. Envía la plantilla de asignación al equipo y úsala en cada crítico.
3. Pregunta a JR por la columna Lead frente al tech lead.
4. Acuerda con Viraj o Camila quién te cubre cuando no estés.
5. Prepara el one-on-one con la matriz como criterio.
6. Construye el mapa de criticidad de clientes.
