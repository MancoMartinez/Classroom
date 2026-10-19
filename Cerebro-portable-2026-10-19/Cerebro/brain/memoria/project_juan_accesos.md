---
name: project-juan-accesos
description: Accesos y herramientas que Juan ya tiene en Appriss — no asumir que le faltan ni sugerir pedirle permisos a otros.
metadata: 
  node_type: memory
  type: project
  originSessionId: 9fc04b4a-14c1-4cb0-b5b5-97ac10fcabe5
  modified: 2026-07-30T17:21:24.840Z
---

Juan **ya tiene** estos accesos. No sugerir que los pida ni que otro corra las cosas por él:

- **Control Panel** (`usprod.apprissretailcloud.com/control`), entorno **USPROD**, roles `SupportL2` + `Engineers`. Incluye Hatr → Trigger Task (p.ej. `System: ReferenceDataBackLoadIncidentOnly`), Ops Overview, WISC, Logs, Incident Logs, Search Stats, Sidekick, Returns Portal, y bajo Engineering: Alerts, Arp Files, Global Config, Config Items, Enumerations, Feature Flags.
- **Bases de datos SQL Server** de producción, con credencial de **lectura y de escritura separadas** — si una query falla o sale vacía sin razón, verificar primero con qué rol está conectado. Acceso vía máquina de salto (bastion o `DEVWUS2DSM01`, nombre de host Windows, no recurso de Azure).
- **Snowflake** y **SnowTime**.
- **Azure Portal** con RBAC limitado: solo ~14 VMs, `Retail-LPMS-Test` y parte de `Retail-Secure-P*`. Las máquinas de dev/prod de otras suscripciones no le aparecen.

- **APIS**. Prep en `https://apis-uat.apprissretailcloud.com`, se reconoce por "uat" en la URL.
  Prod en `https://apis.apprissretailcloud.com`. El login pide tres campos: company ID, usuario y
  clave. Company ID confirmado con acceso: `jcrew-prep`. Usuarios `jmartinez` y `jbarber`, la
  segunda es la cuenta compartida de Julie Barber que sigue activa pese a que ella ya no esta.
  La clave la paso Kristin Krogman por chat el 2 jul 2026 a las 12:34, no se escribe aqui, va en
  el 1Password de Juan. Un company ID por tenant, asi que el acceso a `jcrew-prep` no da entrada
  a `nexcom-prep` ni a ningun otro. El alta por tenant la pide Matt Kamminga o Ryan Barlow.
  Primer login puede rebotar en Cloudflare, se reporta a IT.

**Dos datos útiles del Control Panel:** la tabla *Customers in USPROD* tiene columna **Time Zone por cliente** (relevante para bugs de hora post-migración), y la primera columna es *"Click logo to sign in"* — esa es la vía de acceso de soporte a un tenant, no `/<slug>/signin`, que redirige al SSO del cliente donde su usuario de Appriss no existe. Alternativa non-SAML: `?admin=true` al final de la URL de signin.

Relacionado: [[project-appriss-support-role]], [[project-flujo-tickets]]
