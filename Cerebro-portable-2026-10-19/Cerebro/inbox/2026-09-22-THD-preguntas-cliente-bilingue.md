# THD. Preguntas para la reunión / Client questions

Uso interno para Juan y Camila / Internal use for Juan and Camila.

ES: Respuestas propuestas con la evidencia reunida el 22 de septiembre de 2026, corte 11:55 Bogotá. No representan una nueva verificación en producción. Los compromisos pendientes deben acordarse antes de anunciarlos.

EN: Suggested answers based on the evidence reviewed on September 22, 2026, as of 11:55 AM Bogotá. This is not a new production verification. Agree outstanding commitments before presenting them as confirmed.

<a id="menu"></a>
## Navegación rápida / Quick navigation

| Si preguntan por… / If they ask about… | Ir a / Open |
| --- | --- |
| Qué está resuelto y qué sigue abierto / Resolved and open work | [Resumen / Overview](#overview) |
| Por qué dijimos que estaba resuelto / Previous resolution statements | [Confianza / Trust](#trust) |
| Importes, recibos, recargas y archivos / Amounts, receipts, reloads and files | [Datafeed](#datafeed) |
| Migración, búsquedas y 17 work items / Migration, searches and 17 work items | [Migración / Migration](#migration) |
| Lentitud, 25 pendientes y fecha del 24 / Slow searches, 25 pending and September 24 | [Rendimiento / Performance](#performance) |
| Upgrade y estabilidad / Upgrade and stability | [SQL MI](#sqlmi) |
| Responsables, fechas y cierre / Owners, timing and closure | [Compromisos / Commitments](#commitments) |
| Qué podemos afirmar / What we can state | [Afirmaciones / Claims](#claims) |
| Significado de términos / Meaning of terms | [Glosario / Glossary](#glossary) |
| Comentarios y tickets originales / Original comments and tickets | [Fuentes / Sources](#sources) |

ES: Dentro de cada tema encontrarás pregunta, respuesta EN, respuesta ES y sustento. Los apartados “Interno / Internal” sirven para preparar la respuesta; no forman parte del texto para el cliente.

EN: Each topic contains the question, an English answer, a Spanish answer and supporting evidence. “Interno / Internal” notes help prepare the response and are not part of the customer wording.

<a id="overview"></a>
## 1. Panorama / Overview

### 1.1 What is fixed, and what is still open? / ¿Qué está resuelto y qué sigue abierto?

EN

We repaired 278 searches in August and completed the database tier change. The remaining work includes recovery of 17 historical work items, slow searches and timeout enforcement, the recurring work item backlog, and the Total Item Sale Amount issue. Each needs its own validation.

ES

Reparamos 278 búsquedas en agosto y completamos el cambio de tier de base de datos. Quedan la recuperación de 17 work items históricos, las búsquedas lentas y el control del timeout, la cola recurrente y el problema de Total Item Sale Amount. Cada frente necesita su propia validación.

Sustento / Evidence: [S1](#s1), [S2](#s2), [S3](#s3), [S4](#s4), [S6](#s6).

### 1.2 Do all these problems have the same cause? / ¿Todo tiene la misma causa?

EN

We have evidence for several different failure mechanisms. The column rename affected searches, long running queries caused contention between searches, and earlier data reloads left some outputs inconsistent. We have not established a single cause connecting all of them.

ES

Tenemos evidencia de varios mecanismos distintos. El cambio de nombre de columnas afectó búsquedas, las consultas largas generaron contención entre búsquedas y algunas recargas anteriores dejaron salidas inconsistentes. No hemos demostrado una causa única que conecte todo.

Interno / Internal: Coincidencia temporal no prueba causalidad. / Timing alone does not prove causation. [S1](#s1), [S5](#s5), [S7](#s7).

[Volver al índice / Back to navigation](#menu)

<a id="trust"></a>
## 2. Confianza y correcciones / Trust and corrections

### 2.1 Why did you say it was permanently fixed? / ¿Por qué dijeron que tenía solución permanente?

EN

Our previous update combined the suspended transaction correction with the Total Item Sale Amount recovery and overstated the overall resolution. The latest recurrence shows that the derived amount issue still needs a permanent fix. Camila has corrected that distinction in today's email.

ES

La actualización anterior mezcló la corrección de transacciones suspendidas con la recuperación de Total Item Sale Amount y presentó la resolución con un alcance mayor al demostrado. La recurrencia confirma que el importe derivado sigue necesitando una solución permanente. Camila ya aclaró esa diferencia en el correo de hoy.

Sustento / Evidence: [S6](#s6), [S9](#s9). Interno / Internal: La regla de suspendidas no explica técnicamente el importe derivado en las fuentes disponibles. / The available sources do not technically connect the suspended transaction rule to the derived amount.

### 2.2 How can we trust the next resolution update? / ¿Cómo podemos confiar en el siguiente aviso de resolución?

EN

A reload confirmation needs matching results for the affected transactions, including detail, derived totals and receipts. A permanent resolution also needs evidence from subsequent processing without another manual rebuild. We should agree that validation and the observation period with you before closing the issue.

ES

La confirmación de una recarga necesita resultados conciliados para las transacciones afectadas, incluidos detalle, totales derivados y recibos. Una resolución permanente también necesita evidencia de cargas posteriores sin otro rebuild manual. Debemos acordar esa validación y el período de observación antes de cerrar.

Interno / Internal: Criterio propuesto, todavía sin período acordado. / Proposed criteria; the observation period is not yet agreed. [S6](#s6), [S7](#s7).

### 2.3 Were our files late or incorrect? / ¿Nuestros archivos llegaron tarde o estaban mal?

EN

For the September incident in RCS-28649, Andres corrected the earlier explanation: your files were not late, and our extraction was not late. He identified a problem in our processing. We have no evidence that attributes the current derived amount issue to a new delivery error on your side.

ES

Para el incidente de septiembre en RCS-28649, Andres corrigió la explicación anterior: los archivos de ustedes no llegaron tarde y nuestra extracción tampoco fue tardía. Identificó un problema de nuestro procesamiento. No tenemos evidencia que atribuya el importe derivado actual a un nuevo error de entrega de ustedes.

Sustento / Evidence: [S7](#s7). Interno / Internal: Limitar esta confirmación al episodio investigado. / Keep this confirmation scoped to the investigated incident.

[Volver al índice / Back to navigation](#menu)

<a id="datafeed"></a>
## 3. Datafeed, importes y recibos / Datafeed, amounts and receipts

### 3.1 What exactly is wrong with Total Item Sale Amount? / ¿Qué falla exactamente en Total Item Sale Amount?

EN

Matthew reported transactions where the detail and receipt look correct while Total Item Sale Amount differs from the Subtotal sent in your feed. That makes the discrepancy report unreliable for identifying missing detail. The exact processing mechanism behind the current recurrence still needs technical confirmation.

ES

Matthew reportó transacciones donde el detalle y el recibo aparecen correctos y Total Item Sale Amount difiere del Subtotal enviado en el feed. Eso impide usar el reporte con confianza para identificar detalle faltante. Falta confirmar técnicamente el mecanismo de procesamiento detrás de la recurrencia actual.

Sustento / Evidence: [S6](#s6). Interno / Internal: “Causa identificada” consta en el correo; no tenemos la explicación técnica adicional. / The email says the cause is identified; we do not have the additional technical explanation.

### 3.2 Is the data correct now? Which dates did you reload? / ¿Los datos ya están bien? ¿Qué fechas recargaron?

EN

Camila's email reports a reload for September 20 through 22. The previous Jira update reports correction of September 19 and 20. We still need the reconciliation results after the latest rebuild, including September 19, before confirming the full affected range is correct.

ES

El correo de Camila informa una recarga del 20 al 22 de septiembre. La actualización anterior en Jira informa corrección del 19 y 20. Necesitamos los resultados de conciliación posteriores al último rebuild, incluido el 19, antes de confirmar todo el rango afectado.

Sustento / Evidence: [S6](#s6), [S9](#s9). Interno / Internal: La recarga del 20 al 22 consta en el correo, no en un comentario técnico de hoy en Jira. / The September 20 through 22 reload is reported in the email, not in a technical Jira comment from today.

### 3.3 Can we use the discrepancy report to measure missing data? / ¿Podemos usar el reporte para medir datos faltantes?

EN

It can identify transactions that need review. While the derived amount is inconsistent, its discrepancy count cannot by itself tell us how many transactions are missing detail. We need to compare the flagged transactions with their actual item detail and receipts.

ES

Puede identificar transacciones para revisar. Mientras el importe derivado sea inconsistente, el conteo de discrepancias no permite determinar por sí solo cuántas transacciones tienen detalle faltante. Necesitamos comparar las marcadas con sus líneas y recibos.

Sustento / Evidence: [S6](#s6). Interno / Internal: No tenemos un porcentaje actual de datos afectados. / We do not have a current affected data percentage.

### 3.4 Why can a receipt be correct while the amount is wrong? / ¿Cómo puede estar bien el recibo y mal el importe?

EN

A receipt, item detail and a derived total are separate outputs that need to remain consistent. The reported examples show that correcting one output has not always corrected the others. We need to verify which recalculation and refresh steps ran for the current rebuild.

ES

El recibo, el detalle y el total derivado son salidas distintas que deben mantenerse consistentes. Los ejemplos reportados muestran que corregir una salida no siempre corrigió las demás. Necesitamos verificar qué pasos de recálculo y actualización ejecutó el rebuild actual.

Sustento / Evidence: [S6](#s6), [S7](#s7). Interno / Internal: Esto explica el riesgo; no confirma qué paso falló hoy. / This explains the risk; it does not identify today's failed step.

### 3.5 What do the 750,000 transactions and 4% versus 84% mean? / ¿Qué significan las 750 mil transacciones y el 4% frente al 84%?

EN

Those figures appear in the September 21 update about suspended transaction reporting. They do not quantify the current Total Item Sale Amount discrepancies. We need the technical validation behind those figures before using them to describe any broader impact.

ES

Esas cifras aparecen en la actualización del 21 sobre reportes de transacciones suspendidas. No cuantifican las discrepancias actuales de Total Item Sale Amount. Necesitamos la validación técnica detrás de esas cifras antes de usarlas para describir un impacto más amplio.

Sustento / Evidence: [S6](#s6). Interno / Internal: No interpretar 84% como porcentaje de todas las ventas; el denominador no está explicado. / Do not interpret 84% as a share of all sales; the denominator is not explained.

### 3.6 Do repeated file names prove duplicate loading? / ¿Los nombres repetidos prueban carga duplicada?

EN

The screenshot contains four distinct file names, each shown twice. That alone does not prove duplicate ingestion. We need transaction identifiers and ingestion records to determine whether anything was loaded more than once.

ES

La captura contiene cuatro nombres de archivo distintos, cada uno mostrado dos veces. Eso no prueba ingestión duplicada. Necesitamos identificadores de transacción y registros de ingestión para determinar si algo cargó más de una vez.

Sustento / Evidence: [S9](#s9). Interno / Internal: La fecha de carpeta y la del nombre fuente tampoco prueban retraso. / The folder date and source file date do not establish a delay either.

### 3.7 Do you need more examples from us? / ¿Necesitan más ejemplos nuestros?

EN

We already have examples to validate, including Secure ID 2609210101525048961, store 8918, register 51. We should start by showing the result for those transactions after the rebuild. If a different date or symptom remains, its transaction ID and timing will help scope that additional issue.

ES

Ya tenemos ejemplos para validar, incluido el Secure ID 2609210101525048961, tienda 8918, registro 51. Debemos empezar por mostrar el resultado de esas transacciones después del rebuild. Si persiste otra fecha o síntoma, su identificador y hora ayudarán a delimitar ese caso adicional.

Sustento / Evidence: [S9](#s9). Interno / Internal: La captura no muestra importes ni validación posterior. / The screenshot does not show amounts or post-rebuild validation.

### 3.8 Where is the SOP you promised? / ¿Dónde está el SOP prometido?

EN

Camila committed to a reload and receipt verification procedure on September 10. The record we reviewed still marks that follow-up as pending. We need to confirm its owner and location and ensure it also covers derived totals.

ES

Camila se comprometió el 10 de septiembre con un procedimiento para verificar recargas y recibos. El registro revisado mantiene ese seguimiento pendiente. Necesitamos confirmar responsable y ubicación, y asegurar que incluya los totales derivados.

Sustento / Evidence: [S7](#s7). Interno / Internal: Falta de cierre documentado no prueba que nadie haya trabajado en él. / No documented completion does not prove that no work has occurred.

[Volver al índice / Back to navigation](#menu)

<a id="migration"></a>
## 4. Migración, búsquedas y eventos / Migration, searches and events

### 4.1 Did the migration cause these problems? / ¿La migración causó estos problemas?

EN

We confirmed that a column rename associated with the migration broke some search references. We also identified work items without platform events around the cutover. Those findings do not establish that the migration caused every later timeout or data discrepancy.

ES

Confirmamos que un cambio de nombre de columna asociado a la migración rompió referencias de algunas búsquedas. También identificamos work items sin eventos en plataforma alrededor del corte. Esos hallazgos no demuestran que la migración causara cada timeout o discrepancia posterior.

Sustento / Evidence: [S1](#s1), [S2](#s2). Interno / Internal: HDC/050 a principios de agosto y THD/085 a finales de agosto son referencias distintas. / Early August HDC/050 and late August THD/085 are distinct migration references.

### 4.2 Is Same Name Refunds still failing because of the renamed column? / ¿Same Name Refunds sigue fallando por la columna renombrada?

EN

The original SNR4 failure referenced the old column name. We later recorded a successful SNR4 run on September 2. Subsequent reports include cancellations and slow searches, so we need the current error before attributing another failure to that original rename.

ES

El fallo original de SNR4 usaba el nombre anterior de la columna. Después registramos una ejecución exitosa de SNR4 el 2 de septiembre. Los reportes posteriores incluyen cancelaciones y búsquedas lentas; necesitamos el error actual antes de atribuir otro fallo al rename original.

Sustento / Evidence: [S1](#s1), [S3](#s3).

### 4.3 If you repaired 278 searches, why is the ticket open? / ¿Por qué sigue abierto si repararon 278 búsquedas?

EN

The ticket continued with a different recovery task: 17 historical work items have no associated platform events. The source transactions are present. Engineering has proposed regenerating the affected items, and that recovery remains pending. Simon also noted six searches blocked by another bug; their completion needs separate confirmation.

ES

El ticket continuó con otra recuperación: 17 work items históricos no tienen eventos asociados en plataforma. Las transacciones fuente están presentes. Ingeniería propuso regenerar los afectados y esa recuperación sigue pendiente. Simon también dejó seis búsquedas bloqueadas por otro bug; su cierre necesita confirmación aparte.

Sustento / Evidence: [S2](#s2).

### 4.4 Have the transactions been lost? Can you regenerate the work items? / ¿Se perdieron las transacciones? ¿Pueden regenerar los work items?

EN

Andres confirmed complete ARDM source data for the 17 identified work items. The gap is in their associated platform events. Engineering proposed removing and regenerating the affected items; we still need an owner, schedule and preservation plan for existing work item information.

ES

Andres confirmó los datos fuente completos en ARDM para los 17 work items identificados. El vacío está en sus eventos asociados en plataforma. Ingeniería propuso retirar y regenerar los afectados; faltan responsable, fecha y plan de preservación de la información existente.

Sustento / Evidence: [S2](#s2). Interno / Internal: No garantizar conservación de notas o asignaciones sin confirmación técnica. / Do not guarantee preservation of notes or assignments without technical confirmation.

### 4.5 Why did the August monitoring tickets close so quickly? / ¿Por qué cerraron tan rápido las alertas de agosto?

EN

Those four HDC monitoring tickets concerned alerts from the legacy pipeline after migration. Support requested disabling obsolete monitoring and closed those alerts. That closure did not resolve the separate search, work item or datafeed issues discussed here.

ES

Los cuatro tickets de monitoreo HDC correspondían a alertas del pipeline anterior después de la migración. Soporte pidió desactivar el monitoreo obsoleto y cerró esas alertas. Ese cierre no resolvió los problemas distintos de búsquedas, work items o datafeed que revisamos aquí.

Sustento / Evidence: [S8](#s8). Interno / Internal: No afirmar ajuste de umbrales sin evidencia. / Do not claim threshold changes without evidence.

[Volver al índice / Back to navigation](#menu)

<a id="performance"></a>
## 5. Rendimiento y cola / Performance and backlog

### 5.1 Are the 25 pending items the same as the 17 historical items? / ¿Los 25 pendientes son los mismos 17 históricos?

EN

They represent different measurements. The 17 are historical work items missing associated platform events. The 25 are a snapshot of pending work item jobs in the recurring backlog. We should not add them together or assume they identify the same cases.

ES

Son mediciones distintas. Los 17 son work items históricos sin eventos asociados en plataforma. Los 25 corresponden a una captura de trabajos pendientes en la cola recurrente. No debemos sumarlos ni asumir que identifican los mismos casos.

Sustento / Evidence: [S2](#s2), [S4](#s4).

### 5.2 Is the backlog still there this morning? / ¿La cola sigue pendiente esta mañana?

EN

The latest count in the reviewed records is 25 pending at 01:49 UTC on September 22, which was 9:49 PM ET on September 21. That is an earlier snapshot. We need the current queue before confirming this morning's status.

ES

El último conteo del registro revisado es de 25 pendientes a las 01:49 UTC del 22 de septiembre, 21:49 ET del 21. Es una captura anterior. Necesitamos la cola actual antes de confirmar el estado de esta mañana.

Sustento / Evidence: [S4](#s4). Interno / Internal: En Bogotá corresponde al 21 a las 20:49. / In Bogotá, that is September 21 at 8:49 PM.

### 5.3 Will the September 24 release fix everything? / ¿La versión del 24 arregla todo?

EN

The September 24 target concerns the work item timeout defect. Its development is complete and the version is not yet marked released. Search optimization and historical work item recovery remain separate actions. We do not have a permanent fix ETA for Total Item Sale Amount.

ES

La previsión del 24 corresponde al defecto del timeout de work items. Su desarrollo está terminado y la versión todavía no figura publicada. La optimización de búsquedas y la recuperación histórica son acciones separadas. No tenemos ETA de solución permanente para Total Item Sale Amount.

Sustento / Evidence: [S2](#s2), [S3](#s3), [S9](#s9).

### 5.4 Why do searches still fail after the 80 second improvement? / ¿Por qué siguen fallando después de la mejora a 80 segundos?

EN

The 80 second result came from one optimized search test. A subsequent rerun timed out, and engineering identified 18 other searches referencing the unoptimized search. We need confirmation that the dependent searches use the correction and complete successfully under the operating workload.

ES

El resultado de 80 segundos corresponde a una prueba de una búsqueda optimizada. El intento posterior agotó tiempo y el equipo identificó otras 18 búsquedas que referencian la versión sin optimizar. Necesitamos confirmar que las dependientes usan la corrección y completan bajo la carga operativa.

Sustento / Evidence: [S3](#s3). Interno / Internal: Cancelar a la hora limita consumo; no demuestra que una búsqueda entregue resultados. / Cancelling at one hour limits resource use; it does not prove the search returns results.

### 5.5 Did our searches block the datafeed or other customers? / ¿Nuestras búsquedas bloquearon el datafeed u otros clientes?

EN

The September 10 record documents long running THD queries occupying shared search compute and delaying other searches. It does not establish that those queries caused the datafeed discrepancies. We need the affected job and warehouse evidence before connecting the two.

ES

El registro del 10 de septiembre documenta consultas largas de THD que ocupaban recursos compartidos de búsqueda y retrasaban otras consultas. No demuestra que causaran las discrepancias del datafeed. Necesitamos evidencia de jobs y warehouse afectados antes de conectar ambos frentes.

Sustento / Evidence: [S5](#s5). Interno / Internal: Describe el impacto documentado sin revelar identidades o detalles de otros clientes. / Describe the documented impact without disclosing other customer identities or details.

[Volver al índice / Back to navigation](#menu)

<a id="sqlmi"></a>
## 6. SQL Managed Instance

### 6.1 Didn't the August upgrade solve the timeouts? / ¿El upgrade de agosto no resolvió los timeouts?

EN

The August 14 change addressed high IO and connection timeouts on a SQL Managed Instance. The ticket reports that it helped. The later Secure search incidents involve separate execution and timeout issues in Snowflake. One completed infrastructure change does not validate every later search failure.

ES

El cambio del 14 de agosto atendió IO alto y timeouts de conexión en una SQL Managed Instance. El ticket reporta mejora. Los incidentes posteriores de búsquedas Secure corresponden a otros problemas de ejecución y timeout en Snowflake. Un cambio de infraestructura completado no valida cada fallo posterior de búsqueda.

Sustento / Evidence: [S1](#s1), [S3](#s3), [S5](#s5).

### 6.2 Can you confirm 39 days without recurrence? / ¿Pueden confirmar 39 días sin recurrencias?

EN

We can confirm the August 14 change and the reported improvement. The reviewed ticket does not contain continuous monitoring evidence for the following 39 days. We need the service metrics before making that claim.

ES

Podemos confirmar el cambio del 14 de agosto y la mejora reportada. El ticket revisado no contiene evidencia de monitoreo continuo durante los 39 días siguientes. Necesitamos las métricas del servicio antes de afirmarlo.

Sustento / Evidence: [S1](#s1).

[Volver al índice / Back to navigation](#menu)

<a id="commitments"></a>
## 7. Compromisos y próximos pasos / Commitments and next steps

### 7.1 Who owns this, and when will we get the next update? / ¿Quién responde y cuándo tendremos otra actualización?

EN

Support coordination for RCS-28968 sits with Bikash. We need to confirm the engineering owner for the permanent data fix and agree the next update time. For the other workstreams, the current contacts are Shandana for historical recovery, Gabor for timeout enforcement, and Vlad and Enrique for search and backlog follow-up.

ES

Bikash coordina RCS-28968 desde soporte. Necesitamos confirmar el responsable de ingeniería del arreglo permanente de datos y acordar la hora de la siguiente actualización. En los demás frentes, los contactos actuales son Shandana para recuperación histórica, Gabor para timeout y Vlad y Enrique para búsquedas y cola.

Interno / Internal: Son asignados y contactos de seguimiento, no compromisos nuevos aceptados por ellos. / These are assignees and follow-up contacts, not newly accepted commitments. [S2](#s2), [S3](#s3), [S4](#s4), [S6](#s6).

### 7.2 What does a completed fix look like? / ¿Cómo sabremos que el arreglo está completo?

EN

For data, the affected transactions need consistent detail, derived amounts and receipts, followed by successful new processing. For historical work items, the events need to open correctly and existing information needs to be preserved. For performance, the searches need to complete within the expected window and the timeout needs to work. We should agree the acceptance evidence for each stream.

ES

Para datos, las transacciones afectadas necesitan detalle, importes y recibos consistentes, seguidos de cargas nuevas correctas. Para work items históricos, los eventos deben abrir correctamente y la información existente debe conservarse. Para rendimiento, las búsquedas deben completar en la ventana esperada y el timeout debe funcionar. Debemos acordar la evidencia de aceptación por frente.

Interno / Internal: Criterios propuestos; no pruebas ya ejecutadas ni garantía de preservación. / Proposed criteria, not completed tests or a preservation guarantee.

### 7.3 Can you commit to a permanent fix date or provide an RCA? / ¿Pueden comprometer fecha permanente o entregar RCA?

EN

We do not yet have a confirmed permanent fix date for the derived amount issue. The timeout has a target version, and the historical recovery still needs scheduling. We can provide the confirmed findings and outstanding questions by workstream; a single RCA covering every incident would go beyond the evidence available.

ES

Todavía no tenemos fecha confirmada del arreglo permanente del importe derivado. El timeout tiene una versión prevista y la recuperación histórica necesita programación. Podemos presentar hallazgos confirmados y preguntas pendientes por frente; una RCA única para todos los incidentes excedería la evidencia disponible.

Interno / Internal: Acordar responsable y fecha de próxima actualización, aun sin ETA del arreglo. No prometer informe formal sin confirmar dueño y alcance. / Agree the next update owner and time even without a fix ETA. Do not promise a formal report before confirming ownership and scope.

### Antes de cerrar la llamada / Before ending the call

| Acordar / Agree | Falta confirmar / Needs confirmation |
| --- | --- |
| Datos / Data | Dueño técnico, conciliación del 19 al 22 y siguiente aviso / Technical owner, September 19 through 22 reconciliation and next update |
| 17 work items | Dueño de ejecución, preservación y fecha / Execution owner, preservation plan and schedule |
| Timeout y búsquedas / Timeout and searches | Despliegue, pruebas y avance de las 18 dependencias / Deployment, tests and progress on the 18 dependencies |
| Monitoreo / Monitoring | Frecuencia, responsable y condición para rebuild / Frequency, owner and rebuild trigger |
| SOP | Ubicación, responsable y validaciones incluidas / Location, owner and required checks |

[Volver al índice / Back to navigation](#menu)

<a id="claims"></a>
## 8. Afirmaciones y límites / Claims and limits

| Afirmación / Claim | Cómo tratarla / How to use it |
| --- | --- |
| Simon reparó 278 búsquedas / Simon repaired 278 searches | Confirmado en comentario; seis bloqueadas requerían seguimiento / Confirmed in a comment; six blocked searches needed follow-up. [S2](#s2) |
| Los 17 tienen fuente completa / Source data for the 17 is complete | Confirmado para ese conjunto; no validación de toda la cuenta hoy / Confirmed for that set; not a current account-wide validation. [S2](#s2) |
| Hay 25 pendientes ahora / There are 25 pending now | Solo captura histórica; verificar cola actual / Historical snapshot only; check the live queue. [S4](#s4) |
| El timeout sale el 24 / The timeout fix ships on the 24th | Fecha prevista de versión, todavía sin publicar / Target release date, not yet marked released. [S3](#s3) |
| El 20 al 22 ya está validado / September 20 through 22 is validated | El correo informa recarga; falta evidencia de conciliación / Email reports a reload; reconciliation evidence is outstanding. [S9](#s9) |
| Suspendidas e importe tienen la misma causa / Suspended transactions and amounts share a cause | No demostrado / Not established. [S6](#s6) |
| Compute causó el problema de datos / Compute caused the data issue | Hipótesis sin correlación de jobs y warehouse / Hypothesis without job and warehouse correlation. [S5](#s5) |
| SQL MI lleva 39 días estable / SQL MI has been stable for 39 days | No acreditado por el ticket consultado / Not established by the reviewed ticket. [S1](#s1) |
| El SOP está implementado / The SOP is implemented | Cierre no documentado en las fuentes revisadas / Completion is not documented in the reviewed sources. [S7](#s7) |

[Volver al índice / Back to navigation](#menu)

<a id="glossary"></a>
## 9. Glosario / Glossary

| Término / Term | Español | English |
| --- | --- | --- |
| Datafeed | Archivos o datos que THD entrega para procesar. | Files or data THD supplies for processing. |
| Header / Subtotal | Cabecera de la transacción y subtotal que THD envía. | Transaction header and subtotal supplied by THD. |
| Item detail | Líneas de productos de una transacción. | Product lines within a transaction. |
| Tender | Datos de medios de pago. | Payment method data. |
| Total Item Sale Amount | Importe que Appriss deriva del detalle. No tenemos aquí la fórmula técnica completa. | Amount Appriss derives from item detail. The full technical formula is not established here. |
| Derived field | Valor calculado a partir de otros datos. | Value calculated from other data. |
| Receipt / ardm_json | Vista del recibo; el antecedente documenta recibos precalculados en ardm_json. | Receipt view; the historical incident documents precomputed receipts in ardm_json. |
| Reload | Volver a cargar datos de una fecha o conjunto. No acredita por sí solo todas las salidas. | Reload data for a date or set. This alone does not validate every output. |
| Rebuild / Recalculation | Reconstruir una salida o recalcular un valor a partir de datos. | Reconstruct an output or recalculate a value from data. |
| Reconciliation | Comprobar que detalle, importe y recibo coincidan según la regla de negocio aplicable. | Verify that detail, amount and receipt agree under the applicable business rules. |
| ARDM | Modelo de datos transaccionales consultado en la investigación. | Transaction data model examined in this investigation. |
| Work item | Resultado de investigación generado por reglas o búsquedas. | Investigation item generated from rules or searches. |
| Platform events | Transacciones asociadas al work item que la plataforma debe mostrar. | Transactions associated with a work item that the platform needs to display. |
| fti.Transactions | Tabla de plataforma donde identificamos el vacío para los work items históricos. | Platform table where the historical work item event gap was identified. |
| Backlog | Cola de trabajo pendiente. En ENG-8659 también es un estado de planificación. | Pending work queue. In ENG-8659, it is also a planning status. |
| Timeout | Límite de tiempo de ejecución. Agotarlo o cancelar no equivale a completar con resultados. | Execution time limit. Timing out or cancelling does not mean completing with results. |
| SQL 57014 | Código de cancelación registrado en estos incidentes; no identifica por sí solo su disparador. | Cancellation code recorded in these incidents; it does not identify the trigger by itself. |
| Invalid identifier | La consulta referencia una columna que no resuelve en el esquema. | A query references a column that does not resolve in the schema. |
| Warehouse / secure_WH | Recursos de cómputo de Snowflake; secure_WH aparece en el incidente de contención. | Snowflake compute resources; secure_WH appears in the contention incident. |
| Resource contention | Varios trabajos compiten por recursos y pueden bloquearse o esperar. | Jobs compete for resources and may block or wait. |
| SnowTime / cutover | Plataforma de datos y cambio del flujo anterior al nuevo. | Data platform and transition from the previous flow to the new one. |
| SQL MI / tier | Instancia administrada de SQL y su configuración de recursos. | Managed SQL instance and its resource configuration. |
| Development Complete | Desarrollo terminado; no confirma publicación en producción. | Development finished; does not confirm production release. |
| ETA / target release | Previsión de entrega; necesita alcance y confirmación de despliegue. | Delivery estimate; requires scope and deployment confirmation. |
| SOP | Procedimiento operativo para ejecutar y verificar un proceso de forma consistente. | Operating procedure for performing and verifying a process consistently. |
| RCA | Análisis sustentado de causa raíz, alcance y acciones. | Evidence-based root cause analysis, scope and actions. |
| UTC / ET / Bogotá | El 22 sep, ET es UTC menos cuatro y Bogotá UTC menos cinco. | On September 22, ET is UTC minus four and Bogotá UTC minus five. |

[Volver al índice / Back to navigation](#menu)

<a id="sources"></a>
## 10. Sustento / Supporting sources

ES: Los enlaces abren los tickets o comentarios originales. Los estados corresponden al corte de esta investigación. Las respuestas son propuestas para la reunión; no se enviaron al cliente.

EN: Links open the original tickets or comments. Statuses reflect this investigation's cutoff. Answers are proposed meeting wording and have not been sent to the customer.

<a id="s1"></a>
### S1. Rename y SQL MI / Rename and SQL MI

[Diagnóstico original de SNR4 / Original SNR4 diagnosis](https://trebuco.atlassian.net/browse/RTS-206667?focusedCommentId=3315650).
[SQL MI, confirmación del cambio del 14 ago / August 14 change confirmation](https://trebuco.atlassian.net/browse/RETAILIT-20673?focusedCommentId=3303499).
[Mejora reportada / Reported improvement](https://trebuco.atlassian.net/browse/RETAILIT-20673?focusedCommentId=3296361).

<a id="s2"></a>
### S2. Reparación de búsquedas y 17 work items / Search repair and 17 work items

[278 búsquedas y seis bloqueadas / 278 searches and six blocked](https://trebuco.atlassian.net/browse/RCS-28671?focusedCommentId=3322645).
[Confirmación del cliente / Customer confirmation](https://trebuco.atlassian.net/browse/RCS-28671?focusedCommentId=3324086).
[Fuente completa / Complete source data](https://trebuco.atlassian.net/browse/RCS-28671?focusedCommentId=3327725).
[Propuesta de recuperación / Recovery proposal](https://trebuco.atlassian.net/browse/RCS-28671?focusedCommentId=3333850).
[ENG-8659](https://trebuco.atlassian.net/browse/ENG-8659).

<a id="s3"></a>
### S3. Búsquedas y timeout / Searches and timeout

[SNR4 exitoso / Successful SNR4 run](https://trebuco.atlassian.net/browse/RCS-28799?focusedCommentId=3325670).
[Prueba de 80 segundos / 80 second test](https://trebuco.atlassian.net/browse/RCS-28799?focusedCommentId=3333942).
[Recaída / Subsequent timeout](https://trebuco.atlassian.net/browse/RCS-28799?focusedCommentId=3334548).
[18 búsquedas / 18 dependent searches](https://trebuco.atlassian.net/browse/RCS-28799?focusedCommentId=3337429).
[SNR1 y SNR3, 18 sep / SNR1 and SNR3, September 18](https://trebuco.atlassian.net/browse/RCS-28799?focusedCommentId=3351101).
[ENG-8650](https://trebuco.atlassian.net/browse/ENG-8650).

<a id="s4"></a>
### S4. Cola / Backlog

[Timeout probable del generador y reducción de cola / Suspected generator timeout and queue reduction](https://trebuco.atlassian.net/browse/RTS-207712?focusedCommentId=3348972).
[25 pendientes, fecha y listado / 25 pending, timestamp and list](https://trebuco.atlassian.net/browse/RTS-208130?focusedCommentId=3359318).

<a id="s5"></a>
### S5. Contención / Contention

[secure_WH y cancelación manual / secure_WH and manual cancellation](https://trebuco.atlassian.net/browse/RTS-207372?focusedCommentId=3337373).

<a id="s6"></a>
### S6. Importe derivado y suspendidas / Derived amount and suspended transactions

[Matthew: detalle correcto, derivado incorrecto / Correct detail, incorrect derived amount](https://trebuco.atlassian.net/browse/RCS-28968?focusedCommentId=3358182).
[Camila: suspendidas e importes, 21 sep / Suspended transactions and amounts, September 21](https://trebuco.atlassian.net/browse/RCS-28968?focusedCommentId=3359117).

<a id="s7"></a>
### S7. Antecedente y SOP / Historical incident and SOP

[Corrección de la explicación sobre archivos tardíos / Correction of late file explanation](https://trebuco.atlassian.net/browse/RCS-28649?focusedCommentId=3336400).
[Recibos reconstruidos / Receipt rebuild](https://trebuco.atlassian.net/browse/ENG-8334?focusedCommentId=3338722).
[SOP pendiente / Pending SOP](https://trebuco.atlassian.net/browse/RCS-28649?focusedCommentId=3337469).

<a id="s8"></a>
### S8. Alertas HDC / HDC alerts

[Solicitud de desactivar alertas antiguas / Request to disable legacy alerts](https://trebuco.atlassian.net/browse/RTS-205373?focusedCommentId=3272867).
[Alerta resuelta / Resolved alert](https://trebuco.atlassian.net/browse/RTS-205404?focusedCommentId=3273548).

<a id="s9"></a>
### S9. Correos y capturas / Emails and screenshots

ES: Cadena de correos del 22 de septiembre y dos capturas aportadas por Juan en esta conversación. El correo es la fuente de la recarga del 20 al 22 y del anuncio de causa identificada sin ETA. No contamos con un comentario técnico adicional de hoy en Jira ni con una conciliación posterior al rebuild.

EN: September 22 email chain and two screenshots supplied by Juan in this conversation. The email is the source for the September 20 through 22 reload and the statement that a cause was identified without an ETA. We do not have an additional technical Jira comment from today or post-rebuild reconciliation.

[Guía general / Meeting guide](/Users/MancoMenStudio/Cerebro/inbox/2026-09-22-THD-guia-reunion.md).
[Comparación del Excel por celda / Excel changes by cell](/Users/MancoMenStudio/Cerebro/inbox/2026-09-22-THD-correcciones-excel.md).

[Volver al índice / Back to navigation](#menu)
