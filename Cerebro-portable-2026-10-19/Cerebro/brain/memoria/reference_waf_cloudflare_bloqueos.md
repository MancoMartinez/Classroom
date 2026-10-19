---
name: reference_waf_cloudflare_bloqueos
description: "Cómo se triagea un bloqueo de Cloudflare: la página de bloqueo dice si el disparador es contenido o país, y sin Ray ID no se agrupa con nada"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 8b73134e-5723-4d74-be14-e59eb99f9e25
  modified: 2026-08-14T19:30:21.622Z
---

Verificado el 11 ago 2026 con la captura de RCS-28282.

**La página de bloqueo dice el motivo.** El texto de Cloudflare que ve el usuario incluye *"several actions that could trigger this block including submitting a certain word or phrase, a SQL command or malformed data"*. Eso es una **regla WAF gestionada disparada por el contenido de la petición**, no una regla de país ni de IP. Es la diferencia que llevábamos desde el 30 de julio sin poder resolver en la ola de unificación.

**Sin Ray ID no se identifica la regla.** El Ray ID está al pie de la misma página de bloqueo, debajo del texto. Cuando el cliente manda un recorte, casi siempre falta. Lo que hay que pedir es: bajar el scroll del modal y capturar el pie, más la hora exacta con zona horaria.

**Dos síntomas distintos que se parecen y no son lo mismo:**
- Bloqueo **al entrar** a la aplicación, sin sesión. Es lo de Vitamin Shoppe, cliente 433, producto Incident LPMS: RCS-27766, RCS-28175, RCS-28214, RCS-28289.
- Bloqueo **con la sesión ya abierta**, al pedir una pantalla concreta. Es lo de Co-op, cliente 164, producto Secure 5 EBR, RCS-28282, al abrir el receipt view desde Transaction Details.

Cliente distinto, producto distinto, región distinta y síntoma distinto. **No enlazarlos hasta que un Ray ID confirme si es la misma regla.** Dejar la relación escrita en el comentario interno como hipótesis, con lo que falta para confirmarla, es suficiente. Ver [[feedback_agrupar_no_es_causa_raiz]].

**Un 524 no es un bloqueo.** Error 524 es timeout del origen: la petición pasó por Cloudflare y el servidor nuestro no respondió a tiempo. Un bloqueo es la página de WAF descrita arriba. Matt lo separa explícitamente, así que hay que decir cuál de los dos es en el mensaje, o el equipo se pone a buscar la causa de un bloqueo que no existe. El Ray ID sirve igual en los dos casos. Caso de 524: RCS-28256 Tailored Brands, Ray ID `a299728c9ee465e3` (ver [[project_rcs_28256_tailored_brands]]).

**Un 502 sin Ray ID no es de Cloudflare.** Confirmado el 14 ago 2026. Si Cloudflare está en el camino, la respuesta trae `Server: cloudflare` y `Cf-Ray`; se comprobó por contraste en el mismo tenant adusa, donde un `rs.aspx` de Izenda devolvió `Cf-Ray: a2b189b1c997476b-IAD` mientras la página de 502 que ve el cliente no trae ninguno. El 502 lo genera **nuestro propio reverse proxy, YARP**. Chris Rippingale lo confirmó en el chat de la Unificación: *"It's a proxy status code. Means Yarp isn't getting a timely response from nettrack"*. O sea, el origen no responde a tiempo, que es el mismo cuadro de la regresión de plan de [[reference_query_store_regresion_plan]].

**Los 499 importan más que los 502.** En la ventana de 24 h del 14 ago había 5.95k de 499 contra 2.82k de 502. Un 499 es el cliente cortando antes de recibir respuesta, o sea usuarios abandonando por la espera. Es la medición cuantitativa de la lentitud que reportan. Y el problema es de plataforma, no de un cliente: la ventana de 4 h cubría 7-eleven, staterbros, walmart-usa, adusa y caseys, con `POST /7-eleven/nettrack/index.aspx` fallando 467 de 490.

**No pedir HAR cuando el cliente no puede generarlo.** Leigh Ann Stubbs dijo el 14 ago que su equipo no le permite grabar una sesión con F12. No hace falta: las trazas de App Insights (`appi-prd-wus2-arp`, rol `web-prd-wus2-arp-yarp`) ya traen URL, código y duración, con transacción de punta a punta. Alcanza con pedirle **fecha, hora y zona horaria** del incidente para ubicar la petición del lado servidor.

**Formato con el que se entrega el dato al equipo**, el que usó Diego Buelvas cuando Matt lo pidió para Vitamin Shoppe y funcionó (Matt enlazó ENG-6777 a los dos minutos): ticket, cliente, Ray ID, hora con zona, host, y si es block o timeout. Nada más. Si el cliente no reveló su IP ("Your IP: Click to reveal"), se omite; no se inventa.

Cuando llegue el Ray ID la ruta es **Under Infrastructure Review**, que es quien ve la regla que disparó. En esa ruta el assignee se queda con el ticket y es quien comunica y cierra.

Relacionado: [[reference_multidistrito_lhua]], [[reference_unificacion_patrones]].
