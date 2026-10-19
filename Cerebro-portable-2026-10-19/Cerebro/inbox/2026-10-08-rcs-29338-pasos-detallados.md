# RCS-29338 Pasos detallados (8 oct 2026)

Entornos. Producción: https://apps.lpguys.net/spartannash/nettrack/?NoSaml=1 . Test: https://test.lpguys.net/spartannash/nettrack/?nosaml=1 . Lista de audits: apps.lpguys.net/spartannash/nettrack/Admin/CamsList.aspx

## 1. Lista de plantillas afectadas
Corinne ya dijo cómo actualizó (importación y cambio de versión) y que trabaja en Producción. Falta la lista. Nombró Limited, Fresh Encounter, Piggly Wiggly Test y Metcalfe's Self. Fresh Encounter aparece como importada y como solo versión, así que hay que aclararlo.
Pega a Enrique por Teams:

Hi Enrique, Corinne answered about the import and the version update. Could you ask her for the full list of affected templates, with the exact name and version as shown in Audit Manager? In her last comment Fresh Encounter appears under both the imported and the version-only group, so it would help to confirm which one it is. Also, are the templates that print fine from this fiscal year too?

Esperas una lista con nombre y versión. Plan B si ella no la da: corre la consulta B del paso 3 sin filtro de nombre.

## 2. Verificar Display Reference en Audit Manager
1. Entra por CamsList.aspx y abre la plantilla. Usa test si la copia existe allí. RCS-26171 reprodujo en test con IA - LIMITED Supermarket Store Audit v22. Si no existe en test, abre la de Producción solo para leer y no guardes nada.
2. Ve a la pestaña Sections/Questions y abre una pregunta que tenga texto de referencia.
3. Lee el campo Display Reference. Yes coincide con RCS-19415 y RCS-26171. No tumba la hipótesis. En ese caso revisa, en Admin > Manage Audits > selecciona el audit > Edit Base > sección Audit Report and Action Plan Report, si usa Standard o Custom y qué documento Word usa (Confluence RCS 475250491451). Los documentos viven en Admin > Custom Audit Templates. RCS-26171 sospechó de Audit Report SCORED - 2026.1.docx antes de llegar a Display Reference. La ubicación exacta del tick Include Help Text no está confirmada, viene del triage de Talos y de RCS-17225.
4. Repite en una plantilla que Corinne diga que imprime bien. Si ahí está en No, queda probado que el valor difiere entre plantillas.
5. Imprime el formulario en blanco desde el Audit Workbench con Print Audit. Prueba con y sin Include Help Text. Que ambos deban estar activos viene del triage de Talos (IA). Ningún humano lo verificó.
6. Guarda captura de la pregunta y del PDF. La escalación las exige.
Si la plantilla está publicada, editar puede exigir una versión nueva. Ningún precedente lo documenta. No guardes cambios en Producción sin acuerdo de Corinne.

## 3. Medir el alcance con SELECT
Solo SELECT, nunca UPDATE. Carlos corrió esta consulta contra test en RCS-26171. Yo no sé qué lectura tienes sobre la base de Producción de SpartanNash. Sin acceso, pásala a Enrique o a Carlos, o salta al paso 4.

Consulta A, del precedente (reemplaza el texto entre %):
SELECT q.QuestionText, q.RefText, q.DisplayRef, s.* FROM AuditConfig c JOIN AuditMaster m ON m.AuditConfigID = c.AuditConfigID JOIN AuditConfigSection s ON s.AuditConfigID = c.AuditConfigID JOIN AuditConfigQuestion q ON q.AuditConfigSectionID = s.AuditConfigSectionID WHERE c.Description LIKE '%NOMBRE DE LA PLANTILLA%' AND s.DeleteFlag = 0 AND q.DisplayRef = 1

Consulta B, conteo por plantilla. Adaptación mía con las mismas columnas, sin probar:
SELECT c.AuditConfigID, c.Description, COUNT(*) AS preguntas_con_referencia_visible FROM AuditConfig c JOIN AuditConfigSection s ON s.AuditConfigID = c.AuditConfigID JOIN AuditConfigQuestion q ON q.AuditConfigSectionID = s.AuditConfigSectionID WHERE s.DeleteFlag = 0 AND q.DisplayRef = 1 AND q.RefText IS NOT NULL AND q.RefText <> '' GROUP BY c.AuditConfigID, c.Description ORDER BY c.AuditConfigID DESC

Lectura. Las plantillas afectadas con muchas filas y las que imprimen bien con cero filas confirman la causa a nivel de dato. Si ambos grupos dan lo mismo, la hipótesis cae y vuelves al punto 3 del paso 2.

## 4. Preguntar a Carlos Jacinto
Su comentario del 3 abr 2026 en RCS-26171 dice "i change ALL audit questions config to show no reference text" y enlaza test. El 6 abr dice que revisó todas las preguntas y modificó la configuración. Ninguno dice cómo, quién ni en qué entorno. Sin ese dato no sabes quién puede hacer el cambio masivo en Producción. No sé si Carlos sigue activo.
Pega por Teams:

Hi Carlos, I am looking at RCS-29338, SpartanNash, where reference text prints again on the new fiscal year audits. In RCS-26171 you set Display Reference to No on all the questions of IA - LIMITED Supermarket Store Audit v22. Do you remember how you applied that change? For example question by question in Audit Manager, a script, or through Engineering, and was it in Production or only in test? If I am misreading the comments, please correct me.

Si no responde, pregunta a Scott Buric, que trabajó RCS-26171 desde Engineering, o a Shandana Khan.

## 5. Escalar a Engineering
Escala solo con la causa confirmada en el paso 2 o 3. El defecto sería que la importación o el cambio de versión deja Display Reference en Yes. Eso es código, va a Engineering.
1. Cambia el ticket a Under Engineering Review y asigna a Shandana Khan. El ENG se crea solo con la transición. La transición la ejecutas tú.
2. Antes de la transición deja en el ticket, según el documento de Aimee: el entorno (Production, ya lo dijo Corinne), pasos de reproducción con capturas, las notas de IA que usaste (el triage de Talos) y cualquier conversación fuera del ticket (la de Carlos). Avisa a Corinne de que el ticket se mueve.
3. Agrupa la petición. Cita RCS-19415 (arreglo de código en el release del 26 mar 2025), RCS-26171, RCS-27315, RCS-27794 y RCS-29338. RCS-27794 se cerró cuando la cliente dijo "not printing anymore", sin causa documentada. RCS-18394 y ENG-893 tienen un título casi igual y no los leí, léelos antes de citarlos.
4. Pide dos cosas: Display Reference en No por defecto al importar y al crear versión, y una forma soportada de corregir en masa.
5. Con el ENG creado, espera la transición a Under Support Review antes de comentar al cliente un arreglo de ingeniería.
6. Para redactar la nota interna usa cerebro-comentario.
Mientras llega el fix, tú decides si das a Corinne el paso a paso por pregunta. RCS-26171 se lo dio a John Franklin. Con muchas preguntas es lento.

## Compromisos
Ninguno con el cliente. No prometas fecha.
