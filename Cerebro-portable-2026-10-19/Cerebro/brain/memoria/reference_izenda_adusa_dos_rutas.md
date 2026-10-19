---
name: reference_izenda_adusa_dos_rutas
description: "Izenda en tenants migrados: el visor y la entrega programada leen fuentes distintas, y cómo distinguir cuál falla"
metadata: 
  node_type: memory
  type: reference
  originSessionId: a8293f75-ab64-479b-971f-f586abf0f63b
  modified: 2026-08-14T19:29:19.383Z
---

En un tenant migrado, Izenda tiene **rutas de ejecución distintas que no se comportan igual**. Confundirlas hace perder horas. Aprendido en RCS-28021, ADUSA, 14 ago 2026.

**Las tres cosas que un cliente llama "Izenda no funciona" y que son defectos separados:**

1. **Pantalla en blanco al guardar cambios en un reporte.** Fue configuración, un join mal guardado. Jie Chen lo corrigió el 31 jul 2026 sin cambio de código.
2. **El export no descarga.** Se pulsa Excel o CSV y no pasa nada, sin error, "it says loading and the file never downloads". Es el **síntoma A de ENG-5649**, donde el request de export nunca llega a `rs.aspx`.
3. **Los reportes programados traen datos viejos.** Llegan por correo y **se cortan exactamente en la fecha del cutover**. Ese corte exacto es la firma de la **segunda falla de ENG-5649**: la ruta cae a la cadena de conexión de la base vieja `dbo`, congelada antes de la migración, que no sincroniza desde el esquema `incident`.

**El discriminador clave:** si el usuario dice *receiving* o *reports we receive*, es entrega programada por correo y él no aplica ningún filtro. Si dice que abre el reporte y lo corre, es el visor. Son investigaciones distintas.

**El visor sí devuelve datos actuales.** Verificado en adusa el 14 ago: pidiendo 2026 sí salieron casos de 2026. Así que la base congelada **no aplica al visor**, solo a la ruta programada.

**Defecto propio del visor, reproducido en adusa:** el rango de fechas no persiste. En nueve actualizaciones entre 12:04 y 12:20 se dieron las cuatro combinaciones: rango en 2026 con datos viejos (3 veces), rango revertido con datos viejos (3), rango revertido con datos de 2026 (1), rango en 2026 con datos de 2026 (1). **La fecha que muestra la pantalla y los datos que devuelve son independientes**, y no hay error en ningún momento. Es el síntoma B de ENG-5649, que ese ticket registra como *"not yet isolated separately"*.

**Cookies que hay que capturar siempre** (léelas desde Network, en el header `Cookie:` de cualquier `rs.aspx`, no desde Application, porque algunas son HttpOnly):

```
pCohesion=50012-441
izscResponseServer=/adusa/nettrack/AdHoc/rs.aspx
ntWEBCFG=...&PLT=0&PLTFRMID=441&...
```

**Línea sin confirmar pero concreta:** ENG-5649 registra `PLT=1` en el tenant de Guess. En adusa es `PLT=0` mientras `pCohesion` sí está puesta. Las dos se contradicen sobre si el modo cohesión está activo. Vale confirmar con ingeniería si alguna ruta elige la conexión mirando `PLT` en vez de `pCohesion`.

**Los reportes traen rangos de fecha guardados en su propia definición.** El de Unusual Incidents Details en adusa venía con 6/17/2019 a 6/17/2020. En Guess ENG-5649 documentó 1/1/2025 a 9/30/2025. Un reporte programado corre contra esa definición, así que un rango fijo explicaría un correo idéntico todos los días.

**Antes de probar, leer los comentarios del ticket.** El 14 ago se probó el reporte equivocado porque no se leyó el comentario de la clienta de esa misma mañana, donde ya nombraba los dos reportes afectados: Food Lion "Interview Data with Source" y "PBI Incident Export Q-3" de Jim Cosseboom. Ver [[feedback_verificar_la_fuente_no_el_resumen]].

Ruta: `https://apps.apprissretail.com/<tenant>/nettrack/AdHoc/reportlist.aspx`

Ver [[project_adusa_ficha_y_tickets]], [[reference_medir_lentitud_web_devtools]].
