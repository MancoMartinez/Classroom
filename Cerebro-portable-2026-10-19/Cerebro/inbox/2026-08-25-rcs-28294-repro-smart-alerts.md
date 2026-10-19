# RCS-28294 Vallarta, Smart Alerts. Como reproducirlo y que mandarle a Engineering

Fecha: 2026-08-25
Estado en Jira al momento de escribir: Work in progress, assignee Luis Hernandez, prioridad Medium,
label `Uni_Jul_26_AlertsNotifications`. Reporta Tatiana Barcenas.
Adjuntos guardados en `adjuntos/RCS-28294/`.

## Lo primero, hay un problema con la respuesta que ya salio

El 12 ago David Vargas le dijo a la clienta que la alerta funciono bien porque el caso se completo
el 8/11 a las 12:23 AM. El PDF que Tatiana devolvio ese mismo dia contradice eso.

Cita del PDF `2026-ADUP-40-96.pdf`, encabezado:

    Case Stage: Pending Report to be Completed
    HR Case Status: Open

El caso nunca se completo. La alerta salio igual. La explicacion que se le dio a la clienta no se
sostiene y ella ya lo señalo. Cualquier cosa que se escriba ahora arranca reconociendo eso.

## Lo que la evidencia establece

Fuentes: el PDF del reporte, la captura del Change History y los nueve comentarios de Jira.

1. El caso 2026-ADUP-40-96 sigue en Pending Report to be Completed. Verificado contra el PDF.
2. Los 23 eventos del Change History arrancan el 8/11/2026 a las 12:23 AM. La captura esta
   ordenada descendente y el scroll esta al fondo, asi que el `SAVE.CASE 8/11/2026 12:23 AM` de
   VALDEZ, VIANNEY es el evento mas viejo de los 23.
3. El mismo PDF dice `Date Case Reported: 8/10/2026` y `Date Received by HR: 8/10/2026`.
4. Punto 2 contra punto 3: el reporte dice 8/10 y la traza de auditoria completa empieza el 8/11.
   Las dos pantallas del mismo caso no coinciden en el dia.
5. David reporto el evento inicial a las 4:23 PM del 8/10. El Change History lo muestra a las
   12:23 AM del 8/11. Ocho horas exactas, mismo minuto. Es el mismo evento en dos relojes.
6. Ocho horas es UTC menos 8. Vallarta en agosto esta en PDT, que es UTC menos 7. Un desfase de
   ocho y no de siete apunta a un offset fijo de Pacific Standard Time sin DST, no a una
   conversion IANA. Es la misma trampa que quedo documentada para ADUSA en
   `brain/markdown/19-rcs-procesos-playbook.md`: el fix tiene que ser `America/Los_Angeles` con DST,
   no un offset clavado.
7. El propio David midio el bucket de timezone: 308 de 419 cuentas de Vallarta en `TimeZone = UTC`,
   las 308 con `LastLoginDate = NULL`. Fernando Torres, el sujeto del caso, esta en ese grupo.

No esta establecido cual de los dos relojes miente. Para eso hay que leer el valor crudo en base.

## Los dos defectos van separados

Si se manda todo junto, Engineering lo devuelve. Son dos.

Defecto A, el disparo. La alerta salio la mañana del 8/11 sobre un caso guardado la tarde del 8/10
que nunca se completo. Tatiana ademas dice que antes de la actualizacion de ERMS el guardado con
etapas en Pending disparaba la alerta siempre. Lo que se reclama es la latencia y la
inconsistencia, no la ausencia.

Defecto B, el renderizado de hora. Change History y el reporte muestran dias distintos para el
mismo caso. Esto es lo que llevo a diagnosticar mal el ticket.

## Dos hipotesis que compiten para el defecto A

H1, frontera de fecha UTC. El guardado ocurrio a las 5:23 PM PT, que cae despues de medianoche UTC.
Si la logica de ventana de la alerta evalua contra un registro en contexto UTC, el caso queda del
lado del dia siguiente y la alerta sale por la corrida de la mañana. Encaja con el sintoma literal
que reporto Tatiana, "trigger until the following day".

H2, el envio sincronico falla y reintenta. En el cerebro quedo medido que
`POST /nettrack/api/internal/SendSmartAlert.aspx` acumulaba 2495 client timeouts y 248 errores 500,
248 de esos 500 en ese unico endpoint. Cita en `brain/markdown/16-rcs-soluciones.md`. Si el envio es
sincronico al guardar y se cae, la entrega queda a merced de un reintento o de un barrido
posterior. Eso produce exactamente los tres sintomas que ella lista: a veces sale, a veces al dia
siguiente, a veces al aprobar.

H1 y H2 se separan con una sola variable: la hora del dia a la que se guarda.

## El plan de reproduccion

### Paso 0. Fijar la verdad de base antes de tocar nada

Solo SELECT contra produccion.

Valor crudo del evento de auditoria del caso reportado. Esto decide cual pantalla miente.

    SELECT TOP 50 Operation, DateChanged, UserName, CaseNo, CaseData
    FROM <tabla_de_auditoria>
    WHERE CaseNo = '2026-ADUP-40-96'
    ORDER BY DateChanged ASC;

Timezone de los dos usuarios que intervienen. Vianney Valdez es quien guarda y quien renderiza el
Change History. Fernando Torres es el sujeto.

    SELECT UserId, UserName, TimeZone, LastLoginDate, CreateDate
    FROM membership.Users
    WHERE UserName IN ('<valdez>', '<torres>');

Log de envio de la alerta para ese caso, con la hora de despacho y el codigo de respuesta. Si no
hay tabla de log, pedirle a Engineering donde queda la traza de `SendSmartAlert.aspx`.

Configuracion de la alerta en `Incident > Admin > Manage Smart Alerts` para el tenant de Vallarta,
tipo de incidente Complaints. Captura de la pantalla completa, incluida la ventana de evaluacion.

### Paso 1. Pedirle a Tatiana el material que falta

Sin mas ejemplos esto se queda en un solo caso y Engineering lo rechaza. Necesitas de ella tres a
cinco numeros de caso, y por cada uno: hora de reloj de pared en que guardo, hora en que le llego
el correo, y si alguno no llego nunca. Que incluya al menos uno guardado en la mañana y uno
guardado despues de las 5 PM PT.

### Paso 2. Las cuatro corridas

Entorno: tenant de prueba de Incident con el mismo tipo de incidente y la misma Smart Alert
configurada. Si no existe, pedirlo antes de empezar, no improvisar en produccion.

Para cada corrida anota tres cosas siempre: hora de reloj de pared en PT al pulsar Save, numero de
caso generado, y hora de recepcion del correo leida del header del mensaje, no de la bandeja.

| Corrida | Hora del guardado | Etapas al guardar | Usuario | Que separa |
|---|---|---|---|---|
| 1 | 9 AM PT, mismo dia UTC | todas en Pending | TZ `America/Los_Angeles`, con login previo | linea base. Si falla aca, la hora no importa y es H2 |
| 2 | 6 PM PT, cruza medianoche UTC | todas en Pending | mismo usuario que la 1 | es la condicion exacta de Vallarta. Si solo falla aca, es H1 |
| 3 | 6 PM PT | todas en Pending | `TimeZone = UTC`, `LastLoginDate = NULL` | mete la variable de cuenta migrada |
| 4 | 6 PM PT | caso completado | mismo usuario que la 1 | prueba si completar cambia algo, que es lo que se le afirmo a la clienta |

Lectura del resultado. Si la 1 sale bien y la 2 se retrasa, es la frontera de fecha UTC y va con
todo el material de timezone. Si la 1 tambien se retrasa o se pierde, la hora no explica nada y hay
que ir al endpoint. Si la 3 se comporta peor que la 2, la cuenta migrada agrava y el fix de
timezone que ya corrio para Ahold y Stater Bros aplica tambien aca.

### Paso 3. La reproduccion del defecto B, tres minutos

1. Abre cualquier caso guardado, del que sepas la hora real.
2. Captura el reporte con `Date Case Reported`.
3. Abre el modal de Change History y captura `Date Changed` del evento mas viejo.
4. Resta. Siete horas es UTC puro. Ocho horas es offset PST clavado sin DST.
5. Contra el valor crudo del paso 0, di cual de las dos pantallas convierte mal.

Esto se reproduce sin esperar ningun correo y ya tienes media evidencia en la captura que subiste.

### Paso 4. Documentar como lo exige el flujo

`brain/memoria/reference_escalacion_l3_procedimiento.md` dice que sin excepcion tiene que estar en
el ticket: el entorno, los pasos completos de reproduccion con capturas, las notas de IA usadas en
el troubleshooting y cualquier conversacion con ingenieros que paso fuera del ticket. Falta eso y el
ticket se queda parado semanas. Aimee lo hizo cumplir en cuatro tickets el 13 de agosto.

Destino: Incident Engineering, cola AALPS. Transicion a Under Engineering Review, reasignar a
Shandana Khan. El ENG se auto-crea, no lo crees a mano. Avisale a Tatiana que el ticket se mueve.

## Borrador para el cliente, mientras se arma la reproduccion

Pegar en Jira. Juan lo pega, no lo pega Claude.

Hello Tatiana,

Thank you for sending the report back. You are right, and I want to correct what we told you on
August 12. Case 2026-ADUP-40-96 is still at stage Pending Report to be Completed with an HR case
status of Open. It was never saved as a completed case, so our earlier explanation that the alert
fired on completion does not hold. I apologize for that.

We are now looking at two separate things. The first is why the alert reached you the following
morning rather than at the time of save. The second is a discrepancy we found in the case record
itself. The report shows the case reported on 8/10 while the full change history for the same case
begins on 8/11 at 12:23 AM, an eight hour difference on the same event. We are confirming which of
the two screens is converting the time incorrectly before we go further.

To move this to our engineering team I need a few more examples from you. Please send three to five
case numbers, and for each one the time you saved the case, the time the alert email arrived, and
whether any alert never arrived at all. If you can include at least one case you saved in the
morning and one you saved after 5 PM, that will help us a great deal.

Kind regards,

Juan Martinez
Lead Support Engineer

## Borrador de escalacion a Engineering

Pegar cuando las cuatro corridas esten hechas y las capturas cargadas. Rellenar lo que esta entre
corchetes.

Environment: [Prod or Test tenant name]

Summary. Smart Alerts on the Vallarta Incident tenant are delivered inconsistently. The customer
reports three variants of the same complaint: the alert fires on save, the alert arrives the
following day, or the alert arrives when the case is approved. This started after the July 2026
unification cutover. Before the cutover, saving a case with all stages marked Pending fired the
alert every time.

Reported example. Case 2026-ADUP-40-96, owner Vianney Valdez, subject Fernando Torres. The case was
saved on the evening of 8/10 and the alert was delivered on the morning of 8/11. The case has never
reached a completed state. It is still at stage Pending Report to be Completed with HR case status
Open. The attached PDF confirms this.

Second finding, timestamp rendering. The report for this case shows Date Case Reported 8/10/2026.
The change history for the same case contains 23 events, and the oldest of them is a SAVE.CASE at
8/11/2026 12:23 AM. That is an eight hour offset on the same event, and the minute value matches.
Vallarta is in America/Los_Angeles, which is UTC minus 7 in August, not UTC minus 8. An eight hour
offset points to a fixed Pacific Standard Time offset applied without daylight saving rather than a
DST aware IANA conversion. The raw stored value for that audit row is [value], which means the
incorrect conversion is on the [screen] side.

Account context. 308 of 419 Vallarta accounts carry TimeZone UTC and a null LastLoginDate. IANA
timezone is only written to the database by an async ajax call fired from the browser at platform
login, and Incident only tenants have no other path to set it. This is the same gap addressed for
Ahold on RCS-28030 and for Stater Bros on RCS-28065. The case owner in this example is in the
affected set.

Reproduction. [Paste the four run table with actual times, case numbers and email header times.]
Screenshots attached for each run.

What we need from you. First, confirm the exact trigger condition for a Smart Alert in the current
build: does it fire on SAVE.CASE regardless of stage, or only on case completion. Second, confirm
whether alert dispatch is synchronous at save time through
POST /nettrack/api/internal/SendSmartAlert.aspx or whether a batch sweep also participates, and
whether that sweep evaluates a date window in UTC. Third, tell us which layer converts the change
history timestamp so we can align it with the report.

Troubleshooting notes. [Link the AI notes and any Teams threads with other engineers.]

## Lo que sigue

Antes de nada, el paso 0 y el paso 1. El paso 0 lo haces solo con SELECT y decide el defecto B en
una tarde. El paso 1 depende de Tatiana y es el que mas tarda, asi que pideselo hoy.

Riesgo que hay que nombrar: el ticket lleva desde el 18 de agosto sin respuesta al cliente y la
ultima que recibio estaba equivocada. Es Medium, o sea cadencia semanal, y esa semana ya se cumplio.
