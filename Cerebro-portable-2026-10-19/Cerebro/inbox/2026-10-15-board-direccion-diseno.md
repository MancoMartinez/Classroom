# Board Cerebro: diagnóstico y dirección de rediseño

15 octubre 2026. Análisis solicitado por Juan. No se modificó la aplicación.

Método: evaluación de diseño por /root/design_review y contraste visual, referencias y detector por /root. La evaluación independiente B agotó su cuota antes de entregar; el padre completó su comprobación. Alcance visual: escritorio, vista general oscura, HTML generado. No certifica móvil, accesibilidad completa ni estado actual de Jira.

## Diagnóstico

La composición conserva la estructura de un dashboard de tarjetas y le añade efectos futuristas. La diferencia con las referencias nace de la jerarquía, el espacio y la calidad de la pieza visual protagonista. La tecnología disponible permite el rediseño.

P1. La entrada posterga la decisión. El primer pantallazo contiene navegación duplicada y un hero grande sin tickets accionables. Después aparecen métricas, radar y 13 fichas antes de la lista. Llevar la primera intervención al primer pantallazo y dejar el directorio del equipo bajo demanda.

P1. Indicadores que perjudican la confianza. MetricsDeck calcula salud con max(0,100-conBandera*5). El corte mostrado tiene 34 banderas y obtiene 0%, independientemente del total. El anillo suma equipo 48%, cliente 52% y banderas 23%. Las banderas se solapan con los otros grupos. Separar distribución de responsabilidad y alertas. Distinguir seguimiento cliente de riesgo con reloj activo según AGENTS.md. No interpretar estos números como Jira actual.

P1. Repetición de contenedores. Hero, cuatro KPI superpuestos, seis KPI adicionales, radar, personas y casos repiten paneles. Usar superficie continua, separación por tipografía y espacio, y reservar recuadros para excepciones.

P2. La figura queda tapada. CommandHero importa HoloSphere3D, cuya geometría es esférica con bandas y emisión superior. HumanoidHologram existe sin conexión al hero. La captura muestra una masa de partículas parcialmente cubierta por cuatro KPI. No acredita un humanoide anatómico comparable a FLUX. Construir una silueta propia reconocible con rostro, cuello, hombros y filamentos dirigidos, dejando despejada su zona.

P2. Lenguaje y movimiento compiten. Orbital telemetry, cockpit, flags, radar, halos y giros añaden señales sin explicar la decisión. Unificar términos operativos y concentrar movimiento en el humanoide. Mantener lectura quieta.

Corrección de revisión: el HTML generado SÍ contiene meta refresh de 300 segundos. No afirmar que nunca recarga. La recarga no prueba que la extracción de Jira haya actualizado el archivo. Mostrar fecha del corte y estado de lectura; el reloj actual y Sistema en línea no lo acreditan. Header recibe lastUpdated sin presentarlo.

## Referencias y síntesis

FLUX, https://99designs.com.co/profiles/arthean/designs/2034225: silueta humana reconocible, filamentos que salen en una dirección y contraste contra espacio oscuro. Adoptar anatomía, dirección y protagonismo con arte original.

BLACKBOX, https://99designs.com.co/profiles/arthean/designs/2032165: espacio negativo, texto agrupado, alternancia entre imagen y contenido y pocas delimitaciones. Adoptar la composición editorial. Pintar las tarjetas de blanco no reproduce ese resultado.

ARIIA, https://99designs.com.co/profiles/arthean/designs/2184473: ritmo de secciones y un gráfico focal con etiquetas alrededor. Adoptar gráficos puntuales cuando la relación entre datos lo justifique. No trasladar tokenomics a categorías superpuestas.

Galería consultada: https://99designs.com/inspiration/websites/futuristic. La colección muestra FLUX entre sus ejemplos. Referencias individuales verificadas visualmente en navegador; el lector web no pudo abrirlas.

Dirección propuesta: Cerebro como briefing operativo. Fondo tinta profundo, texto claro, cian/violeta concentrado en una sola figura. Información con ritmo editorial y rojo/ámbar reservados para condiciones operativas verificadas.

Primera pantalla: cabecera compacta con región, búsqueda y fecha de corte. Composición asimétrica con humanoide libre a un lado y síntesis breve del turno junto a la intervención prioritaria al otro. Los datos mandan la jerarquía. La figura conserva presencia sin ocupar toda la entrada.

Continuación: flujo de casos agrupado por decisión, con cliente, problema, motivo de atención, responsable y plazo comprobable. Separación mediante aire y líneas discretas. Detalle desplegable sin perder contexto. Equipo en una sección secundaria con distribución de carga, turno y excepciones. Backlog vacío ocupa una línea.

Modelo visual: silueta estable, dispersión lateral dirigida, respuesta suave al puntero y una transición breve al cambiar de contexto. Alternativa estática si falta WebGL o se solicita movimiento reducido. No asociar intensidad o color a riesgo hasta definir la variable.

## Ejecución recomendada

1. Definir una sola composición de la portada y un caso expandido con el corte local, claramente fechado. Validar jerarquía antes de animación.
2. Crear la pieza humanoide original. Elegir render con animación localizada o modelo 3D según la interacción necesaria; Three.js ya existe en el proyecto.
3. Reorganizar CommandHero, MetricsDeck y GeneralView. Reutilizar filtros, búsqueda, idiomas, vista individual y enlaces Jira. Alinear indicadores y seguimiento con las reglas vigentes.
4. Validar teclado, movimiento reducido, pantalla estrecha y fluidez en el equipo de uso. Comprobar que Juan identifica qué requiere atención, quién lo lleva y por qué en diez segundos. Objetivo de validación, todavía no medido.

## Evaluación heurística provisional

Estado del sistema 1/4; lenguaje real 2/4; control 3/4; consistencia 2/4; prevención 2/4; reconocimiento 2/4; eficiencia 3/4; minimalismo 1/4; recuperación 1/4; ayuda 1/4. Total 18/40. Evaluación experta, no ensayo con usuarios.

Fortalezas: datos de dueño/turno/responsabilidad; filtros y búsqueda; base cromática legible. Perfiles afectados: usuario frecuente tarda en llegar a casos; nuevo usuario debe interpretar jerga; usuario de teclado encuentra contenedores clicables sin semántica equivalente a botón.

Detector: tres advertencias gradient-text en frontend/src/index.css líneas 107, 113 y 119. Son señales estilísticas, no prueba de fallo ni veto al futurismo solicitado. No se inyectó overlay: la API de evaluación del navegador es de solo lectura.

Fuentes locales: frontend/src/components/CommandHero.jsx, HoloSphere3D.jsx, HumanoidHologram.jsx, MetricsDeck.jsx:18-21 y 128, Header.jsx, App.jsx, board/index.html. Historia consultada: inbox/2026-10-09-board-equipo-colombia-v2.md. Las reglas de AGENTS.md del 15 octubre prevalecen sobre sus umbrales antiguos. El backend todavía define SEGUIMIENTO_CLIENTE con tres días; revisar frente a los cinco días hábiles vigentes antes de presentar seguimiento como urgencia.

Siguiente paso: Juan y agente, concretar una portada editorial con humanoide y primera intervención visible. Decisión pendiente para la siguiente fase: aprobar esta dirección visual antes de implementar el rediseño completo.
