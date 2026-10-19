# ADUSA: recuperación, recurrencia y trazabilidad de Screen Designer

Investigación para Juan. Corte: 2 octubre 2026, mensajes hasta 14:26 Colombia. Abarca el incidente del 1 octubre y su continuación del 2 octubre. Horas de Teams en Colombia; las horas internas de logs sin zona confirmada se conservan como aparecen.

## Conclusión

Hubo dos recuperaciones mediante reinicio, pero no una corrección permanente demostrada. El 1 octubre se recuperó el guardado después de rebuild y reinicio de NetTrack. El 2 octubre reapareció tras cambios en Medical911. Después del segundo reinicio J.R. comunicó validación interna a las13:58 y confirmación de Jim a las14:10. La causa exacta sigue abierta.

Hay dos investigaciones diferentes: fallas al guardar casos después de cambios de configuración y fecha de último guardado de configuración ausente o sin actualizar en DB. La segunda impide reconstruir qué se guardó frente a qué se construyó; no hay evidencia de que cause la primera.

## Fuentes y cobertura

1. Jira RCS-29234, descripción, estado y16 comentarios completos:14 públicos y2 internos. Consulta2 oct: Critical, Work in progress, Sebastian Garces, sin issues vinculados. https://trebuco.atlassian.net/browse/RCS-29234
2. Teams: grupo ahora llamado Camila, Chris, J.R., +6; hilo19:72b45a21ac484849a720312e5aae54a6@thread.v2. Mensajes del1 oct y continuación del2 oct hasta hipótesis de Ryan editada14:17. Chat privado J.R.: recordatorio07:00, aclaración09:01 y seguimiento14:21 a14:24. Grupo J.R. and Sebastian: llamada iniciada14:26, sin resultado escrito disponible.
3. AALPS Issues:30 respuestas del hilo público leídas en la revisión inicial. No se afirma que30 siga siendo el total tras la ampliación de hoy. https://teams.microsoft.com/l/message/19:d3b0ee0652e64b87a253d54ba3252810@thread.tacv2/1790881487066?tenantId=00646d1d-3d1b-48b6-bb60-e85055107d85&groupId=251a274e-8105-4474-9da9-bbacfce8f037&parentMessageId=1790881487066
4. Documento de Garces, versión5,2026-10-02 02:06:32UTC: https://trebuco.atlassian.net/wiki/spaces/AALPS/pages/478266851331 . Es interpretación posterior a la primera recuperación, no validación independiente de causa.
5. Runbook: https://trebuco.atlassian.net/wiki/spaces/ARPDT/pages/478244044803/Restart+Secure+Apps+pipeline . Garces enlazó ejecución20261002.4: https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_build/results?buildId=832904&view=results . Resultado sustentado en llamada y validaciones, no en inspección independiente del pipeline.
6. Cuatro transcripciones aportadas por Juan: /Users/MancoMenStudio/.codex/attachments/195df47d-e57a-4a32-8bfa-b22e9e247cd0/Texto pegado.txt . Whisper local; llamada1 tiene nombres sin corregir. No se escucharon audios originales. Se parafrasean y citan minutos; frases dudosas no se tratan como hechos.
7. Cerebro: ficha, bitácora y fuentes de RCS-29234; antecedentes ENG-9281, ENG-556, ENG-7188 y evidencia histórica RCS-28223. No se escribieron bases ni se ejecutaron ingestores.

## Cronología del1 de octubre

| Hora Colombia | Hecho y fuente |
|---|---|
|14:01 a14:06|Rajith acusa recibo en Jira. Jim precisa que Shoplifting funciona y CentralStationMaster parece afectada.|
|14:04 a14:42|Alerta Critical en AALPS Issues, recordatorios de falta de asignación; Juan pide revisar a Rueda14:37, Rueda responde checking14:42.|
|14:55|J.R. pide apoyar a Rueda y enfatiza comunicación en ticket.|
|14:59 a16:03|Rueda pide pasos/grabación. Jim ofrece screenshare15:44 y menciona ambas pantallas. Rueda pide usuarios15:55; Jim responde todos16:03. J.R. solicita llamada si faltan detalles.|
|17:30 a18:00|Jim pregunta por avances. Garces comunica17:54 que descartaron restricciones de seguridad y pide capturas. J.R. pide reproducir juntos y consultar logs.|
|18:02 a18:24|Kiran comparte error DateReported/ACCIDENT y logs Client441; afirma que DateReported sí existe en Accident. Primera llamada grupal.|
|18:27 a19:08|Garces publica fix implementado. Validación falla; Kiran19:03 dice que rebuild no ocurrió. Garces tiene limitación de acceso. Kiran termina Build All Screens19:08.|
|19:32 a19:33|J.R. informa dos casos correctos y tercero con error, incluso tras limpiar caché/cookies. Comparte traza CentralStationMaster.aspx.|
|19:44 a20:14|Escalación a Chris/Opsgenie, revisión de Ryan. Se solicita prueba StaterBros, sin resultado final hallado. Chris centraliza conversación en llamada.|
|20:22 a20:41|Chris comparte runbook y app Azure. J.R. informa en AALPS Issues que reiniciaron10 instancias y desapareció el problema.|
|20:53|J.R. transmite tres pruebas correctas de Jim.|
|21:23|Ryan no encuentra DateReported ni línea 784 en versiones Blob; máximo aproximado 350 líneas. Discrepancia pendiente.|
|21:25 a21:27|J.R. informa cambios/copia de case type por Jim; Leigh Ann seguiría al día siguiente. Jim cancela reunión porque funciona.|

La traza contiene Column 'DateReported' does not belong to table ACCIDENT, LoadPageInfo/Page_Load y HTTP 500. Referencias 9025df69-a770-4795-8452-5c00ca273478 y 5c8ef32f-d7b5-499c-9daf-ddd0475e5437; timestamp 2026-10-02 00:29:32. No demuestra columna físicamente ausente de SQL: Kiran afirmó lo contrario. Debe verificarse el objeto/esquema cargado durante esa petición.

## Cronología del2 de octubre

| Hora Colombia o audio | Hecho |
|---|---|
|07:00 y09:01|J.R. solicita Defect por last save date; aclara que ocurre en DB y GUI no muestra fecha.|
|Llamada1|Revisión de atención y liderazgo con Camila/Juan; detalle separado abajo.|
|12:52|Jim publica recurrencia: Medical911 modificada, Save and Build, casos vacíos o colgados. Comentario público3375792.|
|12:58|Shreyas acusa recibo públicamente,3375796.|
|13:01 a13:12|Llamada interna. Identificar disparador, frenar cambios de diseño y reproducir en test. Kiran mantiene alternativas código/infraestructura.|
|Llamada3,00:02 a02:45|Jim confirma que CentralStationMaster no se tocó hoy y funciona; falla Medical911. Aclara diferencia entre pantalla de entrada y case type.|
|Llamada3,03:13 a03:43|J.R. explica ausencia de fecha Save frente a Save and Build. Afirma que dejó de actualizarse hace2 o 3 años al separarla de GUI; historia no comprobada independientemente. Dice que el defecto debía haberse registrado por la mañana.|
|13:22 a13:25|Ryan relata síntomas con Katy desde unas2 semanas. Clear screen cache, clear cache y nuke cache no ayudaron. Esperar1 hora no es viable operativamente.|
|13:33|J.R. confirma coordinación con Ripp y propone pipeline de Nick.|
|13:38|J.R. publica pasos exactos de Leigh Ann y dos números de caso.|
|13:42|Garces comparte Run20261002.4,buildId832904.|
|13:43|Ryan no ve errores relacionados con esa página. No demuestra ausencia de falla ni permite reutilizar automáticamente excepción de ayer.|
|13:46 a13:49|Timeout aclarado: CPF.Core.LogOnTimeoutMinutes=60, suficiente según Ryan.|
|Llamada4,07:30 y11:55|Pipeline aprobado y finalizado según conversación. Solo NetTrack, no YARP. J.R. permite detener rebuilds pendientes08:13: sospecha que reiniciar bastaba, sin demostrarlo.|
|Llamada4,12:24 a19:57|Prueban creación/guardado Medical en Stop & Shop9999, piden otra prueba y retirarlas. Reproducción de cambios de diseño solo en test.|
|13:58 y14:10|Validación interna y confirmación de funcionamiento para Jim transmitidas por J.R.|
|14:04|Kiran pide conservar ticket en Support hasta decisión de Matt.|
|14:14,editado14:17|Ryan propone conflicto entre pestañas con sesiones distintas. J.R. preguntará.|
|14:15 y14:26|Juan dice que aún no reproducen. Nueva llamada J.R./Juan/Garces14:26, sin resultado escrito leído.|

No afirmar que todos los rebuilds de hoy finalizaron: la instrucción cambió durante la llamada. Tampoco hubo evidencia de despliegue de un fix de código. Hay evidencia de reinicio y recuperación.

## Pasos exactos de Leigh Ann

Mensaje J.R.13:38:

1. Abrir Screen Designer. Añadir Time reported, binding Accident_AccidentTimeReported.
2. Añadir Title of Person Reporting, binding ShopliftingExtra_AssociateReportedEmail.
3. Save and Build.
4. Renombrar AssociateReportedEmail a Title of Person Reported. Conservar diferencia textual respecto al título previo.
5. Crear2026-Food Lion ,LLC-9988-47: correcto.
6. Marcar ambos campos obligatorios en Medical911.
7. Crear2026-Food Lion ,LLC-9988-48: procesamiento indefinido.

El primer guardado después de Build funcionó. Hay que probar cambios de obligatoriedad/Hide/Display, no reducir reproducción a añadir un campo. Falta confirmar dónde se renombró, dónde se marcó required y qué Save se usó en cada etapa.

Ryan reconstruye actividad hasta16:28, login16:59, rebuild17:27, guardado aparentemente correcto17:32 y Hide/Display17:35,17:36,17:39. Son horas citadas de logs, zona sin explicitar; no confundir con publicación14:14 Colombia. La atribución a Leigh Ann es probable según Ryan, no identidad comprobada por nosotros.

## Hipótesis y límites

Confirmado por fuentes: dos episodios; relación temporal con cambios de diseño en segundo; alcance de hoy Medical911 según cliente; recuperación tras reinicio; primer caso postbuild correcto; metadata Save ausente reportada por J.R.; Support conserva asignación.

Principal: estado de pantalla/configuración en caché incoherente con runtime. Apoyan reinicio y antecedentes de retrasos. Falta caché concreta, clave, invalidación, versión e instancia. Un assembly obsoleto específico no está probado por esta investigación.

Adicional: pestaña anterior al nuevo login conservando sesión distinta. Comparar sesión limpia y pestañas previas bajo idéntico cambio. Valor60 del timeout no descarta conflicto de sesión.

También discriminar metadatos required/Hide/Display y configuración específica ADUSA frente a defecto compartido. El cambio a obligatorio es pista, no causa establecida.

No respaldado: timeoutSQL120s como explicación final; usuario olvidó Save and Build; columna físicaSQL ausente; ENG-9699 como causa; recuperación temporal como fix permanente.

## Qué pide J.R. con el Defect

Persistencia/trazabilidad del último guardado de configuración de Incident/Screen Designer. LastBuildDate permite ver builds; fecha Save no reconstruye modificaciones previas. Objetivo: distinguir Save de Save and Build al investigar. No es petición demostrada de añadir una columna visual.

Tres conceptos diferentes: DateReported del caso en excepción; LastSavedDate de configuración, candidato según esquema histórico; LastBuildDate de construcción. Tabla candidata incident.ScreenMaster. No se consultó fila ADUSA en DB; confirmar tabla/campo/valores antes de presentar reproducciónSQL como realizada.

No se encontró duplicado exacto en búsquedas por last save, last saved, LastSavedDate yRCS-29234, incluyendo creados2 oct. No garantiza inexistencia: título distinto o alcance de acceso. La frase de J.R. en llamada no prueba ticket creado; faltaID. Borrador inglés en inbox/2026-10-02-defect-last-saved-date-borrador.md.

## Precedentes y correcciones

ENG-9281, Unknown cache causing screen design changes to not appear, Backlog/High/sin asignar. LVN: cambios tardan horas/días pese a limpiar navegador. Comentario Kathryn22 sept. Ryan hoy aporta semejanza con trabajo de Katy. Referencia fuerte, no duplicado confirmado: https://trebuco.atlassian.net/browse/ENG-9281

ENG-556, Build Date Not in Local Time, Done. Zona horaria, distinto de Save sin actualizar: https://trebuco.atlassian.net/browse/ENG-556

ENG-7188, verificación de pantallas construidas en cutover, Done. Precedente de comprobación de rebuild, no causa probada: https://trebuco.atlassian.net/browse/ENG-7188

inbox/2026-08-27-rcs-28223-EVIDENCIA.md y consultas-parte2 muestran incident.ScreenMaster con LastSavedDate NULL,LastSavedByID 0 y LastBuildDate29 jul para 74 pantallas Audit de McDonalds. Confirma esquema/valores históricos. La antigua inferencia NULL significa que nadie guardó no es segura ante el defecto reportado; NULL tampoco demuestra por sí solo mismo bug.

Confluence dice Client112/aholddelhaize; Kiran y trazas usan441/adusa. Aclarar identificador; no consultar112 a ciegas. Resolved describe primera recuperación y no recurrencia. Su causa definitiva excede evidencia cruzada y objeciones de Ryan.

## Liderazgo y atención: llamada1

Análisis interno para Juan, separado del texto al cliente. Transcripción automática con errores; no convertirla en registro disciplinario literal.

J.R. pide investigación verificable: cliente, reproducción, logs,DB y precedentes; IA para apoyar hipótesis, no reemplazar comprobaciones (00:00 a02:36). Camila reporta dos fallas identificadas en su conversación con Sebastian: urgencia no comprendida y falta de comunicación de prioridades, bloqueo y fin de turno (02:43 a07:46). Es relato de Camila, no observación independiente de todo el trabajo del ingeniero.

J.R. espera de Juan supervisión, comunicación, priorización y escalación, aproximadamente mitad del tiempo tickets y mitad mentoría/gestión (08:45 a13:05). Su objetivo no es que absorba todos los casos complejos. Camila plantea seguimiento frecuente de críticos y revisión diaria de cola hasta lograr autonomía (14:40 a16:11).

Ambos respaldan autoridad de Juan y ofrecen ayuda cuando instrucciones no se siguen (18:18 a20:18). Acción: prioridad explícita, comprobar comprensión/avance, relevo claro al salir y escalación temprana. No hay decisión formal de empleo tomada en estas fuentes; evaluaciones personales son opiniones expresadas.

Juan explica situación personal grave al final; ambos ofrecen cobertura/tiempo y piden aviso para organizar relevo (22:37 a26:13). Aprendizaje: comunicar indisponibilidad y acordar responsable, no exigir disponibilidad continua. Detalles personales no se trasladan al texto técnico.

## Acciones, compromisos y prueba propuesta

Juan/Garces: reproducir en entorno interno no productivo, guardar evidencia y actualizar ticket. Último resultado escrito: sin reproducción14:15. Este agente no ejecutó pruebas productivas ni cambió configuración.

Cliente: pausa de cambios del diseñador, Save/Save and Build de configuración, hasta nueva indicación. Puede seguir creando/guardando casos tras recuperación. No confundir pausa del diseñador con prohibir Save operativo. Los pasos de Leigh Ann ya fueron publicados por J.R.13:38.

J.R.: materiales a ingeniería, preguntar pestañas, revisión con Matt lunes5 oct y conversación con seguridad sobre aprobación del pipeline. Compromisos expresados, no completados verificados. El acuerdo verbal con Ripp no sustituyó aprobación técnica del pipeline.

Support conserva RCS-29234 según Kiran. J.R. plantea bajar prioridad después de estabilizar, probablemente High; Jira sigue Critical. No afirmar cambio realizado ni prometer fix lunes: Matt vuelve para investigar.

Prueba propuesta, no ejecutada: guardar caso base; añadir campos exactos; Save and Build; crear/guardar; renombrar y probar; cambiar required/Hide/Display y probar. Capturar pantalla/caso, hora/zona, request/error y valores Save/Build por paso. Repetir con sesión limpia y pestaña previa al login. Control con pantalla no modificada. Si se investiga caché distribuida, registrar instancia y versión/runtime atendiendo petición.

Pendientes: reproducción; filaDB ADUSA; ID del Defect; respuesta de Leigh Ann sobre pestañas; mecanismo de invalidación; comentario público de recuperación y siguiente compromiso. No hay aún confirmación escrita posterior a llamada14:26.
