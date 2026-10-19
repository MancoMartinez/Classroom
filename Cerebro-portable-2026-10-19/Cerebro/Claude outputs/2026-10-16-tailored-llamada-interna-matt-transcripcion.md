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
[02:27] loaded into the teams table for SSO plus and that is supposed to be replicated into
[02:35] the security level table as well.
[02:40] Right, Dan.
[02:40] What you're saying right here, just so we can send this to them,
[02:42] which is what's supposed to be in the file,
[02:45] what's the requirement to be in the file for this to work at all,
[02:48] and how it's supposed to work.
[02:50] So that way, I don't want to miss anything in translation here.
[02:53] Okay. I can put that together.
[02:55] Do you have access to the files?
[02:57] They're sending us some new files, if that counts.
[03:02] So who on our team can actually pull up
[03:07] and look at the files that they are sending
[03:09] so that we can see what is going on.
[03:19] You have access to that?
[03:20] Yeah.
[03:23] Cause that's one of the biggest things,
[03:25] I don't have access to it.
[03:26] I can't see the files.
[03:27] All I can do is,
[03:31] is there a credit card?
[03:34] I don't have access to it.
[03:35] I don't get data.
[03:37] I do not have access to anything data load
[03:40] for relates interesting.
[03:43] And that's, just goes back.
[03:45] Just for me.
[03:47] I'd like to understand whether an explicit file
[03:50] will change that outcome or still hit the same assignment step for the security ID?
[04:00] So I don't entirely know how that portion happens, where it takes it from the teams and replicates
[04:20] that across.
[04:25] That was done so that the client would not have to make changes on their side, which
[04:30] I feel...
[04:31] Well, that's also where I was kind of scratching at with them,
[04:38] modifying the location file that the customer is saying, if there's a better
[04:43] way for us to do this, that makes this easier for you, just tell us what that is.
[04:46] And we'll see if we can do it.
[04:48] Because that was the conversation that I had with them.
[04:50] I brought it to delivery.
[04:51] They said, no, they're doing it their way.
[04:53] They took over the process and do it the way I wanted to.
[04:56] If you want the truth.
[04:57] Well, that fucking sucks.
[05:00] Um, but.
[05:02] Yeah.
[05:02] they decided to take the existing file replicated across.
[05:06] So we are relying on one that file that they said for teams being correct.
[05:11] I'm never changing anything in security level.
[05:14] And the client doesn't really know what's being said there because
[05:18] no one's had a conversation with the client to really walk through the process
[05:21] and explain what it is that we're doing and why there's this whole thing in place.
[05:25] I didn't even know who could have that conversation map other than a person delivery that may or may not be here still.
[05:31] I agree. Let me see if I can find the, you know, even be something that's in, doesn't
[05:50] look like it's even in Hatr.
[05:51] At least the reference data back load is running.
[06:31] Let me just share my screen here for a second.
[06:41] Look, brand's client IDF and last time anything's been inserted into here was the 15th.
[07:49] So most of these look like their location managers. I assume that location managers.
[08:20] I have a question about this. For example, for Ritual, level 5 was already NSSO before
[08:37] her account was created. But that Fierce and Zyne left her security ID blank while the
[08:44] groups and the team were added.
[08:47] Christine also had a blank account level.
[08:50] Even through, she had an old and persistent assignment.
[08:55] Do you think these have relation when the engineering ticket
[08:59] covers both case or should we look at the existing user
[09:02] case separately?
[09:05] Because yeah.
[09:06] I mean, we should really look at both of them.
[09:08] If it's something where the first time login is not
[09:11] picking up the value.
[09:14] then yeah, that would be something that engineering should be picking up.
[09:19] If this is something where it's just, you know, if the data is there, it should be picked
[09:24] up and then it would be an engineering ticket.
[09:29] If the data is not there, yeah, if the data is not there, then obviously we wouldn't
[09:48] be able to assign, but if the data is there and it's not getting picked up, then
[09:55] we need to investigate to see if it's going down a different route,
[10:00] creating a user versus second login or something like that.
[10:06] Then it could be just as simple as fixing that.
[10:14] Then how many sounds from what they were saying in the call that
[10:17] doesn't seem to work the first time,
[10:19] second login works for some crazy reason?
[10:22] Okay. Based on that,
[10:26] I would say that's probably where our issue is.
[10:32] I think we have a ticket for this one over in
[10:34] Shann's bucket to be doled out.
[10:38] Okay.
[10:39] Come on. Do me a favor.
[10:41] Take the tickets that we have open,
[10:44] keep in mind the ones we spun off for
[10:46] the new versions of what the problem is,
[10:48] and just put the RCS link and what it's
[10:51] about for the three or four tickets in this chat,
[10:54] just so we have a record of this.
[10:56] Okay, sure.
[10:58] And there is one more thing, at least that I, one might have more, there's at least one more thing from my perspective that they said is the most important to them.
[11:06] So I don't know, maybe you should have led with that.
[11:08] I have a feeling I know where it goes.
[11:11] They're saying that the system continues to perform incredibly slow for them.
[11:17] 30 minutes or so before they can take actions and sometimes and it's making it so that sometimes it's taken so long
[11:25] We've heard this with other customers. They get timed out while they're waiting on the action to complete
[11:30] So we we have a ticket for this that we just spun off from another ticket because they were complaining about it and
[11:38] The ticket about the user IDs
[11:40] So we spun it off so that we could track and maintain it on our own
[11:43] what information do you need us to get in that ticket?
[11:47] Because I committed to the customer,
[11:48] we were at least gonna get it over into the queue,
[11:50] or engineering will review it today.
[11:52] And I wanna make sure we have everything you need in that.
[11:57] Okay.
[11:59] I guess, is there any,
[12:03] or have they got any errors that have come up
[12:08] other than just the standard,
[12:11] you know, whatever 502 I would assume,
[12:14] are they getting 502 errors,
[12:15] or is it just latency?
[12:19] Come on, did you hear about any errors?
[12:20] I think it's just latency.
[12:22] That's all they said on the call.
[12:24] Okay.
[12:26] Is it happening just everywhere
[12:30] or are there particular areas
[12:32] that they seem to find the issue?
[12:36] So here's the ticket for that one.
[12:41] Say, slowness in Izenda.
[12:44] What is Izenda?
[12:46] Izenda is the reporting tool.
[12:50] It's a third party reporting tool.
[12:54] So they're saying slow, oh, there are errors,
[12:56] slow load times, timeouts and server side errors.
[13:00] And the errors, they have screenshots or numbers, no numbers.
[13:05] Is it specific to Izenda
[13:09] or is it the incident app itself?
[13:16] Bouncing ball into the ticket it came from.
[13:19] Yeah, because this I mean this ticket itself appears to be I think it's a sender not
[13:28] Was that it's and a it's a tender
[13:31] Is that the only huh?
[13:33] So here's here's one where they started talking about it as well
[13:42] You can see he says reports are loading for him, but the overall application is too slow
[13:54] And then we asked if he's seeing errors and he gave us error occurred on the server side press okay to read the page
[14:01] to cancel to leave it as it is.
[14:05] And then same thing, he got that a few different times.
[14:09] And that's with reporting loading,
[14:10] specifically for open investigations.
[14:20] We close this as a duplicate and then we open the new ticket
[14:23] off of it, we should have probably just reopened
[14:25] this fucking one and unbroken the duplicate,
[14:28] but it is what it is.
[14:35] And then yeah, he's getting time out as a curb,
[14:37] the cloud flare error as well,
[14:40] which I thought had a number on it,
[14:42] but I don't see a number on this one.
[14:43] Oh, there it is, error code 524, I need classes.
[14:53] So he's getting 524s, slowness, across the platform,
[14:57] while leveraging Izenda reports,
[14:59] especially with open incidents.
[15:01] So Matt, just let us know what information
[15:03] you need us to gather, and then we'll work
[15:05] with the customer today, gather all the information,
[15:08] and then we'll get the ticket over to Shan.
[15:12] Okay, I mean, there's some pretty good screenshots
[15:15] here if we're concentrating on Izenda only because it looks like all of this is centered around Izenda
[15:25] then you know we can I think we really have a lot of the information.
[15:32] All right let's just get this one over to Shan then put it waiting for engineering aside to Shan
[15:37] and just make sure she knows that this one is hot you know put a comment in there that this is a
[15:42] a high priority for the customer to get resolved
[15:46] so that she can hopefully get it ever soon.
[15:48] Yes.
[15:49] And one of the things that I've noticed
[15:51] just being on their system as we've been on the call,
[15:55] just getting into incident itself,
[15:59] for Taylor brand specifically,
[16:00] seems to take a lot longer than any other client.
[16:04] You should get on a call with Ahold
[16:07] and maybe it'll all be fixed after this,
[16:10] I did numerous calls without logging into incident and it took forever.
[16:16] Logging in, opening investigations and then sometimes it would work okay.
[16:20] But literally he went to open an investigation while we were on a call.
[16:23] I sat there waiting for 20 minutes for it to open.
[16:26] It didn't open and he's like, yeah, sometimes we wait an hour and it loads.
[16:30] Sometimes we wait an hour and we have to refresh.
[16:33] And I was like, I'm sorry, what?
[16:34] And he just acted like this is normal.
[16:36] He's like, yeah, we're just starting to deal with it.
[16:38] it. So maybe your SSO stuff is going to fix that, Matt, but I was like, what the fuck
[16:43] in my mind? And I said something to rip about it because I had a call with him right afterwards.
[16:46] I was like, is this how slow it is? And he said that, yes, it is very slow. And as we
[16:52] get people through unification into the new platform, it'll be much faster. But I'm
[16:58] probably missing a connection in my brain because I'll hold went through unification.
[17:02] So I thought it would be faster for them.
[17:09] I mean, you should never be waiting 20 minutes for anything
[17:16] in my opinion.
[17:16] Once we get on this call with them on Lunar React,
[17:20] did we set the call?
[17:21] No, Jim's supposed to tell me his some times.
[17:23] Jim's going to tell me times for a call.
[17:25] Once he gets back to me with that mat, if we have time,
[17:27] let's just have him show us a couple things there.
[17:29] Or let's just watch while he's clicking around and stuff
[17:31] and see what it does.
[17:33] I just feel like this is normal.
[17:35] I was thinking in my head, I would have fired us.
[17:38] If it takes 45 minutes to open a single click,
[17:41] that does not work for me.
[17:43] I know I'm seeing I go in on a regular basis
[17:49] with just random clients.
[17:51] And for whatever reason, I am seeing Tailored Brands just
[17:54] going a lot slower than other clients.
[17:58] That's good though.
[18:00] Go in that.
[18:01] We can see it.
[18:02] So then we can hopefully isolate the issue there
[18:05] and fix it. Yeah. Okay. All right. So you're going to write up the bit for the security ID stuff so
[18:14] that we can explain to them how this works. Again, I still feel like there's an opportunity here to
[18:19] undo what delivery did to some level if it's not a huge fucking project, I see you shaking your heads
[18:24] and never mind. You want to fight that one you can but I don't mean working with delivery.
[18:30] I just mean if we can tell the customer add A, B and C into your fucking file and then we
[18:35] We can do something on that.
[18:36] I can do that.
[18:37] If it's more complex than that, no.
[18:39] Just tell me how it works and we'll work with the customer
[18:41] and we'll get them to do whatever they're going to do.
[18:46] The decision was made to keep the customer
[18:48] completely out of it.
[18:50] So, if there any now.
[18:52] Anything that we would do at this point,
[18:55] we would be redoing everything
[18:57] that we already did to get to this point.
[18:59] Okay, then never mind.
[19:00] If it's redoing the entire fucking implementation,
[19:03] we're not doing that.
[19:04] Yeah.
[19:05] In the future, I don't know how much weight I'll be able to give you Matt, but you can
[19:14] start pulling me into these conversations because I'm the one that's going to inherit
[19:17] the bag of shit that delivery is passing over.
[19:21] And I'm more than happy to let them know what I'm going to do when there's problems
[19:24] on it so that we're not surprised.
[19:27] Yeah.
[19:28] So yeah.
[19:29] I will keep that in mind if we can bring something in to deal with it.
[19:37] with that. But I mean, awesome. Is it support that owns the
[19:44] data load? It kind of goes back to that question that I know I've
[19:46] asked you multiple times is who this is. This is where I'm
[19:50] getting the answer in almost real time that the answer is
[19:54] delivery sets it up initially. And then support manages
[19:59] everything that happens after that. As long as it's not
[20:02] something that's long and complex. In other words, like
[20:04] this, if we have to go back and redo the entire
[20:06] implementation? No shot. Think about it like one or two hours worth of work. If it's one or two
[20:11] hours worth of work to unwind what was wound up, cut the string and fix it? Yes, we'll own it. If it
[20:17] goes beyond that, we're either going to call out to engineering or we're going to call out to
[20:21] delivery if they egregiously buck something up. Okay, we're going to go back to the customer
[20:26] and say, hey, yes, and we're going to fix it because you customer let us down the wrong
[20:31] on Primrose path in the beginning.
[20:33] And now we need to undo all this stuff,
[20:36] which is the other option we're going for.
[20:38] But yeah, we're at the center of that target,
[20:40] which makes it even more incentive for me
[20:43] to make sure it's done right.
[20:44] And I'm going to an offsite next week
[20:46] with Kara and Kim, who's the new head of professional services,
[20:50] which is over to the right implementation
[20:52] and the new customer success leader
[20:55] is joining us out there as well.
[20:56] So it'll be a good opportunity for me
[20:59] to talk about this stuff, is my point.
[21:01] should be good because yeah like we just I mean we just need to be on the same
[21:05] page so there's a lot of not on the same page so agreed
[21:11] agreed all right yeah I'll write that up I'll just put it in this chat that way
[21:16] you've both got it and it's from my knowledge of what it is supposed to do
[21:24] so I'm going to use that caveat that's all I can hope for my friend and
[21:30] Second question for you totally unrelated to all this and then I want to ask any questions.
[21:35] Normally when I used to want documentation done pretty much every company.
[21:41] It's public facing I went to product management and product management had a tech writing function and they worked with tech writing to publish those things.
[21:49] And I would go to the product manager that's over the particular product.
[21:53] But if it's something that goes across all of our products, I would go to like Paul,
[21:56] the head of product management and say, make this happen for everybody.
[22:00] Is that how we work here? Like for that shit that I need for the browser support,
[22:04] do I need to go to Paul? I would say, yeah, either Paul or Amy,
[22:11] one or the other. But yeah, that's that's where we need to be going.
[22:15] Amy's going to get products and that's why I hate calling to product managers, right?
[22:19] She's not going to get whatever Carly manages.
[22:22] I'd rather go if it's going to be all the products,
[22:25] I'd rather go to the top and say, take your shit.
[22:27] Yeah.
[22:29] I mean, technically, something like that,
[22:30] browsers should be the same thing across the board
[22:33] for all products.
[22:34] I would, I agree.
[22:37] But they need to publish it for all products, though.
[22:39] You know what I mean?
[22:40] That's where.
[22:41] All right, cool.
[22:42] I'm going to PM.
[22:45] You'll probably be putting a lineup for something like that,
[22:48] because I know they're currently trying to get a tech writer and other things.
[22:54] But I know tech writers too, but I don't want to pay the price.
[22:58] Because I know good tech writers.
[23:02] I would love to have one of them on staff.
[23:04] We could use it. That's it.
[23:06] Oh, yeah, I believe it.
[23:08] It's the pain in the ass to do.
[23:12] Yeah, because you've got to be like an engineering and project manager
[23:15] like all at the same time.
[23:16] You have to understand the information you're getting
[23:18] and then be able to make it comprehensible for customers.
[23:21] Yeah.
[23:22] Paul, any questions for Tailored Brands, for Matt?
[23:26] No.
[23:30] Maybe one.
[23:30] But I see something the Colton shows today
[23:37] and the location site.
[23:39] For example, Chris came through as 9000, et cetera.
[23:44] And Colton confirmed that it's 4000, yes?
[23:49] is the right location for him.
[23:51] The fight they showed has you in the brand column.
[23:55] And Ryan said this looks, Ryan Barlow,
[23:59] said it looks like we had the nine,
[24:01] but he didn't recommend just changing into four.
[24:06] Yes, how are these office and DC locations supposed
[24:10] to work or should they have their own location
[24:15] or map to an existing brand location,
[24:19] where can we check the Q-Rain is no time rule?
[24:21] I don't know if you know something about this
[24:25] because I see nine and the client side is four
[24:28] and maybe this affects something.
[24:33] Yeah, do we know?
[24:35] So the numbers for,
[24:40] I would assume both incident and secure
[24:43] should come from a feed on the client.
[24:53] And then the claim should really match those numbers.
[24:57] But I know historically on the incidents side,
[25:02] do you know, is the store number prefixed with nine
[25:07] on the incident side or on the secure side?
[25:09] probably means that they would have been created manually in incident.
[25:29] So if they're created manually in incident, I mean, they're not in a location feed.
[25:41] Ryan is probably the one that would know that data feed the best and where the data
[25:47] is coming in.
[25:49] Yeah, ultimately, Incident has had the ability to create locations manually.
[25:57] So if a client or somebody has gone in and created that location manually, it's not going
[26:03] to line up with what's in the feed.
[26:07] If the claim always shows the 400, and that's what it should have, is the 400 prefix in
[26:19] Incident as well, or is it only the 900?
[26:26] only 900, 9000.
[26:33] Do you have a specific store number?
[26:35] Yeah, yeah, yeah.
[26:41] I put in the chat, please.
[26:43] Customer meeting in one minute,
[26:50] so I'm gonna have to drop here.
[26:53] Urban outfitters, is that incident?
[26:56] I don't think it is.
[26:58] I have not gone to unification.
[27:06] So I don't see that 9000 in incidents.
[27:14] I see the 4,000 in the incident.
[27:16] I don't see the 9000 in the incident.
[27:21] Thanks guys.
[27:22] Thanks, Jair.
[27:26] Let me just share with you.
[27:30] So I'm in Tailored Brands.
[27:35] That's right.
[27:36] Well, maybe I'm bad.
[27:38] Maybe it's insecure.
[27:39] I'm not sure.
[27:40] I forget this one.
[27:42] So then we can't see the database anymore.
[28:06] So we have the screen shared.
[28:09] Let's see anything in the place.location with this 4000,
[28:29] or with the 9005, or,
[28:45] so I can see the 4000 locations in here,
[28:48] but I cannot see.
[29:03] For example, if you see that this is all
[29:07] that location hierarchy members for Chris Orth,
[29:11] you can see the 9000 to 2005 settings so what was the name let me put in this one
[29:39] I'm not sure I think that you use this query I don't know if you can run in the
[30:02] database here is this ah yes I am but I only see it in the SAO is is a sorry
[30:20] is a oh feet table okay so that yeah would be coming from the SSO file from
[30:32] the client and so are they saying this is the correct value no the correct
[30:41] value it's four okay it's four thousand that's what he has on his actual account
[30:47] is four but yeah from a from an SSO standpoint this is what is being sent in
[31:00] on the feed which I actually think that this here is that it's just showing up
[31:14] Let me see.
[31:36] Because for Chris, I need to add this manually because they don't have the store location
[31:43] hierarchy assigned.
[31:45] I add yesterday this number 2005 MW, etc.
[31:52] I need to add manually yesterday.
[31:57] So he's got two locations right now.
[32:00] One is for the 4000, one is for the 9000.
[32:05] So the 4000 I would assume is the one that, did you insert that one manually or is that
[32:13] Yeah, I insert one only.
[32:19] So that's the top one is the 4000 one and then this one especially based on the fact
[32:26] that the persistent is set to false.
[32:30] This is likely in the feed that is being sent over.
[32:43] Okay.
[32:44] Because this whole SSO plus is a table that gets populated by Tailored Brands, sorry by feed
[32:51] the same way.
[32:53] Okay.
[32:54] Yeah, where that one's coming from.
[33:40] We need to see the original file in order to understand this.
[33:45] Okay.
[33:46] Okay, the one thing that I would say is we don't actually validate any
[33:55] Validate to see whether that location exists or not when it goes into this table
[34:00] So they can send it over but that doesn't necessarily mean that
[34:05] You should exist so
[34:15] issue on their side
[34:18] Okay, okay, got it
[34:31] anything
[34:32] Else that we wanted to look at here with Tailored Brands
[34:36] No, not really.
[34:40] Yeah, this is definitely slower than other places, so there's got to be something going
[34:47] on there that's causing an issue.
[34:49] Okay.
[34:50] All right, we'll see what we can figure out there.
[34:55] So you're coming into the office on Monday next week?
[35:01] Ah, yes.
[35:03] I entered today that you come to Bogota Monday, yes?
[35:09] You stay all week or just some a week?
[35:12] Yeah, yeah, I'll be there all week.
[35:14] Oh, good.
[35:15] So myself and Gina and one other QA team member as well.
[35:23] So the three of us stay on for the week.
[35:27] So yeah, we could meet people in person and actually, you know, get some real face
[35:33] time.
[35:34] So looking forward to it.
[35:36] Yes.
[35:37] Yes.
[35:38] Okay, Matt. Thanks for your help on all things and I hope...
[35:42] ...or your travel and your stay here in Colombia will be good.
[35:48] And you can enjoy work and enjoy this city and country.
[35:54] Thanks, Fla. We'll talk to you later.
[35:59] See you.
