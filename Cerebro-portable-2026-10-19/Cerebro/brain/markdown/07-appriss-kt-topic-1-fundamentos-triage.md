# Appriss KT — Topic 1: Fundamentos & Triage

Carpeta 7 de la base de Moscú. 105 fragmentos.

## Topic 1 · KB Support Operations — Cierre
_chunk 170 · 2026-06-03 · fuente: /Users/MancoMenStudio/Desktop/Topic1_Support_Operations_KB.html_

· Preguntas pendientes KT
Topic 1 · Master Reference
Appriss Retail Support — Operating Knowledge Base
Todo lo que necesitas para operar dentro de la función de Support: quién es quién, cómo fluye un ticket desde que entra hasta que cierra, cómo se disputan los retornos de consumidores, cómo se cargan los datos de los clientes y dónde vive cada recurso. Este documento es tu base de aprendizaje — no un resumen — diseñado para darte contexto y guía.
Alcance · Customer Support (B2B) + Consumer Support (B2C)
Acceso · Todos los links internos requieren VPN
Relacionado · Topic 3 — RCS Ticket Flows
▦

## Reunión 2026-06-09 — Support team technical elevation
_chunk 284 · 2026-06-09_

## Resumen
The meeting was primarily an informal introduction and alignment on expectations. Key points discussed include the current non-technical nature of the support team under JR, which escalates issues directly to engineering or delivery without attempting resolution. The new role aims to elevate the technical capabilities of the team to handle tickets directly, including writing unit tests, raising PRs, and fixing issues. The technology stack includes Snowflake, DBT, React, and SQL Server, which are essential for effective problem-solving. A 'technology all hands' presentation is planned to refresh knowledge about apps and engineering teams. Additionally, there is a tentative plan for a visit to Bogotá in July, pending approval. Deadlines for migrating from Greenplum to Snowflake and closing data centers in LA and Irvine were highlighted, with a target completion by the end of the year. Questions remain about specific metrics for success and the structure of the 'technology all hands' presentation.

## Temas clave
- Support team technical elevation
- Technology stack mastery
- Greenplum migration deadlines

## Decisiones
- **Elevate technical capabilities of the support team to handle tickets directly.** — Current team escalates issues without resolution.
- **Migrate from Greenplum to Snowflake and close data centers by end of year.** — Cost efficiency and technology consolidation.

## Tareas / Action Items
- Prepare for 'technology all hands' presentation, focusing on apps and engineering teams.
- Coordinate approval and logistics for Bogotá visit in July.
- Plan migration from Greenplum to Snowflake and closure of LA/Irvine data centers. — vence 2026-12-31

## Insights en vivo (Ask AI / Analizar)
### [Ask AI] tienes algo que aportar de valor a este meet?
Lo que entiendo es que este encuentro fue más una introducción informal que una sesión técnica. Me explicaron que el equipo de soporte actual bajo JR no tiene un enfoque técnico; cuando reciben problemas, simplemente los escalan a ingeniería o delivery sin intentar resolverlos. La idea detrás de mi rol es cambiar eso, elevar el nivel técnico del equipo para que podamos abordar los tickets directamente, escribir pruebas unitarias, levantar PRs y resolver problemas sin depender tanto de otros equipos. También mencionaron que habrá una presentación general de las aplicaciones y los equipos de ingeniería en un "technology all hands" para refrescar el conocimiento de todos. Además, parece que hay planes para que nos visiten en Bogotá en julio, lo cual podría ser una oportunidad para fortalecer la relación y discutir más a fondo los procesos.

- **Puntos clave**:  
  - El equipo de soporte actual bajo JR no es técnico y escala problemas directamente a otros equipos.  
  - Mi rol busca elevar el nivel técnico del equipo para resolver tickets directamente, incluyendo escribir pruebas unitarias y levantar PRs.  
  - Habrá una presentación general en un "technology all hands" sobre las aplicaciones y equipos de ingeniería.  
  - Planes para una visita a Bogotá en julio, pendiente de aprobación.  

- **Dudas / lo que falta**:  
  - No quedó claro si el "technology all hands" incluirá detalles específicos sobre los procesos de soporte o si será más general.  
  - No se mencionaron ejemplos concretos de cómo esperan que el equipo técnico maneje los tickets en comparación con el enfoque actual.  

- **Próxima pregunta a hacer**:  
  - ¿Qué expectativas específicas tienen para el equipo técnico en términos de métricas o resultados al manejar tickets directamente?  

- **Conexión con tu documentación**:  
  - Esto se conecta con el T-007 (Ticket lifecycle ownership map) y T-006 (Eng escalation packaging), ya que el cambio de enfoque técnico impactará directamente cómo se manejan las transiciones entre soporte e ingeniería.

### [Ask AI] tienes algo que aportar de valor a este meet? responde en ingles
What I understand is that this meeting was more of a casual introduction rather than a technical session. The person explained that the current support team under JR is not technical; they receive issues and immediately escalate them to engineering or delivery without attempting to resolve them. My role is intended to change that dynamic by raising the technical bar—handling tickets directly, writing unit tests, raising PRs, and fixing issues instead of simply passing them along. They also mentioned that there will be a "technology all hands" presentation soon, where all apps and engineering teams will be introduced or refreshed for everyone. Additionally, they are planning a visit to Bogotá in July, pending approval, which could be an opportunity to connect further and discuss processes in more depth.

- **Puntos clave**:  
  - Current support team under JR is non-technical and escalates issues directly to other teams.  
  - My role is to elevate the technical capabilities of the team to handle tickets directly, including writing unit tests and fixing code issues.  
  - A "technology all hands" presentation is planned to introduce or refresh knowledge about apps and engineering teams.  
  - A visit to Bogotá is tentatively scheduled for July, pending approval.  

- **Dudas / lo que falta**:  
  - No specifics were provided about the content or structure of the "technology all hands" presentation.  
  - It’s unclear what metrics or expectations will be used to measure the success of the technical approach for handling tickets.  

- **Próxima pregunta a hacer**:  
  - What specific challenges or gaps have been identified in the current support process that we should prioritize addressing?  

- **Conexión con tu documentación**:  
  - This aligns with the broader goal of transitioning to a more technical support model, which connects to topics like T-006 (Eng escalation packaging) and T-008 (Done definitions per ticket type).

### [Ask AI] tienes algo que aportar de valor a este meet? responde en ingles, aporta un punto de valor en base a lo que sabemos
What I understand is that this meeting was primarily a casual introduction and a chance to align on expectations. The current support team under JR is non-technical; they receive issues and immediately escalate them to engineering or delivery without attempting to resolve them. My role is to change that dynamic by raising the technical bar—handling tickets directly, writing unit tests, raising PRs, and fixing issues instead of simply passing them along. This includes understanding the full stack: Snowflake for data, DBT for transformations, React for UIs, and SQL Server for databases. Additionally, there’s a planned "technology all hands" presentation to refresh everyone’s knowledge about the apps and engineering teams, and a visit to Bogotá in July, pending approval, which could be an opportunity to connect further and discuss processes in depth.

- **Puntos clave**:  
  - Current support team under JR escalates issues directly without technical intervention.  
  - My role is to elevate the technical capabilities of the team to handle tickets directly, including writing unit tests and fixing code issues.  
  - The stack includes Snowflake, DBT, React, and SQL Server, which I need to master for effective problem-solving.  
  - A "technology all hands" presentation is planned to introduce or refresh knowledge about apps and engineering teams.  
  - A visit to Bogotá is tentatively scheduled for July, pending approval.  

- **Dudas / lo que falta**:  
  - No specifics were provided about the content or structure of the "technology all hands" presentation.  
  - It’s unclear what metrics or expectations will be used to measure the success of the technical approach for handling tickets.  

- **Próxima pregunta a hacer**:  
  - What specific challenges or gaps have been identified in the current support process that we should prioritize addressing?  

- **Conexión con tu documentación**:  
  - This aligns with the broader goal of transitioning to a more technical support model, as outlined in T-006 (Eng escalation packaging) and T-007 (Ticket lifecycle ownership map). Understanding the stack also connects directly to T-017 (pyARDM code architecture) and T-021 (Snowflake deployments runbook).


---

## Transcripción completa
Hi, Juan. I'm good, thank you. Thank you. How are you? Good to meet you. Thank you, and last. Thanks for taking the time to chat. I know you've been You've been around a little bit and you're getting yourself settled in, but just thought I'd take some time to say Time to say hi and meet and greet and see how things are going for you, really. Yeah, there's so much to learn. I appreciate it. Appreciate it takes a long time to get up to speed and there's loads of domain knowledge and also All sorts of stuff like that. So yeah, it takes a while. We are... We are going to do a presentation. We'll do a technology all hands, and we're going And we're going to do like a presentation of all the apps, the engineering orgs and stuff. Again, with everybody as a reminder, you know? Okay, yeah, so we need to do introductions. We're going to go back to the next slide. Who are blue team? What do they do? You know, and the various engineers and stuff like that. Stuff like that. Yeah, absolutely. Yeah, of course, yeah. Of course, yeah, it'll take time, it'll take time. So, do you live in Bogota? So I'm scheduled to come out and visit you guys in July. Yeah, so once we get approval, I'll say I'll send all you guys the dates and I'll come out there and hopefully we can Hopefully we can hang out, get someone to eat, and just sort of spend some time together. Cool means, cool means. So how's the process? Did JR talk to you about what we're looking for in terms of I think it's a bit of a challenge for the people who are in the industry. The reason why I'm here is because I'm dealing with support issues and stuff. Okay, I'll take you through it so just So today, the support team under The team under JR, the team that are going away, they're not technical They'll get issues coming in and up. And now have a look at it and go, I can't touch the code, I'll just throw it. Just throw it over the fence to engineering or delivery or somebody else. else you know but we want to raise the You raise the bar to have technical people like you running those teams, so a ticket comes in. I'm going to go back to the beginning of the day. Write some unit tests, raise a PR, and fix it without just throwing Just throwing all these tickets around. Yeah, so you will be doing that. Of course, the... The first job is to make sure everything's running and perfect. We have to deal with that issue. A lot of the time that's going to be making code changes, fixing issues. And then, we can use the application issues to resolve the problems. The problems for support. So like, day two, Data loading into Snowflake, understanding DBT, understanding Snowflake. The URL is the URL that you can find on the website. The UIs are all in React, so understand in React. Our databases are Microsoft SQL Server, so understanding SQL Server, all that. All that technology stack. Yeah, exactly. Yeah, we're trying to get We're trying to get rid of Greenplum. So we've got two types. We've got Greenplum hosted in I'm hosted in Azure, it's really expensive, and we've got green plums. We've been working on a lot of these things. That's going away and we're just going to use Snowflake. Yeah, yeah, yeah, I get it. I get it. It's crazy. I got it, great. Is JL got you working with anybody? Are you shadowing or buddying anybody? With Amy, okay, great, right. Okay, yeah, because it only has a lot of the knowledge, so that's good. So that's good. And I met Camilla for the first time. Time a few weeks ago. She seems really good. You've been working with Kamila. Awesome. Great stuff. Great stuff. Is there any question? Any questions I can answer for you? Anything I can help with? Anything you'd like to know? The Green Plum license is up at the end of the day. At the end of this year, no more No more green plumps, so we need to do all the migrations before then. We need to close down all the data centers before then because we've got So we've got like physical servers in data centers in LA and Irvine. So the migrations have to be done before that, so we've got time to go in there. Go in there and rip all the hardware out. That's our, there are big deadlines like Project Snowtime and I've got to be done by October. October, September, October sort of time. And so the data load that goes into Greenplum Inplan was all written in Python and that's what the People in the US were managing and as they leave the If we leave the business, the new team coming on should Should be working on the new mapping, which is down in dbt into Snowflake. As you and your team ramp up, you'll be looking after Snowflake and With the old team ramped down, so will Green Plum and And Python and those sort of technologies. So as you're coming up, they're coming down. They're coming down, and by the end of the year, it will be done. You do, what, like, Like you own it, you own, you're a leader in the group, so we expect you to own it. You can do whatever you think is necessary. And that's a really important point about Appress Resale. Everybody is expected to take ownership and have initiative and You can do that. You don't have to be hands-off or worry about management. Management or anything like that, it's go get it, you know, we're all in it together. Do I do that? Yeah, exactly. Yeah, so we have a product management group now, they're quite new. Quite new, they've only been in the business like six months, maybe, maybe a bit longer. And they're now looking at the industry, talking to customers, deciding And then they bring it to us and say, right, this is what we're doing. This is what we want and then we have to build it. That's a collaboration between engineering and QA. You can have all these things in your own way. All these different, you think of it as like the, I don't know if you've heard of the spot The Spotify model where you have verticals like app developers, We are all developers, QA developers, infrastructure developers, and in projects, right? It's not a big deal. We put a project together. We'll put that project together with all the right people in and then they go and deliver that project. Yeah, exactly, it's important. It's important to meet people, yeah. Is there anything else you want to know? If you want to know, anything I can help with. Yeah, yeah, I appreciate it. Thanks for taking the time. If you have any questions, If you have any questions, just chat to me on Teams, just reach out. I'm always available. Just ping me whenever you want. All right, appreciate your time. OK, it's on. Have a good day.

## Reunión 2026-07-30 — User login issues · Resumen
_chunk 1412 · 2026-07-30_

## Resumen
The meeting covered multiple technical and operational issues across various tickets. One key discussion involved a user named Eric who had never logged into his account, with investigations ongoing regarding the use of a global ID. Another ticket addressed performance issues in the Isenda system, which are currently under investigation. Additionally, a user is experiencing login issues related to non-SSO access parameters, and confirmation is awaited from another user to apply profile changes across all users. The team also discussed timezone configuration problems caused by a recent migration defaulting to UTC, with a temporary fix involving bulk updates for affected users. Further, issues with duplicate store numbers across divisions were highlighted, impacting hierarchy assignments, and engineering is working on a solution. A missing claim in SSO was identified as the cause of a user's inability to access the system, and this has been communicated to the user. Lastly, there was a debate on whether to remove 'Secure Incident Management System' from the email sender name, pending product team review. The meeting concluded with discussions on preparing for similar challenges in the future and ensuring smoother transitions for customers.

## Temas clave
- User login issues
- Isenda system performance
- Timezone configuration errors
- Duplicate store numbers
- SSO claim issues
- Email sender name modification

## Decisiones
- **Bulk update timezone configurations to correct values for affected users.** — Defaulting to UTC caused incorrect settings post-migration.
- **Communicate the missing SSO claim issue to the affected user.** — Ensure the user is informed and can take corrective action.

## Tareas / Action Items
- Investigate the global ID issue for Eric's account and confirm if further assistance is needed.
- Provide updates on the Isenda system performance investigation. (resp: Matt)
- Verify the non-SSO access parameter for the affected user and trace the exact email ID.
- Implement bulk updates to correct timezone configurations for affected users.
- Continue working on the solution for duplicate store numbers across divisions. (resp: Engineering team)
- Follow up with the product team regarding the email sender name modification request.

## Pulsos de la reunión (resúmenes periódicos + hablantes)
### Pulso 10:13
Se discutieron varios tickets relacionados con problemas técnicos y de acceso. Uno de ellos involucra un usuario llamado Eric que nunca inició sesión en su cuenta, y se está investigando el uso del ID global. Otro ticket trata sobre un problema con el sistema Isenda, que parece ser de rendimiento y está siendo investigado. También se mencionó un caso relacionado con un parámetro de acceso no SSO, donde una usuaria sigue teniendo problemas para iniciar sesión. Finalmente, se está esperando confirmación de una usuaria para realizar cambios en su perfil que podrían aplicarse a todos los usuarios.

**Temas:** Problemas de acceso de usuarios · Rendimiento del sistema Isenda · Confirmación de cambios en perfiles

**Sugerencias / preguntas:**
- ¿Podrías aclarar si el problema de rendimiento en Isenda afecta solo a la creación de casos o también a otras funcionalidades?
- ¿Se ha considerado contactar directamente a Eric para confirmar si necesita asistencia adicional con su cuenta?
- ¿Hay un plan para verificar si el parámetro no SSO está configurado correctamente en otros usuarios con problemas similares?

**Hablantes:**
- **Participante 1:** Explicó varios tickets, incluyendo problemas de acceso de usuarios, un caso de rendimiento en Isenda, y la necesidad de confirmación para cambios en perfiles. Mencionó nombres como Eric y Kiran, y describió acciones tomadas como impersonación y ajustes de parámetros.

### Pulso 10:18
Se mencionó que el único tema pendiente relacionado con Isenda es uno específico que será abordado más tarde. Un participante ofreció contactar después de una hora para continuar con el seguimiento. También se sugirió que otra persona sería la mejor opción para resolver un problema específico y podría orientar en la dirección correcta.

**Temas:** pendiente en Isenda · delegación de tareas

**Sugerencias / preguntas:**
- ¿Podrías aclarar cuál es el tema específico pendiente en Isenda para asegurar que todos estén alineados?
- ¿Quién es la persona mencionada como la mejor opción para resolver el problema y cómo se puede contactar?

**Hablantes:**
- **Participante 1:** Indicó que el único tema pendiente relacionado con Isenda será abordado más tarde y ofreció contactar después de una hora para continuar con el seguimiento.
- **Participante 2:** Sugirió que otra persona sería la mejor opción para resolver un problema específico y podría orientar en la dirección correcta.

### Pulso 10:24
Se discutió un problema relacionado con la configuración de zona horaria en los clientes de unificación, donde parece que se está utilizando UTC por defecto tras una migración. Se mencionó que la solución temporal sería realizar una actualización masiva para corregir los valores de todos los usuarios afectados. También se identificaron problemas con el acceso a adjuntos y se mencionó que algunos usuarios no podían iniciar sesión. Se sugirió verificar el código compartido para identificar de dónde se está obteniendo la configuración de zona horaria.

**Temas:** Configuración de zona horaria en clientes · Problemas de acceso a adjuntos y login

**Sugerencias / preguntas:**
- ¿Podrías confirmar si la actualización masiva para corregir los valores de zona horaria incluirá algún mecanismo para evitar que el problema se repita en futuras migraciones?
- Sería útil detallar cómo se planea abordar los problemas de acceso a adjuntos, ya que parece ser un tema distinto al de inicio de sesión.

**Hablantes:**
- **Participante 1:** Mencionó que la configuración de zona horaria está predeterminada a UTC tras la migración y sugirió una actualización masiva como solución temporal.
- **Participante 2:** Indicó que algunos usuarios no podían iniciar sesión y que otros tenían problemas para acceder a adjuntos, diferenciando ambos problemas.

### Pulso 10:29
Se discutieron varios temas técnicos y operativos. Primero, se mencionó que algunos usuarios están utilizando un enlace no-SAML para iniciar sesión con usuario y contraseña en lugar de SSL, lo cual se está revisando. Segundo, se identificó un problema con números de tienda duplicados en diferentes divisiones, lo que afecta la asignación de jerarquías; ingeniería está trabajando en una solución. Tercero, un usuario no puede acceder al sistema debido a una reclamación faltante en su SSO, y ya se comunicó el problema. Por último, se debatió la solicitud de eliminar 'Secure Incident Management System' del nombre del remitente en correos electrónicos, aunque se espera una revisión del equipo de producto antes de tomar una decisión.

**Temas:** Inicio de sesión no-SAML · Números de tienda duplicados · Problema de SSO · Nombre del remitente en correos electrónicos

**Sugerencias / preguntas:**
- ¿Podrían aclarar si el enlace no-SAML será una solución temporal o si se planea implementarlo como una opción permanente para ciertos usuarios?
- ¿Se ha considerado cómo los números de tienda duplicados podrían afectar otros sistemas relacionados con la jerarquía de divisiones?
- ¿Hay un plan para comunicar a los usuarios afectados por el cambio en el nombre del remitente de correos electrónicos, en caso de que se apruebe la modificación?

**Hablantes:**
- **Participante 1:** Mencionó que algunos usuarios están utilizando un enlace no-SAML para iniciar sesión con usuario y contraseña en lugar de SSL. También habló sobre problemas con números de tienda duplicados en divisiones y cómo esto afecta la asignación de jerarquías. Indicó que ingeniería está trabajando en una solución. Además, mencionó un problema de SSO que ya fue comunicado al usuario afectado. Finalmente, discutió la solicitud de modificar el nombre del remitente en correos electrónicos, aunque se espera una revisión del equipo de producto.

### Pulso 10:34
Se discutió un problema relacionado con la configuración de zonas horarias en la plataforma. Se identificó que algunos usuarios tienen configurada una zona horaria incorrecta (KT en lugar de EST) debido a un cambio reciente en la plataforma. Se propuso forzar a los usuarios a establecer manualmente su zona horaria en el próximo inicio de sesión, lo que podría requerir un cambio de código. También se mencionó que algunos usuarios no pueden crear casos debido a restricciones por división, y se identificó un problema con el componente Isenda que podría ser difícil de resolver. Finalmente, se señaló que algunos clientes han ignorado solicitudes previas, lo que ha generado problemas más grandes de lo esperado, con un objetivo de resolución para finales de septiembre.

**Temas:** Configuración de zonas horarias · Restricciones por división en creación de casos · Problemas con el componente Isenda · Clientes que ignoran solicitudes previas

**Sugerencias / preguntas:**
- ¿Se ha considerado implementar un mecanismo para detectar automáticamente la zona horaria del usuario en lugar de forzar una selección manual en el próximo inicio de sesión?
- ¿Qué pasos específicos se están tomando para resolver el problema con el componente Isenda, dado que parece ser el más complejo?
- ¿Hay algún plan para abordar de manera más efectiva a los clientes que han ignorado solicitudes previas, para evitar problemas similares en el futuro?

**Hablantes:**
- **Participante 1:** Explicó el problema de las zonas horarias incorrectas y sugirió forzar a los usuarios a establecer su zona horaria manualmente en el próximo inicio de sesión, lo que podría requerir un cambio de código. También mencionó que algunos usuarios no pueden crear casos debido a restricciones por división y que el componente Isenda presenta un problema complejo. Señaló que algunos clientes han ignorado solicitudes previas, lo que ha generado problemas más grandes de lo esperado.


---

## Topic 1 · KB Support Operations — Mapa del Topic 1 — cómo leer este documento
_chunk 171 · 2026-06-03 · fuente: /Users/MancoMenStudio/Desktop/Topic1_Support_Operations_KB.html_

El objetivo formal del Topic 1 son cuatro entregables. Este documento los cubre y añade la profundidad operativa para que realmente entiendas el porqué de cada cosa.
🎯
El objetivo del Topic 1 fue: "Master roster + key dashboards + on-call schedule + Confluence links." Esos cuatro pilares son la columna vertebral. Pero el documento "Support" de Confluence —el punto único de referencia de la función— conecta esos pilares con todos los procesos operativos. Por eso aquí los pilares son la base y los módulos de proceso son la carne.
🧑‍🤝‍🧑
Pilar 1 · Master Roster
Quién compone Support, sus fortalezas, ubicación y especialidad por producto.
→ Módulos 01–03
📊
Pilar 2 · Key Dashboards
Los tableros de Jira que revisas a diario y las métricas de SLA que importan.
→ Módulo 14
📞
Pilar 3 · On-call Schedule
Quién está de guardia, cómo se cubre el horario y cuándo escalar por OpsGenie.
→ Módulo 15
🔗
Pilar 4 · Confluence Links
El directorio completo de wikis, portales, SharePoint y herramientas.
→ Módulos 16–17
🧭
Convención de etiquetas: cada módulo lleva chips que indican a qué pilar del Topic 1 contribuye ( Roster Dashboards On-call Recursos ) y Proceso core para el conocimiento operativo de fondo.
Aa

## Topic 1 · KB Support Operations — Glosario esencial — léelo primero
_chunk 172 · 2026-06-03 · fuente: /Users/MancoMenStudio/Desktop/Topic1_Support_Operations_KB.html_

Estos términos aparecen en todo el documento. Tenerlos claros desde el inicio acelera todo lo demás.
RCS Retail Customer Support — el proyecto Jira de soporte B2B y el prefijo de sus tickets ( RCS-##### ).
RTS Retail Tenant Support — proyecto Jira asociado a alertas de infraestructura/data (ej. errores de GreenPlum).
L1 / L2 / L3 Niveles de soporte: L1 triage y primera respuesta · L2 investigación y resolución · L3 Engineering / Delivery.
EBR Enterprise Business Reporting — la plataforma reporting de Secure que usan los clientes.
CRM Herramienta custom (returnx.com / "Incident Search") para procesar disputes de consumidores.
BRTD Business Requirements doc — base para una estimación SOW.
SOW Statement of Work — estimación formal de trabajo billable, liderada por el CSM.
CSM Customer Success Manager — dueño de la relación comercial y de los change requests.
GreenPlum (GP) Base de datos analítica donde se cargan los datos de los clientes. Clusters GP1–GP11.
pyARDM Wrapper de Python que orquesta la carga de datos en el pipeline de DataOps.
RAR Return Activity Report — reporte que un consumidor puede pedir; NO es un dispute.
OpsGenie Herramienta de alertas/on-call para escalar a equipos de Engineering.
01

## Topic 1 · KB Support Operations — La estructura de Support
_chunk 173 · 2026-06-03 · fuente: /Users/MancoMenStudio/Desktop/Topic1_Support_Operations_KB.html_

Dos funciones distintas bajo el mismo paraguas: B2B (clientes retail) y B2C (consumidores finales).
Roster Proceso core
Appriss Retail Support se divide en dos mundos que es crucial no confundir. Customer Support atiende a las empresas retail que compran nuestros productos (TJX, Walmart, Home Depot…). Consumer Support atiende a los consumidores finales cuyo retorno fue negado en una tienda y quieren disputarlo.
Diagrama 1 · Organización de la función de Support
flowchart TD
ARS["APPRISS RETAIL SUPPORT"]:::root
ARS --> CS["CUSTOMER SUPPORT
(B2B · clientes retail)"]:::b2b
ARS --> CO["CONSUMER SUPPORT
(B2C · consumidores finales)"]:::b2c
CS --> M["Manager: Aimee Wadsworth
Suplente: Kristin Krogman"]:::mgr
M --> L1["L1 — Triage y primera respuesta
Asigna prioridad, producto, organización"]:::l1
M --> L2["L2 — Investigación y resolución
Aimee · Kristin · Dean gestionan la cola"]:::l2
L2 --> L3["L3 — Engineering / Delivery
(ver Módulo 08 y Topic 3)"]:::l3
L2 --> SDT["Support Data Team
(solo Secure5 · data)"]:::sdt
CO --> CC["Call Center 24x7x365
1-800 dedicado por cliente"]:::cc
CO --> CL1["L1 — Call Center executives"]:::l1
CO --> CL2["L2 — Escalaciones, disputes, relaciones"]:::l2
classDef root fill:#0f1d3a,color:#fff,stroke:none
classDef b2b fill:#2563eb,color:#fff,stroke:none
classDef b2c fill:#7c3aed,color:#fff,stroke:none
classDef mgr fill:#0d9488,color:#fff,stroke:none
classDef l1 fill:#e0f2fe,color:#0c4a6e,stroke:#38bdf8
classDef l2 fill:#dbeafe,color:#1e3a8a,stroke:#60a5fa
classDef l3 fill:#fef3c7,color:#92400e,stroke:#fbbf24
classDef sdt fill:#dcfce7,color:#166534,stroke:#4ade80
classDef cc fill:#ede9fe,color:#5b21b6,stroke:#a78bfa
🏢
Customer Support (B2B): maneja issues de aplicación, datos y configuración de los clientes retail. Tiene SLAs definidos por prioridad y un flujo L1→L2→L3 estructurado en Jira (proyecto RCS).
👤
Consumer Support (B2C): opera un call center 24×7×365 con números 1-800 dedicados por cliente, scripts personalizados y un CRM custom. Su trabajo central son los consumer disputes .
Para recordar
- Aimee Wadsworth es la manager de Customer Support (saliente, de ahí el KT). Kristin Krogman es su mano derecha y la cubre.
- La cola "Under Support Review" es el corazón de L2 — la gestionan Aimee, Kristin y Dean.
- El Support Data Team es un sub-equipo de L2 con cross-training en data, y solo toca Secure5 .
02

## Topic 1 · KB Support Operations — Los productos que soportamos
_chunk 178 · 2026-06-03 · fuente: /Users/MancoMenStudio/Desktop/Topic1_Support_Operations_KB.html_

Contexto indispensable: el "Product Type" del ticket determina la prioridad, el routing y a qué equipo escala.
Proceso core
No puedes triagear un ticket sin saber qué producto es. Esta es la taxonomía y qué significa cada familia para Support.
Diagrama 2 · Familias de producto
flowchart LR
P["PRODUCTOS
Appriss Retail"]:::root
P --> SEC["SECURE"]:::a
P --> INC["INCIDENT / AUDIT"]:::b
P --> ENG["ENGAGE (Verify)"]:::c
P --> RTI["RTI / RTIaaS"]:::d
P --> LEG["LEGACY"]:::e
SEC --> S1["Secure 3/4 — EBR (legacy)"]:::a2
SEC --> S2["Secure 5 — EBR (actual)
genera la mayoría de tickets"]:::a2
SEC --> S3["Secure Store · Apollo"]:::a2
INC --> I1["Secure Incident (ex-LPMS)"]:::b2
INC --> I2["Secure Audit (ex-CAMS)"]:::b2
LEG --> L1["APIS — sin nuevos features"]:::e2
LEG --> L2["Izenda Reporting — sin desarrollo"]:::e2
classDef root fill:#0f1d3a,color:#fff,stroke:none
classDef a fill:#2563eb,color:#fff,stroke:none
classDef b fill:#0d9488,color:#fff,stroke:none
classDef c fill:#7c3aed,color:#fff,stroke:none
classDef d fill:#d97706,color:#fff,stroke:none
classDef e fill:#64748b,color:#fff,stroke:none
classDef a2 fill:#dbeafe,color:#1e3a8a,stroke:#60a5fa
classDef b2 fill:#ccfbf1,color:#115e59,stroke:#2dd4bf
classDef e2 fill:#f1f5f9,color:#475569,stroke:#cbd5e1
Lo que debes saber de cada familia
Producto | Notas para Support
Secure 5 / EBR | Producto principal. La mayoría del backlog (RCS) son tickets Secure 5 - EBR.
Secure 3/4 | Legacy Secure. Solo fixes menores. DataOps NO maneja sus data loads.
Secure Store / Apollo | Acceso por país, sin IP whitelisting (ver Módulo 18).
Incident (LPMS) | Case management. Dean es el SME.
Audit (CAMS) | Auditorías de pérdida.
Engage (Verify) | Solo Kristin lo maneja como L2 (ver Módulo 06).
RTIaaS | En triage L1 va directo a "Under Engineering Review".
⛔
APIS — legacy: no se hacen más modificaciones ni features. Si un cliente pide cambios, se ofrece Secure Incident + ORC como alternativa y se involucra al CSM. (Hay canned response específico — Módulo 20.)
⛔
Izenda Reporting — legacy: Appriss ya no lo desarrolla. Se llegó al límite de lo que Engineering puede hacer. Redirigir al CSM para discutir alternativas. (Canned response dedicado.)
📋
El "Product Type" es un campo en Jira que L1 valida en cada ticket. Si no se puede determinar por la descripción → contactar al cliente.
04

## Topic 1 · KB Support Operations — Ciclo de vida del ticket (Customer Support)
_chunk 179 · 2026-06-03 · fuente: /Users/MancoMenStudio/Desktop/Topic1_Support_Operations_KB.html_

El recorrido completo de un ticket RCS por sus statuses, desde que entra hasta Closed.
Proceso core
Diagrama 3 · Statuses de un ticket RCS
stateDiagram-v2
[*] --> Open: Cliente / sistema crea ticket
Open --> UnderSupportReview: L1 triage (prioridad, producto, org)
UnderSupportReview --> WorkInProgress: L2 toma el ticket
WorkInProgress --> UnderCustomerReview: Falta info del cliente
UnderCustomerReview --> WorkInProgress: Cliente responde
WorkInProgress --> UnderEngineeringReview: Escala a L3 (ver Mod 08)
UnderEngineeringReview --> WorkInProgress: L3 devuelve resuelto
WorkInProgress --> Complete: Trabajo terminado + Resolution Details
Complete --> Closed: Cliente verifica o pasan 7 días
Complete --> WorkInProgress: Cliente reabre
Closed --> [*]
✅
Regla de oro: el status "Complete" NO cierra el ticket — el cliente todavía puede responder. El cierre real ocurre cuando el cliente confirma o tras 1 semana de silencio. Al poner Complete debes llenar ambos dropdowns de Resolution Details (Módulo 21); si dejas uno en "none", el sistema lo regresa a "additional info needed" y notifica al assignee.
05

## Topic 1 · KB Support Operations — Triage L1 — el primer filtro (1/1)
_chunk 180 · 2026-06-03 · fuente: /Users/MancoMenStudio/Desktop/Topic1_Support_Operations_KB.html_

Cómo L1 clasifica, prioriza y enruta cada ticket que entra a la cola "All Open".
Proceso core
Diagrama 4 · Árbol de decisión del triage L1
flowchart TD
START["Cola: All Open — To be moved to Backlog"]:::root
START --> ST{"Status = OPEN?"}:::dec
ST -->|Sí| PT{"Product Type?"}:::dec
PT -->|"RTIaaS"| ER["→ Under Engineering Review"]:::eng
PT -->|"Todos los demás
(Secure 3/4/5, RTI,
LPMS, CAMS, APIS, ASPECT)"| USR["→ Under Support Review"]:::sup
PT -->|"No se identifica"| ASK["Contactar al cliente
para validar producto"]:::warn
USR --> CR{"Customer Request type
= Change Request?"}:::dec
CR -->|Sí| L2Q["→ cola L2
(no cambiar prioridad)"]:::sup
CR -->|No| PRI["Asignar prioridad
(ver tabla)"]:::pri
L2Q --> ORG["Organización: NUNCA dejar en NONE
buscar y seleccionar la empresa"]:::org
PRI --> ORG
ORG --> REPLY["Reply to Customer:
confirmar recepción del ticket"]:::ok
REPLY --> DONE["Ticket cae en la cola correcta"]:::done
classDef root fill:#0f1d3a,color:#fff,stroke:none
classDef dec fill:#d97706,color:#fff,stroke:none
classDef eng fill:#1e40af,color:#fff,stroke:none
classDef sup fill:#2563eb,color:#fff,stroke:none
classDef warn fill:#fef3c7,color:#92400e,stroke:#fbbf24
classDef pri fill:#7c3aed,color:#fff,stroke:none
classDef org fill:#0d9488,color:#fff,stroke:none
classDef ok fill:#dcfce7,color:#166534,stroke:#4ade80
classDef done fill:#16a34a,color:#fff,stroke:none
Definición de prioridades
Prioridad | Significa
Critical | Application Down — no se puede acceder (ni un solo usuario). Como regla, no se baja.
High | Vital para el día a día (aunque sea 1 usuario) pero hay workaround.
Medium | Importante pero no detiene el negocio.
Low | Cosmético / informativo.
Durante horario laboral, L1 y L2 reciben email de cada Critical y High. Validar a los 15 min que el ticket de Critical/High haya sido asignado.
🔒
Prioridades que NO se bajan:
TJX (cualquier ticket) | Siempre la prioridad que pidió el cliente.
App inaccessible (1 usuario) | No bajar de Critical/High
Application Slow / Timeout | Mantener
Permissions errors (Admin/Power) | Mantener
Work Items missing / not loading | Mantener
Nunca cambiar prioridad en tickets de tipo Change Request, New Feature o SOW Estimation — eso es discreción del cliente.
🚨
Critical fuera de horario (6 PM – 2 AM EST):
1. Contactar al equipo vía su Teams Channel (por producto).
2. Escalar vía OpsGenie a los equipos de Engineering.
Work Items — escalación especial
Durante horario (8–5 Central, L–V), si llega un ticket de: Work Items no cargaron · Work Items faltantes (aunque sea uno) · errores al ver/usar Work Items →
Escalar a mínimo High , publicar en el canal Teams "Secure 5 Issues" y seguir el proceso Critical/High.
NO incluye: creación de Work Items, Work Item que no funciona bien, ni preguntas generales. Fin de semana/fuera de horario: si el cliente lo creó Medium/Low, dejarlo así.
Checklist completo del triage L1 (paso a paso)
- Ir a Queues → "All Open - To be moved to Backlog" en el proyecto Retail Customer Support.
- Abrir el ticket (click en el número RCS bajo "Key").
- A) Status: si está OPEN → mover a cola. RTIaaS → "Under Engineering Review"; el resto → "Under Support Review".
- B) Product Type: identificar el producto. Si no se puede → contactar al cliente.
- C) Change Request: mover a cola L2 (L2 decide si involucra CSM u otro depto). No cambiar prioridad.
- D) Priority: validar/asignar según la tabla de definiciones.
- E) Organization: escribir el nombre de la empresa — nunca dejar "NONE". (Algunos clientes usan nombres distintos.)
- F) Reply to Customer: en el área Activity, enviar nota de confirmación de recepción.
Hecho esto, el ticket cae automáticamente en la cola correcta según su status. RCS Backlog es la cola de tickets ya movidos pero aún sin asignar — monitorearla regularmente.
06

## Topic 1 · KB Support Operations — Triage L2 — investigación y resolución
_chunk 181 · 2026-06-03 · fuente: /Users/MancoMenStudio/Desktop/Topic1_Support_Operations_KB.html_

L2 es responsable de triage, routing, ejecución y resolución de Incidents de todos los productos.
Proceso core
Todos los tickets RCS pasan por la cola "Under Support Review" , gestionada por el leadership (Aimee, Kristin, Dean). Los L2 Engineers toman tickets según disponibilidad. Si un ticket es de data → se le pone el label Support_Data_Team .
A · Asignación y notificación
Leadership revisa todos los tickets para detectar si son del Support Data Team. Critical/High → email automático a L1 y L2 Management; L1 también avisa por Teams y usa OpsGenie si hace falta.
B · Trabajar el ticket
- Pedir un resumen a Claude (documentado así literalmente)
- Confirmar/clarificar información con el cliente
- Replicar el issue
- Identificar el bug
- Follow-up con el cliente
- Resolución
Puede dejar el ticket en "Under Support Review" o pasarlo a "Work in Progress". Si necesita info → "Under Customer Review".
C · Actualizar el ticket
Mínimo 1 vez por semana , aunque no haya cambios ("testing in progress" basta). Comentarios internos o visibles al cliente.
Automatización: status y comentarios de los proyectos ENG, INT, DO se traen a RCS como comentarios internos.
D · Cerrar el ticket
Poner Complete cuando el lado Appriss está listo → llenar los dos dropdowns de Resolution Details + notas de root cause. Esperar verificación del cliente o 7 días → Closed .
E · SOW Estimation tickets
Los usan los CSMs. L1/L2 normalmente no se involucran; el ticket va y viene entre CSM y Engineering. Detalle completo en el Módulo 09.
🎯
Caso especial — Engage tickets: los maneja exclusivamente Kristin Krogman . Es el único punto L2 y de escalación para Engage. Si los CSMs necesitan ayuda → acuden a Kristin. Tras triage, si no se resuelve, se asigna a Marissa Johnson (Solutions Engineering) o Ian Williams (Engineering).
07

## Topic 1 · KB Support Operations — Monitoreo de tickets asignados & SLAs de respuesta
_chunk 182 · 2026-06-03 · fuente: /Users/MancoMenStudio/Desktop/Topic1_Support_Operations_KB.html_

Cómo se vigila que cada respuesta del cliente reciba seguimiento oportuno — el flujo que más se usa en el día a día.
Proceso core On-call
Diagrama 5 · Flujo de monitoreo cuando el cliente responde
flowchart TD
CR["Cliente responde → Jira avisa a L1 (L2 backup)
Ticket vuelve a Work in Progress"]:::root
CR --> CAN["L1 envía canned response al cliente"]:::ok
CAN --> OOO{"¿Assignee OOO /
fuera de turno?"}:::dec
OOO -->|"No"| PRI{"¿Prioridad?"}:::dec
OOO -->|"Sí"| TZ["Cobertura por zona horaria
US OOO → ping EU · EU OOO → ping US
nadie de turno → on-call engineer
sin respuesta 15 min → duty manager reasigna"]:::tz
PRI -->|"Critical: vigilar 1h
High: vigilar 6h"| W1{"¿Cliente
respondido?"}:::dec
PRI -->|"Medium/Low: vigilar 1 día
(lo vigila L2)"| W2{"¿Cliente
respondido?"}:::dec
W1 -->|No| T1["Teams msg al assignee
sin respuesta 15 min →
notificar al manager"]:::esc
W1 -->|Sí| OK["Resuelto"]:::done
W2 -->|No| T2["Teams msg al assignee
sin respuesta 1 día →
notificar al manager"]:::esc
W2 -->|Sí| OK
T1 --> MGR["Manager monitorea / reasigna
según sea Support-owned o no"]:::mgr
T2 --> MGR
classDef root fill:#0f1d3a,color:#fff,stroke:none
classDef dec fill:#d97706,color:#fff,stroke:none
classDef ok fill:#dcfce7,color:#166534,stroke:#4ade80
classDef esc fill:#dc2626,color:#fff,stroke:none
classDef tz fill:#7c3aed,color:#fff,stroke:none
classDef mgr fill:#1e40af,color:#fff,stroke:none
classDef done fill:#16a34a,color:#fff,stroke:none
Critical / High
Ventana de vigilancia | Escalación
Critical: 1 hora
High: 6 horas | Sin respuesta → Teams al assignee → 15 min sin respuesta → al manager del assignee (Support-owned o externo).
Medium / Low
Ventana | Responsable / escalación
1 día | Vigila L2 (Aimee/Kristin/Dean). Sin respuesta → Teams al assignee → 1 día más → al manager.
🌍
Cobertura por zona horaria (assignee OOO): si el cliente responde fuera del horario del assignee, L1 publica en Teams al equipo de turno. US fuera → EU cubre; EU fuera → US cubre. Si nadie está de turno → al on-call engineer del producto. Sin respuesta en 15 min → al duty manager, que reasigna a alguien de turno.
📎 El detalle nodo-por-nodo de este flujo (incluyendo las ramas Support-owned vs. non-Support) está en Topic 3 · RCS Ticket Flows , sección 3 "Assigned Ticket Monitoring (T-003)".
L3 -->
08

## Topic 1 · KB Support Operations — Escalación L2 → L3 (Engineering / Delivery)
_chunk 183 · 2026-06-03 · fuente: /Users/MancoMenStudio/Desktop/Topic1_Support_Operations_KB.html_

Cuándo y a quién escala L2, y la diferencia clave entre Delivery y Engineering.
Proceso core
Diagrama 6 · Hacia dónde escala cada tipo de issue
flowchart TD
L2["L2 triagea el ticket"]:::root
L2 --> Q{"¿Naturaleza del issue?"}:::dec
Q -->|"Bug / código"| ENG["ENGINEERING
Defecto en la aplicación
tipo: Incident"]:::eng
Q -->|"Data / config ya implementada"| DEL["DELIVERY
Problemas con data o config
que ya estaban en prod · tipo: Incident"]:::del
Q -->|"Cambio / update billable"| CSM["CSM
Cambios de config que pueden cobrar
tipo: Change Request"]:::csm
Q -->|"Nuevo feature"| FP["CUSTOMER FEEDBACK PORTAL
Se mueve a Ideas Portal
el RCS se cierra · tipo: Feature Request"]:::fp
classDef root fill:#0f1d3a,color:#fff,stroke:none
classDef dec fill:#d97706,color:#fff,stroke:none
classDef eng fill:#1e40af,color:#fff,stroke:none
classDef del fill:#0d9488,color:#fff,stroke:none
classDef csm fill:#7c3aed,color:#fff,stroke:none
classDef fp fill:#64748b,color:#fff,stroke:none
Delivery vs. Engineering — la distinción clave
Delivery es responsable de la implementación y de updates de configuración respecto a lo originalmente implementado (NO change requests ni features). Ejemplos:
- Set-up de feeds iniciales
- Valores incorrectos / actualizar value reason
- Cambios a views en receipts
- Permissions · agregar o remover info en bulk
- Links que van a páginas incorrectas
Engineering es responsable de cualquier cosa relacionada con código en las aplicaciones.
Nota: issues con feeds después de implementación van a Infrastructure (Incident/Audit).
Cómo se mueve a Delivery (campos Jira)
- Team Ownership → Support (Delivery Dep.)
- Sprint → RCS Support Team
- Status → Under Delivery Review (mueve a la cola "Support Tickets")
Equipos Delivery por producto
Secure Incident & Audit (LPMS/CAMS) | Matt Kamminga
Engage | Ian Williams · Kenny Vu
Secure Store (Sec 3/4/5) | Tomasz Mikunda · Carl Costelow
🔁
Callouts: Engineering, Delivery y CSMs colaboran para decidir si un request es factible/billable. Para feature requests, Product Management trabaja con CSMs (Feature Request Workflow — archivado). Si un Incident llega a Engineering pero podría resolverlo Delivery → transicionar a Delivery.
🔗 Topic 3 · RCS Ticket Flows — mapa de routing por Product Type (Secure EBR → Polonia, Verify → Kenny Vu, AALPS → Shan/Sholan/Ryan)
09

## Topic 1 · KB Support Operations — SOW Estimation Workflow
_chunk 184 · 2026-06-03 · fuente: /Users/MancoMenStudio/Desktop/Topic1_Support_Operations_KB.html_

Cómo se construye una estimación formal de trabajo billable, paso a paso.
Proceso core
Un ticket SOW Estimation se levanta cuando hay que desarrollar un estimado formal o Statement of Work para un cliente. Lo puede abrir el cliente (tipo SOW Estimation o Incident) o un CSM directamente.
Diagrama 7 · Flujo SOW Estimation
flowchart LR
A["1 · Ticket creado
Cliente o CSM"]:::cli --> B["2 · Queue assignment
L1 → Under Support Review"]:::l1
B --> C["3 · Initial legwork
L2 reúne data con Eng/Delivery
→ Waiting for CSM"]:::l2
C --> D["4 · Initial BRTD fill
CSM llena requisitos
→ Waiting for Engineering"]:::csm
D --> E["5 · Update BRTD
Engineering añade nivel de esfuerzo
→ Waiting for CSM"]:::eng
E --> F["6 · Finalize BRTD
CSM pone horas y costos
comparte con cliente"]:::csm
F --> G["7 · SOW development
Cliente aprueba BRTD
CSM construye el SOW"]:::csm
G --> H["8 · Closure
CSM (o PM) cierra
al completar el proyecto"]:::done
classDef cli fill:#0f1d3a,color:#fff,stroke:none
classDef l1 fill:#2563eb,color:#fff,stroke:none
classDef l2 fill:#0d9488,color:#fff,stroke:none
classDef csm fill:#7c3aed,color:#fff,stroke:none
classDef eng fill:#d97706,color:#fff,stroke:none
classDef done fill:#16a34a,color:#fff,stroke:none
↪️
Variantes: si un ticket tipo Incident resulta requerir SOW, L2 lo determina y el proceso continúa desde el paso 3 . Si un CSM abre el ticket, puede empezar en el paso 1 o saltar al paso 4, según cuánto conozca ya del requerimiento. En el paso 7, si un PM corre el proyecto → "Waiting for Project Management".
10

## Reunión 2026-06-10 — Acknowledgment vs. resolution timelines · Transcripción 1/8
_chunk 716 · 2026-06-10_

## Transcripción completa
30 minutes to resolve it, right? And generally, what a... What I have observed throughout my support tenure is 30 minutes is to acknowledge the issue. So, this is the first thing I want to talk about. That's why I was a little bit hesitant to decide anything like, you know, let's Let's not commit anything before even we start working, right? Because... If there is something that is unrealistic, right? We don't want to put ourselves as a part of the team. So, we are getting into a bit of under pressure. But yeah, let's see what JR has to say. But I mean, I am totally okay with any kind of changes that they bring in. The only thing is, you know, it has to be realistic. So, to be accepted at the ground level, wherein, you know, And most of them are able to follow it unless there are certain So, we can see that we have a lot of cases of, you know, that needs details. It's detailed technical analysis or there is some knowledge gaps like that. Yeah, but yeah, let us see just wanted to pay attention. I just wanted to catch up, like, you know, how are you doing? No reason, yeah, just wanted to see like, you know, Yeah, I have actually worked on So, we have talked on a couple of issues with Pj and Carlos is still, you know, little bit I am yet to closely work with him. He is on video today. I did go through a couple of clients. We had a lot of client calls last week with PJ. And sometimes what I have observed even with BJ, like Like I think he is like couple of years of experience into Appreciate Appress retail, I don't know the number of XLs with him, but But sometimes it takes some, at least no. At least half a day even to reprow the issue. Because not all the scenarios are pretty much straightforward. Typically, the KPIs that I have worked for, The resolution part is Is something will always depend on what kind of ticket it is, right? So, tickets are are categorized into different priorities that will be p3, p2, p1, p4, p4 and p2.

## Reunión 2026-06-10 — Acknowledgment vs. resolution timelines · Transcripción 2/8
_chunk 717 · 2026-06-10_

P1 is understandable, the impact is quite wider where a lot of people or the whole company is not able to work or utilize the products. So, such very targeted timelines for resolution on P1 issues is understandable. So, the use of the Cosmos is understandable, but you cannot have very, We have seen similar resolution times for all the I don't have the data and I haven't checked the queue and all. I'm still yet to get figured out like So, let us say there are 15 tickets in your 15 tickets, doesn't mean you have to work on all 15 of them, but there are a couple There are a couple of them that are work in progress. You get three new. So when you start When you start your day, what do you prioritize? That's the first question you ask as an engineer. So, whatever is the most important ticket for you, right, whether it is escalated or It has a higher priority or maybe the customer is a top priority customer. We have a lot of customers, we have a variety customer, right? Like maybe high paid customer or something like that, or maybe for some tickets, some So, you will get a lot of information. So you will start prioritizing your cases accordingly. So that's why I double checked with 30 minutes is really the resolution time. So, yeah, that's why I was like, you know, double checking like, We need to make sure whatever KPIs or changes that we are bringing in, It has to be realistic, but let's see, I will hear out here what he has to say. I have to say about that field. On the other side, I got one-on-one with Chris Rickling. I guess he is the VP of Engineering from UK. He did set a couple of expectations from us in terms of here. He just wanted to know me actually as a person like, you know, who I am, where I work from. We can see the results from what hours I follow at the moment. So most of the important thing for them was oncall. So, Kamila is already working on, with JR on that. L2 needs to grow more into handling the escalations.

## Reunión 2026-06-10 — Acknowledgment vs. resolution timelines · Transcripción 3/8
_chunk 718 · 2026-06-10_

I think it is a good idea to use the same tool as it can. The developers are not just support engineers, they have done full stack development, maybe somebody has turned front-end, somebody has So, people will have their own expertise from their experience and we will So, we will see who is more curious, who has a higher KQL, So, KQL should be to learn, everybody has their own pace for learning, but who can become a So, we had a lot of different things. To make sure that we have a technical depth rather than the current support team. So that is something, you know, it will not happen overnight, right? So I did, I come We have to acknowledge that it will at least take couple of months for us to understand the product because Because if you say that if I am going to resolve an issue in 30 minutes, if I have worked on that issue, So, I think that's all I have to show. Prior to that, I should be able to resolve it. One can't be met unless we are at least 3-4 months or 6 months into the system, right? Because if you have a repeated pattern, you know what to do. So, this is the first issue for the first time. We have to report the issue, try to check the code, try to get some use of We all work with you, right? We don't work in a scene of face-wet. In a face where you can just tap a shoulder and ask. So, you know, these things are going to take time, but Let's see what JRS2 say and whatever changes are going to come along. I just want to make sure that before we take over the Take over the production, right? At least we are shadowing to these guys for two months. After shadowing or maybe Kamila said like next week or something you should start.

## Reunión 2026-06-10 — Acknowledgment vs. resolution timelines · Transcripción 4/8
_chunk 719 · 2026-06-10_

You should start the reverse shadowing in terms of, you know, you start working on tickets, take help from the We will be able to get help from them and start understanding the aspects of the product and start You can start doing by yourself and take help from them, home server, your shadowing, right? But if let's say from July or let's say mid-July, So, this is the case in mid-July, right? If we are going to directly take over the support cases, right? I've been talking about this, right? Because there are so many modules, if you have opened, you know, On the left hand side there is user menu, there are a lot of different menus. I have worked on a couple of SSO issues. So, that functionality I have been a little bit familiar, but not all the products and all the products All the product aspects of what modules or what things are designed for work. That's why I'm a little bit hesitant in terms of defining any KPI So, we have to have a lot of experience with this. So, in some realistic APIs, people will start burning out, right? And we don't want anyone to burn out before even they start working, you know? Otherwise, you never know. People come here, they work a couple of months, and then they find something else. We have the right platform and time to start. Taking over things, understanding things before So, we can commit on any kind of improvements. Other than the existing team. So, existing team is here for many So, we have been taking them for many months, many years, right? Replacing them overnight in one month or two months, it's quite a tough task. So, you need to understand the ground realities. That is the only question that always keep This keeps hampering me. So, I put myself in that situation, right? If you are asking the whole team to put in that situation, It's quite tough, you know, and people will come to me or you or Kamila like Like, you know, we are stuck.

## Reunión 2026-06-10 — Acknowledgment vs. resolution timelines · Transcripción 5/8
_chunk 720 · 2026-06-10_

And right now people are not saying, but when they face this situation, If they don't know, at the end of the day, everything is going to come to you or me. So, I am not able to figure this out, help me, I am at the same page as you. And what am I going to do about that? Expectations are good, unrealistic expectations doesn't take any It doesn't take anyone anywhere. My only concern that is just, you know, scratching up my head. I mean, say little bit of pressure is fine, but the expectations niche So, the solutions need to be realistic, okay? Like, let me give you a specific example. Like, there must be some set of metrics We have a new matrix that JR is tracking for the existing team, time to closure, time to resolution, First response resolution, CSATs, positive or negative feedbacks if they are sending They are sending the service through Jira tickets, so I'm not very sure about that yet. So, there are a lot of support metrics, right? Let us say the support metrics are at 60%, okay? If let us say we If let's say we start working from first of August, just a very blank example. I don't think we are going to do 70%, 80% from the month of August. August, September, maybe from October we will be able to push some Some improvement in terms of faster resolution time to closure. More positive feedback, variety of metrics. I don't think at all from my experience. That immediately you take over and immediately you are able to show the improvements in the metrics. The matrix is not the same as the individual matrix. Not the whole team, right? Support team. Those metrics will improve eventually, not overnight. So those couple of months are something that our guys will get more expertise. And based on, you know, somebody's curiosity, somebody will do, So, above the bar, somebody will do average, somebody will do below average, right? There are 10 people, you can't expect 10 people to do above average. One or two people will always be below average.

## Reunión 2026-06-10 — Acknowledgment vs. resolution timelines · Transcripción 6/8
_chunk 721 · 2026-06-10_

Most of them will be average, one or two guys will be exceptional. We are not going to be able to do that. So, we are going to start working with the other side of the system. Not just me, even you, anybody else who works on a technical domain, right? So, I mean, these are the questions that is, you know, I'm just I'm just a little bit that keeps eating my brain in the sense In the sense, it keeps troubling me, like you know, but yeah, let's But yeah, let's see, you know, how it goes, because there are, There are things like, you know, a couple of guys are not having good experience with one server they are shadowing. I'm going to meet the guys in India this Friday to see how everything is going and probably I will Probably I will try to meet them every week once in a single meeting. Just to track like, you know, they are doing good. We have a lot of people who are interested in this. So, this is the time to speak up. If they don't speak up, head to head. At the end of the day, we have to start working on those tickets tomorrow, right? Whenever. Whenever the time comes, so that's going to happen eventually, right? So they have to speak up. So, I don't want to speak up in the way, but let's see, I am keeping my fingers crossed. And that is why we have the ability to do that. Just that slow changes are agreeable, but all of a sudden meanwhile we are learning technically, also we are trying to understand the system, how it works, processes that they have existing, and then on top of a lot of changes, you know, everything at once. I don't know how it will mess up, you know, people will become very overwhelmed. It will mess up a lot of things. So, we have to do this. How much we are able to dive all the town, right? Like from JR to the Millar to the store at the bottom, right? We will see how it works out, figures out. There are a lot of expectations that So, that's the presentation that they have. But yeah, I mean, let's see how much fast we are able to catch up.

## Reunión 2026-06-10 — Acknowledgment vs. resolution timelines · Transcripción 7/8
_chunk 722 · 2026-06-10_

And then, see whatever best we can for the process and for the plant. Yeah, again, automation usage, right? You will be able to do it unless and until you work. You work on tickets for two months, maybe a month minimum, right? You work for a month. You work for a month, you observe the patterns and from a particular set of patterns, you are You can also use the app to identify the gaps that you can automate. We understand the products and lot of things, the variety of factors before you see the gaps that we can automate. These things takes time, it just can't happen overnight, right? So, a lot of changes with With all these transitions, it's just quite We have quite a lot to grasp and do just Do justice to how much we are able to fulfill based on the understanding not just for me or you. We need to build that product knowledge. That's the very basic foundation first. I am worried about at the moment, not any KPIs, not anything else, just building Just building up the basic foundation, not for me, but also for the resources within Within the whole tip. I think it is cancelled, right? So, what is the reason why this is so important? I have cancelled it. That was supposed to be support team scrub, right? It's cancelled. No worries, man. I just wanted to have a touch base like you You guys are shadowing Amy right? Does she works on tickets or she takes care of the processes mostly? Amy takes care of all the processes or she also works on Also works on those tickets as well. Mostly I see like you know if there is any messages on this support chat. Not from support chat, but support management channel, right? It's Amy who mostly responds on any escalations that So, J.R. Netz helps with, okay, so she works very closely Very closely in terms of process orientation and all right. Yeah, I'm actually closely working with BJ, Vijay Prabhat, he is more into working on the secure and incident. We have a very good example of how we can use this.

## Reunión 2026-06-10 — Acknowledgment vs. resolution timelines · Transcripción 8/8
_chunk 723 · 2026-06-10_

I am still trying to figure out what expertise does Carlos have. So that's like second half of Carlos is first half of So, at least I am able to get 4 to 5 hours daily from Kafka. We're going from Karnos 4 to 5 hours from Bicep. Yeah, it's going quite good, but not at the pace that I'm expecting. I hope in one or two weeks I can bring myself up to the speed. And maybe that reward shadowing will definitely help me understand When I actually start using my brain on those tickets, let's see. No worries man, let's keep our fingers crossed and I will keep I will keep calling you if some things are bugging me, okay? I know I can't. Yeah, I know I can't speak about everything I hope I can speak to you about everything. Just to sometimes just to you know, What do you say? The English word is We forgot English word. Just to get outside everything from your head, you know. Just pick it out. Just pick it out, you know, so your mind is little bit easier and I can focus on one I just don't get myself overwhelmed. Yeah, I would prefer. I would prefer not to do it with my own. I will do it with my wife because again she will not understand the sheet about my work. But I would prefer not to take my work in my home. I work from home, but... I prefer to keep my desk and when I get up the desk I don't talk about work. I try to keep both the things separate as much as I can. Notice man, thanks for talking over. We'll see you later. Bye.

## Reunión 2026-06-10 — Four core pillars of support · Resumen
_chunk 785 · 2026-06-10_

## Resumen
The meeting introduced the monthly Global Support sessions, focusing on the 'four core pillars of support': First Reply, Update Rate, Remediation, and CSAT. SLAs were explained as formal contracts with penalties for non-compliance, contrasted with SLOs and OLAs. Metrics like backlog, tickets by product, and priority were discussed as internal tools to improve operations. The speaker emphasized the importance of meaningful client updates and remediation over resolution. Action items included validating SLA templates, OLAs with engineering, and cross-departmental billing practices. The meeting also outlined plans for team presentations and structural improvements over time.

## Temas clave
- Four core pillars of support
- SLAs and SLOs
- Support metrics

## Decisiones
- **Establish monthly all-hands meetings for global support teams.** — To align teams and discuss key initiatives.
- **Focus on the 'four core pillars of support' as central metrics for success.** — To reduce noise and improve organizational efficiency.

## Tareas / Action Items
- Confirm if Appriss Retail has specific SLA templates or examples for its clients.
- Validate if OLAs exist between L3 Support and Engineering, and their defined response times.
- Investigate if cross-departmental billing or similar practices are relevant to Appriss Retail's operations.

## Insights en vivo (Ask AI / Analizar)
### [Analizar] So when you hear SLA, that's just kind of a high level of what SLA means.
The transcript provides a high-level explanation of SLA, emphasizing its contractual nature and the penalties tied to non-compliance. It also contrasts SLAs with SLOs, which are aspirational targets without penalties. This aligns with the foundational understanding of SLAs in our support context, but we should confirm if there are specific SLA examples or nuances for Appriss Retail clients that differ from this general definition.

**Resumen:**  
- The speaker introduced the concept of SLAs (Service Level Agreements) as formal contracts with penalties for non-compliance, such as monetary compensation or service credits.  
- SLOs (Service Level Objectives) were contrasted as internal, non-penalized targets.  
- Mentioned OLAs (Operational Level Agreements) as agreements between departments, with examples like engineering response times.  
- Highlighted the importance of SLAs in support metrics and their role in reducing noise in the business.  

**Decisiones detectadas:**  
- Monthly all-hands meetings for global support teams will be established.  
- The "four core pillars of support" will be central to measuring success in the organization.  

**Tareas / action items:**  
- Confirm if Appriss Retail has specific SLA templates or examples for its clients.  
- Validate if OLAs exist between L3 Support and Engineering, and their defined response times.  
- Investigate if cross-departmental billing or similar practices are relevant to Appriss Retail's operations.  

**Cruces con tu segundo cerebro:**  
- **Customer escalation playbook**: SLA breaches might trigger escalations; check T-005 for alignment.  
- **Ticket lifecycle map (RCS/RTS)**: SLAs could influence transitions between statuses; review T-007.  
- **Update Rate compliance**: Weekly updates might intersect with SLA requirements; see T-071.  
- **Priority — current state**: SLA urgency could affect priority determination; consult T-092.  

**Aclaraciones:**  
- Are there specific SLA penalties or remedies defined for Appriss Retail clients?  
- Does the engineering team have documented OLAs, and are they tracked in Jira or another system?  
- Is there a formal process for SLA breach notifications to clients?  

This analysis aligns with the transcript and highlights areas where further clarification or documentation is needed.

### [Ask AI] alguna pregunta que pueda hacer de valor en base a lo visto o leido en la reunion?
Could you clarify the timeline for the Jira field consolidation project? Specifically, when should we expect the new field list to be finalized and rolled out? Also, regarding Talos, is there a plan to prioritize certain ticket types or products for its initial implementation, or will it be applied across the board from the start?

- **Jira field consolidation**: The transcript mentions circulating a field list starting with management, combining RCS and RTS, and removing unused fields. Asking about the timeline ensures clarity on when changes will impact workflows.  
- **Talos implementation**: Talos is described as a backend tool to assist with ticket resolution by adding internal comments. Understanding its rollout strategy—whether phased or universal—helps anticipate operational adjustments.  
- Follow-up questions:  
  - Will the field consolidation affect automation rules tied to Jira fields?  
  - How will Talos handle edge cases where documentation is incomplete or ambiguous?  
  - Are there specific metrics or KPIs tied to Talos' success in ticket resolution?


---

## Reunión 2026-06-10 — Four core pillars of support · Transcripción 1/16
_chunk 786 · 2026-06-10_

## Transcripción completa
Happy Wednesday, team. Hope everybody's doing well. You can keep your You can keep your cameras off for this one. If you want to turn them on, feel free, but I'm going to be presenting. I'm presenting for pretty much the entire meeting. We're going to give it, I like to start it about two or three hours. We'll go ahead and get started. So just another minute or two if anybody wants to grab a coffee or water. Or T, or, you know. If you could maybe Could maybe stay on mute, Pima. I'm just going to go ahead and mute him. Before we hear anything crazy. All right, team, we're going to go ahead and We're going to go ahead and get started. Just so everybody knows, I plan to do these every month. We're going to go through the outline of what the deck's going to look like. The next thing you'll see is the This is roughly the time we're going to have it. It should be the second week of every month on the web. I'll be back in a few minutes. Of course, work with your management team first to make sure everybody's aligned, that makes sense. But get them to me early and I'm happy to either present on them or have you folks present. You can also use the link in the description below. We'll be doing one or two slides and the team will be presenting most of these. Let's get to it. So first thing, actually I'm just going to skip the agenda, you guys can I had an idea to show you the metrics that how the business is running today. I'm going to go ahead and talk to you about the ones of those that I think are important. I think are important and why. A couple problems with that. One, still working for me.

## Reunión 2026-06-10 — Four core pillars of support · Transcripción 2/16
_chunk 787 · 2026-06-10_

I'm still working through on making sure that I'm fully aligned with the metrics and how we're collecting We're collecting them today, so I didn't want to show you something that I'm not fully I'm not fully in the loop on yet, but two, I think a lot of you, maybe not, Maybe not a lot, but there's going to be a number of you that aren't even going to know what I mean when I say I figured today's meeting will just explain what these I'll talk first about the four core And we'll talk about the four core pillars of support. I don't know if you're sharing. I'm not seeing anything. Yep, good call. Thanks. Thank you, Amy. You're welcome. I got it all up in presentation. We're going to go through the presentation mode and everything. Information, yeah, because this seems pretty deep. Good call. I'll go ahead and record it. As soon as I find the way to do that. More recording. Recording, start recording. All right, everybody, don't say anything crazy. I'll see it. Here it go. All right, team. So we're going to do our first all hands for support today. This is going to be a skeletal outline where we kind of go through how the structure is going to work of I'm going to work on this over time. I'm going to talk to you about a few key initiatives that I think are important. And if you folks have things that you would like to add to this over time, work with your Work with your management team, bring them to me. I'm not going to be presenting these long term. I'll be presenting one or two slides and new folks will be presenting these as we go through different parts There are different parts of the business and what matters. And this is global support. This is everybody. This is everybody, L1, L2, L3, this is the entire team. And if I miss somebody, my apologies. My apologies, I'll get you on the next one. All right. All right, we'll skip the agenda and just jump right into it. Talk about what matters in support.

## Reunión 2026-06-10 — Four core pillars of support · Transcripción 3/16
_chunk 788 · 2026-06-10_

So I remember a long time ago when I first took When I first took over leadership of a support organization, I had a new boss I had a new boss who came in and he asked me how I measure my business. And I've never really thought about it like that, right? So I talked about the things that The things that I thought were important and he and I kind of went back and forth a bit on them and And he gave me a phrase that I've used since then, which is the four core pillars of support. What are the things that make a support organization successful? I don't care what type of product you support. If you're running a support team and you can get these four things down well, a lot of the A lot of the noise goes away in the business. Now, it's not easy. There's a lot of different ways to Different ways that you get these together, but these are the most important metrics. First reply, and I'm going to talk about these in detail in the next slide, which I do want to talk about service level We'll talk about service level agreements for just a minute, because not everybody knows what that means, and a lot of people use it in A service level agreement is a contract that you have between If you don't do this thing by default, And by the certain time, in this certain way, you owe them something. It could be money, it could be service credits, it could be extensions on the console. Service Bus is a service So service level agreements are very important. Service level objectives are I'm going to try to do that, but if I don't successfully do it, there's no problem. There's no penalty. You can do those within the company too. A, what's called an organizational level objective between us and engineering. We have a lot of people who are interested in engineering that say when we get a ticket over to engineering, their objective is to try It's to try to get it back to us with an answer within three business days.

## Reunión 2026-06-10 — Four core pillars of support · Transcripción 4/16
_chunk 789 · 2026-06-10_

An agreement is what a larger company would have, an organizational or operational level agreement, where we would say if engineering doesn't get it It doesn't get it back to us in this amount of days. They owe us some money. Now, we're never going to get to If you're going to get to that level, I can promise you that, but in really big companies, they do cross-departmental billing. So when you hear SLA, that's just kind of a high level of what SLA means. it means there's a penalty so it's really important the next one's update rate the next is remediation which is probably a new one for a lot of you we'll talk about that in a minute and the last one here is CSAT now a lot of people use CSAT And then, we'll talk about the final metric that you use to tout how your organization's going. Talk about what these mean in detail. First reply, SLA rate. So this is when we have the person who's actually going to work the ticket that's assigned to it. If you're not working the ticket, just take a quick glance at it and find That's the way the contracts are written. So let's first apply. Update rate. Pretty easy. Just means how often you're keeping the client A lot of times when we try to make the update checkbox ticked, We'll just say things like engineering continues to look at the issue, engineering continues to Engineering continues to look at the issue. Oncall, oncall, oncall, oncall, That just infuriates customers. They would like meaningful updates, which means we probably don't have to do it every day unless it's a super critical ticket, but we need to But we need to tell them something. Like, we've escalated this to the right level of engineering, now we've moved over We've moved over to another team. We're actually looking at this in this potential target version that we We need to provide them with a little bit of context. And that context ultimately will stop escalations.

## Reunión 2026-06-10 — Four core pillars of support · Transcripción 5/16
_chunk 790 · 2026-06-10_

It will stop them So stop them from freaking out about the ticket and making it harder for us to get the thing done in the first place. So we're paying in in the beginning to get something out at the end. Remediation, this is a big one. Most companies use resolution. What resolution is, is the code is fixed, everything is perfectly fine and working fine. The trick is, most customers don't even care about They didn't actually even care about resolution. They care about being able to do what they were trying to do. If you are trying to run a report and that report is failing, we say And we say, hey, by the way, you can click over here and then do this, and you can still get the Then they have a workaround. Now they can do what they need to do. That doesn't mean we closed the ticket, but it does mean that we can then tell the customer, we got you back to work. You can also do it by clicking on the link in the description. As it goes over to engineering or in our new world, we'll dive deeper into ways to figure This is an important one, and it is one that I'm working with. I'm working with the legal team to reformat all of our contracts and all of our website language. There are a lot of different ways to measure CSAT, but for support, the most The most important thing is a transactional at the end of every ticket. Was this, did the support experience that you received? Smiley face, frowny face. I mean, as simple as you can get it. One question, not wonderful. Not one to five, yes or no. When you can do that, then you get a better You get a better and better feel for is your support team performing well. Other series of ways that you can measure is the company performing well, things like Net Promoter You can do a different type of CSAT that comes from the customer success team that talks about The talk is about the products. We do in-product CSAT here, but for support, the most important The most important one is that transactional at the end of every ticket, CSAT.

## Reunión 2026-06-10 — Four core pillars of support · Transcripción 6/16
_chunk 791 · 2026-06-10_

Now, those are the four core pillars. There's a lot of other metrics though that take... It's a successful support organization to be able to do effectively. Backlog, this is another one that's important to me on how we articulate We articulate this. Backlog or basically any tickets that We're not waiting on the customer for that still have something to be done. be done for it. So if it's not closed, if it's not solved, if it's not If it's not waiting on the customer, that's part of our backlog. That's our cue of the work that needs to be done. And your goal is to try to keep your backlog low, of course. And when the backlog grows, and we see that our tickets are growing, that's a one for one. One, you can understand it. When your tickets aren't growing a lot, but your backlog is growing, there's other problems in the organization that you need to look at. Maybe we've got new releases that are more complex. Maybe we are low on Or low on staff, whatever it happens to be. But backlog is very important for us. Tickets by product, measuring the individual products, products, subcomponents, and how many tickets we get of that type. I'm not sure what the anatomy of those tickets are. Tickets by priority. Are we getting a ton of critical tickets? Are we getting a ton of low priority? as a subset of these other tickets resolved, tickets assigned, and then time to It's actually a good thing because we can figure out, I know for No, for example, anyone in a level three organization, their tickets take longer. The reason why we're here today is because we're going to be talking about the product line. This is a good idea to make. This product line is too complicated. It takes us too long to diagnose these things. We need better tools in order to be able to get to the resolution as quickly as we can. All of these things are important to help us run a successful business, but the ones that The ones that are important for us to report out are those four core pillars.

## Reunión 2026-06-10 — Four core pillars of support · Transcripción 7/16
_chunk 792 · 2026-06-10_

The rest of it, we try to keep internal unless we need to. All right, so let's talk about team. This is some of the The vision of where I'd like to take the organization over the coming months. The first thing is, and this is especially for the L2 folks, Thank you folks. Focused on break fix work. Our number one job needs to be getting We're going to be getting the clients up and running because we have SLAs. I'm just going away from that time to do projects, to do, I wish the product worked this way. This way, we're going to miss more SLAs and we're going to cost the company money. And then we're also going to be hiding where we're spending money in the company when we do it that way. For L3, they do break fix as well. They do a little bit of the project work. I'm currently negotiating with the professional This is a very easy process to use for a lot of the work that you do. Where that line lives, and I'm trying to shift that line closer to professional service. If it's billing work, my goal is to have them start to focus on that. Own the customer experience end to end. This is incredibly important. It's incredibly important to me, and I want everybody here to remember this. This is a very simple process, and it's very easy to get the data from the data. The reason why that is, if we send it over to engineering, we need to be checking in on that ticket regularly. Just send it over there and forget. If we send it to a customer success manager, we need to have a We have a warm handoff, and a warm handoff means you get on a phone call with someone Make sure they are good to take the ticket and take the ownership of it. We're going to take the ownership of it, and once they agree they're going to take the ownership of it, we can step away. I'll tell you the truth. Over to a CSM to own, or over to an engineer to own.

## Reunión 2026-06-10 — Four core pillars of support · Transcripción 8/16
_chunk 793 · 2026-06-10_

I want them to have their own We have their own ticket projects where we create tickets that go over to them and then we ultimately We can ultimately own the customer communication if it's broken. And if it's not broken, Not broken, we need to get it over into a different ticketing system or different group to work on anyway. There will be process changes coming around this, but the most important thing for you to remember The reason why we're here today is we own the customer experience and support, and we want to make sure that they have as good They have as good of a customer experience when the product isn't working as designed as possible. As possible. Next, more tools. So, I'm working on getting us more things. Now, right now, we're struggling getting even the new And even the new folks' access to everything the current folks have. But once we have that, We're going to be getting access to more tools. We're going to be working with engineering to build tools for us. We're going to be getting access to code, we're going to be getting access to products like Snowtime, We're working on it. Bear with me on this. I recognize we sit in engineering, and that, for all of us, All of us is sometimes a dangerous thing. Honestly, any organization you sit in can be a dangerous thing. Our goal should be making sure the customers have the best experience. Engineering's goal is getting features out the door and making sure that A lot of times those align, but they don't But they don't always align. So one of the things that we're going to be focusing on doing is making The next thing we're going to do is make sure we're raising to engineering, raising to product, the different areas where we need to focus in on the product. Get focus in, fix buggy parts of the product, fix better, make better documentation, make And we're going to do that by data. I'm going to talk a little bit soon about one of the things we're doing, which is a Jira overhaul project.

## Reunión 2026-06-10 — Four core pillars of support · Transcripción 9/16
_chunk 794 · 2026-06-10_

The main reason that you do that is to get the right data into the right Into the right teams, automatically, so that way they can act on it. I'll give you a quick example. Let's say we release a new product and all of a sudden And all of a sudden, we've got 10 times the defect rate in that product as our other products. I want engineering to immediately know that we've got a buggy product over there, and we're not just going to be writing hotfixes. We need to fix the problem upstream. We made major changes and now customers don't understand how to use it and they're constantly talking to us about it. We need to be able to let product know that the documentation is not acceptable. We need training videos to get our customers operating faster. We're going to do this through data. Once we get this rebuilt, it will make It'll make this a lot easier. Team updates. I think some of this is going to be clear for all of you already. I know you already, but I just wanted to make it crisp for everybody. The first thing, our new-off folks. All of our folks are live, they're working with us. They're on this call as well, so welcome aboard team. They're working 16 to 5. We'll also have oncall through the team as well. As well, currently they're doing shadowing, they're getting up to speed, working side by side with the Altoon. The L2 and L3 folks, I think it's going well so far, but we're still really early into that process. We're also going to be talking about the new version of the program, kind of just dovetails off of what I talked about. We've paired folks up. We're also going to pair up with engineers as well soon for the record and development. So it'll be new off-folks pairing with development folks, as well as support engineering folks. We are in a shadowing motion, which means they are watching We're watching everything that the Appress folks are doing and asking questions over the next week or so.

## Reunión 2026-06-10 — Four core pillars of support · Transcripción 10/16
_chunk 795 · 2026-06-10_

Next week we will flip that to a reverse shadowing where they are doing a lot of the work. And then the APRS folks are watching and then giving constructive criticism and making sure that we're sending We're sending the right things out to the clients at the right time. We've now got snow time live for Oncall is a free-to-use platform for all of your clients. Unif ICS is our held on folks, formerly known as glow touch for those of you that have been here a while. They are monitoring everything that's going on with the platform right now. They're raising alerts. We've seen We've seen it happen again and again. We've seen the engineering team jump in and fix the issues. That's going well. Thank you, team. And then product training for the new OPPO. New off folks, I've actually already heard other people mention that they'd be interested in this product training If you're part of the AppRes team that currently has an end date, let me know and I'm happy to add you We're happy to add you folks to the product training sessions we're working on as well. All right, next up. This is something I definitely want to try to make. If you want to try to make a part and parcel of our standard meetings, let's talk about shoutouts. I always like to try to identify when folks are doing especially good jobs. I'm sure you'll be able to see this. Helping the team as a whole be more successful as our customers. First one I wanted to talk about from an L1 perspective, and my apologies if I butcher anybody's anybody's name here is Cherise Ramdas. So Cherise is now one engineer and The engineering team making sure that we had everything set up correctly, making sure that the process of The process was working as it should work, not just taking what he was given, but leaning into the We're getting into the team and making sure that we're getting the right thing to be successful. So, you know, Sharish, You know, Sharish, good job. I've seen you do it in a few other ways as well.

## Reunión 2026-06-10 — Four core pillars of support · Transcripción 11/16
_chunk 796 · 2026-06-10_

I just wanted to call out. Thank you. Thank you. Next up, Tyrone. So Tyrone L2, Very good job lately of using Claude in order to level up his game and job. Level up the game around replies to customers, I started working with engineers, technical nuance, working with engineering. I started reading everybody's tickets and I saw where all the work was. And of course, I continue to do that on a week by week basis. I don't read every ticket. I read a snattering of tickets to make sure that we're having the right experience for our customers. Tyrone, I can tell you that your tickets have definitely improved even just in the last month. The next question is, Just wanted to let you know you're already doing a good job, you're doing an even better job now, and we love And we love the way you've embraced the technology. So thank you. And then last but not least, from a From a data engineer perspective, we have David Beck. So David has been, from what I've heard, I think you'll get a lot of information from what I've heard, a heavy hitter, from the time that he's been in the Data Team, but he's been doing Doing fantastic work lately, helping out Sainsbury, TJMaxx, or TJX, sorry, PSDB, We're going to talk about this in a few minutes. We're going to be putting a lot of ways in everywhere that you can and just being a great team player. So David just wanted to thank you for that. Thank you for that. Payment and the group recognize the work you're doing. I recognize the work you're doing. Well done. All right, let's talk a little bit more about what With more about what are we building? I had to make me a video or a picture of Jira blowing up. And it came back with a series of circles with an exclamation mark in the middle. I didn't have time to groom this too much, but long story short, we're We're going to be blowing Jira up. The first thing that we're doing here, you can see that on the On the left, we've got how does it work today. Priority fields are on undefined.

## Reunión 2026-06-10 — Four core pillars of support · Transcripción 12/16
_chunk 797 · 2026-06-10_

We have a lot of undefined which can create SLA problems for us. I'd like to give an easy way for development to see what tickets are important. So if you look at a P1, not all P1s are weighted exactly the same. One might be for a larger client, it might be more profitable for a larger client, We're going to develop more products that are down. It might be higher SLAs, whatever it happens to be. We're going to develop a system in the backend to put a number on these tickets, and that number will be for us. It's for us, but it'll definitely be for engineering to help them prioritize tickets as they look at what's in their case. We have a bunch of tickets although we have a lot less I have a lot less now and I made this. It was a lot of non-owned tickets. We're currently using a spreadsheet to track images. Let's see what we can do in the new world in Jira. First thing is, I've already changed our priority scheme to be P1 through P4. It's going to be mostly the same. I'm getting super criticals down for everybody. P2, something pretty important's broken. It's a cosmetic issue where I want to know how this works, it just doesn't really make sense. That's what a P4 will be. Kind of standard for those of you that have done support or engineering. We're going to try again. Try again using that case weight and a variety of other things to push the more important tickets to the top. We're going to have different ticket types for Incident, SOW, We're going to go through a few to make sure that we can clearly distinguish what these are. Case way that I talked about all We're going to make sure that tickets have owners and then we're going to be tracking So I'm tracking service disruptions or what this says is incidents. I know incident is a weird word to use here. We're going to be tracking outages, service disruptions in JIRA going forward, which is a process that Amy and I are working on currently. All right, active initiatives.

## Reunión 2026-06-10 — Four core pillars of support · Transcripción 13/16
_chunk 798 · 2026-06-10_

So we've got a few things in flight right now. We've got Project Agus, so if you ever hear me talking about this, for those of you that are nerds, you'll know that that is the Greek shield. Basically, this is a way to up-level Jira. We're talking about potentially taking RCS and RTS, putting them into one ticket type with different We're putting the case weight in there, a variety of different things, but basically So, we're basically kind of modernizing our JSM experience a bit. Before we do that, though, one of the things that I've done, and I want to make sure, please, L2 and L3 If you're working on another ticket, tune in right now. This is very important. So we've got a field that now every single RCS and RTS ticket This is a very important part of the process. Have a ticket that you're working on where it is not something that's broken. Sorry, Jayar, sorry, Jayar for interrupting. Can you move your, move your Move your mouse so we know which part of this slide you're talking. So, can you see my mouse? Yeah, can you see that? This one right here. So if you take a look at this, every ticket right now Right now, underneath team ownership and four time remaining should have change requested. So not the team ownership in more fields, the team ownership up in the top part. Miner change, and you'll see it has a tooltip, you can hover over the I. A minor change is 30 minutes or less worth of work. A major change is more than 30 minutes. 730 minutes worth of work. And a feature request is, the product doesn't do this in We don't do this at all, and we would need to make major changes to the product in order to make this work. L2 and L3, please go through every ticket that you have open over the course of the And that's the course of the next week. And validate, does it need to have this or not? This is important for all of us because this is part of that bucket of work where I'm trying Hey, this is how much of this we're actually doing.

## Reunión 2026-06-10 — Four core pillars of support · Transcripción 14/16
_chunk 799 · 2026-06-10_

I don't know if you guys know how much time we're spending And that's the time we're spending on this. So please help me, help you, help us. Go ahead, Amy. That change requested is not directly below the Team The team ownership. So make sure that you are double checking that more deep or more Or more fields tab on the right side. The last two tickets I looked at, it was is right near the bottom, just above root cause. So I mean, I mean, unfortunately, this is the way Jira works. These are going to be in a different spot on just about every ticket. Just search that more fields section and you'll see it. It's in there. If you don't see it, let me know and we'll search together. Thank you, Amy. And good call out. I would love to tell you that's That's one of the things we'll fix with part of this Jira project, but to your point, Jira's going to Jira. It's a great way to get the data to work with the people who are working with the community. You can pin it and it will bring it to the top. Perfect. Thank you. Perfect, thank you, Vlad. All right, so next up. Next up, after we get Project Aegis in place and we have Jira upleveled, I'm sure I'm sure a lot of you, if not all of you, have seen SupportTriage, the tool that matters We're going to be up-leveling that as well. We have an open position right now that we're looking for This is going to be a This is going to be a new way to help us get our tickets resolved faster. The goal would be to The goal would be that every new ticket that comes in, Talos looks behind the backend every ticket that we've had. We've had all of our documents and put some internal comment to make our troubleshooting easier. To payments point on an earlier meeting, that doesn't mean that we trust implicitly everything That's exactly everything that it says. We still have to do troubleshooting. We still have to do validation. This is a very simple process. I'll have one this soon. Looking forward to this. P1 through P4, I'm going to skip for now.

## Reunión 2026-06-10 — Four core pillars of support · Transcripción 15/16
_chunk 800 · 2026-06-10_

That's it for now because we already talked about it. I think we're running short on time. All right, focus for the rest of the month. ShadowBuddy pairing, please focus on Please focus on that if you have any questions, raise them up to your management team, any issues as well. Writing documentation, the more documentation The more documentation you can write, the easier it's going to be for your shadow buddies to come up to speed, the quicker they're going to start taking Start taking tickets out of the queue, and of course, Talos will benefit from this as well. I'm going to circulate a field list starting with the management This will be the new consolidated We look at combining RCS and RTS and getting rid of I'm getting rid of unused or unneeded fields, so I would like anyone's opinion that has anything Oncall is a new product, and it's not only available to anyone, but it's also available to anyone who has a Any documents we write are going to make this better and better than to be put in the right places. We're going to need to make sure that they get labeled correctly. Matt and I will work on that. This is something that is going to be incredibly important. AI is only as good as the documentation that's under it. If it's under it, LLM AI is only as good as the documentation that's under it. All right, team, with two whole minutes to spare, And I think that's what I've got to present to you today. Any questions, comments, or concerns on any of that? I will. Yep, I'll share the slides out with the team. And also Vlad had a... I had a question in the chat right above mine. Not all tickets, no. Only a ticket where it is not a... But basically, if you have to go modify something that a customer is asking you to modify that is not a break fix If you want a break fix ticket, that's where we want to put it in. Just a question.

## Reunión 2026-06-10 — Four core pillars of support · Transcripción 16/16
_chunk 801 · 2026-06-10_

Yeah, do we already have dashboard We have dashboards in Jira or we are also going to like you know prepare the dashboards based on We do have dashboards in Jira, they're all going to be up I'm going to be updated soon. Amy, I think you sent those over to Camilo already, but if you Let's see what we're looking at. Yep, absolutely. Awesome, thank you very much. Thank you very much. Thanks, Faraj. All right, team. We may expand this to an hour eventually. I want to try to be respectful. I'm glad to be respectful of everyone's time. We have a ton of meetings. I just think it's important to kind of give you an idea of what we're doing. We'll be able to get a little bit of a video of what we're working on, how we're working together, and then give you an opportunity to ask any questions. So anything else, just feel free to slack it to me. Sorry, teams it to me. And I hope everybody has a great day. Everybody has a great rest of the day ahead. Thanks, team. Thanks, everyone.

## Reunión 2026-06-12 — Delivery vs. Engineering responsibilities · Resumen
_chunk 862 · 2026-06-12_

## Resumen
The meeting focused on clarifying processes related to ticket triaging, team responsibilities, and documentation updates. Key points included the distinction between Delivery and Engineering responsibilities, with Shan playing a pivotal role in redirecting tickets based on her judgment. Delivery handles front-end, user interface, data mapping, and setup/configuration issues, while Engineering focuses on back-end issues and bugs. Gray areas in ticket triaging were acknowledged, and it was suggested that a formal guideline or checklist be created to address these ambiguities. Additionally, the team discussed the importance of reviewing existing documentation to ensure accuracy, particularly regarding Shan's process.

The conversation also touched on ticket management processes, including assignment, updates, and closure steps. It was noted that tickets marked as completed are monitored for seven days before being closed, with a suggestion to automate this process to reduce manual effort. The team emphasized the need for customer confirmation in complex cases to avoid escalations. Weekly grooming of tickets by Dean and Kristin was discussed, highlighting their roles in ensuring timely updates and resolution. Dean reviews tickets with no updates for 14 days, while Kristin focuses on incident tickets open for over 60 days.

Other topics included the historical use of account service levels to prioritize tickets based on customer importance, though this practice appears outdated. The team also briefly discussed the 'ready to' status on tickets, which remains unclear and requires further investigation. The meeting concluded with light-hearted exchanges about upcoming vacations, signaling the end of the session.

## Temas clave
- Delivery vs. Engineering responsibilities
- Ticket triaging and management
- Documentation updates and accuracy

## Decisiones
- **Tickets marked as completed will be monitored for seven days before closure.** — To ensure customer confirmation and avoid escalations.

## Tareas / Action Items
- Check existing documentation on Shan's process for accuracy and update if necessary. (resp: null) — vence 2026-06-12
- Create a guideline or checklist for triaging tickets between Delivery and Engineering, including examples of gray areas. (resp: null) — vence null
- Investigate the 'ready to' status on tickets and clarify its meaning. (resp: null) — vence null
- Automate the ticket closure process after the seven-day completion period. (resp: null) — vence null

## Insights en vivo (Ask AI / Analizar)
### [Ask AI] hare esta pregunta -> Delivery vs. Engineering responsibilities are defined, but who decides feasibility/billable when Engineering, Delivery and CSM disagree? , despues de que me repsondan analiza el trnacript y dime que coloco en la repsuesta en ingles.  dame la repsuesta en ingles no en espanol
Lo que entiendo es que la decisión sobre si algo es factible o billable cuando hay desacuerdo entre Engineering, Delivery y CSM no se mencionó directamente en la explicación. Sin embargo, parece que hay un proceso informal donde Shan (Shandana) revisa los tickets de Engineering y, si considera que pertenecen al Delivery team, los redirige. Esto sugiere que la decisión inicial sobre la asignación de responsabilidades puede depender de la experiencia y juicio de personas clave como Shan, pero no se aclaró cómo se maneja específicamente el desacuerdo entre equipos ni quién tiene la última palabra en temas de factibilidad o costos.

- **Puntos clave**:  
  - Shan revisa todos los tickets de Engineering y redirige aquellos que cree que son más apropiados para el Delivery team.  
  - Hay áreas grises en la asignación de tickets, especialmente cuando no está claro si algo pertenece a Engineering, Delivery o incluso CSM.  
  - No se mencionó un proceso formal para resolver desacuerdos sobre factibilidad o costos entre los equipos.  

- **Dudas / lo que falta**:  
  - ¿Existe un proceso formal para resolver desacuerdos entre Engineering, Delivery y CSM?  
  - ¿Quién tiene la autoridad final para decidir si algo es factible o billable?  
  - ¿Cómo se documentan estas decisiones para evitar confusiones futuras?  

- **Próxima pregunta a hacer**:  
  "Could you clarify the formal process, if any, for resolving disagreements between Engineering, Delivery, and CSM regarding feasibility and billable work? Who has the final authority in such cases?"  

- **Conexión con tu documentación**:  
  Esto se relaciona con los procesos de escalación y asignación de tickets en Appriss KT, específicamente en cómo se manejan las áreas grises y los conflictos de responsabilidad. Podría ser útil incluir esta información en el tracker de documentación bajo un tema relacionado con la gestión de conflictos interdepartamentales.

### [Ask AI] hare esta pregunta -> Delivery vs. Engineering responsibilities are defined, but who decides feasibility/billable when Engineering, Delivery and CSM disagree? , despues de que me repsondan analiza el trnacript y dime que coloco en la repsuesta en ingles.  dame la repsuesta en ingles no en espanol
Based on what was explained, the decision-making process for feasibility or billable work when Engineering, Delivery, and CSM disagree seems to rely heavily on informal judgment rather than a formalized process. Shan (Shandana) reviews all Engineering tickets and redirects those she believes are more appropriate for Delivery, indicating that she plays a key role in resolving these gray areas. However, it wasn't clarified who has the final authority in cases of disagreement or whether there is a documented guideline for such scenarios. It appears that the division of responsibilities is based on whether the issue pertains to front-end, back-end, data mapping, or initial setup/configuration, but the process for resolving disputes remains ambiguous.

- **Puntos clave**:  
  - Shan reviews Engineering tickets and redirects them to Delivery if she deems it appropriate.  
  - Responsibilities are divided based on the nature of the issue: front-end (Delivery), back-end (Engineering), data mapping (Delivery), and initial setup/configuration (Delivery).  
  - There are still gray areas where it’s unclear whether an issue belongs to Engineering or Delivery.  

- **Dudas / lo que falta**:  
  - Is there a formal process for resolving disagreements between Engineering, Delivery, and CSM?  
  - Who has the final authority in deciding feasibility or billable work?  
  - Are these decisions documented to ensure consistency?  

- **Próxima pregunta a hacer**:  
  "Could you clarify if there’s a formalized process or guideline for resolving disputes between Engineering, Delivery, and CSM regarding feasibility and billable work? Who ultimately decides in such cases?"  

- **Conexión con tu documentación**:  
  This ties into the broader topic of ticket triage and responsibility assignment, which is covered in the documentation tracker under "Appriss KT — Topic 1." It’s important to ensure this process is clearly documented for future reference.

### [Ask AI] alguna sugerencia para crear lo faltante referente a este tema, el ultimo tema que se esta hablando?
"Could we create a clear guideline or checklist for triaging tickets between Delivery and Engineering? Specifically, it should cover how to identify front-end, back-end, data mapping, and setup/configuration issues, and include examples of gray areas where Shan typically intervenes. Also, could we validate whether the existing documentation on Shan's process is still accurate or needs updating?"

- **Puntos clave**:  
  - Shan reviews all Engineering tickets and redirects those she believes belong to Delivery.  
  - Delivery handles front-end, user interface, data mapping, and setup/configuration issues.  
  - Engineering handles back-end issues and bugs.  
  - There are gray areas in ticket triaging, often resolved by Shan's judgment.  
  - Existing documentation on Shan's process may be outdated or incomplete.  

- **Dudas / lo que falta**:  
  - Is there a formalized checklist or guideline for triaging tickets?  
  - How are gray areas documented to ensure consistency in decision-making?  
  - What specific examples of gray areas could be included in the guideline?  

- **Próxima pregunta a hacer**:  
  "Could you provide examples of tickets that fall into gray areas between Delivery and Engineering, and how Shan typically resolves them?"  

- **Conexión con tu documentación**:  
  This ties into the broader topic of ticket triaging processes and responsibilities between teams, which should be documented in the "Appriss KT — Topic 1" folder for clarity and training purposes.

### [Ask AI] analiza la repsuesta de la ultima pregunta que se hizo y estan respondiendo, ya sea preguntar o sugeror o aportar algo con sentido.
"Could we clarify the best practices for reaching out to Engineering without assigning the ticket directly? For example, should we always use app mentions in the ticket, or is there a preferred protocol for ensuring visibility and timely responses? Also, is there a documented guideline for this process, or should we create one based on current practices?"

- **Puntos clave**:  
  - App mentions in tickets are recommended for reaching out to Engineering without assigning the ticket.  
  - Assigning tickets to Engineering is still a relatively new process and not fully standardized.  
  - There’s ambiguity about whether app mentions alone are sufficient for visibility.  

- **Dudas / lo que falta**:  
  - Is there a formal guideline for reaching out to Engineering without assigning tickets?  
  - How can we ensure timely responses from Engineering when using app mentions?  
  - Should we document this process to avoid inconsistencies?  

- **Próxima pregunta a hacer**:  
  "Could you confirm if there’s a documented protocol for app mentions and ticket assignment when involving Engineering? If not, should we draft one based on current practices?"  

- **Conexión con tu documentación**:  
  This ties into the broader topic of escalation protocols and communication standards between Support and Engineering. It may require cross-referencing existing documentation on ticket triaging and escalation processes.

### [Ask AI] entramos en esta seccion -> 4 of 16 ·  T-004 — Personal queue grooming + Kanban prep 

Reference  trebuco.atlassian.net/wiki/spaces/RTS/pages/475023081474 

QUESTIONS 

How do you decide a ticket needs a Tiger Team vs normal grooming? 

si tienes alguna sugerencia o aporte a su respuesta, en ingles.
"Could we clarify the criteria for escalating a ticket to the Tiger Team versus handling it through normal grooming? For example, is it strictly based on the ticket's age (e.g., 60 days for incidents), or are there other factors like complexity, customer impact, or repeated escalations that trigger Tiger Team involvement? Also, how do we ensure consistency in these decisions across the team?"

- **Puntos clave**:  
  - Tiger Team reviews tickets open for longer than 60 days, focusing on incident-type tickets.  
  - Dean monitors tickets with no updates for 14 days and follows up with assignees or customers.  
  - Kristen handles tickets older than 60 days, checking status and reaching out as needed.  
  - Current process lacks documented criteria for Tiger Team escalation beyond ticket age.  

- **Dudas / lo que falta**:  
  - Are there additional criteria beyond ticket age for Tiger Team involvement?  
  - How is complexity or customer impact factored into escalation decisions?  
  - Is there a documented guideline for Tiger Team escalation?  

- **Próxima pregunta a hacer**:  
  "Could you provide examples of tickets that were escalated to the Tiger Team due to factors other than age, and explain the reasoning behind those decisions?"  

- **Conexión con tu documentación**:  
  This relates to T-004 — Personal queue grooming + Kanban prep and the broader topic of ticket management processes. It may require updating the documentation to include Tiger Team escalation criteria.

### [Ask AI] entramos en esta seccion -> 4 of 16 ·  T-004 — Personal queue grooming + Kanban prep 

Reference  trebuco.atlassian.net/wiki/spaces/RTS/pages/475023081474 

QUESTIONS 

How do you decide a ticket needs a Tiger Team vs normal grooming? 

si tienes alguna sugerencia o aporte a su respuesta, en ingles.
"Could we clarify the specific criteria for deciding when a ticket requires Tiger Team intervention versus normal grooming? For instance, beyond the 60-day threshold for incidents, are there other factors like ticket complexity, customer priority, or repeated escalations that influence this decision? Additionally, how do Dean and Kristen coordinate to ensure consistency in these escalations?"

- **Puntos clave**:  
  - Tiger Team focuses on tickets open for more than 60 days, specifically incident-type tickets.  
  - Dean monitors tickets with no updates for 14 days and follows up with assignees or customers.  
  - Kristen handles tickets older than 60 days, ensuring they progress towards resolution.  
  - Decision-making for Tiger Team involvement seems primarily age-based but lacks documented criteria for other influencing factors.  

- **Dudas / lo que falta**:  
  - Are there additional criteria beyond ticket age for Tiger Team involvement?  
  - How do Dean and Kristen ensure alignment in their processes?  
  - Is there a documented guideline for Tiger Team escalation decisions?  

- **Próxima pregunta a hacer**:  
  "Could you provide examples of tickets escalated to the Tiger Team due to factors other than age, and explain the reasoning behind those decisions?"  

- **Conexión con tu documentación**:  
  This ties into T-004 — Personal queue grooming + Kanban prep and the broader topic of ticket management workflows. It may require cross-referencing the RTS documentation for escalation protocols.

### [Ask AI] algo que aportar??
"Could we explore whether the Tiger Team criteria should include factors beyond ticket age? For example, could complexity, customer priority, or repeated escalations also trigger Tiger Team involvement? Additionally, do Dean and Kristen have any documented triaging guides or best practices for grooming the backlog that we could review?"

- **Puntos clave**:  
  - Tiger Team focuses on tickets older than 60 days, specifically incident-type tickets.  
  - Dean monitors tickets with no updates for 14 days, ensuring follow-ups with assignees or customers.  
  - Kristen handles tickets older than 60 days, reviewing status and pushing for resolution.  
  - The decision-making process for Tiger Team involvement appears primarily age-based, with no mention of other criteria like complexity or customer impact.  
  - Suggestion to reach out to Dean and Kristen for insights into their operational methods and triaging guides.  

- **Dudas / lo que falta**:  
  - Are there additional criteria for Tiger Team involvement beyond ticket age?  
  - Do Dean and Kristen have documented processes or guides for backlog grooming?  
  - How do they ensure consistency in their approaches?  

- **Próxima pregunta a hacer**:  
  "Could you share any documented triaging guides or criteria Dean and Kristen use for backlog grooming and Tiger Team escalation?"  

- **Conexión con tu documentación**:  
  This ties into T-004 — Personal queue grooming + Kanban prep and the RTS documentation on Tiger Team processes.


---

## Reunión 2026-06-12 — Delivery vs. Engineering responsibilities · Transcripción 1/8
_chunk 863 · 2026-06-12_

## Transcripción completa
Just anything having to do with the actual transaction. All transactions is going to be the data team. Is asking about a report. Here's another caveat. The data team is Secure 5 only. One thing when you're looking through these tickets is if it's an incident, a secure incident ticket. For the incident product, you don't need to worry about the data team because that's, you know, they only work secure five. You can get 1,000 or 5 tickets. So that's number 1. Then number 2, you look at it and determine if it's If it's data related or not, and then if it is, then we have to add the label of support data team. So, this is the session that you're going to have with Juan next week since you're going to be recording it. I know that is here in your mind, so maybe write it down is going to be difficult. So I'm going to take the transcript, put it into a clock and say, hey, I need a guideline for someone that have never done I'm not sure if you've ever done this and I need that. You capture everything, any steps that you follow, everything so you can review it and see if that is accurate. I know that you are doing something because you know it. Yes, yes. So, yeah, if we can make sure that in that session, of course, we review them. We reviewed the backlog and the queue and we touched base on it specifically. among the people, depend on specific Leadtable data. How to change if you really review like how to change if it's an SOW to incidents and the other way around. So like we can capture and maybe make a good guide on how you triage the queue. Absolutely. Great. We have everything for that, right? Yeah. Or maybe like we charted. I'm going to start the checkboxes to make sure that it is correctly moved on. Oh God. Right. Again, this is kind of one of those. And there are gray areas still to this day that some people, it's like, I don't know if this is going to I don't know if this is going to be delivery.

## Reunión 2026-06-12 — Delivery vs. Engineering responsibilities · Transcripción 2/8
_chunk 864 · 2026-06-12_

I don't know if this is going to be engineering. There are just times when that happens and we just have to send it to one team. They look at it and go, oh, And this happens a lot. We send it to engineering. Shan looks at every engineering ticket. Shandana. And she's getting pretty good at knowing. I think this is a very good question. I think this is more for the delivery team, okay? And she'll send it to the delivery team. But so it right now, Right now, it's just a matter of, okay, is it the front end? Is it user interface? Is it interface, is it backend, where, or is it code? Okay. And anything having to Having to do with the data mapping and the The setup and configuration of the product, that's going to be delivery. And truly back end, you know, that it's going to be engineering. Could you please repeat that back? Anything having to do with the initial setup and configuration of the product. With the user interface, anything having to do with data mapping, anything Anything having to do with the product itself And the user using the product. OK. That's going to be great. That's going to be delivery. Whereas anything that is more of a bug is it's something that's more broken. If you're more broken, that's going to be engineering. Okay. Got it. Jam reviews every engineering ticket. I think we can through EA. I know that is a process that they do because they know it, but you know that is a human Is that your document anywhere? It is not that I... Well... Let me double check that. I know there's a document in there, but I'm not sure if I'm not sure if it's really valid anymore. Okay, so let me double check that. At this point in time, I'm going to This time I'm gonna say no, it's not, but, shan process. Making a note. What is our understanding so they can review it and say, yes, it is correct, this is missing. because, again, our aim is to take over a lot and not say hey, we need the document of these, we need a note. We need to know if it doesn't exist.

## Reunión 2026-06-12 — Delivery vs. Engineering responsibilities · Transcripción 3/8
_chunk 865 · 2026-06-12_

We created understanding what it is so you guys can sign up and say if it's right or wrong because the amount of work is Love work, you seem the same. Yeah. Agreed. Maybe our understanding, so if the ticket has this, and this, absolutely goes to delivery. We can create it of what we understand, also review in the queue like Like you're like, hmm, this is like in a gray area. Should be this or this so we can understand We can understand the process, the thinking process, and then we can go out and say, hey, is this Is this accurate? Is something that you think we should take into account on this triage? And that's it. That's it. But Amy said that maybe there is a document. So if it is, that's great. And if it's not, we can create it from our understanding. How are you understanding? Yeah, I will check for that this afternoon and let you know. Great. Perfect. Is there, like, it says that get help from engineering without assigning the ticket to them? How that it works? Like, if I'm waiting for engineering answer, maybe I communicate with the customer and say, hey, I'm reaching Reaching out to engineering, that should pause this late, of course, if they don't get back. But there is anywhere that is struck that we That we reach out to engineering. Yeah, it's... Doing an app mention in the ticket if you know the person in engineering you want to reach out to. I recommend always doing both. This is a very important part of the conversation. Assigning the ticket, that's a new thing for us and we're still assigning tickets to engineering. It's a, but if you're not going to be assigning the ticket And if you're looking for a way to take it to the engineer, then yeah, they're definitely not going to see the app mention in the And then, in the ticket, so the team's message is going to be the best way to reach out to them. And of course, the SLA will depend on the communication Any questions you have about that? How about that? One, besides that. Great.

## Reunión 2026-06-12 — Delivery vs. Engineering responsibilities · Transcripción 4/8
_chunk 866 · 2026-06-12_

It would be Teams messages. Also send the team's message so you ensure that they are aware because as you maybe saw. To get a bunch of emails of AppDix in Kira so you can miss it. And a lot of them have those emails from Jira. Like they have a skill set like anything that says Jira, please keep my Keep my e-books. Yes. Yeah. Put it in this file over here and I'll never look at it again. I'll never look at it. Yeah. Okay, so the next one that was in the same topic is This is the RCS ticket management process, so assignment updates and closure steps. So, and I think we already touched base on this and you correct me that after is complete. This completed the customer must confirm that it was resolved so then we can close it. So is there any Bambam solving in place? If we don't hear from the customer, only the one that you told me, that is seven days and give them Thank you for the 21 days more. Right. What we have done is The canned response is, when we complete a ticket, it's dead. It states, we're gonna complete this, as far as we're concerned, as far as we can see, this is recently This is resolved, so I'm going to go ahead and mark it as complete, and if I don't hear back from you within one week, then we'll move it to closed. Okay. Okay. And so we We watch in the dashboard, we have the section for Tickets in completed status. And so everybody watches that and once it hits, you know, six days or seven days since And we'll go in and just close it. We don't... And wait. Right, and it doesn't, it's not a hard and fast rule, at least it's not documented at this point in time, that a customer The customer must confirm that it's resolved before we close it. Again, we can still close it. Let them know as far as we're concerned it's closed, but if you see, you know, if you have any further issues, I think we can create a Vault. About that, just provide like a ping.

## Reunión 2026-06-12 — Delivery vs. Engineering responsibilities · Transcripción 5/8
_chunk 867 · 2026-06-12_

Next day, Next day, I mean 24 hours, then 48 hours, and maximum 7 to 2 hours, and then close it automatically. We will be able to do this very quickly so we don't have to do it manually. Yeah. Yeah. That will come. Yeah, right now we just do it as a courtesy to customers. We're asking for customers when we're asking for them to confirm. It's just like a safety check, just to avoid further escalations and everything. And also like that will depend on... And on how as support people, the file I hate. This is a really complicated case, this was really tough, so we're not going to close anything until then. Until they confirm, hey, we're okay. Yeah, it will depend and we will learn not to check Check-in out tickets and all that. Okay, great. Another topic. The next one, it says, Personal Grooming and Combat Progression. I just opened that point. Entire team, yeah. Okay, we have a Tiger team. Weekly report of tickets. But it's been so long. I want to say hers is we have two There are two types of reports that go out. One goes to Dean. He reviews all tickets that have not had a response in In 14 days. Or haven't had an update, rather, in 14 days. Oncall, oncall, oncall, oncall, It's been sitting for 14 days with no update on it whatsoever. He's looking at the ticket and poking whoever he needs to poke, whether it be the assignee saying, hey, what's going on with this ticket? Or sending a reminder to the So, I'm going to go ahead and add a link to the customer. Kristen is looking at tickets that I can't remember off the top of my head if it's 30 or 60 days. Hold on one quick second. Okay, it's 60 days. So, currently the Tiger team, she looks at all reports, or all tickets that have been That has been opened for longer than 60 days. Okay. And incident only. She looks at incident-type tickets only. And just as a follow up right now, it looks like we've got We've got 35 tickets that have been open longer than 60 days.

## Reunión 2026-06-12 — Delivery vs. Engineering responsibilities · Transcripción 6/8
_chunk 868 · 2026-06-12_

So she'll go through the See what the status is, see who the assignee is, and just kind of And if needed, she'll reach out to me and I'll be able to reach out to her. We'll reach out to the assignee, to the customer to just make Just trying to get that ticket to move along so that we can get it closed and resolved, or resolved and closed. And I like to that like, Like which are the capabilities or expertise of Dean and Chris. And then, like, why they are, like, grooming the 60 and the 14 days. Because he's the lead support, so he's been basically the supervisor for support. We're going to go ahead and do a little bit of a quick look at the report. So he's just making sure that all of our tickets are moving along as they show. As they should. Kristin is... For lack of a better way of putting it, she's my right hand. I'm going to use my right hand. She just makes sure that everything in support The support is moving along and is getting the attention that it We have a lot of questions. And that's just a title that JR's predecessor came up with. Yeah, so, but truly, I mean, she... Everyone in the company knows Kristen. Comes to Kristen with questions and yeah, so that's why she got She's my right hand. I needed somebody to do this. You should guys reach out to Christine and Dean to understand how they deal with the operation. I have some background I have some background on engineer, but I will not be hands-on in operations. So sometimes I will miss things out. I'm going to go through the slides and then we'll go through the slides. We will be talking about the future of the project. If you are hint on not only how things work, but also how they touch. They tackle these kind of reports, maybe if they have any triaging guides. Guides or any idea of how they groom the back look, that would be great. Agreed. For you two guys to understand that. Agreed, for sure. I think that next week that I'm not here and I just erased all the meetings I did.

## Reunión 2026-06-12 — Delivery vs. Engineering responsibilities · Transcripción 7/8
_chunk 869 · 2026-06-12_

I did it for you guys, you will have more time, so maybe that is the time for you. Yeah, and if you'd like, I mean, I can help set those up as well. That will be great. Yeah, I can set those up if you'd like. I can set that meeting up. For this particular Tiger team, it is just the age of the I'm not sure if it's a good idea to do that. I believe JR now calls them SWAT teams, whereas, you know, when, like yesterday, when we were having all of that Waitrose, Craziness. Everyone we brought in together would have been considered We've been considered either a Tiger team or a SWAT team or just the team that's going to... You know, really dive into that particular issue. So, but the documentation that The presentation that you see in there for Tiger Team is specifically around this report. Reports, those are in Jira, Relay in Jira. Yes, they are in Jira. Okay, I think that adding those on Confluence could be useful, like the links, so maybe... So like for last past 14 days age, past 60 days age, I will review those and see what information is That will be great. Sure, absolutely. And you told us how often these groomers This grooming is done by them. Sorry. This weekly, like the cadence. We're not sure exactly that they're looking at this. Sometimes it's dependent on availability of their time. And like, daily grooming is done by... By each engineer, so they should be growing their own backlog and things like that. Yes. That is the expectation. Okay. I already said something about it is organized via account service level. What does it mean? What does it mean? That used to be the case. We used to have, and you'll see, On some tickets, account service level, we used to have The reason why I'm so surprised is because I'm so surprised We'll say TJX is a white glove. Lululemon would be a white glove. Customers, they need a lot of attention. And they pay us a lot of money. It's mostly based on what they pay us, okay, the accounts for I'm not sure if that's the right answer.

## Reunión 2026-06-12 — Delivery vs. Engineering responsibilities · Transcripción 8/8
_chunk 870 · 2026-06-12_

I'm going to take a question for Kara and Libby. And maybe J.R. may know as well. Well, it's been a long time since we've done anything about account service levels. Yeah. And also there was like status on the ticket that it says ready to This is a very important topic for us. What does it mean? Because let me just, because of your face. Let me just recall exactly what I'm seeing. That is something I'm not aware of. Now I can have found it. Of course. Yeah, but we saw that somewhere, right? We couldn't contain that from nowhere. We're going to ask something that does not exist. I'm gonna throw this at her and see what she says. Yeah, I kind of find it to be pretty. To be pretty honest with you. And then we are already over time. So I think we can left that one. We can revisit that later. Thank you again for all your answers. All your answers and your... Absolutely. To be really nice with us always. And yeah, see you in two weeks because I'm gonna see you. I'm going to see you next week, so enjoy your yearning also and your long weekend. We can. Yes, thank you. And I hope you enjoy your time away. You're doing something fun. I'm going to Jamaica with my girlfriends. I'm going to see when I'm get back. No worries. I went to Jamaica. Which part of Jamaica are you going? That is a really good question. I haven't had the time to review this because of the workload. These vacations will be only to rest. Yes, and that's smart in Jamaica especially. There is one area, I went to Montego Bay, absolutely. Is that where you're going? Perfect. Absolutely beautiful. This is a great time of year to go. So I'm jealous. I want to get back there. So. Yeah, maybe I can give you an idea. Thank you for your next vacations. When I was there, they talked me into joining a vacation club for all-inclusive resorts. Enjoy that. Thank you so much. Have a pineapple drink on me. Yeah, we'll do. Thank you so much. Thank you so much. All right. Thank you. See you. Talk to you guys soon. Bye-bye.

## Reunión 2026-06-10 — Acknowledgment vs. resolution timelines · Resumen · Parte 1/15
_chunk 898 · 2026-06-10_

## Resumen
The discussion focused on setting realistic expectations for technical support processes, particularly regarding acknowledgment and resolution timelines. The standard for acknowledgment is 30 minutes, but resolution times vary based on ticket complexity and priority. Concerns were raised about committing to unrealistic KPIs, which could lead to team burnout and dissatisfaction. The speaker emphasized the need for gradual changes, allowing time for the team to gain technical expertise and adapt to new processes. JR's input is awaited to finalize adjustments to metrics like time to closure, resolution rates, and CSAT scores. The importance of shadowing and reverse shadowing was highlighted as a way to onboard new team members effectively. Automation opportunities were mentioned but require pattern observation over time. Open questions include how acknowledgment standards are defined and how complex cases are managed within the current workflow.

## Temas clave
- Acknowledgment vs. resolution timelines
- Realistic KPIs for support team
- Shadowing and onboarding processes

## Decisiones
- **Gradual changes to KPIs and processes are preferable to avoid overwhelming the team.** — Concerns about team burnout and unrealistic expectations

## Tareas / Action Items
- Await JR's input on realistic KPIs and process adjustments.
- Schedule weekly meetings with the India team to track progress and address concerns. (resp: Speaker) — vence 2026-06-13
- Document acknowledgment vs. resolution expectations in a shared resource.

## Reunión 2026-06-10 — Acknowledgment vs. resolution timelines · Resumen · Parte 2/15
_chunk 899 · 2026-06-10_

## Insights en vivo (Ask AI / Analizar)
### [Ask AI] (sin pregunta)
Lo que entiendo es que el interlocutor está hablando sobre la importancia de establecer expectativas realistas en el soporte técnico, especialmente en cuanto al tiempo de respuesta inicial. Mencionó que el estándar observado es dedicar 30 minutos para reconocer el problema, pero no necesariamente para resolverlo. También expresó preocupación por comprometerse con plazos que podrían ser poco realistas, lo que podría generar presión innecesaria en el equipo. Además, señaló que algunos casos requieren análisis técnico detallado o enfrentan brechas de conocimiento, lo que puede complicar el cumplimiento de tiempos establecidos. Parece que están esperando la opinión de JR para ajustar cualquier cambio en los procesos actuales, asegurándose de que sean prácticos y aceptables para el equipo.

- **Puntos clave**:  
  - 30 minutos es el estándar para reconocer un problema, no necesariamente para resolverlo.  
  - Evitar comprometerse con plazos poco realistas para no generar presión en el equipo.  
  - Algunos casos requieren análisis técnico detallado o enfrentan brechas de conocimiento.  
  - Se espera la opinión de JR para ajustar los procesos de manera realista.

- **Dudas / lo que falta**:  
  - ¿Qué cambios específicos están considerando en los procesos actuales?  
  - ¿Qué rol tiene JR en la toma de decisiones sobre estos ajustes?  
  - ¿Cómo se manejan los casos que requieren análisis técnico detallado en el flujo actual?

- **Próxima pregunta a hacer**:  
  "¿Podrías detallar cómo se define el estándar de los 30 minutos para reconocer un problema y cómo se diferencia de los tiempos de resolución en casos más complejos?"

## Reunión 2026-06-10 — Acknowledgment vs. resolution timelines · Resumen · Parte 3/15
_chunk 900 · 2026-06-10_

- **Conexión con tu documentación**:  
  Esto se relaciona con los temas de T-071 Update Rate compliance y T-003 Aged ticket close-out, ya que ambos implican establecer expectativas claras sobre tiempos de respuesta y resolución. También podría conectar con T-005 Customer escalation playbook si los plazos afectan la escalación al cliente.

### [Ask AI] que puedo decir depsues de esto?
Thanks for sharing that perspective. I completely agree that setting realistic expectations is key, both for the team and for the customers. Acknowledging the issue within 30 minutes makes sense as a standard, but I also see how committing to resolution timelines upfront could create unnecessary pressure, especially for cases requiring deeper technical analysis or when there are knowledge gaps. I’d be curious to hear JR’s thoughts on how we balance this—acknowledging quickly while still allowing flexibility for complex cases. Also, are there specific scenarios or ticket types where you’ve seen this tension play out the most?

- **Follow-up questions to ask**:  
  - "What’s the current process for handling tickets that require detailed technical analysis? Are there any specific guidelines or exceptions?"  
  - "How do we currently communicate acknowledgment versus resolution timelines to customers? Is there a standard phrasing or SLA?"  
  - "Are there any metrics or feedback loops in place to track whether the acknowledgment standard is being met consistently?"

- **Related topics**:  
  - T-071 Update Rate compliance: Ensuring weekly updates without overpromising.  
  - T-003 Aged ticket close-out: Handling tickets that exceed standard timelines.  
  - T-005 Customer escalation playbook: Escalation triggers for complex cases.

- **Potential risks to flag**:  
  - Unrealistic commitments could lead to customer dissatisfaction or team burnout.  
  - Knowledge gaps might require additional training or documentation updates.

## Reunión 2026-06-10 — Acknowledgment vs. resolution timelines · Resumen · Parte 4/15
_chunk 901 · 2026-06-10_

- **Next steps**:  
  - Wait for JR’s input to align on realistic standards.  
  - Suggest documenting acknowledgment vs. resolution expectations in a shared resource (e.g., Confluence).

### [Ask AI] que esta diciendo? y como puedo aportar algo?
It sounds like you're emphasizing the importance of distinguishing acknowledgment from resolution timelines, especially when dealing with complex tickets or scenarios that require detailed technical analysis. I completely agree that committing to unrealistic timelines upfront can put unnecessary pressure on the team and lead to challenges in execution. I also appreciate the point about prioritization—how P1 tickets naturally demand faster resolution due to their wider impact, while lower-priority tickets might require more flexibility. I'd be curious to hear more about how we currently balance acknowledgment standards with realistic resolution expectations across different priority levels. Are there any specific metrics or processes in place to ensure this alignment?

- **Key points from the transcript**:  
  - Acknowledgment within 30 minutes is standard, but resolution depends on ticket complexity and priority.  
  - P1 tickets have tighter resolution timelines due to their impact, while P3/P4 tickets allow more flexibility.  
  - Complex scenarios often require detailed technical analysis or face knowledge gaps, which can extend resolution times.  
  - The speaker is hesitant to commit to changes without ensuring they’re realistic and widely adoptable.

- **How you can add value**:  
  - Highlight the importance of realistic timelines for team morale and customer satisfaction.  
  - Ask about current processes for handling tickets requiring detailed analysis or repro steps.  
  - Suggest reviewing metrics or feedback loops to track acknowledgment and resolution performance.

## Reunión 2026-06-10 — Acknowledgment vs. resolution timelines · Resumen · Parte 5/15
_chunk 902 · 2026-06-10_

- **Follow-up questions to ask**:  
  - "What’s the current process for prioritizing tickets in the queue? Are there clear guidelines for balancing acknowledgment and resolution timelines?"  
  - "How do we handle scenarios where knowledge gaps delay resolution? Is there a mechanism for escalating or documenting these cases?"  
  - "Are there any tools or dashboards that help track acknowledgment and resolution KPIs across priority levels?"

- **Related topics**:  
  - T-071 Update Rate compliance: Ensuring weekly updates without overpromising.  
  - T-003 Aged ticket close-out: Handling tickets that exceed standard timelines.  
  - T-005 Customer escalation playbook: Escalation triggers for complex cases.

This approach keeps the conversation constructive and focused on aligning processes with realistic expectations.

### [Ask AI] aporta una respuesta de conclusion o valor a lo que esta diciendo
Thanks for sharing all of that—it’s really helpful to hear your perspective on balancing acknowledgment and resolution timelines. I completely agree that the KPIs we set need to be realistic and grounded in what the team can actually deliver, especially given the complexity of some tickets and the knowledge gaps that can arise. I also think prioritization is key, not just based on ticket priority but also factoring in customer impact and urgency. One thing I’d be curious about is whether we have any documented guidelines or frameworks for prioritizing tickets at the start of the day—something that helps engineers quickly identify what needs immediate attention versus what can wait. That could be a useful tool for ensuring consistency across the team.

- **Key points to reinforce**:  
  - Realistic KPIs prevent unnecessary pressure and ensure team-wide adoption.  
  - Prioritization should balance ticket priority, customer impact, and urgency.  
  - Complex tickets often require detailed analysis, which can extend resolution times.

## Reunión 2026-06-10 — Acknowledgment vs. resolution timelines · Resumen · Parte 6/15
_chunk 903 · 2026-06-10_

- **Follow-up questions to ask**:  
  - "Do we have a documented prioritization framework for engineers to use daily?"  
  - "Are there specific metrics or feedback loops in place to evaluate acknowledgment and resolution performance?"  
  - "How do we currently handle tickets with knowledge gaps—are there escalation paths or resources available?"

- **Potential next steps**:  
  - Suggest reviewing existing prioritization guidelines or creating a framework if none exists.  
  - Explore whether acknowledgment standards are consistently met across different ticket types.  
  - Discuss how to address knowledge gaps systematically, perhaps through training or documentation updates.

- **Related topics**:  
  - T-004 Queue grooming + Kanban prep: Ensuring prioritization aligns with team capacity.  
  - T-071 Update Rate compliance: Balancing acknowledgment and resolution expectations.  
  - T-005 Customer escalation playbook: Handling complex tickets effectively.

### [Ask AI] aporta una respuesta de conclusion o valor a lo que esta diciendo
It sounds like you're emphasizing two key points here: first, the importance of realistic KPIs that the team can actually follow at the ground level, and second, the need for prioritization frameworks that help engineers focus on the most impactful tickets at the start of their day. I completely agree that resolution timelines should depend on ticket complexity and priority, especially for P1 issues where the impact is widespread. One thing I’d add is that having clear prioritization guidelines—whether based on customer tier, urgency, or escalation status—can really help streamline decision-making and reduce pressure on the team. I’d be curious to hear if there’s already a documented process for this, or if it’s something we could refine together.

## Reunión 2026-06-10 — Acknowledgment vs. resolution timelines · Resumen · Parte 7/15
_chunk 904 · 2026-06-10_

- **Key points to reinforce**:  
  - KPIs must be realistic to ensure adoption and avoid unnecessary pressure.  
  - Prioritization should factor in ticket priority, customer tier, and urgency.  
  - P1 tickets understandably demand faster resolution due to their wider impact.

- **Follow-up questions to ask**:  
  - "Do we currently have a documented prioritization framework for engineers to use daily?"  
  - "How do we handle tickets that require detailed technical analysis or face knowledge gaps?"  
  - "Are there specific metrics or feedback loops in place to evaluate acknowledgment and resolution performance?"

- **Potential next steps**:  
  - Suggest reviewing existing prioritization guidelines or creating a framework if none exists.  
  - Explore whether acknowledgment standards are consistently met across different ticket types.  
  - Discuss how to address knowledge gaps systematically, perhaps through training or documentation updates.

- **Related topics**:  
  - T-004 Queue grooming + Kanban prep  
  - T-007 Ticket lifecycle ownership map  
  - T-092 Priority — current state

## Reunión 2026-06-10 — Acknowledgment vs. resolution timelines · Resumen · Parte 8/15
_chunk 905 · 2026-06-10_

### [Ask AI] aporta una respuesta de conclusion o valor a lo que esta diciendo
It sounds like you're highlighting two critical aspects here: first, the importance of realistic KPIs that align with the team's current level of familiarity with the product, and second, the need for a structured transition period where shadowing and reverse shadowing help us gradually build technical depth. I completely agree that resolving issues efficiently will depend on recognizing patterns over time and developing a deeper understanding of the system. The idea of prioritizing tickets based on urgency, customer tier, and escalation status also makes a lot of sense—it ensures we're focusing on the most impactful work first. One thing I’d add is that setting clear expectations for this transition period, including milestones for shadowing and independent ticket handling, could help us track progress and identify areas where additional support or training might be needed.

- **Key points to reinforce**:  
  - KPIs should reflect the team's current learning curve and technical depth.  
  - Shadowing and reverse shadowing are essential for building familiarity with the product.  
  - Ticket prioritization should balance urgency, customer tier, and escalation status.

- **Follow-up questions to ask**:  
  - "Do we have specific milestones or metrics to track progress during the shadowing phase?"  
  - "How do we ensure that the transition to independent ticket handling is smooth and well-supported?"  
  - "Are there any tools or resources we can leverage to accelerate pattern recognition and technical depth?"

- **Potential next steps**:  
  - Define clear timelines and expectations for shadowing and reverse shadowing.  
  - Explore training opportunities or documentation updates to address common knowledge gaps.  
  - Discuss how to refine ticket prioritization frameworks to ensure consistency across the team.

## Reunión 2026-06-10 — Acknowledgment vs. resolution timelines · Resumen · Parte 9/15
_chunk 906 · 2026-06-10_

- **Related topics**:  
  - T-001 Team & Links doc for shadowing schedules.  
  - T-004 Queue grooming for prioritization strategies.  
  - T-007 Ticket lifecycle ownership map for escalation paths.

### [Ask AI] aporta una respuesta de conclusion o valor a lo que esta diciendo
It sounds like you're emphasizing the importance of setting realistic expectations during this transition period, especially when it comes to KPIs and technical depth. I completely agree that shadowing and reverse shadowing are critical steps to ensure we’re not just taking over responsibilities, but actually building the confidence and expertise needed to handle tickets independently. The idea of allowing 3–6 months to develop familiarity with the product and recognize patterns makes a lot of sense, especially given the complexity of the modules and the variety of issues we’ll encounter. One thing I’d add is that while we’re ramping up, it might be helpful to define interim milestones—like resolving specific types of tickets or mastering certain modules—to track progress without overwhelming the team. That way, we can balance learning with operational needs and avoid burnout.

- **Key points to reinforce**:  
  - Transitioning to full ownership of support cases requires time—3–6 months is realistic for building technical depth.  
  - Shadowing and reverse shadowing are essential for gradual skill-building and confidence.  
  - Interim milestones can help track progress without setting unrealistic KPIs.

- **Follow-up questions to ask**:  
  - "What specific modules or ticket types should we prioritize during the shadowing phase?"  
  - "Are there any interim KPIs or metrics we can use to measure progress without adding pressure?"  
  - "How do we ensure knowledge transfer is consistent across the team during this ramp-up period?"

## Reunión 2026-06-10 — Acknowledgment vs. resolution timelines · Resumen · Parte 10/15
_chunk 907 · 2026-06-10_

- **Potential next steps**:  
  - Define a phased approach for shadowing and reverse shadowing, with clear milestones.  
  - Identify key areas of focus for technical depth (e.g., SSO issues, specific modules).  
  - Discuss strategies to prevent burnout, such as rotating responsibilities or setting realistic ticket quotas.

- **Related topics**:  
  - T-001 Team & Links doc — roster, dashboards, on-call, Confluence links  
  - T-007 Ticket lifecycle ownership map — RCS vs RTS, who owns each transition  
  - T-088 Jira automation inventory — tools that could support ramp-up and reduce manual effort

### [Ask AI] puedes agregar algo de valor sobre lo que dice sin repetir lo mismo, mas bien aportando algo nuevo, no diciendo las mismas cosas que ya dijo
What you're saying makes a lot of sense, especially the point about setting realistic expectations and allowing time for the team to build expertise gradually. One thing we could consider is creating a phased approach for the transition, where we start by focusing on specific modules or ticket types that are less complex or more common. That way, the team can build confidence and familiarity step by step, rather than being overwhelmed by the full scope of the product all at once. Another idea might be to pair newer team members with existing experts for targeted mentoring sessions, focusing on areas where metrics like resolution time or first response could improve incrementally. This could help us strike a balance between maintaining operational continuity and gradually raising the bar on performance without creating burnout.

## Reunión 2026-06-10 — Acknowledgment vs. resolution timelines · Resumen · Parte 11/15
_chunk 908 · 2026-06-10_

- **Phased transition idea**: Start with simpler or high-frequency ticket types (e.g., SSO issues) before expanding to more complex modules.  
- **Mentoring sessions**: Pair newer team members with existing experts for focused knowledge transfer on specific metrics or modules.  
- **Metrics improvement timeline**: Accept that improvements in CSAT, resolution time, and closure rates will likely take 3–6 months to materialize.  
- **Follow-up questions to ask**:  
  - "Which modules or ticket types could serve as a good starting point for the team during the transition?"  
  - "Are there specific mentoring or shadowing structures we could formalize to accelerate learning?"  
  - "How do we ensure that the phased approach doesn’t disrupt SLA compliance or customer satisfaction during the transition?"

### [Ask AI] puedes agregar algo de valor sobre lo que dice sin repetir lo mismo, mas bien aportando algo nuevo, no diciendo las mismas cosas que ya dijo, ten encuenta el contexto que tenemos actualmente sobre todo el conociiento de moscu
I completely understand the concern about balancing expectations with the realities of ramping up a team. One additional angle we could explore is leveraging automation or tooling to reduce the operational load during this transition. For example, if there are repetitive tasks or metrics that require manual tracking, we could look into automating those processes through Jira workflows or integrations. That way, the team can focus more on learning and resolving tickets rather than being bogged down by administrative overhead. Another idea might be to create a structured feedback loop where team members can share challenges or blockers weekly, not just during shadowing sessions, but as part of a regular cadence. This could help us identify patterns early and adjust the training or support accordingly, before issues escalate.

## Reunión 2026-06-10 — Acknowledgment vs. resolution timelines · Resumen · Parte 12/15
_chunk 909 · 2026-06-10_

- **Automation opportunities**:  
  - Explore Jira automation for tracking metrics like time to closure, CSAT, or first response resolution.  
  - Use dashboards to visualize team performance trends without manual effort.

- **Structured feedback loop**:  
  - Weekly check-ins for team members to report blockers or challenges.  
  - Use these sessions to identify recurring issues and refine training or processes.

- **Follow-up questions to ask**:  
  - "Are there specific tasks or metrics we could automate to free up the team’s bandwidth during the transition?"  
  - "How can we ensure feedback from shadowing sessions is captured consistently and acted upon?"  
  - "Would it help to define short-term goals for the team, like mastering specific ticket types or modules, to build confidence incrementally?"

- **Potential risks to address**:  
  - Over-reliance on automation could lead to gaps in understanding the underlying processes.  
  - Feedback loops need to be actionable—how do we ensure follow-through on reported blockers?

### [Ask AI] Amy right? Does she works on tickets or she takes care of the processes mostly? Amy takes care of all the processes or she also works on Also works on those tickets as well. Mostly I see like you know if there is any messages on this support chat.
Amy primarily focuses on managing processes rather than directly working on tickets. Her role involves overseeing workflows, ensuring compliance with operational standards like Update Rate and Aged Ticket Close-Out, and coordinating escalations to Engineering when necessary. That said, she does step in on tickets occasionally, especially for high-priority cases or when there's a need for direct customer communication. Most of her involvement with tickets is at a strategic level—defining ownership maps, lifecycle transitions, and escalation protocols—rather than hands-on troubleshooting.

## Reunión 2026-06-10 — Acknowledgment vs. resolution timelines · Resumen · Parte 13/15
_chunk 910 · 2026-06-10_

- Amy's focus areas:  
  - **Processes**: Update Rate compliance, escalation packaging, lifecycle ownership mapping (T-002, T-006, T-007).  
  - **Strategic oversight**: Ensuring tickets follow defined workflows and meet SLA requirements.  
  - **Customer communication**: Occasionally steps in for critical updates or escalations.

- **Follow-up questions to clarify**:  
  - "Does Amy have specific criteria for when she steps into ticket-level work?"  
  - "Are there examples of recent tickets where Amy was directly involved?"  
  - "How does Amy's process management role interact with the shadowing sessions we're doing?"

- **Relevant links**:  
  - Ticket lifecycle map: [trebuco.atlassian.net/wiki/spaces/RTS/pages/477554638871](https://trebuco.atlassian.net/wiki/spaces/RTS/pages/477554638871)  
  - Escalation packaging guide: [trebuco.atlassian.net/wiki/spaces/RTS/pages/123301200564](https://trebuco.atlassian.net/wiki/spaces/RTS/pages/123301200564)

## Reunión 2026-06-10 — Acknowledgment vs. resolution timelines · Resumen · Parte 14/15
_chunk 911 · 2026-06-10_

### [Ask AI] okay, so she works very closely Very closely in terms of process orientation and all right. Yeah, I'm actually closely working with BJ, Vijay Prabhat, he is more into working on the secure and incident. We have a very good example of how we can use this. I am still trying to figure out what expertise does Carlos have. So that's like second half of Carlos is first half of So, at least I am able to get 4 to 5 hours daily from Kafka.
Amy's role is heavily process-oriented, but she does engage with tickets when necessary, especially for escalations or high-priority cases. She’s the one who ensures that workflows are followed, compliance is maintained, and escalations are packaged correctly for Engineering. Vijay Prabhat, on the other hand, seems to be more hands-on with Secure and Incident-related tickets, which makes him a key resource for understanding those areas. Regarding Carlos, it sounds like there’s still some uncertainty about his specific expertise, but if he’s contributing 4 to 5 hours daily, it might be worth clarifying his focus areas to ensure alignment with the team’s priorities.

- **Amy's involvement**: Primarily process management, but steps into tickets for escalations or critical updates.  
- **Vijay Prabhat**: Focused on Secure and Incident tickets—likely a good resource for shadowing in those domains.  
- **Carlos**: Unclear expertise; recommend asking directly about his focus areas or recent contributions.

**Follow-up questions to ask**:  
- "Can we get a clearer breakdown of Carlos's expertise or recent ticket involvement?"  
- "Are there specific Secure or Incident workflows Vijay could walk us through during shadowing?"  
- "Does Amy have a defined threshold for when she steps into ticket-level work, or is it more situational?"

## Reunión 2026-06-10 — Acknowledgment vs. resolution timelines · Resumen · Parte 15/15
_chunk 912 · 2026-06-10_

**Actionable next steps**:  
- Schedule a touchpoint with Carlos to clarify his role and expertise.  
- Leverage Vijay’s Secure/Incident knowledge for targeted learning sessions.  
- Confirm Amy’s escalation criteria to better understand when she intervenes directly.

---

## Reunión 2026-07-15 — structured AI prompts · Resumen
_chunk 1222 · 2026-07-15_

## Resumen
The meeting focused on improving interactions with AI systems, particularly Claude, by designing detailed and structured prompts. Participants emphasized the importance of specifying output formats, constraints, and edge cases to avoid vague or incorrect responses. Common failure patterns in AI responses were discussed, including invented facts, incorrect references, and missing coverage. A three-step verification process was introduced to enhance response accuracy: reality checks to confirm sources, assumption reviews to identify uncertainties, and coverage evaluations to detect missing or unnecessary elements. Examples were provided to illustrate how these practices can be applied in professional contexts, such as recruitment processes and technical investigations.

The discussion highlighted that Claude is better at evaluating its own output than generating it, reinforcing the need for systematic verification. Participants shared experiences of AI hallucinations, such as fabricated statistics and plausible but incorrect technical recommendations. The importance of team collaboration in identifying and sharing assumptions or errors was emphasized, as this collective effort can raise the quality of AI-driven outputs across roles and tasks.

Technical tools and integrations were also covered, including Claude's compatibility with Microsoft 365 and Google Workspace for automating tasks and enhancing productivity. Limitations, such as the lack of an Outlook plugin, were noted. Participants explored the use of prompts for complex tasks, such as multi-step engineering workflows, and discussed how structured prompts can significantly improve AI performance in these scenarios. The meeting concluded with a call to systematically apply the discussed methods and prompts to maximize the value of AI tools in professional environments.

## Temas clave
- structured AI prompts
- AI response verification
- team collaboration on AI outputs

## Decisiones
- **Adopt structured prompts with clear output formats and constraints for all AI interactions.** — Improves response accuracy and reduces errors.
- **Apply three verification checks to all AI outputs before finalizing them.** — Ensures reliability and avoids potential issues in professional contexts.

## Tareas / Action Items
- Implement the three-step verification process for AI responses in critical workflows.
- Design and test detailed prompts for complex tasks, focusing on output format and constraints.
- Evaluate the feasibility of integrating Claude with Outlook for email drafting.

## Insights en vivo (Ask AI / Analizar)
### [Analizar] And then again
Lo que entiendo es que la reunión se centró en cómo mejorar la interacción con sistemas de inteligencia artificial, como Claude, mediante prompts detallados y verificaciones estructuradas. Se enfatizó que los prompts deben incluir formato de salida, restricciones claras y casos límite para evitar respuestas vagas o incorrectas. También se discutieron los patrones de fallos comunes en las respuestas de AI, como hechos inventados, referencias incorrectas y falta de cobertura, y cómo aplicar tres verificaciones (realidad, lógica y cobertura) para mejorar la precisión y confiabilidad de las respuestas. Además, se mencionó que Claude es mejor evaluando sus propias respuestas que generándolas, lo que refuerza la necesidad de estas verificaciones.

- **Resumen**:  
  - La importancia de diseñar prompts específicos y detallados para evitar respuestas vagas o incorrectas.  
  - Patrones de fallos comunes en respuestas de AI, como hechos inventados, referencias incorrectas y falta de cobertura.  
  - Aplicación de tres verificaciones (realidad, lógica y cobertura) para mejorar la precisión de las respuestas generadas por Claude.  
  - Claude es mejor evaluando sus propias respuestas que generándolas, lo que refuerza la necesidad de verificaciones estructuradas.  

- **Decisiones detectadas**:  
  - Se acordó que los prompts deben incluir formato de salida, restricciones claras y casos límite.  
  - Confirmación de que las tres verificaciones son esenciales para garantizar la calidad de las respuestas de Claude.  

- **Tareas / action items**:  
  - Implementar las tres verificaciones en procesos internos que involucren AI, especialmente en contextos críticos como soporte técnico o informes.  
  - Diseñar prompts más detallados y estructurados para tareas complejas.  

- **Cruces con tu segundo cerebro**:  
  - Relación con "Reunión 2026-07-01 — Company growth and AI integration · Transcripción 18/20", que menciona la importancia de aprender y compartir conocimientos en equipo, lo cual se alinea con la idea de mejorar colectivamente el uso de AI.  
  - Sin conexión directa con procesos específicos de Appriss KT, pero aplicable como metodología general para mejorar la interacción con AI.  

- **Aclaraciones**:  
  - No quedó claro si las tres verificaciones son aplicables a otros modelos de AI además de Claude.  
  - Falta explorar ejemplos concretos de cómo aplicar estas verificaciones en casos reales dentro de Appriss.  

Próxima pregunta a hacer:  
"You mentioned that Claude is better at judging its own output than generating it. Could you elaborate on how this insight changes the way we should interact with Claude, especially in high-stakes scenarios like customer support or technical investigations?"


## Pulsos de la reunión (resúmenes periódicos + hablantes)
### Pulso 09:48
Se discutió la importancia de crear prompts específicos y detallados al interactuar con sistemas de inteligencia artificial para evitar respuestas vagas o incorrectas. Se enfatizó que los prompts deben incluir formato de salida deseado, restricciones claras y posibles riesgos o casos límite. También se mencionó cómo estructurar la salida para roles específicos, como el de reclutador senior, y se ejemplificó cómo un mal diseño de prompts puede excluir candidatos calificados. El objetivo es mejorar la calidad del trabajo con AI mediante estructuras repetibles y precisas.

**Temas:** Diseño de prompts específicos · Estructuración de salidas para roles laborales

**Sugerencias / preguntas:**
- ¿Podrías dar un ejemplo concreto de cómo un prompt mal diseñado podría excluir candidatos calificados en un proceso de reclutamiento?
- ¿Qué herramientas o metodologías recomiendas para identificar riesgos y casos límite al diseñar prompts complejos?

**Hablantes:**
- **Participante 1:** Explicó la importancia de diseñar prompts detallados y específicos para evitar respuestas incorrectas de la AI, incluyendo formato de salida y restricciones claras.
- **Participante 2:** Mencionó cómo un mal diseño de prompts puede excluir candidatos calificados en procesos de reclutamiento y dio ejemplos de estructuración de salidas para roles específicos.

### Pulso 09:54
Se continuó discutiendo la importancia de la verificación en las respuestas generadas por sistemas de inteligencia artificial como Claude. Se destacó que las primeras respuestas suelen contener errores como hechos inventados, referencias incorrectas y datos casi correctos pero no precisos. También se mencionaron patrones de fallos comunes, como la falta de cobertura en las respuestas y la confusión en el contexto proporcionado. Se enfatizó la necesidad de realizar al menos dos o tres verificaciones para identificar y corregir estos errores antes de confiar en las respuestas generadas.

**Temas:** verificación de respuestas AI · patrones de fallos en AI

**Sugerencias / preguntas:**
- ¿Podrías dar un ejemplo concreto de cómo identificar un caso de 'falta de cobertura' en una respuesta generada por Claude?
- ¿Qué estrategias específicas recomiendas para verificar si Claude realmente entendió y ejecutó una instrucción compleja basada en un documento proporcionado?

**Hablantes:**
- **Participante 1:** Explicó que las primeras respuestas de Claude suelen contener errores como hechos inventados y datos casi correctos, y que es crucial realizar verificaciones múltiples para corregirlos. También mencionó patrones de fallos como la falta de cobertura y la confusión en el contexto proporcionado.

### Pulso 09:59
Se continuó profundizando en la importancia de realizar tres verificaciones en las respuestas generadas por sistemas de inteligencia artificial como Claude. Estas verificaciones incluyen: un chequeo de realidad para confirmar la fuente y la certeza de la respuesta, una revisión de supuestos y áreas de incertidumbre, y una evaluación de cobertura para identificar elementos faltantes o innecesarios en la salida. Se destacó que estas prácticas son esenciales para mejorar la precisión y confiabilidad de las respuestas, especialmente en contextos profesionales. También se mencionó que aplicar estas verificaciones cambia significativamente la calidad del uso de AI.

**Temas:** verificación en tres pasos · mejoras en la precisión de respuestas AI

**Sugerencias / preguntas:**
- ¿Podrían dar un ejemplo concreto de cómo aplicar la tercera verificación de cobertura en un caso real, como un informe técnico o una consulta de cliente?
- ¿Qué estrategias recomiendan para identificar rápidamente los supuestos que AI hace en sus respuestas y que podrían ser incorrectos?
- ¿Han evaluado si estas tres verificaciones son aplicables a otros modelos de AI además de Claude? ¿Hay diferencias en los resultados?

**Hablantes:**
- **Participante 1:** Explicó las tres verificaciones necesarias para mejorar la calidad de las respuestas de AI: chequeo de realidad, revisión de supuestos e incertidumbres, y evaluación de cobertura. Destacó que estas prácticas son aplicables en cualquier rol profesional y que cambian significativamente la forma de interactuar con AI.

### Pulso 10:04
Se continuó profundizando en la importancia de realizar verificaciones en las respuestas generadas por sistemas de inteligencia artificial, destacando la necesidad de hacer preguntas contrarias para evaluar la lógica y la calidad técnica de las respuestas. Se mencionó que Claude es especialmente útil cuando se le solicita que reanalice su propia salida, ya que puede identificar incertidumbres, supuestos y elementos faltantes o innecesarios. Además, se enfatizó la importancia de memorizar y aplicar sistemáticamente estos métodos de interacción para maximizar el valor de las herramientas de AI en contextos profesionales.

**Temas:** Verificación de respuestas de AI · Uso de prompts específicos para Claude

**Sugerencias / preguntas:**
- ¿Podrías dar un ejemplo concreto de cómo Claude ha identificado un supuesto incorrecto en una interacción previa?
- ¿Qué criterios específicos deberíamos usar para determinar si una respuesta de Claude es suficientemente factual y confiable?
- ¿Cómo podríamos sistematizar el uso de estos prompts en procesos de soporte técnico para garantizar consistencia?

**Hablantes:**
- **Participante 1:** Explicó la importancia de hacer preguntas contrarias y de verificar la lógica técnica de las respuestas de AI, destacando que Claude puede reanalizar su propia salida para identificar incertidumbres y supuestos. También enfatizó la necesidad de memorizar y aplicar estos métodos de interacción de manera sistemática.

### Pulso 10:09
Se discutió la importancia de identificar fallos en las instrucciones, suposiciones ocultas y recomendaciones no fundamentadas en las respuestas de la inteligencia artificial. Se destacó que realizar verificaciones detalladas puede evitar errores significativos y mejorar la calidad del trabajo en equipo, elevando los estándares colectivos. Además, se introdujo el uso de etiquetas XML para estructurar prompts complejos, especialmente en tareas técnicas como la migración de archivos a nuevos marcos. Se mencionó que este enfoque es más relevante para roles técnicos y tareas avanzadas, mientras que para tareas básicas no es necesario invertir tanto tiempo en la preparación del prompt.

**Temas:** Verificación de suposiciones ocultas · Uso de etiquetas XML en prompts complejos

**Sugerencias / preguntas:**
- ¿Podrías dar un ejemplo específico de cómo las etiquetas XML han mejorado un prompt en una tarea técnica reciente?
- ¿Qué criterios recomendarías para decidir cuándo es necesario invertir tiempo en estructurar un prompt complejo versus usar un enfoque más básico?

**Hablantes:**
- **Participante 1:** Explicó la importancia de identificar fallos en las instrucciones y suposiciones ocultas, y cómo compartir estos hallazgos puede elevar los estándares del equipo. También introdujo el uso de etiquetas XML para estructurar prompts en tareas técnicas avanzadas, destacando que este enfoque no aplica para tareas básicas.

### Pulso 10:14
En este tramo, se observa una pausa en la discusión técnica mientras los participantes esperan preguntas o respuestas de los asistentes. Laura confirma que no hay preguntas hasta el momento y se menciona la posibilidad de usar música de fondo para amenizar la espera. También se solicita que los asistentes indiquen en el chat cuando hayan terminado una tarea relacionada con la plataforma mencionada.

**Temas:** espera de preguntas · uso del chat para confirmar tareas

**Hablantes:**
- **Laura:** Confirmó que no hay preguntas hasta el momento y sugirió que los asistentes indiquen en el chat cuando hayan terminado una tarea relacionada con la plataforma.

### Pulso 10:19
En este tramo se discutieron patrones de alucinación en datos generados por AI, específicamente sobre estadísticas inventadas en un escenario relacionado con una política de PTO. Se mencionó que el equipo de ingeniería está mayormente involucrado en este análisis. También se realizaron preguntas directas a varios participantes sobre su progreso en ejercicios relacionados con la identificación de patrones de alucinación y algoritmos de hashing. Se acordó avanzar en dos minutos y no ser demasiado exhaustivos en esta parte del ejercicio.

**Temas:** Patrones de alucinación en AI · Progreso en ejercicios de identificación de patrones

**Sugerencias / preguntas:**
- ¿Podrías aclarar qué tipo de datos se esperaría que Claude utilizara para evitar el patrón de estadísticas inventadas?
- ¿Hay algún ejemplo específico de cómo el algoritmo de hashing mencionado podría aplicarse en este contexto de análisis de AI?

**Hablantes:**
- **Participante 1:** Comentó sobre un escenario de estadísticas inventadas en una política de PTO y cómo se relaciona con patrones de alucinación en AI.
- **Participante 2:** Mencionó que el equipo de ingeniería está mayormente involucrado en este análisis.
- **David:** Preguntó a varios participantes sobre su progreso en ejercicios relacionados con patrones de alucinación y algoritmos de hashing.

### Pulso 10:24
Se discutió la importancia de realizar verificaciones constantes en las respuestas generadas por IA, destacando que su naturaleza no determinista puede llevar a resultados inconsistentes incluso con el mismo contexto y prompt. Se mencionó que las sesiones largas y la relajación de restricciones aumentan la probabilidad de errores. También se enfatizó que nunca se debe asumir que la IA 'sabe' algo y que copiar y pegar respuestas sin revisión es un error común. Finalmente, se habló sobre la necesidad de identificar hábitos nuevos, detener prácticas ineficaces y considerar el contexto y las limitaciones al usar IA.

**Temas:** verificación de respuestas generadas por IA · errores en sesiones largas con IA · hábitos y prácticas recomendadas al usar IA

**Sugerencias / preguntas:**
- ¿Podrías dar un ejemplo específico de cómo realizar las 2 o 3 verificaciones mencionadas para validar una respuesta generada por IA?
- ¿Qué estrategias recomiendas para manejar sesiones largas con IA sin relajar las restricciones ni comprometer la calidad de las respuestas?

**Hablantes:**
- **Participante 1:** Explicó que las respuestas de la IA no son deterministas y pueden variar incluso con el mismo contexto y prompt. Recalcó la importancia de realizar verificaciones para evitar errores.
- **Participante 2:** Mencionó que las sesiones largas con IA y la relajación de restricciones aumentan la probabilidad de errores y que es crucial no asumir que la IA 'sabe' algo.
- **Participante 3:** Habló sobre la necesidad de identificar hábitos nuevos, detener prácticas ineficaces y considerar el contexto y las limitaciones al usar IA.

### Pulso 10:29
Se discutieron herramientas y funcionalidades específicas de Cloud y Claude, incluyendo comandos como Compact y su utilidad en ingeniería. Se mencionó la integración de Claude con Microsoft 360 y Google Workspace mediante extensiones, así como una versión beta de un navegador para Chrome que automatiza interacciones web. También se destacó la importancia de realizar tres verificaciones clave en las respuestas de Claude: origen de la información, consistencia con la evidencia y autocrítica de la respuesta. Finalmente, se enfatizó el uso cuidadoso de estas herramientas en entornos sensibles como la privacidad.

**Temas:** Herramientas de Cloud y Claude · Integraciones con Microsoft y Google Workspace · Verificaciones clave en respuestas de IA

**Sugerencias / preguntas:**
- ¿Podrían detallar más sobre cómo funciona la integración de Claude con Google Workspace y qué casos de uso específicos han encontrado más útiles?
- ¿Qué limitaciones específicas tiene la versión beta del navegador para Chrome y cómo planean abordar los problemas de privacidad mencionados?
- ¿Podrían dar ejemplos concretos de cómo aplicar las tres verificaciones clave en un entorno de trabajo real?

**Hablantes:**
- **Participante 1:** Explicó funcionalidades de Cloud y Claude, como el comando Compact y su utilidad en ingeniería, además de la integración con Microsoft 360 y Google Workspace mediante extensiones. También mencionó una versión beta para Chrome que automatiza interacciones web, aunque con preocupaciones de privacidad. Destacó la importancia de realizar tres verificaciones clave en las respuestas de Claude: origen, consistencia y autocrítica.

### Pulso 10:34
Se discutió la disponibilidad de herramientas de AI como extensiones para Microsoft 365, incluyendo Word, Excel y PowerPoint, pero se confirmó que no hay integración directa con Outlook para redactar o revisar correos electrónicos. Se mencionó que Copilot podría ser una alternativa para estas funciones. También se planteó la preocupación sobre la privacidad y el acceso a datos sensibles al usar estas herramientas. La reunión concluyó con agradecimientos y un cierre general.

**Temas:** Integración con Microsoft 365 · Privacidad en el uso de herramientas de AI

**Sugerencias / preguntas:**
- ¿Existe algún plan futuro para integrar estas herramientas con Outlook, considerando su utilidad para la redacción de correos?
- ¿Qué medidas específicas se están tomando para garantizar la privacidad y seguridad de los datos al usar estas herramientas en entornos corporativos?

**Hablantes:**
- **Participante 1:** Explicó que las herramientas de AI están disponibles como extensiones para Word, Excel y PowerPoint, pero no para Outlook. Mencionó que Copilot podría ser una alternativa para funciones relacionadas con correos electrónicos.
- **Participante 2:** Señaló la importancia de considerar la privacidad y el acceso a datos sensibles al usar estas herramientas.

### Pulso 10:44
En este tramo se mencionaron aspectos generales sobre el uso de AI, aunque con poca claridad en los detalles. Se hizo referencia a la importancia de entender los diferentes tipos de AI y cómo aplicarlos, pero no se profundizó en ejemplos concretos. También se mencionaron herramientas como Google Clicking Button y se sugirió un enfoque práctico para comenzar a trabajar con AI. Hubo comentarios dispersos sobre la interacción humana y la división de tareas, pero sin un hilo conductor claro.

**Temas:** tipos de AI · herramientas prácticas para AI

**Sugerencias / preguntas:**
- ¿Podrías explicar con más detalle qué tipos de AI mencionaste y cómo se diferencian entre sí?
- ¿Qué es exactamente el Google Clicking Button y cómo se relaciona con el uso de AI en el trabajo?
- ¿Podrías dar un ejemplo práctico de cómo empezar a trabajar con AI en un contexto laboral específico?

**Hablantes:**
- **Participante 1:** Habló sobre la importancia de entender los diferentes tipos de AI y sugirió un enfoque práctico para comenzar a trabajar con ellas, aunque no dio ejemplos concretos. También mencionó herramientas como Google Clicking Button sin explicar su función.


## Contexto capturado (notas y capturas)
- 📷 **Captura:** The screen shows a Microsoft Teams meeting discussing "The CRISP Framework" by Nuavv, focusing on context, role, input, specification, and probe for AI calibration. Chat includes workshop-related files and discussions.
  ![captura](file:///Users/MancoMenStudio/Library/Application Support/InterviewApp/Screenshots/shot-1784126640714.png)
- 📷 **Captura:** The screen compares vague vs. CRISP prompts for AI tasks, emphasizing structured inputs for better outputs. It relates to the meeting's focus on improving AI-driven processes and ensuring clarity in task instructions.
  ![captura](file:///Users/MancoMenStudio/Library/Application Support/InterviewApp/Screenshots/shot-1784126871961.png)
- 📷 **Captura:** The screen shows a presentation slide titled "Claude Is a Better Judge Than a Generator," discussing five hallucination patterns in AI outputs. It relates to the meeting by addressing AI verification strategies and improving prompt design for accurate results.
  ![captura](file:///Users/MancoMenStudio/Library/Application Support/InterviewApp/Screenshots/shot-1784126996717.png)
- 📷 **Captura:** The screen displays a slide titled "The Three Pass Read" with three verification steps: Reality Check, Logic Check, and Coverage Check. It relates to the meeting by outlining methods to verify AI outputs for accuracy and reliability.
  ![captura](file:///Users/MancoMenStudio/Library/Application Support/InterviewApp/Screenshots/shot-1784127394437.png)
- 📷 **Captura:** The slide discusses two verification tools for AI outputs: "The Citation Habit" and "Reflexive Critique Prompting." It emphasizes questioning the source of AI responses and critiquing its output for accuracy. This relates to the meeting's focus on improving AI reliability and systematic application in workflows.
  ![captura](file:///Users/MancoMenStudio/Library/Application Support/InterviewApp/Screenshots/shot-1784127762888.png)
- 📷 **Captura:** The screen shows a slide titled "Universal Hallucination Hunt," outlining a live exercise with two activities: "Individual Review" (10 min) and "Round-Robin" (5 min). Participants analyze AI responses for flaws and share findings. It relates to the meeting's focus on improving AI outputs.
  ![captura](file:///Users/MancoMenStudio/Library/Application Support/InterviewApp/Screenshots/shot-1784128270101.png)

---

## Reunión 2026-07-15 — structured AI prompts · Transcripción 1/12
_chunk 1223 · 2026-07-15_

## Transcripción completa
L.A.I to ask us Always, let's make it an expert, always. If you want to find subtle mistakes, you can tell it to take the wrong More specific, the better This means that we are going to put more time Not give it short, vague prompts. Prompts. We're going to take the time to be specific in what we wanted Now the input is important It's important for us to copy-paste what it We ask from it. Don't paraphrase it, right? The output I want you I want you to give me as an output a PowerPoint presentation. presentation. I want you to give me a bullet list Output, Format, we want, a PDF, etc. We wanted to follow what not to do, what not to assume. and we're giving it the constraints so that it basically It basically does not guess, as engineers We shall remember that moving forward. and lastly the Appriss the angles to explore. Check and see if If there are risks that I have not considered, tell me Tell me edge cases that I didn't think about. and Flag and tell me the things that you are assuming I assume this. I assume that other thing. Am I correct on that? And we prompted yes or no. The main goal of this is to replace as cloud some with a repeatable structure that consistently progresses. The Better The Quality Of The Work That We Deliver with the help of AI is going to AI is going to improve regardless of our role, regardless But then again, this very big prompt is for and more complex tasks. Here is the example of a vague normal for a Customer Success Role. This gives so much space for AI AI to guess. Let's remember that it now uses Crazy. So when we give something so vague The Wrong Tone, It Invents Requirements and even will always need AI for 200 people. This is the company type that we're that we're aiming to be. and the context. We're telling the role Senior Recruiter focused an inclusive job to screen. Divide these 300 words in 3 clear sections.

## Reunión 2026-07-15 — structured AI prompts · Transcripción 2/12
_chunk 1224 · 2026-07-15_

Now you see how we are structuring the output and we can and we can imagine what the output can be from the prompt. may exclude qualified candidates. Think of how useful and and interesting this last section is. Here we're telling it that I am missing that would exclude people that we actually want. The result is going to be a brief burnout. The difference is day and night and this takes five extra minutes. Complex, but imagine applying Imagine applying this for something that requires six, seven steps. Steps. Here is where it shines. and here everybody I want you to please pay a lot of attention right now. Blood is a better judge of its output How it's put, than a generator of one. Again, this mental model changes everything. If we will always apply 1 and 2 and 3 verifications to its that cloud is a better job and a better judge of its answer than a generator of one. So far, any questions? So, here's what I meant. Let's please... Let's please memorize this. This is the most important thing. It is a better job. Better judge than a generator and because AI keeps improving, it keeps doing It's getting better. The hallucinations do not go away. Cloud gets smarted by the day. So those have Those hallucinations become more subtle. The Surrounding Output reads more competitively We are prompted to trust it because it looks great. Even if it looks great, it's not. There's always, always, always on the first answer. that this is what the first answer of CLOD will always have. The first one is Invented Facts and References like statistics, sources, certifications You might think, hey, this should not happen, but again... The complexity behind AI is so much So much that if we do not put enough time in the prompting and verification possible but wrong specifics like the content Content, Dates, Numbers and Names that are almost right All most right, but not truly. If we trust it and we delete it the final client or your boss.

## Reunión 2026-07-15 — structured AI prompts · Transcripción 3/12
_chunk 1225 · 2026-07-15_

That's why before that Before that happens, we're going to verify two and three times to make sure we We find them because they will always be there. Now the context that we give it is very specific. Clod gets confused on the context. as well as misreading source material like logs, like If we provide a document, sometimes it might get confused. We asked him to do something very specific, but silently it didn't. but unless we truly verify and ask it, did you actually do it? It might sound truth when it's not. And lastly, a second A second pattern is missing coverage. is a 6 failure mode worth naming. So think about that question to ask back when When Claude gives you an answer, think about that question. Hey What should be in the answer that is not there. and Recheck everything indeed, finding what it missed. That one verification step changes the output drastically. Alrighty, time to do just a Just a random question, Mr. Mr. Juan Jesus Vieira From these five patterns that you see on the screen Can you think of one that one hallucinates? and Hallucination that you have had before with your use of AI. You can post it in the chat or speak out loud I couldn't hear you well, could you please repeat the question please? but from these five patterns that you see on the screen, can you Can you think of one that you believe AI has hallucinated? You can create it when you use it, any of these five Hey, yeah, for sure. and model that I'm using in this tab. are incorrect and it doesn't make sense. Possible but Wrong Answers That is what I believe. Okay, second button. Thank you. Thank you, Sir, for participating. Moving forward. Seems now we know that and Clod is a better judge of its output. and that the first answer that AI gives us will never be okay. OK, never. That's why we're going to apply three checks. to make sure that the answer that we get The first one, and again, this works for any role. is the reality check. Let's do an example. You can think and Answer.

## Reunión 2026-07-15 — structured AI prompts · Transcripción 4/12
_chunk 1226 · 2026-07-15_

We're going to reply back with this. What is the source of your answer? Is it the input I Double checking, verifying what it did. That is what it's going to point to. Verification after it answers, right? We can ask it, where are you uncertain? What? What did you assume is going to then re-check everything it did? and the third after we After we get another answer, the third verification pass we're going to do is cover it. This is the most likely problem users, clients Science, or my boss is going to find if I ship as is. This changes the game so much. Oops, beautiful, beautiful prompt, one of my favorites. Check everything and check for what is missing that should be That should be there. What would a careful What is missing that should be there works the other way around as well. What is there that shouldn't be on your output? See how doing this 3 checks, turn our user AI AI into a larger, more current More Careful Approach Until this moment Do we have any questions or suggestions? It's okay, okay, we're not judging, we're not evaluating, we're just participating. why these three verification checks are not really. Not really, I mean I just and the first problem and then based on the just went I just see like, you know, okay, AI AI is not efficient but haven't deep dive into and more prompts to make sure that i cross 45 were the How much I can rely on the answer that I have with found Claude and more in these details. Same. Same, honestly, until I learned this, everything changed. Thank you for participating. participating, sir. And I believe no questions, right? All right, I'll move on. I forgot to mention this very and the very very important part. Like for RC analysis, right? If we ask them a question Ask them a counter question based on the logic check. from the technical standpoint Prompt them like you know how genuine the information is right In the sense, let's say This is the ticket number.

## Reunión 2026-07-15 — structured AI prompts · Transcripción 5/12
_chunk 1227 · 2026-07-15_

Can you help me investigate what is the issue? but we are not satisfied with that or we tried and it failed. So how would you approach How would you approach that problem from support perspective? That is something I want to know. AI, and then asking three questions, making a conversation. Conversation with it. First, you would ask what is the What is the source of your answer? Input, training data, internet What did you miss that should be in your life? What did you include in your answer that should not be and the other side of the you should not have the issue you mentioned. Technically we have to counter, right? Okay, this resolution I tried, it did not It did not work. This doesn't work. What more we can end? and more we can do. Can you help me where the issue lies? Something like that. Exactly, making a conversation because cloud Cloud will be more useful when When double and triple checking what it did. That's where Claude shines. give you everything you need. Makes sense. Thanks. View for participating. And then again This is the part I wanted to finish this slide on this section right here to your boss or to your client. Moving forward. We truly fully memorize it and start applying systematically every time we use it. This is my answer. We're gonna reply back. What is the source of it? or from Web Search Internet. This is only available if you manually and the other one. Mixup, or Specs. And look at how important that is. It's important to always ask it to double check each and make sure it's factual. Then we continue that conversation I also love these prompts. I hope we all memorize these ones. What you just wrote. It will go back, reanalyze everything. and other things that you can do to extract that value when it goes back and creates. Where are you uncertain? What did you assume that I didn't tell you of that? That prompt is just beautiful. It's a work of art. and for the fifth time, but so that we fully memorize it, Claude.

## Reunión 2026-07-15 — structured AI prompts · Transcripción 6/12
_chunk 1228 · 2026-07-15_

The plot is a better judge of its own output than a generator of one. Instruction failures, hidden assumptions that will sound very trustworthy and the Office of the University, unsupported recommendations, etc. Why is this so important? and the so that we all align on the value that we can derive from the AI. 10 minutes extra in the prompt. If we don't do that Because every use across all teams saves us a lot of time. and when we do these verifications. If your AI catches one assumption or one mistake 1 Mistake, that makes it worth it. That already changed and and helped you avoid an uncomfortable situation. and lastly this is a team skill because each each task is different than the other. Each time we find Find an assumption or something that shouldn't be there. We can share it with our team. This will change our discussions and the output That is noticeable, right? That will set the bar higher, meaning we all as a team Team will need to step up the game to reach that new bar. Moving on. This is mainly for engineers. for Engineering and more complex tasks, we already saw the crisp Crisp Technique in a plain That is quite complex, that will take Claude two entire minutes to do. and mainly for engineering or more complex roles, here is Here is how we would divide the prompt. Just like in These are called XML tags. If you grab them like this Object and its reasoning with it is going to improve. But then again, we spend the time to do it in this way for a complex task. Tasks. You are migrating different files into a new framework, etc. etc. So this does not apply for everyone if you're doing something. If you're doing something basic, no need for you to actually spend the time to do all of this. But but interesting point. If you need to You need to do a complex problem Prompt that is this specific, guess what? Cloud can do it for us, of course. So my first approach would be, hey Hey, this is my objective, something very hard, multi-steps that I need to do.

## Reunión 2026-07-15 — structured AI prompts · Transcripción 7/12
_chunk 1229 · 2026-07-15_

AI, Time for your sip of coffee. In that file, I have added 10 data and different roles in an enterprise organization. There you have a child. and others are random and see what happens, no problem. What are we going to do? First Draft Output that Claude gave you, right? Then you're going to copy that into any AI that you and the techniques that we just learned. I have planted halibut Hallucinations, and on each one of those. So your task Your task is to use these three checks very fast. They look professional, but they are not. So we're going to give it 10 seconds. Let's get to it. I'll be here waiting for your answers, for your question. Questions. Maybe I should have Maybe I should have prepared some music for the background Sure, Laura, it's fine. No questions so far. and the other side of the platform. Cool, please post in the chat if you're done. Yes, so I was exploring the following and the first one CE01 new PTO policy announcement. As you mentioned, can you hear me too? Yeah. Yeah, so Claude actually The card actually invented one, you know, 87% employee service statistics statistic to justify the new policy that's I think I think Pattern 1, Invented Facts and it's only catch-up and never gave Claude any survey data to draw the data from. Excellent, exactly what we were looking for, good stuff Good stuff. Thank you. For what team is that first scenario? All righty, how was it? How are we doing and everybody else? or those will have mostly 99% people in the engineering side I'm going to give you an answer on this project Touch. Thank you. All right. All right, let's give it just two more minutes and let's move on. No need to be so thorough on it. and with your exercise. how about Diego Pueblbas? How you doing? I'm a little busy David, so just taking and Juan Martinez. How did it go? So that's one more than and more than one hallucination pattern that you cut slow collapse No claps for you, sir. Good stuff. Exactly what we were looking for. Mr.

## Reunión 2026-07-15 — structured AI prompts · Transcripción 8/12
_chunk 1230 · 2026-07-15_

Juan Bonilla, how you doing? I'm just trying to figure out What Butters Are Being Applied Here So I'm trying to wait until you're in. No problem. As long as you get one, that's good. Yes, I got one. I am in Engineering Let me put me again there Basically I saw in The first one, but and Viseware Hashing Algorithm, Cloud says Factor of Fan, OUS recommends a minimum factor and the same factor, work factor of 12 for a new application and that is wrong. I think the pattern is plausible but round especially and specifics. Cool. Excellent. Good stuff, thank you for sharing Alrighty, we're reaching the time, let's finish with... and Jazz. Psych'd! How you doin' with your activity? It's okay. Let's move on to Sumit, Sumet Giant, how you doing? How are you doing? I'm self-worth and wanted actually Sure, alright, no problem. Let's just give it one more minute and we're going to stop Reminder, you can do that by asking three different questions. Let's move on. Some of the questions you can ask You can ask our... here. Where are you? What did you assume? What's missing that should be and are the names, number, dates, and reference real? If you ask If you ask any of those questions, it shall find Pause on there. Thank you everybody for your participation on this exercise. and exercise. Moving on. If you didn't finish, you can do that later. Let's grab it up. and all the new habits that we shall consider and Redo's or Stop Doing. Blank context. If you know our situation, the organs, or constraint, it doesn't. and the other one is the is directly linked to the context and the scrutiny we do on verification. So we should never assume Assume that it knows something. Now, if we copy Copy and paste its answer and we don't review it. 2, or 3 verification checks is gonna be wrong almost Almost for a fact, almost always. So we should never treat its output or answers as the true as the Truth, never.

## Reunión 2026-07-15 — structured AI prompts · Transcripción 9/12
_chunk 1231 · 2026-07-15_

That is the single big Biggest cause of regret with AI generator and every long chat, given its complexity and XCD on how it processes information and tasks. The longer the chat makes, the more Things it has to consider. Appreever chat that goes over and over is the correct way to go. If we also have a long session and and we relax the constraints that we give it assuming Continue using it for a long chat session. That's all for now. That's also a mistake. And the only way we catch it is by doing verification, by having it, catching them. and treating quadras deterministic. Its very nature is non-deterministic. The same context, the same prompt if you give it If you give it twice or three times, the answer is The answer is not always going to be the same. Why? Because it has too much to assume. I just want to say something about the forever chat Sometimes we need to keep and more conversation than usual. I'm not completely sure if this functionality is available in in Cloud in general, but in Cloud Code, which is which is the tool that we are using for engineering. We have the Compact command, it is pretty useful and the context in the NAO, but trying to keep the most important and other important things in the chat so we can use it when it's needed. Thank you, sir. Excellent. but you are right that is not a compact is not a Compact is not a feature on Claude Desktop. That's very interesting. Good. All the complexity that it happens on the background makes its very nature non-deterministic, which is why we should We should not ever trust his first or second answer. Always test first before We have very different tools, each one Each one specialized in a specific task or application, or the mobile app. It's for not so complicated. application. These women helps us helps us automate desktop functions. It is also allows for for Dragon Drop of Files and it has the projects. If you have a task task that is a multi-stack task and turn it into a project.

## Reunión 2026-07-15 — structured AI prompts · Transcripción 10/12
_chunk 1232 · 2026-07-15_

And that way, Cloud will help you automate Automate that moving forward. We can also integrate Claude in in Microsoft 360 for our word for Powerpoint, etc. Very, very helpful in all the and all of the Google Workspace. We do this by installing Installing and Extention in Word, in PowerPoint, etc. and Cloud tells us that the teams that can derive Cloud also has a browser extension that helps us automate Crumb, this is not in Edge, it's only in Crumb, but but it's a beta version and we have to realize that the to automate web interactions is by analyzing Analyzing and Taking Constant Screenshots of the website that you are The privacy settings out there are something and a better version. Use with care and don't use it but for other stuff it helps us to summarize web content, it helps us as Clod terminal, mainly for engineering, is a Multiply called Code Coding Agent that helps us for for multi-step tasks that take longer. All of these are in the file that I shared, but again 3 checks that we shall do with the output of Clyde Tell me where did you get your answer from my input? Did you? Did you invent it? that if its answer follows the evidence present, are you as Are you assuming things I never said or that are not present in context? and most beautiful one, Critique, what you just grew up with. You just groat. Why are you uncertain of? That one is beautiful. and to my boss or if I ship it. What is the most likely problem? and Pro. Those are the ones to consider and memorize. and there we go Thank you everybody for joining. Remember that these These prompts are in the files that you can review and the Great Warmly Recyft. Yes, Mr. Virash. Go ahead. Just one question I posted, like you mentioned multiple places where we can use it, right? Is there a plugin for Outlook? I believe I have it right here actually. Let me show you One second, I don't see, I just see this.

## Reunión 2026-07-15 — structured AI prompts · Transcripción 11/12
_chunk 1233 · 2026-07-15_

and Work with anything on Microsoft 365, you first download the and it's an add-on or an extension once Once you download it, then you appear here and you just log in. What about the outdoor? Outlook, emails. I actually don't know. I don't think it's available Word, Excel, PowerPoint, but not really out to the correct fields. Outlook would be very useful I think it's very useful for drafting emails or re-drafting it It's a good point. Yeah, but it also snoop through everything that you are exchanging or outlay. Cloud. That's also very important. Point that you mentioned, only for the plan of close Ask about the email, that's a very important But yeah, it doesn't have it. That's quite interesting. I believe only Copilot is the one that has that So now, no, maybe then you can... no, yeah, no ideas actually. how can I better use your tools to do so? Thank you for bringing it up. Cool. Thank you everybody for joining and participating and and Happy Prompting. Have a good one. Thank you, thank you, take care, and everybody else. and the other side of the world. and the other one. I think it's important to understand the reasons why I hope you will enjoy this. This is a question that you have to ask yourself and the other one. Just double click over it. and the Google Clicking button. This is what I was talking about I'm going to start with how I do it as well as the different types of AI Esta o la otra, no où, ver lo fuer. Verlo fum oí dolores But it's the other, it's the... and the other one This is more local I think it's because I'm not a scientist, I'm a scientist and the other side of the system. No, I don't like to talk to people. No, I don't like to talk to people. I'm going to do this for you We will start with the last moment. Let's put on working vest. Ummm, supos para tener la Division! I don't know. I don't know how to describe it. This is one that I person in the world. Para Victor, Sávez como que la gente pregunta cosas. Acávato, cara gregar. and...

## Reunión 2026-07-15 — structured AI prompts · Transcripción 12/12
_chunk 1234 · 2026-07-15_

I'm really hungry No, no, no, no.

## Reunión 2026-07-16 — ticket prioritization · Resumen
_chunk 1275 · 2026-07-16_

## Resumen
The meeting focused on ticket prioritization, triage processes, and team workload management. Initially, a ticket opened five days ago regarding columns and inventory for system creation was discussed. It was agreed to keep its priority as medium unless the Customer Success Manager (CSM) escalates it due to significant client impact. The distinction between change requests and critical incidents was emphasized, with the latter requiring immediate attention.

Subsequently, a critical ticket related to vehicle information was highlighted. It was suggested that if the user lacks access to the support team's priority channel, someone else should communicate the urgency. The uneven distribution of tickets among team members was also discussed, noting that complexity often dictates workload rather than quantity.

The triage process managed by the Level 2 team was reviewed. This team determines whether tickets should be escalated to the Infrastructure team, which operates on Pacific Time. Clear communication with clients about ticket transfers was recommended, avoiding overpromising while ensuring updates are provided. Assigning tickets before transferring them was also stressed.

The loss of a key Infrastructure team member, Kyle, was noted, potentially impacting ticket handling. Russ was identified as the main contact for ticket assignments to Infrastructure. Changes in support email handling were discussed, with certain team members being copied on emails starting Monday to monitor and assist with tickets. A document requested by JR regarding this process remains pending. Additionally, the limited availability of some team members, including one participant leaving in two weeks and Amy in two months, was mentioned as a factor in task distribution.

## Temas clave
- ticket prioritization
- triage process
- team workload management
- client communication
- infrastructure team changes

## Decisiones
- **Keep the ticket related to columns and inventory as medium priority unless escalated by the CSM.** — It is a change request, not a critical incident.
- **Communicate the urgency of the critical vehicle information ticket if the user lacks access to the priority channel.** — The ticket is critical and needs prompt attention.

## Tareas / Action Items
- Confirm if the CSM has been informed about the ticket related to columns and inventory and gather their feedback.
- Verify access to the support team's priority channel for escalating the critical vehicle information ticket.
- Communicate with Russ to ensure proper assignment of tickets to the Infrastructure team.
- Prepare the document requested by JR regarding the new support email handling process.

## Pulsos de la reunión (resúmenes periódicos + hablantes)
### Pulso 10:33
Se discutió sobre un ticket abierto hace cinco días relacionado con columnas e inventario para carga en un sistema de creación. Se mencionó que la prioridad actual del ticket es media, ya que es un cambio solicitado y no un incidente crítico. Solo se consideraría aumentar la prioridad si el Customer Success Manager (CSM) lo solicita debido a un impacto significativo en el cliente. También se habló sobre la importancia de diferenciar entre solicitudes de cambio y tickets de incidentes que afectan operaciones críticas.

**Temas:** prioridad de tickets · diferenciación entre cambios e incidentes

**Sugerencias / preguntas:**
- ¿Podríamos confirmar si el CSM ya ha sido informado sobre este ticket y si tienen algún comentario al respecto?
- ¿Hay algún criterio específico que podamos establecer para decidir cuándo un cambio solicitado debe escalarse a alta prioridad?
- ¿Se ha considerado si este ticket podría afectar otros procesos relacionados con el POS o la integración completa?

**Hablantes:**
- **Participante 1:** Preguntó si compartir pantalla para revisar los tickets o si el otro participante lo haría. Identificó un ticket abierto hace cinco días relacionado con columnas e inventario. Sugirió mantenerlo como prioridad media a menos que el CSM indique lo contrario debido a un impacto crítico en el cliente.

### Pulso 10:38
Se continuó discutiendo sobre la prioridad de los tickets. Se mencionó que no todos los tickets son iguales y que algunos, como el relacionado con la sección de información de vehículos, son críticos y deben ser atendidos pronto. Se sugirió que, si el usuario no tiene acceso al canal de prioridad del equipo de soporte, alguien más podría encargarse de comunicar la urgencia de este ticket. También se habló sobre la asignación de tickets, destacando que no se asignan de manera uniforme, ya que algunos pueden requerir más tiempo dependiendo de su complejidad.

**Temas:** prioridad de tickets · gestión de asignaciones en el equipo de soporte

**Sugerencias / preguntas:**
- ¿Podrías confirmar si tienes acceso al canal de prioridad del equipo de soporte para agilizar la comunicación sobre este ticket crítico?
- Sería útil preguntar si hay un procedimiento estándar para escalar tickets críticos como el de la sección de información de vehículos, especialmente si el acceso al canal de prioridad no está disponible.

**Hablantes:**
- **Participante 1:** Sugirió mantener la prioridad media para algunos tickets, pero destacó que el ticket relacionado con la sección de información de vehículos es crítico y debe ser atendido pronto. También mencionó que podría encargarse de comunicar la urgencia si el usuario no tiene acceso al canal de prioridad del equipo de soporte.
- **Participante 2:** Comentó sobre la asignación de tickets en el equipo, indicando que no se distribuyen de manera uniforme debido a la variabilidad en la complejidad de los tickets.

### Pulso 10:44
Se discutió el proceso actual de triage de tickets, que está a cargo del equipo de Nivel 2. Este equipo decide si un ticket debe ser escalado al equipo de Infraestructura, quien trabaja en un horario diferente (PST). Se mencionó un ejemplo reciente de cómo manejar la comunicación con el cliente, sugiriendo responder con un mensaje claro sobre la transferencia del ticket al equipo de Infraestructura y evitar promesas excesivas. También se destacó la importancia de asignarse el ticket antes de moverlo y de mantener al cliente informado sobre los próximos pasos.

**Temas:** Proceso de triage de tickets · Comunicación con clientes sobre tickets · Horarios del equipo de Infraestructura

**Sugerencias / preguntas:**
- ¿El proceso de triage por parte del equipo de Nivel 2 incluye algún criterio específico para decidir qué tickets escalar al equipo de Infraestructura?
- ¿Hay un protocolo establecido para manejar tickets urgentes fuera del horario del equipo de Infraestructura?
- ¿Se podría automatizar el envío de respuestas iniciales a los clientes para informarles sobre la transferencia de sus tickets al equipo de Infraestructura?

**Hablantes:**
- **Participante 1:** Explicó que el equipo de Nivel 2 realiza el triage inicial de los tickets y decide si deben ser escalados al equipo de Infraestructura. También mencionó que los tickets deben ser asignados antes de ser transferidos y que el cliente debe ser informado con un mensaje claro y sin promesas excesivas. Recordó que el equipo de Infraestructura trabaja en horario PST, lo que puede afectar la atención de tickets en horarios tempranos.

### Pulso 10:49
Se mencionó que el equipo de Infraestructura perdió a un miembro llamado Kyle, lo que podría afectar la asignación de tickets. Russ parece ser el contacto principal para asignar tickets a Infraestructura. Un participante indicó que solo estará disponible por dos semanas más, mientras que Amy estará por dos meses más, lo que podría influir en la distribución de tareas. Se discutió un cambio en el manejo de correos de soporte, donde a partir del lunes se copiará a ciertos miembros del equipo en los correos para monitorear y ayudar con los tickets. También se mencionó que JR solicitó un documento relacionado con este proceso, pero aún no se ha comenzado a trabajar en él.

**Temas:** Pérdida de un miembro en Infraestructura · Disponibilidad limitada de ciertos miembros del equipo · Cambio en el manejo de correos de soporte · Solicitud de JR para un documento pendiente

**Sugerencias / preguntas:**
- ¿Cómo planean manejar la carga de trabajo adicional en Infraestructura tras la salida de Kyle?
- ¿Qué tipo de soporte específico se espera que brinden los miembros copiados en los correos a partir del lunes?
- ¿Hay un plan para priorizar la creación del documento solicitado por JR, dado que aún no se ha iniciado?

**Hablantes:**
- **Participante 1:** Mencionó que el equipo de Infraestructura perdió a Kyle y que Russ es el contacto principal para asignar tickets. Indicó que estará disponible solo por dos semanas más y que Amy estará por dos meses más. También habló sobre un cambio en el manejo de correos de soporte, donde se copiará a ciertos miembros del equipo a partir del lunes. Además, mencionó que JR solicitó un documento relacionado con este proceso, pero aún no se ha comenzado a trabajar en él.


---

## Reunión 2026-07-16 — ticket prioritization · Transcripción 1/4
_chunk 1276 · 2026-07-16_

## Transcripción completa
Hi Juan, how are you? What? Yes, what's going on today? That's what I'm hearing. That's what I'm here for. Do you want to share with Share with me your screen. Okay, or do you want me to share mine and you can just tell me which ticket you want to ticket you want to look at. Okay. So is it one of the Is it one of these tickets that's sitting here in the backlog? Well, let me look. Right, so this one was open five days ago if I remember correctly. and remember correctly, on the 10th, so yeah. Columns and inventory which we would like to upload to upload to creation we spend in We spend majority of the time on the POS status and the choice to do full integration and Support with a Request. I wonder, this could be Kristin Dyer, who is a solution expert. This one, I guess for me when I look at it It is a change request. At this point, I would leave it as a medium priority. Priority. Okay. I would leave it I would leave it as a medium priority. The only way that Moving something like this to high is if the customer success matter Success Manager, the CSM would reach out and push it and say and say, look, this is something that they need to have now because if they don't They don't, it's affecting XYZ. I would leave this one since it's a change request. if there was a break in it, right, and it was an incident. and Inc. ticket and they came back and said We can't do our work, we can't do our reports, etc. etc. Then at this point, yeah, you know, we would move that to Foundation put in, they weren't able to get to it. and I don't, you know, it's not one of those things where you want to say to them This was part of the process that if you wanted to have this stuff put in etc. So unless the CSM starts starts pushing on this one, I would just leave this as a medium priority. I'm going to go ahead and go ahead and do that. Yeah, and just remember I get that idea because no two tickets are the same, right? All of these tickets can be very different.

## Reunión 2026-07-16 — ticket prioritization · Transcripción 2/4
_chunk 1277 · 2026-07-16_

So it's kind of a, you know So, Casey's. This is an instant vehicle, other info, not Pieces, other info section of the vehicle information will not display. is critical. Okay. This one This one was opened. This information is critical. I would do in a situation like this and I don't know if I don't know if you've got the ability to do it, I can do it for you. and just say, hey, FYI, this ticket needs to be taken sooner and later. Let's get it picked up and then go from there. See should be taken sooner than later. I had asked Amy probably two weeks ago that sounded like it was going to be a discussion with Jay with JR as to when. So I don't know if you have access. Access, if she gave you access or not, but it would be for the Support Team Priority channel. Do you guys have access? So, we'll do this. We will. All. But I gotta get to the right spot. we're gonna grab this one and I go back to and I'll be back to my priority channel. and the other one. and so then I would just let them know just like Meeting, and say, hey Hey, somebody's got to pick this one up who can take it, you know, I don't mean to on a meeting, however your process is going to be for We never, for us, we never just assigned had someone maybe only has three tickets to somebody else's eight. 8 tickets, but the person with three tickets might have data tickets that take him that much that needs to get worked if they're the one that has tickets that'll take longer. and you might just assign it to somebody. So is that answering your questions so far? Okay. Okay. Okay. And the next one. and the other one. Oh, okay. Yeah, okay. Okay, so right now, the way it is set up are supposed to be triaged by the level 2 team. and whoever picks up the ticket makes the, you know Hey, this is going to the infrastructure team, so they need to communicate with the Level 2 does that first and move them somewhere just because it has to be looked at by level 2. 2, a process that may change.

## Reunión 2026-07-16 — ticket prioritization · Transcripción 3/4
_chunk 1278 · 2026-07-16_

So what is this? I've confirmed that the issue will impact Appriss Cact, Appris, opening to get Percatholene Dates for their Web Firewall and I would agree with you. and the next. So my suggestion to you. you would be just like that ticket that we had yesterday. and in the drop down, move it to infrastructure, but you would reach out to COVID. to Kyle, the customer, you'd send a reply to Kyle that says Hello Kyle, your ticket will be moved to Move to the Infrastructure Team once information is available. is available, we will provide you with those updates. Don't over promise anything, but just let him know that hey Hey, your ticket is going to be reviewed by our infrastructure Infrastructure Team and we'll get back to you. And you can leave it like that. If they have follow-up questions Questions, they'll reach out. But at this point, that's what you need to do. Respond to the customer Assign yourself and move it to the infrastructure to the Infrastructure team. Keep in mind with infrastructure Pacific Time. So they are the ones who are two hours behind So they would be working now, but just keep that in mind when other tickets come in if you're working earlier. I just want to remind you of that. I'm not sure who else is there because they just lost one of their people, Kyle and say, hey, you know, Russ, I assigned it Assign a ticket to infrastructure. I'm assuming this needs to be with you if it isn't I'm really good about responding. So that's what I would do. Yeah, because just like when you and I are and the way that I put it down in a document and so having that review, oh absolutely. or I'm happy to help you however I can. I Can. So yeah, but make sure I'm Sure, I'm just, you know, keep this in mind since I only have two weeks left. getting some of this other visual experience for you. is going to be as important. Amy will be here for two more months.

## Reunión 2026-07-16 — ticket prioritization · Transcripción 4/4
_chunk 1279 · 2026-07-16_

which piece is more important for me to help you with if it's if it's going through tickets, looking at the email. the email process and all of that and what you need me to do for and I'll talk to you however you need. Yup, that's good. Did you I talked to JR this morning this morning. And you know how you and I and the support emails that come in to me. I told him that you know another big review on Friday and and starting Monday, we're going to have the to help with these tickets, but they're going to copy me on the emails. and so that I can Can they help with those or monitor those, you know I'm JR asks that I put together a little bit I haven't started working on that one yet, but yeah. But yeah, so just so you're aware that that's going to kind of fall to you guys. you guys starting on Monday. So I copied you and Camilla. that's what that is. You guys are top-ied. Done. No more questions right now. Okay. Well, I am I'm here all day. So Day. So if something else pops up, let me know. You're welcome. You're welcome. Talk to you later. Bye bye.

## Reunión 2026-07-21 — Knowledge Sharing Sessions kickoff · Resumen
_chunk 1326 · 2026-07-21_

## Resumen
The meeting focused on the kickoff of Knowledge Sharing Sessions, where team members present real-world support tickets to share insights and learnings. Nikita Rathore began by discussing a ticket related to payroll check tender amounts not displaying correctly in the frontend. She identified that a backend mapping issue involving Media Number 4 was the root cause. After reproducing the issue in production, she added the missing mapping, tested the fix, and documented her findings in Jira and internal notes. She also explained the pull request process, emphasizing the importance of self-review and approvals before merging changes into production.

The discussion then shifted to repository organization and code testing. Nikita shared her approach to making small code changes and testing them in isolated environments. Another participant presented a ticket about an error in the Engage portal, where certain software was flagged as abusing return policies due to a misconfigured condition in the code. The presenter detailed the debugging process and the code changes made to resolve the issue, which primarily impacted internal databases rather than external customers. The fix is scheduled for deployment on July 29, 2026.

Golshen elaborated on verifying the Engage fix, explaining how the percentage of flagged returns was reduced to 0% through database queries in Snowflake and People’s Trust. Akash introduced a ticket about missing client transactions, noting a continuous drop in transaction data starting April 16, 2026, despite the client reporting the issue from April 28. He demonstrated how to access SFTP folders and verify pipelines in Greenplum (GP9) to identify processing errors. A failed file from the previous Thursday was highlighted, but its relevance to the issue remains unconfirmed.

Viraj concluded the session by explaining how to retrieve transaction snapshots from POS systems. He detailed the format of transaction IDs and demonstrated how to filter and locate specific receipts using backend databases and frontend search tools. The session wrapped up with reminders about saving searches in private folders to avoid client visibility and a brief discussion on improving pipeline error detection processes.

## Temas clave
- Knowledge Sharing Sessions kickoff
- Payroll check tender mapping issue
- Engage portal error and fix
- Missing client transactions investigation
- POS transaction snapshot retrieval

## Decisiones
- **The Knowledge Sharing Sessions will be recorded to generate transcripts for future reference.** — To ensure accessibility and documentation of shared insights.
- **Team members should save searches in private folders to avoid client visibility.** — To maintain confidentiality and prevent accidental exposure of internal processes.

## Tareas / Action Items
- Verify if the Engage fix scheduled for July 29, 2026, includes additional production validation to prevent recurrence. (resp: Surya) — vence 2026-07-29
- Confirm with the client whether the failed file from the previous Thursday contains missing transactions. (resp: Akash)
- Check and report the location of the Walmart database for Diego. (resp: Viraj)

## Pulsos de la reunión (resúmenes periódicos + hablantes)
### Pulso 09:22
Se discutió el inicio de las sesiones de intercambio de conocimientos, con énfasis en compartir experiencias reales de soporte técnico. Se acordó grabar la sesión para generar una transcripción. Nikita comenzó su presentación sobre un ticket relacionado con un problema en la visualización de montos de tipo de cheque de nómina en el sistema. Reprodujo el problema en producción y verificó que no se mostraban los montos correspondientes en el frontend.

**Temas:** inicio de sesiones de intercambio de conocimientos · problema con montos de tipo de cheque de nómina

**Sugerencias / preguntas:**
- ¿Qué pasos adicionales se tomaron para identificar la causa raíz del problema en el frontend?
- ¿Se consideró algún impacto en otros tipos de cheque o funcionalidades relacionadas al resolver este problema?

**Hablantes:**
- **Participante 1:** Propuso grabar la sesión y confirmó que se iniciaría la grabación.
- **Nikita:** Presentó un ticket sobre un problema en la visualización de montos de tipo de cheque de nómina, reprodujo el error en producción y verificó que los montos no se mostraban en el frontend.

### Pulso 09:27
Nikita continuó explicando el problema del ticket relacionado con la visualización de montos de cheques de nómina. Identificó que el backend no incluía un número de medio específico (Media Number 4) que debía mapearse correctamente. Tras agregar este número y realizar pruebas, el problema se resolvió. Nikita detalló el proceso de creación de pull requests (PR), incluyendo revisiones internas y el flujo desde master hasta producción. También mencionó que documentó sus hallazgos en notas internas y en el ticket de Jira para referencia futura.

**Temas:** Problema en el backend con Media Number 4 · Proceso de creación y revisión de pull requests

**Sugerencias / preguntas:**
- ¿Podrías aclarar si el cambio en el backend para incluir Media Number 4 ya está en producción o si aún está en revisión?
- ¿Hay algún protocolo específico para decidir qué hallazgos se documentan en las notas internas y cuáles en el ticket de Jira?

**Hablantes:**
- **Nikita:** Explicó cómo identificó y resolvió el problema en el backend relacionado con Media Number 4, detalló el proceso de creación y revisión de pull requests, y mencionó la importancia de documentar hallazgos en notas internas y tickets de Jira.

### Pulso 09:32
Se discutió cómo clonar repositorios en carpetas específicas dentro de las unidades de red (D o F) y cómo organizar los archivos de código. Nikita explicó que realizó un pequeño cambio en el código, lo probó en un archivo de prueba y obtuvo aprobación para implementarlo. Luego, otro participante presentó un ticket relacionado con un problema en el portal Engage, donde ciertos softwares aparecían como abusando de la política de devoluciones debido a un error en el código. Se mostró el código antes y después de la corrección, destacando que el problema estaba en una condición que no se evaluaba correctamente.

**Temas:** Organización de repositorios · Corrección de errores en Engage

**Sugerencias / preguntas:**
- ¿Podrías detallar cómo se identificó el error en la condición del código en Engage? Esto podría ser útil para otros casos similares.
- ¿Se consideró algún tipo de monitoreo o alerta para detectar automáticamente errores similares en el futuro?

**Hablantes:**
- **Nikita:** Explicó cómo realizó un pequeño cambio en el código, lo probó en un archivo de prueba y obtuvo aprobación para implementarlo.
- **Participante 1:** Presentó un ticket sobre un problema en el portal Engage relacionado con softwares que aparecían como abusando de la política de devoluciones. Mostró el código antes y después de la corrección, explicando que el error estaba en una condición que no se evaluaba correctamente.

### Pulso 09:37
Se continuó discutiendo el problema del portal Engage relacionado con las condiciones de evaluación incorrectas. Se mencionó que el cambio en el código afectaba internamente a la base de datos y no fue reportado por clientes externos. Surya explicó el proceso de aprobación del PR y mencionó que el despliegue está programado para el 29 de julio. Golshen detalló cómo verificó la solución, reduciendo el porcentaje de devoluciones a 0%, y compartió las consultas necesarias para la verificación en Snowflake y People's Trust. Luego, Akash presentó un nuevo ticket sobre transacciones faltantes en los datos del cliente, mostrando una caída continua en las transacciones desde el 28 de un mes hasta junio.

**Temas:** Corrección de condiciones en el portal Engage · Proceso de aprobación y despliegue de PR · Problema de transacciones faltantes en datos del cliente

**Sugerencias / preguntas:**
- ¿Podrías aclarar si el despliegue del 29 de julio incluye alguna validación adicional en producción para garantizar que el problema no se repita?
- Akash, ¿se identificó la causa raíz de la caída en las transacciones o aún está en investigación?

**Hablantes:**
- **Surya:** Explicó el proceso de aprobación del PR y mencionó que el despliegue está programado para el 29 de julio.
- **Golshen:** Detalló cómo verificó la solución, reduciendo el porcentaje de devoluciones a 0%, y compartió las consultas necesarias para la verificación en Snowflake y People's Trust.
- **Akash:** Presentó un nuevo ticket sobre transacciones faltantes en los datos del cliente, mostrando una caída continua en las transacciones desde el 28 de un mes hasta junio.

### Pulso 09:42
Se continuó analizando el ticket sobre transacciones faltantes. El orador explicó que el problema comenzó antes del 28 de abril, específicamente desde el 16 de ese mes, y que las discrepancias no fueron reportadas por el cliente hasta más tarde. Se detalló cómo acceder a los datos en la carpeta SFTP y cómo verificar los pipelines en el servidor Greenplum (GP9) para identificar errores en el procesamiento. Se mencionó un archivo fallido detectado el jueves pasado, pero aún no se ha confirmado con el cliente si este archivo contiene transacciones faltantes.

**Temas:** transacciones faltantes · errores en pipelines · servidor Greenplum (GP9)

**Sugerencias / preguntas:**
- ¿Podrías confirmar si el archivo fallido detectado el jueves pasado está relacionado con las transacciones faltantes reportadas por el cliente?
- ¿Hay algún patrón común en los errores de los pipelines que pueda ayudar a identificar la causa raíz del problema?
- ¿Se ha considerado automatizar la verificación de los pipelines para detectar fallos similares en el futuro?

**Hablantes:**
- **Participante 1:** Explicó que el problema de las transacciones faltantes comenzó antes del 28 de abril, específicamente desde el 16 de ese mes. Detalló cómo acceder a los datos en la carpeta SFTP y verificar los pipelines en el servidor Greenplum (GP9). Mencionó un archivo fallido detectado el jueves pasado, pero indicó que aún no se ha confirmado con el cliente si este archivo contiene transacciones faltantes.

### Pulso 09:47
Se continuó discutiendo el problema de las transacciones faltantes. Se explicó que los archivos procesados están en formato XML y que algunos no se completaron correctamente. Se sugirió revisar los logs y pipelines de varios días previos al reporte del cliente para identificar errores. También se mencionó que los pipelines no siempre muestran fallos específicos de un archivo, lo que complica la detección de problemas. Se propuso que el equipo de DevOps podría optimizar este proceso para hacerlo más eficiente.

**Temas:** archivos XML no procesados · revisión de logs y pipelines

**Sugerencias / preguntas:**
- ¿Podrías detallar qué tipo de optimización podría implementar el equipo de DevOps para facilitar la detección de errores en los pipelines?
- ¿Se ha considerado automatizar la revisión de logs para identificar patrones recurrentes en los errores de procesamiento?

**Hablantes:**
- **Bikesh:** Explicó que algunos archivos en formato XML no se completaron correctamente y sugirió revisar los logs y pipelines de varios días previos al reporte del cliente. También mencionó que los pipelines no siempre muestran fallos específicos de un archivo, lo que complica la detección de problemas.
- **Kamila:** Propuso que el equipo de DevOps podría optimizar el proceso para hacerlo más eficiente.

### Pulso 09:52
Se presentó un ticket relacionado con un recibo de una máquina POS de una tienda específica. El problema radicaba en entender el formato del número de transacción en el recibo, que incluye el número de tienda, número de registro, fecha en formato YYYYMMDD y el número de transacción. Se explicó cómo aplicar filtros en la base de datos para buscar transacciones específicas, utilizando condiciones como el rango de fechas y columnas relevantes como día de transacción, cliente y número de ticket. También se mencionó que inicialmente hubo dificultades para interpretar el formato, pero se resolvieron tras investigar y colaborar con un compañero.

**Temas:** Formato de números de transacción en recibos POS · Filtros en bases de datos para búsqueda de transacciones

**Sugerencias / preguntas:**
- ¿Podrías aclarar si este formato de número de transacción es estándar para todas las tiendas o si varía según el cliente?
- ¿Hay algún procedimiento documentado para interpretar estos números de transacción en casos futuros?
- ¿Se identificaron otros problemas similares en transacciones anteriores que puedan estar relacionados con este formato?

**Hablantes:**
- **Viraj:** Explicó el formato del número de transacción en los recibos POS y cómo aplicar filtros en la base de datos para buscar transacciones específicas. Mencionó las dificultades iniciales para interpretar el formato y cómo se resolvieron tras investigar y colaborar con un compañero.

### Pulso 09:57
Se continuó explicando el formato del número de transacción en los recibos de POS, destacando que incluye el número de tienda, número de registro, fecha y número de transacción. Se mencionó que no hay datos disponibles antes de junio de 2022 debido a que fueron eliminados por el cliente. Se detalló cómo buscar transacciones específicas utilizando columnas como ID de transacción, número de registro, número de ticket y valores negativos en los recibos. También se explicó cómo acceder a los PDFs de los snapshots de transacciones desde el visor de transacciones y cómo guardar búsquedas para que los clientes puedan consultarlas. Finalmente, se sugirió que las columnas pueden variar entre clientes, pero todas se refieren al ID de transacción.

**Temas:** Formato de número de transacción · Acceso a datos históricos · Uso del visor de transacciones · Variabilidad en columnas entre clientes

**Sugerencias / preguntas:**
- ¿Podrías aclarar si hay alguna forma de recuperar los datos eliminados antes de junio de 2022 desde el backend o si están completamente inaccesibles?
- Sería útil detallar cómo se puede estandarizar la nomenclatura de las columnas entre clientes para evitar confusiones al buscar transacciones.
- ¿Hay algún procedimiento recomendado para manejar valores negativos en los recibos, como el caso del -214 mencionado?

**Hablantes:**
- **Participante 1:** Explicó el formato del número de transacción y cómo buscar transacciones específicas utilizando columnas relevantes. Mencionó que los datos anteriores a junio de 2022 fueron eliminados por el cliente. También detalló cómo acceder a los PDFs de snapshots desde el visor de transacciones y cómo guardar búsquedas para los clientes.

### Pulso 10:03
Se explicó que cualquier usuario puede crear búsquedas y guardarlas en una carpeta específica para su uso personal, pero se recomendó no usar la carpeta pública para búsquedas relacionadas con tickets de clientes, ya que estas deben moverse a una carpeta específica para clientes. También se mencionó que habrá dos sesiones adicionales mañana y el jueves, y se agradeció al equipo por su participación.

**Temas:** gestión de búsquedas · organización de carpetas · próximas sesiones

**Sugerencias / preguntas:**
- ¿Podrías aclarar si hay un procedimiento estándar para mover las búsquedas de clientes a su carpeta correspondiente?

**Hablantes:**
- **Participante 1:** Explicó cómo los usuarios pueden guardar búsquedas en carpetas personales y recomendó no usar la carpeta pública para búsquedas relacionadas con clientes, sugiriendo moverlas a una carpeta específica. También mencionó las próximas sesiones y agradeció al equipo.

### Pulso 12:38
Se discutió sobre cómo los roles asignados a los usuarios afectan la visibilidad de ciertas funciones en el sistema. Se mencionó que algunos ingenieros no tenían roles asignados, lo cual puede ser corregido fácilmente. También se describió cómo acceder a información básica de los clientes, como el ID, las URLs y la zona horaria. Finalmente, se sugirió que las mujeres podrían liderar ciertos procesos esta semana para guiar al equipo en tareas específicas.

**Temas:** roles de usuario · información básica de clientes · liderazgo femenino en procesos

**Sugerencias / preguntas:**
- ¿Podrías aclarar qué pasos específicos se deben seguir para asignar roles a los usuarios que actualmente no tienen ninguno?
- ¿Qué criterios se están utilizando para decidir qué mujeres liderarán los procesos esta semana?

**Hablantes:**
- **Participante 1:** Explicó que los roles asignados a los usuarios determinan qué funciones pueden ver en el sistema y que algunos ingenieros no tenían roles asignados, pero esto puede corregirse fácilmente.
- **Participante 2:** Mencionó que al acceder a un cliente, se puede ver información básica como el ID, las URLs y la zona horaria.
- **Participante 3:** Sugirió que las mujeres lideren ciertos procesos esta semana para guiar al equipo en tareas específicas.

### Pulso 12:43
El tramo parece ser una mezcla de ideas desordenadas y fragmentos de conversación, posiblemente debido a problemas de transcripción. Sin embargo, se mencionaron temas relacionados con la priorización de tareas, la asignación de roles y la necesidad de identificar puntos de contacto (POCs) para incidentes y seguridad. También se hizo referencia a la importancia de compartir aprendizajes y feedback dentro del equipo, aunque no quedó claro cómo se estructurará esto. Se mencionaron nombres como Agam, Osman y Jocelyn Cole, pero su contexto no está claro.

**Temas:** priorización de tareas · asignación de roles · identificación de POCs

**Sugerencias / preguntas:**
- ¿Podrías aclarar cómo se decidirán los POCs para incidentes y seguridad? Esto parece ser un punto clave que quedó poco claro.
- ¿Qué criterios se utilizarán para priorizar las tareas mencionadas? Esto podría ayudar a alinear expectativas dentro del equipo.
- ¿Cómo se planea estructurar el proceso de compartir aprendizajes y feedback? Esto podría ser útil para garantizar que todos participen de manera efectiva.

**Hablantes:**
- **Participante 1:** Mencionó la necesidad de priorizar tareas y asignar roles, además de identificar POCs para incidentes y seguridad. También habló sobre compartir aprendizajes y feedback dentro del equipo, aunque no quedó claro cómo se implementará esto.

### Pulso 12:48
La transcripción presenta fragmentos confusos y desordenados, pero se mencionan nombres como Miriam, Asa, Xikone, Jo Poymos, y otros. Parece haber referencias a procesos de tickets y métricas, aunque no se especifican detalles claros. También se habla de la importancia de compartir experiencias y aprendizajes, pero no se define cómo se implementará esto. Se mencionan términos como KPI y métricas, pero se indica que no están claros o definidos. Hay una posible referencia a un proceso general para abordar problemas, aunque no se detalla su estructura.

**Temas:** procesos de tickets · métricas y KPIs · compartir experiencias

**Sugerencias / preguntas:**
- ¿Podrías aclarar cómo se planea estructurar el proceso de compartir experiencias dentro del equipo? Esto parece ser un punto clave pero no se ha detallado.
- ¿Qué métricas o KPIs específicos se están considerando para evaluar el éxito de los tickets o procesos mencionados? Esto no quedó claro en la conversación.
- ¿Hay algún plan para definir roles o puntos de contacto específicos para los temas de seguridad e incidentes mencionados previamente?

**Hablantes:**
- **Participante 1:** Mencionó nombres como Miriam, Asa, Xikone, Jo Poymos, y otros, pero no quedó claro su contexto. También hizo referencia a procesos de tickets y métricas, indicando que no están definidos. Habló sobre compartir experiencias y aprendizajes, pero sin detallar cómo se implementará.

### Pulso 12:53
El tramo es confuso y contiene fragmentos en varios idiomas o con palabras inventadas, lo que dificulta extraer información clara. Se mencionan términos como 'template', 'performances' y nombres como Aziz Z Bronco, pero no se desarrollan ideas concretas. Parece haber una referencia a un proceso o estructura ('at least the template'), pero no se detalla. También hay menciones dispersas a tiempos ('una semana') y posibles problemas de comunicación ('que no nos contestas').

**Temas:** template · problemas de comunicación

**Sugerencias / preguntas:**
- ¿Podrías aclarar a qué te refieres con 'at least the template'? ¿Es un documento que ya existe o algo que se debe crear?
- Mencionaste problemas de comunicación ('que no nos contestas'). ¿Hay un plan para mejorar esto o es algo que deberíamos discutir ahora?

**Hablantes:**
- **Participante 1:** Mencionó términos como 'template', 'performances' y nombres como Aziz Z Bronco, pero no desarrolló ideas claras. También hizo referencia a problemas de comunicación y tiempos ('una semana').


## Contexto capturado (notas y capturas)
- 📷 **Captura:** The screen shows a Microsoft Teams meeting with a shared screen displaying transaction details in a system interface. The discussion appears to involve troubleshooting a tender check issue for specific transaction types.
  ![captura](file:///Users/MancoMenStudio/Library/Application Support/InterviewApp/Screenshots/shot-1784643712897.png)
- 📷 **Captura:** The screen shows a Microsoft Teams meeting with participants discussing a technical issue. A code editor is shared, detailing diagnosis and fixes for a payroll check bug. This relates to debugging and resolving the issue collaboratively.
  ![captura](file:///Users/MancoMenStudio/Library/Application Support/InterviewApp/Screenshots/shot-1784643762968.png)
- 📷 **Captura:** The screen shows a Microsoft Teams meeting with participants discussing code changes and debugging issues related to payroll check tender types. The Visual Studio Code editor displays detailed notes and fixes for backend issues, aligning with the meeting's technical focus.
  ![captura](file:///Users/MancoMenStudio/Library/Application Support/InterviewApp/Screenshots/shot-1784643826558.png)
- 📷 **Captura:** The screen shows a Microsoft Teams meeting with participants and a shared view of an Azure DevOps pull request (RCS-27761). The pull request involves including MediaNo 4 for Payroll Check, with details about its approval and description. This relates to the meeting's discussion on backend fixes and testing workflows.
  ![captura](file:///Users/MancoMenStudio/Library/Application Support/InterviewApp/Screenshots/shot-1784643913270.png)
- 📷 **Captura:** The screen shows a Microsoft Teams meeting with participants and a shared view of PyCharm, displaying steps for implementing and testing code changes. It relates to the meeting's discussion on workflow, code review, and repository setup.
  ![captura](file:///Users/MancoMenStudio/Library/Application Support/InterviewApp/Screenshots/shot-1784644153588.png)
- 📷 **Captura:** The screen shows a Microsoft Teams meeting with participants discussing an issue overview and root cause analysis related to payroll checks not included in tender amounts. A shared dashboard displays data tables and metrics for analysis. The chat includes links and notes relevant to the topic.
  ![captura](file:///Users/MancoMenStudio/Library/Application Support/InterviewApp/Screenshots/shot-1784644250483.png)
- 📷 **Captura:** The screen shows a Microsoft Teams meeting with participants discussing code changes related to a flagged issue in a software system. The shared screen displays a code comparison, highlighting modifications made to address misclassified returns. The chat references a ticket and related documentation.
  ![captura](file:///Users/MancoMenStudio/Library/Application Support/InterviewApp/Screenshots/shot-1784644287272.png)
- 📷 **Captura:** The screen shows a Microsoft Teams meeting with participants discussing a code update in Azure DevOps. The code fixes an issue where price-adjusted returns were misclassified as sales. The meeting focuses on reviewing and explaining the changes made to resolve the problem.
  ![captura](file:///Users/MancoMenStudio/Library/Application Support/InterviewApp/Screenshots/shot-1784644292364.png)
- 📷 **Captura:** The screen shows a Microsoft Teams meeting discussing code changes in Azure DevOps. The code fixes an issue where price-adjusted returns were misclassified as sales. The side-by-side view highlights the modifications made to the script.
  ![captura](file:///Users/MancoMenStudio/Library/Application Support/InterviewApp/Screenshots/shot-1784644380367.png)
- 📷 **Captura:** The screen shows a Microsoft Teams meeting with participants discussing a code change in Azure DevOps. The code review highlights modifications addressing conditions for item returns and sales, resolving an internal issue affecting the database.
  ![captura](file:///Users/MancoMenStudio/Library/Application Support/InterviewApp/Screenshots/shot-1784644413850.png)
- 📷 **Captura:** The screen shows a Microsoft Teams meeting with participants discussing a technical issue. A code file (`setup.py`) is displayed in Azure DevOps, likely related to resolving the data transaction issue mentioned in the transcript.
  ![captura](file:///Users/MancoMenStudio/Library/Application Support/InterviewApp/Screenshots/shot-1784644689753.png)
- 📷 **Captura:** The screen shows a database query interface (DBeaver) with SQL code and query results. It relates to the meeting by demonstrating data retrieval and analysis for client-side discrepancies and database processing issues.
  ![captura](file:///Users/MancoMenStudio/Library/Application Support/InterviewApp/Screenshots/shot-1784644882749.png)
- 📷 **Captura:** The screen shows an Azure DevOps pipeline log for a data load process (CLS ARDM) under run #20206716.1. The meeting likely discusses pipeline execution, data processing issues, and troubleshooting steps for unprocessed or failed files.
  ![captura](file:///Users/MancoMenStudio/Library/Application Support/InterviewApp/Screenshots/shot-1784645130895.png)
- 📷 **Captura:** The screen shows a transaction viewer interface with filters applied for tracking day and display fields like store number, transaction ID, and client transaction ID. It relates to the meeting by demonstrating how to locate and retrieve specific transaction snapshots for client requests.
  ![captura](file:///Users/MancoMenStudio/Library/Application Support/InterviewApp/Screenshots/shot-1784645723694.png)

---

## Reunión 2026-07-21 — Knowledge Sharing Sessions kickoff · Transcripción 1/17
_chunk 1327 · 2026-07-21_

## Transcripción completa
or others to ask. And the end is that you guys learn of what your teammates POC. So, hey, let's see, like, Viraj will is working on XYZ. because he has some knowledge about it. I plan on this. and what your mates are working on, mostly mostly because I don't want to just give you documents that were and Real Issues that the customer has. That's it. Any questions, any comments Any comments before we get started? Okay, great. Okay, great. First question, do you want this to be recorded? and I can send a transcript after it. or it's okay if we do not record it. It's up to you guys. I can tell you best if it is recorded, Kamala. Yes or no? Sorry, I didn't hear you. We can, we can record. who wants to get started. I can start. Okay, Nikita, go for it. Go for it. Let me just start recording. If you want to share your screen, that will be great. So we can start it Kanneh, Start Looking at it. Thank you. Go for it. Okay, so it was a small and a small ticket, another small Delhiz, Paul Klein, The Klein The Client Ideas 46. So the issue was Who Was, Becky Was Not Able To See See, Tendercheck Amount for this Tendercheck Tender Type, Pore Payroll Check Tender Type. So So, first I have reproduced the N1-1 thing, like He or She. So, Becky also won the The Following Tender Type To Be Included In Tender Checkup Kenderchek Amount. So first I have reproduced this and the bug for this transaction idea in and Production. So I can see the The, For The, Tender Type Payroll Check, We Don't We don't have any Tendercheck amount. So first I have I have checked the files where The Front End is for Delhi, but then from in the back end for the news. It's a huge It's a US client, so I've connected, I've and the remote server, so I have checked there. So I found out that we have We have two media numbers for this for the same payroll check. So we have India number Number 4 for Payroll Check and Media Number 36.

## Reunión 2026-07-21 — Knowledge Sharing Sessions kickoff · Transcripción 2/17
_chunk 1328 · 2026-07-21_

In this set where we are checking the media The Four was not included because because originally it was referring to paper footsteps. Food Stamps, but later it was changed to Payroll Check and it was not included in the site. That's why it was not mapping, not getting After Adding The Mega Number 4 In The to test all the backend fixes through and Rupai Jam before raising it for PR review. So I have tested There, and I have asked Claude how I can test it and Deepa Echam, so it suggested me Dutta, who's going to meet. Suggested me to add this This Script at the Bottom of the PBT and I have done that and it worked fine. I have raised PR for the For the Client 46 is like we don't just create and others create PR directly from our working PR directly from production. We first create a I'm sorry, I think we lost Okay, so we first create our walking peer from master, we do self-doubt. and then again create The PR4 Same Fix From Master To Production To It will be merged into production. Production, The Pipeline, The Build Will Run For This, And and it will take some time to and, you know, after the build is finished, if they can see the change or not. and I continuously add my findings in the Nik, Generate, Internal, Notes, With, Root, Cause, Finding, and Other Things and other things to add in the and the Jira tickets. So that's how I can I can keep track of what things I have found for future Future Reference, So, That's How I Have Walked On This Ticket. Perfect. Thank you, Nikita. Nikita, Anybody has any questions about what Nikita shared? shared. No questions but Can you help me understand the pull request, how to be merged? Aya, So, We Create A Local who make our fix and then we do the self-review. and the Chief Review for that grant, for sorry for that That, Here, And Margit into Master by Arsenz. and then we create the same fixed branch for and for the, from Master to Production. To get it reviewed by other people. and Get It Approved. So, I got a couple of minutes.

## Reunión 2026-07-21 — Knowledge Sharing Sessions kickoff · Transcripción 3/17
_chunk 1329 · 2026-07-21_

Nikita, from the, yeah, from the Data Team. Kino, Virgil Machine, Right Now, Irene Do we have access to this repo on our We just have to clone these in our folder We have to create our four units folder in the drive under data science. The, Initial of First Name and Last Name. and then we can create a code folder inside this and we can and we can clone a repose here and walk on. and both of them. because I don't have that one. No, uh... You May Have F-Drive, It Just Be It Should Be Either In D or F Because Everyone Creates Their Folder Inside DRF Dior, I have tried and I suppose that you can prove Improve your changes on this machine, yeah? or can you prove this challenge? Do you ask me? How do you prove your changes? or any environment, I don't know, the developing vitamin or or just write changes and Hope that it works as you expect. Okay, so it was just a small change and all changed to, so I have just tested it in the I have added that change in PD test We Test a File and Run That File It, Vaux, So, and I have a question. and I have asked payment that I have done and this and it's and it was so he just approved it here. Oh, okay. Great, perfect. Thank you, Nikita. If there is no more. No More Questions, We Can Jump With The Next One. So, Voshan, Thank you, Our Viraj Nikash, Whoever Wanted To. Simas, Cleo? Yes, so we are seeing a potion. Thank you. and others. Thank you. Ked, Yeah, Thank You. So this was the deeper time. I think on Friday of the day we first started, I don't know I don't know, but yeah, I got this sticker, this sticker was This ticket was exactly what, basically a flag came on, for a particular Parapetkar, Kaunta, basically what was happening, some softwares were showing up in the engaged and Gage, Portal, Right. So, they were showing as a return overuse signal. Over-returning the things or they were abusing the return policy and all that.

## Reunión 2026-07-21 — Knowledge Sharing Sessions kickoff · Transcripción 4/17
_chunk 1330 · 2026-07-21_

But there was an issue in the code, so and Kannada, and we will be talking about the number of people who have been and if you can see the least classified item and the total number of return. This was the item we needed to remove. So, this could not be here. And why it was not because of some flag that was not matching the code, right? So let me also show you the code that exactly Yeah, it can be so So, this was the before, before the This is what I changed and this is what I have I have rectified here. So what is happening and what will and what was happening exactly. So when there was a case when A dot quantity and after basically a sale came in. K.L. came in. So basically, A.DOR quantity is greater than 2. It means it's a This, When, Zero, Turn, This, Not, Not, So, The, After, Check After checking this condition, A dot quantity is directly going to the next condition. Rishikeshwaran, I have just, you can see, just the readings of the position We are checking that condition and then again we are checking error quantity greater and it is a sale, right? And what we were doing before, we were not checking that condition. and all of that. Every time we were having this price adjustment and it was and taking it as a mortar return. So, this is Change That Was Affecting To The User and into the database and it was an internal, it was not a and customer raised with some of the right Samnadarit, it was an internal picker. So, yeah. Surya mostly, if you can see Yeah, I think if anyone have any question or something, you can ask. Gautam, How Long It Took and Rok to get the PR approved. Nikita, already, Manthar, Viraj So I have typical neurons with this name, like Once you are done with this thing, it's right, it's as much as you can do the Master, and one It can like auto merge into the master. After master we have We have to raise the PR request and then you will have a couple of Kapalaka approval, like we need to get approval from team.

## Reunión 2026-07-21 — Knowledge Sharing Sessions kickoff · Transcripción 5/17
_chunk 1331 · 2026-07-21_

So, yeah, it got quickly, but I think it will deploy one I'll don't remember let me take the release test. I think on 29th July it will get deployed. So, you can see this is still a straight-aside. Okay, no, I'm sorry. Okay, this one. This is the one. And after one city is in production, it will get and it will get fulfilled. Okay, great. So, when it was on production or It was internal ticket, right? Okay, yeah, I mean the internal customer. So I just, once we are done with everything, I just posted my documents, if you can see the same, here you can also, okay, so I have mentioned all the things in my file. Great. Any questions, guys? Yeah, to verify it, you need to run So that's how I verified it. So after verification, this number came to zero. zero. This percent of return that. So after After you will verify it, it will come to a 0%. And I think all the queries, if you want, you can check it also. So all the queries and everything is given out here. So So, Yeah, For The GP cluster, For The Backfill thing, You Have This Query It's a very easy query, you need to run it and for the production fix, it is also given it here. on the Snowflake and as well as the People's Trust. I guess no one has questions, so I can talk to my team. Yeah, perfect. Thank you, Golshen. Yeah. Who's next? Vikesh, Viraj? Akash, you want to go? Go ahead. Yes, thank you, Viraj. Okay, so before she Before sharing, I'll just paste the ticket that I've been working on. Okay, so for this particular ticket, the client had the issue that and the issue that the transactions from their side was missing. and after the data load, the transaction which you You can see over here in the graph that they have shared with us the DD transaction transaction was somewhere around 4.2 to 4.7 This was the day that they have mentioned that after 28th, the transaction and the transactions started dropping continuously throughout the year.

## Reunión 2026-07-21 — Knowledge Sharing Sessions kickoff · Transcripción 6/17
_chunk 1332 · 2026-07-21_

throughout the month and it was I mean I mean, like till June, it was, this was the consistent behavior of the data load that the transaction has been falling. Right? So, this This is a ticket that I picked up midway and Mahamud was working on it before I Before I picked it up. So, what he, I mean I mean, if you go on the ticket, you can see over here that what he has mentioned has mentioned like the 27th and 28th was like and, I mean, the day from which the transaction and I mean the transaction number started falling, right? but I mean the issue The issue over here was not from 28th, what I found I mean, like before going on all of those details, like where we can get the file to the setup.py file on the code for each of the client location. This is basically the location where the The Location of the SFTP Folder Where We Receive all of the and all of the files from the client side. So if we just go on to this particular location, we have We have to just connect to the remote desktop server and, Like, You Can Get The Data, Right? So, for each of the clients, we have this data present over here. So if we go on to 2026, we have different months. and we received the data on a daily format. So, we will be getting the and we are getting the data over here. So let's just say we move on to print. Dita, This Will Be The Day, Date, 26th, 6th, I mean the 6th Month and the 20th of Day. And We Receive This On, Like Even before 28th of April that the The Client Has Said That The Data Level Data Level Started Falling, I Found Out That From 16th Onwards Like 16 was the baseline, the last day 10 I mean, there were discrepancies I found out and this has been going on even before the client reported the issue.

## Reunión 2026-07-21 — Knowledge Sharing Sessions kickoff · Transcripción 7/17
_chunk 1333 · 2026-07-21_

issue and this is something that has to This has been going on and after Like, Checking all of the details and I mean, we also checked on to, I mean, since Since this particular client, we can go onto the pipelines and and we can check that whether or not the data is getting processed properly. properly. So, if we just write the client code Code, We Can See Over Is A Trickle Client And They Use GP9. P9, As the Database Server, Right? So, we can go on to the Database and for that you can, I mean, like, I can show you You, We Can Connect On To The Green Plum and we can just write a simple code, simple SQL query for that particular date and like if, if any If Any, I Mean, For That Particular Date, If Any Pipelines Have Been Failing Or Not. Kaling or Not. So all of these things that we have to check before going on to any conclusion. and Pankajan for a recent processing if If I go on to this particular, like this is from This is from this current Thursday. And if I go on to that, you can see over here There is one file that is getting failed, right? So, this is the file. Green Prom Server, Right, and They Can Be Different Errors Processed the File and if, if anything, I mean, this has This has still not been confirmed by the client's end, like if these particular pipes and other particular files had some transactions that are currently missing. So, this is basically how we can check if there are any errors On the Data Side, If the Processing has failed at any level Level, we can check from going on to all of these different steps. and the correct format and if like the data size was correct or not. and all to any conclusion. Anyone having any kind of questions in that, in this particular thing? Because you are showing some love, right? So, as I showed over re are multiple different files that and, I mean, they are encrypted files, right? So, if you If you go onto these logs, these data pipelines, you can see You can see each of the files getting processed.

## Reunión 2026-07-21 — Knowledge Sharing Sessions kickoff · Transcripción 8/17
_chunk 1334 · 2026-07-21_

I mean, this This, You Can See Over Here, Like ExeML Document Did Not Completed, Right, You Can, You Can See You can see the entire file name and and the batch in which the file was received, what I showed over and Shon in the field file. This is not processed. So what is the issue that which which is why it hasn't been processed. You can, I mean, that is is an XML format, so maybe the transactions, the tag We Processed and for this particular thing we have to check like different run This May Be The Error, This, I Mean For Different for different files and for different days also and this may be an own issue, right? And it may be possible that even though this file is failing to get to get load We have to check for different days as well, not just on the day of the issue that the client The Client Raised For The Loading Of The Data of the data. I hope that answers your question. If you want to go on, I mean, check the logs. This is a trickle client, right? You can see over is a trickle client. So the data is processed through Processed Throughout The Day. Because, so, if we are getting data load Check all pipelines that they run for our love Lok with the Net or Yeah, Yes, Yes, You Can Go for For, Like, A Few Days, Prior To When, The and the client have raised the issue and you can start checking from there. There, Because Just Taking on One or Two Days for the Data Pipelines, Won't give you the correct Rizzo, Correct, Answers, That You Are Looking For, Okay, But But y, they pilot, okay, our, uh, Aplist team, I think that they these pipelines too because all pipelines are successfully. So if we are looking for an error, maybe this pipeline should show an error on this build.

## Reunión 2026-07-21 — Knowledge Sharing Sessions kickoff · Transcripción 9/17
_chunk 1335 · 2026-07-21_

I mean, it should be showing, I mean, I understand what your question is basically, but in general In general, these kind of things, if the entire process is not failing because of one file I mean, even if we try to change it, even if we try to make any Do to a one particular file, I mean the pipeline won't show it as we This Takes A Lot Of Time, You Know, Searching I Fail Here It takes a lot of time, so maybe our DevOps team Team, called, called, improved AS, but okay, thank you so much, Vikasheet. If this is easier and faster for you and you have an idea, work on it. and see if you can implement it, okay? Yeah, sure, sure, Kamila. and all of that. Perfect. Thank you, Bikesh. Anybody else have any other question? Okay, Viraj, you can go in. For the last minutes, share your ticket, please. Yes, sure, good answer. Thumba. Okay. So I have this I have this ticket. So basically, sorry. Sorry, sorry, sorry for this interrupt. Guys, someone knows where a Walmart Martin, Working on Database. Do you know, do you know it, Viraj? We cannot find it. Just as a parentheses conversation, Sarvi. I don't know where it's database. I'm looking in SQL, I'm looking in Snowflake, but they are not. David, do you know? and Kuna. Anyone else? I'll just check Diego if I can find it. I'll let you know, just give me a minute. Okay. Meanwhile, Viraj, you can go ahead. This particular receipt, it It Looks Like This, So This Recept Was Basically From Their POS Machine, And and basically what they were asking was I need the APPRIS transaction snapshot from the Mark store. This is the store number. This is the register. This is This is the transaction number, the date of this was April 2nd, 2025, okay. This was the whole transaction number. So, on looking at the receipt Trans number. Now, this is the receipt from their POS machine, right? Now, some Sometimes in order to find these old tickets, we have to understand how their POS machine Technology System is linked to our existing secure.

## Reunión 2026-07-21 — Knowledge Sharing Sessions kickoff · Transcripción 10/17
_chunk 1336 · 2026-07-21_

Try to open up this customer First of all, we need to understand like, you know, in what way the particular particular transaction IDs saved. So initially I was not able to understand I tried multiple ways but later on working with my buddy what I understood was and all of these things. and the transistor number, trans number, transaction number or ticket number. On doing little of, you know, little bit of research through this cloud, what I found out was basically this transaction number that they have, we can see at the bottom of this ticket, right? It is not the trans number, but basically it consists of multiple things, right? So the first three digits are the store number, the second two digits are the The register number and then we have the date in the YYYMMDT format and then at last there will be the will be the trans number, right? So, once I understood this format, what I did was It was, if you log into the customer and if you and if you click on this magnifying glass, it's called Compose New Compose New Search, Basically, Either You Check It On The Backend Database Or and which date the invoice or the transaction receipt was created. That's the trading that they call it over here. So, what you can do is you can filter the result through the condition. Conditions, I already applied the conditions over here, like trading day should be Today should be between March to September and if you want to see like you know mentioned, Trajection, and whatever fields you see Whatever fields you want to select, you can select over here. transaction, client transaction, different columns I already selected over here just to show you, trading day, client transaction and Transaction ID, Transaction ID, Ticket Number. Based on this filter, this is the result that I am seeing. Now Now, for some reason, I am not able to see any data prior to June 2022. 2022.

## Reunión 2026-07-21 — Knowledge Sharing Sessions kickoff · Transcripción 11/17
_chunk 1337 · 2026-07-21_

So I will not be able to show you exactly like, you know How I was able to find this receipt for every for April 2nd because we don't have any data prior to June, June June 22nd, it looks like it has been cleared from the customer side, but technically But technically what I did was, I understood this format This Format, Like, You Know, How This Transaction Number Is created and I did some R&D and Transiction ID, this is what I see ok. So, if we let If we let see like particular client transaction ID, then Then, the first thing will be the store number, register number Then this is the date, 22 June 2025 when the When This Particular Transaction Was Created For 14.9 and then last is the Trans ID. So this trans ID is basically what we see at the bottom of the page like you know Like, you know, this is the trans-IT for that particular day. So So, on understanding this particular format, I just selected the Trading Day as 22nd of April, specifically. and in the client transaction ID, right? I just used some while collectors. This Particular Field and for April 22nd I was able to find the to find the particular entry. And then customer actually emailed you know, couple of more and a couple of more APRIZ transaction snapshots. So I was able to pull all the snapshots for them at that time around July I will not be able to show you the exact transaction receipts, but if you are able to If you are able to dig down to this particular search, then you can just click this I This, I Symbol, and you should be able to see the particular PDF for the The Apple's Snapshot that they were asking for and you can just download the PDF and send it over to them. If you want to see it in the transaction viewer, then if you click on any particular row entries or different entries that they did on June 22nd.

## Reunión 2026-07-21 — Knowledge Sharing Sessions kickoff · Transcripción 12/17
_chunk 1338 · 2026-07-21_

So just Just a quick way on how you can filter out the Compose New Search or What Are The Different, You Know, Transaction ID, Or Register ID, Or Tan's ID or Ticket Number, right? These are all the and the common definitions, but these are all the common Common Column Names that you will find on the different side of the customers. Customers. So, if a customer, this particular customer had a client transaction ID as the column name Column Name, but some customers will have register number, ticket number, or trans number. Trans number, something like that. But all these columns technically refers to the transaction ID. and the POD for a particular reset in that POS system. So, yeah, just a quick view of, you know, how you can How you can search it from the front end. But yeah, we can also query it on the database on the Kita based on the backend and try to dig down based on the based on the POS receipt that they have and also the second So the second thing is the value of the receipt, it was minus 214. So I was able to find this particular receipt. So the client pure This transaction snapshot is something that looks like this. Yeah, so I was able to I was able to dig down and find the necessary receipts that they were That they needed and that was all the requirement from the client. and on this particular ticket. Anybody has any questions? No, no questions. Viraj, just a suggestion. If we save any search, our client can and see this search. If you are saving this search If you want, all these runnings is something I was doing in my profile. Rofl itself. They also can't, we'll see. Yeah, I don't know any, any use Any User Any User Can Create These Searches but They Can Save These Searches on Preview and Iconon folder below there. Rider, On Right Side, On Folder, On Folder I So you can see all searches done our On the public, on the public icon left there, on top left. Your Files, Your Own Files, This File Is Just For You You, Not For Our Clients.

## Reunión 2026-07-21 — Knowledge Sharing Sessions kickoff · Transcripción 13/17
_chunk 1339 · 2026-07-21_

So, If We Are Working On Any Ticket B folder, okay, not on public folder, please, because we move We move our client searches in this folder. Just a suggestion, yeah, just a suggestion, recommendation. recommendation if you are working on the Search Composer Kit of any of your Any of you guys, yeah. Thank you, Dash. Anybody has any questions? I think all good. We are on time. Thanks everyone. Perfect. I think this was really useful and helps and helps us a lot. So we have two more sessions tomorrow. Tomorrow and on Thursday, so please come to prayer and I will send to Thank you so much, team. Have a good one. Thank you, guys. Kannada, Kannada, Kannada, Kannada Kia ora, Kia ora. Oh, I see. Yeah. It will show you what roles you're in when will depend what you can see down the side here. If you're not an The role we need to be, we can fix that. Easily. Okay, so if something's Like, for example, I was looking at the engineers yesterday and they were in no roles at all. This is just a list of all the customers, as you know, to sign into a customer It will tell you the basics of client ID, the URLs, the abbreviation Abbreviation, What Time Zone Ah, okay, okay, okay. Itadakimasu! Nio, I'm going to be in the room with you today. Como a esquital vatu semana? My name is Tulia, because I am a woman. Kia or Kaparit, Rataarambhir Koneso, Kida Siyas Parmirari, Gualu Kosa Esta Davinda Lopez-Hapue See you Samos, we are done. and Aha, Isaac, Wun, Supra No, no, look, where is the Rathore? Wait, let's take a look. Velke Tienes Dos, Yambo de Stanan de Costo Kondala's Priestess with you. Thank you. Please, ask me the most technical answer. I'll ask that you please speak at some one or two end of time. Saitri-Finn, When, Si, Listo, Sige, Sige Raisa Nesos Tike Tskoneja Kupa, Kya, Como, Orana, Kupa, Nikum, Kamilayo, Abhlar Deque, Alo, Onseno Seiken, Esa Sola This is the place where you will be in the room. If you don't know what happened, you will be in the room for a few hours.

## Reunión 2026-07-21 — Knowledge Sharing Sessions kickoff · Transcripción 14/17
_chunk 1340 · 2026-07-21_

Koma, Aora, Spung Kami, like, Konfwan, Yellow, Delis, and Apna, Oda, Spung Kami, like, Konfwan, Ito Kajunun, Kramusaw, Lal, Naintyen. Roshunarunya Koneja Manana Deva Naora, Hila Egane Korro Kamomira, No, Thir ish katinditen. AIM, TUAPONEL COMO, POR QUE POGONES SESITO, TEL AGRIGAR COMO OPTIONER, EI HUARN, POR QUE POGONES SESITO DAR TEL OQUE SESUPONEN QUE ASE MOS AORA And this is a daily fast review of the whole thing Khelopu, and El Tike, El Elhekum Amira, and the other people here. Kaleiha Adeyar Koma Sadeha Kalei Aloh. They are suggested women this week so we can you can guide me to the process of you do everything We have to let food go. Sauer, Panenten der un poquito maces. Poratola, e mezito kuto en más. Tho and Masthas Kits. Is, Arce Poyo, Nus Pomma do Pockitoma de Tiquets, porque Porkay, Slarr, Sumat just to start them at the in-fetran the for me with one a head and the other side of the world. and Piazza Travajarlo and Miriam, Como Que Puedenas iraciento. Daciendo, Bisteloke Compartio y Cash. Awe, Farkil sta Olland Langan, Sarakloth, Korn, Kornado, Padarizarlo, Spikings Ashur Debs Ops, Jesus Al, Empara and Parita, the five lines that you can see here. Is it not a syllabus? No, go for it. Agalita. Kizino, Pascale, Limpia, Teatro, Harpisto Chisto, Yeah, Magna Naja, Vakuparthi, Loan Koy Todole, Unco el contolequi, ¿Pus decir el calendario y en más? Como buención a dulce un confuen spéx, explica como hacer el sera Meera, Como se resi en un sia se ajno míchte las Alertas Que espera, Sita de un puede tienes quiez hacer, Ado de esa puede As I said, the high priority is to have Agam, Osman, La Efinician de la Prioriad, Es Normal, Virajarita and Shabita, Meghuanike, Pasasito and Sivus, will refer to you, if it's a second time, for the next time. Salah, Siempre Una Parrilla, Clado, La Graciez, Kelsa Condar, No Tenga Que Star and Kia O'Hara, and Katia Gampesh, Sister, the Secondary, but we will see you later. I.K.

## Reunión 2026-07-21 — Knowledge Sharing Sessions kickoff · Transcripción 15/17
_chunk 1341 · 2026-07-21_

Guar, Jojame Conseguilos POCs para vet quienes tambjól de engage, quienes tambjól de incident, quienes tambjól des Sanko, Desecure, Durante, Asuras, Ehm, Espara Quesde Estamil, Bey, Nos, E Nose, Pudya se aki impregunta, Si aikeb asepe te chas a ninte de Me, La Cantilla, El Volume, Me, Inexis, Teng, Te Casi, Uranus, Asura Asura, Escrucion Desuertes, Inditeragmí. and, for example, Jocelyn Cole, who is also a man, who has been a member of the and I will be here in the next video. Intuosus, Pray, Tures Como Térigal Primo and the first one, the second one, the feedback of the team. Samyandese, Okuminto, This World of Common Sheets, Sheets, Parasa, Viraj Yes, and, yeah, Mahasadhiya. Ah, my love, thank you, my love, thank you. Dola y que esperar a su primo de hace bano, en ojol, a voy, como se sentía. Kiya, Pero tiemas que segura que el no má quere. Aser un colinú. This is the last time we have met. Muisa Guramenti, Aksa Sakhra, Ojo, Joleah, Jaya, Ojo Oh, Yawrita, Tengmas, Arderun, Kukapi, Yawasira, Kapi, Yawal, Jodh, Beritikke Kiki, or Kijome Kwenta, via la matri de Roles, Kijoles, Kijoles Uth-Ledman de Asekumu, Dos Meises, Apenos todas entra, Esamatris, Der Olí And the only thing that you can do is to be with them. Averci ayo, Trappusici, Sion para el dentro en nueva. What is the time is not to be a parent what better place. and Kola, Kamsis, Noah, Ashira, Kapi, Nida Kwan Te Mando Kun Kanthiato, El Windhami Mando Kanthiato, I Buena Espo de Viel, Mira Miriam, Asa, Xikone, Jo Poymos, Kooli, La Posizio, Marapio Tu hare se el venticiete, wah biraj, aha, esa tu toca, se el dos biraj, el del tres al nueve, y el seria el días, al días, se. Tú de tú el cloc que esa apenas, tiempo para y tan sara, se, en tres vistas, y ciel de piníciamentes, y que no pújo le deguo a capir.

## Reunión 2026-07-21 — Knowledge Sharing Sessions kickoff · Transcripción 16/17
_chunk 1342 · 2026-07-21_

Ben, ese más Estema, No, No, Sesi, Que esa aliga, Or, No, Ses, Porque Pejón Kepal Jeon Ueyas Perar Osajeon Okeiros Ereso Pero Jeon Okeiro Khelmera Núsis Orela March Sinha Masvinastar, Kommo Auntie Sipa Nikita, Asme, Toma, Osas We are going to be talking about the new year. Masala Salkin, Mimata, Adyopirukisto, Koton, Dokhepore, Techo Megharekon, Kapil, Pores, Pero. This is the end of the day. I will be here in the next week. and the General Contratain, which is the place where you can join the team. and others, generally, at the University. And this is a better way to look at your problems. Aoi nus tirei san do todo tsuki ka tsukiyaan muzo tiempo Sotempoertos y la respos aclentinos de especial. Por qué la cantilla y tiquets de ona chiarra. Anakya, Rlibera, Als, Terenza, Yuno, Es másías. Uno cienta y seis tikas. Dethora, L'Hinte, Kios, Heo, El Tous, Yoko, Hous, Siki, Amadou, Nase, Manata, Los Hietas, Los Hietas. Oya, Mi tepuestin, Siesta Siesta, Mofus, Perando por Eclentina. A and El Total Bapil. Auditai, Trintai, Sis, Yolo, Rises, Tamanyan Daxianne, Daxianne, Eperon, Bintil and the Indian Book of Cinco tickets. Kya pothar kran sa yu, Osa el teres Elthres, Dreyelmit, different time as the year. Elthres Joya Signar Le La Mita Lu Stiketh Dala Hinta Kessush Kwe Avidash, Ilaukamitat, Pati, You says, not one I screw this way, even Kedos, Kua, Nuza, Reza, Ramy, and Teotro, Ocicado, Uno, Iso, and Rachid As a CEO, I am very happy to be here. Nartiket, Noes Porque Que Tous Saes Ono Saes Porque Aida Masil Y Jeonopo P.E. Journal of Open and Global, D.D. and P.N.M.N.C. Synchotic, I don't know if it's not Kipnada, Aali, Ben-Pizzi, Kortiket, Yaavi, Das, Ochru, Kipi, Nivit, Dit, Sajanoti and Senti. and Compassion. Lo e no, no iKPI, no iMetricas, Todori. So, I feel this noise, but I don't know what it is. I'm not sure what it is, but I'm going to do it. Na'eta, Meinu Porque Tansoi Kenvises. Inosto, Kenpesar, Amida, Cuanto, Tempo, Nacis, Tambur, De Mural. Es Basao en Espía.

## Reunión 2026-07-21 — Knowledge Sharing Sessions kickoff · Transcripción 17/17
_chunk 1343 · 2026-07-21_

Taudita no i Plo Cí via, Es implemente para de Tini. Kini, Sia Zawiri, Amatrah, Lano, Sotrif, On. No, yes, it's not me, it's the process, it's the process of what is done. El Estoma Azer Las Cozas porque puesclaros Experiencios Diencios, Hátuno pues pretende que tu pues hacer todo. San los El Mismotriach time ketetoma hacer un tiket que nú Ked, Ken, Nunkad, Vistun, Tui, Aida, Ivemaas, Aum, Aamira, Dase, Tenokimira, Sos This is what I say. Para el kitantiramos a masal de aqui a finale de año, pa pero no hacer de. Te, Tu Performances, Tatte, Rile, O tu Performances, Pura Ora, Lóm, Sae, Hallek Chisto, Tu tienes alibo de tulao, tienes de cita de milao and the name of the space. Contestals, yeah, okay. Listo, esta This is perfect, perfect. Ito no pues de siento. Stiabro, Osya, Kumata Tarle, Ruprosi, Lopi Kosel, Lopi, Shreksen, Singh Clerd. Okay, thank you. Okay, at least the template. Jano Tingonamas, Koda Oda, Aam Thank you. See you guys. Kesh, Piru, Nyoh, Kete I hope you can see See you then, all see, L'Anse, you start. Aziz Z Bronco raised her childobTimes Kinte, Enos Curia, Como Dime que si es la ist a lo que tesquimi por favor, que no mejas tem bisto. Salcual, salcual, los eso mi, zhomiz, zomiz, como, nosotros, somos esquintes, como, Dime que paso, como, mira Mira, la Agerda, Alhuani, Samus, Perna, Pore, Contar, Qui no nos Contestas, Una semana, Sí, en bargo, ¿Qué a lí, semos? ¡Polo a. Or, Lola, Si a la Temana, Juan Seguino Sestando. Asi uno se espero, nos aikia el gustanacín. Dios que se es? En sac, pero en omeda. La jalá, heboreas. Khola Parnano Jai Ghar, Atraaha Ah, Ah, Sathe Kurtiyao Pero Puesi, Gual, Dornuya Cessuis, El Manuya Cessuis Ditro El Santo, Jono y ese ditro el santo, Sano y ese choco mo, A es que cuán?

## Reunión 2026-07-28 — email and ticket management
_chunk 1407 · 2026-07-28_

## Resumen
The meeting focused on the daily workload management of emails and tickets within the team, emphasizing the division of responsibilities between the EU and US teams. Participant 1 explained that their primary workload involves handling emails and tickets, with proactive tickets being generated by alerts. They noted that some tickets require technical assistance from the development team and highlighted the importance of addressing the backlog efficiently. Coordination between teams was discussed to avoid ticket duplication, and Participant 1 shared their approach to monitoring team chats to identify existing tickets and inform relevant teams promptly.

Additionally, the challenge of adapting to the workflow and prioritizing tasks was mentioned, particularly when dealing with tickets that require immediate attention versus those that can wait. Participant 1 also briefly paused the discussion to respond to JR, who informed them about being on a call with Camilla and Juan. The conversation underscored the dynamic nature of ticket management and the need for proactive communication and organization within the team.

The meeting concluded with a reiteration of the importance of managing the backlog and ensuring that basic tasks are completed, especially when Level 1 support is unable to address certain issues. Participant 1 emphasized the need for clear labeling and coordination to streamline the ticketing process and maintain efficiency across teams.

## Temas clave
- email and ticket management
- EU and US team coordination
- backlog prioritization

## Tareas / Action Items
- Clarify how tickets are prioritized between EU and US teams during significant backlogs.
- Investigate if there is an automated system to identify ticket duplications before they reach the backlog.

## Pulsos de la reunión (resúmenes periódicos + hablantes)
### Pulso 14:08
Se discutió sobre la gestión de correos y tickets en el equipo, destacando la carga de trabajo diaria y cómo se divide entre los equipos de EU y US. Se mencionó que los tickets proactivos se generan por alertas y que algunos requieren asistencia técnica del equipo de desarrollo. También se habló de la importancia de manejar el backlog y coordinarse con los equipos para evitar duplicidades en los tickets. JR interrumpió brevemente para informar que estaba en una llamada con Camilla y Juan.

**Temas:** gestión de tickets · coordinación entre equipos EU y US

**Sugerencias / preguntas:**
- ¿Podrías aclarar cómo se priorizan los tickets entre los equipos de EU y US cuando hay un backlog considerable?
- Sería útil saber si hay algún sistema automatizado que ayude a identificar duplicidades en los tickets antes de que lleguen al backlog.

**Hablantes:**
- **Participante 1:** Explicó que su principal carga de trabajo es gestionar correos y tickets, y que los equipos de EU y US tienen roles específicos en este proceso. También mencionó la importancia de manejar el backlog y coordinarse para evitar duplicidades en los tickets.
- **Participante 2 (JR):** Interrumpió brevemente para informar que estaba en una llamada con Camilla y Juan.


---

## Transcripción completa
Okay, so like the kind of emails that I have and the other details that you think is important. I know that you do a lot. I love it. I mean, it's insane the amount of tasks that you do every single day. How is that split or is only you doing that? that definitely it's what I do, right? That's my main My main workload is working through the emails. The US team isn't on yet. I've got to kind of push those forward. If the EU team can't get to the tickets, right, then I've got to start doing what I can. and what I can with the tickets and wait for someone from the US team who could do the technical piece. Peace. Yeah, I would say the big thing that that is probably going to be the biggest challenge is getting used to it. This is something that can't wait, I need to get it done or the backlog, you know, and getting through those tickets. Kids, and making sure to just get the basic stuff set up that maybe L1 didn't get done because they try and help Data, Support Team labels, and some of that stuff just kind of on the ticket. You might be changing. Hold on just a second. JR is actually pinging me. I'll let him know. I'm on a call with Camilla and Juan Sorry about that. No worries. So, yeah. That's kind of the big thing is knowing that you got to go back to the backlog. You know, get yourself in or I see something happening in the teams chats. I'm like, oh, wait a minute. There's a ticket already here. I better let this team know about it. So it's constantly moving. Okay, guys. I know our TS tickets tickets are proactive tickets that are created by alerts and the others I know that we need to take into account both, but I see that I guess because No, they see them first. And if they need assistance with the Mega is what they may get pushed to the developmental tutoring.

## Reunión 2026-07-30 — User login issues · Transcripción 1/6
_chunk 1413 · 2026-07-30_

## Transcripción completa
Let me put down all the tickets Let me share my screen. Sure. So, I am just discussing real quick All the things for this ticket We can see the attachments, so we have just asked them to to retry or if they are facing the issue with any other documents. There was a comma, so engineering is anyhow going to maybe apply the fix for that one on this one we have already We have already asked, the user was trying to log in but that when the user occurs user account was set up, right? That guy never, never logged into the and Lachlan to this account. His name was Eric. So basically what happens is they pass the global ID to us This is like a product product thing, this is not a very top priority, so they can They get the emails where the email address is written, but in front of the email of the email instead of their name, we have the product name, right? So they want to get this changed like so, this is not super urgent Regarding this, this is also This is already been looked in by Kiran, we already discussed with her We also impersonated and tried to check We can see this is America, New York on her profile we said will be set for now and if she confirms right we We can just go ahead and change it for all users. Okay, so we are just waiting for the conversation for the confirmation here We provided them the non-SSO basis is equal to true. Now, this is the parameter we had. She mentioned She mentions she is still not able to log in. I believe she is confused. We just ask, provide the User that they have used, so we can trace the exact Exact email id for world for the non-SSO based access. I am not really sure, so maybe one you will need to work for this one with Matt This one, Matt, this is This is basically unable to use the Isenda System updated in the morning and unable to access IZENDA to update some reports Yeah, it looks like it's mostly a performance thing we are investigating.

## Reunión 2026-07-30 — User login issues · Transcripción 2/6
_chunk 1414 · 2026-07-30_

So this is one thing, maybe we can provide the updates on Checking on this one, right? Met, you are just checking checking on this one right unable to create cases I will go and update it to here soon, at least I will have a free and the Stavrid of France. So in the meanwhile we can just say them that the dream is and the famous look on the toilet. Strolling, this one's back. is because of transcript fields. Waiting for fullness, Waiting for fullness The only thing that is pending is this one on on the Isenda thing, one. will be able to take it from here. Maybe I can ping you after an hour. and Hour once I reach home. Okay, no worries man. May I ask you a question? My time dropping, but one is here for anything you get and the other one. Thanks for your help. Bye. Thanks, Prash. So that is a Let me just double check. Sorry, what's the problem one? That would be he would be the best person to reach out to He will point you in the right direction. Oh sorry Matt, I just pasted the screen and the screenshot in the chat. In the RPpiles, it shows timezone at distance and Distance State Standard Time, but it is completely annoying. It's falling back to you guys. I mean that I would expect all of these users would Get that, but for whatever reason it's not and the database to start. and all the Glens. Check some of the other unification clients that have gone. Yeah, we will have to or leave the client one more time. was not using UTC in-net track then can we can verify those client I have shared you the piece of code, right? It is hardwired to UTC. So we have to check from which configuration it is picking. and Unity Speaking of the time. Yeah, I think with these ones My guess is when we migrated We just simply defaulted that value to utc UTC for all users and then Most likely our fix is to bulk update everything everything for all of their users. That is a temporary fix, right? But what about all other kinds? This might happen in future, right? Yeah.

## Reunión 2026-07-30 — User login issues · Transcripción 3/6
_chunk 1415 · 2026-07-30_

I'm just posting a status here on all tickets. This is going to be messy. and I'll just write that. Not sure why that wants to be a link, but it's okay. We got some starter bros. Statter Bros, I don't know. I don't know. What's Angie saying? Well first she was saying that two out of three people couldn't log in. File a ticket if you still have issues. And then I saw they filed this ticket. but this is not we can't log in this is we can't access attachment and the next one. What's his name, Russ? You guys feeling good today? Getting some work in. I've been pivoting from meeting to meeting and it's like in between everything Thank you as well. In some ways this was was somewhat expected. I mean, obviously not this We were forcing users across because there was lack of communication Why this surprises people so much when we get out. at a conference with some of our customers today. Oh yeah, no I know. It's the same morning. and Learning and G, unable to access attachments. Yes, it is. Perfect. I replied to her, are you on that email Matt? Oh you are. I look at it and then go from there. and then we'll go back to the next slide. All right, that's not our You are putting an update in the channel on the ticket summary for each ticket where we are on all of them. Top one is the non-SAML link to LPMS So I guess a little bit more detail on that one. We're waiting on the This is a link for them to log in with a username and password instead of SSL. in order to log in along with the password whereas previous Previously, they used a login ID. This was one of the things that I specifically covered with her as we were leading Once we get exactly the information, we'll walk her through how to log in and then she'll be able to the next one is the locations that are They have duplicate store numbers across divisions. and so when their hierarchy is getting assigned Brand or the division Division, which is what it's called within secure, is not coming into play.

## Reunión 2026-07-30 — User login issues · Transcripción 4/6
_chunk 1416 · 2026-07-30_

So it's actually pulling both location numbers, not just the singular one for 1 for the brand. We've got that with engineering. We're working and we're working through the fix. We'll have that shortly. Perfect. Third one, which is that one user unable to access the system. System. It is a missing claim in their SSO. and we've communicated that back to them already. The next one, which is the request and the request to remove secure incident management system from the email sender name. I don't know whether we'll actually do this. I'm going to take it up with I know right now I will not get a response from product. When we send out emails, there is now a... Yes. Display Name that is included on an email coming out from the system. and I have to recognize this name so that their users are confused. I don't think we need to do anything, but again, we will wait on product too. review that I think can make the final cut. ServerTime needs adjustment to EST. This was a time zone on the individual user. We've updated the user. All of their other users the same way. So this was just simple KT timezone instead of the correct EST. Why did that change? It is a new piece in platform. in Platform that is not in LPMM. LPMS and my I need to double check Double check exactly the root cause, but quick guess is and the other thing that we're going to do is we are defaulting that to UTC if we don't currently have it. My... So, thinking about this Do we have a place that they tell us their timezone before we did this migration? Summit login to set their time zone. That's what I would recommend. If it's at UTC UTC, force them on the next login to manually set a time zone and it could be UTC again. Yeah, so that might be a code change in order to surface that field somewhere to make it accessible. Accessible, but more to come on that one. I have not found a place to do that in the application yet.

## Reunión 2026-07-30 — User login issues · Transcripción 5/6
_chunk 1417 · 2026-07-30_

I am trying to find trying to find one, but that's going to be the code change if we have to make a code change for this. Yeah, yeah, I think for sure, for sure we need that ability. All right, next one. The issue is, however, we don't really and the other ones. that would probably be something that we would want to do. is users are unable to create cases when restricted by division. It's the exact same and the last one is the Isenda piece. It seems to be a and find out what we can do to figure that out. This was not something that we've seen come up anywhere. and the one in my opinion that might be the hardest to resolve. Okay, and so Matt just to you know because Kara asked me the question These are all the customers who have been ignoring our repeated requests over the last months to work We anticipated there would be some problems, just more than we thought. Yeah. Yeah, and I mean there's everybody would have been aware of is this everybody that has been ignoring us? This will be a continued, hopefully not like this, but we are with a goal of being done by end of September. which was something that we worked closely with. that needs to come from somebody. Direct mandate to try to get these pushed across as quickly as possible. I highly doubt that any of and other things that we can do to help them out. contracts that would cost us money. Some of these customers also have other products of ours. went with first in order to do this properly. Good. Good, good, good. Matt, don't hate me. to most people. Someone asked, how could we prepare for things like this? and that's one of the, I think, friction points we're running into as well. and to be fair, she doesn't know enough about the product to really be able to start. to start having those conversations either. Sure. Makes sense. Makes sense. makes sense, but you know no offense to anybody, either do I, and I'm out there, so. Yep.

## Reunión 2026-07-30 — User login issues · Transcripción 6/6
_chunk 1418 · 2026-07-30_

We are working on the couple tickets that are with engineering and we'll have a and we'll have updates as soon as we have something. Our goal is to push out fixes Let Tyrone know that you had a quick look at the Statterbos, just so he so he can reach out to you if he has any questions. OK. He's taking the ticket. All right, awesome. Thanks Matt. Thanks team. Thanks everyone.
