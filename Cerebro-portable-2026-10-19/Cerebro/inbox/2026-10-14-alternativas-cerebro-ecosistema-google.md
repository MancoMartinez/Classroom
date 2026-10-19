# Alternativas para operar Cerebro en el ecosistema de Google

Fecha: 2026-10-14.
Autor: Antigravity.
Propósito: Evaluar alternativas en el ecosistema de Google equivalentes a Claude Projects y Custom GPTs para interactuar con Cerebro superando las restricciones de Google Cuaderno.

## 1. Google Gemini Gems con Google Drive sincronizado

Gemini Gems es el equivalente directo a Custom GPTs y Claude Projects en la interfaz gráfica de Google.

Mecanismo de operación:
1. Crea un Gem específico para Cerebro en la aplicación web de Gemini.
2. Copia las directrices de AGENTS.md en el cuadro de instrucciones del Gem.
3. Instala Google Drive para macOS en el equipo local.
4. Conecta una carpeta de sincronización local que espeje brain/markdown/, flujos/, investigaciones/ e inbox/.
5. Vincula esa carpeta de Google Drive como fuente permanente del Gem.

Ventajas:
* La sincronización local mantiene los documentos actualizados en la nube sin cargas manuales.
* Permite interacción por chat desde la aplicación web o móvil de Gemini.
* Mantiene el flujo de entrega: los borradores producidos se descargan a inbox/ en el Mac.

Límites:
* Las modificaciones tardan los minutos que tome la sincronización de Google Drive.
* Carece de ejecución de herramientas de terminal como bin/buscar o bin/cerebro.

## 2. Google Antigravity en modo Workspace con modelos Gemini

Antigravity opera como entorno de agente local sobre la carpeta raíz de Cerebro.

Mecanismo de operación:
1. Abre /Users/MancoMenStudio/Cerebro directamente en el entorno de trabajo.
2. Selecciona modelos Gemini como Gemini 3.8 Flash o Pro.
3. La herramienta inspecciona el árbol de archivos, lee fuentes y ejecuta bin/buscar mediante llamadas directas.
4. Genera los entregables directamente en inbox/ respetando la regla permanente de entrega.

Ventajas:
* Elimina la necesidad de exportar o subir archivos a la nube.
* Ejecuta el motor híbrido local de búsqueda BM25 y vectorial en tiempo real.
* Permite edición supervisada y redacción directa en el disco local.

Límites:
* Requiere ejecución en el Mac donde residen los datos.

## 3. Servidor MCP Cerebro conectado a clientes Gemini

Cerebro cuenta con bin/cerebro_mcp.py configurado por stdio.

Mecanismo de operación:
1. Conecta el servidor local de Cerebro mediante configuraciones de clientes compatibles con MCP en el entorno Google.
2. El modelo invoca las herramientas nativas: buscar_conocimiento, contexto_ticket, leer_fuente y estado_cerebro.
3. El motor local atiende la recuperación y devuelve evidencia con rutas exactas al modelo.

Ventajas:
* Accede directamente a los 18325 fragmentos vectorizados y a la base SQLite en solo lectura.
* No duplica almacenamiento ni expone la base entera a la nube.
* Aplica el mismo contrato que ya opera en Claude Desktop y Codex.

Límites:
* Requiere soporte de protocolo MCP por stdio en el cliente que ejecuta Gemini.
