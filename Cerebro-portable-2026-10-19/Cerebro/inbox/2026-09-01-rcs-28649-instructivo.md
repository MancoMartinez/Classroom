# RCS-28649, instructivo tecnico

Version 2, 2026-09-01. Reescrito despues de la evidencia que Juan aporto en siete capturas.
Informe con el razonamiento: `inbox/2026-09-01-rcs-28649-informe.md`.

Ejecuta en orden. Cada paso dice si es lectura o escritura. Ningun paso de escritura corre sin que
Juan lo autorice. Jira es solo lectura para Claude: los bloques se pegan a mano.

Lo que la evidencia ya cerro y sale de este instructivo: la lista de archivos impactados, la
medicion del alcance y la confirmacion de que el dato crudo existe. Los seis nombres estan en el
informe.

---

## Paso 0. Resolver quien es el dueno del ticket

LECTURA. Antes que todo lo demas.

El assignee en Jira es Edwin Garzon. Anil P le pidio a Diego Buelvas que revise, en el comentario
del 2026-09-01 07:39. Dos personas creen que la tiene el otro, y por eso el ticket lleva cuatro dias
quieto.

Accion: escribe a Edwin y a Diego por Teams y fija un dueno unico.

Que se espera ver: un nombre, confirmado por esa persona.

Si falla: si nadie responde en 30 minutos, tomalo tu. El ticket esta escalado y con SLA High
incumplido tres dias.

---

## Paso 1. Confirmar quien tiene el rol admin para REBUILD_RANGE

LECTURA. Bloqueante.

`REBUILD_RANGE` escribe en produccion y exige rol admin. La regla del proyecto no admite que soporte
escriba en produccion.

Accion: pregunta por Teams quien tiene el rol hoy y si lo ejecuta el mismo o lo delega. Empieza por
Peyman Motlagh para Delivery de Secure 5. Luke Du y Jenny Wang son los dos nombres que aparecen en
DO-10275 con conocimiento directo del pipeline de THD.

Que se espera ver: un nombre con el rol y su disponibilidad hoy.

Si falla: si nadie con el rol responde, escala por el Paso 6 igual. El ticket tiene que quedar a
nombre del equipo que puede ejecutar, no del que no puede.

---

## Paso 2. Fijar el rango exacto que recibe el procedimiento

LECTURA. Bloqueante.

El lote tiene tres relojes distintos y ninguno se puede asumir:

    Hora logica del nombre     16:01 del 2026-08-29, sufijo _160100
    Deposito real              entre 20:15:58 y 20:16:27 del 2026-08-29
    Panel del cliente          Issue Start 8/29 6:00 PM, Issue End 9/1 7:00 AM

Accion: confirma con quien ejecuta cual de los tres consume `REBUILD_RANGE`, y si el rango va por
trading day, por hora de archivo o por timestamp de ingesta.

Que se espera ver: el rango escrito, con su unidad declarada, aprobado por quien ejecuta.

Si falla: no lo estimes. Un rango corto deja archivos afuera y un rango largo barre horas sanas.

Decide ademas si el reprocesamiento cubre solo el 29 de agosto o tambien el archivo de la hora 04
del 28. Ese segundo lote tiene 51,842 transacciones con discrepancia sobre los trading days 8/27 y
8/28, y se recupero solo en 7 horas. Verifica si sigue con hueco antes de incluirlo.

---

## Paso 3. Confirmar que hace REBUILD_RANGE con lo que ya esta cargado

LECTURA. Bloqueante. **No ejecutes sin esta respuesta.**

El cerebro no tiene una sola linea sobre este procedimiento. Nadie documento si borra y reconstruye
el rango o si inserta encima de lo existente.

Accion: pide por escrito a quien ejecuta:

1. Si el procedimiento hace truncate o delete del rango antes de insertar.
2. Si es idempotente al correrlo dos veces sobre el mismo rango.
3. Que pasa con las cabeceras que ya cargaron bien dentro del rango.
4. Si existe rollback y cuanto tarda.

Que se espera ver: las cuatro respuestas, en el ticket o en Teams, citables.

Si falla: si nadie responde las cuatro, no se ejecuta. Reprocesar 878,922 transacciones sin saber si
duplica convierte un ticket escalado en un incidente mayor.

---

## Paso 4. Tomar la linea base antes de tocar nada

LECTURA. Solo SELECT.

Sin este numero no vas a poder demostrar que el reprocesamiento funciono.

Corre el reporte del cliente y anota el resultado:

    public/admin searches/gcp exports/appriss_line_level_transaction_discrepencies.search

Guarda el conteo por archivo para el trading day 2026-08-29. La linea base conocida es:

    New1 155,253   New2 154,970   New3 155,710
    New4 154,403   New5 155,673   New6 102,913
    Total 878,922

Guarda ademas un caso puntual verificable. Store 6568 Mansfield TX, 08/27/2026 11:58:12 PM,
Register 90, Trans# 9636, Appriss Secure ID 2608273478023917993, hoy con Subtotal 2,074.00 y Total
Item Sale Amount 0.00.

Que se espera ver: los numeros guardados en `inbox/` antes de que alguien escriba en produccion.

Si falla: el tenant responde en dos hosts. `apps.apprissretail.com/homedepot/` esta verificado en el
cerebro y `homedepot.apprissretailcloud.com` es el que aparece en las capturas del cliente. Usa el
que responda y anota cual fue.

---

## Paso 5. Escribir la nota de triage dentro del ticket

ESCRITURA en Jira. Juan pega. Sin esto el ticket rebota.

En ingles, sin markdown:

```
Internal triage note.

Environment: Production, client 085 THD, Secure 5 EBR.

Scope. Six files for the 8/29 16th hour loaded transaction headers without item and tender detail:

Archive/Prod/2026/08/29/20260829201558660-AP_EBR_POS_JOURNAL_New1_20260829_160100.csv.pgp
Archive/Prod/2026/08/29/20260829201605071-AP_EBR_POS_JOURNAL_New2_20260829_160100.csv.pgp
Archive/Prod/2026/08/29/20260829201610952-AP_EBR_POS_JOURNAL_New3_20260829_160100.csv.pgp
Archive/Prod/2026/08/29/20260829201617101-AP_EBR_POS_JOURNAL_New4_20260829_160100.csv.pgp
Archive/Prod/2026/08/29/20260829201623189-AP_EBR_POS_JOURNAL_New5_20260829_160100.csv.pgp
Archive/Prod/2026/08/29/20260829201627084-AP_EBR_POS_JOURNAL_New6_20260829_160100.csv.pgp

Volume. 878,922 transactions on trading day 8/29 show a header subtotal that does not match the
Appriss derived item total, measured with the customer saved search
appriss_line_level_transaction_discrepencies. Example: store 6568, register 90, transaction 9636 on
08/27/2026 shows Subtotal 2,074.00 with Total Item Sale Amount 0.00 and Total Item Quantity 0.00.

Raw data confirmed present. The detail did not reach the final table.

Separate earlier occurrence. File
Archive/Prod/2026/08/28/20260828080507691-AP_EBR_POS_JOURNAL_New1_20260828_040108.csv.pgp affected
trading days 8/27 and 8/28 with 51,842 transactions. That one recovered on its own within 7 hours.

Pattern. The customer impacted hours panel shows four partial load episodes: 8/29 hour 16 open at 61
hours, 8/30 hour 20 recovered in 1 hour, 8/28 hour 04 recovered in 7 hours, and 4/1 hour 20
recovered after 37 hours. Three of four self recovered through late file reprocessing. This one did
not. Please confirm why this batch was not picked up by the same automatic reprocessing.

File format change. THD file naming and handling changed between 8/23 and 8/24. Files before that
date arrive flat and unencrypted, for example
20260823204123096-AP_EBR_POS_JOURNAL_New6_20260823_160105.csv. Files after arrive with an
Archive/Prod path prefix and a .pgp extension. All August episodes fall after that change.

Related. DO-10275, 085 THD client source data file handling, documents that THD loads through a
dedicated files.py outside appriss_files, that the code combines a special file path and file name
for copying, that a file name pattern change has broken it before, and that the MARKER_FILE
completeness check which would prevent a partial batch from loading is proposed and not built. That
ticket has been in Selected for Development since 2026-04-15 with an inactive assignee.

Requested action. Reprocess the 8/29 range so the pipeline reinserts the missing item and tender
rows. Before execution we need written confirmation of the range unit the procedure consumes, and
whether it deletes and rebuilds the range or inserts on top of existing rows.

Open item. A configuration fix was applied on this ticket on 2026-08-28 at 10:47 for a separate
symptom, receipts failing to display. That change is not documented in any ticket, and the symptom
is still reproducible. Store 7109, register 41, transaction 1123 on 08/27/2026 returns "This
transaction cannot be found. It may be out of data retention." in one view and renders the full
receipt in another. Do not treat that symptom as closed.
```

Que se espera ver: el comentario publicado, sin cambio de estado todavia.

Si falla: revisa que no se hayan colado asteriscos ni vinetas al pegar. Jira los renderiza.

---

## Paso 6. Mover el ticket al equipo que ejecuta

ESCRITURA en Jira. Solo despues del Paso 5.

Si el Paso 1 devolvio que quien ejecuta es Delivery:

    Transicion    Waiting for Delivery, id 601
    Lleva a       Under Delivery Review, status id 14726
    Assignee      Peyman Motlagh
    Sprint        RCS Support Team
    Verificado    getTransitionsForJiraIssue sobre RCS-28649 el 2026-09-01, disponible, sin pantalla

Si quien ejecuta es el equipo de base de datos:

    Transicion    Waiting for Database Services, id 591
    Lleva a       Under Database Services Review, status id 14718
    Verificado    disponible hoy sobre este ticket. No esta en flujos/estado-escalated.md

Un procedimiento almacenado que reescribe tablas de produccion encaja en las dos rutas. El Paso 1
decide. Agrega el hallazgo de la transicion 591 al flujo cuando cierres.

Que se espera ver: el ticket a nombre de quien puede ejecutar, con la nota del Paso 5 arriba.

Si falla: no uses Waiting for Engineering. Ese camino pide un defecto de codigo reproducible y aqui
la accion inmediata es un reprocesamiento. Engineering entra por DO-10275, en el Paso 9.

---

## Paso 7. Verificar despues de la ejecucion

LECTURA. Solo SELECT. Lo corre Juan, no quien ejecuto.

1. Vuelve a correr `appriss_line_level_transaction_discrepencies` para el trading day 2026-08-29 y
   compara contra la linea base de 878,922.
2. Abre la transaccion 9636 de la tienda 6568 y confirma que Total Item Sale Amount dejo de ser 0.00
   y que el recibo muestra lineas.
3. Cuenta las filas del rango para descartar duplicacion. Si el total de transacciones del 29 de
   agosto crecio respecto a la linea base, el procedimiento inserto encima. Levanta la alarma de
   inmediato.

Que se espera ver: discrepancias en cero o cerca de cero, y el conteo total sin crecer.

Si falla: no le digas al cliente que quedo resuelto hasta tener los tres puntos. La verificacion la
hace soporte, no el equipo que ejecuto.

---

## Paso 8. Responderle al cliente

ESCRITURA en Jira. Juan pega, despues del Paso 6. En ingles, sin hallazgos internos, sin fechas
futuras, sin nombrar equipos ni personas.

```
Hi Matthew and Ericka,

Thank you for your patience and for identifying the affected files.

We have confirmed the gap on the 8/29 16th hour files and the request to reprocess that range is now
with the team that performs it. We will update this ticket as the work progresses.

Kind regards,
```

Que se espera ver: el comentario publicado. El estado queda como lo dejo el Paso 6.

Si falla: no prometas una hora ni un dia. No digas que el reprocesamiento ya corrio hasta ver el
Paso 7.

Deja Escalated quieto mientras el motivo de la escalacion siga vivo. La regla esta verificada en
`flujos/estado-escalated.md`. Under Customer Review pausa los SLA y arranca el reloj de auto cierre
a 28 dias.

---

## Paso 9. Empujar DO-10275 aparte

ESCRITURA en Jira, ticket distinto.

Reprocesar el 29 de agosto no cierra el problema de fondo. Cuatro episodios desde abril lo dicen.

Pega en DO-10275, en ingles:

```
Referenced from RCS-28649. Client 085 THD loaded six files for the 8/29 16th hour with headers and
without item or tender detail, leaving 878,922 transactions with a header to item subtotal mismatch.
The customer impacted hours panel shows four partial load episodes since April, three of which self
recovered and one of which did not. The MARKER_FILE completeness check described in items 4 and 5 of
this description would have prevented a partial batch from loading. The assignee on this ticket is
inactive since 2026-04-15. Requesting a current owner.
```

Que se espera ver: DO-10275 con un dueno vivo.

Si falla: subelo en el SCRUM semanal junto con RCS-28649. Escalated alimenta ese Kanban.

---

## Paso 10. Registrar en el cerebro

LECTURA y escritura local. Nada toca Jira.

    bin/anotar RCS-28649 "Triage v2. Seis archivos hora 16 del 29 ago, header sin item ni tender, 878922 txns. Remedio REBUILD_RANGE, pendiente rol admin."
    python3 bin/indexar_tickets.py
    bin/guardar --carpetas
    cat inbox/2026-09-01-rcs-28649-informe.md | bin/guardar 16 "THD carga parcial recurrente, files.py propio y MARKER_FILE sin construir"

Carpeta 16 es RCS Soluciones.

Cuatro huecos del cerebro que este ticket dejo a la vista y que valen mas que el ticket:

1. `REBUILD_RANGE` no existe en la base. Documentalo cuando alguien lo explique: que hace, quien
   tiene el rol, que rango consume, si es idempotente. Va a `flujos/`.
2. No existe flujo para recargar archivos de transacciones POS. Escribelo cuando este corra.
3. El host de THD sigue sin corregirse. La correccion esta verificada desde el 31 de agosto en
   `inbox/2026-08-31-rcs-28671-thd-searches-snowtime.md`. Las capturas de hoy muestran los dos hosts
   respondiendo, asi que anota los dos.
4. La transicion `Waiting for Database Services`, id 591, no esta en `flujos/estado-escalated.md`.
