# RCS-28556. Vitamin Shoppe, User Blocked

Fecha: 2026-08-26. Trabajado por Juan Martinez apoyando a Sebastian Garces, que es el assignee.
Estado en Jira al abrir la sesion: Work in progress. Reporter Joe Austin. Prioridad Medium.
Tipo Incident. Creado 2026-08-24 16:09 EDT. **Sin label.**
Cliente 433, producto Incident LPMS, segun `reference_waf_cloudflare_bloqueos`.

No existe `tickets/RCS-28556.md` ni `bitacora/RCS-28556.md`. La ficha se genera despues de anotar.

## Conclusion

La IP del bloqueo de Michael Holmstrom esta en el mismo /24 de Zscaler Toronto que la IP del bloqueo
de Ahold en RCS-28059, cuya causa raiz Cerebro ya tiene establecida y cuyo fix ya se aplico y se
confirmo con el cliente. Es el mismo caso, en otro tenant que nunca recibio el allowlist.

Y hay que corregir una memoria: `reference_waf_cloudflare_bloqueos` afirma que el texto de la pagina
de bloqueo distingue una regla de contenido de una regla de pais. No lo hace. Esa inferencia es la
razon por la que este cluster lleva siete semanas sin cerrarse.

## Evidencia nueva, de los dos adjuntos

Guardados en `adjuntos/RCS-28556/`. Son los primeros del cluster con los datos legibles. Los tres
tickets anteriores solo traen blobs de media que la API no resuelve.

`01-block-page-url-nameplate.png`

    Pestana   Attention Required! | Cloudflare
    URL       https://apps.apprissretail.com/vitaminshoppe/signin?url=/vitaminshoppe/nettrack/systemselect.aspx
    Texto     Sorry, you have been blocked
              You are unable to access apprissretail.com
    Placa     MICHAEL HOLMSTROM

`02-block-page-rayid-clientip.png`

    Cloudflare Ray ID   a304809aba495425
    Your IP             136.226.130.207

El cliente si revelo la IP, asi que va en el traspaso. La regla de
`reference_waf_cloudflare_bloqueos` de omitirla cuando no la revelo no aplica aca.

## El precedente: mismo /24, no solo el mismo proveedor

RCS-28059, Ahold, label `Uni_Jul_26_WAFAccess`. April Valerio pego el 2026-07-30 14:54 EDT, textual:

    "Cloudflare Ray ID: a236838f99b0f80e • Your IP: 136.226.130.120"

RCS-28556, Michael Holmstrom: `136.226.130.207`.

Las dos en `136.226.130.0/24`. RDAP de ARIN sobre ese bloque:

    "name" : "ZSCALER-YTO3"
    "handle" : "NET-136-226-130-0-1"
    parentHandle : NET-136-226-0-0-1
    bloque padre : 136.226.0.0/16, org ZSCAL, ZSCALER, INC.
    registrant del /24, adr label : "151 Front Street West\nToronto\nON\nM5J 2N1\nCanada"

YTO es Toronto. Mismo nodo de salida de Zscaler, no solo el mismo proveedor.

Causa raiz que Cerebro ya tiene escrita, `brain/markdown/19-rcs-procesos-playbook.md` linea 1864,
textual:

    "El bloqueo 'Sorry, you have been blocked' fue el Cloudflare WAF default-block rechazando trafico
     de Zscaler ruteado por Canada; el fix fue un allowlist de pais. Categoria propia porque el paso
     de checklist que se deriva ('revisar reglas de WAF por cliente antes del corte') es distinto del
     de rutas."

Y el tracker de ADUSA, `brain/markdown/26-adusa-estado-tickets-reuniones.md`, textual:

    "Users at store and corporate locations were intermittently blocked at sign-in. Traffic routed
     through the ADUSA proxy service was exiting through Canadian nodes, which the Appriss web
     security rule was rejecting."
    "Canada was allowed on 7/31, April confirmed users could log on and asked us to close, and it was
     closed on 8/3. Two loose ends: Appriss still owes ADUSA the IP addresses behind the new URL, and
     which other countries traffic may exit through."

El fix se aplico el 31 de julio y la clienta confirmo que los usuarios entraban. Eso zanja la
contradiccion de Jira, donde Kamminga escribio el 13 de agosto "No action/code change needed": esa
frase no puede referirse al allowlist, porque el allowlist ya estaba funcionando desde el 31 de julio
con confirmacion de la clienta.

Vitamin Shoppe nunca recibio ese allowlist. Verificado hoy: no existe ningun ticket CISS de Vitamin
Shoppe y no se modifico ninguna regla WAF para el cliente 433.

Esto no es agrupar por metadata. Sigo `feedback_agrupar_no_es_causa_raiz`: lei los comentarios de
RCS-28059 antes de afirmar el patron, y lo que agrupa es el /24 de salida mas la pagina de bloqueo
mas un mecanismo ya confirmado en el precedente. No agrupo con RCS-28282 de Co-op, que es otro
cliente, otro producto y bloqueo con sesion ya abierta.

## Correccion a reference_waf_cloudflare_bloqueos

La memoria dice, textual:

    "El texto de Cloudflare que ve el usuario incluye 'several actions that could trigger this block
     including submitting a certain word or phrase, a SQL command or malformed data'. Eso es una
     regla WAF gestionada disparada por el contenido de la peticion, no una regla de pais ni de IP."

Esa conclusion es incorrecta y esta siendo load bearing desde el 11 de agosto.

El adjunto de este ticket muestra ese mismo texto. Y RCS-28059 muestra la misma pagina con el mismo
texto, y ahi la causa fue el default block rechazando trafico de Canada, que es exactamente una
decision por origen. El propio playbook de Cerebro lo dice. Las dos afirmaciones no pueden coexistir.

El motivo tecnico es que ese parrafo es la plantilla fija de Cloudflare, no un mensaje por regla. Y
el perimetro de `apps` es default deny. La pagina de ARIT sobre Cloudflare lo dice, textual:

    "For apps and test domains: Default action = Block. Access is granted only when a request matches
     a Skip rule"
    "Skip rules must appear above the global block rule"

Con ese modelo toda peticion que no matchea un Skip cae en la misma regla global de bloqueo y renderiza
la misma pagina con el mismo parrafo. El texto no puede discriminar contenido de pais. Lo unico que
discrimina es Security > Events por Ray ID.

ENG-7176 registra la misma observacion sin sacar la conclusion, textual: "A Cloudflare WAF country
rule. Same block page wording as a separate confirmed case on another tenant."

Consecuencia. Esa inferencia empujo la hipotesis de pais debajo de la de contenido, y de ahi salio el
orden de candidatos de ENG-7176, que puso ENG-5664 primero. Con la correccion, el orden se invierte.

## ENG-5664 queda descartado para este ticket

ENG-7176 fija el criterio de decision el mismo, textual:

    "Read the Cloudflare Ray ID and client IP from the screenshots attached to the four originating
     support tickets and check them against the WAF rules and the request path. A Ray ID with a valid
     slug present points at candidate 2. A missing slug in the request path points at candidate 1."

Candidate 1 es ENG-5664, slug caido en la construccion de la URL. Candidate 2 es la regla de pais.

En la URL del adjunto el slug `vitaminshoppe` aparece dos veces, en el path y en el parametro `url`.
No hay slug caido. El criterio propio de ENG-7176 apunta a candidate 2.

Estado hoy de ENG-5664: Development Complete, assignee Matthew Kamminga, fixVersion
"Secure August 2026 Release 2/2", releaseDate 2026-08-27. No aplica aca.
Estado hoy de ENG-7176: Backlog, sin assignee, Medium, updated 2026-08-19, sin investigacion.

## Por que explica la intermitencia

Zscaler asigna el nodo de salida por ubicacion y por carga, no fijo por usuario. Buffalo esta a 160 km
de Toronto. El mismo equipo sale por YTO en unas sesiones y por un nodo de Estados Unidos en otras.
Sin CA en la lista del tenant, el bloqueo aparece y desaparece sin que nadie toque nada.

Encaja con lo que el cliente ya habia dicho y quedo sin usar. RCS-27766, Joe Austin, 2026-08-17,
textual:

    "Scot's office is in Buffalo and I believe his internet provider is either based in or routed
     through Canada. We have had some issues with other applications we use because of this."
    "Nothing changed for Brandon, just one day he was blocked the next day he was in."

Y con la descripcion de este ticket, textual: "it is occurring at his home office and while he is
visiting stores." Bloqueado en casa y bloqueado visitando tiendas, mismo equipo, es salida de proxy
variable. No es red de tienda ni cuenta bloqueada.

## Lo que no se puede repetir

Cierre interno de Juan en RCS-28214, 2026-08-24 21:35, textual:

    "Do not repeat the migration-side-effect explanation given to this customer on RCS-28175, which
     has no investigation behind it."

En RCS-28175 Diego Buelvas le dijo al cliente que era "a known side effect of a platform migration"
con "user session and authentication data is being reconciled across systems", y despues que habia
hotfix el 10 y otro el 14 de agosto. Joe reabrio el 11 con "This is not resolved." Un bloqueo en el
borde por origen nunca llega a la capa de sesion. La evidencia de hoy contradice esa explicacion.

## La ruta del cambio

La pagina de ARIT sobre Cloudflare no documenta ningun proceso para pedir un cambio de regla WAF o de
pais. Sin dueno, sin cola de entrada, sin aprobacion. Hueco real, vale levantarlo aparte.

En la practica hay dos rutas:

    Ruta A, la que uso Ahold en RCS-28059 y que resolvio en cuatro dias. PR sobre `allow-countries`
    en arpfiles, la levanto Matthew Kamminga y fue a InfoSec. Chris Rippingale, 2026-07-31 14:32,
    textual: "Matt raising PR to allow Canada and sending to InfoSec right now."
    Ruta B, la que uso JCrew en CISS-21846. Ticket CISS a Derek Bringewatt, High. Creado
    2026-08-21 11:49, cerrado 12:43 el mismo dia.

Recomiendo Ruta A por el precedente exacto, y CISS solo si Engineering la rebota. El campo
`allow-countries` esta documentado en la pagina "Seeding Cloudflare Firewall Rules" con el ejemplo de
Ralph Lauren.

Por pais, no por IP. Los rangos de salida de Zscaler cambian y una lista de IPs se rompe sola. La
guia de ARIT pone "Hardcode IPs in rules" en la lista de Do NOT.

## Los dos caminos de arreglo

Camino A, lado Appriss. Agregar los paises que el cliente confirme a `allow-countries` de las URLs de
vitaminshoppe. Requisito previo, y es lo que trabo el caso antes. Matthew Everett en RCS-27766,
2026-08-19, textual:

    "if we do need to open a country like Canada, that is not scoped to one user, it would apply to
     anyone connecting from there. Because of that, we need the request to come from someone at
     Vitamin Shoppe with the authority to approve that scope of change."

Joe contesto "Let's hold off for now". Ese pedido se hizo sin evidencia y el cliente lo freno.

Ojo con el orden. En RCS-28059 nadie pidio un aprobador. Tyrone pidio la lista de paises al equipo de
red del cliente, April contesto "I confirmed with Networking that both US and Canadian IP's are
acceptable", y con eso se ejecuto. Pedir la lista de paises primero es mejor: define el alcance, la
contesta la misma gente que aprobaria, y ya funciono una vez este mes. El aprobador se pide despues,
si Engineering lo exige.

Camino B, lado cliente. Vitamin Shoppe fija la salida de Zscaler a nodos de Estados Unidos para
`apps.apprissretail.com`, o excluye el hostname del tunel. Su equipo de red lo hace sin abrir un pais
entero en nuestro perimetro. Vale ofrecerlo, porque el camino A le baja el nivel de control al propio
cliente.

## Los dos textos para pegar

Van en archivos aparte, con formato Jira completo y sin corte de linea, para copiarlos sin arrastrar
nada del chat.

    inbox/2026-08-26-rcs-28556-COMENTARIO-INTERNO.md    nueve secciones, tablas, bloques de codigo
    inbox/2026-08-26-rcs-28556-RESPUESTA-CLIENTE.md     texto limpio, 80 palabras, un pedido

El comentario interno abre con la correccion, que es la regla de `cerebro-comentario`. Un ingeniero
que lee tres parrafos de contexto antes de enterarse de que la premisa era falsa pierde el tiempo dos
veces.

## Transicion

**461 Waiting For Infrastructure**, a Under Infrastructure Review.

Es la ruta que fija `reference_waf_cloudflare_bloqueos`, textual:

    "Cuando llegue el Ray ID la ruta es Under Infrastructure Review, que es quien ve la regla que
     disparo. En esa ruta el assignee se queda con el ticket y es quien comunica y cierra."

El Ray ID ya esta. Sebastian se queda con el ticket y sigue comunicando. Verificado en vivo que la
transicion esta disponible, `isAvailable: true`, sin pantalla obligatoria. Tambien estan 571 Under
Customer Review, 231 Waiting for Engineering y 621 Waiting for Security.

No mover a 231. ENG-7176 es investigacion y el arreglo aca es de configuracion, no de codigo.

## Orden de ejecucion para Sebastian

1. Pegar el comentario interno.
2. Pegar la respuesta al cliente.
3. Mover a 461 Waiting For Infrastructure.
4. Agregar el label `Uni_Jul_26_WAFAccess`.
5. Vincular a RCS-28059, ENG-7176 y RCS-28289.

## Pendientes aparte, no son de Sebastian

RCS-27766 sigue en Work in progress con Matthew Everett. Joe autorizo el cierre el 2026-08-24.
RCS-28289 cierra con el mismo cambio, es de Juan.
RCS-28032 tiene el label `Uni_Jul_26_WAFAccess` y es el caso multidistrito de Dayna Rivera, distritos
501 y 504. Ese label esta mal puesto. `reference_waf_cloudflare_bloqueos` lista los de Vitamin Shoppe
como 27766, 28175, 28214 y 28289, sin 28032, asi que la memoria esta bien y el label esta mal.
El hueco de proceso: no hay ruta documentada para pedir un cambio de regla WAF o de pais.

## Comandos para cerrar en Cerebro

```bash
bin/anotar RCS-28556 "Ray ID a304809aba495425 e IP 136.226.130.207 leidos de los adjuntos. La IP esta en 136.226.130.0/24, ZSCALER-YTO3 Toronto, mismo /24 que la IP de RCS-28059 cuya causa raiz es el default block de Cloudflare rechazando Zscaler por Canada. Slug presente en la URL, descarta ENG-5664 por el criterio de ENG-7176. Entregado comentario interno, respuesta al cliente y transicion 461 a Sebastian Garces."

cat inbox/2026-08-26-rcs-28556-zscaler-toronto-mismo-24-que-ahold.md | bin/guardar 16 "RCS-28556 Vitamin Shoppe: el bloqueo es Zscaler Toronto, mismo /24 que Ahold RCS-28059"

python3 bin/indexar_tickets.py
```

Y aparte, corregir `brain/memoria/reference_waf_cloudflare_bloqueos.md`. El parrafo de la plantilla
de Cloudflare no distingue contenido de pais. Propuesta de reemplazo en la seccion de abajo.

## Parche propuesto para reference_waf_cloudflare_bloqueos.md

Reemplazar el bloque que arranca en "**La pagina de bloqueo dice el motivo.**" por:

    **La pagina de bloqueo NO dice el motivo.** Corregido el 26 ago 2026 con el adjunto de RCS-28556.
    El parrafo *"several actions that could trigger this block including submitting a certain word or
    phrase, a SQL command or malformed data"* es la plantilla fija de Cloudflare, no un mensaje por
    regla. El perimetro de `apps` es default deny: la pagina de ARIT dice *"Default action = Block.
    Access is granted only when a request matches a Skip rule"*, y *"Skip rules must appear above the
    global block rule"*. Toda peticion que no matchea un Skip cae en la misma regla global y
    renderiza la misma pagina con el mismo parrafo. Prueba: RCS-28059 muestra esa misma pagina y su
    causa fue el default block rechazando Zscaler ruteado por Canada, o sea una decision por origen,
    no por contenido. Lo unico que discrimina es Security > Events por Ray ID.

    **Zscaler y el mismo /24.** Los bloqueos de sign in de Vitamin Shoppe y el de Ahold comparten el
    bloque `136.226.130.0/24`, netname ZSCALER-YTO3, nodo de salida de Zscaler en Toronto. RCS-28059
    IP 136.226.130.120, RCS-28556 IP 136.226.130.207. Cuando aparezca un bloqueo intermitente de sign
    in, resolver la IP del cliente por RDAP antes de cualquier otra hipotesis. Si cae en Zscaler o en
    otro proxy en la nube, es alcance de pais y el fix es `allow-countries` en arpfiles. La
    intermitencia la explica que el proxy cambia de nodo de salida, no la sesion ni la cuenta.

## Fuentes

    Jira
      RCS-28556  https://trebuco.atlassian.net/browse/RCS-28556
      RCS-28289  https://trebuco.atlassian.net/browse/RCS-28289
      RCS-28214  https://trebuco.atlassian.net/browse/RCS-28214
      RCS-28175  https://trebuco.atlassian.net/browse/RCS-28175
      RCS-28059  https://trebuco.atlassian.net/browse/RCS-28059
      RCS-27766  https://trebuco.atlassian.net/browse/RCS-27766
      RCS-28032  https://trebuco.atlassian.net/browse/RCS-28032
      ENG-7176   https://trebuco.atlassian.net/browse/ENG-7176
      ENG-5664   https://trebuco.atlassian.net/browse/ENG-5664
      CISS-21846 https://trebuco.atlassian.net/browse/CISS-21846

    Confluence
      ARIT, checklist de troubleshooting
        https://trebuco.atlassian.net/wiki/spaces/ARIT/pages/477582032916/Additional+Useful+Sections
      ARIT, Cloudflare Usage & Operational Workflow
        https://trebuco.atlassian.net/wiki/spaces/ARIT/pages/477583704065/Cloudflare+Usage+Operational+Workflow+in+Appriss+Retail+Best+Practices+and+Troubleshooting+Guide
      ARPDT, Seeding Cloudflare Firewall Rules
        https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/476625797139/Seeding+Cloudflare+Firewall+Rules

    Cerebro
      brain/memoria/reference_waf_cloudflare_bloqueos.md      se corrige, ver parche
      brain/memoria/feedback_agrupar_no_es_causa_raiz.md
      brain/markdown/19-rcs-procesos-playbook.md  linea 1864  y § Regla de Shandana
      brain/markdown/26-adusa-estado-tickets-reuniones.md     § Login and access
      tickets/RCS-28059.md
      adjuntos/RCS-28556/

    Externo
      RDAP ARIN  https://rdap.arin.net/registry/ip/136.226.130.207
