# Reunión cliente 18 ago — causa raíz confirmada en vivo (Izenda → 502s en Incident)

Transcrito en vivo por Moscú durante la reunión con el cliente (Jim). Pendiente de
guardar en Moscú carpeta 26 cuando la app se cierre (estaba abierta transcribiendo,
`guardar` la bloqueó).

**Confirmación clave de causa raíz, dicha por Appriss en la reunión, no inferida:** la
carga de reportes/Izenda dispara el conteo de threads y eso tiene efecto en cascada sobre
la app de Incident — los 502 que reportan los usuarios en RCS-28353/28356/28407 vienen de
ahí. Confirma en vivo la teoría que ya teníamos por ENG-5649/RCS-28058 sobre el patrón de
exportación Izenda en modo PC.

**Prioridad número uno de Appriss ahora:** separar Incident de Reporting/Izenda para que
el uso diario de Incident no dependa de lo que hagan las herramientas de reporte. Dicen
tener control de eso ya. Siguiente paso: trabajo de performance + esperan luz verde de QA
esta semana, después despliegan.

**Expectativa que ellos mismos pusieron:** separar los dos sistemas quita los 502 y
mejora el performance de Incident, pero no significa que Izenda/Reporting en sí quede
resuelto de una vez — son dos frentes distintos.

**Pregunta del cliente:** si el problema de reporting es across all customers.
**Respuesta de Appriss:** NO, es específico de la pieza Izenda dentro de "classic
incident", y para este cliente solo hay 3-4 usuarios que usan Izenda.

**Idea que salió en la reunión, aceptada como buena:** reprogramar los reportes
automáticos/programados de Izenda para correr en la ventana de menor carga (mencionaron
4am en vez de 10am) para evitar el choque de recursos con usuarios activos de Incident.
Aclaración hecha ahí mismo: eso evita el choque reporte-vs-Incident, pero no evita el
choque entre un reporte generándose y otro usuario tratando de ver reportes al mismo
tiempo.

También sugirieron probar la herramienta de reporting nativa de la plataforma (search
composer, escribir tu propia consulta y generar el reporte desde ahí) como alternativa a
Izenda mientras tanto.

Se ofreció identificar quién es el Solution Expert de Jim. Se mencionó un nombre que
sonó como "Dan Orkquist" — posible transcripción imprecisa de **Dean Korbakis**
(Constantine Korbakis), aunque él aparece **inactivo en Jira** desde hace tiempo (ver
RCS-27009). Vale la pena confirmar el nombre real antes de asumir que es él.

---

## Continuación de la transcripción (mismo llamado, revisión ticket por ticket)

**Cierre general esperado tras la llamada:** Chris/Matt esperan poder cerrar todo el bloque
de "User Issues, Migration Steps, Home Stores" salvo uno o dos temas de IDs de ubicación
no únicos entre niveles, que dicen tener bajo control.

**RCS-28177 (búsqueda con "1" en el correo), revisado en vivo:**
- Sin novedad nueva del ticket en sí, siguen esperando respuesta.
- Nota de Leigh Ann en el ticket: Jonathan Wright confirmó que ya ve sus casos viejos.
  **Pregunta abierta que quedó sin resolver en la llamada:** si el fix fue específico para
  él o universal para todos los afectados.
- Un nombre nuevo salió mencionado como con el mismo síntoma (sonó como "Christina
  Corgero/Colgero", transcripción imprecisa, confirmar nombre real) — **ella confirmó en
  vivo, momentos antes de la llamada, que ya puede buscar por nombre y crear un caso
  nuevo.** Dan por buena esa parte.

**RCS-28342 (Anthony Lopez, datos de empleado faltantes), causa aclarada por Appriss en
vivo:** cuando se manda la información de claim al SSO, se supone que actualiza el
archivo de usuario. El título de cargo viene como **claim de SSO desde Active
Directory**. Hay una lista de personas (Anthony Lopez fue uno, corregido a mano) a
quienes ese título no les está llegando al archivo de usuario del lado de LPMS. Esto
confirma que la causa NO es solo un caso aislado de un usuario, es un patrón de varios
perfiles con el mismo defecto de sincronización SSO → LPMS.

---

## Segunda tanda de la transcripción (repaso ticket por ticket, con Chris compartiendo pantalla)

**RCS-28093 (empleados no restringidos por tienda), causa aclarada en detalle:** la tabla
de empleados no trae la marca, solo el número de tienda, y los números de tienda **no son
únicos entre marcas** (la tienda "1" existe tanto en Food Lion como en Stop & Shop). El
dato de marca debería venir en un campo "miscellaneous 1", pero es intermitente: unos
registros lo traen, otros no. Appriss va a sacar un conteo de cuántos registros están sin
ese dato, lo tratan como problema de mapeo. Confirmado explícitamente como **prioridad
baja** frente a los demás.

**RCS-28123 (asignación de casos):** Appriss cree que ya desplegó el fix y pide **permiso
a Matt (ADUSA)** para abrir un caso real en producción, asignarlo a alguien y seguirlo de
principio a fin para validar — usando un número de tienda "de prueba" poco activo para no
afectar datos reales. Leigh Ann confirma que probablemente afecta a todas las marcas,
Hannaford incluido.

**RCS-28196 (defaults a "No"):** causa confirmada, ya la teníamos: migración de base
cambió una columna que antes admitía null y ahora no, por eso caía en 0/No. Ya está
arreglado y probado, Leigh Ann ya respondió confirmando. **Detalle nuevo que vale la pena
vigilar:** como el campo ahora es obligatorio, un null no lo satisface, así que el usuario
igual tiene que elegir Sí o No aunque nadie haya contestado esa pregunta — quedó sonando a
que esto podría no ser el comportamiento correcto, sin resolver del todo en la llamada.

**RCS-28304 (ancho del campo de tier):** confirmado "ready", pero se manda al final de la
lista de prioridad, es un nice-to-have.

**RCS-28124 (adjuntos no visibles):** el fix de hoy es sobre subir archivo, no sobre
verlo/descargarlo. Appriss probó varios tipos de archivo; encontraron que **los .txt no
funcionan** y le preguntaron a Leigh Ann si eso se usa del lado de ADUSA.

**Exportación de location file (contexto Izenda/exports):** confirmaron que el archivo de
ubicaciones se exporta pero llega en blanco, y ese archivo es el que usan para actualizar
en bloque vía FTP — conecta con los problemas de exportación de Izenda ya documentados.

**RCS-28413 (Izenda, datos incorrectos), aclarado en vivo:** es un **reporte programado
que se exporta y se distribuye automáticamente**, no algo que se corre manual dentro de
Izenda. Antes traía 268 registros, ahora solo 67 — la cifra exacta en vivo difiere un poco
de la que teníamos en el tracker (270→66), son la misma orden de magnitud, confirmar el
número real cuando llegue el conteo que Appriss prometió sacar.
