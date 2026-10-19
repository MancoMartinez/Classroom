# SBX work items, 7 oct 2026

Adarsh Kumar, Teams: abrir chat con Anushka Chaudhary, ingeniera SBX de SnowTime, y dejarlo a el en copia. Adarsh ya le aviso.
RCS-29205: chat grupal Juan, Anushka y Adarsh con la lista de 5 campos. Se le pregunta a Anushka si quiere el ticket asignado.
Ruta: tickets SnowTime de c166_sbx van a Anushka Chaudhary, via Adarsh.

Anushka Chaudhary, 7 oct: causa raiz confirmada. Los mapeos de SnowTime de c166_sbx emiten NULL en los 5 campos; venian de filas construidas por pyardm, que terminaron a fines de agosto. Ella revisa el mapeo.
Repoblacion segun Anushka: PAIDINPAIDOUT si (feed completo, 319,709 filas, falta modelo plano y filas de header con transaction IDs historicos, cliente usa historical_transaction_id_enabled). PARTNEROWNEDTOKEN y PARTNERIDONTOKEN solo en parte: pyardm usaba tabla permanente ref_employee_owntendertoken que no esta en ARDMPROD; reconstruccion desde ardm_customer da 44% a 6 meses. REFUNDTOOWN depende de los tokens, 6 filas por semana.
Riesgo: el periodo 24 ago a 27 sep regenerado puede quedar parcial. Pendiente que Anushka diga si hacia adelante queda completo.
Jira 7 oct: RCS-29207 sigue Completed, falta Closed. RCS-29206 sin actualizar desde el 1 oct, el seguimiento no se ha pegado.
