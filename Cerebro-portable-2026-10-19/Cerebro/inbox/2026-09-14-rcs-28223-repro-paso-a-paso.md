# RCS-28223, reproducir el defecto en la UI. Guion por bloques

Estado hoy: Under Engineering Review, assignee Matthew Kamminga. Hugo pide update el 14 sep.
Los pasos que estan en Jira desde el 27 ago se escribieron desde la base y las capturas de Hugo,
sin tocar la UI. Este guion los ejecuta de verdad.

Tenant mcdonalds, Client ID 402, AuditConfigID 4 Restaurant Cash Audit.

## Bloque 0. Entrar al tenant

1. Control Panel, usprod.apprissretailcloud.com/control, entorno USPROD.
2. Tabla Customers in USPROD, buscar McDonald's.
3. Click en el logo de la primera columna. Esa es la via de soporte.
   No uses /mcdonalds/signin, redirige al SSO del cliente.
   Alternativa non SAML: agregar ?admin=true al final de la URL de signin.

Se espera: sesion abierta dentro del tenant mcdonalds.
Si sale Session Error, es RCS-28486, no este ticket. Anotarlo y parar.

## Bloque 1. Llegar a una auditoria con grilla

1. Menu de Incident, modulo Audit.
2. Abrir Restaurant Cash Audit. No uses la 959-30133, es la de Hugo y esta In Progress.
   Crea una nueva o abre una de prueba propia.
3. Ir a la seccion Manager Week 1.
   Ruta: /mcdonalds/nettrack/Audit/screens/incident/402/audit/screens/AuditSection_V24_S4.aspx
4. Click en Expand All.

Se espera: las preguntas de la seccion visibles.

## Bloque 2. Manager Week 1, el defecto

1. Pregunta 2, AuditConfigQuestionID 57.
   "Are there any managers who are at +/- $2 threshold as per Cash Management Policy?"
2. Response a Yes. Renderiza la grilla de nueve columnas.
3. Click en la celda Coaching de la fila 1. Escribir una x.

Se espera segun diseno: la celda acepta el caracter.
Lo reportado: no acepta entrada en ninguna columna de la 2 a la 8.
Columna 1 Employee Name y columna 9 Comments si responden.

4. Probar las tres: 57, 60 y 61.
5. Control en la misma pantalla: IDs 116, 117, 118, 62 y 63. GridCols vacio, si aceptan texto.
6. Guardar la auditoria aunque las celdas queden vacias.

## Bloque 3. Crew Week 1

1. Seccion Crew Week 1.
   Ruta: /mcdonalds/nettrack/Audit/screens/incident/402/audit/screens/AuditSection_V24_S9.aspx
2. Expand All.
3. Pregunta 2, ID 64. "If so, identify the top two (2) crew members, dollar amount, and what
   action was taken." Esta no trae Response, la grilla sale directo.
4. Celda Coaching fila 1, escribir una x.
5. Repetir en 65, 66, 68 y 69.

## Bloque 4. Confirmar en la base lo que acabas de escribir

SELECT amq.AuditMasterQuestionID, amq.AuditConfigQuestionID, amq.LastEdited,
       LEFT(amq.Comments, 300) AS Fila
FROM   incident.AuditMasterQuestion amq
WHERE  amq.AuditConfigQuestionID IN (57,60,61,64,65,66,68,69)
  AND  amq.LastEdited >= CAST(GETDATE() AS date)
ORDER BY amq.LastEdited DESC;

Se espera si el defecto sigue vivo: la fila guarda nueve campos con las comas seguidas,
patron ",,,,,,,," entre la columna 1 y la 9.
Si aparece la x en el campo 2, el defecto ya no reproduce y eso tambien es un hallazgo.

## Bloque 5. Evidencia para Kamminga

- Captura de la grilla con la URL visible y el cursor en Coaching.
- Numero de la auditoria que usaste y la hora.
- El resultado del bloque 4 pegado como texto.
- Navegador y version.

## Precedentes

- Comentario del 27 ago en Jira, pasos originales: inbox/2026-08-27-rcs-28223-comentario-interno.md
- Evidencia de la base: inbox/2026-08-27-rcs-28223-EVIDENCIA.md
- Consultas completas: inbox/2026-08-27-rcs-28223-plan-repro.sql
- Acceso al tenant: brain/memoria/project_juan_accesos.md

## Compromisos

Nada prometido al cliente hasta que Engineering confirme. Hugo espera respuesta al comentario
del 14 sep. J.R. ya le contesto a Colleen que Engineering esta revisando.

## Bitacora de ejecucion, 14 sep 2026

- Bloque 0 OK. Entrada por Control Panel funciono. Juan llega a
  apps.apprissretail.com/mcdonalds/nettrack/SystemSelect.aspx sin Session Error.
  Pantalla System Selection con tres tarjetas: Admin Tools, Compliance Audit System,
  System Reports. Admin Tools reporta Client ID 114004, 2593 usuarios activos,
  795 ubicaciones activas. Compliance Audit System reporta Open Audits 0.
- Pendiente de aclarar: el Client ID de la tarjeta es 114004 y la ruta del defecto usa
  /incident/402/. Verificar cual aplica al entrar al modulo.
- Bloque 1 en curso. Compliance Audit System abrio en
  /mcdonalds/nettrack/Audit/Menu.aspx?System=CAMS. Audit Main Menu con cuatro tarjetas:
  Start New Audit, Active Audits (New Audits 0, Active Audits 0), Search, Manage Action Plan.
  No hay auditorias activas para el usuario de soporte. Toca usar Search para buscar
  4694-30612 o similar, o Start New Audit si Search no la encuentra.
- Bloque 1 cerrado. Search encontro 4694-30612 por Audit Number. Un resultado, Restaurant
  Cash Audit, 08/27/2026, Audit Completed Yes. Preview muestra 11 paginas, las diez secciones
  Manager/Crew Week 1 a 5 en 100% scored salvo Week 5 N/A, Overall non-scored.
  Click en Edit (lapiz) abrio el Audit Workbench en modo edicion.
  AuditMasterID 24, AuditMasterStoreID 30612, AuditConfigID 4, StoreIdent 888, SetEdit=1.
  Status Completed. Audit Section List con las diez secciones, todas con check verde.
  Entrando ahora a Manager Week 1 para el bloque 2.
- Bloque 2, intento de escritura. Juan reporta haber agregado "test" en el primer campo
  Employee Name y varias x en celdas de la grilla, sin dar Save todavia. Las capturas
  compartidas en el chat siguen mostrando Channelle/Sylvanaa sin "test" ni x visibles,
  identicas a las de antes del intento. Pendiente confirmar con Juan si el texto sigue
  en pantalla ahora mismo o desaparecio antes de esta captura.

## HALLAZGO MAYOR, 14 sep 2026. El defecto no reproduce hoy en esta pantalla

Prueba en vivo sobre la auditoria 4694-30612 (real, tienda 4694 Houston TX, Breck Road),
Manager Week 1, AuditConfigQuestionID 57, fila Channele.

Se escribio x, y, z, a, b, c, d en las siete columnas Coaching a Termination y se agrego
"(test)" al Comments. Se dio Save. Se recargo la pagina completa y se reabrio Manager Week 1.
Los siete valores y el comentario modificado seguian ahi, persistidos en el servidor.

Esto contradice el comentario del 27 ago 2026 en Jira, que dice: "no input is accepted in
any of columns 2 through 8" en las 82 preguntas grid de esta auditoria, para las diez
secciones Manager/Crew Week 1 a 5. Hoy, en Manager Week 1, en la misma auditoria y el mismo
tenant, la escritura entra y persiste.

Pendiente antes de concluir nada:
- Revertir la fila Channele a su estado original. Es un registro real de produccion.
- Probar Crew Week 1 y al menos otra semana (Manager Week 2 o 3) en una auditoria NUEVA,
  no en esta, para no seguir tocando el registro real de la tienda 4694.
- Si el defecto tampoco reproduce en otras secciones, la conclusion del 27 ago necesita
  revision. Posible fix silencioso entre el 27 ago y el 14 sep, o el comentario original
  tenia un confusor no identificado (auditoria completada vs en progreso, version de pantalla).

Marcar como HIPOTESIS hasta probar otra seccion. No escalar ni comentar en Jira todavia.

## Aclaracion de alcance y bloqueo de base, 14 sep 2026

Las dos secciones probadas son Manager Week 1 y Crew Week 1, esta ultima en las preguntas 2 y 4
mas el campo Section Comments. Ambas ya reproducen escritura y persistencia, ambas revertidas.
Estas dos son justo las dos pantallas que el comentario del 27 ago nombra explicitamente,
AuditSection_V24_S4 y AuditSection_V24_S9.

Query del paso 6 extendido devolvio 0 filas. Causa: la base seleccionada en el dropdown de SSMS
no es la del tenant. Nomenclatura correcta segun brain/memoria/reference_acceso_sql_tenants.md:
sqldb-prd-wus2-arp-production-NNN-xxx-platform, NNN el Client ID, xxx el codigo corto.
Client ID 402, Abbreviation MSX confirmado en Control Panel. Base esperada:
sqldb-prd-wus2-arp-production-402-msx-platform. Falta seleccionarla antes de repetir la consulta.

## Hallazgos SQL de hoy (2026-09-14, sesion completa)

Base correcta confirmada: sqldb-prd-wus2-arp-production-402-msx-platform (Client ID 402, McDonald's, abreviatura MSX). El nombre no sigue un patron obvio, se resuelve por brain/memoria/reference_acceso_sql_tenants.md, ClientID+abreviatura del Control Panel.

AuditMaster.DateCreated no sirve como filtro temporal para este caso. Para AuditMasterID 24, DateCreated = 2021 05 27. Ese campo refleja la creacion original del master de ciclo compartido, no la fecha de la auditoria de la tienda. Primer intento de query con filtro DateCreated >= 2026 08 01 devolvio 0 filas por esto, no por base equivocada.

AuditMasterID no es unico por tienda. Es compartido por toda la cadena de auditorias recurrentes de ese ciclo. Consultar AuditMasterQuestion solo por AuditMasterID = 24 devolvio 825760 filas, todas las tiendas del ciclo. El discriminador correcto por tienda es AuditMasterStoreID, visible en la URL del Workbench. Con AuditMasterID = 24 AND AuditMasterStoreID = 30612 (Houston) la query devuelve 82 filas, que coincide con el set completo de preguntas de una tienda (IDs 57 a 150).

LastEdited esta NULL en las 82 filas de esa tienda, no sirve para verificar cuando se guardo algo. La verificacion de que el revert de la pregunta 57 (fila Channele) quedo bien se hizo comparando el valor de Comments contra el estado esperado, no por fecha.

## Prueba manual en vivo, contradice el hallazgo de Aug 27

Se reprodujeron en vivo las dos pantallas exactas que cita el comentario de escalamiento del 27 de agosto: Manager Week 1 (AuditConfigQuestionID 57, 60, 61, pantalla AuditSection_V24_S4.aspx) y Crew Week 1 (AuditConfigQuestionID 64, 65, 66, 68, 69, pantalla AuditSection_V24_S9.aspx).

Resultado de hoy: el grid SI acepta texto en las 7 columnas del medio y SI persiste despues de guardar y recargar. Esto contradice directamente la linea del comentario de Aug 27 que dice "Actual: no input is accepted in any of columns 2 through 8".

Hipotesis de trabajo: el comentario de Aug 27 probablemente se redacto a partir de la evidencia de base de datos (columnas vacias), no de una prueba manual en vivo en ese momento. El mismo patron de columnas vacias en la base es compatible con dos explicaciones distintas: el defecto real, o simplemente que desde el 24 de agosto los usuarios adoptaron el workaround documentado de escribir todo en el campo Comments y dejaron de tocar las columnas del grid. Ambas dejan la misma huella en la base.

Variable sin cerrar: la prueba de hoy se hizo con cuenta de soporte/admin, no con una cuenta real de rol Manager. Si el rol Manager tiene permisos o renderizado distinto en el grid, el defecto podria seguir siendo real para los managers de Hugo especificamente. Ninguna query de SQL puede cerrar esta duda, hace falta que Hugo o un usuario real con rol Manager escriba en una celda del grid hoy mismo.

## Pendiente

Confirmar con Hugo Cortez (o un usuario real con rol Manager) si el grid acepta input en su cuenta. Recien con eso se puede escribir el comentario formal en Jira. No se ha posteado nada a Jira, solo se le informo a J.R. en chat que la prueba manual de hoy no reprodujo el error en las pantallas documentadas, dejando explicito que falta cerrar el rol Manager antes de dar el caso por resuelto.

## Nota adicional, Manage Audits (camslist.aspx)

Juan reviso la pantalla admin/camslist.aspx del tenant mcdonalds. Restaurant Cash Audit muestra Last Screen Build 7/29/2026 6:39 AM, que corrobora de forma independiente, via UI y no solo por SQL, el rebuild de pantallas del 29 de julio ya documentado en el comentario de Aug 27 (alli registrado como 05:39, la diferencia de una hora es probable zona horaria, no un segundo evento). No agrega informacion nueva, solo confirma el mismo hecho por otra via.

Se observo tambien Last Edited 1/9/2026 por Support, Appriss Retail sobre ese mismo audit config. Siete meses antes de que empezara el problema en agosto, no encaja en la linea de tiempo del defecto. Queda anotado, no se persigue como pista a menos que aparezca algo que lo conecte.
