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
> oh, voilà, here is the error. And then error log with the explanation expanded."

**Y los ejemplos concretos que usaste van adentro.** Si reprodujiste con un caso específico,
ese número va en el ticket.

### 5. El Ray ID cuando hay Cloudflare

> "Whenever there is a Cloudflare one, which Matt might have already told you, the Ray ID is
> very important. I am not a Cloudflare person, but I heard Matt a million times asking for
> Ray IDs."

---

## Disecar la descripción del cliente, frase por frase

Esta es la instrucción de método, y es la que más trabajo cuesta adoptar.

> "The reproduction steps, trying to get every sentence that they have in their description
> should be dissected in a way that like, oh, they said something about this, but they did
> not give us any information about that. That piece has to be dissected and ask the
> customer: what do you mean by an audit? Can you please present us a number? Can you please
> present us a screenshot? Stuff like that."

Y el porqué:

> "Because we can dive immediately to the database or to that page and look at for ourselves,
> rather than 'oh, this edit is working, I wonder what it has' kind of situation."

**Cada sustantivo vago en el reporte del cliente es una pregunta pendiente.** "Una
auditoría", "un caso", "un reporte", "un usuario". Ninguno de esos sirve sin un número.

---

## El protocolo, en el orden en que hay que ejecutarlo

Destilado de todo lo anterior. Esto es lo que se vuelve regla del equipo.

**Al recibir el ticket**

1. Lee la descripción completa y subraya cada sustantivo sin identificador.
2. Responde tomando el ticket **y** pidiendo en el mismo mensaje lo que falta: número de
   caso o auditoría, captura, URL.
3. No esperes la respuesta para empezar. Investiga en paralelo con lo que tengas.

**Al reproducir**

4. Reproduce tú en producción. No delegues el trabajo pesado al cliente.
5. Captura la URL de cada paso.
6. Cuando salga el error, **expande el technical explanation** y copia el log. O sácalo del
   Control Panel, Error Logs. Es el mismo log.
7. Si hay Cloudflare de por medio, captura el Ray ID.

**Al escalar a ingeniería**

8. URL de sign in y ruta de navegación, en pasos cortos.
9. Los identificadores concretos que usaste para reproducir.
10. El log expandido, no la captura del mensaje genérico.
11. Capturas de cada punto relevante.
12. Client ID al inicio del comentario interno.

---

## Su oferta al equipo

No es retórica. Lo dijo dos veces y fue específica.

> "If you want to set up anything commonly, like anybody, I am open. I thought there will be
> more people on this meeting. Feel free if you guys want to throw something on the calendar
> all together and we can discuss in depth."

> "My calendar is your calendar, Juan. Add anything, anytime. And we can catch up and discuss
> and maybe learn from each other. There is obviously so many things I have to learn from you
> guys too."

**Acción: agendar una sesión con el equipo completo, Colombia e India.** Ella esperaba más
gente en esta llamada.

---

## Lo que dijo del equipo, y hay que compartirlo tal cual

Esto se lee en la reunión de equipo. Sin editar.

> "Juan, you're amazing to work with. You have been doing great. Even in the retro meeting
> this morning, Matt and I, we were talking about how support has been amazing. You guys just
> jumped into a burning building. So, which I wouldn't want for myself, but you guys came
> running into a burning building and took up on the work, and I'm sure you guys spent more
> than the required hours doing the deployment craziness."

> "But hey, it was very nice because we all really didn't have time to introduce and slowly
> get back in touch. We were like, hey Juan, do this, do that, can you please help me with
> this thing? So we all jumped directly at each other and got the work done. We got our hands
> dirty too. So that's nice. So we survived the storm, I should say, and you guys have been
> doing amazingly well. I really like the support team."

Matt Kamminga y Kiran hablaron del equipo en la retro de esa misma mañana. La lectura de
ingeniería sobre soporte en estas semanas es buena.

---

## Las tres frases que resumen todo

1. **"Throw it back to them."** El ticket incompleto se devuelve el primer minuto, no el
   tercer día.
2. **"I don't want to sit and dig for it."** El log expandido llega hecho, no se busca.
3. **"URL is most important."** Sin URL, ingeniería no sabe qué consulta corre la página.

---

Conocimiento técnico de la misma reunión: `inbox/2026-08-28-KT-reunion-kiran.md`
