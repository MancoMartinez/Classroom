RCS-29224, hallazgos de Snowflake, 13 octubre 2026

Fuente: sesion de Claude en C:\git\SnowTime con snowflake-us, solo SELECT. Yo vi el reporte, no las salidas crudas.

Medido
1. inventory_itemposition: totalsalesquantity y totalreturnedquantity valen 0 en cerca del 100% de las filas del 2 al 12 oct. Solo 10-05 y 10-06 tienen valores y aun asi quedan bajo ardm_item (10-05: 698,551 contra 937,773. 10-06: 160,603 contra 934,597).
2. ardm_item suma entre 503k y 1.03M unidades de venta por dia en ese rango. Devoluciones: 44k a 95k por dia contra 0.
3. Llegadas en UTC, iguales cada dia: strinvdt desde 01:17 hasta 23:2x (232 a 441 archivos), TRE 07:20, tlog 22:10.
4. El primer strinvdt llega antes que el TRE todos los dias, unas 6 h antes. Cerca del 15% de los archivos strinvdt comparte corrida con el TRE y casi ninguno con el tlog (aproximacion por limite de :30).
5. Department nulo en filas Verify: 0.02 a 0.14% del 1 al 11 oct. 1.07% el 12 oct.
6. Taxamount en 0 en filas Verify: 32 a 37% entre semana, 11 a 19% en fines de semana. En XBR, casi 100%.

No probado
Causa de los ceros. Encaja con la mecanica del codigo, pero no se probo. El 7 oct, 56 de 375 archivos compartieron corrida con el TRE y los totales siguen en 0. Esa explicacion sola no alcanza.
Por que 10-05 y 10-06 tienen valores. El commit 4a3097a5c es del 5 oct, solo como pista.
El join de ardm_item a ardm_header no se valido.
Si antes del 2 oct (pyardm) los totales eran distintos de cero. Sin esa linea base no hay forma de saber si es regresion de la migracion.
Si el cero de impuesto es defecto. El fix copia taxamount desde el gemelo XBR y XBR llega casi siempre en 0.
Ninguna llegada cae a las 06:30 UTC (1:30 AM EST). Confirmar con Rocky que job se mueve y en que zona.
