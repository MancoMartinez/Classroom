---
name: project_uni_jul_26_attachments
description: "El bucket Uni_Jul_26_Attachments al 13 ago 2026: los tres tickets, qué validó Juan del release y por qué esa validación todavía no alcanza"
metadata: 
  node_type: memory
  type: project
  originSessionId: 2b736553-ea91-4441-bf59-40e05f44211f
  modified: 2026-08-13T18:26:49.924Z
---

**El tag de Jira es `Uni_Jul_26_Attachments`.** Es la etiqueta con la que se filtra el bucket de adjuntos de la Unificación. Camila la pidió el 13 ago y los tres tickets del bucket la tienen.

Los tres, todos en *Waiting for Software Release* hasta el release del 13 ago, y **ninguno es de Juan**:

| Ticket | Cliente | Qué reporta | Dueño |
|---|---|---|---|
| RCS-28167 | Stater Bros (Rich Aaron) | **No puede abrir** ZIP grandes ya adjuntos; los pequeños abren bien | Viraj Kansara |
| RCS-28305 | Stater Bros (Shenbagasundari Pilavadiyan) | Error al **subir** video | Camila Cortes |
| RCS-28331 | Sportsman's Warehouse | Error al **subir** adjuntos, se congela cerca del 49% | Viraj Kansara |

**Los tamaños reales del cliente están en la descripción del RCS-28331** y son el dato que faltaba en toda la discusión: 499.683 KB (~488 MB), 702.588 KB (~686 MB) y 78.457 KB (~77 MB). El usuario dice que se traba alrededor del 49% y ahí sale el server error. También probaron nombres de archivo más cortos, sin efecto.

**Lo que Juan validó el 13 ago**: txt, pdf y video en dos tenants distintos, Stater Bros y Sportsman's, lo más pesado 150 MB. Todo subió sin error. Diego Buelvas había hecho la misma prueba antes en Vitamin Shoppe con un txt.

**Por qué esa validación no cierra los tres tickets, y esto es lo importante:**

1. **150 MB está muy por debajo** de los 488 y 686 MB que reportó el cliente. Matt Kamminga contó que su prueba en el ambiente de test fue de **5 GB** y pidió "as big as you have got". El objetivo real es 1 GB.
2. **El RCS-28167 no es de subir, es de abrir.** Es descarga de ZIP grandes ya adjuntos. Ninguna prueba de upload lo toca.
3. **Producción tiene una capa que test no tiene**, que es Cloudflare cortando a los 100 segundos. Que test aguante 5 GB no prueba que producción aguante 700 MB con una conexión de tienda.

Camino de la ruta de adjuntos en la app: `.../nettrack/LPMS/ManageAttachments.aspx?SuspectID=&MasterCaseID=&ShopliftingID=&StoreIdent=`. Se llega desde el caso, y el flujo es Browse, Upload, Save All Changes. Convención de nombre para archivos de prueba, la de Diego: número de caso más `-testfile`.

Ver [[project_estado_abierto_2026_08_13]], [[reference_erms_lpms_descarga_pdf]], [[reference_waf_cloudflare_bloqueos]], [[reference_medir_lentitud_web_devtools]].
