---
name: reference_erms_lpms_descarga_pdf
description: "Causa raíz de las fallas de descarga de PDF: el módulo ERMS sube los archivos al directorio lpms"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 8b73134e-5723-4d74-be14-e59eb99f9e25
  modified: 2026-08-11T16:26:20.027Z
---

Causa raíz confirmada por Kiran Vadday en Teams el 10 ago 2026, sobre RCS-28124.

El módulo **ERMS sube los archivos al directorio de lpms**, y por eso la descarga después falla. Mitigación inmediata: Kiran copia los archivos al lugar correcto. Arreglo de código en `release` y en `main`, con cherry-pick al historial de release.

Encaja con lo que Juan había observado el 4 ago: en ADUSA, 7 de 7 archivos de Stop & Shop descargaban bien y 12 de 12 de las otras marcas fallaban con `ERR_RESPONSE_HEADERS_MULTIPLE_CONTENT_DISPOSITION`. Es la misma familia de problema, el archivo no está donde el descargador lo busca.

Cuando vuelva a aparecer una falla de descarga de PDF, la primera pregunta es por qué módulo se subió el archivo.
