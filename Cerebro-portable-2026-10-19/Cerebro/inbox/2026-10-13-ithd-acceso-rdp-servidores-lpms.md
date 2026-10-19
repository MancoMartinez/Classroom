Solicitud ITHD. Borrador para pegar, no enviado.
Fuente: Customer Server Profile, Confluence 474658570288, versión 64 del 6 de octubre, consultada el 13 de octubre de 2026. Incluye los once App Servers IIS. No incluye IZ Servers porque el acceso solicitado corresponde a logs de aplicación NetTrack. IT debe confirmar cuenta, dominio y alcance regional autorizado.
https://trebuco.atlassian.net/wiki/spaces/AALPS/pages/474658570288

Summary
RDP access to LPMS production application servers for Support

Description
Please enable my authorized Support account to connect from qa-lpms-rdp-001 to all application servers listed in Customer Server Profile: pd-lpms-iis-007, pd-lpms-iis-008, pd-lpms-iis-009, pd-lpms-iis-010, pd-lpms-iis-012, pd-lpms-iis-014, pd-lpms-iis-015, pd-lpms-iis-016, pd-lpms-iis-017, pe-lpms-iis-003 and pc-lpms-iis-003. Please confirm the required account and domain and grant the minimum RDP and file read permissions for client application logs. I already have Bastion access to qa-lpms-rdp-001. Connecting from there to pd-lpms-iis-008 as TREBU\jmartinez returns “The connection was denied because the user account is not authorized for remote login.”

Business Justification
As a Support Lead, I need to inspect Incident/Audit and NetTrack logs across client servers to investigate customer issues. The immediate need is Goodwill Sacramento, goodwillsacto, on pd-lpms-iis-008, for RCS-28915. Access to the full application server pool supports the same diagnostics for other clients. I require log reading only, with no administrative or production change permissions.
