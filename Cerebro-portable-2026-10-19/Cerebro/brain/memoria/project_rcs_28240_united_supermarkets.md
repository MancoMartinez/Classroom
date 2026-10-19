---
name: project_rcs_28240_united_supermarkets
description: "RCS-28240 United Supermarkets: el SSO del entorno de test lleva parado desde abril de 2026 esperando que Albertsons actualice su IdP"
metadata: 
  node_type: memory
  type: project
  originSessionId: 2b736553-ea91-4441-bf59-40e05f44211f
  modified: 2026-08-13T18:27:07.143Z
---

**RCS-28240**, "United Supermarkets <> Appriss Retail Platform Unification Announcement | Appriss Incident Update Requested". Medium, *Under Support Review*, **asignado a Camila Cortes**, no a Juan. Labels `FromEmail`, `L1`. Reporter Emma Gomez (Albertsons).

**No es un bug, es un handshake de configuración que nadie completó.** United Supermarkets está a medio migrar de `lpguys.net` al dominio unificado. El login SSO/SAML del entorno de test falla en `test.apprissretail.com/unitedsupermarkets/signin/sso/saml2`. Marcus Young lo reportó y sigue fallando en incógnito y con caché limpia.

**La cadena, que es lo que explica el ticket:** el fallo salió en **abril de 2026**. Matt Kamminga pidió el 17 de julio que el equipo SSO del cliente confirmara que agregaron el nuevo ACS URL y actualizaron el Unique Identity URL. Marcus dijo que no tiene acceso, Emma escaló internamente, David Smith metió a Lakshmi Priya Nair y Greeshma George de Albertsons, y **nadie confirmó nunca si el cambio se hizo**. Kurt Kleist, que era el contacto histórico de SSO, ya no está. Emma escaló a Support el 7 de agosto, después de pedir dos veces que alguien tomara esto.

**Trampa concreta**: los valores del ACS URL y del Unique Identity URL **no están en el texto del ticket**, se perdieron al convertir la cadena de correos a Jira. Sin esos dos valores no se le puede pedir nada accionable al equipo de Albertsons. Hay que sacarlos de Control Panel o pedírselos a Matt.

**El paso que destraba esto** es mirar el SSO Response Log del tenant `unitedsupermarkets` en Control Panel: si los intentos de Marcus aparecen, el problema es nuestro mapeo; si no aparecen, el IdP de Albertsons nunca respondió y el bloqueo es de ellos, con evidencia. Método completo en [[reference_sso_incident_diagnostico]].

Otros nombres del hilo: Sofia Sandner (Transformation PM, la que derivó a Support), Kathleen Garner (CSM, coordina la ventana de cutover a producción), Robin Ursenbach.

Ver [[reference_unificacion_patrones]], [[reference_ficha_clientes_onboarding]].
