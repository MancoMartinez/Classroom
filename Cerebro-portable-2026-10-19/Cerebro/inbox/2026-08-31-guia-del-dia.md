# Guía del día, lunes 31 ago 2026

Los 16 tickets abiertos de Juan, ordenados por lo que desbloquea más con menos esfuerzo. Cada
bloque trae el estado verificado en Jira hoy, el paso concreto de investigación, el texto listo
para pegar y lo que no se debe decir.

Jira es de solo lectura desde acá. Todos los textos los pega Juan.

---

## Lo que cambió y todavía no está reflejado en ningún ticket

Verificado hoy contra Jira en vivo. Tres cosas mueven la prioridad del día.

**El release Secure August 2026 Release 2/2 salió el 27 de agosto.** `released: true`, fecha 27 ago.
Cuatro items que tocan tickets tuyos viajaron en él: ENG-7184, ENG-7191, ENG-7192 y ENG-6565.
Tres de tus tickets están esperando noticias de ese release y ninguno las tiene.

**ENG-6220, Sign Out Behaviours, tiene resolution Declined y status In Testing.** Ese item no va a
salir. Refuerza el matiz que ya venías manejando: escríbele a Ashley sobre logouts prematuros por
timeout, nada más.

**El ítem que le prometiste a Jim el 26 de agosto sigue sin existir.** Repetí la búsqueda en ENG hoy
sobre confirmation, print, approval closure y workbench desde el 20 de agosto. No aparece ningún
item de ADUSA sobre el panel de confirmación. Le dijiste "I have logged it, and engineering is
reviewing it now". Ese es el riesgo más caro del día y el más barato de resolver.

---

## Orden del día

Todo esto es para hoy, lunes 31 de agosto. Los bloques son franjas de la jornada, no días distintos.

| Franja | Tickets | Por qué ahí |
|---|---|---|
| Primera hora | RCS-28153, RCS-28123, RCS-28093 | Casi listos, riesgo alto si se dejan |
| Media mañana | RCS-28256, RCS-28289 | Promesas que vencieron con el release y con el regreso de Scot |
| Mediodía | RCS-28581, RCS-28638, RCS-28327, RCS-28482 | Investigación tuya, sin depender de nadie |
| Tarde | RCS-27676, RCS-27959, RCS-28282, RCS-28496, RCS-28122 | Persecución en lote, texto ya redactado |
| Sin acción hoy | RCS-28099, RCS-27765 | La pelota está afuera y hay registro de eso |

---

# BLOQUE 1. PRIMERA HORA DE HOY

## 1. RCS-28153 · BYF, errores y logout de usuarios · High

Estado: Under Customer Review. Silencio al cliente 19 días. El reloj de cierre automático arrancó el
25 de agosto con aviso de 14 días, así que cierra alrededor del 8 de septiembre.

Este es el primero porque el trabajo ya está hecho. El fix salió, la causa raíz está documentada, y
los dos textos están escritos desde el 27 de agosto en
`inbox/2026-08-27-rcs-28153-respuesta-ashley.md`. Solo falta una verificación de dos minutos.

**Verificado en Jira hoy.** ENG-7184 en Done, resolution Resolved, fixVersion Secure August 2026
Release 2/2 con `released: true` y fecha 27 ago. Assignee Vedant Shirude.

**Paso único de verificación.** Control Panel, USPROD, Engineering, Config Items, cliente 362 Big Y
Foods, `CPF.Core.LogOnTimeoutMinutes`. Solo lectura.

- Si el valor es 240, usa el texto A.
- Si sigue en 60 o está vacío, tu cambio del 11 de agosto nunca se guardó. Aplícalo, verifícalo, y
  después usa el texto A.
- Si es otro número, usa el texto B del archivo del 27, que no cita cifras.

**Texto A, para pegar en Jira.**

```
Hi Ashley,

Update on this one.

On the 11th I set your user timeout to 240 minutes and told you that would cover the logouts. The system kept applying the old 60 minute limit instead, so your users were still being signed out early.

We have corrected that and the correction is live on your environment.

Could you have your team work as normal and confirm on this ticket whether the logouts and the errors have stopped. I am leaving this with you until you confirm.

Thank you.
```

**Qué no decir.** No afirmes que el comportamiento de sesión quedó completo. ENG-6220 está Declined
y In Testing. El alcance de lo que salió es el refresh de la cookie respetando el timeout del
tenant, nada más.

**Efecto lateral que te toca a ti como lead.** ENG-7184 resuelve además RCS-28181, Big Y Foods, en
Work in progress, y RCS-28346, Stater Bros, en Under Customer Review. Ninguno es tuyo. Los dos
siguen abiertos contra un defecto que ya se liberó. Avisa a quien los tenga.

---

## 2. RCS-28123 · ADUSA, case assignment · Medium

Estado: Work in progress. Última promesa tuya hace 5 días.

Este va segundo por riesgo de credibilidad. J.R. Teagle y Chris Rippingale leen ese hilo, y le
dijiste a Jim que el ítem estaba logueado y en revisión de ingeniería.

**Verificado en Jira hoy.**

| Item | Estado | Assignee | fixVersion | Cubre el panel |
|---|---|---|---|---|
| ENG-7191 | Done / Resolved | Matthew Kamminga | Release 2/2, liberado 27 ago | No |
| ENG-7192 | Done / Resolved | Scott Buric | Release 2/2, liberado 27 ago | No |
| Item del panel | No existe | | | |

**Paso 1, antes de escribirle a nadie. Prueba el flujo en producción.** Jim reportó el panel vacío
el 26 de agosto a las 10:36. El release salió el 27. Su reporte es anterior al release. Asigna un
caso de prueba en ADUSA y mira si el panel de confirmación con view o print aparece ahora. Diez
minutos. Si aparece, el ticket se cierra hoy y no necesitas a Matt.

**Paso 2, si el panel sigue vacío. Mensaje corto a Matt Kamminga.** Va como comentario interno en
RCS-28123 o por Teams, lo que sea más rápido de contestar.

```
Hi Matt, quick one on ADUSA.

On RCS-28123 Leigh Ann and Jim report that after assigning a case the confirmation panel comes up empty. Before the cutover that panel showed the assignment confirmation and a view or print PDF button.

ENG-7191 and ENG-7192 both shipped on the 27th and neither covers this panel. Was it removed on purpose in the unification build, or is it a regression?

If it is a regression I will open a new item, I just want to make sure I am not duplicating something you already have.
```

**Paso 3, si Matt no contesta antes del mediodía.** Abre el ENG igual y mándale la clave a Jim. Un
ítem abierto de más se cierra en un minuto. Un cliente que pregunte por el número y no lo encuentre
convierte un tema menor de interfaz en un problema de confianza.

**El ticket no cambia de estado.** El pendiente es interno, se queda en Work in progress.

---

## 3. RCS-28093 · Ahold, empleados no restringidos por tienda · Low

Estado: Work in progress. Nivel 1, Leigh Ann escribió el 28 de agosto y nadie contestó. Tres días.

Es el único ticket donde el cliente espera tu respuesta directa.

**Verificado en Jira hoy.** ENG-6744 sigue en Ready for Development, assignee Matthew Kamminga, sin
fixVersion. No hay fecha ni fix que comunicar.

**Contradicción que hay que cerrar antes del próximo mensaje técnico.** El 27 le dijiste a Leigh Ann
que el campo es la posición 20 de `DA_Employee_Info.dat`. La cosecha del 28 dice que la spec de
Confluence "Employee Import Specs" tiene 54 columnas, que la 20 es Division y la 41 es Company Code,
y que MISC1 no figura en la spec. El campo que bloquea es `incident.Employee.MISC1`. Falta el mapeo
entre la posición del feed de ADUSA y MISC1. Verifica eso antes de volver a hablar de posiciones con
ella. El mensaje de hoy no toca el tema, así que no te bloquea.

**Texto para Leigh Ann, para pegar en Jira.**

```
Hi Leigh Ann,

Thank you, and thanks for bringing April in.

To be clear on what we are asking for: we need that field populated for every employee record, matching the store division. Today it comes through for most employees and is empty for some, and that is what breaks the store restriction on those records.

If April can confirm whether the feed can carry it for all records, we can move forward on our side.

There is no action needed from you beyond that.

Thank you.
```

**Paso paralelo, el que realmente destraba.** Jie Chen te dijo que Support le pida a Delivery un
archivo de Employee Feed de ADUSA. Los contactos son Matt Kamminga para Incident y LPMS, y Ryan
Barlow para importes de datos hacia Incident. Aprovecha que ya le estás escribiendo a Matt por
RCS-28123 y súmalo en el mismo mensaje.

```
Also on ADUSA, separate ticket, RCS-28093. I need a recent Employee Feed file from ADUSA, or the path where it gets archived, so I can work out which field feeds incident.Employee.MISC1. Is that something you or Ryan can point me to?
```

**Qué no decir.** No le des a Leigh Ann fecha ni versión. ENG-6744 no tiene ninguna de las dos.

---

# BLOQUE 2. MEDIA MAÑANA DE HOY

## 4. RCS-28256 · Appriss Incident, timeouts y carga lenta · High

Estado: Under Customer Review. El clasificador lo puso en nivel 3. Está mal. Sube a nivel 2 y esta
es la razón.

El 25 de agosto le escribiste a Colton: "A fix for the slow transition between Secure and Incident is
currently in testing. I will confirm here once it is released." **El release salió el 27.** La
promesa venció. El cliente no sabe.

**Verificado en Jira hoy, y hay que cerrar una ambigüedad antes de escribir.**

| Item | Estado | fixVersion |
|---|---|---|
| ENG-6565, ICA Investigations UI running Slow | Done | Release 2/2, liberado 27 ago |
| ENG-7168, Incident Performance, cache screen label lookups | Development Complete | Release 2/2, liberado 27 ago |

ENG-7168 lleva un fixVersion liberado y sigue en Development Complete, no en Done. Un fixVersion
liberado no implica que todo lo que viaja en él esté terminado. Ese release lleva 118 issues y hoy
113 están en Done, así que cinco quedan fuera y ENG-7168 es uno de ellos. Confirma cuál de los dos
cubre la transición Secure a Incident antes de decirle a Colton que salió. Si ninguno la cubre con
claridad, pregúntale a Chris Rippingale, que es el assignee de ENG-7168.

**No pegues el texto de abajo antes de cerrar esa confirmación.** Es la única afirmación de toda la
guía que le promete a un cliente algo que todavía no está verificado al cien por ciento.

**Segundo pendiente tuyo en este ticket.** Prometiste hacer seguimiento del login de Vincent Fortner
como tema aparte y no volviste sobre eso. Colton adjuntó lo que parece un problema de SSO. El
discriminador es el SSO Response Log, está en `brain/memoria/reference_sso_incident_diagnostico.md`.

**Texto para Colton, para pegar una vez confirmes cuál ENG cubre la transición.**

```
Hi Colton,

Update on this one.

The fix for the slow transition between Secure and Incident went out with our release on the 27th. It is live on your environment now.

On Vincent Fortner, I am still working that as a separate item and will come back to you on it here.

The three checks I asked for on the 25th are still open. When you and a store user get a moment, could you run the report that was timing out, create a test incident from a store login, and move from Secure to Incident. If any of them still fail, send me the date, time, username and store number.

Thank you.
```

---

## 5. RCS-28289 · Vitamin Shoppe, usuarios bloqueados · Medium

Estado: Under Customer Review. El clasificador lo tiene en nivel 4. También está mal, y por una
razón de calendario.

El 24 de agosto Joe Austin escribió "Scot returns from vacation this week". Esa semana era la del 24
al 30. Hoy es 31. La semana pasó y Joe no volvió. El seguimiento es tuyo y ya vence.

**Texto para Joe Austin, para pegar en Jira.**

```
Hi Joe,

Checking in on this one.

You mentioned Scot was back from vacation last week. Has he had a chance to look at the blocked user issue?

If the user is still being blocked, a full page screenshot of the error will let us pick the investigation back up. If it has cleared up, let me know and I will close this out.

Thank you.
```

---

# BLOQUE 3. MEDIODÍA DE HOY, INVESTIGACIÓN PROPIA

Estos cuatro no dependen de que nadie conteste. Son los que mueven el conocimiento del día.

## 6. RCS-28581 · CWH, POS Number regresó al mapeo anterior · Medium

Estado: Under Support Review. Sin ENG enlazado. Sin investigación. Promesa tuya de hace 3 días.

**Lo que dice el hilo y hay que aprovechar.** James McKenna reportó el 26 que funcionaba, y una hora
después se retractó: "I have found the issue in other transaction outside what I had tested. Appears
it may be in a data period." Ese es el discriminador servido. El defecto no es global, cae en una
ventana de fechas.

**Paso 1.** Consigue el SQL del search. Corre el reporte con parámetros dummy para ver el query. Esa
es la lección que destrabó RCS-27644 en H&M y está en
`brain/markdown/16-rcs-soluciones.md:177-188`.

**Paso 2.** Con el query en mano, corre un SELECT sobre transacciones de CWH ordenadas por fecha y
busca dónde el POS number deja de resolver TILL02, TILL03 o DISPENSE01 y pasa al número crudo. Eso
te da la ventana exacta.

**Paso 3.** Cruza esa ventana contra las fechas de release. El release del 13 de agosto y el del 27
son los candidatos. James dijo "until this week", así que la ventana cae cerca del 25.

**Paso 4.** Los overrides de mapeo por cliente viven en `secure_Resource.json`. Ahí se ve si el
mapeo se sobrescribió.

**Texto para James, para pegar si terminas el día sin la ventana cerrada.**

```
Hi James,

Update on this one.

Your note that it may fall in a date period helps. Could you send me two transaction IDs, one where the POS number shows the till correctly and one where it does not, with their dates. With both I can compare the mapping directly rather than work back from the window.

Thank you.
```

**Conexión que vale la pena mirar.** RCS-28099 es también CWH, también lógica de mapeo de
descuentos, también sin resolver. No afirmes causa común. Mira si comparten la ventana de fechas.

---

## 7. RCS-28638 · Myer Australia, mapeo de Header Ext ausente · High

Estado: Under Support Review. Tres días. El análisis pesado ya está hecho y vive en
`inbox/2026-08-28-rcs-28638-myer-header-ext.md`.

**Lo que ya está establecido.** El dato llegó a Appriss. La transacción 2608273342446971618 muestra
Proof Type CUSTOMER ORDER RETURN y Customer Order Number 2002504903 en Retail Transaction Details, y
los muestra vacíos en las columnas del search y en el receipt view. La pérdida está entre el detalle
de la transacción y los campos Header Ext.

**Lo que bloquea.** El cliente dice "missing since 09/08/26". RCS-28640, mismo cliente y misma fecha
declarada, aporta la transacción 2608098315964575603 como correcta, y esa es del 09/08. El corte cae
después del 9. La ventana sigue abierta.

**Paso 1, y es tuyo, no del cliente.** Cierra la ventana con datos. Cliente 109, código MYR,
Greenplum GP3, acceso SSH con credenciales gpadmin del password book, salto por jump server LA4
10.22.0.220. Archivos crudos en `p-ingest-<region>/109_MYR/Archive/Prod/<fecha>`. Corre un SELECT
sobre transacciones por día y busca el primer día donde Proof Type y Financial Statement Date salen
nulos. Eso te da el corte real sin gastarle crédito al cliente.

La sesión del 28 recomendó no comentarle a Christine antes de tener la ventana. Sigue siendo lo
correcto. La forma de tenerla es esta consulta, no una pregunta.

**Paso 2. Escalación a Delivery, no a Engineering.** Data mapping va a Delivery. Myer es Secure
Store, así que los contactos son Tomasz Mikunda o Carl Costelow. Fuente
`brain/markdown/19-rcs-procesos-playbook.md:961`. El mecanismo es Team Ownership a
`Support (Delivery Dep.)` y Sprint a `RCS Support Team`.

**Paso 3. Llévalo como cuenta, no como ticket.** Doce tickets de Myer en agosto, nueve son defectos
de mapeo o datos faltantes, cuatro ventanas de corte distintas declaradas por el cliente: 29/06,
15/07, 09/08 y el comportamiento nuevo del 21 ago. RCS-28612 y RCS-28640 siguen sin asignar. Cuatro
más están con Matthew Everett. La hipótesis del cliente en RCS-28518 es que el payments project se
llevó el mapeo, y que en QA todo estaba bien. Esa hipótesis explica las cuatro ventanas. Mídela, no
la afirmes.

**Segundo defecto que encontraste y el cliente no reportó.**
`Reason Description:$lineItemDomainSpecific.returns.returnNotes` es un token de plantilla sin
resolver. Vale un ticket propio.

**Vacío de conocimiento que este ticket deja expuesto.** El cerebro no tiene una sola entrada sobre
Header Ext, Proof Type, Financial Statement Date ni Auto Reference. Myer no tiene ficha de cuenta.
El runbook T-012 sobre schema drift y mapping breaks sigue Not Started. Cuando cierres, escribe la
ficha.

---

## 8. RCS-28327 · Delhaize, loyalty discounts sin especificar · Medium

Estado: Work in progress. Sin issue links, o sea que la causa raíz de Edwin nunca se convirtió en un
item de ingeniería. Cuatro días desde tu promesa.

**Lo verificado por Edwin el 20 de agosto.** Cliente correcto es `c046dhz`, o sea
`ARDMPROD.ARDM_046`, banner FOOD LION. La fila de descuento tiene `CODE = 'loyalty discount'`,
`TYPE = 'other'`, `REASON = null`, y lo setea el parser a propósito en
`pyardm/us/c046dhz/ardm/python/pd_pos_parser.py:777,842`. El pipeline funciona. La causa está en la
capa de display de Secure: `itemdiscount.searchable` resuelve el texto vía
`GetExcelReferenceData(type, "/system/ebr/crdm/store/2_0/enumerations/crdm pos enumerations.xlsx", "ItemDiscountType")`
y esa VirtualFilePath devuelve 0 filas en `secure.Repo` del cliente.

**Lo que Edwin no confirmó, y bloquea todo lo demás.** Que el campo `type` sea literalmente el que
renderiza la columna "Item Discount Description" que ve Becky. Puede ser otro campo con otro nombre.

**Paso A, el único que importa hoy.** Abre en Composer la búsqueda donde la columna sale en blanco y
anota el field ID al que está bindeada, literal.

| Resultado | Lectura |
|---|---|
| Es el campo de tipo que llama a `GetExcelReferenceData` | La teoría de Edwin se sostiene, sigue al paso B |
| Es `code` u otro campo de texto directo | La teoría no aplica, el valor está en la base y no se muestra, investiga de cero |
| Es un campo compuesto o calculado | Abre su definición antes de concluir |

**Ambigüedad a resolver antes de consultar la base.** La ficha de ADUSA dice Client ID 441. Edwin
habla del Platform DB del cliente 46. Cuarenta y seis es el ID ARDM de Delhaize, 441 es el tenant
ADUSA. Confirma cuál Platform DB sirve la instancia 5.4 de Delhaize contra el Excel de client IDs.

El plan completo con los pasos B, C y D está en
`inbox/2026-08-24-rcs-28327-validacion-composer.md`.

**No le escribas a Becky hoy.** El 27 le dijiste "I have nothing confirmed yet on the cause and I am
not going to give you one until I do." Cumple eso. Escríbele cuando el paso A dé resultado.

---

## 9. RCS-28482 · AHL/DLZ, campos en gris en Izenda · Low

Estado: Work in progress. Tienes una hipótesis propia escrita el 24 de agosto y sin probar.

**La hipótesis.** De las capturas de Jim, los reportes afectados exponen solo Data Sources, Fields y
Preview, mientras uno que funciona expone el juego completo incluido MISC. La vista afectada muestra
además un checkbox Distinct y un selector Results donde la que funciona muestra Records. Los dos no
serían del mismo tipo de reporte, y las pestañas disponibles saldrían del tipo.

**Paso único.** Abre en Izenda la definición de `PBI - Current Location Listing (Jim Cosseboom Test)`
y de `Outlook Export (Jim Cosseboom Test)`, y compárala contra un reporte donde MISC sí aparece.
Mira el tipo de reporte.

Si el tipo explica la diferencia, esto deja de ser un defecto y pasa a ser cómo se creó el reporte.
Esa conversación con Jim es mucho más corta.

**No le escribas hoy sin hallazgo.** Ya se lo dijiste el 26: "I have nothing to report yet on what
makes the tab render greyed out. I will come back to you when I do." Él contestó confirmando que
entendió. La bitácora del 27 lo deja explícito: no volver a escribirle sin hallazgo.

---

# BLOQUE 4. TARDE DE HOY, PERSECUCIÓN EN LOTE

Cinco tickets esperando al cliente. Todos pasan los 7 días que marcan el momento de perseguir. Los
textos están listos, es media hora de pegar.

## 10. RCS-27676 · RLC, cambio de IP y hostname de SFTP · 27 días

El silencio más largo de tu cola. Pediste la vista de IPs públicas el 4 de agosto, van 27 días.
Tyler Aken no manda nada desde el 30 de julio, van 32.

```
Hi Tyler, Matt,

Following up on this one.

We are still waiting on the Public IP Addresses view from your Azure team, or the NAT Gateway view if your outbound traffic routes through one, showing 52.191.249.127, 20.185.215.130, 20.185.215.133 and 20.39.47.206 assigned to your subscription. Our InfoSec team needs that view to approve the whitelisting. The VM level screenshot you sent in July shows private addresses only, so it does not cover it.

Is there someone on your Azure side I should reach out to directly to move this along?

Thank you.
```

## 11. RCS-27959 · PACSUN, whitelisting para MuleSoft · 18 días

Tiene aviso de cierre automático emitido el 26 de agosto. Cierra alrededor del 9 de septiembre.

```
Hi Jongki, Ryan,

Following up on this one.

The three addresses 44.233.90.84, 52.38.195.3 and 52.10.40.88 have been on our allow list since 12 August, and your existing production addresses were left in place as you asked.

All I need is confirmation that both the new environment and your current production connections are working. This ticket is set to close automatically if we do not hear back, so a one line reply keeps it open and lets me close it properly.

Thank you.
```

## 12. RCS-28122 · Blain's, cambios de usuario · 11 días

```
Hi James,

Following up on this one.

Two things are still open from my last message: whether the Admin Tools and user changes issue is fully resolved on your side, and whether the Compliance Audit pictures are attaching now.

If both are working I will close this out. If either is still failing, tell me which one and I will pick it back up.

Thank you.
```

## 13. RCS-28282 · Co-op, notificación de acceso bloqueado · 9 días

El cliente no entiende qué le estás pidiendo. La última línea le baja el costo de responder.

```
Hi Michelle,

Following up on the country list.

To set access by country we need two things: the countries your users should be able to reach the application from, and any you want blocked. Once you send that we apply it and confirm here.

If it is easier, just send the countries your team works from and we will block everything else.

Thank you.
```

## 14. RCS-28496 · PVH, fallas de login en desktop e iPads · 10 días

Rajith pidió siete datos el 20 de agosto, van 11 días sin respuesta. Tu último comentario es del 21.
Siete preguntas es demasiado. Reducirlas a tres sube la probabilidad de respuesta.

```
Hi Bob, Yannick,

Following up on this one.

We still need the details my colleague Rajith asked for on 20 August before we can start. If the full list is hard to put together, the three that unblock us are the exact error message users see, two or three affected store numbers with usernames, and when the issue started.

Are the logins still failing, or has this settled down since you raised it?

Thank you.
```

---

# BLOQUE 5. SIN ACCIÓN HOY

## 15. RCS-28099 · CWH, HYP a RCS, lógica de descuento de ítem

James McKenna dijo el 17 de agosto que su equipo está armando el set de datos completo y que Bryant
McAnnally lo lleva. David Vargas acusó recibo el 18. La pelota está afuera con registro claro. Déjalo
quieto. Míralo cuando toques RCS-28581, que es el mismo cliente y la misma familia de mapeo.

## 16. RCS-27765 · Winn-Dixie, chequeo de archivo de datos

El hilo se partió entre Jira y correo. La respuesta del 27 de julio quedó en Jira y nunca llegó al
correo donde IT esperaba. Le dijiste a Heaven el 25 que el correo ya se respondió y que están
monitoreando. Lo único que toca hoy es confirmar que ese hilo de correo tuvo movimiento. Si lleva
una semana muerto, el problema volvió y hay que retomarlo.

---

# QUÉ MOVER EN JIRA HOY

Ningún estado se mueve solo por pegar un comentario. Esta es la lista.

| Ticket | Acción en Jira |
|---|---|
| RCS-28153 | Queda en Under Customer Review, ya está ahí |
| RCS-28123 | Queda en Work in progress, el pendiente es interno |
| RCS-28093 | Queda en Work in progress |
| RCS-28256 | Queda en Under Customer Review |
| RCS-28289 | Queda en Under Customer Review |
| RCS-28581 | Pasa a Work in progress al arrancar la investigación |
| RCS-28638 | Se queda en Under Support Review hasta cerrar la ventana de fechas |
| RCS-28327 | Queda en Work in progress |
| RCS-28482 | Queda en Work in progress |
| Los cinco de persecución | Quedan en Under Customer Review |

Aparte, los cuatro de la lista de Vedant que ya pasan la semana en Completed: RCS-28334, RCS-28112,
RCS-28364 y RCS-28214 se mueven a Closed. Detalle en
`inbox/2026-08-31-completed-a-closed.md`.

---

# LO QUE HAY QUE ESCRIBIR AL CEREBRO CUANDO CIERRES EL DÍA

```bash
bin/anotar RCS-28581 "lo que encontraste sobre la ventana de fechas"
bin/anotar RCS-28638 "el corte real y a quién de Delivery se escaló"
bin/anotar RCS-28327 "el field ID que devolvió Composer"
bin/anotar RCS-28482 "el tipo de reporte de cada uno"
python3 bin/indexar_tickets.py
```

Dos huecos del cerebro que este día deja expuestos y conviene tapar. Myer no tiene ficha de cuenta
ni entrada en investigaciones, y el cerebro no registra nada sobre Header Ext. El léxico de
`bin/cola.py` no reconoce "I will come back to you when I have it" como promesa, y por eso RCS-28327
cayó a nivel 4 esta mañana.
