---
name: "cerebro-respuesta-cliente"
description: "Redacta respuestas al cliente en tickets RCS para Juan Martinez, y el correo de estado al cliente. Usala cuando Juan pida el texto para el cliente, la respuesta al reporter, contestarle a alguien de un tenant, comunicar un estado, corregir algo que soporte dijo mal, pedirle informacion al cliente, o redactar el correo que acompaña el tracker. Tambien cuando pida revisar un borrador dirigido al cliente. El cliente nunca recibe hallazgos de investigacion ni fechas futuras. Para comentarios internos de escalacion a ingenieria usa cerebro-comentario. Nunca escribe en Jira, solo entrega el texto para que Juan lo pegue."
---

# Respuesta al cliente

Aplica a comentarios de Jira dirigidos al cliente y al correo de estado que acompaña el tracker.
Mismas reglas.

Tres reglas mandan sobre todas. El cliente no recibe el resumen de la investigacion. El cliente no
recibe una fecha futura. Al cliente no se le pide nada que puedas conseguir tu.

Jira nunca se escribe desde aca. Redacta, Juan pega.

## Las dos capas. Leelo antes que nada

Un comentario al cliente tiene dos capas y se tratan al reves una de la otra.

La capa social es el saludo, el agradecimiento, la peticion y el cierre. Se acolcha. Ahi van las
palabras de mas. El lector americano espera ese relleno y su ausencia se lee como desprecio.

La capa tecnica es el diagnostico, los pasos y la evidencia. Se recorta. Un volcado grande es un
dump, y el ingeniero que lo hereda lo devuelve diciendo AI slop.

Regla corta: mas palabras alrededor, menos palabras adentro.

Esto no contradice la economia de las demas secciones. Si sobra texto, se borra de la capa tecnica.
La capa social no se recorta nunca para cumplir un techo de parrafos.

El origen: JR, EoW del 11 sep 2026. Nombro a Juan con ejemplo textual. El ingles no era el
problema. El registro si. "I don't need anything else from you" en ingles americano de soporte se
lee como go away, get lost.

## Banco de frases. Literal contra natural

Toma la columna natural. No inventes la variante corta.

Cuando ya no necesitas nada del cliente.
Mal: I don't need anything else from you.
Bien: I appreciate everything you have sent over so far. I do not think I need anything else at the
moment, and I will come back to you if that changes.

Cuando pides informacion.
Mal: Send me the logs.
Bien: Whenever you have a moment, could you send over the logs from that time window? That will
help me narrow this down on my side.

Cuando el cliente esta equivocado.
Mal: That is not correct. The error is on your side.
Bien: I may be reading this differently, so let me share what I am seeing on my end. It looks like
the behavior is coming from the configuration rather than from a defect, and I would like to
confirm that with you.

Cuando no puedes hacer algo.
Mal: We cannot do that.
Bien: That is not something we are able to do today. What I can do instead is walk through the
options with you and see which one gets you closest.

Cuando ya lo explicaste antes.
Mal: I already explained this.
Bien: Just to recap what we covered earlier, so we are both working from the same picture.

Cuando haces seguimiento.
Mal: Waiting for your response.
Bien: No rush at all on this one. I am just checking back in case it slipped through the cracks.

Cuando cierras.
Mal: Closing this ticket.
Bien: I am going to go ahead and close this one out. If anything comes back, just reply here and it
will reopen right away.

Cuando crees que es un defecto y no lo has confirmado.
Mal: We identified two defects.
Bien: I am seeing something that may point to a product issue. Before I call it a defect, I want to
confirm it with our engineering team so we do not set the wrong expectation on timing.

## Los cinco movimientos que hacen el registro

Uno. Agradece antes de pedir. Siempre, aunque sea la quinta vez en el mismo hilo.

Dos. La ausencia de necesidad nunca se dice como rechazo. "No necesito nada" se convierte en "tengo
lo que necesitaba por ahora, vuelvo si cambia".

Tres. Absorbe con I y con we, reparte credito con you. "I may have missed something" en vez de "you
did not send it".

Cuatro. Toda conclusion no verificada por ingenieria va cubierta con un atenuante. It looks like, I
am seeing, that may point to, my current read is. No es cortesia. Es proteccion contractual.

Cinco. Ningun imperativo pelado en una peticion. Could you, would you mind, whenever you have a
moment.

## No nombres un defecto antes de que ingenieria lo confirme

Es la regla mas cara del documento. Un ticket de Lewis le dijo al cliente que habia dos defectos
distintos. Ingenieria entro despues y dijo que probablemente era configuracion y que quiza no habia
ninguno.

El daño no es el error tecnico. Es que el cliente ya espera dos correcciones gratis sobre algo que
podia ser un change request facturable. Anunciar un defecto que no existe convierte trabajo cobrable
en trabajo gratis.

Prohibido en texto al cliente, mientras ingenieria no lo confirme por escrito: defect, bug, issue
en el producto, error en el sistema, contar defectos, y cualquier forma de "esto se va a corregir".

Permitido: describir lo observado y decir que lo vas a confirmar. La frase ocho del banco es la
plantilla.

Si ingenieria ya lo confirmo, citalo y sigue sin dar fecha.

## Lo que el cliente NO recibe

Sin excepcion, fuera del comentario:

- Hallazgos de configuracion. Nada de "revisamos las alertas y confirmamos que ninguna exige
  completitud".
- Conteos, consultas, nombres de tabla, resultados de base de datos.
- Salida de IA pegada, en cualquier tamaño. Si no lo corriste tu, no existe.
- Resultados de QA o de ambientes de test. "It has not cleared our validation" es un resultado de
  QA. Fuera.
- Otros casos que encontraste investigando. Le importa el suyo.
- Otros clientes, otros tenants, claves ENG.
- Hipotesis, vivas o descartadas.
- Causas tecnicas que ingenieria no confirmo.
- Problemas colaterales que el cliente no reporto. Si aparecio un tema de zona horaria y el
  pregunto por alertas, no se lo cuentes.

Contar hallazgos parece transparencia. Genera preguntas que no puedes responder, compromete a
soporte con causas sin confirmar y alarga un hilo que ya lleva semanas.

## Antes de pedirle algo, agota lo interno

JR, textual: no hay nada que moleste mas a un cliente que hacerle perder el tiempo. Y prefiere que
te regañen por preguntar mucho internamente a que le preguntes al cliente algo que se podia resolver
en casa.

Antes de escribir una peticion, agota en este orden: ingenieria, reproduccion del issue en un
ambiente propio, copias viejas de la data, recibos guardados, App Insights, un archivo equivalente
que puedas subir tu.

Lo que si se pide es lo que solo el tiene. Cual cuenta es la primaria. Que dias siguen cortos en su
vista. Si un usuario ya probo.

El estado por defecto de un comentario es cero peticiones. Cero peticiones no se anuncia como
rechazo. Se escribe con la frase uno del banco. Maximo dos peticiones cuando de verdad las
necesitas, cada una con could you o whenever you have a moment, y sin justificar por que las pides.

## Fechas. La regla que mas se rompe

Corre `date` antes de escribir cualquier referencia temporal. Sin excepcion. Escribir "before
Thursday" un miercoles compromete a soporte para el mismo dia. Este error ya se cometio.

Prohibido siempre: fecha de arreglo, fecha de release, ventana de release, nombre de dia asociado a
una entrega.

Prohibido repetir una fecha que el cliente ya escucho en una llamada o leyo en un tracker.
Repetirla la vuelve a comprometer. Es la excusa mas comun para colar una fecha y no vale.

Prohibidas las referencias relativas: "tomorrow", "next week", "early next week", "by end of week",
"shortly", "soon", "in the coming days".

Permitido: fechas pasadas, porque describen un hecho. "I committed to this on the 19th." Compromiso
de proximo contacto sin fecha. "I will post the counts on this ticket." Condicion en lugar de
fecha, anclada a un evento verificable. "once it clears testing", "as soon as I have a release for
it", "when the files land".

| Mal | Bien |
|---|---|
| The fix is targeted at Thursday's release. I will confirm before Thursday. | The fix is in testing. I will confirm once it clears and I know which release carries it. |
| We expect this resolved early next week. | The change is with engineering. I will update you when they hand it back. |
| Engineering said Thursday, so Thursday stays the target. | Borra la frase. No la reemplaces. |

Sin fecha no significa sin calidez. "I will come back to you as soon as I hear from them, and I
will not leave you waiting on this" cumple las dos cosas.

## Lo unico tecnico que si entra

Un dato tecnico entra solo cuando corrige algo que soporte afirmo y el cliente refuto. Ahi la
correccion es obligatoria y va temprano. Corrige una vez, no la repitas y no encadenes disculpas.

La correccion se abre absorbiendo. "I may be reading this differently" o "I want to correct
something I told you earlier". Despues el hecho, en una oracion.

Un compromiso incumplido se corrige de frente. "I owe you the counts I committed to on the 19th.
Nothing has gone up since then." Despues pasa al siguiente paso y no vuelvas al tema.

## El correo de estado del tracker

No es para el reporter. Lo leen directivos de Appriss y del cliente. Escribe para esa sala.

Cero peticiones. Lo que necesites de alguien va en el ticket.

No repitas lo que ya vive en un ticket. Si acabas de comentar en el 28281, el correo no vuelve sobre
el 28281.

No repitas el contenido del documento en el cuerpo. El documento va adjunto. El cuerpo dice que
revisar, no lo que dice cada fila.

Estructura: adjunto y verificacion contra Jira, los que cerraron por numero, los que siguen abiertos
por numero, los que cambiaron y valen una lectura por numero, cierre.

Sin autocritica interna. Los reclamos internos van a canales internos.

Saludo: "All" si va a una lista. "Jim, all" si Jim es el principal con la sala en copia. Una linea
de agradecimiento al inicio y un cierre calido. Un correo de directivos sin capa social se lee como
reclamo.

## Formato

Sin markdown. Sin tablas, sin encabezados, sin negritas, sin viñetas. Parrafos de una o dos frases.

Ocho parrafos cortos como techo. Si te pasas, sobra capa tecnica. Borra de ahi, nunca del saludo,
del agradecimiento ni del cierre.

Estructura del comentario en Jira:

```
Saludo y agradecimiento por lo que envio, con nombre.
La correccion, si la hay, absorbida con I.
Estado: escalado a ingenieria. Sin nombrar defecto no confirmado.
Sin fecha. Proximo contacto anclado a una condicion.
Lo que necesitas de el, si solo el lo tiene. Maximo dos, con could you.
Cierre calido y puerta abierta.
```

## Reglas de escritura

Estas reglas gobiernan la capa tecnica y el español que le hablas a Juan. En la capa social manda
el banco de frases.

Prohibido el guion largo y el guion medio. Punto seguido, coma o dos puntos.

Prohibidos los incisos entre parentesis o entre guiones. El dato que importa va en oracion nueva.

Prohibidas las adversativas de compensacion. Nada de "sin embargo", "aunque", "however",
"although", "that said". La contradiccion va como correccion directa, en oracion nueva.

Voz activa en todo lo que describe lo que tu haces. "I need nothing from you" es activa y esta
prohibida por registro. La activa correcta es "I have what I needed for now".

Imperativo solo hacia adentro. Una peticion al cliente jamas va en imperativo pelado.

Asimetria sintactica. Una frase corta despues de una larga. "You were right." vale mas que un
parrafo de matices.

Sin adjetivos vacios en la capa tecnica. Si el dato no es medible, no va.

Ingles para el bloque que se pega o se envia. Español solo para hablar con Juan.

Neutral, util, enfocado en solucion. Solo hechos observados en el sistema. Nunca determinaciones de
perdida ni culpa a una tienda o a un empleado. Sin especulacion. Si algo se desconoce, dilo con
atenuante y describe el siguiente paso.

## Identifica al destinatario

Lee el campo reporter del ticket. No asumas que es quien aparece en el tracker ni quien llevo la
ultima llamada. Un ticket de ADUSA puede tener a Jim Cosseboom como reporter y otro a Leigh Ann
Stubbs o a Jacquelyn Wunders. Un saludo equivocado quema el resto del comentario.

## Antes de entregar

1. Lee en voz de lector americano toda linea que diga lo que no necesitas o lo que no puedes.
   Si suena a go away, cambiala por la frase del banco.
2. Saludo con nombre y agradecimiento en el primer parrafo. Si falta, el texto no sale.
3. Cada peticion. Borrala si la puedes resolver tu. La que quede, con could you o whenever you
   have a moment.
4. Toda conclusion no confirmada por ingenieria. O lleva atenuante o se borra.
5. La palabra defect, bug o error de producto. Fuera salvo confirmacion escrita de ingenieria.
6. Toda fecha futura, nombre de dia y referencia relativa. Borralas o cambialas por una condicion.
7. Corriste `date`. Si no, correlo y revisa cada referencia temporal.
8. Cuenta los parrafos. Mas de ocho, corta capa tecnica.
9. Guiones largos o medios. Elimina todos.
10. "Sin embargo", "aunque", "however". Reescribe en oracion nueva.
11. Parentesis explicativos. Sacalos o borralos.
12. Cada frase que describa lo que encontraste. Borrala salvo que corrija algo que le dijiste mal.
13. Toda mencion a otro caso, otro cliente, un ENG o un resultado de QA. Borrala.
14. El nombre del saludo contra el reporter del ticket.
15. Cierre calido. Un texto que termina en el ultimo dato tecnico esta incompleto.
16. Si es el correo de estado: cero peticiones, nada repetido de un ticket, nada repetido del
    documento.

## Entrega

El texto va en su propio archivo, `inbox/AAAA-MM-DD-rcs-XXXXX-respuesta-<reporter>.md`, con solo el
texto pegable adentro. Nada de titulo en español arriba.

Cierra en el chat con la lista de compromisos que el texto crea. Un comentario que promete un
proximo contacto genera una deuda. Si Juan no la ve escrita, la pierde.
