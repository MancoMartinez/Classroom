RCS-28799. Seguimiento adicional consultado el 21 sep 2026.

Qué pasa: Under Engineering Review según enlace vivo de ENG-8650. Último comentario, Vlad el 18 sep: SNR1/SNR3 lentos bloquean el resto. El ENG del timeout tiene desarrollo terminado, aún sin release publicada.

Causa: búsquedas costosas y límite de una hora que no cancela ejecuciones. No demuestra que errores de columna provoquen el consumo. El 7 sep Mohammed redujo una búsqueda de más de 4 horas a 1 min 20 s. El 8 sep Vlad reportó nuevos timeouts aun usando la búsqueda actualizada.

Evidencia: 3325670, 2 sep, SNR4 succeeded. 3333942, 7 sep, optimización y solicitud del bug de timeout. 3337429, 10 sep, búsqueda sin optimizar referenciada por otras 18, requiere cambiar referencias y comunicar al cliente. 3351101, 18 sep, SNR1/SNR3 bloqueadores.
Fuente: https://trebuco.atlassian.net/browse/RCS-28799
https://trebuco.atlassian.net/browse/ENG-8650

Qué hago hoy: pedir a Vlad/Mohammed inventario de las 18 referencias, cuáles cambiaron, rendimiento por definición y cuáles siguen pendientes. Solicitar comparación en condiciones equivalentes. Confirmar comunicación de los cambios al cliente. Con Gabor, confirmar release y validación del timeout; la versión marca 24 sep y released=false.

Precedentes: RTS-206667 y RTS-207372. SNR4 exitoso invalida describir fallo permanente de todas sus corridas; no acredita estabilidad de todas las definiciones.

Compromisos: Mohammed indicó el 10 sep actualizar las 18 referencias y comunicarlo. No consta finalización en comentarios posteriores; Vlad sigue investigando el 18 sep.

Texto interno propuesto:
Vlad and Mohammed, the September 10 comment identifies 18 searches referencing the unoptimized search. Please confirm which references were updated, which remain outstanding, and the current runtime and completion results for SNR1 and SNR3. The improved runtime reported on September 7 was followed by new timeouts on September 8, so please include equivalent execution conditions in validation. Please also confirm whether the planned customer communication was sent. Track the performance work separately from deployment of ENG-8650.
