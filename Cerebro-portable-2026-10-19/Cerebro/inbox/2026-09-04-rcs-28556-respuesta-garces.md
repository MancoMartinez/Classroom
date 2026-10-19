Respuesta a la pregunta de Sebastian Garces sobre RCS-28556, hecha por Teams el 04 sep 2026.
Verificado en Jira antes de responder: sigue en Work in progress, ultimo comentario el de Joe
Austin del 28 ago 08:51 EDT, ningun comentario nuevo desde entonces. La captura de IT que Sebastian
menciona es esa misma, ya la investigacion del 26 de agosto la cubre.

================================================================================
BLOQUE 1. Para pegar en Teams a Sebastian, en espanol
Corregido 04 sep: equipo Colombia se escribe en espanol, no en ingles. Ver feedback_estilo_mensajes.
================================================================================

Sebastian, si, pedile la lista de paises primero. Es el mismo pedido que ya le mandamos a Joe el 26
de agosto y es lo que cerro RCS-28059 en cuatro dias. La respuesta de IT que te llego confirma de
quien es el bloqueo. No trae la lista. Insisti en ese punto puntual, de que paises sale su trafico,
nosotros esperamos Estados Unidos y Canada y queremos estar seguros de que no falta ninguno.

Todavia no le pidas un aprobador. Matthew Everett pidio eso en RCS-27766 el 19 de agosto y Joe
contesto que lo dejaran para despues. Eso se pide solo si Engineering lo exige cuando el cambio ya
este listo.

El cambio de regla no lo hacemos nosotros. Soporte no tiene acceso a la consola de Cloudflare. Con
la lista de paises en mano, transiciona el ticket con Waiting For Infrastructure, eso lo deja en
Under Infrastructure Review y ese equipo lee Security Events y actualiza el allow-countries. Vos
segui de assignee. Segui hablando con Joe y cerra vos el ticket cuando el cambio quede aplicado,
igual que paso en RCS-28059 con el assignee de Ahold.

No hay una ruta unica documentada para pedir esto. El arreglo de Ahold fue por un PR de arpfiles a
InfoSec, lo levanto Matthew Kamminga. JCrew fue por un ticket de CISS en cambio. Escribile directo
a Matthew Kamminga y citale RCS-28059 y el Ray ID de este ticket, a304809aba495425. Es la via mas
rapida porque el ya armo el mismo arreglo una vez.

================================================================================
BLOQUE 2. Para Juan, no va a Teams
================================================================================

Si, es exactamente el mismo patron. RCS-28059 lo cerro Ahold en cuatro dias con el mismo mecanismo,
pais de salida de Zscaler bloqueado por el WAF de Cloudflare, arreglado con un allow-countries.

Sebastian tiene la mitad correcta y la mitad en duda resuelta asi:

Pedir la lista de paises al cliente, correcto, es lo que ya se le pidio a Joe el 26 de agosto y
no ha llegado. La respuesta del 28 solo dice de quien es el bloqueo, no cual es la lista.

Quien ejecuta la regla, no es Sebastian ni Soporte. Es Infraestructura. La ruta documentada en
`reference_waf_cloudflare_bloqueos` dice que con el Ray ID en mano el ticket pasa a Under
Infrastructure Review, y ahi el equipo lee Security Events y decide la regla. Sebastian sigue
siendo el assignee durante todo el proceso, sigue hablando con Joe y cierra el el mismo cuando el
cambio aterrice. No se le va el ticket de las manos, solo se le suma quien puede tocar Cloudflare.

Transicion en Jira, cuando llegue la lista: 461 Waiting For Infrastructure, deja el ticket en Under
Infrastructure Review.

No hay ruta de proceso escrita para pedir el cambio de regla o de pais. Es un hueco conocido, hoy
la unica via es contacto directo. Ahold fue por PR de arpfiles a InfoSec via Matthew Kamminga.
JCrew fue por CISS. El addendum del 28 de agosto ya deja armado el mensaje a Matthew citando
RCS-28059, eso es lo que Sebastian deberia usar en cuanto tenga la lista de paises.
