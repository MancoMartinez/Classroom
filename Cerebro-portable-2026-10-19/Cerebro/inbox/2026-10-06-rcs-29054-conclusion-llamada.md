# RCS-29054 Big 5, conclusión de la llamada del 6 oct

Qué pasa
Región y distrito de las 382 tiendas del xlsx de Nancy ya coinciden con Secure. Faltan 82 tiendas donde el LP Manager difiere, todas con Mike Ibarra en el xlsx. Ibarra tiene 38 en el archivo de Peter, 36 en Secure y 116 en el xlsx.

Causa
Confirmada por Peter y Nancy en la llamada: el archivo location_MMDDYYYY.csv sale del sistema de HR de Big 5, UKG, y su columna LP Manager aún trae la asignación vieja. IT de Big 5 no puede editar UKG. HR debe actualizarlo. El dueño de UKG ya recibió un correo de Nancy y dijo no saber del tema. El nombre suena como Franz o Frans en el audio, confirma el nombre.

Evidencia
Audio 18:30 a 20:40, Peter: el archivo viene de UKG y IT no tiene acceso.
Audio 16:33, Peter: buscar Ibarra en su archivo del 6 oct da 38 resultados.
Audio 12:36 a 15:25: el storemaster.txt es legacy de Aspect y no trae LP Manager.

Qué hago hoy
1. Publica en el ticket la lista de las 82 tiendas con el nombre exacto, Ibarra, Michael A. Nancy aceptó.
2. Escribe a Peyman. Peter dice que envía el archivo completo cada día entre 8 y 9 AM. Peyman recibe uno casi vacío. Pídele que mire dónde se pierde.
3. Mañana corre SELECT COUNT(*), COUNT(X_RLPM) sobre ARDM_PRODUCTION.C147_BFV.REFERENCE_LOCATION. Hoy son 534 y 435.

Precedentes
RCS-27342 y RCS-28576, RLPM en blanco en Big 5.

Compromisos
Publicar la lista hoy. Verificar cuando llegue el siguiente archivo. Los 2 tiendas que cierran se quedan hasta inicios del próximo año.
