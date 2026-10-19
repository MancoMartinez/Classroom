---
ticket: RCS-28638
cliente: Myer Australia, client 109, MYR
prioridad: High
estado_jira_verificado: Under Support Review, 31 ago 2026
tipo: plan de ejecucion
contexto: inbox/2026-08-31-rcs-28638-actualizacion-snowtime.md
---

# RCS-28638, plan de ejecucion

Ocho pasos. Los pasos 0 a 4 caben en una jornada. El 5 al 7 dependen de lo que devuelva el 2.

Datos fijos que vas a usar en todos los pasos:

    Cliente             109, MYR, Myer Australia
    Schema SnowTime     ARDM_PRODUCTION.C109_MYR
    Repo                dev.azure.com/apprissdevops/Sysrepublic Secure/_git/SnowTime
    Ruta de mapeo       dbt/clients/us/c109_myr/models/mapping/
    Campos              Proof Type, Order Number, Financial Statement Date
    Transaccion mala    2608273342446971618, alias RT2196182708260044
                        store 219, register 618, trans 44, 27/08/2026 12:11:49 GMT+10
    Valores esperados   Proof Type CUSTOMER ORDER RETURN, Customer Order Number 2002504903
    Transaccion buena   2608098315964575603, del 09/08, declarada correcta en RCS-28640
    Search del cliente  Public > Validation Folder

Nota de region. Myer es AU y el repo lo tiene bajo `us`. El pipeline de deploy se llama
`Deploy - SnowTime DBT / US - C109_MYR`. No busques una carpeta `au`.

---

## Paso 0. Rompe el silencio hoy. No puede esperar

Tu ultimo comentario es del 27 ago 21:18. Van cuatro dias. Christine respondio activamente en
RCS-28536, 28559 y 28639 en ese lapso, asi que esta mirando.

Este comentario no comunica hallazgos. Pide el dato que necesitas en el paso 6 y renueva el
contacto. Pegalo tal cual en RCS-28638.

    Hello Christine,

    I am working through the mapping of Proof Type, Order Number and Financial Statement Date on
    the transactions you flagged.

    To narrow the affected window precisely, could you confirm two things.

    First, the last transaction where these three fields displayed correctly, with its transaction
    ID and trading day. Your ticket reports the loss starting 09/08/26, and the related ticket
    RCS-28640 cites transaction 2608098315964575603 from 09/08 as correct, so I want to fix the
    boundary rather than assume it.

    Second, confirm whether the saved search you built for this defect is the same one in
    Public > Validation Folder, and whether it filters to a specific transaction type.

    I will follow up with findings once I have replicated your search against the same data set.

    Kind regards,

No transiciones el ticket. Queda en Under Support Review.

---

## Paso 1. Encuentra la tabla y las columnas reales

No asumas el nombre. `ARDM_PAIDIN_PAIDOUT_EXT` existe, asi que la analogia apunta a
`ARDM_HEADER_EXT`, y eso hay que confirmarlo. Tienes Snowflake y SnowTime.

    SHOW TABLES LIKE '%HEADER%' IN SCHEMA ARDM_PRODUCTION.C109_MYR;

    SHOW COLUMNS IN TABLE ARDM_PRODUCTION.C109_MYR.ARDM_HEADER_EXT;

Busca en la salida de columnas los tres campos. Los nombres probables, en minuscula y sin
separador, siguiendo el estilo de las otras tablas, `accountnumber` y `cardnumbermasked`:

    prooftype  o  x_prooftype
    ordernumber  o  customerordernumber  o  x_ordernumber
    financialstatementdate  o  x_financialstatementdate

Si no aparecen en ARDM_HEADER_EXT, ampliar:

    SHOW COLUMNS LIKE '%PROOF%' IN SCHEMA ARDM_PRODUCTION.C109_MYR;
    SHOW COLUMNS LIKE '%ORDER%' IN SCHEMA ARDM_PRODUCTION.C109_MYR;
    SHOW COLUMNS LIKE '%FINANCIAL%' IN SCHEMA ARDM_PRODUCTION.C109_MYR;

Anota los nombres exactos. Los pasos 2 y 4 los necesitan literales.

Criterio de decision. Si la columna no existe en ninguna tabla del schema, el defecto no es de
poblacion, es de esquema. Eso ya es un hallazgo para el hand over y el paso 2 sobra.

---

## Paso 2. La cross tab. Esta es la consulta que decide el ticket

Es el test de Matthew Everett, verbatim en metodo. Fija el tradingday, varia el writer. Sustituye
los nombres de columna por los del paso 1.

    SELECT
        DATE_TRUNC('month', tradingday)    AS tradingday_month,
        DATE_TRUNC('month', _ROW_CREATED)  AS writer_month,
        COUNT(*)                           AS rows_total,
        COUNT(prooftype)                   AS prooftype_pop,
        COUNT(ordernumber)                 AS ordernumber_pop,
        COUNT(financialstatementdate)      AS fsd_pop,
        ROUND(100.0 * COUNT(prooftype) / NULLIF(COUNT(*),0), 2)  AS pct_prooftype,
        ROUND(100.0 * COUNT(ordernumber) / NULLIF(COUNT(*),0), 2) AS pct_ordernumber,
        ROUND(100.0 * COUNT(financialstatementdate) / NULLIF(COUNT(*),0), 2) AS pct_fsd
    FROM ARDM_PRODUCTION.C109_MYR.ARDM_HEADER_EXT
    WHERE tradingday >= '2026-05-01'
    GROUP BY 1, 2
    ORDER BY 1, 2;

Como se lee el resultado.

Si un mismo `tradingday_month` sale poblado cuando `writer_month` es el mismo mes, y sale en cero
cuando `writer_month` es agosto, la causa es el rewrite del 14 de agosto. Mismo dato de origen,
distinto escritor, distinto resultado. Es el caso de RCS-28518.

Si todos los meses salen en cero desde el corte y no hay fila previa poblada, la rama nunca se
reimplemento en SnowTime. Es el caso de RCS-28536, mapping gap desde el dia que se escribio.

Si sale poblado en todos los writers y el cliente igual ve vacio, el dato esta en la tabla y el
problema esta en el render o en el search. Salta al paso 5.

Ahora el test a nivel de fila, sobre las dos transacciones que ya tienes. Este es el que va al
comentario porque es el que Christine puede reconocer.

    SELECT
        transactionid,
        tradingday,
        _ROW_CREATED,
        prooftype,
        ordernumber,
        financialstatementdate
    FROM ARDM_PRODUCTION.C109_MYR.ARDM_HEADER_EXT
    WHERE transactionid IN ('2608273342446971618', '2608098315964575603');

Lo que esperas ver si la hipotesis del rewrite se sostiene: la del 09/08 con `_ROW_CREATED` de
agosto temprano y los campos poblados, la del 27/08 con `_ROW_CREATED` posterior y los campos en
NULL. Si las dos salen en NULL, la transaccion buena de RCS-28640 se ve bien en la UI por otra via
y hay que revisar el paso 5.

Solo SELECT. No corras ningun rebuild. Matthew lo dejo por escrito en RCS-28518:

> REBUILD CAUTION: do not run a repair rebuild before the mapping fix is deployed. A rebuild is
> what caused this damage, and rebuilding again with the current mapping would re-null anything
> still intact.

---

## Paso 3. ArdmProdParity.md. El atajo que puede cerrar el diagnostico en una tarde

El reporte de paridad es donde estos campos debieron detectarse antes del cutover. Matthew encontro
su columna marcada BLOCKED con 19.68% de match en la linea 748.

En el repo SnowTime, busca los tres campos en:

    ArdmProdParity.md
    models/ardm_mapping.md

Si aparecen como BLOCKED, tienes el diagnostico documentado y la prueba de que el gap se conocia
antes del cutover. Eso cambia el tono del hand over: no es un hallazgo nuevo, es un pendiente que
no se persiguio.

Advertencia. Matthew probo que ese reporte tiene entradas obsoletas en las dos direcciones. En
RCS-28518 el BLOCKED era real. En RCS-28536 el BLOCKED era falso y la poblacion escasa era lo que
el origen manda de verdad. Un BLOCKED no es prueba por si solo. Confirmalo contra el paso 2.

---

## Paso 4. Compara la rama contra pyardm

El header de una transaccion sale de `map_ardm_header.sql`, rama tct. Ahi vive el mapeo de Header
Ext.

    dbt/clients/us/c109_myr/models/mapping/map_ardm_header.sql

Busca dentro los tres campos. Lo que tienes que responder es una sola pregunta: la rama que puebla
Proof Type, Order Number y Financial Statement Date, existe o emite NULL.

El patron a reconocer, de RCS-28518:

> map_ardm_tender.sql:333 emits null::VARCHAR as accountnumber

Si ves un `null::VARCHAR` o un `null::DATE` en el lugar de estos campos, es el mismo defecto con
otra columna.

Despues busca el equivalente legacy en pyardm. Los que ya se citaron son `ARDM_1_Tender.sql` y
`ARDM_91_Poshash.sql`, asi que el de header sigue la misma convencion numerada. Compara rama por
rama. Lo que pyardm poblaba y SnowTime no, es tu hallazgo.

Si no tienes lectura en el repo de Azure DevOps, no pidas permisos por este ticket. Pidele a
Matthew Everett que corra el grep. Ya tiene el contexto entero y lo hizo tres veces esta semana.
Azure DevOps es de solo lectura para nosotros, nada de comentar ni aprobar.

---

## Paso 5. El segundo defecto que el cliente no reporto

En tu captura del Retail Transaction Details, la linea de razon dice:

    Reason ID:RC19
    Reason Description:$lineItemDomainSpecific.returns.returnNotes

Ese es un token de plantilla sin resolver. El render pide una propiedad que el payload ya no expone
con ese nombre. El receipt view cae a `OTHER REASON` mientras el detalle guarda `RC19`.

El archivo del render ya esta identificado por los hermanos:

    detail-panel.html

Matthew documento en RCS-28518 que las lineas 303-305 hacen un fallback de tres pasos para Card No,
`accountnumber` luego `cardnumbermasked` luego `x_referencenumber`. Y en RCS-28536 que las lineas
130-137 renderizan `{{pipo.reasontext}}` sin prefijo de etiqueta, por lo cual un valor de texto
libre se lee como si fuera una etiqueta.

Busca en ese archivo el bloque de Return/Exchange With Proof Of Purchase y mira de donde lee Proof
Type y Financial Statement Date. Si los labels se emiten siempre y el valor viene de la tabla, el
vacio del recibo es consecuencia del paso 2 y no un defecto aparte. Si el token
`$lineItemDomainSpecific.returns.returnNotes` aparece hardcodeado ahi, es un defecto propio y va al
hand over como segundo item.

Este paso te da algo que Matthew no tiene: reportas un defecto que el cliente no vio.

---

## Paso 6. Cierra la ventana de fechas

Depende de la respuesta al paso 0.

La tension a resolver: el cliente declara perdida desde el 09/08/26 y RCS-28640, mismo cliente y
misma fecha declarada, aporta la transaccion 2608098315964575603 del 09/08 como correcta.

Si el paso 2 devuelve `_ROW_CREATED` por transaccion, la ventana la fijas tu sin esperar al cliente.
La fecha que importa no es el tradingday que el cliente ve, es cuando se escribio la fila.

Coordina con Nikita Rathore antes de responder. Ella tiene RCS-28640 desde hoy, misma fecha de
corte, y el contraejemplo esta en su ticket. Si los dos preguntan lo mismo por separado, Christine
lo va a notar.

---

## Paso 7. Escribe el hand over

Copia la estructura de Matthew. Es la que Engineering ya acepta en este cliente. Seis bloques:

    Status                que se sabe y si esta arreglado o no
    Root cause            el archivo, la linea, y que hacia pyardm que SnowTime no hace
    Production evidence   la cross tab del paso 2 con numeros, y el test de dos filas
    Scope                 cuantas transacciones y desde cuando
    Related               a que ticket se parece y por que arreglar uno no arregla el otro
    Required action       el fix, con la advertencia de rebuild

Reglas para el texto. Ingles, sin markdown, sin negritas, sin guiones como conectores. No afirmes
mas alla de lo que midio la consulta. Si el remedio no esta probado, escribelo, que es exactamente
lo que Matthew hizo bien y lo que su comentario al cliente del 31 ago contradice.

Ruta de escalacion. Data mapping en produccion va a Delivery, no a Engineering. Myer es Secure
Store, asi que Tomasz Mikunda o Carl Costelow. Este caso toca codigo del repo SnowTime, asi que
entra por el mismo canal que RCS-28518 y RCS-28536 y termina en un PR. Menciona ENG-6418 como
origen del cutover.

Cuando llegues aca, usa la skill `cerebro-comentario` para el hand over interno y
`cerebro-respuesta-cliente` para lo que ve Christine.

---

## Paso 8. Transicion y cierre

Under Support Review es donde esta y donde debe quedarse hasta que el paso 2 devuelva numeros.

Cuando escales, la transicion es la que usaron los hermanos. RCS-28518 y RCS-28536 pasaron a Work
in progress mientras Engineering trabajaba, y a Under Customer Review al responderle a Christine.

No pases a Under Customer Review con lenguaje de verificado sin haber medido tu mismo. La nota de
RCS-28559 dice `THE REMEDY IS UNPROVEN` y su comentario al cliente del 31 ago dice
`completed and verified`. No consta el lab rebuild que la nota exige. Si Christine reabre los tres,
ese es el flanco.

Al terminar:

    bin/anotar RCS-28638 "lo que hiciste"
    python3 bin/indexar_tickets.py

Y si el metodo funciona, promuevelo a `flujos/` como runbook de mapeo roto post migracion. Ese
runbook es el T-012 del tracker, esta en Not Started, y este ticket es material suficiente para
escribirlo.

---

## Criterio de parada

Si el paso 2 y el paso 4 coinciden en que la rama no existe o emite NULL, tienes causa raiz y el
ticket se escala. No sigas midiendo.

Si el paso 2 muestra el dato poblado en la tabla, el defecto esta en el search o en el render, no
en el mapeo, y el ticket cambia de dueno. Ahi el paso 5 pasa a ser el principal.
