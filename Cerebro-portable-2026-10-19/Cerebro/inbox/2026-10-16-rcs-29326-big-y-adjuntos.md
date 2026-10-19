RCS-29326 Big Y, adjuntos de un caso antiguo no abren
Jira en vivo 16 oct: Work in progress, asignado a Enrique, sin ENG enlazado.

QUE PASA
Kevin Snyder abre un adjunto del caso 7546660907071138MB y recibe la pantalla "Something Unexpected Happened". Un compañero ve lo mismo. La URL es attachments.aspx con filename \KCCMS Attachments\Case 7546\HPIM0285[1].jpg y system=LPMS, tenant bigy.

CAUSA
Hipótesis, sin confirmar. El nombre guardado es una ruta heredada con barras invertidas y corchetes. Una segunda hipótesis sigue viva: sesión vencida, que explicó el ticket de Big Y del 11 ago.

EVIDENCIA
1. Talos, 7 oct: el texto de la pantalla es fijo para cualquier excepción y el fallo ocurre antes de enviar el archivo. No prueba problema de acceso.
2. Big Y, 11 ago (RESPUESTAS-NUEVAS-2026-08-11): el mismo attachments.aspx con system=ERMS abrió bien y la causa fue sesión vencida. Este caso usa system=LPMS.
3. RCS-28181, Gina Pilato, 25 sep: la excepción real queda en el log como Application_Error con estado y stack. Esa línea falta aquí.

QUE HAGO HOY
1. Pide a Kevin que haga clic en Technical Details de la pantalla de error y envíe captura. Su captura no lo tiene abierto. En RCS-27573 ese enlace dio el stack completo.
2. Abre la URL exacta de Kevin con tu sesión de soporte en bigy. Anota la hora UTC.
3. Busca en Grafana el Application_Error de esa hora con el texto attachments.aspx y copia la línea completa.
4. Abre un adjunto de un caso reciente de Big Y como control. Si abre, el fallo se limita a casos migrados.
5. Crea el ENG como en RCS-29245 y pega ahí la línea del paso 2.

PRECEDENTES
RCS-28181 y ENG-7181 cubren adjuntos grandes, otra causa. brain/memoria/reference_recreate_caseno_changelocation.md documenta que Matt ejecuta los arreglos de datos.

SIGUIENTE PASO
Matt Kamminga, en el comentario del ENG y no en Teams. El 8 oct Matt contestó en el ENG de RCS-28181 y pidió environment, client y URL. Pide: ¿existe el archivo en el storage con ese nombre? ¿qué excepción da? Incluye client 362, la URL y la hora.
Falta confirmar: que Enrique tenga acceso a Grafana. Slade Jordan lo usó en RCS-29268.
