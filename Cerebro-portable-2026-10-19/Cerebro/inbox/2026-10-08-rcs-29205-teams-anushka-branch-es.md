Hola Anushka, Adarsh, una actualización rápida sobre RCS-29205. Ryan DeVries de Delivery también revisó esto y tiene un branch en el repo de SnowTime que les puede servir: rdevries-rcs29205

Agrega un acumulador reference_partnerownedtendertoken y un modelo enrich_ardm_tender para los dos campos de token, siguiendo el precedente de c179_kny, y un script de seed histórico por año que no se ha corrido. Algunas notas de Ryan:

1. Starbucks solo tiene 1 año de retención, así que el seed quizá no necesite toda la historia.
2. Los dos schemas deberían tener la historia completa antes del cutover. Las filas desde el 27 ago son las que están mal.
3. Las filas del 27 ago en adelante necesitarían un rebuild desde la fecha del cutover para quedar bien.
4. Los campos de razón de paid in y paid out probablemente tienen el mismo problema, pero su branch no los cubre.

¿Esto les sirve para el arreglo? Cuando los datos se reconstruyan, también habría que regenerar los work items del 24 ago al 27 sep. ¿Quieres que te asigne RCS-29205? ¡Muchas gracias!
