# RCS-28671 fase 2. Work items sin transacciones

Fecha: 2026-09-02. Estado en Jira: **Work in progress**, ya no Escalated. Assignee Juan Martinez.

## Que paso entre el 31 ago y hoy

| Cuando | Quien | Que |
|---|---|---|
| 31 ago 14:34 | Simon Smith | Cerro la reparacion. 278 busquedas arregladas. Publicas 164, quedan 2189 de 2282 funcionando, 95.9%. De usuario 114, quedan 1144 de 1203, 95.1%. Seis mas bloqueadas por un bug |
| 31 ago 15:55 | Corey Wood | Todos los usuarios que consulto confirman que sus busquedas funcionan |
| 01 sep 14:11 | Juan | Cierra el ticket. Resolution Details: Engineer Resolved - BackEnd Update |
| 01 sep 15:12 | Corey Wood | Reabre. Reporta work items sin resultados. Pregunta si se pueden regenerar los IDs afectados |
| 01 sep 15:20 | Ericka Smith | Ejemplo concreto del Canada Field Team. Work Item 248159 |
| 01 sep 19:29 | Valerie Cerezo | El cliente pide el alcance: cuantos work items se generaron sin transacciones. Le pregunta a James DeJohn si existe una busqueda para eso |

**El ticket quedo reabierto y con dos preguntas del cliente sin responder.**

## El sintoma nuevo, y por que no es el mismo que arreglo Simon

Simon reparo definiciones de busqueda guardadas. Esto es otra cosa.

Work Item 248159, del Canada Field Team:

- Definicion MD03-APS-D, Consecutive Markdowns for Same Payment Card. Data area Secure Store, Markdowns.
- Rango 08/27/2026 a 08/27/2026. Prioridad High.
- Region 0032-CANADA, District 0157-CHARL, Store 7135, Cashier LDAP DXM6269.
- Unique Count of Appriss Secure ID: 3.
- **Value Potential 0.00 dolares.**
- Al abrir Events, el panel Transactions sale vacio y aparece "There has been a system error."
- Tracking code del error: `774fbb98-fc34-4cd0-8ee8-538f85d2967d`.

El work item existe, dice que agrupa 3 IDs unicos, y no trae ni una transaccion. Ese es el defecto.

Ojo con la entidad. Esto es Markdowns, no Line Item Void, y la region es Canada. La columna que
rompe aca no tiene por que ser `TenderTypeGroup`. No asumas que es la misma.

## El precedente, y esta vez encaja entero

RCS-28543, Kinney Drugs KNY/179, investigacion de Diego Buelvas publicada el 24 ago. **Es el mismo
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

**El SQL de deaggregacion queda persistido por work item.** Esa es la clave. Un work item generado
mientras el esquema estaba roto guarda el SQL roto y lo sigue ejecutando cada vez que alguien abre
Events. Arreglar la definicion no repara los work items ya generados.

Eso explica por que las busquedas ya funcionan y los work items no.

## Medicion contra el Platform DB de THD, 02 sep

Base: `sqldb-prd-wus2-arp-production-085-thd-platform`. Solo SELECT.

### La hipotesis de la SQL persistida cayo

`workview.WorkItemDefinitionGenerationRequest` trae `DeaggregationSql` en **NULL** en los 50 runs
mas recientes de markdowns. En THD esa columna no guarda nada. En Kinney Drugs si tenia contenido.
No se puede leer el SQL generado desde ahi.

Ademas `Failed = 0` y `DeaggregationRequestsCreated = 1` en los 50. La generacion nunca fallo.

### El work item de Ericka esta intacto en base

Run del periodo 27 ago: `2706EDE9-3612-405D-A7D6-72374576B65C`.

Definicion real: `/system/ebr/instant analytics/definitions/canada work items/md03-cit-d - consecutive markdowns for same payment card.fti`.
**La pantalla muestra MD03-APS-D y la definicion es md03-cit-d.** Verificar si son dos variantes.

Ese run produjo 2 deaggregation requests. Los dos con `Failed = 0`, `Duplicate = 0`, `Skipped = 0`.
Ejecutaron el 28 ago de 12:17:26 a 12:17:46, veinte segundos.

RowId 0 es el work item de Ericka. Sus parametros, textual:

```json
{"location_hierarchy2description":"0032-CANADA WEST",
 "location_hierarchy3description":"0157-CHARLENE TURNER",
 "storeno":7135,
 "cashierno":"DXM6269",
 "tender_accountnumber":"1262034041293206",
 "UniqueCountofApprissSecureID":3,
 "MaxofTransactionDate":"2026-08-27T00:00:00"}
```

Coinciden con la captura: store 7135, cashier DXM6269, region 0032-CANADA, district 0157-CHARL,
3 IDs unicos.

**Conclusion. El work item se genero bien, deaggrego bien y guardo sus parametros bien. El fallo
ocurre cuando la UI abre Events y arma la consulta de transacciones en vivo.** No es un artefacto
roto en base. Es una consulta que se construye en el momento.

Eso cambia la respuesta a Corey. Regenerar work items no arregla esto, porque el work item no esta
roto.

Encaja con lo que Simon reporto el 31 ago a las 14:34: seis busquedas quedaron bloqueadas por un
bug. El panel de Events se apoya en una definicion de busqueda. Es hipotesis, no esta confirmada.

Relacionado, de la seccion 6 de RCS-28543: el defecto de Floor and Decor RCS-28352, WISC
SupportingSearches type mismatch. Mismo concepto de busqueda de apoyo que la principal no resuelve.

### Hallazgo colateral, medido y no reportado

Cruzando los dos niveles por RunId, los unicos fallos reales de deaggregacion en THD desde el 01 ago
estan en una definicion que nadie ha mencionado en el ticket:

| Periodo | Definicion | Requests | Fallidos |
|---|---|---|---|
| 2026-08-28 | `snr4 - same name refunds - pro xtra name match.fti` | 6 | 3 |
| 2026-08-27 | `snr4 - same name refunds - pro xtra name match.fti` | 9 | 1 |

Cuatro de quince en dos dias. Cero fallos en markdowns y cero en el resto de definiciones.

Esto si es el patron de RCS-28543: work items que fallan en deaggregacion. Es un defecto distinto al
que reporta Ericka y vale la pena levantarlo, con la salvedad de que el rango medido son dos dias.
Correr la consulta sobre un rango mas largo antes de afirmar tendencia.

## Las dos preguntas del cliente

### 1. Corey: se pueden regenerar los IDs que tuvieron el error

Hipotesis, no confirmada: si el SQL roto esta persistido por work item, regenerar es la via
correcta. Lo que no sabemos es si existe un proceso soportado para regenerar work items ya emitidos,
ni quien lo ejecuta.

Eso lo responde Engineering o Delivery, no soporte. Simon reparo definiciones, no work items.

### 2. Valerie: cuantos work items se generaron sin transacciones

Valerie le pregunto a James DeJohn si hay una busqueda que se pueda crear. Vale aportar que la via
mas directa probablemente no es una busqueda de Secure.

Propuesta a verificar, solo lectura, contra el Platform DB de THD:

```sql
SELECT COUNT(*)
FROM [<PlatformDB>].[workview].[WorkItemDefinitionGenerationRequest] WITH (NOLOCK)
WHERE DeaggregationSql LIKE '%<columna_vieja>%';
```

Falta el nombre de la base y falta el nombre de la columna vieja. Los dos se resuelven antes de
correr nada. La base con `sys.databases` filtrando por `%085%`. La columna, con el log.

## Lo que destraba todo: el log del tracking code

`774fbb98-fc34-4cd0-8ee8-538f85d2967d` va a decir que columna falla y en que actividad. Sin eso, lo
de arriba es analogia con Kinney Drugs, no diagnostico de THD.

Juan no tiene acceso a los logs de HATR. Manisha Naik si, ella pego el primero el 31 ago a las 09:45
con el mismo formato. **Pedirselo a ella es el siguiente paso y cuesta un comentario.**

## Orden propuesto

1. Pedir en el ticket el log del tracking code `774fbb98-fc34-4cd0-8ee8-538f85d2967d`.
2. Con la columna en la mano, confirmar si el defecto es el de RCS-28543 o uno nuevo.
3. Enlazar RCS-28671 con RCS-28543 en Jira. Misma clase de defecto, mismo origen SnowTime.
4. Decidir ruta. Si el SQL roto esta persistido por work item, esto es Engineering, no soporte.
   RCS-28543 ya vive ahi con Shandana Khan en Under Engineering Review.
5. Responderle a Corey y a Valerie con estado, sin prometer regeneracion mientras nadie confirme que
   existe el proceso.

## Advertencia que viene de RCS-28543

No intentes repararlo editando el campo en Composer. Ahi lo probaron:

> "Deleting/re-adding this field worsened the failure count from 3/30 to 11/30. Re-adding via
> Composer re-copies the same stale binding rather than curing it."

Y su recomendacion explicita fue congelar las ediciones:

> "Option B. Freeze further Composer edits. Do not keep trial-and-error editing Expanded Display
> Fields. Each round has widened the failure blast radius."

## Nota de proceso

El ticket se cerro el 01 sep a las 14:11 y el cliente lo reabrio a las 15:12, 61 minutos despues. El
cierre se apoyo en la confirmacion de Corey del 31 ago, que cubria busquedas. Los work items nunca
se verificaron. Vale registrarlo en `flujos/` como criterio: cuando un defecto de esquema toca varias
superficies, confirmar una no autoriza a cerrar las otras.
