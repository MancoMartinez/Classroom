# Appriss KT — Topic 1: Customer & Consumer Support

Carpeta 8 de la base de Moscú. 120 fragmentos.

## Reunión 2026-06-04 — Support ticket updates
_chunk 271 · 2026-06-04_

## Resumen
The meeting focused on support ticket updates, migration challenges, and upcoming training. Key updates included the resolution of the TJX ticket escalation, progress on the TBI ticket, and duplication work completed for ticket 154. An escalated ticket remains blocked pending a conversation with Gap, which Chris has scheduled. Vishal and legal are involved in a high-priority ticket, with JR potentially needing to follow up. Migration from Greenplum to Snowflake has introduced issues requiring engineering support, and Dan will soon provide Snowtime training to address these challenges. The team discussed the need for parallel testing during the migration and clarified that the data load process is now managed in Snowtime while the data remains in blob storage.

## Temas clave
- Support ticket updates
- Migration challenges
- Snowtime training

## Decisiones
- **Leave the TJX ticket open for another week to monitor client feedback.** — Clients tend to escalate quickly if expectations are not met.
- **Avoid manual updates to Snowflake tables during migration.** — Engineering prefers automated processes to ensure data integrity.

## Tareas / Action Items
- Confirm if there are any remaining action items or follow-ups needed for the TJX ticket.
- Request a timeline or expected resolution from Chris regarding the escalated ticket blocked by Gap. (resp: Chris Howard)
- Clarify the scope of Vishal and legal's involvement in the high-priority ticket. (resp: JR)
- Ensure the team has access to Snowtime training materials and schedule.

## Insights en vivo (Ask AI / Analizar)
### [Ask AI] Meeting notes
Support tickets 

David reported that the TJX ticket was escalated but has been addressed and is looking better.
Chenuka shared that they are working on a TBI ticket and another in their queue, with internal tickets to follow.
Chenuka explained that the escalated ticket is currently blocked pending a conversation with Gap, and Chris has a meeting scheduled with them.
Peyman informed the group that Vishal and legal are involved in the escalated ticket, and JR may need to follow up with Vishal.
Peyman provided regular updates to the client regarding the progress on the high priority ticket and reported that the backlog is being resolved.
Smeet completed duplication work for ticket 154, which Luke is currently reviewing, and reported no blockers on their end.
Training and migration 

J.R. shared that Dan will provide snow time training soon to help the team address migration-related issues.
Matt explained that recent migration from Greenplum to Snowflake has caused some tickets to require engineering support due to changes in the data load process.
Matt clarified to Carrie that the data load process is now managed in snow time, while the data itself remains in BLOB storage.
It sounds like the TJX ticket escalation has been resolved and is in a better state now, which is great progress. Chenuka mentioned they're actively working on the TBI ticket and others in their queue, but one escalated ticket is blocked pending a conversation with Gap — Chris has a meeting scheduled to address that. Peyman also shared updates on the high-priority ticket, noting Vishal and legal are involved, and JR might need to follow up with Vishal. On the duplication work for ticket 154, Smeet confirmed it's completed and under Luke's review, with no blockers reported on their end.  

On the training and migration side, JR highlighted that Dan will soon provide snow time training to help the team handle migration-related issues. Matt clarified that the migration from Greenplum to Snowflake has introduced changes in the data load process, which is now managed in snow time, while the data itself remains in blob storage.

- For the TJX ticket, confirm if there are any remaining action items or follow-ups needed.  
- On the escalated ticket blocked by Gap, it might be worth asking Chris for a timeline or expected resolution after the meeting.  
- Vishal and legal's involvement in the high-priority ticket could indicate potential compliance or contractual concerns — JR should clarify the scope of their role.  
- Snow time training will be critical for addressing migration-related tickets; ensure the team has access to the training materials and schedule.  
- The shift from Greenplum to Snowflake may require additional documentation or process updates for the team to adapt smoothly.


---

## Transcripción completa
Key and then after that back to In terms of tickets. I don't see any high priority ones and we talked about Alshaya the other day. The other day that those are kind of on hold is my understanding. So good, this one is, what is this one doing? This one doing us an escalated one. Customer review. Okay, perfect. Yeah. So that one might have that as well. I have that assigned to Chris Howard, depending on I'm not planning on how much longer I'm at the company for. Right now that one's kind of blocked by the fact that we need to We need to chat to Dap. Yep. So that's gonna happen, that's gonna happen soon. I think Chris said he's got something I think he's got something on his calendar with them. I'll get an update on that one as soon as I can. Perfect. Payment, did you raise your hand? And yeah, I think, Chanukha, Chinooka, that's the one that Vishal is involved in. Is it more, am I right? Or was talking to them? Yeah, correct. And legal, am I right? Yes. Yes. I just brought it up so JR is a variant in case. In case he needs to follow up with Follow with Michelle or We paid attention to it. You've been babysitting it up to now and now. We just don't want to drop it. Shneko, do me a favor, send me just a brief write up and We'll be right up and teams on it along with the ticket link, please. Let's jump to payment. This is a high priority one with this one. Yeah. That one, I can't do anything about it, but I can't I keep letting the customer know that we are working on it and the And the jobs are running. And that's all I can do. I can't. I can't really push to change production. It's the production, it's the sheer volume of the data. All the data they provide and the fact that we So we've fallen behind. And I'm not sure why we felt behind, but it appears that we felt We fell behind and now we are recovering. I think within a day or two we'll be fine. If you scroll down, my message to the client was that we We caught up to yesterday. And then the ecom part is the part that is This is behind, and you're catching up. So, I gave them 12. I gave them 12 hours ago, I gave them an update before I leave yesterday and today. And today I give them an update. But there's nothing else I can do except Except waiting for a process to run and make sure that we We are processing the files. Okay, we'll just keep Michelle informed. If you run into any other issues with it and need help, make sure that you're asking. All you got under control. It's under control. They haven't complained anything, given that they think. Oh, no, that was just a seven-day warning that I'm not sure what the name of the name of the name is, but I think it's probably the name of the name. We probably can close out. Yeah, I kept it open. Open for, you know, because see these people are very The moment they don't see In the sense, while at the time they expected, they were We will create a ticket and they escalate. I mean, that's their mode. Modus operandus. So far so good. So far so good. Let's just leave it for another week. If you don't hear anything from them, we'll close it. Yeah, well, like you said, they'll reach out next week and open another one. The moment that we miscreate If we miss creating those Incent reports, we will get We will get one. And I'll take a look at it. That's the one that Luke created. Yep. Look, so you've got a couple internal ones, so... Yeah, I think I've assigned it to... And then a bunch of Delhays because those are Those are on the- Yep, you're right. Yep, you did assign them. And then, we'll just sign those over. So, okay. Keep it moving. I didn't see Smeet before I turned on my screen. My screen is made available. I think you should come out here. Okay, hi, sweet. Hi, so my focus right now is 119 and I completed the duplication work for 154. We had a lot of questions about the application. I'll do that, but no blockers from my end. Perfect. All right, and these are waiting for customers. I'm waiting for customer over there. So, and this was an internal one that The kernel one that was escalated. I'm trying to work on it as fast as I can. It's as fast as I can. Mostly these are duplicate tickets, so it takes time. It takes time since it needs clean up on like Snowflake and... And adding any additional code fixes. Fixing, like duplicates and clean, In the same way, I'm trying to do the same thing, but I'm trying my best. Okay, so we did have a few minutes before the end of the The meeting, does anybody have anything they need to discuss about their ticket? We'll talk about their tickets while we have a minute. I don't know if anyone else is noticing it, but since it might be There might be some recent changes and the snow time migrated. I'm noticing a lot of issues popping up at the moment. If heals like when we get to a point where they can be fixed, we're We're like, oh no, hang on, engineering need to deal with that, because it's no time. It loads in snow time now. Is anyone else seeing? Anyone else saying that? That a lot of their tickets are going in that direction. I just don't like this. I don't see anything. So, I think that's the key. Is it related to ALA? I don't remember. I don't know what the... Yeah, that might be true for them. for them in a row. I think that's Alshaya. That's the only one I saw. I haven't seen any ticket anywhere. Plus, I don't have access to your board anyway. I only see things when you respond to I'm going to respond to it on the ticket, on the RCS ticket. I'm not saying anything. Matt, maybe totally unrelated, but Dan messaged me today. I'll talk to you again soon. I'm going to talk to you about, can you explain to me what that is? Everybody reach out to me. Yeah, that's literally what I'm talking about. It's just the end of the episode. The end of the investigation is required changes for that dates load. Data Load, now they're in snow time, their Data Load is managed by Managed by those functions in... Doesn't use the old green plant data load anymore, so go straight It goes from the blob storage into Snowflakes. Snowflake staging, or raw data as they call it, and then into And then into Snowflake from there. So that's all managed in one place now. It's a bit confusing because you need to kind of This is split if it's an existing issue, so did it exist in GreenPlant beforehand? We've got one for We've got one for one, one was caused by the migration, one was existing. So, I'm not really sure what's going on with the game. I'm like, I'm in a spam. I did send him a lot of information today. I'm putting together pieces. He's basically, before all this, he's like, hey, when can I Hey, when can I train your guys on snow time? And I'm like, great, I've asked you this several times. It would be great. It would be great for you to train us on Snowtime and how to make some of these changes. And then he said, I've got a bunch of these issues. I'm going to do the regression. I can't work on the change requests right now. So long story short, And as a story short, we're going to get snow time training soon folks, just heads up. That's all that's up so that we can evaluate and hopefully work on some of these as well. So stay tuned. Hey, man, I know you've asked for that a couple of days. I've been asked for that a couple of times, so just be careful what you ask for. I have a question, like the customer that we are talking about, is it Is it like recently migrated from green plum to snowflake? No more data, fresh data that is in Greenplum. Arjay, I'm a sucker for learning new stuff. I mean, if anything, something is I think something is new, I love to learn it. That's always been my weakness. I'm looking forward to it. I mean, how long I'll be here, I like to learn that stuff. There is only one caveat, even the guys that are fully migrated, I don't know. Don't know if they're keeping the old data loads alive. Live to do like a parallel test for a certain period of time. I think there was something in the Snowtime repo that was Anybody that was talking about that, but there was no specifics on who Who's still being tested, what's still going where, so... Hey Matt, just to confirm, are you talking about The loading of the data or the data itself. The data itself is still in blob storage. So that won't change. That's where it will be forever now. So it's the load process itself that you're referencing is now. In Snowtime instead of Azure. Actually, if I may interrupt you. Right now, we load the data, we get the raw data We put the data into Greenplum. Then Luke has a program that moves that data into Snowflakes. What will they call legacy process? The whole time job or process is to essentially revamp all that. All that. Use Snowflake. And DBT to do all the work that we do. All the work that we were doing before to glue up the data into Greenplunge. That's the job of Snowtime. And as Dan pointed out correctly, Matt, Matt pointed out correctly, they may have to hold on Hold on for a while to both system in order to be able to make sure Make sure that they have the same data. And then, the other thing that I want to talk about is the So they have to load to both systems. So I don't know about that. All of those is pretty It was a really small time business, but that's my two of them. The following information was provided by the Then the customer noticed. So they're noticing things, but also in parallel. Parallel the customers noticing things and therefore we get a ticket so So then that's why I got involved, because obviously the customer gets involved. We're meeting in the middle somewhere. But I think specifically for Alshire, I think at some point. point once the date is fixed they're going to do a full reload which So I think they're going to do that once they get it to like... It's like 99.9% fixed. So if we do get tickets It's very likely that the path you want The path you want to take is to get the mapping fixed or to suggest Or to suggest the mapping fixes to engineering, they'll do that. And don't worry about backfiring. Backfill data, don't try and get data reloaded, definitely don't do it. They don't do any updates in Snowflake, they want to avoid that. They don't want anyone Anyone manually updating the tables. Okay, we're at the end of time. That's about the end of time. Thank you everybody for joining. And if you need anything, reach out. I'm here today, so. So we'll talk to you soon. Thanks, folks. Have a good day. Good thanks. Thanks, everyone. Bye. Bye.

## Reunión 2026-06-11 — Ticket prioritization
_chunk 651 · 2026-06-11_

## Resumen
The meeting focused on reviewing ticket statuses and addressing specific issues across different priorities. It began with a general scan of high and critical tickets, confirming that there were no critical ones under support and identifying one high-priority ticket in Engine Music. Participants systematically reviewed specific tickets, including one related to Foot Locker payments and another involving schema issues on the new platform. Tyrone was tasked with verifying a payment-related ticket to confirm if it could be closed, given that the backlog had been cleared and data seemed caught up. Another ticket involved replication issues and server changes, with the team noting ongoing adjustments and the need for client confirmation before closure.

The discussion also touched on broader platform changes, such as Secure 5 updates, which were causing access and language issues. These were flagged as areas needing further investigation or patching. Participants shared updates on these challenges and discussed potential next steps, including client follow-ups and coordination with Engineering if necessary. Additionally, the team addressed operational matters, such as alerting problems during Vlad's upcoming absence, and identified alternative contacts for specific issues.

The meeting concluded with a collaborative tone, emphasizing the importance of follow-ups, ticket closures, and monitoring platform changes. Participants expressed appreciation for each other's efforts and shared personal updates, such as congratulating a team member on a new baby and discussing upcoming time off. Overall, the meeting was structured and productive, with clear action assignments and a focus on resolving outstanding issues.

## Temas clave
- Ticket prioritization
- Secure 5 platform issues
- Operational coordination during absences

## Decisiones
- **Close payment-related ticket if backlog is cleared and data is caught up.** — Backlog has been cleared and data appears up-to-date.
- **Investigate Secure 5 platform issues further and follow up with clients.** — Ongoing access and language issues flagged during the meeting.

## Tareas / Action Items
- Verify payment-related ticket to confirm if it can be closed. (resp: Tyrone)
- Follow up with client to confirm resolution of Secure 5 replication issues.
- Coordinate with Vlad to identify alternative contacts for alerting problems during his absence. — vence 2026-06-14

## Insights en vivo (Ask AI / Analizar)
### [Ask AI] analiza todo el flujo de la reunion, como se trato, como se llevo a cabo, lo que se msootro, el orden, todo, necesito una estructura de todo lo que sucedio, como sucedio, como se relaciona esto con lo que tenemos en nuestro programa y como afecta nuestras tareas, etc
The meeting primarily focused on reviewing ticket statuses and addressing specific issues across different priorities. It started with a general scan of high and critical tickets, confirming that there were no critical ones under support and identifying one high-priority ticket in Engine Music. From there, the discussion shifted to specific tickets, including one related to Foot Locker payments and another involving schema issues on the new platform.  

Participants worked through each ticket systematically, checking notes, verifying whether delays were customer-related, and deciding next steps. For example, Tyrone was asked to double-check a payment-related ticket to confirm if it could be closed, given that the backlog had been cleared and data seemed caught up. Another ticket involved replication issues and server changes, with the team noting ongoing adjustments and the need for client confirmation before closure.  

The meeting also touched on broader platform changes, like Secure 5 updates, which were causing access and language issues. These were flagged as areas needing further investigation or patching. Overall, the flow was collaborative, with participants sharing updates, assigning follow-ups, and aiming to close tickets where possible.

- **Structure of the meeting**:  
  1. **Ticket prioritization**: Started with a scan of high and critical tickets.  
  2. **Specific ticket reviews**: Focused on Foot Locker payments, schema issues, replication/server changes, and Secure 5 updates.  
  3. **Action assignments**: Tyrone was tasked with verifying payment-related tickets; others were flagged for client confirmation or further investigation.  

- **Key systems mentioned**:  
  - Secure 5 platform: Issues with access, language settings, and stripped-down functionality.  
  - Payment systems: Backlog cleared, data caught up, pending confirmation for closure.  
  - Engine Music: High-priority ticket with schema-related challenges.  

- **Impact on your tasks**:  
  - Ensure follow-ups on tickets flagged for client confirmation (e.g., Foot Locker payments, Secure 5 issues).  
  - Monitor platform changes affecting Secure 5 and replication processes.  
  - Coordinate with Tyrone and others to confirm ticket closures and reduce backlog.  

- **Questions to ask**:  
  - Are there specific logs or reports we should review for Secure 5 replication issues?  
  - What’s the timeline for resolving schema challenges in Engine Music?  
  - Should we escalate any of these tickets to Engineering based on current findings?  

This meeting aligns with your KT priorities by emphasizing systematic ticket reviews, clear action assignments, and collaboration across support tiers.


---

## Transcripción completa
Review as of Monday. It's like payments on that one. That one should be good. Give them another day or so. We've been collaborating within a group of... For now, I'm just trying to figure out solutions for it. So, but yeah, he's in communication. So just since Monday, we're waiting on Jessica to get you some info. I'll give you some information that looks like or just double check. That's pretty much what that one is. This is the Foot Locker Knocker. Not correcting the module. We rolled it out. We're going to do a little bit of a test of it. We do plan to eventually Eventually put them back. It was just... Is this one of them that we did that we did? We didn't do the forced email. This is something different, right? I think that's a different issue. This one was, yeah. Okay. All right. Yes, store and system. Or incident. Looks like it's been too long. So maybe just send them a quick follow-up and let them know that... Now that we don't hear from them, we're just going to close the take That was the ticket. Sorry, I would provide you a little bit of the phrase for what I'm saying. And for one, I would like to thank you all for joining us. Sorry, you're breaking up. I don't know if you need to... I know you're working off a hotspot. The online form of the I'm glad you're over here. You might have to type it, Dean. What we'll do since these are all waiting. They're all waiting on customer. I'm just going to leave it up to you, Dean, to just check on them. Make sure that they're moving along and will move We'll move along to the next person. Seeing any high or critical at all on your list of incident tickets. Anything you want to Anything you've got going on that you need help with? Not at the moment. Just catching up. I was off a few days. Just catching up on any work in progress. We'll be able to get the progress tickets and respond to customers where needed. All good for now. Thank you. Perfect. Thank you. Glad you're back. Thank you. It's been a crazy, crazy week. Also, congratulations and we hope to see baby pictures all throughout the channel. Yes, yes, yes. Oh, I will share, definitely. Always. You know, I love that. Okay. Okay, Tyrone, let's take a Let's take a look at yours. We don't have any high or critical The critical that are under support got We've got one high in Engine Music. This is the one from yesterday. Yep. Can access the new platform, you can access the old platform. Access the old LP guys page. It should be on the new platform. There's some schema stuff missing probably. All right. Looks like I can't put a note in. Yeah. I mean, I can't even get to... I tried a few different ways, but yeah, there's just nothing It is nothing from the front end of the real front end that we're supposed I got the figure out some of the stuff, notes I gave him, so. Yeah. Okay. Okay, perfect. So we'll just wait for him to take a look at that today. We've got today, and then we've got a couple also. Also one with payment, Footlocker, And that's it for today. Hey, I'm just reading That's reading his notes to see if it's really waiting on the customer. If you're just informing them. Yeah, it looks like it's. It looks like it's just a single delay, the identity. They identified it. Backlog has been cleared. So this one, Tyrone, if you could... If you could just double check, I don't see that it's actually waiting on the customer. I'm going to move it to We will be able to do that in the next few days. If you would just check with payment and see if there's really anything more that needs to be done on it. Yeah, I'll send a message to him here later and... Looks to me like it can probably be closed. That'd be awesome. Yeah. Sure the data's caught. That is caught up by now, it's a couple of weeks. Oh, two six. Two six, nine eight four. So just double check on that one if you would. I got that on my screen now, so thanks. Perfect. And then, for PD. This one looks like Looks like we've been waiting on it's set to under customer reason. Also, have a bunch of notes after that. There's other ticket that he's been more commenting on, so we're... Yeah. It's pretty much... Where the Isenda did. There's certain things, and I will meet you with him later today. day, just to kind of be showing like some even some kind of patching stuff in Yeah, some funky stuff with the layers maybe possibly, but I know yesterday they were doing some We're doing so much stuff with Izendus. I'm not sure if it's calmed down a little bit or whatever. Or whatever, so you can kind of go through some replication stuff. But yeah, it's a... It's just been changing a lot, because every time I log in, it's like, because I can tell I can tell when they redo the servers because it goes back to no language which is a weird stuff so I mean they're gonna be probably just Just multiple things that as they're going to figure out with this one, what they can not do for the next ones maybe, or just depending on understanding if a client is just, you know, doesn't Doesn't have Secure 5 yet, and once you do cut people over, there's just certain things that just... I'm not sure what the answer is. The platform that just changed the view and you can't access users. I'm not going to go into the future of this. It just stripped off a lot of things which you would need to get into. In particular, it looks like we just need confirmation from him on On, if there's anything specific he's unable to find, Or, I mean, it looks like we just need confirmation from him on this one that everything's good now. Things good now. Based on this email you sent It still looks off, or if there are any specific reports you're unable to find. So this one, it sounds like we just need to follow up with him. You may be able to close it if he's, if all's good with this one in particular. I know he's working the other one. But it should be good to get this one closed because since it's a high Since it's a high priority one and just... Yeah. Yeah. So. So just want to send him a reminder, hey. Just need to confirm if this one is all good. It's all good now. Okay, the rest of yours. The servers are looking good. That's good. Last but not least, Last but not least... Also, not seeing any high or critical priority ones on your list. More lists of incident tickets, so that's good. Or issue tickets. I stole some of Vlad's time recently. And I've been working on a few projects for him recently, too, which might be why he's been working on a few projects for me and I think taking a couple of sticks. Cosmos tickets. Yeah, yeah. Thank you, blood. I appreciate it. Hope. Yeah, no problem. Yeah, also I'll be off next week, so I'm trying to... I get fewer tickets now. Perfect. Good to know. To know who can I work with on alerting problems when you're out, Vlad? You can speak with Carlos, but depending on what you need to He might not be able to help. He can help with the file alert, but that's... That's about it. And we can speak with Chris Howard. It's how it's about the green plum alerts if you want to speak about that. OK, just send me a quick message, please, with who I can work with, just wrapping up what you said. I hope you have what you said, please, so I can have it for next week. Thanks. Thanks. Hope you're going somewhere fun. Enjoy. Yeah. Staycation. Enjoy. Yeah, exactly. All right. Yeah. Sometimes those are the best. That covers everyone. I don't think we had anything else we needed to do. We needed to cover. Anyone else have anything quick? Love it. Okay, we can all just get back to it. I know we're all really busy this morning, so afternoon, wherever. Whatever time of day it is for you, I know we're busy. I appreciate you guys. Yeah, the time doesn't change the fact of busyness. Exactly. Thanks, Tim. All right. Thanks, everybody. Thank you.

## Reunión 2026-06-12 — Jira ticket expectations
_chunk 656 · 2026-06-12_

## Resumen
The meeting focused on setting clear expectations for the upcoming week, particularly regarding active participation in Jira tickets. Camila announced her absence until Friday, leaving Viraj and Juan as the primary points of contact for any needs or follow-ups. The team is expected to work on at least two tickets before Friday, ensuring internal notes and at least one customer interaction in one of them. Camila emphasized the importance of continuing shadowing activities to better understand ticket handling processes and customer communication.

Access to Snowflake was discussed, with Camila confirming that an IT ticket has been opened to manage access. If unresolved this week, Viraj and Juan are tasked with ensuring completion next week. Additionally, Camila highlighted the need for team members to collaborate with partners who already have access, potentially setting up short calls to facilitate troubleshooting.

Camila also requested support in completing the EF English certificate, urging team members to block 90 minutes on their calendars to focus on the test. Certificates should be submitted by the end of the week, with Camila available for follow-ups via Teams. She expressed appreciation for the team's efforts and encouraged them to reach out if they encounter any issues during her absence.

The meeting concluded with Camila reiterating her satisfaction with the team's involvement and performance, and she promised to review the completed tickets upon her return. She also mentioned sending an email on Monday outlining the expectations and goals for the week, including the test link for the English certificate.

## Temas clave
- Jira ticket expectations
- Snowflake access management
- EF English certificate completion
- Shadowing processes

## Decisiones
- **Team members must work on at least two Jira tickets with specific requirements by Friday.** — To ensure active participation and progress during Camila's absence.
- **Viraj and Juan will oversee Snowflake access follow-ups.** — Camila's absence requires delegation of responsibilities.
- **EF English certificate test must be completed this week.** — Camila needs the certificates for administrative purposes.

## Tareas / Action Items
- Ensure completion of at least two Jira tickets with internal notes and one customer interaction by Friday. — vence 2026-06-12
- Follow up on Snowflake access ticket with IT and ensure resolution by next week. (resp: Viraj and Juan) — vence 2026-06-19
- Block 90 minutes to complete the EF English certificate test and submit the certificate by the end of the week. — vence 2026-06-12
- Collaborate with partners who have Snowflake access to facilitate troubleshooting and ticket handling.

## Insights en vivo (Ask AI / Analizar)
### [Ask AI] yo soy juan el lead, responde enn espanol cual es el resumen de la reunion
La reunión se centró en establecer expectativas claras para la próxima semana, especialmente en cuanto a la participación activa en los tickets de Jira. Camila mencionó que estará ausente hasta el viernes, dejando a Viraj y a mí como responsables principales para cualquier necesidad o seguimiento. El objetivo para el equipo es trabajar al menos en dos tickets antes del viernes, asegurándose de incluir notas internas y al menos una interacción con el cliente en uno de ellos. También se habló de la importancia de continuar con el shadowing para entender mejor los procesos y cómo manejar la comunicación con los clientes. Por último, se mencionó que se está gestionando el acceso a Snowflake, y que Viraj y yo debemos dar seguimiento para garantizar que esté disponible lo antes posible.

- **Acceso a Snowflake**: Camila confirmó que hay un ticket abierto con IT para gestionar los accesos. Si no se resuelve esta semana, debemos asegurarnos de que se complete la próxima.  
- **Expectativas de tickets**: Cada miembro debe trabajar en dos tickets antes del viernes, con al menos una interacción con el cliente en uno de ellos. Esto será revisado por Camila a su regreso.  
- **Shadowing**: Continuar observando y aprendiendo sobre los procesos de manejo de tickets y comunicación con clientes.  
- **Responsabilidad temporal**: Durante la ausencia de Camila, cualquier problema o necesidad debe ser escalado a Viraj o a mí.  
- **Certificado de inglés**: Camila necesita apoyo para completar este trámite.  

Preguntas de seguimiento que podrías hacer:  
1. ¿Hay algún cliente o ticket específico que debamos priorizar esta semana?  
2. ¿Qué nivel de detalle espera Camila en las notas internas de los tickets?  
3. ¿Hay algún deadline adicional relacionado con Snowflake o el shadowing que debamos tener en cuenta?


## Contexto capturado (notas y capturas)
- 📝 **Nota:** Camila's absence next week shifts responsibility to Viraj and the user; Scrum-based planning applies.
  > Posiblemente mencione que Camila no estara la otra semana y el encargado sera Viraj y yo, por si me pregunta que planeo para la otra semana responde en ingles algo logico basado en scrum general que ya maneja la compania

---

## Transcripción completa
It was pretty busy. Pretty busy with JI R&D. Yeah, but I think that it was more like More like a training of Snowflake and Snowtime, I think was really useful. I know that you didn't have access, but But I think that a lot of things clicked, right? Not only that, we were on a call yesterday. For the fixing of ICA and the project as well. So we got the model from that call as well. Yeah, that was great. I know that BRS will not be able to join. So I don't want to take much time from you. I'm from you guys, as I share with you in the We will be back with you in the one-on-ones this week. I do not expect more from you than You can also find a link to my website, And that you have a start like the, the, or Or continue the shadowing to understand the process on the tickets. Keykits and how to communicate with the customers and everything. And start getting into how the process goes, how How also is review the KQL for each of all. So, that's the nature of your partners there. Again, you already know I'm going to repeat this again. I'm going to be out the whole name. I will be back on Friday. Onleaves will be Juan and Biraj. They already know if you need anything, accesses, if you have any issues. If you have any issues, if you need to go because you don't feel well, anything, you can You can ping them to help you. The other thing is that I want to set expectations We will be doing next week. Of course, we're going to keep working with our partners Partners in a Priest, but also I need that you please start reverse chat. Reaver Shadowing. That means that you need to start working on tickets. I want to see you guys, like your actions on the Jira tickets for customers. We are happy to be here with you today. On Friday, each of you have at least worked two tickets. I want to see internal nodes and at least one interaction. We can do one interaction with the customer in two tickets. That is the expectation and the goal. So on Friday when I'm get back, I'm gonna review I'm going to review the GRS that you have worked on. And if I have any comments or anything like really that I That I want to talk with you, I will ask to have some time. If needed, but at least work two tickets. And one of them should have at least one interaction. And then we can do one interaction with the customer. Any questions about that? Any doubts? Whatever comments? Yeah, we need that. We need that facility to improve doing that, so hope that... Early next week we can get those. Which door? It's no blink, for example. Okay, yes. Yesterday he created like a It's like a big ticket with IT to get you... Thank you guys' accesses. This happened today and if it doesn't, it should happen next week. However, I make sure that Juan and Viraj follow up on that. And that, so you have a Snowflake access as soon as possible. I'm gonna send the email I sent. I sent last, this Monday, it was Tuesday. We will be talking about what we have done this week and also this week. And also the expectations for next week, so you have also read it down. Again, if you have any wings, if you participate in anything, please let me know. Please let me know because I'm really into celebrate you guys. And give you kudos when it is placed. And the second thing that I know The one thing I need you help me with is complete the certificate, the English certificate. The English certificate of EF should be taken to test We can detect that takes 90 minutes. It should not take 90 minutes. However, please block your calendar so you focus on the test because you cannot You cannot pause your room. If you don't completed it, you need to You need to start from scratch, so please block the 90 minutes and if you And if you ended before, it's okay, you can You can spend the rest of the time doing other stuff from work, but I hope you can see it. I need that you please Send me the certificate at the end of the week, like before the end of the week. For the end of the week, I'm going to be out. If it doesn't matter, please send me the message on themes. I know that a couple of you already did, Thank you so much. But I should not take that much, only an hour. So that are the two expectations for these weeks. Any questions, any comments about that? I can find that disk. Test link, like where it is. In the App Presupport game. I know we have a bunch of support teams, but ours, no app. New up conversation is a press support. I'm going to send also the link in the email. I'm going to put a email that I'm going to program to be sent on On Monday, you have the two expectations and goals we have for We have for next week, and I'm going to include the link, OK? Great, any comments, anything that you wanna share about I'm going to share about what happened this week, anything that you want to comment Just to know, we can also... I cannot fix or work on tickets. I'm working right now on one ticket about this. I cannot prove it, I cannot replicate it. It's a great way to get a lot of information. Yes, I know that we have limitations on tools. I'm going to push on that today. Again, my expectation is that you have accesses Today, if it's possible, if not, I'm gonna ask B.R. Hwag to push on next week. And next week, however you can work with your partner. If your partner has access, you can... You can set up a call for maybe 15, 30 minutes so you both You both can, with their access, start troubleshooting and So you can review with the help of them. I know they are also really busy, so I know it's complicated, but I'm not sure if it's complicated, but I promise I'm going to push on that today. Okay, thank you. Great team. So thank you so much. Thank you so much. Again, I'm really happy with the work that you are doing. Only good feedback. And feedback, I really am happy seeing you involved. Thank you so much. If you need anything today, please ping me. I'm not going to be available next week, but if you need something next Friday, we can talk. Okay? Thank you, Kamala. Thank you, Tim. Have a nice weekend. Thanks.

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Resumen
_chunk 1189 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

Sesión KT con Kristin Krogman (1h19m, 2026-07-14, transcript oficial de Teams — reemplaza la captura propia). Cubrió las responsabilidades "fuera de la caja" de Kristin que Juan hereda:

1) INBOX help@appriss (compartido con L1): clientes NO en el portal escriben ahí. No se abre ticket automático — muchas organizaciones controlan quién tiene acceso (Walmart exige UN contacto único; ASDA tiene email dedicado para sus stores). Subject con "RCS" = ya hay ticket. Kristin responde desde SU correo (no el de soporte) para dar un contacto de vuelta. Cheat sheet con canned responses por cliente (ICA, Ahold/Zeus, ASDA...) — la compartirá actualizada.
2) Portal de soporte: Customers → Organizations → Add Customer (invite por email). Validar solicitante desconocido con otro admin de la org. Ideal: que abran ticket y L1 lo haga. CSMs reenvían muchas de estas.
3) Verify (Engage) portal: resets (admin → web user listing → checkbox disabled → reset link) y altas con mirror de acceso (foto del original, checkboxes, retailer, teléfono para 2FA). Acceso de Juan pendiente vía Marissa Johnson (o ITHD/Austin). Claims eligibility / void claims → siempre Marissa.
4) Rutina diaria de cierres: revisar completed→close (13-20 tickets), 28-day forced close (pasará a 21), backlog nunca debe tener tickets unassigned fuera de under-review/waiting; "customer says done = close"; dos dropdowns obligatorios al resolver (si no, no completa); la resolución va como internal note en el ticket (no duplicar en el bubble de cierre).
5) Tiger Team: cada ~6 semanas barrido de tickets viejos por assignee, email con lista + última nota (copió a Juan y Camila anoche), internal notes con lo averiguado, Excel mensual a Aimee. Smeet se va al final de esta semana (dejó varios tickets); Sevda con tickets de abril.
6) Datos sueltos: SREs on-call en schedules EU/US (Dean publica calendario mensual); aliases de productos (NetTrack=Incident/LPMS, CAMS=Audit, Verify=Engage); trust portal para docs de seguridad anuales (DHL, Kohl's); Dick's Sporting Goods "archivo faltante"=timing; inbox legacy Retail Client Services solo recibe junk/legal (canned response de Legal, auto-reply activo); truco: buscar el equipo de alguien por sus chats de Teams; docs de sign-off no subidos a Confluence → decidir con Camila.
Próximos pasos: acceso a help@appriss ANTES de estar listo; acceso Verify portal; shadow de rutina matinal viernes 10-11 AM; Kristin comparte cheat sheet, filtros de correo y canned response de Legal. Juan entra a on-call el 17-jul.

## Reunión 2026-07-15 — KT Kristin: casos en vivo help inbox + Samsung readiness · Resumen
_chunk 1241 · 2026-07-15 · fuente: kt-kristin-2026-07-15-oficial_

Sesión KT con Kristin (15-jul, ~36 min): dos casos reales trabajados en vivo, ambos entrados por el buzón help@appriss (correo que también ve L1). Nombres verificados en Jira: Bryant McAnnally (CSM de Lululemon), James DeJohn (Sr. Solution Expert, el "Jim" de sesiones previas), Alyssa Garrison (contacto de Lulu CON acceso al portal), Shandana Khan.

CASO 1 — LULU, upload roto (RCS-27843). Una persona de Lululemon SIN acceso al portal escribió al buzón (su grupo interno debía abrir ticket en el portal y no pudo). Playbook de Kristin: (1) buscó si ya existía ticket — no; (2) validó con el CSM Bryant McAnnally: no es high priority (internamente lo tienen como medium) y según él era tema de training → Solution Expert; (3) creó el ticket manualmente copiando el texto LITERAL del correo, puso a Alyssa Garrison como reporter (sí tiene portal, recibirá las comunicaciones), product type EBR validado con el CSM, problem type "feature functionality question", prioridad Medium; (4) APAGÓ la notificación automática al cliente porque el CSM lleva la comunicación; (5) nota interna "per request of Bryant" explicando el enrutamiento; (6) lo movió a Solution Expert. GIRO: James DeJohn comentó en el ticket que es el mismo bug que DSG — RCS-27806 "Dick's Sporting Goods — User Data is immediately deleted after it is saved" (reportado por él el 13-jul, asignado a Shandana Khan, Under Engineering Review) — o sea bug real multi-cliente en Secure user data, no training → el ticket volvió a Under Support Review y se linkea con el de DSG. Lección: "that's the beauty of having the communication" — el enrutamiento inicial del CSM puede corregirse al cruzar información.

CASO 2 — Samsung 3rd Party Infra Readiness (RCS-27847, ASIGNADO A JUAN). Vineet Saurav (Accenture, Samsung Operations Lead) pidió por correo la validación de infraestructura para el Flagship launch del 22-jul 6AM PST (preventa 22-jul→8-ago, monitoreo reforzado 48h post-launch). Llegó al buzón porque es CONTRATISTA: los clientes no suelen dar acceso al portal a contractors, así que no puede abrir tickets — está atascado. Proceso enseñado por Kristin: soporte NO tiene los datos del cuestionario (load tests, tráfico esperado, scale-up, rate limits, timeouts, fallback/RTO, code freeze) → los tiene el equipo de Infraestructura. Se crea ticket con JUAN como reporter (no hay nadie de Samsung en el portal a quien poner), se adjunta el cuestionario, se mueve a Under Infrastructure Review y — regla de la matriz del 09-jul — EN TICKETS DE INFRAESTRUCTURA SOPORTE SE QUEDA ASIGNADO. Prioridad Low porque no es break/fix ("información necesaria, pero no para ya"). La comunicación con infra va por EMAIL directo (excepción; normalmente no se comunica por email). Seguimiento MANUAL: el status de infra no vuelve solo a Work in Progress — hay que vigilar el ticket. Pendiente de Juan: vigilar respuesta de infra, y responder formalmente a Vineet con el cuestionario lleno antes del 22-jul.

Reglas destiladas de la sesión: el buzón existe para gente fuera del portal (contractors, contactos no registrados); todo trabajo se formaliza como ticket venga por donde venga; validar prioridad y product type con el CSM antes de guardar; copiar el texto literal del cliente; elegir reporter registrado para que fluyan las notificaciones; apagar la notificación automática si el CSM lleva la comunicación; nota interna siempre que el enrutamiento sea excepcional; linkear tickets con el mismo síntoma entre clientes.

## Reunión 2026-07-29 — Luis's introduction and onboarding
_chunk 1411 · 2026-07-29_

## Resumen
Luis, a new team member, introduced himself as a full-stack developer specializing in React and .NET. He expressed enthusiasm about joining the team and shared his preferred nicknames for communication. Camila welcomed Luis and highlighted key team members, including Gulshan, Bikash, Nikita, and Kafil, who leads operations on the NUOP and Appriss sides. It was mentioned that Luis would soon receive Turbo and JAR credentials to manage customer service and related tasks. Kafil briefly confirmed his role and the tools Luis would access.

Later in the session, participants discussed the value of a follow-up session to better understand customer sentiments. The current session was described as interactive and a refresher on handling various customer types. Documentation and ticket management were identified as areas requiring improvement, with acknowledgment that dedicating three hours to such sessions is significant. Feedback was solicited, including suggestions for enhancing future sessions and addressing any shortcomings.

The meeting concluded with reflections on the session's utility and the importance of refining processes related to customer management and documentation. Participants emphasized the need for actionable steps to optimize time spent on these activities and improve overall team efficiency.

## Temas clave
- Luis's introduction and onboarding
- Turbo and JAR credentials setup
- Customer sentiment follow-up session

## Decisiones
- **Luis will be onboarded with Turbo and JAR credentials.** — To enable him to manage customer service tasks effectively.
- **A follow-up session on customer sentiments will be considered.** — To deepen understanding and improve handling of diverse customer types.

## Tareas / Action Items
- Ensure Luis receives Turbo and JAR credentials for customer service tasks. (resp: Kafil)
- Plan a follow-up session focused on understanding customer sentiments.
- Review documentation and ticket management processes to identify improvement areas.

---

## Transcripción completa
on these books, Kabir

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 1/24
_chunk 1190 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

KT meeting-20260714_100400-Grabación de la reunión
14 de julio de 2026, 3:04p.m.
1h 19m 34s
 Juan Martinez inició la transcripción
 Kristin Krogman   0:03 Okay, so let me click that off because I want to show you what I was just doing so that you know that it's there. Ahh. A... Let's see. Okay. Can you see my knowledge tracker?
 Juan Martinez   0:19 Yeah.
 Kristin Krogman   0:20 Okay, so I was just going back and you know, I was working with David before you and I started working together. So what I did is I went back and I'm finding his and my sessions previously. And I'm also adding the video link here.
 Juan Martinez   0:37 Mm.
 Kristin Krogman   0:39 So yeah, so there's, you know, because he and I went through this thoroughly as well, but I thought, well, I might as well add the link, then you've got it. And as a just in case, right? Because as you know, sometimes these knowledge shares, we find something, we go in a different direction, right? It's kind of fluid.
 Juan Martinez   0:40 Oh, okay, great.
 Kristin Krogman   0:59 So I just wanted to make you aware that I'm also putting in links that David and I did when we discussed these things as well. So I am doing that. Okay, so.
 Juan Martinez   1:11 Okay.
 Kristin Krogman   1:15 Let me, I'm gonna close this out. Come on, my little box got in my way again.
 Juan Martinez   1:24 Mmh.
 Kristin Krogman   1:25 There we go. Okay. So what I want to go through with you real quick today is sharing with you one of the things that's kind of outside the box as far as what I do. Okay.
 Juan Martinez   1:38 Okay, right.
 Kristin Krogman   1:41 One of my responsibilities is with e-mail communications with clients. Those e-mail communications can come in directly to me from my inbox, but there's also this help at Appriss inbox. The help at Appriss inbox is with the L1 team. They see this as well.
 Juan Martinez   1:47 Yes. Bring another. S.
 Kristin Krogman   2:00 When an e-mail comes in here, this is where a ticket can be opened. Specifically, like if Yannick, he is a client that we'll hear from a lot, if he would reach out directly to the e-mail, there's going to be a ticket that's open for him. Okay. We have clients that reach out here that are not in the portal. And let me just show you an example. Like here, this Valerie, she reaches out, but she isn't in the portal. And we just don't automatically open tickets for clients. The reason being is because not all organizations want just anybody added to the portal. A lot of these organizations want to keep control of who has access.
 Juan Martinez   2:44 On.
 Kristin Krogman   2:48 They only want specific people opening tickets. And that has to do for a couple of reasons. And I think for the ones that are really strict about it, for example, Walmart, Walmart wants us to have a contact that we deal with directly when it comes to the application. They want one person getting the information from their team saying, hey, we have a problem.

## Reunión 2026-07-15 — KT Kristin: casos en vivo help inbox + Samsung readiness · Transcripción 1/9
_chunk 1242 · 2026-07-15 · fuente: kt-kristin-2026-07-15-oficial_

Llamada con Kristin Krogman-20260715_105416-Grabación de la reunión
15 de julio de 2026, 3:54p.m.
36m 34s
 Juan Martinez inició la transcripción
 Juan Martinez   0:03 Yeah.
 Kristin Krogman   0:05 Okay, so what we have today is I've got a couple of emails that I want to show you how we're going to take care of it. And I'm actually going to forward you this first one. I forwarded you one already, but the one I want to work on first, I'm going to forward this to you so you can look at it while we work. Okay. Do you remember yesterday when I was showing you that help e-mail? That's the one that you're going to need to get access to. There's that extra e-mail that L1 also sees. And then we have to go, okay, so this is one of those.
 Juan Martinez   0:45 Ohh, yeah.
 Kristin Krogman   0:51 Um, come on. that ended up in here. Okay. So this is where I found it this morning, was sitting in that e-mail inbox. And they opened it. They have their own service now where they work through a group that tries to fix things. And if they can't, they're supposed to open tickets with us. Well, instead of following the protocol and doing what they should have done, which was open a ticket in our portal, they sent it here to this help at Appriss, but this person is not someone who has access to the portal. But the person who reported the issue, this Alyssa,
 Juan Martinez   1:30 Okay. Ohh.
 Kristin Krogman   1:35 She does have access. In this situation, because Bryant, right here, he is the CSM, the customer success manager for Lulu. I was just on a call with him asking him about this because I did look to see if there was already a ticket.
 Juan Martinez   1:46 I'm okay.
 Kristin Krogman   1:56 First of all, I searched for a ticket. There was no ticket. So I followed up with him and just said, hey, did I miss it? You know, did you already do something? He said no. And within that conversation, as you can see, escalation requested, right? So it looks like, oh, high priority. Well, in talking with him, this is not a high priority. This is actually even, they've listed it on, because this is their internal information. They've listed this also as medium priority. Okay, so we know now we don't have to have this high priority. And he explained to me, what this actually is about, he's aware of this, and it's actually something that needs to go to a solution expert right off the bat. Okay. As he explained the situation, it's not something that the technical team would work with them on. So anyway, what we're going to do here per his direction is we're going to open a ticket and we're going to assign it or have. Alyssa, she's going to be the reporter on the ticket. And then we're going to get the information over to Bryant as far as the ticket number, because he's going to respond to the customer from here. So he's going to take care of the response to the customer for us. And we're just going to get this set up.
 Juan Martinez   3:04 No.
 Kristin Krogman   3:23

## Transcript oficial — KT Session 17-jul-2026 (rutina matinal Kristin) — parte 1/8
_chunk 1303 · 2026-07-17_


KT Session-20260717_100218-Grabación de la reunión
17 de julio de 2026, 3:02p.m.
27m 7s
621792274320Juan Martinez inició la transcripción
576072292608Juan Martinez   0:03Well, I have a notice, a bad notice. Maybe we can have two sessions today if you have time, because I need, I, Dean maybe put other meeting in 30 minutes. Yeah, need something about engineering things. I don't know if we can have.These first 30 minutes right now, and after today have the other 30 minute sessions for or cover all all these topics, but you see, it's OK for you.
576072292608Kristin Krogman   0:29Oh, yeah. Yes.Okay, so...Yes, so Dean is stealing you away from me at 1030.
576072292608Juan Martinez   0:39A hunky.
576072292608Kristin Krogman   0:40Is that right? 1030? You need to go to Dean's meeting?
576072292608Juan Martinez   0:45Yeah.
576072292608Kristin Krogman   0:46Okay. All right.Just jump in if we hit that time and you need to go, just in case we're on A roll and I missed the time. So you just jump in and tell me.
576072292608Juan Martinez   1:01Okay.
576072292608Kristin Krogman   1:01Okay, so when I start my day...And this morning, of course, I tried not to get going on too many things, but with there being some high priority issues that were waiting, I did have to jump on a couple of things. So I will show you those as we get to them. But when I start my day,I go in and I go through all of my emails, and these are more recent ones. There's an SLA breach. At the moment with the queue being so large, we're not posting these again for the team, but normally when the queue would be lower.we would post when something was about to breach SLA. So normally I would take this one, look at it, and go post it for the team and say, hey, this ticket is about to breach, somebody pick it up. Okay. So I've already looked at these, but.In the morning, I would go through all of these notifications that I've received to see if there's anything that I need to follow up with on the team. Anything happened overnight in the EU, you know, with the UK team, just to see if there's anything that I should follow up on.You know, a lot of these are team messages. If it's something that I need to check the Teams chat to make sure things were followed up on. So it's just, it's constantly just making sure that things are being handled, right? So that's what I do right away is go through and check on this. So.
576072292608Juan Martinez   2:37No.

## Transcript oficial — Retro-RCA Process Review 17-jul-2026 (Dean) — parte 1/9
_chunk 1311 · 2026-07-17_


RetroRCA Process Review-20260717_103359-Grabación de la reunión
17 de julio de 2026, 3:34p.m.
42m 34s
621792274320Juan Martinez inició la transcripción
576072292608Dean Korbakis   0:04I think we were waiting for, was it Diego? Was that the other one?Although I'm not sure. If not, I mean, we can record it anyway. So it'll be, I mean, we are recording it. So it looks like he's away. So yeah, let's go ahead and get started. And then from there, we'll, you know, we'll have this recording. So, okay.
576072292608Viraj Kansara   0:12Okay.Yeah.
576072292608Dean Korbakis   0:29Me.Well, first thing I want to start off with is I'm going to demonstrate.the first part of the steps that I follow to create the documents for the retro and RCA. And as you saw from yesterday's session, the retrospective that we do, oh, there's Jer. Hey, Jer.
576072292608J.R. Teagle   0:53I'm not going to be here long and I might need to steal somebody because our new chief sales officer or whatever said that there's an emergency going on and he's going to need me and somebody from data science on a call. But I'm here until then. So sorry, Dean. Go ahead.
576072292608Dean Korbakis   0:54Yeah.Okay.Oh.Okay.Yeah, no problem. That's totally fine. All good. Yeah, so as I mentioned, starting yesterday, the reason we have the retrospective, of course, is to get everybody who is responsible, or who was involved with the incident that the customer is requesting an RCA on.
576072292608Juan Martinez   1:07Mhm.

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 2/24
_chunk 1191 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

that person they want communicating with us. They just, that's a better flow for them. Okay. So they're just an example of one that, you know, we're not just going to have a store for Walmart reach out to us and say, hey, I can't access. Well, no, they want you to go through your application administrator because he can maybe fix it. Right? Maybe they just need to move something simple that he can do.
 Juan Martinez   3:34 OK.
 Kristin Krogman   3:37 So that's one of the reasons why we have the process of reaching out to people who need help. Now, the other day there was, you know, you can see this, this kind of goes in spurts because here there really wasn't anything that happened. But now you could see my check marks. These are ones that, yep, we had to reach out to them and do something different with it. And how you're going to know is, like right here, there's an RCS ticket associated with it. You can see it there in the subject line, the RCS. So that means that this is being communicated on a ticket. This one, there's nothing there. This one, this person needs help. Okay, so depending on what the situation is.
 Juan Martinez   4:22 Okay. Yeah.
 Kristin Krogman   4:27 A lot of times, they'll just reach out and say, hey, I want to open a ticket. I don't have access. Well, in a case like that, I would send Jeremy a response. And for me, when I do this, I send it from me. I personally, I don't do it from... the support e-mail, I send it so that they then have my contact information by switching it. So then if there's a problem, they've got a contact to reach back out to instead of trying to go through support or the help support because they're not going to do anything there because this person again is not in the portal. So, for Julian, depending on what his, you know, response or question was. Okay. He was having a password issue. Okay. So I would reach out to Julian and in this case, find out some more information from him. Like what was the message you were receiving? I'd go check also, did he really have access to our portal? Because we would see him in there if he had access. So I'd follow up with that sort of thing and take care of Julian that way. So you will see that sort of thing. A better one. Actually, let's go to my sent items and... I can show you. Let's see, here we go. Okay, so ASDA, they reach out to us a lot and as stores. Okay, again, they don't want the stores to be reaching out to us and opening tickets all the time. That's not what they want. And we don't really want it either. Otherwise, we could end up with a ton of tickets. that are duplicate tickets, right? If every all stores are just opening. So for Asda, they actually have requested from us that we give their associates a specific e-mail address that they reach out to, and that's how they take care of when issues come in. So

## Reunión 2026-07-15 — KT Kristin: casos en vivo help inbox + Samsung readiness · Transcripción 2/9
_chunk 1243 · 2026-07-15 · fuente: kt-kristin-2026-07-15-oficial_

in the system for him and assign it right to the solution expert. So this is kind of the exception to the rule. We know what needs to happen already after having conversations with the CSM. So we're going to go ahead and just move it over to them. So I guess I will ask you this. Would you like... me to create the ticket and you just watch again. Would you like to do that before you give it a try? Okay.
 Juan Martinez   3:47 Yeah.
 Kristin Krogman   3:50 So we'll do that. I'm going to move this off of my screen, though, so I can kind of work. And you've got the copy in your e-mail inbox. And just so you know, here's a list of. And she's in the Lulu group. So I went and looked for her and found her here. So we're just going to. Click on Create. Okay, it's a, there's an issue with it. They're having trouble with it. So I'm actually going to create it as an incident. And this is Lulu, so I'm gonna identify which customer it is. And she's saying that she's unable to upload. Issue with uploading. Documents. OK, and then. I'm just taking a copy of what she wrote. And I'm going to put it in here. And the first thing I should have done is I forgot to put her in here. There she is. So now it'll be hers and she'll get communication too that this ticket has been open for her. Okay, product type, this is actually EBR. I validated that with Bryant because it says EBR and engage and I want to make sure. Problem, we're going to put it as feature functionality question on that one. Organization is Lulu. Okay, so we've got that together. We're going to go ahead and create it. I'm going to grab it. Remember, it pops up over here because I want them to know that it's going to be, I want to grab, whoop, come on. just a medium priority. Now, I'm going to back off of this and not do anything because I want level 1 to take it and send the notification to the client that the ticket has been opened so that she gets that. But what I am going to do is I'm going to take this number here, this 27, 843. And I'm going to reach out to Bryant.
 Juan Martinez   6:41 Brian, the CSM, yeah.
 Kristin Krogman   6:43 Correct, CSM. Take a.
 Juan Martinez   6:52 Okay, the first steps in Lulu is the support team from Lulu try to solve the this issue, but if if they cannot solve, send a mail, they help and apple Retail.com and I want you have the the mail to I want. Support, and and you create the tickets after search the the customer name or see the customer name in this case, Lulu, and I think the the person they actually have access to the portal, yeah?
 Kristin Krogman   7:23 Yeah. Yeah, and after talking with Bryant.
 Juan Martinez   7:30 That is Alisa Garzon. Yeah, and after talking to to Ryan to to do a correct triage, no, it's a high priority, no, no, it's a high priority, it's a medium priority, yeah, like a...
 Kristin Krogman   7:42

## Transcript oficial — KT Session 17-jul-2026 (rutina matinal Kristin) — parte 2/8
_chunk 1304 · 2026-07-17_

576072292608Kristin Krogman   2:43Of course, this morning there was an escalated ticket and also a high priority ticket that I ended up having to look at and I will show you those because there was...Nobody had picked up the ticket by the time I started. And I do know I had knowledge about these issues. So I went ahead and grabbed those. And just let me show you. So it was these two tickets that came in.And it has to do with the platform change that's going on right now with incident. So I knew what information needed to be sent out to the client. So I grabbed those and I sent them out.the information that was needed and then there was some information requested by our engineering team so that they could add some different domain to the database to help them out if it was needed. I haven't heard back from them yet and it's been now a couple of hours. SoI'm hoping that the information we provided them as far as they're supposed to be using the old domain still or the old URL, they're not ready to go to the new one. So they just have to be using the old URL at this time. They're okay with that, but obviously I'll follow up with them.just to make sure that everything is okay, but for now, they're good. We caught on to it and sent it off to them. So then...After my checking my emails, I would go into the backlog, which now you and Camila are doing. And the first thing I would do is I look at the summaries just to make sure that there is, you know, the name is there for the company to make it easier on the team, making sure there aren't any high priority tickets that I might have missed, make sure they're getting posted to the team.
576072292608Juan Martinez   4:28No.
576072292608Kristin Krogman   4:45And then I whip through here and make sure that there aren't any engaged tickets, because if there's the engaged ones, those are the ones that LRetailCustomerSupport does not triage. Those are the ones that if it's a password reset or they just need to have someone added and near someone's.their status, you know, and you can mirror that and add them. We take those. Otherwise, it would be Marissa or Shruti in engineering. And Marissa is that solution expert. So, and that's on the documentation as well. They're very easy to reach out to and ask questions, and they know that
576072292608Juan Martinez   5:14Okay.
576072292608Kristin Krogman   5:26the transition is happening. So, you know, feel free to partner with them as well. They're happy to help you. So after I've checked all of that, and, you know, I look at the summaries too, just to make sure that, hey, there wasn't something that maybe should be high priority. And as you guys know, you're going to be checking ticket types.You're going to be making sure that labels are on data tickets, etc. I was going to show you here one of these, this one, actually shouldn't be an SO, it should be an incident. So that one I need to change.
576072292608Juan Martinez   5:58Yeah.
576072292608Kristin Krogman   6:04Because it's actually was an issue.So I'm going to go ahead and change that one to incident.Don't do anything there. Confirm it. Yes, I want to make this change.And there we go.Now it's in, it's the right ticket type. Okay, so backlog, I go to my own tickets. This is just my cadence. It doesn't have to be your cadence, but it's mine, how I do things. And then I would go through these tickets and do what's needed here, whether I need to follow up with the customer again,
576072292608Juan Martinez   6:41Mmh.

## Transcript oficial — Retro-RCA Process Review 17-jul-2026 (Dean) — parte 2/9
_chunk 1312 · 2026-07-17_

576072292608Dean Korbakis   1:27in a session together to get all the information we need to compile that report so then we can provide that root cause to the customer. And what I bring to the meeting, so what we initially started off with, and oh shoot, I don't have it pulled up here. One moment.Um...Is, and I'm gonna share my screen.So there's that.And then here is...This is the document. And what we do is we have two skills that are created. So that Claude has. The first skill is the creating a retrospective document, which is what we're looking at here. And then once that's done, we have an external RCA document thator skill that Claude would create to provide that final version of the information compiled here. So the way I create this is going into Claude and here I have it in.VS code and but however you access Claude and I'm going to use an example here. I'm going to use Lululemon. This is one of our previous ones here that so I'm pretty much starting from scratch. It's one of the older ones that we had. So I would grab, okay, so I know that this was one of the tickets that were.that was involved in that the customer initiated and a lot of our information, the investigation, the resolution, all of that stuff should be, at least how we handled the ticket, what the nature of it was. And so I would drop that in here and I would just say.create a retro using, so I would have the ticket as the first thing here. Second thing is any meeting notes or any conversations that took place, because there could be a lot more information, a lot of back and forth between us and engineering.of the incident and more information could be surfaced there that could be usefully added into the document. So for that, there happened to be a conversation here. This does show meeting and this was just because it was a reoccurrence of the problem, butIf I copy that link here.and drop it here.and send that. It'll go ahead and analyze both sources and then put everything together into a retro document. So now that this will take a little bit of time to run, I'm going to...Walk you through how I, and I'm sure you may, you know, you may have noticed how I was creating the edits or doing the edits during the retro call.And I'll pull up that document here too. So this was the, where you saw me, I just basically use the tools here that's in the PDF to make the edits. And we're saving along the way just to be sure that I don't lose anything we've already talked about. And of course, there was a video that usually you'd want to cover, or I'm sorry, record.those sessions.in case you miss anything in between or, you know, certain notes that you want to cover or go back to. So after I made these edits, of course it was the original copy. Then I want to make a copy of that just so then that way I have the original retrospective that I'm going to force through.to create the RCA.So now I'm sure there's probably going to be a better way than the way I usually run it for when I conduct this process. But I'll just kind of show you what I do. And if there's an easier or probably a smarter way about it, then.By all means, do what you do what you can do, so I'm gonna go back to Claude Code.And I'm going to search for the ticket that we had here.I think it was.So it's this one here. And what I was doing is...I would.I would kind of split the screen up here, and...And it's on this side, and...For example, here.Actually, it looks like I made a newer one. One second here.Okay.So...Whenever there's a change needing to be made to the PDF.I would go in and...request Claude to make the changes. So for example, replacing all appers. So if I wanted to change.This.Yeah.Let me see if I could find it in here.Oh, this platform.It'll be easier once that other one is created, then I can show you exactly how.I go about it.Ohh.Yeah.It's not still wrong here.It.Sorry if this is a little...confusing at the moment here.because I don't want to change this one. I really kind of want this to complete.Well, if it's okay with you guys, hopefully this won't be too confusing. But what I'm going to do is since I have already made the edits and to the main version of this document, I'll kind of step ahead and say, let's say we corrected the edits already and we want to create the RCA. This is the final.version of the retro that I have. This is what I want to have converted over to the RCA document. Then...Now that the...Still doesn't look right.I apologize.Say.Is it?TRE.So this is the one that I finally was using. Let me just make sure.Change Q3. OK, so this is the one.So after all the edits are completed, after the retro call took place, you have all your information. This document's updated, and we want to push to the final version, or well, not final version, but to the RCA, the root cause analysis document. And of course, we would still make edits at that point, too, based onWhen we meet up with the Jr. or you know we review the final document and make any final touches that we need to, what we need to do to create it is simply create RCA from this retro. That way, it's gonna, you'll notice that it's gonna call up.the external RCA skill. There is also an internal RCA.that what we've done in the past is if it wasn't necessarily called out and requested externally, we would still run an internal one. That's totally up to management at this time. If that is something we want to go forward with, where we were, you're going through a similar analysis structure that you would for an external one.but it would have more detail and more of that raw internal, you know, where did we, where did we win, where did we lose, like, you know, what failures did occur, you know, so all the raw detail, the time, all the time stamps of what took place.It's more thorough and actually goes through, especially if you provided A Teams chat, it'll take those time stamps and what was done, what was said during that entire period and analyzes it, and you know, it gives you the idea of...more, you know, from if it's either a coaching or more just of a learning experience on what we did, what we could have done different or better, or what went extremely well, what do we want to continue going forward, those kinds of things that doesthat would provide us that further level of detail than an external one. Now, the one thing to note, of course, with the external one is that, and if you look at the scale itself for the external RCA, is that it has all of the parameters in there to use customer-facing language, of course, making it.Look at, you know, humanly written, and...

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 3/24
_chunk 1192 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

All I have to do is take and send them this little note that says, hey, you know what? Reach out here. This is where they want you to communicate with the team. And then from there, they'll open a ticket. This type of information. I have a cheat sheet for, and I will share this cheat sheet with you. OK, yeah, so anyway.
 Juan Martinez   6:59 OKOK.
 Kristin Krogman   7:08 Excuse me.
 Juan Martinez   7:09 No, no, no worries.
 Kristin Krogman   7:10 So here, I've got my canned response to the stores in here. So, and I try and, you know, put in the client so it's easy to find it, right? We just, we have a few of them. There's ICA. Let's see who else has given us some information here. I'll hold. They've given us some information. It's about specifically when they reach out about Zeus. This just happened the other day. And when you see Zeus, it's like, oh my gosh, what is that, right? Well, it's all right here. This is where they're supposed to reach out.
 Juan Martinez   7:44 Pin.
 Kristin Krogman   7:46 So there's a couple of clients in here. It's going to just be a matter of getting yourself, and I need to take a few things off probably for you at this point, but. Yeah. So I've just got a few notes on here. We'll get it completely up to date. As far as, let me show you from the top. I've started putting this together on here too for you. Just explaining again, what are our products and what are they also known as? because we have clients that will reach out to us and they'll refer to NetTrack. Well, NetTrack is 10 years ago, right? You know it as incident. But if a client says, hey, NetTrack, you're going to be like, what? I don't know what that is. So also known as LPMS or NetTrack.
 Juan Martinez   8:23 Mm. Yeah.
 Kristin Krogman   8:37 audit is also known as cams, you know, and etc. down the line, right? Engage, this is a big one. Client still want to call it verify. So I've put a few of those things on here. And just letting you know, Delivery team implementation, you know, how the company speaks, right?
 Juan Martinez   9:00 Right.
 Kristin Krogman   9:00 Um, if you... are looking for a team, just a trick that I use is I go into the teams chats and I look at. Like here, who does Matt work with? If I'm trying to find somebody and figure out, yeah, figure out what team they're on, I use that. Sorry, Matt, for using you in my demonstration. You know, that's one that I like to do.
 Juan Martinez   9:18 Other organizations, okay. No.
 Kristin Krogman   9:33 I wrote, oh, here. We also have, I'm not sure if anyone's told you this or not, so I apologize if I'm repeating, but I want to make sure I cover it. We also have SREs on duty. So since we, you know, we cover a lot of the time zones, we do have SREs.
 Juan Martinez   10:10 Mm.
 Kristin Krogman   10:10 I want to go into the on-call schedules and take a look at who is working. Okay, and it defaults there for me. So you just want to look into secure.

## Reunión 2026-07-15 — KT Kristin: casos en vivo help inbox + Samsung readiness · Transcripción 3/9
_chunk 1244 · 2026-07-15 · fuente: kt-kristin-2026-07-15-oficial_

Right, right. Just to validate with him. And the reason again for that is because on the e-mail, when they sent the follow-up e-mail that says, hi, Bryant, you know, can you please investigate? That's when they added the help e-mail. And. So I see that they reached out directly to Bryant. That's why I immediately called him because it's like, okay, I'm not seeing a ticket. And Bryant's on here. I want to make sure that we don't cross communication. You know, I want to make sure I know what he's done. This issue maybe had been resolved. He might have reached out to him and you know, everything was.
 Juan Martinez   8:16 Hmm.
 Kristin Krogman   8:23 was resolved. So now you see that it went to under support review already. They've sent out the information, you know, to the client. So now in this situation, again, this isn't normal, right? I am going to put a note in here that it's going to be sent over to the solution expert team per Bryant, right, to let them know that, hey, the ticket is here. It's going over to a solution expert and. you know, per request of Bryant. So then if someone else from the team looks at it and they see that note, they're going to know, okay, Kristin had a conversation with Bryant and this is how this is supposed to go. So that's what I'm going to do. I'm going to go ahead and I'm just going to move this to solution expert. And I am going to send a note to Alyssa. I can't spell when people are watching me.
 Juan Martinez   9:33 Haha. In Super, we only put the ticket in the... we create the ticket, just create the ticket, but Brian is as well to the client or the team. And... Or, or is a support member that respond to the client too, in this case, in this specific case?
 Kristin Krogman   10:13 Yeah. In this specific case, I'm sending it because I know what the issue is that Bryant told me. He knows what this is. This is something he said that they can work with the solution expert on. So I'm going by the direction of him understanding what this is, that this has happened before, and they need some direction from that team. And so anyway, yeah, so he's going.
 Juan Martinez   10:39 OK, yes, it's a rule exception in the in the OK.
 Kristin Krogman   10:44 Yeah, there's exceptions. Normally this would go through support, right? Normally they would do that. Yep. But this one is a little bit different just because of how it came in, the conversation I had with Bryant, etc.
 Juan Martinez   10:49 Hey, this is my question. Okay, okay, great. Thanks.
 Kristin Krogman   11:00 Oh. Okay, let me check my spelling.
 Juan Martinez   11:36 He's the same.
 Kristin Krogman   11:36 It. It had reported. Not about him. Yeah. out to help. We know. Um... Yeah.
 Juan Martinez   12:21 Mm.

## Transcript oficial — KT Session 17-jul-2026 (rutina matinal Kristin) — parte 3/8
_chunk 1305 · 2026-07-17_

576072292608Kristin Krogman   6:50and say, hey, you know, did you receive my last correspondence? You know, here, I know what's going on with these two, because I actually had to touch base with him yesterday. Anyway, I'm just waiting for them to validate that what we went through actually fixed the issue and that we can get those closed.So those are those are good. And then these three are basically the same thing. They didn't have the information to continue to use the old URL. So they're pretty easy ones.
576072292608Juan Martinez   7:21Okay.
576072292608Kristin Krogman   7:21Okay, so after I check that, then the next thing that I look at is the emails that start coming in for, like, we get notified when an automation has been sent to a customer saying, hey, we haven't heard from you in seven days or it's been 14 days.you know, it notifies us to say this ticket's been out there. Dean handles the 14 day notifications and I help out with the Tiger team, which is the older ones. But I also look at these 28 day ones because that's the one that closes the ticket.I think if I heard correctly, I think you guys are actually going to change that to 21 days. But anyway, I go off of this notification, I look at the ticket, and we'll see if there's any reason to reopen it.Okay, so they were sent lots of it. Oh, this is actually an internal ticket. So this one is going to be okay to keep closed. Smeet had reached out to Luke and let him know that he had finished the stuff that's all that he requested to have cleaned up. So this is okay. And like I said, it's internal.
576072292608Juan Martinez   8:36Yeah.
576072292608Kristin Krogman   8:38So we will leave that one alone. Remote that.And then...For myself, I mark it complete so that I know, yep, I looked at it, it's done.Okay, TJX, we'll take an extra look at this because TJX is a high priority customer and we want to make sure everything's good with them. So this one.
576072292608Juan Martinez   8:59Yeah.
576072292608Kristin Krogman   9:05We'll take a double check at same thing. Oh, this is the RTI portal. Okay.Yep, this one, this is 1 where you don't need to follow up with anybody and go, hey, do we need to reopen, whatever. This one will be good. This one can stay closed.And most of the time with the RTI portal, when it's asking about access, those are ones that the links get sent out, everything is good. A lot of the times the customers don't respond back and say, hey, you know, it's all great, thank you so much. If they could get in.If they could not get in, then they would reach out again. So usually okay with just keeping it closed. If you have, you know, like if you see a couple of those from the same customer, you might want to go, hey, Tom, is everything okay with this? Should we keep it closed or should we reopen it? Would be my suggestion.
576072292608Juan Martinez   9:46Okay.Can you?

## Transcript oficial — Retro-RCA Process Review 17-jul-2026 (Dean) — parte 3/9
_chunk 1313 · 2026-07-17_

576072292608Juan Martinez   11:59Ohh.
576072292608Dean Korbakis   12:04Using not using our internal jargon or our internal verbiage and things that we do or translates it appropriately and.And it produces a pretty decent document. Now, there still could be some tweaks along the way that may be needed to the skill, as I have done, you know, kind of periodically throughout the time using the retro skill. But otherwise,it'll produce that final document. Let's go back and see if this is, all right, now finally it has all the data it needs and it's compiling it. Go ahead. Yes.
576072292608Juan Martinez   12:40Jain.Sorry, just for be sure, who wants the final review before to the goes to the customer, the super engineer or CSM?
576072292608Dean Korbakis   12:52So, at this, what we've done today, or up to this point, is that our manager would be involved. So, in your case, it would be Camila, and then also partner with Jr. So, I think that at least the structure that we've had up to this point is your...your direct manager, then the director of VP or VP, you know, so in this case would be Jr. And then once that's, and then also you'd want to have a final pass from the owner of the department that handled the issue. So if it was engineering or maybe then it would be the engineering manager.If it was engaged, then it'd be the engaged manager. So you'd want to make sure that they're okay and they're, you know, everything is 100% in their opinion as a pass, as well as our group, you know, the manager and VP, and then from there would go out.
576072292608Juan Martinez   13:51Okay.Yeah.
576072292608Dean Korbakis   13:54And then depending on how it was requested would be the way it would be sent out. So if it was requested through the ticket, or in some cases, I've had L1 create a ticket and say, you know, FYI, there's a request for an RCA from this customer, and then I would send it that way. In some cases, the CSM is involved.So...That part, as far as sending it out, could vary depending on the case, but that would be the approval process at that point, so...Yeah.
576072292608Juan Martinez   14:32Okay, okay, okay, I got it, I got it, and and and where is the the trigger for doing extra than RCN? No, does the customer have to request it or doesn't every P1 get one one automatically?
576072292608Dean Korbakis   14:34Sure.We usually go by request. So I mean, we try to recap it in the ticket itself to kind of avoid having to go to the extreme of analyzing the way we are with these. But yeah, that typically, you know, if we can articulate it well within the ticket and it's acceptable to the customer, then
576072292608Juan Martinez   14:47Akgun.
576072292608Dean Korbakis   15:06Uh, that's how we, you know, that's the route we take at that point then, so, uh...
576072292608Juan Martinez   15:13Okay, thanks.

## Topic 1 · KB Support Operations — Customer Support — Equipo US 🇺🇸
_chunk 174 · 2026-06-03 · fuente: /Users/MancoMenStudio/Desktop/Topic1_Support_Operations_KB.html_

Kristin Krogman
Sr. Business Process Analyst
📍 Minnesota · Mano derecha de Aimee
✓ Conoce todo Appriss (no-producto)
⚠ A veces negativa / no ve el panorama
APIS SME
Dean (Constantine) Korbakis
Lead Support Engineer
📍 Chicago
✓ Conocimiento de Incidents excepcional
⚠ Follow-through sin recordatorios
Incident Audit/Legacy SME Secure Data
Carrie Allison
Sr. Support Engineer
📍 Minnesota
✓ Ética de trabajo
⚠ Sensible, toma todo personal
Secure Incident Data
Tyrone Whitney
Support Engineer
📍 Minnesota
✓ Don de gentes; hace sentir importante al cliente
⚠ El mismo don de gentes 😊 (habla de más)
Incident Izenda SME Secure
BJ Probert
Support Engineer
📍 Wyoming
✓ Meticulosidad
⚠ Se distrae con facilidad
Secure Incident Data

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 4/24
_chunk 1193 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

Say DevOps, let's take a look. What do we have? See, there's EU and there's a US. So if you're looking for someone in the US, you just click on it, you can view their schedule. And then it's going to show you, okay, here we are on the 14th, Jason Robinson. So you know who you can reach out to.
 Juan Martinez   10:38 Okay.
 Kristin Krogman   10:52 If you're posting on Teams and you're not getting help, this is the person that's supposed to be responding to you.
 Juan Martinez   10:58 Okay, great.
 Kristin Krogman   10:58 So yep, and you guys as a team, I mean, Dean shares this with the team monthly. He'll like put out the whole calendar for July in an e-mail. So if somebody wants to come in and do that for your teams, you can do the same thing. You just look at it for a month and then take a, you know, take a picture of it up here. I don't know exactly how he does it, but he's able to get... Oh yeah, it is. It's showing the whole month. So then you can see the whole month, which is really nice to have because then you just got it in your e-mail, you just go click on it, it's right there, right? I save it in my...
 Juan Martinez   11:35 I am at the end of the line, Jain. For the alcohol.
 Kristin Krogman   11:39 DM Yep, there you are. You're pulling double duty.
 Juan Martinez   11:43 I start in 77 in of Julie, yes.
 Kristin Krogman   11:48 Oh, that is, that is you for real?
 Juan Martinez   11:50 Yeah, yeah, and on call, yeah, this is on call, yeah, yeah.
 Kristin Krogman   11:52 Yeah. Yeah. Oh, wow, good for you. You're moving on and up in the world.
 Juan Martinez   12:00 Yeah.
 Kristin Krogman   12:00 Okay. Okay, so anyway, so here are, so that's the calendar, SRE, so you know what that is. And then here are some of the people that if you need help during the day, I've found have the team leads that'll direct you in the correct way. A lot of times those guys will say, hey, you know what, yep. just assign that over to me or whatever it may be. So they're the ones that you might need to reach out to. Engage tickets, those go typically to Marissa Johnson as the solution expert if they need things like, you know, Customer needs access to the portal, but to the to the engage portal, we have several portals. But... There's more information that you need other than just copying a certain person's access that she would understand, right? As long as you know, if they give you the information like on my documents where they say, hey, copy this person's access and give it to Juan. Yeah, that's easy. You know, to go in there, you can copy it. but they might ask for some specific things within Engage that support doesn't know. And so then Marissa would have to do it. So that would be anything in the support portal that you can't complete would go to Marissa, or we get tickets that are, they're called claims eligibility.

## Reunión 2026-07-15 — KT Kristin: casos en vivo help inbox + Samsung readiness · Transcripción 4/9
_chunk 1245 · 2026-07-15 · fuente: kt-kristin-2026-07-15-oficial_

I, I'm not sure, is maybe you probably asked for this, that's these questions, but I have need to you, you, you, you just move into a solution into a solution expert, yeah, and that queue wasn't in the status walkthrough with the gesture right now, and with...
 Kristin Krogman   12:24 Yeah.
 Juan Martinez   12:41 When do I wrote something to solution expert instead of Delivery or Engineering, and who on that team is that Marissa Johnson, for example, group on the engage side?
 Kristin Krogman   12:56 Okay. Well... Hold on a second. Okay, well now he's decided, now Jim saw it and he's decided that this is going to be... We're going to put it through Support. It. Okay. Sometimes you just gotta go a different direction. I'm just gonna let Jim know. Okay, somebody's gonna. Um... Okay, so yeah.
 Juan Martinez   15:51 Hmm, it was like a little confusion with the current team, I think, for this ticket.
 Kristin Krogman   15:57 Yeah, yeah, Bryant was, Bryant was sure it was supposed to be with the solution expert due to this happening before, and he thought they needed to just train the team on what data was coming through with the correct information, because he said there was some problem within the data that they found before. And anyway, so that's why he felt it needed to go to solutions expert because it just needed training. He's saying it's different, that there was something yesterday. So. he sees something different and maybe Bryant didn't know that, that it ended up going back to supporter engineering. So that's the beauty of having the communication, right? So we stopped it before anything happened. Now it goes into support review. Support will look at it. And what I'll probably do. is see if I can find the DG ticket that would match up with this one and I'll link it. So that would be my next step. So we could...
 Juan Martinez   17:02 Okay.
 Kristin Krogman   17:07 Let's see. We'll go, no, I don't want to do that. I want to go into my filter because you never know. You can go into the company and search for tickets, but what it doesn't do is it doesn't show you if somebody internally opened a ticket and was working on an issue. If you want to see, like Jim opened a ticket here. For um, DG yesterday. And, or not yesterday, I don't know when he opened it. He opened it. He is not in their organization in JIRA. So if I went and looked at them under the customer section here, it wouldn't show as a ticket because he's not a part of their group. He's a part of Appriss. So that's why I look for tickets. I come here and I look.
 Juan Martinez   18:01 And.
 Kristin Krogman   18:02 Okay, let's see. Well, this was just yesterday, so maybe this is the one. Let's take a look. To data upload. Yep. So this is it. So 27806. Okay, so I'm in a link. Why is that there? What just happened?
 Juan Martinez   18:59 Yeah.
 Kristin Krogman   19:06 Um, relates to. And then I want that Lulu ticket. It was 27 or the Dick's sporting good one.

## Transcript oficial — KT Session 17-jul-2026 (rutina matinal Kristin) — parte 4/8
_chunk 1306 · 2026-07-17_

576072292608Kristin Krogman   10:02Okay.So now we finished that one.All right. So as I was going through the emails, one of the things that I saw was there was an update that a CSM had made. We get the alerts when a customer success manager comments. And so on this one, Paul put the at mentions in there for Carl.And Jim, and just saying that the fix was done right? Well...What is supposed to happen is this should get assigned to the original assignee in support so they can test it. And since he's reaching out to these two guys.Dean may or may not see this, right? Because Dean is the original assignee. So I just let Dean know. I reached out to him and said, hey, this ticket's out here. You know, if you could take a look at it, look at the communication from Paul and take care of this and update the customer would be great because the customer needs an update regardless.because it's been a while. So Dean is going to take care of that.So those are some of the things as far as the e-mail that I go through in the mornings to validate and check. If I had specific communications that I sent out the day before to customers, and I know I need to follow up and make sure that they got help,Those would be things I would go through too. And when I say that, I'm talking about the communications that are sent from L1 to us that you guys will start seeing. And I've been copying you on what I've been responding to customers. Those I will follow up on as well as needed. And the help at Appriss e-mail.I go in here and check and make sure there isn't anything new. Fridays are usually pretty quiet for this one. I typically don't see a lot on Fridays, but I just go through, make sure that I didn't miss something too at the end of the day. But this is the last one that came through that he needed help.So this was someone that I responded to. Again, I had sent and copied you guys as well. So there's Joshua. And then I copied Corey Hendrick on it. And I actually did hear back from Corey.So, Corey.Sent me a note.And he, you know, said, thanks, and he's going to take care of it. Okay. And that'll happen for you a lot, especially when you're, you know, putting yourself on there. And it's actually kind of nice because you get to know some of the other, some of the customers and you kind of understand how they work as well.
576072292608Juan Martinez   12:43And.Oh.
576072292608Kristin Krogman   13:03you know, Corey is somebody who's right on top of things, right? I mean, he got back to me really quick, told me what he was going to do. He's someone we've worked with a lot at TJX or the Home Depot, sorry. We hear from the Home Depot A lot. But yeah, it's just nice to know that there's a contact there because if you have
576072292608Juan Martinez   13:16Oh.
576072292608Kristin Krogman   13:23an emergency, something's coming up, you know, hey, this guy will respond. Let's get a hold of Corey, right?So that's nice for me anyway.Okay, so after I've checked all of my emails, I've looked in the backlog. I've...checked my own tickets to see what kind of updates I maybe need to make. I'm constantly checking here. I'm in here a lot, just looking, just making sure. Again, you know, we're super high. We all know why we're super high.
576072292608Juan Martinez   13:50Okay.
576072292608Kristin Krogman   14:01Um...And towards the end of the day yesterday, it really jumped up a lot. So I did reach out to the team and said, hey, you know, we got to get the shadows on this. We got to get them taking some of these tickets. So if you guys see some, let's make sure we're getting them assigned, et cetera. Because we do have a few tickets that are coming up on these two.are almost a week old, these ASIC ones. This one popped back up down here. Why?That's weird.

## Transcript oficial — Retro-RCA Process Review 17-jul-2026 (Dean) — parte 4/9
_chunk 1314 · 2026-07-17_

576072292608Dean Korbakis   15:14All right. So going back to the Wegmans one, the one we talked about yesterday, it went through, it created a DRCA, it gave us this template. It'll go in your OneDrive, or unless you specify a particular file. I usually like doing the OneDrive, so then that way.It's shareable with, you know, you can usually, you know, then send it to, you know, if it would be Camila or Jr. It's, you know, you can share that live document and then as you make updates to it, it'll show and reflect it on their site as well. So with that being said,I can, I'm gonna go ahead and open this.Um...Okay.So it landed here.And so this is our final document.And then.So you can kind of see how it cleanly demonstrates all that. So for example, if I now in this case, I'll use this as my example to edit.Oh.So.Let me.So there's a couple ways about editing it. So like one way would be like if you wanted to...Let's see if I can, and now these are both TBD, so I'm not sure if it's gonna adjust.both of them. I would paste a screenshot here. I'd say change.Let's say first.TBD to.I don't know, **. Now, I mean, I can change it back or I can say undo it and it'll, so if I go ahead and request that.It's going to...Find it.Hopefully it'll be this one here that'll be changed.kind of a unique scenario where I have identical ones here, but hopefully it catches first TBD. So obviously I'm going to have to put a time in there to go and figure that out, but that's why I know it's going to change anyway. It'll say that it's done and if you do the refresh.you can see that the change was reflected in the PDF. So that's like the clean way. For myself, it's kind of what I've gotten used to as far as cleanly changing this information. Now, if you go in the Python script, or you know, if you want to go ahead and manually do it, if that's easier for you and you're more comfortable in doing that,That's, you know, up to you. You know, if there's, you know, if you have more familiarity on how to manipulate PDFs, go for it. But this is kind of what I do today. So I would go through and, you know, if I read, I have to read through this myself, but then after I approve it, I think it looks good, then I would go to, in my case, I'd share it with Amy, say, hey, what do you think? And then also,share it with, in this case, it would be John Morgan, who was the manager on the engineering side, get that a final pass, and then Jr. would have the final look at it. And then from that point, if all the lights are green and we can send it out, then we would go back to the original method of request andSend it out that way.So does that make sense?
576072292608Juan Martinez   19:12Yeah.
576072292608Viraj Kansara   19:13Yeah.
576072292608Dean Korbakis   19:13Yep, and then, uh, as, ohh, I'm sorry, crashed you something, ohh, OK.
576072292608Juan Martinez   19:14Yeah.
576072292608Viraj Kansara   19:19I was just saying, yes, it makes sense.
576072292608Juan Martinez   19:19Yeah.

## Topic 1 · KB Support Operations — Customer Support — Equipo EU 🇪🇺
_chunk 175 · 2026-06-03 · fuente: /Users/MancoMenStudio/Desktop/Topic1_Support_Operations_KB.html_

Matt Everett
Sr. Support Engineer
📍 UK
✓ Aprende rápido
⚠ Una cosa a la vez
Secure Claude Incident Data
Mohammad Sheikh TOP
Sr. Support Engineer
📍 UK · autor de los docs de Dataflow
✓ Todo (literalmente)
⚠ Ninguna identificada
Secure Data Incident
Carlos Jacinto
Support Engineer
📍 Portugal
✓ Ética de trabajo
⚠ N/A
Secure Incident Data
Vlad Bogus
Monitoring Engineer
📍 Ucrania
✓ Todo monitoring + Secure
⚠ N/A
Monitoring Secure Data Incident

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 5/24
_chunk 1194 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

Eligibility tickets are also seen as void claim requests. She takes care of those too. So if you get engaged tickets that come in specifically for those two things, they can go right to Marissa.
 Juan Martinez   13:48 Jain.
 Kristin Krogman   13:50 I've got a couple links in here that are kind of outside of our. learning sessions. I've got a triage process, which actually that is part of ours. Here's some of these other ones. I guess I have shared a lot of these. The git book external for the customers to see. This is the link. So that can be shared with customers if needed. I just have it there. for quick access and also on my desktop. That's the client contest contacts listing, which I've shared. But again, I've just got them here for myself. We have, I put an example ticket because in the last two years, I've gotten
 Juan Martinez   14:20 Jade. Okay.
 Kristin Krogman   14:37 a few more of these tickets and you don't see them often. So sometimes it's like, oh, what do I do with this? But when they're looking for like our, these annual testing documents that we do to make sure our security is up to date, et cetera, for the clients. They will open tickets. DHL reaches out every year. Kohl's has started reaching out to us. I would have to really think about it. There's a couple others that reach out. And when they do reach out, we have This link to our trust portal. And you can share this with them. So this trust portal is something that is on our main company page that they can get to, but we can just share it with them and they can go in here and they can look for whatever documents that they want. They just have to request them as part of this process.
 Juan Martinez   15:22 In. King.
 Kristin Krogman   15:39 but they're allowed to do that. So I put that link in my cheat sheet as well.
 Juan Martinez   15:43 This is.
 Kristin Krogman   15:45 Yeah, here's the decommissioning ticket process. That's something that sometimes I need to go look for. It's right there. Here's just real quick help payment and data ops, you know, support data, how he wants his tickets to be set up. It's just a reminder that there's a few things on the tickets. Yep.
 Juan Martinez   16:03 Yeah.
 Kristin Krogman   16:04 So we've got that platform unification. So again, I have a lot of things on here that are even process changes that happened like today.
 Juan Martinez   16:15 I, I think that I, I think that all the all things that you have is is very important for Lane, and I understand all the process and different process on situations with different clients and tickets. I think that is a great **** for for Lane and a lot of things.
 Kristin Krogman   16:17 Yeah. Yeah.

## Reunión 2026-07-15 — KT Kristin: casos en vivo help inbox + Samsung readiness · Transcripción 5/9
_chunk 1246 · 2026-07-15 · fuente: kt-kristin-2026-07-15-oficial_

27806, I believe was the one. Here we go. I don't understand why this one is here. Oh.
 Juan Martinez   19:38 Is it the same?
 Kristin Krogman   19:41 I think so. I don't know why they're just opening this now today. Oh, I see. Okay. I see. Bryant. Okay, so how Jr. works? with that e-mail address. So here's another thing you get to see. Okay. So...
 Juan Martinez   20:11 Yeah.
 Kristin Krogman   20:15 When that help at app risk e-mail is used, okay, and someone has access to the portal, it automatically opens a ticket, okay, for them. So here, Brian replied to the customer on that e-mail that I forwarded you, because here's all this information, right? So Bryant responded and when he replied all the help at Appriss e-mail was on there, it recognized Bryant and it opened a ticket.
 Juan Martinez   20:37 Okay. Well...
 Kristin Krogman   20:50 Okay, so now this ticket was opened and all he was saying was, hey, it's, you know, this ticket was open because here we provided him with us, right? It was under Alyssa's name and of course he thought it was going over there too. So he said solution expert.
 Juan Martinez   20:56 Shh.
 Kristin Krogman   21:11 So he put that in there and now what L1 is going to do is they caught it, they saw the two tickets, so they linked them together, right? Here's the action item. And... I'm going to assume that Aisha is going to... I appreciate it if I could get access to the portal. So this is kind of weird, this is happening all at once, but I'm going to just ask Aisha. Oop. I'm just going to validate that she's actually doing it. I'm sure she is. Yeah. Okay, so he was asking me to do it. So we, this is a little, this normally doesn't happen like this, but it's good for you to see, right? And it's great. It's good that you can see the communication happening too, right? So everybody's talking to each other. We'll calm it down.
 Juan Martinez   22:21 Mhm. Okay. Yeah, that is good.
 Kristin Krogman   22:37 the customers being taken care of, that's the big thing, right? And so far, we're all on the same page. So it's going through the process. So yeah. Yep, she's got it. She's excellent at her job. She's someone, if you have questions about, you know, what's happening in L1 and you, you know, you need to talk to somebody, she's been around a long time. She's very competent at what she does and she's very easy to work with. So she is there to help you. Okay, so she's going to take care of this. She even, look, she's putting the note in there. You know, hey, this is why we're marking it as a duplicate, right? Because that other ticket is there. So yeah, so this issue should be. as far as setting it up so that the team can look at it. Everything looks like it's moving forward as it should be. Now the only thing I'm going to add here. Back on this ticket. Is that? This thing DLC ticket, but... DG. Jain.

## Transcript oficial — KT Session 17-jul-2026 (rutina matinal Kristin) — parte 5/8
_chunk 1307 · 2026-07-17_

576072292608Juan Martinez   14:32Actually, we have two to one, yeah, two to one work items is is normal, is a normal flow actually, or is a lot of tickets, more than useful, yeah.
576072292608Kristin Krogman   14:43This is a lot more than usual. Normally,
576072292608Juan Martinez   14:47Okay.
576072292608Kristin Krogman   14:51Normally, we were keeping that backlog down closer to 10 and under. And, you know, we'd all be happy when we got it to 0 because it would only stay like that for a few minutes, right? So yeah, 31 is a lot of tickets. A lot.
576072292608Juan Martinez   14:58Okay.Contract.Okay.
576072292608Kristin Krogman   15:10Unfortunately.
576072292608Juan Martinez   15:11OK, maybe and you experience how much tickets the engineers or the super team have per person, approximately maybe 10, 8, I don't know.
576072292608Kristin Krogman   15:25The kind of the standard that was put into place is that it would be about 10 tickets, not to take more than 10 tickets in your queue at one time. And that always was, it's dependent upon to what type of tickets you're taking. Because you know, we've talked about that and you're aware data tickets take so much longer, right?So those are things you have to be careful of. I don't know, has Aimee shared or shown you the dashboard?
576072292608Juan Martinez   15:47Right.
576072292608Kristin Krogman   15:58and where you can look to see who has what tickets assigned to them in Support. Have you been shared this?Because I use this a lot.So then I can see in support who has what tickets, right? Here's the total that they're holding, you know? And then you could take a quick look too, like this one, we know that's an infrastructure one. So for me, if I was looking through here, if I saw those odd ones like that,
576072292608Juan Martinez   16:22Ohh.
576072292608Kristin Krogman   16:35I would go in there and just make sure that, you know, that the follow-up is being done, that it's in the right spot, et cetera, et cetera. So actually, I think this one needs to be, didn't they?Does that one need to be with Delivery now? Or is this a different one?
576072292608Juan Martinez   16:56No, it is in fresh to review.Is.
576072292608Kristin Krogman   17:00Oh, okay. So the new one. That's right. Yep.
576072292608Juan Martinez   17:02Yeah, it's new, yeah.
576072292608Kristin Krogman   17:04That's right, you had a different one than went to Delivery. Okay, so it hasn't been assigned yet. It's still open, so it's all good. There's nothing there for you to do at this point. Do they have a date on here?
576072292608Juan Martinez   17:05OK.
576072292608Kristin Krogman   17:20August 1st. Okay. So yeah, next week, you know, if you don't get a response, say Monday or Tuesday, next week, I would probably just follow up with them and make sure if it's not assigned, hopefully it'll be assigned by then. That means they've seen it. They've got someone, you know, looking at it. So.
576072292608Juan Martinez   17:37Okay.
576072292608Kristin Krogman   17:41But give them a little bit of time here.So that one's okay.
576072292608Juan Martinez   17:46Yeah, okay, okay, got it.
576072292608Kristin Krogman   17:50Okay.
576072292608Juan Martinez   17:52Maybe you have some questions. We have students about what tickets right now have a, I don't know, priority or whatever that I that I can I take it or.
576072292608Kristin Krogman   17:52So...In the from the backlog, you mean?
576072292608Juan Martinez   18:06Because I only have one, yeah, in the front.
576072292608Kristin Krogman   18:11Um...Well, that's mine. You want all mine?
576072292608Juan Martinez   18:16Yeah.

## Transcript oficial — Retro-RCA Process Review 17-jul-2026 (Dean) — parte 5/9
_chunk 1315 · 2026-07-17_

576072292608Dean Korbakis   19:20Okay, cool. All right, so...If now I did create this, oh, see, it's still thinking. OK, it's taking its time.Now, the method of changing that I've shown here is exactly what I did with this retro document. So like, you know, where I put in all the edits, I saved it, it retained all the information, and then after the R call, I went through and requested all of those changes using that method that I did.peer. So with each step I went through, refreshed it, made sure the changes were correct and made completely, and then continued that on throughout the whole entire document. So.Uh...If this was complete, I think I still want to show you kind of like that front end as far as the RCA, or I'm sorry, the retro.But originally, like generally, it'll come out in this fashion, fill out most of the information that it knows. The skill does know that if any information or any question is not specifically answered to leave it blank. And then that gives me the ability and replace it with lines. So then that way that gives me ability to write in.my notes as needed during the call andI think that is pretty much.I think I covered everything. Sorry, I'm a little sloppy with my demonstration today. I'm going to use the excuse that it's Friday, but you know, anyway, so I appreciate your patience through that. Hopefully this is clear enough for you guys.
576072292608Juan Martinez   20:54Right.Haha.
576072292608Dean Korbakis   21:06That is, is that is there any questions on anything that I've covered with this process?
576072292608Juan Martinez   21:13Um...I have one. Since this one goes out with Wi-Fi still under investigation and two TDB time stamps, yeah. What's the process for closing that loop in this case? Do we send the customer and I mean RCA when the investigation completes and will track that commit?
576072292608Dean Korbakis   21:17Sure.
576072292608Juan Martinez   21:34Men.
576072292608Dean Korbakis   21:36Yeah.In most cases, you know, the investigation is complete, the issue has been resolved, and we do like...In the, let's see here.Yeah.This one here. If there's any actions that are needing to take place going forward, like further investigation and action items, I've had a few instances wherethere is an ongoing investigation of something. So like we did it, we applied a hot fix or a quick fix or maybe even a workaround to get it functioning in a way that is sufficient for the customer. But there have been a few scenarios where like this updating alerting that's happening in the current quarter, migrating away from the.database feature, you know, so there are further action steps. But more times than not, it's going to be, you know, there was a problem, it caused an outage or whatever. We resolved it through our investigation and we explained everything that happened between that time.in this fashion to the customer. And, you know, so it's kind of an open and closed kind of a document. And aside from a few things that could be ongoing that we are working to improve, it would still be with like, here's what we've done to make this.
576072292608Juan Martinez   23:06Okay.
576072292608Dean Korbakis   23:16functioning and here's what we are exploring going forward to provide further reliability or, you know, whatever the case is. So hopefully, does that answer your question?
576072292608Juan Martinez   23:20Yeah.Yeah, yeah, yeah, yeah, got it. Thanks.

## Topic 1 · KB Support Operations — Consumer Support 🇺🇸
_chunk 176 · 2026-06-03 · fuente: /Users/MancoMenStudio/Desktop/Topic1_Support_Operations_KB.html_

Andrea Viveros
Sr. Support Analyst
📍 California
✓ Todo sobre call center y disputes
⚠ Tímida
Kyle Nguyen
Support Analyst
📍 California
Nadia Espinosa
Support Analyst
📍 Colorado

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 6/24
_chunk 1195 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

Yeah, yeah. And these are things that they just don't happen that often or it's a new process. And so I put it on the cheat sheet, you know, just as a reminder. So anyway, oh, hello, Juan. Yeah, yeah. So these are just some quick things that I use and I'll leave them on here for you. And obviously when I'm gone, you guys can do whatever you want with them. You can
 Juan Martinez   16:39 Yeah. No, other one. Okay.
 Kristin Krogman   16:55 Delete, do whatever. Another one I just want to point out is Dick's Sporting Goods opens a ticket where they had been. I have seen one recently, but there was a time that these were being opened a lot more often. And let's see. That one doesn't have the actual link. I'm just going to show it. We can do a copy paste. Okay. And. Let's just look at it. So, basically, they're just waiting on a... a file. So they're looking, it's the same thing. It says that the same file is missing. Well, this one is just usually a timing issue for it, and they just need to be patient. But if they don't see it right away, they start to panic and open a ticket. So.
 Juan Martinez   17:50 Yeah.
 Kristin Krogman   17:50 This is one that usually I pick up and I just let them know, hey, you know, we received your ticket. You know, if you can just be patient and if you don't get it within a certain amount of time, you know, please let us know. So just kind of letting them know it should be there by this time. And if it's not, let us know. And then if it's not there, then I would reach out to payment and say, hey, they're missing this one. So anyway, so I have that example on there as well.
 Juan Martinez   18:18 No. Okay.
 Kristin Krogman   18:25 So, I just wanted to show you that I have this, so that, like I said, I will share this with you, and...
 Juan Martinez   18:29 And it. Okay, thanks.
 Kristin Krogman   18:35 Yeah, so that's one thing. Let me... Move that, and let me also move this off of here. Oh, you know what? I shouldn't have done that. I should bring it back. So our next thing I want to look at. And go ahead and stop me if you end up with questions. Okay. Um, I also, when watching the e-mail inbox. If a ticket gets opened with a one. where they have a question, again, this came in, this person is not in the portal. They will also reach out to me and say, hey, Kristin, oh, sorry, I got rid of the one. They'll say, hey, can you have a check on this? And I'll look at it, see what it is. Okay, this is something that we need to reach out to the customer and let them know that.
 Juan Martinez   19:38 Mhm.
 Kristin Krogman   19:41 We're going to put them in touch with, you know, their application administrator and they can help them get a ticket open or whatever it may be. This is ASDA. Again, this is an easy one because ASDA is the client that we have that little. e-mail address for them and I can just send that back to them. So here's their original e-mail.
 Juan Martinez   20:21 Mmh.
 Kristin Krogman   20:21

## Reunión 2026-07-15 — KT Kristin: casos en vivo help inbox + Samsung readiness · Transcripción 6/9
_chunk 1247 · 2026-07-15 · fuente: kt-kristin-2026-07-15-oficial_

Okay, so now whoever in support picks it up, they'll see my note. They'll go up here. Okay, there's the Dick's Sporting Goods ticket. There's this note, and hopefully they'll put two and two together that, oh, this could be the same issue as, you know, what's on here. This one has been picked up by Shaun, so this is already with engineering, as you could see. So they should be looking into this and determining what their next steps are. They don't have an engaged ticket or anything with it. Okay, so they're in the process.
 Juan Martinez   24:57 Okay.
 Kristin Krogman   24:57 So we've done, so we, meaning you and I, getting this set up, getting it started, moving it forward, we've done everything that we can at this point for the client. And as you can see, Bryant responded to the client. He took care of that. So normally I would reach out to the client and say, hey, you know, I've opened a ticket on your behalf, et cetera, et cetera, if that's what I needed to do. But because I spoke with Bryant and because they reached out to Bryant, he said he would take that and he would respond to the client, which he did. So we're all good. Does that make sense or did you see something you needed help with on that part?
 Juan Martinez   25:35 Okay. No, no, no, I'll have sense and and and it's good that all all these miscommunication happens in in this call because I can see the correct way or or path to solutions currently the this type of tickets or or requests of the clients.
 Kristin Krogman   25:55 Yeah, and it's outside of the norm, right? This is when these are the kind of things that sometimes you have to, you know, reach out and talk to people and go, hey, what do you need? Or what have you already done? Because we don't want to have duplicates. Well, we ended up having a duplicate only because that e-mail address
 Juan Martinez   25:59 Yeah.
 Kristin Krogman   26:16 was in on the response. That doesn't happen a lot, but sometimes it does. So I just wanted you to be aware that that will open a ticket. That's how it recognizes that, hey, Bryant is in there and he's reaching out to help at Appriss. So that means he needs a ticket. So once in a while, you'll see something in there. You're like, wait a second, why do we have a ticket open for this? And sure enough, it's
 Juan Martinez   26:37 Yeah.
 Kristin Krogman   26:38 Because of a response. Okay, so now I'm going to check this one off that that's done. And we will move on to the other one I forwarded you this morning. Okay, now...
 Juan Martinez   26:53 And the other one, the Samsung.
 Kristin Krogman   26:55 I sent a different e-mail over to you this morning.
 Juan Martinez   26:58 No.
 Kristin Krogman   27:04 And it is this one, the reminder, IMP third party. I forwarded it to you. This one, this is one of those where the information came in and it looks like it came in on Monday. Or they sent it on Monday. And then they added, they must have added support. On here, where is it?

## Transcript oficial — KT Session 17-jul-2026 (rutina matinal Kristin) — parte 6/8
_chunk 1308 · 2026-07-17_

576072292608Kristin Krogman   18:17Mine are done, you do want mine.Just waiting on validation. Well, if we would go down here, oops, I got flags coming in. More flags.Okay.What is ongoing data issues up? Have you would be nice to get these done?I guess it just depends on what you've been trained on, you know.
576072292608Juan Martinez   18:50Okay.
576072292608Kristin Krogman   18:52Because what is this one?Please check and see if you received and processed file highlighted in the photo. So do you know how to look up a file in the system already? Do you have access?
576072292608Juan Martinez   19:04Yeah.
576072292608Kristin Krogman   19:07So you could do this one.
576072292608Juan Martinez   19:10Secure 5, um, let me see.
576072292608Kristin Krogman   19:13Yeah.
576072292608Juan Martinez   19:17Yeah.Yeah, yeah, yeah, I have access. I remember the old access that I have, and and and and I can take it.
576072292608Kristin Krogman   19:25You can try that one.
576072292608Juan Martinez   19:26Yeah.
576072292608Kristin Krogman   19:27Nice.Okay, we'll assign it to you and then you can let the customer know that you're going to look into it. Great. One of the backlog. Woo-hoo.
576072292608Juan Martinez   19:36Okay, great.Haha.
576072292608Kristin Krogman   19:40OK, so.Yeah, so anyway, I utilize this to kind of know, too, if we've got something we need to push forward, like if a CSM reaches out to you and says, hey, I need some assistance with this ticket, and maybe we need support assistance, right? Looking to see who maybe has availability.ability that's strong in whichever application and seeing if they would be able to take it. This kind of helps me see who's got what, right? You know, payment, you know, he'd be somebody and be like, okay, I don't want to bug payment. Let's, he's got way too many tickets. Let's see who else could help.
576072292608Juan Martinez   20:19How much have been ah, 40.

## Transcript oficial — Retro-RCA Process Review 17-jul-2026 (Dean) — parte 6/9
_chunk 1316 · 2026-07-17_

576072292608Dean Korbakis   23:30Okay, perfect. Okay, so, all right, so now that this is kind of going backwards as far as the retro that's created, it knows it's going to label the file as RET for retro.2026 and the date of course, this is the incident date that it occurred and the customer.So if I go to my documents here and I can pull this up, here's our documentation. So this is just pretty much what we went through. Something I changed it that I need to figure out is I don't know why that numbering sequence got messed up, but.Otherwise, it filled in everything that it made sense to fill in. Now, of course, we'd have to read through it and make sure that it is correct. And I think right now...Maybe because I gave it one that we've already done. There's a few issues here, so...It looks like a lot of it's filled out, but if I go, let's say I want to fix this, and this will be just another example of a correction.I would say.Um...I mean, again, you can either describe it verbally or use the screenshot like the feature that I did earlier. I think.Since I don't have a title here, if there was a title, then I would have been able to just say, fix the word wrap. So in this case, I'm just going to do the screenshot, drop it in.Fix word.Wrapping.Oh.I'll just leave it at that.So, and as long as you're in the same conversation for where it created the document, then it'll know, obviously, exactly what to what to look at, so.So once that's done, I can refresh here and we should see that change take effect.Yeah.All right, so now that it says that it's fixed, go back here, and as you can see, the word wrapping corrected itself.So that would be another correction there.Like I said earlier, or a few moments ago, is if I wanted to describe where to change, let's say I'll want to change.Y3.Um...Or actually, here's another method that I can, you could just be creative with Quad. It can do anything that you ask it to. So if I say change.change this to, and I just want to change some wording that's in here or.I saw.These dashes, I mean, you could say remove em dashes, but...I don't know why it has those dashes in there; per request was not reviewed as a failure amplifier, but...Same concept as, you know, if you describe where you want, what you want to change, or if it's a blank, you can just say Y3 and then put in your statement that you want to add in, and it'll know to correct that.So, that's done, and then...Um...It's not free to plug, OK, away.Oh, there must have been more than one.Can I take that change?The request is not.Well...Ohh, it was a different one.Or no, I don't know why they didn't change there.Anyway, I mean, you get the idea. I think I gave it, hopefully, I mean, that's okay. Like, you just have to kind of work with it. Just the other thing I want to jump to quick is when you have your final, your final retro done, you have your final RCA done, we're sending that off. There is a spot inthe confluence that we store all these so it's accessible to anybody at any time.And where we would go for that is...Uh...We have a section, it's in the problem management space. So it's not RTS or RCS. It has its own space here. And what I'll do is I can, I'll just drop it in the chat for reference if you guys want to look at further on your time.So...They're all broken down by year. So the RCA would go, you'd want to send it to this space here. And the way to do that, by the way, is if weGo back to Claude. Claude will know that, and I'll...Go here with this is the RCA, so...So, and as you can see, the...The naming structure, as you can see, RCA and it has all the description and then it matches everything that goes in here. And simply what I would do is send.Send this RCA to Confluence.And the external RCA skill will know that it needs to go to the problem management space, root cause report list, and then it.May have to double check this. It may, I know it's going to go into this main folder. Now I might have let it go into a kind of its own spot. Like you'll see it as a draft underneath. And the reason for that is because I was like, all right, well, if I do 2026 now when it comes 2027, someone will have to worry about.switching the skill to reflect that. So if you kind of leave it general and it'll drop it into its main folder, you can kind of move it as needed from there. But.Regardless, the skill itself will know that it's going to send, you know, this final document to this location. And then from there, you'd want to go to the ticket itself.Um...And then...Sorry to backtrack on this. And I only have documentation that explains everything we talked about in this call, so you can follow the correct sequence, because I feel like I've been all over the place, so I apologize. When you have the request for an RCA initially, is, and I haven't done this here yet, so it'll be a real world example here.We have these labels.And what we would need to do is problem management.

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 7/24
_chunk 1196 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

my response because they know I'll take care of it. And I responded back to them to say, hey, go ahead and do this. Once in a while, you'll get a response from a couple days later that they didn't receive any feedback from the team or whatever it may be. The suggestion to them is to try again. but then we add on one of their contacts who is listed on my cheat sheet, that Carl Reasoner. If he gets added to it and they've, you know, tried, he'll jump in and try and help. So I have contacts listed on there as well. And we have our client listing, remember, that you can go to and look. and see who's on there. I utilize the customer area here. And let's just say, for example, I was looking for ASDA and I'm not sure who the correct contact is to reach out to. You know, whoops, I didn't want to do that. I want to do this. You know when you go in here? that anybody who's opened a ticket.
 Juan Martinez   21:32 No.
 Kristin Krogman   21:36 has access is more than likely an application administrator. So I would go in here and look and see who recently, it's the most recent ticket is at the top, who most recently has opened tickets in a couple of them, and then look at what type of tickets are opening. Like Paul's been opening data tickets. He's probably not my guy that's going to be able to help him with the application, right? He's doing other work. So I would just go in here and look and see, okay, here's somebody who's working on incident reports. This is probably someone I can reach out to and say, hey, we've got somebody who needs some help. with an issue with application as far as, you know, working an incident report or access or whatever, this would probably be one of the people I could reach out to. So that's kind of how I determine if I don't know specifically who to reach out to, how I find someone else. Because if they've opened tickets, they've got access to the portal.
 Juan Martinez   22:35 Mm.
 Kristin Krogman   22:35 and they are somebody who can probably help.
 Juan Martinez   22:39 Okay, nice.
 Kristin Krogman   22:40 Any questions? I kind of went fast. Sorry.
 Juan Martinez   22:41 No, no, no, no, no, no, it's clear, and it's good information, and I don't know the customer section, actually. It's nice to research, sorry.
 Kristin Krogman   22:46 Okay. Oh, let's go back and look. Yeah, yeah, let me show ya. Okay, I think this is on one of those sheets too. It should be when you're adding someone to the portal or adding someone or an organization. Yeah, there's a there's a there's a document for that. So let's say for example, you get a client who says, I need to add somebody to the portal. This is where you're going to come to. You're going to come to this customer section. and you're going to go to the organization. And let's say, for example, Meyer. Okay, Meyer needs someone added to the portal. And actually, I just did this person this morning. You would come here. Click on Add Customer and put in their e-mail address.

## Reunión 2026-07-15 — KT Kristin: casos en vivo help inbox + Samsung readiness · Transcripción 7/9
_chunk 1248 · 2026-07-15 · fuente: kt-kristin-2026-07-15-oficial_

Because somehow Support got it and they sent it to me. And so like, you know, they received this e-mail, can you assist? And the reason they need an assist is because this person is reaching out on behalf of Samsung, so they're probably a contractor, which means they're not going to be in the portal because typically people don't put contractors in our portal. It's usually like we've talked about before, there's specific people that most clients want in their portal to have access. And this person is not, I did check. So they can't open a ticket for them. So they're stuck. Now this person is looking for this. They want this readiness checklist taken care of. They need it to move forward. So this would be a situation where in looking at it, it's an infrastructure information type ticket that I don't have the information for. So I'm going to need to get it from somebody else.
 Juan Martinez   28:21 Okay.
 Kristin Krogman   28:37 right? And our infrastructure team would be that group that we would reach out for. So another ticket needs to be created with the information and this request to be filled out, which is just a drop and drag into the ticket once it's open. And this would be a ticket that would be sent to infrastructure. And I know we've mentioned it before, an infrastructure ticket, that's one where support has to remain assigned to it. Okay. So this would be one, your process would be create a ticket. And you would be the reporter on this one, because there isn't someone from Samsung here that we're going to be putting on it. Okay. So this one is you as the reporter, and then you're going to put it in the infrastructure queue and keep it assigned to yourself. And this one you'll do. via e-mail. You know, we don't do a lot of communications via e-mail, but this is the exception to the rule, right? There's not a ticket directly to someone. This infrastructure team needs that information on their side. So we'll communicate directly with them. So my question to you is, do you want to try and create a ticket or do you want to watch me do it again?
 Juan Martinez   29:57 Kill me. Um...
 Kristin Krogman   30:08 Okay. Okay. Three minutes.
 Juan Martinez   30:18 Meeting 6th.
 Kristin Krogman   30:19 Okay. Okay, well, I'll do this quick then. Let me just get that off of there. We're going to go here. Okay, so create a ticket.
 Juan Martinez   30:31 Great ticket.
 Kristin Krogman   30:33 Okay, do you want me to put you as a reporter so you get communication on this? Okay, so we'll do that. So Juan Martinez is going to be the reporter.
 Juan Martinez   30:37 Yeah. Yeah, yeah, cool. Hmm.
 Kristin Krogman   30:46 Okay, and this is actually for Samsung. Samsung. Um... They're just going to put third party. Infra. Okay. So this is not an incident ticket. This is just, hey, we need some information. So it's not a break fix thing.
 Juan Martinez   31:23 So, starting them off work, yeah?
 Kristin Krogman   31:27

## Transcript oficial — KT Session 17-jul-2026 (rutina matinal Kristin) — parte 7/8
_chunk 1309 · 2026-07-17_

576072292608Kristin Krogman   20:20Yeah.40, but he's taking on, you know, everybody else's ticket. He's going to get these too because Smeet's done today. So he's getting more. Okay, so back to this kind of where we're at. What time is it? 1022. Okay. The other part of my day that I dois I go into my filters.And this is where I start looking at my different reports. So here, my normal ones, I go into the complete ones, and I showed you this before where they're in complete status. I look to see if they can be closed out. And I actually know there's one on here that's mine.We can find that and we can, I waited. Yeah, this one.Do I have two maybe? Nope, just the one. Okay.So if this wasn't mine, you'd go in there, just take a look at it.See where we are with the customer.what was said to them. Okay, so this one, they're going to, they need to connect offline. They've been given the information that they need. It's been closed, so it's ready to be closed out completely because they're good. So I'm going to close it. So we did all of the communications there with them.Why is that still thinking?I'm just going to get off of that. So anyway, I would go through here again, look at these.I keep it pretty up to date. So, got all these windows popped up so I can't see my own work.I try and keep it really low too, if I can help it. Looking at the last time it was done, this is the one where I need to ask if anybody's doing a root cause analysis, because I haven't seen anything on Teams either. RCAs were typically done by...Dean, I don't know if he's still doing that. And this is a, you know, the information was put out there about this Teams meeting.So I would go here again, see if anything's been updated as far as root cause. I'd check with Dean to see if anything was done as far as root cause and then determine if there's something else we need to share with the customer or if we're good to go and we can just close this because this issue is resolved. It's just a matter of if we need to share anything additional with them.
576072292608Juan Martinez   23:01K.
576072292608Kristin Krogman   23:02And root cause at this point, as far as if we do a whole RCA for them, that's only shared with them if they request it. And then there's only specific things that are shared, and so it has to go through management as to what's going to be shared with the client.So yeah, so again, part of the day I would, or part of this time, I would go through here, see which tickets I can get completely closed, make sure that there isn't any additional notes. Because if somebody put an internal note on one of these tickets, let's say, for example, this one,If somebody added something to it internally, it wouldn't move this to work in progress. Okay, so look here. Michael Jackson says, hey, this ticket can be closed. Yep, so Michael is letting us know that it's okay to close the ticket. Well,
576072292608Juan Martinez   23:55My projects.Yeah.
576072292608Kristin Krogman   24:03Who is the owner here? Okay, David, new. Then we can go ahead and move it right to closed status.Don't even need to think about it. Customer says it's good, we close it out.
576072292608Juan Martinez   24:17Okay.
576072292608Kristin Krogman   24:17Sorry, so that makes sense, right?
576072292608Juan Martinez   24:19We can put close it manually if the customers put a comment like, I don't need more, thanks for the service, whatever. I can put close manually.
576072292608Kristin Krogman   24:28Yep.Yep.
576072292608Juan Martinez   24:31Okay.
576072292608Kristin Krogman   24:32Absolutely.Okay, then the other thing that I do is that Tiger Team. Oh.

## Transcript oficial — Retro-RCA Process Review 17-jul-2026 (Dean) — parte 7/9
_chunk 1317 · 2026-07-17_

576072292608Viraj Kansara   31:46Mm.
576072292608Dean Korbakis   31:50O, once you add this label here.It's going to take a moment, but it's going to create a PBM ticket, a problem management ticket, which then goes through, see how it created the PBM 425. So this is the, this tells you that there was a request for an RCA.In this ticket, what I would do is...Just as I described of sending this RCA to Confluence, when you're dealing with that retro, let's say this retro was completed, I would do the exact same thing except saying instead of saying RCA, I would say retro, send retro to Confluence. It would go to Confluence, it'll create that.Um...It would create that document or that template for RCA. And the same setup or configuration that we have for the RCA, we have for the retro. So in this particular instance, this is the one that I created for Lululemon at that time. So we keep track of both the retros and the RCAs.Going forward, whatever, you know, if that changes, then you know that would be changed, but for now.We keep both documents available for viewing. So then going back to the ticket.I would put my retro.I'd say.Link page.And then, if you do...Problem management here.you can see like, all right, well, okay, there's my retro. I'm going to go ahead and link it. And then, so this first ticket that's created is for the retro. And then this one, so it creates 2 tickets. When you do problem management in the original RCS ticket, it creates this one here.which was where I put the retro and then where it says create RCA.This is, I would follow that same concept and do page link.Problem management.And then.I would say.you know, RCA, then I did look up the RCA that I had inserted for that given instance and then attach it to this ticket. So then once that's completed, so now you have 3 total tickets. You have the RCS ticket, you have the retro ticket, and then you have the RCA ticket, which then...You'd have to remember that once you're done, you'd go back in and close those three items. So quite a few documentation steps, but you know, it's where then everything could be found if it turns up again in the future, which I haven't really had to go back to an RCA in my past, but you know, of course, keeping that record.Nice and clean is.Certainly essential, so.
576072292608Viraj Kansara   34:58But technically, Dean, just creating a RCA ticket just for documentation, right? We can also put that on internal notes on the existing ticket. Like, what does it make difference?
576072292608Dean Korbakis   35:12Oh, okay, so what's good about this, these two tickets is the...If we go back, okay, so this is the first one that it created. What I would do is I would put in all our internal notes. So like what I used for, so of course it's already referencing the RCS ticket that initially requested the RCA, but then in this thread here is where I would put in chat links.You know, so if I was, you know, wanting to go, you know, for whatever, you know, the secure issues channel, like any communication that was handled with there between L1, L2, and L3, you know, so like all your documents that you use to create.The retro and the RCA, I would I would put here for access or, you know, for visibility, then the the RCA, I'm sorry.
576072292608Viraj Kansara   35:58Mm-hmm.
576072292608Dean Korbakis   36:07The RCA ticket, there's not really much that you would need to add here unless, you know, it called for it, but...I think, you know, the first ticket is the information gathering plus the retro, and then the second one is just RCA itself. And this doesn't go out anywhere. So it's not customer facing. It's these are the problem management is an internal space. So.That's our tracking within Jr. for when it comes to.the RCA process.

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 8/24
_chunk 1197 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

Juan Martinez   23:50 Okay.
 Kristin Krogman   23:50 And then once you put in an e-mail address, see okay pops up. And you would just click OK. So... Here, let me show you. Yeah. I had been in communication.
 Juan Martinez   24:08 We use the the mail that the the customer sends to directly to this mail, or we have a other page or documentations for for at the customers' mails.
 Kristin Krogman   24:23 Um...
 Juan Martinez   24:23 Or, or where, where I can find the customers means specifically, or just in the in the in this mail?
 Kristin Krogman   24:29 It would come from a request. It will either come from a request by e-mail, okay, but you, like I said, it's very fluid. If somebody just requests it and you don't know who they are, right? We don't know who this person is. Then you would reach out to another person at the organization.
 Juan Martinez   24:34 Okay.
 Kristin Krogman   24:51 you know, another admin and say, hey, is it okay to add this person to the portal? Sometimes they will copy someone on the e-mail and you're like, okay, I know who that person is that's copied. The request has come through, you can do it. Our hope and what we ask the clients to do is if they need someone added to the portal, that they open the ticket and then...
 Juan Martinez   25:15 Yeah.
 Kristin Krogman   25:15 Yeah, and then L1 can actually do it. You'll probably get a lot of requests that come from the CSMs. We get a lot of those where they'll forward us an e-mail and say, hey, please add this person. Okay. So if you do that again, You just go to customers? organizations and then type in, you know, whoever it's going to be, Meyer. And then you go here and you look for them, of course, which you can type in, you know, the e-mail here. And you know, like Bernie. Okay, there's Bernie. He's already in. So I can let them know, hey, you have access to our portal already. And you can give them the URL and I'll show you where I have that stashed too, so that it's right at your fingertips. A But if you do need to add them, again, you just click on Add Customer and you put their e-mail address in here, click OK, and they get an invite.
 Juan Martinez   26:16 No, OK.
 Kristin Krogman   26:16 All right.
 Juan Martinez   26:17 Okay.
 Kristin Krogman   26:19 Customers, organizations. If you need to add an organization, you go here. And then when I say organization, I'm talking, you know, Home Depot, ABC Fine Wines, you know, whoever the client is. When we get new clients. bring them in for business. Sometimes we have to add them in here when they get turned over to support. You just click on add organization and then type in whatever their business name is going to be with us. So as you can see here, like Air Force, they're known as APs, but...
 Juan Martinez   26:51 Mm.
 Kristin Krogman   26:56 We just put the parentheses saying, hey, this is who we're talking about.
 Juan Martinez   27:00 Okay.
 Kristin Krogman   27:00

## Reunión 2026-07-15 — KT Kristin: casos en vivo help inbox + Samsung readiness · Transcripción 8/9
_chunk 1249 · 2026-07-15 · fuente: kt-kristin-2026-07-15-oficial_

Yeah, it's just, they just need, they just need the information. So there's nothing to be paid for, nothing like that. We just need to provide them with the information. Okay, so.
 Juan Martinez   31:35 Okay.
 Kristin Krogman   31:42 Here we go. I'm gonna put... This guy's information in here. And then... Believe this was.
 Juan Martinez   32:01 Like the infrastructure.
 Kristin Krogman   32:03 It'll be for infrastructure, yeah, but we need to... I don't know for sure. Oh, that thing's in my way. That's my problem. It's got to double check what Samsung has for a product. If they're engaged, that's what I was wondering.
 Juan Martinez   32:42 Okay.
 Kristin Krogman   32:44 I think that might have been on the... Come back, where's my thing? Where's my ticket? Shoot.
 Juan Martinez   32:59 Maybe we'll save it like a draft because you'll leave the...
 Kristin Krogman   32:59 No. Hey, it should just be there. Here we go.
 Juan Martinez   33:05 No, no.
 Kristin Krogman   33:07 Yeah, okay, so it's going to be engage. The organization is Samsung.
 Juan Martinez   33:14 It's very useful to clean contacts a document now for for be sure for double check the the correct product type.
 Kristin Krogman   33:15 Yeah. Ohh. Yeah, and they aren't even in the portal yet, that's right. I wonder if it'll even let me do this.
 Juan Martinez   33:32 Haha.
 Kristin Krogman   33:34 It might not.
 Juan Martinez   33:42 No matches.
 Kristin Krogman   33:45 Yeah, well, I'm gonna see if it'll let me do it.
 Juan Martinez   33:48 Okay.
 Kristin Krogman   33:50 Yep, it will. And I'm going to grab it right away. And I'm going to assign it to you.
 Juan Martinez   34:05 Okay.
 Kristin Krogman   34:09 And then what we're going to do... is we're just gonna put Appriss in here. just for the time being. All right, we'll do this. Undefined, we're going to put low priority. Because this isn't going to anybody since you're the reporter, right?
 Juan Martinez   34:38 Okay.
 Kristin Krogman   34:39 Okay, so now last thing we need to do is, yes, that dropdown will have to get moved to. The reporter, but we got to bring in. That. attachment. so that Russ can see it.
 Juan Martinez   35:04 Okay, like internal note, we add every doc, picture, screenshot, whatever, and in the mail. I didn't like an internal note when I created this type of ticket from Appriss mail, yeah.
 Kristin Krogman   35:20 Ohh. Yeah, you can, yep, you can put documents in there.
 Juan Martinez   35:22 Hale Boppers Bank. Yeah, from the screenshot, everything. Why is now priority? Why? I am not sure what is now.
 Kristin Krogman   35:28 Yeah, so not. What?

## Transcript oficial — KT Session 17-jul-2026 (rutina matinal Kristin) — parte 8/8
_chunk 1310 · 2026-07-17_

576072292608Juan Martinez   24:40Well, sorry, in this case, why David don't put close, don't change the complete to close the ticket status? Maybe because he don't know he can do this or just Kristin or Camila or Aimee can do this.
576072292608Kristin Krogman   24:49But.No, the associates can, anybody working on tickets can move it to closed status. A lot of times, though, when you're, you know, going through the process,you want to let them know, right? Hey, it's been done. We'll give you a couple days to validate it's okay. And then we're going to close it. Ideally here, it would have been added to this message. You know,
576072292608Juan Martinez   25:20Yeah.
576072292608Kristin Krogman   25:30This work has been completed. If nothing further is needed, this ticket will be closed in two business days. You know, I mean, personally, I mean, this is something that maybe your process will change. But for me, I think it's nice to at least give them a couple days to look and make sure it was done correctly and respond if needed.Once the ticket's closed out, it does not pop back open again if they respond. In completed status, it will move it to work in progress and let you know that, hey, they responded to this ticket, so go take a look at it. And a lot of times people just want to be polite.and say, hey, thank you, right? So a lot of times that's how it gets open and that's nice. So then you just, you know, close it out again. So.
576072292608Juan Martinez   26:12Right.Okay, okay.
576072292608Kristin Krogman   26:21But yeah.Okay, so I would go through all of those just to make sure that there's nothing new for the ticket, make sure it was completed, the work was completed and determined if it can just be closed or if we need to wait a couple days or whatever the case may be. That's just kind of how you feel about the ticket. Kind of up to you guys to determine, right?How much time do we have? Oh, not much. Okay, I won't get started on this then since we're right at the time. I want to make sure you can get to your meeting with Dean. Go ahead and reach out to me later or, you know, after you're done, I can jump on a call any time with you. So just let me know.
576072292608Juan Martinez   26:51Yeah.Yeah.Oh, okay, okay. Thanks, Kristin. See you later. See you later. Okay, bye bye.
576072292608Kristin Krogman   27:04You're welcome. We'll talk to you later. Okay, bye-bye.
621792274320Juan Martinez detuvo la transcripción

## Transcript oficial — Retro-RCA Process Review 17-jul-2026 (Dean) — parte 8/9
_chunk 1318 · 2026-07-17_

576072292608Viraj Kansara   36:45So if you say internal.ticket, right? It means whatever we put, like our internal threads or communications or internal things that will not be seen by the customer, correct?
576072292608Dean Korbakis   36:58Correct, yeah, the so even though we paste there, we we add in the retro when that in the first ticket in RCA in this ticket, it still doesn't go anywhere. It's all for internal tracking within JIRA that could be retrievable and viewed anytime. You'd still have to go to the RCS ticket or an e-mail or you know wherever it was requested.
576072292608Viraj Kansara   37:00Okay.
576072292608Dean Korbakis   37:20initially to provide the RCA document.
576072292608Viraj Kansara   37:25Gotcha, sure, thanks.
576072292608Dean Korbakis   37:27All right. So, yeah, that's all I have. Any other questions?If not, like I say, I'm going to have it well, very well spelled out within the Confluence environment. I have to make some tweaks to, you know, because I've made some changes over time. So I'm going to make sure that that's current and updated and I'll share with the group here. And then that way you have written documentation.On how to go through this process, so...Sounds good.
576072292608Viraj Kansara   38:03Yeah, that will be helpful. Yeah, we need like iterative process, how you do it, like multiple times to make sure you know, you know how to do it. Yeah, okay. But you need to have iterative process to create this RCA documents couple of times, so you know what works and what doesn't.
576072292608Juan Martinez   38:03Ohh, everything is clear.
576072292608Dean Korbakis   38:06Good.Mhm.Yeah.Yeah.Yeah, so it's.Yeah, so using this, I like to, you know, go through and if I go higher up here, oh, not this one, this one I want to show.I can.Um...So in this case, I needed a, I wanted to start a new session with Claude. So I referenced, so if you go here and let's say, okay, I want to make changes or I want to, like I requested here, I want to make changes to this file. If you do copy as path, then that's where this is and it'll go and it'll reference that specific file.So then that way, you know, you're using the right document. And then here is where I added some information into a section.Um...And then I'm like, oh, hold on, like, you know, roll back, you know, roll back some changes. I can say, you know, undo last change. You can do, you know, all sorts of requests to Claude and that'll go through and you can see the changes that are being made within the Python script.So, yeah, so I mean, it's...It, yeah, whichever way works for you guys, or again, if you've had some experience with modifying PDFs and there's an easier way or smarter way about it, then by all means, you know, whatever gets that final document in a way that is presentable to leadership.Then.That's the way to go.
576072292608Viraj Kansara   40:10Yeah, just one, just one thing, like, um, do we have a specific template that we have to use that, like, headers, footers for ApprissSupportGHSorg?
576072292608Dean Korbakis   40:21Well, the templates are stored within the skill. So when you call, when you're dealing with directly with Claude, just like how I did for this one here where I say creating a, create a retro, it'll know it'll go to the skill and it's got that document on already stored within it.
576072292608Viraj Kansara   40:37Huh.

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 9/24
_chunk 1198 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

So yeah, and then the same thing, you just click add once you're done with it and it goes right in. So that's, you know, it's pretty self-explanatory with adding customers.
 Juan Martinez   27:03 Yeah. Yeah.
 Kristin Krogman   27:13 Um... Okay. Let me, let me look at something real quick. I can find my other sheet for you. Okay. Let's look at, since we're here. One of the other things I receive, and I didn't get one of course today, and I think of all the other ones closed out because I do that right away. I'm going to look here. Is we get... 28 day. Here we go. No response after 28 days. And I think this day, I think it's going to switch to 21, I think, to when tickets are going to be forced closed. We wait so long and then they're forced closed. So what happens is you get an e-mail that says, hey, this one is closed. I go in and check them.
 Juan Martinez   28:03 Mm.
 Kristin Krogman   28:17 and make sure that they should have been forced closed. Sometimes we do have to wait for the client, and that's typically when they need to deal with their IT team, right? They're waiting on somebody to get some information to pass it on to us. Because again, not everybody has access to the portal. So sometimes that application administrator has to be the go-between between our people and their people. Okay. So if that happens, then sometimes there's a delay. So all you do is just go in here, take a look at what the last comments were. And they were waiting, it looks like, to do a call. They were in communication, and then, you know, the information fell off. So here, the call happened, let's say, and actually, I wonder, I didn't get a response from Sabda on that one. Yeah, well, here it had closed previously even. And so then I reached out to Sevda and said, hey, you know, do we need to reopen this? you know, because it's been closed, what do we need to do here? So I put a note in it that it's being reopened because it's not resolved. So whenever that happens, that's all you got to do is just put a note in there why it's getting reopened and then you would put it wherever it needs to be. Okay.
 Juan Martinez   29:40 Okay.
 Kristin Krogman   29:43 This one more than likely is she probably hasn't responded because it's probably going to stay closed since this has already been one that's been out there forever and they probably talked already. So we just check them and just find out, hey, should we reopen or not? More than not, the notes on there are going to give you the information to say, hey, this one can be closed. We've reached out to them already how many times they haven't responded. We're good. Sometimes, depending on the, it'll be. ticket dependent. What is this ticket for? I mean, if you look at it and you go, oh, we've got to have this, then reopen the ticket, right? But I would work with whoever the assignee is, whichever data engineer or whomever, you know, infrastructure.
 Juan Martinez   30:24 Yeah.
 Kristin Krogman   30:33

## Reunión 2026-07-15 — KT Kristin: casos en vivo help inbox + Samsung readiness · Transcripción 9/9
_chunk 1250 · 2026-07-15 · fuente: kt-kristin-2026-07-15-oficial_

because it's not like a break fix thing. It's information that's needed, but it's not needed, you know, for a week. It's something that if he's got other things on his list, it's more important than filling out this kind of information. I know you've got to go. I moved it to under infrastructure review. And so now you just kind of watch this ticket to see if he does anything in here. And
 Juan Martinez   35:38 Okay. No. Yeah.
 Kristin Krogman   35:59 We can, if you want to, we can chat about it later too. But right now we just wait on Russ to see what he says.
 Juan Martinez   36:05 Actually, stay in infrastructure review, not super review, yeah.
 Kristin Krogman   36:09 Right, this just goes right to infrastructure to fill out this information.
 Juan Martinez   36:14 Okay, great.
 Kristin Krogman   36:14 And then you hold on to it because he's going to respond to you and then you're going to need to respond to the customer with the information.
 Juan Martinez   36:23 Ah, okay, great, Kristin. Great. Thanks. Thanks for your time and for this plan, John. It's very clear for me. Thanks. I appreciate it. Thanks. Yeah, later. Bye bye.
 Kristin Krogman   36:25 Okay. Yes, yes. Okay, we'll talk later. Okay, bye-bye.

## Transcript oficial — Retro-RCA Process Review 17-jul-2026 (Dean) — parte 9/9
_chunk 1319 · 2026-07-17_

576072292608Dean Korbakis   40:41And then.You know, then you have the...you know, it gives you, it creates everything for you. So there's really not like a blank document or, you know, I mean, of course, we could probably create one, but, you know, since we have everything already built into the skill, we just go straight to it and just say, create this using this information and.leave blank whatever is not answered. And, you know, then you kind of go from there from the proofing and making edits. And of course, you could tell the difference with the document you're dealing with, besides the fact that you have these questions and answers, color-coded, or, you know, whatever is answered in green. You have the...you know, this kind of gold colored label here, whereas, you know, this one's the dark, you know, you know, this is the live document that goes out. So otherwise, like I say, everything's stored within the code, so through the skill.
576072292608Viraj Kansara   41:38Yeah.Got it. Got it. Perfect. Thanks, Dean.
576072292608Dean Korbakis   41:45Mhm.Okay, so yeah, that's really all I have to demonstrate. So if there's no other questions, then I'll update you guys once the documentation is up to date and approved, and that should be able to join in with this meeting. And then of course, I'll have this meeting available in ourSharePoint folder, so you can reference it at anytime, so...All right.
576072292608Juan Martinez   42:16Okay, thanks Deanne.
576072292608Dean Korbakis   42:18Thank you so much, guys.
576072292608J.R. Teagle   42:18Dean, thank you very much. Thanks, team.
576072292608Juan Martinez   42:19I appreciate your time.
576072292608Dean Korbakis   42:20Of course. All right. Happy, happy to help. Take care.
576072292608Viraj Kansara   42:23Be.
576072292608J.R. Teagle   42:24Right.
576072292608Juan Martinez   42:24Bye-bye.
576072292608Dean Korbakis   42:25Bye.
576072292608Viraj Kansara   42:25Have a good day. Bye.
621792274320Juan Martinez detuvo la transcripción

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 10/24
_chunk 1199 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

team them and communicate and say, hey, should we reopen this ticket? What do you think? You know, just partner with them.
 Juan Martinez   30:40 India. Okay.
 Kristin Krogman   30:43 So that's the 28th day. Then what are my other things that I get to do? Is the complete? Status tickets. I go in here and close them out. We put tickets in completed status when... We've fixed something for the client. Appriss has done everything that they can, right? It's done. It's complete. Now we just kind of want them to validate for us, but we can trust that it's done. So we're not too worried about hearing back from them, but we want to give them the opportunity to respond.
 Juan Martinez   31:16 Yeah.
 Kristin Krogman   31:28 When it's in completed status, when the client responds, it'll flip to work in progress and notify whoever the assignee is. Okay? So what I do is I go in here and I find out, okay, does this one still need to stay in completed status or can we go ahead and...
 Juan Martinez   31:36 Okay.
 Kristin Krogman   31:48 Just close it out. So this one, they could, here's that ask Zeus. So for a whole, there's an e-mail address that can be sent to them, right? So, okay, somebody went through and gave them the information. Looks like, oh, this was, there was an outage the other day. Okay, I remember seeing that on Teams. Okay, so this one. would be one that I left because I think they're still trying to find out what the root cause was on this one. Here, root cause investigation is ongoing. So this would be one I'd leave for a couple days just to see if a root cause gets added to it. If it doesn't get closed out after a couple days or a root cause get added to this ticket, then what I would probably do is reach out to say Jr. since he's the one showing this or go to the Chat. See what, so I can't get there, huh? Okay, open. OK, see what they've got going on. Oh, wow, it's a lot. Oh yeah, this was... So it has been resolved. We just don't know if the RCA was done. So at this point, it would be reaching out to whoever's doing the RCA. Right now, Dean does those, see if he's actually working on a root cause. And I lost my spot. Sorry. See if he's working on a root cause and... Then close it out from there if needed. That's not it. Where did I go? Lost my spot, sorry. I'm gonna go back to my filter.
 Juan Martinez   33:57 No.
 Kristin Krogman   34:03 And then my completed closed, got lots of things that I look at here, and... On the completed closed page that I had in the knowledge sharing, this... Filter is on there. Um... So anyway, this one I would keep in completed status for a little while. This one, we'll just take a quick look. So it's basically just going in, taking a quick peek and seeing if it's one that should be left alone or if it should be closed. And I look to see what they have. Okay, I've confirmed the information. Okay. He's loaded the data into there and said that it's completed. What is today the 14th?

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 11/24
_chunk 1200 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

Okay, I probably would reach out to Vlad and just find out if there's anything more possibly they could come back with on this one. It is just for QA. Okay, never mind, because I was wondering if they were going to have to load and prod. So she just was asking about QA. So this one. She's going to. Yeah, loaded into prod. Once information is loaded into prod. For me, I'm going to ask Vlad about this. Because I want to know if we're going to be doing that once she says everything is okay or not, because on this ticket. Yeah, I'm just going to validate with him.
 Juan Martinez   35:47 Okay.
 Kristin Krogman   35:49 Because she's talking about prod, and I don't want... there to close it out too soon. And then just give them the ticket, and then... I'll let you know. Okay. So, we'll leave that one. Tahoe, this one you know about.
 Juan Martinez   36:40 No.
 Kristin Krogman   36:46 OK, let's see. Okay, so he never reached back out. This was from the day that they had all the issues. And so it doesn't surprise me that he couldn't log in again because this was on Saturday and everything was down. There was a problem. So he tried after lunch, which makes sense with the timing. and it looks like everything's working. So he's up, he should be okay here. So I'm just going to go ahead and close this one out. Because they fix that, so that's good.
 Juan Martinez   37:23 This is my ticket.
 Kristin Krogman   37:25 Yeah, yeah, so you, you did this stuff.
 Juan Martinez   37:26 Oh yeah, yeah. I see like, I know this.
 Kristin Krogman   37:30 Yeah, yeah. And so the actual work for this ticket was done, right? Everything was completed. And then we had the weird outage on Saturday, which he's thinking is this again, but it wasn't. So we're just going to close that one out.
 Juan Martinez   37:43 Wow. Okay, great.
 Kristin Krogman   37:48 Yeah, okay, let's take another look.
 Juan Martinez   37:50 Always is a good practice review, they actually complete tickets for confirmed. We don't need to add more information or something else in a way that maybe low. So yeah, it's like a good practice. Do this maybe all day or one time per week or...
 Kristin Krogman   37:59 Yes. Yep, it is. Well, for me, you know, you're going to be working tickets a lot more. You've got other stuff going on, you know, more so than what I would have had with, you know, this. And I don't know how much other
 Juan Martinez   38:18 No.
 Kristin Krogman   38:26 admin stuff such as this you're going to have going on. For me, I just made it a part of my daily routine because it's, as you can see right now, there's 13 tickets. That's not bad. You know, it's pretty easy. And as you do it, you're going to know, okay, yeah, there's a couple of them that you know about. And you're like, yeah, I was going to give it a couple more days and you don't even have to look at it.

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 12/24
_chunk 1201 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

And then you'll go in there a couple days later and look and see anything new and just close it out. And here, this is a good example. Everybody kind of handles their tickets a little different. Sometimes you want to give them, you know, that, yeah, this should be good, but I want to give them a couple of days.
 Juan Martinez   38:54 Okay. If.
 Kristin Krogman   39:08 And you can kind of give the customer a little bit of a push. And he did here. He's telling them that they're putting in his complete, but he's going to close it after three working days. Okay. So, or three business days, however you want to say it. So he's telling them, you better get back to me because this ticket's getting closed out. So if they don't, they've been forewarned, right? And he's saying he's going to close it out. So now three business days, this was Friday. So I'll honor his timeline for the customer and I'll leave it and then come back, you know, tomorrow or Thursday and close it out. Um...
 Juan Martinez   39:45 Okay.
 Kristin Krogman   39:47 Shell ones, I just know this, these typically can be just completed. The customer usually comes back and says, yep, this is done. Yeah, please close. So this is from the customer saying you can go ahead and close it. close it. That's all you got to do. Anytime the customer says, yep, it's all good, it can just be closed. Then we'll just jump over so we can get you some other knowledge. I just want to check this one. Okay, so first of all, just FYI, this is going to be an old ticket because Brooke is an Appriss employee and she's not around anymore. She's been gone for quite some time. Okay, so Ray is a CSM as well. So she's the one that resolved it. She moved it. So we know that we're good to close. We're just going to go ahead and move it. One's really old. Out. Okay, she didn't give us great notes, but... Okay, so anyway, so I would go through those, just make sure that they're, you know, complete to close. I'll do a quick refresh. So we closed out three of them just by looking at those few. So, and like I said, you're going to have 10 to 20 depending.
 Juan Martinez   41:13 Okay.
 Kristin Krogman   41:19 on what's been going on. And it's good to keep them around this if you can. Okay.
 Juan Martinez   41:28 K.
 Kristin Krogman   41:30 Um, since we're right here. I'm going to show you, you were on the meeting where we talked about the Tiger team.
 Juan Martinez   41:37 Okay. And.
 Kristin Krogman   41:39 And we talked about the 14 day, so I won't go through the process with you, but I just wanted to show you one of the things we talked about, but you didn't get to see it in action. So
 Juan Martinez   41:45 No.
 Kristin Krogman   41:53 Again, this filter was shared in that in the document that was put together. And I did add the Tiger Team document to my knowledge share because David wasn't a part of that. But since you were, I did put it on it. So it is also there and on the video that we did together. So.

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 13/24
_chunk 1202 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

This is the report and yesterday I went through and took off of my report. Let me grab. Because about every, I don't do it every month, not every four weeks, but about every six weeks or so, I go through here and look and see who has multiple tickets. I sorted this on a different page, but I see who has multiple tickets. where they're not responding to a, say, a Teams message, or they're not responding to an app mention on a ticket. And I'll put together their... their ticket list and I'll send them to you. You probably saw a bunch of emails from me last night. And those were Tiger Team. tickets that I sent out and I copied you and Camila on it so that you could see it. So for example, you know,
 Juan Martinez   43:21 Okay.
 Kristin Krogman   43:25 Let's make that bigger. I just let Zach know, hey, you got a couple of tickets here that are old. You know, could you please take a look and see what's going on with them and, you know, give me any update that you can? I put what the last note is on there so that they can kind of see as well and maybe they don't have to think too hard about it, might be able to help them. Sometimes they'll respond in e-mail. Other times they'll just put in Zach did on the tickets he put in at mention to me internally on the ticket to say, hey, this is where it's at. Right? And that's fine. This is purely just a, hey, this ticket hasn't had anything happen for quite some time because here this is the beginning of June. right? And here, you know, June, we need to have something else in here for the client. Let's see, who else?
 Juan Martinez   44:17 Okay.
 Kristin Krogman   44:22 Support. Smeet has actually done the end of this week. He got a new job, so that's great. But he's got a bunch of tickets, right? So I sent him a note and said, hey, Smeet, you know, please go through these, make sure that they get to the correct person or any updates you can put on them. He would have gotten this regardless of him leaving or not because he has a bunch and it's just a reminder, right? Just a, hey, I'm following up with you because you've got several in here that need to be looked at. Sevda, same thing. I think they were just, what is she, oh yeah. She's got... Three, four of them. Nope, three of them. That one has a lot of notes. Just making her aware that, hey, this has been sitting in work in progress. There hasn't been anything new here on the ticket. You know, and these tickets are from April. We need to, we need to do something about them. So, that's what we do, and then...
 Juan Martinez   45:26 Okay.
 Kristin Krogman   45:33 Like Marzen, I sent him a note last night and he sent me a note back just letting me know, hey, there's this is what's going on.

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 14/24
_chunk 1203 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

So now we know he's been told, right, that these tickets are there. And if there's anything in here that should be added to the ticket, I'll add it as an internal since he didn't put it on the ticket himself, as far as I can see. But like here, I would take this one, I'd go look at it. See what's there? Okay, so he's still in the same boat that he was on June 8th, but then what I'm going to do is I'm going to go back here and I'm gonna put a note in here that Marzen is continuing to wait on Honeywell. So, I'll just do an internal note. Yeah. It is continuing. Yeah. And that just helps him out and it also shows that hey. I took a look at this and let him know and this is what I found out. So that's what we do with those Tiger team tickets. And then...
 Juan Martinez   47:18 Okay.
 Kristin Krogman   47:20 Yeah. And this is the, when we were on that meeting, this was the Excel spreadsheet that I share at the end of the month with Aimee. And then Aimee does some stuff with the totals and. She takes care of whatever it is that she does with them at that point. There's some matrix or something, I'm sure, metrics, not matrix, metrics that she's dealing with. Okay. Um... Let me look at my little list. Okay, so we did this. We did complete close. We did 28 day. Okay, Best Buy ticket. I wanted to show you this. Okay, so when I'm working... In. In the queue. Okay, let's go back here. And I'm looking at the backlog. So like I came in this morning and there was a ticket that was in here that said work in progress. Well, you should never see a ticket in here that's unassigned in any other status than under score review or possibly waiting on engineering like here. or delivery, something like that, because they're waiting to assign it in those other, off their dashboards. So if you see something that just looks weird, like I did this morning with this ticket. I came in here to figure out, okay, who, somebody didn't assign themselves to a ticket or what's going on. Well, this has been, this was really nice because the request can be closed. We were able to fix this. So I just sent her a note. Thank you for letting us know and closed out the ticket.
 Juan Martinez   49:07 Okay. Great.
 Kristin Krogman   49:09 But it does happen.
 Juan Martinez   49:11 Okay, okay.
 Kristin Krogman   49:13 It does. Next thing, we are cruising through this stuff. Okay, so we have our ticket, our test ticket. I've been reviewing it, right? I've been doing my work. And you know how that works. It goes into a work in progress. We've told the customer, hey, I'm doing work on it. Well... If I need to close it out, you've been through this already. I just want to show you the reminder that there's canned responses in here. if you need anything. I go through tickets. And sometimes I see that other associates have fixed something, but they've just left it in waiting on the customer. But we've been waiting forever for the customer, right?
 Juan Martinez   49:59 Okay. Really?

## Topic 1 · KB Support Operations — Consumer Support — disputes de retorno
_chunk 185 · 2026-06-03 · fuente: /Users/MancoMenStudio/Desktop/Topic1_Support_Operations_KB.html_

El mundo B2C: consumidores cuyo retorno fue negado y piden revisión.
Roster Proceso core
⚠️
No confundir: un dispute es un email de un consumidor pidiendo revisión de un retorno negado o una reclamación. Un RAR (Return Activity Report) NO es un dispute — si el consumidor solo pide su RAR, se le envía su RAR y listo.
Diagrama 8 · El ecosistema Consumer (modelo hexagonal del equipo)
flowchart TD
CN["CONSUMER"]:::core
Q["Queries"]:::n --> CN
D["Disputes"]:::n --> CN
R["RARs"]:::n --> CN
CA["Customer Action"]:::n --> CN
AI["AI model"]:::n --> CN
TEAM["Appriss L1 & L2
Consumer Experience teams"]:::n --> CN
classDef core fill:#1a2c52,color:#fff,stroke:none
classDef n fill:#dbeafe,color:#1e3a8a,stroke:#60a5fa
Capacidades del Call Center
- 24×7×365
- Program Manager dedicado
- Puntos de escalación dedicados
- Número 1-800 dedicado por cliente
- Scripts de respuesta personalizados por cliente
- CRM custom por necesidades de cada cliente
- SLA y reporting específicos por cliente
🌐 Self-Service Portal: los consumidores van a www.theretailequation.com para pedir un RAR o encontrar formas de contacto (teléfono, email, web).
🔧 Herramientas internas: Jira (tracking) + CRM custom (acceso vía "Incident Search" / returnx.com ). Necesitas acceso al CRM para procesar disputes.

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 15/24
_chunk 1204 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

Kristin Krogman   50:07 Well, then I'll put some this canned response in there. You know, it appears your ticket's been resolved and we're going to put it in completed status. If nothing is needed, we'll close it one week after this notification. This is obviously something, as you saw before, like with Vlads, depending on what the ticket is and how long we've been waiting.
 Juan Martinez   50:50 Mm.
 Kristin Krogman   50:50 You can change this as you need to, but that's all you need to do, saying, hey, Kristin Krogman, you know, click save, and then moving this one on to completed status. And, you know, saying whatever it is as far as support resolved or, you know. Whatever. Resolving it, we did it, and now we're going to close it. Because I did everything.
 Juan Martinez   51:16 Yeah, it's not it's not necessary at a comment for for complete the the the ticket.
 Kristin Krogman   51:25 That that's.
 Juan Martinez   51:26 Because these things happened with the last ticket that you write me, the Friday, the last week. I add the comment and the comment put into like a reply to customer and not an internal note, but I think that, I don't know, it was necessary and a comment when you... A change to complete ticket and and put all the information in there.
 Kristin Krogman   51:51 Yeah, if you don't, if you don't do that second dropdown that I did.
 Juan Martinez   51:52 And they pop up.
 Kristin Krogman   51:57 It, it won't, it won't, it won't resolve, it won't put perform customer requested operation. You have to put that second drop down.
 Juan Martinez   52:05 Okay.
 Kristin Krogman   52:09 Otherwise it won't complete it. It'll send you a note and say, hey, this isn't done. You didn't resolve it.
 Juan Martinez   52:15 Okay.
 Kristin Krogman   52:15 So it's got to have the two dropdowns filled in.
 Juan Martinez   52:20 KK.
 Kristin Krogman   52:20 So, and as long as you put... As long as you put what you did in the ticket. That's where that's supposed to be, is your resolution that can, you know, with Claude or however you did it. The resolution needs to be in the ticket part here as an internal note, and you're good to go to set it.
 Juan Martinez   52:44 Okay.
 Kristin Krogman   52:46 And maybe that's a process that'll...
 Juan Martinez   52:46 Okay, okay.
 Kristin Krogman   52:49 That'll go away. Because I used to do that all the time, but then you're doing two things that are unnecessary, putting the same thing in the closure in the bubble. And it's already in the ticket.
 Juan Martinez   53:03 Okay.
 Kristin Krogman   53:04 So... As of right now. OK.

## Topic 1 · KB Support Operations — Proceso de Dispute — Parte 1: Ingresar el dispute
_chunk 186 · 2026-06-03 · fuente: /Users/MancoMenStudio/Desktop/Topic1_Support_Operations_KB.html_

Diagrama 9 · Recepción e ingreso de un dispute
flowchart TD
S1["1 · Ir a Jira
abrir el ticket del dispute"]:::a --> CHK{"¿Es un dispute válido?
(no un RAR request)"}:::dec
CHK -->|"Es RAR"| RAR["Enviar el RAR al consumidor
(fin)"]:::end
CHK -->|"Es dispute"| S2["2 · Recuperar Transaction ID
buscar en el CRM"]:::a
S2 --> DUP{"¿Ya hay un dispute
abierto para ese consumidor?"}:::dec
DUP -->|"Sí"| NODUP["NO crear duplicado"]:::end
DUP -->|"No"| S3["3 · CRM → ADMIN → Consumer Disputes
→ ADD DISPUTE"]:::a
S3 --> FILL["Llenar: Transaction ID · Nature of issue (Complaint)
Notes · fecha recibida/enviada · Jira Ticket # → SUBMIT"]:::ok
classDef a fill:#7c3aed,color:#fff,stroke:none
classDef dec fill:#d97706,color:#fff,stroke:none
classDef end fill:#64748b,color:#fff,stroke:none
classDef ok fill:#16a34a,color:#fff,stroke:none

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 16/24
_chunk 1205 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

So we talked about the Best Buy ticket being work in progress because no one was assigned to it. So when she responded, I should start with us on that ticket that I found it as work in progress. It was sitting in the backlog like that because the team hadn't gotten to it yet. It wasn't assigned to anybody. So it was just sitting there. So then when I saw it, it's like, okay, she's telling it to. done, we could just close it. It didn't need to be, you know, assigned anybody to work. It was just good to go.
 Juan Martinez   53:40 Okay.
 Kristin Krogman   53:41 Stop.
 Juan Martinez   53:43 Okay, I have other other questions about the the sign sign off the documentation. I see some documents. Let me find like like the not get added to conflicts. We need to to add it or what is the plan for?
 Kristin Krogman   53:43 Up. That was something Amy, because Amy reviewed all of those documents. And she put a couple of them in Confluence. And then there were some that she didn't add that she wanted me to talk to you and Camila to determine whether or not you wanted it in Confluence. You know, it might not be something that you guys want in there. It's just something that you'll keep to the side.
 Juan Martinez   54:21 Okay.
 Kristin Krogman   54:26 you know, that you have, but you don't necessarily need it for everybody to have, right?
 Juan Martinez   54:32 Okay, okay.
 Kristin Krogman   54:32 So that'll be the determinant. And of course, you can add whatever you want. It's for you guys to do. So I have the information there for you, and you can do what you want from there. So it's a good question, because that's something we should have covered. Let's see.
 Juan Martinez   54:39 Okay. Okay.
 Kristin Krogman   54:54 Um... Is there anything I went too fast over for the things that we talked about today?
 Juan Martinez   55:04 Okay. I sign off actually the other documents and and and then try to speak today with with Camila about the this documentation and and and what happened with this information in in the future of or see if actually is necessary that our team or we are. Some people have access to to this; it's more for the for design of no for for designing for for you, but but yeah, I actually I don't have more questions about.
 Kristin Krogman   55:31 Yeah.
 Juan Martinez   55:44 And the the sign of or the documentations or other process. I think the this session, this meeting is is is what is what now was a very important to me because I I captured a lot of information that I need, I kept that I need actually to to do my.
 Kristin Krogman   56:03 Oh.
 Juan Martinez   56:04 A lot of things, maybe I need to order my mail. Can you share your your mail organizations for for for copy you for have a better idea?
 Kristin Krogman   56:04 Yeah. Thank you. Yep. What you need to see, yep.
 Juan Martinez   56:19 With the with the filters and and and the whatever.
 Kristin Krogman   56:23

## Topic 1 · KB Support Operations — Proceso de Dispute — Parte 2: Respuesta del retailer
_chunk 187 · 2026-06-03 · fuente: /Users/MancoMenStudio/Desktop/Topic1_Support_Operations_KB.html_

Diagrama 10 · Procesar la decisión del retailer
flowchart TD
R1["1 · Obtener respuesta del retailer
CRM → Consumer Disputes → All Retailers
→ Retailer's Response → DOWNLOAD"]:::a --> DEC{"¿Decisión del retailer?"}:::dec
DEC -->|"Approval (One-Time / 30-Day)"| AP["Go to Special Consumer → retailer → Always Approve
poner End Date · Notes: 'temp approval per [retailer]'"]:::ok
DEC -->|"Void Transaction"| VD["Return History → localizar transacción
checkbox → Void Transaction"]:::warn
DEC -->|"No Change"| NC["Sin acción de aprobación"]:::neutral
AP --> R3
VD --> R3
NC --> R3
R3["3 · Carta de respuesta
SharePoint → Letter Templates → completar
guardar como TID# · CRM EDIT → Reply Date → subir → Submit"]:::a
R3 --> R4["4 · Jira: Reply to Customer → DONE
CRM: Close → Action: No Action · Subject: Retailer Request
Resolution Action: decisión → Close Dispute"]:::done
classDef a fill:#7c3aed,color:#fff,stroke:none
classDef dec fill:#d97706,color:#fff,stroke:none
classDef ok fill:#16a34a,color:#fff,stroke:none
classDef warn fill:#dc2626,color:#fff,stroke:none
classDef neutral fill:#64748b,color:#fff,stroke:none
classDef done fill:#0d9488,color:#fff,stroke:none
📁
Rutas exactas de SharePoint: templates en SharePoint → Customer Service → RAR Disputes → Letter Templates . Guardar la carta completada en SharePoint → COVID-19 → Upload Response con el nombre = Transaction ID . Siempre verificar que el archivo subido corresponde al TID# correcto.
11

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 17/24
_chunk 1206 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

Yeah, because you'll have your own inbox. So this one is just my inbox, but you're going to need this one.
 Juan Martinez   56:30 Yeah.
 Kristin Krogman   56:31 You want to take a picture of that?
 Juan Martinez   56:33 Yeah, actually I take a screenshot here. Okay, yeah.
 Kristin Krogman   56:37 Yep.
 Juan Martinez   56:39 Thanks, yeah.
 Kristin Krogman   56:39 Yep, and I do, I do look at this one, but now. The only thing that seems to come in here is stuff that we don't respond to anyway.
 Juan Martinez   56:52 Okay. Okay.
 Kristin Krogman   56:53 So I've actually talked to the legal department about this and I sent them this response. So. Yeah.
 Juan Martinez   57:01 Yeah, yeah, yeah, okay. Thanks, thanks for share. I, I, I...
 Kristin Krogman   57:04 Yeah, so it's this one and this one that you have to have. This one, the Retail Client Services one, there is an automatic response that goes out to the customer. This is, hey, this is not a valid one, but for whatever reason, there are people that still use it. It's just now it's weird ones, you know, and things that, you know, like I said, this one, Legal gave me a response to give to them, but otherwise you get people just, it's junk mail. And so I just delete it anyway.
 Juan Martinez   57:40 OKOK, I got it.
 Kristin Krogman   57:40 And it doesn't, yeah, it doesn't come in very often anymore, so. That one's okay. Yeah, like.
 Juan Martinez   57:50 You have silent, silent, for example, your automations put a coming in, have a lot of mails in my mail with with this message.
 Kristin Krogman   58:02 Oh, the one, you mean the one that I sent to the legal team?
 Juan Martinez   58:09 Yeah.
 Kristin Krogman   58:10 I, I can give you that. And that one I just respond as Retail Client Services. I don't give them my information. I'll send this to you.
 Juan Martinez   58:25 Okay.
 Kristin Krogman   58:28 So you can see it.
 Juan Martinez   58:30 Okay, thanks.
 Kristin Krogman   58:31 Yeah.
 Juan Martinez   58:32 Mhm.
 Kristin Krogman   58:35 Yeah, and if you see stuff like that.
 Juan Martinez   58:36 Oh.
 Kristin Krogman   58:39 You know, we've got our legal department who you can talk to and say, hey, I got this really weird e-mail. Do I do anything with it? You know, and forward it to them and let them look at it. Let them tell you what you should or should not do with it. Right. And that's all I did when I received those. They come in once in a while and They're like, nope, these are not something we deal with. We just ask them to please take us off of their e-mail list. This is not, you know, for us. And they. They've got us on a recurring, I don't know why, if it's automatic that we get added to it, they don't take us off. Because it's never a response to me like, oh yeah, you guys really do need this. You know, there's nothing like that. There's no response to me or a Retail Client Services reaching out, you know. They just never fix it. So it's just an annoyance at this point.

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 18/24
_chunk 1207 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

Juan Martinez   59:29 Yeah. Okay, okay.
 Kristin Krogman   59:36 Yeah.
 Juan Martinez   59:37 OK, thanks, Kristin, for your time and for this meeting.
 Kristin Krogman   59:41 Oh yeah. So no, you'll just have to decide. I mean, there's obviously there's still stuff we can go through. The, I mean, for you, you'll have to tell me, do you want to, you know, like watch me go through a process in the morning, you know, like that type of thing. I mean, what do you think would be helpful?
 Juan Martinez   59:58 I. Yeah. Yeah, yeah, yeah. I think I will say this. I need, I think that maybe this is a good practice or example for me in a live meeting for CU doing all this process in the morning. I have time in this week or the other week. I don't know if you have time. Let me review my agenda.
 Kristin Krogman   1:00:25 Yeah, let me just see if...
 Juan Martinez   1:00:30 Um... May be there in the morning.
 Kristin Krogman   1:00:39 Yeah, I mean, just so you know, and we don't have to do it at this time. I typically start at 730, but I can hold out, you know, I can just look through this stuff and if there's anything high priority, right, I would do it and then hold it and show you what I did. If there's anything that has to get done and we could always you know, meet later. I don't expect you to start earlier if you don't, that's not a problem. So you just tell me and then like I said, I'll wait and then we'll walk through things and you can watch me do it again. And then at some point we'll flip it and we'll let you look because you need access to that help e-mail anyway.
 Juan Martinez   1:01:00 Mhm. Okay. OKOK, let for the main. To the main, sorry, ohh.
 Kristin Krogman   1:01:24 Yeah, you're gonna need, you're gonna need access to that help e-mail, you know, before.
 Juan Martinez   1:01:30 Yeah, before, before, before, before, yeah.
 Kristin Krogman   1:01:31 For all the processes, yeah, before you're totally ready.
 Juan Martinez   1:01:35 Yeah, yeah.
 Kristin Krogman   1:01:37 Yeah, and then our next knowledge share too, or... I, because I haven't gone through with you, I should just show you engage. Unless you, do you have time right now? I could show it to you.
 Juan Martinez   1:01:48 Now, engage. Right now, no, no, no, no, yeah, I have, I have time, yeah.
 Kristin Krogman   1:01:57 Oh, okay. So let me just show you, because this is this is not hard.
 Juan Martinez   1:02:00 Sharp.
 Kristin Krogman   1:02:04 This is and it'll be on the again that documentation. Let me move my stuff out of the way. Let's close this. Okay. All right. The verify portal. And we're going to have to get you access to this.
 Juan Martinez   1:02:30 To engage.
 Kristin Krogman   1:02:31 Um, yeah, so that you can get in here. Okay.

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 19/24
_chunk 1208 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

All I do in here is it's usually customers that ask for access to the portal. And that would come from one of their administrators already who would say, hey, you know, Juan needs access, he needs to mirror my access. It needs to be the same, mirror it. It looks the same, and... then people need resets. And resets are the things that I see more of. And all you do is you come in here. and you go to admin and you go to web user listing. There it goes. Okay. And whoever the associate is that can't get in, you put in their e-mail address because you'll have that or their name, right? And we'll, let's see, who do I know that's in here? OK. Let's go with one of these. Okay, so let's say it was this Beth Perry Conklin. All right. She can't get in. Well, if you look over here, she's been disabled. Okay, it's checked box. Do you see the difference there between this one and this one?
 Juan Martinez   1:04:09 Yeah.
 Kristin Krogman   1:04:09 Okay, so she needs a reset. All you do is you click, yeah, you just click right here for her on the reset and it sends out a link. Okay.
 Juan Martinez   1:04:11 Okay. Mm.
 Kristin Krogman   1:04:20 Yeah. And so if there's a ticket for that, then you would just let that person, hey, I've sent out a link for Beth's access. She should be good. This is one of the requests that actually sometimes comes into the help desk and they usually don't know what to say because it's usually someone like, hey, I can't get in.
 Juan Martinez   1:04:21 Okay.
 Kristin Krogman   1:04:40 to the application. Okay, well, like Home Depot, we know they have several applications. And if they have engaged, then you have to get them to verify or ask them for the screenshot. You know, what are you trying to get into? And then they'll let you know. And that gives you time to come in here and look for them.
 Juan Martinez   1:04:49 Mm. Okay.
 Kristin Krogman   1:04:59 And then you can usually see, oh yeah, they just need a reset here. But you want to validate that sort of thing. Okay. Now, if you're going to be adding a user to the portal, it's right here. Okay. You just click add user. But let's say that they're supposed to mirror this Beth and Perry. You go to Edit. And edit is going to bring up what they have access to. And do you see there's a checkmark?
 Juan Martinez   1:05:32 Yeah.
 Kristin Krogman   1:05:32 Those are the areas that they have access to what they can see. So you would just need to go, okay, hide default and store manager. Okay. So Beth has access to that. That's what it's supposed to be. You know, for my next use, I want to take this off of here. I don't like this being there. OK, so then I go to add user. It's thinking. Okay. So then you go, you know, to that was store manager, right? And then whatever the other one was, I don't remember. I take a picture of the first one to make sure that I get it right. So the first, if I'm mirroring somebody, I take a picture of what they have.

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 20/24
_chunk 1209 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

And then I come over here and I make sure I'm checking the correct boxes. You put their e-mail up here for the new person. You put their e-mail up here. You check the boxes. Whichever retailer they're a part of, you just select it here, right?
 Juan Martinez   1:06:35 Anything.
 Kristin Krogman   1:06:38 You put in their phone number and you will need a phone number. So if you don't have one, you're going to have to request one because they do the two-factor authentication. So they're going to need their e-mail or their phone number, sorry. And then you just click Save Changes.
 Juan Martinez   1:06:55 Okay.
 Kristin Krogman   1:06:56 So those instructions, again, they're on that document. So no worries there. And I think on that document, I think I've got it. I'm pretty sure I took a. An e-mail or a ticket, so that you have an example ticket. That's what I tried to do. I tried to put example tickets on those documents. So, but yeah, let me reach out to Marissa and I'll see if I can just get you added to this.
 Juan Martinez   1:07:22 Okay. Okay, thanks.
 Kristin Krogman   1:07:31 Yeah, because I'm pretty sure I just requested from her. If not, you have to put in a request with Austin or with the ITHD group, but I'll let you know what you need to do for sure, if we need to go that far or not.
 Juan Martinez   1:07:46 Okay.
 Kristin Krogman   1:07:47 So we'll do that. Do you think we need to get this for Camila as well or? Just you at this point?
 Juan Martinez   1:07:53 Um, no. No, actually, no, no, no.
 Kristin Krogman   1:07:57 Okay, we'll just do you, because I don't know as well if this is something that'll continue to go forward as far as being responsible for it. This is something I just kind of did on my own, to be quite honest, because these tickets come in where somebody's got a password that needs to be reset, right, to get into the system.
 Juan Martinez   1:08:14 Yeah.
 Kristin Krogman   1:08:16 And the group that can do it, they don't come in for another two to three hours. So you've got a client that can't get in and they've got to wait when it's something this simple is going in here and resetting. It's like, it didn't make sense to make them wait. So I just asked what the process was and Marissa got me hooked up. So.
 Juan Martinez   1:08:29 Yeah. Yeah. Yeah, it's a really simple process.
 Kristin Krogman   1:08:40 It is, and they shouldn't have to wait for that. Yeah, it makes them happy when you can help them right away. So anyway, so that's that process as well.
 Juan Martinez   1:08:40 Yeah. Yeah, yeah, yeah, for sure. OK. Okay. Okay, okay. It's very simple processes, but these are really is necessary processes.
 Kristin Krogman   1:08:54 Hi. It's just, it's just remembering. Yes. And now it's just you remembering that, oh, yeah, I know how to do it because it doesn't happen that often.
 Juan Martinez   1:09:07

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 21/24
_chunk 1210 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

And happens frequently with a lot of clients or no, no, no, no, it's frequent. The customers forget the passwords or...
 Kristin Krogman   1:09:12 No. Yeah. Yeah, no, it doesn't happen that often. It seems like when it does, you get a few of them all at once, and then you won't get anything for a month, and then you'll get one or two, and then you don't get anything for a month. It doesn't happen A lot. So, and even setting up users in the portal.
 Juan Martinez   1:09:22 Yeah.
 Kristin Krogman   1:09:35 It's kind of the same thing. You won't get one for a long time and then you'll get two. And then you'll remember how to do it, and then you'll forget how to do it. Until you do it a couple times and you're like, oh yeah, I remember.
 Juan Martinez   1:09:42 Okay. Yeah, yeah. Okay, and and the maybe exists a specific protocol for handling recurring recurring issues like the automatic inclusion in list that hasn't been fixed yet, or should we escalate this to a different team or just continue managing?
 Kristin Krogman   1:09:52 So.
 Juan Martinez   1:10:11 It's anyone, anyone, anyone else.
 Kristin Krogman   1:10:18 Ask the first part of the question again. What needs to be, what do you think needs to be escalated maybe? What are you asking?
 Juan Martinez   1:10:27 The, the, if actually exists a specific protocol for handling recurring issues, like the automatic inclusion in list that hasn't been fixed yet.
 Kristin Krogman   1:10:42 Um... Something that hasn't been fixed yet.
 Juan Martinez   1:10:47 Yeah, yeah, because you mentioned a recurring issues like automatic inclusion in lists that remain unresolved and are considered considered on anyone ends, yeah.
 Kristin Krogman   1:10:59 I'm not sure why I'm not getting that. What did I say? A reoccurring issue. What did I say? A reoccurring issue that hasn't been resolved. Do you remember what the issue was I was talking about? It was resolved.
 Juan Martinez   1:11:13 Yeah, only resolve. And resolve it.
 Kristin Krogman   1:11:19 Unresolve it.
 Juan Martinez   1:11:19 Oh, is in the ticket management process and an escalation protocols for for connect with the documentation which are covered in the first topic of the this knowledge transfer.
 Kristin Krogman   1:11:24 Bish.
 Juan Martinez   1:11:32 And, and.
 Kristin Krogman   1:11:32 Wow, I must be getting old. I can't remember what we talked about first. I just was going through it.
 Juan Martinez   1:11:37 Okay, okay, no worries, no worries.
 Kristin Krogman   1:11:42 Wow, I'm.
 Juan Martinez   1:11:45 Oh, oh, oh, well, if there is a formal escalation path for for recurring issues, or if there are simple managed ad hoc.
 Kristin Krogman   1:12:00 I'm just trying to think what we were talking about that we got to a recurring issue. A recurring issue.
 Juan Martinez   1:12:04 Yeah.
 Kristin Krogman   1:12:08 Well, we were talking about the emails and sending them out to the client.
 Juan Martinez   1:12:12 Yeah.
 Kristin Krogman   1:12:16 If.

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 22/24
_chunk 1211 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

They access issues that it like ASDA was reaching out on and why I have that e-mail address. It's just because they have so many stores and the associates know to look, you know, on the application and they find that help at Appriss and they think, oh, we reach out here. They don't know. to go through their application people. And it's usually an access issue, like they can't get into somewhere. They've been promoted and they need more access. And then that's why they reach out to us. But it's got to go through, they want it to go through ASTA.
 Juan Martinez   1:12:46 Yeah.
 Kristin Krogman   1:12:58 And remember, too, when it comes to access, you know, for ABIS, for incident, you know, we don't make those changes. Those things have to be done on their end for security reasons. You know, we don't want to be changing people's accesses. They should be doing that sort of thing. So now the SSO, of course, is different. Sometimes they got to reach out to us for some help with that, but. Still, they they're supposed to have a list of all that.
 Juan Martinez   1:13:25 Um, okay.
 Kristin Krogman   1:13:26 So hopefully that answered your question. I'm got myself a little, yeah, okay.
 Juan Martinez   1:13:29 Yeah, yeah, yeah.
 Kristin Krogman   1:13:32 Yep. And like I said, I'm going to go back through my cheat sheet, see, make sure that the valid stuff is on there for you, because there could be some stuff that's out of date. I just know where to go look for, hey, I don't remember this. I'm going to look at my cheat sheet and see if it's there. So I can cheat.
 Juan Martinez   1:13:32 Yeah. Yeah. Okay.
 Kristin Krogman   1:13:53 Does that make sense to you, cheat sheet?
 Juan Martinez   1:13:56 Cheat cheat is like a, no, I know, I know what is, yeah, yeah, yeah, yeah.
 Kristin Krogman   1:14:02 Yeah, you got it. Okay, so I just thought about that. Okay, well, we're doing our language thing here. I thought, maybe I better validate he understands what I mean by that. Yeah. Okay.
 Juan Martinez   1:14:12 Yeah, yeah, yeah, but the the I respect about the maybe the the last question that I that I do is I mean. Something you say earlier about the inboxes, not not that in the in the mail, you mentioned there is a recurring e-mail, not issues, or invade the Retail Client Services keeps getting out into automatically.
 Kristin Krogman   1:14:35 Oh, the legal one. Yeah.
 Juan Martinez   1:14:36 Yeah, yeah, and you reached out about it and nobody ever fix it. And my question maybe, but I do in my bad, is that something worth is collecting somewhere or do we just live within is in anyone?
 Kristin Krogman   1:14:46 Yeah. Yeah, no, when I have already talked to legal about it and showed him what they were sending us and they said, yeah, we shouldn't be receiving it. Just give them this canned response and keep sending it to them. That, you know, and that's the one I forwarded to you so you could see what I told them.
 Juan Martinez   1:14:55 Yeah.

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 23/24
_chunk 1212 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

Kristin Krogman   1:15:14 from the Retail Client Services inbox, because that one I don't put my name on. That's just coming from that, you know, inbox saying, hey, but there is an automatic reply on that e-mail that says, we're not using this anymore. So they shouldn't be, they should be getting that as well, telling them this isn't a live e-mail.
 Juan Martinez   1:15:20 Hello. Okay.
 Kristin Krogman   1:15:37 quit using it, right? Because Retail Client Services doesn't exist. So we looked at it for a long time just because clients were so used to it that they kept, you know, they just had in their inbox, right? Their own, when they type up an e-mail, they're like, oh yeah, this one. And we're forgetting that they shouldn't be sending it there. Now, it's been several years and they're better about
 Juan Martinez   1:15:43 Okay.
 Kristin Krogman   1:16:01 not sending e-mail there. That's why that one, like I said, it's really quieted down and I barely get anything. So not a problem. And they usually copy somebody else. That's where you guys are going to run into some trouble, is we have some clients that refuse to open tickets. And we keep telling them.
 Juan Martinez   1:16:06 Okay. Okay.
 Kristin Krogman   1:16:21 you need to open tickets. Well, they're going to find out now why we kept telling them because they're used to, you know, emailing Carrie directly. you know, to get help. And it's like, no, open a ticket because what if I'm not here? Well, they're going to run into that real quick.
 Juan Martinez   1:16:32 Okay. Yeah, yeah, yeah, yeah, okay, okay.
 Kristin Krogman   1:16:43 So, yeah, but utilize your customer, the CSM, the customer success managers. If you have trouble with the clients and need any help, just remember those people are there to assist. They want their customers happy. So if you do run into issues,
 Juan Martinez   1:16:52 Yeah.
 Kristin Krogman   1:17:03 you know, with clients and you're not opening tickets and you need some help with that sort of thing, they're there to help you with as that as well with the communication.
 Juan Martinez   1:17:13 Oh, okay, okay. Thanks, Kristin. Thanks. Thanks.
 Kristin Krogman   1:17:13 So. Yep. Okay. Well, you just tell me when you think you'd like to go kind of step by step through what happens in the morning and we can set something up.
 Juan Martinez   1:17:26 Hey, can you have time on the Friday at Friday?
 Kristin Krogman   1:17:30 Where did my schedule go? Did I close that? Yeah, I should have. You'll just have to tell me what time I think from 10. Ten to 11 on Friday, I think I had a meeting on my schedule.
 Juan Martinez   1:17:47 Um... No, I have a...
 Kristin Krogman   1:17:56 Yeah, what do you have?
 Juan Martinez   1:18:00 Mm. Let me check. Maybe at 8 AM.
 Kristin Krogman   1:18:09 Eight o'clock to 9. I can do that.
 Juan Martinez   1:18:12 Hey, I am at Friday. Yeah, I don't have, I have a super stand up, but I can stay in this new meeting if you have time.

## Reunión 2026-07-14 — KT Kristin: help inbox, portales, cierres, Tiger Team · Transcripción 24/24
_chunk 1213 · 2026-07-14 · fuente: kt-kristin-2026-07-14-oficial_

Kristin Krogman   1:18:24 Yeah.
 Juan Martinez   1:18:24 is more important right now.
 Kristin Krogman   1:18:26 Well, well... I was gonna say it, it doesn't matter.
 Juan Martinez   1:18:29 Or A to maybe. What? Sorry, I think that I closed the call. Sorry. 8 to 9 AM or after in at 10 AM to yeah, to 11 or 12. I don't know. I have time.
 Kristin Krogman   1:18:55 Okay, yeah, because I can miss that 10 o'clock meeting, that one I can miss. So whatever, if that works better for you, so you can still do your 8 o'clock, that's fine. You want to do 10 to 11?
 Juan Martinez   1:19:07 Yeah, that's fun. Yeah, 10.
 Kristin Krogman   1:19:09 Okay. Ten to 11. Perfect. I'll set that up on Friday. And if, yep, if something comes up before then that like you should see, I'll let you know. Okay. And if we have to just jump on a quick call, we'll do that. Or if you want to do another, you know, if you want to do more knowledge share, just reach out. That's what I'm here for.
 Juan Martinez   1:19:12 Thanks. And Tracy. Okay, okay. Okay, okay. Thanks, Kristin. Thanks. Bye bye. Have a good day.
 Kristin Krogman   1:19:30 All right. Talk to you later. Bye-bye.
 Juan Martinez detuvo la transcripción

## Topic 1 · Knowledge Transfer — ¿Qué maneja Consumer Support?
_chunk 214 · 2026-06-03 · fuente: /Users/MancoMenStudio/Desktop/topic1_knowledge_transfer.html_

El equipo maneja consultas y disputas de consumidores finales a nivel global. Son consumidores que recibieron un retorno negado en una tienda retail (ej. Walmart, Target) y quieren cuestionarlo.
Hay dos equipos: L1 (Call Center ejecutivos) y L2 (escalaciones, disputas, relaciones).
El call center opera 24×7×365 con números 1-800 dedicados por cliente y scripts personalizados.

## Topic 1 · Knowledge Transfer — ¿Qué es un Consumer Dispute?
_chunk 215 · 2026-06-03 · fuente: /Users/MancoMenStudio/Desktop/topic1_knowledge_transfer.html_

Un email que el equipo recibe de un consumidor pidiendo revisión de un retorno negado o una reclamación. No es un RAR (Return Activity Report — ese se procesa diferente).

## Topic 1 · Knowledge Transfer — Self-Service Portal
_chunk 216 · 2026-06-03 · fuente: /Users/MancoMenStudio/Desktop/topic1_knowledge_transfer.html_

Los consumidores pueden ir a www.theretailequation.com para:
• Pedir su RAR (Return Activity Report)
• Encontrar formas de contacto (teléfono, email, web)
🔧
Herramientas internas: Jira (tracking de tickets) + CRM (herramienta custom por cliente — acceso en Incident Search / returnx.com ). Necesitas acceso al CRM para procesar disputes.

## Reunión 2026-06-10 — Customer support experiences · Resumen
_chunk 724 · 2026-06-10_

## Resumen
The meeting focused on sharing personal experiences related to customer support, whether external or internal. Participants discussed various scenarios, including handling critical incidents, managing customer sentiment, and learning from mistakes. One participant shared a story about a Black Friday outage, emphasizing the importance of trust-building and clear communication during crises. Another highlighted the need for proactive measures like stress-testing infrastructure to anticipate spikes in demand. The concept of accountability and learning from mistakes was reinforced through examples such as a 'Wall of Failure' initiative, where team members documented and shared their errors to foster a culture of transparency and improvement.

The discussion also touched on the psychological impact of involving managers in customer interactions, noting that their presence often helps calm frustrated clients. Participants shared strategies for maintaining composure under pressure, including frequent updates and leveraging team support. The importance of balancing work and personal life was emphasized, with reminders that team members should not feel obligated to be available 24/7 unless explicitly required. The meeting concluded with encouragement to continue sharing experiences in future sessions to build trust and camaraderie within the team.

## Temas clave
- Customer support experiences
- Learning from mistakes
- Proactive preparation for spikes

## Decisiones
- **Continue sharing customer support experiences in future meetings.** — To build trust and camaraderie within the team.

## Tareas / Action Items
- Think of additional customer interaction experiences to share in the next meeting. — vence 2026-06-17

## Insights en vivo (Ask AI / Analizar)
### [Ask AI] Tienes el contexto de la reunion o el topic, puedes crear una historia o situacion para compartir?
[Error 400: The response was filtered due to the prompt triggering Azure OpenAI's content management policy. Please modify your prom]

### [Ask AI] Tienes el contexto de la reunion o el topic, puedes crear una historia o situacion para compartir relacionada con el topic del meet? Hi team, I'd love us to use our upcoming time together to share a personal experience around supporting a customer, whether that's a stakeholder, a teammate, or an internal...
Sure, I can share an example that ties directly to our work in L3 Support. One time, we had a critical ticket where a customer’s application was completely down during peak business hours. The initial diagnosis pointed to a configuration issue, but after digging deeper, we discovered it was actually a data replication failure between Greenplum and Snowflake. The customer was understandably frustrated, and the pressure was high because downtime was costing them thousands per hour.  

What worked in that situation was clear communication: we followed the escalation playbook to package the issue for Engineering, but we also kept the customer updated every hour, even when there wasn’t new progress. That transparency helped rebuild trust. On the technical side, we collaborated with Data Ops to implement a temporary workaround while Engineering worked on the root fix. The application was back up within four hours, and the customer later mentioned that our responsiveness and clarity made a huge difference.

- **Key actions taken**:  
  - Used the escalation playbook (T-006) to ensure Engineering had all the necessary details: symptom, reproduction steps, customer impact, and attempted fixes.  
  - Maintained hourly updates to comply with Update Rate rules (T-071), even during investigation phases.  
  - Coordinated with Data Ops for a temporary data sync workaround while waiting for the permanent fix.  

- **Lessons learned**:  
  - Early escalation is critical for high-priority issues, but packaging the ticket properly avoids delays.  
  - Customers value consistent updates, even if there’s no new progress — it shows accountability.  

- **Follow-up questions to ask the team**:  
  - Have we had similar cases recently where downtime impacted customer trust?  
  - Are there gaps in our current escalation process that could slow down resolution for critical tickets?  
  - How do we ensure temporary workarounds don’t introduce new risks?  

Let me know if you'd like me to refine or expand this example further.

### [Ask AI] Tienes el contexto de la reunion o el topic, puedes crear una historia o situacion para compartir relacionada con el topic del meet? Hi team, I'd love us to use our upcoming time together to share a personal experience around supporting a customer, whether that's a stakeholder, a teammate, or an internal... pero que no tenga que ver con Appriss, debe ser una anectoda personal de otra empresa o situacion general, es compartir una experiencia pero no dentro de nuaav o appriss
Sure, I can share a personal experience from a previous role. I once worked on a project where we were supporting a retail client during their busiest season — Black Friday. Their e-commerce platform was experiencing intermittent outages, and the issue was traced back to a scaling problem in their cloud infrastructure.  

What stood out in that situation was the collaboration across teams. While the engineering team worked on scaling the infrastructure, my role was to manage communication with the client. I made sure they were updated every 30 minutes, explaining what was being done and setting realistic expectations. At one point, we even had to implement a temporary traffic throttling mechanism to stabilize the platform while the permanent fix was being deployed.  

The client appreciated the transparency and the fact that we were proactive in minimizing their downtime. It was a reminder that technical expertise is important, but clear communication and empathy are just as critical in high-pressure situations.

- **Key actions taken**:  
  - Frequent updates to the client every 30 minutes, focusing on transparency and setting expectations.  
  - Coordinated with the engineering team to implement a temporary traffic throttling mechanism.  
  - Documented the incident thoroughly for post-mortem analysis and future prevention.  

- **Lessons learned**:  
  - In crisis situations, clients value honesty and realistic timelines over vague reassurances.  
  - Temporary fixes can be lifesavers, but they need to be carefully managed to avoid introducing new risks.  

- **Follow-up questions to ask the team**:  
  - Have you ever had to balance technical troubleshooting with customer communication under pressure?  
  - What strategies have worked for you in maintaining trust during critical incidents?  
  - How do you ensure temporary fixes don’t become permanent solutions?

### [Ask AI] algo que agregar? estan hablando despues de escuchar mi experiencia.
I think that’s a great point about anticipating spikes and preparing ahead of time. In the story I shared earlier, one thing we learned was the importance of piloting solutions before peak times. For example, in the Black Friday case, if we had stress-tested the infrastructure earlier, we might have caught the scaling issue before it became a problem. It’s not always possible to predict every scenario, but building in those preventive measures — like load testing or simulating high traffic — can make a huge difference.  

I’d be curious to hear if anyone else has had experiences where proactive preparation helped avoid a major issue, or if there were cases where something unexpected still caught you off guard despite planning.

- **Key takeaway from the discussion**: Proactive measures like piloting and stress-testing are critical for high-traffic events.  
- **Follow-up questions to ask the group**:  
  - Have you ever implemented a pilot or test that uncovered a hidden issue before a big event?  
  - What strategies have worked for you in balancing preparation with the reality of unexpected challenges?  
  - Are there specific tools or processes you’ve used to simulate peak conditions effectively?

### [Ask AI] alguna pregunta para esta persona que nos esta contando algo sobre su experiencia con customer y el shadowing que esta haciendo?
Thanks for sharing your experience! I’m curious about the shadowing process you mentioned — how did you find it helpful in understanding customer sentiment or improving your responses? Were there specific patterns or techniques you picked up during the shadowing that you think could be applied more broadly across the team?

- Shadowing is a great way to learn customer communication styles and expectations.  
- Follow-up questions:  
  - Did you notice any recurring themes in the types of issues customers raised?  
  - Were there any particular strategies or phrasing that seemed to resonate well with the customer?  
  - How do you think shadowing could be structured to benefit others on the team?

### [Ask AI] Alguna pregunta para camila y su previa experiencia? o aportar algo que complemente lo que ha dicho, algo de valor.
Thanks for sharing that, Camila. It’s really insightful how you emphasized both educating the customer and setting clear expectations upfront. I’m curious — when you were managing those escalations, did you find any specific tools or processes that helped streamline communication, especially when dealing with customers who were opening multiple tickets for the same issue? Also, how did you balance being proactive with updates while ensuring your team wasn’t overwhelmed by constant follow-ups?

- Camila highlighted two key strategies: educating customers on efficient system use and setting clear expectations for updates.  
- Follow-up questions:  
  - Were there any automation tools or templates you used to manage repetitive communication effectively?  
  - How did you handle situations where customers were resistant to consolidating their tickets or following the recommended process?  
  - Did you notice any patterns in customer behavior that helped you anticipate and prevent escalations before they reached the executive level?  
- Complementary insight: You could mention how proactive communication aligns with the Update Rate compliance process in Appriss (weekly updates rule), drawing parallels to her approach.

### [Ask AI] algo que agregar sbre cometer errore sy aprneder de ellos?
I think that’s a really valuable perspective — mistakes are inevitable, but accountability and learning are what truly matter. One thing I’d add is that being transparent about the mistake and the steps you’re taking to resolve it can actually build trust with the customer or the team. For example, in my own experience, when we faced a major outage during Black Friday, we didn’t just focus on fixing the issue; we also communicated openly about what went wrong and what we were doing to prevent it in the future. That level of transparency turned a difficult situation into an opportunity to strengthen relationships.  

I’d be curious to hear if others have had moments where owning a mistake led to a positive outcome, either with a customer or internally within a team.

- **Key addition**: Transparency and accountability can turn mistakes into trust-building opportunities.  
- **Follow-up questions for the group**:  
  - Have you ever had a situation where admitting a mistake improved your relationship with a customer or colleague?  
  - What strategies have you used to ensure mistakes don’t happen again, especially in high-pressure environments?  
  - How do you balance being accountable without over-apologizing or undermining confidence in your team’s capabilities?  
- **Example to share**: Black Friday outage story — focus on clear communication and preventive measures post-incident.

### [Ask AI] algo que agregar sbre cometer errore sy aprneder de ellos? en base a lo que ya dijeron en la transcripcion para no repetir lo que ya dijeron.
Building on what’s already been shared, I’d add that mistakes can also be an opportunity to improve processes, not just individual accountability. For example, if a mistake reveals a gap in documentation or a missing safeguard in production workflows, addressing that gap can prevent similar issues across the team. It’s not just about fixing the immediate problem — it’s about using the mistake as a lens to strengthen the system overall. I’d be curious to hear if anyone has had a situation where a mistake led to a broader process improvement or even a new best practice for the team.

- **Key addition**: Mistakes can highlight systemic gaps — documentation, automation, or process safeguards.  
- **Follow-up questions for the group**:  
  - Has anyone experienced a situation where a mistake led to a new team-wide process or tool implementation?  
  - How do you balance resolving the immediate issue with taking time to reflect on broader improvements?  
  - Are there any examples where a mistake actually led to innovation or a better way of doing things?  
- **Complementary insight**: This ties into the importance of RCA (Root Cause Analysis) mentioned earlier — not just identifying the cause but using it to drive systemic change.

### [Ask AI] algo que agregar sbre cometer errore sy aprneder de ellos? en base a lo que ya dijeron en la transcripcion para no repetir lo que ya dijeron. o sobre otro de los topic que se han hablado y complementen todo esto? algo de valor y con sentido en lo que estamos hablando.
I really like the idea of the "wall of failure" that was shared — it’s such a powerful way to normalize mistakes and turn them into learning opportunities. One thing I’d add is that documenting mistakes doesn’t just help the individual; it can also uncover patterns that might point to systemic issues. For example, if multiple people are writing about similar failures, it could signal a gap in training, unclear documentation, or even a process that needs rethinking. So, while it’s great for personal growth, it’s also a chance to improve the team’s overall resilience and efficiency.  

I’d be curious to hear if anyone has seen a situation where documenting failures led to a broader process change or even a cultural shift within the team.

- **Key addition**: Mistakes can reveal systemic patterns — training gaps, unclear processes, or missing safeguards.  
- **Follow-up questions for the group**:  
  - Have you ever noticed recurring themes in mistakes that led to a team-wide improvement?  
  - How do you balance individual accountability with using mistakes as a lens for systemic change?  
  - Are there any examples where a mistake led to a cultural shift, like more openness or collaboration within the team?  
- **Complementary insight**: This ties into the idea of psychological safety — when people feel safe admitting mistakes, it fosters innovation and continuous improvement.  
- **Potential connection**: The "wall of failure" could align with Appriss’ focus on RCA (Root Cause Analysis) and using lessons learned to refine processes.

### [Analizar] Sometimes a small attention is very important.
The key takeaway from this discussion is that small, intentional actions—like promptly acknowledging a customer’s concern or escalating an issue through the right channels—can significantly impact customer sentiment and trust. It’s not just about solving the problem but also about showing attentiveness and accountability, even in high-pressure situations.

**Resumen:**  
- Several participants shared experiences emphasizing the importance of customer communication, accountability, and learning from mistakes.  
- Nikita’s story highlighted composure and perseverance during a challenging incident, with support from her team.  
- The "Wall of Failure" concept from Expedia was discussed as a way to normalize mistakes and foster learning.  
- A story about LinkedIn escalation during Diwali illustrated the need for proactive monitoring of all customer channels, especially for P1 issues.  
- The recurring theme was that small, timely actions—like responding quickly or involving managers—can de-escalate situations and build trust.  

**Decisiones detectadas:**  
- Mistakes should be documented and treated as learning opportunities (e.g., "Wall of Failure").  
- Managers or leads should be involved in critical customer interactions to reassure clients.  
- Proactive communication is essential, especially for P1 issues, to prevent escalations through unconventional channels like social media.  

**Tareas / action items:**  
- Consider implementing a "Wall of Failure" or similar mechanism to document and learn from mistakes.  
- Review escalation protocols to ensure all customer channels are monitored effectively, especially during holidays or off-hours.  
- Train team members on maintaining composure and accountability during escalations.  

**Cruces con tu segundo cerebro:**  
- **T-005 Customer escalation playbook**: Reinforces the importance of timely first-response and escalation protocols.  
- **T-091 Inbound customer channels**: Highlights the need to monitor unconventional channels like LinkedIn for escalations.  
- **T-071 Update Rate compliance**: Aligns with the emphasis on proactive communication and regular updates.  

**Aclaraciones:**  
- The "Wall of Failure" concept could be explored further—how was it implemented, and what measurable benefits did it bring?  
- The LinkedIn escalation example raises a question: are there documented protocols for handling social media escalations in Appriss?  

This analysis ties directly to operational priorities like escalation management and customer sentiment monitoring.


---

## Reunión 2026-06-10 — Customer support experiences · Transcripción 1/12
_chunk 725 · 2026-06-10_

## Transcripción completa
Okay, did you guys Did you guys have the chance to bring an experience? I think an experience you have with a customer. Yeah, I have like one or two things. I had a couple of things. I had couple of time, but I had one of the stories, kind of. Yes, please decide which one you're going to share because I want that everybody is able to It's able to share their experiences and that we have time. We have time to discuss together, maybe. Also, we're not being appealed to make sure that he is here. I'm also going to record this because That's because I know that we're going to share really interesting stories. Just give folks two more minutes and we can get And we can get it started. Okay, I think we can get us started. I'm going to start recording while we wait for a couple of minutes. Okay, great. So anybody that was Anybody that wants to start sharing their experiences or do If you want it, let's go open. Either of both. It's okay. Go for it. And I think something that is really That is really important in those situations when we expect spikes. I know that here in Apprice, we don't expect that much. I really spoke with Amy if there are any questions. We need to be prepared, but in other projects that work, We are not in the process of doing this work. Sometimes we can prevent that. That is a Black Friday. We're going to receive a lot of requests. We can expect spikes, so we can be prepared for that. I think that is also something that Something that you can start looking at, for example, if your customer does that you are working on with some specific things. Think on the application and expect something happening in a specific In a specific date or week that you can prevent that and say, hey, We need to prepare for this and we need to We need to review if there is any way that we can pilot these before. We are going to go live, so we don't have any changes. And, you can make changes or make your origins while you are alive.

## Reunión 2026-06-10 — Customer support experiences · Transcripción 2/12
_chunk 726 · 2026-06-10_

Anything anyone want to comment about this? Any comments? Any other questions or comments? We'll be starting with Kevin, and show you something it's about. It's about work items and the attractor. And what is some business concept like, director supply? The live quiz or quiz or clean code. Let me check what is our audit manager. What means how did manager call now? On our application, so I was working with one or two Or two work items tickets, I fixed one. Also check with carry what is What is that area about some reports? How can we fix some reports failed that we have failed? I was working with I was working with Daz, I will share it with the team. A document or some documentation or some videos. Thank you for your time. With like working with Keri and also the customer itself. Also, if you, if there were any Hints or alerts about the customer sentiment. Can you comment, anything that you can share with us? Yeah, just we were shadow... I showed you my ring, so she answered. I'm not sure if the answer to the client, but I think as a technical Technical team, as technical team on our reporters. So maybe I don't have experience I'm very happy to have experience talking with my client or I saw Answers on these tickets, so I took it. I took this information for me to learn how to Learn how to answer these questions or these issues. Great, if you can share those two. Share those tickets that you have worked on that Alo Yoga ticket so we can So we can see like how was the interaction. I think that would be really helpful for us. Thank you for being helpful for all of us to see how the communication is managed. Hi, Kapil, thank you for joining us. Apologies for being... That's the right way to do this meeting. I'm not important, I'm just listening. Fly on the wall. Yeah, we are sharing our own experiences. As you asked us, we came with one example. For example, we already heard Juan and Diego.

## Reunión 2026-06-10 — Customer support experiences · Transcripción 3/12
_chunk 727 · 2026-06-10_

So anybody else that want to share their experiences? Volunteer or Volume Fold? You decide. I can go next. You can go next, so you don't feel like you are in the spot. So in my previous company I was managing escalation Customers that they know you're working your best to help them. I'm going to talk about the other side of the topic. The company, for some ways, for example, Reddit, they end up with the C. This is a very simple example of how to use a custom API. Is that executives email my team say, hey, this, this, This client reached out to me saying that XYZ is not working. This is not working. Something that I learned on this kind of situation. This was generalized, sometimes people do not understand Understand that you are doing your best to help them. It's people that are not paying us enough. This thing that we used to do is first understand which kind of How much would it cost to run a customer? That's to really put an effort of multiple people, multiple engineers to help them. I call the customer and say, hey, Camilla, we really know what is happening. I have my team up. I'm not sure if you have my team on this, but actually, even though if you reach out to the The way time will be the same. So if you keep sending emails, if you keep opening tickets, we're not going to wait We are not going away to track what has been done and which is the status. This is a very important part of the project. In a phrase that we have customers that open multiple tickets for the same issue, The second thing that I learned from this is that we need to educate also our customers. We have a lot of questions from our customers on how to use our systems efficiently. 10 tickets open with 10 different agents or engineers that will They will give you different information. So if you already have a ticket open, We can keep the information and traction in the It is difficult because We also have a lot of customers that are not able to push back. And then again, expectations.

## Reunión 2026-06-10 — Customer support experiences · Transcripción 4/12
_chunk 728 · 2026-06-10_

So I'm sure that in ticket one, two, three. In the next two hours, you're going to have an update from myself or someone on my team. I got you. My name is Camila Cortez. I'm a manager of the escalation I'm a Congratulations team and you can be sure that I will contact you or someone in my team. My team. And every two hours, if we need to extend the... And the update time because we don't have new updates for you. We will let you know in advance. We are not keep it silent so you don't need You don't need to reach out to anybody because we are reaching out to you in advance. So that was the learning and actually that helps a lot. That these kind of customers stop emailing CEOs because Because they just find out the email or the number or on LinkedIn. We are very excited to be able to reach out to some executives because they don't hear from anybody. Any questions about it? Anything that you want to comment on that experience? Okay, great. So who is the next one that is going to show? I'm just going to share their thoughts. Most of us may not be from support, which is So, which is okay, like, you know, if you heard my experiences, I talked from I talk from either dealing with a customer support or I talk from a perspective of This is a form of me helping a client. If we are a support team or not, or engineering team, we always deal with client. So your experience can come from anywhere because here world we are using And as we said before, I don't know whether I was talking to you or somebody else. Anybody is a customer for us. Even engineering team, if they need anything from us, It's a great way to get anything from us, they are customer for us. So please bring it, the point of The point of conversation is, for us to see what have we experienced We have experienced and learned with our interaction with And then humans who need something from us. So, of course, Kubler has like relevant context. I do not, but I do have... I do have other experiences that I can share.

## Reunión 2026-06-10 — Customer support experiences · Transcripción 5/12
_chunk 729 · 2026-06-10_

Don't worry about it. It doesn't have to be a support team context. It could be any human customer interaction. Or I'm going to start with the first person I see in my screen. Okay, they're done. You go next in my screen. Honestly, I don't have anything. I can think of right now at the moment. I worked with engineering teams. I know everyone is a customer, right? I don't have anything to share. You never had a problem with anybody? Your boss, maybe someone from other team that was requesting you something and it was not that It was not that easy to manage. Nothing has anything like that. I don't have anything. This is a very important thing. No problem. Yeah. Try to think about it and maybe... And maybe you recall something later, okay? If you have something interesting which relates to this, I will definitely share with you. Perfect. I'm glad you are the next one. The next one in my screen. Okay, Nikita, go for it. Yep, I can. I don't really have a custom Customer Support Experience, but a long-term client project. I'm going to go ahead and talk about the design project experience that I can share and Kapil already knows that. I also have experience around this pipeline. This is a spike thing. So we were working for a tough question. So, there I was creating a We have a recipe in their project management tool and Within a span of 6 to 7 hours. There was a spike in the tokens used. And they have a year after year. We have a link here and one subscription for that. My recipe there, it almost... Post consumed 50% of their annual subscription. So, it was a It was a nightmare for me. The other thing I learned from that is you should do a Do a proper reporting and you should do a RCA and And, communicate properly with your client, with your customer. It's okay to make mistakes, but Do not repeat them and learn from them. Make sure you don't make same mistakes. I will give you a few more questions. We have a lot of questions.

## Reunión 2026-06-10 — Customer support experiences · Transcripción 6/12
_chunk 730 · 2026-06-10_

Before doing any work directly in the product, I will be doing the production. So that is the thing I learned. And a great thanks to Kapil, he consoled me very well by giving a lot of A lot of examples, like it's okay to make mistakes, but like it, uh, Somebody is going to like, school. Scholier or anything, but yeah, that was my experience. I'm not sure if it's really important and it's like it's okay to make mistake but also to be accountable like hey, I know. I made the mistake and I'm also working on the resolution. Being accountable makes You feel it like your own. And I think that is what Mikita shared with us. Not only, yes, I made a mistake, I'm going to resolve it. I'm going to resolve it, but yes, I'm accountable. I made that mistake. I know where it lives and how it works. It's not going to happen to you again or anybody else because it could be a learn from them. Thank you, Nikita. I was involved in that incident. And I'll tell you, the most important piece that Nikita missed out of this, It was her composure. See she was open by a couple, like two, come in last point. Mistake. She kept her composure and she She kept persisting on it. We got out of it with flying colors, honestly speaking. With learnings, like I now proudly nickatize sharing that incident that speaks That speaks a lot about her composure, her perseverance that she needs. That's what everybody needs, right? So a load of kudos goes to Nikita for We are very happy to be here. Very unhappy. When I got escalation, point them, I was, they were bad. And And finally we came out with, okay, fine, you learned something, just make sure we don't recruit everything. All good goes to Nikita for that. And also, as you said, the customer was really mad. You can also support on your leads and your managers to manage customer sentiment. Because sometimes people just, ah, there is some manager in the call, they just feel relaxed. So relax, that's it.

## Reunión 2026-06-10 — Customer support experiences · Transcripción 7/12
_chunk 731 · 2026-06-10_

So sometimes you can support on your leads or your managers. This is a very good example of how to use the word Just talk with the manager. Only if the manager is there, they will feel better. I don't know why. I don't know why there is a psychological thing about it, but yes, you don't need to You don't need to deal with mistakes or with difficult customers by yourself. And nobody will have a bad intention, right, behind a mistake. A mistake is a mistake, right? At the end of the day, you know, There is a right judgment in the sense, It was a mistake, you did it unintentionally and And you have a culture of learning from your mistakes. That's how you know support as a process or person That's why this person evolves around technical expertise. And, you know, gain experience within the KQL. When I was working at Expedia, I used to follow a philosophy there, it's called wall of failure. Wall of failure. We used to celebrate each and every failure that we have. We were working with hundreds of customers there as well. It was leading outbound payments, so payments were going out and you know payments. This is why you need to be able to get the payment. Nobody is happy with payments, right? Like, you know, my payment is delayed, like, you know, My payment term was net 30, you are paying me at 45. I need sooner because there was a hurricane hit my hotel, I need to be paid sooner. Lot of issues, right? Nobody, none of our customers were ever happy. I will be happy. And a fall wall of failure. Same thing that Nikita was just talking about, what Viraj just mentioned exactly. Quick failure is a failure if you learn something out of it because you did not have real intention. All of these things are going to be in the same way. Let's understand what is it. We should document it. I actually literally had an actual goal. Anybody can stand up and go. Next day or once in a day, Sometimes people do not feel comfortable talking about it, but they mention it there.

## Reunión 2026-06-10 — Customer support experiences · Transcripción 8/12
_chunk 732 · 2026-06-10_

No name is written. So, and if we read it, we all, who's on it wants to share, they can share more about Share more about it. What did we learn? If you did not want to share anything, it's fine. We'll move on to the next one. This is what I did wrong. The moment you write it, I'm telling you 90% of the roll-up is already solved. Because your mind thinks differently. If you write it, I did this wrong, your mind Your mind sinks it, oh, I found the solution. You get the confidence, your guilt is gone. So, if this idea This idea seems right. You could follow that. My team actually benefited I got to accept that I did a mistake as a person. It does, I agree. It takes time to start getting, having that gut I think that got correct. So I was the first one who wrote in that wall, I think. Because initially, Vault was empty, it was like, man, why are we not making mistakes? It's a problem. Honestly speaking, if we are not making mistakes, there is something wrong with that too. We can never be perfect. So in this case, you are hiding something, or we are manufacturing something, which means that's the one. So, and then once I started writing once or two, and then after that wall was filled, every day we had to take snapshot of it. Tap shot of it, erase it, and then start writing again. So that was fun. It was fun. It was fun. Yeah, and also like maybe you are not making mistakes. You don't need to make mistakes to make enhancements to To work on your efficiency, how you're doing things, so yeah. Yeah, if you are too comfort, that something is odd. You need to recover. I think we have time for one last One last story or experience to discuss. And we can take next week to hear the rest of you guys. Anybody that want to take it? Okay, yes please go.

## Reunión 2026-06-10 — Customer support experiences · Transcripción 9/12
_chunk 733 · 2026-06-10_

So lastly, I was working in a startup, right? The company doesn't have a lot of good processes, so there are multiple ways where supporting Support ticket will come in, right? Not every customer had a habit or CSM's So, if they come If they come from different channels, we create the ticket on behalf of the customer and work upon. I remember the time After a time in Diwali, I went to Kerala, that's something south of India. I was just scrolling something on Something on LinkedIn, just like that. Some of the, one of the customers, He messaged me. Hey, my systems are Systems are down, the opportunities are not sinking. Can you please take a look at this? And then I saw, and this was very strange, and then I saw So, he went to LinkedIn and he did the work spend. Workspan, couple of places, my previous company, and And he tried to make a sim out of there in social media. In the end, social media and everywhere. Basically, there was oncall support. Oncall support, but somehow, you know, that guy was also some in their laser mode. Visual mode, not paying attention of what's coming in work-wise. So, sometimes what learning that I had from this is So, the reason why this is, if you are not hearing If you are not hearing out your customers, or whatever mediums they have, They have exhaust those mediums to Get support for a P1 issue that That is actually impacting the bottom line, that is actually impacting We are going to be impacting if that person is able to The application is able to do his or her job or not. It literally impacts them as a The company that they work impacts as a customer for the And then, we have a number for the company that we work with, right? What I think is a very important part of any company We posted some messages on LinkedIn, tagging WorkSpan and our CEO and all So, I'm going to go through the process of doing this. I can open my Slack and just texted the guy and he did not He did not respond to me in 5 minutes, so I called him up. Amen.

## Reunión 2026-06-10 — Customer support experiences · Transcripción 10/12
_chunk 734 · 2026-06-10_

Are you here? Are you on your computer? He was like, yes, yes, what's happened? He actually was asleep or maybe somewhere in some Diwali functions and I made sure that even that is this something that came up to me, customer is Postmortem is messaging us on LinkedIn. There was a paging on Slack. I think you didn't I can't come to my laptop, but I can get you resources Resources if you need, other people in the company who can, you know, basically can come online. Sometimes a small attention is very important. So, that's all for today. If you work from home, work ethically, at least you know. Try to check things in your phone, right? Kamila messaged me. Hey, I reached Hey, are you joining? I said, hey, give me five minutes. There was a road accident. I'm just coming over. So, at least check your notifications when you are working. It's okay if you go here and there. Make sure you are attentive to those things because your misattention to one thing can We can have a lot of bigger impact on the other side of the world. Yeah, this was one of them. Yeah, and I think that's really important. Like you need to Like you need to read your customer and sometimes your acknowledging the sentiment will help a lot even though Even though you don't have a resolution. But I want to also let I don't want anybody And that is why We will make sure that there is someone there. Of course, if you are paying, you need to be working and if something outside of the ordinary has We are just like, hey, I cannot join because this and this happen, communicate, but also I don't want you to And I want you to be 24-7 there because that is why we are a team. So if you are not on call, now not that. Not primary, not secondary, no working hours. You should not be doing anything because you have a life, like you are a person, you have Longer than it is suspected because that is the expectation and I do not And we are not going to spend you to be there always if you were not requested to.

## Reunión 2026-06-10 — Customer support experiences · Transcripción 11/12
_chunk 735 · 2026-06-10_

Thank you very much. Feeling the sentiment, and also hear that the customer is important. Just so I conclude, it's very important that you be attentive in what And come to your manager's or whatever's notice. So just be attentive in your hours. You can also use the link in the description below. And I think it's important to understand that Your colleagues can see he is on break or he is away or whatever, you know. Yeah, great. I know we are already over time. I'm going to talk about the experience of the time. So those who weren't able to share their experience, There are a lot of different experiences. Please think about it. It could appear, it could be another theme. A client external or internal, even your leader or someone... That is in your same team. We can share those so we can wrap up on these conversations. Conversation about our own experiences. Kapil, do you want to add anything else? No, I think you pretty much covered it. I think this is not a conversation for one time. I think this is something that you will call That's the thing that you will constantly continue to share. You know, what I am really looking forward is, The team is feeling comfortable with each other. What I feel is like, you know, we, the team is the The first one is the second family for each one of us. We spend most of the time together. You spend 8 of that hours here, the rest of the 8 hours you are bathing, you are doing You are doing your normal chores, errands and stuff. So you spend most time with this family. So start being comfortable, hold each other's back is all I would say. I mean, none of us are perfect. I'm not perfect, right? Like, you know, I will make mistakes, but... But what makes me good is you. When you hold my bat, I feel good about it. I can go into the world confidently, We are talking about how I feel, how I am doing, sometimes just my And then, my personal life is interrupting me. Coming back to you helps me regenerate. Other way, my customers are hard.

## Reunión 2026-06-10 — Customer support experiences · Transcripción 12/12
_chunk 736 · 2026-06-10_

Coming back to you, talking to them about it, taking some ideas, we hold each other back. That's what we do. That's what we do, that's what teams are for. And that's the whole intention of this conversation. So please take care of each other. Okay, just one question to your couple, are you also coming on 26th with Umesh? No, not to India. I'm coming to Colombia, though. I will travel to India, But sometime soon this year, maybe September timeframe is when we That's when we plan to travel. Sure, thanks. Thank you, team. So we'll see you next week. Thank you very much. Bye, everyone. Bye everyone. Thank you Tim. Thank you for coming. Thank you. Thank you. Bye bye. Thank you, bye bye.

## Reunión 2026-06-03 — Consumer Support processes · Resumen
_chunk 851 · 2026-06-03_

## Resumen
The session focused on knowledge transfer for Consumer Support processes, specifically addressing T-001 (disputes, L2/L3 support, and support data) and T-003 (close-out timelines of 7/14/28 days). Key discussions included the Return Activity Report (RAR), which provides a two-year history of consumer purchases and returns for dispute resolution, and the CRM system used to manage disputes. The process for submitting help desk tickets for access issues was demonstrated, emphasizing the importance of business justification for Infosec approval. Documentation locations in SharePoint and Confluence were reviewed, including consumer support knowledge bases and client contact lists. Questions arose about automating manual processes like maintaining client contact lists and tracking dispute resolution timelines by retailer. Andrea was tasked with adding definitions to Confluence pages, and the need for updated documentation and dashboards was highlighted.

## Temas clave
- Consumer Support processes
- Return Activity Report (RAR)
- Help desk ticket submission
- Documentation in SharePoint and Confluence

## Decisiones
- **Client contact list will remain manually maintained for now.** — Automation tools are not yet evaluated.

## Tareas / Action Items
- Add definitions to Confluence pages related to Retail Tenant Support and Consumer Support knowledge base. (resp: Andrea)
- Verify if Andrea’s team has a list of dispute resolution timelines by retailer and share it. (resp: Andrea)
- Evaluate automation options for maintaining the client contact list.
- Update the Confluence section on 'Work Item not functioning properly' with troubleshooting steps.

## Insights en vivo (Ask AI / Analizar)
### [Ask AI] puedes hacer otra pregunta en base a la pregunta para aclarar lo de RAR
Could you clarify the exact scope of the Return Activity Report (RAR)? Specifically, does it only cover purchase and return history for the last two years, or does it include additional data points like dispute outcomes or flagged transactions? Also, is the RAR generated automatically for every dispute, or is it only pulled upon request during the dispute process?

- RAR seems to be central to understanding consumer behavior and dispute resolution. Confirm if it’s tied to Salesforce or another backend system.  
- Follow-up: Is there a standard format or template for the RAR, and where is it documented?  
- Edge case: What happens if a consumer disputes the accuracy of the RAR data?

### [Ask AI] hay algo mas que deba pregintar sobre los tiempos dedispute responde en bas e alo que me acaban de decir?
Based on what you just explained, I understand that the dispute resolution timeline varies significantly by retailer, ranging from same-day responses for Home Depot to up to two weeks for others. My question is: are there any specific retailers or scenarios where the timeline consistently exceeds the two-to-four-week range you mentioned? And if so, how do we handle customer expectations in those cases?

- Confirm if there are exceptions to the stated timelines (e.g., seasonal delays, specific retailers with slower processes).  
- Ask if there’s a documented escalation process for disputes that exceed the expected timeline.  
- Verify if the two-to-four-week range is communicated uniformly across all retailers or if it’s adjusted based on historical performance.  
- Check if there’s a dashboard or report tracking dispute resolution times by retailer for monitoring compliance.  
- Follow-up on whether Andrea’s team has any specific SLAs with retailers for dispute handling.

### [Ask AI] Work Items Tickets Process - Retail Tenant Support - Confluence 

What is exactly “Work” Item not functioning properly”?   

Como puedo mejorar mi pregunta o ahondar mas en ella antes de hacerla? para esta seccion?
To refine the question before asking it, I'd focus on clarifying the scope and specifics of "Work Item not functioning properly." For example, I'd ask: "Can you walk me through the typical scenarios or symptoms that classify a ticket as 'Work Item not functioning properly'? Are there specific triggers or patterns we should watch for in Retail Tenant Support, and how are these documented in Confluence?" This way, the question is more targeted and invites a detailed explanation of both the operational process and the documentation.

- **Key refinement**: Focus on symptoms, triggers, and patterns. Avoid vague phrasing like "not functioning properly" without context.  
- **Follow-up angle**: Ask about examples of common "Work Item" issues — e.g., tenant-specific configurations, data discrepancies, or integration failures.  
- **Documentation link**: Confirm if Confluence has a dedicated section for troubleshooting "Work Item" tickets or if this is part of a broader Retail Tenant Support guide.  
- **Potential gaps**: If no clear documentation exists, suggest creating a troubleshooting checklist or flowchart for "Work Item" issues.  
- **Edge case**: Ask if there are exceptions or unique cases for certain retailers (e.g., Home Depot vs. TJX).  

This approach ensures the question is actionable and opens the door for deeper insights into both process and documentation.

### [Ask AI] alguna pregunta que hacer sobre lo ultimo que esta diciendo?
Could you clarify the process for maintaining and updating the client contact list? Specifically, who is responsible for ensuring the information stays accurate and up-to-date, and are there any plans to automate this manual maintenance in the future?

- The client contact list seems critical for outage communication and product tracking.  
- Follow-up questions to consider:  
  - Are there specific fields in the list that are prone to errors or outdated information?  
  - Is there a workflow for verifying the accuracy of the data periodically?  
  - If automation is being considered, what tools or systems are being evaluated for this?  
- Mentioned tabs: Secure EBR, US/Canada/Australia, EU, on-prem, and catastrophic event lists — ensure clarity on how these are segmented and used.  
- If automation isn't feasible, ask about best practices for manual updates.

### [Ask AI] alguna pregunta que hacer sobre lo ultimo que esta diciendo?
Could you clarify the process for updating the client contacts list? Specifically, who is responsible for maintaining it manually right now, and what steps should we follow if we need to make changes or add new entries? Also, is there a timeline or plan for automating this list, or should we assume it will remain manual for the foreseeable future?

- **Responsabilidad actual**: Preguntar quién es el dueño actual de la lista (nombre específico o equipo).  
- **Proceso de cambios**: Confirmar si hay un protocolo para modificaciones (aprobaciones, formatos, etc.).  
- **Automatización**: Si mencionan que hay un plan para automatizar, preguntar qué herramientas o sistemas están evaluando.  
- **Protección de la hoja**: Preguntar cómo se manejará el acceso una vez que se transfiera la protección a Juan y Camila.  
- **Edge case**: ¿Qué pasa si hay un error crítico en la lista durante un evento como un outage? ¿Quién lo corrige?

### [Ask AI] Work Items Tickets Process - Retail Tenant Support - Confluence 

What is exactly “Work” Item not functioning properly”?   

Como puedo mejorar mi pregunta o ahondar mas en ella antes de hacerla? para esta seccion?
To clarify the question further before asking, I'd focus on specifying the scope and expected outcome. For example, instead of just asking "What is a 'Work Item not functioning properly'?", I could frame it like this: "Can you walk me through the typical scenarios where a 'Work Item not functioning properly' ticket is raised? Specifically, what kinds of issues are most common, and how do they impact the Retail Tenant Support workflow? Also, are there any patterns or triggers we should watch for when identifying these tickets?"

- **Scope refinement**: "Work Item not functioning properly" could mean different things depending on the context. Narrowing it down to Retail Tenant Support ensures the answer is relevant.  
- **Expected outcome**: Asking about common scenarios and patterns helps uncover actionable insights, like troubleshooting steps or preventive measures.  
- **Follow-up questions**:  
  - Are there specific tenants or products where this issue is more frequent?  
  - How do these tickets typically transition between RCS and RTS?  
  - Are there any automation tools or dashboards that help monitor Work Item functionality?

### [Ask AI] respondio mi pregunta, que mas puedo preguntar o solicitar en base a lo ultimo que me esta diciendo?
Thanks for walking us through that. I’ve got a couple of follow-ups to make sure I fully understand the process and the tools involved. First, for the manual updates to the main sheet, could you clarify how often those updates typically happen and if there’s a specific cadence or trigger for them? Also, when you mentioned the green customers in implementation, is there a standard handoff process or checklist for when they transition to support? Finally, regarding the data load issues you mentioned, are there any recurring patterns or specific retailers where this happens more frequently?

- **Manual updates cadence**: Ask if there’s a weekly/monthly rhythm or if updates are purely reactive based on requests.  
- **Implementation handoff**: Look for any documented process or checklist for transitioning green customers to support. If none exists, suggest creating one.  
- **Data load issues patterns**: Probe for specific retailers, regions, or products where data issues are more common. This could help identify systemic problems.  
- **Automation plans**: If Salesforce → Jira automation is on hold, ask if there’s a timeline or priority for revisiting it.  
- **Work items impact**: Confirm if missing work items are escalated as Critical priority due to their direct impact on retailer operations.

### [Ask AI] quedo todo claro en base a lo ultimo de la transcripcion?
Based on the recent transcript, I understand the key points about the manual process for maintaining the contact list, the challenges with automating it via Salesforce and Jira, and the importance of work items for loss prevention teams. It’s clear that data issues, especially around data loads and missing data, are a major category of tickets. I also noted the handoff process from implementation to support, including the email details required when a customer transitions.  

I’d like to confirm one thing: for the manual contact list updates, is there a specific cadence or protocol for reviewing and validating the list, or is it purely reactive based on incoming requests?

- Manual contact list: Kristen and Aimee handle updates; green indicates customers in implementation.  
- Automation idea: Salesforce → Jira integration discussed but deprioritized.  
- Work items: Critical for loss prevention teams; delays in data loading impact customer operations.  
- Common issues: Missing data, incomplete data loads, and related investigations.  
- Implementation handoff: Email includes customer/product details, delivery engineer, and open items.  

Follow-up questions:  
1. Is there a documented process for handling missing data tickets, or is it case-by-case?  
2. For the Salesforce → Jira automation, is there a timeline or owner for revisiting this initiative?  
3. Are there specific metrics tracked for work item-related tickets, like resolution time or frequency?

### [Ask AI] algo que pueda agregar como agradeicmiento y cierrte de esta reunion?
Thank you all for the detailed walkthrough today. It’s clear that work item tickets and data load issues are critical areas for us to focus on, especially given their direct impact on customers’ day-to-day operations. I appreciate the clarity on how these processes tie into Secure and the broader support workflow.  

As we move forward, I’ll make sure to prioritize understanding the nuances of these issues and the tools involved, like Greenplum and Azure migrations. If there’s anything specific you’d recommend I dive deeper into before our next session, please let me know. Thanks again for your time and insights.

- Puedes mencionar que te interesa entender más sobre el proceso de transición de clientes a Azure, ya que parece ser un tema en progreso.  
- Si hay algo que quedó sin respuesta, podrías preguntar: "Is there a specific resource or document you'd recommend for understanding the Secure data load workflow in more detail?"  
- Agradecer explícitamente a Aimee por liderar la sesión puede ser un buen toque personal.  
- Si mencionaron algún follow-up pendiente, asegúrate de confirmarlo antes de cerrar.


---

## Reunión 2026-06-03 — Consumer Support processes · Transcripción 1/10
_chunk 852 · 2026-06-03_

## Transcripción completa
Hi, Wala, and how are you? How are you? Doing well. That's a tattoo on your neck. It's an eagle. Oh, that's incredible. That looks like That looks like a painful area trying to decide. I'm just trying to decide. Yeah, I don't think I can do a tattoo. A tattoo there. I have them all, a lot of... Yeah, I can understand that for sure. I mean, I have them in many In many places, you know, on my arms and legs and yeah. This one was probably the most painful, just simply because they I think he was digging for gold. For gold. He was literally burying the needle. I'm not going to get a needle in my wrist. But yeah, I don't know, neck and fingers. I saw somebody the other day that has one in here. And I'm just going to start here on their ear. Can't even, yeah, no. No, I don't think I could do that one. How are things going? Okay, so chaotic is what I'm hearing. Yeah, they're keeping you hopping. In all honesty, I'm not sure where to We'll start with, do you have questions first? Okay, and are you talking about Talking about Jira or, okay, all right. All right, perfect. Okay. Let me ask you this. Let me share my screen. Let's find the right one to share. There you go. So when you open like a Open like a Google page. Do you have this company links option here? All right, so help desk, help desk is... And a help desk ticket is where you're gonna wanna create any. Any tickets for access that you need. Any issues you're having with your hardware, you know, things like Things like that. So that's where I would say I would start for that. And then what will happen is that'll And then they'll take it from there and probably ask Ask JR questions and things like that. You're getting the right access that you need for those items. Yeah, yeah, so you've got your common requirements. Common requests. Yeah, so once you click on that help guest It's a great way to get your best ticket. It'll take you to this screen and you can, you know, hardware software.

## Reunión 2026-06-03 — Consumer Support processes · Transcripción 2/10
_chunk 853 · 2026-06-03_

Hardware software requests, access requests, you just select one of these. We're going to pretend I'm I'm going to pretend I'm going to ask for some access. So we're going to do access change. Change, and then just put in a summary. Summary, need access to Jira. Scroll down, priority is, you know, high, medium, High, medium, low, critical, obviously, for things that have to happen right now. But you can enter a date if you want. If you need it completed by a specific date. And then in here for description, just put in a brief description of This one right here, Business Justified. This justification is the most important part. The Infosec or Infosecurity team will Will always want that. That's a great way to do that. Requesting access to applications or some of the other programs that we use. Trying to think how to, how we would word like Word like this one. September of new apps. I'll see if I spell it right. Let me get it to access. Pass to Gerat Mortar to... If they need more than that, they'll come back to you. Okay, but once you hit send here, And they'll take it from there. They may ask more qualifying questions or whatever. Whatever, but yeah, that's the best way to gain access to anything that you need. So here's one. This is one that is It's currently maintained by me. And I believe I have it in SharePoint. Available for you guys. But basically, yeah, I broke it down, color-coded it, I've also coded it by CSM. And then alphabetized their customers. As you can see, Colleen has the majority of the customer. I believe she has over 100 customers. This is in SharePoint, and I'll get out of the way. Move this out of the way. Where is Where is my SharePoint? Bye. I don't know. Add it open. Oh, that's so funny to hear. So SharePoint, under support. We have all of our documents That's a documentation in here for us that we use regularly. So, that's the way to do it, that's the way to do it. I just gotta remember. We look at that again.

## Reunión 2026-06-03 — Consumer Support processes · Transcripción 3/10
_chunk 854 · 2026-06-03_

Oh, this one's actually, oh, that's good. Oh, that's right. This one's actually in marketing. Because marketing, marketing Marketing first created it, and every once in a while they would They will do an export. Out of Salesforce because that's where most of Most of the real true. Assignments and documentation is, okay, for especially regarding CSA. All of these are available on the website, I'll do an export, and so that's why it's under marketing. And go back and we'll find the marketing, actually. Actually, here, let me just do this. Be easy. Share. I'm going to plug that. In this chat, this is This is CSAM assignments. All right, so now you have a link to it. And you guys should be able to access it that way. Hold on one quick second. Quick second before you ask this question, it just occurred to me we should be recording this mess. This, oh, it is. Okay, good. Just making sure. All right, go ahead. Okay, that will also, I believe So I believe we have documentation for that in confluence. Let me find the right set. It's a great section. It would be under... Well, and of course, you know, it's not going to be easy. And it'd be easy to find. I know I have it. Oh, it is under RTS. RTS. Okay, so under Retail Tenant Support, In confluence, we have our consumer Support knowledge base, okay? I believe I'll double check this document, but But, let me look. She doesn't have it defined in there, so I will have Andrea at the end. Andrea, add a definition to it. I just typed that out to her really quick. Give me a little more. A definition needs this. Well, I've been here three years. And it is a living, breathing thing. All of these documents, they're always I think we've got a lot of things being added and created and added and updated. updated and all of that. So some of my technicians, a couple of A couple of them have been here like 15 years and they've been, yeah. And yeah, so yeah, a long time. So, okay, so I've asked Andrea.

## Reunión 2026-06-03 — Consumer Support processes · Transcripción 4/10
_chunk 855 · 2026-06-03_

I'm very hungry to add a definition to that page. Do you want me to tell you the definition? Do you want me to explain what it is? I mean, short version. So, a customer goes into one of our clients. Clients say they're going into TJ Maxx, okay? They want to return something. They create a return online claim. And they go through our So, our return authorization process on the back end of the And it comes back with a denial. So that person is then directed to call our call center. And that's when they're offered their return authorization I'm not sure what the name of the name is. We have a lot of people who are not familiar with the concept of a And then, that is what is up. That email comes to us as a dispute. And goes through our dispute process. Okay, RAR is Return Activity. And then we have the activity report. We have a lot of consumers that shows all of their of their history with that particular retailer. It shows their purchases, their returns. And kind of gives them for a two year Okay, you've made this many purchases, you've made this many returns. It just helps them to understand maybe why they were denied being able to return And we're able to return that particular time. No problem. No problem. Yeah, it's only pulled up when they call into the All in to the call center and they do say, when we offer and say, would you like that, R-A-R, And the consumer says yes, that's when it is pulled up. Okay. It is a two year. Two year back history. It only goes two years. And it is only for that particular retailer. Tjmaxx, HomeGoods, Marshals, they have several different If a person is trying to return and gets denied at one of those stores, Those stores, their RAR will have the history of all of those stores. Depends on the retailer. As a general rule, it has been two to four weeks. We did get behind earlier in the year, but I believe we're all caught up now.

## Reunión 2026-06-03 — Consumer Support processes · Transcripción 5/10
_chunk 856 · 2026-06-03_

So when we're on the phone with the consumer, we do tell them You tell them, you know, this decision will take two to four weeks to get back to you. And again, each retailer is different. We as a general rule at Appress, Andrea and team get the disputes. The dispute sent over within a day or so of receiving them to the Each retailer differs on how quickly they review the data. Review those and get back to us. I believe like Home Depot is all It's almost immediate. They're same day, usually. I want to say I can't remember others. Others take all the way up. All the way up to like two weeks. It just depends on the retailer. I think Andrea might have a list that states What states which retailer and what their turnaround Turnaround Timus for disputes. Not that I'm aware of. Excuse me. Let me just ask Andriy if she has that. She has that list because it does feel like there might be one, and I can't think of who it is off the top That's off the top of my head. That used to be a problem that way. I am not turning around, so I am not. We'll go back to the last one. All pretty much that two to four week, generally not longer than two weeks. Okay, yep, through the CRM. So the The consumer, there's a CRM. That's how they're managed. That's how they're managed, that's how they're tracked, and everything is done through that CRM. Okay, so yeah, so if we look at We look at the spring here. So we've got customer support knowledge base. That is the title of this section. Yeah, okay. So this is everything. Everything relating to customer support. You click on it, it's a dropdown basically, and it opens it I'm not sure why there's nothing. That section provides pages for support, ticket management processes, you know, and that's... That's defining what is underneath this page. And then, we have the AWS page. Then the next one, you've got consumer support. Again, everything under that Okay, no worries, no worries. No worries, it's a lot to take in. Ah, that is the Kanban voice.

## Reunión 2026-06-03 — Consumer Support processes · Transcripción 6/10
_chunk 857 · 2026-06-03_

I'm on board and I probably just need to grant you guys access. So that is this. Great, so let's take a look. Yeah, probably just not. I probably just need to give you guys this link. So now we put it here. Try clicking on that and see if it opens for you. That's all that happens for you. You should have access. You should have access now. Yeah. Once the link is shared to you, you should have access. You should have access and you shouldn't have any issues. Yeah, so it was a permissions thing. That's a good question. I'm not sure if you're going to answer that question. Most everything that is in here, unless it's under archive, you're going to find useful, okay, at some At some point in time. Some things to note, like the US Support Calendar, you guys aren't going to need to know that afterward. We're done, but right now this is showing everybody in We'll be talking about the future of the world. So, on what days, you know, the office is closed. The office is closed. And so, you know, I would Now I would say yes, go back through, why are you not taking me back? Thank you. The Claude Skills, this is a list. A list. Looks like we only have a couple in there right now. That should be updated. I mean, make it down here. I'll get somebody to update that with... All of the skills that we're using in quad. Oh, shoot. You didn't find any of that. I'm gonna be cheating now. So yeah, I would say, I would recommend that you review One of the most important ones, and I will And I will share this with you right now, is this client contacts. This is how we How we currently maintain all of our client contacts that And we need to contact the customers. This is the list we come to tonight. And so, I think that's a really good question. So this is definitely one you'll want to get familiar with. Currently it is manually maintained. My hope, I have been trying to get this I'm going to hope for you guys that you can do that. Somehow, someway.

## Reunión 2026-06-03 — Consumer Support processes · Transcripción 7/10
_chunk 858 · 2026-06-03_

But, so, let's say Let's say we have an outage. You'll notice these red tabs over here. A secure outage, a secure five outage. I come to this tab here for secure EBR. And if it affects all of the secure customers, that's going to be That's going to be this list here. If it is only the US and US, Canada customers, and Australia. US, Canada, Australia customers. They're all on the same servers. I would come to this list and select these email addresses. If it is EU only, we've got... We've got more lists. And then we have on-prem as well. OK. For engage and incident, It's my understanding you guys won't deal with APHIS and Or if we suddenly have some catastrophic event that we need We need to inform every single one of our customers that would be this list here. And then, I'm going to go back to the list here. But the main page, this main sheet here, is the one And that we all utilize, okay? We all utilize We'll utilize it to know what products a customer has. If they're US or EU or Australia, Who the CSM is in Titan. I'm gonna... I'm going to change that instead of internal contact. I'm just going to change this to CSM. Don't be easier. We do have this first page protected. And I'll turn that protection over to you guys eventually. But we were having a problem. Having a problem with having so many people having access to get in here and make changes. It was getting chaotic and And we had a lot of people who were like, oh, I'm going to do this. So that Kristen and I are the only ones who can actually make changes to this main sheet. So if L1 gets a request or CSM gets a request to add or remove people from their contact list, they just inform us and then Kristen and I go in and make that change. But yeah, this list is definitely one you'll want to take a look at. All of the customers listed. The green ones are customers that are in implementation, so they haven't been yet turned over to support To support for that product. Yeah, right now it is all manual.

## Reunión 2026-06-03 — Consumer Support processes · Transcripción 8/10
_chunk 859 · 2026-06-03_

We were talking about, and this is part of the thing that Libby and What Libby and I and Kara and I were starting to discuss was How do we get that information out of Salesforce and into Jira? So that we don't have to manually maintain this list anymore. But that has been It has been pushed to the back burner for months now. And so hopefully they'll be able to, you know, hopefully JAR will be able to pick We're going to be able to pick it up again with Kara and Libby and get it to be an automated And then we can do a different automated thing in Jira rather than this spreadsheet. Work items is a big one. That is something within the application. And then, there are also applications that it's a list of Of investigations, basically, that That the loss prevention people And if you're interested in people at the retailers, they need the list. That list populates out of secure and it Populates based on the data that we are sent from the retailer. So, if we for some reason are We've had a delay in the last couple weeks with getting customers Then customers data loaded into their applications. And then, in the end, the customer The customer getting their list of work items, which means their loss prevention people have nothing to do. Okay, so that's a big one. Currently, any work item tickets that come into us regarding work items missing So, if you're using or work items not working, We're going to be talking about the new features of the new feature, Because it affects the customer being able to do their day-to-day work. I would say, I was gonna say, we really don't have I have like a top 10 category of, you know, What the most common issues are. But... But having said that, data is Data issues and data load issues are are big, okay. So getting tickets from customers. We're saying things like, we didn't get our data for this date, or we didn't get all of the data for this date in Secure.

## Reunión 2026-06-03 — Consumer Support processes · Transcripción 9/10
_chunk 860 · 2026-06-03_

So then we have to go in, double check the data that they sent us, see if we uploaded everything that we received, and then get back to them and either Either reload that data or let them know that they need to resend the data because we didn't get it all. And we look at the key, the key to the key. Let's see if we can look at the queue right now. Trying to see. Yeah. Sure. Of course. Yeah. We haven't done anything. I love it down pretty well right now. So it's not very often that a customer maybe once a week This is a unique feature of the customer. So and so from your contact list, can you add them? It's not very often at all. Yes, yes, there is. And in fact, that's in influence as well. So short version, the summary of this article is the implementation We're going to go through the implementation project manager once they've finished everything on On their end, they send us an email letting us know, hey, Hey, like I think the most recent, one of the most recent was Walmart. Walmart is ready to come to you guys. Under standard support. We've completed We've completed their implementation. They send us an email that should contain all The customer, the product, is it a new implementation Is it a transition from an old product to a new product? Name of the delivery engineer, which did the data mapping for Any open items on occasion they will They will still have a few open tickets or open items from the implementation. I'm sorry, I'm not going to do that. We'll be able to do that in a couple of days, but we're not going to be able to do that in a couple of days. Update that before we transition out and then we forward that information over to the team. To the team. Okay. Yeah. Yeah. Yeah, absolutely. And that's when we would go into that client contact sheet as well, change Change it out of the green and make sure there are contact names listed under the client contact. Most are being moved to Azure right now. Yes. Yeah, not everything is on Azure at the moment.

## Reunión 2026-06-03 — Consumer Support processes · Transcripción 10/10
_chunk 861 · 2026-06-03_

We have some, but there, I would say, I honestly don't know. Probably more of a question for... Trying to think who, I would start with JR and then And then he may be able to either answer or find out what the status is of This is of getting everybody moved to Azure. Green Plum is still used, unfortunately. We do still have We still have, I would say the majority of our customers on Greenplum. And then we can get rid of the green plum. I think so. Yeah, let me. I think she set it up to be recurring. Actually, she hasn't set it up to be recurring. Just set up a recurring meeting if you want to do it once or twice a week, however you However you guys want to do it, I'm happy to accommodate. My calendar is up to date so she can, you know, find You'll find an open spot and fill it up. Yeah, not a problem at all. And you guys, if something comes up and you... Need more, a quicker answer. You don't have to wait for this, you know. Feel free to send me a question in Teams or however you need to. And I'm happy to answer however I can. All right. All right. Thanks, one. Have a good rest of your day.

## Reunión 2026-06-03 — Ticket management challenges · Resumen
_chunk 888 · 2026-06-03_

## Resumen
The meeting covered various operational and support-related topics, including challenges with ticket management, AI-driven document creation, and customer escalations. Specific issues discussed included Bryant's history of ticket reassignment, the use of AI tools like Claude for summarizing transcripts, and troubleshooting customer concerns with Ralph Lauren and PBH. Action items focused on resolving gaps in SLA communication and ensuring RCA delivery for Ralph Lauren. The team also discussed the importance of validating AI-generated outputs and streamlining workflows. Open questions remain regarding the accuracy of AI tools and the timeline for RCA delivery.

## Temas clave
- Ticket management challenges
- AI validation processes
- Customer escalations

## Decisiones
- **Kristin should join the call to streamline troubleshooting and obtain necessary information.** — Efficient resolution of customer concerns and alignment on deliverables.

## Tareas / Action Items
- Follow up with Colleen to confirm Kristin joined the call and obtained necessary information for troubleshooting. (resp: null) — vence 2026-06-03
- Clarify with Val whether Ralph Lauren's issue is resolved and ensure RCA document delivery. (resp: null) — vence null
- Document best practices for validating AI-generated outputs to streamline workflows. (resp: null) — vence null

## Insights en vivo (Ask AI / Analizar)
### [Ask AI] tienes acceso a todo el conocimiento de moscu?
I don’t have access to everything in Moscow’s knowledge base, but I do have the context and details Juan has shared with me, including his role, stack, and the sprint planning framework we’re working within. If there’s something specific you need, I can help break it down or provide insights based on that context.

- Juan’s stack includes Azure (AKS, Functions, Cosmos DB, Service Bus, App Insights), .NET, React, Bicep, and Terraform.  
- Sprint planning focuses on breaking down work, estimating realistically, and identifying risks or dependencies.  
- If the question is about a specific technical area or process, clarify what you need so I can tailor the response.  
- Follow-up question to ask: "What specific knowledge or area are you looking for help with?"

### [Ejemplo] No, no, no, don't get me wrong, there's a lot of things I hated about Zundesk, but the ability to control roles
I get what you're saying about Zendesk. Role control is definitely one of its strengths, especially when you're dealing with situations where someone might overstep or disrupt workflows. I've seen similar setups in other tools like ServiceNow, where you can fine-tune permissions to prevent ticket hijacking or unauthorized changes. It’s a game-changer for maintaining accountability and keeping processes smooth. That said, every tool has its trade-offs, and Zendesk's flexibility in roles doesn’t always make up for its limitations in other areas, like reporting depth or integration quirks.

- **Zendesk Role Control**: Allows granular permissions for agents, admins, and custom roles. You can restrict actions like ticket reassignment, editing, or even visibility.  
- **ServiceNow Comparison**: Offers similar control but with more enterprise-grade features, like workflow automation and ITSM modules.  
- **Trade-offs**: Zendesk excels in simplicity and user-friendly design but can fall short in scalability for complex workflows or deep analytics.  
- **Follow-up Question**: "What specific challenges did you face with Zendesk beyond role control? Were they related to scalability, integrations, or something else?"  
- **Edge Case**: If the team is considering switching tools, evaluate how role control aligns with broader needs like reporting, automation, and cross-platform integrations.

### [Analizar] A lot of times I've let AI create something and looked at it and been like, hang on a second, because 80% of it, 90% of it is
The key point here is that while AI tools like Claude can be incredibly efficient for tasks like summarizing transcripts or generating documents, it's critical to validate the output. Even if 80–90% of the content looks correct, that remaining 10–20% can introduce errors or misinterpretations that could impact the final deliverable. So, using AI as a starting point is great, but always double-check and refine the results manually to ensure accuracy and alignment with the intended context.

**Resumen:**  
- Discussion about using AI tools like Claude for summarizing transcripts and generating documents.  
- Concerns raised about the accuracy of AI-generated content, emphasizing the need for manual validation.  
- Mention of Vedant and Tyrone collaborating on AI-driven workflows.  
- General commentary on past experiences with AI tools producing mostly correct but occasionally flawed outputs.  

**Decisiones detectadas:**  
- No explicit decisions were made, but there’s a clear recommendation to validate AI-generated content thoroughly.  

**Tareas / action items:**  
- If Tyrone is actively using Claude for document creation, ensure he has a process for manual review before finalizing outputs.  
- Consider documenting best practices for AI validation within the team to streamline workflows and avoid errors.  

**Cruces con tu segundo cerebro:**  
- Relates to **Sprint Planning** context: If AI tools are being integrated into workflows, this could impact task estimations and dependencies. AI might speed up certain subtasks but introduce risks that need mitigation.  
- No direct mention of nuaav-specific tools like Azure or Cosmos DB, but the general principle of validating automated outputs aligns with engineering best practices.  

**Aclaraciones:**  
- What specific tasks or documents is Claude being used for? Are these internal deliverables or customer-facing?  
- Are there any metrics or benchmarks being used to evaluate the accuracy of AI-generated content?  
- Does the team have a formalized process for AI validation, or is it ad hoc?

### [Ask AI] habla sobre los temas que quedaron pendientes de la reunion anterior con Aimee
From the last meeting with Aimee, we still have a few key topics to address. First, we need to finalize the initial document that captures the team's assigned topics. It seems like we've covered a lot of ground already, but there are still some areas that need refinement or confirmation. Second, there are follow-ups related to syncing with Juan and ensuring alignment on the deliverables for Friday. Lastly, we should revisit any open questions or unresolved points from the previous discussion to make sure nothing gets overlooked before moving forward.

- **Document refinement**: Ensure the first document accurately reflects all assigned topics and any updates from the team.  
- **Sync with Juan**: Confirm the agenda for Friday's meeting and prioritize deliverables.  
- **Open questions**: Review notes from the last meeting to identify any gaps or pending clarifications.  
- **Potential risks**: If the document isn't finalized by Friday, it could delay subsequent tasks.

### [Analizar] Maybe you guys Maybe you guys can just try and kill two birds with one stone and she can get what she needs to try and troubleshoot a little bit.
The suggestion to have Kristin join the call makes sense as a way to streamline the troubleshooting process and ensure she gets the information she needs directly. It could also help clarify any miscommunications or delays with the customer. If Kristin can align with Colleen during the call, it might save time and reduce back-and-forth later.

**Resumen:**  
- Discussion about Kristin's role in keeping the platform unification on track and her challenges with customer dependencies.  
- Mention of Colleen attempting to connect with customers to resolve issues and the suggestion to involve Kristin for efficiency.  
- Frustration with delays caused by customers not providing necessary information.  
- Reference to past issues with PVH and the need for caution in similar scenarios.  

**Decisiones detectadas:**  
- Suggestion to have Kristin join Colleen's call with the customer to address multiple issues simultaneously.  

**Tareas / action items:**  
- Confirm Kristin's availability for the call with Colleen.  
- Ensure the agenda for the call includes both troubleshooting and gathering missing information.  
- Follow up on PVH-related issues to avoid repeating mistakes in platform unification.  

**Cruces con tu segundo cerebro:**  
- No direct references to specific items in your KB, but this aligns with general practices for managing dependencies and customer communication in platform unification projects.  

**Aclaraciones:**  
- What specific information is Kristin missing from the customer?  
- Are there any technical blockers tied to the platform unification that need escalation?  
- Is there a clear timeline for resolving the customer-side delays?

### [Ask AI] que estan dicienco sobre esos tickets?
From what I’m hearing, there are two tickets flagged for Ralph Lauren: 27079 and 199484. It sounds like 27079 was created off of 199484, and Dean has been working on them. The main issue seems to be that Ralph Lauren is waiting for the RCA of a resolved issue, and their contact is frustrated with the delay. Val flagged this because the Ralph Lauren team is pushing for answers, and there’s been some back-and-forth in emails about the timeline. If I’m understanding correctly, the technical issue itself is resolved, but the RCA documentation is what’s holding things up.

- Ticket IDs: **27079** and **199484**.  
- Ralph Lauren’s concern: They want the RCA (Root Cause Analysis) for a resolved issue.  
- Dean is the point person working on these tickets.  
- Val flagged the situation due to escalating frustration from Ralph Lauren’s contact.  
- Potential misunderstanding: Val might have thought the issue itself wasn’t resolved, but it’s the RCA that’s pending.  
- Follow-up questions to clarify:  
  - What’s the ETA for delivering the RCA?  
  - Are there blockers or dependencies delaying the RCA?  
  - Is Dean coordinating directly with Ralph Lauren’s team, or does Val need to step in further?  
  - Could we streamline RCA delivery for similar cases in the future?

### [Ask AI] que es lo ultimo que estan diciendo?
They're discussing the transition of new team members into the support queue and the importance of balancing training with maintaining service quality. The focus is on ensuring critical tickets are handled effectively while onboarding and upskilling new staff. They're also emphasizing the need for clear documentation and training plans to support this transition smoothly.

- The queue is described as "on fire," indicating high demand or backlog.  
- There's a priority on critical tickets to avoid service misses.  
- New team members are being onboarded with responsibilities like writing documentation, training, and actively working on the queue.  
- The goal is to have the new staff fully skilled by the end of the transition period.  
- Follow-up questions to clarify:  
  - What's the timeline for completing the transition?  
  - Are there specific metrics or KPIs to measure the success of onboarding?  
  - Any risks identified in balancing training with queue management?

### [Ask AI] algo de valor o que se pueda agregar teniendo en cuenta que yo aun estoy en KT y no tengo trabajo estoy en onboarding?
It sounds like the team is in a transitional phase, with new members onboarding and knowledge transfer happening. Since I'm still in my onboarding process and not yet fully active in the queue, I’d like to ask: is there any specific area or type of documentation that’s a priority for me to focus on during this KT period? Or, are there any recurring patterns in the queue that I could start analyzing to better understand the workflows and challenges? I want to make sure I’m preparing in a way that aligns with the team’s immediate needs.

- You could offer to shadow someone actively working on the queue to observe how they handle tickets, especially critical ones.  
- Ask if there are any specific tools or systems you should prioritize learning during onboarding.  
- If the queue is noisy, inquire about the types of tickets that are most common or problematic — this could help you identify areas to focus on during KT.  
- Suggest reviewing past tickets or documentation to understand trends or pain points.  
- If training materials are being created, offer to review or contribute to them as part of your onboarding.


---

## Reunión 2026-06-03 — Ticket management challenges · Transcripción 1/9
_chunk 889 · 2026-06-03_

## Transcripción completa
To be accepted just a few minutes ago, so she should be joining. If not, I'll give her shit. Please do. I know Kara declined. I'm not giving her shit. I'm giving her shit. Oh, come on. Getting her in a meeting is tough. I'm like, all right, just five minutes. I just need five minutes. I just need five minutes. And she's like, 6.30 at night, my time. My time, which is like 7.30 your time. So, yeah. Yeah. She's busy. She is busy. Yes, she is. She's on the phone with Bryant. That could be a minute. Wait a minute. I wasn't going to say anything because I don't know. I don't know the lay of the land yet, but I had a very But I had a very similar thought. I've had a few conversations with Brian, or had Brian talk at me for a few days. Nice guy. Smart guy. Smart guy. Very smart. He can be a nice guy. Be a nice guy. He can also not be a nice guy. But we did finally, it took about... Oh, let's see, I've been here three, just over Just over three years. It took about two and a half of those years to get him To get him to stop taking tickets away from From engineers. Yeah, that's tough. But it has finally come. Calm down and just ask questions now instead of just Just, you know, because Kerry, he would do it to Kerry all She'd be in the middle, she will all be in the middle. She's got some message to the customer in the ticket and she's like, And she's like, what is he doing? Yeah, that's why I like Zendesk. I had a lot more control than Zendesk where I'm just I'm just like, we're going to change your role. We're going to change your permissions. No, no, no, no. No, no, no, don't get me wrong, there's a lot of things I hated about Zundesk, but the ability to control roles that at least was nice. Yeah yeah. Oh I like Bryant. He's just. I'm just kidding, the two of them together. Yeah, they would for sure. Well, I was just on a one-on-one with Tyrone and he was showing me that he is using Claude to... He met with Vedant earlier.

## Reunión 2026-06-03 — Ticket management challenges · Transcripción 2/9
_chunk 890 · 2026-06-03_

Is that how you say his name? Okay. The transcript and the questions that Vedant asked, he's having Claude pull those out so that he can, and then he'll have Claude Have Claude create the document. And yeah, it's pretty cool. I don't want to be the AI curmudgeon, but just double check it all. Oh, yes. A lot of times I've let AI create something and looked at it and been like, hang on a second, because 80% of it, 90% of it is Yup. And then you go, wait, where did you come up with that? How did you get that? On my home version of both Gemini and Claude, my My instructions file are ClaudeMD for Claude are like three or four pages long. It's just, you know, thing after thing where I'm like, don't ever do this. Yes, thanks, Tom. Yes, yeah. We're going to start the meeting. Wanna and I had a pretty good meeting a little earlier. Of course, the time flew by. You know, we felt like we just got started. We're at the end of time already. But, yeah, it was pretty good. Yeah, I'm sorry that I couldn't join. I have something origin to catch up on. But I'm planning to have another sync with you and Juan on the On Friday, so maybe I can, like we can finish that first document. I think it also captures a lot of the teams, the top The topics that we have assigned. So I think that it was great. That is definitely That is the first one because I know that a lot of the topics will be okay. We already covered this. Discover this, cover this, and cover this, yeah. Yeah, nice. Yep, sounds good. Sorry, I'll be right back. So Camilla, how are you feeling? Are you overwhelmed yet? Yeah, of course. It is a lot because the teams that The teams that I used to work on, they are teams that are already settled and they are not They are not in transition, so for me has been challenging to keep them like their sentiment up. I hope you guys will be able to come up and say, hey, I know it's hard, it's painful, it's not the best context for transition, it will be better for all of us.

## Reunión 2026-06-03 — Ticket management challenges · Transcripción 3/9
_chunk 891 · 2026-06-03_

So, for me, has been a little bit of I think it's a little bit overwhelming because my biggest concern is that my people are The developers were born out and overwhelmed, so they just decided like, hey, you know what, I don't like this. Like this, and I don't want to do it. So I think it's a challenging start. I'm really excited. This is a new challenge for me and I'm learning a lot. I'm trying to keep it up and also And also like to, because that is, no, it's okay. I really like those cameos of PEL. And he, when my husband leaves for work in the afternoon. He comes in and he puts his little paws up on me like, mom, I'm bored, I'm lonely. I'm lonely and he brings me his ball. He always wants to play fetch. So he's a dog cat. My grandparents are dogs. He is a dog cat. I'm telling you, he eats Eats, what my dog eats most of the time. He is the strangest cat I've ever met. He's a ginger cat. He's the youngest. I have three cats and a dog. He's just barely a year old. He's always the one who has to get on camera. I was wondering, all I saw was orange cat coming in. I was like, somebody's cat's coming in. I've only had black cats growing up, which have Which have their own different personality, but the orange ones, I think they all share a brain cell and And some cats get it one day and some don't. So. Yeah, I have a blast. I have a black one as well. Her name is Salem. She's the oldest and yeah, you're right. She definitely has her own personality. Yeah, because he's part, it's a Siamese. Oh, because I've seen like I mean, like a sealed tip that's got the gray tip tail and... Yeah. Yeah. He's not really chatty, but we were just talking. He's more of a dog cat, hey? He plays batch for hours. He eats, he's all about. He'll sit there right next to the dog waiting for the food to drop on the floor. That's how big Black Cat was. Except for my Black Cat really liked goldfish. Old Fish, easy, Fruit Loops too. There's that. Animals. You gotta love them.

## Reunión 2026-06-03 — Ticket management challenges · Transcripción 4/9
_chunk 892 · 2026-06-03_

And they all got their own personality, but sorry. Brighton had a bunch of updates and I was trying to accelerate. I think it's not right. Yeah, no worries, no worries. I figured it might be a minute once I set up. It was Bryant, so. He's great. Sometimes there's just, there's just a lot. There's just a lot going on. He's got busy. He has. Yes. He does. Our friends at Gap and Lulu. And Lulu, they like to keep him busy. Yeah. Yeah. Yes. Not just him. I was like, yeah, everybody, no, I feel ya. I feel ya. How are things? We're good. I saw the comment from I had a comment from Kristin yesterday. So, Carly is really kind of owning, like, kind of key I'm kind of keeping everything on track from the product side for some of that platform unification. So she was connecting with the CSMs. We were like, what's taking so long? We're kind of at the mercy of the customer doing these things, but also like you guys asking us about Python That's about five-frame unification results in the middle of like 45 other things we were asking customers to do. So like Victoria's Secret is kind of like, which one of these do you need? One of these geniuses to do, right? So I think they finally understand some of the issues we were having with We're having some of those customers and so some of the things they were trying to do was practically ship some of those over. And that's what happened with PBH. That's what I was going to say. And, you know. With PVH being one of the first that they did that. And it broke more than it did anything else. We need to be more careful. Yeah, so Colleen was getting on a call with them today, or at least was trying to because they were They're not giving the stuff to Kristin that she needs. I was like, see if Kristin can join that call. Maybe you guys Maybe you guys can just try and kill two birds with one stone and she can get what she needs to try and troubleshoot a little bit.

## Reunión 2026-06-03 — Ticket management challenges · Transcripción 5/9
_chunk 893 · 2026-06-03_

I'll have to check in with Colleen to see if she was able to get Kristin on that. I know that Colleen and Tyrone took the ticket. So Colleen, Tyrone, Matt, and I think Kristin. All talked today. Okay. I've been talking about the ticket, so, but that was like That was last I heard. OK. So I mean, she hasn't flagged anything to me, so I'm hoping that means I'm hoping that means things are moving the way they need to. But I'll check with her. Check with her, because I trust that she's bringing in the right folks. Right. The only other one that popped up for me just to put on your guys's radar, this is one that got flagged That flag to me from Val was Ralph Lauren, which Ralph Lauren is Ralph Lauren. They had to do with A couple of tickets that I think are open. The ones that I see, at least, You can see, at least in this email thread, is 27079. And one nine nine four eight nine. I can drop these in the chat. I don't know if they're related or not. We're not related or not, but this is just what's in the subject of the email. I'll drop them in the chat. So the 27079 was probably created off of the 199484. And I think Dean has been trying to work with them on these tickets, but basically Ralph Lauren, The Colmer guy at Ralph Lauren is kind of riled up about this and that's what kind of What triggered it for Val is he's been going back and forth with her in an email thread basically saying, so you're telling me You're telling me you're not going to be able to give us an answer for a week and this has been going on for a while and we're just trying to figure out like is this I mean, the issue is resolved. All they're waiting for is the RCA of the issue. That has been resolved. So, yeah, that's all there's meaning for. Anytime they're asking for the RCA, and I think this has been the process, and it certainly will be the process, And maybe that was Val's misunderstanding too.

## Reunión 2026-06-03 — Ticket management challenges · Transcripción 6/9
_chunk 894 · 2026-06-03_

It made it seem like we wouldn't have an answer in terms of like, The issue actively still being an issue. I'll clarify that with her. It's just simply getting the RCA document over to them. And I am just double checking. I mean, it looks like the It looks like the last time we told him we were going to do an RCA was on the... No, actually, I guess I guess it was when we apologized for just saying there's a delay on it on the 28th. So, you know how it goes. It takes a while. Take a while sometimes and this one has been... And understanding what was going on in the thread either is that it was an active issue and we said we wouldn't have anything for I don't have anything for them for another week and they were like freaking out. No, no. Knock on wood. We haven't had an issue with the Ralph Lauren And then load in over a week. Okay, good. And just to close the loop. Close the loop Amy was right, the RTS is the alerting ticket that came in that we then spun the RCS. I haven't. Awesome. So, I know what we just jumped right in. I'm sorry. All good. All good. This is Libby. She's Director of Customer Success. We may know each other from our previous life as We're going to talk about the future of the previous life as well. She's managing our Nuav support folks. She's based out of Bogotá, Colombia. Juan has also recently joined us. He's a team lead over the Bogotá, Colombia folks. So they are relatively new. They're shadowing, understanding, We will be able to help more and more over time. Thank you. So nice to meet you. I only know only a little bit, so. That was perfect, actually. How much do I know as well? Well, I used to be far more fluent, like in high school, and I just never I just never kept it going, but I'm grateful we have a very large Mexican population, and I'm based in Chicago. We have a very large Mexican population, so sometimes I get to practice. Now, and I'm pretty sure that with one beer, you start being fluent again. Yes, perfect. I'll practice more.

## Reunión 2026-06-03 — Ticket management challenges · Transcripción 7/9
_chunk 895 · 2026-06-03_

All right. Sorry, that was what else you got for us. One of the two only hot tickets. I didn't get anything from Kara. I know her calendar made me want to vomit looking at I'm sorry for the fact that I'm not looking at it today, so I think she had quite a bit. But those are just the main key pieces and usually JR2 with this one. We had it as just like a standing one in case there were In case there were other functional things we needed to chat through or try and Trends like the support team was noticing or anything on our side. So it's just sort of a formal Sort of a formal touch base where we can chat through things. No, it'll be good. We'll keep it rolling. Rollin', you know, we'll make sure we keep doing this. I think it's a good idea to stay connected. Yeah, for sure. I don't think I had anything off the top of my head, I can't remember. Team is just doing what they can to transition and I think that's a good thing. I'm joined up, so Libby, of course, keep me posted on anything you hear, but, you know, So we can help with before the team is transitioned out. We've been hearing a lot of folks say, the queue's on fire. I mean, they don't have to say that. We know the queue's on fire. We've also got new folks that are coming in and we're doing transition plans so people are responsible for They're responsible for writing documents, they're responsible for training people, and working on the queue. And what I've set everybody's expectations for. Before we have the misses, because of the utmost importance, of course, our customers and our critical tickets.

## Reunión 2026-06-03 — Ticket management challenges · Transcripción 8/9
_chunk 896 · 2026-06-03_

You know, five ballad watering kits are going to help interest our kids, taking res differentiate you finding your way in trying to Somewhere we can understand all the applicants but getting the new folks skilled up so that way they can help, Because if we can do that within by the end And then by the end of the month, then we're going to start seeing the dividends of that, you know, and they'll be able to help Lauren more. But I just want to prep you. It might get a little noisy for the next two to three weeks while we're working through that. So if you see any that we need to jump on that we're not, if you think it's critical, raise your hand and Amy, Camila, and myself will make sure that it gets prioritized. Okay. Well, yeah, I think whether or not you guys like it, I know where to find you. Yes, you do. And that's not a bad thing. And along those lines, yeah, we want to make sure that we're getting these, you know, our counterparts trained. So that when those of us that know what's going on do leave, We are not leaving people with no knowledge. No knowledge and not knowing what to do and things like that. So yeah, the key was right now I think was Right now, I think there's 26 tickets in the queue. The oldest one is the 29th, which is Which is pretty good. That's pretty good. I was afraid you were going to say it was like two months ago. But yeah, I haven't seen anything like that in a while. Yeah, so, but yeah. But yeah, so that's a good point. Okay, yeah, I'll keep you guys posted. CSMs aren't shy. So, yeah. Yeah, there a lot of them are reaching out direct to me and Kristin. We're trying to explain it as well. They've been advised to go work with you guys if anything super on fire. Usually they just fly So they just flag it if they're like, oh, I think this one is getting a little spicy. All right. All right. I appreciate it. Well, awesome, guys. Welcome again. And then just let me know if anything pops up. Sounds good. Thank you. Thank you, everybody.

## Reunión 2026-06-03 — Ticket management challenges · Transcripción 9/9
_chunk 897 · 2026-06-03_

Bye, everybody. Bye.

## Reunión 2026-06-17 — system updates
_chunk 919 · 2026-06-17_

## Resumen
The meeting covered several topics, including system updates, training sessions, and customer service strategies. Participants discussed issues with meeting notifications and the possibility of sessions starting early. Updates on Snowtime training were shared, with plans for future sessions and feedback collection to improve content. Access issues for new employees were highlighted, with efforts underway to consolidate access requests into a single IT ticket. Additionally, the importance of balancing technical and customer service skills was emphasized, with plans to enhance these through coaching and tailored training.

Operational challenges were addressed, such as managing aged tickets and prioritizing customer service training. Participants shared insights on understanding clients' industries to improve communication and service delivery. The discussion also touched on emergency preparedness, with a focus on ensuring personal safety during severe weather events in Illinois. Suggestions were made to create guides for investigating client contexts and to develop hybrid skill training programs for support teams.

The meeting concluded with updates on shadowing programs, feedback from both mentors and mentees, and the importance of leveraging experienced team members for customer service improvement. Participants shared personal experiences and tips for handling customer interactions effectively, including strategies for de-escalating conflicts and tailoring communication based on client profiles. The team expressed appreciation for ongoing efforts to improve processes and training, with a commitment to continuous learning and adaptation.

## Temas clave
- system updates
- Snowtime training
- customer service strategies
- access issues
- emergency preparedness

## Decisiones
- **Consolidate access requests for new employees into a single IT ticket.** — To streamline the process and ensure timely access for all team members.
- **Focus on aged tickets and work through the list from top to bottom.** — To address the most delayed issues and improve queue management.

## Tareas / Action Items
- Confirm if meeting notifications are functioning correctly for all users.
- Finalize the schedule for upcoming Snowtime and customer service training sessions.
- Prioritize resolution of the Snowtime access ticket to expedite team operations.
- Develop a training plan to enhance hybrid skills in technical and customer service areas.
- Create a quick guide for investigating client contexts based on their industry.

## Insights en vivo (Ask AI / Analizar)
### [Ask AI] alguna pregunta de valor?
Thanks, Tim. One question that comes to mind regarding the customer service training you mentioned: will there be specific modules or scenarios tailored to the Appriss Retail products, like Secure Store or Engage Return Authorization? Since these products have unique workflows and customer pain points, it might be helpful to align the training with those specifics. Also, will the training include guidance on handling escalations effectively, especially when technical issues overlap with customer frustrations?

- Pregunta clave: ¿Cómo se adaptará el entrenamiento a los productos específicos de Appriss Retail?  
- Escalaciones: ¿Habrá un enfoque en cómo manejar casos donde el cliente está frustrado por un problema técnico que requiere intervención de Engineering?  
- Contexto: Appriss Retail tiene productos con flujos únicos (ej. Secure Store, Engage Return Authorization) que pueden generar desafíos específicos en soporte.  
- Posible seguimiento: ¿Habrá documentación o playbooks específicos para cada producto que complementen el entrenamiento?

### [Ask AI] alguna pregunta de valor? o aporte?
Thanks for sharing those insights. One thing that stood out to me was your point about tailoring communication based on the client's industry or their familiarity with the software. Could you elaborate on how you've approached that in the past? For example, when working with less technical customers, are there specific strategies or tools you've found effective for bridging that gap? And on the flip side, for more technical clients, how do you ensure you're not oversimplifying or missing the depth they might expect?

- Estrategias para clientes menos técnicos: ¿Usan guías visuales, ejemplos concretos, o reuniones introductorias para explicar conceptos básicos?  
- Clientes técnicos: ¿Cómo se maneja el balance entre simplificar y mantener profundidad técnica? ¿Hay documentación avanzada o playbooks específicos para ellos?  
- Posible seguimiento: ¿Han identificado patrones en los tickets que ayudan a categorizar clientes según su nivel técnico o industria? ¿Cómo se reflejan esos patrones en el soporte diario?


## Pulsos de la reunión (resúmenes periódicos + hablantes)
### Pulso 09:40
Se discutieron varios temas relacionados con actualizaciones de sistemas, acceso a herramientas y entrenamientos. Se mencionó un problema con notificaciones de reuniones y un posible inicio temprano de una sesión. También se habló sobre entrenamientos recientes y futuros, incluyendo sesiones de Snowtime y formación en servicio al cliente. Se está trabajando en consolidar accesos para nuevos empleados y en mejorar procesos de soporte y capacitación.

**Temas:** actualización de sistemas · entrenamientos Snowtime · acceso para nuevos empleados · formación en servicio al cliente

**Sugerencias / preguntas:**
- ¿Podríamos confirmar si las notificaciones de reuniones están funcionando correctamente para todos los usuarios?
- ¿Hay un cronograma definido para los próximos entrenamientos de Snowtime y servicio al cliente?
- ¿Podemos priorizar la resolución del ticket de acceso para Snowtime para agilizar el trabajo del equipo?

**Hablantes:**
- **Participante 1:** Comentó sobre problemas con notificaciones de reuniones y un posible inicio temprano de una sesión.
- **Participante 2:** Mencionó entrenamientos recientes y futuros, incluyendo Snowtime y formación en servicio al cliente.
- **Baraj:** Indicó que su equipo necesita acceso a herramientas y está trabajando en consolidar una lista para IT.
- **Participante 3:** Confirmó que el ticket de acceso para Snowtime está aprobado pero aún no resuelto.

### Pulso 09:40
Se está discutiendo sobre los desafíos del soporte al cliente, destacando que este trabajo requiere habilidades específicas. Se mencionó que las personas suelen ser muy buenas en servicio al cliente o en aspectos técnicos, pero no necesariamente en ambos. Esto parece ser una continuación del tema de entrenamientos y procesos de soporte mencionado anteriormente.

**Temas:** desafíos en soporte al cliente · habilidades técnicas vs servicio al cliente

**Sugerencias / preguntas:**
- ¿Cómo podríamos diseñar un entrenamiento que combine habilidades técnicas y de servicio al cliente para mejorar el soporte?
- ¿Hay algún ejemplo reciente de éxito en soporte que podamos usar como modelo para entrenamientos futuros?

**Hablantes:**
- **Participante 1:** Comentó que el soporte al cliente es un área difícil porque requiere habilidades específicas, ya sea en servicio al cliente o en aspectos técnicos, pero no siempre ambas.

### Pulso 09:45
Se continúa la discusión sobre las habilidades híbridas necesarias en el soporte al cliente, destacando que encontrar personas con un balance perfecto entre habilidades técnicas y de servicio es casi imposible. Se propone entrenar y mejorar estas habilidades con el tiempo mediante coaching. También se mencionan desafíos operativos relacionados con la gestión de incidentes y auditorías, y se comparten experiencias personales sobre cómo entender mejor a los clientes según su industria y contexto. Finalmente, se aborda la importancia de priorizar la seguridad personal y familiar en situaciones de emergencia, como las tormentas en Illinois.

**Temas:** habilidades híbridas en soporte al cliente · gestión de incidentes y auditorías · prioridad de seguridad personal en emergencias

**Sugerencias / preguntas:**
- ¿Podríamos definir un plan de entrenamiento específico para desarrollar habilidades híbridas en el equipo de soporte?
- ¿Sería útil crear una guía rápida para investigar el contexto de los clientes según su industria antes de interactuar con ellos?
- ¿Cómo podemos garantizar la continuidad operativa en caso de emergencias climáticas como las tormentas mencionadas?

**Hablantes:**
- **Participante 1:** Destacó que encontrar personas con habilidades equilibradas entre servicio al cliente y aspectos técnicos es difícil, pero se pueden entrenar y mejorar con el tiempo mediante coaching. También mencionó que casi la mitad de los incidentes más antiguos ya han sido gestionados y sugirió trabajar de arriba hacia abajo en la lista restante.
- **Participante 2:** Compartió experiencias personales sobre cómo entender mejor a los clientes investigando su industria y contexto, y cómo esto puede influir en el enfoque del servicio.
- **Participante 3:** Comentó sobre las tormentas en Illinois y la importancia de priorizar la seguridad personal y familiar en situaciones de emergencia, asegurando que la empresa apoya estas decisiones.


---

## Transcripción completa
App Service is having a good one. Strange thing is I did not get a notice that Usually I get a note of the time. Notice whenever a meeting starts. It's kind of a surprise to see everybody on when I joined. It was a Windows update. That was update yesterday, right? Yeah, I think I'm not sure. Sure, that was weird, I did notice that too. But it looked like when I was looking at the I'm looking at the meeting and it looked like it was already started, so I'm not sure if someone had it open early. Yeah. But it usually would still show. Seven minutes early. I got that one. Yeah, I saw Matt, but I thought Matt was in the other meeting. I didn't realize he was in the meeting. And I can't even realize who was in this meeting. All right, team. I meant having started it, not in both of them. What are we at? Wednesday? Is it Wednesday today? I think it is. Happy Wednesday. The holiday in Colombia and Friday is a holiday in the US. So, most of the US folks will have off. I'll have my phone if anybody needs anything, if something crazy happens, It happens, you're working on call, you need an assist, or you're working on shift, you need an assist. I'm not afraid to ping me on Teams. My phone number is also in my profile and case. We had an ad hoc training this week. Thank you for joining us for this week's training this week for Snowtime, and that was presented by Dan We go from support at various times that join the training. It was our first real... We'll talk about the real view of Snowtime and how to use Cloud to troubleshoot it, which is We will be having another I'm still working through the logistics of it. Originally, it was going to be presented. I'm going to be presented by Dan because Dan's the one that trained delivery anyway. He's going to give us another session. If there is something that you want that you That you didn't receive in that session within Reason, then please... Please take the chat where I asked in support team and where I put the I put the poll in there and just write underneath it what you're hoping to see in the next session. I'm going to go back to Dan and make sure he's armed with a few things that will help We're going to record it. I do want to prepare most of you. This was my first session like this. I'm here with the company where engineering is training us on how to use a product. And it is a little bit different than what I've experienced in other companies. So for those of you that are new and you're wondering about the curriculum and it will have a different You'll have a different type of curriculum going forward as we firm up more support training Support training is onboarding at our process. We will have those out of support. I'm going to give you a little bit of support and I will work with the leaders across the company to try to have a little bit more. We can only control the data that we need to control. We can only control what we can control. I'm just happy we can get the time of the architecture. We can architect over the product to show us what's going on, and then we can try to put something together. Put something together better for the future. So I appreciate you folks bearing with us while we figure this out. Next bit for those of you on the new The new upside, I'm working through getting some customer service training for Please stay tuned for that. I'm going to work with Rip over the coming week or two and then with Copper. And then with Koppel on the new offside and see about presenting that to you folks. You can also visit us at www.kl.com. Service 101 and 201, which means, you know, You know, intro and then more intermediate customer service skills. Those are the big topics for me. If you find yourself not in Not if I'm talking about something that's in a channel and you don't see it, it might mean It might mean that you're not in the channel. I've done a once over and tried to make sure that everybody's Everybody's in every channel. If you suspect there's a channel out there, though, that you're missing, If you're missing, please have a conversation with your team leader manager about it. Team leads and managers, please just double check and make sure that everybody that reports The only way that reports to you is in all of the channels under the support team group. I think that's a good point. I think those are the major updates from me. The queue continues to deliver. I appreciate everybody's patience with each other, with the customers. Customers, as we're working through this, I know doing coaching shadowing sessions. sessions is complex while the queue's being worked, but what I anticipate is The next week we're going to start to see a little bit of the fruits of that labor and then that will only get better and better as each week goes by. And what I mean by that is for those of you that have been coached, next week I expect that you're going to start taking some tickets while super While supervised by your shadow buddy and starting to work through some things, I've heard good feedback from everybody, from both sides, I should say. should say from the shadow words and the shadow ease about how the shadowing has gone. That's it from me. Let's go around the horn with the managers that I see on the line really quick, and if I don't call on you and you're a I'm not missing you and you're a manager. It's probably because your camera's not on and I'm missing you. So payment, we'll go with you first. Anything for the team? I don't have anything for the team, just weird, you know, weird. The first group of people It's going to be gone from my team. The first person is going to be gone. We got my team four weeks from now. That's what I heard. So we will get more Tickets assigned to other people within this. This is the next cube in this meeting. But otherwise we are chugging along. You know, we're still learning how to crawl. We haven't walked yet. So we'll see how there's no time. There's no time for war. But otherwise, everything is OK. Thanks, Pan. I appreciate it, sir. We'll bounce around, I'll grab some team leads as I go. Kristin, anything for the team on your side? No, nothing new today. Thank you, ma'am. Juan, how about you? How's the shadowing coming? Anything to share with the team? All right, sounds good, Tim. Real quick to that point. As you folks are working through some of this, if you have questions for the new folks specifically, if you have If you have questions about process, if you have questions about how to handle How to handle particular issues, of course start with your shadow buddy and go through your management Go through your management team, but I'm also happy to help. If you guys just want to get on and you want to see it And you want to see a ticket and you want to talk about the best way to reply to a customer or if you see a really mad customer. Been doing support for 27 years now in a variety of large, small companies. So customer service is a skill that takes a long time Get training on it is one thing, but you're going to need experience. We're going to be talking about the experience and leveraging those around you that are experienced. We'll be back with more on the next session. If you want to gut check on something, even before your shadow buddy sees it, I'm I'm happy to take a look at it, so feel free to take me up on that team. All right, sorry, Baraj, I saw you came off mute. What's going on in your answer? Nothing much, I took actually one ticket closely working with Carlos. This is Chingonet. We'll work accordingly with closely with him. Other than that, our team needs a lot of access. So, once Kamala is back, what we are trying to do is, Segregate all the list of access, create a single ticket with IT for all the new WoW guys. So we can have the basic access we can start playing with. I appreciate that, Baraj. I did see that the I can see that the Snowtime Access, I put in a large ticket to get a variety Variety of different accesses for snow time, and that was approved, but it's But it's not marked resolved yet, so I was told by the folks The folks in IT and InfoSec, while they are going to do it, it does take a while because That's been a while because there's a lot of systems and there's a lot of people to do. So they're working on it. So, I have a question for you, like you mentioned a separate Separate rings for the service desk or something like that, right? That will be like, that will be trainings for customer service or? This is our customer service training for the product side. This will be specifically customer service, how to deal with customer service. How to deal with customers, how to write a reply in a friendly manner for a customer, How to take an angry customer and de-escalate them. Basically, how to work with Work with a customer. Exactly, exactly that. Because support, especially in a common Support is a hard thing to do because typically you have people that are usually really good at They're really good at customer service, or you have people who are really good at technical and And finding a person that's perfect at both is almost impossible. We're looking for 60-40 in one way on both sides. We have to train you on it. We'll see you on it. You'll experience it over time and get better and better at it. And we'll coach you. We'll coach you, of course, as we start seeing more and more of these replies. Okay. I believe, last but not least, from the management team, what's going on on your side. Let's focus on taking a look at the It was 5 p.m. yesterday. Looks like about almost Almost half of them have been taken, but those are the most aged. So, and I think we should start with that list and kind of And kind of work our way top to bottom. Other than that, Other than that, everything else is business as usual. Unfortunately, since Illinois has become part of the Tornado Al Tornado Alley for our region today and tomorrow. And tomorrow's expected to have storms, so I'm hoping and praying that. I don't lose power or enter in it, but compared to a tornado, I don't care. Sorry. Sorry, but not sorry. But, you know, yeah, so that is... is what I'm up against for today, so we'll see how things go. Hopefully everything will be like, you know, so. Your health and family always comes first, right? So there's a danger. In any way, shape, or form. No one's dying at this company if you have to go. Have to go save your family's life. Don't worry. Do what you need to do, Dean. Stay safe. That's all I have. Thank you. Anything you need help with, anything you want to raise. Just add to that customer service that you're talking about too, just as you're As you're talking about hybrid skills, I find myself in that fancy in the middle where I got Experience from both sides is just kind of just from all angles and I just kind of give some Some easy suggestions for people for customer services as you're finding out sometimes, I find I find, just depending on what customer you're dealing with, sometimes I find it... Find it helpful just to understand what business they are in or just kind of somehow look up the name of the business and see And see what products they have or understanding how big or complex they are to understand the client I'm working for. I'm working for it. Then the other thing too, then I kind of, the last few years I've kind of I've kind of taken into more of my own, because a lot of times the people we deal with, especially I'll talk more about the incident audit side, just to understand what your clients may be I'm going to go ahead and start with the question. I kind of worked in some different engines. I used to work in an entertainment industry where you'd kind of come into places Come into places, bars and restaurants, people are offering you drinks and food, and there's a lot more loosey-goosey Stiff, you know, the people, you know, no offense to our clients, but there's more business in the people. The software is more like accounting people, they're just crunchy numbers. It's all about loss, so it's not the fun side of business. So that's a good point around. You know, I've worked with a ton of retail. I worked for the The people that we're working with here is entirely different, and the way that you work with them is entirely different. And then, like I said, then I've been on the bad side of the company, but sometimes I felt bad because even when I've been working with companies doing AV, audio, video installation, where I have to come in and help get I was in there showing them footage of people I didn't know. The people that did stuff and like, hold on, I'll be right back. And I'm like, oh crap, I have chills talking about now. Now, where I see people getting fired, or know things are going to talk to someone, or even like, like pulling up a very uncomfortable footage of people leaving bars We're going to talk about the investigation of people from the company. I think we're going to have a lot of time to talk about the things we're going to be talking about. That's my kind of tips for certain things, especially the company like The way it's done, you can have a little bit of time to talk to this person until like a half a year later than you just I've even had some newer clients too, sometimes if there's someone newer in the Newer in the software, just getting, having a half hour meeting with them just to understand things and try Try to explain to them, like, hey, when you send screenshots, or just almost explain the easy stuff, you know. All of these stuff, just like that, will help you out later on with the tickets of people, so 100%. 100%, man. One of the first things I always think about, no matter what industry you're in doing customer service, This is, you've all had bad customer service experiences, and you've all had good customer That's a great way to get a good customer service experience. Whether you're calling the company, whether you're emailing, submitting, links, submitting a ticket, whether you're in the store, working with somebody over-the-counter. You You know what it's like to have a bad experience. So I always just try to take in my mind that that person's usually having a bad day. They're not calling us because they're having a good day. They're calling us because there's a problem. And I just try to put my Try to put myself in their shoes, be reasonable, try to help them, be realistic, keep them up to date. Get them operational as quickly as possible. You guys really want the same thing, right? They don't want to be on the phone with you. They don't want to be in this email. We're going to start with the first step. Put yourself in their shoes, it gets easier and easier. Some customers are technical, some customers aren't. Most of our customers We'll start with the next slide. I still have plenty of room to grow like everybody who's been doing this. There's nobody that's perfect at this. It's ever evolving. All right, team, what else we got? Anybody got any questions, comments, concerns? I do. Just an FYI. That's why I need to leave at 3.30 today for a dentist appointment. Just to mention talking about training, our Our legacy team had to do We had to do weeks and weeks and weeks of customer service training. I can't remember what it was called even, but it was... It was a lot of customer service training. I got the documentation for that, Kerry. How did you like it? I've been a developer for 20 years, so a lot of it was stuff I knew I knew in common sense, but it was good. It was just a It was just a lot. That's all. It was good training, though. It was heavy. Matt was the king of the getting it done, though. I see he raised his hand. I just want to say one more thing about the... I just want to comment on the Comment on Diego. Diego is working multiple work item tickets. We have been shadowing practically every day. She also being a full stack engineer has been teaching me a lot. A lot. So it's going well. That's great to hear. That's really great to hear. Thank you, Carrie, and thank you, Diego. And you're cutting. Mr. Everett, you had a comment. That training, it was heavy, but there was some stuff in there that's That's probably worth you checking so I can send you a I sent it to Amy back in the day so I can just send it over again to see if there's anything in there. It's never even considered, but I use even now, so. We're always our men. Look, I've received, sorry, Kerry, I've had about 15 of these I've learned something out of it. I picked up a new skill out of every single one of them. Sorry. Sorry, Gary, go ahead. No, I just was saying that's true. Yeah. All right, team. Team, well, if we don't have anything else, we can get 10 minutes back in our day. Any help? Next team. Thank you, Tim. Thank you Tim, have a nice day. Thank you. Thanks everyone. Thank you.

## Reunión 2026-07-22 — Access issues for Kimberly Baney
_chunk 1373 · 2026-07-22_

## Resumen
During the meeting, participants discussed resolving access issues for Kimberly Baney regarding the customer support ticketing portal. It was confirmed that Kimberly currently does not have access to the portal, and an email was drafted to request permission from Ronald, the application administrator, to grant her access. The email also included Colleen, the Customer Success Manager (CSM), to keep her informed about the situation. The importance of users opening tickets directly in the portal was emphasized to prevent emails from being lost. Additionally, the participants discussed the process for handling urgent cases when portal access is unavailable, suggesting that technical assistance should be sought promptly.

The conversation also touched on a follow-up to a previous ticket related to the portal's backend setup. It was noted that users should not access certain URLs directly, as these are still being configured. The participants acknowledged that similar issues have been recurring frequently and discussed the need for a streamlined process to address them efficiently. The meeting concluded with a plan to send the drafted email to Ronald and await his response before proceeding with further actions.

## Temas clave
- Access issues for Kimberly Baney
- Customer support ticketing portal
- Handling urgent cases

## Decisiones
- **Include Colleen in the email thread to keep her informed about Kimberly's access issue.** — Colleen is the Customer Success Manager and needs to stay updated on customer-related matters.

## Tareas / Action Items
- Send the drafted email to Ronald requesting permission to grant Kimberly Baney access to the customer support ticketing portal. (resp: Yo) — vence 2026-07-22
- Follow up with Ronald for his response regarding Kimberly's access. (resp: Yo)
- Document a procedure for handling urgent cases when portal access is unavailable.

## Pulsos de la reunión (resúmenes periódicos + hablantes)
### Pulso 13:11
Se discutió un problema relacionado con el acceso de Kimberly al portal de tickets de clientes. Se mencionó que Kimberly no tiene acceso actualmente, y se está solicitando permiso a Ronald para agregarla. Mientras tanto, se ha reenviado un correo electrónico con detalles del problema y se está copiando a Colleen, la CSM, para mantenerla informada. También se destacó la importancia de que los usuarios abran tickets directamente en el portal para evitar que los correos se pierdan.

**Temas:** Acceso al portal de tickets · Gestión de solicitudes de soporte

**Sugerencias / preguntas:**
- ¿Ronald ya ha respondido previamente a solicitudes similares? Esto podría acelerar la decisión sobre Kimberly.
- ¿Hay un procedimiento documentado para manejar casos urgentes cuando el acceso al portal no está disponible? Esto podría evitar retrasos en el futuro.

**Hablantes:**
- **Participante 1:** Explicó que Kimberly no tiene acceso al portal de tickets y que se está solicitando permiso a Ronald para agregarla. Mientras tanto, se ha reenviado un correo con detalles del problema y se está copiando a Colleen para mantenerla informada. También mencionó que es preferible que los usuarios abran tickets directamente en el portal para evitar que los correos se pierdan.


## Contexto capturado (notas y capturas)
- 📷 **Captura:** The screen shows an email draft requesting permission to grant Kimberly Baney access to the customer support ticketing portal. It relates to the meeting as participants discuss resolving access issues and ensuring proper ticketing processes.
  ![captura](file:///Users/MancoMenStudio/Library/Application Support/InterviewApp/Screenshots/shot-1784743690793.png)
- 📷 **Captura:** The screenshot shows an email thread discussing a technical issue with a portal login. The meeting focuses on resolving access for Kimberly and coordinating with relevant stakeholders to address the error message displayed in the portal.
  ![captura](file:///Users/MancoMenStudio/Library/Application Support/InterviewApp/Screenshots/shot-1784743769087.png)

---

## Transcripción completa
incident. They were made to make a new So they were having trouble. So she also put new requests. Request, which is true. She has a new request because she's having an issue. I checked in the organization Kim does not have access to our portal, okay? So what I did is I did a forward email. Okay. again I can give this to you and if you want to send it of course I just put this together so you could see what I was doing This guy is copied. He's their application administrator. Okay, so I forwarded I put a forwarding on here here and I'm asking Ron if Kimberly Kimberly is someone who should have access to our customers. Customer Ticketing Portal. We're happy to add her. We just need his permission to do so, if not, you know If you need technical assistance for that last request to move forward with assisting here. We try not to but we try and force them to open the tickets. tickets. Otherwise they send these emails and then they get lost, right? Or Oh, you're supposed to open a ticket in the portal. So, I guess, like I said, my question to you is If you would like to send this message, I can give this to you. and you can send it to Ron Ronald, or I can just add you here however you want to do this. Response that we get from him. Just to add you to it? Okay. So we'll do that. We'll put one on. Whoop, I've got a spelling name right. Put one on here. Okay. So we're going to So we're gonna do that and I'm actually going to put Colleen on here. Who's the CSM? and the other one. Yeah, yeah, so I'm just copying her Situation. So I'm going to do this. We'll send it off. and then we'll see what happens. is going forward, we would like it if you would do you would do this because it's quicker if we're not available, you know, to make sure you get assistance. If the application had been completely down, then we Ronald on it and then deal with the back end stuff of who should have access or not after the fact. the Fact. But this is one where she has access. She's just having trouble getting to a So that's why I'm doing it the other way with just checking in and following the process. Yeah, so anyway, that's what I'm doing there. I was trying to think if anything else came through through. This was just a follow up to a different tick. Ticket, just so you know, again. uh this one um with the pla and at this time, all they're doing is setting up Main URL that says LP guys at this time. Okay. OK, they're not supposed to be going directly to it should be on should be on here to this one. On the back end. but they can't access it directly from here yet. All that has to do with Anyway, that kind of stuff is coming in a lot. I feel like it's coming in a lot. So anyway, I just wanted to show that to you too. You're welcome. I thought I better show this to you while it's there. and the next steps will be taken depending on what he says. added to the portal. Do you want me to show you that? Again, we've looked at it once real quick. Yeah, I'll just watch you. and the other one. Okay, we'll talk to you later. Bye-bye.

## Reunión 2026-07-28 — Breakout sessions
_chunk 1388 · 2026-07-28_

## Resumen
The training session focused on handling customer reactions and complaints. Jeff introduced the session and emphasized the importance of breakout groups, where participants were encouraged to collect materials and responses. He committed to answering questions honestly and suggested using a second monitor to follow the 20-page presentation. The session's main resource, a PDF titled 'Customer Service Excellence,' was shared after initial technical issues with the link. The document includes topics such as the customer's point of view, three guiding principles of customer service, and strategies for handling complaints. Participants verified the link and successfully downloaded the PDF. Jenny assisted in resolving the link issue. Jeff also mentioned that he would periodically check in during breakout sessions to ensure progress and provide support. The session concluded with participants being given time to review the material and prepare for the breakout discussions.

## Temas clave
- Breakout sessions
- Customer Service Excellence PDF
- Handling customer reactions and complaints

## Decisiones
- **Breakout sessions will be used to facilitate group discussions and material collection.** — Encourages active participation and practical application of concepts.
- **Jeff will periodically check in during breakout sessions.** — Ensures progress and provides support to participants.

## Tareas / Action Items
- Organize breakout sessions and ensure participants collect necessary materials and responses.
- Verify the functionality of shared links before the session to avoid delays.
- Prepare and distribute the 'Customer Service Excellence' PDF to all participants.

## Pulsos de la reunión (resúmenes periódicos + hablantes)
### Pulso 09:12
Se mencionó que habrá sesiones de trabajo en grupos pequeños (breakout sessions) y que el facilitador, Jeff, estará revisando periódicamente el progreso. Se sugirió utilizar un segundo monitor para seguir el material de la presentación, que consta de aproximadamente 20 páginas. Jeff enfatizó que los participantes deben recopilar los materiales y respuestas necesarias durante las sesiones grupales. También hizo un compromiso de responder preguntas de manera honesta, sin inventar respuestas.

**Temas:** sesiones grupales · material de presentación

**Sugerencias / preguntas:**
- ¿Podrías aclarar cómo se organizarán las sesiones grupales y si habrá roles específicos asignados a los participantes?
- ¿Hay algún formato sugerido para recopilar las respuestas durante las sesiones grupales?

**Hablantes:**
- **Jeff:** Explicó que habrá sesiones grupales y que estará revisando el progreso. Recomendó usar un segundo monitor para seguir el material de la presentación y pidió a los participantes recopilar materiales y respuestas durante las sesiones. Se comprometió a responder preguntas de manera honesta.

### Pulso 09:17
Se presentó el tema de la sesión: 'Manejo de Reacciones y Quejas de Clientes'. Se compartió un enlace al recurso principal, un PDF titulado 'Customer Service Excellence', que incluye un índice con temas como el punto de vista del cliente, los tres principios guía del servicio al cliente y el manejo de quejas. Hubo problemas iniciales con el enlace, pero finalmente se verificó que todos los participantes pudieron descargarlo. Jenny fue mencionada como alguien que ayudó en este proceso.

**Temas:** Manejo de reacciones y quejas de clientes · Customer Service Excellence PDF

**Sugerencias / preguntas:**
- ¿Podrías aclarar cómo se aplican los tres principios guía del servicio al cliente en situaciones específicas de manejo de quejas?

**Hablantes:**
- **Participante 1:** Introdujo el tema de la sesión y mencionó el recurso 'Customer Service Excellence'. Hubo problemas iniciales con el enlace, pero se resolvieron y se verificó que todos pudieron descargar el PDF. También mencionó los temas principales del documento, como el punto de vista del cliente y los principios guía del servicio al cliente.


---

## Transcripción completa
Team members, JR, if you want to jump in here and say anything and Starting just a little bit. Go ahead Jeff. Thanks Chris, I appreciate it. There will be breakout sessions. I'm going to drop in from time to time to check to see if and other things available on Teams. Chris, thank you for this. I appreciate it. No problem, JR. You have a great day, and we'll see you a little bit later. All right, everybody. and that accompanied this presentation we're going to go through today. It's 20 pages long or so. There's two ways that you can You can also do it on a second screen if you've got a PDF version of it. I have a hope every time I do one of these sessions that I can get a few people to turn Is it a verage? I want you to stop and ask any questions that you have on this. and I will not make up an answer. That's my commitment to you. I don't make up answers. Makeup Anches, the real skinny on it, everything that I can and help you with. and the other one I always like to say is when we send you to a breakout session, and by the way, there's one coming up right away. Collect the material that you want and the responses that you want to give. It's always good for you guys to sometimes at least select some and the session that we're going to be doing here. It's called Handling Customer Reactions and Complaints and we give you a nice resource that you can use later on OK, well let's see if JR is still here. May have left, but let's look and see now. He is not here. I'm gonna try to know that I can honestly send this on Interesting that you didn't get that. I can see what I can do here Let me see if I can copy this link to the workbook and stick it in the chat. and all link to the chat. I'll be right back behind the scenes working on another thing. is a duplicate. Okay. That workbook link work for you folks. I'm not seeing it Yeah, nothing was that imitated. Let me try it. Let me try it one more time folks. See if it will go again. She looks like it's in the chat now. Yeah, verify. Verifying the link. Yeah, we can download it. We are able to get the PDF So everybody give me a thumbs up if you got that link. Link to this one. Thank you, Jenny. Appreciate it. Thank you. So what I had told you was you'll find out the front of that piece. It says the customer service excellence You've got that table of contents. So customer point of view, the three guiding principles of customer service and handling and other ways that you can fill in as we go through. If you can do that, I'll give you a minute. That's pretty close to a minute. Ms. Mahar maybe. Yes, Aisha.

## Reunión 2026-07-28 — Empathy in customer service · Resumen
_chunk 1389 · 2026-07-28_

## Resumen
The training session focused on improving customer service interactions, emphasizing empathy, professionalism, and respect for customers' time. Participants discussed the importance of clear communication, especially through tools like Teams chat and text, and how these channels require specific protocols to ensure effective interactions. Key customer needs such as fairness, information, and control were highlighted, with suggestions to provide consistent updates and realistic expectations to avoid leaving customers in uncertainty. Camilla emphasized the value of understanding customers' perspectives and providing timely updates to enhance their experience.

The session also explored strategies for handling frustrated customers, noting that their frustration is often directed at the situation rather than the individual. Techniques such as allowing customers to vent, maintaining a professional demeanor, and offering clear solutions were discussed. Participants shared examples of successful customer interactions, highlighting the role of empathy and collaboration in resolving issues effectively.

Towards the end, participants ranked different customer types based on frequency of interaction, including informed experts, bargain hunters, and socializers. The importance of tailoring customer service approaches to these types was emphasized. The session concluded with a focus on action planning, encouraging attendees to reflect on their learning and set specific goals for improving their customer service skills over the next 30 days.

## Temas clave
- Empathy in customer service
- Clear communication protocols
- Handling frustrated customers

## Decisiones
- **Focus on empathy and understanding as key elements in customer interactions.** — Customers value being understood and receiving timely updates.
- **Allow customers to vent to reduce frustration and improve communication.** — Venting helps release pressure and facilitates problem-solving.

## Tareas / Action Items
- Develop specific protocols for Teams chat and text to improve customer interactions.
- Provide consistent updates and realistic expectations to customers to enhance their sense of control.
- Rank customer types and tailor service approaches accordingly.
- Create a 30-day action plan to implement training insights. — vence 2026-08-27

## Insights en vivo (Ask AI / Analizar)
### [Ask AI] que es lo que tengo que hacer en la sala?
Lo que entiendo es que en la sala, tu rol principal es absorber conocimiento sobre cómo manejar la interacción con clientes de manera efectiva, especialmente en canales como Teams chat y texto. Esto incluye mostrar respeto por su tiempo, ser consistente en el trato, y demostrar empatía y profesionalismo. También se espera que identifiques cualquier hueco en los procesos actuales o en tu comprensión, para poder hacer preguntas relevantes y profundizar en los temas que aún no están claros.

- **Puntos clave**:  
  - Mostrar respeto por el tiempo del cliente es crítico para mantener su fidelidad.  
  - Los clientes buscan resolver problemas específicos, no interacciones innecesarias.  
  - La empatía, profesionalismo y consistencia son fundamentales en la comunicación.  
  - Teams chat y texto son herramientas frecuentes, pero requieren protocolos claros para ser efectivos.  

- **Dudas / lo que falta**:  
  - No se especificaron protocolos concretos para Teams chat y texto.  
  - No quedó claro cómo manejar situaciones donde el cliente ya está frustrado.  

- **Próxima pregunta a hacer**:  
  You mentioned that showing respect for a customer's time is critical, especially when using Teams chat or text. Could you share specific examples or protocols that have worked well in these channels to ensure effective and respectful communication?  

- **Conexión con tu documentación**:  
  Sin conexión directa con la doc actual.


## Pulsos de la reunión (resúmenes periódicos + hablantes)
### Pulso 09:42
Se discutió sobre la importancia de mostrar respeto por el tiempo de los clientes, destacando que cuando no se hace, puede generar frustración y pérdida de fidelidad. Se mencionó que los clientes buscan resolver problemas específicos y que la apreciación por su negocio es clave para mantener una buena relación. También se hizo referencia a un doctor llamado John Young y a la interacción con él, aunque no fue positiva. Finalmente, se mencionó el uso frecuente de herramientas como Teams chat y texto en la comunicación con clientes.

**Temas:** Respeto por el tiempo de los clientes · Apreciación por el negocio de los clientes · Interacción con el Dr. John Young · Uso de Teams chat y texto en comunicación

**Sugerencias / preguntas:**
- ¿Podrías profundizar en cómo se puede mejorar la interacción con clientes cuando se utiliza Teams chat o texto? ¿Hay algún protocolo o recomendación específica?
- ¿Qué estrategias se han implementado para mostrar respeto por el tiempo de los clientes en situaciones donde hay múltiples canales de comunicación involucrados?

**Hablantes:**
- **Participante 1:** Habló sobre la importancia de respetar el tiempo de los clientes y cómo la falta de esto puede llevar a que no regresen. También mencionó la necesidad de agradecer y mostrar apreciación por su negocio.
- **Participante 2:** Compartió una experiencia con el Dr. John Young, señalando que la interacción no fue positiva.
- **Participante 3:** Comentó sobre el uso frecuente de Teams chat y texto en la comunicación con clientes.

### Pulso 09:47
Se mencionó que el 81% de los consumidores en Estados Unidos sienten lealtad hacia las empresas que respetan su tiempo y los ayudan sin agregar interacciones innecesarias. Se discutió la importancia de atributos como amabilidad, empatía, justicia, control, opciones y alternativas en el servicio al cliente. También se destacó la necesidad de consistencia en el trato profesional y cortés hacia los clientes. Se sugirió trabajar en conjunto para mejorar estos aspectos y se mencionó que habrá una reunión con las mismas personas en cinco minutos.

**Temas:** lealtad del cliente · atributos clave en el servicio al cliente · consistencia en el trato

**Sugerencias / preguntas:**
- ¿Cómo se puede medir la consistencia en el trato hacia los clientes para garantizar que se mantenga en todos los niveles de interacción?
- ¿Qué estrategias específicas se podrían implementar para mejorar la percepción de justicia y control en el servicio al cliente?

**Hablantes:**
- **Participante 1:** Destacó que el 81% de los consumidores en Estados Unidos valoran el respeto por su tiempo y la ayuda sin interacciones innecesarias. También mencionó atributos clave como amabilidad, empatía, justicia, control, opciones y alternativas en el servicio al cliente.
- **Participante 2:** Subrayó la importancia de la consistencia en el trato profesional y cortés hacia los clientes y sugirió trabajar en conjunto para mejorar estos aspectos.

### Pulso 09:52
Se presentó un documento con seis necesidades básicas del cliente en la página 8. Se propuso discutir al menos una o dos de estas necesidades, destacando 'justicia' e 'información' como áreas clave para mejorar. Camilla sugirió que la empatía y la comprensión son fundamentales, especialmente al proporcionar actualizaciones claras y expectativas realistas a los clientes. También mencionó la importancia de no dejar a los clientes en la incertidumbre durante largos períodos de tiempo.

**Temas:** necesidades básicas del cliente · empatía y comunicación con clientes

**Sugerencias / preguntas:**
- ¿Podríamos detallar cómo implementar mejoras en la comunicación para evitar que los clientes se sientan en la incertidumbre durante largos períodos?
- ¿Qué herramientas o procesos específicos podríamos usar para garantizar que las expectativas de los clientes sean claras y realistas desde el inicio?

**Hablantes:**
- **Participante 1:** Propuso discutir las necesidades básicas del cliente, destacando 'justicia' e 'información' como áreas clave para mejorar.
- **Camilla:** Subrayó la importancia de la empatía y la comprensión, sugiriendo que se deben proporcionar actualizaciones claras y expectativas realistas para evitar que los clientes se sientan en la incertidumbre.

### Pulso 09:57
Se enfatizó la importancia de la empatía y la comprensión hacia los clientes, destacando que los clientes no están frustrados con los ingenieros, sino con la situación que enfrentan. Se discutió la necesidad de proporcionar actualizaciones claras y consistentes para devolverles una sensación de control. También se mencionó que ser profesional y amigable en las interacciones mejora la experiencia del cliente. Finalmente, se sugirió que los clientes valoran opciones y alternativas justas, y se animó a tomar notas sobre estos puntos clave.

**Temas:** empatía hacia el cliente · actualizaciones claras y control · profesionalismo y amabilidad · justicia en opciones y alternativas

**Sugerencias / preguntas:**
- ¿Podríamos explorar ejemplos específicos de cómo devolver control al cliente en situaciones complejas?
- ¿Qué estrategias concretas se pueden implementar para garantizar que las actualizaciones sean consistentes y claras?
- ¿Cómo podemos entrenar a los equipos para manejar clientes que están venting out sin comprometer la profesionalidad?

**Hablantes:**
- **Participante 1:** Subrayó la importancia de la empatía y la comprensión hacia los clientes, destacando que su frustración no es personal hacia los ingenieros, sino hacia la situación. También mencionó que proporcionar actualizaciones claras ayuda a devolverles una sensación de control.
- **Participante 2:** Comentó que ser profesional y amigable en las interacciones mejora la experiencia del cliente y que los clientes valoran opciones y alternativas justas.

### Pulso 10:02
Se retomó el concepto de 'Verage Venting', destacando que permitir que alguien se desahogue sirve para liberar presión. Se introdujo la idea de ser centrado en el cliente, señalando que es difícil mantener una posición única o superior en el mercado. Se mencionaron estrategias para expandir el negocio, como trabajar con clientes actuales y nuevos, y se plantearon preguntas sobre cómo superar expectativas, qué acciones tomar y qué obstáculos podrían surgir. Se pidió a los participantes reflexionar sobre estas cuestiones.

**Temas:** Verage Venting · Centrado en el cliente · Expansión del negocio

**Sugerencias / preguntas:**
- ¿Podrías dar un ejemplo concreto de cómo permitir que un cliente se desahogue ha ayudado a resolver una situación difícil en el pasado?
- ¿Qué estrategias específicas se han utilizado para superar las expectativas de los clientes actuales y nuevos en este contexto?
- ¿Qué tipo de obstáculos comunes han enfrentado al intentar expandir el negocio con clientes existentes y cómo los han superado?

**Hablantes:**
- **Participante 1:** Explicó el concepto de 'Verage Venting' como una herramienta para liberar presión y mencionó la dificultad de mantener una posición única en el mercado. También planteó preguntas sobre cómo superar expectativas, qué acciones tomar y qué obstáculos podrían surgir.

### Pulso 10:07
Se discutió la importancia de compartir ideas y conocimientos dentro del equipo para mejorar la atención al cliente y resolver problemas de manera más efectiva. Se mencionó que un estudio de Forum Corporation encontró que el 70% de los clientes dejan de hacer negocios debido a la falta de atención, lo cual es un factor controlable. También se destacó la necesidad de comunicar adecuadamente los recursos y conocimientos internos hacia la comunidad. Hubo problemas técnicos con los micrófonos de algunos participantes, lo que interrumpió brevemente la conversación.

**Temas:** colaboración interna · retención de clientes

**Sugerencias / preguntas:**
- ¿Podríamos profundizar en cómo se está comunicando actualmente el conocimiento interno hacia la comunidad y qué herramientas se están utilizando para ello?
- ¿Qué estrategias específicas se podrían implementar para garantizar que los clientes reciban la atención adecuada y evitar que abandonen el negocio?

**Hablantes:**
- **Participante 1:** Destacó la importancia de compartir ideas y conocimientos dentro del equipo para resolver problemas y mejorar la atención al cliente. Mencionó que un estudio de Forum Corporation encontró que el 70% de los clientes dejan de hacer negocios por falta de atención.
- **Participante 2:** Subrayó la necesidad de comunicar los recursos internos hacia la comunidad y sugirió que todos trabajen juntos para compartir ideas y conocimientos.

### Pulso 10:12
Se continuó la discusión sobre la importancia de los clientes internos y externos, destacando que cada miembro del equipo tiene soluciones para los problemas comunes que enfrenta la empresa. Se mencionó la necesidad de mostrar disposición para ayudar y utilizar un lenguaje cortés como parte de las mejores prácticas para mantener la satisfacción del cliente. También se hizo un llamado a los participantes para que reflexionen sobre qué podrían hacer de manera diferente en su trabajo, aunque no se les presionó para compartir sus ideas públicamente.

**Temas:** clientes internos y externos · mejores prácticas para la satisfacción del cliente

**Sugerencias / preguntas:**
- ¿Podrías dar un ejemplo concreto de cómo mostrar disposición para ayudar ha marcado una diferencia en la satisfacción del cliente en tu experiencia?
- ¿Qué estrategias específicas recomendarías para fomentar que los equipos compartan sus soluciones de manera más activa?

**Hablantes:**
- **Participante 1:** Subrayó que cada miembro del equipo tiene respuestas para los problemas comunes y que la empresa necesita esas soluciones. También mencionó la importancia de mostrar disposición para ayudar y utilizar un lenguaje cortés como mejores prácticas para la satisfacción del cliente.

### Pulso 10:17
Se continuó la discusión sobre las mejores prácticas en atención al cliente, destacando la importancia de mostrar empatía y disposición para ayudar. Se mencionó que muchos profesionales de servicio al cliente no demuestran estas cualidades, lo que genera insatisfacción. Cherise intervino para señalar que ser directo y llegar al fondo del problema es clave para resolverlo eficientemente. También se hizo referencia a experiencias personales donde estas estrategias han funcionado bien.

**Temas:** empatía en atención al cliente · resolución directa de problemas

**Sugerencias / preguntas:**
- ¿Podrías compartir un ejemplo específico de cómo ser directo ayudó a resolver un problema complicado en tu experiencia?

**Hablantes:**
- **Cherise:** Destacó la importancia de ser directo y llegar al fondo del problema para resolverlo eficientemente. También mencionó que estas estrategias han funcionado bien en su experiencia.

### Pulso 10:22
Se continuó hablando sobre la importancia de la empatía y la disposición para ayudar en el servicio al cliente, destacando que proyectar confianza y mantener una actitud positiva son esenciales. Se mencionó que los profesionales deben escuchar primero y permitir que los clientes expliquen sus problemas antes de responder. También se enfatizó que no hay espacio para actitudes negativas en este rol, y que ser humano y tener una conversación genuina son claves para construir relaciones efectivas.

**Temas:** empatía en servicio al cliente · actitud positiva y profesionalismo

**Sugerencias / preguntas:**
- ¿Podrías profundizar en cómo proyectar confianza puede influir en la resolución de problemas del cliente?
- ¿Qué estrategias específicas recomiendas para mantener una actitud positiva en situaciones difíciles con clientes?
- ¿Cómo se puede entrenar a los equipos para escuchar primero y responder de manera efectiva?

**Hablantes:**
- **Participante 1:** Destacó la importancia de proyectar confianza, ser humano y mantener una conversación genuina en el servicio al cliente. También mencionó que escuchar primero y permitir que los clientes expliquen sus problemas es esencial para resolverlos.

### Pulso 10:28
Se introdujo una actividad práctica en la que los participantes deben escribir una carta de agradecimiento desde la perspectiva de un cliente hacia un profesional de servicio al cliente. El objetivo es reflexionar sobre cómo una interacción positiva puede mejorar el día del cliente y beneficiar la imagen de la organización. Se asignaron cinco minutos para completar esta tarea en grupos previamente establecidos. Hubo cierta confusión por parte de un participante sobre las instrucciones de la actividad.

**Temas:** actividad práctica de reflexión · impacto del servicio al cliente en la organización

**Sugerencias / preguntas:**
- Podrías preguntar si hay ejemplos específicos de cartas de agradecimiento que puedan servir como guía para los participantes que están confundidos.
- Sugiere que se compartan las cartas más destacadas al final para aprender de las mejores prácticas.
- Pregunta cómo se planea utilizar estas reflexiones en futuras capacitaciones o estrategias organizacionales.

**Hablantes:**
- **Participante 1:** Introdujo la actividad de escribir una carta de agradecimiento desde la perspectiva del cliente y explicó los objetivos de la tarea. También mencionó que los grupos ya están establecidos y que tienen cinco minutos para completarla.
- **Participante 2:** Expresó confusión sobre las instrucciones de la actividad, indicando que no estaba seguro de qué se debía hacer.

### Pulso 10:33
Se continúa con la actividad práctica de escribir una carta de agradecimiento desde la perspectiva del cliente. Un participante expresó su intención de reescribir la carta para destacar la contribución de Diego, un profesional de servicio al cliente, mencionando que es un activo para la organización y que tiene un enfoque detallado en sus soluciones. Se enfatizó la importancia de la colaboración grupal para lograr mejores resultados en la actividad.

**Temas:** actividad práctica de cartas de agradecimiento · colaboración grupal en la capacitación

**Sugerencias / preguntas:**
- ¿Podrías explicar cómo el enfoque detallado de Diego impacta en la experiencia del cliente y en los resultados de la organización?
- Sería útil explorar cómo la colaboración grupal puede mejorar la calidad de las cartas de agradecimiento en comparación con el trabajo individual.

**Hablantes:**
- **Participante 1:** Mencionó su intención de reescribir la carta para destacar las cualidades de Diego, como su enfoque detallado y su valor para la organización. También subrayó la importancia de la colaboración grupal para obtener mejores resultados.

### Pulso 10:38
Se continúa la discusión sobre la importancia del profesionalismo y la empatía en el servicio al cliente. Se mencionaron ejemplos concretos de interacciones exitosas, como una sesión de trabajo telefónica en la que se resolvieron problemas de manera eficiente y agradable, lo que generó agradecimiento por parte del cliente. También se destacó la capacidad de influir positivamente en cada llamada y la relevancia de combinar empatía extendida con disculpas para mejorar la experiencia del cliente.

**Temas:** profesionalismo en el servicio al cliente · empatía y disculpas como herramientas efectivas

**Sugerencias / preguntas:**
- ¿Podrías detallar cómo se puede entrenar al equipo para aplicar empatía extendida y disculpas de manera efectiva en situaciones difíciles?
- ¿Qué estrategias específicas se pueden implementar para garantizar que cada interacción telefónica sea positiva y productiva, como el ejemplo mencionado?

**Hablantes:**
- **Participante 1:** Destacó la importancia de influir positivamente en cada llamada y mencionó ejemplos de interacciones exitosas con clientes, incluyendo una sesión telefónica donde se resolvieron problemas de manera eficiente y agradable.
- **Participante 2:** Subrayó la relevancia de combinar empatía extendida con disculpas para mejorar la experiencia del cliente.

### Pulso 10:43
Se continúa la discusión sobre la importancia de mantener una actitud profesional, amable y asertiva en el servicio al cliente. Se enfatiza la necesidad de buscar soluciones que generen resultados beneficiosos para ambas partes (win-win). Se menciona un ejemplo práctico sobre cómo manejar solicitudes específicas de clientes, destacando la importancia de enfocarse en lo que sí se puede hacer en lugar de lo que no. También se introduce un ejercicio relacionado con la resolución de problemas, utilizando un caso hipotético sobre la búsqueda de zapatos específicos para un evento próximo.

**Temas:** actitud profesional y asertiva · soluciones win-win · manejo de solicitudes específicas

**Sugerencias / preguntas:**
- ¿Podrías explicar más sobre cómo se estructura el ejercicio para identificar soluciones posibles en casos complejos como el de los zapatos específicos?
- ¿Qué estrategias recomiendas para manejar situaciones en las que no se puede cumplir con la solicitud del cliente pero se quiere mantener una relación positiva?

**Hablantes:**
- **Participante 1:** Destacó la importancia de ser amable, profesional y asertivo, y de buscar soluciones win-win para los clientes. Mencionó un ejercicio práctico sobre cómo manejar solicitudes específicas, enfocándose en lo que se puede hacer en lugar de lo que no.

### Pulso 10:48
Se continúa con la dinámica de ejercicios grupales, donde los participantes comparten ideas y soluciones. Se menciona un concurso entre equipos, destacando la participación de Kristin y Aisha, quienes forman parte de un equipo. Se espera que otros grupos presenten sus propuestas para comparar resultados. El enfoque sigue siendo colaborativo y competitivo, incentivando la participación activa.

**Temas:** dinámica grupal · competencia entre equipos

**Sugerencias / preguntas:**
- ¿Podrías detallar cómo se evaluarán las ideas de los equipos para garantizar que todos comprendan los criterios?
- Sería útil saber si habrá una retroalimentación específica para cada grupo después de presentar sus ideas.

**Hablantes:**
- **Kristin:** Participa activamente en la dinámica grupal y levanta la mano para intervenir.
- **Aisha:** Forma parte de un equipo junto con otra persona, mostrando entusiasmo por ganar el concurso.
- **Participante 1:** Menciona la expectativa de que otros grupos presenten sus ideas para comparar resultados.

### Pulso 10:53
Se continúa con la dinámica de brainstorming, destacando que Aisha propuso la idea para la siguiente parte del ejercicio. Se menciona que las sesiones de brainstorming deben durar entre 5 y 15 minutos, enfocándose en generar ideas sin discutir cuál es la mejor, priorizando cantidad sobre calidad. Se anima a los participantes a ser valientes y compartir ideas, aunque algunos parecen dudar. Se introduce el término 'fire-horsting', aunque no queda claro su significado en el contexto. Se enfatiza la importancia de no repetir ideas y de mantener un flujo constante de propuestas.

**Temas:** brainstorming efectivo · idea de Aisha · fire-horsting

**Sugerencias / preguntas:**
- ¿Podrías aclarar qué significa 'fire-horsting' en este contexto y cómo se aplica al ejercicio?
- ¿Hay algún criterio para decidir cuándo finalizar una sesión de brainstorming si excede los 15 minutos sugeridos?
- ¿Cómo se manejarán las ideas repetidas durante el brainstorming para evitar redundancias?

**Hablantes:**
- **Aisha:** Propuso la idea para la siguiente parte del ejercicio.
- **Participante 1:** Mencionó que las sesiones de brainstorming deben durar entre 5 y 15 minutos y que deben enfocarse en cantidad sobre calidad.
- **Participante 2:** Introdujo el término 'fire-horsting', aunque no explicó su significado claramente.

### Pulso 10:58
Se enfatiza la importancia de no descalificar ideas durante las sesiones de brainstorming, ya que esto puede inhibir la participación futura de los integrantes. Se introduce el concepto de 'conocimiento del producto' como un principio clave del servicio, destacando la diferencia entre características y beneficios. Las características describen lo que el producto hace, mientras que los beneficios explican cómo impacta positivamente al cliente, como ahorrar tiempo o dinero. Se mencionan herramientas útiles para profundizar en el conocimiento del producto, como literatura, folletos, sitios web relevantes y comentarios de clientes en redes sociales.

**Temas:** brainstorming y respeto a las ideas · principio de servicio: conocimiento del producto

**Sugerencias / preguntas:**
- ¿Podrías dar un ejemplo concreto de cómo transformar una característica en un beneficio para el cliente en un contexto específico?
- ¿Qué estrategias recomiendas para fomentar la participación de quienes dudan en compartir ideas durante el brainstorming?
- ¿Cómo se podría integrar el uso de testimonios en redes sociales dentro de las capacitaciones sobre conocimiento del producto?

**Hablantes:**
- **Participante 1:** Recalcó que no se deben descalificar ideas en el brainstorming, ya que esto puede desmotivar a los participantes y limitar su contribución futura.
- **Participante 2:** Explicó el principio de conocimiento del producto, diferenciando entre características y beneficios, y sugirió herramientas como literatura y comentarios de clientes para profundizar en este conocimiento.

### Pulso 11:03
Se continúa el tema del conocimiento del producto, destacando la importancia de identificar fortalezas y áreas de mejora en este aspecto. Se sugiere revisar revistas especializadas, conversar con colegas y compartir historias de servicio al cliente como métodos para profundizar en el conocimiento. Además, se introduce el manejo de reacciones y quejas de los clientes como un nuevo tema. Se establece un receso de 11 minutos y se recuerda a los participantes apagar micrófonos y cámaras antes de salir.

**Temas:** conocimiento del producto · manejo de reacciones y quejas de clientes

**Sugerencias / preguntas:**
- ¿Podrías dar un ejemplo específico de cómo compartir historias de servicio al cliente ha ayudado a mejorar el conocimiento del producto en tu experiencia?
- ¿Qué estrategias recomiendas para manejar reacciones negativas de los clientes de manera efectiva?

**Hablantes:**
- **Participante 1:** Destacó la importancia de identificar fortalezas y áreas de mejora en el conocimiento del producto, sugiriendo revisar revistas especializadas, hablar con colegas y compartir historias de servicio al cliente. También mencionó el manejo de reacciones y quejas de los clientes como un tema relevante. Recordó apagar micrófonos y cámaras antes del receso.

### Pulso 11:13
Se retoma la reunión tras el receso y se introduce el último módulo sobre manejo de reacciones y quejas de clientes. Se cita una frase de Bill Gates que destaca la importancia de aprender de los clientes insatisfechos. Se propone una actividad en la que los participantes deben escribir tres preguntas para reflexionar sobre su desempeño en situaciones con clientes, tanto positivas como negativas. Se mencionan ejemplos de aspectos a evaluar, como actitud, atención al cliente y eficiencia.

**Temas:** manejo de reacciones y quejas de clientes · aprendizaje de clientes insatisfechos

**Sugerencias / preguntas:**
- ¿Podrías explicar cómo adaptar estas preguntas de reflexión a situaciones específicas con clientes recurrentes o de alto valor?
- ¿Qué estrategias recomiendas para manejar reacciones negativas de clientes que no están dispuestos a dialogar?

**Hablantes:**
- **Participante 1:** Retoma la reunión tras el receso y confirma que todos están presentes. Introduce el último módulo sobre manejo de reacciones y quejas de clientes. Cita una frase de Bill Gates y propone una actividad de reflexión con tres preguntas sobre el desempeño en situaciones con clientes.

### Pulso 11:18
Se continúa con el módulo sobre manejo de reacciones y quejas de clientes. Se introducen tres preguntas clave para reflexionar sobre cómo mejorar el desempeño en atención al cliente y cómo impactar en los resultados. Se menciona el método Q-tip para manejar clientes molestos y se destaca la importancia de identificar el tipo de cliente y adaptar las habilidades de servicio para mejorar la experiencia. Además, se propone una actividad en grupos para clasificar seis tipos de clientes según la frecuencia con la que se interactúa con ellos.

**Temas:** manejo de clientes molestos · clasificación de tipos de clientes

**Sugerencias / preguntas:**
- ¿Podrías explicar más sobre el método Q-tip y cómo aplicarlo en situaciones específicas con clientes molestos?
- ¿Qué criterios se deben considerar al clasificar los tipos de clientes en la actividad propuesta?

**Hablantes:**
- **Participante 1:** Introdujo tres preguntas para reflexionar sobre el desempeño en atención al cliente y cómo mejorar los resultados. Mencionó el método Q-tip para manejar clientes molestos y la importancia de adaptar las habilidades según el tipo de cliente. Propuso una actividad grupal para clasificar seis tipos de clientes según la frecuencia de interacción.

### Pulso 11:23
Se continúa la discusión sobre los tipos de clientes, específicamente se menciona al 'Cliente Experto Informado' como el primer tipo, y se propone al 'Cazador de Gangas' como el segundo. Hay cierta confusión en la interpretación de los términos y en cómo se relacionan con el perfil técnico de los participantes. Se observa un intento de clasificar los clientes según características específicas, pero no se llega a un consenso claro.

**Temas:** Clasificación de clientes · Confusión en términos y perfiles

**Sugerencias / preguntas:**
- ¿Podríamos aclarar cómo se define exactamente el 'Cliente Experto Informado' y qué características lo diferencian de otros tipos de clientes?
- ¿Qué criterios específicos estamos utilizando para determinar que el 'Cazador de Gangas' es el segundo tipo de cliente más relevante para nosotros?

**Hablantes:**
- **Participante 1:** Propone al 'Cliente Experto Informado' como el primer tipo de cliente y al 'Cazador de Gangas' como el segundo, aunque muestra dudas sobre la clasificación y los términos utilizados.

### Pulso 11:28
Se continúa la clasificación de tipos de clientes. Se mencionan seis categorías: 'Cliente Acelerador', 'Cliente con Expectativas Exageradas', 'Cliente Experto Informado', 'Cazador de Gangas', 'Cliente Socializador' y 'Cliente Precavido'. Se discute cómo cada perfil tiene diferentes prioridades, como rapidez, ahorro, conocimiento técnico, interacción social y cautela. Se observa que los ingenieros deben adaptarse a estas necesidades específicas para ofrecer soluciones efectivas.

**Temas:** clasificación de clientes · adaptación de soluciones técnicas

**Sugerencias / preguntas:**
- ¿Cómo se priorizan las necesidades de los clientes cuando hay conflicto entre rapidez y ahorro, por ejemplo entre el 'Cliente Acelerador' y el 'Cazador de Gangas'?
- ¿Qué estrategias específicas se han implementado para manejar las expectativas del 'Cliente con Expectativas Exageradas'?
- ¿Podrían dar ejemplos concretos de cómo los ingenieros han adaptado soluciones para el 'Cliente Socializador' en el pasado?

**Hablantes:**
- **Participante 1:** Propuso seis tipos de clientes, incluyendo el 'Cliente Acelerador' y el 'Cliente con Expectativas Exageradas'. Destacó la importancia de adaptar soluciones técnicas según las prioridades de cada perfil.
- **Kristen:** Mencionó que su grupo prioriza al 'Cliente Acelerador' como el más importante, seguido por el 'Cliente con Expectativas Exageradas' y el 'Cliente Experto Informado'.

### Pulso 11:34
Se amplía la discusión sobre los tipos de clientes, enfocándose en el 'Cliente Precavido'. Se menciona que este perfil puede temer cometer errores y tiende a prolongar las conversaciones con preguntas detalladas. También se aborda cómo algunos clientes tienen expectativas claras basadas en experiencias previas con productos similares. Se sugiere involucrar a los clientes en el proceso de solución mediante colaboración y brainstorming, lo que les da confianza y los hace sentir parte del proceso. Se destaca la importancia de frases tranquilizadoras como 'Estás en buenas manos' para generar confianza.

**Temas:** Cliente Precavido · Colaboración en soluciones · Frases tranquilizadoras para clientes

**Sugerencias / preguntas:**
- ¿Cómo se puede adaptar el enfoque de brainstorming y colaboración para clientes que tienen dificultades para expresar sus necesidades claramente?
- ¿Qué estrategias específicas se han probado para reducir el tiempo de conversación con clientes precavidos sin comprometer la calidad del servicio?

**Hablantes:**
- **Participante 1:** Explicó que los clientes precavidos suelen prolongar las conversaciones debido a su miedo a cometer errores y que es útil tranquilizarlos con frases como 'Estás en buenas manos'. También mencionó que involucrar a los clientes en el proceso de solución mediante brainstorming y colaboración genera confianza y los hace sentir parte del proceso.

### Pulso 11:39
Se aborda cómo manejar clientes que se sienten confundidos o abrumados. Se sugiere identificar rápidamente el problema específico y acordar una solución inmediata. También se menciona la importancia de investigar las razones detrás de la confusión del cliente para ajustar el enfoque. Se indica que habrá un video explicativo adicional para profundizar en el tema. No se profundiza en detalles específicos sobre cómo realizar esta investigación o aplicar las soluciones propuestas.

**Temas:** manejo de clientes confundidos · investigación de causas de confusión

**Sugerencias / preguntas:**
- ¿Podrías detallar cómo se realiza la investigación sobre las razones detrás de la confusión del cliente?
- ¿Qué herramientas o métodos recomiendas para identificar rápidamente el problema específico de un cliente abrumado?

**Hablantes:**
- **Participante 1:** Sugiere identificar rápidamente el problema específico del cliente confundido y acordar una solución inmediata. También menciona la importancia de investigar las razones detrás de la confusión y promete un video explicativo adicional.

### Pulso 11:44
Se continúa el tema de cómo manejar clientes que se sienten ignorados o no valorados. Se menciona que esto puede reducir su frustración y se discuten puntos clave sobre cómo defender el ego del cliente. Se pide a los participantes que elijan el mejor consejo entre los puntos discutidos, pero no se profundiza en cuáles son esos puntos ni en cómo aplicarlos. Se hace referencia a un ejemplo relacionado con la Organización Mundial de la Salud, pero no se explica su relevancia en este contexto.

**Temas:** manejo de clientes frustrados · defensa del ego del cliente

**Sugerencias / preguntas:**
- ¿Podrían aclarar cómo se relaciona el ejemplo de la Organización Mundial de la Salud con el manejo de clientes frustrados?
- Sería útil detallar cómo aplicar los puntos clave mencionados para defender el ego del cliente en situaciones específicas.

**Hablantes:**
- **Participante 1:** Mencionó que reducir la frustración del cliente pasa por hacer que se sienta valorado y respetado. También pidió elegir el mejor consejo entre los puntos discutidos.
- **Kristen:** Recibió comentarios positivos sobre su participación, pero no se especificó qué aportó exactamente.

### Pulso 11:49
Se continúa el tema de cómo manejar clientes frustrados, enfocándose en estrategias para responder a quejas. Se menciona la importancia de mantener una actitud no acusatoria y explicar las razones detrás de los retrasos en el soporte. Se hace referencia a prácticas del equipo de soporte, como marcar en el calendario los problemas recurrentes y comunicar de manera proactiva con los clientes. También se destaca que la ira de los clientes puede ser una manifestación de falta de control emocional, no necesariamente dirigida al equipo de soporte.

**Temas:** manejo de clientes frustrados · estrategias de respuesta a quejas

**Sugerencias / preguntas:**
- ¿Podríamos detallar cómo se implementa la práctica de marcar problemas recurrentes en el calendario para mejorar la comunicación con los clientes?
- ¿Qué pasos específicos recomienda el equipo de soporte para explicar los retrasos de manera efectiva y evitar malentendidos?

**Hablantes:**
- **Participante 1:** Sugirió mantener una actitud no acusatoria y explicó la importancia de comunicar las razones detrás de los retrasos en el soporte.
- **Edwin:** Mencionó la práctica de marcar problemas recurrentes en el calendario y destacó que la ira de los clientes puede no estar dirigida al equipo, sino ser una falta de control emocional.

### Pulso 11:54
Se continúa el tema de la gestión de emociones, específicamente la ira, en el contexto profesional. Se enfatiza que la ira es una emoción real que debe ser reconocida y asumida como propia, sin atribuirla a otros. Se menciona la importancia de identificar los desencadenantes personales de la ira y mantener la perspectiva, recordando que cada situación es solo un momento dentro de un día. Se hace un llamado a reflexionar sobre las circunstancias personales que pueden influir en las emociones de cada individuo.

**Temas:** gestión de la ira · perspectiva emocional en el trabajo

**Sugerencias / preguntas:**
- ¿Podrías profundizar en cómo identificar los desencadenantes de la ira en un entorno laboral específico? Esto podría ayudar a aplicar el concepto de manera más práctica.
- Sería útil explorar estrategias concretas para mantener la perspectiva en situaciones de alta presión. ¿Hay herramientas o técnicas recomendadas para esto?

**Hablantes:**
- **Participante 1:** Destacó que la ira es una emoción real que debe ser asumida como propia y no atribuida a otros. Subrayó la importancia de identificar los desencadenantes personales y mantener la perspectiva en situaciones difíciles.

### Pulso 11:59
Se continúa el tema de la gestión emocional y se introduce la importancia de desarrollar un plan de acción personal para aplicar lo aprendido en la capacitación. Se menciona la necesidad de establecer metas específicas, identificar obstáculos y contar con un compañero de responsabilidad para asegurar el progreso. También se aborda la relevancia de la actitud positiva y el fortalecimiento mental como elementos clave para el éxito. Finalmente, se hace referencia a posibles áreas de mejora en la capacitación, como inteligencia social y servicio al cliente.

**Temas:** plan de acción personal · actitud positiva y fortalecimiento mental · mejoras en capacitación: inteligencia social y servicio al cliente

**Sugerencias / preguntas:**
- ¿Podrías detallar cómo se selecciona un compañero de responsabilidad y qué criterios se deben considerar para que sea efectivo?
- Sería útil profundizar en cómo los conceptos de inteligencia social y servicio al cliente pueden integrarse en el plan de acción personal mencionado.

**Hablantes:**
- **Participante 1:** Explicó la importancia de desarrollar un plan de acción personal, incluyendo metas específicas, obstáculos y un compañero de responsabilidad. También destacó la actitud positiva y el fortalecimiento mental como claves para el éxito.
- **Participante 2:** Mencionó áreas de mejora en la capacitación, como inteligencia social y servicio al cliente, y sugirió trabajar en algunos problemas técnicos de la sesión.


---

## Reunión 2026-07-28 — Empathy in customer service · Transcripción 1/17
_chunk 1390 · 2026-07-28_

## Transcripción completa
and you were in a place and you were looking for help but nobody would even come up and talk to you. It happens from time to time and it can be really frustrating. or if you just if you end up in a call tree, their patient starts to I might say to Katie, hey, Katie, thanks for calling. Listen, I'm a little... We've got anything that we haven't covered so far. Looking for any hand to go up. They say that there is no sweeter sound to a custom and the other names that are newer to me on this call right today. He was a doctor, his name was John Young. He's a good doctor. Good afternoon John, how's it going today? and he held up his hand like that at me and I kind of Dr. Young did not go well. It's still hard for me to say John. They called you for one thing and one thing only and that's to resolve an issue or a problem. Look down number six show respect for customers time. We're going to address that in just when they are offended and we don't do a good job with them, they sometimes never come back to us. Appreciation for their business and say thank you. on one of those spectrum or somewhere in between, but I can tell you that because we've been doing so much text and so much Teams chat and so many 7, Showing Respect for a Customer's Time. 81% of US consumers feel loyal to the Just want people to help us and respect their time and leave them alone. They don't want extra and the other behaviors that we just talked about. How did you feel about it? Person Helping You. Anybody willing to share that? I was hoping that maybe there's sometimes there's a you know it's an Friendliness, Understanding and Empathy, Fairness Control, Options and Alternatives with a friendly person.

## Reunión 2026-07-28 — Empathy in customer service · Transcripción 2/17
_chunk 1391 · 2026-07-28_

They want somebody who can understand them and show them that they care about them in Consistency, Consistency, Fairness is a tough one to say, oh Service, Professionalism, Politeness, but I want to be consistent across the board because when on how you can improve the friendliness, the understanding and empathy, the fairness, control Control, Options, Alternatives, and Information. If you can get to 2, that would be great. and Start Working Together on that one. So with that said, give me one second to You'll be back with the exact same people and I'll see you within five minutes. Here we go. And there you go! Okay, so I think we are talking about I think Chris will stop me. I guess one of the most important aspects Shane, I'm not sure. No, no, we do not. I mean we need to just like fish shared basically a document and Page 8, you can see the six basic customer needs. and what we need to do over here is discuss one at least at least one or two among these six customer needs. What we think if you guys have any thoughts on this. Oh, if you'd like to share anything. I guess Fairness or Information Can be an important point. that we can improve on I mean, I think yes, information can be one because Obviously, I mean, from my perspective, I think understanding and Again, as I said, I mean, as Chris was discussing about that, right? and the other thing that goes throughout the process for that. We need to be aware of that too as well. Need everybody to share maybe just one of these See if I can see who's gonna do that Do you want to do that for me? Be brave now, come on. Alright Camilla we're gonna kick it right off with Camilla and we'll How about right there? Alright Camilla, what do you got for me? Give me one. I think this is based on on our current team is that understanding an empathy I'm wearing customer shoes is difficult by giving them proper app. and the proper updates that giving the proper expectation sometimes being an engineer.

## Reunión 2026-07-28 — Empathy in customer service · Transcripción 3/17
_chunk 1392 · 2026-07-28_

and the other one that we can work on to give them Enough information about what is happening and the other one. in the other side, what would you prefer to hear in and not keep and not keeping in the dark, just waiting for an answer for weeks or something like that. and Understanding for People. We move from one side of the desk over to their side of the desk and I understand what you're going through. I've had too many people I can only imagine what you're going through. You are showing some kind of an empathy and people want you to be and the other side. No, actually it's the same one. Understanding and Empathy to as Camila rightly said, to think from To think from customer source, we need to have the empathy with what the customer has been Satisfaction for what they are spending the time with with us and calling us. supports have their own scripts that is what we discussed in two minutes. Scripts is fine, but if you don't have the empathy you will not be able to understand and all of these things. Yes, and to deal with the added customers, sometimes it's okay if the customer if the customer is venting out, they are not venting out at you as an engineer. Engineer, they are venting out at the situation that they are sitting at. customer is at the right tone with you. They really are desperate for us and so we do have to show them those two things. The Understanding and Empathy? Yes, we decided number four. 4, that is Control, because customers need control through Clear Update. updates that we provide and the next steps that we are working on so customers want to feel Basically we are giving them status update as the next time update and giving control by Control back to the customer. Yes, definitely we have to be, yes.

## Reunión 2026-07-28 — Empathy in customer service · Transcripción 4/17
_chunk 1393 · 2026-07-28_

Absolutely, I will tell you this, Ayesha I want to give as much control as the customer needs but I I still have to direct them through the process so I can't just throw out my hands and say It kind of seems a little silly that I have to tell people to be friendly. Professional and friendly with them and I'm consistent with them the call generally goes and Fairness options and alternatives. I'm going to encourage you to write this down. I want to go back to Verage Venting. He said, let somebody vent. Event, Event is designed to do one thing and that's Release Pressure. Let's move on here if we can. We're going to look at this one here. here. This is what it means to be customer centric on the top of page nine there. on the Screen versus your Book, but it's difficult to maintain Maintain a unique or superior position in the marketplace. and other ways. Look at the one on the top right, it says expanding business with Lower left there, newer customers are more likely to switch service providers. and the last one there and Expand the business that you may be doing with them then a and a new customer. So a couple of things we want us to do here. It says it wants you to think about What would it be? How could you exceed it? What would that action could you take? and then what obstacles could get in the way. I want you just to take a minute or two and see if anybody Be right back to you. All right, anybody willing to share here? Anybody got an ID? and I do what it has to be and and Power to Exchange. Let's see what's next. We can not hear you well. We can not hear you well. Your microphone is broken I think, or Ismaic Network, Console 1 and someone confirmed, please. App1 Now, not yet Not yet, so bad Kati, is it me or is it him? It's you. You're broken up a little bit, but try talking again. and it sounds like you're... We can hear you now. Okay. Thank you very much. Anybody and even the share there. I could go. I think that's my microphone's on.

## Reunión 2026-07-28 — Empathy in customer service · Transcripción 5/17
_chunk 1394 · 2026-07-28_

When somebody's calling in with a problem or they're opening a ticket. customer such as help building a search or report. or where you can get really unique ideas. That's really helpful. That's a great reporting idea. We'll get a lot of benefit It's just our internal knowledge and it's just getting the communication out there to the community. Suppose resources can you correct me if I'm wrong? That's the way you're thinking, KT. You know, we have to realize it. All of us are better than what others do So work together and share those ideas and spread the knowledge Solid ground, we've been finished with a little long, so I'd like to have some of you here. Anybody else got anything to share? One, one. One, one. No, I think we're in the order. and Landmark study by Forum Corporation found that 70% of customers stopped doing business. You know, that's a controllable, you know, too little attention. Well, let's make sure we're communicating properly. Internal or External Customers and Clients. Is there anything that you know that you could do differently? and I'll come up with that. I don't like to call people out, so I won't make you do it. How many of you have got at least one thing written down here? It's all of a sudden a quag. and the Quiet Group. It's not my microphone, is it, Katie? I can tell you this right now, your company needs you and the solutions to the issues that we face on a regular basis regardless of the company we work for. We've got most of the answers. Somebody here on this call has got a couple of things that can share. Satisfaction, and keep them here. And as you see the third bullet point, we're going to discuss Display a willingness to help. Utilize courteous phrasing. and if you had to pick one of those and Chat box and get ready to send that to me and we'll do that on the count of three. 1, 2, 3. Send those to me if you could. If you could.

## Reunión 2026-07-28 — Empathy in customer service · Transcripción 6/17
_chunk 1395 · 2026-07-28_

Which one do you think is most important? All right, so we're getting a nice group of people here who are Give you a few more seconds. A few more seconds there. Same with Kristin. Kristin said it. Show empathy, display a willingness to help. 3 seems to be a display of willingness to help. They did call us for that reason. It never ceases to amaze me how many customer service people really don't, don't really dis... I told you earlier about those two things. for a lot of people for a high number of years. I said no, you didn't you picked a different one. I'm sorry, but but maybe we'll go with the Cherise. Cherise, why'd you pick that one? Yes, you. Yes, ma'am. Yeah, it's more to be direct actually. and try to cut through the end. Get what is the problem and we say cut to the chest TET to the chase, right? Get to the bottom line. What's going on? Yeah, very nice. Let's just talk this through. I get it. Yeah. Yeah. I really said this stuff, I really tried this stuff and for me it really worked in a They are looking for someone who can not only identify with them or understand NAU. I say, you know what? You called the right person. You called the right person. And then you could almost But I knew the right person I needed to get to or the steps that they needed to take to solve these issues and other things that we can do to help solve these issues. So that's something that we want to use to our advantage as best we can. and the Professional image that we're talking about. We're talking about what you see on the screen right there. and all those willingness to help, Cardius phrasing the show The Show and the Empathy, Project Confidence, and then Be Human and Have a Conversation and Quit taking it personally Little stinker there, where the empathy can enter. Top of page 14. Well, listen first. As a matter of fact, you can write this quote Listen first and then let them explain what happened The Brain Still Works.

## Reunión 2026-07-28 — Empathy in customer service · Transcripción 7/17
_chunk 1396 · 2026-07-28_

One there it says be upbeat and positive be in it together Ask you to answer this question. Give me a thumbs up. If you like talking to people that are positive or the negative. You don't really get a day off where you get to be in a bad mood or be rude to people. and a beat with people. I know that seems, you know, maybe elementary, but Prejudice, a little bit of bias in you. I know that as hard as I try to These are the things that we got to get our hands wrapped around. I'm going to give you about five minutes on this, a full five minutes on this. and Share their most recent, successful customer service experience Thank you, note. Yes, this is a tough one. I want you to write a thank you. Thank you, letter from that customer to the customer service professional. and Reflect on how the interaction made the customer's day better and how and how it reflected on the organization. I'm going to give you five minutes to do this. So with that said, I will let you open up those rooms again Open up those rooms again. You work with your same groups. Hopefully that makes it easier. Open it up. Open up the rooms and you're going to be there in just no time at all. I'll see you back in five minutes. I'm sorry guys, what are we supposed to do? I was looking at something and I'm looking at something else. So I am not sure. Right, I'm left out. All of us are better than one of us, so between us all, we're going to get the point. So go ahead and dig in. I will read our letter I want to re-do it I want to reach out and let you know how much I appreciate working with Diego He is an asset to your organization and Detail Orient with his solution. Professionalism through the process. I look forward to Kristin, you got it from Garage, look at that, even Aisha saying go for it Your hero today man, your hero and Accompany with the Entire World, with reviews and things like we have now.

## Reunión 2026-07-28 — Empathy in customer service · Transcripción 8/17
_chunk 1397 · 2026-07-28_

Every situation with every person that calls in for help, you can influence those calls It is under your control. It's not something that you just have to do. One other person at least, raise those hands up for me. Who's it gonna be? You're welcome Diego. as we were sharing some experiences we had lately. They were on their first day of UAT and they sent a response where they copied and and they said afterwards How appreciative they were to just get on a phone call and have a working session. where we were just kind of picking one thing at a time that we just hopped on the call. We figured We figured it out. We were pleasant. We were happy. We were upbeat. We got it all fixed. Fixed. They were happy and they said thank you very much. We very much appreciated that. I bet you were human and having a conversation with them too at the same time weren't you? or some feedback from a customer like that and things go well for you. and on page 15 Page 15. This is so cool to me. I really want you to pay attention to this. This is so It says, when it's coupled with an extended empathy Empathy and Apologies, Customers Sometimes Are Be nice, be professional, be assertive, let's jump on this and solve this problem for this person. for the clients, you have to focus on a win-win outcome like it says on the upper left. with Skillpath, and I can tell you right now, win-win, if I can do it like Right below that it says, when you brainstorm and build a long-term customer relationship as far as the creative part, but you certainly can have a great attitude. The customer request is, no matter how outlandish it is, I always say the same thing. I say I say, well, here's what I can do. Well, here's what we can do. Having what can be done versus what can't be done is a very very important thing and the exercise works like this. They need a pair of red, size 9 Converse, high top tennis shoes. Blue, and Neon Pink. Red size nines are available at another location Days, Business Days.

## Reunión 2026-07-28 — Empathy in customer service · Transcripción 9/17
_chunk 1398 · 2026-07-28_

But when is this party? Somebody tell me. When's this party? I'm listening. Be ready to share What you have come up with as far as a potential answer and here we go. and you should, there you go. There you go, there you go, right? That was an extra too. All right, I'm I called you again Do I get you back too early? Do you have enough? Enough. Let me know. Unkown. You think you're good? All right, raise those hands up for me. and all that stuff. Kristin, Kristin's got her hand up. Now we got Aisha, we got I wonder who's going to win this contest here I'm gonna win because Aisha's on my team, so it's two of us. Oh, two of you. Okay. All right. Well, Kristin. Yes. and I'm looking for those three other groups to find out what kind of ideas they had. and then I'll let Aisha go because it was actually her idea for the next part. In form first, we could also adjust to size 10. We could suggest that to the customer if they really want to Clothes to Red, maybe a dark pink or something that could I bet you did, I bet you did, there's usually a little bit of Raise that hand up. I don't want to have to start calling around. Anybody else have some? I know you got some ideas. Be brave. I hate to admit something, I kind of do. And it was a little wild. One thing I will tell you is when you're brainstorming, still one of the most effective ways 10-15 minutes. Ayesha, what did you say? and Sessions should last no more than five minutes. The brainstorming session is designed to come up with ideas, not pick the ideas and the idea not argue over which one's best, it's just to come up with just ideas. Overquality, quantity over quality. Who cares how many you get? You just want to You guys are smart, so let somebody jump in here and say, I think Firehosen is this, what is it? Oh, go ahead, dude. I don't know what is fire-horsting, but it's all like... I just don't give and repeat some some ideas on this brainstorm. I don't know.

## Reunión 2026-07-28 — Empathy in customer service · Transcripción 10/17
_chunk 1399 · 2026-07-28_

Proceso, Down the Yes Don't what, Shrees? Don't shoot down the ideas or any ideas that have been Diego could say something in my brainstorming session and then I could just go, ah, Diego. Don't put somebody down. Once you put somebody down, they will not contribute again. They sometimes come up with the best ideas. Just sharing that with you. The other thing I'll tell you... Service Principle number three product knowledge. Just a couple of things for you to look here. A lot of this is just reading, but I Product Knowledge. If you're talking to somebody else, go ahead and mute yourself just in case. I don't and the benefit of the product. So I want to kind of share this with you. It says It says a feature is what the product is or what it does. It's just simply My phone can receive calls and make calls. Service people, we sometimes get into what we call being feature rich and beneficial. and Benefit or we're really good at saying text and phone mails and emails. and any kind of, you know, it can make and receive all those kinds of things. I can use text, I can make text and receive text. I'm not patronizing you. I'm not trying to say, oh, you don't get the is that benefits generally do something for a customer. They usually save Save time, save money, make you more efficient. Literature, Product Brochures, relevant websites, maybe your own website could help. It's Impacting Me Financially in a Good Way. Customer Comments, Testimonials on Social Media. and the other one. How they position the product to their customers, if that's applicable to you, that's a good way to do it. You know where you're strong, you know what you need to strengthen in terms of product knowledge and things. Also, it tells you to review the trade magazines, talk with peers, and share customer service stories. It's all right there for you if you'd like it and I want you to read down through those and ask yourself do I know That takes us to handling customers' reactions and complaints.

## Reunión 2026-07-28 — Empathy in customer service · Transcripción 11/17
_chunk 1400 · 2026-07-28_

is that you keep your time. And I would like to see you back here. 11 minutes from right now Don't forget to kill your microphones and your cameras before you leave. and the other side of the screen. 10 minutes, right? 11 minutes. Okay. All right, I am back. and Back. Give me the thumbs up. Let me know that you're back and you're ready to go. Give me those thumbs up. Thumbs Up. Thank you, Veraj. Appreciate it. Kristin's good. Good, good. Can't go anywhere without Diego, man. Gotta have him back. There's the Rees. Good. All right. Everybody's back. Yeah. Yeah. Give me that little heart. All right, so we're into our last module and it's this one handling customer reactions. Reactions and Complaints. A little bit of work for you guys to do here, not anything that's hard. It's hard, but we'll jump right into a couple of things. You'll notice on page 18 there's a quote from Bill Gates that says Your most unhappy customers are your greatest source of learning. It's not always going to be fun, but there's always something that you can learn. I'm done with the client, no matter whether the thing went really well. at the bottom of that page, maybe up at the top in the corner. I want you to write down three questions to ask Good or bad? What did I do well? What did I do well? Well, I had a good attitude. I addressed the customer. I didn't waste time. You might list a number of things that you did well. 2nd question I always ask myself and by the way I'm going to ask myself these questions Differently next time if I have the same kind of a situation. and the other one. I might want to try something differently. So what could I do differently? and the third question is how would that affect the outcome of the call? I hope you're writing these down from a customer service person. on the very next page. on the Top of Page 19.

## Reunión 2026-07-28 — Empathy in customer service · Transcripción 12/17
_chunk 1401 · 2026-07-28_

CSR Professional, Real Customer Service Representative Professional Professional does these things does these things a real customer service? customer service professional does these things. One, they realize that the customer is upset and the Q-tip method. but I just realized the customer is upset and it is my job to make sure that gets Yes, see, Bébérage says yep. Kristin, thank you. And a number of you got your hands going up. and that's what they're looking for. The third piece there, a real customer service Service Professional identifies the customer type or their customer reaction and then tailors my customer My Customer Service Skills to Turn That Customer Experience Around. It's a lofty statement. and Types of Customer Reactions. I'm going to put you in your room. I'm going to trash all the old ones and I'm going to give you somebody new to work with. and the other one. or more. Great in those rooms now. Hopefully you get somebody different. and they are ready. Yep, they're ready. Yep, they're ready now. And here's what I'd like you to do. I'd like you to rank these. Socializer Customer, The Accelerated Customer, The Informed Customer No, 1 through 6. Which one do you get the most? Second, third, fourth, fifth, all the way down to sixth. I'm just asking you to rank those 1 through 6 on who you get the most. One second for a question here, anybody? and no questions, so here you go, rank those 1 through 6. That question is how we feel like clients or how how our clients feels with us. our clients feel with us as customers. Support, I mean. Because Chris said something like how How we feel like plants So, I don't know, someone wants to rank this Rinsor and Minkluration lives in the part of Yeah, like a client I think. I think I'm not pretty sure about that. I don't know if ArcGIS knows that, but I think and I think that as clients.

## Reunión 2026-07-28 — Empathy in customer service · Transcripción 13/17
_chunk 1402 · 2026-07-28_

I think that it could be our first one because I think that we are technical persons I think that we could be This type of client, this kind of client, you know? So yeah, I'm agree with the first one The first one is the Informered Expert Customer I think that the second one could be or Gang Hunter maybe There it is. Yep. Because I think that we're... Let me stop you stop ready you're saying OK, so that's number one. What's number two? The very game Hunter customer. Arginator? Yeah. So they want it cheaper Cheaper, Faster, that kind of thing. That's number two. We are technical people, so we So we are engineers, so the phrase is be an expert solution Solutions, and Tech environment. 1 could be a better game because we are looking for money, saving money, you know? Oh, boy. Hey, your customers are too, you know, so yeah. Yeah. Yeah, the third could be the overly cautious Yeah, it's technical. You want it as cheap as they possibly The number 4 will be the Exaggerate Expert The first will be the Accelerate customer Customer, and the last one will be the Socializer customer. Step up here. Yes, Kristen, what do you got? Okay, our group, the Accelerator Accelerated Customer is our number one. 2 is the Exaggerated Expectation customer. So, interesting. OK, keep going. and our number three is the informed expert. Okay, so the other one would be the bargain hunter the Socializer, and the Apprisions and the last group. Fast resolution to be quick and they want to write straightaway answers. 3rd was the same informed expert customer, so already knows what exactly Expect their knowledge also. That's why we need to work together to find the best time. Assurance before we make any decisions or we need to be patient Socializer customer and the bargain hunters because they They definitely like to talk a lot. They might go off topic apart from the The Bargain Hunter at the end.

## Reunión 2026-07-28 — Empathy in customer service · Transcripción 14/17
_chunk 1403 · 2026-07-28_

and that also plays into the overly cautious customer because some customers and then you have like th They know they want something, right? But they're afraid of making a mistake sometimes. List question spirals into our hours of conversation because they are so We do have a lot of customers who have been through these different products before and they definitely have an idea and expectation of what they think. You kind of just slide it to accelerated bargain hunter and the socializer. and Move Directly into Brainstorming, Questioning and Solution Finding to Show Earth Brainstorming and Collaboration lets them be a part of the solution process. and I'm going to work with me and collaborate so we can come up with the right solution for you. And almost everybody's like, well, yeah, that's why I called. I used to come up with phrases like, listen, I know this is scary, but you're in good hands right now. and other things that could possibly work with these and then verify that and test that out. and the same types. There's just only so many different behavioral types. So keep this handy for yourself. There we go. Yeah, there we go. This is called customer complaints and a solution-oriented on each one of those. For the person that's over confused and overwhelmed, see if you can agree on what and you should be moved there very quickly. Go! I'm going to show you how to do it in the next video. I'll be back soon Seses, but the karaoke The Kirokin and Stappe everyone. So just like a sershing or for making a search about why our customer is over is overwhelming or confused and on some issue. OK, so we must We must review other ones now. I don't want to speak more So, you will say that about it and I think and I think that is it's good. Okay. Thank you. Alright, you're all back. It is all. Let's do this together. Somebody raised their hand. Just jump in, unmute yourself and tell me which one you picked. Pretty good, very good, Kristen. Oh, absolutely. gas on a fire.

## Reunión 2026-07-28 — Empathy in customer service · Transcripción 15/17
_chunk 1404 · 2026-07-28_

It seems like rather basic information that we just shared there with you. there with you, but you'r Yes, so what we discussed was customer feels ignored or not valued and Respected, which often reduces their frustration. and so which of those bullet points you think was the best piece of advice there. Yeah, probably ignore that and the World Health Organization. 3, which one you think is the best weapon on defending their ego. I know somebody's got an answer here. What do you think is the best answer for that one? We said number one. Rest in saying number one, maintain a non-accusatory attitude use factor out, right? You need to w You had to deal with Kristin, no wonder you had a problem there, you know, we don't want to throw Kristin under the bus. and the same time we do want to kind of own up to it. You know, Kristen, I'd like to thank you for laughing at least. and let's come up with a better solution, a quicker solution and one that works for you as quickly as possible. We in the support team, we used to take tickets that and explain why his trouble or his ticket ticket is hapies taking more time of expect and he and the like that, yes, try to communicate the why is taking so and Home we as support team, please Point 2, Arrive this problem. So try to have a conversation or a Be closer to the climbing, so on this way they are going to be like Explain why it's delayed. And then like Edwin, I believe Edwin said this. for a Client, mark it on your calendar, even if when that shows up We're kind of practicing a little bit complaint responses and strategies. I would encourage everybody in their group to 20, 19, 20. Keep those handy for yourself. Those are two great pages Anger is just a person who is not in control of their emotions, but they may not be angry at you. and the US on a fire. Anger is bad and unsafe. Anger is just real. Own it. Own it. No one else is responsible for your anger. That's the second time I've said it.

## Reunión 2026-07-28 — Empathy in customer service · Transcripción 16/17
_chunk 1405 · 2026-07-28_

Recognize and Identify What Triggers Anger. I know what sets me off. and I can tell you I bit my tongue, I grit my teeth a little bit and I'm telling you right off. Professionals, and I want to do the best thing for my organization. It says get perspective, this is just one situation on one day of the day One Day Out of Many. I'm going to ask you guys to do me a favor. I just want to know. Give me the thumbs up saying that there's stuff going on in your life that nobody knows about like and all that, but make sure you take care of yourself and make sure you get that good attitude that you need. and the last one there it says remember that the next shift I'm going to make it as positive as I possibly can. You'll notice one thing. and you'll notice that in the back of your book, you got an action plan. and Working Sheet there. And I just want to kind of walk you through this real quick. It says for how you put into practice what you've learned during this train. And since we develop specific steps Day, but there's no more important job. So you got to develop yourself. You got to ask yourself those questions. and how you'll use these skills in this training to move in the right direction. So that I'm a little bit, got my, you know, feet underneath me a little bit more, I've got the strength in the mentality. and Mentality to do it. So that's just giving an example there also. and the Psychology Professor, Isaac. and Perceived Efforts, so when I'm successful, I will feel this way. Across the Isle, my one's just down the street, somebody's on my team, whatever. Usually if you have set goals you've got an accountability partner, but always have an accountability partner. 1. The third one is perceived effort, list any potential obstacles and the ways you plan to overcome them. I'm going to try to do this, but I know if I do this.

## Reunión 2026-07-28 — Empathy in customer service · Transcripción 17/17
_chunk 1406 · 2026-07-28_

Reun 2014 accountability and it's just simply a little path for you to go through so that you can figure out what steps you need Apps you need to take and where you are and how you can complete them in the next 30 days. Alright, I got a question for you. and we have an okay day. Was this session okay and fascinating for you? Maybe it's a frown. I don't know. I'll give a thumbs up from a couple of you. Thank you. I appreciate that. We can maybe get some of those bugs worked out, I'm not going to make excuses. Just maybe get a few of those bugs worked out. and the other ones. AR, Social Intelligence, and a little more customer service training would be good for everybody in the community. Gaming, and say, and cut down the card. Yeah, I didn't see how you were doing. Just look, I did not. Okay, well then you just step with me then.
