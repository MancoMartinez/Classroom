# Reuniones — Prep

Carpeta 17 de la base de Moscú. 80 fragmentos.

## Reverse Shadowing Check-In — Context & Agenda (2026-06-18)
_chunk 943 · 2026-06-18_

Meeting: Reverse Shadowing Check-In
Date: 2026-06-18, 10:00-10:15 AM (15 min)
Organizer: Juan Martínez
Attendees: David Vargas, David Lora, Sebastian Rueda, Diego Buelvas, Anubhav Jha, Viraj Kansara
Declined: Vedant Shirude

Purpose: Quick standup-style check-in on reverse shadowing progress this week.

Context:
- Team is in KT phase transitioning from shadowing (observing) to reverse shadowing (leading tickets with backup).
- Viraj coordinates weekly cadence meetings with India team.
- Documentation Tracker used to log sessions (T-001 Team & Links doc for shadowing schedules).
- KT sessions ongoing: Secure EBR (3 days completed with J.R. Teagle), Engage, LPMS.
- Claude AI being used by team for transcript summaries and ticket research. Vedant mentioned using Claude for document creation (meeting 2026-06-03).
- Key concern from prior meetings: validating AI-generated outputs before sending to clients.
- Escalation path clarity needed: when to handle vs when to escalate.
- Access requirements: Jira/ServiceNow, Secure platform (support login), Azure portal, VPN, Doc Tracker.

Agenda:
1. Opening (2 min) — context, standup format
2. Round-robin (6 min) — what shadowed, blockers, next focus
3. Deeper questions (3 min) — end-to-end ticket ownership, product confidence
4. Access & Claude (2 min) — permissions, AI tool usage
5. Close (2 min) — action items, next check-in

## Reverse Shadowing Check-In 2026-06-18 — Análisis y transcript
_chunk 951 · 2026-06-18_

## Reverse Shadowing Check-In — Análisis del equipo

**Reunión:** Reverse Shadowing Check-In
**Fecha:** 2026-06-18, 10:00 AM (20m 32s)
**Facilitador:** Juan Martínez
**Asistentes:** Viraj Kansara, Anubhav Jha, Sebastian Rueda, Gulshan Kumar, Nikita Rathore, Bikash Kumar, David Lora, David Vargas, Diego Buelvas
**Ausente:** Vedant Shirude

### Meta semanal (acordada con Camila)
1 a 2 tickets manejados por persona (liderando, no solo observando) + al menos una interacción con el cliente cuando sea posible.

### Scorecard por persona vs. meta

**Cumplen o exceden la meta:**
- **Diego Buelvas** — Más activo del equipo. 4-5 tickets (work items, white rows, broken data). Dando soluciones a Sainsbury, TJX Canada (Rhodes) y Nordstrom. Colabora con Kerry y Shumi (database engineer).
- **David Vargas** — Primer ticket resuelto end-to-end: tema de restitution (cubierto con Dean). Hizo triage, verificó configuración, revisó logs con Dean, encontró problema de SQL query, escaló a engineering (no puede debuggear en su máquina), engineering creó una función pendiente, y el cliente confirmó la resolución. Continúa con otro ticket.
- **Bikash Kumar** — 1 ticket resuelto (data clearance). Trabajando con Mohammed (Luke de licencia esta semana). Descubrió que Snowflake/Snowtime es accesible vía browser en My Apps — hallazgo útil para todo el equipo. Sesión con Mohammed mañana para acceso a workstations.

**En transición activa (con buddy, en camino a la meta):**
- **Viraj Kansara** — 1 ticket (impersonation, notificaciones, links de reportes descargados), investigando con buddy. Interacción con cliente por email en este ticket + tuvo contacto el viernes pasado. Enfoque del buddy: "encuéntralo tú mismo, Claude es tu asistente". Bloqueos de acceso, resolución estimada 1-2 semanas.
- **Sebastian Rueda** — Shadowing con Payman. Llamada larga de troubleshooting de Delhaize (transacciones + errores de descuentos), sin terminar, finalizando hoy. Payman es owner pero Sebastian co-trabaja. Tiene 1 ticket asignado a sí mismo hoy (también Delhaize).
- **Anubhav Jha** — 1 ticket (RCS-2427470) con notas internas, hallazgos y causa raíz documentados. No interactúa con cliente directamente. Segundo ticket bloqueado por falta de acceso a US workstation; levantó tickets a IT.

**Bloqueados por acceso (capacidad demostrada, no pueden ejecutar):**
- **Gulshan Kumar** — 2 tickets (con Nikita, asignados por David). Encontraron la causa raíz; tuvieron shadow session con David y aprendieron a levantar PR. Bloqueados: sin acceso a DBA, remote desktop, ni objetos dentro de recursos Azure (Key Vault).
- **Nikita Rathore** — Mismos 2 tickets que Gulshan, mismo buddy. Espera entender mejor el sistema al empezar el reverse shadowing real.

**Aún en shadowing:**
- **David Lora** — Shadowing con Bonnie en tickets APS (aplicación legacy). Mayormente infraestructura (certificados SSL, whitelisting/blacklisting de IPs). Ya obtuvo acceso a IPs. Cristina le asignará tickets propios la próxima semana (está fuera hoy y mañana). **Pregunta abierta para Camila:** ¿el equipo va a manejar estos tickets de infra o se siguen escalando al infrastructure team?

### Patrones clave

1. **El acceso es el cuello de botella, no el conocimiento.** Varios ya diagnostican y encuentran causa raíz pero no pueden ejecutar por falta de acceso a DB, remote desktop, workstations US/EU, y objetos en Azure Key Vault.
2. **Nadie lidera tickets de forma totalmente independiente todavía** salvo David Vargas (1 resuelto) y Diego (volumen alto). El resto sigue en co-trabajo con buddy.
3. **La interacción directa con cliente es mínima** — solo Viraj (email) y David Vargas (confirmación de resolución). Nadie en llamada directa.
4. **El equipo de India hace trabajo técnico real** (SQL, root cause, frontend/backend) pero completamente bloqueado por accesos.

### Decisiones tomadas
- Centralizar las solicitudes de acceso en un request grupal (Viraj consolida lista de Carlos) en lugar de pedirlos caso por caso. Resolución estimada: próxima semana.
- Para accesos urgentes individuales: levantar ticket directo a IT (Trey). Aprobaciones: equipo India → Viraj; equipo Colombia → Juan.

### Action items
- **Juan:** seguimiento a solicitudes de acceso (Azure, workstations US/EU, remote desktop).
- **Juan:** aclarar con Camila el scope de tickets APS/infra (SSL, IPs) — ¿se manejan o se escalan?
- **Anubhav:** compartir el link del jump server cheat sheet (GTC, acceso EU + US) en el canal del equipo.
- **Bikash:** documentar/compartir cómo acceder a Snowflake vía My Apps.
- **Viraj:** enviar lista consolidada de accesos para request grupal.
- **David Lora:** empezar tickets propios la próxima semana con Cristina.
- **Equipo:** seguir documentando hallazgos y causas raíz aunque falte acceso completo — es el enfoque correcto.

---

## Transcripción completa

Reverse Shadowing Check-In-20260618_100045-Grabación de la reunión
18 de junio de 2026, 3:00p.m.
20m 32s
 Juan Martinez inició la transcripción
 Anubhav Jha   0:06 I want an article for this jump server only. And it's the jump server cheat sheet, it is called.
 Viraj Kansara   0:17 Can you send me the link?
 Anubhav Jha   0:19 You are being true.
 Viraj Kansara   0:26 Okay, I got it.
 Juan Martinez   0:43 Well, I think we can start. Thanks for joining everyone. The proposal of this call is to check in on the reverse Harrowing progress for this week and make sure we are all aligning on the where things stand. Yeah. I'd like to go away by one and hear from each of you and share where Were you working on anything you need help with or any questions that came up during the week? Who, who won't start?
 Viraj Kansara   1:20 Sure, I can go ahead one. I picked up one ticket like yesterday. I'm still researching and working closely with my buddy. So I mean, I'm working on by myself and trying to reprove the issue and asking whether I can.
 Juan Martinez   1:22 Okay, English.
 Viraj Kansara   1:38 I I do have questions like you how to impersonate the user and try to see where is the notification where the reports are downloaded and if there is a lag then why it is a lag in if it is working in other version right then what version it was working and all that so basic stuff I'm working on the ticket and. It's still not resolved, but yeah, I'm closely working with my buddy to. close it out based on what my findings are. So his approach is you find it out. I want to see how much you are able to understand the system by yourself and how much you are able to research by on your own. You know, Claude is your assistant. Use that, use other resources and try to see where you can progress by yourself. But yeah, if I have questions, he does answer things. Yeah. The other thing is there are some access that doesn't help me to take any tickets. But yeah, I think we will be able to resolve those access issues maybe in one or two weeks.
 Juan Martinez   2:40 Okay, and you have some interaction with the client directly or I just review the ticket and I'm working on the.
 Viraj Kansara   2:49 The client interaction I had last week, Friday, on a couple of tickets, but again, I was not directly interacting with the client. But this ticket, I am interacting with the client on email, not over call.
 Juan Martinez   3:01 Oh, okay, okay, thanks Viraj. Let's go to Anwash.
 Anubhav Jha   3:13 Me.
 Juan Martinez   3:14 Yeah.
 Anubhav Jha   3:15 Yeah, so for last week I had calls with my buddy and we went through the secure. This week also we were doing the same. Till now I have just taken on one ticket. Ohh. That is RCS 2427470. So I am not directly interacting with the client on this, but I have posted my internal notes with the findings and the root cause that I feel could be what. is going on this ticket. And right now I'm working on another ticket with my buddy, but I don't have access to the US workstation also. So because of that, I'm not able to fully work on it. So currently I have raised tickets to the IP for that.
 Juan Martinez   4:12 Okay, okay. Yesterday I sent the ticket for our team for have access to all these places or pages that I need to kind of full of work with the tickets, but okay, okay, thanks. Sebastian.
 Sebastian Rueda   4:32 Sure.
 Juan Martinez   4:32 Go ahead.
 Sebastian Rueda   4:34 I've been working with Payman on some tickets from last week, just shadowing him. But yesterday we have a very long call when we were troubleshooting an issue for Del Hayes about the transaction and some discounts errors. We couldn't finish. We will finish today. He is owning the ticket, but we are actually working on it. And I have a ticket now assigned to myself for today, also to be reviewing, also from Del Hayes. He has some of... this client tickets like they are a lot and have not been touching in a while. So we have this urgency. I did so Viraj post on the QA that we had. I suggested to him, but he prefers the. to be working on those Del Hayes tickets. We will be reviewing today that ticket that I am owning and for that is related also to Del Hayes and an issue with a transaction.
 Juan Martinez   5:42 I.
 Sebastian Rueda   5:56 We'll be discussing that ticket in two hours.
 Juan Martinez   5:57 On. Okay, okay. Thanks, Austin. Gulshan, you turn.
 Gulshan Kumar   6:10 Yeah, so me and Nikita is working. So we have got two tickets to work on. So we started working on those tickets. So David asked us to try to find out the problem and try to find out if there is any solution that you can have or anything. So me and Nikita both tried to find those things and tried to find what exactly the reason and what exactly the cause was that was happening because of the reason, right? So we found out the reason and we also today we had the shadow session. So we also sort those things to David and yeah, we were like a bit of correct, a bit of wrong also that yeah, these changes not need to be done and all those things, right? So we find out that our front end and back end needs to be changed. So basically. At the end, David mentioned and David also sold us key. This is how you have to do this. This is how you have to raise your PR and all those things, right? So how you have to make the changes. But yeah, still we cannot do all those things ourselves because we don't have the access to DBA. We don't have access to remote desktop connection. We don't have access to like a couple of things on Azure portal. So a lot of access that we require to complete or to work on anything. But yeah, we try to find out the reason on the ticket, exactly what's happening and all. Yep.
 Juan Martinez   7:49 Well, okay, okay. Thanks, Gulshan.
 Gulshan Kumar   7:51 Yeah.
 Juan Martinez   7:53 Um, Nikita, how has it been in your end?
 Nikita Rathore   8:01 Yep, like we both were working on the same things and our buddy is same, so it's going well still now. And once we start working on the tickets, like we start reverse shadowing, then we will able to understand it more accurately now. Like how the things are, where we have to look for the issues, and and how we can like approach these solutions, so yeah. Thank you.
 Juan Martinez   8:33 Okay, thanks. Thanks, Nikita. Bikash.
 Bikash Kumar   8:41 Oh, hey, hi, Juan. So, I mean, I was working with Mohammed because Luke is on leave for this week, right? So, I mean, apart from the work, I mean, I was walking through a few of the pipelines for different times. And
 Juan Martinez   8:43 Hi, hi, Bikash.
 Bikash Kumar   9:01 Like the issue that I was having and what Mohammed told me was that I would be needing access to the US and EU workstations. So I raised a request for that, but I got a message from Trey that I must be having the access to that already. But I didn't have. Like the connection string for the, I mean the remote desktop, so he shared me a, I mean an ID for that, but I can access it right now, but I am not sure how to like access all of the detailed pages or whatever there are. So I have another session with Mohammed tomorrow. I'll look into that as well. Apart from that, I was working on, I mean, I picked one ticket. It was at that time, I mean, no one has picked that. But as of now, it stands resolved. It was regarding some, just check on it once. Yeah, so it was regarding some data clearance. Right. And I mean, I asked this to Mohammed as well. And like I was thinking, I mean, if we had an kind of an admin page from where we can remove all of the data, backlog data, or if we ran some kind of queries in the snowflake or snowtime environment, right? So what I got to know is that we have to run some queries to, I mean, data clearance from, if you want to do it from the back end. So we have to run some kind of queries. And for that also, I just got to know after I talked to Trey regarding this, that we have the access to. the snowflake or snowtime environments. We just have to, from our browser, we just have to go on to my apps and from there we can access all of those tables, whatever you have. I checked and I mean it is accessible for me. So if anyone else want to access it, I think it would be accessible for them as well.
 Juan Martinez   11:02 Okay, great. Thanks. Thanks, Bikash. Anyone have any other pending access requests for Azure or VPN or documentation tracker specifically, or some direct link that don't work for? For the shadowin, or how is cloud working for you so far? Because some people have problems with cloud.
 Gulshan Kumar   11:29 So like I have some issues, like I have access of Azure portal and also I can view those resources, but still we don't have access to the objects inside all resources, right? So like we have a keyboard, so we don't have any visibility to the resources inside that keyboard. So, yeah, a couple of access are still need to get on, so yeah, I think I have also raised to Camila also, so I don't know. I think in the once Camila will be available or then we will get all those access and everything, but yeah, and there is a lot of access that we need.
 Juan Martinez   12:11 Okay, okay, okay, then we'll chat. David.
 David Lora   12:18 Yes, for me, I've been showing my shadow Bonnie mostly into AP's tickets, which is a really old legacy application that we still will need to support. A lot of the issues that we have are mostly related to infrastructure, which is something I don't know how we're going to be handling on RAM, because what they do basically now is just escalate those tickets to the infrastructure team. And I am not sure, that's something I wanted to discuss with Camila, if we are going to be doing the same, because this is mostly related to like SSL certificates and white listing, black listing IPs for access for the customers. Other than that, I already got access to IPs. I don't know if anyone else has worked on that. It's really all a platform and we have to load some configurations. to tell you something is running on Flash. So, it's pretty real.
 Juan Martinez   13:09 Mhm.
 David Lora   13:10 In my shadow morning, that is Cristiean also will assign me a couple of tickets so I can start working on my own. I think next week because she is going to be out today and tomorrow.
 Juan Martinez   13:24 Yeah, okay. Thanks, David. Um, David Vargas.
 David Vargas   13:32 Hi, Tim. Good morning. So, I started working on a ticket yesterday. It was related to a topic we covered with Dean, which was restitution. So... I was able to troubleshoot on my own, all the to check all the triage part that the configuration were fine, which indeed were. So then Dean told me how to review some logs. There we had, we saw that it was a problem with SQL, an SQL query that was being. So we then escalated this ticket to engineering because right now I can't debug on my machine. Turns out that there was a function that was pending to be created. Engineering created a function. Today I sent a ticket to the client to review and they said it was resolved now. So, I was able to resolve my first first ticket, and yeah, I continue to check on our ticket, see if I can work on the other one.
 Juan Martinez   14:35 Okay, thanks. Um, Diego.
 Diego Buelvas   14:43 Yeah, when I've been working with three or four or five or four or five tickets about work items, white rows, data broken, and yeah, this is my job, my actual job, so I've been working with Kerry and Shumi, that is the database engineer. I don't know, I'm not pretty sure about that, but... I think it, I think it, and I'm giving some solutions to Sainsbury clients, TJX Canada with Rhodes, and I'm working right now and a ticket about Nordstrom client, so yep. I don't have any more.
 Juan Martinez   15:31 Okay, okay, thanks. Thanks, Diego. I know the access is the main blocker for several of you right now. We already submitted the request for Azure, US, and your work stations and Remote Desktop. I follow up on the status and push to get those results as soon as possible. In the meantime, and can doing what you can with what you have and investigate what you are doing, finding root causes and documenting findings. Is this the right approach even without full access? I saw the article about the PRD new jump service with the access. to the bot that you want and US, please share that link in the team channel so everyone has it. If you already have the connection in stream for Trey, try to connect and document what you can and can reach or send on DM to be or to me. And that way when we have the follow up sessions, we can troubleshoot the specific apps. Um... On the knowledge transfer side, I want to say that we complete 3 security VR session this week, covering world view, on seers, composers, profilers, all their settings, and smart tracks, the links of these videos, and it was sent in the chat. and the ApprissSupportGHSorg team. Incident and audience sessions are coming up next. So then the knowledge base is growing and ideally that should be translating into more confident, yeah, confidence when working tickets, yeah. And overall, I can see good progress on the investigative side, and the next step for everyone is to start owning tickets directly, but well, I need to... A scene and tend to yourself or document the resolution and communicate with the client is is is the goal, and you brought your backup and and and yeah, if you have more questions or or more things to say, you can send a DM to Viraj to me or send. DM to Camila tomorrow, and and that's it, and thank you all, and for those, we will come make it and please send a quick update via DM or whatever, we'll do this again next next week, again next week, Viraj.
 Viraj Kansara   18:10 Just one quick to add one. Just on the access side, I think there are multiple things that will need access. I have a rough list that Carlos sent me, but if we find that there are any other accesses that we will need, I think we will need to put them all together and send a request for the whole team. So, individually, they don't need to request it on a case-to-case basis, right?
 Juan Martinez   18:37 Okay.
 Viraj Kansara   18:38 So, access will be one of the things, because even if we have a list of 10 things, one or the other thing will miss, but if you guys think that you guys need access to any particular thing, what you can do is... I'm sending you this link. Feel free to directly raise the request with the IT team. If you need any approvals, you know, as your team lead or something, right? India guys can reach out to me or directly Colombian team to Juan. And I think the IT guys directly provide the access if you provide the... Business certification, so if you need any immediate access, just go ahead and raise the access request directly for individual things, but we are also working on getting a group access for a list of items that we have on our site, but it should be resolved within next week. Sure, and I think mostly it's a Trey. Trey, you just from the IT team. So mostly if you create a ticket, he will respond back to you on the ticket or tips.
 Juan Martinez   19:53 Okay, thanks, Viraj. And thank you all. That's it. Have a good day.
 Viraj Kansara   20:00 Thanks, everyone. Bye.
 Diego Buelvas   20:01 What are your day, guys?
 Nikita Rathore   20:01 Thank you. Bye.
 Sebastian Rueda   20:02 Thanks, have a nice day.
 Juan Martinez   20:03 Thanks.
 Anubhav Jha   20:04 Thank you.
 Juan Martinez detuvo la transcripción

## Team access request — referencia (Vedant Shirude, 2026-06-18)
_chunk 952 · 2026-06-18_

Correo de Vedant Shirude (Senior Full Stack Engineer - Contractor) solicitando acceso. To: Camila Cortes, Viraj Kansara. Cc: Juan Martinez, Tyrone Whitney. Buddy: Tyrone.

Sirve como TEMPLATE del request de acceso grupal que Viraj está consolidando para todo el equipo.

Sistemas y recursos solicitados:
- 1Password (Password Manager)
- Global Protect VPN (LA4-Gateway)
- Secure 5 Clients — Staging & Production
- 10.42.100.x Network Range
- All Secure Databases
- Azure Bastion / RDP (qa-lpms-rdp-001)

Database Access (MSSQL Prod):
- pd-lpms-uswest2-sqldb-001
- pc-lpms-canadacentral-sql-001
- pe-lpms-northeurope-sql-001

Nota: este set de accesos es el que el equipo necesita para desbloquearse en tickets de Secure/LPMS. El acceso a Bastion (qa-lpms-rdp-001) ya tiene ticket propio aprobado por Infosec (ver memoria appriss_lpms_logs_bastion_access).

## Guion Reunión J.R. Teagle — Overview, problema, arco y pedido
_chunk 1320 · 2026-07-21_

Reunión 2026-07-21 con J.R. Teagle (VP Global Support, dept 421). Presenta: Juan Martínez, Lead Support Engineer (nuaav, bajo Camila Cortes). Objetivo real: que J.R. vea las dos herramientas ya corregidas, entienda el problema que resuelven, y salga con una decisión concreta (piloto + un SME que valide contenido).

EL PROBLEMA: El equipo de soporte está en reconstrucción y el conocimiento se va con las personas. Kristin Krogman sale 31-jul; Aimee Wadsworth de salida (~2 meses); Smeet ya salió. El SharePoint de Kristin (kkrogman_trebu_co) muere cuando se va. El onboarding oficial son 2-3 semanas leyendo una KB de Confluence de 1.454 páginas (auditoría 477390143498). El conocimiento operativo es tribal. Encuadre para VP: esto es mitigación de riesgo de continuidad y reducción de tiempo a productividad, no "hacer documentación".

DOS HERRAMIENTAS COMPLEMENTARIAS: (1) moscu-ops = el MAPA de toda la operación (referencia, para quien ya trabaja aquí). (2) Onboarding Appriss = la RUTA de 6 días que reemplaza las 2-3 semanas del onboarding oficial (rampa para quien llega el día uno). Mismo conocimiento debajo, dos puertas de entrada.

EL ARCO (una línea): Problema (el conocimiento se va con la gente) → Ya escuché tu feedback (moscu-ops corregido) → Y fui más allá (ruta de onboarding de 6 días) → Así se mantiene y encaja (vive en Moscú, consultable) → Esto es lo que te pido (piloto + un SME).

EL PEDIDO (nunca cerrar sin pedido concreto, pasos de bajo riesgo): (1) Un piloto con el próximo ingreso, midiendo días hasta productividad vs. 2-3 semanas actuales. (2) Un SME de Support que valide el wording operativo (J.R. mencionó a Matt E la vez pasada) — un par de horas. (3) Una decisión de adopción si el piloto funciona. Frase: "No te pido que lo bendigas oficial hoy; te pido dos cosas pequeñas: correrlo con la próxima persona que entre, y un SME que valide el wording. Si la rampa pasa de tres semanas a una, los dos sabremos que vale la pena volverlo oficial." Cero costo, cero PII, offline.

## Triage backlog sin asignar 2026-08-03 — 37 tickets en 11 patrones + reparto
_chunk 1444 · 2026-08-03 · fuente: ~/Downloads/TRIAGE-BACKLOG-2026-08-03.md_

# Triage del backlog sin asignar
Primer pase agrupado, autorizado por J.R. el sábado · Juan Martinez · 3 ago 2026

---

# El titular

**37 tickets sin asignar hoy.** Ninguno es High. Ninguno es Critical. 34 Medium, 1 Low, 5 sin prioridad puesta.

Eso es lo primero que hay que decir en la reunión, porque cambia la estrategia: esto es **volumen, no severidad**. Y por eso agrupar funciona.

**La aritmética de la reunión.** Al ritmo de 5 minutos por ticket que planteó J.R., 37 tickets son **3 horas y 5 minutos**. Imposible en una hora. Agrupados quedan **11 grupos**, y 11 por 5 minutos son **55 minutos**. Entra justo. Esa es la razón por la que el primer pase valía la pena y por la que J.R. lo aprobó.

## El dato que nadie ha dicho todavía

| Producto | Tickets sin asignar |
|---|---|
| Secure 5 - EBR | **24** |
| Incident (f.k.a. LPMS) | 8 |
| Otros (Audit, Legacy Apis, Engage, Secure 3/4) | 5 |

**El backlog no es la unificación.** La unificación es Incident. Este backlog es Secure 5 en un 65%. Por eso se estancó: todo el mundo lleva dos semanas metido en Incident y en la ola del 27 de julio, y la cola de Secure 5 se fue acumulando sin que nadie la mirara.

Consecuencia práctica: **la gente quemada en unificación no es la que tiene que vaciar esta cola.** Los perfiles de datos del equipo, que es donde vive Secure 5, casi no han tocado unificación.

---

# El equipo real

Tomado de la pestaña Miembros de **Support Appriss** en Teams, no deducido de Jira.

| Persona | Puesto | Grupo | Abiertos | Nota |
|---|---|---|---|---|
| Vedant Shirude | Senior Full Stack Engineer | India | **21** | Recibió los cuatro de Tyrone. **Fuera del reparto** |
| Juan Martinez | Lead Support Engineer | Colombia | **14** | |
| **Sebastian Rueda** | Senior Data Engineer | Colombia | **13** 🔴 | **1 Critical + 1 High.** Y dos tickets de 137 y 101 días. **Fuera del reparto** |
| Bikash Kumar | Data Engineer | India | **10** | |
| Nikita Rathore | Full Stack Engineer | India | **9** | |
| Edwin Garzon | Data Engineer | Colombia | **9** | |
| David Vargas | Full Stack Engineer | Colombia | **8** | Pero **6 en Under Customer Review**, carga activa real 2 |
| Diego Buelvas | Full Stack Engineer | Colombia | **7** | Tres High |
| Gulshan Kumar | DevOps / SRE | India | **5** | 4 en Work in progress |
| **Luis Hernandez** | Senior Full Stack Engineer | Colombia | **0** ✅ | **El primer nombre por la regla de J.R.** |
| Camila Cortes | Support Manager | Colombia | propietaria | Comunicación con cliente |
| Viraj Kansara | Lead Data Engineer | India | el otro lead | Par tuyo, no subordinado |

**Los dos datos que mandan en el reparto de hoy:**

**Luis Hernandez está en cero.** J.R. dijo textual *"start assigning in order one to each person, starting with the person who has the lowest amount of tickets"*. Ese es Luis, y se lleva el bloque más grande.

**Sebastian Rueda es el segundo más cargado y no lo puede recibir.** 13 abiertos, con el Critical de Santikos y el High de refunds de Ahold. Lo único que se le acerca hoy es una consolidación, no trabajo nuevo.

## Los números crudos engañan en dos casos

**David Vargas, 8 pero 6 esperando al cliente.** Está esperando, no trabajando. Carga activa 2. Puede recibir.

**El problema de antigüedad no está en esta cola.** El ticket sin asignar más viejo tiene 82 días. Sebastian tiene **RCS-26088 con 137 días** y **RCS-26632 con 101**, los dos de duplicación de datos. Los tickets realmente viejos ya tienen dueño y nadie los mira. Vale decirlo en la reunión, porque el ejercicio de hoy no los toca y son peores que todo lo que vamos a repartir.

## Cruce urgente que no puede esperar a la reunión

**RCS-28106**, "Santikos SmartAlerts Not working", **Critical**, de Sebastian desde el 31 de julio.

En el análisis del RCS-28112 el viernes, de los 255 errores HTTP 500 del app service de nettrack, **248 estaban en `POST /nettrack/api/internal/SendSmartAlert.aspx`**. Es el mismo endpoint.

Su Critical de Santikos y la degradación de Stater Bros están mirando lo mismo desde dos lados. Habla con Sebastian hoy y linkea 28106 con 28112 y 28114.

## Antes de repartir: dos tickets huérfanos que no están en la cola

No aparecen como "sin asignar" porque tienen nombre, pero el nombre está desactivado.

| Ticket | Cliente | Prioridad | Edad | Detalle |
|---|---|---|---|---|
| **RCS-27549** | ICA SE | **High** | **39 días** | "Degraded system performance". El cliente pidió RCA formal. Asignado a **Carlos Jacinto, cuenta desactivada** |
| RCS-27762 | SSP Group | Medium | 24 días | Secure 3 usando MDS completo en vez de MDS Lite. Misma cuenta desactivada |

**El 27549 es el ticket más grave de todo este ejercicio** y no está en la lista que J.R. mandó. Es el único High, es el más viejo con síntoma activo, y lleva 39 días en una cuenta que ya no existe. Ábrele la reunión con esto si quieres que la sala entienda por qué el proceso falló.

---

# Los 11 grupos

## G1 · Chemist Warehouse, handover de hypercare (5 tickets)

| Ticket | Edad | Asunto |
|---|---|---|
| **RCS-28098** | **82 días** | Códigos de ítem vuelven a PLU en items anulados en vez de MyChem/MyMID |
| RCS-28096 | 18 días | Si los datos de recibo reimpreso se están recibiendo y mapeando |
| RCS-28100 | 18 días | Si los datos de apertura de caja se están recibiendo |
| RCS-28097 | 6 días | Hueco de transacciones anuladas del 29 jun al 15 jul |
| RCS-28099 | 5 días | Lógica de descuento por ítem, más compleja de lo esperado |

**Los cinco son iguales por dentro.** Reporter interno (James McKenna), label `clientproject`, título "CWH - HYP to RCS", prioridad **sin poner**, y todos son preguntas de descubrimiento de datos, no incidentes de un usuario bloqueado.

El 28099 lo dice textual: *"plan is to let this be the way it is, continue with hypercare and CW can add this as a ticket in RCS for us to check once CW updates the issue."* O sea, ese ni se trabaja todavía.

**El 28098 es el ticket más viejo de toda la cola, 82 días.** Es el que va a salir en cualquier reporte de aging y va a hacer ver mal al equipo, aunque no sea un cliente esperando.

> **Decisión que hay que sacarle a J.R.:** ¿estos 5 entran al reparto del equipo de soporte o vuelven al equipo de proyecto de Chemist Warehouse? Son 5 de 37. Si vuelven, la cola baja a 32 antes de repartir nada.
>
> Si se quedan: **un solo dueño para los cinco**, no repartidos. Propuesta **Bikash Kumar**, Data Engineer. **No Sebastian Rueda**, que está en 13 con un Critical y ya arrastra cuatro tickets de duplicación de datos. Y ponerles prioridad, porque `Undefined` no aparece en ningún filtro de nadie.

## G2 · Resolución de rol y jerarquía de ubicación (6 tickets)

**El patrón técnico más grande del backlog.**

| Ticket | Cliente | Edad | Síntoma |
|---|---|---|---|
| RCS-28031 | Genuine Parts | 5 días | "Region" de Location Hierarchy no funciona en New Work Items |
| RCS-28054 | Genuine Parts | 4 días | RAPMs configurados por área, varios solo ven New York |
| RCS-28070 | DHL | 4 días | OM no puede editar audit aunque el security setting está activo |
| RCS-28085 | Ollie's | 3 días | RLPM resuelto como DLPM, pierde aprobación de casos |
| RCS-28118 | Myer | hoy | Usuario sin el tile de transferir a Incident, permisos se ven bien |
| RCS-28122 | Blain's | hoy | "With the change we are not able to get to the user fields" |

**Ya asignados, misma familia:** RCS-27857 (Wild Fork, jerarquía en una tienda pero ve todas, **Diego, desde el 16 de julio**) y RCS-28093 (Ahold, empleados no restringidos por tienda, Edwin). Y desde hoy también **RCS-28033** (Big Y, Add Person falla solo a algunos usuarios, tuyo).

Tres cosas que ahorran trabajo:

1. **28031 y 28054 son el mismo problema en el mismo cliente.** El 28054 dice *"when Jim made that change"* y Jim Gould es el reporter del 28031. Se linkean y uno de los dos probablemente se cierra como duplicado.
2. **28122 ya tiene respuesta.** "No podemos llegar a los campos de usuario tras el cambio" es exactamente la pregunta de RCS-28080 (Stater Bros, cerrado) y RCS-28094 (Vallarta), ya contestada con un video. Es cierre de 10 minutos, no investigación.
3. **Regla de Kiran que aplica a todo el grupo:** la vista `incident.lpuser` es lo que maneja la app. `secure.LocationHierarchyUserAssignments` es destino de migración, no la capa que decide permisos. Para síntoma funcional, la vista primero.

**Propuesta: Diego Buelvas** para 28031, 28054 y 28070. Ya lleva el 27857 que es el mismo bug en otro cliente, así que es una investigación, no tres. Los otros tres salen a otros dueños por relación con el cliente, ver G9 y G11.

## G3 · Adjuntos y subida de archivos (3 tickets)

| Ticket | Cliente | Edad | Síntoma |
|---|---|---|---|
| RCS-28000 | Luxottica | 6 días | Factura adjunta desapareció de la sección vendor payment |
| RCS-28101 | Costco | 3 días | "Web Server Returned Unexpected Response" al adjuntar archivo |
| RCS-28124 | ADUSA | hoy | jpeg sí se ve, PDF y MOV no |

**Ya asignados, misma familia:** RCS-28022 (Santikos, `ShowAttachments.aspx` 404, **Juan**), RCS-28058 (Stater Bros, Vedant), RCS-28067 (Vallarta), RCS-28027 (VSM, regla de seguridad bloqueando zips con exe, Diego, ya cerrado).

Tres mecanismos distintos que no hay que fusionar:
- **archivo ausente en el deployment** (28022)
- **regla de seguridad por tipo de archivo** al subir (28101, y el 28027 ya cerrado)
- **filtro de extensiones al leer** (28124)

Pero **la petición a Matt es una sola** y cubre a los tres: revisar el filesystem del app service compartido de nettrack para `/nettrack/lpms/`, y de paso decir cuál es la lista de extensiones permitidas y el límite de tamaño. Una acción, cuatro tickets.

**Propuesta: Juan** para 28000 y 28101, porque ya llevas el 28022 y la conversación con Matt. El 28124 va con el bloque de ADUSA, ver G9.

## G4 · Conteos e items en búsquedas de Secure 5 (4 tickets)

| Ticket | Cliente | Edad | Síntoma |
|---|---|---|---|
| RCS-28026 | TJX EU | 5 días | Smart track del receipt viewer da 16 txns, el quick link da 31. El cliente sospecha duplicación por filas |
| RCS-28049 | Smyths | 4 días | Búsqueda de Manual Discount duplicando filas, antes no lo hacía |
| RCS-28055 | Genuine Parts | 4 días | Devolución muestra 1 ítem, en TAMS son 4 partes |
| RCS-28117 | Alshaya | 1 día | EC Count 1 y Amount 0.25 en la búsqueda, en el recibo son 3 y 1.85 |

**28026 y 28049 son la misma hipótesis:** fan out de un join a nivel de ítem que multiplica filas cuando hay condición de item level. El 28026 lo dice el cliente solo: *"I wonder if the reason is because its duplicating over several rows."* El 28049 dice *"it does have an Item Level condition"*. Dos clientes distintos, mismo mecanismo probable.

**28055 y 28117 son el espejo:** en vez de duplicar, subcuentan. 1 ítem cuando son 4, EC count 1 cuando son 3.

Duplicar y subcontar en el mismo agregado suelen ser el mismo bug visto desde los dos lados. Vale investigarlos juntos aunque terminen separándose.

**Propuesta: Luis Hernandez** para 28026, 28049 y 28055, porque está en cero y es el primer nombre por la regla de J.R.

**El 28117 va a Sebastian Rueda como consolidación, no como trabajo nuevo.** Él ya lleva **RCS-27951**, "Alshaya - Error Correct Count not captured". El 28117 es "Alshaya - Error correct count and amount incorrect". Mismo cliente, mismo síntoma, muy probablemente duplicado. Se linkea y se cierra uno.

**Y hay contexto que Luis debe leer antes de arrancar:** Sebastian tiene **RCS-27910**, "Alshaya - SHR Report Duplicate lines", que es la misma duplicación de filas de 28026 y 28049 en otro cliente. Linkear los tres ahorra la mitad del trabajo.

## G5 · Datos de item ausentes o retención (3 tickets)

| Ticket | Cliente | Edad | Síntoma |
|---|---|---|---|
| **RCS-27546** | Loblaw / SDM | **40 días** | Campos de ítem en blanco para códigos abiertos de prescripción. Lo abrió la SE Kristen Dyer a nombre del cliente |
| RCS-27846 | 7-Eleven | 19 días | Money order search sin transacciones. Solo trae screenshots, sin texto |
| RCS-28104 | Safeway | 3 días | Búsqueda trae 2023, 2024 y 2025 cuando solo hay 90 días de histórico |

El 27546 es el segundo más viejo de la cola y **lo abrió un SE nuestro, no el cliente**, o sea hay alguien interno esperando también.

El 28104 es el interesante: si solo hay 90 días de retención y la búsqueda devuelve 2023, o la retención no se aplica o los datos viejos no se borraron. Cualquiera de las dos es un hallazgo que aplica a más clientes.

**Propuesta: Edwin Garzon** para los tres. Es trabajo de datos puro, es su perfil, y ya lleva siete de Secure 5.

## G6 · Rendimiento (1 en cola + 1 huérfano)

| Ticket | Cliente | Edad | Estado |
|---|---|---|---|
| **RCS-27549** | ICA SE | **39 días** | **High**, huérfano en cuenta desactivada |
| RCS-27994 | ICA SE | 6 días | Sin asignar. "Slow to get results when loading receipts, and when loading store number adding a work item" |

**Mismo cliente, mismo síntoma, uno huérfano y uno sin dueño.** El cliente reportó lentitud el 25 de junio, pidió RCA, no pasó nada, y volvió a reportarla el 28 de julio con capturas. Desde su lado esto es un mes y medio de silencio.

**Propuesta: Gulshan Kumar.** Es el único **DevOps / SRE** del equipo y esto es exactamente un RCA de rendimiento, no un bug funcional. Está en 5 abiertos, así que tiene espacio. Los dos tickets al mismo dueño y linkeados.

Si Gulshan no puede, esto **no** entra en rotación por carga, sube a Engineering hoy mismo. Es el único High del ejercicio y trae petición formal de RCA.

## G7 · Dashboards y comportamiento de UI (2 tickets)

| Ticket | Cliente | Edad | Síntoma |
|---|---|---|---|
| RCS-28068 | lululemon | 4 días | Engage Analytics, Top 10 SKUs y Top 10 Consumers vacíos. Probó cambiando rangos de fecha |
| RCS-28060 | Starbucks NA | 4 días | Open investigations muestra todas aunque el toggle "show all" esté apagado |

**El 28068 es el mismo síntoma que RCS-27991, que ya es tuyo** ("Engage Analytics Not Populating Sections", High, desde el 27 de julio). El tuyo es interno, el de lululemon es un cliente esperando. Es el único ticket de la cola que cae directo sobre algo que ya tienes abierto.

**Propuesta: Juan** toma el 28068 y lo linkea al 27991. El **28060** es comportamiento de toggle, va con David Vargas en G11.

## G8 · Feeds, archivos y confirmaciones (4 tickets)

| Ticket | Cliente | Edad | Qué es | Esfuerzo |
|---|---|---|---|---|
| RCS-28012 | interno C175_GEU | 6 días | 13 archivos raw_pos_log con error CDATA. Ya investigado en RCS-27225, ~650 ocurrencias en dos meses | Medio |
| RCS-28087 | Academy | 3 días | Empleados en el feed de HR pero no en APIS. 4 números de empleado dados | Medio |
| RCS-28121 | ICA SE | hoy | Confirmación de flujos de datos existentes | **Bajo** |
| RCS-28126 | Kinney Drug | hoy | Avisan que desde el viernes 8/7 dejan de mandar el archivo EmpHours | **Muy bajo** |

**El 28126 no es un problema, es un aviso con fecha.** El cliente está siendo cortés avisando que un archivo va a dejar de llegar el 7 de agosto para que no lo reportemos como faltante. Necesita un acuse y un aviso a monitoreo, nada más. Si nadie lo lee, el viernes generamos una alerta falsa.

El 28012 tiene precedente documentado (RCS-27225, donde ya se ajustó el SnowTime Data Loader para datos malformados), así que arranca con la mitad del camino hecho.

**Propuesta: Bikash Kumar.** Data Engineer, y los cuatro son feeds y archivos. Está en 10 abiertos, así que cuatro es carga razonable si dos de ellos se cierran hoy mismo.

## G9 · ADUSA / Ahold, la ola de hoy (3 tickets)

| Ticket | Edad | Síntoma |
|---|---|---|
| RCS-28123 | hoy | "Assigned to can't be blank" al asignar caso. Muestra asignado en el caso pero no al individuo en la búsqueda. Y llegan varios correos de "you have been assigned case" |
| RCS-28124 | hoy | PDF y MOV no visibles en adjuntos, jpeg sí |
| RCS-28125 | hoy | Datos de prueba de EBT para Delhaize en Zeus 3.5 y Secure 5.4. Relacionado con RCS-27990 |

**Los tres entraron hoy y dos son de Leigh Ann Stubbs**, que ya es la reportera de tus RCS-28023 y RCS-28030. **Es una sola persona con cuatro tickets abiertos con nosotros.** Si los repartimos entre cuatro dueños distintos va a recibir cuatro conversaciones desconectadas, y ella es la voz de ADUSA en la migración.

El 28123 vale mirarlo bien: "asignado en el caso pero no al individuo" más correos duplicados de asignación huele a la misma resolución de usuario del G2, no a un bug de UI.

El 28125 es distinto, es Secure 3/4, es carga de datos de prueba, y ya tiene ticket padre (RCS-27990). Es tarea de datos programada, no un incidente.

**Propuesta: Luis Hernandez** para 28123 y 28124, que son los dos de Leigh Ann y los dos de aplicación. **Edwin Garzon** para el 28125, que es carga de datos.

Y un dato de continuidad: **David Vargas ya lleva el RCS-28053 de Leigh Ann**, el del link non-SAML. Si Luis toma estos dos, los dos tienen que hablarse, porque ella tendría tres tickets abiertos con dos ingenieros distintos.

## G10 · No se pueden trabajar como están (2 tickets)

| Ticket | Cliente | Edad | Problema |
|---|---|---|---|
| **RCS-27753** | PVH Corp | **25 días** | Descripción **completamente vacía**. Título: "Incident report are complete when I click save". Problem = Performance Degradation |
| RCS-28108 | Alo Yoga | 3 días | Descripción **completamente vacía**. Título: "Cameras failing to load. Order #41213355" |

Mismo defecto estructural que el RCS-28044 del viernes. **Nadie puede trabajar esto**, y el 27753 lleva 25 días en los que el cliente cree que estamos investigando algo que no sabemos qué es.

No es trabajo técnico, es una llamada de vuelta al reporter. Es lo más rápido de todo el ejercicio y lo que más mejora la percepción, porque el cliente descubre que sí leímos su ticket.

**Propuesta: Camila Cortes.** Es la manager del equipo y ya hace este seguimiento (lo hizo en el 27840 de Kohl's el 23 de julio). Son dos mensajes, no dos investigaciones. Que salgan hoy los dos.

## G11 · Sueltos con dueño claro (6 tickets)

| Ticket | Cliente | Edad | Nota | Propuesta |
|---|---|---|---|---|
| **RCS-28018** | Ollie's | 5 días | "Secure 5 multiple issues", **cuatro problemas en uno**: Receipted Flag y Cash Back Flag dando resultados inexactos, link de Emp Sale ID roto, filter groups desaparecidos de la librería. **Misma reportera que el 28085** | David Vargas |
| **RCS-28085** | Ollie's | 3 días | El que J.R. pidió priorizar. Ver informe | David Vargas |
| RCS-28060 | Starbucks NA | 4 días | Toggle de open investigations ignorado | Luis Hernandez |
| RCS-28103 | Hot Topic | 3 días | Restitución no se envía, no encuentra SETUP en Admin settings, tuvo que quitar a Zelman del provider para ver la lista | Nikita Rathore |
| RCS-28127 | Wegmans | hoy | 674 registros en blanco a borrar por batch delete. **Trae dos precedentes: RCS-18639 y RCS-18926** | Nikita Rathore |
| RCS-28122 | Blain's | hoy | Campos de usuario, ya tiene respuesta conocida | **David Vargas**, es la misma pregunta que su RCS-28094 de Vallarta |
| RCS-27664 | Sainsbury's | 31 días | Estadísticas de uso del reporte TLP. Es pregunta de datos de uso, no incidente | Bikash Kumar |
| RCS-27967 | Target AUS | 10 días | Añadir "Investigation Completed" como Reason for completing. **Ya está en Waiting for Software Release**, el trabajo está encolado | Camila Cortes, solo comunicar |

**Los dos de Ollie's van juntos.** Charity Mackey tiene dos tickets abiertos, ninguno con dueño, y uno de ellos dice que sus filtros guardados desaparecieron. Si atendemos solo el que J.R. señaló, la percepción del cliente no mejora. Son productos distintos, Incident y Secure 5, pero es una sola relación.

**El 28127 es el cierre más rápido de la cola:** tarea de runbook con dos tickets de precedente ya documentados.

**El 27967 no necesita trabajo, necesita un mensaje.** Ya está esperando release.

---

# Propuesta de reparto

Excluye a Vedant (21 abiertos). Reparte por perfil primero y por carga después, que es lo que J.R. pidió al revés, pero en esta cola el perfil manda porque el 65% es Secure 5.

| Persona | Tickets | Nuevos | Queda en | Por qué |
|---|---|---|---|---|
| **Luis Hernandez** | 28123, 28124, 28026, 28049, 28055, 28060 | **6** | 6 | Está en **cero**, es el primer nombre por la regla de J.R. Senior Full Stack. Se lleva los dos de Leigh Ann y el bloque de agregados de Secure 5 |
| **Edwin Garzon** | 27546, 27846, 28104, 28125 | 4 | 13 | Datos puros, ya lleva siete de Secure 5 |
| **Bikash Kumar** | 28012, 28087, 28121, 27664 | 4 | 14 | Data Engineer, feeds y archivos. Dos cierran hoy |
| **Camila Cortes** | 27753, 28108, 27967, 28126 | 4 | | Contacto al reporter y comunicación de estado. Los cuatro son mensajes, no investigación |
| **David Vargas** | 28085, 28018, 28122 | 3 | 11 | Carga activa real 2. El 28122 es la misma pregunta que su 28094 de Vallarta, cierre rápido. Ollie's completo bajo un dueño |
| **Diego Buelvas** | 28031, 28054, 28070 | 3 | 10 | Ya lleva el 27857, mismo bug de jerarquía. Una investigación, no tres |
| **Nikita Rathore** | 28103, 28127, 28118 | 3 | 12 | Incident y permisos, y uno con respuesta conocida |
| **Gulshan Kumar** | 27549, 27994, 28101 | 3 | 8 | DevOps / SRE. Los dos de ICA son un RCA de rendimiento y el 28101 es respuesta del servidor al subir archivo |
| **Juan Martinez** | 28068, 28000 | 2 | 16 | Caen sobre familias que ya llevas, Engage Analytics y adjuntos |
| **Sebastian Rueda** | 28117 | **1** | 13 | **No es trabajo nuevo, es consolidación.** El 28117 de Alshaya es "Error correct count and amount incorrect" y él ya lleva **RCS-27951**, "Alshaya - Error Correct Count not captured". Mismo cliente, mismo síntoma. Muy probablemente duplicado. Se linkea y se cierra uno |
| **Vedant Shirude** | ninguno | 0 | 21 | Excluido, el más cargado |

**Suma: 33 repartidos**, más el 27549 huérfano que no estaba en la lista de J.R.

Quedan **5 de Chemist Warehouse** esperando la decisión. **Si se quedan van a Bikash Kumar, no a Sebastian.** Sebastian está en 13 con un Critical, y además ya arrastra cuatro tickets de duplicación de datos, tres de ellos de 13, 55 y 101 días. Cargarle cinco más de descubrimiento de datos es hundirlo.

## Lo que hay que proteger, no repartir

**Sebastian Rueda no recibe nada.** Tiene el Critical de Santikos (28106), el High de refunds de Ahold (28077) y dos tickets de 137 y 101 días. Lo que necesita es lo contrario del reparto: que alguien le saque los dos viejos o los cierre. Vale plantearlo en la reunión como el otro lado del ejercicio.

**Y su Critical toca lo tuyo.** Ver el cruce del `SendSmartAlert.aspx` más arriba.

---

# Los 6 cierres rápidos

Si la reunión se alarga y hay que mostrar movimiento hoy mismo:

| Ticket | Por qué es rápido |
|---|---|
| **RCS-27840** (tuyo, Kohl's) | El trabajo está hecho desde el 30 de julio. Solo falta el comentario y cerrar |
| **RCS-28122** (Blain's) | Misma pregunta del 28080 y el 28094, ya contestada con video |
| **RCS-28126** (Kinney) | Es un aviso. Acuse y notificar a monitoreo |
| **RCS-27967** (Target AUS) | Ya está en Waiting for Software Release. Solo comunicar |
| **RCS-28127** (Wegmans) | Runbook con dos precedentes documentados |
| **RCS-28031 + RCS-28054** (GPC) | Probablemente duplicados entre sí. Se linkean y uno se cierra |

---

# Guion de la reunión, 55 minutos

**Minuto 0 a 5. El marco.**
37 sin asignar, ninguno High ni Critical, 65% Secure 5 y no unificación. Peyman bajó de 40 a 26 el sábado pero entraron 9 nuevos, así que el trabajo del sábado sí sirvió. Y el que de verdad importa no está en la lista: RCS-27549, High de ICA, 39 días, en una cuenta desactivada.

**Minuto 5 a 45. Los 11 grupos.**
Un grupo a la vez, no un ticket a la vez. Por cada grupo: qué tienen en común, quién ya lleva algo parecido, voluntario y si no hay voluntario, la propuesta de la tabla. Cuatro minutos por grupo.

**Minuto 45 a 50. Las decisiones que no son tuyas.**
Chemist Warehouse (¿los 5 vuelven al proyecto?), el High de ICA (¿Gulshan o Engineering?), el 27951 repartido a Sebastian Rueda y a Vlad al mismo tiempo, el label correcto para Incident, y **qué se hace con los dos tickets de Sebastian de 137 y 101 días**, que son más viejos que todo lo que estamos repartiendo.

**Minuto 50 a 55. El compromiso.**
Comentario público hoy en cada ticket nuevo. 30 minutos por ticket repartidos en el día, tope de 30, como pidió J.R. Los seis cierres rápidos primero, para que la cola se mueva de verdad hoy y no solo cambie de nombre.

## Lo que hay que decir aunque incomode

Repartir no es resolver. El viernes Chris Rippingale hizo una pasada de comentarios y **14 de unos 20 eran pedidos de seguimiento al cliente**, no hallazgos técnicos. Este backlog no está atascado porque el diagnóstico sea difícil, está atascado porque **nadie está hablando con los clientes**.

La prueba está dentro de esta misma cola: el RCS-27753 de PVH lleva 25 días con la descripción vacía. El 27840 de Kohl's llevaba 6 días resuelto sin que se le dijera. El 27967 de Target ya está esperando release y el cliente no lo sabe.

Si el compromiso de hoy es "comentario público en cada ticket nuevo", eso es lo que va a mover la aguja, más que las 30 horas de investigación repartidas. Vale decirlo así: **el entregable de hoy son 37 clientes que sepan que alguien tiene su ticket**, y el trabajo técnico viene después.

## Prep 2026-06-17 · L2/L3 Support sync + Technology All Hands
_chunk 917 · 2026-06-16_

Dos reuniones el mié 17/06/2026 (en inglés), de naturaleza OPUESTA. J.R. Teagle (VP Global Support) en ambas.
TU VENTAJA: llegas con la radiografía del backlog, el proceso Tiger Team y tus notas de causas raíz. Pero estás en INDUCCIÓN: aportas CRITERIO y CURIOSIDAD, no te ofreces a 'tomar' procesos todavía.

REGLA CLAVE: sync (9:30)=TRABAJO -> participas. All Hands (10:00)=BROADCAST -> escuchas.

PRINCIPIO DEL APORTE: el aporte va PEGADO a la pregunta — es una observación que muestra que pensaste el tema, NO un ofrecimiento de trabajo ni ponerse de ayuda directa en inducción.

=== 1) L2/L3 SUPPORT TEAM SYNC (9:30-10:00, organiza J.R. Teagle, primera de la serie). ACEPTAR la invitación. ===
PREGUNTAS (EN para decir / ES para pensar), con su aporte pegado cuando aplica:
 [Abrir] "Since this is our first sync, what outcome do we want each week — live triage, blockers, or L2<->L3 coordination?"
 [Rol] "As I step into the L3 lead role, what would success look like in my first 90 days?"
 [Rol] "Where's the biggest gap today you'd want this role to close first?"
 [Backlog] "Looking at the open queues, I noticed a tail of 60-day-plus tickets and several not updated in weeks — is that a current focus?"
   + aporte: "From what I saw, the buildup looks more on the older tickets than on intake — so the entry side seems healthy. Is that how the team sees it?"
 [Backlog] "Do we track the aging-backlog trend week over week, or mainly the current count?"
   + aporte: "I ask because the trend would show whether we're gaining or losing ground — more actionable than a snapshot."
 [Proceso] "Who drives the Tiger Team / 60-day cleanup today?"
   + aporte: "I came across the process doc and wanted to understand how it works in practice — it looks like the main lever against the aging tail."
 [Proceso] "When we escalate to Engineering or DataOps, is there a standard for what the ticket must include?"
   + aporte: "I've noticed the cases that resolve fastest tend to have the root cause framed up front — curious if there's already a template."
 [Backlog/SLA] "How do we weigh priority when a Medium ticket sits on a White Glove account?"
   + aporte: "I saw a fair number of open premium-account tickets, so I'm curious how service level factors into day-to-day prioritization."
 [Proceso] "What metrics do we report up — first-response SLA, aging, stale? Is there a dashboard?"
 [Conocimiento] "Is there a shared place where we capture the root causes of recurring issues?"
   + aporte (alinear, no duplicar): "I've been keeping my own notes on a few I dug into — I'd rather align with a team practice than duplicate it."
 [Gente] "Who are the go-to people for Data (pyARDM/DataOps) and the CSM side?"
DO: pregunta + aporta criterio (observación pegada) + escucha. DON'T: ofrecerte a 'tomar' procesos en la primera reunión; sonar crítico.
1:1 (cuando ya tengas contexto/confianza): dueño Tiger Team; estándar de escalado (T-006); reparto L2 vs L3; dashboards; ALINEAR tus notas de causas raíz con la práctica del equipo (no imponerlas).

=== 2) TECHNOLOGY ALL HANDS (10:00-11:30, host J.R. Teagle, invita Chris Rippingale, 46) ===
Modo ESCUCHA. Captura en Moscú. Anotar: prioridades de tecnología; roadmap (Pendo); cambios de org/nombres; Support/Data/RCS/Secure/Engage; lenguaje del liderazgo.
Si hay Q&A, 1 pregunta de altitud: "How does the L2/L3 Support team fit into the technology priorities mentioned?" o "Is there a direction on using our KB / AI to cut repeat support work?"
NO preguntar por ticket/cliente/proceso concreto. Después: pasar notas a Moscú, cruzar con RCS, 1-2 follow-ups para 1:1.

## Guion J.R. — Cómo sonar humano y seguro (no a robot / no a AI)
_chunk 1321 · 2026-07-21_

Cinco principios de tono (lo más importante del guion; el contenido ya lo tiene, lo que juega en contra es el tono):

1. EMPEZAR POR EL PROBLEMA que él vive, no por la herramienta. Un VP se emociona con "resolví un riesgo tuyo" (fuga de conocimiento por salida de Kristin/Aimee), no con una SPA bonita.

2. RECONOCER LOS ERRORES ANTES de que él los mencione — es la carta más fuerte. J.R. corrigió 2 cosas reales el 9-jul; nombrarlas tú primero te posiciona como quien ejecuta feedback, no quien se defiende. "You caught two real errors last time, and you were right on both. Let me show you what changed, because it changed the model, not just the wording."

3. MOSTRAR LAS COSTURAS. Honestidad calibrada > brillo. Decir qué está sólido, qué falta validar (SME), y el riesgo real (bus factor: hoy solo Juan lo mantiene). Un VP confía más en quien le señala el riesgo.

4. PRIMERA PERSONA DE JUICIO, no de tarea. Robot: "Se implementaron 6 módulos con quiz." Humano: "Decidí partirlo en 6 días porque nadie retiene 1.454 páginas, y le puse quiz porque quería que pruebe que entendió, no que solo lea." Usar "yo decidí / noté / me equivoqué en / propondría".

5. CERRAR CADA BLOQUE CON PREGUNTA O PEDIDO, no monólogo. "Does this match how you see the process?" Convierte presentación en conversación.

Micro-hábitos: pausar tras frases importantes (el silencio proyecta seguridad); si no sabe algo, decirlo y anotarlo (nunca inventar con un VP); no leer el guion; ritmo pausado (3 cosas bien > 8 atropelladas); dejar que J.R. interrumpa (buena señal).

Frases de recuperación si se queda en blanco: "Buena pregunta, déjame pensarlo un segundo"; "No lo tengo de memoria, lo confirmo y te lo mando hoy"; "Déjame mostrártelo mejor que explicártelo" (abre la herramienta); "Tienes razón en eso, ¿cómo lo harías tú?" (convierte crítica en colaboración).

## Guion J.R. — moscu-ops (el mapa) y el feedback aplicado
_chunk 1322 · 2026-07-21_

moscu-ops en una frase: el MAPA de toda la operación de soporte — dónde está cada cosa y cómo se conecta. Para quien ya trabaja aquí y navega productos, org, ciclo de ticket, infra, escalación sin preguntar. Secciones: Panorama, Organización, Ciclo de ticket, Secure, Engage, APIS (Legacy), Infraestructura, SnowTime, Links, Estado actual, Quick Reference. Bilingüe ES/EN (tecla L). ~16 diagramas de flujo.

EL MOMENTO CLAVE — feedback de J.R. del 9-jul aplicado (esto es la credibilidad de Juan):
- Error de modelo #1: Juan tenía a L1 escalando directo a Engineering/Delivery. FALSO. La ruta real es L1 → Under Support Review → L2 Support para la mayoría de productos; solo RTIaaS va directo a Engineering. Corregido.
- Error de modelo #2: L3 estaba solo como "Ingeniería". Le faltaba el brazo de Delivery (data, config, data mapping de menor alcance). Ahora L3 = Engineering (bugs/código) + Delivery (data/config/data mapping).
- Aprendizaje de fondo: al simplificar, Juan convirtió el soporte en una escalera lineal. El soporte real es triage y enrutamiento — UN GRAFO, NO UNA ESCALERA. Ese era el error conceptual. Re-modeló todo, no solo las flechas.
- Forma: contraste ilegible (grises y violeta de marca como texto quedaban <3:1). Creó variante legible y subió secundarios a ≥4.5:1 → WCAG AA.

Línea que más suma en toda la reunión: "The real fix wasn't cosmetic. You made me realize I'd drawn support as a ladder, and support isn't a ladder, it's routing. A graph. So I re-modeled it: L1 routes into Support first, and L3 always shows both arms, Engineering and Delivery." Cerrar con: "Is the routing model right now, in your view?"

## Guion J.R. — Onboarding Appriss (ruta 6 días) y decisiones de diseño
_chunk 1323 · 2026-07-21_

Onboarding Appriss en una frase: ruta guiada de 6 días que reemplaza las 2-3 semanas del onboarding oficial. Donde moscu-ops es el mapa (referencia), esto es el camino (rampa). Distinto propósito, público y diseño a propósito (Field Manual editorial, papel marfil, acento oxblood — distinto al dark de moscu-ops).

LA RUTA (6 días): 1) Llegada & Accesos (checklist 18 accesos que persiste). 2) La empresa & los productos (Azure, Secure/Engage/Incident-APIS, capa de datos). 3) El ciclo de ticket (11 pasos, prioridades, estados, cadencia 7/14/28, SLAs reales TJX/ICA). 4) Escalación & equipos (regla, matriz, Critical fuera de horario, proyectos Jira). 5) Herramientas & infraestructura (JQL, Snowflake, ADO, Control Panel, jump servers, Key Vaults, SnowTime). 6) Práctica con casos reales (4 post-mortems: RCS-27140/25547/23837/22394). Referencia permanente: Glosario ~28 términos, Enlaces 34 links verificados, Reglas 12 no negociables.

DECISIONES DE DISEÑO A JUSTIFICAR (demuestran criterio, no ejecución):
- ¿Por qué 6 días y no 3 semanas? Nadie retiene 1.454 páginas leyendo. Rampa curada que apunta a Confluence para profundidad. NO reemplaza a Confluence como sistema de registro; es la entrada curada hacia él.
- ¿Por qué un solo camino y no L1/L2/L3? Somos ingenieros de soporte con escalada natural a ingeniería. Un rol, un camino. Respeta el modelo de enrutamiento, no de escalera.
- ¿Por qué quiz por módulo? Que el que llega pruebe que entendió, no que solo pase páginas. Recuperación activa retiene más.
- ¿Por qué post-mortems reales? El soporte se aprende decidiendo sobre casos, no memorizando.
- ¿Por qué "manual de campo" y no dashboard? Es contenido de aprendizaje, no de monitoreo; separado visualmente a propósito.

Frase que ordena el par: "Two different jobs. The ops deck is the map, for someone who already works here. The onboarding is the path, for someone on day one. Same knowledge base underneath, two different front doors."

## Guion J.R. — Mantenimiento, encaje (Moscú), y honestidad del bus factor
_chunk 1324 · 2026-07-21_

CÓMO SE MANTIENE Y ENCAJA (adelantar las dos preguntas del VP: quién lo mantiene y cómo no queda desactualizado):
- Fuente única de verdad: todo el contenido en archivos de datos (espejo ES/EN), no regado en slides. Cambiar un dato es un solo lugar. Fuentes: sesiones KT (Kristin, Aimee), Confluence RTS, post-mortems reales.
- Es consultable, no solo legible: ambas herramientas conectadas a Moscú. Cualquiera puede PREGUNTARLE al material ("¿a quién escalo un ticket de Engage?") en vez de leer todo. Conocimiento queryable.
- Cero costo y cero riesgo técnico: SPAs estáticas (React/Vite), offline, sin backend, sin licencia, sin PII ni datos de cliente.

HONESTIDAD CALIBRADA (decirla tú, no esperar a que J.R. la saque — te hace ver senior): "I'll be straight about the one real risk: right now I'm the only person maintaining this. That's the same bus-factor problem we have with the knowledge itself, just moved. So part of what I'm asking for is a way to make this shared and official, not a personal side project, because a tool only one person can update is a risk, not a solution." Al nombrar tú la debilidad la desarmas y le das a J.R. la razón para adoptarlo oficialmente.

CIERRE (corto): "Bottom line: we're losing knowledge faster than we're writing it down, and these two tools are the fastest way I found to catch it and make it usable. I'll keep improving them either way, I just think they're more useful to the team than to me alone. Tell me where you want me to take this next." El "keep improving either way" comunica alguien que mejora su trabajo cada día con o sin aplauso.

## Guion J.R. — Banco de Q&A y objeciones difíciles
_chunk 1325 · 2026-07-21_

Q&A LISTAS:
- ¿Quién validó el contenido? Sale de KT (Kristin, Aimee), Confluence RTS y post-mortems reales; ya incorporé tus correcciones de enrutamiento; falta un pase de SME de Support sobre wording (es lo que pido). Curado y verificable, no infalible.
- ¿Reemplaza Confluence? No, a propósito. Confluence sigue siendo el sistema de registro (1.454 páginas). Esto es la entrada curada (on-ramp) que apunta a él.
- ¿Por qué dos herramientas? Dos trabajos: mapa (quien ya trabaja aquí) vs. camino (quien llega). Mezclarlos haría ambas peores.
- ¿Quién lo mantiene? Hoy yo, y ese es el riesgo; por eso pido volverlo oficial. Contenido en un solo lugar (data files espejo ES/EN), consultable en Moscú.
- ¿Cuánto costó/cuesta? Cero. SPAs estáticas offline, sin backend ni licencias.
- ¿Seguridad/datos? Sin PII ni datos de cliente; estático, local/offline.
- ¿No deberías estar en tickets? Lo construí en paralelo al KT (capturando lo que ya absorbía); mis tickets están al día (Samsung, Kohl's, Winn-Dixie).
- ¿No es "AI slop"? La IA aceleró la producción; el criterio es mío: pedagogía (6 días, quiz, post-mortems), cacé y corregí el modelo de enrutamiento, curé qué entra, verifiqué los 34 enlaces. Una IA no habría sabido que L1 enruta primero a Support; eso lo supe por tu corrección y por el KT.
- ¿Cómo mides que funciona? Días hasta productividad del próximo ingreso vs. 2-3 semanas; y baja de preguntas repetidas al equipo.

OBJECIONES DIFÍCILES (no defenderse; dar la razón donde la tenga y redirigir a la solución):
- "Es un proyecto personal tuyo." Tienes razón, hoy lo es, y ese es el problema que quiero resolver contigo; un proyecto personal muere cuando la persona se va (el error que pagamos con Kristin). Por eso pido volverlo oficial.
- "No tengo ancho de banda para SME/piloto." El piloto no cuesta extra (el próximo ingreso hará onboarding de todos modos); el SME son 2 horas. Si ni eso hay, dime cuándo y lo dejo listo.
- "¿Cómo sé que no tiene más errores?" No puedo garantizar cero errores en contenido operativo; garantizo el proceso: fuentes reales, pasó tu revisión de modelo, quiere pasar la de un SME. Prefiero material que se corrige rápido a uno que nadie revisa (la KB de hoy).
- "Esto ya existe (Confluence)." El contenido existe, regado en 1.454 páginas de 2-3 semanas. Lo que no existe es el CAMINO por ese contenido. Diferencia entre biblioteca y plan de estudio.

## REUNION-L2-L3-2026-08-05 — parte 1
_chunk 1610 · 2026-08-05 · fuente: REUNION-L2-L3-2026-08-05.md_

# Reunión L2/L3 Support, 5 ago 2026
**Duración:** 29 min · **Fuente:** transcripción completa + resumen de Moscú (meeting 94)
**Asistentes identificables:** J.R. Teagle, Camila Cortes, Amy, Pavan, Vlad (mencionado), Vedant

> Nota: el resumen automático de Moscú capta bien el tono de la reunión pero **omitió el punto que toca directamente a Juan**, la escala de la próxima ola de unificación y el pedido explícito de sugerencias. Ese punto va primero acá.

---

## 1. Lo que toca a Juan directamente

Salió la escala de la próxima ola de unificación. Textual del transcript:

> *"Folks have seen this happen where we just had 20 customers. Split all of them appropriately. We're probably looking at closer to 80 to 90 different tickets."*

Con 20 clientes fueron **61 tickets** (la cifra verificada de la ola del 27/28 jul). En la siguiente esperan **80 a 90**.

Y pidieron sugerencias explícitamente a Camila y a Juan sobre la parte de unificación, *"because we're the ones close"* a eso. Alguien planteó que el rol del equipo es sentarse aguas abajo y callarse, y la respuesta fue que hacerlo más suave está en el interés propio del equipo.

**La puerta está abierta y la abrieron por nombre.**

### Con qué llegar

Lo que ya existe y aplica:
- La taxonomía de **19 buckets** con los 61 tickets etiquetados y verificados por JQL
- Los patrones de causa raíz documentados (`reference_unificacion_patrones`)
- La oferta que quedó pendiente del 31 jul: **correr la verificación de correos contra los 10 clientes del 10 de agosto antes del corte**, con el select que mencionó Matt, para marcar a quien no tenga email vinculado antes y no después

Ese chequeo previo es lo que evita que el bucket de SSO mapping, que ya fue el más grande con 14 tickets, se multiplique cuando el volumen se vaya a 80 o 90.

---

## 2. Canales y puntos de contacto (quedó aclarado)

Lo más operativo de la reunión. Estaba difuso y Amy lo confirmó en vivo.

| Producto | Canal |
|---|---|
| Incident y Audit | canal **ALPS** (Aspect, APIS, LPMS) |
| Engage | canal **Engage Issues** |
| Secure 5, Legacy Secure 3 y 4 | canal **Secure 5** |

**Sobre on-call:** la duda de Amy fue si sigue existiendo el experto nombrado por día que tenía ALPS (un SRE o solutions expert distinto cada día). La respuesta es que **sí hay un schedule de on-call y esa persona es el punto de contacto del día**. Se le puede escribir por mensaje directo, no solo publicar en el canal. Vlad quedó mencionado como disponible aunque ocupado.

**Nota de Camila:** si un POC devuelve la pelota diciendo que no es la persona correcta, está bien, preguntarle a quién sí. Ella misma advirtió que los POCs que reparte pueden estar desactualizados porque las responsabilidades del equipo cambiaron.

---

## 3. Lo que pidió J.R.

**Escalaciones.** La respuesta al cliente no puede ser copy paste de la anterior. Incluso *"esto es más complejo de lo que pensaba, estoy profundizando"* previene una escalación mejor que repetir lo mismo. Recomendó bloquear tiempo en el calendario para responder.

> Coincide exactamente con el diagnóstico del backlog del 3 ago: la cola no está atascada por dificultad técnica sino por comunicación con el cliente.

**Pedir ayuda.** Puso el límite explícito: responde la misma pregunta hasta tres veces, después espera que ya sepas lo básico. Y el corolario que sí es acción: **si estás preguntando algo es porque no hay proceso escrito, así que escríbelo.** La documentación sirve para uno mismo y para el siguiente.

**Trainings pendientes**, en especial **OWASP**. Revisar si falta alguno.

**India:** trabajan QMATE / Q-Maintenance la próxima semana en persona.

---

## 4. Lo de Amy, aplicable a tickets estancados

Si un ticket va y viene por correo **más de dos veces**, agendar llamada. Una llamada de 10 minutos resuelve lo que 10 correos no. Y hay clientes que abren el ticket pidiendo llamada directamente porque prefieren no escribir.

J.R. añadió: en la llamada, revisar qué otros tickets tiene ese cliente y bajarlos juntos. Y ser breve, una llamada de 30 minutos no tiene que durar 30.

### Dónde aplica ya

| Caso | Situación |
|---|---|
| Vitamin Shoppe (RCS-28005, 28084, 28032) | Los tres esperan lo mismo de Joe Austin. Una conversación desatasca tres tickets |
| RCS-27765 Winn-Dixie | 8 días sin movimiento, esperando al cliente |
| RCS-27959 PacSun | 5 días sin movimiento, esperando al cliente |

Camila ofreció **preparar y liderar la llamada** mientras uno se acostumbra, y va a hacer sesiones en altavoz las próximas dos semanas para que el equipo escuche llamadas reales.

---

## 5. Tono y contexto del equipo

- Período de transición que esperan dure **uno o dos meses**. J.R. y Camila los dos lo reconocieron explícitamente.
- Camila: si sientes que te asignan muchos tickets y ninguno se mueve, decírselo. Ella está aprendiendo quiénes son los POCs también.
- Camila: pedir a quien resolvió algo que te enseñe cómo, para poder hacerlo la próxima. No arreglarlo solo si no sabes.
- **Reconocimientos:** Pavan agradeció a **David Beck** y a **Luke** (que no le reporta), y dijo que Luke, Vlad y David son su respaldo. Camila reconoció el mes en que el equipo llevó tickets por su cuenta.
- Próxima semana arrancan en limpio con los tickets nuevos.

---

## REUNION-L2-L3-2026-08-05 — 6. Action items
_chunk 1611 · 2026-08-05 · fuente: REUNION-L2-L3-2026-08-05.md_

## 6. Action items

**De Juan:**
- [ ] Llevar sugerencias de proceso para la próxima ola de unificación (pedido explícito, 80 a 90 tickets esperados)
- [ ] Ofrecer la verificación de correos de los 10 clientes del 10 de agosto, antes del corte
- [ ] Revisar trainings pendientes, en especial OWASP
- [ ] Agendar llamada consolidada con Joe Austin (Vitamin Shoppe, 3 tickets)
- [ ] Recordatorio a Winn-Dixie y PacSun

**Del equipo (del resumen de Moscú):**
- Preparar el trabajo de Q-Maintenance en India
- Completar trainings pendientes, incluido OWASP
- Organizar sesiones en altavoz para escuchar llamadas
- Documentar procesos y soluciones de tickets
- Aclarar canales y POCs por línea de producto (ya resuelto en esta reunión, ver sección 2)

**Decisiones registradas:**
- Respuestas detalladas y personalizadas al cliente para prevenir escalaciones
- Escuchar llamadas de colegas con experiencia
- Arrancar en limpio con los tickets nuevos la próxima semana

## SYNC-L2-L3-RESUMEN-BILINGUE-2026-08-05 — parte 1
_chunk 1612 · 2026-08-05 · fuente: SYNC-L2-L3-RESUMEN-BILINGUE-2026-08-05.md_

# Resumen para el sync L2/L3 · inglés y español
**Fecha:** 5 ago 2026 · Juan Martinez
**Para qué:** qué decir en el sync sobre lo trabajado y lo que está en marcha, en tono humano y conversacional.

**Fuentes:** base de Moscú (`sessions.db`, 93 reuniones al 4 ago, 1408 knowledge chunks, 453 items), los 20 archivos de memoria, y los documentos de trabajo en `~/Downloads` del 29 jul al 4 ago.

**Sobre la reunión:** no existe un evento titulado literalmente "L2/L3 Support team sync" en la base. El hilo recurrente del equipo sí está: 31 jul (transiciones, spreadsheet de Jira de Camila, proceso de escalación de incidentes), 17 jul (L2 en 86 tickets, backfills), 14 jul (rotación de on-call India/Colombia), 26 jun, 24 jun (queue grooming), 22 jun. Ese es el público para el que está escrito.

---

# 🇬🇧 ENGLISH

## The short version, if the sync is moving fast

> The unification labeling pass is done, 61 tickets labeled and verified in Jira across 19 buckets, and the root cause patterns are written up so we're not investigating from scratch anymore. My queue is at 21 and I closed five Monday night, nothing sitting resolved but unclosed. I ran the Colombia triage session for the seven tickets Viraj's team left after their pass. Three things I need answers on: the right label for Incident tickets, the Chemist Warehouse five, and the real session timeout value per tenant.

## The full update, about two to three minutes

> On unification, the labeling pass is finished. All 61 tickets from the July 26 wave are labeled and verified by JQL, spread across 19 buckets. Worth flagging the number, because in chat I told J.R. 45 and that was what filter 43256 showed. Once I swept all statuses like he asked, 17 closed tickets from the same wave came in, plus RCS-27573, so it's 61. There's a JQL saved that you can group by label from the search bar if anyone wants to walk a single bucket live.
>
> The real value out of that wasn't the labels, it was getting the patterns written down. SSO mapping is by far the biggest at 14 tickets, and almost all of it traces back to one change: email became the username. From that you get two whole families of failures, duplicate accounts with the 1, 2, 3 suffix, and users who never linked an email before the cutover who either didn't migrate or can't authenticate. Forgot Password doesn't rescue those, because the mail goes to an address that isn't theirs. Fix the email first, then reset.
>
> I had a 56 minute session with Kiran on Sunday going ticket by ticket, and a few things came out that save us real time. Session timeout going from 300 to 30 minutes isn't a bug, it's a decision they took syncing NetTrack with Secure. Admins losing permission groups at the cutover is a known pattern, confirmed at Ahold, we fix it by hand and don't need to escalate. And employee searches returning everyone in a store isn't a bug either, we verified that live on Food Lion.
>
> On my own queue, I'm at 21 and closed five Monday evening: the Ahold duplicates, Tahoe Donner, the Santikos 404, the Samsung Engage API allow list, and the DHL Sedgwick automation. Completed and Under Support Review are both at zero, so there's no finished work sitting unclosed under my name. The one I'll flag is RCS-27941 for Tailored Brands, six days in Work in progress with the SLA running and the action on me.
>
> On the triage exercise, Viraj's team went first because of the time zone and took 14 of the 21, so I ran the Colombia session Monday with the remaining seven. I want to say something about method, because my first pass was wrong. I deduced the team from who had tickets in Jira and ended up with four people who aren't on the team and missing five who are. The order that works is roster first, then real workloads, then profile. And on workloads, Diego looked lightest at 6, but with the orphan tickets already on him he's actually at 12, so nobody was starting from zero.
>
> The thing I'd like the group to sit with: the queue isn't stuck on technical difficulty. Of the 37 unassigned, none were High or Critical, and 24 of the 37 were Secure 5 with only 8 Incident. It stalled because everyone was on Incident, and because of customer communication. Chris did a pass Friday and 14 of about 20 comments were follow up requests, not findings.

## Two crosses worth naming out loud

> Sebastian has RCS-28106, Santikos SmartAlerts, Critical. When I analyzed RCS-28112 for Stater Bros, 248 of the 255 HTTP 500s on the nettrack app service were on the same SendSmartAlert endpoint. His Critical and the Stater Bros degradation look like the same thing seen from two sides, so it's probably worth working them together.
>
> And RCS-27549, ICA SE, High, open since June 25 with a formal RCA request, is sitting on Carlos Jacinto's deactivated account. It wasn't on the list and it's the most serious thing I turned up.

## Open questions to raise

> First, which label should we be using on Incident tickets? The one I have documented is Support_Data_Team and that's Secure 5. Team Ownership and Sprint are also empty across all of them, and there are two fields with nearly the same name, so I'd rather confirm which one feeds the reports before I fill anything in.
>
> Second, the Chemist Warehouse five. Hypercare handover, no priority set, oldest one at 82 days. Do those go back to the project team or do we distribute them?
>
> Third, the session timeout. Kiran said Secure is 30, but Engineering gave different figures in RCS-28153, 60 by default with a max of 240. I don't want to quote a number to a customer until we confirm what's actually set per tenant.

## SYNC-L2-L3-RESUMEN-BILINGUE-2026-08-05 — If someone asks for detail
_chunk 1613 · 2026-08-05 · fuente: SYNC-L2-L3-RESUMEN-BILINGUE-2026-08-05.md_

## If someone asks for detail

**Santikos 404**: the app was building URLs without the `screens/incident/<client number>/lpms/screens/` segment, so everything past the first step 404'd. Started working after a screen rebuild, and there are now two more confirmed precedents in the same wave, Vitamin Shoppe and Big Y. That's a reusable fix now, Screen Manager with `?ADMIN=9QQP` then Build All Screens.

**Big Y WAF block**: Cloudflare blocking the root domain when you hit it without the tenant slug. Ray ID `a23606220b52590b`.

**The 13 users missing from membership.Users**: the discrepancy with Kiran wasn't a data problem, it was a join key problem. I was joining on `incidentUserID`, she was searching by email. A user can have a row in membership with the link unpopulated, so it "exists" by email and is "missing" by join. There are at least three distinct failure classes in that one bucket, and any reconciliation query needs to show both join paths in separate columns. Numeric UserID thresholds don't work for scoping the new block, ADUSA starts at 1.8 billion and returned 2,300 false positives.

**Ahold duplicates, RCS-28135**: the plan Kiran and I agreed was to disable, not delete. What got executed was a DELETE of 376 rows in `membership.Users` with `Inactive = 1` only in `incident.LPUser2`, and the customer was promised individual reactivation as an exception. That difference is still open with Kiran, so I'd frame it as a finding in validation rather than a closed item.

**RCS-28032, Vitamin Shoppe**: still open, no confirmed root cause. Dayna Rivera covers districts 501 and 504 and can only reach one at a time. Permission groups are ruled out, she has the same three base groups as the DMs that work. What's actually different is that she has two stores where every working DM has one.

**Timezone, RCS-28030**: Incident reads the timezone from the browser session, not the profile, so nobody sees the correction until they sign out and back in. It looks like a failed fix if you skip that step. Also worth confirming with Matt which zone landed on each tenant, ADUSA should be EST and Stater Bros is California and should be PST.

---

# 🇪🇸 ESPAÑOL

## Versión corta, si el sync va rápido

> La pasada de labels de la unificación quedó lista, 61 tickets etiquetados y verificados en Jira en 19 buckets, y los patrones de causa raíz quedaron escritos, así que ya no investigamos desde cero. Mi cola está en 21 y cerré cinco el lunes en la noche, no quedó nada resuelto sin cerrar. Corrí la sesión de triage de Colombia con los siete tickets que quedaron después de la pasada del equipo de Viraj. Necesito respuesta en tres cosas: el label correcto para Incident, los cinco de Chemist Warehouse, y el valor real del timeout de sesión por tenant.

## La versión completa, dos a tres minutos

> Del lado de la unificación, la pasada de labels está terminada. Los 61 tickets de la ola del 26 de julio quedaron etiquetados y verificados por JQL, repartidos en 19 buckets. Vale aclarar el número, porque en el chat le dije 45 a J.R. y eso era lo que traía el filtro 43256. Cuando hice el barrido con todos los estados que él mismo pidió, entraron 17 tickets cerrados de la misma ola, más el RCS-27573, y de ahí salen los 61. Dejé un JQL que se puede agrupar por label desde la barra de búsqueda, por si alguien quiere recorrer un bucket en vivo.
>
> Lo que realmente sirvió de todo eso no fueron los labels, fue dejar los patrones escritos. SSO mapping es de lejos el más grande con 14 tickets, y casi todo se remonta a un solo cambio: el email pasó a ser el username. De ahí salen dos familias enteras de fallas, las cuentas duplicadas con sufijo 1, 2, 3, y los usuarios que nunca vincularon su email antes del corte, que o no se migraron o no pueden autenticarse. Y Forgot Password no los rescata, porque el correo va a una dirección que no es la suya. Primero se corrige el email, después se resetea.
>
> Tuve una sesión de 56 minutos con Kiran el domingo, ticket por ticket, y salieron varias cosas que nos ahorran tiempo real. El timeout de sesión bajando de 300 a 30 minutos no es un bug, es una decisión que tomaron al sincronizar NetTrack con Secure. Los administradores que perdieron sus permission groups en el corte son un patrón conocido, confirmado en Ahold, se arregla a mano y no hace falta escalarlo. Y las búsquedas que devuelven todos los empleados de una tienda tampoco son un bug, eso lo verificamos en vivo con Food Lion.
>
> En mi cola propia estoy en 21 y cerré cinco el lunes en la tarde: los duplicados de Ahold, Tahoe Donner, el 404 de Santikos, el allow list de la Engage API de Samsung, y la automatización de Sedgwick de DHL. Completed y Under Support Review están los dos en cero, así que ya no queda trabajo terminado sin cerrar a mi nombre. El que sí quiero marcar es el RCS-27941 de Tailored Brands, seis días en Work in progress con el SLA corriendo y la acción del lado mío.
>
> Sobre el ejercicio de triage, el equipo de Viraj arrancó primero por el huso horario y tomó 14 de los 21, así que yo corrí la sesión de Colombia el lunes con los siete que quedaron. Quiero decir algo del método, porque mi primera pasada estuvo mal. Deduje el equipo de quién tenía tickets en Jira y me salió con cuatro personas que no son del equipo y sin cinco que sí. El orden que funciona es roster primero, después cargas reales, después perfil. Y sobre cargas, Diego parecía el más liviano en 6, pero con los tickets huérfanos que ya tenía encima está realmente en 12, así que nadie arrancaba de cero.
>
> Lo que me gustaría que el grupo se quede pensando: la cola no está atascada por dificultad técnica. De los 37 sin asignar, ninguno era High ni Critical, y 24 de los 37 eran Secure 5, solo 8 de Incident. Se estancó porque todos estaban en Incident, y por comunicación con el cliente. Chris hizo una pasada el viernes y 14 de unos 20 comentarios eran pedidos de seguimiento, no hallazgos.

## SYNC-L2-L3-RESUMEN-BILINGUE-2026-08-05 — Dos cruces que vale decir en voz alta
_chunk 1614 · 2026-08-05 · fuente: SYNC-L2-L3-RESUMEN-BILINGUE-2026-08-05.md_

## Dos cruces que vale decir en voz alta

> Sebastian tiene el RCS-28106, SmartAlerts de Santikos, Critical. Cuando analicé el RCS-28112 de Stater Bros, 248 de los 255 errores HTTP 500 del app service de nettrack estaban en el mismo endpoint de SendSmartAlert. Su Critical y la degradación de Stater Bros parecen la misma cosa vista desde dos lados, así que probablemente conviene trabajarlos juntos.
>
> Y el RCS-27549, ICA SE, High, abierto desde el 25 de junio con pedido formal de RCA, está a nombre de la cuenta desactivada de Carlos Jacinto. No estaba en la lista y es lo más grave que encontré.

## Preguntas abiertas para plantear

> Primero, qué label deberíamos usar en los tickets de Incident. El que tengo documentado es Support_Data_Team y ese es de Secure 5. Team Ownership y Sprint también están vacíos en todos, y hay dos campos con nombre casi idéntico, así que prefiero confirmar cuál alimenta los reportes antes de llenar nada.
>
> Segundo, los cinco de Chemist Warehouse. Handover de hypercare, sin prioridad puesta, el más viejo en 82 días. ¿Vuelven al equipo de proyecto o los repartimos?
>
> Tercero, el timeout de sesión. Kiran dijo que Secure son 30, pero Engineering dio otras cifras en el RCS-28153, 60 por defecto con máximo 240. No quiero darle un número a un cliente hasta confirmar qué quedó configurado realmente por tenant.

## Si alguien pide detalle

**404 de Santikos**: la app armaba las URLs sin el tramo `screens/incident/<número de cliente>/lpms/screens/`, así que todo lo que pasaba del primer paso daba 404. Empezó a funcionar después de un rebuild de pantallas, y ya hay dos precedentes más confirmados en la misma ola, Vitamin Shoppe y Big Y. Eso ya es un arreglo reusable, Screen Manager con `?ADMIN=9QQP` y después Build All Screens.

**Bloqueo del WAF en Big Y**: Cloudflare bloqueando el dominio raíz cuando se le pega sin el slug del tenant. Ray ID `a23606220b52590b`.

**Los 13 usuarios ausentes de membership.Users**: la discrepancia con Kiran no era de datos, era de clave de join. Yo unía por `incidentUserID`, ella buscaba por email. Un usuario puede tener fila en membership con el vínculo sin poblar, así que "existe" por email y "falta" por join. Hay por lo menos tres clases distintas de falla metidas en ese bucket, y cualquier query de reconciliación tiene que mostrar las dos rutas en columnas separadas. Los umbrales numéricos de UserID no sirven para delimitar el bloque nuevo, ADUSA arranca en 1.800 millones y devolvió 2.300 falsos positivos.

**Duplicados de Ahold, RCS-28135**: el plan que acordamos con Kiran era deshabilitar, no borrar. Lo que se ejecutó fue un DELETE de 376 filas en `membership.Users` dejando `Inactive = 1` solo en `incident.LPUser2`, y al cliente se le había prometido reactivación individual como excepción. Esa diferencia sigue abierta con Kiran, así que lo plantearía como hallazgo en validación y no como algo cerrado.

**RCS-28032, Vitamin Shoppe**: sigue abierto, sin causa raíz confirmada. Dayna Rivera cubre los distritos 501 y 504 y solo alcanza uno a la vez. Permission groups quedó descartado, tiene los mismos tres grupos base que los DM que funcionan. Lo que sí la hace distinta es que tiene dos tiendas donde todos los DM que funcionan tienen una.

**Timezone, RCS-28030**: Incident lee la zona horaria de la sesión del navegador, no del perfil, así que nadie ve la corrección hasta que cierra sesión y vuelve a entrar. Parece un fix fallido si uno se salta ese paso. También vale confirmar con Matt qué zona quedó en cada tenant, ADUSA va a EST y Stater Bros es California y debería ser PST.

## MOSCU-KIRAN-LLAMADA-2026-08-03 — parte 1
_chunk 1615 · 2026-08-04 · fuente: MOSCU-KIRAN-LLAMADA-2026-08-03.md_

# Llamada con Kiran Vadday, 3 ago 2026 (56 min) — conocimiento operativo

**Fuente:** transcripción de Teams, sesión de revisión ticket por ticket con Kiran Vadday (bvadday@apprissretail.com), Data/Migration Engineering, 4 años en Appriss.
**Tickets cubiertos:** RCS-28135 (Ahold, duplicados), RCS-28093 (Ahold, filtros de empleados), RCS-28112 y relacionados (timeouts e Izenda), permisos de admin perdidos.
**Para qué sirve este documento:** estas reglas rigen el diagnóstico de cualquier ticket de la Unificación. Contrastar contra esto antes de investigar desde cero.

---

## Dónde está el flag Disabled en Control Panel

Está en **User details, arriba del todo, junto al email**.

> *"it's like the very top e-mail user details and Disabled. So once they click this and that user is gone, bye bye."*

Kiran lo buscó en vivo por cinco pestañas antes de encontrarlo y perdió varios minutos:

> *"Nothing here says Disabled, right? Permission groups, not hierarchies is also not the place. User teams, nope. Secure incident, nope. Advanced properties, nope. Yeah, there is nothing. Oh, I hate this. There is nothing that disables."*

Y al encontrarlo:

> *"We wasted time, I'm sorry. There is Disabled. You see this?"*

**No está en:** Permission groups, Hierarchies, User teams, Secure incident, Advanced properties.

Por debajo es la columna `Disabled` de `membership.Users`, se pone en 1. Un usuario deshabilitado deja de aparecer en la vista `lpuser`: *"if I change that to one. This won't come up in the view."*

El cliente puede hacerlo solo desde Control Panel. No hace falta que Support toque la base para eso.

---

## Por qué existen las cuentas duplicadas con sufijo 1, 2, 3

Es consecuencia directa del cambio de modelo de identidad, no un defecto de la migración.

En el sistema legacy una misma persona podía tener varios LoginID bajo un mismo email, porque así se probaba con distintos niveles de seguridad:

> *"you are trying to log in yourself multiple different ways only because you are setting yourself up for different security levels. So you're trying to log in with J. Martinez for admin. And if you wanted to test something as a store manager, you can do that yourself by creating an extra login."*

La migración exige email único, así que Kiran conservó el email real y renombró los demás:

> *"when I'm migrating stuff, I'm only caring about e-mail address. So J. Martinez, Martinez J or JM, everything has the same e-mail address. So I am picking one, the actual e-mail address, and brought in the other two as J. Martinez 1, J. Martinez 2, and so on, because the migration would break in between if I don't have unique e-mail addresses."*

**La cuenta buena es siempre la del email limpio, sin número.**

**Riesgo que ella misma marcó:** si el email real de una persona termina en 1 y no existe la versión sin número, esa cuenta no es duplicada y no se debe tocar. El criterio de detección es la existencia del par, no el sufijo suelto.

**El plan acordado era deshabilitar, no borrar:**

> *"anything with ones, twos, and threes, I think can be set to Disabled equals to one. I can write up a script and save that... so if any client comes forward saying, hey, this is causing issues because we are seeing duplicates, then we can rerun the script."*

En RCS-28135 lo que se ejecutó después fue un DELETE de 376 filas en `membership.Users`, dejando `Inactive = 1` en `incident.LPUser2`. Al cliente se le había prometido reactivación individual como excepción. Esa diferencia sigue pendiente de aclarar con Kiran.

---

## La regla de identidad de la plataforma unificada

> *"in secure, your platform unification, we are not allowing any such kind. You have to create a new e-mail address, not just login, because there is nothing called a new login. Any new login is a new e-mail address."*

Todo lo que sea "el usuario quiere otro login" se responde con esto: en la plataforma unificada un login nuevo es una dirección de correo nueva.

---

## Cómo identificar la cuenta real entre duplicadas

Por la contraseña. La cuenta que sigue con la contraseña por defecto nunca se usó.

> *"you see how the password is default password. If you see H24, it's like the default password... So if the password for this person changed, then that means this is the right person. This person also has the default password."*

**Equivalente en Control Panel, sin tocar la base:** un usuario sin last login nunca entró. Es el chequeo rápido antes de asumir que una cuenta está bloqueada, y normalmente apunta a que el email del registro está mal, no a un bloqueo. Verificado el 4 ago 2026 con Dillon Wadsworth de Big Y (RCS-28033): se corrigió email y LoginID, no hubo desbloqueo.

---

## Timeout de sesión: 300 a 30 minutos

No es un bug, es una decisión de arquitectura tomada al unificar.

> *"we sync that time out with secure, so we used to do 300 minutes in the old NetTrack, but secure guys do it 30 minutes. NetTrack is not the major pro app of everything. The secure, engage, EBR, these are top-notch apps and everything is in secure side. So we went and sat with them. You won't dictate rules to them, right? You will keep your mods, you will adapt to them."*

> *"our NetTrack users are not used to logging out in 30 minutes. So either increase the time for NetTrack, keep it separate from secure, or I don't know what they'll do."*

En RCS-28153 Engineering le dio a Big Y otras cifras, 60 minutos por defecto con máximo 240 configurable. Confirmar el valor real del tenant antes de comprometer un número con un cliente.

---

## MOSCU-KIRAN-LLAMADA-2026-08-03 — No perseguir el síntoma antes que la causa
_chunk 1616 · 2026-08-04 · fuente: MOSCU-KIRAN-LLAMADA-2026-08-03.md_

## No perseguir el síntoma antes que la causa

Sobre el fallo de export a Excel en Izenda:

> *"I don't want to talk about exporting Excel before talking about timeout issues. Maybe if the timeout issues are fixed and everything is working flawlessly, that's when we can go to the export issue... I think it's a wasted effort if we start looking at the exports even before Izenda issue is resolved."*

> *"if nobody's pressing on 'hey, we are not able to export reports', then let it be internal."*

Regla práctica: si el síntoma depende de algo roto aguas arriba, se documenta como nota interna y se espera. Solo se convierte en trabajo propio si el cliente lo presiona o si la causa raíz ya está cerrada y el síntoma persiste.

---

## Pedir el caso concreto antes de investigar

La lección más repetida de la llamada. Sin un caso reproducible se pierden horas navegando pantallas.

> *"Whenever they say something like that, can you say hey, can you please give us the URL of the incident you're trying? Which incident, can you give us the link to the workbench that you're trying? All we need is this. Once we get this, we can immediately go to that page and be like, okay, this is where they're trying, and we can try it ourselves."*

> *"we need screenshots and exact details... a sample example would really help. Like, Amanda of Food Lion should not exist in this search for Stop and Shop."*

> *"see, we are wasting time in figuring. So if she had given us an incident or a case or anything, that would have been really helpful."*

Lo que hay que pedir: URL del incidente o link al workbench, usuario afectado, captura, y un ejemplo concreto de qué se ve mal frente a qué se esperaba.

---

## Lo que la migración no tocó: empleados y asociados

> *"employees and platform unification have nothing to do... Associate lookup actually looks into the employee table and we did nothing to employee table. So I highly doubt how this is an issue."*

> *"there were initial issues with LP user view because we did not get that synced, and it syncs now, and employees has nothing to do with anything else."*

Un reporte de empleados duplicados o cruzados entre marcas se trata primero como no relacionado con la migración. Se pide confirmación de si sigue ocurriendo y un ejemplo, antes de escalar.

**Comportamiento correcto verificado en vivo:** buscar por marca Food Lion y ubicación 0001 en Manage Employees devuelve todos los empleados de esa tienda, con nombres y departamentos distintos. Eso no es duplicación.

> *"it's bringing all the records belonging to 001 location, which is right. And that is what it should bring."*

**Nombre real de la pantalla:** el cliente y los tickets dicen Manage Associates, pero en el nivel de admin se llama **Manage Employees** (`manageemployees.aspx`). Kiran: *"we are so bad at naming our stuff."*

---

## Permisos de admin perdidos en el corte

Confirmado en Ahold con Leanne Stepps y April Valerie: eran administradoras antes de migrar y quedaron sin el grupo.

> *"Absolutely no clue. They should all have."*

Se arregla a mano en Control Panel. Ruta completa que mostró Kiran: sitio de producción, `All apps`, `Settings`, `Users`, buscar al usuario, `User details`, `Permission groups`, agregar y **guardar**.

> *"Try add as many as you want and save at the end. Don't forget to save."*

**Línea base de grupos para cualquier usuario:** `ApprissCase Search Users`, `ApprissCase Users`, `Basic Users`.

> *"I wonder why Leanne doesn't have these three. Because that's basic for everybody."*

Si a alguien le faltan, agregarlos aunque no sea lo que vino a pedir.

Para verificar accesos de admin de alguien: abrir el usuario, `User details`, `Permission groups`. El título del usuario no sirve como indicador.

---

## Client ID obligatorio en cada ticket

Kiran lo pidió expresamente y se lo propuso a Matt como estándar.

> *"Whatever you did with your first comment putting on the client IDs, that's what I said to Matt. I think it should become mandatory in every ticket, because now the platform looks like this. If you say Adusa Delhaize, I have to go to the Excel sheet, find out what Delhaize or Sportsman's is, find out their client ID 420, and then go to 420."*

> *"we got rid of company names in the database and got only client IDs. Back in the day it was not a big deal because databases are named by company names. But not anymore."*

Poner el número de cliente en el comentario interno ahorra un paso a cada persona que abre el ticket después.

---

## Acceso a la infraestructura: orden de los pasos

Para llegar a `PLAFRMTRDP01` y de ahí a SQL MI:

1. VPN arriba
2. Activar PIM en la URL de activación
3. Recién ahí conectar por RDP
4. Desde el RDP, conectar a SQL MI, producción o staging

> *"VPN step one, activation step two, RDP step three, and then in the RDP you can connect to SQL MI."*

Bastion funciona pero es lento, y para cambios de permisos Control Panel es más rápido que ir a la base.

---

## Cierre

Kiran sobre el trabajo de Juan:

> *"you did a great job on documenting and writing stuff up, making our lives easier. We wanted more people like you who can do a great support work."*

## Call with Kristin Krogman — parte 1/7
_chunk 1629 · 2026-07-22 · fuente: Call with Kristin Krogman.docx_

Call with Kristin Krogman-20260722_150111-Meeting Recording
22 de julio de 2026, 8:01p.m.
53m 52s
Juan Martinez inició la transcripción
Juan Martinez   0:04Okay.
Kristin Krogman   0:04Yep, OK.Well, wait, like it's going OK.
Juan Martinez   0:07Ready.
Kristin Krogman   0:11So, do you remember where to go? That's correct.
Juan Martinez   0:12I need to create.Space, this is like a nice incident, or yeah, or yes, incident.
Kristin Krogman   0:24Yep, because there's something wrong here. And just remember where you're at here. Right now, you're opening it because we have to wait till we add her to the portal. So we'll have to go back and change her to the reporter in this particular case. Otherwise, if they're already in the portal,
Juan Martinez   0:24Okay.K.
Kristin Krogman   0:44you could put them there.
Juan Martinez   0:46Okay.
Kristin Krogman   0:48Okay, so Kimberly.Hey, she's from Easy Corp.
Juan Martinez   1:00And organizations.
Kristin Krogman   1:03Yep, Easy Corp, that's it right there.
Juan Martinez   1:09This takes us.
Kristin Krogman   1:10Okay.
Juan Martinez   1:12Easy Corp.
Kristin Krogman   1:12Yeah.
Juan Martinez   1:14The problem is logging.
Kristin Krogman   1:18This one, let's see what are our options. Because she's in, she's having trouble being able to view or edit a case. So I would just put a feature. It's kind of a feature functionality question. There isn't a good answer for that one.
Juan Martinez   1:34K.
Kristin Krogman   1:36And then this will be incident.
Juan Martinez   1:40Instant, OK.
Kristin Krogman   1:43Yeah, at least I believe so, master case. OK, so then first, well, back on that play, go back, yep, up in the summary, started off doing the easy Corp as your company, and then the dash.
Juan Martinez   2:00Is Easy Corp?
Kristin Krogman   2:02Yep.
Juan Martinez   2:04Yes, is it called Dash?
Kristin Krogman   2:06Yep.Yeah.
Juan Martinez   2:08Uhh.
Kristin Krogman   2:12Do the, not that it really matters, but where Corp is, just switch the P and the R around.
Juan Martinez   2:22Yeah, yeah.
Kristin Krogman   2:22There you go.Gotta get used to those names.
Juan Martinez   2:27Yeah, is like a...What an issue, or I don't know?
Kristin Krogman   2:33Just put.Unable to edit case. That'll be easy.Yep, unable.
Juan Martinez   2:46Naveen.Two.
Kristin Krogman   2:48to edit.Case.
Juan Martinez   2:55Sorry, Kit.
Kristin Krogman   2:57Pace, yeah.
Juan Martinez   3:01Yeah.It.A CS.Sorry, I tried to find the mail to do currently.
Kristin Krogman   3:15There you go, there you go.I just put it in your in the chat what I want you to put.
Juan Martinez   3:29Games.Okay, sorry.
Kristin Krogman   3:34Yep, there you go.
Juan Martinez   3:35To any case, I have a new issue that was.
Kristin Krogman   3:37Yeah.So go ahead and just go ahead and copy her words there.
Juan Martinez   3:42Ah, okay.In description.
Kristin Krogman   3:51Yep, just take what she put that hello all.You can just take all of that.
Juan Martinez   4:00Okay.
Kristin Krogman   4:08Okay, and then, yep, yep, yep, put that in there too.
Juan Martinez   4:10This part 2 Samsung set as a separate.What this?
Kristin Krogman   4:19It's not playing nice.
Juan Martinez   4:22Okay.
Kristin Krogman   4:23Okay, now this, what you're going to want to do is put the picture in there as well, the screenshot, and you can put it in the description. Yeah, so you're going to copy it and put it in there.
Juan Martinez   4:29The image?
Kristin Krogman   4:42There you go.Hey.
Juan Martinez   4:45Yeah.
Kristin Krogman   4:46All right, so then what you're going to do is go ahead and...Create it.And then go ahead and what I would do is grab it quick when it pops up.And then go ahead and put medium on it for right now for priority.
Juan Martinez   5:15A priority, not here.
Kristin Krogman   5:16Oh, sorry. Yeah, right there. Yep.
Juan Martinez   5:19Is it like a noun or a medium?
Kristin Krogman   5:21Just put it on medium, yeah.
Juan Martinez   5:23Okay.
Kristin Krogman   5:24OK, and then...
Juan Martinez   5:26Success.
Kristin Krogman   5:28Okay, then the Edwin team is going to do their thing and even though you're the reporter, we'll let that go. Because what we want to do now is you've got that number where you can see it.Right.
Juan Martinez   5:42The number of the ticket?
Kristin Krogman   5:44Yeah, what is it? 27930?
Juan Martinez   5:47Yeah.
Kristin Krogman   5:49Okay.So what you're going to want to do is we need to let her know about this now, right? So do you want to try typing something to her? Do you want me to put it together for you so you can send it to her?
Juan Martinez   5:56Okay.Aimee.Okay, you can, you can put it to send it to Eric.
Kristin Krogman   6:09You want me to put something together? Okay.Let me just do that quick.And then I'll share it with you.You.
Juan Martinez   7:00Okay.The request participants put automatically when I select the organization, yes?

## Call with Kristin Krogman — parte 2/7
_chunk 1630 · 2026-07-22 · fuente: Call with Kristin Krogman.docx_

Kristin Krogman   7:38But.Yes, they'll be, they will be set up automatically for you.
Juan Martinez   7:43A let me know black.
Kristin Krogman   7:46Yep, clean will show up in there as the CSM.
Juan Martinez   7:50Okay.
Kristin Krogman   9:05I'm almost done.
Juan Martinez   9:11Yes.
Kristin Krogman   9:19Almost done.OK.Quit.Okay, there we go. So now you go.To that e-mail that has, you know, everybody on it.
Juan Martinez   10:08I.
Kristin Krogman   10:11You reply all and put this in there for her so that she...So this will notify her that we've opened a ticket on her behalf.
Juan Martinez   10:24Yeah.
Kristin Krogman   10:24and that we're going to invite her to the customer support ticketing portal. And then once you do that, then we're going to, on that, the e-mail I sent you that has the instructions.You're going to use that and put it in another e-mail.
Juan Martinez   10:43Okay.
Kristin Krogman   10:44Okay, and we'll walk through this and you're going to send that to her and then we're going to put her in the portal. So step one is let's notify her about the ticket and that you know.We've opened it up for her and we're going to send her the invite. So what I just put in the chat, go ahead and put into the e-mail. If you want to change anything on here, feel free to do so. But this is what I would be doing to, or what I would end up sending to the customer, something along those lines.
Juan Martinez   11:00Yeah.Uh, okay, the mail is...Kimberly, yeah.
Kristin Krogman   11:28Yes.Let's make sure, okay, you've got that. Okay. But now this one, you're going to want to respond to the one where she sent that error message.
Juan Martinez   11:46The.I'm lost. The first one is the...
Kristin Krogman   11:51Good luck, hear that last.
Juan Martinez   11:56Hi, this, yeah?
Kristin Krogman   11:58Okay, let's go to what I want you to do. Go to the one where Kimberly, where you took the information and made the ticket. Go to that e-mail.
Juan Martinez   12:09Here.
Kristin Krogman   12:13Nope, go find, keep going backwards in time.Ohh.Let's see. At 12.50 your time.There should be an e-mail in there from Kimberly.
Juan Martinez   12:33Twelve 15.In the same thread, yeah, and in.
Kristin Krogman   12:41Mm.
Juan Martinez   12:41No, because in the 12th, I don't have males in the 12th.
Kristin Krogman   12:48How is that possible?That's weird.
Juan Martinez   12:54I just, uh.11.56 AM and the next one is 1.24 PM.
Kristin Krogman   13:07Okay, go to the top of this one then. Maybe it is on this e-mail string.And...Where's where's the one that we that you took it off of that we just created the ticket from? You were looking at it and you took the screenshot.
Juan Martinez   13:29This is screenshot.
Kristin Krogman   13:31No, the one we just put on the ticket.
Juan Martinez   13:37Oh.Sorry, sorry, sorry, is this?
Kristin Krogman   13:50Here we go. Here we go. Okay, so reply.All to this one.
Juan Martinez   13:58Reply to all.
Kristin Krogman   14:01Yes, we want them all to see it.
Juan Martinez   14:03Okay.
Kristin Krogman   14:04And now, what I put in the chat?That's what we want to.
Juan Martinez   14:08Hey, hello, Kimberly.Okay.
Kristin Krogman   14:12No.
Juan Martinez   14:16Up.close.I don't know.
Kristin Krogman   14:30Oh, go to your draft. I think it's opened in your draft.
Juan Martinez   14:33No.
Kristin Krogman   14:36Because there's two there.There you go.
Juan Martinez   14:40Yes.
Kristin Krogman   14:41Perfect.
Juan Martinez   14:42Yeah.Thanks.Let me fix the space.
Kristin Krogman   14:51Yeah.
Juan Martinez   14:57Okay.Yeah, I think that.Look forwarding the way up, yeah.
Kristin Krogman   15:13Okay, so then what you can do is you can go ahead and send that to send that one.
Juan Martinez   15:20Signed.
Kristin Krogman   15:22Yep.Okay, now you're going to want to grab the information from the e-mail I sent you. It has the instructions.
Juan Martinez   15:24Okay.In the mail that I that I sent, yes?
Kristin Krogman   15:43that I just sent to you, the one with the...
Juan Martinez   15:46Okay, so yes, yes.
Kristin Krogman   15:48Yeah.Yep, that one.Go ahead and get that information and put it on an e-mail just to her, because this is just for her.
Juan Martinez   15:54Yeah.Just her, okay.Uh, t-t-tum.Kimberly, Kimberly were.Kimberly.Yeah.
Kristin Krogman   16:34Okay.and then put a subject line in there. You can take the subject line for my e-mail too.
Juan Martinez   16:46Okay.
Kristin Krogman   16:49Yep, the subject, go back to the e-mail I sent you, that subject line that's in there.What did that?Where did it go? Oh yeah, the Appriss Retail Customer Support ticketing portal access information. Copy that and put it in the subject line.
Juan Martinez   17:13After we take coffee, Support.
Kristin Krogman   17:13There you go.Yep.
Juan Martinez   17:16Okay.
Kristin Krogman   17:17So then.Go ahead and send that to her.And then you're going to need her e-mail address again.
Juan Martinez   17:24Mhm.To her.

## Call with Kristin Krogman — parte 3/7
_chunk 1631 · 2026-07-22 · fuente: Call with Kristin Krogman.docx_

Kristin Krogman   17:30Yeah, you're going to need her e-mail address, Kimberly's.
Juan Martinez   17:35Okay, in the new, do you or readily?
Kristin Krogman   17:39Just so you've got it copied, because you're going to have to paste it in the, you know, when we send her her invite, we're going to need her contact.
Juan Martinez   17:52Okay, it's a new mail, yeah?
Kristin Krogman   17:55Yeah, you need that.So now, grab, grab her contact e-mail.
Juan Martinez   18:04This?
Kristin Krogman   18:06Yeah, we need her e-mail out here. It might be easier if I just go like this.
Juan Martinez   18:15Or maybe.
Kristin Krogman   18:15I'll put it in the chat too. That might be easier for you.
Juan Martinez   18:24Okay.
Kristin Krogman   18:25Okay, so you're going to want to copy that and then we're going to go into Jr. and you need to go to customers.On the left side.On the left-hand side, all the way to the left in the column.
Juan Martinez   18:49Postline.
Kristin Krogman   18:49Keep going left.
Juan Martinez   18:50Okay.
Kristin Krogman   18:50You can get off the ticket and go to the left. There you go. Now go up to customer.
Juan Martinez   18:57Oh yes, customers.
Kristin Krogman   18:58Yep, now organization.
Juan Martinez   19:01Yeah.
Kristin Krogman   19:03At the very top there.and then type in EZ and EZ Corp should come up. Okay, click on that.Okay, and then see where it says add customer.
Juan Martinez   19:19Yeah.
Kristin Krogman   19:20There you go.Yep, no, you just can click OK.Yeah.
Juan Martinez   19:30Look constable.Ready?
Kristin Krogman   19:37There you go. So now you can see she's been invited. Okay. It takes it takes just a minute. Sometimes you have to refresh, but if you go now to the ticket.
Juan Martinez   19:42Okay.
Kristin Krogman   19:49And her name is Kimberly Baney. So if you go to that Easy Corp ticket.And where it says over onto the right hand side, if you find a reporter.And it says your name. Click on that. Yep, click on it and type in Kimberly. KIM. Yep.
Juan Martinez   20:10Yes.
Kristin Krogman   20:18And...Ohh.
Juan Martinez   20:21Oh.Kimberly Benny, OK.
Kristin Krogman   20:24Yeah.Okay.She might not be in there yet. Oh, yeah, she spells it weird, so you have to backspace. Instead of L-Y, it's L-E-E.
Juan Martinez   20:41Ah, yeah, sorry.
Kristin Krogman   20:42Yeah.Okay, refresh your ticket because it might not, it might have to refresh in order for it to grab her name.OK, and then try again.
Juan Martinez   21:20No.Kimberly, no, it's OK, perfect.
Kristin Krogman   21:28Kimberly under score.Oh, there she is.
Juan Martinez   21:32Right, yeah, right.
Kristin Krogman   21:34Okay, perfect. Okay.So there you go.
Juan Martinez   21:40Okay, I need to put the screen and team on the ship.
Kristin Krogman   21:44I think this one is going to go to, and here, let me show you, because there was a ticket earlier that came in while you were on break.
Juan Martinez   21:49Yes.
Kristin Krogman   21:59that actually came into the high priority channel. Hold on, let me find it.
Juan Martinez   22:05Okay.Sorry, I feel like a fool, but I feel nervous since my freeze warfare with all this.
Kristin Krogman   22:15No, don't worry. You're getting so much stuff thrown at you, so don't worry. This is...It takes time to get used to this.
Juan Martinez   22:27Things.
Kristin Krogman   22:28So, no worries, and why is...This not showing up.Let me find it. Hold on.Different, Bryant.Different Ryan. I'm trying to find it back. Should be an Alps issues and it's not there.Oh yeah, there it is.Okay.The.I'm going to share my screen with you real quick.
Juan Martinez   23:07OK, I stop sharing my screen.
Kristin Krogman   23:12OK.So, in Alps issues, there was a ticket that came in here from Secure Audit, and I opened the ticket. It had that same error that we just saw from them.They're trying to key in safety meeting notes.Ryan Barlow, he's in Delivery.And he's working at, so this might be one.Might be. Let's take a look.Be.See, here's your, here's your message.and they're trying to key in safety meeting notes.And her issue.was very similar.She can't view a case or edit it regardless of who assigned it.Oh shoot, it's not there yet for me.It.Why is that showing up there?Okay, so we will see what he says because it might just be one that we assign right to him. You know, we see that message. Am I sure? Yeah, I am. Am I sharing my screen with you?
Juan Martinez   25:57No, no, actually, no.
Kristin Krogman   25:58Ohh.You didn't get to see any of that. I'm sorry.Okay, so I sent Ryan Barlow a message because...This ticket right here.Had the same message.And they were trying to key in safety meeting notes, which is a little different than, you know, what the other, what Easy Corp was doing. It's a little different, but yet there's similarities in what they were trying to do. So that's why I'm going to ask Ryan.
Juan Martinez   26:19Okay.Yes.

## Call with Kristin Krogman — parte 4/7
_chunk 1632 · 2026-07-22 · fuente: Call with Kristin Krogman.docx_

Kristin Krogman   26:40because it's possible that he already, he's going to end up with it anyway. And since he was just working on something, I want to point it out to him because it could potentially be a bigger issue for all of the incident products. And he would, you know, this brings it to its attention that, hey, we've got more than one.
Juan Martinez   26:50Okay.
Kristin Krogman   26:59right? So he'll get back to me and let me know, you know, yep, this is the same thing, assign it to me, whatever it is he says, or no, it's different. Well, if it's different, it needs to be triaged, you know, with the team, right? If it's the exact same issue, then we'll end up linking the tickets.So that.And we've got them together again, just in case there's a bigger issue, we can link other tickets. But I just wanted to show you that that I saw the same error here. And then I just reached out to Ryan because he is working on it. And where I saw that.was in a channel.Here.So they didn't put that same error message on, they put this one on, but this is it. So Ryan is working on it.So that's where I pulled that from was that Teams channel. Have you gotten access to these Teams channels too?
Juan Martinez   28:12And let me see, but I think that...Retail Ops.Ohh.Yes.Yes, but...But...I don't know why this group is looks like a height. I need to go to the see more channels and put in show because I can see previously, but actually yes, I have.access to AALPS issues, data issues.Legacy and security issues is I need to.All these channels.
Kristin Krogman   28:59There's potential for things to pop up, yeah, in all of this stuff. You'll want to be able to see data issues channel.Um, but anything under Retail Apps?you're going to want to be able to see or have access to, which you probably do if you start going in there.
Juan Martinez   29:18Yes, I...Yes, no, actually I have access to all all channels in Retail Ops, but I don't, I probably I don't configure the the option to show these channels. This is my, I don't know that I need to this manually to to to find these channels, but actually yes.
Kristin Krogman   29:23Good.Yeah.The.
Juan Martinez   29:39Yes, I have us.
Kristin Krogman   29:39Yeah, yeah, because you're going to see a lot of stuff here, here.
Juan Martinez   29:44In Retail, I don't have...I, I'm not.I'm not part of the retail, I know, yes, retail ops.
Kristin Krogman   29:58Hmm, I wonder who's...
Juan Martinez   29:58Engage issues.
Kristin Krogman   30:01Oop.Yeah, because you want, you're gonna need to see all of this. I wonder who owns this.It's public. You should be able to get into it then.
Juan Martinez   30:16Yes.Yes.Yes, I don't know the process to show the channels, but yes, actually I have access. But this is my first time seeing my teams because I never notified that I need to do this process. It's very important to know, but thanks. Yes, I have access.
Kristin Krogman   30:28Oh.Yeah.Yeah, this is going to be very important for you. This will be your best, your best friend.
Juan Martinez   30:41Ohh.Ohh.I need maybe access to...
Kristin Krogman   30:47This one, too.
Juan Martinez   30:50Priority issues.Chanel.
Kristin Krogman   30:56You'll need it here. This one, this one was the current L2 group. So you guys are probably going to make your own, I would think, you know, or or Amy will unlock this one and you guys will get it. I'm not 100% sure.
Juan Martinez   30:56Support.Um...Yeah.
Kristin Krogman   31:15Because we also post here. So I have posted that ticket there as well to the team so that we can get a hold of it and send a note to the customer that, hey, you know, we've received your high priority. You know, I'm currently triaging, whatever it may be. And once it goes to a different team.you know, your ticket has been moved to the delivery team, etc. So.
Juan Martinez   31:41OK.
Kristin Krogman   31:44Yeah, the other one you're going to want is this R&D channel.
Juan Martinez   31:48All right.Yes, yes, I have this channel with the 2026 engaging size, alpha and beta.
Kristin Krogman   31:58Yeah, because yeah, that's got the snowflake.Things, let's see. What's the platform unification? This is one that's continued ongoing. You're probably gonna, you and Camila are probably gonna have to watch this channel.
Juan Martinez   32:15Okay.
Kristin Krogman   32:16I'm thinking Amy will be around to probably help with that one. Hopefully it'll be done before Amy leaves.
Juan Martinez   32:24Ohh, the letter for modification. This is a good channel to review.
Kristin Krogman   32:30Yeah, there's lots of stuff here that you can see is going on.
Juan Martinez   32:32Boring.Okay, yes.
Kristin Krogman   32:36Here's your snow, here's your snow time one.
Juan Martinez   32:40Yes.
Kristin Krogman   32:42Snowflake that's going on, we send out communications for them too, so...
Juan Martinez   32:43Support.Yes.
Kristin Krogman   32:49Lots of fun. You having fun yet, Juan?
Juan Martinez   32:54Sorry?

## Call with Kristin Krogman — parte 5/7
_chunk 1633 · 2026-07-22 · fuente: Call with Kristin Krogman.docx_

Kristin Krogman   32:55Say, say, yes, I'm having fun.
Juan Martinez   32:57Yeah.
Kristin Krogman   33:00So much to learn.
Juan Martinez   33:03Yes, I I don't know because I I never see this in maybe an onboarding process or something like a say, hey, you need to add the channels and and and in teams, but whatever it's okay.
Kristin Krogman   33:21Okay, so Kimberly just responded and said, once on the ticketing portal, I received this message.Okay, that's weird.
Juan Martinez   33:33Probably.OK, yes, she you have. She's my direct supervisor. Thank you.
Kristin Krogman   33:37Oh.Okay, so this has to do with her access to Jr.Okay.Let's see.Feel like she might have done something wrong.I don't know what she could have done wrong.Hold on, let me...
Juan Martinez   34:10Ah, I see they mention it now have access.
Kristin Krogman   34:14Well, that's what she's saying. I think what we're going to do.I wonder if she tried once on the ticketing portal, I received this message. Is there something else I should be doing to avoid this error message? Okay.Let's.Okay.I'm going to show you something else. Okay. When you are communicating internally, you can grab this link and send this link to anybody internally and it shows everything that's on the ticket. Okay? Internal, external comments. When you're dealing with the customers,If you...Click here.This is the view that they see.when they log into the portal.
Juan Martinez   35:10Yeah.
Kristin Krogman   35:10And if you, if you grab the link from here, they will see this.Okay, so I'm gonna put this in our chat.
Juan Martinez   35:17Okay.
Kristin Krogman   35:24Baby, in our chat.And let's see, send this back to her. OK, so.I'm sorry, you ran to an issue.Okay.And then...Okay, then you could put the spaces in it as you need.but respond to Kimberly in her e-mail that she sent, you know, saying, hey, I couldn't see this. So you could take this and put it in your response to her, you know, apologizing for the running into the issue.have her try accessing that link to the ticket. And then obviously we gave her the portal URL.for her convenience. And then she should let you know if she runs into any other issues, right? Because I don't know why she got that message. But it's good for us to see this, you know, because you're going to run into things once in a while. And if she continues to have trouble,
Juan Martinez   38:06Okay.Okay, because eventually these things happens, no?
Kristin Krogman   38:14These things happen and if it does happen again, then we will.Um...We'll go to our next steps.
Juan Martinez   38:26Okay, I sent the message, the mail, sorry.
Kristin Krogman   38:30Yep.
Juan Martinez   38:32Ready, I'm waiting for Kimberly.
Kristin Krogman   38:34Yeah.Okay.Okay.Yes.Okay.Yeah.Okay, so yeah, that was what I wanted to show you was opening a ticket, which you did by yourself. Next time it'll be easier.
Juan Martinez   39:04K.Yes, yes, yes, open chicken.
Kristin Krogman   39:10You added her to the portal. You sent her the note on how to access and set up her credentials.
Juan Martinez   39:14Matthew.
Kristin Krogman   39:20All right, so you got that set up. You also saw earlier how we have to ask if someone should be in the portal when I sent that note to Ron saying, hey, you know, is this someone you want to have access? Because again, not every company wants.certain people in there looking at every ticket. They don't want people to have access to everything that's in there. So they have their own reasons for it. A lot of time it's just for control of who we're communicating with. They want us only communicating with certain people.You'll find there's other companies, they'll say whoever, right? And they have way too many people in there. They really shouldn't have so many, but they do. They don't care. They just whatever.
Juan Martinez   40:09Okay.
Kristin Krogman   40:11But we want to follow those processes. So do you have any questions about what we just did?
Juan Martinez   40:18No, just create the ticket and send the mail to the correct persons. I know, create the ticket, add to the organizations and the mail of the persons, send the mail and just say or pay attention to the response of.Of the the customer, yeah.
Kristin Krogman   40:39Yeah, and it'll it'll get easier.
Juan Martinez   40:41Well, and it's very important: copy the link, the direct link in the in the number of the ticket, yes, to.
Kristin Krogman   40:47Yes.
Juan Martinez   40:48Uh, to the persons can see the currently the the portal with the the ticket where that we created previously to.
Kristin Krogman   40:48Yes, and...Yeah, and and to give them the one under their name and not the one that gives like all the information for the, you know, the inside of the ticket. We don't want them. We want them to see.
Juan Martinez   40:57Two.Okay, the personal on the direct mail that I sent to Camila, yes, with the image.

## Call with Kristin Krogman — parte 6/7
_chunk 1634 · 2026-07-22 · fuente: Call with Kristin Krogman.docx_

Kristin Krogman   41:16Yeah.Yeah, you want to just, here, let me just make sure. So when I showed you how we got here, that we take that link instead of this link.
Juan Martinez   41:19Yeah.Yes.Right, OK.
Kristin Krogman   41:35Because this link shows them anything that's been put in internally, so you want to go from the other one.
Juan Martinez   41:43Yes, OK. I got it. I got it. This is very different, not Jr. is for us, and this leak is for the client, yeah.
Kristin Krogman   41:45Yeah.The.Yeah. And so this shows you too, this is what she sees. So this is what she sees with the ticket and they can look at the responses. While I'm here, I'm going to show you this too. You can get here as well. And I actually on my cheat sheet.
Juan Martinez   41:54The customer.Yes.
Kristin Krogman   42:11I have the information for this, but since we're right here, I'm going to show you. If I'm Kimberly and I come in here and I am looking for information. Let's say I want to see the release schedule, like when they're going to do the updates. I can go to search and I can just type in.Release.And it's going to show me release notices. Let's say I actually want to see the calendar. When is the next update?Alright, let's see, we should be able to get right to the calendar.Confluence. Let's look at release notes because I know you can type calendar and it'll take you right there too.Okay, let's do calendar.At least it's supposed to. Here we go.But this will also show them how-to articles. So they could come here and if they're looking for, you know, how do I update a fiscal calendar? Well, there's an article there, they can click on it and it'll take them to the wiki or the get books so that they can see it. So here's a user guide.
Juan Martinez   43:16Hey.
Kristin Krogman   43:32They can get to that link.Oh.
Juan Martinez   43:36K.
Kristin Krogman   43:38So fiscal calendars. It should have usually popped right up at the top though.Because this is just imports hard to articles. Why isn't it showing our actual?
Juan Martinez   43:50Yes, I remember the preview session. I see the calendar together.
Kristin Krogman   43:57Yeah, because you can we can get in another way too, but they should be able to just get in this way. What else would they call? How come that isn't popping up under releases?Oh, there.Release notes, maybe. No, we tried that already. Why isn't that showing up?Schedule.There we go. So, reschedule.
Juan Martinez   44:35Yeah.
Kristin Krogman   44:36is the calendar. Okay.Then you get here in the wiki.And now they can look up, okay, I want to see incident.And here's the information for, well, there's a, this is not up to date.Here's the calendar.So then you can see when all the releases were and when they are coming up. So next week, there's a release for both of them, incident and then secure. Always goes the second day.
Juan Martinez   45:0829.
Kristin Krogman   45:16on Wednesday and Thursday. So that's good to have to know when the releases are happening because also with the tickets.Tickets will get assigned back to the original assignee when a bug fix has happened so that they can test it and then reach out to the customer to say, hey, this has been done, it's been tested, and please validate on your end that everything's okay.
Juan Martinez   45:46Yeah.Okay, okay, great. Thanks.
Kristin Krogman   45:49Yeah, but yeah, just as far as managing things, it's nice to know when the next one is coming.
Juan Martinez   45:55Okay, Kristin, have you the link to engage portal? Remember that you told me about the create a request in IT help desk to engage portal? Try to send me a message, a mail that I have actually access, but I am not sure.
Kristin Krogman   46:16OK, let me grab that.Oh, where is it? Oops.Okay.Okay, portal.Let me put it in our chat.
Juan Martinez   46:37Okay.
Kristin Krogman   46:42and see if you can get it to pop up.
Juan Martinez   46:45Okay.
Kristin Krogman   46:46Yeah.
Juan Martinez   46:49So, you have to block it?Maybe, uh, um, I have...The BP and off.
Kristin Krogman   46:58Ohh, you have to do what you can on.
Juan Martinez   46:59Yeah.Let me change.I don't like the...In migrate the times we need to.Receive a notification for Microsoft Authenticator.To singing constantly to my my travel mail.
Kristin Krogman   47:29Yeah.To.It.So I think that's what you're going to have to put for your login ID, I think, for once you get it open.
Juan Martinez   47:46Yes.Okay, but refresh, refresh, can't reach up, yes, actually.Hey, what are my opinions?With that, see you.Remember me?Please remember you.
Kristin Krogman   48:15Yeah, please remember.
Juan Martinez   48:15Okay, actually I have a window with change retailer and no more like a reports operations and.Let me.
Kristin Krogman   48:25Can you share your screen and show me?
Juan Martinez   48:27Yeah.
Kristin Krogman   48:40Okay, let me take a picture of it.
Juan Martinez   48:44Okay.

## Call with Kristin Krogman — parte 7/7
_chunk 1635 · 2026-07-22 · fuente: Call with Kristin Krogman.docx_

Kristin Krogman   48:51Okay, what I'm going to do is for you.I'm gonna reach out to Marissa.And I'll take a picture of my dashboard and just ask her how we get that. Oh wait, she's, is she out? She might be out on vacation.
Juan Martinez   49:05Ah.No.
Kristin Krogman   49:12Yeah, no, not allowed.
Juan Martinez   49:13Ohh.
Kristin Krogman   49:16Let me think about it. I should be able to find someone else who can help. Otherwise, we might have to wait for her to come back on Monday, which is fine, because if something comes up with Engage, that, you know, we'll do a screen share and walk through it or whatever, right?
Juan Martinez   49:31It.
Kristin Krogman   49:35It'd be better if you did it and I watched, but if we have to, we can do it the other way.Let's see. Yeah, I think Nicole maybe knows how to do it. There's another person that works with Marissa now. And so I'll reach out to her and see if she knows how to give you those permissions, because I think it's going to be a permissions issue.
Juan Martinez   49:58Yeah.Yes.
Kristin Krogman   50:01So we'll see if we can get that taken care of.
Juan Martinez   50:06Okay.
Kristin Krogman   50:08Any other questions while you have me?
Juan Martinez   50:12Uh...Ah, yes, actually I have access to the help mail.Yeah, how come I configure this in my my?
Kristin Krogman   50:21Okay.
Juan Martinez   50:27In my mail and in Outlook, I don't know. I have access now.
Kristin Krogman   50:31Okay, you wanna show me?
Juan Martinez   50:31Because.And.Yes, here, added Juan. I should come back to help inbox, but, and after this, what what happened? How can I configure this the help inbox?
Kristin Krogman   50:50****, I think just...Um, have you, I'm just curious, I don't, let's see, that's one of your favorites.Let me look at mine.Because I'm...Okay.Go to Krogman.I'm wondering.On your inbox, it doesn't look like it, but do you have a dropdown on where it says inbox underneath your name? Okay, so that's all you've got there.
Juan Martinez   51:51Yes.
Kristin Krogman   51:52Is just for yours.Because mine just popped up.It's there it mine is down towards the bottom that you don't have like.
Juan Martinez   52:07I suppose that the maybe automatically appears here in this section, like a support help Appriss Retail. Maybe a refresh e-mail.
Kristin Krogman   52:14Yeah, that's what I'm wondering. Maybe, maybe you have to like refresh it or something.
Juan Martinez   52:20Okay.No.
Kristin Krogman   52:39What's what is your go-to groups?At on the.
Juan Martinez   52:45Go to group.
Kristin Krogman   52:46That's a, yeah, what is that?
Juan Martinez   52:50The Q release communications.
Kristin Krogman   52:52No.
Juan Martinez   52:542024
Kristin Krogman   52:56I don't want that.
Juan Martinez   53:00I don't know.
Kristin Krogman   53:06Huh.I would.Yeah.Because I will take a picture. Well, let's see. Yeah, I can take a picture.And show you.Mine.Okay, because the one at top up top, of course, I saved to favorites, but then mine just shows up down at the bottom, you know, under like a carrot thing.
Juan Martinez   53:47Okay.
Kristin Krogman   53:48So I don't know how that showed up there for me.
Juan Martinez detuvo la transcripción

## Call with Peyman Motlagh — parte 1/15
_chunk 1636 · 2026-08-11 · fuente: Call with Peyman Motlagh.docx_

Call with Peyman Motlagh-20260811_154639-Meeting Recording
11 de agosto de 2026, 8:46p.m.
2h 20m 59s
Juan Martinez inició la transcripción
Juan Martinez   0:04Okay.
Peyman Motlagh   0:05And we also, I don't know whether the first thing I'll, you know, I when I looked at this ticket here, let me share screen here.
Juan Martinez   0:17Because, okay.
Peyman Motlagh   0:18When I look at the screen here, I didn't pay attention to what everybody says here, okay? I just went in and looked at this ticket, okay? And, you know, just do this search that he, this person has done.I don't know, is this here? Maybe this one. If you do this search, you see they're going to look, you know, in location hierarchy two. For some reason, I don't know why they're going to two, but these are five conditions applied to item. This had previously not resulting in Cartesian effect, but after July 30th, it did.So what that tells me, look, anytime they run anything on product, okay, these are all coming from item, but really this is a product coming from product. So.That's what made me to go and look at the reference product. What we can do, you know, but I could be wrong, by the way. Don't go with what I say. Usually the best way is try to reproduce this.this run, okay? And the reason I'm not, you know, going with what Diego does, did, and he may be right, it's just that I don't want to make mistake and just follow what the way he says, you know, and then make a mistake at going the wrong way.Because this is what the client is showing us, all right? It's showing us these are all repeating. See this article IDs? They'll keep repeating.
Juan Martinez   1:52Jain.Yeah, yeah, yeah, because...
Peyman Motlagh   2:01Okay, and and this could be go ahead, sir.
Juan Martinez   2:05Because Diego analysis say the pipeline ran six times on the theory of July and left duplicate behind, yes? I checked it today and every product still had sadly 6 copies, no?
Peyman Motlagh   2:12Uh-huh.Uh-huh.Yes, and, and, and the reason, go ahead, go ahead, finish your talk, sir.
Juan Martinez   2:20Six copies, and here is the...I put a comment with the with the like an internal node because every row in that table has the same row created down to the milliseconds from today, for example, 8 million of them, yeah.
Peyman Motlagh   2:31Yes.
Juan Martinez   2:42So the table is not filling up over time. It gets replacing in one operation, and that single operation writes these copies of every product. This is the actual state.
Peyman Motlagh   2:48Exactly.Exactly, as you, as you, as I showed you and as you pointed out, this is what these these files come from the customer, so it is the customer who is duplicating these. That's my guess. OK, but this is a we can fix this.
Juan Martinez   3:09Okay, okay.
Peyman Motlagh   3:15Let's see if we can fix this. First, just going forward, we cannot go in and reprocess these transactions, you know what I mean? Because the receipt, I mean, the receipt doesn't show it, but maybe, maybe we, I mean, maybe we can. Hold on. Before I say anything, let me, let me just, and as you can see,They did a, I think Diego was rightfully asking where the, you know, we can go look at these searches, you know what I mean? But before we do that, when I looked at this in DBeaver.I'm sorry, in my workstation, I see six.files are sent. See that? And each one of them has a different time stamps. So the client probably something was wrong in their system and they send these files six times.
Juan Martinez   3:59No.
Peyman Motlagh   4:08OK, and so that could be the reason we see, like you know, what I did is I went in and look at, you know, run this query, OK, to get duplicates. I'm gonna put it in chat in case, in case you wanna look at it yourself.
Juan Martinez   4:09The.Okay, thanks.
Peyman Motlagh   4:27Of course, I can.Yeah, yeah, so let me just put it in here.Okay, so this is whenever you want to find duplicates, that's the best way to do it in Greenplum and even in Snowflake.So the reason I'm working, I'm solving Snowflake first is because usually this is, this client has a move to Snowtime. That means we first process everything in Green Plum and then we duplicate, we move the data to Snowflake.So if you fix Snowflake, but we don't fix this, next time it runs, it will cause problem. It will give you duplicates. So that's why I'm concentrating on this, on Green Plum. And as you can see, it runs on Green Plum 9 now.
Juan Martinez   5:26Nine, okay.
Peyman Motlagh   5:27How do you know it's running on Green Plum 9? That's what you asked me, am I right?
Juan Martinez   5:31Yes, yes, yes.

## Call with Peyman Motlagh — parte 2/15
_chunk 1637 · 2026-08-11 · fuente: Call with Peyman Motlagh.docx_

Peyman Motlagh   5:33I would go, you know, I would go to the pipeline, you know, this Azure pipeline here.Okay, I'm going to put this in the chat for you. So this is the Azure pipeline.What does that mean is that when you go here, you see all the jobs that are running. And if you can click here, that's the pipeline. And if you want to know how to get here, the best way is to go to Azure DataOps. You click on that, and you have three options. You see here.And the option you want to look is DataOps. This is essentially all ARDM stuff is running on. If you click on this one, you see the code, all the codes, okay?
Juan Martinez   6:12Yes.
Peyman Motlagh   6:25on the orange one. On the blue one, if you click on the blue one, you see the pipeline.
Juan Martinez   6:25Okay.
Peyman Motlagh   6:33All the pipelines are here and if you type in this was web client 11.One, two, am I right?And if you look here, it says GP9.
Juan Martinez   6:42All right.Ohh, okay, great, great.
Peyman Motlagh   6:48Okay, so the other way you can do this equal is AHL. You can, if you remember the.
Juan Martinez   6:49Yes.
Peyman Motlagh   6:55the abbreviation, it also works that way too. So you don't have to remember the number. Now, what if you don't remember, like, you know, I'm getting old, so I don't remember everything anymore. So what I do is I go to this location, and this is essentially you can.search by name of the company. So this is a home. See that here is AHL client 112 and is a SFTP puts it at least until recently is the data is coming through SFTP. And there's some more information here that.may not be accurate. For example, now they moved into, they're not CRDM anymore, they're actually GP. And so some of this information is old.A couple of bosses ago, who was really a good man, he created this. So I still use it, still active. People actually update it. So you can look at every client name. So what I'm going to do here, I'm going to give you a copy of this and put it in a chat.
Juan Martinez   8:06Yeah, is that coming really help me? Yeah.
Peyman Motlagh   8:06That's why I want to call you. That's why I want to call you, because I knew that you didn't get proper training by anybody. And this is the way to, I want you to have, I want you to succeed. That's my goal. You know, I want you to be able to do this work without my help.at all. So this is where you go, you know, like any client, you just type the name in there, make sure you don't, you know, mess up, mess up the spreadsheet. But yeah, just, you know, click here and give it a name and see if it's here. If it's not here, let me know. But that's how I get the names everywhere if I wanted to go to the, you know.
Juan Martinez   8:36Yeah.
Peyman Motlagh   8:49So with that said, that's how I get the, you know, that's how I find out that I have to go to GP9 and I have to go to client 112.And since I've been around, I actually know, you know, I created this little cheat sheet for myself and set, so that way I can just look here, I see GP6 here, these are all the client for GP6, this is GP9, GP3, you know, that's how I...
Juan Martinez   9:08Yeah.
Peyman Motlagh   9:20That's how I quickly go between, you know, and I know where things are most of the time, not all the time, because people change, people are changing things, at least for FireDM, that's what I've been doing. Okay, that said, so that's how I know I have to come here, and then I run this query, okay?And it tells me that, you know, article ID is a SKU number.
Juan Martinez   9:40K.
Peyman Motlagh   9:45And this tells me, and this reference product is a, let me do a better thing. This reference product is essentially gives the customer, customer send the specification for an item in their inventory, okay, or in their, is an item.Based, if you look at it, you know, let me just pull this one out, this.Now, do you have access to the viewer?
Juan Martinez   10:17Yeah, I have it.
Peyman Motlagh   10:19You have, and on DB, where did you connect to all these all these different machines?
Juan Martinez   10:26Hey, not all, maybe I actually just set up the GP09, but I don't have the other one.
Peyman Motlagh   10:33Okay.Yeah, let me show you how to do it quickly. OK, right-click here, right-click here, OK, and do copy.
Juan Martinez   10:37Okay, thanks.
Peyman Motlagh   10:44Okay, then come here and just click on the white space and then press paste. And now you have this copy. Now if you want to, you know, I don't want to create anything, but the first thing I do, I rename this something else. Let's say 9, you know, let's say I want to say.
Juan Martinez   10:57Yeah.

## Call with Peyman Motlagh — parte 3/15
_chunk 1638 · 2026-08-11 · fuente: Call with Peyman Motlagh.docx_

Peyman Motlagh   11:039 copy, I want to say 3 copy.Okay, so I just create it. Now, what I do is I right-click here, I do edit connection. Now, let's see, I want to change that to three. I go here and I put just three here. Everything else stays the same, my friend. You click here.And boom, it's connected. Now you have GP3 copy. See that? That easy. So that's how you quickly get these. Okay? So my suggestion is to create one for every one of them, except this one is different. The GP1 is the dev.
Juan Martinez   11:31Okay.Okay, great.
Peyman Motlagh   11:45and QA. If you look at this one, the difference is this says death. You see here.
Juan Martinez   11:52Yes, Dean.
Peyman Motlagh   11:52All the production one says Appriss.OK, so you can, you can, if you don't like to call it, if you want to remember this is a dev, you call it rename.
Juan Martinez   11:58Okay.
Peyman Motlagh   12:05And just put.Yes.And that way, you know, it's dead, and everything else is one moment.Okay, so now, now you know how to create these, am I right?
Juan Martinez   12:26Right, I got it, yes.
Peyman Motlagh   12:26Yes, no?You got it. Okay. And we are recording this so you can actually go and listen to it or have AI to create a document for you so you can refer to it. Okay. So now,
Juan Martinez   12:42Okay, okay.
Peyman Motlagh   12:46With that said, we run this query, okay? This is the reference product. We have also reference location and we have reference employee. Those are the three reference tables in PI RDM, okay?But in this case, we want to concentrate on reference product. And when I go to reference product and I search for this, notice that it has the article ID, which is essentially SKU value. So if we go to the ticket here,See.You see here this article ID? You see that?
Juan Martinez   13:28Okay.
Peyman Motlagh   13:30Okay, most probably this article ID comes from...This reference product.And how do I know that? Just experience. You can ask Claude, you can do, let me just say, let me just do something with Claude. Do you have Claude Cowork, my friend?
Juan Martinez   13:55Yes.
Peyman Motlagh   13:56Yeah, if you go to Cloud Corp Work and let's say...This is, this is RCS. What ticket is that? RCS.What was the ticket number?
Juan Martinez   14:09Only 077.
Peyman Motlagh   14:09Uh, 28 - no, no, 077 - OK.Do this a hold duplicate rows.All right.Could you review the?With code repository.No.Or the call ID.descriptions or playlist and then they are doing ID.Here.It is, yeah.The version of the report is the story. OK, so essentially I'm saying it where, where this article ID. OK, we look here.is looking at article ID and there's a description. You see here receipt description. So I'm essentially saying, hey, where is the...How the, how?I see description.So this you are.placed in ARDM item table, because I know this is coming from item table. And you would say, well, how do you know this item table, Peyman? If you go here and you see these are items, see here, item, item, this tells me the item table.
Juan Martinez   15:47Yeah.Ah, yes, yes, I can see.Okay.
Peyman Motlagh   16:01Now, let's go to OK. Now, I want to give it a repository where the code is, so I go here.and I want to go to the repository. Let me see here. If I go here and I know it's 121, I'm sorry, 112. In the repository, you know, how do you go to repository? You go Azure, you go to this middle one, you know, DataOps, and then orange one.And this is the R repository here. You just type in 112 or AHL. Either way will work. And then you go here, and now you can tell Claude that this is where the data is.where the repository is and let it go and see if it can find something for you.Okay.
Juan Martinez   17:07Okay.
Peyman Motlagh   17:10That, you know, that is that is one way to, when you don't know when payment is not around, you, you know, don't don't always start with the, you know, give it the RCS and say, you know, go and figure out what it is. And I know it's hard, but it just, you know, a little bit of looking at the code could help you.Quote a bit, and, as you learn, OK, so here it is, you see, just found it, is load script for item list. Let me do that.
Juan Martinez   17:32Okay.
Peyman Motlagh   17:43So, it's trying to read the ARDM one item, and since you know I've worked with this for many years, so I know it's an ARDM. You go to SQL, you go load ARDM scripts, and then you go load ARDM item. That's where it is, that's where the description is coming, and if I wanted to do it, you know, control F.You know, like, receive.And as you can see, the item receipt description. You see that here, my friend?
Juan Martinez   18:11Yes.
Peyman Motlagh   18:11That item receipt description is created by a join. You see here, is joining this receipt description from RP. If you look at the ticket, here is RP, you see here.
Juan Martinez   18:25Yes, yes, yes.

## Call with Peyman Motlagh — parte 4/15
_chunk 1639 · 2026-08-11 · fuente: Call with Peyman Motlagh.docx_

Peyman Motlagh   18:27So that's why I went to the reference product table.Now, I jumped through this because I sort of had experience with it. You know, that's why I sort of jumped and went all, you know, immediately into this table, because I've done it before. Okay, it's not a big deal. Now, let's see what this claude would tell us.See here.
Juan Martinez   19:12Yes.
Peyman Motlagh   19:13So, it found exactly what I found.Now, the problem is, my problem is here is that it doesn't give you the line number in code, so you can actually manually look at it.That's my...
Juan Martinez   19:31K.
Peyman Motlagh   19:49Um...Let's see what it says.You see here, you see the problem is finding read this.So I'll let you read it and then we can talk about it.
Juan Martinez   20:18Miss Ronald.Dreams new for for.
Peyman Motlagh   20:21It's a lot of things. Yeah, let me tell you what it does, because I'm a slow reader, terrible reader, slow reader. It takes me forever to read something. You see, what it's saying that there is nothing that makes this to be unique, you know what I mean, this article ID to be unique in this reference product.If the reference product master, which is reference product, has more than one row for the same UPC code, that differs in any other column.Reference by this thing keeps the, you know, keeps the row end up with two or more sharing the same article ID.Because what is happening, if you go back to the code, I want to show you in the code because that makes hopefully more sense. You see here, this RP here is joined, is joined by article ID. So if there are duplicate in this table, it would generate duplicateHere in this in this reference.ARDM item update.That's why the client sees multiple. Could be one reason. It doesn't mean that it is always that. But this could be the first thing I will check, the reference product. Now, you would say, well, how would I clean this up? You know, you know what I mean? That's reasonable, am I right?
Juan Martinez   21:47Is.
Peyman Motlagh   21:47The, the, the, before you modify any production table, so do not modify any production table unless you back it up manually. Unfortunately, you know, you have to be, we don't, we don't have a lot of guardrail to stop.people from doing the wrong thing. So what I, here's how I would, let's say I want to, I want to back this table up so I can clean it up, okay?
Juan Martinez   22:18K.
Peyman Motlagh   22:18All right, so what I do is I go to the ARDM 112.K.I find a reference product.And notice this is ref product. You don't want to go to ref product. You want to go to reference product. You see that?
Juan Martinez   22:42Yes.
Peyman Motlagh   22:43Is a ref, you know, so go to ref product.Right-click here, OK, right-click, and then...Generate SQL DLL.You gotta wait until it generates it, so for some reason it's taking its sweet time.Okay, so once you get there, you don't need to, you just click copy. My suggestion is to be just open a new.You know, page, and as you can see, I right-click on it and I say, "Do, you know, new SQL this, you see how it is?"
Juan Martinez   23:50Okay, yes.
Peyman Motlagh   23:51And that way it generates GP9. You got to make sure that you're in public, not on somebody else's machine.Okay.No, I hate.
Juan Martinez   24:02OK, Paul.
Peyman Motlagh   24:04Huh?Then I paste what I created here. So the way you want, you see anything, this is something that you don't know, but I'll tell you. If you call anything reference product and then anything after it, the code that Luke has written to copy,these reference product tables every day to Snowflake would think that this is a table that needs to copy. So you don't want to do that. You want to make sure that it's a backup, you know. So what you want to call it is EKUP under score, and then today date is 2026-08.OK, 11 and then under score. OK, so now you created a table.and you give this reference product that we know, somebody look at it, you know is a backup. Okay, so let's create that. Okay, I just created it. Now, let's populate this.
Juan Martinez   25:00Yeah.
Peyman Motlagh   25:08And how do I populate it? I populate by insert.Into, and this I want to insert into this this table.Select star from.This table.And what this query does is put all the rows that are here.In here.So now I backed up the horrible table. You see here, it has almost like 8 million records.
Juan Martinez   26:00Yes.

## Call with Peyman Motlagh — parte 5/15
_chunk 1640 · 2026-08-11 · fuente: Call with Peyman Motlagh.docx_

Peyman Motlagh   26:01See how big it is now, not that I created a backup, I just wanted to see just so select just to make sure that that is inserted.It is inserted because you know it's telling you that, but in case you you are doubting yourself.And you should just remember, 8.33 million, something like that. And if we run it, same thing, you see 8.33, whatever. So this is populated now, the backup is populated. Now we can work on the D.We can work on.deduping it. Am I right? So what I do is, there are multiple ways to do this, but the way, and again, you can use Claude to do all this stuff. This is just me because this is simple. I don't want to use Claude, you know what I mean? This is simple thing. So what I do is I say,First, I will now, why did I create it this way? Why did I create a backup this way? The reason I created a backup this way is because, as you can see, this table is defined a certain way, and I wanted to keep that all the...structure and permissions the same as the original table.Okay, that's why I created this way.There are many, many ways you can create tables, but that's why I choose to create it this way. Now, what I do is we can, you know, I'm going to do...I'm going to truncate, and this is really, you need to be really careful not to truncate production table, okay? So unless you back it up, don't ever use truncate anything in production or drop a table in production. Be very, very careful.
Juan Martinez   27:57Jain.
Peyman Motlagh   28:07So you want to do truncate table.I think is that.OK, so.Okay, I just truncated, see here.
Juan Martinez   28:24Ohh, yes.
Peyman Motlagh   28:25Now, I want to do insert into this table.Select.I wanted to...This changed.Okay.Distinct from.This table.Now, this works because these are all same thing, duplicated. You know what I mean?The reason this work is because it is, you know, everything is every line is duplicated, so let me just do this.
Juan Martinez   29:06Yes.
Peyman Motlagh   29:17OK, let me.Let me see if it worked.Okay, so to see if it works, I don't know it worked by the way. I think it didn't work.
Juan Martinez   29:23Okay.
Peyman Motlagh   29:29Um...I don't think it worked, my friend, but I'll double-check, see whether I got rid of it.Yep, it didn't work. See here? Still has the thing. So we need to find something about another way to do this.Let's just run this and see what we get.Let's just look at one of these. And by the way, if you want to pin this, you right-click here and pin tab, okay?And you can put that in there. Let's see what we get.
Juan Martinez   30:39Okay.
Peyman Motlagh   30:45So why this distinct doesn't work?Oh, look at that. Look at this here.
Juan Martinez   31:00Okay.
Peyman Motlagh   31:02See that you set up a date-time.Is different.
Juan Martinez   31:06Ohh, yes, yes.
Peyman Motlagh   31:08You see that? So, we have to find a different way to, you know, to do this, and a way to do this is 1 quick way is to select.This change.And we want to do article all IT, OK?And.
Juan Martinez   31:36Okay.
Peyman Motlagh   31:37Inserted data.Okay, and we want to go, I'm just testing this right now, okay?Store from.Then I just want to use where article ID called that.
Juan Martinez   32:10No.
Peyman Motlagh   32:15Order.Bye.Insert it.time extending. So what this does is, you see this, I'm going to pin this here just for you to demonstrate this. What this query does is essentially grab.Delete, you know, it it.It gives you everything, but is essentially put this, you know, whatever updated insert date time is the latest, it goes on top.Okay.
Juan Martinez   32:53Okay.

## Call with Peyman Motlagh — parte 6/15
_chunk 1641 · 2026-08-11 · fuente: Call with Peyman Motlagh.docx_

Peyman Motlagh   32:54And I think it should give you only one row because you're doing distinct based on this article ID and insert a date time. So if you look at this insert a date time, this is 26.31, 26, 30, 30, 26. So this is the one that should give us this row when I run this.If it works.Why did it not work?Nope, that's not it.Oh, I forgot the word on.Nope, absolutely.Oh, that's it.Ohh, I put the thing in the wrong way.Distinct on with here.You what?Try it again.Okay, let's try it again.So it put this one on top.But it didn't do what I wanted to do. I wanted to give me one article ID.Let me see.At least.Oh, maybe this way.No, that's not it.We can do it this way, too.This way, this way.I don't have time to. Let's do this.O, if we run this.He will give us the latest.And if we...If we just...Run it for everything.Why is it only giving me one?No, this doesn't work. That doesn't work.It has to be this way.Let's try this way.Okay, so this gives us a one, and if I remove this...And to this.And sorry, I need to...So now it should work.Insert into this.Why is it not working?Select Store.You miss?Oh, because of this. Damn it.Because of that, and...It should work now.Mm.Okay, got it. Sorry about that. Took me a little while to figure it out, but I did.I can just figure it out. So the reason I'm doing this is because I want to get the latest one, the top row. And now that I have the top row, I can remove this order.
Juan Martinez   43:21Aimee.
Peyman Motlagh   43:26OK, and I can do.Insert into, and I want to insert it into the ARDN reference part.Okay, so this will get the latest, only the top one, top row, and then put it into the reference products.Why is it having more than one expression?Oh, I know what.Why is this?Why is it giving me that?The first one I got ID.Let's do this.Let's see, select distinct is.How many rules do we have?OK.Now, I have the and I can now do this.Oh no, now it's worse. It's now 7. Used to be 6. What happened? Let's see.
Juan Martinez   45:02Yes.
Peyman Motlagh   45:13What happened here?We'll do that, OK.This gives you only one.Let's truncate the product reference product table. OK, reference product table does nothing. OK, now...If I run this, it should give me one.Am I right?Difference product.Let's do this.Okay, he only gave me one. That's what I wanted.Okay, now there's nothing in here.Empty. Okay, good.Now, if I remove this...It should be me only.The ones that they have.And if I do this.And if I do this, test.Yep, there's no duplicate you see here.No duplicates.Now, this is the Du.And now you have...And this is the in case you need it, because I always forget it. I have to struggle to find it.And this is the query to the Du.And now you have, now you have a reference product table.
Juan Martinez   47:10Jain.
Peyman Motlagh   47:15That is not, there's no duplicate in it. And this used to be 6, now there's one. Okay.No, if you go back, go ahead.
Juan Martinez   47:24Okay.
Peyman Motlagh   47:27Go ahead. Please say what we want to say.So if I go in, this was the client A-hole, am I right, 112?11.One, one, two.Oh, I am never... Okay, so let's see if we can...Do a search.And if I go here, change area, I think there's a ref, you know, product somewhere, product you see here, reference product.And if I do just...Particle ID equal and let's look at that.This one.Let's see if it gives us six of them.If it gives us six of them, we gotta wait a little bit until... Oh, it did give us six, unfortunately. So it hasn't really...It hasn't updated yet.Let's see.One, one, two.Uh, is the cache? Do you remember the cache? Remember the cache is?Here, that's permissions cache.Now, the other thing you want to check is whether this is calling from Snowflake or from Green Plum. So that's what we want to check. I go home.Yeah.112.And it is going for green plum, but I'm not sure is it going to snowflake too?What do you think?
Juan Martinez   50:19Yes.
Peyman Motlagh   50:20Yes means, yes means what? Is it, is it getting, is it getting the data from Snowflake or from Green Plum?
Juan Martinez   50:23No, Peter, is no, please, too.No, from from the implum.
Peyman Motlagh   50:32You think he's getting it from going flow? So why did it not update then?
Juan Martinez   50:33Yeah.

## Call with Peyman Motlagh — parte 7/15
_chunk 1642 · 2026-08-11 · fuente: Call with Peyman Motlagh.docx_

Peyman Motlagh   50:41Let's try it again.Gosh.Clear client has translation.Clear system cache.Okay, let's see if it works. Oh, choose a client, that's why.112Okay, let's go see if...He didn't urge.Come on.Why did it not purge?Cash for you, cash.Quiet.YouTube.So, I let's see if it worked.Didn't work.I don't think it worked.Oh, I'm still going in and getting the old thing.Let's try it.From the beginning.Change the area.Seth.That filter.Come on, man.And it doesn't have product description either.What is going on?It's.Reference product for this product, it should say one.Product description 3, product two, product description.It's in here. Why is it not getting it?Why is it not getting?See here.Is it a trigger I have to run something?Let's see.No, it's not here.It's not here.I have.Let's try it one more time.
Juan Martinez   57:58Yeah.
Peyman Motlagh   58:00I think so. I think it's.
Juan Martinez   58:00Sometimes, Kasha fixes a lot of things.
Peyman Motlagh   58:04Yeah, it's just, I think we've done the right thing. It's just a matter of getting the data.And let's grab something else.Nope, something is not right. Something is not right. And it must be the cache.
Juan Martinez   59:02No.
Peyman Motlagh   59:10There's no nothing else here that that.Let's see.One thing is, if you look at this query, this is the query that is running. Oh, I know what the problem is.The wait, the problem is that is this is querying the snowflake.
Juan Martinez   59:26Where is the Krogman?
Peyman Motlagh   59:33It's not coring the, um, the green from, so we need to do the DG in.Snowflake.In order to...Make that make this work. This is pointing to, so let me try doing that.Okay, so let's just...I wanna.Do I have Dale Hayes here?
Juan Martinez   1:00:20Do you like the white version?
Peyman Motlagh   1:00:22Hao.
Juan Martinez   1:00:24The wide version and screen, which is nothing.
Peyman Motlagh   1:00:26I do like, I, I, yeah, it bores me. It really bores me if I, I can't stand black.
Juan Martinez   1:00:37Yeah.
Peyman Motlagh   1:00:39I know most people are different. And I also like to create folder for all my searches.That way, I can keep them all.Russ, yes. Do you remember the name, the number? What was the?
Juan Martinez   1:00:56And...The number.
Peyman Motlagh   1:01:00Yeah, the RCS number.
Juan Martinez   1:01:03Yes, 28077.
Peyman Motlagh   1:01:07Like that?And...I wanna, okay, so let's see.Um...Okay, so...Database is.Here again, and then I want one, one, two.Let's do...Yes.I found this. Let's actually put those home in there.I should have just...Put it in there.The meal is taking forever. Green plum used to be fast.And now it's taking forever. Look at that.I don't even know is running and going plow or not.Oh, come on.It's ridiculous.Why are you unable to do it?What is wrong with this?Crazy.It is crazy. There was nothing wrong with that for...He is all six, that's why.See, from how I figured out is when I click on this query, it gives you the query that this application is sending towards the database, and this is not the query that...You know, if I run this in Greenplum.
Juan Martinez   1:05:21K.
Peyman Motlagh   1:05:24Do I run it here?See, that gives you 6.Yeah, so the duplicate is here.Let's see, um, let's see if we can duplicate this table.If I go here, what is that? Okay, if I go here.If I go to...You are being prod.If I go to...112You know.Reference product.One of these has a...One of these has a place that I can copy it and duplicate.I just don't remember where it is.How do I do this?Can I right click here? Let's see.Can I reload, save as? No, that's not it.Columns, lineage, data load, ohh, clone.And I want to call it 2026 to 811. OK, actually, I want to save that call.Okay.Reference, OK.
Juan Martinez   1:09:08For any type of change, the process is the same, no? Just create a backup, the table, it, it, there's the new code for Schick that actually works, and after copy to the base.
Peyman Motlagh   1:09:13I just created a backup.
Juan Martinez   1:09:25The database T.
Peyman Motlagh   1:09:28Say that again. Repeat, please. Please repeat.
Juan Martinez   1:09:33Always is the same process, no? You need to create a backup in the correct section or correct item.
Peyman Motlagh   1:09:41That's what I try to do usually. I try to create a backup.
Juan Martinez   1:09:45Yes.Not directly in the prediction, yeah, just in a backup, you verify that everything works, and after this, you can.
Peyman Motlagh   1:09:54And you.Drop tobacco.
Juan Martinez   1:09:57Good, OK.
Peyman Motlagh   1:09:58Yeah, you can, you can after that drop the backup, so now I let's just see whether we have.Select store from ARDM 112.But, OK, see.Should have said limit 10 or something, so...And if I do it here with this.Hello, Isa.If I put it here.And look for this product.You give me 6.I don't know what was wrong.
Juan Martinez   1:11:21Ha ha.
Peyman Motlagh   1:11:22Oh, oh, I know this is this has the database in it.

## Call with Peyman Motlagh — parte 8/15
_chunk 1643 · 2026-08-11 · fuente: Call with Peyman Motlagh.docx_

Juan Martinez   1:11:24Yes, or again, breath.
Peyman Motlagh   1:11:26Yeah.Yeah, so he gives you 6.And.Now, if I run this, I suppose...Would this work?Okay.I actually made a mistake. I should have not truncated, but that's okay. Hopefully I can run it fast and it's not going to deal with production.I should have been more careful.Let me see here.All right, now if I run this here.I will get one.Hola, now let's go look at the...
Juan Martinez   1:13:30Yes.
Peyman Motlagh   1:13:34Cancel.Go and.Let's just get outta here.Oh, it's cash.It is cached.That is impossible.You saw me purge my my.
Juan Martinez   1:15:38Yes, yes, it's very useful.
Peyman Motlagh   1:15:38Aimee.Okay, so let's try it. Let's see if it works. It is useful, but if it doesn't work, it's useless.
Juan Martinez   1:15:45I hope.
Peyman Motlagh   1:17:15Yep, see.
Juan Martinez   1:17:16Yeah.
Peyman Motlagh   1:17:19Now, why it doesn't give you, you know, give you product description? You can always go here and you see, look, and you can run this in.In Snowflake.
Juan Martinez   1:17:34Okay.
Peyman Motlagh   1:17:36And so if I go here.And run this.Because this is what the this is what what we get.See, product, yeah, the product description is empty, that's why it's not giving you a description.
Juan Martinez   1:17:54Golden.
Peyman Motlagh   1:18:05Okay.
Juan Martinez   1:18:06Okay, yes, I understand.
Peyman Motlagh   1:18:06No, so now let's go look at the ticket.Okay, so...These are some of the searches the customer has drawn.And we can try to go and see if we can, if we run this search and see what we get, okay? So we gotta go to public, you gotta go giant company search, and then look, look, refund giant Martinez, okay?
Juan Martinez   1:18:29Okay.Jain.
Peyman Motlagh   1:18:37So, let's keep that in mind.I want to go here.And this is public.You wanna go try and food search, alright?And because I don't remember it.Refund, join, refund, join, so DG and Company Search.
Juan Martinez   1:19:03Refiles.
Peyman Motlagh   1:19:11Dean join Company Search.Yes, right here.And you were looking for a refund.
Juan Martinez   1:19:19Play phone.
Peyman Motlagh   1:19:25Refund John Martin with charts or just refund John Martin? This one, this one.
Juan Martinez   1:19:29No, this.His Martinez, yeah.
Peyman Motlagh   1:19:33Yeah, let's see.Let's look at it, edit.So.Let's see what it does.So what do we do here? Let's see.Before you do that, let's see here.Let's go here. Let's go grab this query here.Okay, now I know where this is going. You see here? This tells me is hitting the green flow.
Juan Martinez   1:20:45Yes.
Peyman Motlagh   1:20:50that the other table was hitting snowflake. See how confusing it is.
Juan Martinez   1:20:54Yeah, it's not really confusing.
Peyman Motlagh   1:20:57Very confusing. This is now hitting green plum.I know that because Green Plum usually writes with CST.
Juan Martinez   1:21:08Okay.
Peyman Motlagh   1:21:09And CTE, I'm sorry, it creates a CTE and you don't, you don't, you don't see that in Snowflake.You don't see that in Snowflake. This is very much green plug.
Juan Martinez   1:21:24OK, very interested is a mixed client, no?
Peyman Motlagh   1:21:29In the, yeah, some of the you, it some of them hit different places, so you have to be careful. So, let me, let's see what does this person says.
Juan Martinez   1:21:31Hello.
Peyman Motlagh   1:22:03So when they run it, you know, I don't know what this means.
Juan Martinez   1:22:06Yes.
Peyman Motlagh   1:22:11Let's see what you said. Unfortunately, I'm seeing the same problem. To clarify, the problem isn't the summary level that shows total by store, but when I drill down into an individual store result to see the item refunded, here is the example. Even though only one item was refunded, it's listed 6.
Juan Martinez   1:22:32Fix.
Peyman Motlagh   1:22:35And do we know what stored it went to cache here? So went to store. Can you remember this and tell me what they are? These values here?Would you?
Juan Martinez   1:22:47No.
Peyman Motlagh   1:22:48Would you remember these? Can you go to the ticket and remember this? Give me these values.
Juan Martinez   1:22:57No, no, no, not really. Let me check.
Peyman Motlagh   1:23:00No, I'm asking, can you read the, keep this in your, open the ticket and then tell me, tell me these values when I ask you?
Juan Martinez   1:23:04Yes, I can read.Okay, on Deepa.
Peyman Motlagh   1:23:14Okay, so if I go here...
Juan Martinez   1:23:18Okay, long.
Peyman Motlagh   1:23:19What was the store number?
Juan Martinez   1:23:24The store is...22
Peyman Motlagh   1:23:26Actually, what's the store?
Juan Martinez   1:23:3120, 22, 7, or 227.
Peyman Motlagh   1:23:34Let me see here.327, huh? Let's see what... Okay.The store is 327. Of course, we don't have a store. The store number is 327. Let's see.Store 384.
Juan Martinez   1:23:54Apple, do you see other image? Let me check, because I...
Peyman Motlagh   1:24:00I'm looking at this one.

## Call with Peyman Motlagh — parte 9/15
_chunk 1644 · 2026-08-11 · fuente: Call with Peyman Motlagh.docx_

Juan Martinez   1:24:03Uh, Julie Juan.
Peyman Motlagh   1:24:09384.
Juan Martinez   1:24:12Yes, 384. Sorry, I see other image.
Peyman Motlagh   1:24:16That's okay, man. Don't worry about it.That store is not here, so...
Juan Martinez   1:24:22Ohh.White.
Peyman Motlagh   1:24:24Because I don't know, because this is just this search here. See, this is the search that she's running. She's running it, going to this thing, looking at the last 30 days, okay?
Juan Martinez   1:24:27The.Yeah.
Peyman Motlagh   1:24:39And it's checking this based on these condition. I don't know what these conditions are, so I when I run it, it gives me this this thing. Now, if I go here.
Juan Martinez   1:24:39Okay.
Peyman Motlagh   1:24:50and expand the results. Let's see what it does.Now, if it gives us duplicate, it's possible because...It is.Um...We still need to run it. I mean, maybe, maybe going forward, we just fixed it going forward. I'm not sure.Of course, this is such a large...Let's go look at something else. This is too big.
Juan Martinez   1:25:33But the start numbers here looks different than none.The clean side is just three numbers here, have 4 numbers and the store number, no?
Peyman Motlagh   1:25:46Uh-huh, I understand what you mean.But that means that doesn't mean anything. It means that the refund, see, this is looking for refunds. So those are, you know, those are the store refunded. That's new.Let's see, let's do past 60 days.Will take longer.That was the store, 384.
Juan Martinez   1:26:47384.
Peyman Motlagh   1:26:49Store 384, 715.I don't know why these are different. You're right. Two numbers are not the same.
Juan Martinez   1:27:09Yeah.I don't understand, Du.
Peyman Motlagh   1:27:15You know what I mean?
Juan Martinez   1:27:18Refund John Martinez.
Peyman Motlagh   1:27:27Huh.I don't know.Let's see, see, but she can, yeah.I don't know why the numbers are all...See you.
Juan Martinez   1:27:57No, all the stars here have 4 numbers. Any star have three.
Peyman Motlagh   1:28:01Yeah.Yep, something is not right.Everything starts with six, you see here.
Juan Martinez   1:28:10Yes, maybe 6, 6, three. Yeah, maybe.
Peyman Motlagh   1:28:11Ohh.6384.No.
Juan Martinez   1:28:18No, no.But it's the same panel, we found John Martinez, we found should be con in a moment.
Peyman Motlagh   1:28:38I don't know.
Juan Martinez   1:28:39I don't know what happened.No.
Peyman Motlagh   1:28:55Something makes no sense to me.Why, why is this 6 digit and this is a hole?
Juan Martinez   1:29:06Maybe in the ticket.
Peyman Motlagh   1:29:10Let's go to.
Juan Martinez   1:29:11We have the link in the next password, the site client.
Peyman Motlagh   1:29:15Uh-huh.Let's do that. Let's just put that in there. Giant food.
Juan Martinez   1:29:20Yeah, if only the last one.I know, yeah, the first one, the last one is Jain.
Peyman Motlagh   1:29:59Oh.
Juan Martinez   1:30:01Here is, but, but what is different?
Peyman Motlagh   1:30:01How in the world?
Juan Martinez   1:30:05Maybe in the settings after run the search, in the settings.
Peyman Motlagh   1:30:11I don't know.
Juan Martinez   1:30:19It's crazy.
Peyman Motlagh   1:30:21It is interesting.What was the article ID that was in the ticket?
Juan Martinez   1:30:39The article ID.
Peyman Motlagh   1:30:44Oh, transaction ID is this.
Juan Martinez   1:30:45For, for.Article or transaction?
Peyman Motlagh   1:30:50It doesn't matter one of one of them, whatever, because there is no article ID here.
Juan Martinez   1:30:55Yeah.
Peyman Motlagh   1:30:55So we should, let's we let's use transaction ID.And I'm lazy, I don't wanna, you know.
Juan Martinez   1:31:16What's faster?
Peyman Motlagh   1:31:17Huh?
Juan Martinez   1:31:19It's more faster than typing a number.
Peyman Motlagh   1:31:21Yeah, no, I'm a terrible typer. Anything I can do to not type. Anything I can do to not type, my friend. And I don't see transaction ID here. That's the problem. See here.
Juan Martinez   1:31:27Yeah.Yeah.Ah, yes.
Peyman Motlagh   1:31:38DG.So let's see if we can add transaction ID here.
Juan Martinez   1:31:50Yeah.
Peyman Motlagh   1:31:51Okay.And now I'll run it.What happened? Oh.To be here.Okay.And that is not even there, that transaction is not even there.You see?
Juan Martinez   1:32:29Yes.
Peyman Motlagh   1:32:29In this new search, that transaction ID is not there. There's no transaction ID. I don't know why. It's empty.
Juan Martinez   1:32:39Ohh.Ohh.Let me check.
Peyman Motlagh   1:32:48Receipt description.Oh, article ID 43. That's article ID.
Juan Martinez   1:32:56Yes, 43.
Peyman Motlagh   1:32:58Okay, so let's just go back.And let's remove this. Oh, this is from gift card. That's why. You got to remember, this is wrong.
Juan Martinez   1:33:15Yes, no, no good.
Peyman Motlagh   1:33:17You want a header?
Juan Martinez   1:33:18No, get, get hard.
Peyman Motlagh   1:33:21Yeah, you don't want to, yeah, you don't want to, and do you have article ID? Yes, they do have article ID, so let's run this.

## Call with Peyman Motlagh — parte 10/15
_chunk 1645 · 2026-08-11 · fuente: Call with Peyman Motlagh.docx_

Juan Martinez   1:33:21Sexual *******.
Peyman Motlagh   1:33:37Okay, now you're talking.And...Yep, only one. See here.
Juan Martinez   1:33:54This one. Oh, okay.
Peyman Motlagh   1:33:56You see that?
Juan Martinez   1:33:58Great.
Peyman Motlagh   1:33:58So, you can just get this.See that?
Juan Martinez   1:34:04Maybe, actually, I need to investigate why, yeah, the Sears.The clean search fonts, it's okay, but our search not found correctly, no?I don't know why.
Peyman Motlagh   1:34:19I don't know. I don't know why.
Juan Martinez   1:34:24What is something that I can check?
Peyman Motlagh   1:34:26Don't spend too much time on it. If you want to do it, do it.
Juan Martinez   1:34:27After.
Peyman Motlagh   1:34:32I'm going to put this in the chat for you. You can respond to the client, okay?Say, we, we, so you think that we fixed this?
Juan Martinez   1:34:38Okay.
Peyman Motlagh   1:34:46Just send this to the customer, say, we think we fixed this issue. This was had to do with, you know, tell them that it has to do with this.We, you know, your, your, your, your company is sending multiple.And we can actually...Modify the code.in the reference product to only grab the latest file. You see what I mean?
Juan Martinez   1:35:17Okay.
Peyman Motlagh   1:35:19Maybe if we do that, then in future if they do this, it wouldn't cause problem.
Juan Martinez   1:35:26Yes, yes, of course.
Peyman Motlagh   1:35:28Okay, that would be something to do. Okay.Okay, let me see.One sent of multiple.No.Sorry, it took me a little while to get it right, but we got it.
Juan Martinez   1:36:49No words.Um...Bryant.
Peyman Motlagh   1:37:21So, if we add this distinct, see here...
Juan Martinez   1:37:25Yes.
Peyman Motlagh   1:37:26It would then grab the latest file you see here.
Juan Martinez   1:37:31Okay.Our priest was following, okay?
Peyman Motlagh   1:37:39So.Ohh.Okay, so let's keep that in mind.Okay, so raw product master.And it just puts in.Reference very distinct.The sweetness.I think this customer used UPC code and both we take it and we make it an article ID.
Juan Martinez   1:39:14Okay.One 60 yet at the Rumford.
Peyman Motlagh   1:39:33You tell Luke was there.Go, go, go, go see Mommy, go see Susan.Okay.Let's see.Alright, what I am going to do is this: Have you done this before?That's right.Save the context.Oh, I can.No to.Let's see.A lot of times I start with my computer, my desktop context, and then desktop, you know, not context, but cloud, and then I move, you know, I need to do some code change, and I don't feel comfortable to do code change here.So I'll take it to my workstation and I continue working from my workstation.
Juan Martinez   1:40:42No, okay.
Peyman Motlagh   1:40:44And that's what I'm doing right now. So let me close this here. If I go here.And I have some things that worked here.I am going to...Okay, so I'm going to just close this.I'm going to open Cloud CLI.Actually, before I do that, let me see what client is that. This is client 112. Oh, okay. I have 112 here.So let me make sure that 112, what I'm doing right now is trying to make sure that client 112, I have the latest repo. So what I'm doing, I pull, I create a pull request because I have a branch called dev PM. See if you look at branches.
Juan Martinez   1:41:37Okay.
Peyman Motlagh   1:41:45I have a branch called Dev PM, so I'm going to go ahead and...you know, make sure that Dev PM is in sync with production. So I'm going to create a pull request.And I'm going to go to from production to dev PM. See they're the same. See here.So another way, my branch is exactly what it is in production. So I don't need to do anything.I don't need to create a pull request.Okay, so if I go to my...
Juan Martinez   1:42:23Okay.
Peyman Motlagh   1:42:25I use GitHub Desktop because it's easier, but you can use anything you want. If I fetch it, then I know that this branch of, it has the latest. My local branch has the latest. Okay, now I synced up.I can essentially...Open.Open white Jr.OK, and...What I have done is I actually put cloud code here on PyCharm as an extension, so it makes it life easier for me a little bit, I suppose. Now, what I do is I go to...Where was I?I go to my cloud code, see it's already put this here.I will show in the folder.I copy this.And I just put it in temp at 112 here.Okay, and I just...Tell Claude.Ah.I don't know, if you know a better way to do it, tell me. This is how I do it. Doesn't mean it's right, you know.
Juan Martinez   1:44:00Okay.
Peyman Motlagh   1:44:03Um...I want to continue my work.You can want that.context.Yeah.I'll let it read.Do you use Cloud CLI or you just use Cloud? How do you how do you use Cloud?
Juan Martinez   1:44:48Always CLAI.
Peyman Motlagh   1:44:51You always see, you see a lie. Good for you. But you never used it like this.Ohh.
Juan Martinez   1:45:04but usually is general, I use a CLA. It's more useful, it's more clear. And like a developer, I feel more comfortable with CLA.

## Call with Peyman Motlagh — parte 11/15
_chunk 1646 · 2026-08-11 · fuente: Call with Peyman Motlagh.docx_

Peyman Motlagh   1:45:11So, you...Sure, so you do it, you do it here like this.
Juan Martinez   1:45:19Yeah, yeah, I like, I like this bit.
Peyman Motlagh   1:45:20Okay.No, no, I understand. I mean, I was thinking about using that.Does this make sense to you? What I've done so far? You follow, you follow what I've done.
Juan Martinez   1:46:06Yes.Yeah, yes, I understand. It's very interesting because I I never seen all the all the process for for try to fix this type of problem and and now it's really clear for me the for follow the workflow is.
Peyman Motlagh   1:46:18Mmh.Yes.
Juan Martinez   1:46:27Spiritual and and this record is maybe the base to create a guide for the new faults in the in the team.
Peyman Motlagh   1:46:35Yes, yes, yes, yes. And if you need help again, come back. That's why I ask you to, that's why I ask you to call and let's make, you know, I know English is not your first language and it may be hard. I mean, I can't speak Spanish at all.
Juan Martinez   1:46:41Yeah.No call.
Peyman Motlagh   1:46:55So, I'm useless. At least you can speak more than more than I do. OK, so what is saying that isn't unique and so on?
Juan Martinez   1:46:59Yeah.
Peyman Motlagh   1:47:06All right, replace product distinct build line 1 to 87 and so on. Okay, so if I go here...I go to MRDM.And if I go to SQL and if I go load ARDM script, then if I go to reference C reference one, that's the code.
Juan Martinez   1:47:29Yes.
Peyman Motlagh   1:47:32OK, so there is a distinct here.Somebody tried to create a distinct.But it's not working, you see here.
Juan Martinez   1:47:44Mm.It's different, no?
Peyman Motlagh   1:47:52Yeah.So.If I go to Claude.
Juan Martinez   1:48:34Now, sometimes it doesn't work like a expected.
Peyman Motlagh   1:48:38Mhm.Yeah.But you see exactly what I expected to do.
Juan Martinez   1:48:47Right now is the change is up.
Peyman Motlagh   1:48:50For me, the change is ugly, you said?What, what?
Juan Martinez   1:48:53Actually, yes.
Peyman Motlagh   1:48:55You, you, what did you say? The changes what?
Juan Martinez   1:48:59Was ugly, ugly.Right now, in the in the console, I see the actually it looks like the real solution, the real fix.
Peyman Motlagh   1:49:09Yeah, this is a real fix.
Juan Martinez   1:49:12No, yes.
Peyman Motlagh   1:49:16Okay, so...Now, I don't trust this, you know what I mean? That this would work. Well, because I haven't tested it.
Juan Martinez   1:49:24Yes.
Peyman Motlagh   1:49:30You know what I'm saying? So, the way to test this, we need, we can, we need to test this.
Juan Martinez   1:49:30Okay. Yes.
Peyman Motlagh   1:49:37And for me to test it, I usually do in QA, I run it on GP1. So the first thing you want to do, you want to go to use this virtual environment. I don't know, you set yourself up, but...
Juan Martinez   1:49:38Okay.Ohh, OK.
Peyman Motlagh   1:49:56This is a common Python that we use for all ARDN. OK, and it is located in this, you know, I set that up.
Juan Martinez   1:50:02Okay.
Peyman Motlagh   1:50:10And.I can, I can tomorrow, if you call me, I can show you how to run this, run the code and test this code in prior DMGP1.
Juan Martinez   1:50:20Yeah.Please, yes.
Peyman Motlagh   1:50:24Do you want to do that?
Juan Martinez   1:50:25Yes, I need this call.
Peyman Motlagh   1:50:26Okay, so.Yeah, sure. Before we go, I'm just going to connect to GP1 here.And this is how you connect it. You go to, you click here, you see here. And this is, this is, you can use, you know, VS Code if you want, but this is, this is, this is easier when you use, I'm so used to using PyCharm. That's why. So if you go to source, if you go to green plum,
Juan Martinez   1:50:38Yes.
Peyman Motlagh   1:50:58Okay, I always, because I want to go to GP1, GP1, I always color these my my my different instances, if it's if it's dev or GP, this is GP1, I always make it green, okay? And...
Juan Martinez   1:51:16Okay.
Peyman Motlagh   1:51:18I put GP1.And...And this is there, but...You see, that's what I change it, test it.Okay, now I am connecting to GP1. See that? And I can use dev and I want to go to client 112. So I'll go ARDM 112.
Juan Martinez   1:51:40Yes.
Peyman Motlagh   1:51:51Okay, I don't know if you saw that or not, but that's why you know you click here, you click on dev, and then you pick the, you know, you want to always pick ARDM, and then you also want to use T-log, and the reason I do T-log is because most of the initial code goes to T-log before it gets.Course.Okay, so now it's going to do its thing and if I go schema dev.and public, that's what I want. And if I do select store from ARDN.To that.And these are all the instances that run, you know, runs by RDM in dev. This is the dev instance. I also want to create a production instance, so I go to, again, green plum, and this time I give it a, you know, rose color.And notice that they were on GP9, all right?I think it was, yeah, I think it was in GP9.
Juan Martinez   1:53:08Okay.
Peyman Motlagh   1:53:14Then.

## Call with Peyman Motlagh — parte 12/15
_chunk 1647 · 2026-08-11 · fuente: Call with Peyman Motlagh.docx_

Juan Martinez   1:53:14Right.
Peyman Motlagh   1:53:22And here is...Appriss.Okay.OK, and I'll do the same thing here. I want to go to...Appriss.I want to go to.112 and T log.
Juan Martinez   1:53:53You know.
Peyman Motlagh   1:53:54One, one, two.So now I have, you see, you see here, this green kernel means what to me? Means it's deaf.
Juan Martinez   1:54:09Okay.
Peyman Motlagh   1:54:09This one, this one means production. You see how nicely the colors do it for you?
Juan Martinez   1:54:15Yeah, Green Production and no Green Death and Rose Corp Production, yeah.
Peyman Motlagh   1:54:21Exactly, you see here, GP1 dev and this.
Juan Martinez   1:54:24Yeah.
Peyman Motlagh   1:54:26And now I have settled my thing. Tomorrow, I'm going to show you how to run PI RDM.
Juan Martinez   1:54:35Okay, okay.
Peyman Motlagh   1:54:35Okay, because it's getting late and I'm tired. I don't want to tell you. I've been up since like 4 in the morning, so it's hard for me to concentrate.
Juan Martinez   1:54:39Ohh.Okay, no worries. Yes, okay.
Peyman Motlagh   1:54:46So.So you good with this picture? You good with everything so far?
Juan Martinez   1:54:52Yes, yes, a lot. Thanks Peyman for the time for take this call and explain me all the process because it's very useful for me. I need this.
Peyman Motlagh   1:54:55Up.
Juan Martinez   1:55:10Yeah, yeah, yeah, sure.
Peyman Motlagh   1:55:13Once you, you know, tell them, you know, tell them to set, you know, go in and have them set things up.
Juan Martinez   1:55:19OKOK, thanks for.
Peyman Motlagh   1:55:20Okay, so they understand and you understand. If you explain it to them, you will learn something as well.
Juan Martinez   1:55:25Yes.For now, I told you that the ticket, I need to respond the client to the client to the customer, yeah.
Peyman Motlagh   1:55:36Yep, yep, you respond to the client.
Juan Martinez   1:55:38And I have a question, a little question, sorry. You send me a screenshot for the Nike ticket.
Peyman Motlagh   1:55:50This one?
Juan Martinez   1:55:52Yeah, uh, up.
Peyman Motlagh   1:55:54Let me see.This one, this this Nike ticket. OK, and let's see what I what I say. Yeah, go ahead.
Juan Martinez   1:56:00I just have a question, because in the...
Peyman Motlagh   1:56:05This one, yeah.
Juan Martinez   1:56:07No, no, no, no, no, no up.Scroll, scroll up the image of the recipe, this this one, yeah.
Peyman Motlagh   1:56:17This one.Okay.
Juan Martinez   1:56:22The other one, the...
Peyman Motlagh   1:56:24This one?
Juan Martinez   1:56:25No, no, no, scroll down, sorry, just in the receipt in the night receipt, yeah, yes, and the final of the...
Peyman Motlagh   1:56:31This, this one. Uh huh.
Juan Martinez   1:56:39Number of the store, name of the store.The we have a null.
Peyman Motlagh   1:56:47Oh, you talking about this? No.
Juan Martinez   1:56:49Yeah.Yeah.
Peyman Motlagh   1:56:51OK, this is similar thing if you, if you go to the customer, you see, if the this is the store, you know, this null is coming from what? This is the address.Okay, this is the address. Am I right? If you go, I mean, my suggestion, if I can go to this transaction.
Juan Martinez   1:57:08Okay.
Peyman Motlagh   1:57:17OK, go to this transaction and and I I set up cloud to to see do this.
Juan Martinez   1:57:18Okay.
Peyman Motlagh   1:57:26I have set up Claude to look for, I call it,Find.The 4.RT.On this receipts, so...And I define what I define the scale called four-part key. You don't have to worry about it, but you can create it yourself. It's so easy. Essentially, four-part key is date, store, register. OK, so as soon as I give the give me four-part key, it goes in here and gives me this.
Juan Martinez   1:58:02Ohh.
Peyman Motlagh   1:58:07or part.You can see that 225115105 and then 8726. So see 2026 0807 25 and that's the four part key. So when I take this, I can go into here, go to.
Juan Martinez   1:58:14Okay.Okay.
Peyman Motlagh   1:58:29I think this is GP 11, so I better go to DB over here. And if I go here and get the, I have something called four part key and paste the four part key here.Okay, so now for this is client 67.I'm a terrible typer, so anytime I can create a shortcut to help me write things, I'll do it. You know, you know what I mean? I'm a terrible typer. I cannot type if my life depended on it. It's just, it makes it very tiresome for people to watch me.
Juan Martinez   1:59:19OKOK, babe.
Peyman Motlagh   1:59:31So what I do is I just...I do whatever I can to make things faster.
Juan Martinez   1:59:37Yes, yes.
Peyman Motlagh   1:59:38Minimum amount of typing for me.
Juan Martinez   1:59:42Yes, right now I understand why you prefer the video call, the call and not just text in the chat.

## Call with Peyman Motlagh — parte 13/15
_chunk 1648 · 2026-08-11 · fuente: Call with Peyman Motlagh.docx_

Peyman Motlagh   1:59:50Yeah, well, exactly. It just takes too much effort to type. And what I could show you, what I showed you in this hour of your talking to each other is almost like I should have, I could have written a book in chat. I mean, that makes no sense, you know what I mean?
Juan Martinez   1:59:55Yeah.Yes.
Peyman Motlagh   2:00:23I got what I want to tell you, but I'm sorry.Oh, oh, you wanted to know why the the the thing is null.
Juan Martinez   2:00:33Yeah.
Peyman Motlagh   2:00:33The.
Juan Martinez   2:00:35Because actually have the 319 of their 994 address have this null.
Peyman Motlagh   2:00:46Okay, so if you look at, again, this is addressed, okay? So you need to go to the reference location.Because that's where the data is coming from.See, the reference location.And that is a store, I mean location ID 2506.Oh, it's right here.If you go to reference location 2506Yeah.
Juan Martinez   2:01:23Jain.
Peyman Motlagh   2:01:23You see, this, let me cancel this because it's taking too long. We don't need to have it. If you click here.And you get address.Where is that address coming from? It's right here.
Juan Martinez   2:01:40Yes.
Peyman Motlagh   2:01:41So, the one that they provided, the street.Null is what they provided us.
Juan Martinez   2:01:47Yeah, no.
Peyman Motlagh   2:01:50Let me give you a quick understanding. If you go to here, if you go to P ingest, that's most of the data is coming from to P ingest. If you go to client 67.
Juan Martinez   2:01:50Mmh.
Peyman Motlagh   2:02:02And go to archive, go to production, go to today.And, you know, if you look at...Here, there is a...something called location or product master, something like that.
Juan Martinez   2:02:22Yeah.
Peyman Motlagh   2:02:22And that's the file that, let me see.Let me use location here.Okay.
Juan Martinez   2:02:41Vagina slang.
Peyman Motlagh   2:02:48Ohh.What do they call it?I got to eyeball it.Just the employee.
Juan Martinez   2:03:08Ohh.
Peyman Motlagh   2:03:10Oh, I know what the problem is. They went to, it's not in here. They went to, they went to BLOB. We get their location from the BLOB and this is what we get from there. If they fix this, that's what, that's what I, that's what I told the customer.
Juan Martinez   2:03:24Mm.
Peyman Motlagh   2:03:29If they fix this information from the BLOB, it will give them the right answer.You see what I mean?
Juan Martinez   2:03:36Okay, yes.
Peyman Motlagh   2:03:38So, when when the data goes into the BLOB, then gets then populates this. OK, if they remove the null from that information, it would not show, it would it would be OK.Because if you go, if you go to the ticket.
Juan Martinez   2:03:53Okay.
Peyman Motlagh   2:04:07You see, this is not good. You know why? Because what was the one before it?You know, you know what I'm saying?What was, you know, what is that? What was before? Because it's not clear to me when she's when he says I've added the last data from API and we have the same outcome as as shared before. What we, you know, share it again. What do you, what's the problem?
Juan Martinez   2:04:18Yes, yes.
Peyman Motlagh   2:04:37And as you can see, when you go and look at the, you know, here, see, back then they didn't even have a shipping address. You see that?
Juan Martinez   2:04:46Yes, empty.
Peyman Motlagh   2:04:48Empty, so...My suggestion to you is that...Here, let me, you know, my suggestion to you is.So, that's what I would say is that you, OK, what, which I mean, I don't, I don't have time, you know, what report, what does this report mean? Message Joe Hafi.You know what I mean?
Juan Martinez   2:05:34Yes.
Peyman Motlagh   2:05:35What, what is that? How can you do that?How would you know, how can you find all the stores globally? I think Sebastian had a way to do that, but I'm not sure which one.Right now, in this table, I'm a little bit confused in this table.
Juan Martinez   2:05:55Because.I, I checked, I wanted to know when this table that we have a fresh data, like Joel is the name, I know, and inserted at the time on reference location says for August, but on released product in the same schema it says 2021.
Peyman Motlagh   2:06:05Yeah.Ohh, where let me let let let me are you are you talking about this this table reference location?
Juan Martinez   2:06:17Right.No, not, not really, no.
Peyman Motlagh   2:06:26Show me, show me, my friend. Show me. Can you show me or?
Juan Martinez   2:06:28Let me, yes, yes, let me find the...The my screen.
Peyman Motlagh   2:06:36Yeah, sure.Take your time.
Juan Martinez   2:06:40Air.Screen.
Peyman Motlagh   2:06:42Okay.
Juan Martinez   2:06:45Here, yes, I do snowflake and the first one.
Peyman Motlagh   2:06:47One moment, sir.Uh-huh.Mm-hmm.
Juan Martinez   2:06:55Um...An observation is this.
Peyman Motlagh   2:06:58That's OK.
Juan Martinez   2:07:05I have the, I just tried to verify the, sorry, sorry, sorry, is this, this, sorry, my bad.
Peyman Motlagh   2:07:14No, no, take your time.

## Call with Peyman Motlagh — parte 14/15
_chunk 1649 · 2026-08-11 · fuente: Call with Peyman Motlagh.docx_

Juan Martinez   2:07:18I do a lot of queries today here. This is our reference product location.
Peyman Motlagh   2:07:19Yeah, yeah.Okay, so it it that that that that doesn't necessarily mean thatThat was updated on 8.4.It could be.Okay, it could be that it was up in the 900 and 994 were updated because it's possible that they're sending us incremental. They don't send us, they don't replace the entire reference location.Okay, so there are some clients replace the entire reference location and store file every time. Some clients just give you daily basis as they find it necessary.
Juan Martinez   2:07:53Mm.OKOK, I got it. Yeah, I understand.
Peyman Motlagh   2:08:10So...So, you know, for example, if I, you know, this is reference location here.
Juan Martinez   2:08:18Yes.
Peyman Motlagh   2:08:18And if you know updated date time is different, you know, this is 622.
Juan Martinez   2:08:27Yes.
Peyman Motlagh   2:08:29Okay, 84, you see that?
Juan Martinez   2:08:31A4.
Peyman Motlagh   2:08:33Yeah, so for this store.For this store, let me pin this.
Juan Martinez   2:08:42But are you sharing your screen or just tell me?
Peyman Motlagh   2:08:45No, oh, so sorry, so sorry. Yes, I need to share my screen. I apologize. So you see here, this is for everything, for reference, all the reference locations. You see here, some of them have a location, open date, location, close date. Some of the update date, you see here.So they open and close all the time, everywhere.So, if the information is null somewhere here.
Juan Martinez   2:09:09Hey.
Peyman Motlagh   2:09:15If the address is null, is because that's what they put in here.And this information, if you look at the ticket, what's her name, Sebastian, mentions this.So, if you read the read the message that Sebastian wrote, is that if they if they fix this data, everything is fixed.
Juan Martinez   2:09:30Okay.
Peyman Motlagh   2:09:44It's up to them.
Juan Martinez   2:09:47Okay.Okay, okay. Okay. Yes.
Peyman Motlagh   2:09:51So, the question is, you know, my question to him is...You know, what do you mean updated the report?You know what I mean? Do you want me to write the message to him?
Juan Martinez   2:10:08Yes.Okay, see, yes, thanks.
Peyman Motlagh   2:10:14No, you're good.
Juan Martinez   2:10:24But the principal issue.Maybe.We can write back to the to the client, and the issue appears to fix it for.Or, no.
Peyman Motlagh   2:10:42Why not?
Juan Martinez   2:10:45No, yes, it's fixed, yes.
Peyman Motlagh   2:11:18Let me.
Juan Martinez   2:11:20For the solution of the.
Peyman Motlagh   2:11:41And the other thing is that, let me see here, let me go to there.Uh, sixty-seven.Nike.Come on, if you go to here, if you go to history, not history, if you go to ARDM.iPhone.Unload.Scott Production.
Juan Martinez   2:12:49How much time do you have doing this to Appriss?
Peyman Motlagh   2:12:52Pardon me?
Juan Martinez   2:12:53Yeah.
Peyman Motlagh   2:12:54How, how much time?
Juan Martinez   2:12:56How much time, yeah?
Peyman Motlagh   2:12:58How much time do I have with the apparis?
Juan Martinez   2:13:01Yeah, working on operator.
Peyman Motlagh   2:13:03Uh, I probably until December.My last day is in the summer.
Juan Martinez   2:13:13No, no, no, no, but your experience with Appriss, how much years you have working?
Peyman Motlagh   2:13:17Oh, I've been here, this is 13 year.This is my 13th year.
Juan Martinez   2:13:23Two 13 years? Ohh, this is a lot of time.
Peyman Motlagh   2:13:27Yeah.
Juan Martinez   2:13:28Man, this is playing a lot of things because you are like a master doing a lot of process.
Peyman Motlagh   2:13:28Yeah, yeah.I'm not a master, I'm just, no, no, far from it, honestly. There are a lot more smarter people than me here in this company. Far more.Oh, okay. So this is the location where the Avro file is.See, we grabbed the data from the W.S.W.S.2 production, and then...That's where we get the data.From the blog.You, you follow me?
Juan Martinez   2:14:12Okay, yes, yes, yes.
Peyman Motlagh   2:14:14So if you go to WS2PRD, you can see the, let me see if I can go over there.Could be this one.WS2PRD. WS2PRD.
Juan Martinez   2:14:50In the list.
Peyman Motlagh   2:14:56never used to impurity.
Juan Martinez   2:15:02Did, did you?
Peyman Motlagh   2:15:03In log, this is the log.
Juan Martinez   2:15:06Dean.The teared, no? The teared.
Peyman Motlagh   2:15:15I don't know which one it is.
Juan Martinez   2:15:20And.
Peyman Motlagh   2:15:22It's not this one.
Juan Martinez   2:15:24Not is the tears that.
Peyman Motlagh   2:15:26Let me see.
Juan Martinez   2:15:32Is this?
Peyman Motlagh   2:15:33This one?
Juan Martinez   2:15:35Yeah, PRD is positional that, uh, that, uh, W is too.
Peyman Motlagh   2:15:37Let's see, let's see.Let's see if this is the one.This doesn't look right to me.That doesn't look right to me.This is you, this is you, you see here.Is that EU?No, this is not it.Yeah, this could be it.identity.
Juan Martinez   2:16:49Ronald.

## Call with Peyman Motlagh — parte 15/15
_chunk 1650 · 2026-08-11 · fuente: Call with Peyman Motlagh.docx_

Peyman Motlagh   2:16:51Store.Yeah, yeah.To the log.Oh, man.So annoying.
Juan Martinez   2:19:28Well, if we can find it, we can see this tomorrow. No worries. Because actually, the two tickets are fixed right now.
Peyman Motlagh   2:19:33Yeah, no, just, yep, I think we should do this tomorrow.
Juan Martinez   2:19:42Yeah.
Peyman Motlagh   2:19:42Okay, anyway.We will find out exactly tomorrow where it's coming from so we can grab the data.
Juan Martinez   2:19:52Yeah.
Peyman Motlagh   2:19:52I think Sebastian did that on his own, so...
Juan Martinez   2:19:56Yeah, but Sebastian's come back to the next Tuesday, maybe.
Peyman Motlagh   2:20:03Okay. Yeah, he was, he was ill. What happened to him?
Juan Martinez   2:20:04Because...He was sick.
Peyman Motlagh   2:20:08Yeah, he was sick.
Juan Martinez   2:20:10He was sick and have a medical.Problem and maybe don't come back to the next week, maybe Tuesday, because the Monday is another holiday here in Colombia.
Peyman Motlagh   2:20:16Issue.Oh.TRE.OK, well.You know, we'll get it done. No problem.
Juan Martinez   2:20:39Yeah, well, I prefer to send the message, the comments to the two tickets. Thanks for your help, Peyman, and tomorrow maybe we can have other call and learn a lot of things.
Peyman Motlagh   2:20:47Yeah.Of course.OK, have a good day.
Juan Martinez   2:20:57Have a good day, the rest of the day. Thanks very much.
Peyman Motlagh   2:20:59You're welcome, sir.
Juan Martinez detuvo la transcripción

## Llamada con Kiran Vadday — parte 1/9
_chunk 1651 · 2026-08-03 · fuente: Llamada con Kiran Vadday.docx_

Llamada con Kiran Vadday-20260803_160939-Grabación de la reunión
3 de agosto de 2026, 9:09p.m.
56m 13s
Juan Martinez inició la transcripción
Juan Martinez   0:03Yeah, got it.
Kiran Vadday   0:06Not to.
Juan Martinez   0:06We.I have this question because I recently have a meeting with Jacob and the customer and I need just to clarify this process or if I need to do something different or something new relation I will just take it for move forward and advance or put comments currently in the meeting.internal comments in the tickets for the other people, the other folks knows the actual situation or have a more clear perspective about this.
Kiran Vadday   0:40So sorry, I'm been typing. Sorry. Oh, share your screen and then we can go over ticket by ticket.
Juan Martinez   0:48Okay, review ticket by ticket.
Kiran Vadday   0:52Did you put, okay, so you want me to share my screen or your screen?
Juan Martinez   0:57Your screen, because I, I don't know what happened with my teams, but no, as usual, but I can share, I, I can share, I need to OK.
Kiran Vadday   1:01Oh, okay. No worries. No, no worries. So we are going with RCS 28135. Let me open that and quickly share my screen so that we both can see what I'm talking about.
Juan Martinez   1:11Okay.
Kiran Vadday   1:16Okay, so this is an old ticket and I guess there was something new coming from this. What is that?
Juan Martinez   1:25Yeah.
Kiran Vadday   1:26Okay, this is Augusta. Thank you. Oh.What's the question again? When trying to assign case to a new user, some users are duplicated in the user table with an incorrect, for example, Jeffrey Hayes. Jeff has one. Yes, we did that because these guys had the same e-mail address for different users. So in order to get rid of the migration process, we had to duplicate the e-mail addresses.
Juan Martinez   1:55Okay.
Kiran Vadday   1:55Yeah, so what do you what is the problem? Why are they caring about two e-mail addresses? They have one e-mail address per account, so why aren't they logging in with that one is the question.
Juan Martinez   2:08Yeah, yeah, the question, or just we...
Kiran Vadday   2:12So, whoever they think...
Juan Martinez   2:12We need to, we have the permissions to disable or is something about the...
Kiran Vadday   2:17Okay, let's go to them. So you are on this, so let's go to, they can do it themselves, but I'll, because we are here, so we can, this is a loser, right? I mean, a hold, right? Okay, so I will show you right away how to do that. Or do I even know, like, like, it's like your side even I'm new, so I...
Juan Martinez   2:29Yeah.
Kiran Vadday   2:39There should be something under the users and we can figure it out.
Juan Martinez   2:43Okay.
Kiran Vadday   2:43So these guys had the same e-mail address for like because incident side we we I love like K Vadde or Juan Martinez, right? You can be like J Martinez, right? So if you once and you can be J Martinez or Martinez J different login IDs are possible for you, but your e-mail address is the same thing because you are trying to log in as store manager as.supervisor and as somebody else in the old system, right? So that's why the login IDs are unique, but the e-mail address has been same. But coming to me when I'm migrating stuff, I'm only caring about e-mail address. So J Martinez, Martinez J or JM, everything has a same e-mail address. So I am picking one.
Juan Martinez   3:09Game.
Kiran Vadday   3:25the actual e-mail address and brought in the other two as J. Martinez 1, J. Martinez 2, and so on, because the migration would break in between if I don't have unique e-mail addresses, right? So that's where this whole duplication of things came in. So if any e-mail is bad, just Jeffrey, I think I have to go all the way.Jeffrey, because they have way too many people.That is not enough. Jeffrey Pearson. Oh, right. Not Jeffrey Pearson.
Juan Martinez   3:52A lot of jcaps.
Kiran Vadday   3:59Okay, so that is good. This is bad. Let's go into this one.Now let's figure it out. I know this page, so okay. Nothing here says Disabled, right? Permission groups, not hierarchies is also not the place. User teams, nope. Secure incident, nope. Advanced properties, nope.Yeah, there is nothing. Oh, I hate this. There is nothing that disables. I think they have to give us a list of people whom they want to disable and we can disable all of them.
Juan Martinez   4:33Yeah.
Kiran Vadday   4:40It's a simple database, Disabled equals to one or two. There is a column in membership to users where there is a disabled column. And I can disable them for, but that shouldn't be like a priority priority. So.If that is the only person or but they are trying it appears that some users are duplicated in the user table.With an incorrect e-mail address.
Juan Martinez   5:09Yeah, he's approximately 297.
Kiran Vadday   5:20It is OK.

## Llamada con Kiran Vadday — parte 2/9
_chunk 1652 · 2026-08-03 · fuente: Llamada con Kiran Vadday.docx_

Juan Martinez   5:20But I, I'm not sure if all all is duplicate, no, because maybe one person have one number in the e-mail, but no, it's duplicate, no, I...
Kiran Vadday   5:29I am with you Juan on that. I'm with you. I'm with you. That's why we need a list, a definitive list of the sure short people that we want to, what do you mean we want to do that? So why is the LP user tape?
Juan Martinez   5:32Yeah.Yeah.
Kiran Vadday   5:48Oh, okay.Taking too much time on this one, but I just want to look at.LP User.I had to change password this weekend and it's annoying because I keep typing the old one.
Juan Martinez   6:06Mmh.
Kiran Vadday   6:06Let's see if I got the right one or the wrong one.
Juan Martinez   6:10Okay.
Kiran Vadday   6:10While this is going on, let's see.Okay, there we are. And this is a hold. A hold is 441.Would be really nice if every ticket comes up with the client ID. Okay, 441. I'm already on 441. This is 441.This is also 441. OK, OK, let let me sync. OK, this is staging though.Good thing I took a second to look at it. Oh, 41.Out all from I'll do incident dot.Of the user, because this is where they are getting duplicates.Oh, users.Select all from membership.But users were.User ID equals.Okay, where is incident user ID?So they are also seeing this because it's in the LPUs of year one.
Juan Martinez   8:41Okay.
Kiran Vadday   8:41Yeah, yeah, so you see how the password is default password. If you see H24, it's like the default password. So for them to be Disabled, this is membership.Wait a second, do we have...Yeah, so if you see this membership dot users.There is a Disabled column.But I wonder why they are not giving it out for users to make somebody Disabled. Yeah.So, if I change that to one.This won't come up in the view.For example, OK, we can do it right now because we know that, uh, that's so, for example, as we are trying to, it appears that some are duplicate in the user table with an example, Jeffrey Harris.So which one is the right one? How do I know?Because this is about wait a second.From membership dot to users where e-mail equals.So that is 1 already. So if the password for this person changed, then that means this is the.right person.This person also has the default password.
Juan Martinez   10:34Okay.
Kiran Vadday   10:36I mean, I am simply going by login, but if they are sure which one is the right one, then I can disable the.You know what? I think I can dissemble the...Jeffrey Pearson, one e-mail address. I say that with confidence because as a person previously, you are trying to log in yourself multiple different ways only because you are setting yourself up for different security levels.So you're trying to log in with C. Martinez, or sorry, J. Martinez for admin. And if you wanted to test something as a, you know, store manager, you know, you can do that yourself by creating an extra login and do it. So that was the main reason why these guys had so many different logins, because they want to set up different things differently, just to see, you know, who has what access.But now in secure, your platform unification, we are not allowing any such kind. You have to create a new e-mail address, not just login, because there is nothing called a new login. Any new login is a new e-mail address. So this person was no longer what he thinks he is. He is now only one person that is with the right e-mail ID, and the right e-mail ID is always Jeffrey dot Pierce.Right, so anything with ones, twos, and threes, I think can be set to Disabled equals to one. I can write up a script and...
Juan Martinez   11:53Right.
Kiran Vadday   12:03Save that and but I need confirmation which is the right one. No, I don't think I need a confirmation that was because any person the one twos and threes are by me. I did that.
Juan Martinez   12:0810.
Kiran Vadday   12:18Unless I am not sure if there is any person, like for example, their actual e-mail address ended in one, then I might ruin it.That's a possible danger because I will only add ones, twos, and threes only if there are duplicate e-mail addresses of that person. If Juan Martin.Martin is 1 at Appress Retail is only one e-mail address across one database, Appress Retail, then it's not duplicate. It came in nicely without issues.
Juan Martinez   12:47Okay, have some noise.
Kiran Vadday   12:47So there is no way for me to know which is the right one, which is a not valid one.Fax.But...I can do account where, you know, if there is one dot Martinez.And Juan Martinez one, then one is the duplicate one, but if there is only one e-mail address, Juan Martinez.One, that is not in duplicate because there is no e-mail address without the one, no e-mail address with two, right?
Juan Martinez   13:21Yes.
Kiran Vadday   13:22So I think I can write a script for this, but we need time. I mean, this is not like priority one. At least we have some game plan, right?
Juan Martinez   13:31Okay.

## Llamada con Kiran Vadday — parte 3/9
_chunk 1653 · 2026-08-03 · fuente: Llamada con Kiran Vadday.docx_

Kiran Vadday   13:32Yeah, so in the whole thing is we'll discuss and we'll enter the notes and we can pick it up when we get time, okay? So for this, can you please add the note saying Kiran is going to come up with a script where she will disable the same disabled column from membership dot users.
Juan Martinez   13:40Okay.
Kiran Vadday   13:53That one I showed you just now, where's that column? Disabled, I think it's right in the front. Yeah.Disabled. Disabled column will be set to 1 for the users with e-mail addresses.which are duplicating. I think that should be enough. No need to mention it's one, two, three, unless you have the time and patience to do things.
Juan Martinez   14:15Okay.
Kiran Vadday   14:18So, so yeah, so then I can come up with the script, save the script, so if any client comes forward saying, hey, this is causing issues because we are seeing duplicates, then we can send rerun the scripts and say bye bye to them.
Juan Martinez   14:33Okay, okay, sure.
Kiran Vadday   14:35Or, you know, the easier way is giving some feasibility in here. Oh, there is! There is one!
Juan Martinez   14:45We only need to scroll down.
Kiran Vadday   14:47Yeah.We wasted time, I'm sorry. There is Disabled.You see this?
Juan Martinez   14:54Yes, yes, yes, I see.
Kiran Vadday   14:56You want to take a screenshot and so that you can add it to your teams or you want me to take a screenshot and add it to this chat so that you can copy whenever you want.
Juan Martinez   15:00Yeah.
Kiran Vadday   15:05So that they can decide.
Juan Martinez   15:05Yes.
Kiran Vadday   15:11But if it still, it should not come because the LP user view is smart enough, but if it comes.Okay, I am adding this to chat. But good discussion though.Okay, next one.
Juan Martinez   15:31Then this one is.
Kiran Vadday   15:32I seriously did not see it. I just went back and forth and did not realize it's there.
Juan Martinez   15:38Yeah.
Kiran Vadday   15:39So yeah, it's like the very top e-mail user details and Disabled. So once they click this and that user is gone, bye bye.And easy, yeah, so, but before that, yeah, so Pearson one can go bye bye. Ohh, OK, what's the next one? Let me open the chat again.Today, the this I did not get what location filters here and.Is this for sleep?
Juan Martinez   16:05And is.
Kiran Vadday   16:10Oh, a hold, so that should be fine. Okay, so, okay.This is resolved, so what are we discussing this far?
Juan Martinez   16:28The filters don't not found correctly today.
Kiran Vadday   16:33Like, okay, guide me through this then, Juan. Okay.
Juan Martinez   16:33Maybe one, one hour ago, and...
Kiran Vadday   16:38Where should I go?
Juan Martinez   16:42To the client name, sorry, let me go to them.To the link.I go to the Control Panel and enter to with the client.
Kiran Vadday   16:57Yeah, so once I'm already on a hold, so I'm wondering where in this are we filtering?
Juan Martinez   17:02Hi, sorry, yes, let's go.
Kiran Vadday   17:04Yeah, I'm already on Adusa, yeah.
Juan Martinez   17:07Yeah, yeah, yeah, sorry, sorry, just use the location filter to create a incidentals, whatever, and put, for example, I don't know.
Kiran Vadday   17:18Oh, you want me to go to secure incident? Let me go to secure incident.OK, so create a new incident.
Juan Martinez   17:32Yeah, and use the location filter.
Kiran Vadday   17:35Yeah, yeah, yeah, I'm with you now, and...What do you want me to?
Juan Martinez   17:46Put 000 lion through lion, the first the first one.
Kiran Vadday   17:52Okay.
Juan Martinez   17:54and see the results with this filter.
Kiran Vadday   17:59Okay.Am I doing the right thing? You mean these case classes or the incident types?
Juan Martinez   18:14And.Let me confirm here in my notes.
Kiran Vadday   18:19Okay, yeah, yeah, take your time.
Juan Martinez   18:20For, for, for find the exactly the error exactly.
Kiran Vadday   18:24Okay.No worries.
Juan Martinez   18:48Sorry, we need to go admin and manage associate associates. No, not here, sorry. Yeah, my bad.
Kiran Vadday   18:56Sorry, admin, oh, okay, admin and no worries, admin and...And then?
Juan Martinez   19:07Manage associates.
Kiran Vadday   19:09Manage associates. I don't have manage. I have never seen manage associates. Which section or manage audits you mean?Where did you, where did you? Is there a screenshot, Juan?
Juan Martinez   19:27Yeah, sure. I tried to find the screenshot. Let me one moment.
Kiran Vadday   19:32Age Associates.Today, I don't even know.
Juan Martinez   19:36Is this one?Yeah, I put the image in the chat, but the name, yes, is Manage Associates.
Kiran Vadday   19:51Okay.I see only my, okay, you're typing in, okay.Manage employees dot ASPX.So that must be employee on the, sorry, we are so bad at naming our stuff. So on the admin levels, it's employees.And managers.
Juan Martinez   20:24Ah, okay, employees.
Kiran Vadday   20:25So that's just like, okay, okay, so the state, sorry, location filter.

## Llamada con Kiran Vadday — parte 4/9
_chunk 1654 · 2026-08-03 · fuente: Llamada con Kiran Vadday.docx_

Juan Martinez   20:32Uh...Bran is Food Lion in Bran.
Kiran Vadday   20:37Oh, okay, I have to put that too. Okay, where is Bran? Okay, FFFF Food Lion LLC, just one. Okay, and click on the locations.
Juan Martinez   20:48Location is 0001.
Kiran Vadday   21:0000.Oh, 3 zeros and one.
Juan Martinez   21:04Three zeros and one, yeah.
Kiran Vadday   21:07Okay, search.Nothing's coming.
Juan Martinez   21:13But brandies appear.
Kiran Vadday   21:15Nothing's coming up for 000.
Juan Martinez   21:19But Brandon.
Kiran Vadday   21:23Oh, I did not enter anything for the brand. Okay, let me...
Juan Martinez   21:23It's empty.
Kiran Vadday   21:26At.Okay, you mean store lookup? Oh, oops. Okay. Now I'm going to enter brand and then...
Juan Martinez   21:38Good lion.
Kiran Vadday   21:38Food line, and then search, OK.So you're saying for the store lookup, when you enter the brand, okay.
Juan Martinez   21:48Yeah, and you see the 715 results.Any filter is was applied.Yeah, 101.
Kiran Vadday   22:04What? Exactly, 1,142. So the problem is what?
Juan Martinez   22:16Did the filter, yeah, yeah, yeah.
Kiran Vadday   22:16It should be much smaller, much smaller values. But everything is Food Lion and the brand is correct. Are you thinking it's getting duplicated? I don't see any.
Juan Martinez   22:29Because I see in the in the call.
Kiran Vadday   22:30Let me go to, let me go to page one.See, 001, 6, 10, 14, 13. I don't see any duplication. Juan, let me go to page 21. Let's see.
Juan Martinez   22:44Okay.
Kiran Vadday   22:47It's 2026, 27. Yeah, there is no duplication.That's fine.
Juan Martinez   22:53But if you, if you, if you put full lion and the numbers location just for review one location.
Kiran Vadday   22:59Okay, so okay, yeah, yeah, that is correct. Triple 01, let's do it.It's taking a second, I guess.So, okay, in the manage employees to look up your main. I get only one.Juan.
Juan Martinez   23:21Wow, in the COLLETT, I...
Kiran Vadday   23:22Give me some other store number.Let me try it because this is the first one you said 0011 tried with.Nothing for 0011. Okay, any other store number?
Juan Martinez   23:38No, not really. The example is what I watch with the...
Kiran Vadday   23:43Yeah, but...
Juan Martinez   23:43Zero 0011.Hum.
Kiran Vadday   23:48So, as for manage employees, it is unique.
Juan Martinez   23:54Full line 0 citizens.I don't know, and the screenshot looks different, like in your screen, because you put 00000 on one and slash full lion, but here just see the numbers.
Kiran Vadday   24:02Maybe it's fixed.Yeah.
Juan Martinez   24:12I don't know what happened.
Kiran Vadday   24:15Yeah, try again, but this looks fine to me. Food lion and 0001. That's all I'm typing. And in a second, I think I'll get back the results. The slowness, yeah. Okay, yeah, I'm getting only one for now.
Juan Martinez   24:33Employees? Yeah, I don't know.What happened? Because if you see the screenshot, is the same filter, the same brand, the same number, but the results was 750.
Kiran Vadday   24:47Oh, this is directly, okay, wait a second. This is directly in the search. I am in the store search. So let me grab this. So.So I put in, okay, wait, let me check your screenshot filters. Employee ID, nothing is there. Brand Food Lion and these two, okay. So I have Brand Food Lion and location. Let me search. So I'm in the store, should search like this one.Now, we have many results.Ta-da.But there is no way to know, so...But that is all the things for location 001. How do we know which is duplicated? Don't think these are duplicated. They have different names on this.Different first name, last name.
Juan Martinez   25:45Just last names, I have other screen sharing, I think, fine, and the other page is the same.
Kiran Vadday   25:50Let me.Wait.
Juan Martinez   25:52For example, I don't know, Dave 13, 14.
Kiran Vadday   25:57Sorry, which one are you talking about?
Juan Martinez   25:59Other, other page.
Kiran Vadday   26:00So even in here, this is also good. Yeah, they are 001, but the first name is different, last name is different, and their departments are different. So it's bringing all the records belonging to 001 location, which is right.And that is what it should bring, 000001. The location has to be the same across all the filters and we are getting all the records belonging to that store.
Juan Martinez   26:27Okay, okay. Maybe I misunderstand the road or I.
Kiran Vadday   26:28Yeah.Yeah, yeah, yeah. So for the brand Food Lion and location 001, these are all the employees existing, I guess.One is a part-time, one is a full-time, etc. is given here and these are the employees working for them.Fur brand.Food lion and 001 location.
Juan Martinez   26:57Yeah, yeah, maybe it's my my bad my mistake.
Kiran Vadday   26:59Let us see Stop and Shop because I'm curious because even Stop and Shop has 0001.
Juan Martinez   27:05I have the notes, the Jr. note is like a...Is this been 2893? Yeah, ticket.
Kiran Vadday   27:15Yeah.

## Llamada con Kiran Vadday — parte 5/9
_chunk 1655 · 2026-08-03 · fuente: Llamada con Kiran Vadday.docx_

Juan Martinez   27:18And a ticket says.
Kiran Vadday   27:18Not this, I guess, sorry.93, yep.
Juan Martinez   27:21Um...
Kiran Vadday   27:26But this does not talk about employees though, 2893, does it?
Juan Martinez   27:30Because the description is 1 employee series has applied within a case, employees from store 0001 for layout and stop and shop appear with the ability to select from either brand. Previously, the selection was restricted to each brand.
Kiran Vadday   27:44But this is fixed. This is behind the scenes something.No, yeah, yeah, I get, yeah, I can see that point, so employee search.Oh, when an employee searches are applied within a case, within a case in the sense.
Juan Martinez   28:02Is in.And also broken inside the case as well as when an admin searches. Yeah.
Kiran Vadday   28:10You.Not like an admin search. I'll show you. So for that, what you will have to test is...What will you search for? Okay, you know what's the best way to find this?I'm all around the places.Let's open admin.Sometimes you can look at the incident.K-step configuration.Let's go to search here. I'm trying to do 2 things. One is case log on. Sometimes by employee, they are adding employee, right? So maybe we can find out in cases like.theft, threat, these kind of cases have the high probable internal theft, right? Internal theft are most because it needs employees to be entered, right? Internal theft is, you're saying somebody within the company stole this, right? So there will be a very good chance thatit has employee control in it. So we have to find out incidents like that and see if there is like even operational issue, right? Because it needs employee ID, who's, what is the operational issue, who first identified it.stuff, stuff like that. So even with those, there is a good chance.Internal dishonesty. So associate dishonesty. Perfect. That's the kind of, okay. So incident type.This one.Search.We'll go in, so my whole approach here is to trying to find out the where there is an employee field in a case because they did not give us any case saying, hey, here is a case. These are the kind of things that are really helpful for one. Whenever they say something like that, can you say like, hey, can you please give us the URL of the incident you're tiring?or you know, yeah, which incident can you give us the link to the workbench that you're trying? All we need is this. Once we get this, and it would be really nice if they point out even internally these links too. So the more information, the better, right? We can immediately go to that page and be like, okay, this is where they're trying and we can try it ourselves.
Juan Martinez   30:38Ohh, okay, yeah.Okay, okay, okay, I got it.
Kiran Vadday   31:02Rather than us figuring out, you know, oh, employee ID, which case, what case.
Juan Martinez   31:09And.
Kiran Vadday   31:09Okay, do you see any employee fields here? Let me know. I am going through as well, but...My eyes are only as good as they are right now, so I don't see anything. Okay, this page is useless. I didn't find key dates and times, basic information, e-commerce.Employee ID, it clearly says employee here, so somewhere. If it doesn't, that's fine.His details does not have it. Maybe.
Juan Martinez   31:47How much do you have? How much do you have with Abriz?
Kiran Vadday   31:52More like 4 years easily, Juan.
Juan Martinez   31:55Wash. Okay. I see you have a lot of practice to navigate in different sections.
Kiran Vadday   32:00Yeah.Exactly right. It's a habit. Yeah. Once you get into it, you will realize like the tricks and tips what might be useful, right? It's on.
Juan Martinez   32:13Yeah, it's like a practice, no, just with the time, practice, and...
Kiran Vadday   32:18Exactly, exactly. You look at 10 different cases and then you're like, oh, I need this part. It would be nice if somebody gives me this.
Juan Martinez   32:26Yeah, sure.
Kiran Vadday   32:28Okay, let's see persons involved, if that helps. Yeah, see, we are wasting time in figuring. So if she had given us an incident or a case or anything, that would have been really helpful. So that we can directly go to that case or incident, click on the workbench link is much more best. It's the best because you log in and use that link and you are inside the.
Juan Martinez   32:41Yeah.
Kiran Vadday   32:50actual workbench and a little more details will help us. Like click this link, go here. Okay, associate ID. Okay, I'm with you here, Juan. So what's that thing? So let's try and see. What are they saying?So, when a search employee search is applied within a case employee store for Foodland and store up with the ability to.Okay, employee ID.Okay, location is what they were complaining, right?
Juan Martinez   33:23Hang on.

## Llamada con Kiran Vadday — parte 6/9
_chunk 1656 · 2026-08-03 · fuente: Llamada con Kiran Vadday.docx_

Kiran Vadday   33:25Search.There is no brand here. Oh, thank God there is Food Lion.Yeah, we need more information. Like, okay, when an employee search is applied within a case, what case? Where?Employees from stores for Food Lion and stuff.So she is saying that there is no brand here. Oh, God.We don't have a brand in this one to realize who or what.Yeah.We need examples for that one. That would really help us. I believe them, but need more details so that we can tweak our stuff, right?
Juan Martinez   34:36Okay.
Kiran Vadday   34:37Yeah, so because I typed in, so this is the employee associate that she's talking about. What she is trying to say is, for example, this David is for, should not be coming for Food Lion because this David belongs to Stop and Shop, something along those lines. So we need screenshots and exact details.cases where she's seeing and thinking. That way we can refer to them and see if what she's saying is right or wrong, stuff like that. Because employees and platform unification have nothing to do.At least before we were at least on the LP user level, but the LP user is fixed. Every employee is now perfectly synced. They should not be seeing this either. First, can you say, hey, this is resolved and to which they did not respond yet.Hey, can you please verify and let us know if this is still an issue? If not, can you please send us the case that you're talking about or any screen where you're seeing the employee is repeating itself? Any screenshots or a sample example would really help kind of situation.
Juan Martinez   35:51Okay, okay, thanks. Very easy for this information.
Kiran Vadday   35:52Yeah, so for, yeah, because right now we have been in two different places and everything seems fine to me. And yes, there were initial issues with LP user view and because we did not get that synced and it syncs now and employees has nothing to do with anything else and it should be fine.
Juan Martinez   36:13Okay, okay.
Kiran Vadday   36:14It should work as expected, yep.
Juan Martinez   36:16In this case, we need more details, maybe in from the client, yeah?
Kiran Vadday   36:19Yeah, yeah. First, let confirm if that's still an issue, and if it is, then give us the example of the ones that they're thinking an issue is, and with the, you know, case name or workbench detail, a sample example of a working like, like, you know, Amanda Barahuna of Food Lion should not exist in this search forstop and shop or something. So those kind of examples really help us to look into the table and realize it. But we didn't touch employees. You know, this is not actually user temple. Associate lookup actually looks into the employee table and we did nothing to employee table. So I highly doubt how this is an issue.
Juan Martinez   36:58Okay, okay, okay. Hang on.
Kiran Vadday   36:59Yeah, but just giving them a benefit because yes, the LP user also has employees in it, you know, just giving them the benefit of doubt. But again, if they have anything, yes, we are always here to resolve it, but we need more examples right now. But by the looks of what you just saw, even the employee associate lookup looked fine, right?
Juan Martinez   37:20Okay.
Kiran Vadday   37:21Yeah, so that's that. We are good so far. Now moving on to the...My God.
Juan Martinez   37:31It's a little message in the channel.Chen.
Kiran Vadday   37:35Active audits is also failing. I have got just simply refresh the screen. You should be good.Where is it?Where is your comment? Have you really come this far?Oh boy, okay.
Juan Martinez   37:56Do you think that the timeout errors, we can fix it, really? It depends for, I don't know, other people, because we have a lot of tickets with the same error and the same things. Yeah.
Kiran Vadday   38:09Exactly right, so we sync that time out with, we sync that time out with secure, so we used to do 300 minutes, you know, in the old NetTrack, but secure guys do it 30 minutes, so when we platform unified, we did not app, I'll be honest, NetTrack is not the major pro app of everything, right?The secure, engage, EBR, these are like top-notch apps and everything is in secure side. So we went and sat with them. So you won't dictate rules to them, right? You will keep your mods, you will adapt to them, like, you know. So we took what secure said the time, secure logs off every 30 minutes.
Juan Martinez   38:43Hmm.
Kiran Vadday   38:54And our NetTrack users are not used to logging out in 30 minutes. So either increase the time for NetTrack, keep it separate from secure, or I don't know what they'll do. Please test exports for ISN are using, yeah, I need a specific room. Okay, this one, what's the...
Juan Martinez   38:59Yeah.

## Llamada con Kiran Vadday — parte 7/9
_chunk 1657 · 2026-08-03 · fuente: Llamada con Kiran Vadday.docx_

Kiran Vadday   39:14Okay, this one, it's, let's test it. A hold using a sender might be, oh, all our Del Jesus issues, good. So I don't need to log out and log back in. Let's go to system select.I'm gonna close this.Okay, nope.I'm going to close this as well and go to system cell reports. So one is an export issue, right? Unable to use eyes under.Time outs, time outs, I have no clue.Aizenda, what is this? Unable to use Aizenda. I think they both go hand in hand.OK, so far is loading up fine. What was your question about?Previous preview works, but the CSV export fails. Does the export use a different endpoint? Yeah, if the CSV export fails with a separate issue, we'll deal with it.Later, for example.Because first if we get the timeout issue resolved, I guess the export issue will be...Resolved as well. Okay, let me try and export this.What is there to export? There is nothing in here. Why can't I see the results?Okay, good.Good, there are some results. Export to Excel.
Juan Martinez   41:09Nothing happens.
Kiran Vadday   41:09Okay.Nothing happens, right? I know I fixed this issue and they did not specifically mention about export anywhere, right? Did they say anything about export?
Juan Martinez   41:25Yeah.
Kiran Vadday   41:27Okay, they said I can only export the data from my sender when I use, oh, I can't, oh, okay. See, they are able to export, so let's not create.
Juan Martinez   41:27Matt.Use Google.
Kiran Vadday   41:38Anything, but keep in mind that there is an export. Are you doing this for your own reasons, or did somebody complain about exporting?Did somebody talk about exporting as in that one?
Juan Martinez   42:00Hey, sorry, sorry, Edwin something, so...
Kiran Vadday   42:03No, I was asking if anybody complained about exporting and it's not working, or no, no, okay, so right now keep it in in the in the internal notes, not to the external customer, as long as they are good resolution suggested. Thank you. Okay, for passing along this feed.
Juan Martinez   42:08No, no, anybody, no.
Kiran Vadday   42:23Yeah.Yeah, it's not an emergency if they are not pressing on it. Yeah, if you want to close that ticket, but you know, we can, because I don't want to talk about exporting Excel before talking about timeout issues, right? Maybe that if the timeout issues are fixed and everything is working flawlessly, that's when we can go to the export issue.It might be very well be an internal reason because of that too, right? Based upon John's analysis on the Isenda issue, somewhere in the code that we are doing, we are doing a system lockup or something. So let's get the Isenda issue resolved, like users able to being able to use Isenda fully to the full scale.and really point out that export is the only issue, then we can look at it. I think it's a wasted effort if we start looking at the exports even before eyes and eye issues resolved, right?
Juan Martinez   43:21Okay.
Kiran Vadday   43:22So yeah, make an internal note if you want, but if nobody's pressing on, hey, we are not able to export.Reports.Only then we can go to it, then let it be internal, and let's figure out the eyes and the why eyes and eyes the issue. Ohh, OK, that's about that. OK, CSVM, but does the export use a different in time mode than trivial?Okay.Yeah, nothing. Unfortunately, we are slowly working on it with regards to the root cause of why. Yeah, also can whether two administrators who will have regained access. Who lost access?
Juan Martinez   43:53Okay.All the administration, administrators.
Kiran Vadday   44:07Like, like I need their names.to in order to gain the give them access you want.Who lost access? Because right now I'm able to log.
Juan Martinez   44:16Let me check.OK, let me check.
Kiran Vadday   44:25Meanwhile, let me see what the new messages are.
Juan Martinez   45:59Okay, it's Lakeman stops and April Valerie.I put the names, yeah, in the chat, yeah.
Kiran Vadday   46:05Put that in the chat one.
Juan Martinez   46:12Ah, sorry for my delay. I have a lot of things open right now, and...
Kiran Vadday   46:16No problem. Take your time. I'm typing up notes for Jr. 2.
Juan Martinez   46:20Um, relation of the duplication IDs? Well, where the number one in the IDs?
Kiran Vadday   46:23Yes.Yeah, uh, we go by e-mail.Okay, I'm back.So what about these two? These 2 don't have administrative access.Let me.
Juan Martinez   48:14Hey, sorry, in Spanish, yeah, they they lost their the access, the admin access.
Kiran Vadday   48:21I have a hard time believing that. Let's check. Let's check. So, okay, this is another way, one more thing I can show you as well. Like how to check administrator access is you pick a user, she's the one. Dean steps is then you go to.Title doesn't help.
Juan Martinez   48:48Sorry.And.
Kiran Vadday   48:55User details.These are teams.
Juan Martinez   48:58and permission groups.

## Llamada con Kiran Vadday — parte 8/9
_chunk 1658 · 2026-08-03 · fuente: Llamada con Kiran Vadday.docx_

Kiran Vadday   49:02For mission groups, yes, you're right, so...Okay, I don't know how that happened.Okay, and so she should be able to check it again. What's the other user? I give her admin access.April Valerie.
Juan Martinez   49:22Rea.But what happened? These is that I were.
Kiran Vadday   49:27Absolutely no clue. They should all have.
Juan Martinez   49:31Because it's okay, I know that manually we can put the correct access to the correct persons, but previously they have access, no?
Kiran Vadday   49:32If...April Valerie. Okay, yeah, so.Is she admin?She should definitely add her title here.Permission groups.Administrators.Add.Save. See, those three are basic. I wonder why Leanne doesn't have this three app risk case search users, app risk case users, basic users.You want me to give these three as well to her? Because that's basic for everybody. Let's do that.
Juan Martinez   50:20Okay, oh, it's really easy to do this in the control panel because if I try to do or shares the data in the database is more.
Kiran Vadday   50:29You mean this one? This is not control panel.Yeah.OK.
Juan Martinez   50:47information, I go directly to the database in Bastion, for example, and do our queries, but here is more easy.
Kiran Vadday   50:50A press.Yeah.Exactly right. And so log into there.And I just start in the production site because we are Tribu accounts, we have all the access, simply going to all apps and users, admin, all apps and settings and users. Find the user that you're trying to add the permissions and that's it. Try add as many as you want and save at the end. Don't forget to save.That's it, so Valerie.And...She's IT support. I got her admin access to, yeah, they both should be good. Anything else, Juan?
Juan Martinez   51:42No, no more. I really appreciate your time. You are out of the work time right now, yeah? Maybe one hour ago.
Kiran Vadday   51:46Oh, no problem. Anytime.Yeah, it's like 6, 6:00, but with the production issues, you know, I'm like at the laptop most of the time these days. So no worries. The sooner you speed up, Juan, I will be free. I'm just kidding. But you're doing great. You have been doing an amazing job. And with your...
Juan Martinez   51:58Uh-huh, okay. No, thanks.Yeah.Yeah.Yeah.
Kiran Vadday   52:14Whatever you did with your first comment putting on the client IDs, that's what I said to Matt. Like, I think it should become mandatory in every ticket because now the platform, it looks like this.All days it was much easier. This is how our old databases are. So you say Delhays, I know, but if you know say Aruza Delhays, I have to go to the Excel sheet, find out what Delhays or Sportsman's is, find out their client ID 420 and then go to 420.
Juan Martinez   52:27Okay.Yeah, yeah, yeah, I got it.
Kiran Vadday   52:50Because we got rid of company names in the database and got only client IDs back in the day. It's not a big deal because databases are named by company names.But not anymore.
Juan Martinez   53:02I think this is more reason in play for MTRDP 01 and remote desktop because I do all these things in Bastion, but Bastion is very slowly and now obviously I have permissions to enter or have a lot of time for the correct permissions.
Kiran Vadday   53:15Yeah, I do agree. Bastian is true. Yep, yep.I agree. Yeah, so that's really helpful once we get everything up and running. If we have the client IDs. So you did a great job on, you know, documenting and writing stuff up, making our lives easier. We wanted more people.like you who can, you know, do a great support work and keep up the testing and everything up going forward.
Juan Martinez   53:47I have access to this virtual machine to play for MTRDP01.
Kiran Vadday   53:55You mean this one? I'd like to go into the production database.
Juan Martinez   53:59No, the the the name that you put that you put in the remote desktop connection computer, sorry, the computer.
Kiran Vadday   54:05Oh, this is old one. This one?
Juan Martinez   54:08No, in the top of the left side.
Kiran Vadday   54:11This one.
Juan Martinez   54:13Nope.
Kiran Vadday   54:13You mean there's a remote desktop?
Juan Martinez   54:16Yeah, in the top of the left is flat.
Kiran Vadday   54:19Oh, as in platform, yeah, the PLA for empty RDP 01. Yeah, this is the remote desktop RDP. Oh, for that, I don't know because do you do you PIM up PIM up?
Juan Martinez   54:19Blah.
Kiran Vadday   54:37According to Matt, you guys should. So peaming up is you need to have this URL up. Once this URL is up, you have to activate yourself, which you will see shortly. You have to get the VPN up before you do anything. So I have to click on activate. And once I think I already have that activated.
Juan Martinez   54:53Yeah, yeah.
Kiran Vadday   54:58So VPN step one, activation step 2, RDP step 3, and then in the RDP you can connect to SQL, MI, PD, whatever that thing is, and you have to production and here is my staging that which I play with.

## Llamada con Kiran Vadday — parte 9/9
_chunk 1659 · 2026-08-03 · fuente: Llamada con Kiran Vadday.docx_

Juan Martinez   55:19Okay, okay. Thanks. Thanks, Kiran.
Kiran Vadday   55:22So I'm not sure. Yeah, no problem. So yeah, so your four things there. I think I have addressed them. If you have any questions, let me know, Juan.
Juan Martinez   55:31Okay, okay, sure. I really appreciate your help. I learned a lot this session, a lot of information.
Kiran Vadday   55:33Ohh.I am glad that I'm off help.
Juan Martinez   55:40And I see your skill for navigating different sections and find the correct section easily or faster. Maybe I think this is a job.
Kiran Vadday   55:49Oh yeah, I'm pretty sure you'll catch that up in like a month in a few days, Juan, with the way that you're working.
Juan Martinez   55:54Yeah.Sure, sure. Thanks, Kiran. Thanks, thanks. Kiran, Kiran or Kiran or sorry, how can I? Kiran. OK, OK, Kiran.
Kiran Vadday   55:58No worries.It's Kiran.Yeah, you got that right.
Juan Martinez   56:06Okay, okay. Thanks. See you later or tomorrow.
Kiran Vadday   56:08No worries. Talk to you later. Talk to you tomorrow. Bye.
Juan Martinez   56:10Okay, bye bye.
Juan Martinez detuvo la transcripción

## Nota de voz de J.R. Teagle antes de la reunión ADUSA — 18 ago 2026
_chunk 1699 · 2026-08-18 · fuente: inbox/2026-08-18-nota-voz-jr.md_

# Nota de voz de J.R. Teagle — 18 ago 2026, antes de la reunión con ADUSA

Transcrito localmente con whisper.cpp (medium.en). 5 min 20 s.


 Okay. Okay. Okay. And what I mean by that is you're going to be in front of Rip. You're going to be in front of one of our biggest customers who's threatened to leave us. Don't let that scare you. Just remember to shut the fuck up. Let Rip drive the vast majority of the conversation. Only weigh in when it comes to a ticket. And don't be afraid to either say two things, right? Sometimes I'm like, "Hey guys, look, let me come to speed on that real quick and then we can come back to it. We can move on to the next one." And when you hurry up, open the ticket, make sure you know where you're at. You can either type the comment or then you can say it. you're going to update a ticket, you're going to reply to an email, you're going to do anything. You got to do it, right? So set a calendar reminder, whatever it takes. So sweep the tickets, open the spreadsheet, the one on the web, sweep the tickets, make sure that they're all in a decent state and then they get a comment today, right? Once everything you feel like you're comfortable with, then you can generate a new version of the spreadsheet to send Jim. Set yourself a calendar reminder, like maybe 4.30 to 5.30 your time for you to work on that, assuming you don't have other things. So that way you're catching it at the end of your day. You want to get as many updates in there as you can. Any questions about any of this? No, the mail is just sent to Jim or copy to Cara? Cara? Okay. Okay. So just put it on your game face, baby. You know what I mean? Smile, be helpful. Don't say anything that if you don't know the answer to it, don't be afraid to get back to people. Okay. Okay. Okay. Sure. Yeah. Excellent. Anything I can do to support you, my friend? Uh, no, not really. Actually, I try to review all the information shots, the ticket status, the spreadsheet, the, the, the previous meet. Um, and maybe I have questions after this. Perfect. Perfect. I'm going to throw the, uh, the Claude commands that I use most recently to update the spreadsheet in here. Don't copy it word for word, because I told it to do some things like to the main spreadsheet, you're not going to want to do, but it'll give you an idea of the places that I'm telling it to grab and like the way that I'm working with it. Okay. Okay. Okay. Sure. And normally, I don't know, man, I feel weird using plug for this, but we've got like 80 fucking tickets, you know, 90 tickets across unification and I'll hold itself. I'm going to say there's like 69 rows on the spreadsheet we're working through right now. So there's a lot of work. My point is, don't be afraid to use Claude, but like everything, double check what the fuck it's saying. Okay. Okay. Yeah. Yeah, sure. All right. Awesome. Raj, anything on your side? Okay. Okay. Thanks. Awesome. All right team. Thank you very much. Thank you.

## Nota de voz de Viraj Kansara: reparto de la cobertura de Camila — 18 ago 2026
_chunk 1700 · 2026-08-18 · fuente: inbox/2026-08-18-nota-voz-viraj.md_

# Nota de voz de Viraj Kansara — 18 ago 2026, reparto de la cobertura de Camila

Transcrito localmente con whisper.cpp (medium.en). 7 min 52 s. Audio con ruido, hay tramos inciertos.

 Just make sure we have a group for this ticket, right?
 Make sure you add him or her to this group so he can directly work with You know Chris Chris Howard Okay I don't have anything else. But yeah, he hold tickets. I'm trying to go through the list and try to Follow up as much as I can But Like do you need any help with I can still be available for
 Okay, okay. Thanks is Before for me this holiday with you Because maybe I have questions or I need help with something because I need to cover a lot of things And I try to update me right now for for half the time to have a good perspective or summary With all the things we're lashing it with At all, but thanks. Thanks. Maybe if I have a question I can
 Write you But for now I try to read a lot information of data the shots and and that's it maybe more later I have a meeting with my Columbia team. I tried to review the tickets and maybe have Maybe find a correct person to to take this call with this this client with this ticket And that's it. Yeah, if I had something
 I can make sure I can get help from the team over here in the morning. I was on this No time migration checklist. I know Sophia has status. Let me take care of it. Okay Okay. Okay. I have a question maybe maybe a How you manage a just or they or with you are the main?
 The yeah the request of the meals that the customer sings because I have a portal access Yeah, the hippie box oh Maybe we don't have anything
 It was something just from Phillips but I don't look at that too often right doing it to Look at that every day in terms of what is coming and not coming Okay, I Mean, I don't technically I don't monitor it on a day-to-day basis I just went to that inbox when we done when a customer forwarded couple of email reports over there But is it like something we need to monitor it on?
 A daily basis like what comes in on that inbox because most of the emails that I see right? Those are my ticket responses so and if the tickets are assigned to individual site I Mean they can check on the response for the tickets based on if something is responded right the ticket gets converted to work in progress and the Engineer can take a look when they prioritize the ticket on that particular day, right? Okay, right
 Other thing I need one thing brush I try to find them the chat with the conversation with the chat with Camila and you about the This weekend on them Yeah, I don't remember the name of this this meeting in the calendar But maybe can you share me the links because I can find this this meeting with the links the Camila sent
 previously the last week with the The notes or the document that she was created for this this and the other week that she have a I can find and I have a lot of shots but I can't find each other So this is the check okay check to the To the meeting that we had. Okay, and one second. She also sent us an email
 Just one second And I had Okay, yeah, I know I had this So in your inbox, like can you search this subject? H whole document. Okay, let me let me find So it comes on top of your inbox
 Okay, great I have Yeah, you send me there Thanks. Thanks. I have I thought you have the Camila leave another guy. Yeah. Thanks
 Oh, okay
 So this is the document link I can send it to you over here again I don't want to go into this because there are a lot of other priority things that you want to take care So snow time customer communication or let me take care of it Sophia is notified in the group Stop snow time migration. Let me take care of it weekly matrix. That's end of the week. I mean daily backlog review Let's do it later. Don't get assignments new member on boarding the Please go team rotational one-on-one with team members everyone call rotations. I Know you're committing. I don't know what that is, but maybe You can take care of it. Um, let me take care of this no time communications. Okay for today. Okay, um rest rest I don't think there is any urgency on list of those topics. Sure. Just ping me if you need anything. Okay. Thanks. Okay. Okay. Okay. Thanks You
. Thanks
 You

## Prep del standup del equipo Colombia — 18 ago 2026
_chunk 1701 · 2026-08-18 · fuente: inbox/2026-08-18-prep-standup-colombia.md_

# Prep relámpago — reunión equipo Colombia, 18 ago

Barrido del tracker 10:30 (el más reciente) cruzado con lo que se dijo hoy en el chat de
End of July Unification. Colombia: tú, Diego Buelvas, Sebastian Rueda, Edwin Garzon,
Luis Hernandez, David Vargas.

## Tuyos

| Ticket | Estado tracker | Lo nuevo de hoy en Teams |
|---|---|---|
| RCS-28021 Izenda export | Work in progress | Matt: "looks to be working, however we need to get an actual report" — sigue pendiente de ti el nombre del reporte que falla |
| RCS-28123 Asignación de casos | Work in progress | Matt: "Fixed in Prod, we have not tested as it requires approving a record in a live system" — el bloqueo de permiso sigue en pie |
| **RCS-28124 Adjuntos** | Under Customer Review | **Contradicción a resolver hoy**: el tracker dice fix desplegado y probado el 14. Matt dijo a la 1:09 p.m. de ayer "in release just waiting for me to push to prod". Pregunta al equipo: ¿ya se empujó a prod o seguimos con el fix del 14 nada más? |
| RCS-28342 Anthony Lopez | Under Customer Review | Sin novedad nueva, esperando retest del cliente |
| RCS-28364 Brian Somsky | Under Customer Review | Sin novedad nueva, esperando retest del cliente |
| RCS-28353 502 al editar tienda | Work in progress | El fix grande de YARP/otelcol-swap (ENG-7270) se confirmó en prod para el cambio de ubicación de casos. Preguntar si aplica también a este ticket o es causa distinta |

## Del equipo

| Ticket | Dueño | Estado | Lo nuevo de hoy |
|---|---|---|---|
| RCS-28379 Case Owner/Creator en blanco | Diego Buelvas | Active with Appriss | Kiran: "Incident UserID <-> LoginID mapping is done... currently working on getting the missing User information on Incident tables like MasterCase and Shoplifting" — avanza, no está cerrado |
| **RCS-28093 Empleados no restringidos** | Edwin Garzon | Work in progress | **Punto de fricción real**: Matt dice "the true root cause of what this ticket was opened for is working as expected", pero avisa "Jim Cassebom may not agree, due to his interpretation of what should be happening here". Hay que decidir hoy cómo se lo explicamos al cliente antes de que Chris lo toque en la reunión |
| **RCS-28281 Carga de transacciones 10 ago** | Edwin Garzon | Under Support Review | **Vencido, 5 días sin comentario.** No hay update nuevo en Teams tampoco. Pregúntale a Edwin en la reunión directamente, es el único de los 21 así |
| RCS-28407 502 frecuente | Edwin Garzon | Under Support Review | Se está aislando moviendo Izenda a su propio app service (`web-prd-wus2-arp-izenda`), en dev/staging, no en prod. Sin ETA confirmado |
| RCS-28053 Link no-SAML | David Vargas | Completed | Cerrado, sin acción |

## Las tres preguntas que vale la pena hacer en la reunión

1. **28124**: ¿el segundo despliegue ya salió o seguimos con el del 14? Lo necesitas resuelto antes de armar el correo de hoy.
2. **28093**: si Matt considera que el comportamiento real es el esperado, ¿cerramos y explicamos, o esperamos a que Chris lo alinee con el cliente en la reunión de hoy?
3. **28281**: ¿alguien le puede pedir estado a Edwin ahora mismo, dado que es el único vencido?

## No es tuyo, pero afecta tu correo de hoy

**RCS-28196** (Vedant, no es Colombia) está confirmado resuelto en prod por Gabor, con el matiz de
Matt sobre los casos históricos con el valor por defecto. Tu versión del tracker todavía dice
"esperando release". Corrígelo antes de enviar.

## ENG-6555. Guion de preguntas para Kiran, 28 ago 2026 — 2026-08-28
_chunk 1708 · 2026-08-28 · fuente: inbox/2026-08-28-meet-kiran-preguntas.md_

Ticket ENG-6555. Trabajado el 2026-08-28. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Si la reunión se corta a la mitad, las cinco primeras son las que mueven la aguja. Todas en inglés, listas para leer. --- No abras con una petición. Abre con el conteo y con el error propio.

## Rastro
2026-08-28 inbox/2026-08-28-meet-kiran-preguntas.md

## RCS-27389. Tracker Alo Yoga para la reunion — 1 sep 2026 — 2026-09-01
_chunk 1711 · 2026-09-01 · fuente: inbox/2026-09-01-tracker-alo-yoga.md_

Ticket RCS-27389. Trabajado el 2026-09-01. 1 notas en inbox.

## Que sigue
1. RCS-27389, responder el reporte del 14 ago sobre ship from store e impossible travel. 18 dias sin respuesta de Appriss.
2. RCS-27389, decidir el reload historico desde el 20 jun 2025 que pidio el plan de Carolyn Allison.
3. RCS-27557, sacarle a Thomas Walker la posicion sobre derivar la zona horaria de la direccion de tienda.
4. RCS-28108, abrir las capturas del 14 ago en Jira antes de la reunion. El ticket no tiene descripcion.
5. Izenda en el tenant de Alo, riesgo latente identificado el 2 jul en RCS-27598 y nunca validado. No mencionarlo al cliente sin verificar.

Fuente cruda con la cronologia completa y las citas literales: `inbox/2026-09-01-dossier-alo-yoga.md`.

## Rastro
2026-09-01 inbox/2026-09-01-tracker-alo-yoga.md

## KT de la reunión con Kiran Vadday, 28 ago 2026 — 2026-08-28
_chunk 1758 · 2026-08-28 · fuente: inbox/2026-08-28-KT-reunion-kiran.md_

# KT de la reunión con Kiran Vadday, 28 ago 2026

Support-Eng Process Review. 53 minutos, Juan Martinez y Kiran Vadday.
Fuente: grabación y transcripción completas. Las rutas, queries y IDs salen de la pantalla
que Kiran compartió, no de memoria.

Este documento es para el equipo. Todo lo técnico está verificado contra el video.

---

## 1. Credenciales de netTrack. Se acabó pedirlas

**Este es el entregable más grande de la reunión.** Kiran nos dio la ubicación del archivo
que tiene todos los usuarios y contraseñas de netTrack, para que nadie más tenga que
pedírselas a ella ni a Matt.

**Ruta exacta, vista en pantalla:**

```
C:\LPMS Utilities\VB Scripts\SELECT\DB_SELECT.vbs
```

23 KB, VBScript Script File. En esa misma carpeta hay además `Notes`, `SQL` y
`SQL_DB_STORAGE`, más una subcarpeta `Scott`.

**Cómo llegar:** Azure Bastion hacia el servidor `qa-lpms-rdp-001`. El nombre completo que
Kiran usó es **QALPMSRDP001**. Ese servidor tiene la red de producción y la de QA.

**Cómo abrirlo:** clic derecho, Edit in Notepad. Si Notepad++ lanza el aviso de Network Path
Warning apuntando a `\\pd-lpms-iis-007\Clients\<cliente>\nettrack\App_Data\connectionstrings.config`,
darle Skip a todos los mensajes.

**Qué contiene:** los seis entornos. Kiran los enumeró así, y la regla mnemotécnica es suya:

> "PE I think is Europe, QC, QE, QA. You know, anything with A is like PD PQ A, USA, PE QE,
> Europe, PC, QC, Canada. So these three, so total six."

- **PD / QA** = Estados Unidos
- **PE / QE** = Europa
- **PC / QC** = Canadá

Producción y QA de cada región. Con esas credenciales tienes operaciones CRUD completas en
netTrack. Sin ellas puedes entrar, pero solo lees.

> "with these you do have the credentials, operations possible. Without that, you can still
> access, but you won't be able to do all the CRUD work."

**Lo que Kiran pidió que hiciéramos:**

> "If do yourself a favor, create some account in one password, I mean a vault. Throw them
> in there so you don't have to go this horrible route."

Cada uno guarda las credenciales en su bóveda de 1Password con su propio tag. No se
comparten por chat ni por correo.

### El lado Platform no necesita credenciales

Ojo con esta distinción, es importante y mucha gente la confunde:

> "Coming to platform, it's not like that. It totally gets off based off your Windows
> thingy. And all you need to do is teaming up onto the server, then turning on the VPN,
> then RDP into platform RDP 01. And you should be able to do all the CRUD operations
> without any interruption. So you don't need credentials there."

**Platform: autenticación integrada de Windows, cero credenciales.** VPN, RDP al servidor de
platform, y ya tienes CRUD.
**netTrack: sí necesitas el archivo.** Y netTrack va a desaparecer:

> "eventually we'll get away from netTrack anyways."

---

## 2. RCS-28342 y el problema de los títulos

### Dónde vive el título de un usuario, y por qué está en dos sitios

La historia completa, en palabras de Kiran. Cuando se migró de `incident.LPUser2` a
`membership.Users`, el equipo creyó que `membership.Users` no tenía columna de título. Para
acomodar lo que netTrack necesitaba, metieron el título en una tabla aparte:

```
incident.LPUser2  ->  membership.Users
                      membership.UserExtensionData   (aquí se guardó el Title)
```

`membership.UserExtensionData` funciona por atributos: `UserID`, `AttributeName`,
`AttributeValue`. Cuando `AttributeName = 'Title'`, el `AttributeValue` es el título.

La vista `LPUser` arma el resultado uniendo las dos: todos los datos vienen de
`membership.Users` y el título de `membership.UserExtensionData`, mapeado por el **UserID
GUID grande de membership**, no por el UserID numérico.

Kiran lo describió sin adornos:

> "But that's what happened there because we were not tying directly between the two. We
> were going in squiggly lines."

### El query que ella corrió, verbatim de la pantalla

```sql
WITH Candidates AS (
    SELECT
        u.UserId,
        MAX(lp2.Title) AS Lp2Title      -- MAX handles any accidental LPUser2 duplicates
    FROM membership.Users u
    JOIN incident.LPUser2 lp2
        ON lp2.LoginID = u.UserName
    LEFT JOIN membership.UserExtensionData ued
        ON  ued.UserId        = u.UserId
        AND ued.AttributeName = 'Title'
    WHERE lp2.Title IS NOT NULL
      AND LTRIM(RTRIM(lp2.Title)) <> ''
      AND (
            ued.UserId IS NULL
         OR ued.AttributeValue IS NULL
         OR LTRIM(RTRIM(ued.AttributeValue)) = ''
      )
    GROUP BY u.UserId
)
MERGE membership.UserExtensionData AS target
USING Candidates AS source
    ON  target.UserId        = source.UserId
    AND target.AttributeName = 'Title'
WHEN MATCHED
 AND (target.AttributeValue IS NULL OR LTRIM(RTRIM(target.AttributeValue)) = '')
    THEN UPDATE
        SET target.AttributeValue = source.Lp2Title
WHEN NOT MATCHED BY TARGET
    THEN INSERT (UserId, AttributeName, AttributeValue)
        VALUES (source.UserId, 'Title', source.Lp2Title);
```

Target es `membership.UserExtensionData`. Source es el CTE que cruza `membership.Users` con
`incident.LPUser2` por LoginID igual a UserName. El ticket incluye primero un SELECT de
preview y después el MERGE.

**Esto es DML. Cualquiera del equipo con escritura lo puede correr.**

### Y esto cambia el 15 de septiembre

`membership.Users` **sí tiene** una columna llamada `JobDescription`. Se dieron cuenta
tarde. El nuevo stored procedure va a mapear el título directo a `membership.Users.JobDescription`,
y la UI va a leer de ahí.

> "So going forward, we will be mapping title to job description. I'm still inserting in
> here, but we won't be looking at that anymore. You can ignore it."

> "PR is not still in, but by September 15th, that should be in main, that should be across
> the board."

**Qué significa para nosotros.** Los clientes que ya se desplegaron, más de 20, no reciben
ese cambio. Para ellos hay que correr un update a mano. Kiran nos dijo cómo:

> "Or simply write update statement from title directly from LPUser2.Title to
> JobDescription. Why should we even go to the user extension data? Just try to run it
> right away."

**Advertencia que dio y que hay que respetar:**

> "But make sure that they did not make any changes to job description already because
> we'll be overriding them."

Antes de correr ese update, verificar que `JobDescription` no traiga ya datos del cliente.
Si los trae, los pisas.

**Después del 15 de septiembre, el título en la UI, en Users Settings, tiene que venir de
`membership.Users.JobDescription`, no de `UserExtensionData`.** Si ves lo contrario en un
tenant desplegado, ya sabes por qué.

---

## 3. RCS-28379 y la causa raíz de los nombres en blanco

### Por qué pasó

Este es el conocimiento más valioso de la reunión, porque explica una familia entera de
tickets.

Cuando se escribió el script de migración de `incident.LPUser2` a `membership.Users`, se le
pusieron **reglas extensas de exclusión**: no traer cuentas inactivas, no t

## Rastro
2026-08-28 inbox/2026-08-28-KT-reunion-kiran.md

## Recomendaciones de Kiran Vadday al equipo de soporte — 2026-08-28
_chunk 1775 · 2026-08-28 · fuente: inbox/2026-08-28-recomendaciones-kiran-equipo.md_

# Recomendaciones de Kiran Vadday al equipo de soporte

Cierre de la reunión del 28 ago 2026, minutos 38 a 53. Juan le pidió una lectura directa:

> "Based on everything we deal with these past few weeks, do you think we should prioritize
> something specific to deliver faster solutions or start implementing a more efficient
> process? I'd like to hear your thoughts and recommendation on this so I can share it with
> the team."

Lo que sigue es su respuesta. Las citas son textuales.

---

## La recomendación central: devuelve el ticket incompleto de inmediato

Es lo primero que dijo y lo repitió tres veces. Es el cambio de proceso que más le importa.

> "If there will be information missing right in the customer's request and they forget to
> mention the details of what it is, throw it back to them. You don't need to stop
> investigating with whatever little you have, but throw it back to them."

**Las dos cosas van juntas: sigues investigando con lo que tengas, y al mismo tiempo pides
lo que falta.** No es una en lugar de la otra.

El costo de no hacerlo, en sus palabras:

> "Rather than you coming to us and us digging deeper and then us asking you, which might
> take two to three days. So it'll give the kind of information like, oh, they asked me this
> now after three days. It will be the client's expression."

Tres días después de abierto el ticket, preguntarle al cliente lo que se le pudo preguntar
el primer minuto, es lo que quema la relación.

### El momento exacto en que hay que pedirlo

Con el primer mensaje. El mismo en que dices que tomaste el ticket.

> "Whoever is the first one who responded, I think it looks like a defaulted message that
> they are sending, but I would actually stop and look at the ticket description and see if
> they can add more to it. Like right after 'hey, I took this ticket, I'll be investigating
> this for you', meanwhile, can you please present me the audit number of the one which you
> tried to edit and couldn't access, so that I can check in the background."

**El acuse de recibo no puede ser una plantilla vacía.** Lee la descripción, identifica qué
falta, y pídelo en ese mismo mensaje.

### El ejemplo concreto que usó, y hay que leerlo sin ponerse a la defensiva

Kiran nombró a David Vargas y a un ticket de Boot Barn. Antes de criticar, encuadró:

> "These are all L1 guys. I won't blame them."

Y después:

> "Instead of saying that, hey Debbie, I have taken the ownership of this ticket and we'll be
> investigating for you, but before I move ahead, can you please show the screenshots? What
> screenshots did she show? There is nothing here. So what is that one audit that she's
> seeing? Is she even lying to us? She's not seeing anything there, but she says there is.
> So there is no information, but we can't tell to her face, hey, stop lying. So we have to
> be nice and say, hey, I will be investigating this for you, but can you please give me
> this audit that you're trying to edit."

El punto no es el error de David. El punto es que la usuaria escribió "hago clic en una
auditoría y me devuelve atrás" y nadie le preguntó **cuál** auditoría.

> "The user clearly said that hey, I'm clicking on an audit and it's going back, rather than
> saying oh, I'm going to investigate, find out what exact audit that is."

### La regla, tal como la formuló

> "Every time when we see something where they're saying oh, I'm clicking this or I did
> this, and don't give what that thing is, I would recommend: stop whatever you're doing,
> push it back to them, say can you please give us a screenshot, URL, and also the case
> number or audit number or something that ties us to it."

Y anticipó la objeción sola:

> "Because in this case, URL won't be helpful because she will click it and it will go back.
> So she can't give you a URL, but she can give us the audit number, the case number. At
> least a screenshot of 'hey, I'm trying to click this', and at least it will have the audit
> number or case number."

**Cuando la URL no se puede capturar, el identificador sigue siendo obligatorio. Número de
caso o de auditoría.**

---

## Lo que exige recibir antes de que un ticket llegue a ingeniería

Esta es su lista, en su orden de importancia.

### 1. La URL. Es lo primero que nombró y lo repitió

> "Anytime when you pass it to the engineering team, I would really appreciate if you give
> me the URL."

> "So missing, yeah, so URL is most important, and screenshots."

### 2. El error log expandido, no la captura del error

Este es el punto donde fue más específica y más tajante.

> "Most of the time, customers come back throwing you the error screen, but they will take
> the screenshot of the error rather than expanding it and showing it. So I'm not asking you
> to ask customers, but by the time you reach us, I want it there. I want it to have an error
> log. I don't want to sit and dig for it."

La pantalla de error tiene un botón de **technical explanation**. Los usuarios no lo abren.
Nosotros sí tenemos que abrirlo.

> "It actually has a technical explanation button. Users don't want to click it. But by the
> time you guys recreate it, you can expand it and throw in the error log, or go to the
> Control Panel and error logs. Throw in the error log from there or directly from that URL,
> that technical explanation thing, that's also the same exact log."

Y por qué le importa tanto:

> "Throw that in there because it makes me go to the exact point and throw it at Claude or
> myself and just analyze it behind the scenes, just to see if it's an actual issue or
> something that is data related."

Su veredicto sobre la captura pelada del error:

> "I don't need to see the screenshot. That gives me zero information and is defaulted for
> everybody. But the actual technical explanation, which would vary for different errors."

**La captura del mensaje genérico de error no sirve. Es igual para todos. El log expandido
es lo que distingue un caso de otro.**

### 3. Screenshots, muchos

> "Screenshots, tons of screenshots. Any screenshots that you are able to recreate, or the
> customer's."

Y de paso definió cómo entiende el reparto de trabajo, que conviene citar cuando alguien
diga que soporte solo escala:

> "I'm assuming support will be doing most of the leg work rather than asking clients,
> because we don't want to be like 'you do the work and we'll sit and enjoy'. So if you're
> doing it, recreating the same thing in production, screenshot, URL, URL."

### 4. Pasos de reproducción

No tienen que ser una novela. Tienen que ser el camino.

> "By the time it comes to me, recreation steps or reproduction steps, however you want to
> call it, saying the sign-in URL, number two, go here, go here, go here. At least the going
> path need not be elaborate like a million points. Say netTrack, Admin, Step Configuration,
> Edit, for example. Whatever examples you're using, actually throw them in there. And then,
> oh, voilà, here is the error. And then error log with the

## Rastro
2026-08-28 inbox/2026-08-28-recomendaciones-kiran-equipo.md

## EoW 11 sep 2026, feedback sobre uso de IA y registro de servicio al cliente — 2026-09-11
_chunk 1821 · 2026-09-11 · fuente: inbox/2026-09-11-eow-registro-cliente-y-uso-de-ia.md_

# EoW 11 sep 2026, feedback sobre uso de IA y registro de servicio al cliente

Grabacion: `EoW 11 septiembre.m4a`, 16 min 20 s, ingles.
Transcrita en local con whisper.cpp large-v3-turbo. El audio no salio de la Mac.
Participantes que se alcanzan a identificar: JR conduce, Camila, Juan, Viraj.
Se nombran sin estar presentes: Lewis, Edwin, Carl, Kim, Rip, Matt, David, Dan Endersby.

## Lo que hay que entender antes de leer nada mas

JR dio feedback directo y con nombre propio sobre el registro de los comentarios
de cara al cliente. No es un regano, lo enmarco como diferencia cultural y dijo
dos veces que no estaba senalando a nadie. Pero el punto de fondo es real y hay
que corregirlo.

El problema no es el ingles. El ingles esta bien. El problema es que una frase
neutra en espanol se vuelve cortante al pasar a ingles palabra por palabra. El
ejemplo que dio textual es "I don't need anything else from you". En espanol
"no necesito nada mas de usted" es neutro y hasta amable. En ingles americano de
soporte suena a despido, a "ya no me sirves". JR lo dijo asi: suena a "go away,
get lost".

La correccion no es escribir mas largo. Es otra cosa, y conviene tenerla clara
porque en la misma reunion JR pidio las dos cosas a la vez y parecen opuestas.

## La regla de las dos capas

Un comentario al cliente tiene dos capas y se tratan al reves una de la otra.

La capa social, o sea el saludo, el agradecimiento, la peticion y el cierre, se
acolcha. Ahi van las palabras de mas. Ahi es donde el americano espera el relleno
y donde su ausencia se lee como frialdad.

La capa tecnica, o sea el diagnostico, los pasos, la evidencia, se recorta. Ahi
JR fue durisimo: dijo que los volcados grandes de salida de IA son un dump, que
muchas veces es informacion inutil, y que los ingenieros que reciben la
escalacion los devuelven diciendo "this is AI slop, the answer here is wrong".

Resumido: mas palabras alrededor, menos palabras adentro.

## Banco de frases, literal contra natural

Para pegar directo. Sin markdown, sin negritas, sin guiones.

Cuando ya no necesitas nada del cliente.
Literal que suena mal: I don't need anything else from you.
Natural: I appreciate everything you have sent over so far. I do not think I need
anything else at the moment, and I will come back to you if that changes.

Cuando pides informacion.
Literal que suena mal: Send me the logs.
Natural: Whenever you have a moment, could you send over the logs from that time
window? That will help me narrow this down on my side.

Cuando el cliente esta equivocado.
Literal que suena mal: That is not correct. The error is on your side.
Natural: I may be reading this differently, so let me share what I am seeing on
my end. It looks like the behavior is coming from the configuration rather than
from a defect, and I would like to confirm that with you.

Cuando no puedes hacer algo.
Literal que suena mal: We cannot do that.
Natural: That is not something we are able to do today. What I can do instead is
walk through the options with you and see which one gets you closest.

Cuando ya lo explicaste antes.
Literal que suena mal: I already explained this.
Natural: Just to recap what we covered earlier, so we are both working from the
same picture.

Cuando haces seguimiento.
Literal que suena mal: Waiting for your response.
Natural: No rush at all on this one. I am just checking back in case it slipped
through the cracks.

Cuando cierras.
Literal que suena mal: Closing this ticket.
Natural: I am going to go ahead and close this one out. If anything comes back,
just reply here and it will reopen right away.

Cuando crees que es un defecto pero no lo has confirmado.
Literal que suena mal: We identified two defects.
Natural: I am seeing something that may point to a product issue. Before I call
it a defect, I want to confirm it with our engineering team so we do not set the
wrong expectation on timing.

Esa ultima es la mas cara de todas y tiene su propia seccion abajo.

## Los cinco movimientos que hacen el registro

Uno. Agradece antes de pedir. Siempre, aunque sea la quinta vez.

Dos. Nunca digas la ausencia de necesidad como un rechazo. Convierte "no
necesito nada" en "tengo lo que necesitaba por ahora, vuelvo si cambia".

Tres. Absorbe con "I" y "we", reparte credito con "you". "I may have missed
something" en vez de "you did not send it".

Cuatro. Cubre toda conclusion no verificada con un atenuante. It looks like, I am
seeing, that may point to, my current read is. Esto no es cortesia, es proteccion
contractual, y enlaza con la seccion siguiente.

Cinco. Ningun imperativo pelado. Could you, would you mind, whenever you have a
moment.

## El error que puede costar plata

JR conto un caso de un ticket de Lewis donde se le dijo al cliente que habia dos
errores distintos. Ingenieria entro despues y dijo que no habia dos errores, que
probablemente habia un tema de configuracion y posiblemente ningun defecto.

La consecuencia que JR marco no es la verguenza. Es que ya se le creo al cliente
la expectativa de que va a recibir dos defectos corregidos, cuando puede que no
haya ninguno, y cuando de hecho podria tratarse de un change request facturable.
Anunciar un defecto que no existe convierte trabajo cobrable en trabajo gratis y
deja a la empresa debiendo algo que nunca prometio nadie.

De ahi sale la regla: no se nombra un defecto hasta que ingenieria lo confirme.

## Como quiere JR que se use la IA

No prohibio nada. Textual, dijo que la IA es una herramienta y no siempre tiene
razon, y que hay que pensarla como un ingeniero junior que triaga cosas, alguien
que quizas era muy bueno en su empresa anterior pero no entiende como se conectan
nuestras herramientas ni las sutilezas que no estan escritas en ningun lado.

El flujo que pidio, en orden: usa la IA, mirala, corre tu mismo lo que dijo,
verificalo, y solo entonces escribe un comentario que valga. Y el comentario que
vale tiene esta forma, textual de el:

Claude told me it thinks this is the root cause. I checked this, this, and this.
This is what I think. Can someone else please evaluate this for me and give me
your thoughts?

Fijate que eso no esconde que uso IA. Declara la hipotesis, declara la
verificacion propia, y pide revision. Esa es la forma que no le rebota.

Dato de contexto que dio: esta semana tres ingenieros distintos se le quejaron y
cada uno le llevo un ticket de ejemplo. Tambien reconocio que dentro de la
empresa hay quien empuja lo contrario, nombro a Dan Endersby diciendo "just use
Claude, Claude will give you all the answers", y su respuesta fue que se ha
probado una y otra vez que se equivoca.

Y aclaro que a el tambien le pasa. Dijo que le cuenta locuras, que el escarba,
pregunta, y entonces la IA responde que estaba equivocada.

## Lo que dijo Camila

Dos cosas. La primera, que se esta confiando sin cuestionar, y que precisamente
por no ser experto uno asume que la respuesta de la IA es la correcta. Conto su
propio metodo: le pide a Claude que le explique el ticket, 

## Rastro
2026-09-11 inbox/2026-09-11-eow-registro-cliente-y-uso-de-ia.md

## RCS-28342. Leigh Ann reporto el 3 sep otro usuario con el titulo vacio, mismo sintoma que Anthony Lopez. Ticket Work in p — 2026-09-14
_chunk 1827 · 2026-09-14 · fuente: inbox/2026-08-28-meet-kiran-preguntas-RCS.md;2026-09-14-rcs-28342-fix-titulos.md;2026-09-14-rcs-28342-queries-titulo.md_

Ticket RCS-28342. Trabajado el 2026-08-28 a 2026-09-14. 3 notas en inbox.

## Que pasa
Leigh Ann reporto el 3 sep otro usuario con el titulo vacio, mismo sintoma que Anthony Lopez.
Ticket Work in progress, asignado a Juan. Falta aplicar la correccion al usuario nuevo.

## Causa
Kiran, 10 de agosto, cortando de raíz:
> "No. Once deployed, all the clients get the same code."

Úsalo tú mismo como ejemplo de algo que ya no hay que volver a preguntar.

---

## Evidencia
Comentario de Kiran Vadday en RCS-28342, 17 ago 2026, trae el MERGE completo que corrio para
poblar UserExtensionData desde LPUser2.Title.
brain/markdown/17-reuniones-prep.md, seccion 2, transcribe el mismo query y el mapeo completo.
Matthew Kamminga, comentario del 19 ago, actualizo la configuracion SSO para sincronizar el
claim en cada login, no solo en el backfill puntual.

## Precedentes
RCS-28342, Anthony Lopez, mismo ticket, resuelto el 14 ago con el MERGE de Kiran.
RCS-28177, Jonathan Wright y otros, misma familia, pero con 20 usuarios sin contraparte que el
MERGE no alcanza. Revisar si el usuario nuevo tampoco aparece en LPUser2.
brain/memoria/project_estado_abierto_2026_08_18.md confirma que no es un caso aislado.

## Rastro
2026-08-28 inbox/2026-08-28-meet-kiran-preguntas-RCS.md
2026-09-14 inbox/2026-09-14-rcs-28342-fix-titulos.md
2026-09-14 inbox/2026-09-14-rcs-28342-queries-titulo.md

## ENG-8659. THD. Guía para la reunión del 22 de septiembre — 2026-09-22
_chunk 1837 · 2026-09-22 · fuente: inbox/2026-09-22-THD-guia-reunion.md_

Ticket ENG-8659. Trabajado el 2026-09-22. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Revisé las tres hojas del Excel local, correos y capturas de Juan, la investigación del 21 y 22 tickets en Jira. El original de Camila queda intacto. Camila ya corrigió por correo que la recarga es temporal. El Excel todavía invita a cerrar el caso y presenta como pendiente una reparación de búsquedas que Simon realizó en agosto.

## Rastro
2026-09-22 inbox/2026-09-22-THD-guia-reunion.md

## ENG-9486. RCA Smart Alerts, 29 septiembre 2026. Borrador interno local para retrospectiva — 2026-09-29
_chunk 1838 · 2026-09-29 · fuente: inbox/2026-09-29-smart-alerts-rca.md_

Ticket ENG-9486. Trabajado el 2026-09-29. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
RCA Smart Alerts, 29 septiembre 2026. Borrador interno local para retrospectiva. inbox/2026-09-29-smart-alerts-rca-internal.docx. Incluye la plantilla Internal RCA 474709983443, cronología, impacto, corrección, causa, acciones propuestas, hoja de reunión y fuentes.

## Rastro
2026-09-29 inbox/2026-09-29-smart-alerts-rca.md

## RCS-28342. Leigh Ann reporto el 3 sep otro usuario con el titulo vacio, mismo sintoma que Anthony Lopez. Ticket Work in p — 2026-09-16
_chunk 1860 · 2026-09-16 · fuente: inbox/2026-08-28-meet-kiran-preguntas-RCS.md;2026-09-14-rcs-28342-fix-titulos.md;2026-09-14-rcs-28342-queries-titulo.md;2026-09-16-rcs-28342-revision-cola.md_

Ticket RCS-28342. Trabajado el 2026-08-28 a 2026-09-16. 4 notas en inbox.

## Que pasa
Leigh Ann reporto el 3 sep otro usuario con el titulo vacio, mismo sintoma que Anthony Lopez.
Ticket Work in progress, asignado a Juan. Falta aplicar la correccion al usuario nuevo.

## Causa
Kiran, 10 de agosto, cortando de raíz:
> "No. Once deployed, all the clients get the same code."

Úsalo tú mismo como ejemplo de algo que ya no hay que volver a preguntar.

---

## Evidencia
Comentario de Kiran Vadday en RCS-28342, 17 ago 2026, trae el MERGE completo que corrio para
poblar UserExtensionData desde LPUser2.Title.
brain/markdown/17-reuniones-prep.md, seccion 2, transcribe el mismo query y el mapeo completo.
Matthew Kamminga, comentario del 19 ago, actualizo la configuracion SSO para sincronizar el
claim en cada login, no solo en el backfill puntual.

## Precedentes
RCS-28342, Anthony Lopez, mismo ticket, resuelto el 14 ago con el MERGE de Kiran.
RCS-28177, Jonathan Wright y otros, misma familia, pero con 20 usuarios sin contraparte que el
MERGE no alcanza. Revisar si el usuario nuevo tampoco aparece en LPUser2.
brain/memoria/project_estado_abierto_2026_08_18.md confirma que no es un caso aislado.

## Rastro
2026-08-28 inbox/2026-08-28-meet-kiran-preguntas-RCS.md
2026-09-14 inbox/2026-09-14-rcs-28342-fix-titulos.md
2026-09-14 inbox/2026-09-14-rcs-28342-queries-titulo.md
2026-09-16 inbox/2026-09-16-rcs-28342-revision-cola.md

## RCS-29207. Starbucks NA reporta cero resultados en el run mensual del 29 sep y lo relaciona con RCS-28873. Jira: Under Su — 2026-10-07
_chunk 1920 · 2026-10-07 · fuente: inbox/2026-09-30-rcs-29207.md;2026-10-01-rcs-29207-escalacion-delivery.md;2026-10-01-rcs-29207-paquete.md;2026-10-01-sbx-paquete-orden.md;2026-10-02-rcs-29207-escalacion-delivery.md;2026-10-02-sbx-correccion-notas-escalacion.md;2026-10-05-sbx-work-items-estado.md;2026-10-06-sbx-work-items-estado.md;2026-10-07-rcs-29207-evaluacion-talos.md_

Ticket RCS-29207. Trabajado el 2026-09-30 a 2026-10-07. 9 notas en inbox.

## Que pasa
Starbucks NA reporta cero resultados en el run mensual del 29 sep y lo relaciona con RCS-28873. Jira: Under Support Review, High, asignado a Juan.

## Evidencia
[2026-09-30] 1. RCS-28873, Sebastian 25 sep 15:36: Numeric value '1870125876697924' is not recognized, QueryId 01c74f01-0109-be1e-0120-d20105f2fa0f.
2. RCS-28848, Gabor 17 sep: SearchInputValueOverflowException en 2-Star Accrued by Member ID. ENG-9112 en Backlog.
3. Tres definiciones en cero en el mismo periodo, RCS-29205/06/07.
[2026-10-06] RCS-29207: Completed. Manish verifico el 6 oct 13:08 ("Verifed. Thanks"). Resolution Details quedo "Infrastructure Resolved - Patch Applied"; el arreglo fue de configuracion de Delivery (Carl Costelow), la opcion que mejor calza es Delivery Resolved, configuracion modificada. Falta pasar a Closed.
RCS-29205: Work in progress, a nombre de Juan. Manish pregunto "Any update on this item?" el 6 oct 13:09. Ultima respuesta al cliente fue el 2 oct; la del 5 oct no se pego. Nota interna con los 5 campos pegada el 5 oct. Sin respuesta de Adarsh en el ticket. Reunion con Ryan sin agendar.
RCS-29206: Under Customer Review desde el 1 oct, sin respuesta de Manish. El seguimiento del 5 oct no se pego.
Archivos 6 oct: respuesta a Manish en 29205, seguimiento a Adarsh, seguimiento a Manish en 29206.

## Que sigue
1. Si Sebastian confirma que es la condición guardada en la definición, es configuración en producción. Va a Delivery Secure 5: estado Under Delivery Review, assignee Peyman Motlagh, Team Ownership Support (Delivery Dep.) y Sprint RCS Support Team.
2. Si dice que es código del motor de búsqueda, va a Engineering: estado Under Engineering Review, assignee Shandana Khan, y relates a RCS-28873.
3. En los dos casos, le aviso a Manish que ya pasó al equipo que lo corrige. Sin fecha.
4. Cuando lo corrijan, verifica en Snowflake que la consulta pase a SUCCESS y en Executive Workbench que aparezcan items del periodo 24 ago a 27 sep.

## Precedentes
RCS-28873 SBX, binding numerico de MemberID, tickets/RCS-28873.md
RCS-28848 SBX, overflow de MemberID en busqueda de estrellas, ENG-9112
RCS-28671 THD, WISC no regenera por dedup, tickets/RCS-28671.md

## Rastro
2026-09-30 inbox/2026-09-30-rcs-29207.md
2026-10-01 inbox/2026-10-01-rcs-29207-escalacion-delivery.md
2026-10-01 inbox/2026-10-01-rcs-29207-paquete.md
2026-10-01 inbox/2026-10-01-sbx-paquete-orden.md
2026-10-02 inbox/2026-10-02-rcs-29207-escalacion-delivery.md
2026-10-02 inbox/2026-10-02-sbx-correccion-notas-escalacion.md
2026-10-05 inbox/2026-10-05-sbx-work-items-estado.md
2026-10-06 inbox/2026-10-06-sbx-work-items-estado.md
2026-10-07 inbox/2026-10-07-rcs-29207-evaluacion-talos.md

## THD. Preguntas para la reunión / Client questions — 2026-09-22
_chunk 1945 · 2026-09-22 · fuente: inbox/2026-09-22-THD-preguntas-cliente-bilingue.md_

# THD. Preguntas para la reunión / Client questions

Uso interno para Juan y Camila / Internal use for Juan and Camila.

ES: Respuestas propuestas con la evidencia reunida el 22 de septiembre de 2026, corte 11:55 Bogotá. No representan una nueva verificación en producción. Los compromisos pendientes deben acordarse antes de anunciarlos.

EN: Suggested answers based on the evidence reviewed on September 22, 2026, as of 11:55 AM Bogotá. This is not a new production verification. Agree outstanding commitments before presenting them as confirmed.

<a id="menu"></a>
## Navegación rápida / Quick navigation

| Si preguntan por… / If they ask about… | Ir a / Open |
| --- | --- |
| Qué está resuelto y qué sigue abierto / Resolved and open work | [Resumen / Overview](#overview) |
| Por qué dijimos que estaba resuelto / Previous resolution statements | [Confianza / Trust](#trust) |
| Importes, recibos, recargas y archivos / Amounts, receipts, reloads and files | [Datafeed](#datafeed) |
| Migración, búsquedas y 17 work items / Migration, searches and 17 work items | [Migración / Migration](#migration) |
| Lentitud, 25 pendientes y fecha del 24 / Slow searches, 25 pending and September 24 | [Rendimiento / Performance](#performance) |
| Upgrade y estabilidad / Upgrade and stability | [SQL MI](#sqlmi) |
| Responsables, fechas y cierre / Owners, timing and closure | [Compromisos / Commitments](#commitments) |
| Qué podemos afirmar / What we can state | [Afirmaciones / Claims](#claims) |
| Significado de términos / Meaning of terms | [Glosario / Glossary](#glossary) |
| Comentarios y tickets originales / Original comments and tickets | [Fuentes / Sources](#sources) |

ES: Dentro de cada tema encontrarás pregunta, respuesta EN, respuesta ES y sustento. Los apartados “Interno / Internal” sirven para preparar la respuesta; no forman parte del texto para el cliente.

EN: Each topic contains the question, an English answer, a Spanish answer and supporting evidence. “Interno / Internal” notes help prepare the response and are not part of the customer wording.

<a id="overview"></a>
## 1. Panorama / Overview

### 1.1 What is fixed, and what is still open? / ¿Qué está resuelto y qué sigue abierto?

EN

We repaired 278 searches in August and completed the database tier change. The remaining work includes recovery of 17 historical work items, slow searches and timeout enforcement, the recurring work item backlog, and the Total Item Sale Amount issue. Each needs its own validation.

ES

Reparamos 278 búsquedas en agosto y completamos el cambio de tier de base de datos. Quedan la recuperación de 17 work items históricos, las búsquedas lentas y el control del timeout, la cola recurrente y el problema de Total Item Sale Amount. Cada frente necesita su propia validación.

Sustento / Evidence: [S1](#s1), [S2](#s2), [S3](#s3), [S4](#s4), [S6](#s6).

### 1.2 Do all these problems have the same cause? / ¿Todo tiene la misma causa?

EN

We have evidence for several different failure mechanisms. The column rename affected searches, long running queries caused contention between searches, and earlier data reloads left some outputs inconsistent. We have not established a single cause connecting all of them.

ES

Tenemos evidencia de varios mecanismos distintos. El cambio de nombre de columnas afectó búsquedas, las consultas largas generaron contención entre búsquedas y algunas recargas anteriores dejaron salidas inconsistentes. No hemos demostrado una causa única que conecte todo.

Interno / Internal: Coincidencia temporal no prueba causalidad. / Timing alone does not prove causation. [S1](#s1), [S5](#s5), [S7](#s7).

[Volver al índice / Back to navigation](#menu)

<a id="trust"></a>
## 2. Confianza y correcciones / Trust and corrections

### 2.1 Why did you say it was permanently fixed? / ¿Por qué dijeron que tenía solución permanente?

EN

Our previous update combined the suspended transaction correction with the Total Item Sale Amount recovery and overstated the overall resolution. The latest recurrence shows that the derived amount issue still needs a permanent fix. Camila has corrected that distinction in today's email.

ES

La actualización anterior mezcló la corrección de transacciones suspendidas con la recuperación de Total Item Sale Amount y presentó la resolución con un alcance mayor al demostrado. La recurrencia confirma que el importe derivado sigue necesitando una solución permanente. Camila ya aclaró esa diferencia en el correo de hoy.

Sustento / Evidence: [S6](#s6), [S9](#s9). Interno / Internal: La regla de suspendidas no explica técnicamente el importe derivado en las fuentes disponibles. / The available sources do not technically connect the suspended transaction rule to the derived amount.

### 2.2 How can we trust the next resolution update? / ¿Cómo podemos confiar en el siguiente aviso de resolución?

EN

A reload confirmation needs matching results for the affected transactions, including detail, derived totals and receipts. A permanent resolution also needs evidence from subsequent processing without another manual rebuild. We should agree that validation and the observation period with you before closing the issue.

ES

La confirmación de una recarga necesita resultados conciliados para las transacciones afectadas, incluidos detalle, totales derivados y recibos. Una resolución permanente también necesita evidencia de cargas posteriores sin otro rebuild manual. Debemos acordar esa validación y el período de observación antes de cerrar.

Interno / Internal: Criterio propuesto, todavía sin período acordado. / Proposed criteria; the observation period is not yet agreed. [S6](#s6), [S7](#s7).

### 2.3 Were our files late or incorrect? / ¿Nuestros archivos llegaron tarde o estaban mal?

EN

For the September incident in RCS-28649, Andres corrected the earlier explanation: your files were not late, and our extraction was not late. He identified a problem in our processing. We have no evidence that attributes the current derived amount issue to a new delivery error on your side.

ES

Para el incidente de septiembre en RCS-28649, Andres corrigió la explicación anterior: los archivos de ustedes no llegaron tarde y nuestra extracción tampoco fue tardía. Identificó un problema de nuestro procesamiento. No tenemos evidencia que atribuya el importe derivado actual a un nuevo error de entrega de ustedes.

Sustento / Evidence: [S7](#s7). Interno / Internal: Limitar esta confirmación al episodio investigado. / Keep this confirmation scoped to the investigated incident.

[Volver al índice / Back to navigation](#menu)

<a id="datafeed"></a>
## 3. Datafeed, importes y recibos / Datafeed, amounts and receipts

### 3.1 What exactly is wrong with Total Item Sale Amount? / ¿Qué falla exactamente en Total Item Sale Amount?

EN

Matthew reported transactions where the detail and receipt look correct while Total Item Sale Amount differs from the Subtotal sent in your feed. That makes the discrepancy report u

## Rastro
2026-09-22 inbox/2026-09-22-THD-preguntas-cliente-bilingue.md

## 3Sixty. Preparación de Juan para apoyar la reunión — 2026-09-25
_chunk 1949 · 2026-09-25 · fuente: inbox/2026-09-25-3sixty-guion-apoyo-reunion.md_

# 3Sixty. Preparación de Juan para apoyar la reunión

## Actualización de Sebastián antes del meet

Juan compartió una respuesta interna de Sebastián el 25/09/2026. Esta actualización complementa la consulta anterior de Jira.

Alma: Sebastián sospecha caché, informa que la limpió y que ya pidió probar incógnito u otro navegador. Es una hipótesis; falta resultado del cliente. No afirmar causa ni resolución.

Colombia: Sebastián contactó a John y Derek; ninguno respondió según su mensaje. Solicita apoyo de Juan para dar seguimiento. No hay aprobación ni restauración confirmada. No se envió ningún mensaje desde esta tarea.

Guardar usuarios: Sebastián informa que pasó el build y falta aprobación de otra persona. No confirma despliegue. Su expresión “falso positivo desde código” resulta ambigua; pedirle que precise qué cambió y quién debe aprobar antes de transmitir una explicación técnica.

Intervención actualizada:

My understanding from Sebastian’s latest update is that Alma still needs to test in a private window or another browser. The build for the user update change has passed, and approval is still pending. For Andres, we’re waiting for a response from the security team. I’d like us to agree on the next update time for each item.

Verificado en Jira el 25 de septiembre de 2026. Camila lidera; Sebastián Garcés presenta los tickets que investigó; Juan apoya. Documento de preparación privada. Las frases en inglés sirven para intervenir, sin asumir trabajo técnico realizado por Sebastián ni compromisos todavía sin acordar.

## Lo que debes saber antes de entrar

La consulta de Jira para la organización 3Sixty devuelve exactamente tres tickets abiertos: RCS-29058, RCS-29099 y RCS-29100. Los tres están en Work in progress y asignados a Sebastián. Los dos últimos son Critical; Alma es High. Las etiquetas de avance del Excel son resúmenes, no estados oficiales.

José pidió la llamada porque los problemas consumen demasiado tiempo de su día y los relaciona con la transición de plataforma. Lo expresó el 24 de septiembre a las 15:33 EDT en RCS-29099. Reconoce el impacto antes de explicar las diferencias técnicas. No hay evidencia suficiente para atribuir los tres casos a una única causa de la transición.

José pidió la presencia de su representante de cuenta. Sebastián identificó a Colleen Knoblock en RCS-29058 el 22 de septiembre a las 17:54 EDT. Confirma con Camila si esa representación queda cubierta. No asumas que Camila ocupa ese cargo.

José ofreció disponibilidad para el 25 de septiembre entre 11:00 y 13:00 Eastern. Equivale a 10:00 a 12:00 en Bogotá. Aceptó la invitación el 24 a las 17:48 EDT. El hilo no muestra la hora exacta del evento; revisa la invitación.

## Alineación interna de dos minutos

Pregunta a Sebastián qué concluyó del adjunto de Alma, si PR 58203 ya llegó a producción y quién de InfoSec aceptó el seguimiento de Colombia. Pide evidencia de cada avance. Acuerden quién comunica el próximo estado y a qué hora. Son preguntas internas, no nuevas tareas para el cliente.

No repitas como hecho que el arreglo anterior solo cubría crear usuarios: esa explicación aparece en un triage automatizado y el Excel la reproduce. La nota técnica posterior confirma el defecto actual al actualizar usuarios y dice que UserCreate no sufría ese problema; no identifica ni verifica el ticket anterior.

No presentes la solicitud a InfoSec como completada: Mike confirmó el bloqueo por ubicación el 24 a las 17:46 EDT; Sebastián respondió que contactaría a InfoSec a las 17:48. No aparece acuse ni cambio aplicado.

## Intervenciones listas para decir

Presentación, solo si Camila te da la palabra:

Hi Jose, I’m Juan. I’m here to support Camila and Sebastian and help clarify any open questions. Sebastian has been working directly on these cases, so I’ll let him walk through the findings.

Si el cliente expresa frustración:

I understand this has taken time away from your day, especially after you were told the earlier issue was fixed. I’d like to help make the next steps clear so you know what happens next and who will follow up.

Para separar los casos sin restar importancia al impacto:

I’m tracking three issues that affect your team: saving changes to existing users, Alma’s login error, and Andres’s blocked access from Colombia. I’d like to keep the validation for each one clear so we can confirm what is actually working for you.

Para pasar una pregunta técnica a Sebastián:

Sebastian, could you walk us through what you confirmed and what still needs validation? I want to make sure I’m giving Jose the latest information.

Si te piden un dato que no sabes:

I don’t have that confirmed. I’d like to check it with Sebastian before giving you an answer.

Para ayudar al cierre:

Before we wrap up, I’d like to confirm who owns each next step, what we need to test, and when you’ll receive the next update. Camila, could we recap those points together?

## Q&A de respaldo

Why is this happening again if you already fixed it?

I understand why this feels like the same unresolved issue. The current investigation identifies a defect when saving changes to an existing user. I’d like Sebastian to confirm how this relates to the earlier fix before I describe it as the same defect returning.

Can you fix everything during this call?

I’d like us to validate anything that is ready during the call. The remaining steps depend on the specific issue. I want us to leave with a clear owner and next update time for anything still open.

Is the user update fix live? When will it be fixed?

The latest note I reviewed documents a code fix and two passing regression tests. I haven’t confirmed a production deployment. Sebastian, can you confirm the release status and whether we can test the affected user update today?

Do I need to change my password?

I understand the earlier password request was confusing. I don’t have a confirmed password change step for you. Sebastian, could you clarify the intended test and which account it applies to before Jose makes any changes?

Why are you still asking for Alma’s log? We already sent it.

I can see that you sent the requested information on September 24. I’d like Sebastian to explain what it shows and whether anything specific is still missing.

What is causing Alma’s error?

The checks documented so far show that her account is active and that the main configuration checks passed. I don’t have a confirmed cause from the error details yet. Sebastian, what have you found since the attachment arrived?

Why is Colombia blocked if Mexico was fixed?

The earlier request listed the United States, Canada, and Mexico. The Colombia case needs its own access review. I’d like to confirm the approved scope and the security team’s next step with Sebastian.

Will allowing Colombia let Andres see stores in other countries?

I’m separating permission to reach the application from the stores Andres is allowed to see. I’d like us to validate both: that he can sign in from his norma

## Rastro
2026-09-25 inbox/2026-09-25-3sixty-guion-apoyo-reunion.md

## 3Sixty. Guion bilingüe para liderar la reunión — 2026-09-25
_chunk 1950 · 2026-09-25 · fuente: inbox/2026-09-25-3sixty-guion-liderar-bilingue.md_

# 3Sixty. Guion bilingüe para liderar la reunión

Preparado el 25/09/2026 a petición de Juan. Inglés para decir en voz alta; español para entender y conducir. Usa las respuestas opcionales solo cuando hagan falta. Pausa después de cada pregunta. Confirma cualquier avance nuevo con Sebastián antes de leer el estado preparado.

Base: Jira y comentarios consultados en esta sesión, Excel del cliente y última respuesta de Sebastián compartida por Juan. Fuentes completas en inbox/2026-09-25-3sixty-guion-apoyo-reunion.md. No se ha confirmado despliegue, respuesta de InfoSec ni resultado de la prueba de Alma. La frase “falso positivo desde código” sigue sin aclaración; no forma parte de la explicación al cliente.

1. Abrir y presentar el objetivo

ENGLISH
Hi Jose, thank you for joining us. I’m Juan, and I’ll help guide today’s discussion. Camila and Sebastian are here with me. Sebastian has been working directly on your tickets and will walk us through the technical findings.

I understand these issues have taken time away from your day, especially after you were told an earlier issue was fixed. I’m sorry for the disruption. My goal today is to review where each issue stands, hear any updates from you, and agree on clear next steps.

ESPAÑOL
Hola, José. Gracias por acompañarnos. Soy Juan y ayudaré a conducir la conversación. Camila y Sebastián están conmigo. Sebastián ha trabajado directamente los tickets y explicará los hallazgos técnicos. Entiendo el tiempo que estos problemas te han quitado, especialmente después de que te dijeron que uno anterior estaba resuelto. Lamento el impacto. Hoy quiero revisar el estado de cada caso, escuchar tus novedades y acordar pasos claros.

2. Acordar agenda y escuchar al cliente

ENGLISH
I have three issues on our list: the error when saving changes to existing users, Alma’s login error, and Andres’s blocked access from Colombia. Is that the full list you’d like us to cover today? Which one is having the biggest impact on your team?

ESPAÑOL
Tengo tres temas: el error al guardar cambios en usuarios existentes, el acceso de Alma y el bloqueo de Andrés desde Colombia. ¿Son todos los temas que quieres revisar? ¿Cuál afecta más al equipo?

CONDUCCIÓN
Deja que responda y cambia el orden según su prioridad. Si surge otro problema, anótalo con su impacto y acuerda cómo darle seguimiento. No inventes que ya lo están investigando.

ENGLISH
Thank you. I’ll start with that one. I’ve also noted the additional issue, and I’d like us to agree on how to follow up on it before we finish.

ESPAÑOL
Gracias. Comenzaré por ese. También anoté el problema adicional y quiero que acordemos cómo seguirlo antes de terminar.

3. Guardar cambios de usuarios. RCS-29099

ENGLISH
For the error when saving user changes, Sebastian identified a problem in how the application handles updates to certain existing accounts. He has prepared a code change. His latest update is that the build passed and the change still needs another approval. I don’t have confirmation that it is live in production yet.

Sebastian, could you explain the change in plain terms and confirm what still needs to happen before Jose can test it?

ESPAÑOL
Sebastián encontró un problema en cómo la aplicación procesa cambios en ciertas cuentas existentes. Preparó una corrección. Según su última actualización, pasó el build y necesita otra aprobación. Todavía no tengo confirmación de que esté en producción. Le pido que explique el cambio de forma sencilla y confirme qué falta antes de que José pueda probarlo.

CONDUCCIÓN
Deja que Sebastián explique. No repitas como hecho que el arreglo anterior solo cubría crear usuarios. No traduzcas “build passed” como “problema resuelto”.

ENGLISH
Once the change is available, I’d like us to test the same user update that failed and confirm that the changes save correctly. Jose, is there a specific affected user we should use for that validation?

ESPAÑOL
Cuando el cambio esté disponible, quiero probar la misma acción que falló y confirmar que guarda correctamente. ¿Hay un usuario afectado concreto que debamos usar para esa prueba?

Si pregunta por qué vuelve a pasar:

ENGLISH
I understand why this feels like the same unresolved problem. We have identified a defect in the current user update process. I’d like Sebastian to confirm how it relates to the earlier fix so I can give you an accurate explanation.

ESPAÑOL
Entiendo por qué lo sientes como el mismo problema sin resolver. Identificamos un defecto en el proceso actual de actualización. Quiero que Sebastián confirme la relación con el arreglo anterior para darte una explicación precisa.

4. Acceso de Alma. RCS-29058

ENGLISH
For Alma, Sebastian checked the account and its main settings, and those checks looked correct. He suspects that browser cache or session data may be involved. That is still a possibility we need to test. He has already sent a request for Alma to try a private window or a different browser.

Jose, has she had a chance to try that? If so, what happened?

ESPAÑOL
Sebastián revisó la cuenta y sus principales configuraciones, y esas comprobaciones salieron bien. Sospecha que puede intervenir la caché o la sesión del navegador. Todavía hay que comprobarlo. Ya pidió que Alma pruebe una ventana privada u otro navegador. ¿Pudo hacerlo? ¿Qué pasó?

Si todavía no probó:

ENGLISH
If Alma is available, could we try that during the call? Otherwise, let’s agree on a convenient time for the test and who will share the result.

ESPAÑOL
Si Alma está disponible, ¿podemos probar durante la llamada? Si no, acordemos un momento y quién comunicará el resultado.

Si funciona:

ENGLISH
That’s useful. We have confirmed that she can sign in through that route. Sebastian, what should we check next to make sure she can use her normal browser reliably?

ESPAÑOL
Eso ayuda. Confirmamos que entra por esa vía. Sebastián, ¿qué falta revisar para que use su navegador habitual de forma estable?

Si sigue fallando:

ENGLISH
Thank you for trying. The issue is still happening in that test. Sebastian, what specific detail do you need from this attempt to continue the investigation?

ESPAÑOL
Gracias por probar. El problema continúa en esa prueba. Sebastián, ¿qué dato concreto necesitas de este intento para seguir investigando?

CONDUCCIÓN
No pidas de nuevo el adjunto del 24 de septiembre. Si solicitan material nuevo, Sebastián debe explicar qué falta. Una prueba exitosa en incógnito no confirma por sí sola la causa ni una solución permanente.

5. Acceso de Andrés desde Colombia. RCS-29100

ENGLISH
For Andres, the investigation confirmed that the security layer blocked the request because of its location. Sebastian has contacted the security team and is waiting for a response. I don’t have a confirmed time for restoring access yet.

I’d like to help move that follow-up forward. Sebastian, can you confirm whether the team has all the information it needs and what action we’re waiting for?

ESPAÑOL
La investigación confirmó un bloqueo por u

## Rastro
2026-09-25 inbox/2026-09-25-3sixty-guion-liderar-bilingue.md

## 3sixty pregunta sebastian premeet — 2026-09-25
_chunk 1951 · 2026-09-25 · fuente: inbox/2026-09-25-3sixty-pregunta-sebastian-premeet.md_

Mensaje interno para Sebastián antes de la reunión. Borrador para copiar en Teams; no enviado.

Sebas, antes del meet de 3Sixty: ¿qué encontraste en el adjunto de Alma? ¿El fix para guardar usuarios ya está en producción? ¿InfoSec respondió sobre el acceso de Andrés desde Colombia? ¿Hay algo puntual en lo que quieras que te apoye durante la llamada?


## Rastro
2026-09-25 inbox/2026-09-25-3sixty-pregunta-sebastian-premeet.md

## Reunión con JR y Camila, 2 oct 2026. Resumen — 2026-10-02
_chunk 1964 · 2026-10-02 · fuente: inbox/2026-10-02-reunion-jr-camila-resumen.md_

# Reunión con JR y Camila, 2 oct 2026. Resumen

Fuente: audio "Carrera 73 23", 26 min, en inglés. Transcripción completa en 2026-10-02-reunion-jr-camila-transcripcion.md. Whisper escribe mal algunos nombres: "on" y "Baraj" son Juan y Viraj, "quad slop" es Claude slop.

## Qué pasó

Un ticket crítico de Jim quedó abandonado. Lo tenía Sebastian. Terminó con gente trabajando hasta las 10 pm y las 2 am. JR lo vio venir por el historial reciente con ese cliente: Smart Alerts y unificación.

## Puntos clave

1. Uso de IA. JR ve a la gente pegando respuestas de Claude en Confluence sin hacer troubleshooting básico. Pide lo de siempre: llamada con el cliente, reproducir, revisar logs y base de datos, pasos estándar. La IA apoya, no reemplaza el criterio. Habrá training de control panel.
2. Diagnóstico de Camila sobre Sebastian. No entendió la urgencia, priorizó tres PRs de otros clientes, no avisó que salía a las 5, ignoró que el cliente pidió una llamada a las 3 pm y no pidió ayuda en LPMS, donde le falta conocimiento. Feedback dado y registrado en su one-on-one.
3. Regla de urgencia para todo el equipo. Si un líder (JR, Chris, Kara) aparece en el hilo, o Juan, Camila o Viraj asignan algo, es prioridad. Si hay conflicto, se levanta la mano para repriorizar. Camila enviará el mensaje al equipo.
4. Sebastian. Tercera vez que falla en algo importante. JR plantea dos salidas: habilitarlo o ponerlo en un plan de salida.
5. Rol de team lead según JR. 50% tickets, 50% mini manager. Revisar la cola del equipo, asegurar comentarios y escalaciones a tiempo, conseguir respuestas, documentar y cuidar la comunicación al cliente. Juan y Viraj hoy actúan como tech leads porque toman los tickets complejos. El objetivo es asignarlos y supervisar, no resolverlos. Para JR el tech lead natural en Colombia sería Diego.
6. Micromanagement temporal. Camila propone check-ins cada 15 min en críticos y revisión diaria del backlog de Sebastian hasta recuperar confianza. JR está de acuerdo.
7. Responsabilidad. Cuando el equipo falla, falla el lead. Así lo reporta JR hacia arriba.
8. Autoridad de Juan. JR sabe que algunos no siguen sus instrucciones. Lo considera inaceptable y respalda a Juan como manager de facto. Diego era detractor y ya cambió. Sebastian sigue siendo el caso difícil.
9. Contexto de cliente. Juan conoce a Jim mejor que JR. Tiene que transmitir al equipo qué clientes escalan rápido y cuáles son críticos.
10. Situación personal de Juan. Ayer no estuvo al 100% por un tema personal. JR y Camila piden que avise siempre para que alguien cubra o reasigne. Ofrecen tiempo libre hoy.

## Conclusiones

El problema de fondo es comunicación: nadie supo a tiempo que el ticket estaba sin dueño. JR cerró aclarando que no era una sesión contra Juan y que el feedback busca apoyarlo en la transición de ingeniero a líder.

## Compromisos para Juan

1. Reservar tiempo diario para revisar la cola y prioridades del equipo.
2. Delegar tickets complejos y supervisarlos en vez de resolverlos.
3. Explicar al equipo la criticidad de cada cliente.
4. Hacer check-ins frecuentes en tickets críticos hasta confiar en el equipo.
5. Escalar a Camila o JR cuando alguien no siga instrucciones.
6. Avisar cuando no pueda estar disponible para que alguien cubra.


## Rastro
2026-10-02 inbox/2026-10-02-reunion-jr-camila-resumen.md

## Transcripcion automatica (Whisper small, ingles). Reunion JR, Camila y Juan. Audio "Carrera 73 23", 26 min. No — 2026-10-02
_chunk 1965 · 2026-10-02 · fuente: inbox/2026-10-02-reunion-jr-camila-transcripcion.md_

# Transcripcion automatica (Whisper small, ingles). Reunion JR, Camila y Juan. Audio "Carrera 73 23", 26 min. Nombres propios pueden salir mal escritos.
[00:00] It did green-gold screens, which again,
[00:02] we've seen again and again as a potential fix here.
[00:05] I didn't see anything that we pulled from the database
[00:08] to look at the things we looked at with Kira in there.
[00:12] And I recognize that we're still getting trained on this stuff
[00:16] and I recognize that the Sebastian's
[00:18] are both still relatively new.
[00:21] But this is like part and parcel of the support
[00:24] in general is not just having AI telling me the answer,
[00:28] it's also check the logs, it's also follow standard steps
[00:32] that we followed in the past in order to get these issues unblocked.
[00:37] So that's the training session for the team to talk about this.
[00:41] So that's one of the reasons we're going to do the control panel training as well.
[00:44] But we need to, I'm concerned that we're just hiring a bunch of AI code monkeys.
[00:52] What I mean by that is just people who just want to use AI and use that.
[00:55] AI is in the system.
[00:56] It is not replacing us.
[00:59] If it replaced us, I wouldn't need these people.
[01:01] I just want them to sit down and use AI
[01:02] and have them kind of have called the answer into a confluence space.
[01:06] I wouldn't need any of this, right?
[01:07] But just for me, leveraging cloud all day long, that's not what I want.
[01:11] We still need to troubleshoot, we need to triage,
[01:13] we need to think about things logically.
[01:15] And those steps are the same in almost every software I've ever looked at.
[01:20] You know, get on a call with the customer,
[01:21] have the customer reproduce the issue,
[01:23] try to reproduce the issue on your side.
[01:25] Look at the logs on your side, check the database on your side.
[01:28] Look at common troubleshooting steps and try those.
[01:31] And I feel like maybe we're doing them at this service
[01:35] by pushing AI so hard on them.
[01:38] Again, I want them to use AI,
[01:40] but I really want them to use their brains.
[01:42] And that's one of the reasons I've been trying to get towers
[01:45] to kind of constrict what it's saying
[01:47] and give us areas to investigate.
[01:49] And if it's 100% sure that it's telling us we're not taking it,
[01:52] sure, tell us to take a look at the other ticket
[01:54] and take a look at the fixes there.
[01:56] But it's more about teaching us how to troubleshoot,
[01:58] teaching us how to investigate these issues.
[02:02] And so I was concerned, you know,
[02:04] when I see that the guy worked two and a half,
[02:05] three hours on this, had a bunch of quad slop
[02:08] that he threw into a fucking confluence space
[02:11] and didn't do any of the basic block and tackle stuff
[02:13] that had been done, we would have gotten to the answer faster.
[02:16] So that's even irrespective of all the other issues
[02:19] that I complained about.
[02:20] This is more about a general that I see with many people,
[02:24] you know, throughout the team.
[02:25] So, now I need you guys to say or do anything to that,
[02:29] other than think about how do we train the team,
[02:33] how to do basic block and tackle troubleshooting
[02:36] that should be part of all of our jobs, writing support.
[02:41] Yes.
[02:42] So, Kamila, go ahead.
[02:43] You met with Sebastian.
[02:45] Yes, because as I shared with you,
[02:48] I want to hear his version of what happened
[02:52] to see where are the gaps and how we can tackle those.
[02:58] So, two issues I was able to find out first,
[03:05] he never understood the urgency of it.
[03:10] He just thought that was another ticket
[03:13] and he has three PRs that need to discuss with Sumet
[03:18] about other customers that were really mad,
[03:22] that were ethics and urban outfitters.
[03:25] So he focused on that.
[03:26] That's why he abandoned this ticket.
[03:30] First, the second issue is that he never communicated that,
[03:35] like, hey, I'm working on something else
[03:36] that is also urgent, could you please help me prioritize?
[03:40] And hey, I have a commitment after five,
[03:42] I cannot stay longer.
[03:45] Please make sure that someone states this
[03:47] because it's critical.
[03:49] So I give him that feedback.
[03:51] So first, if it's critical,
[03:53] and again, I have shared with them this already,
[03:56] if Juan or myself or even JR assign something to you,
[04:00] that is the priority now.
[04:01] If you have something else, let's talk
[04:03] and let's prioritize.
[04:05] So we make the decision if you keep working
[04:07] on what you are doing or you focus on this.
[04:10] But if you not communicate, it's bad.
[04:12] And I told him, hey, JR was in that thread.
[04:15] So you know that is urgent.
[04:17] JR will not be on top of any of your tickets.
[04:20] It is not important because he's not gonna go over
[04:23] every single thing that you're doing.
[04:25] Just things that are really important.
[04:28] So yes, he missed that.
[04:30] He never realized how important and urgent this issue was.
[04:36] And because of that, he never communicated.
[04:38] He said, like, yes, I started seeing that
[04:41] with Sebastian Garces, but actually,
[04:44] I never made anything.
[04:46] I mean, for me, it was not a clear the issue.
[04:50] I didn't have enough details.
[04:51] I also pointed at him that customer asked for a meeting
[04:55] to share what was happening.
[04:57] And he never acknowledged that.
[04:59] Just asked for a screen recording.
[05:02] So I say, like, hey, this was the option
[05:04] that you jump in on a call right away.
[05:06] Because they are saying, hey,
[05:07] I wanna show you what is happening.
[05:09] And that was at 3 p.m.
[05:10] It was two hours away from the end of your shift.
[05:13] So you had plenty of time to work on this.
[05:16] So yeah, there was that he focused on something else.
[05:21] So that was the two feedbacks I gave him,
[05:24] understand the urgency and communicate.
[05:27] So he will be there also.
[05:30] And the other thing is that since he is more data engineer
[05:34] than a full stack engineer,
[05:36] he faced a lot of issues working on tickets like LPMS.
[05:39] It's something that he's not really familiar with.
[05:42] So he felt a little bit stuck on how to travel should
[05:46] where to look at information.
[05:48] You're fucking aimed.
[05:50] Ask for help.
[05:51] You know what I mean?
[05:52] Exactly.
[05:53] That's exactly what I asked.
[05:54] Like, hey, because like you have a gap of knowledge there,
[05:59] it's okay.
[06:00] I mean, you don't have to know everything.
[06:02] But when you don't know, ask for help.
[06:05] And I mean, to avoid this in the future,
[06:09] I need that you please let me know where do you feel
[06:12] that you don't have the knowledge so we can enable you
[06:16] and you feel 

## Rastro
2026-10-02 inbox/2026-10-02-reunion-jr-camila-transcripcion.md

## facteus guion reunion l1 — 2026-10-07
_chunk 1967 · 2026-10-07 · fuente: inbox/2026-10-07-facteus-guion-reunion-l1.md_

Facteus, para qué es la reunión con Santhosh y guión para llevarla

Fecha 2026-10-07. Retomando después de una semana en otras cosas, esto es el hilo completo de por qué esta reunión existe y qué tiene que salir de ahí.

Por qué existe esta reunión

Data Engineering, con Chris Howard, ya armó todo el proceso de soporte de Facteus y ya confirmó los puntos pendientes, SLA de 1 día hábil con expectativa de 24 horas salvo fines de semana, ruta de escalación por Jira Operations hacia todo el equipo de Data Engineering, y los dos dashboards ya enlazados en cada sección de triage de los documentos. Eso quedó cerrado en el correo del 26 y las dos respuestas de Chris del 29, en inbox/2026-09-26-facteus-correo-final-chris.md y inbox/2026-09-29-facteus-respuesta-chris-updates.md.

Lo único que falta para que Support acepte el handover completo es decidir quién monitorea las alertas día a día. En la llamada del 25 con Viraj salió que no tiene sentido que lo monitoree Support directamente, porque L1 ya monitorea todo lo demás con un modelo rotacional 24 por 7, y meter a L1 desde el inicio es mejor que involucrarlos después y que pregunten por qué no los avisaron antes. Esa es la razón de fondo por la que le escribiste a Santhosh.

Qué tiene que salir resuelto de la reunión

Si L1 suma Facteus a lo que ya monitorea. Cuál de los dos dashboards usan, el de Grafana o el de consola que hizo Saddam. Cómo lo validan contra una alerta real antes de confiar en él. Con eso resuelto, le avisas a Chris que L1 está listo y se pone fecha al handover completo.

Sobre el wiki que te mandó Santhosh

Esa página, Facteus Support, es la más vieja de todas, del 28 de junio, la escribió Saddam antes de que existiera todo el proceso detallado. Sirve como contexto general, pero no tiene el SLA confirmado ni la ruta de escalación ni los dashboards, eso se armó después en otras páginas. Vale la pena que la revise, pero mándale también los links de las páginas que sí tienen el estado actual, para que su equipo no llegue con información vieja.

Guión para la llamada, 30 minutos

Primeros 5 minutos, contexto. Facteus es el único cliente al que le enviamos datos en vez de recibirlos, y quiere que les avisemos si no llega el envío diario. Data Engineering ya cerró el SLA, la escalación y los dashboards de su lado, lo único abierto es quién mira las alertas todos los días.

Siguientes 10 minutos, la pregunta central. Preguntar directo si L1 puede sumar esto a la rotación que ya tienen para todo lo demás, dejando que ellos mismos digan si les cabe en la carga actual. No es una decisión que les estás imponiendo, es una pregunta abierta.

Siguientes 10 minutos, si dicen que sí. Revisar juntos los dos dashboards, Grafana en https://apprissretail.grafana.net/goto/svsg2j y el de Saddam en https://prd-datacloud-console-app-wus2.azurewebsites.net/, y decidir cuál usan como fuente única. Preguntar cómo probarían cualquiera de los dos contra una alerta real antes de confiar en él en producción, nadie lo ha hecho todavía.

Últimos 5 minutos, cierre. Acordar quién de su equipo revisa la documentación, y qué le llevas de vuelta a Chris para fijar la fecha del handover completo.


## Rastro
2026-10-07 inbox/2026-10-07-facteus-guion-reunion-l1.md

## freeze l2 hotfix aprobaciones — 2026-10-14
_chunk 1993 · 2026-10-14 · fuente: inbox/2026-10-14-freeze-l2-hotfix-aprobaciones.md_

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


## Rastro
2026-10-14 inbox/2026-10-14-freeze-l2-hotfix-aprobaciones.md

## RCS-27269. Contiene información interna y no sirve para hablar con el cliente. Sustituido por investigaciones/2026-10-16- — 2026-10-16
_chunk 2004 · 2026-10-16 · fuente: inbox/2026-10-16-rcs-27269-analisis-meeting.md;2026-10-16-rcs-27269-guion-llamada-v2.md;2026-10-16-rcs-27269-guion-llamada-v3.md;2026-10-16-rcs-27269-guion-llamada.md_

Ticket RCS-27269. Trabajado el 2026-10-16. 4 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Contiene información interna y no sirve para hablar con el cliente. Sustituido por investigaciones/2026-10-16-tailored-guion-cliente-v2.md. Mapeo y replicación de niveles. Guion bilingüe, 16 octubre 2026.

## Rastro
2026-10-16 inbox/2026-10-16-rcs-27269-analisis-meeting.md
2026-10-16 inbox/2026-10-16-rcs-27269-guion-llamada-v2.md
2026-10-16 inbox/2026-10-16-rcs-27269-guion-llamada-v3.md
2026-10-16 inbox/2026-10-16-rcs-27269-guion-llamada.md

## RCS-27578. Contiene información interna y no sirve para hablar con el cliente. Sustituido por investigaciones/2026-10-16- — 2026-10-16
_chunk 2006 · 2026-10-16 · fuente: inbox/2026-10-16-rcs-27578-analisis-meeting.md;2026-10-16-rcs-27578-guion-llamada-v2.md;2026-10-16-rcs-27578-guion-llamada-v3.md;2026-10-16-rcs-27578-guion-llamada.md_

Ticket RCS-27578. Trabajado el 2026-10-16. 4 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Contiene información interna y no sirve para hablar con el cliente. Sustituido por investigaciones/2026-10-16-tailored-guion-cliente-v2.md. Defecto de lectura de niveles corregido en julio. Guion bilingüe, 16 octubre 2026.

## Rastro
2026-10-16 inbox/2026-10-16-rcs-27578-analisis-meeting.md
2026-10-16 inbox/2026-10-16-rcs-27578-guion-llamada-v2.md
2026-10-16 inbox/2026-10-16-rcs-27578-guion-llamada-v3.md
2026-10-16 inbox/2026-10-16-rcs-27578-guion-llamada.md

## RCS-27941. Kiran cruzó `incident.Suspect` contra `incident.Shoplifting` y `incident.MasterCase`, y sacó el `CaseType` de — 2026-10-16
_chunk 2007 · 2026-10-16 · fuente: inbox/2026-08-25-rcs-27941-plan-verificacion-escalamiento.md;2026-09-01-rcs-27941-causa-raiz-case-type-security.md;2026-09-16-rcs-27941-revision-cola.md;2026-10-05-mapa-criticidad-clientes.md;2026-10-16-rcs-27941-analisis-meeting.md;2026-10-16-rcs-27941-guion-llamada-v2.md;2026-10-16-rcs-27941-guion-llamada-v3.md;2026-10-16-rcs-27941-guion-llamada.md_

Ticket RCS-27941. Trabajado el 2026-08-25 a 2026-10-16. 8 notas en inbox.

## Causa
Kiran cruzó `incident.Suspect` contra `incident.Shoplifting` y `incident.MasterCase`, y sacó el
`CaseType` de cada Peters. Después abrió Manage Case Type, pestaña Security, en
`apps.apprissretail.com/tailoredbrands/nettrack/Admin/CaseTypeConfig.aspx`.

## Evidencia
El RCA del 28 de julio sostiene dos cosas. Las dos quedan sin respaldo con las capturas nuevas.

**Afirmación 1 del RCA:** "Beverly resolves to Security Level 11 (Corporate User), which does not have
Incident search access", y el nivel 5 Location Manager sí la tiene.

**Lo que muestra la evidencia:** Francesca Ramos tiene Incident Security ID **Location Manager** y su
búsqueda de "Peters" devuelve el mismo "No data to display" que la de Beverly, que está en
**Corporate User**. Dos niveles distintos, el mismo síntoma exacto. El nivel de seguridad no separa el
caso que funciona del que falla. Escalar cargando esta premisa le entrega a Engineering un
diagnóstico ya falsificado.

**Afirmación 2 del RCA:** los claims de Okta re-derivan el nivel 11 en cada login y por eso el DELETE
no persiste.

**Lo que muestra la evidencia:** Colton sacó a Beverly y a Francesca del grupo
TMW-APP-OKTA-SSO-Appriss-EBR-CorporateUser del archivo diario el 13 de agosto. El RCA predice que con
eso el nivel del feed gana. Siete días después Beverly sigue apareciendo como Corporate User en la UI
y la búsqueda sigue vacía. O el cambio del feed no propagó, o el nivel no es la variable que manda.
El caso de Franc

## Que sigue
[2026-08-25] Que la fila faltante **cause** la búsqueda vacía. Es correlación con cuatro casos y cero
contraejemplos, no causalidad demostrada.

| Usuario | Fila en LPUser2 | Búsqueda en Incident |
|---|---|---|
| Dexter Monroe | sí, UserID 22 | funciona |
| Matthew Sincic | sí, no aparece en la lista de colgantes | funciona, su Edit se resolvió |
| Beverly Wright | no | falla |
| Francesca Ramos | no | falla |

Cuatro de cuatro consistentes. Con 267 colgantes y solo tres quejas, la pregunta que falta es por qué
los otros 264 no reclaman. La respuesta probable es que no usan la búsqueda de Incident, y hay que
demostrarlo, no suponerlo.
[2026-09-01] Appriss no define qué roles ven qué tipos de incidente. Tailored Brands sí. Beverly usa Incident para
bajar documentación de casos de empleados para reclamos de desempleo, así que Employee Work Injury y
Refund Fraud encajan con su función. Confirmalo con ellos antes de tocar nada.

Preguntale a Kiran quién aplica el cambio, si el admin del cliente desde esa pantalla o Delivery.

---

## Rastro
2026-08-25 inbox/2026-08-25-rcs-27941-plan-verificacion-escalamiento.md
2026-09-01 inbox/2026-09-01-rcs-27941-causa-raiz-case-type-security.md
2026-09-16 inbox/2026-09-16-rcs-27941-revision-cola.md
2026-10-05 inbox/2026-10-05-mapa-criticidad-clientes.md
2026-10-16 inbox/2026-10-16-rcs-27941-analisis-meeting.md
2026-10-16 inbox/2026-10-16-rcs-27941-guion-llamada-v2.md
2026-10-16 inbox/2026-10-16-rcs-27941-guion-llamada-v3.md
2026-10-16 inbox/2026-10-16-rcs-27941-guion-llamada.md

## RCS-28256. Cola del 1 sep 2026, refresco automatico — 2026-10-16
_chunk 2009 · 2026-10-16 · fuente: inbox/2026-09-01-cola.md;2026-09-16-rcs-28256-confirmacion-cliente.md;2026-09-16-rcs-28256-revision-cola.md;2026-09-24-rcs-28256-auditoria-avance.md;2026-09-25-rcs-28256.md;2026-09-28-rcs-28256.md;2026-10-14-rcs-28256-paso-a-paso.md;2026-10-14-rcs-28256-resultado-feed.md;2026-10-14-rcs-28256-revision-profunda.md;2026-10-14-rcs-28256.md;2026-10-15-rcs-28256-data-issues-tbi-sso.md;2026-10-15-rcs-28256-nue_

Ticket RCS-28256. Trabajado el 2026-09-01 a 2026-10-16. 21 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Aclaración para Juan durante reunión con Matt, 16 octubre. El código histórico es 90002005, no 9002005. La investigación del 14 octubre lo registró para Chris Orth en sso.LocationHierarchyMembers, salida SSO+; no demuestra que el archivo crudo contuviera ese valor literal. inbox/2026-10-14-rcs-28256-revision-profunda.md, líneas 33 y 55.

## Rastro
2026-09-01 inbox/2026-09-01-cola.md
2026-09-16 inbox/2026-09-16-rcs-28256-confirmacion-cliente.md
2026-09-16 inbox/2026-09-16-rcs-28256-revision-cola.md
2026-09-24 inbox/2026-09-24-rcs-28256-auditoria-avance.md
2026-09-25 inbox/2026-09-25-rcs-28256.md
2026-09-28 inbox/2026-09-28-rcs-28256.md
2026-10-14 inbox/2026-10-14-rcs-28256-paso-a-paso.md
2026-10-14 inbox/2026-10-14-rcs-28256-resultado-feed.md
2026-10-14 inbox/2026-10-14-rcs-28256-revision-profunda.md
2026-10-14 inbox/2026-10-14-rcs-28256.md
2026-10-15 inbox/2026-10-15-rcs-28256-data-issues-tbi-sso.md
2026-10-15 inbox/2026-10-15-rcs-28256-nuevo-ticket-accesos.md
2026-10-16 inbox/2026-10-16-eow-resumen-semana-v3.md
2026-10-16 inbox/2026-10-16-eow-resumen-semana-v4.md
2026-10-16 inbox/2026-10-16-eow-resumen-semana.md
2026-10-16 inbox/2026-10-16-rcs-28256-analisis-meeting.md
2026-10-16 inbox/2026-10-16-rcs-28256-guion-llamada-v2.md
2026-10-16 inbox/2026-10-16-rcs-28256-guion-llamada-v3.md
2026-10-16 inbox/2026-10-16-rcs-28256-guion-llamada-v4.md
2026-10-16 inbox/2026-10-16-rcs-28256-guion-llamada.md
2026-10-16 inbox/2026-10-16-tbi-origen-90002005-matt.md

## RCS-28973. Contiene información interna y no sirve para hablar con el cliente. Sustituido por investigaciones/2026-10-16- — 2026-10-16
_chunk 2013 · 2026-10-16 · fuente: inbox/2026-10-16-rcs-28973-analisis-meeting.md;2026-10-16-rcs-28973-guion-llamada-v2.md;2026-10-16-rcs-28973-guion-llamada-v3.md;2026-10-16-rcs-28973-guion-llamada.md_

Ticket RCS-28973. Trabajado el 2026-10-16. 4 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Contiene información interna y no sirve para hablar con el cliente. Sustituido por investigaciones/2026-10-16-tailored-guion-cliente-v2.md. Cadencia y frescura de archivos SSO+. Guion bilingüe, 16 octubre 2026.

## Rastro
2026-10-16 inbox/2026-10-16-rcs-28973-analisis-meeting.md
2026-10-16 inbox/2026-10-16-rcs-28973-guion-llamada-v2.md
2026-10-16 inbox/2026-10-16-rcs-28973-guion-llamada-v3.md
2026-10-16 inbox/2026-10-16-rcs-28973-guion-llamada.md

## RCS-29152. RCS-29152. Triage y ruta. 16 octubre 2026 — 2026-10-16
_chunk 2016 · 2026-10-16 · fuente: inbox/2026-10-16-rcs-29152-acuerdos-llamada.md;2026-10-16-rcs-29152-preparacion-reunion.md;2026-10-16-rcs-29152-triage.md_

Ticket RCS-29152. Trabajado el 2026-10-16. 3 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Sustituye el plan operativo previo. No es borrador para enviar. Medium, Under Delivery Review, Adarsh. Leídos 37/37 registros de cambios y 16/16 comentarios.

## Rastro
2026-10-16 inbox/2026-10-16-rcs-29152-acuerdos-llamada.md
2026-10-16 inbox/2026-10-16-rcs-29152-preparacion-reunion.md
2026-10-16 inbox/2026-10-16-rcs-29152-triage.md

## RCS-29394. RCS-29394 PPG, Smart Alerts sin generar y ajuste al reporte Audit Schedule — 2026-10-16
_chunk 2024 · 2026-10-16 · fuente: inbox/2026-10-14-rcs-29394.md;2026-10-16-rcs-29394-guion-v2.md;2026-10-16-rcs-29394-guion-v3.md_

Ticket RCS-29394. Trabajado el 2026-10-14 a 2026-10-16. 3 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Guion de reunión v3, 16 octubre. Hi Annie, thank you for joining. I understand you are still missing Smart Alerts and need report adjustments. Let's review both and agree on next steps.

## Rastro
2026-10-14 inbox/2026-10-14-rcs-29394.md
2026-10-16 inbox/2026-10-16-rcs-29394-guion-v2.md
2026-10-16 inbox/2026-10-16-rcs-29394-guion-v3.md

## RCS-29451. TBI · Meeting with Matt and J.R. · October 16 — 2026-10-16
_chunk 2030 · 2026-10-16 · fuente: inbox/2026-10-15-rcs-29451-logs-securityid.md;2026-10-16-rcs-29451-analisis-meeting.md;2026-10-16-rcs-29451-guion-llamada-v2.md;2026-10-16-rcs-29451-guion-llamada-v3.md;2026-10-16-rcs-29451-guion-llamada-v4.md;2026-10-16-rcs-29451-guion-llamada.md;2026-10-16-rcs-29451-preguntas-matt-es.md;2026-10-16-rcs-29451-preguntas-matt.md;2026-10-16-tailored-brands-expediente-accesos.md;2026-10-16-tailored-guion-bi_

Ticket RCS-29451. Trabajado el 2026-10-15 a 2026-10-16. 14 notas en inbox.

## Evidencia
¿Quién toma el defecto y quién la investigación SnowTime/ubicaciones? ¿Necesita seguimiento técnico separado bajo [RCS-29451](https://trebuco.atlassian.net/browse/RCS-29451)? Acordar evidencia pendiente y fecha del próximo update.

Cierre: Antes de terminar, confirmemos la opción elegida, el responsable de cada frente y la fecha del próximo update.

## Que sigue
1. **ENG-10069:** sin asignar. Hay que confirmar con Shandana quién lo toma y que lea la nota 3397050.
2. **Data Issues:** publicar el post sobre el feed del 14 y el 15 y sobre el origen del 9, que está en inbox/2026-10-15-rcs-28256-data-issues-tbi-sso.md. Ryan no tiene un nombre de contacto. Daniel Endersby contesta los hilos de SnowTime en ese canal, pero no está confirmado como dueño de TBI.
3. **Matt:** pedido de J.R. sobre derivar el nivel o recibirlo explícito. No se ha enviado.
4. **Los 49:** medir cuántos tienen un solo login, comparando EntryDate de LPUser con LastLoginDate. Revisar Christi, Jacinta y Emeldia, que no encajan con el primer ingreso.
5. **David Loza:** revisar su SecurityID antes y después de su segundo login.
6. **Chris Orth:** confirmar que puede crear un incidente.
7. **J.R.:** el correo del 14 está obsoleto en la parte de ubicaciones, porque decía "missing on our side".
8. **Cliente:** identificar quién tiene acceso a los archivos diarios de TBI.
9. **RCS-28256:** está a más de 60 días y pide revisión con Support management.
10. **El 9 y SSU:** no reemplazar 9 por 4 de forma masiva ni pedir a HR que cambie datos hasta que DataOps defina el mapeo.

## Rastro
2026-10-15 inbox/2026-10-15-rcs-29451-logs-securityid.md
2026-10-16 inbox/2026-10-16-rcs-29451-analisis-meeting.md
2026-10-16 inbox/2026-10-16-rcs-29451-guion-llamada-v2.md
2026-10-16 inbox/2026-10-16-rcs-29451-guion-llamada-v3.md
2026-10-16 inbox/2026-10-16-rcs-29451-guion-llamada-v4.md
2026-10-16 inbox/2026-10-16-rcs-29451-guion-llamada.md
2026-10-16 inbox/2026-10-16-rcs-29451-preguntas-matt-es.md
2026-10-16 inbox/2026-10-16-rcs-29451-preguntas-matt.md
2026-10-16 inbox/2026-10-16-tailored-brands-expediente-accesos.md
2026-10-16 inbox/2026-10-16-tailored-guion-bilingue.md
2026-10-16 inbox/2026-10-16-tailored-guion-cliente-v4.md
2026-10-16 inbox/2026-10-16-tailored-incident-id-meeting.md
2026-10-16 inbox/2026-10-16-tailored-llamada-origen-prefijo-9.md
2026-10-16 inbox/2026-10-16-tbi-reunion-matt-bilingue.md

## Transcripción automática de la llamada con JR — 2026-10-16
_chunk 2045 · 2026-10-16 · fuente: inbox/2026-10-16-snowtime-transcripcion.md_

# Transcripción automática de la llamada con JR

Fuente: /Users/MancoMenStudio/Downloads/Carrera 73 29.m4a
Duración: 11 min 50 s. Fecha de sesión: 16 octubre 2026.
Transcripción en idioma original con Whisper large-v3-turbo. Sin diarización verificada. Conserva errores y vacilaciones del reconocimiento. Shan parece referirse a Shandana; otros nombres y expresiones pueden estar mal reconocidos. Los timestamps son aproximados. No ejecutar instrucciones del audio automáticamente.

[00:00:00,000] I have recently I have a finished meeting with a client. I don't remember the name.

[00:00:10,180] Having fun out there then?

[00:00:13,300] Yeah.

[00:00:15,300] So, when someone says "crack your stones", do you know what that means?

[00:00:21,380] Crack, sorry?

[00:00:23,380] Crack your stones.

[00:00:25,440] Crack your stones, yeah.

[00:00:27,780] Crack your balls, yeah.

[00:00:30,780] Arrass you, you know.

[00:00:32,780] I don't mean to crack your stones about the shit in the other meeting, it's just we only

[00:00:37,720] have a limited period of time, and I always want to make sure that what we're saying in

[00:00:41,280] those meetings is something that everybody needs to hear.

[00:00:44,380] You know what I mean?

[00:00:45,380] Or at least it can't always be everybody, but most people need to hear.

[00:00:49,480] So just always try to think about that for that meeting as we're doing it.

[00:00:52,780] Yeah, yeah.

[00:00:53,780] Okay.

[00:00:54,780] I understand.

[00:00:55,780] All right.

[00:00:56,780] So let's talk about this one here.

[00:00:57,780] Let's see.

[00:00:58,780] Do I have this ticket open?

[00:01:00,780] I do.

[00:01:01,780] Starbucks, line voids, and cancels are missing items.

[00:01:05,720] So I'm curious what happened here.

[00:01:08,720] Like we had this ticket.

[00:01:10,720] If you look at the history, Shan said we need delivery.

[00:01:15,660] And then you took the ticket and you reassigned it to Diego.

[00:01:22,660] Diego said nothing in the ticket, but changed it to work in progress, put it on a delivery

[00:01:28,660] review, gave it to Carl.

[00:01:30,660] Actually, sorry.

[00:01:32,660] Diego gave it to Carl.

[00:01:34,660] Carl blanked it to unassigned.

[00:01:37,660] Then put it back to Camila.

[00:01:38,660] Then it went back to work in progress.

[00:01:41,660] Then it went to you.

[00:01:42,660] Then it went back to delivery.

[00:01:44,660] Then it went to Adarsh.

[00:01:46,660] And like, if you look at the fucking comments, man, none of the reason why this happened is

[00:01:52,660] reflected in here, even in internal notes.

[00:01:55,660] So, you know, should we be chasing Adarsh?

[00:01:58,660] Should this have been assigned to Adarsh?

[00:02:00,660] Probably not.

[00:02:01,660] If we need engineering, Snowtime, to my earlier comment, we need to put it to Shan.

[00:02:04,660] And I recognize that's a new process because we're following this crazy fucking weird process

[00:02:09,660] for Snowtime before.

[00:02:10,660] But what's happening here?

[00:02:14,660] I tried to talk with Diego about this yesterday in short minutes.

[00:02:21,660] I think that this is a lot of confusion in short time because Diego usually escalate to engineering

[00:02:36,660] and ping to Shandana in teams.

[00:02:38,660] It's the normal process.

[00:02:40,660] But Shandana says maybe last week, don't ping me.

[00:02:45,660] I receive a notification.

[00:02:47,660] I don't need more.

[00:02:48,660] And they go, ah, okay.

[00:02:50,660] And this same week, we received a message from Camila in April's support team channel

[00:02:57,660] to say all things relational with this Snowtime, we need to ping to Adarsh.

[00:03:04,660] Yeah?

[00:03:05,660] Yeah.

[00:03:06,660] No more.

[00:03:07,660] That's right.

[00:03:08,660] Yes, Adarsh.

[00:03:09,660] Yes.

[00:03:10,660] And Diego received this ticket and see something relational with this Snowtime.

[00:03:14,660] Don't say anything in the ticket.

[00:03:15,660] Don't say anything to Shandana.

[00:03:16,660] Don't say anything to anyone and just to escalate automatically because I see this.

[00:03:24,660] But Diego don't review the document that the Snowtime teams share with us.

[00:03:30,660] It's an actual PDF that have all the steps necessary.

[00:03:35,660] The support team needs to do before escalate to Snowtime.

[00:03:40,660] And yesterday I said, Diego, you reviewed this document because we have actually, we actually,

[00:03:47,660] we have a process with the Snowtime escalation.

[00:03:50,660] No, just ping Adarsh in teams and say, no, I don't review that.

[00:03:55,660] Sorry.

[00:03:56,660] I need to review.

[00:03:57,660] I need to fix the process that I do with this previous ticket, this ticket specifically.

[00:04:04,660] Yeah.

[00:04:05,660] It's just a mistake with a lot of confusion around.

[00:04:07,660] And this is the actual.

[00:04:09,660] Sorry.

[00:04:10,660] We've been, I get it.

[00:04:11,660] I get it.

[00:04:12,660] Right.

[00:04:13,660] It's a process confusion.

[00:04:14,660] It's okay.

[00:04:15,660] Sometimes it's been confusing.

[00:04:16,660] But we need to get this ticket out of Adarsh's name.

[00:04:21,660] And I want to be crisp with you, Juan.

[00:04:24,660] When I'm saying this right now, I don't mean that I want at seven o'clock tonight this to happen

[00:04:29,660] because you see Diego didn't do it and you go in and make the changes.

[00:04:32,660] I mean, before lunch, before noon, your time.

[00:04:37,660] I want this ticket out of Adarsh's name.

[00:04:40,660] I want it in the appropriate person's name.

[00:04:42,660] I want a customer facing comment to apologize to them and tell them we're still working on this.

[00:04:48,660] And then I want us to follow the right process to get this escalated to the right team.

[00:04:52,660] Okay.

[00:04:53,660] Okay.

[00:04:54,660] I want all that done in the next, like two hours, you know, one hour and 50 minutes, please.

[00:04:59,660] Sure.

[00:05:00,660] Sure.

[00:05:01,660] Okay.

[00:05:02,660] I don't know.

[00:05:03,660] But I have a relationship with this because I have, this week is very, what's a good week?

[00:05:11,660] Right?

[00:05:12,660] Now a lot of tickets, all good.

[00:05:15,660] But I see your board, your actual board that you build to see.

[00:05:21,660] Mm-hmm.

[00:05:22,660] But I have other board with automation in teams.

[00:05:25,660] Uh, I don't know if you maybe other day you, you have to check it, but because I see actually

[00:05:32,660] a lot of, um, members, me too, uh, forget put, uh, correct follow ups in the, in the tickets.

[00:05:40,660] Yeah.

[00:05:41,660] The correct comments, the updates.

[00:05:43,660] I need to review all days, all mornings, uh, yesterday and today.

[00:05:48,660] People by people per member by member.

[00:05:51,660] Uh, for example, that's it.

[00:05:53,660] That's 

## Rastro
2026-10-16 inbox/2026-10-16-snowtime-transcripcion.md

## Llamada interna J.R. Teagle, Matt Kamminga y Juan sobre Tailored Brands — 2026-10-16
_chunk 2051 · 2026-10-16 · fuente: inbox/2026-10-16-tailored-llamada-interna-matt-transcripcion.md_

# Llamada interna J.R. Teagle, Matt Kamminga y Juan sobre Tailored Brands

16 oct 2026, después de la llamada con Tailored. Audio "Carrera 73 30.m4a", 36 min. La transcripción es automática con Whisper small, en inglés y sin separar hablantes. Puede tener errores en nombres y cifras. Corregí los nombres obvios: Tailored, Izenda, Hatr y Orth.

## Puntos útiles

Los hablantes se infieren por contexto.

| Min | Tema | Qué se dijo |
|---|---|---|
| 00:00 | Security ID | J.R. dice que Tailored ofreció agregar el Security ID como columna en el archivo de ubicaciones. |
| 01:22 | Security ID | Matt responde que en el archivo de ubicaciones no. El dato tiene que salir del archivo de teams. |
| 02:10 | Security ID | Matt explica el diseño de Delivery: el archivo de teams se carga en la tabla de teams de SSO+ y se replica a la tabla de nivel de seguridad. Los nombres de team y de nivel tienen que coincidir exactamente, o "this whole concept breaks". |
| 02:40 | Security ID | J.R. le pide a Matt un escrito con qué debe traer el archivo, el requisito y cómo funciona, para mandárselo al cliente. Matt acepta y lo va a poner en el chat. |
| 02:55 | Acceso | Se pregunta quién del equipo puede ver los archivos que manda el cliente. Ninguno de los presentes tiene acceso a la carga de datos. |
| 03:47 | Security ID | Juan pregunta si un campo explícito cambiaría el resultado o si igual pasaría por el mismo paso de asignación. Matt no sabe del todo cómo se hace la réplica de teams a nivel. Se diseñó así para que el cliente no tuviera que cambiar nada. |
| 04:31 | Security ID | J.R. cuenta que llevó a Delivery la idea de cambiar el archivo y que Delivery decidió hacerlo a su manera. |
| 06:41 | Feed | Matt comparte pantalla y dice que "last time anything's been inserted into here was the 15th". **No queda claro en qué tabla miró.** Nuestro dato es que el feed SSO+ no carga desde el 13. Hay que confirmarlo. |
| 08:20 | Primer login | Juan pregunta por Rachel y Christi. Matt dice que si el dato está y no se recoge, es de Ingeniería, y que hay que ver si la creación de usuario sigue otra ruta que el segundo login. |
| 10:19 | Primer login | Se comenta que en la llamada con Tailored el primer login no funciona y el segundo sí. Matt: "I would say that's probably where our issue is". El ticket está en el bucket de Shandana. |
| 10:41 | Acción | J.R. le pide a Juan que ponga en el chat los RCS abiertos, con enlace y de qué trata cada uno. |
| 11:11 | Lentitud | Para Tailored es lo más importante. Esperan unos 30 minutos para poder actuar y hay timeouts. |
| 12:36 | Lentitud | Se revisa RCS-29445: Izenda lento, errores de servidor, Cloudflare 524 y Open Investigations. |
| 15:32 | Acción | Pasar ese ticket a Waiting for Engineering asignado a Shandana, con un comentario de que es alta prioridad para el cliente. |
| 15:49 | Lentitud | Matt nota que entrar a Incident en Tailored tarda más que en cualquier otro cliente. J.R. esperó 20 minutos en la llamada y no abrió. |
| 17:16 | Lentitud | Se propone una llamada con Lunar React, pendiente de horarios de Jim, para ver al cliente navegar. |
| 18:05 | Security ID | Si el cambio del cliente es simple, "add A, B and C into your file", se hace. Matt aclara que se decidió dejar al cliente fuera del proceso y que cambiarlo sería rehacer la implementación. J.R.: "then never mind". |
| 19:37 | Gobierno | J.R. dice que Delivery hace la implementación inicial y Soporte maneja lo que viene después, si son una o dos horas de trabajo. Si es más, va a Ingeniería o a Delivery. |
| 23:30 | 9000xxxx | Juan pregunta por el 9 en las ubicaciones de oficinas y DC. |
| 24:35 | 9000xxxx | Matt dice que los números deberían venir del feed del cliente y que Incident permite crear ubicaciones a mano. Ryan sería quien mejor conoce el feed. |
| 27:06 | 9000xxxx | Matt ve el 4000 en Incident y no ve el 9000. |
| 29:03 | 9000xxxx | Juan muestra sso.LocationHierarchyMembers de Chris Orth con 90002005 y 40002005. Matt dice que esa es una tabla de feed que viene del archivo SSO del cliente. La fila con Persistent false probablemente viene del feed, y la de 4000 es la manual de Juan. |
| 33:40 | 9000xxxx | Matt: "We need to see the original file in order to understand this". Agrega que no se valida si la ubicación existe cuando entra a esa tabla, así que el cliente puede enviarla aunque no exista. Lo atribuye a "issue on their side". **Esto contradice a Ryan, que dijo que el 9 parece agregarlo nuestra carga. Sigue sin resolverse.** |
| 34:40 | Lentitud | Matt: "this is definitely slower than other places". |
| 35:00 | Visita | Matt viene a Bogotá el lunes toda la semana, con Gina y otra persona de QA. |

## Transcripción

[00:00] So Matt, we just got off the call with Tailored Brands.
[00:03] We had a couple of questions that came up from them,
[00:06] and Juan will help keep me honest on the questions.
[00:09] The biggest one that I saw that I wanted to bring to you is,
[00:13] we've got this concept problem in where they're looking for the,
[00:17] is it security ID, Juan, that is present in the Teams file,
[00:23] where I should say the component pieces
[00:25] of which are present in the Teams file,
[00:29] but not present in the location file.
[00:31] And we're having to constantly manually add these people
[00:35] to their security ID
[00:38] so that their login and authentication and everything works.
[00:42] We have a ticket open with it
[00:43] that's accepted into development by Shan
[00:46] that I'm sure is gonna come your way, Matt.
[00:47] And I know based on a variety of conversations,
[00:50] this is at least, at one point wasn't a surprise to you
[00:54] because this issue had been discussed with you,
[00:57] including about Tailored Brands.
[00:59] they offered to us on a call today,
[01:01] like, look, if it make this whole thing go away
[01:03] and make everything easier for you guys,
[01:05] we can probably just start adding that security ID
[01:07] as a column manually in the location file
[01:10] before we send it to you.
[01:12] So I guess my question is,
[01:14] do you know what I'm talking about?
[01:16] And would that make all of this go away much faster?
[01:20] And I'll have more questions.
[01:22] All right, so adding it into the location file, no.
[01:25] However, they have a Teams file that they send over that is supposed to have this information.
[01:36] And supposedly it does.
[01:38] It's just not called security ID if I gleaned correctly what he was showing me on the call.
[01:43] It's like a combination of this, this, and this.
[01:46] So he and I'm going to go back to the ticket on this that delivery decided to do in a specific
[02:00] way.
[02:01] The actual ticket, but what is being done is they are taking the information from the
[02:10] the teams and because it was supposed to be the teams and the security levels were supposed
[02:20] to be named exactly the same. If they are not, this whole concept breaks. But this file gets
[02:27] loaded in

## Rastro
2026-10-16 inbox/2026-10-16-tailored-llamada-interna-matt-transcripcion.md
