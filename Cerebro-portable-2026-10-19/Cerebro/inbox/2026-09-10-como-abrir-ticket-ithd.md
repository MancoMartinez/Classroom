# Como se abre un ticket interno para IT en Appriss

Consulta del 10 sep 2026. No es un ticket de cliente. Ruta distinta a RCS.

## Que aplica

El IT Help Desk de Appriss es un proyecto de Jira Service Management propio, con portal de cliente.
No se crea en RCS y no se asigna a una persona. IT lo toma de la cola y el aprobador se contacta
solo cuando la solicitud lo exige.

Portales equivalentes:
- https://trebuco.atlassian.net/servicedesk/customer/portals
- http://support.apprissretail.com/
- https://help.apprissretailcloud.com/
- Telefono de respaldo 502-657-5285

Tambien esta enlazado en el menu Company links del navegador de trabajo.

## Categorias del portal

- Common Requests para incidencias rapidas.
- Computer Hardware para equipo.
- Applications / Software para software, items y accesos.
- Account / Access Requests -> Access Change para cambios de permisos sobre un recurso existente.
- Requests para hacerle seguimiento a lo ya abierto.

## Que exige el ticket

Escribe siempre Business Justification. InfoSec la revisa y sin ella el ticket se devuelve.
Nombra el recurso exacto: grupo de AAD, VM con su resource group y subscription, tenant, o
aplicacion. Lista los usuarios afectados con nombre y correo. Si un lider ya aprobo, ponlo en el
cuerpo. IT verifica con esa persona.

Ejemplo verificado del acceso a Bastion:
Summary: Access Change - Bastion access to QA-LPMS-RDP-001 (approved by J.R. Teagle)
Description: VM QA-LPMS-RDP-001, RG qa-lpms-uswest2-rg, sub 21723631-8442-4e6b-818f-562f2251d8be,
lista de usuarios, pedir alta en el grupo AAD qa-lpms-rdp_Reader_Bastion_Access y creacion de las
cuentas LPGUYS.NET con rol AAA-ROLE-CLIENT_SERVICES.

## Lo que no pasa por ITHD

1Password sale por autoservicio en https://myaccess.microsoft.com/. El acceso basico lo aprueba el
Security Architect en un dia habil. El vault especifico lo aprueba el manager.

## Precedentes en Confluence

- Space ITHD: "How to Submit a Ticket", "Requesting access to 1password", "Jira Service Management
  project - watchers and request participants", "Moving Your Claude Account to apprissretail.com".
- Space RTS: "New L1 Team Member Onboarding Access", "New L2 Team Member Onboarding Access",
  "How to Open a Ticket in JIRA: Steps and Guidelines", "GitHub Desktop".
- Space ARIT: runbook del lado de IT, "Provide Azure Access", "User Login Process" de Snowflake.
- Cerebro: brain/markdown/13-appriss-onboarding-base-de-conocimiento.md, seccion de acceso a
  QA-LPMS-RDP-001.

## Pendiente

Falta el asunto concreto del ticket que Juan quiere abrir. Con el tema se redacta el Summary, la
Description y la Business Justification en ingles, listos para pegar en el portal.
