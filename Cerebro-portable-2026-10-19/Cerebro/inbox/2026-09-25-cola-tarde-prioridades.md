Cola de Juan, 25 sep 2026, 14:52 Bogotá. Jira en vivo.
18 abiertos: 10 UCR, 5 WIP, 2 Support Review, 1 Delivery Review. Nuevo RCS-29123; RCS-29026 volvió a WIP.

Prioridad 1: RCS-29123 y RCS-29026, alertas ADUSA.
29123: solo acuse propio de las 14:03 Bogotá. Cliente reporta ausencia de alertas de Defrauded Customer y Shoplifting. Determinar generación contra entrega con casos concretos y logs actuales; confirmar responsable técnico y siguiente revisión. Talos es hipótesis, no diagnóstico confirmado.
29026: último comentario cliente 12:16 Bogotá, primer caso sin alerta alrededor de 16:20 del 24 sep, hora declarada por Leigh Ann. Debe respuesta. Leer hallazgo con Vedant: Success fijo en historial no confirma entrega; duplicación TO/CC sigue hipótesis; logs históricos insuficientes. Hay trabajo local sin comunicar en Jira. No mezclar el fallo de entrega del 20 sep con el corte nuevo de generación sin prueba común. El borrador respuesta-leighann-4 afirma escalación; verificar escalación efectiva antes de pegar esa afirmación.
Fuentes: RCS-29123 descripción y comentario 3364643; RCS-29026 comentario 3364480; inbox/2026-09-25-rcs-29026-hallazgo-codigo.md.

Prioridad 2: RCS-28256 Tailored Brands, High. Último público 18 sep, siete días. Nota interna de ayer recoge investigación de Matt sin causa. Pedir próximo hito/fecha y actualizar a Colton hoy.

Prioridad 3: RCS-28756 Nike. Ya respondiste a Ganesh. RTS-206999 comentario 3364610 de hoy 13:42 Bogotá: pipeline 20260925.2 corriendo en load_raw_ecom_blob.py; 8/28 llega a 15,701, 9/1 a 32,008. Falta respuesta sobre archivos pendientes, capacidad y fin de recuperación. Push interno con Peyman, no nuevo acuse vacío.

Prioridad 4: RCS-29104 GPC, High. Kristen escribió hoy 11:07 Bogotá que contactó al cliente sobre archivos sin tender. Seguimiento activo; coordinar con ella y Delivery sin duplicar pedido. No convertir su correo en confirmación de causa.

Antes del lunes: RCS-28881 NEXCOM, verificar invitación del 28 y sesión con Carlo. RCS-28667 ADUSA usuarios, poner fecha con especialista SSO. RCS-28294 Vallarta, pedir planificación a Matt/Shandana para ENG-9152; sin comentario nuevo desde 22 sep.

RCS-28871 Walgreens baja de urgencia. Respuesta pública 12:28 Bogotá de hoy, comentario 3364499, cierra cuestionario con migración a auto scaling. Queda compromiso explícito de confirmar migración terminada. No repetir solicitud de stress testing como deuda de respuesta intacta.

Esperando cliente, sin respuesta nueva: RCS-28281 Ahold reenvío; 28984 Skechers; 28223 McDonald’s; 28351 Blain’s; 28099 CWH; 27765 Winn-Dixie; 28212 7-Eleven; 28240 United; 29054 Big 5. Seguimientos de anoche ya publicados en seis de ellos. Blain’s tiene plazo comunicado 29 sep. No insistir otra vez hoy ni cerrar por mero silencio.

Orden práctico: alertas ADUSA y respuesta a Leigh Ann, update Tailored Brands, seguimiento recuperación Nike, confirmar sesión NEXCOM. Conservar seguimiento de GPC y compromisos de Vallarta/SSO/migración Walgreens.
Jira y sessions.db solo lectura. Fuentes de actividad: comentarios reales; sin inferir antigüedad por updated ni declarar SLA vencido.
