---
name: project_flujo_trabajo_cerebro
description: La carpeta ~/Desktop/Cerebro es la raíz única del segundo cerebro desde el 18 ago 2026, con buscar/guardar/exportar como herramientas de terminal
metadata:
  type: project
---

Creada el **18 ago 2026** para acabar con la dispersión: había siete carpetas compitiendo por ser "la organizada" (`Organizado`, `MOSCU-TRANSFER-2026-08-06`, `Moscu-Portable`, `Moscu-Portable 2`, `moscu-ops`, `moscu-ops-onboarding`, más lo suelto en Escritorio y Descargas).

**Raíz única: `~/Desktop/Cerebro/`**

| Carpeta | Qué es |
|---|---|
| `inbox/` | todo lo nuevo cae aquí sin pensarlo, se clasifica después |
| `brain/sessions.db` | copia consistente de la base de Moscú |
| `brain/markdown/` | la base entera en texto plano, un archivo por carpeta |
| `brain/memoria/` | copia de las memorias de Claude Code |
| `bin/` | `buscar`, `guardar`, `exportar.sh`, `db_a_markdown.py`, `hacer_indice.py` |
| `archivo/` | material crudo: adjuntos de tickets, grabaciones, capturas, trackers |

**Comandos, ya enlazados en `~/bin` y en el PATH:**
- `buscar "lo que sea"` — FTS5 sobre conocimiento, mesa de trabajo y memorias, en un segundo. Prueba AND y cae a OR si no hay resultados.
- `guardar <carpeta> "título"` con el cuerpo por stdin; `guardar --carpetas` lista los IDs. Moscú tiene que estar cerrada.
- `bin/exportar.sh` — regenera todo y produce `Cerebro-AAAA-MM-DD.zip` de ~14 MB, portable a cualquier máquina. Excluye `archivo/` a propósito (1.3 GB de crudo que no viaja).

**El contrato para otras sesiones está en `Cerebro/CLAUDE.md`** y el punto de entrada generado en `Cerebro/README.md`. Un Claude en otro PC solo necesita descomprimir el zip y leer el README.

**Reversión:** `archivo/DESHACER.sh` revierte los 106 movimientos de archivos del 18 ago leyendo `archivo/_movimientos.tsv`.

Ver [[project_moscu_sin_gpt]] y [[feedback_nada_solo_en_consola]].
