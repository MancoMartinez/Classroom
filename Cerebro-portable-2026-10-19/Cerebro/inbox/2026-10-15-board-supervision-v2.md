# Corrección de dirección del board

Juan rechazó la versión editorial por perder utilidad, indicadores por persona, legibilidad y efectos interactivos. La propuesta anterior de portada con imagen y mínimos indicadores queda superada por esta corrección. No hay borradores para terceros.

Implementación en curso: cabecera de supervisión compacta, alertas por motivo, monitores por persona con carga y distribución equipo/cliente, tipografía de tickets mayor, atención seleccionada por defecto. Humanoide construido como geometría de puntos WebGL desde el arte original, con profundidad, repulsión por cursor y dispersión al pulsar. No es un modelo anatómico completo; sí son partículas renderizadas e interactivas.

Conservar datos actuales y plantilla. Espera cliente separada del reloj activo. Sin acciones Jira o Teams.

Cambios terminados: monitores por persona ordenados por cantidad de casos con señal de atención; al pulsar filtran tickets. Métricas separadas para respuesta, ownership y actualización. Filas con prioridad, estado, responsable y acción visible; títulos de 17 px en escritorio y 16 px en móvil, motivos de 13 px. Los indicadores siguen el snapshot existente, sin consulta nueva a Jira.

Validación: build correcto, siete pruebas previas de clasificación/turnos correctas. Navegador sin errores WebGL; canvas activo, dispersión al pulsar y filtro Por responder devuelve un caso. Foco por persona comprobado. Móvil 390 px sin desborde horizontal del documento. Capturas supervision-desktop.jpg y supervision-mobile.jpg en .impeccable/review/ del proyecto.

Límite visual: nube de puntos con profundidad derivada del arte, no malla anatómica de 360 grados. El corte puede cambiar por el recolector habitual. No se validaron SLA ni compromisos contra Jira en vivo.

Revisión visual independiente final: ship, sin bloqueantes comprobados en las capturas. Detalle expandible comprobado tras compilar. Fuente y plantilla actualizadas, datos conservados. Servidor temporal detenido. Las notas editoriales previas conservan valor histórico; esta corrección fija la dirección vigente.
