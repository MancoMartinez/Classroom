---
name: reference_unificacion_patrones
description: "Causas raíz recurrentes de la Unificación de julio 2026, explicadas por Kiran Vadday, que deben guiar el diagnóstico antes de investigar desde cero"
metadata: 
  node_type: memory
  type: reference
  originSessionId: f1250f28-e367-4743-9ca8-90b661b376fc
  modified: 2026-08-13T18:20:37.844Z
---

Patrones confirmados de la ola de migración del 27 y 28 jul 2026 (21 clientes). Antes de investigar un ticket nuevo de esos clientes, contrastar contra esto primero.

**El cambio de fondo es que el email pasó a ser el username.** Textual de Kiran: *"in secure, your platform unification, we are not allowing any such kind. You have to create a new e-mail address, not just login, because there is nothing called a new login. Any new login is a new e-mail address."*

De ahí salen dos familias enteras de fallas:

**Cuentas duplicadas con sufijo 1, 2, 3.** El sistema legacy permitía varios LoginID por persona bajo un mismo email compartido, para distintos roles. La migración los desambiguó agregando el sufijo. Kiran sobre por qué existían: *"you are trying to log in yourself multiple different ways only because you are setting yourself up for different security levels"*. La cuenta buena es siempre la del email limpio, sin número.

**Usuarios que no vincularon su email antes del corte no se migraron o no pueden autenticarse.** Y Forgot Password no los rescata porque el correo va a una dirección que no es la suya. Corregir el email primero, después resetear. Casos: Stater Bros (RCS-28071, RCS-28078), Mattress Firm (RCS-28057, 14 de 206 usuarios en la base), Caribou (RCS-28091, ninguno), Vallarta, Sportsman's.

**El plan acordado para los duplicados era deshabilitar, no borrar.** Kiran en la llamada: *"anything with ones, twos, and threes, I think can be set to Disabled equals to one. I can write up a script"*, guardando el script para reusarlo con otros clientes. Ella misma marcó el riesgo: si el email real de alguien termina en 1 y no tiene gemelo sin número, no es duplicado. Lo que se ejecutó después en RCS-28135 fue un DELETE de 376 filas en `membership.Users` con `Inactive = 1` solo en `incident.LPUser2`, y al cliente se le prometió reactivación individual como excepción. Esa diferencia sigue sin cerrarse con Kiran.

**Administradores que perdieron sus permission groups en el corte.** Confirmado en Ahold con Leanne Stepps y April Valerie. Kiran no supo explicarlo: *"Absolutely no clue. They should all have."* Se resuelve a mano agregando `Administrators` más los tres grupos base. Si un cliente reporta pérdida de accesos de admin después de migrar, es este patrón y no hace falta escalarlo.

**Búsquedas que devuelven muchos empleados por tienda no son un bug.** Verificado en vivo con Food Lion, tienda 0001: la pantalla trae todos los registros de esa ubicación y eso es lo correcto. Kiran: *"it's bringing all the records belonging to 001 location, which is right."* La queja real de RCS-28093 era ver empleados de otra marca, que es distinto, y quedó sin reproducir.

**El timeout de sesión no es un bug, es una decisión.** NetTrack usaba 300 minutos, Secure usa 30, y al unificar se adoptó el estándar de Secure. Kiran: *"you won't dictate rules to them, right? You will keep your mods, you will adapt to them"*. Las opciones que él mismo planteó son subir el tiempo para NetTrack o mantenerlo separado. Ojo que en RCS-28153 Engineering dio otras cifras, 60 por defecto con máximo 240, así que confirmar el valor real por tenant antes de responderle a un cliente.

**No perseguir el síntoma antes que la causa.** Kiran sobre el fallo de export de Izenda: *"I don't want to talk about exporting Excel before talking about timeout issues... I think it's a wasted effort if we start looking at the exports even before Izenda issue is resolved"*. Si el export depende de algo roto aguas arriba, se arregla solo. Dejarlo como nota interna salvo que el cliente lo presione.

**Pedir ejemplos concretos antes de investigar.** Kiran, ante el reporte de empleados visibles entre marcas: *"we need screenshots and exact details"*, y descartó el reporte porque la tabla de empleados no se tocó en la migración. Sin caso, usuario y pantalla específicos, no arrancar.

**No importar una causa raíz de una reunión a un ticket que no la evidencia.** Error propio cometido el 4 ago 2026 y detectado el 5: al RCS-28075 (Ahold) se le puso el label `Uni_Jul_26_SessionExpiry` atribuyéndole el cambio de 300 a 30 minutos de sesión que explicó Kiran, pero ese cambio no aparece en ningún comentario del ticket. La evidencia real era un Cloudflare 524, que es timeout de request con el origen sin responder, no expiración de sesión (esa da redirect al login). El label correcto era `Uni_Jul_26_Timeouts`. Las reglas de esta página sirven para **contrastar** hipótesis, no para reemplazar la lectura del ticket.

**Distinguir siempre timeout de request de expiración de sesión.** 524 de Cloudflare, host en error, origen sin responder = request timeout. Deslogueo a mitad del trabajo con redirect al login = session expiry. Son mecanismos distintos con arreglos distintos y se reportan igual desde el lado del cliente ("se cae y tengo que volver a entrar").

**Antes de investigar un timeout, buscar si ya se cerró el mismo en otro tenant.** El RCS-28075 apuntaba a `NewIncident.aspx` (timeout al crear incidente), que es la misma operación del RCS-28084 de Vitamin Shoppe, ya cerrado con *"Unification platforms hotfix created and published"*. Mismo dueño en los dos tickets y la conexión no se había hecho. Con tenants compartiendo servidor, un hotfix ya publicado puede ser la respuesta.

**Verificar quién subió cada adjunto antes de tratarlo como evidencia.** En el RCS-28075 una de las capturas la había subido el propio ingeniero de soporte como intento de reproducción, no el cliente. Leerla como síntoma llevaba a una conclusión falsa.

**La causa raíz del bucket de login es la migración en dos pasos.** El paso uno le pide al usuario vincular un email y crea la fila en `membership.Users` con la contraseña AES-256 desencriptada de lpguys. El paso dos, el job de Hatter, sincroniza al resto desde `incident.LPUser2` pero les asigna una contraseña por defecto, y por eso a esos usuarios el reset de contraseña les resuelve el problema (firma reconocible). **Sin email en lpguys no se creó cuenta ninguna.**

**Usuario bloqueado: remediación aprobada** (página de bucket review, 13 ago 2026): `UPDATE membership.Users SET Locked = 0 WHERE UserID = X` más **purgar** la caché del cliente, no borrarla. Queda pendiente que Ripp defina si se permite desbloquear desde la UI.

**Adjuntos: el tope real era 4 MB de subida a blob**, y no tenía relación con archivos bloqueados por tipo. Liberado a producción el 13 ago 2026. Las smart alerts fallaban por la misma causa aguas arriba: adjunto o documento de impresión ausente en el blob.

El análisis completo por categoría vive en la página de Confluence "Platform Unification Jul 26 - Issue Review by Bucket" (espacio RTS) y los 61 tickets están etiquetados en Jira con labels `Uni_Jul_26_*`.

Ver [[reference_control_panel_admin]], [[reference_esquema_usuarios_incident]] y [[reference_screen_designer_rebuild]].
