# RCS — Soluciones

Carpeta 16 de la base de Moscú. 99 fragmentos.

## RCS-27280 · AutoZone — Reuso de campos/categorías para case type California Workplace Violence (WIP)
_chunk 1145 · 2026-07-14 · fuente: ingesta-2026-07-14_

Jira RCS-27280 (proyecto RCS, tipo SOW, prioridad Medium, WIP). Reporta Nik Swiney (AutoZone); asignado Tyrone Whitney. Necesidad real (comentario Nik 2026-06-16): crear case type nuevo "California Workplace Violence" (hoy en Microsoft Forms) → migrar a Appriss. Requiere dropdowns (categorías) + campos nuevos → reusar campos/categorías sin uso.

Análisis de BJ Probert sobre dbo.MasterCase (81.057 casos). Clave: los datos reales viven en schema dbo, NO en schema incident (vacío).
- Campos vacíos (reusables): Misc1, CaseTier2, CaseTier3, CaseTier4, CaseTier5
- Casi vacíos (18 registros — confirmar si es test data): CaseType2, CaseType3
- En uso (NO tocar): Misc2, Misc3, CaseType4, CaseType5

Categorías sin uso en dbo.ListDetail (ListId=10), 3 grupos:
1. Tipos Español/LatAm (Robo, Acoso…) nunca usados → mejor opción de reuso.
2. Duplicados (mismo nombre, IDs distintos; ej. "Robo (SSC LP)" en IDs 1613/1417/1982/2178) → consolidar primero.
3. Prefijo Z/Y (training/internos Appriss) → NO tocar.

Pendiente: conseguir el doc CA WPV de Nik (attachment Jira no descargable vía API), mapear campos requeridos vs reusables, detectar gaps, comentar plan en el ticket.
OJO fuente de datos: dbo.MasterCase/dbo.ListDetail es SQL Server (case management), NO necesariamente Snowflake. AutoZone = cliente c072azo en SnowTime (pyardm/us/c072azo). Confirmar dónde viven los datos de incidentes antes de elegir conexión.
[Fuente: memoria de Daniel Buelvas (soporte), compartida 2026-07-10]

## SmythsToys — Update Site Listing (runbook Load Stores Reference File + gemelo RCS-27227)
_chunk 1274 · 2026-07-15 · fuente: rcs-27833-twin-research_

PLAYBOOK — SmythsToys "Update Site/Store Listing" (ticket recurrente, ~cada 1-2 meses por región: FR/UKI/CE/NL)

PATRÓN: el reporter efinnucane@smythstoys.com abre el ticket SIEMPRE sin descripción — solo summary + Excel adjunto ("Store Listing with Region & Address*.xlsx", hoja "Store Codes": Store ID, Store Name, Regional Manager, Country, Address). El adjunto ES la solicitud completa; no hay que pedir aclaraciones. Aimee (15-jul-2026): el portal no obliga descripción y este cliente asume que summary+adjunto basta.

GEMELO CANÓNICO: RCS-27227 "Update France Store Listing" (SOW, 2-jun-2026, Carlos Jacinto, resuelto en 2 días sin preguntas al cliente). Serie histórica: RCS-27623 (NL), 27564/27296/24165/22910 (UKI), 26910/24537/22135 (CE), 24041/22749 (FR), 17967... — casi todos ejecutados por Carlos Jacinto, Matthew Everett o Vlad Bogus. Type correcto: SOW (los viejos venían como Incident por el default del portal).

RUNBOOK OFICIAL (Confluence RTS 475044675592, "Load Stores Reference File", autor Carlos Jacinto):
1. Copiar el Excel al servidor DL02, directorio D:\SFTP\WeeklyReports
2. Renombrarlo EXACTO al filemask: "Store Listing with Region & Address.xlsx"
3. La instrucción RTI que lo recoge es OPSFeed
4. Confirmar en la DB que la data se actualizó (screenshot de confirmación al ticket)

CIERRE: comentario al cliente "I have loaded the updated file as requested" + cerrar con Resolution "Support Resolved - Performed Customer Requested Operation" (recordar: al cliente se le dice que puede responder al ticket para reabrir).

APLICACIÓN ACTUAL: RCS-27833 (15-jul-2026, "Update France Site Listing", 56 tiendas FR01-FR60) — mismo flujo. Nota: requiere acceso al servidor DL02; si Juan no lo tiene aún, pedirle a Carlos Jacinto/Matthew Everett que lo ejecute o que muestre el proceso (candidato ideal de reverse shadowing).

## Patrones recurrentes de la cola RCS y reglas tecnicas de la unificacion
_chunk 1445 · 2026-08-03 · fuente: triage 2026-08-03_

Taxonomia de patrones recurrentes en la cola RCS, derivada del triage del 3 de agosto de 2026 sobre 37 tickets sin asignar mas los tickets de la ola de migracion del 27 de julio. Sirve para agrupar tickets nuevos en vez de investigarlos uno por uno.

LOS 11 PATRONES
1. Handover de hypercare de proyecto. Reporter interno, label clientproject, prioridad sin poner. No son incidentes de usuario. Decision: vuelven al equipo de proyecto o van completos a un solo dueno.
2. Resolucion de rol y jerarquia de ubicacion. El patron mas grande. Sintomas: usuario con rol equivocado, no restringido por tienda, no puede editar aunque el permiso este activo, falta un tile, no llega a los campos de usuario. Clientes vistos: Ollie's, Ahold, Genuine Parts, Wild Fork, Myer, DHL, Big Y.
3. Adjuntos y subida de archivos. TRES mecanismos distintos que no hay que fusionar: archivo ausente en el deployment, regla de seguridad por tipo de archivo al subir, filtro de extensiones al leer.
4. Conteos e items en busquedas de Secure 5. Duplicacion de filas por fan out de join a nivel de item, y su espejo, el subconteo. Suelen ser el mismo bug visto de los dos lados.
5. Datos de item ausentes o retencion mal aplicada.
6. Rendimiento y timeouts. Perfil de clasificacion: muchos client timeouts contra pocos HTTP 500 apunta a web request timeout, no a SQL command timeout, porque un command timeout saldria como 500 con excepcion.
7. Dashboards y comportamiento de UI.
8. Feeds, archivos y confirmaciones. Muchos son avisos del cliente, no problemas, y solo necesitan acuse.
9. Bloques por cliente y por reportero. Si una sola persona tiene varios tickets, van a un solo dueno aunque sean productos distintos, porque la relacion es una.
10. Tickets con descripcion vacia. No se pueden trabajar. Necesitan llamada de vuelta al reporter, no investigacion.
11. Preguntas y SOW que no son incidentes. Varios ya estan en Waiting for Software Release y solo falta comunicarlo.

REGLAS TECNICAS REUSABLES
Vista lpuser. La app se maneja con la vista incident.lpuser. secure.LocationHierarchyUserAssignments (lhua) es destino de migracion, no la capa que decide si un usuario puede crear un caso. Para sintoma funcional, la vista primero. Regla de Kiran Vadday.
Bloqueo de WAF en dominio raiz. Pegarle a apps.apprissretail.com sin el slug del tenant devuelve una pagina de bloqueo de Cloudflare, no un redirect. Los clientes migrados que tenian el punto de entrada viejo en favoritos caen ahi. La URL correcta es apps.apprissretail.com/<slug>/signin.
Defecto de construccion de URL. En Santikos (RCS-28022) la app armaba rutas sin el tramo screens/incident/<numero de cliente>/lpms/screens/, y todo lo posterior al primer paso daba 404. El 404 venia de CheckVirtualFileExists de ASP.NET, o sea el archivo estaba genuinamente ausente en la ruta pedida. Si ese tramo depende del contexto del usuario, explica que la misma pantalla falle para un usuario y funcione para otro.
Migracion de correos y contrasenas. En lpguys el LoginID podia ser cualquier cosa, la plataforma nueva necesita un correo. Durante seis semanas antes de migrar un proceso forzaba a ligar correo al iniciar sesion y re-hasheaba la contrasena en ese mismo momento. Quien no entro en esa ventana no tiene correo ligado ni contrasena trasladada, y Forgot Password no sirve porque no hay buzon. Se arregla poniendo la contrasena desde admin, Users, Edit.
Timezone en cookie. Incident lee el timezone de la cookie de secure, no del perfil. Un cambio de perfil no surte efecto hasta que el usuario abre sesion nueva. Consecuencia: cualquier bulk update de timezone va a parecer que fallo hasta que cada usuario tenga sesion nueva. La prueba barata es que el usuario abra una ventana de incognito.
Cookie de division. Para restriccion por division en Ahold, el dato a recolectar en devtools es la cookie ntSECURITY: CDIV.
Enrutamiento de OpsGenie por label de Jira. El label AALPS_LPMS_DevOps_OpsGenie enruta el paging a la rotacion de AALPS DevOps, que es una cadena de escalacion distinta a la del on-call de soporte RCS. Cerrar la alerta de OpsGenie detiene la escalacion de inmediato. Estar en on-call no pone a nadie en la lista de notificaciones de un ticket, eso lo deciden assignee, reporter y watchers.
Ordenacion de niveles de log4net. DEBUG < INFO < WARN < ERROR. Cambiar un logger.Debug a logger.Warn AUMENTA el volumen de log en produccion si prod corre en WARN o mas alto. Y si Log4NetBlobAppender escribe sincronico en el camino del request, el costo real es el appender, no la cantidad de sitios que llaman a Debug.
Precaucion con Build All Screens. En Santikos el rebuild del 31 de julio coincidio con que la lista de incident types quedo en cero. Secuencia observada, causalidad no probada. No reconstruir pantallas en un tenant migrado hasta que eso este aclarado.
Reconstruir pantallas si arreglo un 404. En Vitamin Shoppe (RCS-28005) el 404 se arreglo reconstruyendo las pantallas de audit el 28 de julio. Precedente confirmado en la misma ola del 27 de julio, en tension con la precaucion anterior.

## Bucket de adjuntos Uni_Jul_26: los tres tickets y por que probar 150 MB no cierra un caso de 686 MB
_chunk 1497 · 2026-08-13 · fuente: session-2026-08-13_

El tag de Jira es Uni_Jul_26_Attachments. Los tres tickets del bucket lo tienen y ninguno
es de Juan.

RCS-28167, Stater Bros, Rich Aaron, dueno Viraj Kansara. No puede ABRIR ZIP grandes ya
adjuntos; los pequenos abren bien.
RCS-28305, Stater Bros, Shenbagasundari Pilavadiyan, duena Camila Cortes. Error al SUBIR
video.
RCS-28331, Sportsman's Warehouse, dueno Viraj Kansara. Error al SUBIR adjuntos, se congela
cerca del 49 por ciento.

LOS TAMANOS REALES ESTAN EN LA DESCRIPCION DEL RCS-28331
499.683 KB que son unos 488 MB, 702.588 KB que son unos 686 MB, y 78.457 KB que son unos
77 MB. El usuario dice que se traba alrededor del 49 por ciento y ahi sale el server error.
Tambien probaron acortar el nombre del archivo, sin efecto.

LO QUE SE VALIDO EL 13 DE AGOSTO
Juan probo txt, pdf y video en dos tenants distintos, Stater Bros y Sportsman's, lo mas
pesado 150 MB, todo subio sin error. Diego Buelvas habia hecho la misma prueba antes en
Vitamin Shoppe con un txt.

POR QUE ESA VALIDACION NO CIERRA LOS TRES TICKETS
1. 150 MB esta muy por debajo de los 488 y 686 MB del cliente. Matt Kamminga conto que su
   prueba en el ambiente de test fue de 5 GB y pidio "as big as you have got". El objetivo
   real es 1 GB.
2. El RCS-28167 no es de subir, es de abrir. Ninguna prueba de upload lo toca.
3. Produccion tiene una capa que test no tiene: Cloudflare cortando a los 100 segundos. Que
   test aguante 5 GB no prueba que produccion aguante 700 MB desde una tienda.

RUTA EN LA APP
.../nettrack/LPMS/ManageAttachments.aspx con SuspectID, MasterCaseID, ShopliftingID y
StoreIdent. Se llega desde el caso. Flujo: Browse, Upload, Save All Changes. Convencion de
nombre para archivos de prueba, la de Diego: numero de caso mas -testfile.

## RCS-28240 United Supermarkets: el SSO de test lleva parado desde abril esperando a Albertsons
_chunk 1498 · 2026-08-13 · fuente: session-2026-08-13_

RCS-28240, Medium, Under Support Review, asignado a Camila Cortes. Labels FromEmail y L1.
Reporter Emma Gomez de Albertsons.

NO ES UN BUG, ES UN HANDSHAKE QUE NADIE COMPLETO
United Supermarkets esta a medio migrar de lpguys.net al dominio unificado. El login SSO y
SAML del entorno de test falla en test.apprissretail.com/unitedsupermarkets/signin/sso/saml2.
Marcus Young lo reporto y sigue fallando en incognito y con cache limpia.

LA CADENA
El fallo salio en abril de 2026. Matt Kamminga pidio el 17 de julio que el equipo SSO del
cliente confirmara que agregaron el nuevo ACS URL y actualizaron el Unique Identity URL.
Marcus dijo que no tiene acceso, Emma escalo internamente, David Smith metio a Lakshmi Priya
Nair y Greeshma George de Albertsons, y nadie confirmo nunca si el cambio se hizo. Kurt
Kleist, el contacto historico de SSO, ya no esta. Emma escalo a Support el 7 de agosto tras
pedir dos veces que alguien tomara esto.

TRAMPA CONCRETA
Los valores del ACS URL y del Unique Identity URL no estan en el texto del ticket, se
perdieron al convertir la cadena de correos a Jira. Sin esos dos valores no se le puede
pedir nada accionable al equipo de Albertsons. Hay que sacarlos de Control Panel o pedirselos
a Matt.

EL PASO QUE DESTRABA
Mirar el SSO Response Log del tenant unitedsupermarkets en Control Panel. Si los intentos de
Marcus aparecen, el problema es nuestro mapeo. Si no aparecen, el IdP de Albertsons nunca
respondio y el bloqueo es de ellos, con evidencia en la mano.

OTROS NOMBRES DEL HILO
Sofia Sandner, Transformation PM, la que derivo a Support. Kathleen Garner, CSM, coordina la
ventana de cutover a produccion. Robin Ursenbach.

## RCS-22394 · Walmart — WRMC applications no visibles en Secure (SIN RESOLVER)
_chunk 913 · 2026-06-16 · fuente: https://trebuco.atlassian.net/browse/RCS-22394_

Cliente: Walmart (Service Level: White Glove). Producto: Secure (Canadá / WRMC = Walmart Rewards Mastercard).
Síntoma: no se pueden ver ni buscar las aplicaciones de Walmart Rewards Mastercard en Secure; no hay registro de la transacción en la tabla operatoraction (ni por transactionid ni por detalles).
Causa raíz: el campo de origen AUTH_TYPE_CODE viene SIEMPRE 0 en BigQuery, por lo que no se puede derivar el ActionType de las OperatorActions. La tabla de OperatorAction es CA_WM_MB_SECURE.HOST_AUTHORIZATION.
Estado / fix: SIN RESOLVER tras ~315 días (ago 2025 – jun 2026). Aplazado repetidamente ("as priorities shift, this has to wait again"). Pendiente: confirmar con Walmart cómo determinar action types específicos o mapear otro campo de origen.
Tiempo: ~315 días abierto. Prioridad: Medium. Tipo: Incident. Label: Walmart.
Lección de líder: ticket Medium en cuenta White Glove que cayó en el limbo del backlog; es el caso típico que el proceso Tiger Team (tickets +60 días) debería haber rescatado.

## RCS-27635 · Starbucks — Admin-abandon de Work Items unassigned (RESUELTO 2026-07-02)
_chunk 1146 · 2026-07-14 · fuente: ingesta-2026-07-14_

RESUELTO 2026-07-02 — el data-fix SQL funcionó. RCS-27635 (Starbucks, reporter Nancy Sciascia): aplicar "admin abandon due to age" a todos los Work Items UNASSIGNED con periodo terminando el/antes del 3/29/2026 en su "Regional Review Work Flow". No borrar/deshabilitar; confirmado unassigned-only en comentarios.

Filtro correcto (SQL Server, tenant SBUX Platform DB): AssignedToUserID IS NULL AND StatusID = 0 AND PeriodToDateTime < '2026-03-30'.
- 3.905 WIs activos unassigned matcheaban (StatusID=0) → esos se abandonaron.
- 99.806 con el mismo periodo ya estaban en StatusID=3 (abandono previo) → no tocar.
- Ejemplo: Category "Discounts-All", Headline "Discounts - Cashier - txn with 0 tender and disc - fiscal period", CreatedDateTime 04/01/2026, PeriodEnd 3/29/2026.

Checklist previo al UPDATE (aplicado): perfilar por VirtualFilePath/SourceApp/Category + join workview.Team para confirmar workflow; nombre real de la Platform DB; AbandonReasonID del enum WorkviewAbandonReason del tenant; timezone de PeriodToDateTime vs 11:59:59 PM del screenshot. Backup + UPDATE batcheado + tabla de recovery.
Procedimiento general: ver chunk "Playbook — Admin-abandon masivo de Work Items en Secure" (folder RCS Procesos).
[Fuente: memoria de Daniel Buelvas, 2026-07-10]

## RCS-25547 · Canadian Tire — Token data incorrecto en transacciones CTP (client-side)
_chunk 914 · 2026-06-16 · fuente: https://trebuco.atlassian.net/browse/RCS-25547_

Cliente: Canadian Tire / CTC (label Support_Data_Team). Producto: tokenización vía PartSource POS.
Síntoma: las tarjetas tokenizadas muestran solo los últimos 3-4 dígitos en vez del token de 14-18 dígitos; faltaba información de maskedPAN.
Causa raíz: NO es defecto de Appriss. El cliente envía los archivos de token (LP_PS_Token .json.pgp) con retraso y sin los archivos de sales header / tender correspondientes; además 2 archivos llegaron cifrados con la clave equivocada. El maskedPAN sí se mapea correctamente (campo cardnumbermasked); el "CardNo" de 4 dígitos solo está mal etiquetado, no es un bug.
Fix: recarga histórica de datos (ene–mar), ~1 día completo de trabajo de ingeniería. Recomendación al cliente: corregir el retraso/origen de los token files para evitar nulls.
Tiempo: 119+ días, abierto (label 60daysopen). Prioridad: Medium. Tipo: Incident.
Lección de líder: "client error" es una resolución válida; documentar la dependencia del cliente para no asumir culpa propia ni rehacer el análisis.

## RCS-27644 · H&M — Cashier risk report sin datos: filtro 60 días + regresión ActionType 99 (DOS causas)
_chunk 1147 · 2026-07-14 · fuente: ingesta-2026-07-14_

El "data cliff" del cashier risk report de H&M (EU127/C127_HAM) tuvo DOS capas — la investigación evolucionó:

CAPA 1 (diagnóstico 2026-07-09, Daniel Buelvas): el search de Composer usa "Trans Date Within last 60 days" → corriendo el 9-jul el límite cae ~10-may, exactamente el go-live de SnowTime V2 para H&M. Los datos pre-10-may (cargados por pyardm) existen y están sanos, pero quedan fuera de la ventana. Mitigación enviada: cambiar el filtro a rango explícito (May 1–9). Datos verificados en Snowflake ARDM_PRODUCTION.C127_HAM: JOIN OPERATORACTION→HEADER May 1–9 = 11.393.996 matched, 0 unmatched.

CAPA 2 (investigación 2026-07-10 con Daniel Endersby, en vivo): al darle a Claude el SQL real del report apareció una REGRESIÓN genuina: el filtro del cliente hace ActionType NOT IN (…) y descartaba el 94% de los headers. pyARDM inyectaba una fila sintética de operator action con ActionType 99 ("no operator action") para CADA transacción sin OA real; SnowTime V2 no emite esas filas → el NOT IN ya no matchea nada. Legacy daba ~48% de transacciones con la fila 99. Fix hecho en la capa de mapping de SnowTime: si la transacción no trae OA en control transactions, crear la fila sintética 99 y recombinar. Validado en ARDM Lab sobre los 2 días del cutover: match pasó de 53% a 99.9% (discrepancia residual 0.08% explicada por ventana de llegada de datos).

Mapping de campos H&M (secure_Resource.json overrides): "Trans Date"=ARDM_HEADER.TradingDay; "Business Date"=ARDM_HEADER.BusinessDate (puede diferir en tiendas 24h); "Operater Action Type" (typo real)=ARDM_OPERATORACTION.ActionType (raw, NO StdActionType; pre-May-10 StdActionType=99 default de pyardm).
Lección: pedir/conseguir siempre el SQL del search (correr el report con parámetros dummy para ver el query) — fue lo que destrabó la causa raíz.
[Fuentes: memoria Daniel Buelvas 07-09 + call Daniel Endersby 07-10]

## RCS-23837 · GAP — Filas duplicadas en devoluciones ECOM (Engage)
_chunk 915 · 2026-06-16 · fuente: https://trebuco.atlassian.net/browse/RCS-23837_

Cliente: GAP (049) (label Support_Data_Team). Producto: Engage / reporte RAR.
Síntoma: devoluciones duplicadas en el Engage report; un mismo OrderNo aparece en varios feeds (NGPOS, LTLOG, ECOM-GDP) y se cuenta dos veces; afecta a consumidores en el RAR.
Causa raíz: el flag CompletedNonVoidCustTxnFlg debe ponerse a 0 para transacciones que ya aparecieron desde otro feed; es un problema de lógica de de-duplicación entre NGPOS / LTLOG / ECOM-GDP. Se complica cuando ECOM-GDP carga después de LTLOG o cuando LTLOG no trae order no.
Fix: varios PRs en Azure DevOps (DataOps/c049gap); correcciones de datos históricos vía SQL (UPDATE de flags por orderno y por endtransdatetime+ticketamount). El primer fix funcionó en test pero falló en producción. El trabajo reveló duplicados de LTLOG → generó el ticket RCS-25673 (overlap LTLOG/ECOM-GDP).
Tiempo: 231+ días; cerrado y reabierto ~3 veces; finalmente escalado a un equipo completo (Chris Howard, Flavio Smirne, Vishal Patel, Steve Carroll, Kellie Beckman). Prioridad: Critical.
Lección de líder: un ticket puede exceder al ticket y volverse proyecto; vigila el ciclo Complete→reabrir y escala a tiempo.

## RCS-27650 · GUESS — Cancel en Case Review devuelve 403 de nginx (capa proxy, no permisos)
_chunk 1148 · 2026-07-14 · fuente: ingesta-2026-07-14_

Botón Cancel en Case Review (módulo Secure Incident) devuelve página cruda "403 Forbidden" de nginx, reemplazando toda la app. Reproducido internamente.

Causa: el 403 viene de la capa reverse-proxy nginx, NO de la aplicación — no es tema de roles/permisos. El Cancel dispara una navegación/request que nginx bloquea antes de llegar al backend. Investigación arranca en nginx access.log/error.log + pestaña Network de DevTools durante la repro. Causa probable: location block faltante, regla WAF o restricción de método sobre la URL destino del Cancel.

Detalles: cliente GUESS (ID 117535), versión 6.26.6. Usuario probado: Stephanie Benedetti (rol Administrators). Flujo: System Selection → Secure Incident → Incident Main Menu → Case Review → Cancel. Case Review muestra "No data to display" antes del click. Doc de escalación preparado + comentario Jira listo para pegar manual.
Relacionado: Juan reportó 2026-07-10 a Chris Rippingale un caso análogo (error 403 al click en Back button) — Chris lo clasificó como incidente: si algo que funcionaba se rompió, es fix rápido/hotfix, no "sale en el próximo release".
[Fuente: memoria Daniel Buelvas, 2026-07-10]

## RCS-27140 · Alo Yoga — Fotos no aparecen en recibos de Appriss (Shopify)
_chunk 916 · 2026-06-16 · fuente: https://trebuco.atlassian.net/browse/RCS-27140_

Cliente: Alo Yoga (label Support_Data_Team). Producto: Secure 5 - EBR / receipt viewer. Integración: Shopify Plus.
Síntoma: las fotos de mercancía no aparecen en algunos recibos de Appriss aunque sí están en Shopify; a veces aparecen imágenes incorrectas.
Causa raíz: image_url es NULL en ardm_Item.extra_fields para ~16% de los items (1.355.744 de 8.695.552 en 30 días). El payload del evento de Shopify (Avro) no incluye URL de imagen cuando la variante de producto no tiene imagen propia asignada; OrderJsonToARDM.cs mapea NULL. El receipt viewer (detail-panel.html:234) usa un ng-if guard y no renderiza nada. NO es defecto de pipeline ni de viewer: es un hueco de datos de origen.
Fix (3 opciones): (1) [preferida] que Alo asigne una imagen a cada variante en Shopify; (2) fallback en el pipeline a la imagen del producto padre (cambio DataOps en OrderJsonToARDM.cs); (3) aceptar como by-design y documentarlo.
Tiempo: root cause estructurado en 7 días (modelo de buen triage, formato "Stage 4 – Root Cause Statement"). Impacto: Low (cosmético). Prioridad: High.
Lección de líder: el root cause temprano y metódico es lo que separa 7 días de 7 meses. Este es el estándar a replicar.

## Composer — Bug: no se puede borrar display field en Work Items legacy (leftExp undefined)
_chunk 1149 · 2026-07-14 · fuente: ingesta-2026-07-14_

Error: TypeError: Cannot read properties of undefined (reading '0'). Stack: composerApp.service.getDisplayFieldsInReferenceJoin → removeField → Object.removeDisplayField.
Archivo: Sources/UI/Components/src/scripts/Explorer/Content/Scripts/Services/composerService.js, función getDisplayFieldsInReferenceJoin (~línea 946).

Causa raíz: `referenceSearchJoinGroup[i].leftExp[0].description` crashea cuando leftExp es undefined (datos de WIs guardados antes de que leftExp se inicializara de forma confiable). La línea siguiente ya usa optional chaining para rightExp — inconsistencia.
Fix: `referenceSearchJoinGroup[i].leftExp?.[0]?.description ?? ""`.

Patrón de diagnóstico: borrar display field → crash JS → el campo no se elimina; crear un WI NUEVO desde el roto → la eliminación funciona (join conditions reconstruidas con defaults). Solo afecta WIs legacy.
Cómo aplicar: en cualquier ticket donde el cliente no pueda borrar un display field/columna en Composer, revisar la consola buscando este TypeError exacto antes de asumir otra causa.
[Fuente: memoria Daniel Buelvas, 2026-07-10]

## RCS-27542 · Boot Barn — Users cannot complete an audit (DBNull en Audit/CAMS) — RESUELTO por Juan
_chunk 1087 · 2026-07-02 · fuente: chat Claude 2026-06-26_

Cliente: Boot Barn. Producto: Audit (f.k.a. CAMS / LPMS). Prioridad: High, Incident. Primer ticket manejado end-to-end por Juan (26-jun-2026, Camila OoO, J.R. Teagle lo @mencionó).

Síntoma: al marcar un audit como completado (Mark Audit Completed → Save) sale "Something Unexpected Happened" (500). NO afecta a todos los audits — es data-dependent.

Root cause (Carlos): DBNull donde se espera string en Audit_UpdateAuditStatus, archivo UpdateAuditStatus.aspx.vb línea 416 (vive en el server F:\\IIS\\Clients\\bootbarn\\, no en el repo). Revienta solo en registros con ese campo NULL. Por eso Kiran no reprodujo: probó store 0456 (audit 90535) que SÍ guardaba, mientras 0286 (90380) fallaba. Afectaba ConfigID 108 (Quarterly Audit Systems & Equipment), 129 (FY27 DM OSR), 131 (FY27 Store OSR).

Reproducción: VM qa-lpms-rdp-001 (Azure Bastion) → nettrack Boot Barn → Compliance Audit System → Search por Store No (PROHIBIDO desmarcar "Show My Audits Only") → Edit audit → Mark Audit Completed → Save → 500.

Workaround verificado: en el audit fallido, entrar a Modify Audit Date/Times, RE-GUARDAR Audit Date y End Date (ya seteadas) y luego Mark Audit Completed → Save. El re-guardado repuebla el campo NULL. Verificado: fila pasó a Audit Completed = Yes.

Lecciones: (1) un workaround probado UNA vez ≠ workaround oficial — antes de decírselo al cliente se necesita sign-off de Engineering + verificarlo en otro tipo afectado; (2) no asignarse el ticket si no lo piden ("leave that with Kiran"); (3) reply al cliente: neutral, sin sobre-prometer, sin jerga interna. Resultado: reproducido, cliente respondido en SLA, movido a Under Engineering Review.

## RCS-27573 · Tahoe Donner — Incident types fallan al crear reporte (tabla ACCIDENTEQUIPMENT faltante, migración DB-only) — RESUELTO por Juan
_chunk 1088 · 2026-07-02 · fuente: chat Claude 2026-07-02_

Cliente: Tahoe Donner. Producto: Secure Incident (LPMS). Segundo ticket de Juan (jul-2026). Kristin lo linkeó a RCS-27542 (Boot Barn) pensando "mismo issue" — NO lo era: misma pantalla genérica de error, causa totalmente distinta. Aquí Kristin SÍ pidió auto-asignarse.

Síntoma (Ian Carr, cliente): no puede crear incident reports de ciertos tipos — Guest Injury Summer/Winter y First Aid Refusal fallan; Facility y Property Damage funcionan. Ese contraste guió la reproducción (repro del tipo fallido + PRUEBA DE CONTROL con un tipo que funciona).

Root cause: la pantalla "Something Unexpected Happened" tiene link "Technical Details" con el stack trace completo (mejor que el log). Error: DAL.ReadDataTable: Invalid object name 'ACCIDENTEQUIPMENT' en SummerPageGeneralLiability.aspx.vb:1113. La tabla ACCIDENTEQUIPMENT no existe en la DB del tenant: Tahoe Donner es cliente de MIGRACIÓN DB-ONLY (asterisco * en el Customer Server Profile Incident/Audit → usa la platform DB, no lpguys; app server node-m / pd-lpms-iis-015) y la tabla no se migró. Solo fallan los tipos que la consultan.

Efecto secundario: "Start New Incident → Next" CREA un case shell en el sistema en vivo del cliente aunque la página reviente después. Hay que borrar/void los casos de prueba (menú "..." de la fila) y documentarlo en la nota interna.

Escalación: Under Engineering Review (AALPS/Engineering) — NO a Database Services (eso es solo Greenplum; Tahoe Donner es SQL Server/Azure MI). Estado cambiado ANTES del reply al cliente para no sobre-prometer. URL nettrack: apps.lpguys.net/{cliente}/nettrack/.

Patrón reutilizable: "tabla faltante por migración DB-only" — si un cliente DB-only falla solo en ciertos tipos/pantallas con Invalid object name, sospechar tabla no migrada.

## TJX Identify linking — trío de tickets 27-jul (RCS-27984/27987/27979) y criterio de respuesta
_chunk 1409 · 2026-07-28_

TJX Canadá/US levantó 3 tickets el 27-jul-2026 sobre "Linked Activity / Identify linking" en la Consumer ID page.

VEREDICTO DE INGENIERIA (Ian Williams + Hao Nguyen, dueno del dato): un consumidor SOLO aparece como perfil vinculado en Identify si ese consumidor tiene actividad en Engage (TRE). Sin actividad Engage -> "Linked Activity of this ID not found" y en Identify search "no profiles containing that ID". Esto es ESPERADO/por diseno ("not every group loads in Identify — always been true"). Los consumidores de los ejemplos se buscaron por Identify General Search, no por Engage Consumer ID.

LOS 3 TICKETS:
- RCS-27984 (reporter Owen Booth, Consumer 6097981) = el bug REAL (permisos), YA resuelto y CERRADO (Anil P). Es el "otro" que menciona Ian.
- RCS-27979 (reporter Karina Thomas, "Profile not loading", perfil con historia 2024 no carga por email/phone) = Under Solutions Expert Review, dueno MARISSA JOHNSON. Es el caso que Kristin menciono en el KT ("pull a profile history back to 2024 will not pull -> ask Marissa"). NO es de soporte.
- RCS-27987 (reporter Tatiana Manchavrakos, TJX Canada; Cody De la Cuba respondio "still broken") = Under Support Review, SIN asignar = EL UNICO EN CANCHA DE SUPPORT (Juan).

CRITERIO DE RESPUESTA en RCS-27987 (NO cerrar como "resuelto"): el ticket tiene 4 sintomas; 3 (magnifying glass error, "No information found", "no profiles containing that ID") = comportamiento esperado (requiere actividad Engage). El 4o ("profile fails to load ~50% via other methods") NO esta confirmado como esperado. Responder: (1) explicar el requisito de actividad Engage, (2) pedir Consumer IDs concretos que SI tengan actividad Engage y no linkeen, o un perfil alcanzable que falle al cargar, para separar lo esperado de un defecto real y, si lo hay, devolver a Ingenieria. Asignarse el ticket. Respuesta neutral/no-tecnica por skill appriss-jira-support.

Aparte: RCS-28002 (TJX access a RTIaaS portal) es acceso, ya asignado a Tom Duncan — no es de este grupo. Contexto: Ayesha Mehar reenvio a Camila+Juan el pedido de Ian de responder el ticket abierto.

## Esquema de usuarios y jerarquias en Incident (explicado por Kiran Vadday)
_chunk 1419 · 2026-07-30 · fuente: Teams / Kiran Vadday 2026-07-30_

Explicado por Kiran Vadday (bvadday@apprissretail.com) el 30 de julio de 2026, despues de dos discrepancias en las que ella y yo mirabamos capas distintas del mismo problema.

LLAVES DE COMPARACION CORRECTAS (nunca por ID numerico)
- membership.Users: columna username
- incident.lpuser (vista): columna loginid o email
- incident.lpuser2: columnas loginid y emailaddress

RUTA DE LA MIGRACION
incident.lpuser2 se migra hacia membership.Users Y hacia secure.LocationHierarchyUserAssignments (lhua). Los usuarios que originalmente vivian en el esquema incident se migran al lado secure.

FUENTE DE VERDAD
Para clientes que son solo Incident, la fuente de verdad sigue estando en el esquema incident, principalmente la vista lpuser. Pero esa vista esta construida a partir de membership.Users mas incident.lpuser2.

REGLA OPERATIVA (textual de Kiran)
"Secure.lhua y lpuser view both must be checked". Las dos, no una.

LOS DOS ERRORES QUE CAUSARON LAS DISCREPANCIAS
1. Usar un umbral numerico de UserID para delimitar el bloque nuevo de unificacion. No sirve: hay clientes cuyos IDs nativos ya estan en ese rango. ADUSA arranca en 1.800 millones, y por eso una query devolvio 2.300 falsos positivos.
2. Reportar una sola ruta de join. Unir por incidentUserID y unir por email dan respuestas distintas y las dos son ciertas: la fila puede existir por email con el vinculo incidentUserID vacio. Siempre sacar las dos rutas en columnas separadas y clasificar el estado.

CASO QUE LO ORIGINO
RCS-28023 (ADUSA, usuarios sin poder crear casos por restriccion de division) y la investigacion de los 13 usuarios ausentes de membership.Users en la ola de migracion del 27 de julio de 2026.

## Jerarquia de ubicaciones en Incident — como se resuelve el alcance de distrito
_chunk 1477 · 2026-08-11 · fuente: sesion 2026-08-10/11_

VERIFICADO CON SQL EN EL TENANT 433 (VITAMIN SHOPPE), 10 AGO 2026.

TABLAS
structure.LocationHierarchyMaster define la forma de la jerarquia. En 433 son 4 niveles: Company, Division, Region y District en el nivel 4.
place.Location lleva columnas planas LocationHierarchy1..6 mas sus Descriptions, una fila por tienda.
secure.LocationHierarchyUserAssignments (LHUA) guarda el alcance por usuario. Cada fila apunta a un LocationId concreto o a un valor de nivel de jerarquia.
incident.Store lleva StoreIdent, StoreNo, Region, District y DistrictManagerID.
incident.LPUser es una VIEW sobre incident.LPUser2. El puente desde Secure es membership.Users.IncidentUserID (int) hacia incident.LPUser2.UserID (int).

EL HALLAZGO
En 433 las 884 filas de LHUA estan asignadas por LocationId. Cero usan las columnas de distrito, region o division. El alcance de distrito no se asigna, se hereda del distrito de la tienda asignada.

Y solo se hereda del StoreIdent primario. Verificado en cuatro usuarios: cada uno ve el distrito de su StoreIdent primario y nada del secundario, incluso cuando el secundario esta en otro distrito y la persona figura como DistrictManagerID de ese otro distrito.

Mapeo comprobado en incident.Store:
617 = tienda 249 Tanasbourne OR = distrito 504, DM 10419 Dayna Rivera
466 = tienda 500 Everett WA = distrito 501, DM 10419 Dayna Rivera
596 = tienda 226 Centennial CO = distrito 210, DM 52508 Journey Armstrong
548 = tienda 177 San Jose CA = distrito 305
615 = tienda 247 Round Rock TX = distrito 213, DM 13034 Daniel Garza
539 = tienda 167 Fresno CA = distrito 303
391 = tienda 75 Norwalk CT = distrito 108, DM 8510 Gisele Pohl

CONSECUENCIA PRACTICA
Un usuario que gestiona dos distritos no se resuelve desde Support. Agregar una segunda fila en LHUA a mano desde Control Panel no le da el segundo distrito, solo la tienda. La pestana Hierarchies de Control Panel no es el mecanismo de distrito.

COMO DISTINGUIR MIGRACION DE EDICION MANUAL
La migracion creo una sola fila LHUA por usuario. Si un usuario tiene dos filas y la segunda tiene un HierarchyUserAssignmentId igual o cercano al total de filas de la tabla, esa fila se agrego a mano despues.

QUE SE DESCARTO CON EVIDENCIA, NO REPETIR
Grupos de permisos (identicos entre los cuatro usuarios), estado de cuenta (Locked, Disabled y Deleted en false), mapeo Secure a Incident (los cinco usuarios resuelven bien, las 16 filas rotas son cuentas internas trebu.co y es lo esperado), cuentas duplicadas de la unificacion (cero emails duplicados), feature flags de sesion (ambos True en 433), datos maestros de distrito (501, 504 y 210 existen con sus tiendas), SupervisorFlag y SecurityID (identicos en los cuatro).

## Acceso SQL a las bases de tenant, nomenclatura y barrido cross-database
_chunk 1478 · 2026-08-11 · fuente: sesion 2026-08-10/11_

ACCESO
Azure Bastion hacia SSMS, Managed Instance sqlmi-prd-wus2-arp-001. Login de Juan: jmartinez@trebu.co.

NOMENCLATURA
Las bases de tenant se llaman sqldb-prd-wus2-arp-production-NNN-xxx-platform, donde NNN es el Client ID y xxx el codigo corto del cliente. Las bases ya no llevan nombre de compania, solo numero de cliente. Por eso el Client ID es obligatorio al inicio de todo comentario interno, como lo pidio Kiran.

Client IDs conocidos:
209 = Tailored Brands (tbi)
423 = Stater Bros (sbs)
433 = Vitamin Shoppe (vse)

BARRIDO CROSS-DATABASE
Para revisar la misma cosa en todos los tenants: leer sys.databases filtrando state = 0 AND database_id > 4 AND name LIKE '%platform', construir SQL dinamico con QUOTENAME(name), insertar en una tabla temporal, EXEC sp_executesql, y hacer el pivot al final con MAX(CASE WHEN ...).

GOTCHA QUE COSTO UNA SESION
SQL Server compila el batch completo antes de ejecutarlo. Si la tabla temporal ya existe en la sesion con un esquema viejo, el SELECT final se resuelve contra el esquema viejo y sale Msg 207 Invalid column name, aunque el batch tenga un DROP TABLE arriba. La solucion es usar un nombre nuevo de tabla temporal, no arreglar el DROP.

REGLA
Todo lo que se corre en produccion es de solo lectura. Diagnostico si, cambios nunca.

## Feature flags: viven en secure.ConfigurationItem y el valor efectivo es CustomerEditedValue
_chunk 1479 · 2026-08-11 · fuente: sesion 2026-08-10/11_

Los items de configuracion de features estan en secure.ConfigurationItem, NO en incident.ConfigurationItem, aunque el nombre del flag empiece por Feature.Incident. Verificado el 10 ago 2026 en el tenant 433.

Columnas que importan: Name, DataType, Value, CustomerEditedValue, CustomerEditedDateTimeUtc, IsVisible.

EL VALOR EFECTIVO PUEDE SER CustomerEditedValue, no Value. Por eso Matt Kamminga insiste en verificarlos en la base y no en Control Panel: Control Panel puede mostrar una cosa y el sistema estar leyendo otra. Al consultar usar siempre ISNULL(CustomerEditedValue, Value).

FLAGS CONOCIDOS
Feature.Incident.EnableAdHocInitCaching
Feature.Incident.EnableAdHocPerRequestUserScope
Feature.Incident.EnableBlobAppendLogging

Los dos primeros quedaron en false en 209-tbi despues de un release del 6 ago 2026 porque faltaban en el historial de seed y el default es false. Ese es el patron a buscar cuando un tenant se degrada justo despues de un despliegue: no es que alguien los apagara, es que nunca se sembraron.

## Descarga de PDF rota: ERMS sube los archivos al directorio lpms
_chunk 1480 · 2026-08-11 · fuente: sesion 2026-08-10/11_

Causa raiz confirmada por Kiran Vadday en Teams el 10 ago 2026, sobre RCS-28124.

El modulo ERMS sube los archivos al directorio de lpms, y por eso la descarga despues falla. Mitigacion inmediata: copiar los archivos al lugar correcto. Arreglo de codigo en release y en main, con cherry-pick al historial de release.

Encaja con lo observado el 4 ago en ADUSA: 7 de 7 archivos de Stop & Shop descargaban bien y 12 de 12 de las otras marcas fallaban con ERR_RESPONSE_HEADERS_MULTIPLE_CONTENT_DISPOSITION. Misma familia de problema, el archivo no esta donde el descargador lo busca.

Cuando vuelva a aparecer una falla de descarga de PDF, la primera pregunta es por que modulo se subio el archivo.

## Regla de redaccion: el hallazgo interno nunca se le cuenta al cliente
_chunk 1481 · 2026-08-11 · fuente: sesion 2026-08-10/11_

Correccion de Juan, repetida dos veces el 10 ago 2026.

La forma correcta del comentario al cliente cuando se necesita evidencia es literal: saludo, una linea tipo "based on what we have so far we need a bit more to keep moving", la lista de lo que se pide, gracias. Punto. Nada mas.

Juan lo dijo asi: "solo necesito que lo saludes, le digas que en base a la informacion necesitamos lo siguiente para tener mas evidencia y avanzar con el caso".

NO VA AL CLIENTE: el analisis, el mecanismo tecnico, nombres de empleados o equipos internos, problemas de otros clientes, fechas o hallazgos internos, codigos de error, nombres de infraestructura. Todo eso va al comentario interno.

Casos reales donde se devolvio el borrador el mismo dia:
RCS-28256, el borrador llevaba el 524 de Cloudflare, la regresion de planes y el CommandTimeout.
RCS-28032, el borrador le explicaba al cliente que su usuaria era la unica configurada en dos distritos y que solo uno tomaba efecto.

ADEMAS: al pedir evidencia de un reporte funcional, siempre pedir la URL de la pagina, no solo la captura y la hora. Kiran: "with the url in hand, we can verify what our queries are looking at". Sin URL no se puede saber que consulta corre la pagina.

## ARDM: rastrear un campo de la pantalla hasta la tabla de referencia que lo rompe
_chunk 1482 · 2026-08-11 · fuente: llamada Peyman 2026-08-11_

VERIFICADO EN PANTALLA CON PEYMAN MOTLAGH, 11 AGO 2026, RESOLVIENDO RCS-28077.

LAS TRES TABLAS DE REFERENCIA
reference_product: la especificacion de cada articulo del inventario del cliente. La llave es article_id, que es el SKU.
reference_location: una fila por tienda, con direccion, apertura y cierre.
reference_employee: el maestro de empleados.
Casi todo problema de "un campo salio vacio o repetido" cae en una de las tres. En DBeaver aparecen ref_product y reference_product juntas; la buena es reference_product.

EL METODO
1. Del nombre de la columna al nombre de la tabla. En el resultado de la busqueda se leen prefijos: si las columnas dicen item, el dato sale de la tabla item.
2. De la tabla al script que la carga. En el repositorio del cliente: SQL / load ARDM scripts / load_ardm_item. La convencion de nombres es literal.
3. Ctrl+F por el campo. Buscando receipt aparece item_receipt_description.
4. Leer el join. Ese campo viene con alias RP, o sea reference_product, unido por article_id. Si reference_product tiene N filas para un article_id, el join multiplica por N las lineas del item.

POR QUE EL AGREGADO SALE BIEN Y EL DETALLE NO
El nivel agregado de la busqueda no hace ese join. Por eso el resumen por tienda estaba correcto y solo el drill down mostraba seis copias de cada articulo.

COMO USAR CLAUDE EN ESTE PASO
Consejo explicito de Peyman: no pasarle el numero de RCS y esperar el diagnostico. Pasarle la ruta del repositorio del cliente y preguntarle donde se construye ese campo concreto. La pega: no devuelve el numero de linea.

ACTUALIZACION COMPLETA O INCREMENTAL
Unos clientes reemplazan la tabla de referencia entera en cada carga y otros mandan solo lo que cambio. Una fila con updated_datetime viejo no significa dato podrido, puede ser que ese registro no haya cambiado. Consecuencia: si el cliente arregla datos de su lado y manda incremental, solo se corrigen los registros que el reenvie.

## Greenplum o Snowflake: como saber a que motor pega una pantalla, y por que importa
_chunk 1483 · 2026-08-11 · fuente: llamada Peyman 2026-08-11_

VERIFICADO EL 11 AGO 2026 EN AHOLD, CLIENTE 112.

Un cliente puede ser mixto: unas pantallas leen de Greenplum y otras de Snowflake. Peyman dedupo reference_product en Greenplum, refresco la aplicacion, purgo cachés, y la pantalla seguia mostrando seis filas. La causa no era el cache: esa consulta iba a Snowflake.

COMO SE DISTINGUE
En la busqueda se puede ver la consulta que la aplicacion manda a la base. Con esa consulta a la vista:
Greenplum arma un CTE, un WITH al principio. Es su firma.
Snowflake no. Si no hay CTE, estas mirando Snowflake.
Palabras de Peyman: "this is very much green plum, you don't see that in Snowflake". Y sobre el conjunto: "see how confusing it is".

LA REGLA
Antes de corregir datos, mira la consulta real de la pantalla y confirma el motor. Si la pantalla no cambia despues de un cambio de datos, la primera hipotesis no es el cache, es que corregiste la base equivocada.

POR QUE SE CORRIGEN LAS DOS
El flujo es Greenplum primero y de ahi se copia a Snowflake. Arreglar solo Snowflake da un resultado que dura hasta la siguiente carga: "if you fix Snowflake but we don't fix this, next time it runs it will cause problem".

CACHE
En Control Panel estan Clear client translation cache y Clear system cache, y hay que elegir el cliente antes de purgar. Pero la leccion de la llamada es la contraria a la esperada: se purgo varias veces y nunca era el cache.

## Respaldar y deduplicar una tabla de produccion en Greenplum y Snowflake
_chunk 1484 · 2026-08-11 · fuente: llamada Peyman 2026-08-11_

VERIFICADO EN PANTALLA, 11 AGO 2026. Peyman: "we don't have a lot of guardrail to stop people from doing the wrong thing".

BACKUP EN GREENPLUM
1. Click derecho sobre la tabla, Generate SQL, DDL.
2. Copiar, abrir un editor SQL nuevo, pegar.
3. Cambiar el nombre a BKUP_20260811_<tabla>, con la fecha del dia.
4. Ejecutar. Queda la tabla vacia con la misma estructura y los mismos permisos que la original. Se hace por DDL y no con CREATE TABLE AS precisamente por eso.
5. INSERT INTO backup SELECT * FROM original;
6. Contar las dos y comparar.

NUNCA NOMBRAR EL BACKUP EMPEZANDO POR EL NOMBRE DE LA TABLA DE REFERENCIA
El codigo que escribio Luke para copiar las tablas de referencia a Snowflake todos los dias toma cualquier cosa que se llame reference_product* y la considera tabla a copiar. Un backup llamado reference_product_bkp termina viajando a Snowflake. Por eso el prefijo va adelante.

BACKUP EN SNOWFLAKE
Click derecho sobre la tabla, Clone, y nombre con la fecha.

ENCONTRAR DUPLICADOS (sirve igual en Greenplum y Snowflake)
SELECT article_id, COUNT(*) AS cnt FROM ardm_112.reference_product GROUP BY article_id HAVING COUNT(*) > 1 ORDER BY cnt DESC;

POR QUE DISTINCT NO FUNCIONA
INSERT INTO ... SELECT DISTINCT * devuelve los mismos duplicados porque las filas no son identicas: difieren en inserted_datetime. DISTINCT compara la fila entera.

LO QUE SI FUNCIONA, quedarse con la ultima fila por llave:
SELECT DISTINCT ON (article_id) * FROM ardm_112.reference_product ORDER BY article_id, inserted_datetime DESC;

SECUENCIA COMPLETA
backup poblado y contado, truncate de la tabla original, INSERT del resultado deduplicado, volver a contar duplicados por llave y confirmar que da 1, y por ultimo abrir la aplicacion y correr la busqueda del cliente con el mismo filtro. Esa ultima es la unica verificacion que cuenta.

REGLAS DURAS
Nada de truncate ni drop en produccion sin backup ya poblado y contado. El backup se borra despues de verificar, no antes. Confirmar el esquema antes de crear nada. Colorear las conexiones de DBeaver, verde dev y rojo produccion.

## Instancias de Greenplum por cliente, el Product Delivery Client Matrix y el acceso a los clusters
_chunk 1485 · 2026-08-11 · fuente: llamada Peyman 2026-08-11_

VERIFICADO 11 AGO 2026 contra el Excel y contra lo visto en pantalla.

EL PRODUCT DELIVERY CLIENT MATRIX
Excel de una hoja, Clients, 373 filas, una por cliente. Trae ID, codigo de tres letras, instancia de Greenplum, esquema ARDM, version, plataforma y POS. Es la forma mas rapida de ubicar un cliente. Lo mantiene el equipo a mano y tiene filas viejas: dice CRDM para Ahold cuando ya es GP. Sirve para orientarse, no para citarlo en un ticket.

FILAS VERIFICADAS
67 NKE Nike, GP11, ardm_067
112 AHL Ahold, GP9, ardm_112
138 NOR Nordstrom, GP9, ardm_138
164 COP Coop UK, GP8, ardm_164
176 UNS Marks & Spencer, GP6, ardm_176
209 TBI Tailored Brands, GP9, ardm_209

DOS LECTURAS QUE SALEN DEL MATRIX
BYF es Big Y Foods, cliente 362. Cierra la pregunta abierta de la pagina de Confluence de la ola de unificacion sobre el cliente de RCS-28153.
Los clientes nuevos no tienen instancia de Greenplum: 362 BYF, 378 GEL, 423 SBS, 433 VSE, 438 TGJ y 505 ALO estan vacios porque nacieron en la plataforma nueva. Si un ticket de esos habla de ARDM, algo no cuadra.

LAS OTRAS DOS FORMAS DE UBICAR LA INSTANCIA
Azure DevOps, proyecto DataOps: el icono azul son los pipelines, buscar por numero de cliente o por codigo de tres letras y el nombre del job trae la instancia. El icono naranja son los repositorios de codigo.
O por el esquema, que se llama ardm_<id> a tres digitos. En Snowflake es ARDMPROD.ARDM_<id>.

ACCESO A LOS CLUSTERS (Confluence R&D, pagina Cluster Access, 478097309697)
Todos por un salto al jump server LA4, 10.22.0.220 por RDP con credenciales trebu.co.
GP3, GP6 y GP9 son on premise: SSH por alias DNS con credenciales gpadmin del password book.
GP1 y GP11 estan en Azure y usan llave gp5newnew.ppk, no contrasena.
GP1 es dev y QA. Las conexiones de produccion llevan appriss en el nombre, las de dev llevan dev.

CLONAR UNA CONEXION EN DBEAVER PARA SALTAR DE INSTANCIA
Click derecho Copy, click en blanco Paste, renombrar, Edit connection y cambiar el numero de la instancia en el host. Todo lo demas queda igual.

LOS ARCHIVOS CRUDOS
p-ingest-<region>/<id>_<CODIGO>/Archive/Prod/<fecha>. Ahi se ve lo que el cliente realmente mando. Para Nike la ruta es //p-ingest-fsla4/067_NKE/Archive/Prod con mascara *NIKE_Store_Location*. La pagina de Confluence Clients Files, espacio RTS, 474617381084, tiene la tabla de que archivos esperamos de cada cliente con mascara y horario.

AVISO 2026-08-28. La seccion LOS ARCHIVOS CRUDOS de arriba quedo parcialmente obsoleta. Los 13
clientes de GP11, incluido el ejemplo de Nike 067_NKE, ya no exponen sus archivos recientes en
p-ingest. Pasaron al file share \\stprdwus2shrdtlog.file.core.windows.net\<codigo>. El resto del
chunk sigue vigente. Ver el chunk titulado "p-ingest ya no tiene los archivos crudos de los 13
clientes de GP11" en la carpeta Data Pipeline & DevOps.

## Caso RCS-28077: seis copias de cada producto en reference_product de Ahold
_chunk 1486 · 2026-08-11 · fuente: llamada Peyman 2026-08-11_

ESTADO AL 11 AGO 2026.

SINTOMA
Las busquedas de refunds de Ahold devolvian cada articulo seis veces en el drill down. El nivel agregado por tienda salia bien. El sitio de QA no reproducia el problema.

CAUSA CONFIRMADA
reference_product de ARDM 112 tiene seis filas por article_id. En p-ingest hay seis archivos de producto con timestamps distintos y el pipeline los reprocesa todos en cada corrida.

LA CORRECCION IMPORTANTE AL ANALISIS DEL 31 DE JULIO
No es la resaca de las seis ejecuciones del 30 de julio. La tabla se reconstruye entera en cada carga: el 11 de agosto todas las filas tenian INSERTEDDATETIME de ese mismo dia entre 09:25:16 y 09:26:31. Cada carga vuelve a escribir seis copias. Por eso la limpieza sola no resuelve, aguanta hasta la siguiente corrida.

QUE SE HIZO
Backup y dedup en Greenplum GP9, y otra vez en Snowflake porque esa pantalla lee de Snowflake. Verificado en la aplicacion: la busqueda refunds-giant food con Article ID igual a 43 paso de seis lineas a una.

PENDIENTE
El cambio de codigo en el load de reference_product para tomar solo el archivo mas reciente. Escrito en la rama dev_pm de Peyman en el repo del cliente 112, sin probar. Se prueba en GP1. Hasta que este en produccion el ticket no se cierra.

SIN RESPUESTA
Que disparo las seis corridas del 30 de julio, y si otros clientes en pyardm legacy tienen el mismo patron.

DETALLE QUE CONFUNDIO DURANTE LA VERIFICACION
La busqueda del cliente traia un gift card en el header que no tenia article_id, y por eso las primeras corridas daban resultados que no cuadraban. No era el arreglo, era el filtro.

## Caso RCS-28003: direcciones vacias en los recibos de Nike, el dato llega vacio del feed
_chunk 1487 · 2026-08-11 · fuente: llamada Peyman 2026-08-11_

ESTADO AL 11 AGO 2026.

Se creo el 28 jul para aislar el tema de la direccion de RCS-27724.

CAUSA
Desde la modernizacion del feed de junio (cambio de Ryan DeVries a produccion el 22 jun, con el commit de SnowTime de Daniel Endersby el mismo dia), la ubicacion se lee del blob //p-ingest-fsla4/067_NKE/Archive/Prod con mascara *NIKE_Store_Location*. La migracion cambio el formato de CSV a JSON, la estructura de columnas del destino no cambio.

El recibo de Secure 5 resuelve la direccion desde reference_location. El vacio del recibo es el vacio que llega en el feed. Nada de nuestro lado lo reescribe. No hay cambio de codigo nuestro pendiente.

EJEMPLO DEL REGISTRO QUE LLEGA VACIO
LocationNumber 37, Nike Value Store Gilroy, con ShippingStreet, ShippingCity, ShippingStateProvince y ShippingZipPostalCode todos en blanco.

EL FEED ES INCREMENTAL
No reemplaza todas las tiendas en cada corrida. Un arreglo del lado de Nike solo se ve en los registros que ellos reenvien. Eso es lo que hay que explicarle a Joe Haffey, que el 10 ago pregunto si ya vemos todas las tiendas despues de que Nike Tech actualizo el reporte.

EL TICKET PADRE, RCS-27724
Sigue en Under Support Review desde el 8 de julio, High. Sebastian dejo el analisis completo de la migracion de POS Aptos a AssistInCloud: 8 campos afectados, 3 arreglables con COALESCE en los scripts ARDM con 2 a 3 dias de esfuerzo, 5 requieren que Nike cambie la configuracion de su POS. Bloqueado en una decision que nadie ha tomado.

## Triage de un bloqueo de Cloudflare: contenido o pais, y por que sin Ray ID no se agrupa
_chunk 1488 · 2026-08-11 · fuente: sesion 2026-08-11_

VERIFICADO EL 11 AGO 2026 CON LA CAPTURA DE RCS-28282 (CO-OP).

LA PAGINA DE BLOQUEO DICE EL MOTIVO
El texto que ve el usuario incluye: "several actions that could trigger this block including submitting a certain word or phrase, a SQL command or malformed data". Eso es una regla WAF gestionada disparada por el CONTENIDO de la peticion, no una regla de pais ni de IP. Es la distincion que llevabamos sin resolver desde el 30 de julio en la ola de unificacion.

SIN RAY ID NO SE IDENTIFICA LA REGLA
El Ray ID esta al pie de la misma pagina de bloqueo. Cuando el cliente manda un recorte casi siempre falta. Lo que se le pide: bajar el scroll del modal y capturar el pie, mas la hora exacta con zona horaria.

DOS SINTOMAS QUE SE PARECEN Y NO SON LO MISMO
Bloqueo AL ENTRAR a la aplicacion, sin sesion. Vitamin Shoppe, cliente 433, producto Incident LPMS: RCS-27766, RCS-28175, RCS-28214, RCS-28289.
Bloqueo CON LA SESION YA ABIERTA, al pedir una pantalla concreta. Co-op, cliente 164, producto Secure 5 EBR, RCS-28282, al abrir el receipt view desde Transaction Details.
Cliente distinto, producto distinto, region distinta, sintoma distinto. NO enlazarlos hasta que un Ray ID confirme si es la misma regla. Dejar la relacion escrita en el comentario interno como hipotesis, con lo que falta para confirmarla.

UN 524 NO ES UN BLOQUEO
Error 524 es timeout del origen: la peticion paso por Cloudflare y el servidor no respondio a tiempo. Un bloqueo es la pagina de WAF. Matt los separa explicitamente, asi que hay que decir cual de los dos es, o el equipo busca la causa de un bloqueo que no existe.

FORMATO CON EL QUE SE ENTREGA EL DATO AL EQUIPO
Ticket, cliente, Ray ID, hora con zona, host, y si es block o timeout. Nada mas. Si el cliente no revelo su IP se omite, no se inventa.

RUTA
Con el Ray ID en mano, Under Infrastructure Review. En esa ruta el assignee se queda con el ticket y es quien comunica y cierra.

## Reparto de la cola RCS: capacidad real, duenos por bucket y el filtro que se queda corto
_chunk 1489 · 2026-08-11 · fuente: sesion 2026-08-11_

SESION DEL 11 AGO 2026. La cola paso de 46 sin asignar a 24 el mismo dia.

EL HALLAZGO QUE HAY QUE REPETIR EN CADA REPARTO
La capacidad real del equipo con dos personas fuera eran unos 22 tickets contra 45 esperando. Repartir todo no es un plan, mueve el atasco de la cola a las colas individuales, que es exactamente lo que paso el 3 de agosto. Mejor repartir lo que cabe y dejar el resto agrupado con dueno propuesto.

DUENOS POR BUCKET (propuesta de J.R., derivada de lo que cada uno ya tenia, no inventada)
Login, acceso, permisos, WAF: Juan
Attachments y print docs: Diego
Reports, exports, Izenda: Vedant
Alerts y notifications: David Vargas
Data integrity y feeds: Viraj y Bikash
Location hierarchy: Edwin
Timeouts y latencia: Gulshan
UI behavior: Nikita

EL FILTRO 29803 SE QUEDA CORTO
Devuelve menos que la consulta directa porque no indexa lo que entra el mismo dia. Para un barrido completo:
project = RCS AND assignee IS EMPTY AND statusCategory != Done

COBERTURA DE LOS QUE ESTAN FUERA
Los tickets de una persona ausente nunca aparecen en la cola sin asignar, asi que ningun reparto los toca. Hay que sacarlos a mano. Sebastian Rueda tenia 13 abiertos con dos High al irse.

VERIFICAR DESPUES DE REPARTIR
Al dia siguiente conviene correr la lista contra Jira y comparar assignee real contra propuesto. En este reparto 23 de 25 se aplicaron tal cual, y las dos que se desviaron eran las dos de la misma persona, que termino sin un solo ticket. Eso solo se ve verificando.

## Regresion de plan de ejecucion en SQL Server: el estimador de cardinalidad 140 contra 160
_chunk 1491 · 2026-08-17 · fuente: moscu://memoria/2026-08-13_

FIRMA DEL CASO
La misma consulta, el mismo query_id, pasa de subsegundo a decenas de segundos de un dia para otro, sin despliegue de codigo y solo en algunos tenants. Eso no es carga ni red, es un plan nuevo.

HALLAZGO ORIGINAL (Tailored Brands, 10 ago 2026)
Las consultas de LPUser promediaban 0,5 a 0,8 s hasta el 5 de agosto y saltaron a 57 s de promedio con maximo de 120 s desde el 6 de agosto 17:35 UTC. Mismos query IDs, planes distintos. Los planes buenos se compilaron con estimador de cardinalidad 140 y los malos con 160. Las 137 bases de produccion estan en nivel de compatibilidad 160 y solo 3 de las 39 que corren la consulta se degradaron: el nivel es la condicion, no la causa; el disparador es la recompilacion.

NIVEL DE COMPATIBILIDAD
SELECT name, compatibility_level FROM sys.databases WHERE name = DB_NAME();

PLANES Y ESTIMADOR DE LOS ULTIMOS DIAS
CardinalityEstimationModelVersion es un atributo XML de StmtSimple dentro de query_plan.

WITH planes AS (
  SELECT q.query_id, p.plan_id, p.is_forced_plan,
         CAST(p.query_plan AS xml).value(
           '(//*:StmtSimple/@CardinalityEstimationModelVersion)[1]','int') AS ce_version,
         rs.count_executions, rs.avg_duration, rs.max_duration, i.start_time
  FROM   sys.query_store_query q
  JOIN   sys.query_store_query_text t ON t.query_text_id = q.query_text_id
  JOIN   sys.query_store_plan p ON p.query_id = q.query_id
  JOIN   sys.query_store_runtime_stats rs ON rs.plan_id = p.plan_id
  JOIN   sys.query_store_runtime_stats_interval i
         ON i.runtime_stats_interval_id = rs.runtime_stats_interval_id
  WHERE  t.query_sql_text LIKE '%LPUser%'
    AND  i.start_time > DATEADD(day, -3, SYSUTCDATETIME())
)
SELECT query_id, plan_id, is_forced_plan, ce_version,
       MIN(start_time) AS desde, SUM(count_executions) AS ejecuciones,
       AVG(avg_duration)/1000.0 AS avg_ms, MAX(max_duration)/1000.0 AS max_ms
FROM   planes
GROUP  BY query_id, plan_id, is_forced_plan, ce_version
ORDER  BY avg_ms DESC;

DOS ADVERTENCIAS
Query Store puede estar apagado en esa base, y entonces la comprobacion no se puede correr y hay que pedirla.
Forzar un plan es un cambio de produccion, no un diagnostico: se propone, no se ejecuta desde Support.

EL TECHO DE 120 SEGUNDOS NO ES CASUALIDAD
Es el CommandTimeout de la aplicacion. Cloudflare corta a los 100 s, asi que el usuario ve un 524 antes de que la aplicacion alcance a rendirse.

## Caso RCS-28256 Tailored Brands al 13 de agosto: que queda abierto y como se remide
_chunk 1492 · 2026-08-17 · fuente: moscu://memoria/2026-08-13_

Tailored Brands, Client ID 209, tenant tbi, base sqldb-prd-wus2-arp-production-209-tbi-platform. Reporta Colton Neal; tambien Mike DiTommaso, Sam Fuentes y Shelley Cameron.

RESUELTO Y CONFIRMADO POR EL CLIENTE
Sign in y creacion de incidentes. Colton lo dijo el 11 ago 18:56 UTC.

ABIERTO
1. El salto de Secure a Incident tarda de 30 a 45 segundos.
2. El timeout de Izenda en nettrack/AdHoc/reportlist.aspx. Desde el 13 ago tiene dueno: Jack, con hipotesis de load balancing (pagina de bucket review).

DESCARTADO, NO VOLVER A MIRAR
Un despliegue faltante (Kiran, 11 ago: una vez desplegado todos los clientes reciben el mismo codigo).
Los dos flags de AdHoc que Jon reactivo el 10 ago: EnableAdHocInitCaching y EnableAdHocPerRequestUserScope, los dos True en este tenant, verificado en base.
Un bloqueo de Cloudflare: el Ray ID a299728c9ee465e3 del 11 ago 18:56:16 UTC en us.apprissretail.com es un 524 de timeout, no un bloqueo.

CABO SUELTO
EnableBlobAppendLogging esta en False en el 209, editado 2026-08-10 14:09:57 UTC, y nadie ha confirmado cual deberia ser el valor esperado.

EL PROBLEMA DE FONDO
No hay una sola medicion propia. Todo son autorreportes: Colton 39 s y luego unos 30 s, Mike DiTommaso unos 45 s y Sam Fuentes unos 45 s, los dos el 12 ago 15:25. Y nadie ha documentado cuanto deberia tardar ese salto, asi que "30 segundos" por si solo no significa nada.

EL DISCRIMINADOR QUE DECIDE EL CASO
Si los TTFB se comen los 30 a 45 segundos, el tiempo se va en el servidor y la cache de screen labels de Chris (en PR, en USDEV) no le va a arreglar nada a este cliente. Si los TTFB son rapidos y el total sigue alto por cientos de requests pequenos, esa cache es exactamente el arreglo. Esa respuesta hoy no la tiene nadie y es lo que se le lleva a Ripp y a Jon.

ENG-7182 esta enlazado pero acotado al 524 al guardar, que es justo lo que el cliente dice que ya funciona, y sigue en Backlog. Hay que definir si debe cubrir el 524 de Izenda o si va uno nuevo.

Protocolo de remedicion en seis fases: tenant de control, DevTools, Query Store, flags, Izenda medido aparte, conclusion.

## Unificacion: causa raiz del bucket de login, desbloqueo de usuario y el tope real de 4 MB en adjuntos
_chunk 1493 · 2026-08-17 · fuente: moscu://memoria/2026-08-13_

CAUSA RAIZ DEL BUCKET DE LOGIN: LA MIGRACION EN DOS PASOS
El paso uno le pide al usuario vincular un email y crea la fila en membership.Users con la contrasena AES-256 desencriptada de lpguys.
El paso dos, el job de Hatter, sincroniza al resto desde incident.LPUser2 pero les asigna una contrasena por defecto. Por eso a esos usuarios el reset de contrasena les resuelve el problema: es una firma reconocible, si el reset lo arregla venia por Hatter.
Sin email en lpguys no se creo cuenta ninguna.

USUARIO BLOQUEADO: REMEDIACION APROBADA (pagina de bucket review, 13 ago 2026)
UPDATE membership.Users SET Locked = 0 WHERE UserID = X
mas purgar la cache del cliente, no borrarla. Pendiente que Ripp defina si se permite desbloquear desde la UI.

ADJUNTOS: EL TOPE REAL ERA 4 MB
La subida a blob tenia un maximo de 4 MB y no tenia relacion con archivos bloqueados por tipo. Liberado a produccion el 13 ago 2026, necesita prueba en PROD. Cadena escrita en la pagina: Matt, luego Support, luego el cliente.
Las smart alerts fallaban por la misma causa aguas arriba: adjunto o documento de impresion ausente en el blob. Fix a produccion el mismo dia. A Support le toca verificar que el monitoreo de smart alerts este en pie.

TIMEZONE
Se agregara a Incident la actualizacion de timezone segun el navegador, que la plataforma ya hace y los clientes Incident-only se saltan porque entran directo a Incident. Eso confirma el analisis de David Vargas en RCS-28294: la IANA timezone solo se escribe por ajax al login y las cuentas Incident-only migradas quedan en UTC.

LO QUE NO ES DE LA UNIFICACION
Associate issue y Employee Lookup. Location Hierarchy quedo resuelto.

CONTEO
Al 13 ago 2026 hay 88 tickets con label de la ola y 50 abiertos. La pagina de Confluence imprime 71 y 46 con corte del 6 de agosto, y sus filas por bucket tambien estan vencidas. La cifra impresa nunca es la fuente de verdad; el link JQL de la propia pagina si.

## HANDOFF-RCS-28072-y-RCS-28077 — parte 1
_chunk 1599 · 2026-07-30 · fuente: HANDOFF-RCS-28072-y-RCS-28077.md_

# Handoff — RCS-28072 y RCS-28077
Preparado por Juan Martinez · 30 jul 2026

Los dos llegaron por Teams pidiendo asignación (Anil P y Neha Haridas), los dos son **High**, y ninguno es mío. Este documento es el triage hecho y lo que hay que dejar listo **antes** de pasarlos, para que quien los reciba no empiece de cero.

---

# RCS-28072 — Guess, Timeout errors, Multiple Users

**High · reportado por Guess · canales: AALPS Issues + L2 Team · pedido de asignación por Anil P**
*Descripción del cliente:* "Multiple users are reporting slowness of Secure Incident and Time outs"
*Justificación de prioridad:* "Multiple users cannot use the system"

## ⚠️ Antes de asignarlo: NO es un ticket aislado

Es **el mismo error** que RCS-28021 (ADUSA / Izenda), que ya está diagnosticado.

| | RCS-28072 (Guess) | RCS-28021 (ADUSA) |
|---|---|---|
| Error | Cloudflare **524 — A timeout occurred** | Cloudflare **524 — A timeout occurred** |
| Hora UTC | 18:49:48 | 19:08:27 |
| Host origen | `us.apprissretail.com` | `us.apprissretail.com` |
| Módulo | Audit Workbench | AdHoc Reporting (Izenda) |
| Tenant | guess | adusa |
| Nodo Cloudflare | Toronto | Ashburn |

**Dos tenants distintos, dos módulos distintos, el mismo host de origen, 19 minutos de diferencia.**

**Qué es un 524:** Cloudflare corta la conexión cuando el servidor de origen no responde en 100 segundos. El usuario ve una pantalla que parece un error de la aplicación, pero en realidad es la página de error de Cloudflare — la app nunca respondió. Por eso no hay mensaje de error propio del sistema.

**Conclusión de triage:** esto apunta a degradación de rendimiento del origen, no a un problema del tenant de Guess. Investigarlo por separado es duplicar trabajo.

## Antes de pasarlo

1. **Linkear a RCS-28021** como *relates to*. Sin esto, quien lo reciba repite la investigación completa.
2. **Comentario interno** con la tabla de correlación (abajo).
3. **Verificar campos:** tipo Incident ✅, prioridad High ✅, empresa **Guess** taggeada + prefijo en *Export to Power BI*.
4. **Publicarlo en el canal Support Team Priority** — es High con múltiples usuarios bloqueados y lleva sin dueño desde las 2:38 p.m.
5. **Decirle a quien lo reciba que hable conmigo primero.** Ray ID de la instancia de ADUSA: `a236a3e3b8154160`.

## Comentario interno (copiar y pegar)

> Correlates with **RCS-28021** (ADUSA / Izenda AdHoc). Both are Cloudflare **524 timeouts** against the same origin host, `us.apprissretail.com`, 19 minutes apart:
>
> - Guess — Audit Workbench — 2026-07-30 18:49:48 UTC — Cloudflare node Toronto
> - ADUSA — AdHoc Reporting — 2026-07-30 19:08:27 UTC — Cloudflare node Ashburn — Ray ID `a236a3e3b8154160`
>
> A 524 means the origin did not respond within Cloudflare's 100-second limit, so the response the user sees is Cloudflare's error page rather than anything the application returned. That is why there is no application error message.
>
> Two different tenants and two different modules failing the same way within 20 minutes points to origin-level performance rather than a tenant-specific defect. Linking the two tickets so they travel together.
>
> Diagnosis on RCS-28021 is already done — whoever picks this up should coordinate rather than restart the investigation.

## Perfil de quien debería recibirlo

Alguien de **Incident / Secure Incident**, no de EBR. Y conviene que sea la misma persona que RCS-28021 o alguien que trabaje coordinado, porque son el mismo problema. Si termina siendo infraestructura, la ruta es `Under Infrastructure Review` — y ojo, en esa ruta **el assignee se queda con el ticket** y es quien comunica y cierra.

---

# RCS-28077 — Ahold, Refund Searches Are Broken (AHL/AHOLD)

**High · reportado por Ahold · canales: L2 Team + Secure 5 Issues · pedido de asignación por Neha Haridas**

## Qué está pasando

El cliente estaba minando refunds buscando indicadores de fraude y encontró que las transacciones devuelven **múltiples líneas del mismo ítem**. Lo describe como un efecto cartesiano por cada condición basada en ítem.

**El cliente ya encontró el patrón**, y es lo más valioso del reporte:

> *"The above highlighted item-based conditions had not previously caused a cartesian effect. This search has been in use for years with no issue. However, as of July 30th, 2026, every single item refunded is now being listed out exactly 5x — that is, the count of item-based conditions applied to the search."*

Las condiciones de ítem en su búsqueda son cinco:

1. `Department Not in 22, 23`
2. `Non Merch Flg Equal to False`
3. `Return Flg Equal to True`
4. `Cancel Flg Equal to False`
5. `Voided Flg Equal to False`

**Cinco condiciones → cada línea sale exactamente cinco veces.** Eso es consistente con que el generador de la búsqueda esté aplicando cada predicado de ítem como un **JOIN independiente** a la tabla de líneas, en lugar de un solo JOIN con los predicados unidos por AND.

## El control negativo que trae el cliente

Esto es lo que hace el reporte tan bueno: incluye una búsqueda que **sí** funciona. *Non-Scanned Items Sales-Precise List* tiene **3 condiciones de ítem** (`Article ID In`, `Department Not in 22,23`, `Amount Charged Greater than 0`) y devuelve correctamente — 2 ítems, 2 filas, sin duplicación.

**Conclusión:** no es un problema de las condiciones de ítem en general. Es específico de la ruta de refunds / `Transaction Type = Return/Exchange`.

Detalle adicional del recibo que adjuntó: las líneas anuladas y canceladas **no** se duplican, solo la línea del refund.

## HANDOFF-RCS-28072-y-RCS-28077 — ⚠️ Lo primero que hay que revisar: la fecha
_chunk 1600 · 2026-07-30 · fuente: HANDOFF-RCS-28072-y-RCS-28077.md_

## ⚠️ Lo primero que hay que revisar: la fecha

**"as of July 30th, 2026" es hoy.** Y el release de Secure sale miércoles y jueves de la semana de release. Hoy es jueves.

Si hubo un release de Secure el 29 o 30 de julio, **esto es una regresión y no es el problema de un cliente** — afecta a todos los tenants de Secure 5 que corran búsquedas de refunds con condiciones de ítem. Eso cambia la urgencia, cambia el destino y abre la conversación de rollback.

Calendario: `docs.apprissretail.com/products/product-docs/general/release-calendar`

## Por qué el High está bien justificado

Los Display Fields de la búsqueda incluyen `Count`, `Sum of Amount Charged` y `Unique Count of Transaction ID`.

Con la inflación 5×, **los agregados están mal**. No es que el cliente vea filas repetidas y le moleste: están tomando **decisiones de fraude sobre cifras infladas cinco veces**. Ese es el argumento cuando alguien pregunte por qué es High.

## Antes de pasarlo — campos a corregir

| Campo | Valor correcto |
|---|---|
| Tipo | **Incident** (algo que funcionaba se rompió) — verificar que no llegó como SOW |
| Prioridad | **High** — dejarla |
| Label | **`Support_Data_Team`** (es Secure 5) |
| Team Ownership | **Support Delivery** |
| Sprint | **RCS Support Team** (escribir "support" y autocompleta) |
| Campo *Problem* | **Data** — no dejarlo en "Other" |
| Empresa | **Ahold Delhaize** taggeada + prefijo en *Export to Power BI* |

## Lo que le falta al ticket

**El SQL generado.** Es lo primero que va a pedir Engineering y nadie lo capturó. Quien lo tome tiene que sacar la consulta que el motor genera para la búsqueda de refunds y compararla con la de Non-Scanned Items. El JOIN duplicado se ve a simple vista.

## Pasos para quien lo reciba

1. **Calendario de releases** — ¿hubo release de Secure el 29 o 30 de julio? Si sí, ya hay sospechoso.
2. **¿Es multi-cliente?** Correr una búsqueda de refunds con varias condiciones de ítem en otro tenant de Secure 5. Si duplica también, es regresión de release y se escala de inmediato.
3. **Prueba determinística:** reducir las condiciones de ítem a 2 y luego a 3. Si la multiplicación baja a 2× y 3×, la relación queda demostrada y es evidencia irrefutable.
4. **Capturar el SQL generado** de la búsqueda que falla y de la que funciona.
5. Con eso → **`Under Engineering Review`**, cola de **Secure 5** (cubre Secure EBR y Secure 5), asignar a **Shandana Khan**, y desasignarse.

**No mandarlo a Delivery.** No es data mal configurada, es generación de consulta. Es código.

## Comentario interno (copiar y pegar)

> Triage notes for whoever picks this up.
>
> The customer has already identified the pattern: each refunded item is duplicated **exactly 5 times**, matching the **5 item-level conditions** on the search — `Department Not in 22,23`, `Non Merch Flg = False`, `Return Flg = True`, `Cancel Flg = False`, `Voided Flg = False`. That is consistent with each item-level predicate being applied as a separate join to the line table rather than being ANDed within a single join.
>
> Important control case they provided: a *Non-Scanned Items Sales-Precise List* search with **3** item conditions returns correctly — 2 items, 2 rows, no duplication. So this is specific to the refunds path / `Transaction Type = Return/Exchange`, not to item-based conditions in general. Their receipt also shows that voided and cancelled lines are not duplicated, only the refund line.
>
> Reported start date is **2026-07-30**, today. First action should be checking the release calendar for a Secure release on 7/29–7/30 and testing a refunds search with multiple item conditions on another Secure 5 tenant. If it reproduces elsewhere this is a release regression, not a client-specific issue.
>
> Impact note supporting the High priority: the search's display fields include `Count`, `Sum of Amount Charged` and `Unique Count of Transaction ID`, so the aggregates are inflated 5×. They are mining refunds for fraud indicators against numbers that are wrong, not merely visually duplicated.
>
> Missing and needed before escalation: the **generated SQL** for the failing refunds search versus the working Non-Scanned Items search.
>
> Suggested deterministic confirmation: reduce the item conditions to two, then three, and verify the duplication factor tracks the condition count.

## Perfil de quien debería recibirlo

**Secure 5 / EBR**, no Incident. La guía es explícita en que en el equipo unos son más fuertes en Incident y otros en EBR, y este es claramente EBR.

Criterio de carga: el estándar son ~10 tickets por persona, con la advertencia de que **los de datos pesan más** — tres de datos pueden ser más carga que ocho simples. Este pesa.

---

# Resumen de acciones antes de asignar

| # | Acción | Ticket |
|---|---|---|
| 1 | Linkear a RCS-28021 como *relates to* | 28072 |
| 2 | Pegar el comentario interno de correlación | 28072 |
| 3 | Publicar en Support Team Priority | 28072 |
| 4 | Corregir label, Team Ownership, Sprint, Problem, empresa | 28077 |
| 5 | Pegar el comentario interno de triage | 28077 |
| 6 | Verificar que el tipo sea Incident y no SOW | 28077 |
| 7 | Asignar a perfil Incident (28072) y perfil EBR (28077) | ambos |

**Los dos son High y los dos llevan horas sin dueño.** Camila está esperando respuesta en 28072 desde las 3:27 p.m.

## HANDOFF-RCS-28075-2026-08-05 — parte 1
_chunk 1601 · 2026-08-05 · fuente: HANDOFF-RCS-28075-2026-08-05.md_

# RCS-28075 · Handoff para Vedant Shirude
**Fecha:** 5 ago 2026 · Juan Martinez
**Ticket:** https://trebuco.atlassian.net/browse/RCS-28075
**Cliente:** Ahold Delhaize / ADUSA (slug `adusa`, cliente 441) · corte de migración 27 jul 2026
**Reporter:** leighann.stubbs@adusa.com · **Assignee:** Vedant Shirude
**Estado:** Escalated · Medium · Account Service Level High-Touch
**Labels:** `Escalated`, `Uni_Jul_26_SessionExpiry`
**Creado:** 30 jul 2026 20:19 UTC · **Última actualización:** 4 ago 2026 19:51 UTC

**Versión 2**, reescrito el 5 ago con el ticket completo a la vista. La v1 se había construido solo con los adjuntos y contenía dos errores, documentados abajo.

---

## Descripción original

> Operators have been experiencing time outs over the last few hours. It's happening to multiple associates in Central Station. They have to close the program and come back in.

---

## Correcciones a la v1 de este documento

**1. `image-20260731-174628.png` no es evidencia del cliente.** Lo subió Vedant, no Leigh Ann. Su comentario del 31 jul 17:47 lo explica: *"I was able to open ADShopliftingEntrypage.aspx page which the screenshot has in the URL but not the exact one."* Es su intento de reproducción, y los campos con borde rojo son el estilo normal de campos obligatorios en un formulario abierto sobre un caso cerrado. No es un síntoma. El argumento de la v1 sobre "las dos capturas son la misma página" se apoyaba en que ambas fueran del cliente, así que se cae.

**2. El label `Uni_Jul_26_SessionExpiry` está mal y lo puso Juan el 4 ago.** En el ticket no aparece en ningún momento el cambio de 300 a 30 minutos de sesión. Esa causa se importó de la llamada con Kiran del 3 ago al documento de categorización y se pegó a este ticket sin respaldo del ticket. La evidencia real es un Cloudflare 524 y la hipótesis de Izenda de Chris Rippingale.

**Label correcto: `Uni_Jul_26_Timeouts`.** Además el campo `Problema` está en `Other` y debería ser `Performance Degradation`.

**3. Inconsistencia propia.** En `LABELS-UNIFICACION-FINAL-2026-08-04.md`, sobre el RCS-28084, quedó escrito *"Es timeout de request, no expiración de sesión"*. Esa distinción se hizo para ese ticket y no se aplicó a este.

---

## El hallazgo principal: RCS-28084 es el mismo problema y ya tiene hotfix

De la tabla de labels del 4 ago:

> RCS-28084 | Vitamin Shoppe | **Closed** | timeout al crear incidente, cerrado con *"Unification platforms hotfix created and published"*

Y en el comentario del 31 jul 20:19 UTC, Leigh Ann finalmente da la URL:

> *"Yes, users are experiencing time outs. They are at least to this page: https://apps.apprissretail.com/adusa/nettrack/LPMS/**NewIncident.aspx** — April and I can't get into the system at all."*

**Timeout al crear incidente. Es la misma operación que el 28084.**

Los dos tickets son de Vedant. Él cerró el 28084 con ese hotfix y puede no haber conectado que el 28075 es la misma familia en otro tenant.

**La pregunta concreta: ¿ese hotfix se desplegó al tenant adusa?**

### Loop abierto asociado

Vedant pidió la URL completa dos veces (31 jul 15:47 y 18:40). El cliente la dio el 31 jul 20:19 apuntando a `NewIncident.aspx`. Lo que Vedant probó fue `ADShopliftingEntrypage.aspx`. **La respuesta del cliente nunca se usó.**

---

## El ticket tiene dos problemas distintos metidos en uno

### Problema A · Los timeouts (abierto, es el escalado)

Jim Cosseboom, 1 ago 17:16 UTC:

> *"This issue has worsened and is affecting most users"*

Evidencia: `image001.png`, subido por Leigh Ann el 31 jul.

| | |
|---|---|
| Error | Cloudflare **524** |
| Timestamp | 2026-07-30 19:21:24 UTC (≈1h antes de que se creara el ticket) |
| Host en error | `us.apprissretail.com` |
| Browser | Working |
| Cloudflare (Ashburn) | Working |
| Host | **Error** |
| URL | `apps.apprissretail.com/adusa/nettrack/LPMS/screens/incident/441/lpms/screens/ADShopliftingEntrypage.aspx?StoreIdent=2552&MasterCaseID=1548395&ShopliftingID=15765…` |

Texto de Cloudflare: *"The origin web server timed out responding to this request. The likely cause is an overloaded background task, database or application, stressing the resources on the host web server."*

Un 524 es timeout de request, el origen no contestó. Una sesión que expira produce redirect al login, no un 524.

**⚠️ La pista más concreta del ticket y nadie la cerró.** Chris Rippingale, 31 jul 18:03 UTC:

> *"Possibly related to Izenda generating thumbnails. Jack is making a change to turn it off until we understand the perf. Suggest ask the user if this has happened again since? Are do not see spikes at the moment."*

No hay un solo comentario posterior que diga si el cambio de Jack se hizo, ni si sirvió. Es lo más accionable que hay en el ticket.

### Problema B · El bloqueo de Leigh Ann y April (arreglado, falta confirmación)

Comentario de Juan, 3 ago 22:35 UTC: ninguna de las dos cuentas tenía el permission group `Administrators` ni los tres grupos básicos. Se agregaron y se guardó.

**Es un patrón documentado.** De la llamada con Kiran del 3 ago: *"Administradores que perdieron sus permission groups en el corte. Confirmado en Ahold con Leanne Stepps y April Valerie."* Es la misma April. Kiran no supo explicar la causa: *"Absolutely no clue. They should all have."* Se resuelve a mano y no hace falta escalarlo.

### Por qué separarlos importa

El último comentario al cliente (Vedant, 3 ago 14:25) dice que engineering trabaja en un fix de los timeouts. El de Juan de esa misma noche habla de permisos. Desde el lado del cliente son dos respuestas que no se conectan. Y **el ticket lleva dos días sin update estando escalado.**

---

## HANDOFF-RCS-28075-2026-08-05 — Cruces con otros tickets de la ola
_chunk 1602 · 2026-08-05 · fuente: HANDOFF-RCS-28075-2026-08-05.md_

## Cruces con otros tickets de la ola

| Ticket | Cliente | Estado | Relación |
|---|---|---|---|
| **RCS-28084** | Vitamin Shoppe | Closed | **Timeout al crear incidente, cerrado con hotfix de unificación. Misma operación.** Dueño: Vedant |
| RCS-28138 | Stater Bros | Under Support Review | Host error `us.apprissretail.com`, el mismo host |
| RCS-28112 | Stater Bros | Work in progress | Cloudflare 524 confirmado, origen sin responder |

**Dato de clasificación disponible:** en el app service de nettrack había unos 2495 client timeouts contra 255 errores 500, y 248 de esos 500 en un solo endpoint, `POST /nettrack/api/internal/SendSmartAlert.aspx`. Un command timeout de SQL saldría como 500 con excepción y no se ve ese volumen, así que apunta a web request timeout. **Esa última lectura es de Juan, no está en los logs.**

**Nadie ha separado los timeouts por tenant todavía.** Ofrecible.

---

## Mensaje para Vedant (Teams)

Corto y directo. El objetivo es explicar **por qué existe el comentario del 3 ago**, no exponer el análisis completo.

> Vedant, te explico el comentario que dejé el domingo en el 28075 para que no te descuadre.
>
> Leigh Ann había dicho el 31 que ella y April no podían entrar al sistema, y eso me sonó a algo distinto de los timeouts. Revisé las dos cuentas y a ninguna le habían quedado los permission groups después de la migración, les faltaba Administrators más los tres básicos. Se los puse y guardé. Kiran ya había visto ese patrón en Ahold, con la misma April, así que se arregla a mano y no va a engineering. Solo falta que ellas confirmen que ya entran.
>
> Así que el ticket tiene dos cosas adentro: el bloqueo de ellas dos, que ya está resuelto, y los timeouts que reportó Jim, que es lo escalado y sigue abierto.
>
> Y algo que te puede servir: cuando Leigh Ann te dio la URL apuntó a NewIncident.aspx, o sea timeout al crear incidente. Eso es lo mismo que el 28084 de Vitamin Shoppe que cerraste con el hotfix de unificación. Vale confirmar si ese hotfix llegó a adusa.
>
> Una última, el label de session expiry lo puse yo el lunes y está mal, la evidencia es un 524 que es timeout de request. Lo paso a Timeouts si estás de acuerdo.
>
> ¿Te sirve así o lo miramos juntos?

### Lo que se dejó fuera del mensaje a propósito

Está todo en este documento por si la conversación sigue, pero no va en el primer mensaje:

- Los números del app service de nettrack (2495 client timeouts, 248 de 255 errores 500 en `SendSmartAlert.aspx`)
- Los cruces con RCS-28138 y RCS-28112 por el host `us.apprissretail.com`
- La discrepancia del valor del timeout de sesión (Kiran 30 vs Engineering 60/240)
- Que la URL que dio el cliente nunca se probó
- **La pista de Izenda de Chris.** Es la más accionable de todas, pero es pregunta para Chris Rippingale o Jack directamente, no para Vedant. Va por separado

---

## Comentario interno para el ticket (borrador)

> Consolidating analysis, and correcting a labeling error of mine.
>
> **Label.** I applied Uni_Jul_26_SessionExpiry on 8/4 based on the 300 to 30 minute session change Kiran described. That root cause does not appear anywhere in this ticket and the evidence does not support it. The attachment is a Cloudflare 524, which is a request timeout with the origin not responding, not a session expiry (which presents as a redirect to sign in). Should be Uni_Jul_26_Timeouts, and Problem should move from Other to Performance Degradation.
>
> **Likely known fix.** Leigh Ann's 7/31 20:19 comment gives the URL as NewIncident.aspx, i.e. timeout on incident creation. That is the same operation as RCS-28084 (Vitamin Shoppe), which was closed with "Unification platforms hotfix created and published". Worth confirming whether that hotfix reached the adusa tenant. Note the customer-supplied URL was never tested; reproduction on 7/31 was against ADShopliftingEntrypage.aspx.
>
> **Two separate issues in this ticket.** (1) The timeouts reported by Jim Cosseboom on 8/1, still open, this is the escalated item. (2) Leigh Ann and April unable to access at all, which I resolved on 8/3 by restoring the Administrators permission group plus the three base groups on both accounts. Item 2 matches the confirmed Ahold post-cutover permission group loss pattern (same April, per Kiran's 8/3 review) and needs only customer confirmation. Suggest addressing them separately in customer comms, since the current comment thread mixes them.
>
> **Open lead not closed out.** Chris Rippingale, 7/31 18:03: possible Izenda thumbnail generation, with Jack making a change to disable it pending perf review. No follow-up on the thread confirms whether that change was made or whether it helped. This is the most concrete engineering lead on the ticket.
>
> **Cross-references.** Host us.apprissretail.com also fails in RCS-28138; same 524 pattern in RCS-28112. Both Stater Bros. nettrack app service showed ~2495 client timeouts vs 255 HTTP 500s, 248 of those on POST /nettrack/api/internal/SendSmartAlert.aspx. Timeouts have not been broken down per tenant.

---

## HANDOFF-RCS-28075-2026-08-05 — Comentario al cliente (borrador, si Vedant lo quiere)
_chunk 1603 · 2026-08-05 · fuente: HANDOFF-RCS-28075-2026-08-05.md_

## Comentario al cliente (borrador, si Vedant lo quiere)

> Hello Leigh Ann, Jim,
>
> An update on both parts of this ticket.
>
> On the access problem you mentioned on July 31, your account and April's were both missing the Administrators permission group along with three base groups, which we have now restored. Could you both confirm whether you are able to sign in and work normally? This was a known effect of the platform migration on administrator accounts.
>
> On the timeouts affecting the wider group of operators, that is a separate issue and it remains our priority. The page you identified, NewIncident.aspx, matches a timeout pattern we have already fixed for another customer, so we are confirming whether that fix has been applied to your environment. We are also following up on a possible cause related to report thumbnail generation.
>
> I will come back to you with a firm answer on the timeouts. In the meantime, if the operators see the timeout again, the exact time it happened would help us match it against our logs.
>
> Kind regards,

---

## Pendientes

- [ ] Confirmar si el hotfix de unificación del RCS-28084 se desplegó al tenant adusa
- [ ] Preguntar a Chris Rippingale o a Jack si el cambio de thumbnails de Izenda se hizo y si sirvió
- [ ] Probar `NewIncident.aspx` en adusa, que es la URL que dio el cliente y nunca se probó
- [ ] Cambiar label a `Uni_Jul_26_Timeouts` y `Problema` a `Performance Degradation` (coordinar con Vedant primero)
- [ ] Update al cliente hoy, lleva 2 días quieto estando escalado
- [ ] Confirmación de Leigh Ann y April de que ya pueden entrar
- [ ] Corregir la fila del RCS-28075 en `LABELS-UNIFICACION-FINAL-2026-08-04.md` y en `CATEGORIZACION-UNIFICACION-2026-08-04.md`
- [ ] Separar los timeouts del app service de nettrack por tenant (ofrecible, nadie lo ha hecho)

## NOTA-INTERNA-RCS-28022 — parte 1
_chunk 1604 · 2026-07-31 · fuente: NOTA-INTERNA-RCS-28022.md_

# RCS-28022 — Santikos Entertainment: 404 on Incident Entry and Attachments

**Prepared: 2026-07-31 | Analyst: Juan Martinez | Status:** Escalated

---

## 🎟️ Ticket Details

| **Field** | **Value** |
| --- | --- |
| **Ticket** | RCS-28022 |
| **Customer** | Santikos Entertainment |
| **Issue Type** | Incident |
| **Priority** | High |
| **Status** | Escalated |
| **Opened** | 2026-07-29 |
| **Reporter** | Maricela Rico. Escalated by Jacob Weil, Director of Security (jacob@santikos.com) |
| **Assignee** | Juan Martinez (jmartinez@apprissretail.com) |
| **Jira URL** | [RCS-28022: Santikos - Error With Incident Info](https://trebuco.atlassian.net/browse/RCS-28022) |

---

## 🔍 Problem Statement

Clicking anything in the incident information section of a case, including attaching video, returns a 404 Page Not Found. The customer also reports the same error when entering a new incident: location and incident type can be selected, but every action after that fails. Reported 2026-07-29, two days without service, escalated by the customer's Director of Security on 2026-07-31.

---

## 👤 Client Profile

| **Field** | **Value** |
| --- | --- |
| **Client ID** | 411 |
| **Abbreviation** | STI |
| **Client slug** | `santikos` |
| **Server** | 9 |
| **Platform DB** | `sqldb-prd-wus2-arp-production-411-sti-platform` |
| **Migration phase** | 5 |
| **Production migration date** | 2026-07-27 |
| **CSM** | Colleen Knoblock |
| **Records migrated** | 520,781 |
| **Active products** | Incident, LPMS, OSHA module enabled |
| **In-app client ID** | 94423, 63 active users, 40 active locations |

---

## 🕵️ Investigation

Checked three layers: the error returned to the customer, the tenant's screen configuration, and the New Incident flow reproduced through impersonation via Control Panel.

### 📋 Customer error page technical details

**POINT OF FAILURE FOUND.** The 404 page's technical details give the cause directly:

```
Requested URL: https://web-prd-wus2-arp-nettrack.azurewebsites.net/nettrack/lpms/ShowAttachments.aspx
                 ?SuspectID=13980&MasterCaseID=13931&ShopliftingID=13980
Timestamp:     2026-07-29 14:15:32
Client Slug:   /santikos
HTTP Status:   404
Type:          System.Web.HttpException
Message:       The file '/nettrack/lpms/ShowAttachments.aspx' does not exist.
Stack:         at System.Web.UI.Util.CheckVirtualFileExists(VirtualPath virtualPath)
Return URL:    /santikos/platform
```

`CheckVirtualFileExists` throwing means the physical file is absent from the deployed application, on the shared app service host `web-prd-wus2-arp-nettrack.azurewebsites.net`. This is not tenant configuration.

Note the requested path is lowercase `/nettrack/lpms/`, while the working New Incident page is served from `/santikos/nettrack/LPMS/NewIncident.aspx` with uppercase `LPMS`.

### 📋 Tenant screen configuration

**PASS. No issue found here.** Screen Designer at `/santikos/nettrack/Admin/ScreenManager.aspx?admin=9QQP` lists 61 screens. All 61 show Build Status `CREATED` with Last Build Date **2026-07-29 8:32 AM**, which precedes the customer's error at 14:15 the same day. `ShowAttachments.aspx` does not appear among the 61 definitions.

Build All Screens was run again on 2026-07-31 with no change to the reported behaviour.

### 📋 New Incident flow, reproduced by impersonation

**POINT OF FAILURE FOUND.** Signed in to the tenant through Control Panel. `/santikos/nettrack/LPMS/NewIncident.aspx` loads. Location selects correctly (tested `0100 Mayan` and `0500 Northwest`, San Antonio TX). Case Class `All` selects and the Case Type step renders.

The Incident Type control does not open. Browser console against the DevExpress combo `fld_MasterCase_CaseType`:

| **Check** | **Result** |
| --- | --- |
| `typeof fld_MasterCase_CaseType` | `object`, control initialised |
| `GetEnabled()` | `true`, not disabled |
| `GetItemCount()` | `0`, no items |
| Network on click | No request to the application. All traffic captured was Pendo analytics |

The control is present, initialised and enabled, and holds zero items, so clicking produces nothing and typed text is cleared because no item matches. The loading panel elements `fld_MasterCase_CaseType_LP` and `_LD` are present in the DOM, indicating the control is configured for server-side loading, yet no callback is issued.

---

## 📌 Root Cause Statement

| **Field** | **Detail** |
| --- | --- |
| **What broke** | Attachment viewing and incident entry on the `santikos` tenant, since the 2026-07-27 migration to the unified platform. |
| **Why** | `/nettrack/lpms/ShowAttachments.aspx` is not present in the deployed application on the shared nettrack app service. Confirmed by ASP.NET's own `CheckVirtualFileExists` exception, not inferred. |
| **Scope** | Confirmed for `santikos`. Because the missing file is on the shared app service rather than in tenant configuration, other tenants on that service would be expected to hit the same 404 on the same page. Not verified. |
| **Business impact** | Cannot attach evidence to cases and cannot complete incident entry. Two days of no service on the core product function. Escalated by the customer's Director of Security. |
| **Evidence** | Cloudflare-independent server exception with full stack trace, timestamp 2026-07-29 14:15:32, plus 61 of 61 screens confirmed built before that timestamp. |

---

## NOTA-INTERNA-RCS-28022 — 💡 Additional Findings
_chunk 1605 · 2026-07-31 · fuente: NOTA-INTERNA-RCS-28022.md_

## 💡 Additional Findings

**Incident Type list returns zero items.** Separate from the missing file, the Incident Type combo on New Incident holds no items for this tenant, which blocks incident entry independently of the attachment page.

**Sequence worth flagging, causation not established.** The customer's 2026-07-29 report states she could select the location and the incident type, and that the 404 came after that step. As of 2026-07-31, after Build All Screens was run, there are zero incident types. Only the sequence is known. If a rebuild can affect the case type list, that should be confirmed before it is run on another migrated tenant.

| **Metric** | **Value** |
| --- | --- |
| Screens in Screen Designer | 61, all `CREATED` |
| Last Build Date before failure | 2026-07-29 8:32 AM |
| Customer error timestamp | 2026-07-29 14:15:32 |
| Incident Type item count | 0 |
| Application requests on dropdown click | 0 |

---

## 🔧 Recommended Fix

Both items are outside Support's scope. Neither is tenant configuration.

### 🅰 Restore the missing application page

Confirm whether `ShowAttachments.aspx` and any sibling pages under `/nettrack/lpms/` are present in the current nettrack deployment, and redeploy the missing files. If a set of legacy LPMS pages was not carried into the unified build, the scope is platform wide rather than client specific.

### 🅱 Restore the incident type list

Determine why `fld_MasterCase_CaseType` resolves to zero items for tenant `santikos`, and whether the list is populated from migrated configuration data or generated at build time.

---

## ❓ Open Questions

1. Is `ShowAttachments.aspx` missing from the deployment for all tenants on `web-prd-wus2-arp-nettrack`, or only resolving incorrectly for `santikos`?
2. Was a group of `/nettrack/lpms/` pages omitted when the legacy application was carried into the unified build? RCS-28033 (Big Y, also migrated 2026-07-27) reported a 404 on `/bigy/nettrack/LPMS/CaseEntry.aspx`, which may be the same gap.
3. Can Build All Screens affect the available case type list? The customer could select an incident type before the rebuild and cannot now.
4. Does the case type list depend on the location hierarchy, which would make this a data mapping issue rather than a deployment one?

---

## 🚫 Ruled Out

- Screen build state. All 61 screens built, and built before the failure.
- Tenant screen configuration.
- Client-side JavaScript failure on the Incident Type control. The control initialises and reports enabled.
- The `unload` Permissions Policy console violation from `DXR.axd`. Present, but the control initialises regardless.

---

## 🗣️ Work Outside This Ticket

Discussed with **Matt Kamminga** in Teams on 2026-07-31, covering the missing file, the screen build timeline and the zero item Incident Type list.

Investigation above was worked through with AI assistance. All findings were then verified directly in the browser, in the browser console, and in Screen Designer, and the migration facts were taken from the Incident Migration 2026 tracker.

---

## 📷 Extras

### 🏷️ Customer 404 technical details

Full exception and requested URL, as quoted in the investigation section. Source: attachment provided by Maricela Rico, 2026-07-29.

### 🏷️ Screen Designer listing

61 screens, Build Status column and Last Build Date column, tenant `santikos`.

### 🏷️ Browser console output on the Incident Type control

`GetEnabled()` returning `true` and `GetItemCount()` returning `0`.

## RCS-28032-INVESTIGACION-2026-08-04 — parte 1
_chunk 1606 · 2026-08-04 · fuente: RCS-28032-INVESTIGACION-2026-08-04.md_

# RCS-28032 — Vitamin Shoppe, alcance de Dayna Rivera

**Ticket:** https://trebuco.atlassian.net/browse/RCS-28032
**Cliente:** Vitamin Shoppe (slug `vitaminshoppe`, corte de migración 27 jul 2026)
**Contacto:** Joe Austin
**Estado al 4 ago 2026:** Work in progress, sin causa raíz confirmada

---

## El problema según el cliente

Joe reportó el 31 de julio que Dayna Rivera cubre los distritos 501 y 504 pero solo puede acceder al 504. Él intentó agregarle el 501 desde su lado y no se reflejó.

El 4 de agosto, después de que agregamos los nodos de District, Joe respondió dos cosas importantes:

1. Ve el 501 en el sistema pero ya no ve el 504.
2. **Ninguno de sus otros District Managers está configurado de esa forma.**

---

## Evidencia recogida

### Los tres DM que funcionan

Comparados en la pestaña Hierarchies del Control Panel:

| Usuario | Entradas | Nivel | Location Code | Location Name |
|---|---|---|---|---|
| Journey Armstrong | 1 | 0 Location | 226 | 226 - Centennial CO Store |
| Daniel Garza | 1 | 0 Location | 247 | 247 - Round Rock TX Store |
| Gisele Pohl | 1 | 0 Location | 75 | 75 - Norwalk CT Store |

Los tres tienen **una sola entrada, a nivel Location, una sola tienda. Ningún nodo District.**

### Dayna Rivera

| Nivel | Location Code | Location Name | Origen |
|---|---|---|---|
| 0 Location | 249 | 249 - Tanasbourne OR Store | preexistente |
| 0 Location | 500 | 500 - Everett WA Store | preexistente |
| 1 District | 501_2639 | 501 | agregado por Support el 4 ago |
| 1 District | 504_2648 | 504 | agregado por Support el 4 ago |

Antes de nuestro cambio ya era distinta al resto: **dos tiendas en vez de una.**

---

## Descartado

**Permission groups no es el diferenciador.** Verificado el 4 de agosto: Dayna tiene los mismos grupos que los DM que funcionan. En Journey Armstrong son ApprissCase Search Users, ApprissCase Users y Basic Users. La línea base confirmada por Kiran para cualquier usuario son esos tres, así que ninguno tiene nada especial.

---

## Corrección de una deducción anterior

Una versión previa de este documento concluía que la pestaña Hierarchies no controla el alcance de distrito, razonando que los tres DM de comparación funcionan con una sola tienda cada uno. **Esa conclusión es falsa** y quedó descartada por dos motivos:

1. El modelo de accesos de la plataforma tiene tres niveles y el segundo es exactamente la jerarquía de ubicaciones: define qué ubicaciones ve cada usuario. Textual de la documentación interna: *"a district manager sees their district; a store manager sees their store."* La pestaña Hierarchies **sí** es el campo correcto.
2. Los tres usuarios de comparación no son comparables. Joe escribió que ellos acceden a **sus tiendas**, no a sus distritos. Una sola tienda a nivel 0 es consistente con alcance de tienda, no prueba nada sobre el alcance de distrito.

Queda entonces abierta la pregunta de por qué agregar los dos nodos District no le dio a Dayna el 501.

---

## Hipótesis vigente

Dayna accedía al 504 **antes** de que existiera ningún nodo District en su configuración, solo con las dos tiendas de nivel 0. Después de agregar los nodos ve el 501 y perdió el 504. Es decir, el nodo agregado sí surtió efecto, pero reemplazó el alcance en vez de sumarse.

Dos posibilidades que hay que separar con datos:

**A. Las filas de nivel 0 y nivel 1 pertenecen a jerarquías distintas** y la aplicación resuelve por una sola. La tienda 249 (Tanasbourne OR) y la 500 (Everett WA) le daban acceso por su rama; al insertar nodos de nivel District la resolución cambió de rama.

**B. Es el mismo defecto de datos de RCS-28023**: filas en `secure.LocationHierarchyUserAssignments` apuntando a registros de `place.Location` cuya rama de jerarquía no coincide con la división real de la tienda en `incident.Store`. Kiran las eliminó y reinsertó las correctas para Ahold.

En ambos casos la pregunta que hay que responder primero es concreta: **a qué distrito pertenece realmente la tienda 249, y qué tiendas cuelgan del nodo `501_2639`.** Si el nodo 501 está vacío o no contiene la tienda de Dayna, el síntoma se explica solo.

El patrón de RCS-28023 ya quedó documentado como no exclusivo de ADUSA en la página de revisión de Unificación, bucket `Uni_Jul_26_LocationHierarchy`.

### Por qué encaja con RCS-28023

En RCS-28023 (Ahold) el defecto fue exactamente ese: filas en `secure.LocationHierarchyUserAssignments` apuntando a registros de `place.Location` cuya rama de jerarquía no coincidía con la división real de la tienda en `incident.Store`. Kiran Vadday las eliminó y reinsertó las correctas.

Ese patrón ya quedó documentado como no exclusivo de ADUSA en la página de revisión de Unificación, bucket `Uni_Jul_26_LocationHierarchy`.

---

## RCS-28032-INVESTIGACION-2026-08-04 — Consultas de verificación
_chunk 1607 · 2026-08-04 · fuente: RCS-28032-INVESTIGACION-2026-08-04.md_

## Consultas de verificación

**Base de datos:** `sqldb-prd-wus2-arp-production-433-vse-platform`

Van en tres pasos, de menos a más. Correr el paso 1 primero y mirar el resultado antes de seguir, porque el paso 1 dice si los otros dos tienen sentido.

### Advertencia sobre la consulta que estaba antes en este archivo

La versión anterior era un solo SELECT con `JOIN place.Location` y `LEFT JOIN incident.Store s ON s.StoreNo = loc.StoreNumber`. **No servía**, por tres motivos concretos:

1. El `JOIN` interno contra `place.Location` **desaparece justo las filas que nos interesan.** Las asignaciones de nivel 1 (District) no tienen StoreNumber, así que los dos nodos que agregamos el 4 de agosto no habrían salido en el resultado.
2. **`StoreNo` no es único.** En estos tenants el mismo número de tienda existe en más de una división o marca, verificado en Ahold con la tienda 0001 que existe para Food Lion y para Stop & Shop. Unir solo por `StoreNo` multiplica filas y ensucia la lectura.
3. **Filtrar por `LastName = 'Rivera'` a secas** puede traer más de una persona y no descarta cuentas deshabilitadas ni duplicados con sufijo. Hay que filtrar por email.

### Paso 1, qué tiene Dayna asignado realmente

```sql
SELECT u.UserID, u.Email, u.Disabled,
       lhua.LocationId,
       loc.StoreNumber,
       loc.LocationHierarchy2Description
FROM secure.LocationHierarchyUserAssignments AS lhua
JOIN membership.Users AS u
    ON u.UserID = lhua.UserId
LEFT JOIN place.Location AS loc
    ON loc.LocationId = lhua.LocationId
WHERE u.Email LIKE '%rivera%'
ORDER BY u.Email, loc.StoreNumber
```

El `LEFT JOIN` es deliberado: deja ver las filas de District, que no tienen StoreNumber. Deberían salir cuatro filas para ella, las dos tiendas y los dos nodos.

**Qué mirar:** si aparece más de un UserID para Rivera, ahí está el problema y es un duplicado de migración, no un tema de jerarquía. Ver la sección de duplicados en la documentación de la llamada con Kiran.

### Paso 2, a qué distrito pertenece de verdad cada tienda suya

```sql
SELECT s.StoreNo, s.Division, s.StoreIdent,
       loc.LocationId, loc.LocationHierarchy2Description
FROM incident.Store AS s
LEFT JOIN place.Location AS loc
    ON loc.StoreNumber = s.StoreNo
WHERE s.StoreNo IN ('249', '500')
  AND ISNULL(s.Inactive, 0) = 0
```

**Qué buscar:** si `Division` de la tienda 249 no coincide con el distrito 501 que Joe dice que ella cubre, entonces el dato de origen está mal y agregarle nodos en Control Panel nunca lo iba a resolver. Si `StoreNo` viene con ceros a la izquierda en esta base, ajustar los literales.

### Paso 3, qué cuelga del nodo 501

```sql
SELECT loc.LocationId, loc.StoreNumber,
       loc.LocationHierarchy2Description
FROM place.Location AS loc
WHERE loc.LocationHierarchy2Description LIKE '%501%'
ORDER BY loc.StoreNumber
```

**Qué buscar:** si el nodo no tiene tiendas colgando, o no contiene la 249, el síntoma queda explicado sin necesidad de más.

### Consulta original de Kiran en RCS-28023, como referencia

Esta es la correctiva, no correrla acá sin adaptar. Sirve para ver el criterio de detección.

```sql
DELETE lhua
OUTPUT DELETED.UserId INTO #FixedUsers
FROM secure.LocationHierarchyUserAssignments AS lhua
JOIN membership.Users AS u
    ON  u.UserID = lhua.UserId
JOIN incident.LPUser2 AS lpu
    ON  lpu.UserID    = u.IncidentUserID
    AND lpu.FirstName = u.FirstName
    AND lpu.LastName  = u.LastName
JOIN incident.Store AS s
    ON  s.StoreIdent       = lpu.StoreIdent
    AND ISNULL(s.Inactive, 0) = 0
JOIN place.Location AS assigned_loc
    ON  assigned_loc.LocationId  = lhua.LocationId
    AND assigned_loc.StoreNumber = s.StoreNo
    AND assigned_loc.LocationHierarchy2Description <> s.Division
WHERE lpu.StoreIdent IS NOT NULL
  AND u.Disabled = 0
  AND u.Deleted  = 0
```

El criterio clave es la última condición del join: `assigned_loc.LocationHierarchy2Description <> s.Division`.

---

## Pasos siguientes

1. **Correr el paso 1** y confirmar que hay un solo UserID para Dayna, sin duplicado con sufijo.
2. **Correr los pasos 2 y 3** para saber a qué distrito pertenece la tienda 249 y qué cuelga del nodo 501.
3. **Revisar User teams** de Dayna y de un DM que funcione. Es la única pestaña del Control Panel que queda sin comparar.
4. Según el resultado, corregir la fila desalineada o escalar a Kiran junto con RCS-28023, RCS-28043 y RCS-28093, que son el mismo bucket.

## Qué no hacer todavía

**No quitar los dos nodos District que agregamos el 4 de agosto** hasta confirmar la causa real. Si se hacen dos cambios a la vez no se puede saber cuál produjo qué efecto.

---

## Verificación pendiente

**Los tres DM de comparación no son comparables.** Joe escribió que ellos acceden a **sus tiendas**, no a sus distritos. Que tengan una sola entrada de nivel 0 es consistente con alcance de tienda y no dice nada sobre cómo se configura un distrito. Antes de sacar conclusiones de esa tabla hay que pedirle a Joe un District Manager que efectivamente cubra varios distritos y funcione bien.

**Dayna confirmó por correo a Joe que sigue sin acceso al D501** después de que agregamos los dos nodos. Es decir, el cambio no resolvió y además le quitó el 504. Eso es lo que hay que explicarle a Joe en la próxima respuesta.

---

## Vínculos

- Mismo bucket que RCS-28023, RCS-28043 y RCS-28093 en la revisión de Unificación: `Uni_Jul_26_LocationHierarchy`
- Precedente de rol que viene del archivo de empleados y no de la configuración manual: RCS-28085 (otro cliente)

## RESPUESTAS-NUEVAS-2026-08-11 — parte 1
_chunk 1608 · 2026-08-11 · fuente: RESPUESTAS-NUEVAS-2026-08-11.md_

# 11 ago 2026 — Tickets con respuesta nueva

| Ticket | Qué llegó | Acción |
|---|---|---|
| RCS-28256 Tailored Brands | Mike DiTommaso escaló 9:17. Sigue lento, ahora toda la compañía en Incident | Responder + empujar reporting en Teams |
| RCS-28032 Vitamin Shoppe | Dayna ve 501 y perdió 504. Brandon agregado, Joe en PTO hasta el 17 | Hecho. Esperando captura |
| RCS-28153 Big Y | Ashley confirmó 240 minutos. El error de esr40 es el bug de adjuntos ERMS | Timeout + preguntar en Teams |
| RCS-28123 ADUSA | Leigh Ann le pidió el case number a Shane | Pasar a Under Customer Review |
| RCS-28023 ADUSA | April Valerio: le escribieron a Edward hoy para que pruebe | Esperar |

---

## RCS-28032 Vitamin Shoppe

Lo de Dayna confirma el defecto. Le agregaste 501 y 504, y ahora ve 501 y perdió 504.
Solo un distrito resuelve a la vez. Ya no es una muestra de uno, son dos estados
observados en el mismo usuario.

### Comentario al cliente

```
Hi Joe and Brandon,

Thank you for the update on Dayna, and noted on the PTO. Brandon, I have you on
the ticket now.

What Dayna described tells us exactly what we needed to know, so that part is
useful. Her profile has both districts assigned on our side, and only one is
showing at a time. That is not how it should work, and we have it in front of
our engineering team now with the detail from her test.

I will come back to you here as soon as I have something firm.

Thank you.
```

### Comentario interno

```
Client ID 433.

Update on the Dayna Rivera portion. On 04 Aug both districts were added to her
profile, 501 and 504. Before that change she could see 504 only. The customer
reported on 11 Aug that she now sees 501 and no longer sees 504.

Two rows exist in secure.LocationHierarchyUserAssignments for this user and only
one district resolves at a time. This is the same user, same profile, with the
visible district having changed after the second row was added.

This removes the earlier caveat that the finding rested on a single failing
sample. Multi district assignment is not being honoured. She is the only user on
this tenant assigned to two districts, which is why no other District Manager
reports it.

Kiran, this is the confirmation you were waiting on. The page and URL request is
still open with the customer but the behaviour is now observable from the
assignment side alone.

Joe Austin is on PTO from 11 Aug midday and returns 17 Aug. Brandon Bigelow,
brandon.bigelow@vitaminshoppe.com, has been added as the contact in the meantime.
```

---

## RCS-28153 Big Y

Un solo hilo, no dos. Client ID 362, tenant `bigy`.

La primera lectura fue que el error de esr40 era el bug de adjuntos de Vallarta,
por la URL con `system=ERMS`. **Descartado con reproducción:** el adjunto
`40-0826-EMPR-6-.pdf` abre correctamente con esa misma URL, y nadie tocó el
almacenamiento de Big Y entre el 8 de agosto y hoy.

Lo que sí sostiene la evidencia es expiración de sesión:

- El error dice `without proper platform initialization or authentication context`.
- Una de las pestañas del propio usuario decía "Your session has expired".
- Sábado 8:11 PM, term recap, sesión larga.
- El mismo archivo aparece subido dos veces, 8:11 PM y 8:12 PM. Patrón de reintento.

Así que los 240 minutos cubren las dos cosas que reportó Ashley.

### Paso a paso

1. Aplicar el timeout de 240 en Control Panel, Config Items del tenant `bigy`.
2. Verificar que el valor quedó aplicado y no solo en `CustomerEditedValue`.
3. Publicar los dos comentarios.
4. Pasar a Under Customer Review y esperar unos días de uso real antes de cerrar.

Acceso a ERMS concedido por Kiran el 11 ago para poder reproducir. Los contadores
en 0 son normales, el usuario de soporte no tiene ubicaciones asignadas.

### Comentario al cliente

```
Hi Ashley,

Thank you for confirming, and for sending the screenshot.

The session timeout for your users is now set to 240 minutes. That takes effect
on their next sign in, so please have them sign out completely and sign back in
once.

The error your user hit on Saturday evening comes from the same thing. The
document itself is fine, I opened it here without any issue, so nothing was lost.
What happened is the session had already ended by the time they went to open it,
and the longer timeout is what prevents that.

Please let me know how your team gets on over the next few days.

Thank you.
```

### Comentario interno

```
Client ID 362, tenant bigy.

Reproduction done. Opened the exact attachment from the customer's screenshot,
40-0826-EMPR-6-.pdf, at
apps.apprissretail.com/bigy/nettrack/attachments/attachments.aspx with
system=ERMS. It renders correctly. The file is intact and no storage change was
made on this tenant between 08 Aug and today.

Initial reading was that this matched RCS-28024 Vallarta, where ERMS writes
uploads to the lpms directory. Ruled out.

What the evidence supports instead is session expiry. The error page states the
request lacked proper authentication context, one of the customer's own browser
tabs reads "Your session has expired", and the case shows the same file uploaded
twice, at 8:11 PM and 8:12 PM on Saturday, which is the retry pattern of a user
whose session had ended.

Session timeout raised from 60 to 240 minutes at the customer's request. That
covers both parts of this ticket. No separate attachment issue open.
```

---

## RESPUESTAS-NUEVAS-2026-08-11 — RCS-28256 Tailored Brands
_chunk 1609 · 2026-08-11 · fuente: RESPUESTAS-NUEVAS-2026-08-11.md_

## RCS-28256 Tailored Brands

Sign-in resuelto. Sigue abierto lo lento en general y el reporting de Izenda, ambos
reportados por el cliente. Izenda lo nombró Colton el 10 ago dos veces, y Mike hoy
habla de "reporting and incident creation".

### Comentario al cliente

```
Hi Mike,

Thank you for following up, and I understand the impact now that everyone is on
Incident.

The sign in failures were corrected yesterday and those have not come back. The
slower load times and the reporting timeouts are a separate piece that is still
open, and it is with our engineering team as a priority.

I do not want to give you a date I am not sure of, so what I can commit to is an
update here by end of day tomorrow whether or not we have the fix.

If your users hit a timeout in the meantime, the time of day and what they were
doing helps us a lot.

Thank you.
```

### Comentario interno

```
Client ID 209.

Customer escalated on 11 Aug. Mike DiTommaso reports slow load times on sign in
are ongoing and notes the whole company is now on Incident, so impact is wider
than the original two users.

Status: the plan regression on the LPUser query was corrected on 10 Aug and sign
in recovered. Slow page loads and Izenda reporting timeouts are still reported
and are not covered by that fix.

Open with Engineering, shared with Matt K. No direction received since 10 Aug.
Linked to RCS-28134, same origin and same 524 mechanism.

Pending on our side: confirm whether the same plan regression is present on
441-dai, and get an owner for the Izenda timeout, which was never traced.
```

### Teams, chat grupal

```
Tailored Brands escalated this morning on RCS-28256. They have the whole company
on Incident now, so this is no longer two users.

Sign in is fixed since yesterday and has not come back. What is still open is the
slow load times and the reporting timeouts in Izenda, both still reported today.
I have no direction on those since yesterday.

Who can pick up the reporting side? I committed to the customer for an update by
end of day tomorrow.
```

---

## Pendiente arrastrado

- Los 77 punteros colgando de ADUSA, sin enviar a Kiran.
- RCS-27959 PACSUN: comentarios + Under Security Review, después de revisar el CASD del 23 jul.

## Nordstrom RCS-28219: PU vs clásico, el host decide quién administra permisos
_chunk 1677 · 2026-08-18 · fuente: terminal_

# David sin permisos en dashboards de Nordstrom — RCS-28219

18 ago 2026. Juan ayudando a David Vargas. Error: `Permission Required` en
`usprod.apprissretailcloud.com/platform/cpf/errorhandler/nopermission`, con branding de
Nordstrom. David tampoco puede usar Impersonate User. Trey no maneja permisos dentro de apps.

## Qué dijo Kiran y qué significa

Kiran pidió *"the Prod url for Nordstrom"*. Juan le mandó enlaces profundos a dashboards.
Ella corrigió: *"I meant the signing url"* — quería la URL de **inicio de sesión**, con la
que identifica plataforma y tenant. Un `#/dashboard/...` no se lo dice.

Y el dato de fondo: *"usprod is not PU yet"*, *"app.apprissretail.com is pu"*.
**PU = Platform Unification.** El host que le pasaron es de la plataforma **clásica**, no de
la unificada, que es donde ella administra.

## La consecuencia práctica

David está entrando por **usprod**, o sea plataforma clásica. Sus permisos **no** se
administran del lado de Kiran, se administran en **Control Panel USPROD**, donde Juan ya
tiene acceso con `SupportL2` + `Engineers`. No hace falta escalar.

Ruta:
1. `usprod.apprissretailcloud.com/control`
2. En *Customers in USPROD*, **clic en el logo de Nordstrom** para entrar al tenant.
   No usar `/<slug>/signin`, que redirige al SSO del cliente donde el usuario de Appriss
   no existe.
3. All apps → Settings → Users → buscar a David
4. User details → Permission groups → agregar los que falten y **guardar**
5. Verificar la base de tres que llevan todos: `ApprissCase Search Users`,
   `ApprissCase Users`, `Basic Users`. Como el error es de dashboards, buscar además el
   grupo específico de dashboards o reporting.

## Duda abierta

Juan le dijo a David que entrara por `nordstrom.apprissretailcloud.com` y terminó en
`usprod`. Puede ser un redirect o que entrara por otra ruta. Confirmar con David la URL
exacta de login: si Nordstrom estuviera en PU, el sitio sería `app.apprissretail.com` y
entonces sí sería caso de Kiran.

RCS-28219 no se pudo abrir, el conector de Jira lleva caído toda la tarde (HTTP 404).

## Nordstrom RCS-28219: David Vargas sin permisos en dashboards — 18 ago 2026
_chunk 1696 · 2026-08-18 · fuente: inbox/2026-08-18-nordstrom-david-permisos.md_

# David sin permisos en dashboards de Nordstrom — RCS-28219

18 ago 2026. Juan ayudando a David Vargas. Error: `Permission Required` en
`usprod.apprissretailcloud.com/platform/cpf/errorhandler/nopermission`, con branding de
Nordstrom. David tampoco puede usar Impersonate User. Trey no maneja permisos dentro de apps.

## Qué dijo Kiran y qué significa

Kiran pidió *"the Prod url for Nordstrom"*. Juan le mandó enlaces profundos a dashboards.
Ella corrigió: *"I meant the signing url"* — quería la URL de **inicio de sesión**, con la
que identifica plataforma y tenant. Un `#/dashboard/...` no se lo dice.

Y el dato de fondo: *"usprod is not PU yet"*, *"app.apprissretail.com is pu"*.
**PU = Platform Unification.** El host que le pasaron es de la plataforma **clásica**, no de
la unificada, que es donde ella administra.

## La consecuencia práctica

David está entrando por **usprod**, o sea plataforma clásica. Sus permisos **no** se
administran del lado de Kiran, se administran en **Control Panel USPROD**, donde Juan ya
tiene acceso con `SupportL2` + `Engineers`. No hace falta escalar.

Ruta:
1. `usprod.apprissretailcloud.com/control`
2. En *Customers in USPROD*, **clic en el logo de Nordstrom** para entrar al tenant.
   No usar `/<slug>/signin`, que redirige al SSO del cliente donde el usuario de Appriss
   no existe.
3. All apps → Settings → Users → buscar a David
4. User details → Permission groups → agregar los que falten y **guardar**
5. Verificar la base de tres que llevan todos: `ApprissCase Search Users`,
   `ApprissCase Users`, `Basic Users`. Como el error es de dashboards, buscar además el
   grupo específico de dashboards o reporting.

## Duda abierta

Juan le dijo a David que entrara por `nordstrom.apprissretailcloud.com` y terminó en
`usprod`. Puede ser un redirect o que entrara por otra ruta. Confirmar con David la URL
exacta de login: si Nordstrom estuviera en PU, el sitio sería `app.apprissretail.com` y
entonces sí sería caso de Kiran.

RCS-28219 no se pudo abrir, el conector de Jira lleva caído toda la tarde (HTTP 404).

## RCS-28219 Nordstrom: por qué dan 403 los links y cómo reproducir — 18 ago 2026
_chunk 1697 · 2026-08-18 · fuente: inbox/2026-08-18-rcs-28219-403-links-y-repro.md_

# RCS-28219 — por qué dan 403 los links y cómo reproducir

Ticket: https://trebuco.atlassian.net/browse/RCS-28219
Nordstrom · Incident · Work in progress · asignado a David Vargas · reporta Sara Beaty (nordstrom.com)
Sintoma reportado: el parametro Location ID no funciona cuando se usa el data area Workview,
ni directamente ni en una search-of-a-search que lo consuma. Afecta Explorer y Dashboards.

## 1. El 403 no es el bug. Son tres problemas de acceso distintos.

### Links 1, 2 y 3 — host equivocado
Apuntan a `usprod.apprissretailcloud.com/platform/...`. `usprod` es el host de ENTORNO
(ahi vive el Control Panel), no el host de un tenant. La ruta `/platform/explorer` en ese
host resuelve contra el tenant de tu sesion actual. Sin sesion de tenant activa, o con
sesion en otro tenant, el server rechaza el path del contenido con 403.

El primer segmento del path NO es del usuario, es el GUID del espacio del tenant:
- `f287cbc6-65b9-490b-a8b6-4ac2ea3739df` = espacio de Nordstrom. Se confirma solo:
  el link 4, que ya va a `nordstrom.apprissretailcloud.com`, usa ese mismo GUID.
- `accb858f-c478-47e9-b770-7e715f5acb78` = otro espacio distinto. Sin confirmar cual.
  Puede ser otro tenant o un workspace aparte. Verificar al entrar.

### Link 4 — urldefense + SSO de Nordstrom
Va envuelto en `urldefense.com/v3/...`, el proxy de correo (Proofpoint) de Nordstrom.
Ese wrapper caduca y espera venir del correo original. Debajo apunta a
`nordstrom.apprissretailcloud.com`, que redirige al SSO de Nordstrom, donde el usuario
de Appriss no existe. Doble 403.

URL real desenvuelta:
https://nordstrom.apprissretailcloud.com/platform/dashboards#/dashboard/f287cbc6-65b9-490b-a8b6-4ac2ea3739df/wi%20dashboard%20test.dashboard

### Respondiendo la pregunta directa
No es "una busqueda especifica del usuario" en el sentido de estar atada a la cuenta de
Sara. El GUID es de espacio, no de persona. Pero el link 2 apunta a una carpeta
`working drafts`, o sea un borrador sin publicar. Un borrador puede seguir sin ser
visible incluso ya dentro del tenant correcto. Si eso pasa, pedirle a Sara que lo
publique o que exporte la definicion.

## 2. Que dicen las URLs sobre el bug

Link 1:
  searchPath   = /accb858f.../region and store parameters.search
  builderPath  = /system/ebr/ardm/store/builder/ardm.builder
  El builder es `/system/...`, existe en todos los tenants. Es ARDM sobre data area store.

Link 3 — este es el caso interesante, la search-of-a-search:
  searchDefinitionPath = /f287cbc6.../test wi with expanded hierarchy.search   (search base)
  searchPath           = /f287cbc6.../Test Search for WI Dashboard.search      (la que consume)
  "WI with expanded hierarchy" es la pista fuerte. La jerarquia expandida es sospechosa
  como causa: si expande a nodos padres de la jerarquia de ubicacion, el filtro por
  Location ID puede quedar sin efecto o aplicarse al nodo equivocado.

## 3. Paso a paso

### Ruta A — abrir el contenido original (preferida, es exactamente lo que ve el cliente)

1. Entrar a `https://usprod.apprissretailcloud.com/control`
2. Tabla *Customers in USPROD*, buscar Nordstrom.
3. Primera columna, **Click logo to sign in**. NO usar `/<slug>/signin`, eso manda al SSO
   del cliente. Si el logo falla, alternativa non-SAML: `?admin=true` al final de la URL
   de signin.
4. Ya dentro, la barra de direcciones muestra el host del tenant. Tomar ese host y pegarle
   detras el fragmento de la URL del ticket, todo desde el `#` en adelante. Ejemplo:

   https://nordstrom.apprissretailcloud.com/platform/explorer#/search?searchDefinitionPath=%2Ff287cbc6-65b9-490b-a8b6-4ac2ea3739df%2Ftest%20wi%20with%20expanded%20hierarchy.search&searchPath=%2Ff287cbc6-65b9-490b-a8b6-4ac2ea3739df%2FTest%20Search%20for%20WI%20Dashboard.search

5. OJO: es routing por hash. Cambiar solo lo que va despues del `#` no recarga la SPA.
   Recargar con F5 despues de pegar, si no se queda mostrando la vista anterior.
6. Si el path con GUID `accb858f` sigue en 403 desde Nordstrom, es que pertenece a otro
   espacio. Ese link 1 probablemente no es de Nordstrom.

### Ruta B — recrear desde cero (si el contenido original no abre)

Todo dentro del tenant, ya autenticado por Ruta A.

1. Explorer, nueva search sobre el data area **Workview**.
2. Agregar **Location ID** como PARAMETRO, no como filtro con valor fijo. La distincion
   importa, el bug reportado es del parametro.
3. Ejecutar en Explorer y cambiar el valor del parametro. **Este es el punto de biseccion
   mas importante del ticket**:
   - Si el parametro NO filtra ya aqui, el bug esta en el data area Workview.
   - Si SI filtra aqui pero falla en el dashboard, el bug esta en el paso de parametros
     del dashboard hacia la search. Son dos tickets de ENG muy distintos.
4. Crear encima una search-of-a-search que consuma la anterior, con la jerarquia expandida
   (replicando "test wi with expanded hierarchy"). Repetir la prueba del paso 3.
5. Crear un dashboard, meter la search como widget, mapear el parametro Location ID del
   dashboard al de la search.
6. Cambiar el valor del parametro en el dashboard y ver si cambia el conteo de filas.

### Control para aislar si es especifico de Workview
Repetir exactamente lo mismo con otro data area, por ejemplo el de store/ARDM del link 1
(`/system/ebr/ardm/store/builder/ardm.builder`). Si ahi Location ID SI filtra, queda
probado que es especifico de Workview y eso va derecho al ticket de ENG.

### Evidencia que hay que capturar para escalar
- DevTools abierto en pestana **Network** mientras se ejecuta la search.
- Buscar la request de ejecucion y revisar el payload: ¿el Location ID viaja en el body?
  ¿llega vacio? ¿llega pero el resultado lo ignora?
  - Va en el payload y aun asi no filtra -> el problema es del lado servidor / del data area.
  - No va en el payload -> se pierde en el mapeo de parametros del front.
- Screenshot del mismo widget con dos valores distintos de Location ID dando el mismo conteo.

## 4. Hipotesis a validar, no confirmadas
- La jerarquia expandida expande a nodos padres y el filtro de ubicacion queda mal aplicado.
- En Workview el Location ID puede estar mapeado a un campo distinto del esperado, por
  ejemplo la tienda del creador del work item y no la tienda del incidente.

## 5. Pendiente
- Confirmar de quien es el espacio `accb858f-c478-47e9-b770-7e715f5acb78`.
- Confirmar si `test dashboard.dashboard` bajo `working drafts` esta publicado.

## 6. Las 4 URLs listas para pegar

Base asumida: `nordstrom.apprissretailcloud.com`. Si al entrar por Control Panel el host que
queda en la barra es otro, cambiar SOLO esa parte y dejar todo lo demas igual.
Recordar F5 despues de pegar, es routing por hash.

### 1. Region and Store Parameters (search + builder ARDM store)
https://nordstrom.apprissretailcloud.com/platform/explorer#/search?searchPath=%2Faccb858f-c478-47e9-b770-7e715f5acb78%2Fregion%20and%20store%20parameters.search&builderPath=%2Fsystem%2Febr%2Fardm%2Fstore%2Fbuilder%2Fardm.builder

Este es el que mas probable siga en 403: el GUID accb858f NO es el espacio de Nordstrom.

### 2. Test Dashboard (working drafts)
https://nordstrom.apprissretailcloud.com/platform/dashboards#/dashboard/public/_2026/_2026%20dashboards/region%20and%20store%20status%20dashboard/working%20drafts/test%20dashboard.dashboard

Path bajo `public`, sin GUID. Si falla es por borrador sin publicar, no por tenant.

### 3. Test Search for WI Dashboard (search-of-a-search, el caso del bug)
https://nordstrom.apprissretailcloud.com/platform/explorer#/search?searchDefinitionPath=%2Ff287cbc6-65b9-490b-a8b6-4ac2ea3739df%2Ftest%20wi%20with%20expanded%20hierarchy.search&searchPath=%2Ff287cbc6-65b9-490b-a8b6-4ac2ea3739df%2FTest%20Search%20for%20WI%20Dashboard.search

GUID de Nordstrom. Este deberia abrir. Empezar por aca.

### 4. WI Dashboard Test (urldefense desenvuelto)
https://nordstrom.apprissretailcloud.com/platform/dashboards#/dashboard/f287cbc6-65b9-490b-a8b6-4ac2ea3739df/wi%20dashboard%20test.dashboard

Ya venia con el host de tenant correcto, solo habia que quitarle el wrapper de Proofpoint.
Decodificacion: el sufijo `__;IyUl` es base64 de los caracteres sustituidos por `*`,
en orden `#`, `%`, `%`. Coincide con el texto visible del link en el ticket.

## RCS-28442 Torrid SSO: a quién asignar y por qué la premisa del ticket está mal — 18 ago 2026
_chunk 1698 · 2026-08-18 · fuente: inbox/2026-08-18-rcs-28442-torrid-sso-asignacion.md_

# RCS-28442 Torrid SSO — a quien asignar, y por que la premisa del ticket esta mal

Fecha: 2026-08-18
Pedido en Teams (Aimee Wadsworth, 3:47 pm): "verificar los registros del SSO para ver
si la certificacion ya expiro".

## CONCLUSION CORTA

A quien: **Diego Buelvas**. Segunda opcion David Vargas.
NO Sebastian Rueda, aunque sea el de menor carga. Explicado abajo.

Pero antes de asignar: esto no es un ticket de Torrid. Es un incidente multi tenant.

## 1. La hipotesis del certificado expirado no cuadra

### Evidencia A: volumen anomalo
Tickets de login/access/SSO creados en RCS:
- 8 al 15 de agosto:  8 tickets   (linea base)
- 15 al 18 de agosto: 21 tickets  (casi 3x)

### Evidencia B: multiples clientes distintos, misma ventana
- RCS-28442 Torrid, Login Error, Critical, 18 ago
- RCS-28440 VSS, Login error with SSO, High, 18 ago
- RCS-28431 Stater Bros, Login Failure ("LPMS completamente caido"), 18 ago
- RCS-28429 Hobby Lobby, Server Error SSO Saml, 17 ago, YA CERRADO
- RCS-28409 Smart and Final, No Access, Session Error
- RCS-28419 Big Y, LPMS crashes
Un certificado de Torrid no tumba a Stater Bros, Hobby Lobby y Smart & Final.

### Evidencia C: el mismo AJ Mueller mata la hipotesis
Comentario del 18 a las 13:07: "at HQ this morning and I am able to login".
Y a las 16:39 su field team volvio a fallar.
Un certificado SAML expirado falla igual para todos, desde cualquier red, todo el tiempo.
Que dependa de la ubicacion apunta a red, IP allowlist o balanceo, no a cert.

### Evidencia D: la mas fuerte
RCS-28429 (Hobby Lobby, mismo error SAML) se cerro el 17 ago 19:34 con resolucion
**"Engineer Resolved - Restored Services"**. Sin nota de causa raiz.
"Restored Services" significa que alguien del lado Appriss restauro algo y volvio.
Eso encaja exacto con que AJ pudiera entrar el 18 en la manana y su equipo fallara
en la tarde. Servicio inestable, no certificado vencido.

### Que si hay que revisar primero
Preguntar a quien cerro RCS-28429 QUE restauro exactamente. Es muy probable que sea
la misma causa raiz y la respuesta ya exista, sin investigar nada desde cero.

## 2. Carga real del equipo Colombia

Tickets RCS abiertos (statusCategory != Done) al 18 ago 2026:

| Persona          | Abiertos | Tickets SSO/login historicos | Estado |
|---|---|---|---|
| Sebastian Rueda  | 10 | 0  | disponible |
| David Vargas     | 12 | 4  | ya tiene RCS-28219 Nordstrom |
| Diego Buelvas    | 13 | 4  | disponible |
| Camila Cortes    | -- | -- | FUERA DE OFICINA (aviso en Teams) |
| David Lora       | -- | -- | sin cuenta Jira activa |
| Julian Orjuela   | -- | -- | sin cuenta Jira activa |

## 3. Por que Diego Buelvas y no Sebastian Rueda

La diferencia 10 vs 12 vs 13 es ruido, no es carga distinta. Asi que la carga no
puede ser el criterio. El criterio real es el perfil.

Sebastian Rueda tiene **cero** tickets de SSO, login, SAML o acceso en su historial.
Su carga abierta es toda de datos y pipeline: Nike data load, Nike receipts null,
CWH voided PLU, Gen Parts receipt items, Alshaya error counts. Es el perfil de datos
del equipo. Meterlo en un incidente de autenticacion multi tenant, en Critical y con
el cliente encima, es ponerlo a aprender bajo presion en el peor momento posible.

Diego Buelvas tiene 4 tickets de SSO/login/acceso y solo un ticket abierto mas que
Rueda. Es la opcion correcta.

David Vargas tambien tiene 4 y funciona, pero ya carga RCS-28219 de Nordstrom, que
tambien es investigacion abierta. Dejarlo como segunda opcion.

## 4. Mensaje para Teams (ingles, pegable)

Happy to take this one. Before we chase the certificate angle, one thing worth flagging.

This does not look like a Torrid specific certificate expiry. We have 21 login and SSO
tickets created since August 15, against 8 in the previous week, and they span different
tenants: Torrid, VSS, Stater Bros, Hobby Lobby, Smart and Final and Big Y. A tenant
certificate would not affect all of them at once.

Two more things point away from an expired cert. AJ Mueller reported he could log in from
HQ on Tuesday morning while his field team still could not, and an expired SAML cert fails
the same way from every network. And RCS-28429 for Hobby Lobby, which is the same SAML
server error, was closed on August 17 as Engineer Resolved, Restored Services, with no root
cause recorded.

Suggested first step is to find out what was actually restored on RCS-28429, since it is
very likely the same root cause and the answer may already exist. Diego Buelvas has the
background on SSO tickets and can pick this up.

## 5. Pendientes
- Confirmar con quien cerro RCS-28429 que se restauro exactamente.
- Si se confirma causa comun, agrupar los 21 tickets bajo un solo incidente en vez de
  investigarlos por separado.

## RCS-28153. `TryRefreshPlatformCohesionCookie`, el refresh de ventana deslizante del `CPFCookie` que corre en cada carga d — 2026-08-27
_chunk 1721 · 2026-08-27 · fuente: inbox/2026-08-27-rcs-28153-fix-liberado.md;2026-08-27-rcs-28153-verificacion-tenant.md_

Ticket RCS-28153. Trabajado el 2026-08-27. 2 notas en inbox.

## Causa
`TryRefreshPlatformCohesionCookie`, el refresh de ventana deslizante del `CPFCookie` que corre en cada
carga de página de Nettrack, leía el timeout de sesión desde
`System.Configuration.ConfigurationManager.AppSettings("CPF.Core.LogOnTimeoutMinutes")`.
Esa clave de `web.config` **nunca se cableó**. El refresh caía siempre al default hardcodeado de 60
minutos e ignoraba el timeout configurado del tenant. Los usuarios que trabajaban solo dentro de
Nettrack quedaban deslogueados en el momento equivocado respecto de la sesión de la plataforma Secure.

Solución: leer el valor desde `secure.ConfigurationItem`, reusando
`LPSBO.Common.ReadEffectiveConfigurationValue(Name, PlatformID)`, que se amplió de `Private Shared` a
`Public Shared` porque ya la usaba el flag de screen label de ENG-7168. Resuelve
`COALESCE(NULLIF(CustomerEditedValue,''), Value)` para el ClientID del request, la misma precedencia
de override que espera el Control Panel. El decrypt de la cookie se movió más arriba en el método
para que `info.ClientID` esté disponible.

Eso también explica el comentario de Vedant del 19 ago sobre probar con `CustomerEditedValue` en 1.

## Evidencia
**Capa 1, el ticket ENG.** ENG-7184 en `Done`, resolution `Resolved`, fixVersion
`Secure August 2026 Release 2/2` con `released: true` y fecha 27 ago. Labels `lpguys-deployed-prod`
y `lpguys-deployed-test`.

**Capa 2, las Release Notes.** Página `Secure August 2026 Release 2/2 Release Notes`, espacio ARPDT,
id 478150459393, autora Shandana Khan, estado Released, fecha 8/27/2026.
https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/478150459393

ENG-7184 aparece en la sección **`Completed issues by product area`**, la de trabajo entregado. La
línea literal:

> ENG-7184 — Platform session cookie expiry discards in-progress case entry

No está en `Open and follow-up items`, no lleva salvedad y no está duplicado. Cuenta como entregado.

**Dato que importa.** De los 118 issues del fixVersion solo 81 están en Done. Un fixVersion liberado
no implica que todo lo que viaja en él esté listo. ENG-7184 sí lo está.

**Confirmado además:** ENG-6220, Sign Out Behaviours, **no aparece en este release**. La cadena "Sign
Out" no está en la página. Eso ratifica el matiz: escríbele a Ashley solo sobre los logouts
prematuros por timeout.

## Rastro
2026-08-27 inbox/2026-08-27-rcs-28153-fix-liberado.md
2026-08-27 inbox/2026-08-27-rcs-28153-verificacion-tenant.md

## RCS-28212. Cuando un incidente de 7-Eleven se eleva a caso, APIS copia el código corto del incidente al campo Case Type d — 2026-09-02
_chunk 1722 · 2026-09-02 · fuente: inbox/2026-09-02-rcs-28212-informe.md;2026-09-02-rcs-28212-instructivo.md_

Ticket RCS-28212. Trabajado el 2026-09-02. 2 notas en inbox.

## Que pasa
Cuando un incidente de 7-Eleven se eleva a caso, APIS copia el código corto del incidente al campo
Case Type del caso en lugar de mapearlo al valor de la lista de casos. El resultado es un caso con
Case Type `* COR` en vez de `Corporate`, y el reporte AdHoc "Corp_Internal_Theft_Fraud" filtra por
igualdad exacta contra `Corporate`, así que esos casos desaparecen del reporte. El caso creado
directamente sí sale bien, lo que aísla el defecto al camino de elevación.

---

## Causa
**Hipótesis, no causa raíz confirmada.** La marco como hipótesis porque falta un paso de
verificación que exige entrar a APIS.

Enunciado: el camino de elevación de incidente a caso copia el valor de tipificación del incidente
al campo homólogo del caso sin mapearlo a la lista de valores de caso. La lista de casos no contiene
`COR`, contiene `CORP` con etiqueta `Corporate`, así que el valor queda huérfano y la UI lo pinta
con asterisco. El mismo mecanismo explica `* CORPORATE EMPLOYEE` en el sub type y el
`Event Alpha Code` vacío.

Lo que sostiene la hipótesis: el asterisco en dos campos a la vez, el `Related incident (Elevated)`
presente solo en los casos malos, el campo requerido sin poblar, y el contraste con
`CA-43895-CORP-2026-0001` que se creó bien.

Lo que falta para confirmarla: abrir en APIS la lista de Case Types del tenant 7-Eleven y verificar
si `COR` existe como valor activo, como valor desactivado, o si no existe. Y abrir un caso bueno
para confirmar que no tiene `Related incident (Elevated)`. El instructivo lleva los dos pasos.

Descartada por evidencia: error de digitación del usuario. Un usuario no escribe el asterisco, la
aplicación lo pinta.

---

## Evidencia
**1. El reporte filtra por igualdad exacta contra un literal.**
Fuente: captura 1, pantalla "Ad Hoc Query Builder: Configure filters", Report Title
`Corp_Internal_Theft_Fraud`. La primera línea de filtro es:

    Selected Column: case.event_type
    Report.default label: Case Type
    Report.name of filter: case.event_type
    Comparison Operator: =
    Operand: Corporate
    User Input Type: Fixed

Operador `=`, operando `Corporate`, tipo Fixed. Un caso cuyo `event_type` valga `COR` nunca entra
en ese resultado. El síntoma reportado queda explicado sin necesidad de hipótesis adicional.

La segunda línea usa otro operador. `case.event_sub_type` con `IN` sobre una lista múltiple que
incluye CDC Chargebacks, Critical Incident, Expense Fraud AP y Fraud. El pie de la pantalla lo
confirma: "Use comma delimiter with IN". El constructor sí soporta `IN` en ese campo.

**2. El caso malo nació de una elevación, y lo dice el propio caso.**
Fuente: captura 2, ficha de `CA-44541-COR-2026-0001`. En el bloque Additional Information:

    Related incident: IN-44541-COR-2026-0001 (Elevated)

El incidente origen ya trae `COR` en su número. El caso heredó ese mismo `COR`.

**3. El valor mostrado llev

## Impacto
Alcance dentro de 7-Eleven: todo caso elevado desde un incidente queda fuera de cualquier reporte
AdHoc que filtre `case.event_type` con operador `=`. El reporte 5165 es uno. Hay que contar cuántos
más usan igualdad exacta sobre ese campo, porque el mismo hueco los afecta a todos.

Alcance fuera de 7-Eleven: el camino de elevación es código de producto, no configuración de tenant.
Los otros catorce clientes de APIS que elevan incidentes a casos podrían tener el mismo hueco sin
haberlo notado, porque solo se ve si construyeron un reporte con filtro exacto. Los nombres están en
`brain/markdown/21-kt-kristin-sign-off-procesos-rts.md` líneas 599 a 619, documento interno, no
compartir fuera.

Riesgo de negocio para el cliente: los casos que no salen del reporte son de robo interno
corporativo. El caso de la captura vale 1.930,32 USD con reason CASH THEFT. Casos que existen y no
aparecen en el reporte de fraude interno es un hueco de reporting, no un hueco cosmético.

Riesgo de la ventana: 7-Eleven migra a Incident alrededor de sep/oct 2026. Un arreglo de código en
APIS no va a llegar a tiempo ni está permitido por política. El entregable realista es el
workaround en el reporte más una c

## Que sigue
**Recomendación: avanza tú, no lo sueltes, y tampoco te lo lleves entero.**

Razones. El ticket lleva quince días sin movimiento desde el comentario de Viraj del 18 de agosto.
Tienes acceso a PROD de APIS. La parte que desbloquea al cliente hoy es configuración de reporte,
que es trabajo de soporte, no de ingeniería. La parte que exige escritura en base de datos es de
Kamminga y solo de él.

El reparto que propongo:

1. Tú verificas en APIS los dos puntos que faltan para cerrar la causa raíz, y pruebas el workaround
   del filtro `IN`. Eso convierte una hipótesis en un diagnóstico cerrado.
2. Tú le entregas a Kamminga el diagnóstico cerrado más el conteo de casos afectados. Él decide la
   corrección de datos.
3. El cliente recibe el workaround del reporte cuando el ticket vuelva a soporte, o antes si
   Kamminga lo autoriza.

Qué **no** hacer todavía. El ticket está en Under Engineering Review con assignee de Engineering. No
le comentes al cliente sobre el fondo del defecto mientras siga así. Ese es el error que se cometió
en RCS-28161.

Los pasos concretos, en orden y listos para ejecutar, están en el instructivo.

## Precedentes
| Ticket | Qué aporta | Estado |
|---|---|---|
| RCS-1508 | 7-Eleven APIS, case types. Kamminga documenta que `Event Type` en pantalla es `event_sub_type` en el filtro, y que el cliente crea sus propios subtipos. Rounok Joardar cerró ajustando el formulario del incidente | Closed |
| RCS-12432 | Define elevar como investigación → caso, y que hay campos requeridos configurables antes de elevar | Closed |
| RCS-3053 | Krogman confirma que mover CA a IN no existe en APIS y sería un enhancement cobrable | Closed |
| RCS-27330 | 7-Eleven APIS, sin valor. Krogman: "Claude opened this ticket from a search I was doing. Not needed". Descartar | Closed |

Sin precedente de truncamiento COR contra CORP. RCS-28212 es el primero, y la búsqueda de
"Corp Internal Theft Fraud" en todo el Jira devuelve solo este ticket.

---

## Rastro
2026-09-02 inbox/2026-09-02-rcs-28212-informe.md
2026-09-02 inbox/2026-09-02-rcs-28212-instructivo.md

## RCS-28631. El ticket tiene dos problemas separados y Luis ya resolvio uno. El pendiente es que cuatro definiciones de Wor — 2026-09-04
_chunk 1740 · 2026-09-04 · fuente: inbox/2026-09-04-rcs-28631-informe.md;2026-09-04-rcs-28631-instructivo.md_

Ticket RCS-28631. Trabajado el 2026-09-04. 2 notas en inbox.

## Que pasa
El ticket tiene dos problemas separados y Luis ya resolvio uno. El pendiente es que cuatro definiciones de Work Item nuevas, 900, 901, 902 y 118, son invisibles para todo usuario de Nordstrom sin importar equipo ni rol de Administrator, mientras las definiciones viejas 116 y 117 siguen visibles. Luis ya escalo esto una vez a Under Engineering Review con Shandana Khan de assignee, ella lo devolvio a Under Delivery Review por considerarlo permiso o configuracion y no bug, y Luis respondio con un analisis de codigo que apunta a un bug de plataforma. El ticket esta hoy otra vez en Under Delivery Review, con la respuesta de Luis sin una segunda escalacion formal detras.

## Causa
Hipotesis, marcada como tal por el propio Luis y no verificada contra base de datos todavia. El endpoint Save de ApiController.cs no normaliza el sufijo `.fti` en `VirtualFilePath` antes de persistir, a diferencia del endpoint Get que si lo hace. Si el flujo "New" del Composer envia un vfp sin `.fti`, el campo `Extension` en `secure.Repo` queda correcto pero `VirtualFilePath` no, y cualquier regla de `filemappings.json` que dependa de que el path termine en `.fti` deja de matchear, lo que vacia el panel de Permissions para ese archivo especifico. Explica por que 900, 901, 902 y 118 estan rotos y 116 y 117 no: son items guardados antes y despues de que el problema empezara a manifestarse. Luis no corrio la consulta SQL que confirmaria esto, esta en su lista de verificacion sugerida y pide acceso de base de datos que Support no tiene.

## Evidencia
La membresia del equipo Admin se caia sola cada dia. Sara Beaty, 1 sep 2026: "I've added myself and Brent Hamlin to the list 3 times now, but when I check the next day, we're no longer on the list." Luis lo marca resuelto en su comentario del 3 sep: agrego "Admin" a Mandatory Teams en la configuracion SSO de Nordstrom, Control Panel, Client SSO Config, y confirmo que persiste tras guardar y recargar. Cita textual de Luis sobre la causa de esa parte: "This stops the SSO login flow from wiping the Admin team assignment for Sara Beaty / Brent Hamlin on each login."

La visibilidad de los work items nuevos sigue rota, independiente de equipos. Luis, mismo comentario del 3 sep: "confirmed no user of any team can see work items 900, 901, 902, or a brand-new item (118), while pre-existing items (116, 117) are unaffected." La reproduccion en vivo esta descrita y sostenida por capturas adjuntas: el lightbox de Permissions en Work Item Composer abre y muestra "Permissions Details" vacio, "Selected Groups" con el texto "There are no permissions available for this file", y un toast "Unable to process the request. Please contact your administrator if the issue persists."

## Impacto
Toda definicion nueva de Work Item que Nordstrom guarde en Secure Store queda con el panel de permisos vacio hasta que se corrija el codigo. Si la hipotesis de Luis es correcta, esto no es exclusivo de Nordstrom. Cualquier cliente que use el Composer para crear un Work Item nuevo despues de que el defecto entrara en produccion puede tener el mismo sintoma sin haberlo reportado todavia. Nadie ha corrido el barrido para saber cuantos `secure.Repo.VirtualFilePath` de tipo FTI carecen del sufijo `.fti` fuera de Nordstrom.

## Que sigue
El ticket ya paso una vez por Under Engineering Review con Shandana Khan y ella lo devolvio, con esta condicion explicita: "Please feel free to send back to Engineering with supporting details if it's felt this is a platform-level bug though." Luis entrego esas supporting details en el mismo hilo, con archivos y numeros de linea concretos, pero eso quedo solo como comentario. Nadie repitio la transicion despues. El unico cambio posterior fue Juan reasignando el ticket a Luis, sin tocar el Status.

Segun la regla de ruteo y el precedente RCS-28283, la evidencia que hay hoy justifica una segunda escalacion, no quedarse en Delivery. La diferencia con la primera vez es que ahora hay que dirigirla a Shandana puntualmente, porque ella ya la rechazo una vez y una segunda transicion silenciosa corre el riesgo de que la rebote de nuevo sin leer el analisis. Conviene que el comentario de re escalacion la mencione a ella directamente y cite su propia condicion, no solo repetir la transicion. Falta ademas avisarle a Sara Beaty que el ticket vuelve a moverse, requisito previo a cualquier escalacion segun el doc de Aimee. El detalle de la transicion y el aviso al cliente va en el instructivo apa

## Precedentes
RCS-28283, TG Jones, mismo Product Type Secure 5 EBR, mismo dilema de ruteo entre Delivery y Engineering, documentado en `brain/markdown/19-rcs-procesos-playbook.md`, seccion "2. RCS-28283". Cita textual de esa nota: "La regla es codigo o bug a Engineering, dato o configuracion ya en produccion a Delivery. La descripcion dice bug de aplicacion, asi que Engineering es lo razonable, pero eso lo decide la reproduccion, no la descripcion." Ese ticket se resolvio reproduciendo y documentando primero, y transicionando despues a Under Engineering Review con Shandana Khan como assignee.

`brain/memoria/reference_escalacion_l3_procedimiento.md` fija la tabla de ruteo de Aimee Wadsworth: Secure / Incident Engineering va a Under Engineering Review con Shandana Khan, y el ENG se autocrea con la transicion, no se crea a mano.

`brain/markdown/19-rcs-procesos-playbook.md` linea 961 separa el contacto de Delivery para Secure Store (Sec 3/4/5), que es Tomasz Mikunda o Carl Costelow para datos y configuracion ya en produccion, del contacto Peyman Motlagh que en `reference_escalacion_l3_procedimiento.md` aparece ligado a "Secure 5" pero que en la practica, ver `reference_peyman_motlagh.md` y los pre

## Rastro
2026-09-04 inbox/2026-09-04-rcs-28631-informe.md
2026-09-04 inbox/2026-09-04-rcs-28631-instructivo.md

## RCS-28756. Nike, cliente 067, dejo de enviar archivos ECOM raw_order a partir del 28 de agosto de 2026. El ultimo archivo — 2026-09-04
_chunk 1750 · 2026-09-04 · fuente: inbox/2026-09-04-rcs-28756-informe.md;2026-09-04-rcs-28756-instructivo.md_

Ticket RCS-28756. Trabajado el 2026-09-04. 2 notas en inbox.

## Que pasa
Nike, cliente 067, dejo de enviar archivos ECOM raw_order a partir del 28 de agosto de 2026. El
ultimo archivo cargado fue el 27 de agosto a las 19:02 UTC. Hoy 4 de septiembre el cliente ya fue
notificado, el proximo seguimiento esta agendado para el 8 de septiembre a las 8pm IST via
RTS-206999, y la revision de logs que aporto Juan descarta el pipeline ARDM de Appriss como causa.

## Causa
Marco esto como HIPOTESIS, no como causa raiz confirmada. Nike dejo de enviar archivos
ECOM/raw_order a partir del 28 de agosto de 2026. La sostienen tres puntos independientes: la
ausencia de archivos nuevos despues del 27 de agosto a las 19:02 UTC, la confirmacion de Carl de
que los servicios de ingesta de Appriss estan arriba, y la ejecucion limpia del pipeline ARDM para
cliente 067 en la ventana revisada por Juan. Ningun log revisado muestra una falla de Appriss que
explique el corte. Nike no ha confirmado la causa de su lado a la fecha de este informe.

## Evidencia
Ultimo archivo cargado, citado en la propia descripcion del ticket:
`prd-datacloud-wus2-ehub-1/c67_rawdata_order/2026/08/27/19/02_42_1.avro`, corrida
`Pipelines - Run 20260827.2`. Ningun archivo ECOM cargo despues de la corrida
`Pipelines - Run 20260828.1`.

Carl, de ingenieria, confirmo que los servicios de Appriss estan arriba:

> "Checked with Carl. He has confirmed that services are ups and running. we are not receiving any
> data from the Nike for the ECOM/RAW_ORDER feed after the 28th Aug, 2026."
— Anil P, comentario en RTS-206999, 2026-09-04T09:07:39

El cliente ya fue notificado por correo:

> "Mail has been sent to client as we have stopped receiving the ECOM data from 2026-08-28."
— Anil P, comentario en RTS-206999, 2026-09-04T10:18:02

El correo mismo quedo capturado en el adjunto de pantalla que trajo Juan, asunto
`[RTS-206999] Nike Load`, enviado el viernes 4 de septiembre a las 7:44pm a Taylor Gilgan y Chris
Coomler de Nike, con copia al equipo de soporte. El cuerpo dice literal: "We have noticed that we
stopped receiving ECOM data from your end to our ingestion API, from 2026-08-28. Due to this, we
are observing low data loaded from Trading day 2026-08-28." La tabla 

## Impacto
Los Work Items del control GNG para Nike/67 quedan en pausa desde el 1 de septiembre por conteo
bajo el minimo de 560392 transacciones. Eso incluye definiciones de auditoria de descuentos no
autorizados y de fraude en devoluciones, segun el listado de Ayesha Mehar del 3 de septiembre. Cada
dia adicional sin archivos ECOM ensancha la brecha de datos y retrasa esos controles de manera
acumulativa, no puntual.

## Que sigue
La decision pendiente no es tecnica, es de estado del ticket. RCS-28756 sigue en Under Support
Review desde el 3 de septiembre pese a que la investigacion de soporte esta cerrada y lo unico
pendiente es la respuesta de Nike, ya agendada para el 8 de septiembre via RTS-206999. Dejarlo en
Under Support Review dos dias mas dice, para quien mire la cola, que falta trabajo de Appriss.
No es el caso. La transicion a Under Customer Review documenta con precision donde esta el bloqueo
real. El instructivo trae el comentario y la transicion listos para pegar.

## Precedentes
RTS-206999 es el ticket donde vive la investigacion tecnica completa y la comunicacion con el
cliente. RCS-28756 y RTS-206999 se referencian mutuamente desde el 3 de septiembre.

El runbook generico de monitoreo SnowTime documenta "cliente dejo de enviar" como una de las tres
causas comunes de un feed sin datos, junto a infraestructura de Azure Blob Storage y cambios de
formato con rechazos silenciosos. Esta en
`brain/markdown/20-snowtime-monitoring-migración.md`, linea 64. Describe el stack de feeds via
Azure Function Loader, no el pipeline pyARDM que usa Nike. Sirve como patron general, no como caso
identico resuelto.

El feed INKIRU de refund verification de Walmart lleva parado desde el 30 de marzo de 2026 sin
causa raiz confirmada, documentado en `tickets/RCS-28620.md` y en
`inbox/2026-08-31-rcs-28618-comentario-interno.md`. Es la referencia de que un feed externo
detenido puede alargarse meses si el cliente no prioriza la respuesta. No es un precedente resuelto,
es una advertencia de riesgo.

## Rastro
2026-09-04 inbox/2026-09-04-rcs-28756-informe.md
2026-09-04 inbox/2026-09-04-rcs-28756-instructivo.md

## Cosecha: RCS-28452 TempArea y la familia de fallas de Smart Alerts — 2026-08-27
_chunk 1754 · 2026-08-27 · fuente: inbox/2026-08-27-cosecha-rcs-28452.md_

# Cosecha: RCS-28452 TempArea y la familia de fallas de Smart Alerts

Fecha: 2026-08-27. Sesión de origen: local_957c60cc-8505-4e22-8c2b-900c01c874cf,
"Caso de Sebastian 28452". Todo sale de Jira y Confluence en vivo.

## Dueño

Juan asignó RCS-28452, SpartanNash, a Sebastián Rueda. Él pidió el contexto y el KB de Smart Alerts
porque ya había trabajado un caso del mismo síntoma.

Sus otros dos abiertos: RCS-28465 y RCS-28534, ambos Stater Bros., ambos en Under Support Review.

Acción pendiente que quedó nombrada: enviar el follow up a Jason Mann. RCS-28452 lleva sin respuesta
desde el 19 de agosto, después de que David Vargas tomó ownership.

## Causa raíz confirmada del caso anterior: RCS-28106

RCS-28106, Santikos, SmartAlerts Not working. Engineering lo resolvió en ENG-6612, asignado a
Matthew Kamminga, released en Secure August 2026 Release 1/2 el 13-ago-2026. PR 55537.

Dos bugs en `Sources/Incident/Components/LPSBO/SmartAlert.vb`:

Bug 1, línea 703. El guard de separador final solo revisaba `\`. En modo Platform Cohesion las rutas
usan `/`, así que el código agregaba `\` encima y producía rutas inválidas del tipo
`/incident/411/lpms/\filename.pdf`. Falla el lookup del adjunto.

Bug 2, línea 1106 más las ramas Case/HR alrededor de L1433 y SRMS alrededor de L1475. El código
llamaba `FileLen(strPath)` en vez de `AzureFilesystem.GetBlobSize(strPath)`. En Cohesion los
archivos viven en Azure Blob Storage. `FileLen` mira el filesystem local, tira file not found y
descarta el adjunto en silencio.

El ENG clasifica el patrón como "blob storage gate pattern failure": código que condiciona en
`IsPlatformCohesionMode()` en algunas ramas y no en todas.

## Precedente del string "TempArea": ENG-2154

Mismo string de error exacto que RCS-28452. Resuelto en Secure May 2026 Release 2/2.

Causa raíz: `ASPxUploadControl` tenía hardcoded `AdvancedModeSettings-TemporaryFolder="~/TempArea"`
en el markup. En Azure App Service `~/TempArea` resuelve a
`C:\home\site\wwwroot\nettrack\TempArea`, ruta que no existe. El fix movió la asignación a
`Page_Init` chequeando `LPSDAL.GlobalAppConfiguration.RunningInAzure`.

Archivo afectado: `CAMSImportAudit.aspx`. No es `SmartAlert.vb`. El patrón compartido es ruta
temporal mal resuelta en Azure y Cohesion. Punto de arranque de la investigación, no causa
confirmada para RCS-28452.

## Dato de tiempo a verificar

El cliente reporta que el problema empezó entre el 10 y el 13 de agosto. ENG-6612 salió el 13 de
agosto. Verificar si RCS-28452 es regresión de ese fix antes de escribirle al cliente.

## Contexto vivo de la familia

ENG-6541, "Harden smartalerts functionality", en Backlog con Matthew Kamminga. Es el paraguas del
tema.

RCS-28131, Sportman, Smart Alerts not working, en Under Engineering Review con Kamminga.

RCS-28294, Vallarta, Smart Alerts no Triggering, de Juan. Mismo label `Uni_Jul_26_AlertsNotifications`
que RCS-28106.

## Knowledge base de Smart Alerts que existe en Confluence

| Página | Espacio | Contenido |
|---|---|---|
| Smart Alert Config, 475461517316 | RTS | Standard contra Special, tabs de configuración, filtros, Attach PDF to Email, Include Attachment Types, límite de 25mb, tags |
| Alert Not Triggered, 476537552897 | RTS | Pasos de investigación cuando la alerta no dispara |
| Smart Alerts, Stale Subscriptions After Region Reassignment, 477449814017 | RCS | Suscripciones que no se actualizan al cambiar región |
| Incident (LPMS) vs Audit (CAMS): Setup Differences, 478022959110 | RTS | Sección de Smart Alert wiring y known failure modes |
| RET20260727, Platform Unification Jul 26 Wave, Bucket Review, 478085283848 | PBM | El bucket de alertas de esta ola |

## Fuentes

- https://trebuco.atlassian.net/browse/RCS-28452
- https://trebuco.atlassian.net/browse/RCS-28106
- https://trebuco.atlassian.net/browse/ENG-6612
- https://trebuco.atlassian.net/browse/ENG-2154
- https://trebuco.atlassian.net/browse/ENG-6541
- https://trebuco.atlassian.net/browse/RCS-28131


## Rastro
2026-08-27 inbox/2026-08-27-cosecha-rcs-28452.md

## Cosecha: a quién se asigna un RTS al escalarlo — 2026-08-27
_chunk 1755 · 2026-08-27 · fuente: inbox/2026-08-27-cosecha-rts-escalacion.md_

# Cosecha: a quién se asigna un RTS al escalarlo

Fecha: 2026-08-27. Sesión de origen: local_c3f3a283-f4b8-42d7-a140-4976e98ec0c5,
"RTS escalation team assignments". Medido contra Confluence y Jira en vivo.

## Hallazgo central

La matriz de assignees de L3 es de RCS, no de RTS. La página 478006902856 lo dice literal: "when
moving RCS tickets to different L3 departments". No existe matriz publicada de assignees para RTS.

En RTS el status enruta el ticket. El assignee se queda con el ingeniero de L1 que tiene el alert.

## Mediciones en Jira, 27 ago 2026

RTS con assignee Shandana Khan, Peyman Motlagh o Ian Williams, creados en los últimos 365 días: 1
ticket en total entre los tres.

Los 15 RTS más recientes que pasaron por `Under Engineering Review` en 180 días conservan su
assignee de L1 y llevan el label `L1`. Ninguno se reasignó.

RTS abiertos hoy en `Under Engineering Review`: 2. Uno sin asignar, uno con Matthew Kamminga.

En `Under Support Data Team Review`, sobre los 50 RTS que pasaron por ese status en 60 días, los 13
assignees distintos son todos del equipo L1 de India. Se agrega el label `Support_Data_Team` y el
assignee no cambia.

El equipo Support de Colombia ha tocado 12 RTS en toda la historia del proyecto. Uno solo pasó por
`Under Engineering Review`.

## El único precedente del equipo: RTS-206268

Grafana, Kinney Drugs (KNY/179), Active Alerts: 1. Reporter svc rts. Timeline del changelog:

| Fecha y hora | Quién | Qué hizo |
|---|---|---|
| 20-ago 20:49 | Madhuraj Gujaran (L1) | Se quita el assignee, pasa a `Under L2 Support Review` |
| 21-ago 10:19 | Diego Buelvas | Se asigna, pasa a Work in progress |
| 21-ago 12:34:06 | Diego Buelvas | Publica el informe de triage completo |
| 21-ago 12:34:17 | Diego Buelvas | Pasa a `Under Engineering Review` |
| 21-ago 12:34:34 | Diego Buelvas | Se quita el assignee, queda sin asignar |
| 22, 23 y 24-ago | svc rts | El alert sigue firing, nadie de engineering lo toca |
| 24-ago 06:13 | Vlad Bogus | Comenta "Ticket Moved to RCS: RCS-28543" |
| 24-ago 06:14 | Vlad Bogus | Under Engineering Review → Completed |

Diego lo dejó sin asignar. Nadie de engineering lo recogió en tres días. Vlad Bogus resolvió el caso
convirtiéndolo en RCS-28543.

La causa raíz no llegó por el status. Llegó por Teams. Shireesh Ramdas de L1 pegó el 21-ago a las
05:30 el link al canal R&D > 2026 SnowTime con el mensaje de Daniel Endersby. Causa raíz de ese
alert: la migración SnowTime, error de compilación de Snowflake, invalid identifier `T2.POS_ARTICL`.

## Procedimiento para el equipo

Al pasar un RTS a `Under Engineering Review`, dejarlo sin asignar. Misma regla que RTI/RTIaaS.

El status por sí solo no consigue que nadie actúe. Postear en el canal de Teams del dominio. Secure
5 Issues si es Secure 5.

Si hay impacto en cliente, convertirlo en RCS. Ahí sí aplica la matriz de L3 con Shandana Khan o
Peyman Motlagh.

## Camino de escalación a Data Engineering

Fuente: "Process - Internal Alerts", espacio DS, página 478102126595, Chris Howard, 12-ago-2026. Si
el retry del task en Snowflake no lo arregla, escalar a Data Engineering por Teams y OpsGenie, y
avisar en el canal Data Engineering > Alerts. Miembros al 12-ago-2026: Chris Howard, Nicholas Turner
y Saddam Hussain como manager.

## Matriz de L3 para RCS, referencia

| Producto | Assignee |
|---|---|
| Secure / Incident Engineering | Shandana Khan. Se auto crea un ENG y los comentarios sincronizan en ambos sentidos |
| Engage Engineering | Ian Williams. Mensaje obligatorio por Teams. Backups Shruti Golwalker y Kenny Vu |
| RTI / RTIaaS | Dejar sin asignar. Los engineers lo toman de su cola |
| Support Data Team | Peyman Motlagh. Label `Support_Data_Team`, Team Ownership "Support (Delivery dep.)", Sprint "RCS Support Team". Alcance solo Secure 5 |

## Fuentes

- https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478006902856
- https://trebuco.atlassian.net/wiki/spaces/DS/pages/478102126595
- https://trebuco.atlassian.net/browse/RTS-206268
- https://trebuco.atlassian.net/browse/RCS-28543

El detalle completo de esta sesión quedó en `inbox/2026-08-27-rts-escalacion-a-quien-asignar.md`.


## Rastro
2026-08-27 inbox/2026-08-27-cosecha-rts-escalacion.md

## Cosecha cola-proceso — 2026-08-28 — 2026-08-28
_chunk 1763 · 2026-08-28 · fuente: inbox/2026-08-28-cosecha-cola-proceso.md_

# Cosecha cola-proceso — 2026-08-28
Fuente: sesiones local_e3fd54bb-46fc-4e37-b348-de3ac2724e7f, local_2c86f407-b8b7-4cc0-b29b-eed21a678c7f y local_82b793ff-9432-4abd-93b2-93f1e7db5867

## Hallazgos verificados

El clasificador de la cola bajó del 100%. Dos corridas del día lo midieron por separado: una dio 67% y la otra dio 64%, esta última con 9 aciertos de 14 casos según `bin/eval_cola.py`.

La causa no es el léxico. `cola/EVAL-clasificador.json` se fijó el 24 de agosto y el estado real de los tickets avanzó después. Las fallas por etiqueta vencida se identificaron una por una: RCS-28327, RCS-28289, RCS-27765, RCS-28482 y RCS-28123. El clasificador leyó el estado correcto en los cinco. El set de referencia quedó atrás.

Existe una falla real de léxico. RCS-28256 lleva dos señales en el mismo comentario del 25 de agosto: pide confirmación al cliente y promete seguimiento. `cola.py` lo manda a nivel 3. La lectura humana lo pone en nivel 2.

Regla de reloj corregida. El plazo de 24 horas hacia el cliente corre solo cuando el cliente pregunta algo. Un acuse de recibo sin pregunta no abre plazo. El caso que lo estableció fue RCS-28482, donde Jim Cosseboom solo acusó recibo.

Escalación de RCS-28294. El changelog confirma que Juan sí transicionó a Under Engineering Review el 25 de agosto a las 20:02 con Shandana Khan como assignee. Shandana lo devolvió a Under Support Review el 26 a las 08:02 y pidió pasos exactos de reproducción en el mismo minuto. Devolver el ticket es su forma de pedir el dato, no una segunda decisión. Repitió el mismo patrón en RCS-27991.

El comentario del 25 cumplía uno de los cinco requisitos del checklist de Aimee Wadsworth. Le faltaban los pasos de reproducción. El comentario del 26 sí los trae, con precondiciones, ocho pasos numerados y query de verificación.

No existe ningún ENG auto creado el 25 ni el 26 para RCS-28294. El barrido del proyecto ENG lo confirma. J.R. quitó el enlace a ENG-6612 el 25.

ENG-7359, "Smart Alert not working with Quick Entry", Backlog, Matthew Kamminga, creado el 17 de agosto, describe el mecanismo del caso 48786. Texto literal del ticket: los usuarios en Quick Entry no reciben cookie cpf ni autentican al iniciar sesión, y la alerta no se crea ni se envía. Conecta con la medición de Juan de 308 cuentas con `LastLoginDate = NULL` sobre 419. Ryan Barlow reportó ahí el 18 de agosto que a Claire's le fallaron más de 140 smart alerts en un fin de semana en producción.

ENG-2819, "Smart Alert failing to run in Incident/Audit", Done, Kiran Vadday, aporta la firma de log a buscar: `LPSBO.SendHatrJob - Exception in HatrSmartAlert`.

## Decisiones y compromisos

Refijar `cola/EVAL-clasificador.json` contra el volcado de hoy. Mientras el set arrastre etiquetas del 24 de agosto, el porcentaje no mide nada.

Reclasificar RCS-28256 a nivel 2 a mano hasta que el léxico distinga la señal doble.

Escalar RCS-28294 de nuevo con el comentario corregido. Orden fijado: pegar el comentario interno, enlazar RCS-28131 de Sportman como relates to, transicionar a Under Engineering Review con Shandana, mandar el Teams, corregir a Tatiana. El ENG se auto crea con la transición.

No readjuntar el PDF del caso. Ya está en el ticket. El requisito de Aimee exige que los pasos vengan con capturas, no que se suban de nuevo.

ENG-7359 y ENG-2819 van nombrados como candidatos en la sección 6 del comentario, sin enlazar. Shandana hace el triage y decide si cierra contra ENG-7359, lo enlaza, o es aparte.

Juan quitó la declaración de uso de IA y la constancia de conversaciones externas del comentario. Son dos de los cuatro requisitos de Aimee. Ese es el motivo posible si el ticket rebota otra vez.

## Pendiente de verificar

Borrar `cola/estado.previo-run.json`. El sandbox no permitió eliminarlo. Ningún script lo lee.

Comparar `LastLoginDate` de la cuenta que creó el caso 48786 contra la que creó el 48575. Si la de 48786 está en NULL y la otra no, el mecanismo de ENG-7359 queda confirmado y RCS-28294 se cierra contra él.

El archivo de la cola quedó afirmando que Juan no hizo la transición de RCS-28294. Corregirlo.


## Rastro
2026-08-28 inbox/2026-08-28-cosecha-cola-proceso.md

## Cosecha RCS-28223 — 2026-08-28 — 2026-08-28
_chunk 1769 · 2026-08-28 · fuente: inbox/2026-08-28-cosecha-rcs-28223.md_

# Cosecha RCS-28223 — 2026-08-28
Fuente: sesion local_72d9daf2-1a75-43d6-9c90-948a319b3f83, "RCS-28223 trabajo continuación"

## Hallazgos verificados

- La prueba del defecto es el corte de escritura por columna. Siete columnas de la pantalla de Audit dejan de aceptar dato en agosto 2026: Coaching, 1st Verbal, 2nd Verbal, 1st Written, 2nd Written, First and Final y Termination. La primera columna y la ultima responden de forma intermitente. Esa asimetria es el punto que Engineering debe revisar en codigo.
- Conteo mensual de campos con dato en las columnas 2 a 8: veinte meses seguidos entre 561 y 1419. 2026-03 dio 1419 sobre 4037 totales. 2026-06 dio 1377 sobre 4122. 2026-07 dio 815 sobre 2501. 2026-08 dio 0 sobre 60.
- El volumen total tambien colapsa. Pasa de 2501 filas en julio a 60 en agosto. Julio conserva 28 dias con dato. El corte cae entre el 27 y el 31 de julio.
- Hipotesis descartada 1: `BuildStatus = CREATED` no es anomalo. 93 de las 110 pantallas del tenant se construyeron el 29 de julio en ese estado, 72 de Audit y 21 de otros modulos. El campo no distingue nada.
- Hipotesis descartada 2: los `ScreenLabelID` huerfanos no explican el defecto. Afectan a 1270 campos del tenant por igual, 676 de Audit y 594 de otros modulos. `ScreenLabel` llega hasta el ID 2309 con 407 filas y 407 IDs distintos, rango 100 a 2309. `ScreenDetail` apunta a IDs de seis digitos, 201141 a 201148 y 201186 a 201193. El join no aplica.
- El precedente de Vitamin Shoppe en RCS-28032 sobre rebuild de pantallas de Audit y entradas faltantes en Screen Labels no sostiene este caso. Los conteos lo tumban.
- `ScreenDetail` tiene 8 filas por pantalla, una por pregunta, con `ReadOnly`, `HiddenField` y `FieldProtected` en cero. No hay bloqueo por permisos, como afirmo David.
- Tablas y campos tocados: `ScreenMaster` con `ScreenMasterID`, `PageName`, `BuildStatus`. `ScreenDetail` con `ScreenLabelID`, `ReadOnly`, `HiddenField`, `FieldProtected`. `ScreenLabel` con `LPMSFieldName`, `NewFieldName`, `Editable`, `ShowVisible`, `FieldClass`.
- Pantallas implicadas: `AuditSection_V24_S4.aspx` con ScreenMasterID 83 y `AuditSection_V24_S9.aspx` con ScreenMasterID 88.
- Procedimiento que funciono: reemplazar el `CASE` dentro del `GROUP BY` por `SUM` condicional. La consulta 16 devolvia vacio con `CASE`. La consulta 20 devolvio el corte mensual completo.
- Correccion a la instruccion de David sobre el campo Comments. En las preguntas con tabla ese espacio pertenece a la tabla. Existe evidencia de otra auditoria donde lo que escribio un usuario termino dentro de la estructura de la grilla.

## Estado del ticket segun la sesion

- Comentario interno redactado y cerrado, con las dos hipotesis descartadas escritas dentro para que nadie las repita.
- Comentario cubre los cuatro requisitos de Aimee, incluida la declaracion de uso de IA.
- Respuesta al cliente redactada para Hugo. Cinco parrafos, cero peticiones, sin fecha. El proximo contacto queda anclado a la devolucion de Engineering.
- Orden de ejecucion definido: pegar el comentario interno, pegar el comentario al cliente, quitar el label `Uni_Jul_26_SSOMapping`, transicionar a Under Engineering Review con Shandana Khan.
- El ticket es Medium. La cadencia obliga a una actualizacion semanal aunque no haya movimiento.
- Compromiso creado: volver a Hugo en el ticket cuando Engineering conteste.

## Pendiente de verificar

- No se reprodujo el defecto en Test. La reproduccion propuesta corre en produccion: abrir la auditoria 4694-30612, ir a Manager Week 1, escribir una x en la columna Coaching y capturar.
- Falta la causa del corte entre el 27 y el 31 de julio. La fecha del rebuild es el unico rastro que sigue en pie del paso 12.
- Falta explicar por que la primera columna y la ultima responden de forma intermitente y las siete del medio no.


## Rastro
2026-08-28 inbox/2026-08-28-cosecha-rcs-28223.md

## Cosecha RCS-28618 — 2026-09-01 — 2026-09-01
_chunk 1778 · 2026-09-01 · fuente: inbox/2026-09-01-cosecha-rcs-28618.md_

# Cosecha RCS-28618 — 2026-09-01
Fuente: sesion local_c803ec7e-3e24-4ec6-8b9f-2628420911be, "RCS-28618 ticket analysis"

Walmart, C300_WMT. Refund Audit quick links devuelven cero. Reporter Steve Curry. Causa raiz cerrada en esta sesion.

## Causa raiz probada

El feed externo de INKIRU esta detenido. `inkiru_rva` tiene 31.442.997 filas, 4.634 tiendas y el ultimo `scanned_time` es el 30 de marzo de 2025. La tabla completa, no un subconjunto.

El reporte impone una ventana movil de 60 dias hacia atras. Hoy es 31 de agosto y el rango generado arranca el 2 de julio. La ventana persigue el presente y el dato se acabo en marzo de 2025, asi que el reporte no puede devolver nada nunca.

Los dos defectos se esconden mutuamente. Cualquier rango que pida el usuario se intersecta con los 60 dias y queda reducido. Juan pidio desde 2020 y Steve pidio desde enero. Ninguno podia mirar atras lo suficiente para descubrir donde se acaban los datos.

El reporte lleva roto desde mayo de 2025 y se reporto el 27 de agosto de 2026. Dieciseis meses.

Cuatro tiendas del reporte de Walmart cortan en la misma semana, del 20 al 26 de marzo de 2025: 3238, 4470, 3062 y 5693. La 4470 declara 36 expired y la 5693 declara cero. Cortan igual. No es una tienda, es el tenant.

## El cutover no es la causa

ENG-2829 se resolvio el 31 de julio de 2026. El feed murio en marzo de 2025. Dieciseis meses de distancia. Esto no es inestabilidad post migracion. Es un feed externo caido desde antes que la migracion arrastro tal cual. Ese es el dato que cambia la conversacion con Zack.

## SQL real del quick link

Obtenido con el boton Query de Composer. Sintaxis `set var =` con `$var`, lo que confirma Snowflake y no Greenplum para este reporte. El cutover ya esta efectivo aqui.

```
FROM ardm_Header T1
LEFT JOIN ardm_RecalledTransaction T2 ON (T1.TransactionID = T2.TransactionID AND T1.TradingDay = T2.TradingDay)
LEFT JOIN inkiru_rva T3 ON (T2.x_TCNumber = T3.tc_nbr)
WHERE (T1.TradingDay BETWEEN CAST('2026-07-02T00:00:00' AS DATE) AND CAST('2026-08-31T23:59:59' AS DATE))
AND (T3.storeno = $inkirustoreno AND T1.TradingDay BETWEEN $tradingday AND $tradingday1 AND T3.audit_result = $auditresult)
```

Datos firmes del SQL:
- El nombre fisico es `inkiru_rva`, no `ext_inkiru_rva`, y la columna es `storeno`. El rename de Kamil de 2023 sigue en pie.
- Los dos LEFT JOIN se comportan como INNER. Las condiciones sobre T3 en el WHERE descartan las filas donde T3 es NULL.
- El rango 2026-07-02 a 2026-08-31 no sale de ningun parametro visible. El indicador naranja con el 2 al lado de Query marca condiciones fijas que el usuario no puede ver ni corregir.

## Hipotesis derribadas dentro de la sesion

- H1, literal en minusculas. Falsa. `inkiru_rva` guarda `success`, `expired` y `fail` en minusculas y coincide exacto con el Searchable. Hay 9,8 millones de filas expired, asi que el dato de refund audits si existe en Appriss.
- Join roto por `T1.TradingDay = T2.TradingDay` con NULL. No aplica a la causa. El join a `inkiru_rva` es `ON (T2.x_TCNumber = T3.tc_nbr)` y no toca `T3.TradingDay`. Que esa columna este 100% NULL en las 513 filas medidas es un defecto latente aparte.
- H3, nombre de columna de tienda. Descartada por el SQL real.
- H6, cuenta de Steve Curry. Descartada. Juan reprodujo el cero con su propio usuario en USPROD, lo que sube el ticket de reporte de cliente a defecto reproducible.

## Defectos separados que hay que reportar aparte

- La ventana movil de 60 dias. Necesita que alguien lea el XML en `[C300_WMT_033WMT_Platform].[secure].[Repo]` para decidir el ruteo. Si la ventana esta escrita en el XML del Searchable va a Delivery. Si la inyecta el generador va a Engineering. No lo escales a ciegas y no bloquea nada.
- `MIN(scanned_time)` devuelve año 0005. Fecha corrupta, misma familia que ENG-7205 con `AuditCompletionDate = 1900-01-01`, que tambien pega en Walmart. Cualquier consulta que ordene por esa columna va a mentir.
- `TradingDay` 100% NULL en `ardm_RecalledTransaction` para las filas medidas.

## Ruteo verificado contra precedente

El estado `Under Support Data Team Review` no existe en RCS. Si aparece en un runbook, esta mal. Lo que se usa para "dato que dejo de llegar":

```
Under Delivery Review · assignee Zackary Graas · label Support_Data_Team
Team Ownership "Support (Delivery dep.)" · Sprint "RCS Support Team"
```

Precedente cerrado casi identico: RCS-27485, TJX EU, Adyen dejo de entregar los archivos diarios desde el 18 de junio. Precedente vivo del mismo tenant: RCS-28602, C300_WMT, caida del conteo de archivos, ya en Under Delivery Review.

## Pasos operativos acordados

1. Pega la nota interna con visibilidad interna, no Service Desk Team.
2. Pega la respuesta a Steve con visibilidad cliente. Va segunda porque el quinto requisito de Aimee es avisarle al cliente que el ticket se mueve.
3. Transiciona a Under Delivery Review.
4. Assignee Zackary Graas.
5. Campos: label `Support_Data_Team`, Team Ownership `Support (Delivery dep.)`, Sprint `RCS Support Team`.
6. Postea en Teams, canal Data Issues. La transicion sola no mueve a nadie. Leccion de RTS-206268.
7. Enlaza RCS-28602 como relates to.

No abras tickets para los otros seis quick links. Todos leen la misma tabla y el alcance queda declarado en el comentario.

Antes del paso 1, habla con Zack. Encontro algo en la llamada del 28 con Steve que no esta escrito en ningun ticket. Si su hallazgo cubre esto, cambia el comentario. Si no, borra el punto 4 de "Still open" antes de pegar.

RCS-28620 es de Edwin y esta parado esperando lo mismo, que alguien hable con Zack. Una llamada resuelve los dos. Avisale a Edwin.

RCS-28602 ya esta donde debe. Solo enlazarlo.

RCS-9452, RCS-17323 y RCS-27485 estan cerrados y ya van citados dentro del comentario.

## Deuda que crea el texto al cliente

Volver al ticket cuando el equipo de datos confirme que hace falta para restaurar el feed. Sin fecha, anclado a esa condicion.

## Referencias

RCS-28618, RCS-28602, RCS-28620, RCS-27485, RCS-28578, RCS-28380, RCS-9452, RCS-17323, ENG-2829, ENG-7205, RTS-206268.


## Rastro
2026-09-01 inbox/2026-09-01-cosecha-rcs-28618.md

## Cosecha 4 sep 2026 — Proceso Pendo / Ideas Portal para feature requests — 2026-09-04
_chunk 1795 · 2026-09-04 · fuente: inbox/2026-09-04-cosecha-pendo-ideas-portal-proceso.md_

# Cosecha 4 sep 2026 — Proceso Pendo / Ideas Portal para feature requests

Sesión fuente: "Pendo definition inquiry" (local_ae0af428), transcripción del 3 sep 2026.

## Hallazgo verificado, proceso

Un ticket de feature request no se desarrolla dentro de RCS. Se mueve a Pendo/Ideas Portal y el RCS se cierra. Es support quien registra el feature request en Pendo/Ideas Portal, el cliente no llena ningún formulario.

Existe un canned response fijo llamado "Ideas Portal Ticket" o "Feature Request Response". Le avisa al cliente que su ticket se movió del RCS al Ideas Portal, que sigue en evaluación aunque el RCS aparezca cerrado, y que recibirá notificaciones si avanza o se convierte en Idea votable.

No existe una transición de Jira separada para Pendo. El cierre usa la transición normal Resolve a Completado. Al poner Complete, dos dropdowns de Resolution Details son obligatorios. Uno de los valores fijos de ese dropdown es exactamente "Feature Request - Pendo Referred". Si algún dropdown queda en "none", el sistema regresa el ticket solo a "additional info needed" y le manda email al assignee.

Proceso completo, en orden: enviar el canned response de Ideas Portal Ticket al cliente, pasar el ticket a Complete, llenar los dos dropdowns con "Feature Request - Pendo Referred" en el que corresponde, y escribir en las notas de resolución qué se registró y dónde quedó. El ticket pasa a Closed después de que el cliente verifica.

## Caso aplicado

RCS-28646, Stephanie confirmó avanzar con dos de tres ítems solicitados, auto populate en No y help text de campos HTML box. Ambos gaps de producto, van a Pendo/Ideas Portal por Luis Hernandez.

No existe un canned response distinto con la palabra "roadmap" en la base de conocimiento. El único es "Ideas Portal Ticket / Feature Request Response".

Fuentes citadas en la sesión: [RCS-28646](https://trebuco.atlassian.net/browse/RCS-28646), [RICED: Scoring Feedback in the Ideas Portal](https://trebuco.atlassian.net/wiki/spaces/PTO/pages/477860069383/RICED+Scoring+Feedback+in+the+Ideas+Portal), [Pendo Requests](https://trebuco.atlassian.net/wiki/spaces/PTO/pages/477476093954/Pendo+Requests).


## Rastro
2026-09-04 inbox/2026-09-04-cosecha-pendo-ideas-portal-proceso.md

## Cosecha 4 sep 2026 — Secure ICA, estado de los cuatro tickets y PRs — 2026-09-04
_chunk 1797 · 2026-09-04 · fuente: inbox/2026-09-04-cosecha-secure-ica-prs-estado.md_

# Cosecha 4 sep 2026 — Secure ICA, estado de los cuatro tickets y PRs

Sesión fuente: "ICA receipt viewer issues analysis" (local_04925369), transcripción del 3 sep 2026.

## Hallazgo verificado

PRs 55913 y 56235, que cubren RCS-28254 y el fix original de RCS-28253, están mergeados en producción desde el 29 de agosto.

La regresión que ICA reportó el 2 de septiembre se está atendiendo en un PR nuevo, 57002, que también cubre el problema de descuento de RCS-28717. Ese PR seguía en draft sin reviewers asignados al 3 de septiembre, no había llegado a staging ni a producción.

RCS-28716, causa raíz confirmada: falta un guard en el banner de la sección Audit. Sin PR abierto todavía.

RCS-28719 sigue sin causa raíz identificada. Cita textual de Nikita en su resumen de investigación: "We need an actual example of a missing row/transaction from the customer to investigate further, nothing in the data we can access points to a mechanism."

## Carga verificada en Jira al 3 sep, usada para decidir quién cubre

Diego Buelvas: 7 abiertos, 0 en Work in progress, la mayoría esperando cliente o release.
Edwin Garzon: 16 abiertos, 5 en Work in progress, 2 High.
Sebastian Rueda: 15 abiertos, 6 en Work in progress, uno escalado.

## Decisión

Con Nikita fuera el 4 de septiembre, Diego Buelvas queda cubriendo PR 57002 y los tickets RCS-28716, RCS-28717 y RCS-28719 mientras ella no está. Aviso enviado a Diego en español pidiendo que reporte si el PR avanza o si ICA manda la transacción faltante para RCS-28719.


## Rastro
2026-09-04 inbox/2026-09-04-cosecha-secure-ica-prs-estado.md

## RCS-27407. Confirmada. ManageSmartAlerts.aspx no regenera las columnas Filters y FiltersSQL de dbo.SmartAlertConfig cuand — 2026-09-04
_chunk 1712 · 2026-09-04 · fuente: inbox/2026-09-04-rcs-27407-informe.md;2026-09-04-rcs-27407-instructivo.md_

Ticket RCS-27407. Trabajado el 2026-09-04. 2 notas en inbox.

## Causa
Confirmada. ManageSmartAlerts.aspx no regenera las columnas Filters y FiltersSQL de
dbo.SmartAlertConfig cuando se modifican y guardan las selecciones de tipo de auditoría en una
alerta ya existente. Afecta las ocho alertas SSVR, SmartAlertConfigID 33 a 40. Reproducida dos
veces por Tyrone Whitney, 6/17 y 7/2, mismo resultado ambas veces.

## Evidencia
El estado en Jira hoy es Under Support Review. El assignee es Luis Hernandez. La prioridad es
Medium. El reporter es Annie Brown, cliente de PPG. No existe ficha previa de RCS-27407 en
`tickets/`, ni entrada en `bitacora/`, ni mención en `brain/markdown/` de SmartAlertConfig,
FiltersSQL o ManageSmartAlerts.aspx. Este ticket no tiene precedente propio en el cerebro. Todo lo
que sigue viene del hilo vivo de Jira.

Tyrone Whitney tomó el ticket el 2026-06-15 y en el call del 6/17 hizo un primer intento de
corrección directamente desde la UI de Manage Smart Alerts. Agregó los dos tipos de auditoría
nuevos al filtro existente y dio el ticket por resuelto en ese momento.

Annie Brown reportó el 2026-06-22 que las alertas seguían sin llegar. Store 9718 completó una
auditoría el 6/19 y no generó alerta.

Tyrone reabrió la investigación el 6/30 y el 7/2 confirmó la causa raíz con reproducción propia,
documentada en el ticket como nota interna:

"The Manage Smart Alerts page (ManageSmartAlerts.aspx) does not regenerate FiltersSQL when audit
type selections are modified and saved. The UI visually accepts the changes and displays them as
saved, but the underlying dbo.SmartAlertConfig.Filters a

## Impacto
El bug de ManageSmartAlerts.aspx no es exclusivo de PPG. Cualquier cliente que edite tipos de
auditoría en una alerta ya configurada sufre el mismo fallo silencioso, la UI confirma el cambio y
la base no lo aplica. Ryan Barlow señaló el 7/2 que no había visto el problema antes en otros
clientes. Tyrone lo reprodujo dos veces de forma independiente el mismo día que Ryan escribió eso.
Para PPG el impacto acumulado a hoy es de casi cuatro meses sin alertas de auditoría SSVR, desde el
2026-05-06. Afecta el seguimiento de action plans y de auditorías completadas para los tipos de
auditoría nuevos.

## Que sigue
Luis Hernandez, assignee actual de RCS-27407 y de ENG-8117, ejecuta el fix de código bajo ENG-8117
siguiendo el flujo estándar de code change. Confirma primero el repositorio y pipeline correctos
para netTrack legado, porque la guía documentada no cubre explícitamente esa plataforma. El fix
corrige la comparación de tipo de auditoría para que use AuditConfigID en vez de igualdad de texto
contra el nombre. Una vez desplegado a producción, alguien del equipo re-guarda la configuración de
las ocho alertas SSVR desde la UI corregida para que el FiltersSQL se regenere. Support comunica a
Annie Brown solo después de confirmar con las queries de solo lectura que el filtro cambió y que
hubo al menos un disparo real posterior al re-guardado. El detalle ejecutable está en el instructivo
adjunto.

## Precedentes
No existe precedente específico de SmartAlertConfig, FiltersSQL o ManageSmartAlerts.aspx en
`tickets/`, `investigaciones/` ni `brain/markdown/`. El precedente que sí aplica es de proceso, no
de síntoma: `brain/markdown/24-appriss-dev-workflow-code-change.md`, guía Making a Code Change,
confirma que Support puede quedarse con la ejecución del código de un ticket que Engineering
triagea y decide no tomar directamente. La regla de comunicación al cliente de
`brain/markdown/19-rcs-procesos-playbook.md`, caso RCS-28161, sigue aplicando en espíritu aunque el
orden del flujo esté invertido en este ticket. La regla de solo lectura en producción de
`brain/memoria/reference_acceso_sql_tenants.md` descarta la opción de DB fix directo que Tyrone dejó
planteada como alternativa.

## Rastro
2026-09-04 inbox/2026-09-04-rcs-27407-informe.md
2026-09-04 inbox/2026-09-04-rcs-27407-instructivo.md

## RCS-27991. RCS-27991 · Engage Analytics Not Populating Sections · avance del 26 ago 2026 — 2026-08-26
_chunk 1715 · 2026-08-26 · fuente: inbox/2026-08-26-rcs-27991-avance-y-escalacion.md_

Ticket RCS-27991. Trabajado el 2026-08-26. 1 notas en inbox.

## Evidencia
Captura en `adjuntos/RCS-27991/2026-08-26-harbor-freight-engage-analytics-tiles-error.png`. Juan
confirmo que es del momento del reporte, 27 jul 2026, y que el adjunto `Engage Analytics Issue.docx`
del ticket es la misma imagen dentro de un documento. **No hay que descargar el docx, no aporta
nada nuevo.**

Portal Harbor Freight, pestana Engage Analytics:

| Elemento | Resultado |
|---|---|
| Calls to Appriss | 179 · carga |
| Calls Per Action | 5.31% · carga |
| Activity Reports | 126 · carga |
| No ID (NR) | control View presente |
| Manual ID Entry | control View presente |
| Boris Return Amount | $0 · carga |
| Panel inferior izquierdo | triangulo de advertencia, sin datos |
| Panel inferior derecho | triangulo de advertencia, sin datos |

**Los seis tiles agregados cargan. Solo fallan los dos paneles de detalle SKU.** Descarta
autenticacion, permisos, sesion y el dashboard como conjunto. El fallo vive en la capa de datos de
SKU.

Que la captura sea del 27 jul resuelve la contradiccion aparente con lo que dijo Paul el 14 de
agosto. Harbor Freight todavia tenia Engage Analytics ese dia y migro a Insights despues.

## Que sigue
1. Pedirle a Shandana Khan el numero de bug de Azure DevOps del 28068
2. RCS-28004 lleva 29 dias sin un comentario con Jon Morgan. Va aparte
3. Cuando ingenieria confirme la causa raiz, escribir la investigacion en `investigaciones/`. El
   cerebro no tiene ninguna sobre Engage Analytics ni sobre la migracion a Engage Insights

## Rastro
2026-08-26 inbox/2026-08-26-rcs-27991-avance-y-escalacion.md

## RCS-28638. El 28 de agosto propuse el payments project como causa candidata, apoyado en la cita del cliente en RCS-28518 — 2026-08-31
_chunk 1741 · 2026-08-31 · fuente: inbox/2026-08-28-rcs-28638-myer-header-ext.md;2026-08-31-rcs-28638-actualizacion-snowtime.md_

Ticket RCS-28638. Trabajado el 2026-08-28 a 2026-08-31. 2 notas en inbox.

## Causa
El 28 de agosto propuse el payments project como causa candidata, apoyado en la cita del cliente en
RCS-28518. Esa hipotesis es incorrecta. La causa raiz de la familia completa de defectos de mapeo
de Myer esta establecida por Matthew Everett con evidencia de produccion y es otra.

Myer paso de Greenplum legacy a SnowTime. Go live ENG-6418, cerrado el 17 ago 2026. Validacion del
cutover ENG-3795. La reimplementacion de pyardm en SnowTime dejo logica sin portar, y cada ticket
de Myer es una omision distinta de la misma migracion.

## Evidencia
Jira vivo, getJiraIssue RCS-28638, 28 ago 2026. Estado Under Support Review, prioridad High,
assignee Juan Martinez. Dos comentarios: acuse de Akshaya Purappemane y toma de propiedad de Juan
el 27 ago 21:18. Ningun comentario tecnico todavia.

Tres adjuntos del reporter, guardados en `adjuntos/RCS-28638/`:

image-20260828-004653.png. Fila de resultados del search. Transaction ID 2608273342446971618,
Store No 219, Cashier No 1077380, End Trans Date Time 27/08/2026 12:11:49 PM, Transaction Amount
-500.00, Register 618, Transaction 44, Transaction Type Return/Exchange With Proof Of Purchase.
Las columnas Financial Statement Date, Order Number y Proof Type salen vacias.

image-20260828-004816.png. Retail Transaction Details de la misma transaccion. Store ID 219,
Transaction ID RT2196182708260044, Total Amount -500.00, Team Member Name Aravinda (1077380),
Training Mode N, Authorized by Team Member 1148897, Register ID 219618, Transaction Status
Finished, begin 27/08/2026 12:07:36 GMT+10, end 12:11:49 GMT+10. Card Number 627804******0812.
Bloque RETURN/EXCHANGE WITH PROOF OF PURCHASE con dos lineas resaltadas por el cliente:
`Proof Type : CUSTOMER ORDER RETURN` y `Customer Order Number :

## Impacto
Los tres tickets que Matthew paso a Under Customer Review el 31 ago usan lenguaje de completed and
verified. La nota tecnica de RCS-28559 dice lo contrario:

> THE REMEDY IS UNPROVEN. It should work ... But there is no observed case of a rebuild repairing
> this column. A single-day lab rebuild would settle it. Please do not present the fix as confirmed
> until that runs.

No consta en ningun comentario que ese lab rebuild se haya ejecutado. Si Christine reabre, la
posicion queda expuesta. Juan no debe usar lenguaje de verificado sin la medicion propia.

## Precedentes
RCS-26403, Completed. Request to map Return With Proof of Purchase Type: Receipt. Es el ticket que
mapeo Proof Type originalmente. Sirve para saber donde se configuro y quien lo hizo:
Chenuka Ratwatte.

RCS-26010, Customer Resolved. Mapeo de informacion de cliente en Return With Proof of Purchase,
hacia las Customer Extension Tables. Mismo tipo de transaccion, misma familia de tablas de
extension.

RCS-25061, Resolved. Delivery Fee Details Missing en Point of Sale. Antecedente exacto de
RCS-28612. Ya paso una vez y volvio.

RCS-27262, Resolved. POS Hash del 29 y 30 mayo 2026. Antecedente exacto de RCS-28559. Se resolvio
recargando los archivos. Ya volvio.

RCS-22051, Resolved. Velocity Tender Account Number no mapeado, el numero de referencia ocupaba el
lugar del numero real. Mismo patron que RCS-28518.

RCS-27644 H&M, del cerebro, `brain/markdown/16-rcs-soluciones.md:177-188`. Leccion procedimental:

> pedir/conseguir siempre el SQL del search (correr el report con parametros dummy para ver el
> query), fue lo que destrabo la causa raiz

Y el dato de donde viven los overrides de mapeo por cliente: `secure_Resource.json`.

## Rastro
2026-08-28 inbox/2026-08-28-rcs-28638-myer-header-ext.md
2026-08-31 inbox/2026-08-31-rcs-28638-actualizacion-snowtime.md

## RCS-28701. RCS-28701 es un ticket de configuración de IGEntryPage e IGIncidentReport para la organización JSD "DHL Global — 2026-09-02
_chunk 1747 · 2026-09-02 · fuente: inbox/2026-09-02-rcs-28701-informe.md;2026-09-02-rcs-28701-instructivo.md_

Ticket RCS-28701. Trabajado el 2026-09-02. 2 notas en inbox.

## Que pasa
RCS-28701 es un ticket de configuración de IGEntryPage e IGIncidentReport para la organización JSD "DHL Global Mail" (id 72), abierto el 1 sep 2026 por Stephanie Kudla y asignado a Sebastian Garces. Afecta la configuración del caso Illegal Goods de ese cliente, sin relación con identidad de tenant. Ningún repositorio interno consultado, ni Cerebro ni Confluence ni Jira, confirma el número de cliente ni el slug de tenant de DHL Global Mail en Control Panel.

## Causa
El slug de tenant de DHL Global Mail es probablemente "dhl", tomado literalmente del encabezado "DHL (`dhl`)" en el runbook de Incident vs Audit. Esa cita no trae confirmación por URL, a diferencia de otros clientes en el mismo documento que sí la traen. El número de cliente numérico, equivalente al 15778 de Advance Auto Parts o al 110794 de Ralph Lauren, no aparece en ningún documento revisado. Marca esto como hipótesis, no como hecho verificado.

## Evidencia
Se leyó el ticket vivo con getJiraIssue, RCS-28701, estado Work in progress, asignado a Sebastian Garces desde el 1 sep 18:15. Se buscó en tickets, brain/markdown, investigaciones, bitacora y adjuntos de Cerebro por "DHL" vía subagente, sin resultado de número de cliente. Se corrió Rovo search y CQL contra Confluence y JQL contra Jira por "DHL Global Mail" y variantes con "client", "tenant", "control panel".

## Impacto
DHL Global Mail se maneja en RCS-28701 como caso Incident, LPMS, no Secure Audit. Los tres perfiles citados documentan el cliente del lado de Secure Audit, CAMS Mobile. Confirma en Control Panel que el tenant al que buscas impersonar para IGEntryPage e IGIncidentReport es el mismo DHL que aparece en esos perfiles, y no un tenant distinto bajo el mismo nombre. Otros clientes grandes del corpus, Walmart con client IDs 300, 301, 303, 308, 309, y Finish Line con client IDs 375 y 376, muestran que un mismo nombre comercial puede cubrir más de un tenant. No hay evidencia de que esto aplique a DHL Global Mail, pero tampoco hay evidencia de que no aplique.

## Que sigue
El dato no está resuelto en ninguna fuente interna consultada. La decisión es confirmarlo directo en Control Panel, y si el nombre no aparece igual a "DHL Global Mail", cruzarlo con el tracker Incident Migration 2026.xlsx que ya tienes localmente.

## Precedentes
Tres perfiles internos de DHL coinciden en el mismo vacío de dato, lo que sugiere que nadie lo ha confirmado todavía, no que el dato no exista:

Secure Audit (CAMS): Internal Setup & Configuration Runbook, https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478007787572
Incident (LPMS) vs Audit (CAMS): Setup Differences Side-by-Side, https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478022959110
Customer Escalation Handoffs -- Secure Audit & Legacy, https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478022139957
Runbook: DHL, https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478007066660

## Rastro
2026-09-02 inbox/2026-09-02-rcs-28701-informe.md
2026-09-02 inbox/2026-09-02-rcs-28701-instructivo.md

## RCS-28709. RCS-28709 sigue en Work in progress con Viraj Kansara como assignee. El rebuild de pantalla aplicado el 3 de s — 2026-09-04
_chunk 1748 · 2026-09-04 · fuente: inbox/2026-09-04-rcs-28709-informe.md;2026-09-04-rcs-28709-instructivo.md_

Ticket RCS-28709. Trabajado el 2026-09-04. 2 notas en inbox.

## Que pasa
RCS-28709 sigue en Work in progress con Viraj Kansara como assignee. El rebuild de pantalla aplicado el 3 de septiembre redujo el problema. No lo eliminó. Angie Martinez reportó hoy dos casos nuevos con el mismo síntoma en las tiendas 139 y 208, y el ticket gemelo RCS-28742 quedó cerrado sin que nadie creara el ENG que Shandana Khan había condicionado a aceptar el síntoma como bug real.

## Causa
Hipótesis, no causa raíz confirmada. Nadie identificó por qué el Save deja el caso vacío en vez de fallar o de guardar completo. El rebuild de pantalla bajó la frecuencia del síntoma el 3 de septiembre y no lo eliminó, la recurrencia de hoy en dos tiendas distintas lo confirma. Ingeniería no tiene ningún ticket abierto investigando la causa. Todo lo que existe hasta ahora es un workaround aplicado dos veces sobre el mismo síntoma.

## Evidencia
Estado real en Jira, `getJiraIssue` al momento de escribir esto. RCS-28709 está en Work in progress, prioridad High, assignee Viraj Kansara, reporter Angie Martinez, label `Uni_Jul_26_Unbucketed`. La ficha del cerebro decía Under Customer Review. Ese dato quedó obsoleto, el estado real es otro.

RCS-28742, el ticket técnico gemelo que Viraj abrió el 3 de septiembre para documentar la reproducción, está Closed. Se cerró el 4 de septiembre a las 02:10 hora Colombia, sin ningún ENG vinculado. El único issuelink que tiene es de vuelta a RCS-28709.

Shandana Khan escribió en RCS-28742 el 3 de septiembre a las 08:23, convirtiendo el ticket de vuelta a RCS: "If we accept this as a legitimate bug, I'll raise and schedule a linked ENG as per our current process." Esa condición nunca se cerró. Matthew Kamminga sugirió en cambio, el mismo día a las 08:26, probar el rebuild en la aplicación. Viraj corrió Build All Screens esa mañana. Angie confirmó a las 12:04 que el blank screen le seguía pasando de forma intermitente después de esa primera corrida. Juan corrió Build All Screens una segunda vez sobre el mismo tenant a las 20:57, retesteó el caso 2026-083-STORE SHOPLIFT-220 siete veces y las s

## Impacto
El síntoma ya no es un caso aislado. Pasó de una tienda, la 356 con el caso 220, a tres tiendas distintas en cuatro días, 356, 208 y 139. Cada tienda es un usuario propio del sistema, según lo que Angie misma aclaró el 2 de septiembre. El daño no es solo una pantalla que no responde. El caso queda en el sistema con datos perdidos, cero dólares y sin investigador asignado, lo que significa que un caso de shoplifting o de incidente real puede quedar sin trabajar y sin que nadie lo note hasta que alguien lo busque a mano. Nadie verificó todavía si la lista de Incident Types de Stater Bros sigue completa después de dos corridas de Build All Screens. Si ese conteo bajó, hay una segunda causa de pérdida de datos corriendo en paralelo sin diagnosticar.

## Que sigue
[2026-09-04] La decisión que le toca a Juan hoy, antes de que Viraj se desconecte por el fin de semana, es de cobertura. El ticket sigue High y Viraj sigue de assignee, y el síntoma acaba de repetirse en dos tiendas nuevas un viernes en la tarde. Juan decide si asume el monitoreo del ticket hasta el lunes o si lo deja en la cola de guardia normal.

La segunda decisión es si forzar hoy mismo la aceptación de Shandana Khan como bug real, dado que la condición que ella puso el 3 de septiembre ya se cumplió con la recurrencia de hoy, o si espera al lunes con Viraj de vuelta. El comentario interno y el mensaje de Teams para esa conversación están listos en el instructivo.

La tercera es si pedirle a alguien que confirme la lista de Incident Types de Stater Bros antes de que se ejecute un tercer Build All Screens, dado el precedente de Santikos.
[2026-09-04] Registra lo trabajado hoy en la bitacora del ticket y deja que Claude recalcule la cola en la proxima sesion.

## Precedentes
RCS-28742, ticket gemelo, cerrado sin ENG el 4 de septiembre. RCS-28022 Santikos, precedente del riesgo de Build All Screens sobre la lista de Incident Types. `brain/memoria/reference_screen_designer_rebuild.md`, el procedimiento y su advertencia. `brain/memoria/project_teams_unificacion_2026_08_12.md`, la causa candidata de rendimiento sin confirmar.

## Rastro
2026-09-04 inbox/2026-09-04-rcs-28709-informe.md
2026-09-04 inbox/2026-09-04-rcs-28709-instructivo.md

## RCS-28753. Nike pide la logica exacta o el snippet de codigo con el que Appriss calcula el campo Manual Discount Amount e — 2026-09-03
_chunk 1749 · 2026-09-03 · fuente: inbox/2026-09-03-rcs-28753-informe.md;2026-09-03-rcs-28753-instructivo.md_

Ticket RCS-28753. Trabajado el 2026-09-03. 2 notas en inbox.

## Que pasa
Nike pide la logica exacta o el snippet de codigo con el que Appriss calcula el campo Manual Discount Amount en Secure 5. Nadie en la base tiene ese nombre de campo documentado literal, pero hay dos piezas fuertes que acotan la hipotesis, un precedente cerrado con Nike donde Ingenieria explico una familia de campos casi identica, y la funcion PostgreSQL que calcula los fast facts de descuento manual desde donde probablemente sale el dato. La decision sigue siendo confirmar con Ingenieria, ahora con nombre propio y evidencia concreta para acelerar la respuesta.

## Causa
Hipotesis, marcada como tal porque nadie confirmo el mapeo exacto del nombre de campo. No hay causa raiz porque esto no es un bug, es una solicitud de documentacion de logica de calculo.

La hipotesis con mas respaldo es que Manual Discount Amount en Secure 5 se surte del mismo fast fact que Confluence documenta como SalePriceModifyAmount, SalePriceOverrideAmount o ReturnPriceOverrideAmount, calculado por la funcion pre_insert_generate_fast_facts sobre ardm_item con la condicion manual_price_flag = 1, o es un alias de negocio del campo que Peyman Motlagh describio en RCS-21540 como Total Discount Modify Amount, el total de overrides manuales del cajero. Las dos piezas describen la misma idea de negocio, un monto que se genera solo cuando el precio se modifico a mano en el POS, y las dos salen de la ingesta de Appriss, no del TLOG crudo, lo que coincide con lo que Damir describe en la descripcion del ticket.

Hipotesis secundaria, mas debil, que la definicion vive en un Searchable XML del Search Service de Secure 5 respaldado por la funcion GetTransactionJson.sql del override client specific 67 de Nike en Snowflake, la misma familia de funciones que causo el bug de RCS-28420. No se 

## Evidencia
Confirmado directo en Jira con getJiraIssue. Estado Under Support Review, prioridad High, asignado Juan Martinez, reporta damir.demirovic@nike.com, sin adjuntos. Dos comentarios en el ticket, la respuesta automatica de triage de Akshaya Purappemane el 2026-09-03 12:52 y el de Juan Martinez el mismo dia 18:11 tomando ownership: "I have taken ownership of this ticket and will be investigating it for you. Please allow some time for me to research the issue and I will get back with you just as soon as I have any information." Ningun comentario de escalacion a Ingenieria todavia.

La ficha local en tickets/RCS-28753.md solo tenia la entrada de la corrida de cola de esta tarde, marca el ticket como Triage sin asignar de fondo, ese dato es mas viejo que el estado real y no debe usarse para reportar estado.

No existe bitacora/RCS-28753.md ni adjuntos/RCS-28753/, nadie ha investigado este ticket especifico antes de hoy en Cerebro.

## Impacto
Nike esta bloqueada en su propio trabajo de agregacion y reporte mientras no tenga la formula. Damir ya pidio explicitamente que este ticket pase por encima de los otros cuatro abiertos de Nike. El riesgo tecnico es responder con una de las dos hipotesis como si fuera la formula confirmada. Eso repite el patron de RCS-28161 que la skill exige evitar, comprometer una respuesta tecnica sin la fuente exacta.

## Que sigue
La decision es escalar a Peyman Motlagh de Ingenieria, no a un canal generico, porque ya resolvio la misma familia de preguntas para Nike en RCS-21540 y conoce el mapeo de campos de descuento contra columnas fuente. Se le entrega la hipotesis con las dos piezas de evidencia, la pagina de Fast Facts y la cita de su propia respuesta en RCS-21540, para que confirme en minutos si Manual Discount Amount es el mismo campo que el describio como Total Discount Modify Amount o uno nuevo. Si dice que es uno nuevo, la segunda pregunta para el es si vive en el mismo Searchable de Secure 5 o si hay que mirar GetTransactionJson.sql del override 67.

## Precedentes
RCS-21540, Nike, cerrado 2025-07-24, Peyman Motlagh de Ingenieria. Precedente directo, mismo cliente, mismo tipo de pregunta sobre a que corresponden los campos de descuento y de donde salen. Ingenieria entrego una tabla completa de definiciones con las columnas fuente. Ver cita completa en la seccion de evidencia.

Confluence, pagina Fast Facts - ARDM Header Pre Insert Calculated Columns, espacio Product Delivery, documenta la funcion PostgreSQL real que calcula los montos de modificacion y override manual de precio durante la ingesta a ARDM. Es la unica fuente en toda la busqueda, Jira, Confluence y Cerebro, con SQL real de un campo de descuento manual.

RCS-28049, Smyths, confirma que Manual Discount es un Searchable del Search Service de Secure 5 sujeto a fan out por join a nivel de item, sintoma de duplicacion de filas, no de formula. brain/markdown/19-rcs-procesos-playbook.md.

RCS-28420, Nike, causa raiz confirmada por Vlad Bogus, item_discount_ext ausente en GetTransactionJson.sql del override 67. Accepted into Development, prioridad Medium, estimado para el release de fin de septiembre segun Shandana Khan.

RCS-28508, Nike, causa raiz confirmada por Edwin Garzon el 2026-09

## Rastro
2026-09-03 inbox/2026-09-03-rcs-28753-informe.md
2026-09-03 inbox/2026-09-03-rcs-28753-instructivo.md

## RCS-28779. Usuarios de Home Depot Canada no podían entrar a EBR Secure vía SSO SAML2 la mañana del 4 de septiembre. La ca — 2026-09-04
_chunk 1751 · 2026-09-04 · fuente: inbox/2026-09-04-rcs-28779-informe.md;2026-09-04-rcs-28779-instructivo.md_

Ticket RCS-28779. Trabajado el 2026-09-04. 2 notas en inbox.

## Que pasa
Usuarios de Home Depot Canada no podían entrar a EBR Secure vía SSO SAML2 la mañana del 4 de septiembre. La causa fue un 429 Throttled de Azure Key Vault, `VaultOperationLimitReached`, en la aplicación `web-prd-wus2-arp-legacysecure`. Infraestructura corrigió con un rolling restart de las 10 instancias, y el ticket sigue en Work in progress sin que ese hallazgo quede escrito en Jira ni en Cerebro.

## Causa
Confirmada. El servicio detrás de `/secure/sso/saml2` para Home Depot depende de Azure Key Vault vía private endpoint para completar el handshake SAML. Key Vault empezó a devolver 429 Throttled, `VaultOperationLimitReached`, y esa dependencia caída tumbó el sign in para los usuarios que autenticaban contra esa instancia. Infraestructura, Jon Morgan y Jose Parocua, corrigió con un rolling restart de las 10 instancias de `web-prd-wus2-arp-legacysecure`. No es un problema de configuración SAML ni de mapeo de claims. No es el patrón de Cloudflare contra Zscaler Canada que cerró RCS-28059 y RCS-28556, ese bloquea en el borde antes de llegar a la aplicación y esto es una dependencia interna agotada dentro de la aplicación.

## Evidencia
Ticket vivo vía `getJiraIssue`. Campos leídos: summary, description, status, priority, assignee, reporter, created, updated, labels, comment, attachment. Total de comentarios: 5, todos leídos.

Cronología de comentarios:

07:18:02 EDT, Shireesh Ramdas, auto-triage de recepción del ticket.
07:22:38 EDT, Shireesh Ramdas, enlace a un hilo de Teams, canal Retail Ops, Secure 5 Issues.
07:26:01 EDT, Vedant Shirude toma ownership: "I have taken ownership of this ticket and will be investigating it for you."
07:43:09 EDT, Ericka Smith: "EBR Secure is now working. What was the root cause? Thank you :)"

El campo `updated` del ticket marca 08:46:26 EDT, una hora después de la pregunta de Ericka. Ningún comentario nuevo acompaña ese cambio. Vedant movió algún campo del ticket, no dejó texto.

No existe ficha previa en `tickets/RCS-28779.md`. No existe entrada en `bitacora/`. Este es el primer contacto de Cerebro con este ticket.

## Impacto
El límite de operaciones de Key Vault es una cuota compartida entre todo lo que cuelga de esa instancia de Key Vault, no solo Home Depot. Un pico de tráfico o de otro consumidor de la misma vault puede repetir el mismo 429 en cualquier tenant que dependa de `web-prd-wus2-arp-legacysecure`. El restart manual es un parche, no elimina la causa de fondo, que es por qué se alcanzó el límite. Home Depot levantó el mismo incidente por su cuenta, `ITHD-9187`, señal de que el impacto no fue menor.

## Que sigue
Cerrar con la cliente confirmando que el acceso está restablecido, sin entrar en los detalles de Key Vault, el restart ni los nombres de los ingenieros. Guardar este hallazgo en Cerebro, carpeta RCS Soluciones, para que quede buscable la próxima vez que aparezca `VaultOperationLimitReached` o un Server Error en `/secure/sso/saml2`.

## Precedentes
`brain/memoria/reference_sso_incident_diagnostico.md`, discriminador SSO Response Log, no aplica a este caso porque el fallo nunca llegó al mapeo de claims.
`tickets/RCS-28240.md`, United Supermarkets, SSO de test caído en `saml2`, síntoma distinto.
`inbox/2026-08-26-rcs-28556-COMENTARIO-INTERNO.md` y `tickets/ENG-7176.md`, patrón Cloudflare contra Zscaler Canada, descartado para este ticket por mecanismo.
Sin precedente previo en Cerebro para throttling de Key Vault contra `legacysecure`. Este es el primero. Vale la pena guardarlo en la base para el próximo ticket que muestre el mismo `VaultOperationLimitReached`.

## Rastro
2026-09-04 inbox/2026-09-04-rcs-28779-informe.md
2026-09-04 inbox/2026-09-04-rcs-28779-instructivo.md

## Cosecha RCS-27991 — 2026-08-28 — 2026-08-28
_chunk 1766 · 2026-08-28 · fuente: inbox/2026-08-28-cosecha-rcs-27991.md_

# Cosecha RCS-27991 — 2026-08-28
Fuente: sesion local_3f09bb45-325d-4cb2-a71c-040296fd2840, "Cerebro Ticket RCS-27991"

## Hallazgos verificados

- Regla de routing corregida. El destino de una escalacion lo decide donde vive el componente, no el nombre del producto. Engage Analytics corre sobre la plataforma Secure, asi que va a Secure Engineering.
- Prueba documental 1: RCS-23643, el precedente identico, abre con la nota "Note: Even though this is related to Engage, the ticket is for the Secure team." El bug 66220 salio catalogado como Secure EBR en la pagina del sprint.
- Prueba documental 2: RCS-28068, el mismo defecto hoy, ya esta con Shandana Khan y ella lo movio a Accepted into Development.
- Shandana Khan es el punto de entrada de Engineering y reasigna. Cita suya en RCS-23643 del 22 oct 2025: "Assigning to @Mohammed Mutahhar for initial Engineering support as current SRE. Please assign back to me for planning if this needs deeper investigation or is a legitimate platform bug."
- Estado leido en vivo de Jira: Status `Under Engineering Review`, Assignee Shandana Khan, Priority High, link `relates to RCS-28068`, label `EB&F_scheduled`. El link a RCS-27586 ya no aparece.
- Platform fue consultado dos veces dentro del ticket, el 28 de julio y el 3 de agosto. Ninguna consulta obtuvo respuesta en 26 dias. Ese registro justifica la escalacion por via formal.
- Precedente de rechazo por requisitos: el 13 de agosto Aimee devolvio cuatro tickets de Vedant. RCS-28007 llevaba la investigacion completa de Tyrone Whitney y no paso, porque el assignee solo habia puesto "CC: Matthew Kamminga".
- Procedimiento que funciono para los pasos de reproduccion: uno por tenant, numerados, con resultado esperado contra resultado observado. Harbor Freight con rango por defecto, Floor & Decor con el rango 08/08 a 08/14 que dio Paul, lululemon con la variacion de rangos que hizo la clienta.
- La skill `cerebro-comentario` quedo corregida con cuatro cierres: tabla explicita de los cuatro requisitos de Aimee, subseccion de como escribir pasos de reproduccion, paso 0.1 de verificar el destino contra dos precedentes antes de redactar, y regla de que el reporter interno no relaja nada. La lista de verificacion final paso de cinco a siete puntos.

## Estado del ticket segun la sesion

- Ticket en Under Engineering Review con Shandana Khan. La transicion ya esta hecha y verificada contra Jira.
- Pasos 1 y 3 del PLAN marcados como hechos.
- Mensaje de Teams reescrito y dirigido a Shandana, conectando RCS-27991 con RCS-28068. El mensaje anterior dirigido a Ian quedo obsoleto.
- Quedan tres acciones para Juan: pegar el comentario interno, mandar el Teams a Shandana, responderle a Paul, en ese orden.

## Pendiente de verificar

- El ENG debe auto crearse con la transicion segun el documento de Aimee, con sincronizacion de comentarios en ambos sentidos. Al leer el ticket solo aparecia el link a RCS-28068. Revisar si el ENG salio.
- La etiqueta `EB&F_scheduled` aparecio en el ticket y no esta documentada en ninguna parte de Cerebro. Se desconoce quien la puso y que dispara.
- Los pasos de HFT dicen "leave the default date range applied". Paul nunca confirmo que rango tenia el 27 de julio, solo entrego el de Floor & Decor.
- El archivo obsoleto del mensaje para Ian sigue en disco. No se pudo borrar desde el sandbox.
- La regla del reporter interno no esta escrita en `cerebro-respuesta-cliente`.


## Rastro
2026-08-28 inbox/2026-08-28-cosecha-rcs-27991.md

## Cosecha RCS-28294 — 2026-08-28 — 2026-08-28
_chunk 1770 · 2026-08-28 · fuente: inbox/2026-08-28-cosecha-rcs-28294.md_

# Cosecha RCS-28294 — 2026-08-28
Fuente: sesion local_6b9ddbe6-cea3-4ade-a8bb-a3632ed3e03c, "Cerebro Ticket RCS-28294"

## Hallazgos verificados

- La comparacion de dos casos es la evidencia que sirve a Engineering. Mismo tenant, mismo tipo de caso, mismas tres alertas, mismo filtro satisfecho, siete dias de diferencia. `ShopliftingID 48575` genero tres filas. `ShopliftingID 48786` no genero ninguna.
- Cero filas significa que el motor nunca se invoco para ese caso. Ese fallo es distinto de que el motor corra y el filtro devuelva falso. Diferenciar los dos caminos de ejecucion es trabajo de codigo.
- La explicacion que se dio al cliente el 12 de agosto es falsa. El PDF de Tatiana mas los filtros lo prueban.
- El defecto es intermitente y la condicion no esta aislada. Los pasos de reproduccion llegan hasta el punto de fallo y no lo fuerzan.
- Fallo de proceso identificado: el comentario escalado salio sin la seccion de pasos de reproduccion. La reestructuracion en seis secciones la dejo fuera. JR los pidio explicitos el 25, documentados en detalle. Shandana quedo bloqueada por esa ausencia.
- Distincion que causo el fallo: probar que el defecto existe no equivale a poder depurarlo. Para lo primero basta la configuracion. Para lo segundo Engineering necesita una ruta recorrible en codigo.
- Advertencia tecnica marcada en el paquete: `DateEntered` puede estar en UTC. Tomar esos timestamps como hora local reconstruye una teoria de horario que ya se cayo.
- Advertencia operativa: los pasos implican crear un caso de Employee Relations en produccion del cliente. Quien los ejecute debe usar nombres de prueba evidentes.
- Existe un segundo caso documentado, del 18 de agosto. El problema ya no depende de un solo caso del cliente.
- Decision de arquitectura de skills: `cerebro-comentario` y `cerebro-respuesta-cliente` quedan separadas por proposito y cada una apunta a la otra en su descripcion. `cerebro-comentario` se dejo intacta.
- Regla confirmada por Juan sobre comentarios a cliente. El cliente no recibe resumen de la investigacion ni detalle tecnico. La unica excepcion es corregir algo que se le dijo mal o que el refuto.

## Estado del ticket segun la sesion

- Paquete con los pasos de reproduccion escrito y listo para responderle a Shandana. Ese es el desbloqueo que Engineering pidio.
- Nota al cliente reescrita en texto plano, siete parrafos, sin tablas ni negritas. Corrige el 12 de agosto una sola vez, declara que esta escalado, no promete fecha y pide dos cosas.
- Skill `cerebro-respuesta-cliente` creada con la regla que se rompio y un checklist final que obliga a borrar toda frase que describa hallazgos.

## Pendiente de verificar

- La condicion que dispara el defecto sigue sin aislar. No se sabe por que `48786` no invoco el motor y `48575` si.
- Falta confirmar si `DateEntered` esta en UTC.
- Shandana no ha corrido los pasos ni ha respondido.
- `cerebro-comentario` conserva su seccion "Formato 2. Respuesta al cliente", ahora duplicada contra la skill nueva. Juan no autorizo quitarla.


## Rastro
2026-08-28 inbox/2026-08-28-cosecha-rcs-28294.md

## Cosecha RCS-28581 — 2026-09-01 — 2026-09-01
_chunk 1777 · 2026-09-01 · fuente: inbox/2026-09-01-cosecha-rcs-28581.md_

# Cosecha RCS-28581 — 2026-09-01
Fuente: sesion local_96c44601-41c1-4a02-8a2d-0c7ef495cf4b, "RCS-28581 investigacion avance"

Chemist Warehouse, POS number equivocado en el recibo. La ficha decia "Camping World" y quedo corregida a Chemist Warehouse.

## Hallazgos verificados

- Estado en Jira al 1 sep: Under Support Review, asignado a Juan, sin ENG enlazado. Ultima actividad propia el 27 ago. Cuatro dias de deuda con James.
- Existe el fix original. DO-9495, "CW - UAT - Wrong POS number for transactions", cerrado el 29 abr 2026. Tomasz Sutkowski lo diagnostico textual: `The value '71' is taken from ardm_event_vw.pos_number, while I can see requested 'TILL11' is available in ardm_header_vw.machine name`. El fix cambio la fuente del campo a `machine_name`.
- DO-9495 cerro con `fixVersions` vacio, paso por el estado "Reload Required" y Bartosz Bereski lo materializo recargando a mano un archivo bajo `c248_rawdata_postransactions/2026/02/17/17/`. La correccion nunca quedo persistida en `map_ardm_header.sql`. Eso encaja con el "data period" que reporto James.
- DO-9495 aparece modificado el 19 ago. Es un bulk edit de label por Austin Flannery. No es trabajo tecnico, descartalo.
- Dato que no cuadra. El valor malo actual es 863485, seis digitos. En DO-9495 el valor malo era 71, un register de dos digitos. No afirmes reversion limpia a DO-9495 hasta comprobar de que columna sale 863485.
- Limite de la evidencia. Las dos capturas son de tiendas distintas, store 036 Coburg contra store 803 Sydney, y sin fecha visible. Con eso no se separa corte por fecha de corte por tienda.
- Riesgo a declarar antes de proponer cualquier correccion: `posno` entra en `get_transaction_id()`, la PK de 19 digitos. Remapear POS number cambia el `transactionid` de las transacciones nuevas.

## Decision de metodo

No hace falta nada de James para avanzar. El discriminador fecha contra tienda sale de la base. El comentario al cliente queda con cero peticiones.

El primer borrador rompio dos reglas de `cerebro-respuesta-cliente`: pidio datos que Juan resuelve solo con un SELECT, y justifico la peticion contando que las capturas eran de tiendas distintas, que es un hallazgo de investigacion. Reescrito con cero peticiones, la deuda del 27 corregida en una oracion y el proximo contacto anclado a tener la causa.

## Conseguir el SQL del search

Precedente: RCS-27644 en H&M, registrado en `brain/markdown/16-rcs-soluciones.md`. Textual: "al darle a Claude el SQL real del report aparecio una REGRESION genuina: el filtro del cliente hace ActionType NOT IN (…) y descartaba el 94% de los headers". La leccion quedo escrita asi: "pedir/conseguir siempre el SQL del search (correr el report con parametros dummy para ver el query), fue lo que destrabo la causa raiz".

En este ticket el SQL real sirve para tres cosas. Dice de que columna sale el 863485. Confirma si el campo lee `machine_name` o volvio a `pos_number`. Y deja el query listo para reusarlo como SELECT sobre CWH agrupando por tienda y por tradingday.

## Accesos y ruta verificada

- Composer vive dentro del tenant del cliente. Confluence "Secure EBR Application Topology", pageId 477571317762: `Search Composer, Routes client transaction queries to either Green Plum or Snowflake depending on migration status`.
- Control Panel es interno. Confluence "Control Panel - Start Here", pageId 475169095710: `Control Panel is internal to Appriss Retail only. Customers do not have access to the Control Panel.` Control Panel es el salto, no el destino.
- Ruta operativa: `usprod.apprissretailcloud.com/control`, tabla Customers in USPROD, buscar Chemist Warehouse, primera columna "Click logo to sign in". No uses `/<slug>/signin`, redirige al SSO del cliente donde el usuario de Appriss no existe. Ya dentro: All Apps, Secure Store, Explorer, Composer. El boton Query de la barra imprime el SQL generado.
- Snowflake directo: rol `PUBLIC` por defecto con lectura sobre ARDMPROD, warehouse `SUPPORTDATA_XS_WH`, login `app.snowflake.com/okb13541/jn80103/`. La guia de RTS dice `without waiting on Engineering`.
- El cerebro registra CWH como `248 | chemistwarehouse.com | CWH | GP11 | GP1 | Azure`. GP11 y GP1 son instancias Greenplum. Si CWH no migro a SnowTime, el query no va a Snowflake sino a Greenplum, y eso se alcanza por salto al jump server LA4 por RDP. Circulan tres nombres de base distintos en la documentacion y ninguno coincide.
- Orden acordado: corre Composer primero. El boton Query resuelve las dos incognitas de un tiro, que columna alimenta el campo Pos y a que motor apunta el query. No pidas acceso a nada hasta saber que motor responde.
- Gotchas de Composer: el quick link materializa una copia efimera bajo `unsaved searches`. Abrir, correr, leer, sin editar nada.

## Adjuntos

Guardados en `adjuntos/RCS-28581/` con descripcion textual buscable.

## Referencias

RCS-28581, DO-9495, DO-7534, RCS-27644. Confluence: dbt-mapping pageId 477834641411, Customer Profile Myer pageId 477951524865, Secure EBR Application Topology pageId 477571317762, Control Panel Start Here pageId 475169095710, Using Snowflake for Support Investigations pageId 477651730444, Support Team Snowflake Access pageId 477731028995.


## Rastro
2026-09-01 inbox/2026-09-01-cosecha-rcs-28581.md

## RCS-28212, hipotesis con evidencia dura de capturas de pantalla — 2026-09-03
_chunk 1790 · 2026-09-03 · fuente: inbox/2026-09-03-cosecha-rcs-28212-apis-case-elevation.md_

---
fecha: 2026-09-03
fuente: cosecha de sesion local, RCS-28212 ticket resolution
sesion: local_fe6e5567-7400-4bc1-b3ef-44b95546c918
---

# RCS-28212, hipotesis con evidencia dura de capturas de pantalla

Las capturas de pantalla que llegaron cambiaron el diagnostico. Sigue siendo hipotesis, faltan dos
verificaciones dentro de APIS.

## Lo que las capturas muestran

El reporte 5165 filtra `case.event_type` con operador `=` contra el literal `Corporate`. El caso
`CA-44541-COR-2026-0001` guarda el valor `* COR`. Ese filtro lo excluye por construccion, no por un
bug del reporte.

El asterisco es la pista. Aparece en dos campos a la vez, `* COR` y `* CORPORATE EMPLOYEE`. La
aplicacion pinta el asterisco cuando el valor guardado no existe en la lista activa del dropdown del
tenant. El caso trae `Related incident: IN-44541-COR-2026-0001 (Elevated)` y el campo requerido
`Event Alpha Code` vacio. La hipotesis es que la elevacion de incidente a caso copia el codigo del
incidente sin mapearlo a la lista de casos.

## Verificaciones que faltan, pasos 3 y 4 del instructivo

Abrir el dropdown de Case Type en APIS y confirmar si `COR` esta o no en la lista del tenant.
Abrir `CA-43895-CORP-2026-0001` y confirmar que los casos buenos no vienen de una elevacion.

## Lo que Cerebro tenia y lo que no tenia

Los siete reflejos de troubleshooting de APIS que enseño Kristine estan en
`brain/markdown/21-kt-kristin-sign-off-procesos-rts.md`, lineas 499 a 512. El acceso PROD por la
cuenta de Julie Barber esta en la linea 527. Nada en Cerebro ni en Confluence cubre case types de
APIS, COR, CORP, ni la elevacion incidente a caso. El espacio AALPS de Confluence tiene dos paginas
de 2021 y la principal apunta a un manual de administracion en el OneDrive de una cuenta desactivada.

## Que hacer y que no hacer todavia

El workaround que desbloquea al cliente hoy es cambiar el operador del reporte de `=` a `IN` con
`Corporate,COR`. Es trabajo de soporte, Juan tiene acceso PROD para hacerlo. La correccion de datos
exige escritura en base y es territorio de Kamminga.

No comentar al cliente todavia. El ticket sigue en Under Engineering Review con assignee de
Engineering. Comentar ahi repite el error que ya paso en RCS-28161. El instructivo trae el comentario
interno para Kamminga con cinco huecos que se llenan con lo que salga de los pasos 3 a 7.

Dato que acota la ventana: 7-Eleven migra a Incident alrededor de septiembre u octubre de 2026. La
ventana util de cualquier arreglo en APIS es de semanas, no de meses.

## Pendiente manual para Juan

Los PNG originales no se pudieron mover a `adjuntos/RCS-28212/` porque bash estaba denegado en esa
sesion. Arrastrarlos ahi a mano como `image-20260806-133803.png` y `image-20260806-134110.png`. La
descripcion en texto ya quedo guardada y buscable.


## Rastro
2026-09-03 inbox/2026-09-03-cosecha-rcs-28212-apis-case-elevation.md

## RCS-27549. High de ICA SE, abierto 25 jun (76 dias). Lentitud al cargar recibos en Work Items y, desde 10 ago, en Investi — 2026-09-09
_chunk 1809 · 2026-09-09 · fuente: inbox/2026-09-09-rcs-27549-protocolo.md;2026-09-09-rcs-27549.md_

Ticket RCS-27549. Trabajado el 2026-09-09. 2 notas en inbox.

## Que pasa
High de ICA SE, abierto 25 jun (76 dias). Lentitud al cargar recibos en Work Items y, desde 10 ago, en Investigation. Hoy J.R. Teagle dijo que Jon Morgan lo da por resuelto y pidio a Juan verificar antes de avisar al cliente. Estado: Under Support Review, assignee Juan.

## Evidencia
- Jira, Gabor Remenyi 26-jun 09:51: "not a bug, it's a limitation with Snowtime"
- Jira, J.R. Teagle 09-sep 11:51: "Jon Morgan says this is resolved... switched to ARDM Json loaded by SnowTime... double check"
- Jira, Camila Cortes 04-sep 16:32: la mejora de cache de jul no estaba habilitada para ICA; lo del 10 ago en Investigation seguia sin causa confirmada

## Precedentes
- RCS-27994, ICA SE, mismo sintoma, separado 28 jul, sin asignar al 8 sep. tickets/RCS-27994.md
- SnowTime, monitoreo y migracion. brain/markdown/20-snowtime-monitoring-migracion.md
- Sin investigacion previa sobre carga por clic ni migracion a ARDM Json. Se documenta aqui primera vez.

## Rastro
2026-09-09 inbox/2026-09-09-rcs-27549-protocolo.md
2026-09-09 inbox/2026-09-09-rcs-27549.md

## RCS-28212. Escalacion critica de 7-Eleven sigue abierta. Hoy se ejecuto en APIS PROD toda la investigacion pendiente desd — 2026-09-15
_chunk 1823 · 2026-09-15 · fuente: inbox/2026-09-02-rcs-28212-informe.md;2026-09-02-rcs-28212-instructivo.md;2026-09-15-correccion-company-id-7eleven.md;2026-09-15-rcs-28212-hoy.md_

Ticket RCS-28212. Trabajado el 2026-09-02 a 2026-09-15. 4 notas en inbox.

## Que pasa
[2026-09-02] Cuando un incidente de 7-Eleven se eleva a caso, APIS copia el código corto del incidente al campo
Case Type del caso en lugar de mapearlo al valor de la lista de casos. El resultado es un caso con
Case Type `* COR` en vez de `Corporate`, y el reporte AdHoc "Corp_Internal_Theft_Fraud" filtra por
igualdad exacta contra `Corporate`, así que esos casos desaparecen del reporte. El caso creado
directamente sí sale bien, lo que aísla el defecto al camino de elevación.

---
[2026-09-15] Escalacion critica de 7-Eleven sigue abierta. Hoy se ejecuto en APIS PROD toda la investigacion
pendiente desde el 2 sep. La causa raiz quedo confirmada en vivo. El workaround de reporte del
Paso 7 se probo y no es viable con las herramientas estandar de APIS.

## Causa
**Hipótesis, no causa raíz confirmada.** La marco como hipótesis porque falta un paso de
verificación que exige entrar a APIS.

Enunciado: el camino de elevación de incidente a caso copia el valor de tipificación del incidente
al campo homólogo del caso sin mapearlo a la lista de valores de caso. La lista de casos no contiene
`COR`, contiene `CORP` con etiqueta `Corporate`, así que el valor queda huérfano y la UI lo pinta
con asterisco. El mismo mecanismo explica `* CORPORATE EMPLOYEE` en el sub type y el
`Event Alpha Code` vacío.

Lo que sostiene la hipótesis: el asterisco en dos campos a la vez, el `Related incident (Elevated)`
presente solo en los casos malos, el campo requerido sin poblar, y el contraste con
`CA-43895-CORP-2026-0001` que se creó bien.

Lo que falta para confirmarla: abrir en APIS la lista de Case Types del tenant 7-Eleven y verificar
si `COR` existe como valor activo, como valor desactivado, o si no existe. Y abrir un caso bueno
para confirmar que no tiene `Related incident (Elevated)`. El instructivo lleva los dos pasos.

Descartada por evidencia: error de digitación del usuario. Un usuario no escribe el asterisco, la
aplicación lo pinta.

---

## Evidencia
[2026-09-02] **1. El reporte filtra por igualdad exacta contra un literal.**
Fuente: captura 1, pantalla "Ad Hoc Query Builder: Configure filters", Report Title
`Corp_Internal_Theft_Fraud`. La primera línea de filtro es:

    Selected Column: case.event_type
    Report.default label: Case Type
    Report.name of filter: case.event_type
    Comparison Operator: =
    Operand: Corporate
    User Input Type: Fixed

Operador `=`, operando `Corporate`, tipo Fixed. Un caso cuyo `event_type` valga `COR` nunca entra
en ese resultado. El síntoma reportado queda explicado sin necesidad de hipótesis adicional.

La segunda línea usa otro operador. `case.event_sub_type` con `IN` sobre una lista múltiple que
incluye CDC Chargebacks, Critical Incident, Expense Fraud AP y Fraud. El pie de la pantalla lo
confirma: "Use comma delimiter with IN". El constructor sí soporta `IN` en ese campo.

**2. El caso malo nació de una elevación, y lo dice el propio caso.**
Fuente: captura 2, ficha de `CA-44541-COR-2026-0001`. En el bloque Additional Information:

    Related incident: IN-44541-COR-2026-0001 (Elevated)

El incidente origen ya trae `COR` en su número. El caso heredó ese mismo `COR`.

**3. El valor mostrado llev
[2026-09-15] - Dropdown de Case Type en CA-44541-COR-2026-0001: lista real es Corporate, External, Franchise,
  Labor/Tips/Subpoena, Vendor/Contractor. COR no esta, solo aparece como fila `* COR` inyectada
  fuera de la lista para mostrar el valor guardado.
- Copia de prueba del reporte 5165 (ID 5511, Corp_Internal_Theft_Fraud_Copy): el Operand de
  event_type se llena desde el mismo catalogo, con CONTAIN o IN nunca ofrece COR.
- Filtro adicional sobre case.iice_id CONTAIN -COR-, en OR, corrido dos veces con Update Fields y
  Preview: cero casos nuevos. iice_id es el ID interno, no el texto visible del Case ID.

## Impacto
Alcance dentro de 7-Eleven: todo caso elevado desde un incidente queda fuera de cualquier reporte
AdHoc que filtre `case.event_type` con operador `=`. El reporte 5165 es uno. Hay que contar cuántos
más usan igualdad exacta sobre ese campo, porque el mismo hueco los afecta a todos.

Alcance fuera de 7-Eleven: el camino de elevación es código de producto, no configuración de tenant.
Los otros catorce clientes de APIS que elevan incidentes a casos podrían tener el mismo hueco sin
haberlo notado, porque solo se ve si construyeron un reporte con filtro exacto. Los nombres están en
`brain/markdown/21-kt-kristin-sign-off-procesos-rts.md` líneas 599 a 619, documento interno, no
compartir fuera.

Riesgo de negocio para el cliente: los casos que no salen del reporte son de robo interno
corporativo. El caso de la captura vale 1.930,32 USD con reason CASH THEFT. Casos que existen y no
aparecen en el reporte de fraude interno es un hueco de reporting, no un hueco cosmético.

Riesgo de la ventana: 7-Eleven migra a Incident alrededor de sep/oct 2026. Un arreglo de código en
APIS no va a llegar a tiempo ni está permitido por política. El entregable realista es el
workaround en el reporte más una c

## Que sigue
**Recomendación: avanza tú, no lo sueltes, y tampoco te lo lleves entero.**

Razones. El ticket lleva quince días sin movimiento desde el comentario de Viraj del 18 de agosto.
Tienes acceso a PROD de APIS. La parte que desbloquea al cliente hoy es configuración de reporte,
que es trabajo de soporte, no de ingeniería. La parte que exige escritura en base de datos es de
Kamminga y solo de él.

El reparto que propongo:

1. Tú verificas en APIS los dos puntos que faltan para cerrar la causa raíz, y pruebas el workaround
   del filtro `IN`. Eso convierte una hipótesis en un diagnóstico cerrado.
2. Tú le entregas a Kamminga el diagnóstico cerrado más el conteo de casos afectados. Él decide la
   corrección de datos.
3. El cliente recibe el workaround del reporte cuando el ticket vuelva a soporte, o antes si
   Kamminga lo autoriza.

Qué **no** hacer todavía. El ticket está en Under Engineering Review con assignee de Engineering. No
le comentes al cliente sobre el fondo del defecto mientras siga así. Ese es el error que se cometió
en RCS-28161.

Los pasos concretos, en orden y listos para ejecutar, están en el instructivo.

## Precedentes
[2026-09-02] | Ticket | Qué aporta | Estado |
|---|---|---|
| RCS-1508 | 7-Eleven APIS, case types. Kamminga documenta que `Event Type` en pantalla es `event_sub_type` en el filtro, y que el cliente crea sus propios subtipos. Rounok Joardar cerró ajustando el formulario del incidente | Closed |
| RCS-12432 | Define elevar como investigación → caso, y que hay campos requeridos configurables antes de elevar | Closed |
| RCS-3053 | Krogman confirma que mover CA a IN no existe en APIS y sería un enhancement cobrable | Closed |
| RCS-27330 | 7-Eleven APIS, sin valor. Krogman: "Claude opened this ticket from a search I was doing. Not needed". Descartar | Closed |

Sin precedente de truncamiento COR contra CORP. RCS-28212 es el prime

[cortado en el techo, el detalle esta en el rastro]

## RCS-28223. Las dos auditorias juntas, para comparar de un vistazo. ```sql SELECT acs.AuditConfigID, acs.SectionDescriptio — 2026-09-14
_chunk 1824 · 2026-09-14 · fuente: inbox/2026-08-27-rcs-28223-EVIDENCIA.md;2026-08-27-rcs-28223-causa-raiz.md;2026-08-27-rcs-28223-consultas-parte2.md;2026-08-27-rcs-28223-consultas-parte3.md;2026-08-27-rcs-28223-consultas-parte4.md;2026-08-27-rcs-28223-consultas.md;2026-08-27-rcs-28223-continuidad-david-vargas.md;2026-08-27-rcs-28223-esquema-audit.md;2026-08-27-rcs-28223-hallazgos-pdf.md;2026-09-14-rcs-28223-repro-paso-a-paso.md_

Ticket RCS-28223. Trabajado el 2026-08-27 a 2026-09-14. 10 notas en inbox.

## Que pasa
Las dos auditorias juntas, para comparar de un vistazo.

```sql
SELECT  acs.AuditConfigID,
        acs.SectionDescription,
        acq.QuestionType,
        COUNT(*) AS Preguntas,
        SUM(CASE WHEN acq.GridCols IS NULL THEN 1 ELSE 0 END) AS SinGridCols,
        SUM(CASE WHEN acq.GridConfig IS NULL THEN 1 ELSE 0 END) AS SinGridConfig,
        MIN(DATALENGTH(acq.GridCols)) AS GridCols_Min,
        MAX(DATALENGTH(acq.GridCols)) AS GridCols_Max
FROM    incident.AuditConfigQuestion acq
JOIN    incident.AuditConfigSection acs ON acs.AuditConfigSectionID = acq.AuditConfigSectionID
WHERE   acs.AuditConfigID IN (2, 4)
  AND   ISNULL(acq.DeleteFlag, 0) = 0
GROUP BY acs.AuditConfigID, acs.SectionDescription, acq.QuestionType
ORDER BY acs.AuditConfigID, acs.SectionDescription, acq.QuestionType;
```

---

## Evidencia
[2026-08-27] Corrido el 27 y 28 ago 2026 contra el tenant mcdonalds, Client ID 402, AuditConfigID 4.
Todo sale de SELECT.
[2026-09-14] - Captura de la grilla con la URL visible y el cursor en Coaching.
- Numero de la auditoria que usaste y la hora.
- El resultado del bloque 4 pegado como texto.
- Navegador y version.

## Que sigue
[2026-08-27] El SELECT de `inbox/2026-08-27-rcs-28223-plan-repro.sql` ya se puede correr con Client ID 402.
Sirve para numerar las preguntas de Crew y confirmar su FieldType.
[2026-09-14] Confirmar con Hugo Cortez (o un usuario real con rol Manager) si el grid acepta input en su cuenta. Recien con eso se puede escribir el comentario formal en Jira. No se ha posteado nada a Jira, solo se le informo a J.R. en chat que la prueba manual de hoy no reprodujo el error en las pantallas documentadas, dejando explicito que falta cerrar el rol Manager antes de dar el caso por resuelto.

## Precedentes
- Comentario del 27 ago en Jira, pasos originales: inbox/2026-08-27-rcs-28223-comentario-interno.md
- Evidencia de la base: inbox/2026-08-27-rcs-28223-EVIDENCIA.md
- Consultas completas: inbox/2026-08-27-rcs-28223-plan-repro.sql
- Acceso al tenant: brain/memoria/project_juan_accesos.md

## Rastro
2026-08-27 inbox/2026-08-27-rcs-28223-EVIDENCIA.md
2026-08-27 inbox/2026-08-27-rcs-28223-causa-raiz.md
2026-08-27 inbox/2026-08-27-rcs-28223-consultas-parte2.md
2026-08-27 inbox/2026-08-27-rcs-28223-consultas-parte3.md
2026-08-27 inbox/2026-08-27-rcs-28223-consultas-parte4.md
2026-08-27 inbox/2026-08-27-rcs-28223-consultas.md
2026-08-27 inbox/2026-08-27-rcs-28223-continuidad-david-vargas.md
2026-08-27 inbox/2026-08-27-rcs-28223-esquema-audit.md
2026-08-27 inbox/2026-08-27-rcs-28223-hallazgos-pdf.md
2026-09-14 inbox/2026-09-14-rcs-28223-repro-paso-a-paso.md

## RCS-28756. Nike respondio el 2026-09-11 via Akshaya que ellos no hacen push, que exponen un stream Kafka y Appriss se con — 2026-09-15
_chunk 1830 · 2026-09-15 · fuente: inbox/2026-09-04-rcs-28756-informe.md;2026-09-04-rcs-28756-instructivo.md;2026-09-09-instructivo-cierre-del-dia.md;2026-09-09-rcs-28756-chat-nichols.md;2026-09-09-rcs-28756-chat-peyman.md;2026-09-09-rcs-28756-fraseo-corte.md;2026-09-09-rcs-28756-instructivo.md;2026-09-09-rcs-28756.md;2026-09-10-rcs-28756.md;2026-09-11-rcs-28756-kafka-bridge.md;2026-09-15-rcs-28756-update-saddam.md_

Ticket RCS-28756. Trabajado el 2026-09-04 a 2026-09-15. 11 notas en inbox.

## Que pasa
[2026-09-10] Ayesha pidio tres veces hoy la informacion segura para el cliente. El ticket esta en Under Support
Review con Juan. La arquitectura ya esta documentada y las cinco respuestas estan listas.
[2026-09-11] Nike respondio el 2026-09-11 via Akshaya que ellos no hacen push, que exponen un
stream Kafka y Appriss se conecta a consumirlo. Copiaron a un arquitecto suyo.
Piden logs o errores de conexion de nuestro lado.

Eso contradice la respuesta que Ayesha ya envio a Nike el 2026-09-10, donde le
dijimos que no hay consumer de Appriss, que no es Kafka y que ellos publican a
nuestra Ingestion API. Los puntos 1, 2 y 3 de esa respuesta estan mal.

## Causa
Marco esto como HIPOTESIS, no como causa raiz confirmada. Nike dejo de enviar archivos
ECOM/raw_order a partir del 28 de agosto de 2026. La sostienen tres puntos independientes: la
ausencia de archivos nuevos despues del 27 de agosto a las 19:02 UTC, la confirmacion de Carl de
que los servicios de ingesta de Appriss estan arriba, y la ejecucion limpia del pipeline ARDM para
cliente 067 en la ventana revisada por Juan. Ningun log revisado muestra una falla de Appriss que
explique el corte. Nike no ha confirmado la causa de su lado a la fecha de este informe.

## Evidencia
[2026-09-10] Confluence PD 477499490306, Ingestion API - EventHub, Carl Costelow: "Customers POST data to the
API, which routes it into Azure Event Hub (small payloads) or Azure Blob Storage". El hub se nombra
solo como c{customerID}_rawdata_{dataType}, de ahi c67_rawdata_order.
Tres validaciones inbound: nombre de cliente 400/10, identidad contra ClientID y ClientScope 401/12,
dataType permitido 400/11.
Incoming Messages y Captured Messages de c67_rawdata_order en cero desde 2026-08-27 19:02 UTC.
[2026-09-11] - ENG-4235, descripcion completa, lineas 573, 541 y 457 de kafka_ingestion/nike.py
- Event Hub prd-datacloud-wus2-ehub-1, entidad c67_rawdata_order, Incoming y
  Captured en cero desde 2026-08-27 19:02 UTC
- Correo de Nike del 2026-09-11 en RCS-28756, arquitecto de Nike en copia

## Impacto
Los Work Items del control GNG para Nike/67 quedan en pausa desde el 1 de septiembre por conteo
bajo el minimo de 560392 transacciones. Eso incluye definiciones de auditoria de descuentos no
autorizados y de fraude en devoluciones, segun el listado de Ayesha Mehar del 3 de septiembre. Cada
dia adicional sin archivos ECOM ensancha la brecha de datos y retrasa esos controles de manera
acumulativa, no puntual.

## Que sigue
La decision pendiente no es tecnica, es de estado del ticket. RCS-28756 sigue en Under Support
Review desde el 3 de septiembre pese a que la investigacion de soporte esta cerrada y lo unico
pendiente es la respuesta de Nike, ya agendada para el 8 de septiembre via RTS-206999. Dejarlo en
Under Support Review dos dias mas dice, para quien mire la cola, que falta trabajo de Appriss.
No es el caso. La transicion a Under Customer Review documenta con precision donde esta el bloqueo
real. El instructivo trae el comentario y la transicion listos para pegar.

## Precedentes
[2026-09-10] investigaciones/ingestion-api-como-entra-la-data.md. Flujo completo y criterio de que compartir.
RCS-28753. Peyman compartio nombres de campos y feeds con Nike, no codigo. Mismo criterio.
tickets/RTS-206999.md. Canal con Nike.
[2026-09-11] - ENG-4235, mismo servicio, 2 fallas Sev0 de health check en prd, 8 y 10 de abril
- Peyman confirmo el 2026-09-09 que hay una API de Appriss entre Nike y el blob.
  Iba en la direccion correcta, la cadena tiene una pieza mas arriba
- AR Gateway normaliza ingesta por REST, Kafka o colas al formato de landing,
  brain/markdown/14-appriss-ingenieria-docs-fuente.md

## Rastro
2026-09-04 inbox/2026-09-04-rcs-28756-informe.md
2026-09-04 inbox/2026-09-04-rcs-28756-instructivo.md
2026-09-09 inbox/2026-09-09-instructivo-cierre-del-dia.md
2026-09-09 inbox/2026-09-09-rcs-28756-chat-nichols.md
2026-09-09 inbox/2026-09-09-rcs-28756-chat-peyman.md
2026-09-09 inbox/2026-09-09-rcs-28756-fraseo-corte.md
2026-09-09 inbox/2026-09-09-rcs-28756-instructivo.md
2026-09-09 inbox/2026-09-09-rcs-28756.md
2026-09-10 inbox/2026-09-10-rcs-28756.md
2026-09-11 inbox/2026-09-11-rcs-28756-kafka-bridge.md
2026-09-15 inbox/2026-09-15-rcs-28756-update-saddam.md

## RCS-28099. Revisión integral, 28 septiembre 2026. Qué pasa CWH sigue preparando seis conjuntos de datos para revisar desc — 2026-09-28
_chunk 1850 · 2026-09-28 · fuente: inbox/2026-09-16-rcs-28099-revision-cola.md;2026-09-24-rcs-28099-seguimiento-ucr.md;2026-09-28-rcs-28099-prioridad-auditoria.md_

Ticket RCS-28099. Trabajado el 2026-09-16 a 2026-09-28. 3 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Revisión integral, 28 septiembre 2026. Qué pasa CWH sigue preparando seis conjuntos de datos para revisar descuentos. Esperando evidencia; revisar antigüedad. consolidación del cliente; resolución técnica no confirmada.

## Rastro
2026-09-16 inbox/2026-09-16-rcs-28099-revision-cola.md
2026-09-24 inbox/2026-09-24-rcs-28099-seguimiento-ucr.md
2026-09-28 inbox/2026-09-28-rcs-28099-prioridad-auditoria.md

## RCS-28212. Escalacion critica de 7-Eleven sigue abierta. Hoy se ejecuto en APIS PROD toda la investigacion pendiente desd — 2026-10-05
_chunk 1851 · 2026-10-05 · fuente: inbox/2026-09-02-rcs-28212-informe.md;2026-09-02-rcs-28212-instructivo.md;2026-09-15-correccion-company-id-7eleven.md;2026-09-15-rcs-28212-hoy.md;2026-09-16-rcs-28212-revision-cola.md;2026-09-16-rcs-28212-verificacion-pendiente.md;2026-09-24-rcs-28212-seguimiento-ucr.md;2026-09-25-rcs-28212-consulta-7-eleven.md;2026-09-28-rcs-28212-prioridad-auditoria.md;2026-10-05-cierre-turno-cola.md_

Ticket RCS-28212. Trabajado el 2026-09-02 a 2026-10-05. 10 notas en inbox.

## Que pasa
[2026-09-02] Cuando un incidente de 7-Eleven se eleva a caso, APIS copia el código corto del incidente al campo
Case Type del caso en lugar de mapearlo al valor de la lista de casos. El resultado es un caso con
Case Type `* COR` en vez de `Corporate`, y el reporte AdHoc "Corp_Internal_Theft_Fraud" filtra por
igualdad exacta contra `Corporate`, así que esos casos desaparecen del reporte. El caso creado
directamente sí sale bien, lo que aísla el defecto al camino de elevación.

---
[2026-09-15] Escalacion critica de 7-Eleven sigue abierta. Hoy se ejecuto en APIS PROD toda la investigacion
pendiente desde el 2 sep. La causa raiz quedo confirmada en vivo. El workaround de reporte del
Paso 7 se probo y no es viable con las herramientas estandar de APIS.

## Causa
**Hipótesis, no causa raíz confirmada.** La marco como hipótesis porque falta un paso de
verificación que exige entrar a APIS.

Enunciado: el camino de elevación de incidente a caso copia el valor de tipificación del incidente
al campo homólogo del caso sin mapearlo a la lista de valores de caso. La lista de casos no contiene
`COR`, contiene `CORP` con etiqueta `Corporate`, así que el valor queda huérfano y la UI lo pinta
con asterisco. El mismo mecanismo explica `* CORPORATE EMPLOYEE` en el sub type y el
`Event Alpha Code` vacío.

Lo que sostiene la hipótesis: el asterisco en dos campos a la vez, el `Related incident (Elevated)`
presente solo en los casos malos, el campo requerido sin poblar, y el contraste con
`CA-43895-CORP-2026-0001` que se creó bien.

Lo que falta para confirmarla: abrir en APIS la lista de Case Types del tenant 7-Eleven y verificar
si `COR` existe como valor activo, como valor desactivado, o si no existe. Y abrir un caso bueno
para confirmar que no tiene `Related incident (Elevated)`. El instructivo lleva los dos pasos.

Descartada por evidencia: error de digitación del usuario. Un usuario no escribe el asterisco, la
aplicación lo pinta.

---

## Evidencia
[2026-09-02] **1. El reporte filtra por igualdad exacta contra un literal.**
Fuente: captura 1, pantalla "Ad Hoc Query Builder: Configure filters", Report Title
`Corp_Internal_Theft_Fraud`. La primera línea de filtro es:

    Selected Column: case.event_type
    Report.default label: Case Type
    Report.name of filter: case.event_type
    Comparison Operator: =
    Operand: Corporate
    User Input Type: Fixed

Operador `=`, operando `Corporate`, tipo Fixed. Un caso cuyo `event_type` valga `COR` nunca entra
en ese resultado. El síntoma reportado queda explicado sin necesidad de hipótesis adicional.

La segunda línea usa otro operador. `case.event_sub_type` con `IN` sobre una lista múltiple que
incluye CDC Chargebacks, Critical Incident, Expense Fraud AP y Fraud. El pie de la pantalla lo
confirma: "Use comma delimiter with IN". El constructor sí soporta `IN` en ese campo.

**2. El caso malo nació de una elevación, y lo dice el propio caso.**
Fuente: captura 2, ficha de `CA-44541-COR-2026-0001`. En el bloque Additional Information:

    Related incident: IN-44541-COR-2026-0001 (Elevated)

El incidente origen ya trae `COR` en su número. El caso heredó ese mismo `COR`.

**3. El valor mostrado llev
[2026-09-15] - Dropdown de Case Type en CA-44541-COR-2026-0001: lista real es Corporate, External, Franchise,
  Labor/Tips/Subpoena, Vendor/Contractor. COR no esta, solo aparece como fila `* COR` inyectada
  fuera de la lista para mostrar el valor guardado.
- Copia de prueba del reporte 5165 (ID 5511, Corp_Internal_Theft_Fraud_Copy): el Operand de
  event_type se llena desde el mismo catalogo, con CONTAIN o IN nunca ofrece COR.
- Filtro adicional sobre case.iice_id CONTAIN -COR-, en OR, corrido dos veces con Update Fields y
  Preview: cero casos nuevos. iice_id es el ID interno, no el texto visible del Case ID.

## Impacto
[2026-09-02] Alcance dentro de 7-Eleven: todo caso elevado desde un incidente queda fuera de cualquier reporte
AdHoc que filtre `case.event_type` con operador `=`. El reporte 5165 es uno. Hay que contar cuántos
más usan igualdad exacta sobre ese campo, porque el mismo hueco los afecta a todos.

Alcance fuera de 7-Eleven: el camino de elevación es código de producto, no configuración de tenant.
Los otros catorce clientes de APIS que elevan incidentes a casos podrían tener el mismo hueco sin
haberlo notado, porque solo se ve si construyeron un reporte con filtro exacto. Los nombres están en
`brain/markdown/21-kt-kristin-sign-off-procesos-rts.md` líneas 599 a 619, documento interno, no
compartir fuera.

Riesgo de negocio para el cliente: los casos que no salen del reporte son de robo interno
corporativo. El caso de la captura vale 1.930,32 USD con reason CASH THEFT. Casos que existen y no
aparecen en el reporte de fraude interno es un hueco de reporting, no un hueco cosmético.

Riesgo de la ventana: 7-Eleven migra a Incident alrededor de sep/oct 2026. Un arreglo de código en
APIS no va a llegar a tiempo ni está permitido por política. El entregable realista es el
workaround en el reporte más una c
[2026-10-05] La cola automática marcó RCS-29132 como esperando al cliente por tomar el comentario interno de Talos como último movimiento. El cliente nunca recibió la actualización. Trátalo como deuda de Juan.

## Que sigue
**Recomendación: avanza tú, no lo sueltes, y tampoco te lo lleves entero.**

Razones. El ticket lleva quince días sin movimiento desde el comentario de Viraj del 18 de agosto.
Tienes acceso a PROD de APIS. La parte que desbloquea al cliente hoy es configuración de reporte,
que es trabajo de soporte, no de ingeniería. La parte que exige escritura en base de datos es de
Kamminga y solo de él.

El reparto que propongo:

1. Tú verificas en APIS los dos puntos que faltan para cerrar la causa raíz, y pruebas el workaround
   del filtro `IN`. Eso convierte una hipótesis en un diagnóstico cerrado.
2. Tú le entregas a Kamminga el diagnóstico cerrado más el conteo de casos afectados. Él decide la
   corrección de datos.
3. El cliente recibe el workaround del reporte cuando el ticket vuelva a soporte, o antes si
   Kamminga lo autoriza.

Qué **no** hacer todavía. El ticket está en Under Engineering Review con assignee de Engineering. No
le comentes al cliente sobre el fondo del defecto mientras siga así. Ese es el error que se cometió
en RCS-28161.

Los pasos concretos, en orden y listos para ejecutar, están en el instructivo.

## Precedentes
[2026-09-02] | Ticket | Qué aporta | Estado |
|---|---|---|
| RCS-1508 | 7-Eleven APIS, case types. Kamminga documenta que `Event Type` en pantalla es `event_sub_type` en el filtro, y que el cliente crea sus propios subtipos. Rounok Joardar cerró ajustando el formulario del incidente | Closed |
| RCS-12432 | Define elevar como investigación → caso, y que hay campos requeridos configurables antes de elevar | Closed |
| RCS-3053 | Krogman confirma que mover CA a IN no existe en APIS y sería un enhancement cob

[cortado en el techo, el detalle esta en el rastro]

## RCS-28223. Las dos auditorias juntas, para comparar de un vistazo. ```sql SELECT acs.AuditConfigID, acs.SectionDescriptio — 2026-10-13
_chunk 1852 · 2026-10-13 · fuente: inbox/2026-08-27-rcs-28223-EVIDENCIA.md;2026-08-27-rcs-28223-causa-raiz.md;2026-08-27-rcs-28223-consultas-parte2.md;2026-08-27-rcs-28223-consultas-parte3.md;2026-08-27-rcs-28223-consultas-parte4.md;2026-08-27-rcs-28223-consultas.md;2026-08-27-rcs-28223-continuidad-david-vargas.md;2026-08-27-rcs-28223-esquema-audit.md;2026-08-27-rcs-28223-hallazgos-pdf.md;2026-09-14-rcs-28223-repro-paso-a-paso.md;2026-09_

Ticket RCS-28223. Trabajado el 2026-08-27 a 2026-10-13. 17 notas en inbox.

## Que pasa
Las dos auditorias juntas, para comparar de un vistazo.

```sql
SELECT  acs.AuditConfigID,
        acs.SectionDescription,
        acq.QuestionType,
        COUNT(*) AS Preguntas,
        SUM(CASE WHEN acq.GridCols IS NULL THEN 1 ELSE 0 END) AS SinGridCols,
        SUM(CASE WHEN acq.GridConfig IS NULL THEN 1 ELSE 0 END) AS SinGridConfig,
        MIN(DATALENGTH(acq.GridCols)) AS GridCols_Min,
        MAX(DATALENGTH(acq.GridCols)) AS GridCols_Max
FROM    incident.AuditConfigQuestion acq
JOIN    incident.AuditConfigSection acs ON acs.AuditConfigSectionID = acq.AuditConfigSectionID
WHERE   acs.AuditConfigID IN (2, 4)
  AND   ISNULL(acq.DeleteFlag, 0) = 0
GROUP BY acs.AuditConfigID, acs.SectionDescription, acq.QuestionType
ORDER BY acs.AuditConfigID, acs.SectionDescription, acq.QuestionType;
```

---

## Evidencia
[2026-08-27] Corrido el 27 y 28 ago 2026 contra el tenant mcdonalds, Client ID 402, AuditConfigID 4.
Todo sale de SELECT.
[2026-09-14] - Captura de la grilla con la URL visible y el cursor en Coaching.
- Numero de la auditoria que usaste y la hora.
- El resultado del bloque 4 pegado como texto.
- Navegador y version.

## Que sigue
[2026-09-14] Confirmar con Hugo Cortez (o un usuario real con rol Manager) si el grid acepta input en su cuenta. Recien con eso se puede escribir el comentario formal en Jira. No se ha posteado nada a Jira, solo se le informo a J.R. en chat que la prueba manual de hoy no reprodujo el error en las pantallas documentadas, dejando explicito que falta cerrar el rol Manager antes de dar el caso por resuelto.
[2026-10-06] Primero el reintento en incognito y otro navegador (comentario ya redactado). Razones: el password existe y la cuenta no esta bloqueada, un reset no ataca el sintoma; RCS-28486 y RCS-28984 registran que un reset disparo el mismo Session Error; ya hay un reset a las 22:10:40 UTC y otro mas borra la evidencia de LastPasswordReset. El reset queda como opcion si incognito y otro navegador fallan y Engineering lo pide.

## Precedentes
[2026-09-14] - Comentario del 27 ago en Jira, pasos originales: inbox/2026-08-27-rcs-28223-comentario-interno.md
- Evidencia de la base: inbox/2026-08-27-rcs-28223-EVIDENCIA.md
- Consultas completas: inbox/2026-08-27-rcs-28223-plan-repro.sql
- Acceso al tenant: brain/memoria/project_juan_accesos.md
[2026-10-06] No hay flujo escrito para Session Error en flujos/INDICE.md, solo el de SecurityID (ya corrido). Lo que hay en el cerebro:
RCS-28676 y RCS-28294, Vallarta 31 ago: tras resetear password sale Session Error y en incognito si entran. Apunta a cookie de sesion y no a credenciales.
RCS-28984 (17 sep), paso 2: probar en otro navegador, limpiar cookies, copiar la URL completa, sin pedir un reset nuevo.
RCS-28486 McDonald's: reset forzado, segundo login entra.
RCS-29147 (Enrique): cerrar sesion en Secure y entrar una vez mas, si falla pasa a Engineering.
El comentario a Hugo ahora pide incognito y, si repite, otro navegador. La URL ya esta en su captura (apps.apprissretail.com/mcdonalds/nettrack/?id=L).

## Rastro
2026-08-27 inbox/2026-08-27-rcs-28223-EVIDENCIA.md
2026-08-27 inbox/2026-08-27-rcs-28223-causa-raiz.md
2026-08-27 inbox/2026-08-27-rcs-28223-consultas-parte2.md
2026-08-27 inbox/2026-08-27-rcs-28223-consultas-parte3.md
2026-08-27 inbox/2026-08-27-rcs-28223-consultas-parte4.md
2026-08-27 inbox/2026-08-27-rcs-28223-consultas.md
2026-08-27 inbox/2026-08-27-rcs-28223-continuidad-david-vargas.md
2026-08-27 inbox/2026-08-27-rcs-28223-esquema-audit.md
2026-08-27 inbox/2026-08-27-rcs-28223-hallazgos-pdf.md
2026-09-14 inbox/2026-09-14-rcs-28223-repro-paso-a-paso.md
2026-09-16 inbox/2026-09-16-rcs-28223-revision-cola.md
2026-09-24 inbox/2026-09-24-rcs-28223-seguimiento-ucr.md
2026-09-28 inbox/2026-09-28-rcs-28223-prioridad-auditoria.md
2026-09-29 inbox/2026-09-29-rcs-28223-password-nsn14283.md
2026-10-01 inbox/2026-10-01-rcs-28223-engineering-chat.md
2026-10-06 inbox/2026-10-06-rcs-28223-session-error-admin-hugo.md
2026-10-13 inbox/2026-10-13-rcs-28223-estado-cierre.md

## RCS-28351. Revisión integral, 28 septiembre 2026. Qué pasa Blain’s debe confirmar si ya puede adjuntar PDF al reporte — 2026-09-28
_chunk 1861 · 2026-09-28 · fuente: inbox/2026-09-16-rcs-28351-revision-cola.md;2026-09-24-rcs-28351-seguimiento-ucr.md;2026-09-28-rcs-28351-prioridad-auditoria.md_

Ticket RCS-28351. Trabajado el 2026-09-16 a 2026-09-28. 3 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Revisión integral, 28 septiembre 2026. Qué pasa Blain’s debe confirmar si ya puede adjuntar PDF al reporte. Causa Resolución todavía no confirmada por cliente; no cerrar por asumir que un fix antiguo funcionó. Evidencia https://trebuco.atlassian.net/browse/RCS-28351?focusedCommentId=3363510 Snapshot local:

## Rastro
2026-09-16 inbox/2026-09-16-rcs-28351-revision-cola.md
2026-09-24 inbox/2026-09-24-rcs-28351-seguimiento-ucr.md
2026-09-28 inbox/2026-09-28-rcs-28351-prioridad-auditoria.md

## RCS-28534. Angie escribio el 29 sep que es su problema mas importante: HR no recibe alertas posteriores al cierre y el ta — 2026-09-30
_chunk 1863 · 2026-09-30 · fuente: inbox/2026-09-30-confluence-smart-alerts-runbook.md;2026-09-30-rcs-28534-grafana-consultas.md;2026-09-30-rcs-28534-grafana-hallazgos.md;2026-09-30-rcs-28534-guia-llamada-diego.md;2026-09-30-rcs-28534.md_

Ticket RCS-28534. Trabajado el 2026-09-30. 5 notas en inbox.

## Que pasa
[2026-09-30] 205148 y 205157 son atascos reales, no filtro. Corrigen la nota anterior: el filtro de Discipline Request no mira CaseStatus, mira SUSPECT.DAYSOFFNOTES y CaseType.
[2026-09-30] Angie escribio el 29 sep que es su problema mas importante: HR no recibe alertas posteriores al cierre y el tab Smart Alerts del workbench sale vacio. Diego publico un RCA de 242 casos con InProcess = 1 y un segundo gatillo propio de Stater. Kiran respondio pidiendo evidencia de Grafana antes de hablar de fix, y asigno a Juan revisar con Diego y re disparar solo si hace falta.

## Evidencia
[2026-09-30] 205148, 24 sep: 15:51:53 6a Rows=1, 8, 8a, 11, 11d 15:52:03, 12b 15:52:04, sin 13a ni End. Quit desde 15:57 hasta 20:43.
205157, 24 sep: 19:31 6a Rows=0, DaysOffNotes vacio. 19:32 6a Rows=1, 8, 8a, 11, 11d, 12b 19:32:30, sin 13a. Quit 19:36.
Post fix: 13a y 13b pareados 99 de 100 desde 29 sep 16:56. Unico 13a sin 13b: 29 sep 23:10:37, Stater Bros. Investigation 129, 0 adjuntos.
HATR NettrackSmartAlertActivity 500: 17 veces el 28 sep entre 05:11 y 17:49, ninguna despues del deploy.
Quit desde 28 sep: 404 lineas, 200 IDs. 25 terminaron despues, 132 son un Quit suelto sin prueba, 35 empezaron antes del fix, 8 empezaron despues: 205264, 205376, 205356, 205296, 205378, 205462, 205158, 205171.
205367 y 205395: Quit desde antes del 29 sep, su corrida colgada es anterior. 205211 y 202901 sin lineas en la ventana.
[2026-09-30] Kiran, Jira 29 sep 19:34: SELECT CaseStatus en 205148, caso 2026-008-DISCIPLINE REQUEST-3, sale vacio. Igual en 205157.
RCA de Diego, Jira 29 sep 17:22: 98 casos post PR 58273, sin ninguna linea de Grafana.
Cerebro: inbox/2026-09-24-rcs-29103.md, RootCause 205157 = NULL.

## Que sigue
Nombres de columna de SmartAlertConfig en un tenant Cohesion. Ruta ProcessCaseAlert igual al slug. Ruta de menu en LPMS para buscar caso. Validar con RCS-29195.

## Precedentes
[2026-09-30] inbox/2026-09-28-smart-alerts-mecanismo-8-deadlock.md
inbox/2026-09-28-grafana-smart-alerts-lectura.md
[2026-09-30] Guia de disparo v2: flujos/smart-alert-disparo-manual.md
Lectura de Grafana: inbox/2026-09-28-grafana-smart-alerts-lectura.md
Mecanismo 8, deadlock PR 58273: inbox/2026-09-28-smart-alerts-mecanismo-8-deadlock.md
Metodo de Matt: inbox/2026-09-18-flujo-debug-smart-alerts-inprocess.md

## Rastro
2026-09-30 inbox/2026-09-30-confluence-smart-alerts-runbook.md
2026-09-30 inbox/2026-09-30-rcs-28534-grafana-consultas.md
2026-09-30 inbox/2026-09-30-rcs-28534-grafana-hallazgos.md
2026-09-30 inbox/2026-09-30-rcs-28534-guia-llamada-diego.md
2026-09-30 inbox/2026-09-30-rcs-28534.md

## RCS-28558. Tailored Brands, Colton Neal. No podia crear casos Recovery de tipo Cash, Gift Card o Perfect Fit Certificates — 2026-09-18
_chunk 1864 · 2026-09-18 · fuente: inbox/2026-09-16-rcs-28558-revision-cola.md;2026-09-18-rcs-28558.md_

Ticket RCS-28558. Trabajado el 2026-09-16 a 2026-09-18. 2 notas en inbox.

## Que pasa
Tailored Brands, Colton Neal. No podia crear casos Recovery de tipo Cash, Gift Card o Perfect Fit Certificates, la pantalla quedaba en blanco al dar Next. Resuelto. Colton confirmo el 17 de septiembre, Juan cerro el ticket ese mismo dia.

## Evidencia
Triage de Luis Hernandez, 27 ago, comentario 3314222. Predijo la causa exacta desde el codigo, Incident.vb linea 292, GenerateCaseNumber, sin acceso a base de datos.

Matthew Kamminga, 15 sep, comentario 3347215. Reprodujo, reviso Control Panel, Incident logs, encontro literal ERROR Case Number Not Defined. Configuro la pestaña Numbering del case type Recovery, el siguiente caso se creo, 2026-1-REC-217.

## Precedentes
Ninguno citado en el hilo. Vale la pena indexar el patron para la proxima vez que un tenant agregue un Incident Type nuevo, fila de numeracion faltante en CaseInc, pantalla en blanco por el bug del filtro de respuesta.

## Rastro
2026-09-16 inbox/2026-09-16-rcs-28558-revision-cola.md
2026-09-18 inbox/2026-09-18-rcs-28558.md

## RCS-28671. De los 17 WI borrados el 25 sep volvieron 2. 248159 de Ericka y 248160 no vuelven. RCS en Work in progress con — 2026-09-29
_chunk 1869 · 2026-09-29 · fuente: inbox/2026-08-31-rcs-28671-thd-searches-snowtime.md;2026-09-02-actualizaciones-cliente-thd-myer.md;2026-09-02-rcs-28671-lista-work-items-texto.md;2026-09-02-rcs-28671-snowflake-para-alguien-con-acceso.md;2026-09-02-rcs-28671-work-items-sin-transacciones.md;2026-09-04-rcs-28671-native-command-comparison.md;2026-09-07-verificacion-antes-de-d16.md;2026-09-21-RCS-28671-actualizacion.md;2026-09-22-THD-RCS-28_

Ticket RCS-28671. Trabajado el 2026-08-31 a 2026-09-29. 16 notas en inbox.

## Que pasa
De los 17 WI borrados el 25 sep volvieron 2. 248159 de Ericka y 248160 no vuelven. RCS en Work in progress con Juan, ENG-8659 Done. Notas internas pegadas 15:15 y 16:55, respuesta a Ericka 15:21, Teams a Mohammed enviado.

## Causa
[2026-09-02] `workview.WorkItemDefinitionGenerationRequest` trae `DeaggregationSql` en **NULL** en los 50 runs
mas recientes de markdowns. En THD esa columna no guarda nada. En Kinney Drugs si tenia contenido.
No se puede leer el SQL generado desde ahi.

Ademas `Failed = 0` y `DeaggregationRequestsCreated = 1` en los 50. La generacion nunca fallo.
[2026-09-22] Qué cambia: Hay contención comprobada entre búsquedas en secure_WH. No tenemos los warehouse, jobs, QueryIds e intervalos que conecten esa contención con el procesamiento del datafeed. Tampoco consta que Engineering esté investigando activamente ese vínculo específico.

Fuente: [RTS-207372](https://trebuco.atlassian.net/browse/RTS-207372?focusedCommentId=3337373); [RTS-207712](https://trebuco.atlassian.net/browse/RTS-207712?focusedCommentId=3348972).

## Evidencia
[2026-09-28] Cierto para la informacion. WISC, en Control Panel USPROD, lista cada Run con Total results, Generated, Duplicate, Failure y State. Ahi se ve si Mohammed corrio las 17 definiciones y que devolvio cada una. Juan tiene rol SupportL2 y Engineers, brain/memoria/project_juan_accesos.md.
Probable tambien para la regeneracion. Soporte ya relanza WI desde WISC: RCS-28170 TJX, Diego Buelvas, "re-run via the WISC Control Panel"; RCS-28352 Floor & Decor, "Manual Rerun" contra control/api/wisc/run. Precedentes de otros clientes, no un SOP escrito.
Lo unico que soporte no podia hacer era borrar WI. Eso ya lo hizo Mohammed. Lo que falta es un rerun por definicion y periodo.
[2026-09-28] 1. WISC run 92b446fe, 9/24, Success, 0 results.
2. Show Query del run, T4AsCte TradingDay BETWEEN 2026-09-23 AND 2026-09-24.
3. Snowflake ARDM_PRODUCTION.C085_THD, query en inbox/2026-09-28-rcs-28671-md03-query-ventana-0827.sql con ventana 27 ago: 2 filas.

## Impacto
Los originales ya estan borrados, asi que no hay WI previo que choque. El borrado quito la asignacion a DAPM Sean y las notas. El nuevo sale con la asignacion por defecto de la definicion.

## Que sigue
[2026-09-22] Qué cambia: El comentario público de Camila mezcla un arreglo de transacciones suspendidas con una corrección puntual de importes. Las cifras de 750 mil y 4% frente a 84% no prueban que Total Item Sale Amount haya quedado resuelto. El SOP prometido el 10 también necesita seguimiento.

Fuente: [Camila, 21 sep](https://trebuco.atlassian.net/browse/RCS-28968?focusedCommentId=3359117); [SOP pendiente, 10 sep](https://trebuco.atlassian.net/browse/RCS-28649?focusedCommentId=3337469).

Qué conservar o dónde evitar duplicación: Conserva DF B6. Ya atribuye los 11 días al reporte de Matthew previo al 17; no lo conviertas en conteo actualizado. A9:B11 están vacías en la copia revisada. Son adiciones, no reemplazos.
[2026-09-28] Nombres exactos de columnas y el flujo del boton New Run salen de la bitacora del 7 sep, no de un documento. Confirmalos en pantalla.

---
Lectura de WISC, 28 sep 14:29, capturas de Juan.
md03-cit-d periodo 2026/08/27, Run 92b446fe-85d1-4463-ac8f-03ee9acd1164. Queued 9/24 18:53:30 UTC, Ended 20:59:05. Success, 0 results, 0 gen. MD03 si se relanzo y la busqueda disparadora no devolvio ningun grupo.
com1 periodo 8/27, Run 8c9da172: 2 results, 1 gen, 1 dupe. Queued 9/25 21:41 UTC.
denver mkd2 periodo 8/27, Run f163cc7d: 1 result, 1 gen. Queued 9/25 21:20 UTC.
Failed en la ventana: snr4, sls1, ref3. Otra familia, rendimiento, no es de este ticket.
La vista recorta por cantidad de runs. Con To 28 sep el filtro md03 perdio el run del 9/24. Usa rangos cortos.
Conclusion: un New Run de md03-cit-d para 8/27 probablemente devuelve 0 otra vez. El bloqueo no es de permisos sino de que la busqueda no encuentra el grupo de 7135 y 7161 hoy.
Siguiente: Logs del run 92b446fe. Abrir el .fti y correr su busqueda en el Portal para 8/27, store 7135, cajero DXM6269.

Teams de seguimiento a Mohammed:
Hi Mohammed Mutahhar, one more data point on RCS-28671. In WISC, md03-cit-d for period 8/27 ran on 9/24 a

## Precedentes
[2026-09-02] RCS-28543, Kinney Drugs KNY/179, investigacion de Diego Buelvas publicada el 24 ago. **Es el mismo
defecto sobre Work Items, no sobre busquedas.** Sigue en Under Engineering Review.

Su root cause statement, textual:

> "WI stock count adjustments.fti (entity ADJUSTMENT, c179_kny/KNY). Step3 deaggregation SQL
> references physical column POS_ARTICLEID, which does not exist. SnowTime migration renamed the
> column to canonical ARTICLEID. Secure's Instant Analytics field metadata for entity ADJUSTMENT was
> never resynced."

Ahi el work item generaba 30 resultados y 3 fallaban en deaggregation. Aca el work item genera 3 IDs
y trae 0 transacciones.

El hallazgo de esa investigacion que responde la pregunta de Corey esta en su seccion 9, query 5.
Buscaron el nombre de la columna vieja en el Platform DB y lo encontraron aqui:

| Tabla | Columna | Coincidencias |
|---|---|---|
| stats.Search | NativeCommand | 6 |
| stats.Search | NativeCommandParameters | 6 |
| workview.WorkItemDefinitionGenerationRequest | DeaggregationSql | 487 |
| workview.WorkItemDefinitionGenerationRequest | DeaggregationNativeCommand | 582 |

**El SQL de deaggregacion queda persistido por work item.** Esa es la cla
[2026-09-28] inbox/2026-09-28-rcs-28671-wisc-soporte.md, proceso WISC y hallazgo.
Soporte relanza WI desde WISC: RCS-28170 TJX, confluence/RTS-triage/RCS-28170-tjx-no-work-items-populated.md.

## Rastro
2026-08-31 inbox/2026-08-31-rcs-28671-thd-searches-snowtime.md
2026-09-02 inbox/2026-09-02-actualizaciones-cliente-thd-myer.md
2026-09-02 inbox/2026-09-02-rcs-28671-lista-work-items-texto.md
2026-09-02 inbox/2026-09-02-rcs-28671-snowflake-para-alguien-con-acceso.md
2026-09-02 inbox/2026-09-02-rcs-28671-work-items-sin-transacciones.md
2026-09-04 inbox/2026-09-04-rcs-28671-native-command-comparison.md
2026-09-07 inbox/2026-09-07-verificacion-antes-de-d16.md
2026-09-21 inbox/2026-09-21-RCS-28671-actualizacion.md
2026-09-22 inbox/2026-09-22-THD-RCS-28671.md
2026-09-22 inbox/2026-09-22-THD-correcciones-excel.md
2026-09-28 inbox/2026-09-28-cerebro-guia-uso.md
2026-09-28 inbox/2026-09-28-rcs-28671-prioridad-auditoria.md
2026-09-28 inbox/2026-09-28-rcs-28671-sql-regenerados.md
2026-09-28 inbox/2026-09-28-rcs-28671-wisc-soporte.md
2026-09-28 inbox/2026-09-28-rcs-28671.md
2026-09-29 inbox/2026-09-29-rcs-28671-llamada-viraj.md

## RCS-28701. RCS-28701 es un ticket de configuración de IGEntryPage e IGIncidentReport para la organización JSD "DHL Global — 2026-09-21
_chunk 1873 · 2026-09-21 · fuente: inbox/2026-09-02-rcs-28701-informe.md;2026-09-02-rcs-28701-instructivo.md;2026-09-21-rcs-28701-clasificacion.md_

Ticket RCS-28701. Trabajado el 2026-09-02 a 2026-09-21. 3 notas en inbox.

## Que pasa
RCS-28701 es un ticket de configuración de IGEntryPage e IGIncidentReport para la organización JSD "DHL Global Mail" (id 72), abierto el 1 sep 2026 por Stephanie Kudla y asignado a Sebastian Garces. Afecta la configuración del caso Illegal Goods de ese cliente, sin relación con identidad de tenant. Ningún repositorio interno consultado, ni Cerebro ni Confluence ni Jira, confirma el número de cliente ni el slug de tenant de DHL Global Mail en Control Panel.

## Causa
El slug de tenant de DHL Global Mail es probablemente "dhl", tomado literalmente del encabezado "DHL (`dhl`)" en el runbook de Incident vs Audit. Esa cita no trae confirmación por URL, a diferencia de otros clientes en el mismo documento que sí la traen. El número de cliente numérico, equivalente al 15778 de Advance Auto Parts o al 110794 de Ralph Lauren, no aparece en ningún documento revisado. Marca esto como hipótesis, no como hecho verificado.

## Evidencia
Se leyó el ticket vivo con getJiraIssue, RCS-28701, estado Work in progress, asignado a Sebastian Garces desde el 1 sep 18:15. Se buscó en tickets, brain/markdown, investigaciones, bitacora y adjuntos de Cerebro por "DHL" vía subagente, sin resultado de número de cliente. Se corrió Rovo search y CQL contra Confluence y JQL contra Jira por "DHL Global Mail" y variantes con "client", "tenant", "control panel".

## Impacto
DHL Global Mail se maneja en RCS-28701 como caso Incident, LPMS, no Secure Audit. Los tres perfiles citados documentan el cliente del lado de Secure Audit, CAMS Mobile. Confirma en Control Panel que el tenant al que buscas impersonar para IGEntryPage e IGIncidentReport es el mismo DHL que aparece en esos perfiles, y no un tenant distinto bajo el mismo nombre. Otros clientes grandes del corpus, Walmart con client IDs 300, 301, 303, 308, 309, y Finish Line con client IDs 375 y 376, muestran que un mismo nombre comercial puede cubrir más de un tenant. No hay evidencia de que esto aplique a DHL Global Mail, pero tampoco hay evidencia de que no aplique.

## Que sigue
El dato no está resuelto en ninguna fuente interna consultada. La decisión es confirmarlo directo en Control Panel, y si el nombre no aparece igual a "DHL Global Mail", cruzarlo con el tracker Incident Migration 2026.xlsx que ya tienes localmente.

## Precedentes
Tres perfiles internos de DHL coinciden en el mismo vacío de dato, lo que sugiere que nadie lo ha confirmado todavía, no que el dato no exista:

Secure Audit (CAMS): Internal Setup & Configuration Runbook, https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478007787572
Incident (LPMS) vs Audit (CAMS): Setup Differences Side-by-Side, https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478022959110
Customer Escalation Handoffs -- Secure Audit & Legacy, https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478022139957
Runbook: DHL, https://trebuco.atlassian.net/wiki/spaces/RTS/pages/478007066660

## Rastro
2026-09-02 inbox/2026-09-02-rcs-28701-informe.md
2026-09-02 inbox/2026-09-02-rcs-28701-instructivo.md
2026-09-21 inbox/2026-09-21-rcs-28701-clasificacion.md

## RCS-28756. Nike respondio el 2026-09-11 via Akshaya que ellos no hacen push, que exponen un stream Kafka y Appriss se con — 2026-09-25
_chunk 1874 · 2026-09-25 · fuente: inbox/2026-09-04-rcs-28756-informe.md;2026-09-04-rcs-28756-instructivo.md;2026-09-09-instructivo-cierre-del-dia.md;2026-09-09-rcs-28756-chat-nichols.md;2026-09-09-rcs-28756-chat-peyman.md;2026-09-09-rcs-28756-fraseo-corte.md;2026-09-09-rcs-28756-instructivo.md;2026-09-09-rcs-28756.md;2026-09-10-rcs-28756.md;2026-09-11-rcs-28756-kafka-bridge.md;2026-09-15-rcs-28756-update-saddam.md;2026-09-16-rcs-28756-r_

Ticket RCS-28756. Trabajado el 2026-09-04 a 2026-09-25. 14 notas en inbox.

## Que pasa
[2026-09-10] Ayesha pidio tres veces hoy la informacion segura para el cliente. El ticket esta en Under Support
Review con Juan. La arquitectura ya esta documentada y las cinco respuestas estan listas.
[2026-09-11] Nike respondio el 2026-09-11 via Akshaya que ellos no hacen push, que exponen un
stream Kafka y Appriss se conecta a consumirlo. Copiaron a un arquitecto suyo.
Piden logs o errores de conexion de nuestro lado.

Eso contradice la respuesta que Ayesha ya envio a Nike el 2026-09-10, donde le
dijimos que no hay consumer de Appriss, que no es Kafka y que ellos publican a
nuestra Ingestion API. Los puntos 1, 2 y 3 de esa respuesta estan mal.

## Causa
Marco esto como HIPOTESIS, no como causa raiz confirmada. Nike dejo de enviar archivos
ECOM/raw_order a partir del 28 de agosto de 2026. La sostienen tres puntos independientes: la
ausencia de archivos nuevos despues del 27 de agosto a las 19:02 UTC, la confirmacion de Carl de
que los servicios de ingesta de Appriss estan arriba, y la ejecucion limpia del pipeline ARDM para
cliente 067 en la ventana revisada por Juan. Ningun log revisado muestra una falla de Appriss que
explique el corte. Nike no ha confirmado la causa de su lado a la fecha de este informe.

## Evidencia
[2026-09-10] Confluence PD 477499490306, Ingestion API - EventHub, Carl Costelow: "Customers POST data to the
API, which routes it into Azure Event Hub (small payloads) or Azure Blob Storage". El hub se nombra
solo como c{customerID}_rawdata_{dataType}, de ahi c67_rawdata_order.
Tres validaciones inbound: nombre de cliente 400/10, identidad contra ClientID y ClientScope 401/12,
dataType permitido 400/11.
Incoming Messages y Captured Messages de c67_rawdata_order en cero desde 2026-08-27 19:02 UTC.
[2026-09-11] - ENG-4235, descripcion completa, lineas 573, 541 y 457 de kafka_ingestion/nike.py
- Event Hub prd-datacloud-wus2-ehub-1, entidad c67_rawdata_order, Incoming y
  Captured en cero desde 2026-08-27 19:02 UTC
- Correo de Nike del 2026-09-11 en RCS-28756, arquitecto de Nike en copia

## Impacto
Los Work Items del control GNG para Nike/67 quedan en pausa desde el 1 de septiembre por conteo
bajo el minimo de 560392 transacciones. Eso incluye definiciones de auditoria de descuentos no
autorizados y de fraude en devoluciones, segun el listado de Ayesha Mehar del 3 de septiembre. Cada
dia adicional sin archivos ECOM ensancha la brecha de datos y retrasa esos controles de manera
acumulativa, no puntual.

## Que sigue
La decision pendiente no es tecnica, es de estado del ticket. RCS-28756 sigue en Under Support
Review desde el 3 de septiembre pese a que la investigacion de soporte esta cerrada y lo unico
pendiente es la respuesta de Nike, ya agendada para el 8 de septiembre via RTS-206999. Dejarlo en
Under Support Review dos dias mas dice, para quien mire la cola, que falta trabajo de Appriss.
No es el caso. La transicion a Under Customer Review documenta con precision donde esta el bloqueo
real. El instructivo trae el comentario y la transicion listos para pegar.

## Precedentes
[2026-09-10] investigaciones/ingestion-api-como-entra-la-data.md. Flujo completo y criterio de que compartir.
RCS-28753. Peyman compartio nombres de campos y feeds con Nike, no codigo. Mismo criterio.
tickets/RTS-206999.md. Canal con Nike.
[2026-09-11] - ENG-4235, mismo servicio, 2 fallas Sev0 de health check en prd, 8 y 10 de abril
- Peyman confirmo el 2026-09-09 que hay una API de Appriss entre Nike y el blob.
  Iba en la direccion correcta, la cadena tiene una pieza mas arriba
- AR Gateway normaliza ingesta por REST, Kafka o colas al formato de landing,
  brain/markdown/14-appriss-ingenieria-docs-fuente.md

## Rastro
2026-09-04 inbox/2026-09-04-rcs-28756-informe.md
2026-09-04 inbox/2026-09-04-rcs-28756-instructivo.md
2026-09-09 inbox/2026-09-09-instructivo-cierre-del-dia.md
2026-09-09 inbox/2026-09-09-rcs-28756-chat-nichols.md
2026-09-09 inbox/2026-09-09-rcs-28756-chat-peyman.md
2026-09-09 inbox/2026-09-09-rcs-28756-fraseo-corte.md
2026-09-09 inbox/2026-09-09-rcs-28756-instructivo.md
2026-09-09 inbox/2026-09-09-rcs-28756.md
2026-09-10 inbox/2026-09-10-rcs-28756.md
2026-09-11 inbox/2026-09-11-rcs-28756-kafka-bridge.md
2026-09-15 inbox/2026-09-15-rcs-28756-update-saddam.md
2026-09-16 inbox/2026-09-16-rcs-28756-revision-cola.md
2026-09-24 inbox/2026-09-24-rcs-28756-auditoria-avance.md
2026-09-25 inbox/2026-09-25-rcs-28756-revision-cola.md

## RCS-28872. Guess perdio la vista Izenda AMQComment y dos reportes (Audit Tabular Grid Comments, Area 999) tras migrar a a — 2026-10-07
_chunk 1878 · 2026-10-07 · fuente: inbox/2026-09-17-rcs-28872-amqcomment-vista.md;2026-10-07-rcs-28872.md_

Ticket RCS-28872. Trabajado el 2026-09-17 a 2026-10-07. 2 notas en inbox.

## Que pasa
[2026-09-17] Guess reporta en RCS-28872 que la vista AMQComment y los dos reportes de Izenda que la usan,
Test Reports Audit Tabular Grid Comments e Inventory Reports Area 999, desaparecieron tras la
migracion del tenant a la nueva URL apps.apprissretail.com/guess/signin. Piden reponerlos.
Ticket Incident, prioridad Low, asignado a Enrique Jimenez desde el 11 sep 2026.
[2026-10-07] Guess perdio la vista Izenda AMQComment y dos reportes (Audit Tabular Grid Comments, Area 999) tras migrar a apps.apprissretail.com/guess/signin. Estado Work in progress, Low, assignee Enrique Jimenez, reporter Stephanie Benedetti. Kiran Vadday (Teams, 7 oct) dice que el script debe ir por deployment en code changes y pregunta si el cliente corre en modo PU.

## Evidencia
[2026-09-17] RCS-15815, Guess Inc, SOW Estimation, cerrado el 5 ago 2024. Louis Marchand y Ryan Barlow,
ambos Engineering, escriben y prueban el script en dos iteraciones. La version final la corre
Louis Marchand en produccion Guess US el 24 jul 2024 y en produccion GuessEU el 26 jul 2024. Se
factura como SOW, 15 horas. El script que trae Juan es identico caracter por caracter a esa
version final, copiada del comentario de Ryan Barlow del 26 jul 2024.
[2026-10-07] 1. Jira RCS-28872, comentarios 3358862 (21 sep): vista dejada en la migracion, schema dbo a incident.
2. inbox/2026-09-17-rcs-28872-amqcomment-vista.md: script identico al de Ryan Barlow del 26 jul 2024, es DDL.
3. Lunar, db:knowledge_chunks/305: cambios de schema por EF Core migrations, Programmability solo para SP y funciones.

## Precedentes
[2026-09-17] RCS-15815, ruta completa del script y del despliegue, resuelto el 5 ago 2024.
[2026-10-07] RCS-15815 Guess, script y despliegue por Engineering (Louis Marchand), US 24 jul 2024, EU 26 jul 2024.
RCS-27598 Guess, Izenda PC mode, inbox/2026-09-01-dossier-alo-yoga.md.

## Rastro
2026-09-17 inbox/2026-09-17-rcs-28872-amqcomment-vista.md
2026-10-07 inbox/2026-10-07-rcs-28872.md

## RCS-28984. Scott Harbin, Skechers (scotth@skechers.com), no puede entrar al sitio. Recibe "Session Error, Your Incident s — 2026-09-28
_chunk 1885 · 2026-09-28 · fuente: inbox/2026-09-17-rcs-28984.md;2026-09-28-rcs-28984-prioridad-auditoria.md_

Ticket RCS-28984. Trabajado el 2026-09-17 a 2026-09-28. 2 notas en inbox.

## Que pasa
Scott Harbin, Skechers (scotth@skechers.com), no puede entrar al sitio. Recibe "Session Error,
Your Incident session could not be established" y el sistema le pide volver al portal Secure y
loguearse de nuevo. Under Support Review, prioridad High, asignado a Juan.

## Evidencia
- tickets/RCS-28486.md, cita: "Session Error. Your Incident session could not be established.
  This is usually caused by a temporary account configuration issue." Texto identico al de Scott.
- Dave Abril en RCS-28486, 20 ago: reset post unificacion, segundo login entra directo.
- Jira RCS-28321, Kiran Vadday, 24 ago: "I do not believe this is a code issue."

## Precedentes
- RCS-28486 McDonald's, mismo texto de error, resuelto con segundo login post reset.
- RCS-28321 Boot Barn, hipotesis de Options table descartada, causa real ajena al login.

## Rastro
2026-09-17 inbox/2026-09-17-rcs-28984.md
2026-09-28 inbox/2026-09-28-rcs-28984-prioridad-auditoria.md

## RCS-29058. RCS-29058. Apoyo a reunión 3Sixty — 2026-09-25
_chunk 1898 · 2026-09-25 · fuente: inbox/2026-09-25-rcs-29058-apoyo-meet.md_

Ticket RCS-29058. Trabajado el 2026-09-25. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Actualización interna compartida por Juan el 25/09: Sebastián sospecha caché, informa limpieza y solicitud ya enviada de probar incógnito u otro navegador. Falta respuesta del cliente. Hipótesis, no causa confirmada.

## Rastro
2026-09-25 inbox/2026-09-25-rcs-29058-apoyo-meet.md

## RCS-29127. RCS-29127: segundo candidato — 2026-09-25
_chunk 1906 · 2026-09-25 · fuente: inbox/2026-09-25-rcs-29127-evaluacion.md_

Ticket RCS-29127. Trabajado el 2026-09-25. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
PSEB/PacSun solicita ranking de devoluciones con tarjeta por monto y cantidad, igual al CASH existente. Under Support Review, sin asignar, verificado 25 sep. petición de variante de reporte. Hipótesis de solución por configuración; definición del tenant y cobertura de campos pendientes.

## Rastro
2026-09-25 inbox/2026-09-25-rcs-29127-evaluacion.md

## RTS-207372. Verificado en Jira el 21 sep 2026. Closed, resolución Resolved, Rajith Suvarna — 2026-09-21
_chunk 1935 · 2026-09-21 · fuente: inbox/2026-09-21-RTS-207372-actualizacion.md_

Ticket RTS-207372. Trabajado el 2026-09-21. 1 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Verificado en Jira el 21 sep 2026. Closed, resolución Resolved, Rajith Suvarna. 10 sep, 12:21 EDT, confirma que la alerta despejó tras cancelar consultas. evidencia operativa de consultas largas de work items de THD en secure_WH, otras consultas en cola y timeouts multicliente.

## Rastro
2026-09-21 inbox/2026-09-21-RTS-207372-actualizacion.md

## UO excel client update — 2026-09-17
_chunk 1941 · 2026-09-17 · fuente: inbox/2026-09-17-UO-excel-client-update.md_

Target: Long-term solutions, row 5. Replace C5:H5 only.

Completed in the shared workbook on 17 September 2026. Verified by downloading the saved workbook and reading C5:H5 from /Users/MancoMenStudio/Downloads/Urban Outfitters - Ticket Review Aug 2026 (1).xlsx. No comments, links, local paths, PR references, or internal investigation notes were added to the workbook.

C5 Root Cause Summary
Review identified two separate failure modes. The missing customer name and account number fields were caused by an incorrect field type in the search configuration. That configuration was corrected. The zero-row export is a different symptom: the on-screen search returned results while the background export reported zero. The available evidence does not confirm a caching or session issue, and further reproduction is required to isolate that path.

D5 Fix Type(s)
Configuration validation
Engineering / Product
Quality assurance

E5 Recommended Long-Term Action
Add automated validation for search field types before configuration changes are released. Add end-to-end regression tests that compare on-screen results with the exported file, including text identifiers, customer names, blank values, standard export, and export all. For zero-row exports, improve diagnostics so each export records the search version, filters, user context, processing status, and row counts. Reproduce the reported scenario with the same saved search and filters, then use that evidence to determine whether an additional product change is required.

F5 Owner
Engineering / Product / QA

G5 Priority & Rationale
Medium-High. The known missing-field configuration was corrected. Preventive validation and stronger export diagnostics are needed to reduce recurrence and shorten resolution time if the zero-row symptom returns.

H5 Update
Configuration correction completed for the missing fields. Next steps are preventive validation, regression coverage, and targeted reproduction of the zero-row export.


## Rastro
2026-09-17 inbox/2026-09-17-UO-excel-client-update.md

## facteus resumen llamada l1 — 2026-10-07
_chunk 1969 · 2026-10-07 · fuente: inbox/2026-10-07-facteus-resumen-llamada-l1.md_

Facteus, qué salió en la llamada de hoy con L1, aparte de lo que ya hablamos

Fecha 2026-10-07. Transcripción completa en Facteus_L1_L2.docx, 20 minutos, Viraj liderando con Santhosh, Shreyas Udupa y un tercer participante de L1.

Qué quedó resuelto en la llamada misma

Viraj sí contestó en vivo la pregunta de si L1 escala primero a L2, dijo que por ahora sí, L1 monitorea y cuando hay algo, lo manda a L2, y L2 maneja la comunicación y la asignación del ticket. No esperó a resolverlo por fuera como habíamos hablado, lo decidió ahí mismo. Vale la pena que lo sepas para no contradecirlo después.

Sobre prioridad, Viraj dijo que es P1 si no llega la data, P3 todo lo demás. No quedó claro si esto lo sacó de la documentación o lo está asumiendo, hay que confirmarlo con Chris.

La pregunta de Data Issues quedó igual que te la pasé, se postea ahí por ahora, pero ni Viraj sabe si el canal correcto se llama Data Issues o Data Engineering Alerts, queda como pregunta abierta para Chris o Sadam.

Dato nuevo, son 31 clientes los que cubre esta alerta.

Preguntas nuevas que salieron hoy, para sumar a la lista de Chris y Sadam

L1 pidió, por boca de Shreyas, un artículo por cada tipo de alerta, que diga cómo confirmar que la alerta es real, qué herramienta de monitoreo revisar, si L1 puede resolverlo o debe escalar, a quién, en qué tiempo, con qué frecuencia de seguimiento y qué SLA aplica. Hoy no existe esto, es una pieza de documentación completa que falta.

Si un cliente lleva uno o dos días sin enviar datos, al notificar, ¿se debe decir qué cliente es o solo que hay un problema sin nombrarlo? Viraj no supo contestar, dijo que lo iba a preguntar con Sadam o Chris.

Falta un punto de contacto específico para escalar a Data Engineering, no solo "el equipo". Viraj dijo que lo pregunta por el mismo hilo de correo.

No está claro en qué canal de Teams caen las alertas internas, si es Data Engineering Alerts u otro, y L1 no tiene acceso a ese canal hoy.

Sobre el go-live, alguien de L1 preguntó cuándo arranca esto en serio. Viraj dijo que la documentación menciona fin de septiembre, pero no ha llegado ningún ticket RCS o RTS todavía, así que está atrasado.

Acceso, hilo aparte

Esto es nuevo y separado de lo que ya trámitó Viraj con IT para PRODDATACLOUD.FACTEUS_CONFIG, PRODDATACLOUD.FACTEUS y FACTEUS_DATASHARE. Ahora Viraj pidió a Santhosh la lista completa del equipo L1 para abrir acceso de lectura a las tablas ARDM, que son otras. Santhosh ya le mandó esa lista por correo, Viraj dijo que la revisa.

Qué hacer con todo esto

Son cinco preguntas nuevas más la del drop_ratio que ya veníamos arrastrando desde el 22 de septiembre, todas para Chris y Sadam. Si quieres, armo el correo consolidado con las seis cuando tengas tiempo de revisarlo, mejor mandarlas juntas que una por una.


## Rastro
2026-10-07 inbox/2026-10-07-facteus-resumen-llamada-l1.md

## facteus revision faq chris — 2026-10-07
_chunk 1970 · 2026-10-07 · fuente: inbox/2026-10-07-facteus-revision-faq-chris.md_

Facteus, revisión del FAQ que armó Chris

Fecha 2026-10-07. Página: https://trebuco.atlassian.net/wiki/spaces/DS/pages/478282350598/Facteus+-+Support+FAQs. Contestó todo, incluido lo que pensábamos que seguía abierto.

El umbral de drop_ratio, resuelto. Chris dice que drop_ratio es solo informativo, no dispara nada. Lo que de verdad dispara la alerta es una ventana de 24 horas, revisando si llegó dato nuevo según _row_created en la tabla ARDM_Header. Ojo con un detalle menor, la página de Missing Clients habla de 26 horas y Chris ahora dice 24, no es grave pero vale la pena señalarlo como pregunta abierta, no como corrección, por si cambiaron el valor y no actualizaron la página vieja.

El artículo por tipo de alerta que pedía Shreyas, resuelto. Hay un documento central con todos los tipos de alerta y sus guías, cada una con sus pasos de triage, enlace https://trebuco.atlassian.net/wiki/x/A4AbUW8. La regla general que dio Chris, si se disparó la alerta hay que asumir que hay un problema real, y si una alerta genera puro ruido, se desactiva y se rediseña, eso también se escala a Data Engineering.

Nombrar o no al cliente, resuelto, y es una regla clara. Nunca mencionar nombres de clientes hablando con Facteus, los datos van ofuscados en ese feed. El único nombre que se menciona es el de Facteus mismo. Hay plantillas ya armadas en cada guía para esto.

Si la alerta se dispara cuando el problema es del cliente, resuelto. Sí se dispara. Si faltan varios clientes a la vez, se agrupan en un solo ticket en vez de uno por cliente. La responsabilidad ahí es notificar al cliente directamente, aparte de escalar a Data Engineering, eso no contradice la regla anterior, esa regla es sobre no nombrar clientes frente a Facteus, no sobre no contactar al cliente mismo.

Punto de contacto para escalar, canal, fin de semana y go-live, todo igual a lo que ya tenías, sin cambios frente a lo que te mandé antes.

Lo único que sigue sin resolver, son cosas nuestras, no de Chris

Levantar el ticket de helpdesk para crear el Product Type de Facteus en Jira, sigue sin hacerse, y sigue sin estar claro si lo hace Camila o Support directamente.

Decidir si Support ya está listo para aprobar que Facteus escriba directo al support desk, eso prende el go-live de External Alerts y depende solo de ustedes.


## Rastro
2026-10-07 inbox/2026-10-07-facteus-revision-faq-chris.md

## RCS-28671. De los 17 WI borrados el 25 sep volvieron 2. 248159 de Ericka y 248160 no vuelven. RCS en Work in progress con — 2026-10-14
_chunk 1982 · 2026-10-14 · fuente: inbox/2026-08-31-rcs-28671-thd-searches-snowtime.md;2026-09-02-actualizaciones-cliente-thd-myer.md;2026-09-02-rcs-28671-lista-work-items-texto.md;2026-09-02-rcs-28671-snowflake-para-alguien-con-acceso.md;2026-09-02-rcs-28671-work-items-sin-transacciones.md;2026-09-04-rcs-28671-native-command-comparison.md;2026-09-07-verificacion-antes-de-d16.md;2026-09-21-RCS-28671-actualizacion.md;2026-09-22-THD-RCS-28_

Ticket RCS-28671. Trabajado el 2026-08-31 a 2026-10-14. 17 notas en inbox.

## Que pasa
De los 17 WI borrados el 25 sep volvieron 2. 248159 de Ericka y 248160 no vuelven. RCS en Work in progress con Juan, ENG-8659 Done. Notas internas pegadas 15:15 y 16:55, respuesta a Ericka 15:21, Teams a Mohammed enviado.

## Causa
[2026-09-02] `workview.WorkItemDefinitionGenerationRequest` trae `DeaggregationSql` en **NULL** en los 50 runs
mas recientes de markdowns. En THD esa columna no guarda nada. En Kinney Drugs si tenia contenido.
No se puede leer el SQL generado desde ahi.

Ademas `Failed = 0` y `DeaggregationRequestsCreated = 1` en los 50. La generacion nunca fallo.
[2026-09-22] Qué cambia: Hay contención comprobada entre búsquedas en secure_WH. No tenemos los warehouse, jobs, QueryIds e intervalos que conecten esa contención con el procesamiento del datafeed. Tampoco consta que Engineering esté investigando activamente ese vínculo específico.

Fuente: [RTS-207372](https://trebuco.atlassian.net/browse/RTS-207372?focusedCommentId=3337373); [RTS-207712](https://trebuco.atlassian.net/browse/RTS-207712?focusedCommentId=3348972).

## Evidencia
[2026-09-28] Cierto para la informacion. WISC, en Control Panel USPROD, lista cada Run con Total results, Generated, Duplicate, Failure y State. Ahi se ve si Mohammed corrio las 17 definiciones y que devolvio cada una. Juan tiene rol SupportL2 y Engineers, brain/memoria/project_juan_accesos.md.
Probable tambien para la regeneracion. Soporte ya relanza WI desde WISC: RCS-28170 TJX, Diego Buelvas, "re-run via the WISC Control Panel"; RCS-28352 Floor & Decor, "Manual Rerun" contra control/api/wisc/run. Precedentes de otros clientes, no un SOP escrito.
Lo unico que soporte no podia hacer era borrar WI. Eso ya lo hizo Mohammed. Lo que falta es un rerun por definicion y periodo.
[2026-09-28] 1. WISC run 92b446fe, 9/24, Success, 0 results.
2. Show Query del run, T4AsCte TradingDay BETWEEN 2026-09-23 AND 2026-09-24.
3. Snowflake ARDM_PRODUCTION.C085_THD, query en inbox/2026-09-28-rcs-28671-md03-query-ventana-0827.sql con ventana 27 ago: 2 filas.

## Impacto
Los originales ya estan borrados, asi que no hay WI previo que choque. El borrado quito la asignacion a DAPM Sean y las notas. El nuevo sale con la asignacion por defecto de la definicion.

## Que sigue
[2026-09-22] Qué cambia: El comentario público de Camila mezcla un arreglo de transacciones suspendidas con una corrección puntual de importes. Las cifras de 750 mil y 4% frente a 84% no prueban que Total Item Sale Amount haya quedado resuelto. El SOP prometido el 10 también necesita seguimiento.

Fuente: [Camila, 21 sep](https://trebuco.atlassian.net/browse/RCS-28968?focusedCommentId=3359117); [SOP pendiente, 10 sep](https://trebuco.atlassian.net/browse/RCS-28649?focusedCommentId=3337469).

Qué conservar o dónde evitar duplicación: Conserva DF B6. Ya atribuye los 11 días al reporte de Matthew previo al 17; no lo conviertas en conteo actualizado. A9:B11 están vacías en la copia revisada. Son adiciones, no reemplazos.
[2026-09-28] Nombres exactos de columnas y el flujo del boton New Run salen de la bitacora del 7 sep, no de un documento. Confirmalos en pantalla.

---
Lectura de WISC, 28 sep 14:29, capturas de Juan.
md03-cit-d periodo 2026/08/27, Run 92b446fe-85d1-4463-ac8f-03ee9acd1164. Queued 9/24 18:53:30 UTC, Ended 20:59:05. Success, 0 results, 0 gen. MD03 si se relanzo y la busqueda disparadora no devolvio ningun grupo.
com1 periodo 8/27, Run 8c9da172: 2 results, 1 gen, 1 dupe. Queued 9/25 21:41 UTC.
denver mkd2 periodo 8/27, Run f163cc7d: 1 result, 1 gen. Queued 9/25 21:20 UTC.
Failed en la ventana: snr4, sls1, ref3. Otra familia, rendimiento, no es de este ticket.
La vista recorta por cantidad de runs. Con To 28 sep el filtro md03 perdio el run del 9/24. Usa rangos cortos.
Conclusion: un New Run de md03-cit-d para 8/27 probablemente devuelve 0 otra vez. El bloqueo no es de permisos sino de que la busqueda no encuentra el grupo de 7135 y 7161 hoy.
Siguiente: Logs del run 92b446fe. Abrir el .fti y correr su busqueda en el Portal para 8/27, store 7135, cajero DXM6269.

Teams de seguimiento a Mohammed:
Hi Mohammed Mutahhar, one more data point on RCS-28671. In WISC, md03-cit-d for period 8/27 ran on 9/24 a

## Precedentes
[2026-09-02] RCS-28543, Kinney Drugs KNY/179, investigacion de Diego Buelvas publicada el 24 ago. **Es el mismo
defecto sobre Work Items, no sobre busquedas.** Sigue en Under Engineering Review.

Su root cause statement, textual:

> "WI stock count adjustments.fti (entity ADJUSTMENT, c179_kny/KNY). Step3 deaggregation SQL
> references physical column POS_ARTICLEID, which does not exist. SnowTime migration renamed the
> column to canonical ARTICLEID. Secure's Instant Analytics field metadata for entity ADJUSTMENT was
> never resynced."

Ahi el work item generaba 30 resultados y 3 fallaban en deaggregation. Aca el work item genera 3 IDs
y trae 0 transacciones.

El hallazgo de esa investigacion que responde la pregunta de Corey esta en su seccion 9, query 5.
Buscaron el nombre de la columna vieja en el Platform DB y lo encontraron aqui:

| Tabla | Columna | Coincidencias |
|---|---|---|
| stats.Search | NativeCommand | 6 |
| stats.Search | NativeCommandParameters | 6 |
| workview.WorkItemDefinitionGenerationRequest | DeaggregationSql | 487 |
| workview.WorkItemDefinitionGenerationRequest | DeaggregationNativeCommand | 582 |

**El SQL de deaggregacion queda persistido por work item.** Esa es la cla
[2026-09-28] inbox/2026-09-28-rcs-28671-wisc-soporte.md, proceso WISC y hallazgo.
Soporte relanza WI desde WISC: RCS-28170 TJX, confluence/RTS-triage/RCS-28170-tjx-no-work-items-populated.md.

## Rastro
2026-08-31 inbox/2026-08-31-rcs-28671-thd-searches-snowtime.md
2026-09-02 inbox/2026-09-02-actualizaciones-cliente-thd-myer.md
2026-09-02 inbox/2026-09-02-rcs-28671-lista-work-items-texto.md
2026-09-02 inbox/2026-09-02-rcs-28671-snowflake-para-alguien-con-acceso.md
2026-09-02 inbox/2026-09-02-rcs-28671-work-items-sin-transacciones.md
2026-09-04 inbox/2026-09-04-rcs-28671-native-command-comparison.md
2026-09-07 inbox/2026-09-07-verificacion-antes-de-d16.md
2026-09-21 inbox/2026-09-21-RCS-28671-actualizacion.md
2026-09-22 inbox/2026-09-22-THD-RCS-28671.md
2026-09-22 inbox/2026-09-22-THD-correcciones-excel.md
2026-09-28 inbox/2026-09-28-cerebro-guia-uso.md
2026-09-28 inbox/2026-09-28-rcs-28671-prioridad-auditoria.md
2026-09-28 inbox/2026-09-28-rcs-28671-sql-regenerados.md
2026-09-28 inbox/2026-09-28-rcs-28671-wisc-soporte.md
2026-09-28 inbox/2026-09-28-rcs-28671.md
2026-09-29 inbox/2026-09-29-rcs-28671-llamada-viraj.md
2026-10-14 inbox/2026-10-14-acceso-cerebro-otra-ai-consola.md

## RCS-29445. TBI: orden de ejecución después de la llamada — 2026-10-16
_chunk 2027 · 2026-10-16 · fuente: inbox/2026-10-16-rcs-29445-guion-llamada-v2.md;2026-10-16-rcs-29445-guion-llamada-v3.md;2026-10-16-rcs-29445-guion-llamada-v4.md;2026-10-16-rcs-29445-guion-llamada.md;2026-10-16-tbi-auditoria-cierre-operativo.md;2026-10-16-tbi-cierre-del-dia.md;2026-10-16-tbi-paso-a-paso-post-llamada.md_

Ticket RCS-29445. Trabajado el 2026-10-16. 7 notas en inbox.

## Evidencia
1. Abre [RCS-29445](https://trebuco.atlassian.net/browse/RCS-29445). La consulta actual: Work in progress, Vedant Shirude, prioridad Medium. La prioridad verbal del cliente no cambió automáticamente ese campo.
2. Coordina con Vedant el traspaso que pidió J.R. Usa la nota preparada en ese ticket como comentario interno. Es la nota de rendimiento, no la de accesos.
3. La nota ampliada contiene la evidencia necesaria. El anexo técnico queda disponible si el investigador pide más detalle. Las capturas originales están en [RCS-29060, reporte del 14 octubre](https://trebuco.atlassian.net/browse/RCS-29060?focusedCommentId=3396117) y están enlazadas en la nota. RCS-29445 no tiene adjuntos propios; conserva esos enlaces y, si incorporas copias, usa los archivos originales, no solo la miniatura del guion.
4. Avisa al cliente del traslado con un update breve antes de moverlo. No prometas una fecha de solución ni copies las hipótesis del anexo. La guía de escalación exige ese aviso. No redacté una respuesta al cliente adicional porque pediste las notas internas.
5. En el menú de estado, la transición comprobada es Waiting for Engineering. El estado de llegada es Under Engineering Review. No so

## Que sigue
[2026-10-16] 16 octubre 2026. Juan indica que esta validación ya se hizo. No repetir la revisión de estructura, CSV, teams, nivel y cuenta. No hay resultado adicional antes/después de un login real registrado en los datos compartidos; no inferir que una prueba nueva corrigió las cuentas ni pedirla de nuevo por rutina.

Completado: lista de tickets en el chat y respuesta a Matt, confirmadas por Juan sin consulta de Teams. RCS-29445 escalado a Shandana, nota interna y respuesta a Colton publicadas. RCS-29469 con nota de evidencia y respuesta pública publicadas. Archivos y 29 imágenes revisados. Datos de cinco cuentas y sso.teams recibidos. Definición actual de GetUserSecurityLevel leída.

Conclusión de datos: los cinco tienen cuenta con SecurityID NULL, team Location Manager y fila SSO+ nivel 5 del 15 octubre 10:34:36. Sus últimos logins preceden esa carga. Christi tiene además nivel 5 Persistent 1 de abril. El procedimiento filtra vigencia y prioriza Persistent; las filas aportadas son compatibles con resultado 5. No demuestra aplicación en una sesión posterior ni reconstruye el código de julio.

Pendiente hoy:
1. Confirmar con Shandana recepción, responsable técnico y próximo punto de actualiza
[2026-10-16] Shandana y Vedant: concretar RCS-29445, confirmar el ENG y el próximo update; obtener dueño de ENG-10069.
Matt: precisar la tabla donde observó carga del día 15 y cómo se aplica la expectativa de una fila por usuario cuando existen asignaciones manuales Persistent.
Ryan y responsable actual de SnowTime por identificar: seguir el lote de Chris y la regla SSU+2005 antes de decidir una corrección.

Texto listo para el chat que pidió J.R.: [Lista de los cuatro RCS en inglés](/Users/MancoMenStudio/Cerebro/inbox/2026-10-16-tbi-teams-lista-tickets-jr-v2.md). Borrador, no publicado.

Verificación de borradores: las dos notas internas y la lista de Teams pasaron verificar_borrador destino interno sin bloqueantes. La alerta sobre otros reportes de RCS-29445 se contrastó con la descripción vigente y el comentario 3396117 de RCS-29060, leídos en Jira en esta preparación. No se publicó ningún texto.

## Rastro
2026-10-16 inbox/2026-10-16-rcs-29445-guion-llamada-v2.md
2026-10-16 inbox/2026-10-16-rcs-29445-guion-llamada-v3.md
2026-10-16 inbox/2026-10-16-rcs-29445-guion-llamada-v4.md
2026-10-16 inbox/2026-10-16-rcs-29445-guion-llamada.md
2026-10-16 inbox/2026-10-16-tbi-auditoria-cierre-operativo.md
2026-10-16 inbox/2026-10-16-tbi-cierre-del-dia.md
2026-10-16 inbox/2026-10-16-tbi-paso-a-paso-post-llamada.md

## RCS-29469. Explicación escrita de Matt en el chat, aportada por Juan — 2026-10-16
_chunk 2035 · 2026-10-16 · fuente: inbox/2026-10-16-rcs-29469-analisis.md;2026-10-16-rcs-29469-validacion-primer-paso.md;2026-10-16-rcs-29469-validacion-resolucion-resultado.md;2026-10-16-tbi-matt-proceso-sso-confirmado.md_

Ticket RCS-29469. Trabajado el 2026-10-16. 4 notas en inbox.

Sin secciones reconocibles. Extracto de la nota mas reciente:
Juan confirma que Matt publicó el siguiente texto. No se dispone de enlace o identificador del mensaje. Es evidencia aportada por Juan, no lectura independiente del chat. ok, so SSO+ process works in this way.

## Rastro
2026-10-16 inbox/2026-10-16-rcs-29469-analisis.md
2026-10-16 inbox/2026-10-16-rcs-29469-validacion-primer-paso.md
2026-10-16 inbox/2026-10-16-rcs-29469-validacion-resolucion-resultado.md
2026-10-16 inbox/2026-10-16-tbi-matt-proceso-sso-confirmado.md

## RTS-207681. Fuente: PDF SnowTime_RCS_Root_Cause_Review.pdf, preparado por Adarsh Kumar con Sumeet Jain, 42 tickets RCS de — 2026-10-15
_chunk 2037 · 2026-10-15 · fuente: inbox/2026-10-15-snowtime-rcs-root-cause-review.md_

Ticket RTS-207681. Trabajado el 2026-10-15. 1 notas en inbox.

## Causa
Fuente: PDF SnowTime_RCS_Root_Cause_Review.pdf, preparado por Adarsh Kumar con Sumeet Jain, 42 tickets RCS de 15 clientes migrados, verificado contra Jira el 18 sep 2026. Compartido al equipo de Support el 15 oct 2026. Texto extraido del PDF, sin cambios.

SnowTime RCS Root Cause Review
42 RCS tickets across 15 migrated clients, collected from the SnowTime engineers and verified against Jira comments on 18 Sep 2026. 41 of 42 tickets
verified (RTS-207681 sits in a tenant we could not open). Two internal migration stories (AZO, DSG) are excluded because they are not support tickets.
Prepared by Adarsh Kumar for review with Sumeet Jain.

1. What is common across clients
Four patterns explain all 42 tickets. The first two are ours to prevent; the third needs the client; the fourth is not a SnowTime issue.
 Root cause              Tickets       What went wrong                                  How it was resolved                       What support can try next time
 pattern
 1. Migration            19 of 42      Logic that the legacy load (pyardm) had          dbt mapping or enrichment fix,            If a field is blank or a count is zero
 mapping gap-            ALA 7,        was not c

## Rastro
2026-10-15 inbox/2026-10-15-snowtime-rcs-root-cause-review.md

## tailored guion cliente v3 — 2026-10-16
_chunk 2047 · 2026-10-16 · fuente: inbox/2026-10-16-tailored-guion-cliente-v3.md_

OBSOLETO. Juan limitó el guion a problemas repetidos que siguen abiertos. Usar investigaciones/2026-10-16-tailored-guion-cliente-v4.md.

Guion externo bilingüe, versión 3. 16 octubre 2026.

Juan corrigió que la versión 2 preguntaba demasiado al cliente y no explicaba el estado del trabajo. Quedan reemplazados el guion de cliente v2 y sus 11 tarjetas. La versión 3 explica ajustes realizados, pendientes, por qué falta una resolución y próximo paso por cada ticket. Distingue antecedentes cerrados de problemas actuales. No afirma que exista desarrollo activo ni fecha de release.

Guion para la llamada: investigaciones/2026-10-16-tailored-guion-cliente-v3.md.
Tarjetas: inbox/2026-10-16-rcs-XXXXX-guion-llamada-v3.md.

Conserva lenguaje externo y omite tickets de Engineering, responsables internos, logs y conteos no publicados. Las acciones futuras se presentan como próximos pasos pendientes, no como trabajos ya ejecutados. El hecho de un ajuste manual no equivale a una corrección permanente.

Siguiente paso:
Appriss: concretar corrección y validación para accesos, rendimiento y reportes.
Participantes de la llamada: acordar la fecha del próximo update sin confundirla con fecha de resolución.


## Rastro
2026-10-16 inbox/2026-10-16-tailored-guion-cliente-v3.md

## tailored llamada acceso archivos y correccion — 2026-10-16
_chunk 2048 · 2026-10-16 · fuente: inbox/2026-10-16-tailored-llamada-acceso-archivos-y-correccion.md_

Tailored Brands. Actualización de llamada, 16 octubre 2026.

Fuente: captura codex-clipboard-d1d0ba0f-6347-4309-b3f8-9c9b1fad71c4.png y aclaración directa de Juan: no ha dicho las respuestas propuestas. Ningún guion generado demuestra compromiso verbal ni envío.

Nueva restricción confirmada por declaración de Colton
No tiene acceso directo a los archivos diarios; debe pedirlos a otra persona. Toda propuesta previa de pedirle comprobar o modificar el archivo por sí mismo queda inaplicable. Falta identificar al responsable con acceso. No se infiere su identidad ni permisos.

Continuación del relato
Colton dice que algunos usuarios logran entrar al reintentar; no sabe la causa y aclara que no revisó a todos. Es observación anecdótica, sin tiempos ni secuencia comprobada. No demuestra resolución automática, error del usuario ni retraso diseñado de 24 horas.

Colton retoma la ubicación hub 2005 y recuerda una discrepancia de ubicación o marca. Su explicación no prueba que el archivo original omita la marca. La captura anterior y la evidencia conocida distinguen valor recibido en la aplicación de archivo original. Origen de transformación pendiente.

Correos visibles en la hoja Emails
Jennifer Alba-Faust, 14 octubre 2026: reporta que Appriss no carga y muestra errores; no se ve mensaje de error preciso.
Johnny Hernandez, 14 septiembre 2026: reporta imposibilidad de ingresar después de escribir short name y contraseña; no se ve URL ni error detallado.
Nuri Ceylan aparece al final con fecha 8 septiembre; cuerpo fuera del encuadre. No se atribuye síntoma.

Estos correos no permiten asignar a todos la causa de Security ID vacío ni confundir carga lenta con autenticación.

Borradores afectados
Las respuestas anteriores continúan sin pronunciarse. El guion v4 no acredita nuevos compromisos. Las preguntas de archivo dirigidas directamente a Colton requieren reformularse hacia coordinación con quien sí tenga acceso. La consulta a Matt solicitada por J.R. permanece como acción pedida, no ejecutada.

Siguiente paso:
Appriss: rastrear el valor de ubicación y su transformación antes de atribuirlo al cliente.
Tailored Brands: identificar al responsable de los archivos, sin asumir que Colton pueda inspeccionarlos directamente.
Juan: conservar los ejemplos por usuario y distinguir autenticación, carga y permisos antes de agruparlos.


## Rastro
2026-10-16 inbox/2026-10-16-tailored-llamada-acceso-archivos-y-correccion.md

## tailored llamada duda segundo login — 2026-10-16
_chunk 2049 · 2026-10-16 · fuente: inbox/2026-10-16-tailored-llamada-duda-segundo-login.md_

Tailored Brands. Aclaración durante la llamada, 16 octubre 2026.

Fuente: captura codex-clipboard-32d322ba-a6b5-4bcb-87ed-af8ea7315f9b.png compartida por Juan.

Colton plantea como duda si en uno o dos casos el Security ID llegó al día siguiente o en un segundo login. También duda entre un problema de ruta de acceso y un comportamiento de la aplicación. No aporta tiempos comprobados ni confirma causa.

No invalida los borradores previos que distinguen llegada de datos y aplicación al ingresar. Refuerza que no se debe convertir segundo login o espera de 24 horas en solución confirmada. El uso esporádico de tiendas sigue siendo requisito de negocio.

ENGLISH
That distinction is important. As we clarified previously, once the correct assignment has reached the system, it should apply at the next SSO sign-in. There should not be an additional 24-hour wait triggered by that sign-in. We have not confirmed whether the examples you mentioned reflect delayed data arrival or a failure to apply an available assignment. We need to compare those timings and the sign-in path before attributing it to user error or recommending a second sign-in as the solution.

ESPAÑOL
Esa diferencia importa. Como aclaramos antes, una vez que la asignación correcta llegó al sistema, debería aplicarse en el siguiente ingreso por SSO. Ese ingreso no debería iniciar otra espera de 24 horas. Todavía no confirmamos si los ejemplos reflejan datos que llegaron tarde o una asignación disponible que no se aplicó. Necesitamos contrastar esos tiempos y la ruta de ingreso antes de atribuirlo a error del usuario o recomendar un segundo ingreso como solución.

Evidencia previa: comentario público 3214374 del 6 julio en RCS-27578 explica que se espera llegada del archivo, no un día adicional después de ingresar. La observación interna de octubre no se expone al cliente ni se generaliza a estos casos.

Siguiente paso:
Juan y revisión técnica: contrastar fecha de disponibilidad de asignaciones y login por SSO de los ejemplos recibidos. Solicitud de Matt sobre campo explícito continúa pendiente, sin decisión de cambio de formato.


## Rastro
2026-10-16 inbox/2026-10-16-tailored-llamada-duda-segundo-login.md

## tailored llamada ssu comparacion — 2026-10-16
_chunk 2053 · 2026-10-16 · fuente: inbox/2026-10-16-tailored-llamada-ssu-comparacion.md_

Tailored Brands. Respuesta propuesta durante la llamada, 16 octubre 2026.

Fuente: captura codex-clipboard-e7e8acb7-9829-42af-b101-936b7b589b5b.png. Archivo visible appriss_sso_locations_20261014024505, solo lectura. Columnas Company, Brand y Location separadas. Brand muestra SSU en varias filas corporativas; otras filas muestran MSP o TMW. No se ve Chris Orth en las filas visibles. Location 2005 aparece en algunas filas SSU.

Colton pregunta si Appriss puede ayudar a identificar asignaciones semejantes y si HR debe cambiar ubicaciones. Sugiere posiblemente todos los SSU. Es una hipótesis del cliente, no causa confirmada.

Borradores afectados
No invalida el ajuste individual de Chris ni la consulta a Matt. Precisa que no se debe afirmar marca ausente: el archivo mostrado contiene Brand=SSU. No se debe convertir SSU a TMW o LocationID 9000xxxx a 4000xxxx masivamente sin establecer la regla correcta. Los ejemplos visibles no prueban que todos los SSU fallen.

ENGLISH
Yes, a useful next step would be to compare the location and brand values in this file with the locations available in Appriss, starting with the SSU examples you are showing. That comparison would help identify which assignments do not match and whether the change belongs in the source data or in our mapping. I would hold off on asking HR to change those values until we establish the expected mapping, since SSU alone does not tell us that the record is wrong.

ESPAÑOL
Sí, un próximo paso útil sería comparar ubicación y marca del archivo con las ubicaciones disponibles en Appriss, empezando por los ejemplos SSU que muestran. Eso ayudaría a identificar asignaciones sin correspondencia y si el cambio corresponde a los datos de origen o a nuestro mapeo. Antes de pedir cambios a HR establecería el mapeo esperado, porque SSU por sí solo no demuestra que el registro sea incorrecto.

Siguiente paso:
Appriss y responsable del archivo de TBI: establecer mapeo esperado y comparar Brand más Location con ubicaciones del sistema. Es propuesta para acordar, no trabajo ya ejecutado ni acceso confirmado a todo el archivo.


## Rastro
2026-10-16 inbox/2026-10-16-tailored-llamada-ssu-comparacion.md
