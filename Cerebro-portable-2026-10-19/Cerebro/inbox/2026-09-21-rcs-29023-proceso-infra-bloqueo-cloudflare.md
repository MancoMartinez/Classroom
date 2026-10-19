# RCS-29023. Proceso para escalar a Infraestructura un bloqueo de Cloudflare

Fecha: 2026-09-21. Pregunta de Juan sobre el proceso con Infra para RCS-29023, 3Sixty Duty Free.
No hay ficha ni bitacora de este ticket todavia en Cerebro, es nuevo de hoy.

## El ticket

RCS-29023, https://trebuco.atlassian.net/browse/RCS-29023. Reporter Jose Montenegro, 3Sixty Duty
Free. Creado 2026-09-21 13:25 EDT. Prioridad High. Estado Work in progress. Sebastian Garces tomo
ownership a las 13:36. Descripcion del reporter, textual: "We are having trouble logging in when we
are in our stores located in Mexico and Canada we are getting this message, see attachment." La
pagina del adjunto es la misma plantilla de bloqueo de Cloudflare, "Sorry, you have been blocked",
sobre apps.apprissretail.com/3sixty/nettrack/.

## Es el mismo patron de RCS-28059 y RCS-28556

Ahold, RCS-28059, y Vitamin Shoppe, RCS-28556, cerraron por la misma causa. El perimetro de
`apps.apprissretail.com` en Cloudflare es default deny. Trafico que sale por un pais fuera de la
lista `allow-countries` cae en la regla global de bloqueo y renderiza esa misma pagina. En los dos
casos previos el pais bloqueado era Canada, con el trafico saliendo por un nodo de Zscaler en
Toronto. Aca el reporter ya nombra dos paises, Mexico y Canada. Mexico no aparece en ningun caso
anterior de Cerebro. Trata cada pais como su propia confirmacion, no asumas que un fix de Canada ya
cubre Mexico.

## Por que no hay una ruta unica documentada

La pagina de ARIT sobre Cloudflare no define un proceso para pedir un cambio de regla WAF o de pais.
Sin dueno fijo, sin cola de entrada, sin aprobacion formal. Es un hueco de proceso real, no algo que
Juan este pasando por alto.

En la practica hay dos rutas que ya funcionaron:

Ruta A, la que cerro Ahold en cuatro dias. Un PR sobre el campo `allow-countries` en el repo
`arpfiles`, levantado por Matthew Kamminga y enviado a InfoSec para aprobacion. Es la ruta directa
cuando ya existe el precedente. Matthew ya armo este mismo arreglo dos veces, para Ahold y para el
seguimiento de Vitamin Shoppe.

Ruta B, la que uso JCrew. Un ticket de CISS a Derek Bringewatt. Se uso cuando Engineering rebota la
ruta A.

Soporte no tiene acceso a la consola de Cloudflare. Nadie en Colombia ejecuta el cambio. Lo que
Soporte controla es reunir la evidencia, transicionar el ticket a Infraestructura y despues seguir
de assignee hasta que el cliente confirme.

## Los pasos, en orden

Primero, pedir al cliente la lista completa de paises desde donde sale su trafico. No solo Canada y
Mexico como sospecha, la lista completa que su equipo de red confirme. Ese pedido lo hizo Tyrone en
RCS-28059 y April, la contraparte de Ahold, contesto con la confirmacion de red en el mismo dia.
Pedir esto primero define el alcance del cambio y lo responde la misma gente que despues lo aprueba.

Segundo, leer el Ray ID y la IP del cliente en el pie de la misma pagina de bloqueo. Estan debajo
del texto visible, hay que bajar el scroll del recorte o pedirle al cliente que lo haga. Sin Ray ID
no se identifica la peticion en Security Events y el caso no se puede vincular a nada. El adjunto de
RCS-29023 hoy no trae ese pie visible en lo que llego por la API, hay que pedirselo al cliente o
revisar el adjunto completo.

Tercero, no pedir un aprobador todavia. Eso se pide solo si Engineering lo exige una vez el cambio
este listo para aplicarse, nunca antes. Pedirlo temprano fue lo que trabo RCS-27766 semanas.

Cuarto, con la lista de paises y el Ray ID en mano, transicionar el ticket con 461 Waiting For
Infrastructure. Esa transicion deja el ticket en Under Infrastructure Review, que es el equipo que
lee Security Events y decide la regla. El assignee no cambia. Sebastian sigue de dueno, sigue
hablando con el cliente y cierra el cuando el cambio quede confirmado.

Quinto, escribir directo a Matthew Kamminga citando RCS-28059 y RCS-28556 como precedente. Es la via
mas rapida porque el ya armo el mismo PR dos veces y conoce el patron.

## Lo que Juan recordaba a medias

La conversacion previa con alguien de Infra para un usuario de Canada es RCS-28059, Ahold, cerrado
via Matthew Kamminga con un PR a InfoSec el 31 de julio. El mismo contacto, la misma ruta, sirve
para RCS-29023.

## Fuentes

    Jira
      RCS-29023  https://trebuco.atlassian.net/browse/RCS-29023
      RCS-28059  https://trebuco.atlassian.net/browse/RCS-28059
      RCS-28556  https://trebuco.atlassian.net/browse/RCS-28556
      RCS-27766  https://trebuco.atlassian.net/browse/RCS-27766

    Cerebro
      brain/memoria/reference_waf_cloudflare_bloqueos.md
      inbox/2026-08-26-rcs-28556-zscaler-toronto-mismo-24-que-ahold.md
      inbox/2026-09-04-rcs-28556-respuesta-garces.md
      tickets/RCS-28059.md
