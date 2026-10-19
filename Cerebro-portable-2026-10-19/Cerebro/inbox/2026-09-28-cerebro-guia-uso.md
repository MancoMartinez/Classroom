# Cómo usar Cerebro desde hoy

El mismo motor sirve por consola, Codex y Claude Desktop. La recuperación es local; el modelo de la aplicación redacta a partir de las fuentes que recupera. Guardar una nota en inbox la vuelve consultable en la siguiente búsqueda, sin esperar a cerrar ni a ingerir la base.

## Codex y Claude Desktop

Quedó configurado un servidor MCP llamado cerebro en ambos clientes. Reiniciar completamente la aplicación o recargar sus servidores y abrir una sesión nueva. No es necesario reinstalar el plugin Atlassian. La configuración es para este Mac, con rutas absolutas; un escritorio remoto, Windows o un entorno aislado requieren su propia instalación o acceso autorizado a estas fuentes.

Prueba de aceptación dentro de cada aplicación:

“Usa estado_cerebro. Después usa contexto_ticket para RCS-28671 y lee la nota del 28 de septiembre sobre la ventana histórica. Distingue lo confirmado para md03-cit-d de lo que sigue abierto para las demás definiciones. Cita el archivo y las líneas.”

Deben aparecer cuatro herramientas: buscar_conocimiento, contexto_ticket, leer_fuente y estado_cerebro. Si no están disponibles, usar la consola. Estar conectado no garantiza que una respuesta genérica haya consultado Cerebro: la respuesta debe mostrar fuentes concretas.

## Consola

Desde /Users/MancoMenStudio/Cerebro:

```sh
python3 bin/buscar "un usuario tiene distrito pero no ve tiendas"
python3 bin/buscar RCS-28671
python3 bin/cerebro read inbox/2026-09-28-rcs-28671-comentario-interno-ventana.md --start 1 --count 100
python3 bin/cerebro status
```

El buscador devuelve JSON con evidencia, ruta y líneas. Un resultado no reemplaza leer el contexto completo. Si no encuentra lo esperado, reformular con el término técnico o una versión en inglés. Para búsquedas puramente literales, python3 bin/cerebro search "término" --mode bm25.

## Qué sucede por dentro

1. Revisa el texto de las fuentes y detecta cambios por contenido.
2. Actualiza solamente los fragmentos modificados en .cerebro/retrieval.sqlite.
3. Vectoriza lo nuevo con multilingual-e5-small en el Mac.
4. Combina posiciones de búsqueda BM25 y similitud vectorial mediante RRF, suma de 1/(60+posición).
5. Devuelve fragmentos con fuentes. Para IDs exactos construye un paquete con bitácora, notas recientes, ficha y referencias.

Las relaciones de items conservan enlaces registrados. Las relaciones entre tickets por menciones son pistas, no causas probadas. No se entrenan los pesos de Claude o GPT, ni se transforma una hipótesis vieja en un hecho nuevo.

## Mantenimiento y comprobaciones

```sh
python3 bin/cerebro index --vectors
.venv-cerebro/bin/python bin/test_cerebro_motor.py
.venv-cerebro/bin/python bin/test_cerebro_mcp.py
python3 bin/test_cola.py
.venv-cerebro/bin/python bin/eval_cerebro.py
```

index solo actualiza el índice derivado, nunca sessions.db. Si el índice falta se reconstruye desde las fuentes. El modelo está descargado y fijado a una revisión. Dependencias directas en bin/requirements-cerebro.txt; inventario del entorno en .cerebro/runtime-freeze.txt. La primera búsqueda de un proceso carga el modelo y tarda más que las siguientes; incorporar muchas transcripciones también tarda más que añadir una nota.

Si el canal vectorial falla, la respuesta avisa y conserva BM25. No interpretar esa degradación como resultados equivalentes. Si sessions.db no puede leerse, se muestra el error y no se reemplaza el índice completo con uno parcial.

El resultado de esta auditoría está en .cerebro/evaluacion-2026-09-28.json. Las siguientes ejecuciones guardan un archivo evaluacion-FECHA-HORA.json con firmas del corpus y preguntas, sin sobrescribir la evidencia anterior. El set heredado no mide exactitud de respuestas ni sustituye evaluar consultas reales nuevas. No modificar sus anclas para subir el resultado.

## Límites y recuperación

No indexa contenido visual ni adjuntos PDF/Excel automáticamente. No consulta Jira sin que el agente llame al conector. No existe aún un evaluador humano independiente de respuestas; leer las fuentes sigue siendo necesario. No se activó ningún servicio en segundo plano ni se programaron notificaciones.

No tocar brain/sessions.db. No ejecutar bin/guardar, bin/ingerir_inbox.py o cerrar desde el agente. Juan sigue ingiriendo manualmente desde su terminal cuando quiera consolidar la base.

Copias anteriores: .cerebro/buscar-antes-20260928.py, .cerebro/cola-antes-20260928.py y .cerebro/ARCHIVO.md.antes-20260928 para los documentos raíz. Configuraciones previas: ~/.codex/config.toml.before-cerebro-20260928 y ~/Library/Application Support/Claude/claude_desktop_config.json.before-cerebro-20260928. Para revertir después de otros cambios, retirar solo la entrada cerebro de MCP; restaurar todo el archivo antiguo podría perder configuraciones posteriores.
