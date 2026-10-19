# RCS-27407 — Instructivo

Runbook para ejecutar el fix de código bajo ENG-8117 y cerrar RCS-27407. Cualquiera del equipo lo
puede seguir sin leer el informe completo.

Paso 1. Confirmar ownership y estado antes de tocar nada
Dónde se ejecuta: Jira, lectura.
Acción: abrir ENG-8117 y RCS-27407. Confirmar que el assignee de ambos sigue siendo Luis Hernandez
y que ENG-8117 sigue en Backlog.
Qué se espera ver: assignee confirmado en los dos tickets.
Si falla: si no hay assignee claro en ENG-8117, comentar pidiendo a Shandana Khan que confirme quién
lo ejecuta.

Paso 2. Confirmar repositorio y pipeline de netTrack legado
Dónde se ejecuta: Confluence o Teams, lectura.
Acción: preguntar a Engineering, Matthew Kamminga o Shandana Khan, cuál es el repositorio y el
pipeline de Azure DevOps para netTrack legado. La guía Making a Code Change documenta el flujo sobre
la plataforma Secure moderna, no sobre netTrack.
Qué se espera ver: nombre del repositorio y carpeta de pipeline confirmados por escrito.
Si falla: no continuar al paso 3 sin esta confirmación.

Paso 3. Escribir acceptance criteria en ENG-8117 antes de escribir código
Dónde se ejecuta: Jira, campo Acceptance Criteria. Escritura. Autoriza Luis Hernandez como assignee.
Bloque para pegar en el campo:

Given a SmartAlertConfig with an existing audit type filter
When the user opens Manage Smart Alerts, changes the audit type selection, and saves
Then the Filters and FiltersSQL columns on dbo.SmartAlertConfig update to reflect the new selection
And the updated filter correctly matches audits under any of the selected AuditConfig descriptions
And this includes names with different word order, for example Structured Store Visit Report,
Structured Store Visit Report (US/PR), and Store Structure Visit Report (Canada)

Qué se espera ver: campo poblado, disponible para que QA empiece a generar test plans.

Paso 4. Actualizar main y crear el branch de trabajo
Dónde se ejecuta: terminal, git. Escritura. Autoriza Luis Hernandez.
Comando, usando el repositorio confirmado en el paso 2:

git checkout main
git pull origin main
git checkout -b lhernandez/eng-8117/manage-smart-alerts-filterssql

Qué se espera ver: branch creado y disponible en origin tras el push.
Si falla: resolver conflictos contra main antes de seguir.

Paso 5. Cambiar ENG-8117 a In Development
Dónde se ejecuta: Jira. Escritura. Autoriza Luis Hernandez.
Acción: transicionar el estado al empezar a codear.
Qué se espera ver: estado actualizado, visible para Shandana Khan y Matthew Kamminga.

Paso 6. Replicar el bug en local antes de tocar código
Dónde se ejecuta: ambiente local, lectura y diagnóstico.
Acción: levantar la app, abrir Manage Smart Alerts para un SmartAlertConfig de prueba, quitar y
volver a agregar tipos de auditoría, guardar, y confirmar en la base local que FiltersSQL no cambió.
Qué se espera ver: la misma reproducción que documentó Tyrone Whitney el 2026-07-02.
Si falla: si no reproduce en local, detener y comentar en el ticket antes de escribir ningún cambio.

Paso 7. Implementar el fix
Dónde se ejecuta: código, ManageSmartAlerts.aspx. Escritura. Autoriza Luis Hernandez.
Acción: corregir el método de guardado del filtro para que compare por AuditConfigID en vez de
comparar el texto exacto contra la descripción del tipo de auditoría, y para que regenere Filters y
FiltersSQL cada vez que la selección cambia.
Qué se espera ver: al guardar en local con los tres tipos seleccionados, FiltersSQL refleja los
tres AuditConfigID con una condición OR.
Si falla: revisar si el método está cacheando el valor original del filtro en vez de recalcularlo.

Paso 8. Unit tests
Dónde se ejecuta: código. Escritura. Autoriza Luis Hernandez.
Acción: escribir tests para el método de guardado del filtro, arrange-act-assert, cubriendo el caso
de agregar un tipo nuevo y el caso de quitar uno existente.
Qué se espera ver: tests en verde, cobertura no baja respecto a main.

Paso 9. Checklist de desarrollador y PR
Dónde se ejecuta: Azure DevOps. Escritura. Autoriza Luis Hernandez.
Acción: abrir el PR con título obligatorio ENG-8117 al inicio, completar el checklist de
conformidad, dejar constancia del defence tester.
Qué se espera ver: gates automáticos en verde, Codeant, unit tests, code coverage, lint.
Si falla: corregir los comentarios de Codeant o los tests fallidos antes de pedir review.

Paso 10. Deploy a dev y verificación de solo lectura
Dónde se ejecuta: SQL sobre el ambiente de dev, solo lectura.
Bloque:

SELECT SmartAlertConfigID, SmartAlertName, Filters, FiltersSQL
FROM dbo.SmartAlertConfig
WHERE SmartAlertConfigID BETWEEN 33 AND 40

Qué se espera ver: tras re-guardar la config de prueba en dev con los tres tipos, FiltersSQL cambia
para reflejar la condición OR.
Si falla: revisar si el deploy incluyó el artifact con el fix, o si el ambiente de dev fue pisado por
otro branch.

Paso 11. QA y release
Dónde se ejecuta: Jira, seguimiento. Lectura.
Acción: mover ENG-8117 a Ready for Test al completar el PR, seguir el ciclo hasta Tested, esperar la
ventana de release quincenal siguiente.
Qué se espera ver: ENG-8117 en Tested y el release desplegado a producción.

Paso 12. Re-guardar la configuración de las ocho alertas SSVR en producción
Dónde se ejecuta: Manage Smart Alerts, producción. Escritura vía aplicación, no SQL directo.
Autoriza Luis Hernandez, solo después de confirmar que el fix está en producción.
Acción: para cada SmartAlertConfigID del 33 al 40, abrir el filtro y seleccionar los tres tipos de
auditoría, Structured Store Visit Report, Structured Store Visit Report (US/PR), y Store Structure
Visit Report (Canada), y guardar.
Qué se espera ver: confirmación visual del guardado para los ocho configs.

Paso 13. Verificar el resultado en producción, solo lectura
Dónde se ejecuta: SQL sobre producción, solo lectura.
Bloque:

SELECT SmartAlertConfigID, SmartAlertName, Filters, FiltersSQL
FROM dbo.SmartAlertConfig
WHERE SmartAlertConfigID BETWEEN 33 AND 40

Qué se espera ver: FiltersSQL con la condición OR para los tres tipos en los ocho configs.
Si falla: el fix no llegó completo a producción, no comunicar nada al cliente y reabrir la
investigación con Engineering.

Paso 14. Verificar el flag Active
Dónde se ejecuta: SQL sobre producción, solo lectura.
Bloque:

SELECT sac.SmartAlertConfigID, sac.SmartAlertName, ac.Active
FROM dbo.SmartAlertConfig sac
INNER JOIN dbo.AlertConfig ac ON ac.AlertConfigID = sac.AlertConfigID
WHERE sac.SmartAlertConfigID BETWEEN 33 AND 40

Qué se espera ver: Active en NULL para los ocho, que es el valor de activo según el criterio
documentado por Tyrone Whitney.
Si falla: si algún registro quedó en 0 por los intentos de junio, corregirlo desde la pantalla de
administración del alert, nunca con un UPDATE directo.

Paso 15. Confirmar el primer disparo real
Dónde se ejecuta: SQL sobre producción, solo lectura.
Bloque:

SELECT sap.SmartAlertProcessID, sac.SmartAlertName, sap.RunDate, sap.RunStatus, sap.EmailAddresses
FROM dbo.SmartAlertProcess sap
INNER JOIN dbo.SmartAlertConfig sac ON sac.SmartAlertConfigID = sap.SmartAlertConfigID
WHERE sac.SmartAlertConfigID BETWEEN 33 AND 40
ORDER BY sap.RunDate DESC

Qué se espera ver: al menos un RunDate posterior al re-guardado del paso 12.
Si falla: esperar al siguiente ciclo de proceso de alertas y repetir la consulta antes de escalar.

Paso 16. Comunicar a la clienta
No es un paso técnico. Recién después de confirmar el paso 15, redactar el mensaje a Annie Brown con
la skill cerebro-respuesta-cliente. No comunicar antes, la regla de Shandana sobre RCS-28161 aplica
en espíritu aunque el ticket ya esté en Under Support Review.

Transición sugerida

ENG-8117 pasa de Backlog a In Development al ejecutar el paso 5, y avanza por el ciclo estándar
hasta Tested y Done. RCS-27407 permanece en Under Support Review hasta confirmar el paso 15, y
recién ahí se mueve según el workflow estándar de cierre con el cliente.

Comentario para pegar en ENG-8117

Support will own this fix per Shandana Khan confirmation on 2026-09-01. Root cause is documented in
RCS-27407. ManageSmartAlerts.aspx does not regenerate Filters and FiltersSQL on dbo.SmartAlertConfig
when audit type selections are changed and saved. This affects the eight SSVR SmartAlertConfig rows,
IDs 33 through 40, which only match the original audit type name and never fire for Structured Store
Visit Report US/PR or the Canada variant. Plan is to update the save logic to match by AuditConfigID
instead of exact string comparison, add unit tests, and verify FiltersSQL regenerates correctly in
dev before release. Acceptance criteria added to this ticket. Confirming repository and pipeline for
netTrack legacy before starting branch work.
