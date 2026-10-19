# Instructivo. RCS-28756, Nike ECOM Load issue

## Paso 1. Confirmar que Nike no respondio despues del ultimo comentario

Donde se ejecuta: Jira, lectura.

Abre RTS-206999 y revisa si hay comentario nuevo despues del de Akshaya Purappemane del
2026-09-04 a las 19:16 hora este. Ese es el ultimo registrado al momento de este informe.

Que se espera ver: ningun comentario de Nike todavia. El proximo contacto agendado es el
2026-09-08 a las 8:00pm IST.

Si falla, es decir si Nike ya respondio: no pegues el comentario del Paso 2 tal cual. Avisa que
cambio y se redacta de nuevo con la respuesta del cliente incorporada.

## Paso 2. Pegar el comentario interno en RCS-28756

Donde se ejecuta: Jira, comentario en RCS-28756. Escritura, autorizado por Juan.

El bloque completo, listo para copiar y pegar:

```
This ticket tracks the same root cause under investigation in RTS-206999. No c67_rawdata_order files have loaded since prd-datacloud-wus2-ehub-1/c67_rawdata_order/2026/08/27/19/02_42_1.avro, confirmed through the load_raw_ecom_blob.py logs referenced in RTS-206999. Carl confirmed on 2026-09-04 that Appriss ingestion services are running.

I reviewed the ARDM load logs for client 067 covering the last successful window, pipeline runs 20260827.2 through 20260828.1. The pipeline completed all SQL transformation steps through Step 20, Loading JSON Table, without a fatal error. One transient 503 occurred during ARDM_13_Tender_Ext.sql at 23:06:22 on 2026-08-28 and the next file executed successfully 39 seconds later. trickle_condition.py reported Vacuum condition not fulfilled, out of time window, and exited cleanly. That message reflects the trickle scheduler stop time logic. It is not an error.

This rules out the ARDM transformation layer as a contributing cause. The gap sits upstream of ARDM, in the raw ECOM ingestion from Nike.

The ARDM Trickle failure in get_exchange_rates.py on 2026-09-02, recovered by L2 on 2026-09-03, is a separate incident. It does not explain the file gap that started four days earlier.

Nike was notified by email on 2026-09-04. Next client follow up is scheduled for 2026-09-08, 08:00 PM IST, per RTS-206999. No action pending on the Appriss side until that follow up or until new files arrive.
```

Que se espera ver: el comentario visible bajo RCS-28756, con el enlace a RTS-206999 ya activo
como smart link de Jira.

Si falla: si Jira rechaza el bloque por longitud, divide en dos comentarios en el mismo orden.

## Paso 3. Transicionar RCS-28756

Donde se ejecuta: Jira, menu de transiciones de RCS-28756. Escritura, autorizado por Juan.

Transicion sugerida: `Under Customer Review`.

Que se espera ver: el estado cambia de `Under Support Review` a `Under Customer Review`.

Si falla: si esa transicion no aparece en el menu para tu rol, deja el ticket en
`Under Support Review` y agrega una linea al comentario del Paso 2 indicando que el estado no se
pudo mover y por que.

## Paso 4. Registrar en la cola de Cerebro

Donde se ejecuta: terminal.

```
bin/anotar RCS-28756 "Triage completo. ARDM cliente 067 revisado en logs del 27 y 28 de agosto, sin fallas del lado Appriss. Comentario interno pegado, transicion sugerida a Under Customer Review. Pendiente respuesta de Nike, seguimiento 2026-09-08 via RTS-206999."
```

Que se espera ver: la linea se agrega a la bitacora de la cola sin error.

## Transicion sugerida

```
Under Customer Review
```

## Comentario que Juan pega

```
This ticket tracks the same root cause under investigation in RTS-206999. No c67_rawdata_order files have loaded since prd-datacloud-wus2-ehub-1/c67_rawdata_order/2026/08/27/19/02_42_1.avro, confirmed through the load_raw_ecom_blob.py logs referenced in RTS-206999. Carl confirmed on 2026-09-04 that Appriss ingestion services are running.

I reviewed the ARDM load logs for client 067 covering the last successful window, pipeline runs 20260827.2 through 20260828.1. The pipeline completed all SQL transformation steps through Step 20, Loading JSON Table, without a fatal error. One transient 503 occurred during ARDM_13_Tender_Ext.sql at 23:06:22 on 2026-08-28 and the next file executed successfully 39 seconds later. trickle_condition.py reported Vacuum condition not fulfilled, out of time window, and exited cleanly. That message reflects the trickle scheduler stop time logic. It is not an error.

This rules out the ARDM transformation layer as a contributing cause. The gap sits upstream of ARDM, in the raw ECOM ingestion from Nike.

The ARDM Trickle failure in get_exchange_rates.py on 2026-09-02, recovered by L2 on 2026-09-03, is a separate incident. It does not explain the file gap that started four days earlier.

Nike was notified by email on 2026-09-04. Next client follow up is scheduled for 2026-09-08, 08:00 PM IST, per RTS-206999. No action pending on the Appriss side until that follow up or until new files arrive.
```
