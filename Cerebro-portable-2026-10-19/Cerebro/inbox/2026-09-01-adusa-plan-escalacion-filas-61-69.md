# ADUSA. Qué escala a ingeniería y qué no. Filas 61 a 69 del interno

Fecha: martes 1 sep 2026.
Los nueve tickets leídos en Jira en vivo, descripción y comentarios completos, vía los
hipervínculos de la columna A del interno. Los enlaces sí funcionan y los nueve están consultados.
Jira quedó en solo lectura. Aquí no se movió nada.
Contenido verificado por un segundo pase contra Jira, incluido el changelog de transiciones.

**El criterio es el de Matt, y J.R. lo dejó por escrito dentro de un ticket.** RCS-28683, 1 sep
10:47, J.R. Teagle: *"once you're able to get steps to reproduce in here, let's please get an ENG
ticket created for this and linked (and sent to @Matthew Kamminga)."* Defecto más pasos de
reproducción escritos en el ticket. Sin las dos cosas no escala.

---

## Tabla de decisión

| Fila | Ticket | Status hoy | Assignee | ¿Defecto? | ¿Pasos escritos? | Decisión |
|---|---|---|---|---|---|---|
| 61 | RCS-28482 | Work in progress | **Juan** | Configuración probable, sin verificar | No | **No escala.** Appriss nunca lo reprodujo |
| 62 | RCS-28519 | Closed | Diego Buelvas | — | — | Cerrado, sin acción |
| 63 | RCS-28533 | Closed | Diego Buelvas | — | — | Cerrado, sin acción |
| 64 | RCS-28667 | Work in progress | Megha Rathi | Indeterminado | No | **No escala.** Falta contestar la pregunta de diseño |
| 65 | RCS-28123 | Work in progress | **Juan** | **No es defecto** | Sí, para el síntoma abierto | **Escala como cambio de producto**, no como bug |
| 66 | RCS-28693 | Work in progress | Vlad Bogus | **Sí, autorización** | No aún, reconstruibles | **Prepara y escala hoy.** Tiene ángulo de seguridad |
| 67 | RCS-28683 | Work in progress | Megha Rathi | Sí, 404 | No | **No escala todavía.** J.R. puso la condición |
| 68 | RCS-28596 | Accepted into Development | Shandana Khan | Sí, confirmado en código | Sí | **Ya escalado.** ENG-7904, Backlog |
| 69 | RCS-28589 | Under Engineering Review | Matthew Kamminga | Candidato en el export | Parcial | **Ya escalado.** Hoy 11:32 |

Uno escala hoy con trabajo previo de una hora. Uno escala por otra ruta. Tres están frenados por
falta de material. Dos ya están arriba. Dos están cerrados.

---

## Corrección al auto-create del ENG, ahora con changelog

Ayer te dije que RCS-28589 no tenía ENG porque la transición se hizo con el assignee equivocado.
**Eso es falso y el changelog lo prueba.** Corrijo, y la corrección invierte el consejo práctico.

`brain/memoria/reference_escalacion_l3_procedimiento.md` dice, línea 13, *"El ENG no se crea a mano.
La transición de estado lo auto-crea"*. **Ese documento está equivocado para este flujo.** Las dos
transiciones observadas:

- RCS-28596 entró a Under Engineering Review el **27 ago 17:07:00**, transición de Ryan Barlow. No
  se creó ningún ENG en ese momento. ENG-7904 apareció **quince horas y dieciocho minutos después**,
  el 28 ago 08:24:59, como clon creado a mano por Shandana Khan.
- RCS-28589 entró a Under Engineering Review el **1 sep 11:32:50**, transición de Ryan Barlow, con
  Shandana como assignee cinco segundos más tarde. Tampoco se auto-creó nada.

La teoría del assignee equivocado cae sola. El assignee **era** Shandana en el momento de la
transición.

**No existe automatización.** Mover el RCS a Under Engineering Review no produce nada por sí solo.
Depende de que alguien actúe, y en estos dos casos ese alguien fue Shandana. No lo conviertas en
regla: ENG-7192 lo creó J.R. Teagle, no ella.

**Qué hacer con eso.** Transiciona y asigna a Shandana, que es la ruta correcta. Después
**persigue el ENG**, porque no va a aparecer solo. Si a las 24 horas no existe, escribe en el
ticket pidiéndolo. Crearlo tú a mano sigue siendo mala idea, produce duplicado cuando Shandana haga
el clon.

---

## Los dos que escalan

### RCS-28693, fila 66. Prepara hoy, escala hoy, y sepáralo

**Assignee Vlad Bogus. No es tuyo. Coordina antes de mover el estado.**

Este ticket trae dos fallos en direcciones opuestas y solo uno está siendo investigado.

**Harrison Xu, sub permisionado.** Giant Food tienda 233, Asset Protection for Giant District 104,
grupo AP Level 2 Ahold. No puede entrar. Vlad sospecha del grupo en Azure del lado cliente, que es
hipótesis viva y no descartada. Pidió un usuario de control y Leigh Ann dio a Kyle Moses.

**Paula Dotson, sobre permisionada. Este es el hallazgo grande y nadie lo está tratando como tal.**
Leigh Ann lo escribió hoy 13:06, verbatim: *"a user that does not have LPMS access was able to
authenticate to the system under the Store Reporter role. That user was Paula Dotson. I checked her
Azure provisioning on this side and she is not provisioned to LPMS and never has been."* Con
capturas de la sesión abierta.

Una identidad sin aprovisionar obtuvo sesión válida en producción con un rol asignado. Un grupo mal
puesto del lado cliente no explica eso, porque no hay grupo. Es la lógica de fallback la que está
entregando rol por defecto a quien no debería autenticar.

**Los pasos todavía no están escritos.** El comentario de Leigh Ann narra lo ocurrido, no lo
enumera. No hay entorno declarado ni URL transcrita. Lo que sí hay es material suficiente para
escribirlos en quince minutos, y ahí el criterio de Matt queda cumplido. Es el único de los tres
frenados que puede desbloquearse hoy.

Aparece además una variable que ningún otro ticket menciona: *"the new URL to sign in"*. Hubo
cambio de endpoint de acceso y la prueba se hizo contra él.

**Lo que hay que hacer, en orden:**

1. **Abrir `LPMS SSO Issue pt 2.docx`**, adjunto de Leigh Ann del 1 sep 09:51, 14.598 bytes. El
   mensaje de error puede estar ahí en texto y ahorrarte la transcripción del PNG.
2. Escribir los pasos del escenario Paula Dotson como pasos numerados en el ticket.
3. Declarar el entorno y transcribir la URL nueva.
4. Hablar con Vlad y con J.R. sobre partirlo en dos. El de Harrison Xu sigue con Vlad comparando
   claims contra Kyle Moses. El de Paula Dotson va por severidad de acceso.
5. Decidir la ruta del de Paula Dotson. Under Engineering Review con Shandana es la ruta normal.
   El doc de Aimee tiene otra para acceso, Under Security Review, que se queda a tu nombre y
   auto-crea INFOSEC. **Esa decisión no la tomes solo. Pregúntale a J.R. hoy.**

**Comentario interno para pegar en RCS-28693, en inglés, listo:**

```
Two separate defects are being tracked in this ticket and they point in opposite directions.

Defect 1, Harrison Xu. User cannot authenticate. Giant Food store 233, Asset Protection for
Giant District 104, group AP Level 2 Ahold. Control user provided by ADUSA is Kyle Moses.
Vlad Bogus is comparing SSO claims between the two. Client-side Azure group membership has not
been ruled out.

Defect 2, Paula Dotson. A user with no LPMS provisioning in Azure, and no history of
provisioning, authenticated successfully and received the Store Reporter role. ADUSA verified
the Azure state on their side and attached screenshots of the open session. Client-side group
membership does not explain this, because there is no group. The fallback logic is granting a
default role to an identity that should be rejected at authentication.

Steps to reproduce defect 2:
1. Select any tenant user with no LPMS provisioning in Azure.
2. Navigate to the new LPMS sign-in URL.
3. Authenticate with that user.
4. Observed: the session opens and the user receives the Store Reporter role.
5. Expected: authentication is refused and no role is granted.

Environment: to be confirmed and recorded here before this moves.

Both defects surfaced against the new sign-in URL. That endpoint change is a variable in both.

Requesting a routing decision on defect 2. It is an access control defect in production and
may belong under Security Review rather than Engineering Review.
```

Antes de pegar: sustituye la descripción de la URL por la URL literal, escribe el entorno, y añade
el texto del mensaje de error de Harrison Xu.

---

### RCS-28123, fila 65. Escala, y no como bug

**Este es tuyo. Nadie más lo va a mover.**

Matt cerró la pregunta hoy 09:50, verbatim: *"Based on my investigation the reassign case does not
provide the popup as explained. Is it possible the user is thinking about Complete case, or some
other action. FYI the reassign path to this page was commented out in code 3.5 years ago
intentionally. If you mark a case complete you do get redirected to a page like this and that
functionality is working as expected."*

**Si la ruta se comentó a propósito hace tres años y medio, restaurarla es cambio de producto, no
corrección de defecto.** Por la regla de ruteo de Aimee eso va al Feedback Portal, o va a ENG con
justificación de negocio. No va como bug.

**El hueco urgente es otro y es visible para el cliente.** El 26 de agosto le escribiste a Jim,
verbatim: *"The missing confirmation and print option is a separate issue. I have logged it, and
engineering is reviewing it now."* **Ese registro no existe.** Se buscó en RCS y en ENG creados
entre el 25 y el 28 de agosto con texto "confirmation" y "print", y no aparece nada de ADUSA. El
único ticket que abriste en esa ventana es RCS-28665, de ASDA. El único enlace de RCS-28123 sigue
siendo ENG-7192, que está Done. Lleva seis días así.

**Cuidado con lo que se le atribuye a ENG-7192.** Su alcance escrito son dos cosas: que la
reasignación quede en Changes/History y que llegue un solo correo. El error de campo vacío tiene
ticket propio, ENG-557, en Backlog, y **siguió reportándose después del deploy**. Chris desplegó el
17 de agosto a las 14:20. Jim reportó el 19 a las 14:40, verbatim: *"the system is not recognizing
that someone is in the assigned to field and is returning an error that "User Cannot be Blank""*.
Matt contestó ese mismo día que no pudo reproducirlo. Lo que sí está confirmado por el cliente es
que el 26 de agosto la asignación funcionaba. No escribas que ENG-7192 cerró el error de validación.

**Dato que no está en el ticket y que la llamada dio por sentado.** Matt escribió *"Complete case,
or some other action"*. Nunca nombró approve. La afirmación de que el popup está atado a approve y
a mark case completed existe solo en la llamada. No la escribas en el tracker como hecho de Jira.

**La queja de fondo sí está escrita, y desde el 13 de agosto.** Leigh Ann, verbatim: *"the screen
goes white and it does not state that the case has been assigned"* y *"I had to go in and do a
refresh on the screen in order for Jim's name to populate into the field."* Eso es falta de
confirmación inmediata. La llamada lo generalizó a reassign. La formulación original es sobre Send
to Approver. Esa diferencia decide si el arreglo es restaurar una pantalla o añadir un refresco.

**Lo que hay que hacer, en orden:**

1. Preguntarle a Leigh Ann si la pantalla que recuerda es la de Mark Case Completed. Es la pregunta
   de Matt del 1 sep y sigue sin respuesta. Bloquea todo lo demás.
2. Pedir evidencia del comportamiento histórico. Ningún adjunto muestra la pantalla con el botón de
   imprimir. Sin captura, ingeniería no tiene contra qué comparar.
3. Cerrar el compromiso del 26 ago. Crear el registro o corregir lo dicho.
4. Decidir con J.R. si va al Feedback Portal como feature o a ENG con justificación de negocio.

**Comentario interno para pegar en RCS-28123, en inglés, listo:**

```
Status split, so the record matches what is actually open.

Confirmed working by ADUSA on 8/26: case assignment itself. ENG-7192 is Done and its recorded
scope is that a reassignment is written to Changes/History and that only one notification email
is sent. The "User Cannot be Blank" validation error is tracked separately under ENG-557, which
is still in Backlog.

Still open: the confirmation screen after assignment. Per Matthew Kamminga on 9/1, the reassign
path to that page was commented out in code 3.5 years ago intentionally. Marking a case complete
does redirect to a page of that kind and works as expected. Restoring the path from reassign is
a product change, not a defect fix, so it needs a business justification rather than a bug
ticket.

Correction to the note posted on 8/26. That note said the missing confirmation and print option
had been logged and was under engineering review. No such record exists. The only link on this
ticket is ENG-7192, which covers a different scope.

Two items are needed before this can be routed:
1. Confirmation from ADUSA on whether the screen they remember is the Mark Case Completed
   screen or a different one.
2. A screenshot of the prior behaviour showing the confirmation text and the print option.

The underlying request from ADUSA, written on 8/13, is that assigning a case returns no
immediate confirmation. The screen goes blank and the Assigned to field only populates after a
manual refresh. That is the requirement to solve, whether the solution is the old screen or an
immediate refresh of the panel.
```

---

## Los tres que no escalan todavía, y qué falta exactamente

### RCS-28683, fila 67. Falta lo que el propio J.R. condicionó

Es el que más cerca está en claridad de defecto. Un submit devuelve 404 y aun así persiste el caso.
Eso no lo produce un permiso ni un dato de tenant.

**No tiene pasos de reproducción y J.R. lo dijo dentro del ticket.** Falta, literalmente: número
del caso de origen, usuario que lo ejecutó, tienda, marca, rol, entorno, qué ítems se marcaron para
copiar, el endpoint que devolvió 404, y si el caso creado queda íntegro o parcial.

Assignee Megha Rathi. Coordina con ella, no lo tomes por encima.

Hay un segundo elemento embebido de menor peso. Verbatim de la descripción: *"it has to be selected
in order to add additional information to the case."* Eso es fricción de flujo, no fallo. Sepáralo
o diluye el 404.

**Cuando los pasos estén escritos:** Under Engineering Review, Shandana Khan, y avisar a Matt como
pidió J.R.

### RCS-28482, fila 61. Appriss nunca lo reprodujo

**Este es tuyo.**

La única nota técnica del ticket es del 24 de agosto y se autodescalifica. Verbatim tuyo: *"That is
a reading of the screenshots, not verified."* No hay una sola línea que diga que alguien de Appriss
abrió esos reportes en Izenda. Eso no pasa el estándar de Aimee.

**Tienes una promesa abierta con Jim desde hace seis días.** El 26 de agosto escribiste *"I have
nothing to report yet on what makes the tab render greyed out. I will come back to you when I do."*
Sin fecha. Jim confirmó ese mismo día que el reporte corre bien y que solo no es editable. Sin
actividad desde entonces.

El cliente ya corrigió el rumbo una vez. El 22 de agosto, verbatim: *"I think there is a
misunderstanding, what I am trying to do is go to the MISC tab at the top to change report
distribution which I am unable to access. That info is not in the Data Sources."* Es la pestaña
MISC, para cambiar distribución del reporte.

**Lo que falta antes de escalar:**

1. Reproducirlo tú en el tenant AHL/DLZ y escribirlo en el ticket.
2. Registrar el tipo de reporte de `PBI - Current Location Listing (Jim Cosseboom Test)` y de
   `Outlook Export (Jim Cosseboom Test)`, y el de un reporte de control nombrado que sí muestre
   MISC. Nombrarlo, no decir "a working report".
3. Comparar rol y permisos de Izenda del usuario de Jim contra el de un reporte que sí funciona.
4. Probar si al recrear el reporte desde cero aparece MISC. Ese es el workaround candidato y nadie
   lo probó.
5. Declarar el entorno.

Tu propia hipótesis del 24 de agosto es la línea de investigación buena y solo hay que ejecutarla:
la vista afectada muestra Data Sources, Fields y Preview, mientras la sana muestra el set completo
con MISC, y la afectada muestra un checkbox Distinct y un selector Results donde la sana muestra
Records. Eso apunta a que el set de pestañas deriva del tipo de reporte.

### RCS-28667, fila 64. El usuario ya está desbloqueado. Lo abierto es la pregunta

**Assignee Megha Rathi. Coordina antes de tocarlo.**

Encuadre correcto, y no es el de un caso vivo. **Gabriel Quist ya trabaja.** La propia descripción
lo cierra, verbatim: *"The latest information I received from the user since adding a hierarchy is:
I am able to select locations now and create cases. Thank you. Gabriel Quist"*. El workaround
manual funcionó y se aplicó.

Lo único abierto es una pregunta de diseño dirigida a Appriss, verbatim de Leigh Ann: *"does this
fall under the admin functions to set up a hierarchy for each new user or should that be set in set
up configuration?"* Tres días sin respuesta.

**Esa respuesta es la que decide la clasificación.** Si el diseño dice que la jerarquía debe llegar
poblada desde el claim de SSO o desde el store file, el vacío es fallo del pipeline y es defecto. Si
el diseño dice que la pone el admin del cliente, es tarea de administración y el ticket se cierra
con una respuesta, no con un ENG.

No hay pasos de reproducción, no hay entorno, no hay una sola nota de troubleshooting de Appriss.
Un acuse enlatado y una nota de espera de Megha del 31 ago sin hallazgo y sin fecha.

Faltan además marca, tienda y rol de Gabriel Quist, y un segundo usuario afectado. El plural "new
users" no está respaldado por ningún segundo nombre.

**Sobre agrupar 28693 con este hilo, cuidado.** RCS-28415, RCS-28519 y RCS-28667 fallan después de
autenticar, el usuario entra y el selector está vacío. RCS-28693 falla en la autenticación. Y la
dirección del error es opuesta, sub permisionamiento contra sobre permisionamiento. El dato que
decide no está en ningún ticket: si la ubicación viaja dentro del claim SAML u OIDC, o si se
resuelve del lado servidor después de autenticar. Deja 28693 en fila propia y marca el patrón como
pendiente de confirmar.

---

## Los dos que ya están arriba, y qué sigue faltando

### RCS-28596, fila 68. Escalado completo. El hueco es el silencio

ENG-7904 existe, es clon del RCS, hereda la causa raíz completa y una propuesta de fix concreta.
Ingeniería no necesita pedir nada más. Ryan Barlow lo dejó cerrado el 27 de agosto, verbatim: *"Root
cause is confirmed to be code, not data."* La causa: el query hace LEFT JOIN de Employee a Store por
StoreNumber, y en Delhaize los números de tienda solo son únicos por Division más StoreNo, así que
un empleado empareja con varias filas de Store. Archivo afectado `Popups/EELookupList.aspx.vb`.
Precedente ya resuelto igual para Lux.

**Tres cosas pendientes, ninguna técnica:**

1. **Jim reportó el 26 de agosto y no ha recibido nada desde el acuse de Sanath Acharya. Seis
   días.** Ese acuse es texto enlatado con autor humano, no automatización. Nadie le ha escrito.
2. ENG-7904 está en Backlog, sin sprint y con fixVersions vacío. No hay nada que prometerle.
3. **No hay workaround documentado y es la primera pregunta que va a hacer.** Confirma con
   ingeniería si las dos filas duplicadas apuntan al mismo EmployeeID. Si es así, seleccionar
   cualquiera es equivalente, y eso se le dice hoy.

### RCS-28589, fila 69. Escalado hoy. Falta la pregunta que decide el caso

**Este ticket ya se había dado por cerrado una vez.** Estuvo Completed con resolution Resolved desde
el 27 de agosto 12:13. Lo reabrió Automation for Jira hoy a las 10:29:43 cuando Jim comentó. Esa es
la historia detrás de lo que dijo Leanne en la llamada sobre que lo cerraron y solo estaba resuelto
en parte.

Ryan Barlow lo dejó claro hoy 11:32, verbatim: *"The actual values do not contain an apostrophe in
the database. The apostrophes are either being added via excel, or through the export function.
This ticket needs to go to engineering to review the export to file functionality."*

**Dos causas alternativas vivas, y nadie hizo la pregunta que las separa: con qué abrió Jim el
archivo exportado.** Excel muestra un apóstrofe delante de valores numéricos guardados como texto.
Si Jim lo abrió en Excel, esto puede ser artefacto de la herramienta y no defecto de plataforma.
Sin esa respuesta, ingeniería arranca sin poder descartar lo primero que hay que descartar.

La capa uno ya está cerrada: el apóstrofe entraba en el archivo del propio cliente, Ryan limpió 432
registros y añadió una regla que lo ignora en `EASFrequency` y `CCTVIPAddress`. Esa es la mitad que
el cliente considera resuelta.

**Pídele a Jim hoy, en el mismo mensaje:** con qué abrió el archivo, y el archivo exportado en
crudo como adjunto sin abrirlo ni guardarlo desde Excel.

**Comentario para pegar en RCS-28589, en inglés, listo:**

```
One question decides where this goes next, and it has not been asked yet.

Ryan Barlow confirmed on 9/1 that the stored values carry no apostrophe. Two causes remain
open: the export function inserts the character, or Excel displays it because the value is
stored as text. Excel shows a leading apostrophe for text formatted numbers, so that path has
to be ruled out before engineering treats this as a platform defect.

Requested from ADUSA:
1. Confirm whether the exported location listing was opened in Excel or in a plain text editor.
2. Attach the raw exported file to this ticket, without opening or saving it from Excel.

Also needed to scope the engineering review: the exact screen and menu used to run the export,
the file format produced, and whether the behaviour affects Latitude and CCTVIPAddress as well
as Longitude.
```

---

## Los dos cerrados, filas 62 y 63

**RCS-28519**, Closed, Resolved, `Support Resolved - Fixed Configuration`, cerrado el 26 de agosto
por Diego Buelvas. La confirmación la relayó Jim Cosseboom, verbatim: *"Both Deborah Jean and Sammy
Rivera tested and it worked. Ticket can be closed. Thank you!"* Ninguno de los dos usuarios comentó
el ticket. **La causa raíz no está escrita.** Nadie registró qué se cambió ni en qué cuenta. La
hipótesis de que es el mismo caso de RCS-28415 quedó sin confirmar ni descartar.

**RCS-28533**, Closed, Resolved, `Customer Resolved - Customer Requested Ticket to be Closed`,
cerrado el 26 de agosto. Ralph Valentine lo arregló por su cuenta sin decir qué tocó. Nada apunta a
defecto de producto. Queda como incidencia local de estación de trabajo sin diagnóstico.

Los dos van a la fila del interno con los campos completos y escondidos, que es la convención.
Ninguno necesita más trabajo.

---

## Orden de ejecución para hoy

1. **Pregúntale a J.R. por la ruta de RCS-28693 escenario Paula Dotson.** Engineering Review o
   Security Review. Es lo único que no puedes decidir solo y es lo más serio del lote.
2. **Escribe los pasos de Paula Dotson en el ticket** y abre el docx adjunto por si trae el error en
   texto. Es una hora de trabajo y desbloquea la única escalación limpia del día.
3. **Cierra el hueco de RCS-28123.** Seis días con un compromiso sin respaldo en Jira.
4. **Contéstale a Jim en RCS-28596.** Seis días de silencio sobre un ticket con causa raíz
   confirmada. Es el que peor se ve.
5. **Contéstale a Jim en RCS-28482.** Seis días con una promesa sin fecha, y es tuyo.
6. **Pide el archivo crudo y la pregunta de Excel en RCS-28589.**
7. **Coordina con Megha** el 28683 y el 28667, y con Vlad el 28693.
8. **Después de que los estados se muevan, actualizamos el tracker.** Las filas 61 a 69 quedan
   listas de una vez con los estados nuevos, sin tener que tocarlas dos veces.

---

## Lo que no se puede escribir en el tracker todavía

Cinco cosas que aparecen en la llamada o en tu propia nota y no tienen respaldo en Jira. No las
pongas como hechos:

- Que el popup de RCS-28123 esté atado a **approve**. Matt nombró Complete case y dejó el resto en
  "some other action".
- Que ENG-7192 haya cerrado el error de validación de campo vacío. Ese tiene ticket propio,
  ENG-557, y siguió reportándose dos días después del deploy.
- Que RCS-28693 pertenezca al hilo de provisioning de 28415, 28519 y 28667. Falla en otra etapa y
  en dirección opuesta.
- Que la causa de RCS-28482 sea el tipo de reporte. Es tu hipótesis y está marcada como no
  verificada por ti mismo.
- Que el apóstrofe de RCS-28589 lo meta el export. Ryan dejó dos causas abiertas.

Verifica también un nombre antes de escribir. La transcripción dice **Leanne**. El ticket nombra a
**Leigh Ann Stubbs**. Si son la misma persona, corrige la grafía en todo lo que salga de aquí.

---

## Enlaces

- `inbox/2026-09-01-adusa-dos-reuniones-y-el-encargo-de-jr.md`
- `brain/memoria/reference_escalacion_l3_procedimiento.md`, con la salvedad del auto-create de
  arriba, que ese documento tiene mal
- `brain/memoria/reference_tracker_adusa_formato.md`
