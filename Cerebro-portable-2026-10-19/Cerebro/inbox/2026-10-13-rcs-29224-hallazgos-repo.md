RCS-29224, hallazgos del repo SnowTime, 13 octubre 2026

Fuente: sesion de Claude dentro de C:\git\SnowTime, solo lectura. Es lectura de codigo, sin datos de Snowflake. Yo no vi el repo.

Derivado del codigo
1. inventory_itemposition usa strinvdt como base (map_inventory_itemposition.sql:107-133). Los totales de ventas y devoluciones salen de ardm_item y ardm_header (198-222) y se unen por tienda, SKU y dia (289-292).
2. Sin POS en la corrida, los totales quedan en 0 por coalesce (266-269). Es cero, no nulo.
3. Un POS tardio no dispara recalculo. La fila del dia D solo se reemite cuando strinvdt de D entra en la ventana de la corrida (236-248; mapping_transaction_registry.sql:46-69). Si POS y strinvdt llegan en corridas distintas, el merge sobrescribe con la suma parcial (sin merge_coalesce_on_update para esta tabla, dbt_project.yml:126-127).
4. Reparacion: REBUILD_RANGE manual (dbt/docs/rebuild-range.md) o re entrega de strinvdt del dia.
5. La carga corre cada hora a :30 UTC si el stream tiene datos (create_task.sql:125-129, 213). Ningun modelo espera completitud de POS, tlog o strinvdt. Confirma a Viraj y Daniel y contradice a Talos.
6. PR 58891 no toca inventory_itemposition. Solo enrich_ardm_item.sql y un script de catch up (vibeZone/c021-tlog-dept-tax-catchup.sql). Su logica supone Verify a las 07:20 y tlog a las 22:10 en corridas distintas.
7. Ventana raw de 7 dias por file_arrival_time (raw_window.sql:55). Un corrimiento de 8 horas no saca archivos de ventana. Los mueve entre corridas y dias de trading.

No verificado
Orden real de llegada de strinvdt y POS por dia. Falta consulta en Snowflake.
Si tlog_twin sigue valido cuando el tlog llega antes que Verify tras el corrimiento.
Searches o work items de C021 antes de las 9:30. No estan en el repo.
9:30 EST son 14:30 UTC, o 13:30 UTC si el cliente habla de hora del Este con horario de verano. Confirmar con Rocky.
Alertas L1 de llegada. CLIENT_ALERTING_CONFIG vive en Snowflake.

Conclusion: la captura 05 ("inventario solo toca costos") queda descartada. Jenny tiene razon.
