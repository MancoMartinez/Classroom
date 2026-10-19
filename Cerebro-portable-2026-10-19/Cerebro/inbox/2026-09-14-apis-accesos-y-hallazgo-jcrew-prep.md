---
fecha: 2026-09-14
autor: Claude
tema: accesos APIS confirmados, y el panel en blanco reproducido en jcrew-prep
ingerir_en: 27 Cerebro
---

# Accesos APIS, confirmados con captura

Prep: `https://apis-uat.apprissretailcloud.com`. Prod: `https://apis.apprissretailcloud.com`.
El login pide company ID, usuario y clave. Company ID con acceso confirmado: `jcrew-prep`.
Usuarios `jmartinez` y `jbarber`. La clave la paso Kristin por chat el 2 jul 2026 12:34 y vive en
el 1Password de Juan, no en Cerebro.

Un company ID por tenant. `jcrew-prep` no abre `nexcom-prep`. El alta por tenant la pide Matt
Kamminga o Ryan Barlow.

Ficha actualizada: `brain/memoria/project_juan_accesos.md`.

# Hallazgo que toca RCS-28881

La captura de jcrew-prep del 14 sep muestra el mismo patron que la de NEXCOM. Menu izquierdo
completo, "Case Information" resaltado en naranja, panel derecho completamente en blanco.
Otro tenant, otro hosting, hosted contra on-prem, mismo dibujo en pantalla.

Esto NO confirma nada todavia. Un dashboard vacio en un ambiente de prep sin data no es lo mismo
que un formulario de audit que no abre en prod. Case Information es un dashboard, Annual
Ops/Services Review es un template de audit.

La prueba que separa las dos cosas se puede correr hoy y no necesita a NEXCOM. En jcrew-prep,
Audit Section, Audit Center y View Audit, abrir un audit existente en modo edicion.

- Si abre normal, APIS rinde formularios de audit bien y el problema vive en NEXCOM. Sigue la
  hipotesis del template corrupto y toca pedirle a Milan los logs.
- Si sale en blanco igual, la hipotesis del template se cae. Seria APIS, y el alcance pasa de un
  cliente a los quince clientes APIS activos. Eso cambia la prioridad del ticket y deja de ser de
  Soporte solo.
