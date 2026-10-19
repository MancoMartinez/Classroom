# RCS-29129 flags de MRC pedidos por Roseanne, factibilidad en Composer

Verificado 25 sep noche impersonando a Roseanne. Solo lectura, nada construido.

Ranking: quick link visible y corre en su vista. Sus cajeros de ejemplo aparecen en el reporte.

Flag 2, MRC cuando la venta original fue tarjeta. Casi hecho. Existe "Return Report- Different Tender" de Carlos Figueroa, público y con quick link en carpeta 8: Transaction Type In Return, Exchange; Transaction Amount < 0; Sale Date requerido; Store opcional; Recalled Transaction Orig Primary Tender Type Not in Tender Type. Clonar y agregar Tender Type In Gift Card. No editar el original: banner de uso en otra aplicación.

Flag 1, MRC en return sin recibo. HIPÓTESIS: return con Gift Card y sin transacción recuperada, Orig Trans Number vacío. Los recibos del escenario 1 no traen bloque Original Transaction Information. Falta ver si Composer tiene operador de vacío. SRA lookups 3a y 3b son genéricos, no cubren esto.

Flag 3, MRC no transferible con varios clientes. HIPÓTESIS: agrupar por Gift Card Card No y contar Customer Full Name distintos mayor a 1 con Display Filter. Campos existen: Gift Card Card No, Tender Card Number Masked y Last4, Tender Cardholder Name, Customer Full Name, Header Customer ID, Recalled Orig Customer Name. Riesgo: el nombre solo existe si capturan cliente o loyalty; con número enmascarado pueden chocar tarjetas distintas.

Proceso: alcance nuevo, ticket SOW aparte enlazado a RCS-29129, creado por Juan con reporter Roseanne. Validar con JR el lunes si es soporte o CSM y si es facturable antes de dar alcance al cliente.
