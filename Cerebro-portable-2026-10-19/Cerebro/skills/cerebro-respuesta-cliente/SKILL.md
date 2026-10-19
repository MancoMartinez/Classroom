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

## Lo que el cliente NO recibe

Sin excepcion, fuera del comentario:

- Hallazgos de configuracion. Nada de "revisamos las alertas y confirmamos que ninguna exige
  completitud".
- Conteos, consultas, nombres de tabla, resultados de base de datos.
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

## Antes de pedirle algo

Verifica que no lo puedas conseguir tu. Si puedes reproducirlo con un archivo propio, medirlo con
una consulta, o sacarlo de App Insights, no lo pidas. Pedirle un tamaño de archivo cuando puedes
subir uno equivalente traslada trabajo al cliente y alarga el ticket.

Lo que si se pide es lo que solo el tiene. Cual cuenta es la primaria. Que dias siguen cortos en su
vista. Si un usuario ya probo.

El estado por defecto de un comentario es cero peticiones. Si no necesitas nada, dilo en una linea.
"I need nothing from you on this one." Maximo dos peticiones cuando de verdad las necesitas, y no
justifiques por que las pides.

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

## Lo unico tecnico que si entra

Un dato tecnico entra solo cuando corrige algo que soporte afirmo y el cliente refuto. Ahi la
correccion es obligatoria y va temprano. Corrige una vez, no la repitas y no encadenes disculpas.

Un compromiso incumplido se corrige de frente, en una oracion. "I owe you the counts I committed to
on the 19th. Nothing has gone up since then." Despues pasa al siguiente paso y no vuelvas al tema.

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

Saludo: "All" si va a una lista. "Jim, all" si Jim es el principal con la sala en copia.

## Formato

Sin markdown. Sin tablas, sin encabezados, sin negritas, sin viñetas. Parrafos de una o dos frases.

Ocho parrafos cortos como techo. Si te pasas, sobra contenido. No lo reescribas mas bonito.
Borralo.

Estructura del comentario en Jira:

```
Saludo y gracias por lo que envio.
La correccion, si la hay.
Estado: escalado a ingenieria.
Sin fecha. Proximo contacto anclado a una condicion.
Lo que necesitas de el, si solo el lo tiene. Maximo dos peticiones.
Cierre corto.
```

## Reglas de escritura

Prohibido el guion largo y el guion medio. Punto seguido, coma o dos puntos.

Prohibidos los incisos entre parentesis o entre guiones. El dato que importa va en oracion nueva.

Prohibidas las adversativas de compensacion. Nada de "sin embargo", "aunque", "however",
"although", "that said". La contradiccion va como correccion directa, en oracion nueva.

Voz activa e imperativo. "Nothing is needed from you" es pasiva. "I need nothing from you" es
activa. Nada de "cabe destacar".

Asimetria sintactica. Una frase corta despues de una larga. "You were right." vale mas que un
parrafo de matices.

Sin adjetivos vacios. Si el dato no es medible, no va.

Ingles para el bloque que se pega o se envia. Español solo para hablar con Juan.

Neutral, util, enfocado en solucion. Sin relleno y sin empatia excesiva. Solo hechos observados en
el sistema. Nunca determinaciones de perdida ni culpa a una tienda o a un empleado. Sin
especulacion. Si algo se desconoce, dilo y describe el siguiente paso.

## Identifica al destinatario

Lee el campo reporter del ticket. No asumas que es quien aparece en el tracker ni quien llevo la
ultima llamada. Un ticket de ADUSA puede tener a Jim Cosseboom como reporter y otro a Leigh Ann
Stubbs o a Jacquelyn Wunders. Un saludo equivocado quema el resto del comentario.

## Antes de entregar

1. Cuenta los parrafos. Mas de ocho, sobra.
2. Cada peticion. Borrala si la puedes resolver tu.
3. Toda fecha futura, nombre de dia y referencia relativa. Borralas o cambialas por una condicion.
4. Corriste `date`. Si no, correlo y revisa cada referencia temporal.
5. Guiones largos o medios. Elimina todos.
6. "Sin embargo", "aunque", "however". Reescribe en oracion nueva.
7. Parentesis explicativos. Sacalos o borralos.
8. Voz pasiva. Reescribe en activa.
9. Cada frase que describa lo que encontraste. Borrala salvo que corrija algo que le dijiste mal.
10. Toda mencion a otro caso, otro cliente, un ENG o un resultado de QA. Borrala.
11. El nombre del saludo contra el reporter del ticket.
12. Si es el correo de estado: cero peticiones, nada repetido de un ticket, nada repetido del
    documento.

## Entrega

El texto va en su propio archivo, `inbox/AAAA-MM-DD-rcs-XXXXX-respuesta-<reporter>.md`, con solo el
texto pegable adentro. Nada de titulo en español arriba.

Cierra en el chat con la lista de compromisos que el texto crea. Un comentario que promete un
proximo contacto genera una deuda. Si Juan no la ve escrita, la pierde.

