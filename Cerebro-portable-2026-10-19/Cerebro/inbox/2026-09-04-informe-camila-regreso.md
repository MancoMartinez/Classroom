# Informe para Camila — regreso al equipo (18 ago a 4 sep 2026)

Preparado por Juan Martínez. Fuentes: Cerebro (inbox, bitácora, memoria, cola), Jira en vivo y Confluence. Estados de tickets verificados en Jira al 4 de septiembre.

## 1. ADUSA (Ahold Delhaize): la escalación central del periodo

El 14 de agosto Tom Blackburn, VP de IT del cliente, exigió el rollback completo de la migración a Incident/LPMS. Amenazó revisar el contrato de 800.000 USD. Durante esa misma llamada, Leigh Ann Stubbs recibió dos errores 502 en vivo.

El equipo confirmó la causa raíz el 18 de agosto. Los reportes de Izenda disparaban un conteo de threads que arrastraba a Incident al error 502. El tráfico afectado era menos del 0.5% del total. Appriss separó Incident de reportes y definió dos trackers para el cliente, uno de 10 columnas visible para Jim Cosseboom y otro interno de 14 a 15 columnas con causa e ingeniero asignado, que nunca sale del equipo.

Chris Rippingale, Matt Kamminga y J.R. Teagle sostuvieron la escalación con reuniones diarias hasta el 1 de septiembre, día en que J.R. propuso pasar a cadencia asíncrona. El 3 de septiembre el tracker registraba 49 tickets, 38 resueltos y 10 activos. Diego Buelvas y Edwin Garzón recibieron traspaso de tickets el 24 de agosto para sostener el volumen.

Estado verificado hoy en Jira:

- RCS-28535 (adjuntos, Hannaford): Under Customer Review, actualizado hoy. Jim lo describe como el único ticket que le genera preocupación real. El fix asociado, ENG-7181, está In Development.
- RCS-28693 (usuario sin aprovisionamiento que igual autentica): Under Customer Review, asignado a Vlad Bogus. Es un hallazgo de seguridad genuino, un usuario sin acceso formal en LPMS recibió rol Store Reporter por defecto.
- RCS-28482 (campos grises en Izenda): Under Support Review, prioridad Low. J.R. pidió escalar aceptando una reproducción débil. El comentario para transicionarlo está redactado y no se ha pegado en Jira.
- RCS-28123 (asignación de casos): Completed. Se cerró como comportamiento esperado, código retirado hace tres años y medio.
- RCS-28093 (empleados sin restricción por tienda): Accepted into Development. La causa raíz apunta a la columna MISC1 del feed VisualCron de Delhaize, que reporta éxito aunque el archivo no llegue.
- RCS-28342 (datos de empleado faltantes, ticket nuevo): Work in progress, sin primera respuesta de Appriss durante 8 días según el registro de cola.

De esta escalación salieron dos guías nuevas para el equipo: `flujos/tracker-interno-vs-tracker-cliente.md`, sobre cómo mantener separados los dos trackers, y `flujos/estado-escalated.md`, sobre la diferencia entre el estado Escalated y la etiqueta homónima.

## 2. Otros incidentes mayores con clientes, estado verificado en Jira

- RCS-28671 (The Home Depot, búsquedas rotas por la migración SnowTime): Work in progress, prioridad High. Simon Smith reparó 278 definiciones de búsqueda. El cliente reabrió el ticket 61 minutos después del cierre por un síntoma nuevo, trabajos sin transacciones asociadas. Manisha Naik investiga la segunda fase.
- RCS-28638 (Myer Australia, campos vacíos tras el cutover a SnowTime): Work in progress, prioridad High, asignado a Sebastián Garcés. El fix ya se desplegó el 2 de septiembre, pendiente de confirmación del cliente.
- RCS-28618 (Walmart, Refund Audit sin datos): Work in progress, asignado a Zackary Graas del equipo de datos. La tabla inkiru_rva no recibe datos desde marzo de 2025. El reporte lleva roto 16 meses, no tiene relación con SnowTime.
- RCS-28556 (Vitamin Shoppe, bloqueo intermitente de login): Work in progress, prioridad Medium, última actualización en Jira el 28 de agosto. El cliente confirmó el 3 de septiembre que el bloqueo es de Appriss, mismo mecanismo de Zscaler Toronto que ya se resolvió antes para Ahold. El comentario para escalarlo a Matthew Kamminga está redactado y tampoco se ha pegado.
- RCS-27941 (Tailored Brands, 40 días abierto): Work in progress. Causa raíz confirmada el 1 de septiembre, los Case Types del cliente no habilitan seguridad para ciertos roles. Colton Neal, del lado del cliente, va a responder la semana próxima.
- RCS-28223 (McDonald's, grillas de auditoría sin guardar desde marzo 2024): Under Engineering Review desde el 28 de agosto, sin movimiento desde entonces.
- RCS-28212 (7-Eleven, reporte APIS legado): Under Engineering Review desde el 18 de agosto, 17 días sin avance.
- RCS-28153 (Big Y Foods, timeout de sesión): Under Customer Review, prioridad High, última actualización el 25 de agosto. El fix salió en producción el 27 de agosto, PR 56323, ENG-7184 Resolved. El comentario que informa al cliente nunca se pegó en Jira. El cliente lleva más de una semana sin noticias sobre un problema ya resuelto.
- RCS-27959 (PACSUN): Under Customer Review desde el 26 de agosto. Cola ya emitió aviso de cierre automático por inactividad.
- RCS-27676 (Ralph Lauren, cambio de SFTP): Under Customer Review desde el 4 de agosto. Es el ticket con más silencio acumulado de toda la cola.
- RCS-27991 (Engage Analytics): se cerró como duplicado el 27 de agosto.
- RCS-28032 (Vitamin Shoppe, accesos): Closed, cliente confirmó la solución el 25 de agosto.
- RCS-28621: Closed. Sebastián Garcés importó un archivo de empleados al tenant de staging por error, trabajando desde una carpeta local no sincronizada. Ya se corrigió.

## 3. Volumen y salud de la cola

El total de tickets abiertos de Juan se movió entre 16 y 19 a lo largo de las tres semanas, 19 al cierre de hoy. La cola clasifica cada ticket en cuatro niveles de urgencia desde el 1 de septiembre. Hoy marca 3 en nivel "toca responder", 0 en "promesa incumplida", 7 en "esperando al cliente" y 9 en movimiento interno.

Tres patrones se repiten en los tickets más viejos. RCS-28153 tiene el fix liberado desde hace diez días y el comentario para el cliente sigue sin pegarse. RCS-28556 tiene la escalación redactada y tampoco se pegó. RCS-27676 lleva un mes sin respuesta del cliente. Los tres casos comparten la misma causa, un borrador queda listo y nadie lo lleva a Jira.

## 4. Cambios de personal

David Vargas, Full Stack Engineer contractor, salió del equipo. El registro más reciente de su trabajo es del 24 de agosto en RCS-28223. Sus tickets huérfanos se redistribuyeron entre varios analistas, incluido Juan.

Kiran Vadday, de ingeniería en India con rotación de ocho semanas, hizo una sesión de transferencia de conocimiento con Juan el 28 de agosto. Revisaron 18 tickets del cluster de permisos e identidad y Kiran recomendó devolver de entrada los tickets incompletos, pidiendo URL, log expandido, captura de pantalla y Ray ID de Cloudflare antes de aceptarlos.

Sebastián Garcés tiene una discrepancia de roster abierta desde el 31 de agosto. El roster oficial de Teams del 3 de agosto no lo incluye. El asignador automático sí lo incluye, con un techo de 5 tickets. Hoy tiene 6 tickets abiertos, por encima de ese techo.

## 5. Documentación nueva en Confluence

Aimee Wadsworth publicó el 2 de septiembre dos páginas de referencia para el equipo: "RCS Ticket Workflow Inception → Closure" y "RTS Ticket Workflow Inception → Closure", con el modelo completo de estados y quién es dueño de cada transición.

Viraj Kansara cerró el 2 de septiembre la retrospectiva del incidente RET20260817, la caída de SSO multi-cliente de Secure del 17 y 18 de agosto por la instancia administrada de SQL y el límite de tasa de Key Vault.

Diego Buelvas y Vedant Shirude empezaron a publicar fichas de triage en Confluence para tickets de RTS, con formato fijo de cliente, prioridad, estado y analista. Es una práctica nueva que no existía antes del periodo.

## 6. Herramientas internas de Cerebro

La key de Azure que alimentaba el chat y los embeddings de Moscú murió el 18 de agosto. Moscú quedó reducido a almacén y buscador. Claude Code pasó a ser el motor de razonamiento sobre esa base.

El 24 de agosto se encontró el índice de búsqueda corrupto, 25 de 28 consultas fallaban. La causa fueron triggers de borrado mal escritos. Ya se reconstruyó y quedó en 0 fallos sobre 28 pruebas.

El clasificador automático de la cola bajó a 54% de exactitud el 2 de septiembre porque las etiquetas de referencia quedaron desactualizadas. Se corrigió el 3 de septiembre y llegó a 100%. Volvió a fallar un caso la mañana de hoy, RCS-28753 de Nike, porque el léxico no reconoce el triage automático de un ingeniero como respuesta de Appriss. El ajuste sigue pendiente.

## 7. Puntos que necesitan tu decisión

RCS-28535 sigue sin cierre después de casi dos semanas y es el ticket que más le preocupa a Jim en ADUSA. Tres comentarios ya redactados nunca se pegaron en Jira: la escalación de RCS-28556, la notificación de fix de RCS-28153 y la transición de RCS-28482. Sebastián Garcés está sobre su techo de asignación mientras su lugar en el roster oficial sigue sin resolverse. RCS-27676 y RCS-27959 llevan más de tres semanas sin respuesta del cliente y están cerca del cierre automático por inactividad.
