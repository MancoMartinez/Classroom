# Cosecha 7 sep 2026. Roster, clasificador y sistema

Hallazgos verificados de sesiones de Cowork no cosechadas antes de hoy. Descarta hipótesis sin cerrar y borradores descartados.

## Roster incompleto en bin/asignar.py

Sesión "Cerebro asignacion diaria" verificó en vivo la carga de las 14 personas que aparecen en la captura de Teams del equipo Support Appriss. Dos no están en el roster de `brain/memoria/project_appriss_support_team.md` ni en el diccionario `EQUIPO` de `bin/asignar.py`.

Megha Rathi ya sostiene 7 tickets activos en RCS, incluidos RCS-28667 y RCS-28683 donde coordina reproducción para ingeniería. Enrique Jimenez no tiene ningún ticket abierto. Falta confirmar rol y país de los dos con `lookupJiraAccountId` antes de meterlos en la lógica de techo del reparto diario. Deducir el equipo de quién tiene tickets en Jira ya sacó cuatro personas ajenas al equipo el 3 de agosto, no repetir ese error a la inversa dejando a alguien real fuera.

Camila Cortes, marcada en el roster como no asignataria técnica, tiene dos tickets viejos a su nombre en Jira: RCS-28351 y RCS-28240.

## Clasificador de la cola bajó de exactitud

Sesión "Cerebro cola manana" del 5 sep midió el clasificador contra las etiquetas fijadas a mano y dio 93%, no 100%. RCS-27765 quedó mal clasificado en nivel 3 cuando debería estar en nivel 4. El léxico de `bin/cola.py` se desactualizó. Revisar antes de confiar en el orden de la cola tal cual sale.

## bin/guardar falló con disk I/O error

Sesión "Respuesta de cierre cliente" (RCS Home Depot, error SAML por throttling de Azure Key Vault) intentó guardar el hallazgo en `brain/sessions.db` y `bin/guardar` falló dos veces con `disk I/O error`. El informe quedó escrito en `inbox/` así que no se perdió, pero el hallazgo no entró a la base todavía. Confirma la sospecha ya documentada en `brain/memoria/project_moscu_sin_gpt.md` de que la carpeta montada en Cowork no soporta bien el locking de SQLite. Correr `bin/guardar` desde el Mac para que este hallazgo y cualquier otro de esta sesión entre a la base.

## Toggle de comentario interno mal puesto, RCS-28671

En RCS-28671, un comentario técnico interno de Andres Marciales con nombres de tabla y el mecanismo completo del diagnóstico quedó visible para la cliente Ericka Smith, que respondió citándolo por nombre ("Hi Andres"). El toggle de comentario interno de Jira Service Desk no quedó bien puesto en ese comentario y sigue sin revisarse. Antes de pegar cualquier internal note técnico en ese ticket, confirmar el toggle. Este riesgo aplica en general a cualquier ticket donde se redacte un internal note con detalle técnico.
