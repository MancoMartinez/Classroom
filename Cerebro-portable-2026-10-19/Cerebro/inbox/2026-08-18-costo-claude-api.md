# Cuánto costaría mover Moscú a Claude — cálculo con volumen real

Medido sobre tu base, no estimado. Ventana: **25 may – 18 ago 2026, 85 días**.

## Lo que Moscú realmente consumió

| Uso | Volumen real |
|---|---|
| Chunks contextualizados | 1.511 llamadas |
| Turnos de chat | 33 (66 mensajes, 16 conversaciones) |
| Sesiones de transcripción | 6 |
| Texto total en la base | 4,06 M caracteres ≈ 1,0 M tokens |

El dato que sorprende: **el gasto no estuvo en el chat, estuvo en la indexación**. 1.511
llamadas de contextualización contra 33 turnos de conversación. Chateaste con Moscú 33 veces en
tres meses.

## Tamaño exacto de cada llamada

Leído del código de `ChunkContextualizer`:
- Entrada: 3 fragmentos vecinos × 200 chars + 800 chars del fragmento + instrucciones ≈ **400 tokens**
- Salida: máximo 60 palabras ≈ **90 tokens**

Chat, con el `PromptBudgetManager`: perfil 300 + insights 200 + contexto 800 + summaries 750 +
RAG 3.000 ≈ 5.200 tokens de sistema, más historial. Unos **7.000 de entrada** y **510 de salida**
por turno.

## Total de los 85 días

**~0,94 M tokens de entrada · ~0,20 M tokens de salida**

## Costo con tarifas de la API de Anthropic

| Modelo | Entrada | Salida | Los 85 días | Por mes |
|---|---|---|---|---|
| Haiku 4.5 | 1 $/MTok | 5 $/MTok | **1,94 $** | 0,70 $ |
| Sonnet | 3 $/MTok | 15 $/MTok | **5,82 $** | 2,10 $ |
| Opus | 15 $/MTok | 75 $/MTok | **29,10 $** | 10,40 $ |

Con la Batch API (50 % de descuento, y la contextualización es indexación offline, perfectamente
batcheable) Sonnet baja a unos **3,90 $** por los tres meses.

**Embeddings**: Anthropic no tiene API de embeddings, recomienda Voyage. `voyage-3-lite` cuesta
0,02 $/MTok, así que tu millón de tokens vale **2 centavos**. Con Ollama en local, cero.

## Escenario de uso intensivo

Si pasas a procesar reuniones a diario: un transcript de 1 hora son ~12.000 tokens; procesarlo
(resumir, estructurar, extraer acciones) sale a ~15.000 de entrada y 2.000 de salida. Con 20
reuniones al mes:

- Haiku: **0,50 $/mes** · Sonnet: **1,50 $/mes** · Opus: **7,50 $/mes**

## La conclusión incómoda

Tu carga de trabajo es diminuta para precios de API. Estás hablando de **entre 1 y 10 dólares al
mes**, y eso solo si usas la API directamente.

Pero es que probablemente **no necesitas pagar nada extra**: ya tienes Claude Code con
suscripción, y hoy hace exactamente lo que hacía GPT-4o dentro de Moscú, con más contexto y
acceso a Jira, Confluence y tus archivos. El transcript de J.R. y el de Viraj los procesé aquí,
sin API key, sin costo marginal.

**Recomendación:** no metas una API key en Moscú. Deja Moscú como almacén y transcriptor, y usa
Claude Code como motor. Si algún día quieres automatizar la indexación sin estar presente,
entonces sí, una key de Haiku por menos de un dólar al mes cubre la contextualización de todo lo
que entre.

Tarifas a confirmar en anthropic.com/pricing antes de decidir.
