# Diagnostico por codigo de error. Que significa cada uno y a que memoria ir

Escrito el 8 sep 2026. Timeout, lentitud y los codigos 5xx tocan 56 de las 443 fichas de ticket, el
12%. El material esta bien escrito y repartido en tres memorias que si se citan entre si. Lo que
faltaba era la tabla de entrada, porque para saber cual de las tres abrir hay que leer las tres.

Esto no reemplaza a ninguna. Enruta.

## La tabla

| Lo que ves | Que es | A donde vas |
|---|---|---|
| Pagina "Sorry, you have been blocked" con Ray ID | Regla WAF gestionada de Cloudflare disparada por el contenido de la peticion. La peticion nunca llego a la aplicacion | `brain/memoria/reference_waf_cloudflare_bloqueos.md` |
| **524** | Timeout de origen. La peticion paso por Cloudflare y nuestro servidor no respondio a tiempo. No es un bloqueo | misma memoria, seccion del 524 |
| **502 sin `Cf-Ray` en la respuesta** | Lo genera YARP, nuestro propio reverse proxy, no Cloudflare. Significa que netTrack no responde a tiempo | misma memoria, mas `reference_query_store_regresion_plan.md` |
| **502 con `Cf-Ray` y `Server: cloudflare`** | Cloudflare si esta en el camino. Contrasta antes de concluir | misma memoria |
| **499** | El cliente corto antes de recibir respuesta. Son usuarios abandonando por la espera | misma memoria, seccion de los 499 |
| **429 `VaultOperationLimitReached`** | Azure Key Vault agotado. Tumba el handshake SAML de Secure EBR | `investigaciones/sso-cuatro-capas-donde-falla-el-login.md` capa 2 |
| La misma consulta pasa de subsegundo a decenas de segundos sin despliegue | Regresion de plan de ejecucion en SQL Server | `brain/memoria/reference_query_store_regresion_plan.md` |
| "Tarda 30 segundos", sin codigo de error | Autorreporte. Todavia no hay medicion | `brain/memoria/reference_medir_lentitud_web_devtools.md` |

## Tres numeros que conviene tener en la cabeza

**120 segundos es el `CommandTimeout` de la aplicacion.** Cloudflare corta a los 100, asi que el
usuario ve un 524 antes de que la aplicacion alcance a rendirse. Un maximo de 120 s en Query Store
no es casualidad, es el techo.

**Los 499 pesan mas que los 502.** En la ventana de 24 horas del 14 ago 2026 habia 5.95k de 499
contra 2.82k de 502. El 499 es la medicion cuantitativa de la lentitud que el cliente reporta en
prosa.

**Un problema de plataforma se ve en la lista de tenants.** Esa misma ventana cubria 7-eleven,
staterbros, walmart-usa, adusa y caseys, con `POST /7-eleven/nettrack/index.aspx` fallando 467 de
490. Si el fallo aparece en varios tenants a la vez, deja de ser el caso de un cliente.

## Antes de medir cualquier lentitud

**Consigue un tenant de control.** Si el defecto afecta a 3 bases de 39, quedan 36 sanas. Medir los
mismos pasos en una sana convierte "30 segundos" en "N veces mas lento de lo normal". Sin control no
hay medicion, hay anecdota. El protocolo completo de DevTools, con los tres errores que arruinan la
corrida y el discriminador de servidor contra cliente, esta en
`reference_medir_lentitud_web_devtools.md`.

**Cuando el cliente no puede generar un HAR, no insistas.** Las trazas de App Insights,
`appi-prd-wus2-arp`, rol `web-prd-wus2-arp-yarp`, ya traen URL, codigo y duracion de punta a punta.
Alcanza con pedirle fecha, hora y zona horaria del incidente.

## Dos cosas que no se hacen desde Support

**Forzar un plan de ejecucion es un cambio de produccion.** Se propone, no se ejecuta.

**Enlazar dos bloqueos de WAF sin Ray ID que confirme la misma regla.** Cliente distinto, producto
distinto y region distinta no bastan para agrupar. Deja la relacion escrita como hipotesis con lo
que falta para confirmarla.

## Precedente medido que sirve de vara

El 31 jul 2026, entre las 20:30 y las 22:35 UTC, el app service de netTrack acumulo cerca de 2495
client timeouts contra 255 errores 500, con 248 de esos 500 en `POST
/nettrack/api/internal/SendSmartAlert.aspx`. La lectura de que eso apunta a timeout de peticion web
y no a command timeout de SQL es de Juan y no esta confirmada por logs. Nadie ha separado los
timeouts por tenant todavia. Detalle y contexto en
`investigaciones/smart-alerts-familia-de-fallas.md`, mecanismo 2.
