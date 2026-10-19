# Appriss Secure — EBR

Carpeta 18 de la base de Moscú. 11 fragmentos.

## Secure EBR — Introducción y Roles
_chunk 924 · 2026-06-18_

Secure Store 5 es una plataforma de rendimiento minorista que combina inteligencia artificial y análisis de datos para mitigar pérdidas por fraude, robo y errores operacionales.

Roles principales:
- Analista Central: Identifica riesgos emergentes mediante métricas de riesgo clave y modelos analíticos. Configura Work Items, búsquedas, dashboards.
- Usuario Final/Investigador: Resuelve excepciones con velocidad mejorada (30% más casos, 50% investigaciones más rápidas). Usa Work View como cola de trabajo.

La plataforma se accede via web. El Menú Waffle da acceso a aplicaciones disponibles según datos e implementación del cliente. La barra de menú muestra: Work View, Searches, Investigations, User Menu — visibles según permisos del usuario.

## Secure EBR — Terminología Clave
_chunk 925 · 2026-06-18_

Glosario esencial de Secure EBR:

- Work View: Cola o lista donde aparece trabajo nuevo o asignado para investigación.
- Instant Analytics: Análisis automático completado sistemáticamente para excepciones detectadas.
- Exception/Work Item: Actividad individual de cajero/tienda que requiere investigación.
- Search/Búsqueda: Consulta de datos creada ad-hoc o guardada previamente.
- Investigation: Área de recopilación digital para evidencia y capacitación.
- Watchlist: Lista de monitoreo de tiendas o cajeros específicos.
- Event Viewer: Interfaz que muestra recibos, auditoría y transacciones relacionadas.
- Profile: Dashboard con métricas de desempeño de tienda/cajero y análisis comparativo.
- Dashboard: Elementos gráficos o informativos en página accesible.
- Report: Resultado de búsqueda programado distribuido a usuarios autorizados.
- SRA (Sales Reducing Activities): Métricas para actividades reductoras de ventas.
- Smart Tracks: Navegación contextual clic-derecha (Cashier Profile, Store Profile, Transaction Viewer).

## Secure EBR — Flujo Work View Investigation
_chunk 926 · 2026-06-18_

Flujo completo de investigación en Work View (4 fases):

FASE 1 — Recepción de Trabajo:
1. Sistema presenta New Work (excepciones en cola)
2. Usuario selecciona elemento de trabajo
3. Presiona Start Work → asignado automáticamente

FASE 2 — Análisis Inmediato (Instant Analytics):
Sistema genera automáticamente tiles analíticos con codificación por colores:
- Verde: Sin problemas detectados
- Ámbar: Actividad inusual presente
- Rojo: Actividad sospechosa que excede normalidad

FASE 3 — Investigación Detallada:
- Events Tab: Lista transacciones en investigación
- Journal Tab: Transacción en contexto secuencial
- Selected Tab: Recibo con opciones auditoría/CCTV
- Pinned Section: Hasta 4 transacciones simultáneas para comparación

FASE 4 — Disposición:
- Abandon: Sin fraude detectado (requiere razón de abandono)
- Add to Investigation: Evidencia de fraude encontrada

## Secure EBR — Search Composer
_chunk 927 · 2026-06-18_

Search Composer permite crear búsquedas personalizadas.

Estructura básica:
- Conditions: Criterios de filtrado con operadores In, Not In, Fields, Functions
- Display Fields: Campos que aparecen en resultados (nivel header)
- Expanded Display Fields: Campos a nivel transacción

IMPORTANTE — Multiplicación de conteos:
Los conteos multiplican según tabla origen:
- Header + Item = Conteo de artículos
- Header + Tender = Conteo de pagos
- Combinaciones múltiples producen multiplicaciones matemáticas

Navegación de resultados:
- Drill-down: Clic izquierdo para siguiente nivel de detalle
- Tabular/Graphical: Toggle visualización (máx 250 filas para gráficos)
- Quick Receipt: Ícono i muestra transacción en popup movible
- Export to Excel disponible
- Parameterized Options: Modificar parámetros y reejecutar

## Secure EBR — Work Item Composer (6-7 pasos)
_chunk 928 · 2026-06-18_

Configuración de Work Items — proceso de 6-7 pasos:

Paso 1: Título, búsqueda origen, sinopsis del work item
Paso 2: Tiles de análisis instantáneo (activar/desactivar cada tile)
Paso 3: Búsquedas de referencia suplementales
Paso 4: Enlaces a dashboards de tienda/cajero
Paso 5: Directrices para el investigador (protocolos, PDFs adjuntos)
Paso 6: Calendario y frecuencia de ejecución
Paso 7: Configuración de tarjeta Work View (aplicación origen, categoría, secciones de información)

## Secure EBR — Event Viewer
_chunk 929 · 2026-06-18_

Event Viewer es la interfaz central para revisar transacciones.

Sección EVENTS (izquierda):
- Investigation Tab: Lista transacciones excepcionales
- Journal Tab: Contexto transaccional secuencial
- Filter: Por POS, cajero, tipo transacción

Sección SELECTED (centro):
- Vista de recibo POS
- Opciones: Pin, CCTV link, descarga JPG
- Tabs: Receipt (renderizado), Audit (detalles keystroke/entrada), Links (profiles, búsquedas históricas), Associated (investigaciones contenedoras)

Sección PINNED (derecha):
- Máximo 4 transacciones simultáneas para comparación
- Modo Receipt/Audit
- Barras scroll sincronizables
- Highlighting de puntos idénticos entre recibos

## Secure EBR — Profiles (Store y Cashier)
_chunk 930 · 2026-06-18_

Dos tipos de perfiles en Secure:

STORE PROFILE:
- Información de la tienda y comparación con tiendas similares
- Análisis de métricas clave por período
- Gráficos outliers identificando áreas de mejora
- Uso: Preparación visitas, auditoría operacional, capacitación enfocada

CASHIER PROFILE:
- Datos del cajero y historial de transacciones
- Análisis de métricas con detección de outliers
- Historial para determinar duración y alcance de actividad
- Identificación de múltiples Métodos de Operación (MO)
- Comparación contra peers en misma tienda/cadena

Ambos accesibles vía Smart Tracks (clic derecho) o Watchlist.

## Secure EBR — Watchlist y Monitoreo
_chunk 931 · 2026-06-18_

Watchlist permite seguimiento continuo de tiendas o cajeros específicos.

Características:
- Link directo a Profile desde el portal Watchlist
- Identificador visual: ícono de ojo ámbar en resultados de búsqueda
- Clic en el ícono abre notas de watchlist
- Comparar actividad contra cadena/tienda/cajeros similares

Herramienta clave para monitoreo proactivo — marca entidades de interés antes de que generen excepciones formales.

## Secure EBR — Dashboards, SRA y Chart Wizard
_chunk 932 · 2026-06-18_

Dashboards en Secure EBR:

WORKBENCHES (Portales):
- Dashboard centralizado priorizando excepciones por severidad
- Insights accionables guiando decisiones
- Detección temprana de tendencias mediante ML
- Distribución óptima de recursos

DASHBOARD SRA (Sales Reducing Activities):
- Métricas especializadas para actividades reductoras de ventas
- Acceso a guía interactiva (Scribe)

CHART WIZARD:
Paso 1: Tipo gráfico (Area, Bar, Bubble, Column, Line, Pie, Scatter), ejes, título
Paso 2: Tooltips, colores, leyenda
Máximo 200 filas para gráficos legibles.

## Secure EBR — Notificaciones y Configuración
_chunk 933 · 2026-06-18_

Centro de notificaciones (User Menu):
- Indicador contador no leídas, reenvío por correo automático
- Escalamiento configurable
- Out of Office: delegación a usuario alternativo
- Estados: Rojo (sin leer), Negro (leída)

Configuración usuario:
- Idioma y página de inicio
- Notificaciones (email/sistema)

Documentación: versiones Markdown disponibles agregando .md a URLs. llms.txt contiene índice completo. Client Services contactable vía User Menu.

Pro Tips: Logo empresa → Home Portal. Filtros grupo búsqueda guardables (tres puntos). Nomenclatura organizada en búsquedas es crítica para eficiencia.

## Reunión 2026-06-18 — Secure EBR Day 3: Settings, Outliers, Smart Tracks
_chunk 934 · 2026-06-18_

## Resumen
En esta reunión se discutieron varios temas relacionados con la aplicación y su funcionamiento. Se mencionó que un cliente dejó un comentario sobre la aplicación, lo que llevó a analizar un problema técnico en el sistema que sigue intentando ejecutar procesos sin éxito. Se identificó la necesidad de una solución técnica para abordar este problema. Además, se habló sobre un editor de numeración que permite subir ciertos datos, aunque no quedó claro el propósito exacto de esta funcionalidad. También se mencionaron diferentes tipos de clientes y cómo se convierten en usuarios de búsqueda o en clientes activos, aunque la conversación fue algo confusa en este punto.

Se destacó la urgencia de atender ciertos comentarios y ventas relacionadas con los clientes, pero no se definieron acciones concretas ni se asignaron responsables específicos. La reunión parece haber sido más exploratoria que resolutiva, con varios temas mencionados de manera superficial y sin llegar a conclusiones claras o decisiones importantes.

## Temas clave
- problema técnico en la aplicación
- editor de numeración
- tipos de clientes y conversión

---

## Transcripción completa
And then do account, you'll see just enough Just a number will show up. So what'll happen is we'll see
