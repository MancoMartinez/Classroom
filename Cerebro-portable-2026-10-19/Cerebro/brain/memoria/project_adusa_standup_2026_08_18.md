---
name: project_adusa_standup_2026_08_18
description: Standup ADUSA del 18 ago 2026 con Chris Rippingale, la causa raíz completa de la migración de usuarios y los compromisos con fecha
metadata:
  type: project
---

Standup **solo de Incident/LPMS** para Ahold Delhaize, conducido por **Chris Rippingale** recorriendo el `Appriss ADUSA-Support-Tracker.xlsx` fila por fila. Secure tiene sus dos standups aparte, no los mezcles.

**El encuadre de Chris, y es el que manda:** todos los tickets de ADUSA son **P1**, porque el cliente está amenazando con dejar un contrato de **800 mil**. No se prioriza por severidad técnica aquí, se prioriza porque la cuenta está en riesgo.

**La posición oficial ante el cliente sobre latencia:** el problema viene del **sistema de reportes (Izenda)**, no de la plataforma. Secure y Engage corren bien, Incident no y es por el reporting. Chris lo va a comunicar así. Matt lo validó. Si te preguntan por lentitud, esa es la línea.

**Causa raíz de la migración de usuarios, explicada completa.** Explica RCS-28177, RCS-28342, RCS-28364 y RCS-28379 de una sola vez: la migración alineó registros **por dirección de correo**; en el intervalo hasta el corte algunos usuarios **entraron y el sistema les creó un incident user ID nuevo** que quedó por defecto en su perfil; al limpiar los IDs viejos el dato quedó apuntando a un user ID **que ya no es válido**. Chris preguntó explícitamente si era problema de Appriss y la respuesta fue **sí, un problema de timing dentro de la migración**, nuestro, no del cliente. Complementa [[reference_lpuser_lpuser2_membership]] con el *cuándo*, que ahí faltaba.

Quedaban **3 usuarios sin remapear**; Kiran no los halló en el restore y se comprometió a cerrarlos el 18 en la tarde. El resto "apples to apples".

**Bloqueos concretos que salieron:**
- **RCS-28123**: el fix está en producción pero verificarlo exige **aprobar un registro real en producción**. Se le pidió permiso a ADUSA.
- **RCS-28196**: el cambio de default de columna que hacía Gabor **no está en prod**, hay que aplicarlo a mano, y el asignado **no tiene permisos de ALTER**. Depende de John.
- **RCS-28124**: salen **dos despliegues** porque el release branch trae cosas extra; los cambios de Matt van detrás de flag y se pueden desplegar apagados.
- **RCS-28161**: probado en test, **no está en el release branch** todavía.

**Sin dueño y hay que asignarlos: RCS-28413 y RCS-28415.** El 28413 es grave por reputación: el reporte Interview by Source de Food Lion Central Division pasó de más de 270 casos a 66, y **los managers ya recibieron la versión de 66**.

**RCS-28021**: confirmado que el scheduler de Izenda sí corre, llegó el correo a las 8:12 a.m. Lo que sigue roto es que algunos CSV llegan sin datos. **RCS-28093** se reclasificó como feature request.

**Punto de proceso sin cerrar:** si el "Resolved" del tracker lo escribe el cliente o debe salir del estado de Jira. Hoy pueden contradecirse.

Detalle completo en el chunk 1568 de Moscú (folder 26) y el snapshot del tracker en el 1569. Ver [[project_adusa_ficha_y_tickets]].
