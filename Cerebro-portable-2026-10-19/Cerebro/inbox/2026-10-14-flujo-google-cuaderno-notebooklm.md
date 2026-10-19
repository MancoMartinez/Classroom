# Integración de Cerebro con Google Cuaderno (NotebookLM)

Fecha: 2026-10-14.
Autor: Antigravity.
Propósito: Definir el flujo operativo para consultar, trabajar y alimentar Cerebro usando Google Cuaderno sin violar las reglas del proyecto.

## 1. Arquitectura y límites técnicos

Google Cuaderno opera en la nube de Google. Carece de acceso al sistema de archivos local de este Mac, a SQLite y a los conectores de terminal.

Límites de Google Cuaderno:
* Acepta archivos de texto plano, Markdown, PDF y Google Docs.
* Admite un máximo de 50 fuentes por cuaderno.
* Cada fuente tolera hasta 500000 palabras.

Cerebro almacena 3952 fuentes y 18325 fragmentos. Subir el repositorio completo en archivos individuales satura el límite de 50 fuentes. La carga exige fuentes consolidadas.

## 2. Preparación y carga de fuentes (Consulta)

Usa la exportación en texto plano de Cerebro. No intentes subir brain/sessions.db.

Fuentes recomendadas para cargar:
1. brain/markdown/: 27 archivos Markdown consolidados por carpeta de conocimiento. Representan todo el contenido de sessions.db.
2. flujos/INDICE.md y sus archivos vinculados para procedimientos operativos.
3. investigaciones/INDICE.md y sus carpetas para análisis de causas raíz y mapas de sistemas.
4. confluence/RTS-triage/INDICE.md para antecedentes de fallas resueltas en otros clientes.

Estructura de cuadernos sugerida en la app:
* Cuaderno Base Técnica: los 27 archivos de brain/markdown/.
* Cuaderno Operaciones y Flujos: flujos/, investigaciones/ e índices de triage.
* Cuadernos por Caso o Cliente: notas de tickets específicos de tickets/ o bitacora/.

Para refrescar brain/markdown/ con cambios recientes de la base:
Ejecuta en terminal:
python3 bin/db_a_markdown.py brain/sessions.db brain/markdown

## 3. Reglas durante la sesión de trabajo en el cuaderno

Jira es la única fuente de verdad sobre el estado de un ticket. Las notas cargadas en Google Cuaderno describen el momento de su redacción. Verifica siempre el estado en vivo antes de emitir conclusiones de cola.

Separa hechos confirmados de hipótesis. Si Google Cuaderno propone una causa técnica, valida la evidencia citada contra los archivos locales antes de aceptarla.

## 4. Retorno de conocimiento a Cerebro (Alimentación y actualización)

Google Cuaderno no sincroniza cambios hacia el Mac. El flujo de retorno es manual y sigue el protocolo permanente de AGENTS.md:

1. Redacta o descarga el entregable generado en la sesión.
2. Guarda el archivo en inbox/AAAA-MM-DD-tema.md.
3. El motor local de Cerebro (.cerebro/retrieval.sqlite) detecta la nueva nota en inbox/ y la vectoriza en la siguiente búsqueda. Queda disponible de inmediato para búsquedas por consola y MCP.
4. Juan consolida formalmente la nota en brain/sessions.db ejecutando cerrar desde su terminal personal. El agente nunca ejecuta cerrar ni scripts de ingestión.
