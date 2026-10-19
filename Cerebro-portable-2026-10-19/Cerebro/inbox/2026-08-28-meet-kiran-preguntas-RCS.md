# Preguntas sobre los RCS donde Kiran metió mano

Este es el lado que faltaba. Aquí es donde está el argumento de verdad: no es que Kiran
arregle bugs de código, es que **entra a tus tickets de soporte y corre DML que tu equipo
podía correr.**

Inglés para leer. Español para saber qué estás preguntando.

Aviso: las fechas y acciones vienen del cerebro y están fechadas. El estado actual de cada
ticket verifícalo en Jira antes de afirmarlo en la llamada.

---

## EL CASO ESTRELLA. Con este abres

### RCS-28342, Anthony Lopez, ADUSA

El 14 de agosto a las 5:56 p.m. Kiran entró a **tu** ticket y encontró un tercer UserID: el
correcto de la base vieja era **1194761**, ni 11139 ni 1789032. El login de la entrada 11139
era `5701194761`, con el UserID bueno embebido.

Lo que hizo, textual: corrigió el correo en `LPUser2`, apuntó `membership.Users` al
IncidentUserID correcto poniendo `UserName` y `SupervisorFlag = 1`, e insertó la fila que
faltaba en `secure.LocationHierarchyUserAssignments`, LocationId 8031.

**Los tres son UPDATE e INSERT sobre tablas donde tú tienes escritura. Cero código. Cero
ALTER. Cero despliegue.**

**EN**
> "On August 14 you went into RCS-28342 and fixed Anthony Lopez yourself. You corrected the
> email in LPUser2, pointed membership.Users at the right IncidentUserID with UserName and
> SupervisorFlag, and inserted the missing row in
> `secure.LocationHierarchyUserAssignments`. All three are writes to tables I already have
> access to. What stopped you from handing that back to me as three statements? Was it
> faster to just do it, or did you not think Support could?"

**ES**
El 14 de agosto entraste a RCS-28342 y arreglaste a Anthony Lopez tú misma. Corregiste el
correo en LPUser2, apuntaste membership.Users al IncidentUserID correcto con UserName y
SupervisorFlag, e insertaste la fila faltante en `secure.LocationHierarchyUserAssignments`.
Los tres son escrituras a tablas donde ya tengo acceso. ¿Qué impidió devolvérmelo como tres
sentencias? ¿Fue más rápido hacerlo, o no pensaste que soporte pudiera?

**Y hay una contradicción abierta que puedes usar:** en la llamada Leigh Ann dijo que hay más
de un Anthony Lopez, personas distintas. Kiran lo trató como una sola persona con varios
correos, "Due to multiple email addresses, the UserID that was matched was erroneous". Eso se
resuelve contando filas de `membership.Users` para ese nombre. Es un SELECT. Ofrécete a
correrlo.

---

## Los que también eran DML tuyo

### RCS-28177, ADUSA, búsquedas con número en el correo

Kiran alineó 44 filas. Jonathan Wright quedó bien. **Pero ADUSA no quedó limpio:** quedaron
20 usuarios reales sin contraparte en LPUser2, 18 sin rastro por ninguna llave y 2 con la
identidad vieja de Ahold. El update no los podía alcanzar. Se asignó a Viraj, no a ti.

**EN**
> "You aligned 44 rows here, but 20 real ADUSA users were left with no counterpart in
> LPUser2 — 18 with no trace by any key and 2 carrying the old Ahold identity. Your update
> couldn't reach them. That leftover is exactly the kind of case-by-case reconciliation my
> team can grind through. Can we own the tail on these instead of it going back to
> Engineering?"

**ES**
Alineaste 44 filas aquí, pero quedaron 20 usuarios reales de ADUSA sin contraparte en
LPUser2: 18 sin rastro por ninguna llave y 2 con la identidad vieja de Ahold. Tu update no
los alcanzaba. Ese remanente es exactamente el tipo de reconciliación caso por caso que mi
equipo puede moler. ¿Podemos quedarnos con la cola de estos en vez de que vuelva a
ingeniería?

---

### RCS-28379, Delhaize, Case Owner y Creator en blanco

Kiran hizo el mapeo UserID contra LoginID revisando alrededor de 100 registros de MasterCase
y Shoplifting.

**EN**
> "You did the UserID-to-LoginID mapping by hand across about 100 MasterCase and Shoplifting
> records. That's volume work, not judgment work. If you give me the matching rule, my team
> takes the next hundred. What's the rule?"

**ES**
Hiciste el mapeo UserID contra LoginID a mano sobre unos 100 registros de MasterCase y
Shoplifting. Eso es trabajo de volumen, no de criterio. Si me das la regla de emparejamiento,
mi equipo se lleva los próximos cien. ¿Cuál es la regla?

---

### RCS-28256, Tailored Brands, los tres feature flags

El 10 de agosto, a petición de Matt, Kiran corrió la verificación de los tres feature flags
en la base del cliente 209 y publicó la captura. **Tú tienes Feature Flags y Config Items en
el Control Panel bajo el rol Engineers, y tienes lectura a esa base.** Esa verificación era
tuya y casi la repites por no haber leído el hilo.

**EN**
> "On August 10 Matt asked you to verify three feature flags on the 209 database and you
> posted the screenshot. I have Feature Flags and Config Items in Control Panel under the
> Engineers role, and read access to that database. Why did that request go to you? Is there
> something about reading flags at the database level that Support isn't supposed to do?"

**ES**
El 10 de agosto Matt te pidió verificar tres feature flags en la base del 209 y publicaste la
captura. Yo tengo Feature Flags y Config Items en el Control Panel bajo el rol Engineers, y
lectura a esa base. ¿Por qué ese pedido fue a ti? ¿Hay algo sobre leer flags a nivel de base
de datos que soporte no deba hacer?

**Ojo, hay un cabo suelto para mencionar:** `EnableBlobAppendLogging` está en False en el 209,
editado el 10 ago 14:09:57 UTC, y nadie ha confirmado cuál debería ser el valor esperado.

---

### RCS-28196, el caso del ALTER

Este es el único de todo el barrido donde el bloqueo sí fue un permiso. El cambio de default
de columna que hacía Gabor no está en producción, hay que aplicarlo a mano, y el asignado no
tiene permisos de ALTER. Depende de John.

**EN**
> "This is the one case in three weeks where the blocker was genuinely a permission. Gabor's
> column default change isn't in prod, it has to be applied by hand, and the assignee has no
> ALTER. It's been sitting on John. Who on my team should have ALTER, or should we always
> route DDL to a named person?"

**ES**
Este es el único caso en tres semanas donde el bloqueo sí fue un permiso de verdad. El cambio
de default de columna de Gabor no está en prod, hay que aplicarlo a mano, y el asignado no
tiene ALTER. Lleva parado en John. ¿Quién de mi equipo debería tener ALTER, o siempre
enrutamos DDL a una persona con nombre?

---

## Los que Kiran te devolvió, y tenía razón

Reconocerlos primero te da autoridad para todo lo demás.

### RCS-28093 y la regla de la URL

Kiran, en la llamada:
> "can you please give us the URL of the incident you're trying, the link to the workbench.
> All we need is this."

Y en otro punto: "with the url in hand, we can verify what our queries are looking at". Sin
URL no se puede saber qué consulta corre la página. Se perdieron horas reproduciendo a ciegas.

**EN**
> "You told us on RCS-28093: give us the URL, the link to the workbench, that's all we need.
> We lost hours reproducing blind before that. I want to turn that into a hard intake rule on
> my side — URL, user, screenshot, no exceptions. Is there a fourth thing you'd add?"

**ES**
Nos dijiste en RCS-28093: dennos la URL, el link al workbench, es todo lo que necesitamos.
Perdimos horas reproduciendo a ciegas antes de eso. Quiero volverlo regla dura de admisión de
mi lado: URL, usuario, captura, sin excepciones. ¿Hay una cuarta cosa que agregarías?

---

### RCS-28321, Boot Barn, el diagnóstico de David

David atribuyó el 500 de `SystemSelect.aspx` a un registro faltante de clave de cifrado en la
tabla Options para `/bootbarn`. Kiran lo descartó doce días después:
> "Hi @David Vargas I do not believe this is a code issue. Could you please replicate the
> problem and share the reproduction steps with me."

**EN**
> "David called this a missing Options table record and you dismissed it twelve days later.
> He read a real error string and promoted it to root cause without a counterfactual. That's
> a habit I want to break on my team. When you get a root cause claim from Support, what
> would make you trust it on first read?"

**ES**
David dijo que era un registro faltante en la tabla Options y tú lo descartaste doce días
después. Leyó un error real y lo promovió a causa raíz sin contrafactual. Ese hábito lo quiero
romper en mi equipo. Cuando te llega una afirmación de causa raíz desde soporte, ¿qué haría
que le creyeras a la primera lectura?

---

### RCS-28084, la hipótesis del hotfix faltante

Kiran, 10 de agosto, cortando de raíz:
> "No. Once deployed, all the clients get the same code."

Úsalo tú mismo como ejemplo de algo que ya no hay que volver a preguntar.

---

## Donde soporte cerró solo y Kiran no pudo

### RCS-27542, Boot Barn, audit completion

Kiran no reprodujo porque probó la tienda 0456, audit 90535, que sí guardaba, mientras la
0286, audit 90380, fallaba. Es data-dependent: `DBNull` donde se espera string en
`Audit_UpdateAuditStatus`, `UpdateAuditStatus.aspx.vb` línea 416. Y el archivo vive en el
servidor `F:\IIS\Clients\bootbarn\`, **no en el repositorio.**

El workaround lo encontró soporte: reguardar Audit Date y End Date en Modify Audit Date/Times
y después Mark Audit Completed. El re-guardado repuebla el campo NULL.

**EN**
> "You couldn't reproduce this because you tested store 0456, which saves fine, while 0286
> fails — it's data-dependent on a NULL. Support found the workaround. Two things: first,
> that file lives on the server at `F:\IIS\Clients\bootbarn\`, not in the repo, so who owns
> per-client files like that? Second, when Support finds a workaround, what does it take to
> make it official instead of a one-off?"

**ES**
No pudiste reproducirlo porque probaste la tienda 0456, que guarda bien, mientras la 0286
falla: depende del dato, de un NULL. Soporte encontró el workaround. Dos cosas: primero, ese
archivo vive en el servidor en `F:\IIS\Clients\bootbarn\`, no en el repo, ¿quién es dueño de
los archivos por cliente así? Segundo, cuando soporte encuentra un workaround, ¿qué hace
falta para volverlo oficial en vez de un caso aislado?

---

## Las reglas de Kiran que ya seguimos, y las que hay que cerrar

### La regla de la vista lpuser

Textual de Kiran: **"Secure.lhua y lpuser view both must be checked"**. Las dos, no una.
`secure.LocationHierarchyUserAssignments` es destino de migración, no la capa que decide si
un usuario puede crear un caso. Para síntoma funcional, la vista primero.

Y las llaves de comparación, nunca por ID numérico: `membership.Users` por `username`,
`incident.lpuser` por `loginid` o `email`, `incident.lpuser2` por `loginid` y `emailaddress`.

**EN**
> "You gave us the schema rules on July 30 after we kept looking at different layers of the
> same problem — check both lhua and the lpuser view, never join on numeric ID, always
> report both join paths in separate columns. That's the single most useful thing anyone in
> Engineering has handed my team. Is that written down anywhere, or does it only exist in
> that Teams thread?"

**ES**
Nos diste las reglas de esquema el 30 de julio después de que estuviéramos mirando capas
distintas del mismo problema: revisar lhua y la vista lpuser, nunca unir por ID numérico,
siempre reportar las dos rutas de join en columnas separadas. Es lo más útil que alguien de
ingeniería le ha dado a mi equipo. ¿Está escrito en algún lado, o solo existe en ese hilo de
Teams?

---

### RCS-28153 y RCS-28346, el timeout de sesión

Contradicción abierta y sin resolver: **Kiran dijo 30, Engineering dijo 60 y 240.** El 28346
entró el 13 de agosto a las 00:52, Stater Bros, escalado por J.R., diciendo que la sesión
sigue expirando antes de los 240 minutos. O sea que el arreglo del 28153 no está tomando.

**EN**
> "On session timeout you said 30 and Engineering said 60 and 240 on RCS-28153. Then
> RCS-28346 came in on August 13 saying Stater Bros still expires before 240, so whatever we
> set isn't taking. What is the actual per-tenant session timeout, and where does the
> effective value live — the config item, or CustomerEditedValue?"

**ES**
En el timeout de sesión tú dijiste 30 y Engineering dijo 60 y 240 en RCS-28153. Después entró
RCS-28346 el 13 de agosto diciendo que Stater Bros sigue expirando antes de los 240, o sea
que lo que pusimos no está tomando. ¿Cuál es el timeout de sesión real por tenant, y dónde
vive el valor efectivo, en el config item o en CustomerEditedValue?

**Por qué importa:** si el valor efectivo puede quedar solo en `CustomerEditedValue`, eso es
una trampa que soporte pisa cada vez. Necesitas la regla escrita.

---

### RCS-28124, la descarga de PDF

Kiran confirmó la causa raíz en Teams el 10 de agosto: el módulo ERMS sube los archivos al
directorio de lpms. Mitigación inmediata: copiar los archivos al lugar correcto.

**EN**
> "You confirmed the root cause on August 10 — ERMS uploads to the lpms directory. The
> mitigation was copying the files to the right place, and Support did that copy for Big Y.
> Files uploaded before the fix are stuck at the old path permanently. Can my team get
> credentials to the production storage account and an inventory query, so we do the copy
> without opening a ticket every time?"

**ES**
Confirmaste la causa raíz el 10 de agosto: ERMS sube al directorio lpms. La mitigación era
copiar los archivos al lugar correcto, y soporte hizo esa copia para Big Y. Los archivos
subidos antes del fix quedan clavados en la ruta vieja de forma permanente. ¿Puede mi equipo
tener credenciales del storage account de producción y una consulta de inventario, para hacer
la copia sin abrir un ticket cada vez?

---

### El truco de Screen Designer, y su advertencia

Kiran te dio el atajo para pantallas rotas o en 404: `?ADMIN=9QQP` más Build All Screens. Y
hay una advertencia registrada: en Santikos, RCS-28022, el rebuild del 31 de julio coincidió
con que la lista de incident types quedó en cero. Secuencia observada, causalidad no probada.

**EN**
> "You gave us the `?ADMIN=9QQP` plus Build All Screens shortcut for broken screens. But on
> Santikos, RCS-28022, the July 31 rebuild coincided with the incident types list going to
> zero. Observed sequence, causality unproven. Is Build All Screens safe on a migrated
> tenant or not? Right now my team is afraid to use a tool you gave us."

**ES**
Nos diste el atajo `?ADMIN=9QQP` más Build All Screens para pantallas rotas. Pero en Santikos,
RCS-28022, el rebuild del 31 de julio coincidió con que la lista de incident types quedó en
cero. Secuencia observada, causalidad no probada. ¿Build All Screens es seguro en un tenant
migrado o no? Ahora mismo mi equipo tiene miedo de usar una herramienta que tú nos diste.

---

## La pregunta que resume todo el lado RCS

**EN**
> "Here's my count. In the last three weeks you personally went into Support tickets and ran
> writes — RCS-28342, RCS-28177, RCS-28379 — that hit LPUser2, membership.Users and
> `secure.LocationHierarchyUserAssignments`. Every one of those is a table I have write
> access to. None of them needed ALTER, code, or a deploy. That's not escalation, that's
> Engineering doing Support's job because the path wasn't defined. What has to be true for
> the next RCS-28342 to stop on my desk?"

**ES**
Este es mi conteo. En las últimas tres semanas entraste personalmente a tickets de soporte y
corriste escrituras, RCS-28342, RCS-28177, RCS-28379, que tocan LPUser2, membership.Users y
`secure.LocationHierarchyUserAssignments`. Todas son tablas donde tengo escritura. Ninguna
necesitó ALTER, ni código, ni despliegue. Eso no es escalación, es ingeniería haciendo el
trabajo de soporte porque el camino no estaba definido. ¿Qué tiene que ser cierto para que el
próximo RCS-28342 se quede en mi escritorio?

---

## Los cinco RCS que nombras si te piden ejemplos

| Ticket | Qué hizo Kiran | Veredicto |
|---|---|---|
| RCS-28342 | UPDATE a LPUser2 y membership.Users, INSERT en lhua | Era tuyo. Puro DML |
| RCS-28177 | Alineó 44 filas, dejó 20 sin resolver | Era tuyo, y la cola sigue abierta |
| RCS-28379 | Mapeo manual de ~100 registros | Trabajo de volumen, era tuyo |
| RCS-28256 | Verificó 3 feature flags en la base del 209 | Tienes el rol y la lectura |
| RCS-28196 | Bloqueado, nadie tiene ALTER | El único bloqueo real de permisos |
