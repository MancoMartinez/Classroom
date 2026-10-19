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
propio metodo: le pide a Claude que le explique el ticket, y si no entiende
acude a Juan. Te nombro como "my guru". Eso, mas alla de lo simpatico, te ubica
como la referencia tecnica del grupo, y es consistente con que el banco de frases
de arriba lo termines liderando tu.

La segunda, un criterio para las notas internas que vale la pena adoptar: antes
de escribir un bloque grande, preguntate si a ti te serviria recibirlo. Si tu
fueras quien recibe ese ticket de otra persona, esa nota te da informacion util.
Si la respuesta es no, no la escribas.

Tambien pregunto por el plan de tener una skill de soporte. JR respondio que se
reune con Matt la semana entrante para empezar AI Ops, que la posicion de Matt no
arranca hasta el 15 de septiembre y que trabaja desde Inglaterra, y que va a
conectar a Camila con el para que armen las skills y se compartan con el equipo.

## Anuncios operativos

Sobre trabajo de delivery. Se hizo mucho ultimamente y parte salio mal, y JR
aclaro que en varias de esas no fue culpa del equipo, que hubo cosas de la
conversion de snowtime que rompieron el sistema sin estar documentadas. Delivery
armo un equipo nuevo bajo alguien llamado David, con contratistas nuevos. Carl
esta proponiendo que por los proximos seis meses el equipo no haga nada de
delivery: se evalua, se da un assessment, y se manda al equipo de David.

Ojo con esto, porque es lo mas facil de malinterpretar. Todavia no aplica. Viraj
pregunto si ya hay que mandarselo a David y JR dijo que no, textual, que se sigue
el proceso actual. Falta que Carl consiga la firma de Kim, la nueva VP de
professional services, y de Rip, el jefe de JR.

Sobre documentacion. Va a salir un proceso con una cuota mensual de articulos por
persona. El criterio que dio: si descubres que hay que ir a cierto lugar para
conseguir algo y no existe documento que lo diga, escribelo.

Sobre recursos internos. Antes de preguntarle al cliente hay que agotar lo
interno, ingenieria, reproduccion del issue, copias viejas de la data, recibos
guardados. Textual: no hay nada que moleste mas a un cliente que hacerle perder
el tiempo, y que prefiere que te regane por preguntar mucho internamente a que le
preguntes al cliente algo que se podia resolver en casa.

Sobre turnos. El equipo de India se corre una hora mas tarde a partir del 21 de
septiembre, con lo que el solape con Estados Unidos y Colombia pasa de cuatro a
cinco horas. Camila lo anuncia en el canal.

## Transcripcion completa

Sin diarizacion, whisper no separa hablantes. El nombre Viraj sale mal
transcrito varias veces como payment, Baraj y Varad. Quan es Juan. Copile es
Copilot. Shreya en el minuto 13 es dudoso. Eco alrededor del minuto 10 no se
pudo resolver, puede ser un sistema o un cliente.

```
00:00:00  examples. Raj, you use Claude, I'm guessing, for your customer facing updates. Am I correct or incorrect?
00:00:07  I use Copile.
00:00:10  Okay, great. Your customer facing updates are great. I can tell they're written by AI only because I know how you write and I read the writing that you send in these customer facing updates.
00:00:28  I love your customer facing updates. They do the right job of taking the technical down a little bit of using all the flowery customer service language that you want to use. They sound good. I like them.
00:00:41  Quan, I'm going to guess that you then use Claude for your customer facing updates, which is okay, right? But I don't like some of the things that happen in your customer facing updates.
00:00:52  I'm not trying to pick on either one of you by this, by the way. I'm talking to you guys because I understand English is a second language for everybody on this call except for me.
00:01:04  And that sometimes the customer service bend is hard to get when you're doing it through a translation.
00:01:09  So, and I'm going to give some examples. And again, Quan, don't feel picked on here. I'm only saying this because I've seen this a number of times in your tickets.
00:01:13  Your tickets will commonly say things like, I don't need anything else from you. I need nothing from you or phrases like that, which probably translate in a way that sounds okay.
00:01:26  But when you're actually doing, especially for Americans and like Western Europeans, when you're doing customer service for them, you have to put flowery words around these things.
00:01:37  Like, I appreciate everything that you've given me so far. I don't think I need anything else yet. I'll come back to you soon. And I'll let you know if I need more.
00:01:49  Now, this is simple for us to train our AI agents on, but we have to train them. So my Claude MD rules have a ton of rules for me about the things that irritate me when it writes so that it pulls those things out.
00:02:01  And you guys should not only be doing the same thing, you should be doing this with your teams.
00:02:07  It goes beyond that though. Like if we take a look, I'm going to show you guys a few tickets here.
00:02:13  I wish you would have used me. I love to hear feedback like that. Do you use AI, Viraj?
00:02:23  Uh, I do use AI and I use Claude, and sometimes I use co-pilot.
00:02:30  I've already talked to you before about saying, I don't need anything from you in tickets. So, but I didn't assume that was Claude that was saying that because it was just a sentence.
00:02:40  Didn't I say go away? If I said go away, it was definitely me, not Claude.
00:02:44  I don't need anything from you. Go away. Get lost.
00:02:50  All right. So let's take a look at this ticket from Louis right now. Now, again, I'm not picking on anybody here. I recognize everybody's doing what they're told to do.
00:02:59  I recognize that Louis here is new to the organization, and he's trying to pick these things up as he goes.
00:03:04  So you've got a ticket. Customer comes in. Louis is working with them. This is a good reply, right? No problem here. This is a good reply.
00:03:10  The way that he's asking the questions here, this is very good. Customer servicey, all great. So I have no problems so far with his customer service answers.
00:03:20  But then you get up to areas like this, and this is, I recognize from Claude, and I recognize that he's asking it to give him this information. But this big of a dump, this is, it is exactly that.
00:03:34  It is a dump that we're taking in the ticket. It's too much information that is in many times useless.
00:03:40  I'm not giving you this feedback solely for me. I've got a couple other issues that I'll show you.
00:03:46  Many times developers look at this when we escalate it, and they read it, and they come back and they say, this is AI slop. The answer here is wrong.
00:04:00  And it has way too much extraneous information that doesn't matter at all. So what we need to do, we need to remember that AI is a tool. It is not always right.
00:04:07  So two angles for me. The first angle is, we need to get some rules together, like an MD file or something similar, a skill that we can share with the entire team about how to get Claude, if we're going to use Claude, to give us good customer service answers.
00:04:26  Or we can choose that we're going to use CoPilot for our customer service answers. Because again, I really like Viraj's CoPilot answers. Either way, I don't care.
00:04:32  Let's figure out a way that works. Let's test it. And let's share it with the entire team.
00:04:37  But the second thing though is, you cannot trust this shit. This is, think about this like a junior engineer that's triaging things for you.
00:04:50  Maybe they were really good at their other company, but they don't understand how our different tools connect together. They don't understand all the intricacies that aren't written down. They only understand the documentation that they're provided.
00:04:59  So I'm not saying don't use this. I'm saying do it, look at it, run it on your own, check it, and then put a comment in the ticket that is worthwhile.
00:05:14  Like Claude told me it thinks this is the root cause. I checked this, this, and this. This is what I think. Can someone else please evaluate this for me and give me your thoughts?
00:05:19  This week, I've had three different engineers that have come to me and said, you guys are killing me with this stuff. And they've given me three different example tickets of this.
00:05:28  And again, I fully recognize many people in this company, Dan Endersby, are saying just use Claude. Claude will give you all the answers. Well, we've proven again and again that it's wrong.
00:05:44  And so we need to double check the answers that it's giving us. We need to check our resources and we should use it as an initial starting point, right?
00:05:49  This is a place for us to walk from and then figure out what we want to figure out. Yes, Camila?
00:05:52  I have one comment and one question.
00:05:56  Yes, Camila.
00:05:56  The comment is like, I think, and it's general. Like, we're so relying on AI that we don't question it at all.
00:06:06  So we just decide, because we are not experts on something, AI is giving us like the right answer.
00:06:15  Me, because I'm not a really technical person. I mean, I have a technical background, but I haven't been on technical things for a while now. And there is a lot of things that I don't know indeed.
00:06:27  And sometimes I came with a ticket. I go to AI and I said to Claude and say, hey, explain to me what is this? Why is this product when I came in?
00:06:39  And if I do not understand, I go to Juan always. Like Juan, my guru in Appriss, help me. Like, I don't know what this means. I don't know exactly why they are referring to.
00:06:47  Because for me, in my understanding, this should be to engineering, but it is not like I'm confused.
00:06:54  Questioning, I think it's something that we need to start doing. And I'm reinforcing that to my team.
00:07:00  It's taking a while because it's tough because of the volume that we have. So they want to get rid of tickets as soon as possible.
00:07:13  And also to be mindful, if you are the one receiving that ticket, is something like that big note, internal note, something that you want to get phase two, is something that is useful for you, if you are the one receiving that ticket from someone else.
00:07:25  It's giving you the right information. It's giving you useful information. So that is also something that we need to standardize.
00:07:36  And my question is that I know that we have a plan with Matt to have skills, to have a support skill that is based on, so we can rely more on what Claude is giving us.
00:07:48  That's a good point. That's a good point. So Camila, I think this would be a good one. I'm meeting with Matt finally next week to start talking about AI Ops.
00:08:01  His position doesn't start until September 15th and he works in England. So I have to be careful not to make him an AI Ops guy until September 15th fully.
00:08:13  So next week, I'm meeting with him on AI Ops for the first time. I'm going to connect him to you behind the scenes so you guys can work out these skills and we can share it with the team.
00:08:23  All right, we got seven minutes and I have a hard stop. I want to bang through a few more things, guys. I'm sorry. Any updates you guys have, you can write them down.
00:08:28  Not questions, but any updates about things you have going on, write them down in the chat and we'll look at them async.
00:08:38  This is another example and I've seen many, many times this exact thing has happened. I brought one up yesterday. I know I raked Lewis over the coals a little bit in front of you, Juan and Camila, because I've seen him do it a couple times.
00:08:48  Where we come out to a customer and we say like, Hey, we identified two different issues here. Like there's two different errors.
00:08:52  But by the way, when engineering got involved in this, they're like, there's not two different errors. Actually, there's like a configuration issue here, maybe, but there's probably not a defect at all.
00:09:08  So this is where we go back to. We have to be really, really careful what we're telling customers, because now we've set the expectation to this customer that they're going to get two different defects fixed when there might be none.
00:09:18  As a matter of fact, we might have to charge this customer because they want a change request done, you know? So that's where this can lead us down a really bad path.
00:09:27  And I see it happening more with the new people, no question, but it happens with all of us. I mean, it tries to do it to me too, from time to time, for the record. It tells me crazy shit.
00:09:37  And then I dig deeper into it. I do what Camila's doing. I tell it, explain this to me, explain that to me. I question it. And then it's like, ah, yeah, I was wrong. I was wrong. Sorry.
00:09:46  So we just have to be more mindful. This is another example. We're not going to go deep into this one. It's an Edwin ticket, same kind of thing.
00:09:52  First, huge bits of troubleshooting that are incorrect. Second, telling the customer things that are incorrect based on the Claude troubleshooting that was done.
00:10:02  We got to validate these things. It should give us an idea. We test it. We look at it. We look at the code. It does not take away our autonomy. So please help me. Please help me with the teams on these.
00:10:14  The second thing that I wanted to talk to you guys about was checking all of our resources for eco. So eco, we can't have gotten everything that I wanted to get in eco.
00:10:30  As a matter of fact, I've got Rip building something to give us a little bit more, but the point here is we shouldn't be just, just like AI, we shouldn't be telling the customer, this is how it is. We need you to do this. We need you to do that.
00:10:42  Until we've checked all of our internal resources, check with engineering and see if they've got a way that we can reproduce the issue, check with engineering and see if maybe we've got an older copy of the data, check and see if we hold receipts that we can look at how things looked in the past.
00:10:56  Don't always rely on the customer to answer every question. I know that in support, it is an easy method to look at a queue of 30 tickets and say, all right, I'm going to fire questions off to 20 of these tickets and I'm going to wait for those customers to get back and then I'm going to troubleshoot this issue.
00:11:12  And that's okay many times, but first be 100% sure we can't get that answer internally because there's nothing that pisses a customer off more than wasting their time.
00:11:20  And when they know we've got that data and we're asking them the question, we're wasting their time. So just always try to reinforce with the team, check internally, check internally.
00:11:31  I'd rather you get yelled at because you're asking too many questions than ask the customer the wrong thing that we should have been able to solve on our own.
00:11:35  And people will get better at this over time, right? You'll start to figure out your resources. You'll start to document them. That's the other thing everybody needs to start doing.
00:11:43  If you find out we go to a certain place to get a thing and you can't find a document that says that, write a document.
00:11:48  We're going to roll out a process soon where there's going to be a certain amount of articles that are required every month by everybody. So this will be good things to start writing down and start creating documents on.
00:12:04  Final thing I want to talk about is delivery work. So we've done a lot of delivery type work lately and some of it has fucked up.
00:12:10  And in many areas where it's fucked up, it's actually not been our fault. As crazy as that is to say, there were things that happened between the snowtime conversion that we didn't realize that broke things in the system.
00:12:20  And we made a change and it broke a whole bunch of other stuff, but none of it was documented. We have no way to know that these things were happening.
00:12:31  So in delivery, they've actually started a new team under this guy named David. And I believe they're also new contractors. So you guys might know some of these folks whose whole job is to do this type of work.
00:12:41  So what Carl is talking about right now with Kim and Chris, my boss, Rip, is maybe for the next six months, we don't do any delivery work.
00:12:50  When we get a customer who wants to change something, like they want something to work differently, we look at it, we give an assessment about what it would need to be. And then we send it over to David's team.
00:13:01  And then they're the ones that do the work and get it up and running. And then after six months or so, then they're going to come back to us and say, okay, so here's the types of tickets that you guys can work on that we want you working on. Here's the way to do it.
00:13:15  And then for everything else, you send it to us and we determine, are we charging the customer or are we just going to do it for free out of our team?
00:13:19  Go ahead, Viraj. You're on mute again, Viraj.
00:13:28  I think he hung up. He tried to raise his hand and he hung up.
00:13:32  I'm done. He's done.
00:13:37  All right, team. I'm sorry. I didn't intend to take the entire meeting. Shreya said some good things for us to talk about, which took a little bit more time than I anticipated.
00:13:48  We got one, two minutes. Any last questions, comments, concerns?
00:13:52  There's a lot to talk about, but not enough time.
00:13:57  All right. Well, async, if you guys want to type anything in this chat, if you want to take it to the support management chat, wherever you guys want to talk about it, let's talk about it. I appreciate the work everybody's doing.
00:14:06  I want to announce one thing is that we're going to have moving India team one hour later, so they have more time to work with US and Colombia folks.
00:14:22  So the coverage for on-call will be not four hours, but five hours. So that is going to take place on the 21st of September, but I'm going to make the announcement in the channel.
00:14:36  So everybody knows, and that is a line in the on-call shift, but just to let you know that we will have our India folks for one more hour to work with them.
00:14:43  Perfect. Thanks, Camila. Viraj, you had something? You want to drop it real quick before we leave?
00:14:51  Right, but not all of them.
00:14:52  Yeah, good question. Current delivery tickets are sent to Carl, and it has to be David?
00:14:58  Nope, we're not sending. Follow the process you've been following right now.
00:15:04  What I was telling you is a process that Carl is working on, that once he gets approval from Kim, who's the new VP of professional services, my peer in professional services, who's his boss, and from my boss, Rip, once he gets those two to sign off on it, then we'll roll that process out.
00:15:23  But I'm just giving you guys a little bit of visibility that soon we're going to stop working on any of those delivery tickets.
00:15:26  Okay, sure, thanks. I mean, thank you.
00:15:30  Yeah, exactly. I told him, he told me like I was going to be sad about it. I was like, oh no, take work from me. How bad?
00:15:39  So anyway, all right, thanks team. Happy Friday.
00:15:39  They're creating a data ops under Carl, essentially.
00:15:42  Yeah, sure. That's what they're doing, which is fine, as long as, good luck.
00:15:47  Right, exactly. Exactly. All right, thanks team.
00:15:53  Have a good day, everybody.
00:15:53  Thanks everybody. Bye, happy weekend.
00:15:56  Good weekend. Good weekend. Good weekend.
```

## Zonas dudosas

Minuto 10:14 y 10:25, la palabra que suena "eco" no se resolvio. Por el contexto
es un recurso interno de datos, pero hay que confirmarlo.
Minuto 13:41, "Shreya said some good things" es dudoso, puede ser otro nombre.
Minuto 15:39, "data ops under Carl" se oye entrecortado.
