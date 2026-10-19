# Reunion interna de revision del tracker de Ahold, 10 sep 2026

Grabacion: `JR & Matt review ahold.m4a`, 6 min 57 s, ingles, tres participantes.
Transcrita en local con whisper.cpp large-v3-turbo. El audio no salio de la Mac.

## Que es esta reunion

Repaso interno, previo a la llamada con el cliente, del archivo de seguimiento
que se le presenta a ADUSA. Se recorre ticket por ticket marcando lo completado
y se acuerda que Juan actualiza el archivo en vivo mientras avanzan.

## Decisiones que se tomaron

Uno. El archivo bueno es el que se le ha venido presentando al cliente. Hay
demasiadas versiones circulando y es facil abrir la equivocada. La version que
manda es la del que se reune con el cliente, y no cambia hasta que el cliente
pida otra cosa.

Dos. No se agregan al tracker todos los tickets que Juan viene sumando, y es a
proposito. El tracker es la lista corta que el cliente pidio atacar, no el
inventario completo. Si el cliente quiere sumar tickets, se suman en la llamada.

Tres. No se despliega en viernes. Textual: hot fixes para P1 si, veinticuatro
siete. Fuera de eso, no. El criterio que se dio es que si hay caida y no se
puede entrar al sistema, eso es hot fix, y eso es otra cosa distinta a un
despliegue programado. El fix del store shop, que ya esta en pruebas, se
pospone a principios de la semana siguiente.

## Formato acordado para el tracker

Las filas completadas se pintan de verde claro, con relleno de celda. El verde
se deja incluso en las que ya venian marcadas, para no perder de vista cuales
eran criticas. Son dos columnas las que Juan actualiza. Las notas las escribe
directamente el que dirige la revision. Las columnas de accion se ocultan
durante la presentacion.

## Tarea pendiente para Juan

Antes de la reunion con Jim, revisar la lista propia y los correos de Jim, y
detectar cuales tickets Jim marco como realmente importantes. El criterio es
estricto: no vale que Jim pregunte por un ticket ni que reporte uno nuevo, tiene
que ser uno donde Jim insista en que es importante. Esos se suman al tracker.
Lo demas se espera a que Jim lo pida en la llamada.

## Estado ticket por ticket

Los numeros se transcribieron de audio y varios se dijeron incompletos o
entrecortados. Los marcados como inciertos hay que confirmarlos contra el
archivo real antes de usarlos.

| Referencia en audio | Tema | Estado que se dio |
|---|---|---|
| 093, incierto | primera fila de la lista | completado, pintar verde |
| sin numero | upload attachments | ya marcado, se pinta verde igual por critico |
| 242, incierto | no se nombro | completado |
| RCS-28667 | SSO | en progreso, sin causa raiz todavia, se estaba investigando durante la reunion |
| RCS-28123 | no se nombro | completado |
| RCS-28693 | SSO | bajo investigacion, ligado a 28667 |
| sin numero | adding additional associate to case | el fix se conoce y es facil, aun sin completar, del lado nuestro funciona |
| sin numero | duplicated view | completado |
| sin numero | store shop | reincidente, el de los apostrofes, fix en pruebas, despliegue a principios de la semana siguiente |

Sobre SSO se dijo, textual, que todos los temas de SSO que tiene el cliente
estan ligados entre si. Eso conecta con el mapa de cuatro capas de SSO que ya
esta en investigaciones.

Sobre store shop se menciono que Shan si creo un ticket de ingenieria. La
palabra se oye como "inch ticket" en el audio, casi seguro ENG.

## Transcripcion completa

Sin diarizacion. Whisper no separa hablantes, asi que no se atribuye cada linea
a una persona. Solo es seguro que a Juan se le habla en segunda persona.

```
00:00:00  The red ones are the ones that we can stop having to call, but let's go through each one.
00:00:06  So this one's completed.
00:00:07  Great.
00:00:10  Juan, can you please update the tracker as I go with some of my notes here?
00:00:15  So the first one, 093 here, is completed.
00:00:19  Let's just mark this as completed and maybe color this for the ones that are completed.
00:00:26  We'll do like a light green.
00:00:28  Okay.
00:00:28  It's the fill, fill like this.
00:00:34  Okay.
00:00:35  So that way we can easily see that this is completed and we have the call.
00:00:39  So these are the two columns that you need to update for those.
00:00:42  And then I'll type in any notes that we might have.
00:00:45  Okay. Sure.
00:00:47  I'm just going to hide these columns right now for all of the action of these columns.
00:00:53  And then one, hide. There we go.
00:00:56  Cool, cool, cool. All right.
00:00:57  So yeah, just make these.
00:01:01  Did I just fuck it up? Oh, there we go. Okay.
00:01:04  Make those two.
00:01:05  Is this the file from the last call that we had with them here?
00:01:08  Mm-hmm.
00:01:09  I'm just making sure because I was looking at the one that Juan said last night.
00:01:13  I'm like, there's a lot of stuff that does not line up here.
00:01:16  Yeah, all good. You know, we're going to keep presenting on this file.
00:01:19  This is the file we've shown them.
00:01:21  And if he wants to add extra tickets, we'll add extra tickets.
00:01:24  But candidly, I'm not adding all the tickets that Juan is adding in here on purpose.
00:01:29  No, because it's the ones that you want to start for.
00:01:32  Yep.
00:01:32  Same thing on this one, upload attachments.
00:01:36  This one has been marked. There we go. That one's already good.
00:01:40  So I'm going to mark this over here green.
00:01:45  because I wanted to still denote that this was one of the ones that was, like, critical for that.
00:01:50  Um, 242 here.
00:01:56  Fuck yes. Do my favor.
00:01:58  I'll mark this one completed as well, Juan.
00:02:04  Probably good if you do these as we go, Juan. I don't know.
00:02:08  If you have the... Do you need the link?
00:02:09  Here's the link.
00:02:10  Yeah, please.
00:02:13  Because I see you don't work around it.
00:02:14  Too many versions of this file, man. It's so easy to get onto the wrong one.
00:02:19  I'm using Matt's version. That's the one that I've been using, uh, since the beginning.
00:02:25  And since it's the one I meet with the customer on, it's the one I'm going to keep using until they tell me otherwise.
00:02:28  Okay. Um, all right.
00:02:30  Next up, we've got 28667.
00:02:35  Under-engineer.
00:02:37  This one's, this one is something with SSO.
00:02:40  I'm actually trying to troubleshoot this one right now.
00:02:44  If I happen to get any kind of an update before the call, we'll have that.
00:02:47  But as of right now, it's in progress.
00:02:50  Okay. So you're still looking for root cause on this one?
00:02:53  Yeah.
00:02:54  Okay. Leave that alone, though.
00:02:57  28123.
00:02:59  Fuck yes. Another completed.
00:03:05  Let's go do it there. Let's go do it here.
00:03:09  So you can work. This one completed as well, Juan.
00:03:12  Uh, 28693. Let me just grab this.
00:03:16  That exact same thing.
00:03:17  Yeah, SSO. SSO.
00:03:20  Thur. All of the SSO things they have are, um, tied in together.
00:03:28  Okay, so this one. Got it. Under investigation.
00:03:35  Nine, ten, twenty, twenty-six.
00:03:39  Under investigation.
00:03:42  Most likely tied to, what was the other one?
00:03:46  Um, one, twenty-three. Was that it, or was it?
00:03:51  Not one, twenty-three. It's one, I think, above that.
00:03:56  Uh, two, eight, six, six, seven.
00:03:59  Yep, that sounds right.
00:04:01  Okay. Cool.
00:04:06  Got this bad boy. Adding additional associate to case.
00:04:15  Um, it's, I know what the fix is. It's an easy fix.
00:04:20  We just haven't completed it yet.
00:04:22  So it's, it works on our side.
00:04:27  Okay. Uh, uh, nine, ten, nine, ten, ten. Uh, sex.
00:04:45  Okay. Cool.
00:04:49  Great. Duplicated view. Completed.
00:05:06  Store shop. This is the one that keeps fucking coming back.
00:05:08  It had the apostrophes in it last time.
00:05:11  Um, Shan did indeed create an inch ticket.
00:05:15  I've got a fix for this in testing right now.
00:05:18  Um, so early next week, considering it is Thursday today.
00:05:23  I don't want it to play tomorrow.
00:05:24  I don't want you to deploy tomorrow either.
00:05:28  I'm glad we agree on that.
00:05:31  I'm sure you've had many other people that are like, yeah, fuck it. Deploy Friday, Saturday, Sunday.
00:05:35  That does not work for me.
00:05:37  Yep. I've worked in mission critical environments.
00:05:39  In mission critical environments, it is what it is.
00:05:41  If you're saving somebody's life, if you're saving somebody's company, we do what we got to do.
00:05:46  But that is not this.
00:05:48  Like, if there's an outage and you physically cannot log into the system or do anything, sure, we'll fix it.
00:05:55  That's a hot fix, though, to me.
00:05:56  You know, hot fixes for P1s, sure, 24-7.
00:06:01  But outside of that, no.
00:06:05  Okay, uh, Juan, based on your list, do you think there's any that Jim is going to want us to add here that he's been hot on?
00:06:13  Okay.
00:06:15  And you don't need to answer that question in a second, but we are meeting with Jim soon.
00:06:21  So, take a look through this list, look at his emails, and see if there's any tickets that he said, this one's really important.
00:06:28  Not just asking a question about it or saying there's a new ticket, but ones that he's stressing are important.
00:06:34  If so, let's add those to the list.
00:06:36  Otherwise, we'll wait for him to say, hey, I want this one on the list.
00:06:39  Okay. Thank you. Okay?
00:06:42  Yeah.
00:06:44  All right. Gentlemen, thank you for your time.
00:06:48  And, uh, I'll see you guys on call soon.
00:06:51  All right, sounds good. See you.
00:06:53  Thanks, guys. Bye.
```

## Zonas dudosas del audio

En 00:03:35 y 00:04:27 se dictan secuencias de digitos sueltos que whisper
convirtio a palabras, "nine, ten, twenty, twenty-six" y "nine, ten, nine, ten,
ten". Son numeros de ticket leidos en voz alta y no se pueden reconstruir con
confianza. Hay que sacarlos del archivo real.

En 00:03:20 se oye "Thur", probablemente el arranque cortado de un nombre.
En 00:04:27 el "uh, sex" es casi seguro "six" mal transcrito.
