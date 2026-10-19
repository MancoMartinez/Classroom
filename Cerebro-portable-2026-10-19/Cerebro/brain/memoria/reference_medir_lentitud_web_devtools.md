---
name: reference_medir_lentitud_web_devtools
description: "Protocolo para medir una queja de lentitud web con DevTools y decidir si el tiempo se va en el servidor o en el cliente"
metadata: 
  node_type: memory
  type: reference
  originSessionId: a8293f75-ab64-479b-971f-f586abf0f63b
  modified: 2026-08-13T18:19:34.457Z
---

Cuando un cliente reporta "tarda 30 segundos", lo único que hay son autorreportes. Sin números propios ni línea base, Engineering no actúa y el cliente puede discutir la cifra. Este es el protocolo.

**Antes de medir: consigue un tenant de control.** Si el defecto afecta a 3 bases de 39, quedan 36 sanas. Medir los mismos pasos en una sana convierte "30 segundos" en "N veces más lento de lo normal", que es la única forma de un número defendible. Sin control no hay medición, hay anécdota.

**Los tres errores que arruinan la medición en DevTools:**
1. **Preserve log sin marcar.** El log se borra en cada redirección, y los saltos entre aplicaciones *son* cadenas de redirecciones. Sin esto se pierde justo lo que se quería medir.
2. **Throttling activo.** Debe estar en No throttling. Disable cache desmarcado para la corrida tibia, marcado para una corrida fría al final.
3. **Una sola corrida.** Tres corridas y se toma la mediana.

**El número que importa no es el total, es el `Waiting for server response` (TTFB)** de cada request de tipo `document`, en la pestaña Timing. Registrar también requests, transferred, Finish, DOMContentLoaded y Load. Guardar la evidencia con *Save all as HAR with content*.

**El discriminador, que es el punto de todo el ejercicio:**
- Si la suma de los TTFB se come el tiempo reportado, **el tiempo se va en el servidor**: una caché de front-end no arregla nada para ese cliente.
- Si los TTFB son rápidos (menos de ~2 s cada uno) y el total sigue siendo alto por cientos de requests pequeños, **el tiempo se va en el cliente** y una caché de assets o labels es exactamente el arreglo.

Esa respuesta casi nunca la tiene nadie, y es lo que se lleva a Engineering. Aplicado por primera vez en [[project_rcs_28256_tailored_brands]].

Complemento del lado de base de datos: [[reference_query_store_regresion_plan]]. Si el síntoma es un 524, primero [[reference_waf_cloudflare_bloqueos]].
