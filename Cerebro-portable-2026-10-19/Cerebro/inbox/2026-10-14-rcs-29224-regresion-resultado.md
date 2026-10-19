RCS-29224, regresion de inventory_itemposition, 14 octubre 2026

Fuente: dos sesiones de Claude en el repo SnowTime. La de Daniel lee solo codigo. La mia suma SELECTs en snowflake-us. Yo vi los reportes, no las salidas crudas.

Medido
1. Las filas en cero son normales: 99.94% de unas 955M por dia. La senal es la suma. totalsalesquantity suma 0 el 2 al 4 y el 7 al 13 oct, contra 0.5 a 1.0M en ardm_item.
2. Del 15 al 27 sep, posicion y ardm_item coinciden en 97 a 98%. Parece historia de pyardm, inferido por fechas.
3. El 28 sep al 1 oct las escribio SnowTime en un catch up del 7 oct, con 83 a 94%.
4. Llegadas UTC para el dia D: filas de posicion de D 07:13 a D+1 01:18, POS Verify D+1 07:20, tlog D+1 22:08.
5. pyardm reconstruia el dia completo en cada corrida (x_Inventory_01_Position.sql). SnowTime escribe la fila cuando llega strinvdt y no la reescribe cuando llega el POS.
6. Ningun REBUILD_RANGE toco inventory_itemposition. Hubo backfills el 2, 3 y 5 oct, uno fallido.

No probado
Que sea el unico mecanismo. Por que el 5 y 6 oct tienen valores. El fallo del test del 2 oct (arreglado en caed3563c). Filas bajas el 28 sep, 1, 5 y 12 oct. Si pasa en C138_NOR y C177_CTC, migrados en el mismo hilo.

Efecto en el cambio de Rocky
Mover inventario 8 h no arregla ni empeora de forma clara. Solo cambia que chunks comparten corrida con el POS. Inferencia sin verificar.

Arreglo propuesto, solo texto
A: recalcular tras llegar el POS leyendo ardm_item de produccion. B: REBUILD_RANGE diario despues de las 07:30 UTC. Limpieza: una corrida unica para los dias en cero, accion de operador.

Otros hallazgos de la sesion de Daniel, solo codigo: tender cash ignora el cambio, lineas void XBR salen como venta, inventory_document pierde lineas, buckets de movimiento con 290 de unos 729 codigos. No tocan este ticket.
