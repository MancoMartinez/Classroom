---
ticket: RCS-28638
cliente: Myer Australia (client 109, MYR)
prioridad: High
estado_jira_verificado: Under Support Review, 31 ago 2026
updated_en_jira: 2026-08-27T21:18:50, sin movimiento en 4 dias
reemplaza_hipotesis_de: inbox/2026-08-28-rcs-28638-myer-header-ext.md
---

# RCS-28638, actualizacion del 31 ago. La causa raiz ya esta establecida y no es la que supuse

## Correccion de la hipotesis anterior

El 28 de agosto propuse el payments project como causa candidata, apoyado en la cita del cliente en
RCS-28518. Esa hipotesis es incorrecta. La causa raiz de la familia completa de defectos de mapeo
de Myer esta establecida por Matthew Everett con evidencia de produccion y es otra.

Myer paso de Greenplum legacy a SnowTime. Go live ENG-6418, cerrado el 17 ago 2026. Validacion del
cutover ENG-3795. La reimplementacion de pyardm en SnowTime dejo logica sin portar, y cada ticket
de Myer es una omision distinta de la misma migracion.

## Lo que cambio en Jira entre el 28 y el 31 de agosto

    RCS-28639  Closed / Resolved         Vlad Bogus         31 ago 07:24
    RCS-28518  Under Customer Review     Matthew Everett    31 ago 05:41
    RCS-28536  Under Customer Review     Matthew Everett    31 ago 05:38
    RCS-28559  Under Customer Review     Matthew Everett    31 ago 05:36
    RCS-28537  Work in progress          Matthew Everett    31 ago 05:42
    RCS-28640  Work in progress          Nikita Rathore     31 ago 09:09
    RCS-28612  Work in progress, subio de Medium a High     Sebastian Garces   29 ago
    RCS-28638  Under Support Review      Juan Martinez      27 ago 21:18, sin tocar

RCS-28638 es el unico de los siete sin una sola linea de investigacion. Es High. Lleva cuatro dias.

## La causa raiz, citada

Matthew Everett, RCS-28518, hand over del 26 ago:

> map_ardm_tender.sql:333 emits null::VARCHAR as accountnumber. Legacy pyardm
> ARDM_1_Tender.sql:128-132 populated it via a four-branch CASE; SnowTime implements only branch 4,
> the POS hash, restored in enrich_ardm_tender.sql. Branch 3, the gift/return card number where
> length is under 20, was never reimplemented.

Matthew Everett, RCS-28559, hand over del 26 ago:

> Legacy pyardm had exactly this catch-up: ARDM_91_Poshash.sql, a 90-day trailing pass re-filling
> any tender with length(accountnumber) under 60. SnowTime has no equivalent.

Matthew Everett, RCS-28536, resolution summary del 26 ago:

> The mapping was wrong from the day it was authored.

El patron se repite: SnowTime no reimplemento una rama que pyardm si tenia.

Matthew separa causas de forma tajante y hay que respetarlo. RCS-28518:

> Related to RCS-28559: same column, different branch of the legacy CASE. That ticket is branch 4
> reimplemented without a self-heal, a timing gap. This one is branch 3 never reimplemented, a
> mapping gap. Fixing one will not fix the other.

## El mecanismo que explica la fecha 09/08/26 del cliente

El cliente reporta perdida desde el 09/08/26, seis dias antes del corte del 13 al 17 de agosto. Eso
parecia una contradiccion. Deja de serlo con el segundo hallazgo de Matthew.

RCS-28518:

> A large rewrite on 2026-08-14 then re-ran that mapping across historical tradingdays that were
> already correctly populated, replacing good values with NULL. This is data destruction rather
> than a forward-only gap, which matters for how it is audited: a check asking whether the new
> pipeline populates a column going forward would miss it entirely.

El rewrite del 14 de agosto reescribio dias comerciales anteriores y los nuleo. Una transaccion del
9 de agosto pudo escribirse bien ese dia y perder el valor cuando el rewrite la reproceso. El
tradingday no cambia, el writer si.

La prueba que uso Matthew, y que sirve tal cual para Proof Type, Order Number y Financial Statement
Date. RCS-28518:

> Holding tradingday month fixed and varying the writer month: May tradingdays written in May show
> 32.12% populated; the same May tradingdays written in August show 0.00% across 3.28M rows.
> Identical source bytes, different writer, different result. Row level on the customer's own
> examples: her 30 Apr "correct" receipt was written 2026-04-30 and retains its value; her 30 Jul
> "defect" receipt was rewritten 2026-08-14T22:00:20 and lost it, same tender types. A source-side
> POS change was tested as the alternative hypothesis and disproven by the same cross-tab.

Esa cross tab de tradingday contra _ROW_CREATED es la consulta que decide RCS-28638.

## Territorio nuevo, confirmado

Proof Type, Order Number, Financial Statement Date y Header Ext no aparecen en ninguno de los seis
tickets hermanos. Cero menciones. Nadie ha mirado estos campos. El diagnostico hay que hacerlo, no
hay nada que copiar. La plantilla de metodo si se copia entera.

## Referencias tecnicas cosechadas de los hermanos

    ENG-6418     go live cutover Greenplum a SnowTime, cerrado 2026-08-17
    ENG-3795     cutover validation
    PR 56577     dev.azure.com/apprissdevops/Sysrepublic Secure/_git/SnowTime/pullrequest/56577
                 merge commit ba487d5d0, un solo archivo
    Deploy       ADO pipeline Deploy - SnowTime DBT / US - C109_MYR, 2026-08-25 15:07:24Z

    2026-08-13   corte duro, GP3 deja de cargar
                 historical_transaction_id_map trae cutoff='2026-08-13' hardcodeado
    2026-08-14   rewrite que nuleo historicos, y correcciones de offset del parser POSHASH
    2026-08-15   inicio del 100% de fallo en accountnumber
    2026-08-17   cutover declarado, Matthew corrige que el break se ve el 13

Archivos del repo SnowTime, ruta de mapeo por cliente:

    dbt/clients/us/c109_myr/models/mapping/map_ardm_paidin_paidout.sql
    map_ardm_header.sql          la rama tct emite el header, aqui vive Header Ext
    map_ardm_tender.sql
    enrich_ardm_tender.sql
    dbt_project.yml
    detail-panel.html            render del receipt view, lineas 130-137 y 303-305
    ArdmProdParity.md            reporte de paridad, lineas 699-706 y 748
    models/ardm_mapping.md

Legacy pyardm, para comparar rama por rama: ARDM_1_Tender.sql, ARDM_91_Poshash.sql.

Tablas: ARDM_PRODUCTION.C109_MYR.ARDM_HEADER, ARDM_TENDER, ARDM_PAIDIN_PAIDOUT,
ARDM_PAIDIN_PAIDOUT_EXT, ARDM_GIFTCARD, REFERENCE_CARD. Legacy en GP3: ardm_109.ardm_header,
ARDMPROD.ARDM_109. Funcion resolve_historical_id().

Advertencia operativa de Matthew, RCS-28518, aplica a cualquier reparacion:

> REBUILD CAUTION: do not run a repair rebuild before the mapping fix is deployed. A rebuild is
> what caused this damage, and rebuilding again with the current mapping would re-null anything
> still intact.

Y el estado del reporte de paridad, que es donde deberian haberse detectado estos campos:

> The parity report recorded this column as BLOCKED with a 19.68% match (ArdmProdParity.md:748);
> include it in the wider parity review.

Si Proof Type, Order Number o Financial Statement Date figuran como BLOCKED en ArdmProdParity.md,
el ticket queda diagnosticado en una tarde.

## Presion de negocio registrada

Bryant McAnnally, RCS-28559, 29 ago:

> Can you please provide how quickly you can resolve this ticket and RCS-28518? We will be having
> an in person meeting with the customer and it's critical to have the issues related to the recent
> Showtime upgrade resolved prior to that meeting.

Bryant McAnnally, RCS-28612, 29 ago:

> This seems to be tied to several other issues related to the Showtime migration and needs to be
> immediately corrected for this customer. Please have someone review it as soon as possible.
> There are 5+ tickets in progress.

Escribe Showtime, el sistema es SnowTime. RCS-28638 es uno de esos tickets.

## Riesgo que Juan no debe repetir

Los tres tickets que Matthew paso a Under Customer Review el 31 ago usan lenguaje de completed and
verified. La nota tecnica de RCS-28559 dice lo contrario:

> THE REMEDY IS UNPROVEN. It should work ... But there is no observed case of a rebuild repairing
> this column. A single-day lab rebuild would settle it. Please do not present the fix as confirmed
> until that runs.

No consta en ningun comentario que ese lab rebuild se haya ejecutado. Si Christine reabre, la
posicion queda expuesta. Juan no debe usar lenguaje de verificado sin la medicion propia.

## Que verificar, en orden

1. Correr la cross tab de tradingday contra _ROW_CREATED sobre la tabla de extension de header en
   ARDM_PRODUCTION.C109_MYR, para proofType, order number y financial statement date. Solo SELECT.
   Si el mismo tradingday poblado con writer de agosto sale en cero, es el rewrite del 14.
2. Buscar los tres campos en ArdmProdParity.md. Si estan BLOCKED, el diagnostico esta hecho.
3. Comparar la rama que puebla estos campos en map_ardm_header.sql contra el pyardm equivalente. Si
   la rama no existe en SnowTime, es una mapping gap como RCS-28518.
4. Confirmar la ventana real con el cliente. RCS-28640 declara la misma fecha de corte y aporta la
   transaccion 2608098315964575603, del 09/08, como correcta.

## Transicion sugerida

Ninguna todavia. Queda en Under Support Review hasta cerrar la medicion.
