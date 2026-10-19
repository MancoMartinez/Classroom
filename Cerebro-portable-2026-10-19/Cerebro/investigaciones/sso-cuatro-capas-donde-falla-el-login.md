# SSO: cuatro capas donde falla el login, y como saber en cual estas

Escrito el 8 sep 2026 a partir de material que ya estaba en la base. 82 de las 443 fichas de ticket
tocan SSO o SAML, el 18%.

`brain/memoria/reference_sso_incident_diagnostico.md` cubre una sola de las cuatro capas, la del
handshake y el mapeo de claims en Incident, y la cubre bien. Las otras tres aparecieron entre el 30
de julio y el 4 de septiembre de 2026 y no estaban recogidas en ninguna parte. Dos de ellas ni
siquiera son de Incident.

El sintoma que reporta el cliente es siempre el mismo: los usuarios no pueden entrar. Empieza por el
discriminador.

## Discriminador. Cuatro preguntas, en este orden

1. **¿El usuario ve una pagina de bloqueo antes de llegar al formulario de login?** Si el texto dice
   "Sorry, you have been blocked" y trae un Ray ID, es la capa 1 y la peticion nunca llego a la
   aplicacion. No mires configuracion SAML.
2. **¿Fallo de golpe para muchos usuarios a la vez, y se recupero solo o con un reinicio?** Es la
   capa 2, una dependencia interna agotada. No es configuracion.
3. **¿Falla para un usuario, un grupo o un claim concreto, con el resto entrando bien?** Es la capa
   3, handshake y mapeo. Ahi manda el SSO Response Log.
4. **¿El usuario entra, y lo que pierde son permisos, equipo o ubicaciones?** Es la capa 4. El login
   funciona y lo que rompe es lo que el login escribe.

## Capa 1. El borde bloquea el trafico antes de la aplicacion

**Sintoma.** Pagina de Cloudflare, "Sorry, you have been blocked", con Ray ID al pie. El usuario
nunca ve el formulario.

**Causa establecida.** Regla WAF gestionada de Cloudflare, default block, rechazando trafico de
Zscaler ruteado por Canada.

**Evidencia dura, dos casos con la misma huella.** April Valerio pego el 30 jul 2026 a las 14:54
EDT una IP `136.226.130.120`. Michael Holmstrom aporto `136.226.130.207`. Las dos caen en
`136.226.130.0/24`. RDAP de ARIN sobre ese bloque devuelve `ZSCALER-YTO3`, handle
`NET-136-226-130-0-1`, bloque padre `136.226.0.0/16` de ZSCALER, INC., con el registrant del /24 en
151 Front Street West, Toronto. YTO es Toronto. No es solo el mismo proveedor, es el mismo nodo de
salida.

**Tickets.** RCS-28059 de Ahold y RCS-28556, ambos con label `Uni_Jul_26_WAFAccess`. El cluster de
Vitamin Shoppe es el mismo cuadro visto desde otro cliente: RCS-27766, RCS-28175, RCS-28214 y
RCS-28289.

**Lo que hay que pedirle al cliente.** El Ray ID esta al pie de la misma pagina de bloqueo, debajo
del texto, y en los recortes casi siempre falta. Pide bajar el scroll del modal y capturar el pie,
mas la hora exacta con zona horaria. Sin Ray ID no se identifica la regla y el caso no se agrupa con
ningun otro.

**Ruta.** Under Infrastructure Review, que es quien ve la regla que disparo. En esa ruta el assignee
se queda con el ticket y es quien comunica y cierra.

**Hueco de proceso, abierto.** No hay ruta documentada para pedir un cambio de regla WAF ni de pais.
Se detecta, se traspasa, y ahi se acaba lo escrito.

**Trampa de etiquetado.** RCS-28032 lleva el label `Uni_Jul_26_WAFAccess` y no pertenece al cluster,
es el caso multidistrito de Dayna Rivera con distritos 501 y 504. El label esta mal puesto. La lista
buena de Vitamin Shoppe es la de la memoria de Cloudflare, sin 28032.

## Capa 2. Una dependencia interna agotada dentro de la aplicacion

**Sintoma.** Caida masiva y subita del sign in, sin cambio de configuracion, que se recupera con un
reinicio y deja al cliente preguntando cual fue la causa.

**Causa confirmada.** El servicio detras de `/secure/sso/saml2` depende de Azure Key Vault por
private endpoint para completar el handshake SAML. Key Vault empezo a devolver 429 Throttled,
`VaultOperationLimitReached`, en la aplicacion `web-prd-wus2-arp-legacysecure`. Esa dependencia
caida tumbo el sign in de todos los usuarios que autenticaban contra esa instancia.

**Arreglo aplicado.** Infraestructura, Jon Morgan y Jose Parocua, hizo un rolling restart de las 10
instancias de `web-prd-wus2-arp-legacysecure`.

**Alcance real, y es lo que importa.** El limite de operaciones de Key Vault es una cuota compartida
entre todo lo que cuelga de esa instancia, no solo el cliente que reporto. Un pico de otro consumidor
de la misma vault repite el mismo 429 en cualquier tenant que dependa de esa aplicacion. El restart
es un parche, no elimina la causa.

**Como se separa de la capa 1.** El bloqueo de Cloudflare corta en el borde antes de llegar a la
aplicacion. Este agota una dependencia interna dentro de la aplicacion. Cliente canadiense en los
dos casos, mecanismo distinto. No los enlaces por la geografia.

**Ticket.** RCS-28779, Home Depot Canada, EBR Secure. Reporter Ericka Smith, que pregunto la causa
raiz a las 07:43 EDT del 4 sep y no la recibio. El ticket quedo en Work in progress con el hallazgo
sin escribir en Jira.

## Capa 3. Handshake y mapeo de claims

Cubierta en `brain/memoria/reference_sso_incident_diagnostico.md`, fuente Confluence RTS
`477557096452`. Resumen del discriminador para no tener que abrirla:

En Control Panel cada cliente tiene dos pestañas. El **SSO Response Log** registra cada claim
recibido en cada intento de login. Si los intentos del usuario aparecen ahi, el IdP del cliente si
responde y el problema esta en nuestro mapeo, que se mira en la pestaña **SSO Tab**. Si no aparece
nada, el claim nunca llego y es el ACS URL o el Entity ID del lado del cliente.

El XML crudo del claim esta en New Relic filtrando por `Category LIKE '%SAML%'`, y ahi se ve si es
audience mismatch, ACS mismatch o certificado. El claim minimo obligatorio son nombre, apellido y
email.

**Alcance.** Esta capa esta documentada para Incident. Para Secure EBR no hay equivalente escrito
del SSO Response Log, y esa es la razon por la que RCS-28779 se investigo desde cero.

## Capa 4. El login entra y pisa lo que el usuario tenia

**Sintoma.** El usuario autentica sin problema y pierde su equipo, sus permisos o sus ubicaciones.
Se le vuelven a asignar a mano y al dia siguiente los perdio otra vez.

**Cita del cliente que fija el patron.** Sara Beaty, 1 sep 2026: "I've added myself and Brent Hamlin
to the list 3 times now, but when I check the next day, we're no longer on the list."

**Causa y arreglo.** El flujo de login por SSO reescribe la asignacion de equipos en cada entrada.
Luis Hernandez agrego "Admin" a Mandatory Teams en Control Panel, Client SSO Config del cliente, y
confirmo que persiste tras guardar y recargar. Cita textual: "This stops the SSO login flow from
wiping the Admin team assignment for Sara Beaty / Brent Hamlin on each login."

**Ticket.** RCS-28631, Nordstrom. Ojo con este ticket: trae dos problemas separados y solo este
quedo resuelto. El pendiente es la visibilidad de las definiciones de Work Item 900, 901, 902 y 118,
que es otro asunto y no tiene que ver con SSO.

**Regla que se saca de aqui.** Cuando un cliente reporta que pierde permisos de forma periodica,
revisa Mandatory Teams antes de investigar el modulo de permisos. La periodicidad diaria es la
firma: lo que se repite cada dia es el login.

## Donde vive cada cosa

| Que | Donde |
|---|---|
| Handshake, mapeo de claims y SSO Response Log en Incident | `brain/memoria/reference_sso_incident_diagnostico.md` |
| Triage de bloqueos de Cloudflare, Ray ID y formato de traspaso | `brain/memoria/reference_waf_cloudflare_bloqueos.md` |
| Las dos IP de Zscaler Toronto y el RDAP del bloque | `tickets/RCS-28556.md` |
| Key Vault 429 y el rolling restart | `tickets/RCS-28779.md` |
| Mandatory Teams y la cita de Sara Beaty | `tickets/RCS-28631.md` |
| SSO de test parado desde abril, caso largo | `brain/memoria/project_rcs_28240_united_supermarkets.md` |
| A donde se escala cada capa | `brain/memoria/reference_escalacion_l3_procedimiento.md` |
