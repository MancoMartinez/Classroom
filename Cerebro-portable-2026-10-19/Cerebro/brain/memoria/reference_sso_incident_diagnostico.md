---
name: reference_sso_incident_diagnostico
description: "Cómo diagnosticar un fallo de SSO/SAML en un tenant de Incident: el SSO Response Log es el discriminador que dice de qué lado está el problema"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 2b736553-ea91-4441-bf59-40e05f44211f
  modified: 2026-08-13T18:26:30.630Z
---

Fuente: **"SSO Training Guide Summary"**, Confluence espacio RTS, página `477557096452`.

**El discriminador, y es el primer paso siempre.** En Control Panel cada cliente tiene dos pestañas de SSO:

- **SSO Tab**: la configuración del handshake, incluido el mapeo de campos del claim.
- **SSO Response Log**: el registro de **cada claim recibido en cada intento de login**, simplificado a los elementos que Appriss usa.

Con eso el caso se parte en dos sin adivinar nada:

- Si los intentos del usuario **aparecen** en el Response Log, el IdP del cliente sí está respondiendo y el problema está en nuestro mapeo. Se mira la pestaña SSO.
- Si **no aparece nada**, el claim nunca llegó, y entonces es el ACS URL o el Entity ID del lado del cliente. Ahí no hay nada que arreglar de este lado y pedirlo por correo otra vez sin esta evidencia no mueve el ticket.

**XML crudo del claim**: New Relic, filtrando por `Category LIKE '%SAML%'`. Ahí se ve si es audience mismatch, ACS mismatch o certificado.

**Mapeo de campos del cliente**: repo `arpfiles` en Azure DevOps, archivo de configuración SSO del cliente. Sirve para comparar contra lo que llega.

**El claim mínimo obligatorio** son nombre, apellido y email. Ubicación y grupos son opcionales; cuando no vienen, el cliente los gestiona en un HR externo o a mano.

**La bandera `Persistent` en el SSO Portal** dice cómo se provisionaron ubicaciones y grupos: `TRUE` vino de un import de archivo, `FALSE` se puso a mano. Solo 1 de cada 5 clientes automatiza esto. Ojo con un `TRUE` de fecha vieja, puede ser una carga masiva única de hace años y no un pipeline vivo.

Relacionado: [[reference_control_panel_admin]], [[project_rcs_28240_united_supermarkets]], [[reference_configuration_items_features]].
