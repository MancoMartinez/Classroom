# Cola completa, ordenada por SLA, prioridad y ADUSA

Jueves 27 ago 2026, 19:00 hora Colombia. 17 tickets abiertos.
Método: leí los comentarios completos de los 17, no solo el último. Crucé con bitácora, inbox y
adjuntos. Todo estado sale de Jira.

RCS-27991 salió de la cola desde el pull de las 15:26. Verifica qué le hiciste, la ficha ya no está.

## Las reglas que uso para ordenar

De `brain/markdown/19-rcs-procesos-playbook.md` y
`brain/memoria/reference_escalacion_l3_procedimiento.md`:

| Regla | Valor |
|---|---|
| SLA de primera respuesta | P1 1 hora 24/7, P2 High 4 horas hábiles, P3 Medium 12 horas hábiles, P4 Low periodo razonable |
| Cadencia de update obligatoria | Critical cada hora, **High diario**, Medium y Low mínimo semanal |
| Prioridad máxima de cola | Critical o High **más tipo Incident** |
| Under Customer Review | **Único status que pausa todos los relojes SLA** |
| Cierre automático | Avisos día 7, 14 y 28. Auto cierre pasado el 28 |
| ADUSA | *"todos los tickets de ADUSA son P1, porque el cliente está amenazando con dejar un contrato de 800 mil"*, encuadre de Chris Rippingale |

Consecuencia directa: los 10 tickets en Under Customer Review no queman SLA. Los 7 en Work in
progress o Under Support Review sí. Eso reordena todo respecto de lo que te di esta tarde.

**Tus tickets ADUSA son cuatro**: RCS-28093, RCS-28123, RCS-28482 y RCS-28327. Delhaize es banner de
ADUSA, client ID 441. Big Y no lo es, es el cliente 362.

**Compromiso de cuenta pendiente hoy**: correo resumen diario a Jim más check-in de los jueves a las
3:30 PM ET. Esa hora ya pasó.

---

# ROJO. Hoy, sin falta

## 1. RCS-28294 Vallarta, Smart Alerts no Triggering
Medium, **Under Support Review**, SLA corriendo. Reporter Tatiana Barcenas.

**Le dijiste al cliente algo que no es cierto.** El 25 de agosto escribiste:

> "This is now with our Engineering team as a tracked defect."

No hay ningún issuelink a un ENG. El ticket sigue en Under Support Review y asignado a ti. Nadie de
ingeniería lo tiene. Van dos días.

El material está armado desde el 25 en `inbox/2026-08-25-rcs-28294-repro-smart-alerts.md`: el plan
de 4 corridas, las mediciones de `POST /nettrack/api/internal/SendSmartAlert.aspx` con 2495 timeouts
y 248 errores 500, y el borrador completo de escalación. Le entregaste los pasos de reproducción a
Shandana el 26 y ella no ha vuelto.

**Acción:** transiciona a Under Engineering Review y reasigna a Shandana Khan para que el ENG se
auto cree. Pega el borrador del inbox. Enlaza ENG-6541 "Harden smartalerts functionality" y
RCS-28131 de Sportman, que ya está en Under Engineering Review.

Suelto que arrastra el ticket: la remediación de timezone de RCS-28030 nunca se aplicó a Vallarta.
308 de 419 cuentas siguen en `TimeZone = UTC` con `LastLoginDate = NULL`. ENG-7236 lleva en Backlog
desde el 13 ago.

## 2. RCS-28093 ADUSA, empleados no restringidos por tienda
Low en Jira, **P1 por encuadre de cuenta**. Under Support Review, SLA corriendo. Reporter Leigh Ann
Stubbs.

**La respuesta ya está escrita y bloquea a un colega.** Jie Chen te preguntó el 21 de agosto:

> "@Juan Martinez Please ask client if it's possible to provide Employee.misc1 value (same as
> Store.Division) to all Employees in adusa Employee Feed... This will help us to solve the problem."

Trasladaste la pregunta, Leigh Ann devolvió otra el 24 y ahí se paró. Jie Chen lleva 6 días
esperando. Leigh Ann lleva 3.

`inbox/2026-08-27-CONCLUSION-misc1-adusa.md` ya tiene el dato duro: el campo es la **posición 20 de
`pii-pgp-DA_Employee_Info.dat`**, justo después de EmployeeID que es la 19. StoreNumber es la 27.
Fuente `F:\Clients\Delhaize\RefLoader_Prod\fmt\employee.xml` versión 2025.07.09. La respuesta a
Leigh Ann y el comentario interno están redactados y sin pegar.

**Acción:** pega los dos textos. Antes corre el conteo de `Misc1` vacío en `incident.Employee` para
tener la línea base, porque en cuanto ADUSA toque el feed pierdes la referencia.

## 3. RCS-28153 Big Y Foods, errores y cierre de sesión
**High**, Under Customer Review. SLA pausado. El reloj que corre es el de cierre automático, aviso
de 14 días del 25 ago. Reporter Ashley McFarlane.

16 días sin que el cliente oiga nada, en un High. La cadencia exigida para High es diaria.

El fix salió a producción hoy y ella no lo sabe. ENG-7184 en Done y Resolved, fixVersion Secure
August 2026 Release 2/2 liberado hoy, listado en la sección de entregados de las release notes.

**Acción:** lee en Control Panel el config item `CPF.Core.LogOnTimeoutMinutes` del cliente 362. Si
es 240, pega el texto A de `inbox/2026-08-27-rcs-28153-respuesta-ashley.md`. Si sigue en 60,
aplícalo primero.

Avisa además a quienes llevan **RCS-28181** en Work in progress y **RCS-28346** en Under Customer
Review. Los dos cuelgan del mismo ENG-7184 y siguen abiertos con otros dueños.

## 4. RCS-28223 McDonald's, Cash Audit Questions
Medium, **Under Support Review**, SLA corriendo. Reporter Hugo Cortez.

Matthew Kamminga te bloquea desde el 25 de agosto:

> "@David Vargas, are the affected questions all grid style questions? Are you able to provide
> reproduction steps on how to recreate this error?"

Nadie contestó. **David Vargas ya salió**, así que el contexto del análisis se pierde si no lo
traspasas ahora. Él acotó la causa a FieldType 35, el control compuesto de "top two managers, dollar
amount, action taken", contra FieldType 11 que sí funciona.

Hay una decisión sin tomar desde el 17 de agosto. J.R. Teagle escribió:

> "It looks like we have 2 different issues in this ticket, which should probably be split if that's
> still the case."

Nadie la tomó. El problema de login salió a RCS-28486, el original sigue aquí.

**Acción:** contesta a Kamminga en el ticket con los pasos sobre `AuditSection_V24_S4.aspx`, tenant
`mcdonalds`, y di sí o no a si son preguntas tipo grid. En el mismo movimiento decide el traspaso a
Sebastián Rueda que propone `inbox/2026-08-27-cosecha-salida-david-vargas.md`.

---

# NARANJA. Mañana a primera hora

## 5. RCS-28256 Tailored Brands, timeouts y lentitud
**High**, Under Customer Review, SLA pausado. Reporter Colton Neal. 20 comentarios.

Es el ticket con más deuda acumulada de la cola. **Cuatro promesas vivas:**

- 12 ago: *"will follow up with you once we have more information"* sobre los tiempos de carga.
- 21 ago: *"We are addressing this separately from the slowness and will provide an update here."*
- 25 ago: *"Vincent Fortner's login is a separate issue on our side... I will follow up with you on that."*
- 25 ago: *"A fix for the slow transition between Secure and Incident is currently in testing. I will confirm here once it is released."*

Y dos preguntas sin respuesta que pesan más que las promesas:

- **Mike DiTommaso, cliente, 14 de agosto:** *"This is a store-facing system, and these issues need
  to be resolved as soon as possible. Do we have an update on a resolution?"* Solo recibió el acuse
  automático. Nadie humano le contestó. 13 días.
- **J.R. Teagle, VP Global Support, 16 de agosto:** *"Team, this might be the same problem, might be
  a new one... let's please look into this ASAP."* Nadie respondió en el ticket. 11 días.

**Acción:** entrega el hallazgo del login SSO de Vincent Fortner, tienda TMW 1405. Responde a Mike
DiTommaso directo. Persigue a Colton por la confirmación de las tres pruebas del 25 ago.

## 6. RCS-28099 Camping World, Item Discount Logic
Medium, Under Customer Review. **Posible cierre automático mañana.**

Aviso de 7 días el 7 de agosto, aviso de 14 días el 14 de agosto anunciando cierre en 14 más, o sea
alrededor del **28 de agosto**. El cliente escribió el 17, lo que debería reiniciar el contador. No
hay ningún comentario posterior del bot que lo confirme.

**Acción:** verifica si el reloj se reinició. Si no, comenta hoy mismo para que no se cierre solo un
ticket que está esperando datos legítimos de Bryant McAnnally.

## 7. RCS-27959 PACSUN, IP whitelisting
Medium, Under Customer Review. Aviso de 14 días el 26 ago, cierre alrededor del 9 de septiembre.

**Riesgo abierto, no es solo perseguir al cliente.** Jongki Lingga fue explícito el 11 de agosto:

> "Please do not remove our existing current production IP addresses."

RETAILIT-20648 responde *"I have updated the clients sftp allow list"*. Esa frase no distingue entre
añadir y reemplazar. Si alguien reemplazó, PACSUN perdió su producción actual y no lo ha notado
porque no ha probado.

Además dejaste un pendiente interno del 10 de agosto sin cerrar: *"Checking whether it already
covers this request before raising a new one"*, sobre el CASD del 23 de julio. Nunca dijiste qué
pasó con él.

**Acción:** abre RETAILIT-20648 y confirma que se añadieron sin quitar. Después pega el comentario
de persecución ya redactado.

## 8. RCS-28123 ADUSA, Case assignment issues
Medium, **P1 por cuenta**, Work in progress, SLA corriendo. Reporter Leigh Ann Stubbs.

Ayer le dijiste a Jim Cosseboom:

> "I have logged it, and engineering is reviewing it now."

El único ENG enlazado es ENG-7192, que cubre la asignación y los correos duplicados. **No aparece
ningún ticket nuevo para el popup de confirmación con view/print.** La afirmación no está respaldada
por el ticket.

Suelto viejo: Matthew Kamminga dejó abierto el 19 de agosto *"Will see what we can do to speed up
this look up"* sobre la lentitud del lookup de nombres. Ocho días sin update.

**Acción:** crea o localiza el work item del popup, enlázalo, y dale el número a Jim. Pídele a
Kamminga el estado del lookup.

---

# AMARILLO. Esta semana

## 9. RCS-27676 Ralph Lauren, SFTP IP change
Low, Under Customer Review. **23 días de silencio, el récord de la cola.**

Dos cosas que nadie ha visto:

**La automatización nunca disparó aquí.** No hay ningún aviso de 7, 14 ni 28 días pese a los 23 días
de silencio. Este ticket puede envejecer indefinidamente sin alerta.

**Tu comentario interno del 4 de agosto no menciona a nadie con arroba.** Pediste *"confirmation from
InfoSec that the VM-level screenshot is acceptable as indirect evidence"* al aire. Compáralo con el
comentario de Aimee del 6 de julio, que sí etiquetó a Josh Imler, John Mason, Ricardo Calhoun, Derek
Bringewatt y Matthew Dennison. Probablemente nadie lo leyó.

Y hay una promesa rota que el cliente puede sacar: Camila escribió el 22 de julio *"We'll go ahead
and close this ticket out on July 29th"*. Nunca se cerró y nunca se le dijo que la fecha se retiró.

**Acción:** reescribe el comentario interno mencionando a Matthew Dennison y a InfoSec Operations. En
paralelo escribe a Tyler Aken y a Matt Reid.

## 10. RCS-28289 Vitamin Shoppe, Blocked Users
Medium, Under Customer Review. **Puedes avanzar sin esperar a Scot.**

`inbox/2026-08-26-rcs-28556-zscaler-toronto-mismo-24-que-ahold.md` ya dice: *"RCS-28289 cierra con el
mismo cambio, es de Juan"*. Causa raíz documentada: default block de Cloudflare rechazando tráfico
Zscaler desde Canadá, mismo /24 que RCS-28059. El ticket lleva label `Uni_Jul_26_WAFAccess`. Nada de
eso está en Jira.

**Acción:** pega el comentario interno conectando con RCS-28059, RCS-28556 y ENG-7176, y crea los
enlaces. Con eso deja de depender de la captura de Scot.

## 11. RCS-28122 Blain's, cambios de usuarios
Medium, Under Customer Review. 8 días sin update, viola la cadencia semanal.

Kiran Vadday dejó el 13 de agosto un SELECT que compara `incident.LPUser2.SecurityID` contra
`membership.Users.SecurityID` marcando OK o MISMATCH. **Nadie lo corrió.**

Prometiste el 6 de agosto sobre las fotos del Compliance Audit: *"that is a different area of the
system, so I am tracking it separately"*. No existe ese ticket separado.

**Acción:** corre el SELECT filtrando MISMATCH. Con el dato cierras Admin Tools sin depender del
*"I think we have gotten the changes taken care of"* de James. Y abre el ticket de las fotos.

## 12. RCS-27765 Winn-Dixie, Data file check
Medium, Under Customer Review. El bot no corre aquí tampoco.

El 25 de agosto pegaste una versión de dos frases. El bloque completo del
`inbox/2026-08-24-rcs-27765-hilo-partido-email.md` nunca entró: la tabla de conteos de la tienda 358
con 773 transacciones el 25/06 contra 2323 el 24/06 y 2421 el 26/06, y la corrección del diagnóstico
SFTP contra Ingestion API.

**Dato que envejece:** el reenvío del 25/06 llega a 60 días. Si hay rechazo por antigüedad de
transacción, eso es un hallazgo nuevo y conviene medirlo antes de que IT reenvíe.

**Acción:** pega el bloque completo. Fija una fecha de revisión del hilo de correo.

## 13. RCS-28482 ADUSA, campos en gris en Izenda
Low, P1 por cuenta, Work in progress. **No le escribas.** Cerraste ayer con *"I need nothing from you
on this one"*. Un segundo mensaje de estado sin hallazgo resta.

Datos ya recogidos: los reportes afectados son "PBI - Current Location Listing (Jim Cosseboom Test)"
y "Outlook Export (Jim Cosseboom Test)", uno clon del otro. La vista afectada muestra checkbox
Distinct y selector Results donde la que funciona muestra Records.

**Acción:** verifica en Izenda el tipo de reporte y los permisos de esos dos contra uno que sí
exponga la pestaña MISC.

## 14. RCS-28327 Delhaize, Loyalty Discounts
Medium, P1 por cuenta, Work in progress. Comentario de estado publicado hoy, el reloj de cara al
cliente está limpio.

Edwin dejó una recomendación el 20 de agosto que nadie ejecutó: *"worth flagging to
Engineering/DataOps as a possible systemic risk for other clients migrated V2→V3"*.

**Acción:** los pasos A a D de `inbox/2026-08-24-rcs-28327-validacion-composer.md`. Empieza por el
field ID en Composer, porque si la columna está atada a `code` la teoría de Edwin cae entera.

## 15. RCS-28581 Camping World, POS number regresó al mapeo viejo
Medium, Under Support Review. Lo tomaste hoy. El ticket **no tiene descripción, solo dos imágenes.**

**Acción:** pídele a James McKenna números de transacción concretos con el mapeo viejo, el rango de
fechas, y cuáles sí muestran el correcto. Él mismo planteó la hipótesis del periodo de datos, así que
la petición es legítima y no traslada trabajo gratuito.

## 16. RCS-28496 PVH, fallos de login
Medium, Under Customer Review. **Error a corregir:** tu comentario del 21 de agosto saluda a
"Yannick" y el reporter es **Bob Dunphy**.

Rajith pidió siete datos el 20 de agosto y el cliente no ha escrito nunca en el ticket.

**Acción:** follow up a Bob Dunphy reduciendo las siete preguntas a tres: texto exacto del error, dos
o tres números de tienda con cuentas de ejemplo, y fecha de inicio.

## 17. RCS-28282 Co-op, bloqueo intermitente
Medium, Under Customer Review. Esperas la lista de países desde el 21 de agosto.

**Acción:** en vez de repetir la pregunta abierta, ofrécele un punto de partida. Reino Unido más los
países desde donde operan sus usuarios remotos, para que solo tenga que decir sí o añadir. Una
pregunta cerrada se contesta, una abierta se pospone.

---

# Por dónde empezar

**RCS-28294.** Le dijiste a Vallarta el 25 de agosto que el caso está con ingeniería y no lo está.
Es la única deuda de la cola donde el riesgo no es tardanza sino credibilidad, el material está
armado desde hace dos días, y se resuelve con una transición y un pegado.

Después RCS-28093, que es ADUSA, tiene la respuesta escrita y hay un ingeniero parado esperándote
hace seis días.

# Patrón que se repite y conviene cortar

Seis tickets tienen el trabajo técnico terminado viviendo en `inbox/` mientras Jira muestra dos
frases: 28093, 28294, 28289, 27765, 28153 y 28327. El cuello de botella de tu cola no es la
investigación. Es el pegado.
