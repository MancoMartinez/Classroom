# Ajuste de skills con el feedback de JR, 11 sep 2026

Fuente: `inbox/2026-09-11-eow-registro-cliente-y-uso-de-ia.md`.
Skills tocadas: `cerebro-respuesta-cliente` y `cerebro-comentario`.
Versiones completas en `inbox/2026-09-11-skill-respuesta-cliente-v2.md` y
`inbox/2026-09-11-skill-comentario-v2.md`.

## El hallazgo que obliga el cambio

La skill `cerebro-respuesta-cliente` contenia textualmente la frase que JR marco en la reunion.
Linea original, en la seccion de peticiones:

    El estado por defecto de un comentario es cero peticiones. Si no necesitas nada, dilo en una
    linea. "I need nothing from you on this one."

No fue un descuido de Juan al escribir. La skill lo instruia. Cuatro reglas mas empujaban en la
misma direccion: "sin relleno y sin empatia excesiva", "voz activa e imperativo", "asimetria
sintactica", "ocho parrafos como techo". Todas correctas para la capa tecnica. Aplicadas al saludo
y a la peticion producen el registro que JR llamo go away, get lost.

Diagnostico: la skill optimizaba economia de palabras sin distinguir capa. El defecto es de diseño,
no de ejecucion.

## Cambios en cerebro-respuesta-cliente

Seccion nueva "Las dos capas", puesta antes de todo lo demas. La social se acolcha, la tecnica se
recorta. El techo de ocho parrafos ahora recorta capa tecnica y nunca saludo, agradecimiento ni
cierre.

Banco de frases con los ocho casos, literal contra natural. Es la columna natural la que se toma.

Los cinco movimientos del registro: agradecer antes de pedir, nunca decir la ausencia de necesidad
como rechazo, absorber con I y repartir credito con you, atenuante en toda conclusion no
confirmada, ningun imperativo pelado en una peticion.

Seccion nueva sobre el defecto no confirmado, con el caso de Lewis y el argumento de facturacion.
Prohibidas las palabras defect, bug y error de producto mientras ingenieria no confirme por escrito.

La regla de agotar recursos internos ahora cita el orden que dio JR y su frase sobre hacerle perder
el tiempo al cliente.

Resuelta la contradiccion del imperativo. Voz activa para describir lo que hace Juan. Peticion al
cliente siempre suavizada. La activa correcta de "I need nothing from you" es "I have what I needed
for now".

Salida de IA pegada entra a la lista de lo que el cliente no recibe, en cualquier tamaño.

Checklist de salida pasa de doce a dieciseis puntos. El primero es leer en voz de lector americano
toda linea que niegue una necesidad.

## Cambios en cerebro-comentario

Seccion 0.3 nueva. Nada entra al ticket sin que Juan lo haya corrido. Tres cajones marcados en el
texto: verificado, hipotesis de IA declarada, y fuera. Si Juan no corrio nada, la skill no entrega
el borrador.

Seccion 0.4, el test de Camila. Si tu heredaras el ticket, esa nota te sirve. Si no, se borra, no se
reescribe mas corta.

Seccion 0.5, el defecto no confirmado, con la advertencia de filtracion hacia el texto de cliente.

Techos duros en la nota interna. Findings seis lineas, salida de consulta diez lineas, un caso
concreto, ruled out cuatro filas, still open cuatro peticiones. Pasos de reproduccion y tablas de
precedentes no cuentan, son lo que ingenieria si usa. Lo que sobra se va a `investigaciones/` y se
cita por ruta.

La declaracion de uso de IA pasa de una instruccion vaga a la forma que JR dicto, con sus tres
partes: lo que la IA propuso, lo que Juan verifico enumerado, y la peticion de revision.

Formato 2 ahora resume la regla de las dos capas y cita la frase corregida, para que un comentario
al cliente escrito desde esta skill no repita el error.

Checklist de salida pasa de siete a diez, mas tres extra para texto de cliente.

## Lo que no se toco

Reglas de ruta y escalacion, requisitos de Aimee, privacidad de RRHH, fechas, formato de entrega.
Nada en el feedback las contradice.

## Pendiente

JR pidio una skill o un MD de registro de servicio al cliente para compartir con todo el equipo, y
va a conectar a Camila con Matt, que arranca AI Ops el 15 de septiembre desde Inglaterra. El banco
de frases de arriba es el insumo. Falta decidir si Juan la lleva el mismo antes de esa reunion.
