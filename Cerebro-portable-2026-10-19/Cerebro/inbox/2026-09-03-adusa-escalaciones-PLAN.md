# ADUSA. Plan de ejecución para hoy, corregido contra el estado real de cada ticket

Corrección primero. RCS-28667 y RCS-28589 ya están en Under Engineering Review desde el 2 y el 1
de septiembre. No hay transición que hacer en esos dos. Solo faltan RCS-28482 y RCS-28683, que
siguen en Work in progress. Abajo va ticket por ticket, con la acción exacta de Jira y sin repetir
un paso que ya está dado.

Los cinco comentarios internos se reescribieron con la estructura completa de seis secciones,
corrección, entorno y pasos, hallazgos, qué se probó y qué no alcanza a ver soporte, qué se
descartó, y qué sigue abierto. Ábrelos, revisa que digan lo que tú sabes que pasó, y pega tal cual.

## RCS-28482. Necesita transición completa

Estado hoy: Work in progress, asignado a ti mismo. Nunca pasó por ingeniería.

1. Abre RCS-28482 en Jira.
2. Cambia el estado a **Under Engineering Review**.
3. Reasigna a **Shandana Khan**.
4. Pega `2026-09-03-rcs-28482-comentario-interno.md` completo.

Aviso que ya te di antes y repito porque importa: este es el más débil de los cinco porque nadie
de Appriss abrió los reportes en Izenda todavía. J.R. pidió escalarlo igual hoy, así que el
comentario lo dice explícito en la sección 5. Si rebota pidiendo la reproducción, ya sabes por qué
y no es un error tuyo.

## RCS-28683. Necesita transición completa

Estado hoy: Work in progress, asignado a Megha Rathi.

1. Abre RCS-28683.
2. Cambia el estado a **Under Engineering Review**.
3. Deja a Megha Rathi como asignada, ella sigue coordinando la reproducción. No la quites.
4. Pega `2026-09-03-rcs-28683-comentario-interno.md`, que ya cita textual la condición que puso
   J.R. el 1 de septiembre pidiendo que se etiquete a Matthew Kamminga.
5. En el comentario o en el campo de menciones, etiqueta a **Matthew Kamminga**, tal como J.R. lo
   pidió por escrito.

## RCS-28667. Ya está en Under Engineering Review, no toques el estado

Estado hoy: Under Engineering Review desde el 2 de septiembre, asignado a Matthew Kamminga. Este
es el que confundiste con los otros dos, y tienes razón en no tocarlo de nuevo.

Lo único que falta es pedir el clon a ENG de forma explícita, porque pasar a este estado no lo
crea solo, eso ya se verificó contra el changelog dos veces.

1. Abre RCS-28667.
2. Pega `2026-09-03-rcs-28667-comentario-interno.md` tal cual.
3. Etiqueta a **Matthew Kamminga**, que ya es el asignado, y en copia a **Shandana Khan** como
   responsable formal de la cola de Under Engineering Review.

## RCS-28589. Ya está en Under Engineering Review, no toques el estado

Estado hoy: Under Engineering Review desde el 1 de septiembre, asignado a Matthew Kamminga por la
propia Shandana Khan, quien escribió textual que se lo daba a él "as current SRE" y le pidió que
se lo devolviera a ella si esto necesita planeación.

Antes de pegar nada, resuelve una cosa que no es de Jira. Pregúntale a tu contacto de Delivery o a
Ryan Barlow directamente si el export a archivo lo trabaja Delivery o Engineering. Ryan ya escribió
el 1 de septiembre que esto necesita revisión de ingeniería sobre la función de exportación, así
que lo más probable es que la respuesta confirme Engineering. Aun así, pregúntalo, porque Matt lo
puso en duda en la llamada de hoy.

1. Confirma delivery contra engineering.
2. Pega `2026-09-03-rcs-28589-comentario-interno.md`. Ya incluye la corrección de que este ticket
   se cerró en falso el 27 de agosto, cubriendo solo la mitad del defecto.
3. Etiqueta a **Matthew Kamminga**.

## RCS-28693. No cambies el estado todavía

Estado hoy: Under Customer Review, asignado a Vlad Bogus. Este no se mueve a ingeniería hasta que
J.R. decida la ruta del caso Paula Dotson.

1. Pega `2026-09-03-rcs-28693-comentario-interno.md`. Ya trae los dos defectos separados, con la
   URL real de producción y de test, y sin tocar el estado del ticket.
2. Envía `2026-09-03-rcs-28693-teams-jr.md` a J.R. por Teams, en paralelo.
3. Cuando J.R. conteste, si dice Engineering Review, transiciona y asigna a Shandana Khan. Si dice
   Security Review, el ticket se queda a tu nombre y pasas el estado a Under Security Review, que
   es el único destino donde no se reasigna.

## El ticket nuevo de RCS-28123, proceso completo

J.R. pidió partir el síntoma del correo de notificación, distinto del popup de confirmación que ya
se cerró como diseño esperado esta madrugada. Esto no es un ENG, es un RCS nuevo.

1. Abre RCS-28123 en Jira.
2. Busca el menú de acciones del issue, el ícono de tres puntos junto al botón de estado, o el
   botón **Link** si tu vista ya lo muestra separado.
3. Si tu instancia ofrece **Create linked issue** directo desde ahí, úsalo. Te abre el formulario
   de creación con el enlace ya armado hacia RCS-28123 y solo eliges el tipo de enlace, **relates
   to**.
4. Si no lo ofrece, créalo por separado. Botón **Create** en la barra superior de Jira. Proyecto
   **RCS**. Tipo de issue, el mismo que tiene RCS-28123 abierto ahora mismo, revísalo en el campo
   Type de ese ticket antes de elegir, para no crear un tipo distinto por accidente.
5. Summary: `Ahold Delhaize, reassignment notification email not sending`.
6. Description: abre `2026-09-03-rcs-28123-nuevo-ticket-descripcion.md` y pega el contenido
   completo en el campo de descripción.
7. Reporter: si tu proyecto te deja elegirlo, pon a Leigh Ann Stubbs, porque es quien reportó el
   síntoma el 1 de septiembre. Si el campo te fuerza a quedar tú como reporter, dilo en la primera
   línea de la descripción, ya está cubierto en el texto que pegaste.
8. Guarda el ticket y copia su clave, el formato es RCS seguido de un número.
9. Si no lo enlazaste en el paso 3, vuelve a RCS-28123, usa **Link issue**, tipo **relates to**,
   pega la clave nueva, guarda.
10. Abre `2026-09-03-rcs-28123-comentario-split.md`, reemplaza las dos apariciones de
    `[PON AQUI LA CLAVE DEL TICKET NUEVO]` por la clave real, y pégalo como comentario en
    RCS-28123.

## Los dos que no se tocan hoy

**RCS-28535.** Ya tiene ENG-7181 en desarrollo. No lo escales. Envía
`2026-09-03-rcs-28535-teams-matt.md` a Matt por Teams. Si confirma el hallazgo de Cloudflare,
pégalo tú mismo en el ticket en una frase, no hace falta plantilla para eso.

**RCS-28596.** Nada que pegar. El acuerdo de no liberar en viernes y apuntar a martes quedó cerrado
en la llamada misma. Solo revisa que se cumpla cuando llegue el viernes.

## Después de pegar todo

RCS-28482 y RCS-28683 son los dos que de verdad crean expectativa de un ENG nuevo, porque hasta
hoy nunca pasaron por Under Engineering Review. RCS-28667 y RCS-28589 ya llevan uno y dos días ahí
sin que aparezca el clon, así que persíguelos mañana antes de la llamada del jueves si siguen sin
ENG. No crees ninguno a mano. Eso produce un duplicado cuando el ingeniero correcto haga el clon
real después.
