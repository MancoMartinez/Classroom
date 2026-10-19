# Instructivo. RCS-28756, hoy 2026-09-09

Orden fijo. El paso 3 depende del 1. El 2 corre en paralelo.

## Paso 1. Preguntarle a Peyman por chat directo

Peyman Motlagh pidio abrir este RCS el 3 de septiembre. Es el nivel que desbloquea los puntos 1 a 4
sin abrir cuatro conversaciones.

Que pegar: inbox/2026-09-09-rcs-28756-chat-peyman.md, completo.

Que esperas recibir, una de dos:
a) Nike publica directo al Event Hub. La causa queda en el origen y los puntos 1 a 4 se responden
   con lo que te den.
b) Hay un componente de Appriss en medio. Para de decir que el dato nunca llego y revisa ese
   componente antes de responderle a Nike.

Ademas te debe dar el nombre de quien administra el namespace, para los puntos 2 y 4.
Si no responde hoy: repregunta mañana antes de mediodia. No abras el frente con Nike sin esto.

## Paso 2. Anclar la cifra de volumen. HECHO el 2026-09-09

Juan reprodujo el grafico. Total 64.61M en 30 dias, granularidad automatica de 6 horas, eje
UTC-05:00. El tooltip del 20 de agosto 9:00 AM marca 1.17M, que es un bucket de seis horas y no un
dia. amehar leyo 65.53M porque miro la ventana unas horas antes. Misma serie.

Cuenta derivada: 64.61M sobre 17.8 dias con dato da 3.63M mensajes por dia, unos 0.91M por bucket.
Contra 195352 a 234363 transacciones ECOM cargadas por dia, salen entre 15 y 19 mensajes por
transaccion. Un mensaje del hub no es una orden.

Conclusion para el cliente: la cifra de impacto es 195352 a 234363 transacciones ECOM por dia, de
la tabla ECOM Data Load Check. Los 250000 a 300000 del borrador quedan descartados.

## Paso 3. Contestarle a Madhuraj. SOLO cuando esten los cuatro puntos

Decision de Juan del 2026-09-09: la respuesta va completa y en orden, o no va.

Que pegar: inbox/2026-09-09-rcs-28756-respuesta-5-puntos-BORRADOR.md, despues de rellenar los
bloques 1 a 4 y de borrar la primera linea del archivo.

Que esperas ver: el comentario publicado bajo el de Madhuraj del 9 de septiembre 15:59.

Revisa antes de pegar que el punto 5 siga diciendo la verdad del dia. Si para entonces llegaron
archivos nuevos, esa frase cambia.

## Paso 4. Transicionar

El boton NO se llama Under Support Review. Se llama Waiting for Support y lleva a ese estado.
Verificado en el workflow del ticket hoy, transicion 641.

Que esperas ver: el ticket sale de Under Customer Review y queda en Under Support Review, contigo
como assignee.

## Paso 5. Registrar

    cd ~/Cerebro
    bin/anotar RCS-28756 "Comentario pegado a Madhuraj con el punto 5 respondido. Preguntado el camino del dato en Teams. Transicionado a Under Support Review."
    cerrar

`cerrar` ingiere el inbox del dia. Sin eso, nada de esto entra a la base.
