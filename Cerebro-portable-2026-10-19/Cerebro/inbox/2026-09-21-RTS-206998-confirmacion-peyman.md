RTS-206998 | Actualizado 2026-09-22 | Peyman y Gulshan

Fuentes: mensajes y capturas aportados por Juan. No se inspeccionaron los logs completos en vivo. El enlace de Gulshan llegó truncado; build identificado: 819877.
https://trebuco.atlassian.net/browse/RTS-206998
https://dev.azure.com/apprissdevops/DataOps/_build/results?buildId=818999&view=results
https://dev.azure.com/apprissdevops/DataOps/_build/results?buildId=819877&view=results

Build 818999: ecomintl_pd_loader.py arroja invalid input syntax for type json, Character with value 0x0a must be escaped. El log dice Process continues. Después get_exchange_rates falla al conectar con openexchangerates.org y detiene el proceso. Peyman confirma recuperación desde get_exchange_rates cuando volvió la conectividad. Cree que los archivos fallidos no se reprocesaron ni se notificaron; no lo afirma con certeza. Propone pedir archivos corregidos.

22 sep: Gulshan reporta que build 819877 ejecutó get_exchange_rates.py, analyze.py, load_ardm.py, load_ardm_ecom.py, load_ardm_ecom_intl.py, appriss_snowflake, analyze.py y clean.py. Dice que solo queda ecomintl_pd_loader.py.

Conclusión: la recuperación avanzó por las etapas posteriores, pero el loader de ingestión internacional quedó fuera o pendiente según Gulshan. Es el mismo script de las excepciones JSON originales. Ejecutar load_ardm_ecom_intl.py no demuestra reingestión de los archivos fallidos por ecomintl_pd_loader.py. No hay prueba de recuperación completa de esos datos, tampoco de pérdida definitiva. Una lista de pasos ejecutados no valida cada archivo.

Hoy: identificar los archivos aún pendientes y verificar cargas posteriores antes de solicitar reenvío, para evitar duplicados. Si siguen rechazados, obtener archivos corregidos y validar ingestión y carga final. No reiniciar sin corregir o aclarar el JSON inválido; no atribuir su origen al cliente sin revisar el original. SAS y SQL aclarados en sus notas; GP3 sigue aparte. Sin ETA ni prevención del timeout confirmados. Jira y producción sin cambios. Juan ingiere con cerrar.

Respuesta propuesta, no enviada:
Thanks, Gulshan. That confirms the later steps ran, while ecomintl_pd_loader.py remains outstanding. Could you identify which files from the original failed run still need a corrected resend, checking whether any were loaded in a later run? We can then send the client the exact list and verify the data after reprocessing.
