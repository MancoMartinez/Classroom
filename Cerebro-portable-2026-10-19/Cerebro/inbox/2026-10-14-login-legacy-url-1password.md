# Procedimiento de login en clientes legacy con credenciales de 1Password

Fecha: 2026-10-14.
Autor: Antigravity.
Propósito: Documentar la modificación de URL para ingresar a portales legacy evitando el SSO corporativo del cliente.

## 1. Problema

Los tenants legacy alojados en apps.lpguys.net redirigen por defecto al proveedor de identidad corporativo del cliente cuando tienen configurado SSO. La URL estándar index.aspx impide el uso directo de las cuentas genéricas o de supervisor almacenadas en 1Password.

## 2. Modificación de la URL

Agrega el parámetro ?nosaml=1 al final de la ruta del portal NetTrack:

https://apps.lpguys.net/<slug>/nettrack/index.aspx?nosaml=1

El parámetro desactiva la redirección SAML del cliente y despliega el formulario estándar con campos de usuario y contraseña.

Variante documentada para entornos de prueba:
https://test.lpguys.net/<slug>/nettrack/?nosaml=1

Variante para autenticación interna de Appriss (solo si el tenant tiene ApprissSAML=1):
https://apps.lpguys.net/<slug>/nettrack/index.aspx?APSAML=1

## 3. Ubicación de credenciales en 1Password

* Vault: LPMS - Tenant Databases.
* Criterio de búsqueda: nombre del cliente, slug o nombre comercial.
* Nombre de registro típico: <Cliente> - Supervisor o entradas con el código de tenant.

## 4. Fuentes verificadas en Cerebro

* inbox/2026-10-06-rcs-29195-guia-diagnostico.md: líneas 40-45.
* inbox/2026-10-07-talos-evidencia/lecturas-seleccionadas.txt: línea 3151.
* inbox/2026-10-08-rcs-29338-pasos-detallados.md: línea 3.
