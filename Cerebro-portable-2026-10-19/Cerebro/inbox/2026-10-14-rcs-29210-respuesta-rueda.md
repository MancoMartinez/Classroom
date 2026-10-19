RCS-29210. Goodwill Central Coast. Revisión 14 octubre 2026.

Qué pasa
Rueda investigó en goodwillcc, servidor pd-lpms-uswest2-sqldb-001.database.windows.net. No encontró conexión en sqlmi-prd-wus2-arp-001-production.d4f7681860d3.database.windows.net.

Causa y límites
Confluence respalda la ruta legacy: goodwillcc aparece en node-h, pd-lpms-iis-009, sin asterisco de DB only migration. No inspeccioné conexión activa, base ni logs. La hipótesis temporal del score permanece abierta; LastEdited no prueba qué cambió. Verificar política de reenvío de esta alerta.

Evidencia
Customer Server Profile 474658570288, versión 64 del 6 octubre, leído hoy: goodwillcc en node-h; asterisco significa base Platform y goodwillcc no lo tiene.
Client URLs 474930806894: https://apps.lpguys.net/goodwillcc/nettrack/ y pd-lpms-iis-009.
Antecedente Kiran y Diego, 6 octubre, RCS-29195: Manasota legacy, investigación SQL; no prueba causa común. Sacramento usa node-g, pd-lpms-iis-008. Juan recibió rechazo RDP allí el 9 octubre; no acredita permisos de Rueda.

Qué hago hoy
Continuar lectura SQL legacy para AuditMasterStoreID 63055. Revisar Change History y Alert History. Para archivos de logs, entrar por Bastion a qa-lpms-rdp-001 y conectar al IIS pd-lpms-iis-009 con cuenta autorizada. Comprobar F:\IIS\Clients\goodwillcc\nettrack\logs; ruta derivada del patrón, existencia sin verificar. Buscar goodwillcc o Goodwill Central Coast en 1Password para identificar credenciales aplicables. Confirmar con Kiran, Ryan o IT cuenta y permisos si falta acceso. Ubicación específica de logs HATR pendiente.

Precedentes
inbox/2026-10-06-rcs-29195-guia-diagnostico.md
inbox/2026-10-09-acceso-bastion-nettrack-logs.md

Compromisos
Borrador no enviado. Sin ETA ni causa confirmada del score.

Respuesta pegable
Sebastian, sí tiene sentido la base que usaste. Confluence lista goodwillcc en node-h, servidor pd-lpms-iis-009, sin la marca de migración de base a Platform. Eso respalda continuar en la base legacy que ya consultaste.

Para revisar logs, el servidor de aplicación es pd-lpms-iis-009. Desde qa-lpms-rdp-001 por Bastion, comprueba la carpeta F:\IIS\Clients\goodwillcc\nettrack\logs. Busca las credenciales correspondientes en 1Password; el acceso a Bastion no garantiza permiso al IIS. Si te rechaza, confirma cuenta, dominio y permisos con Kiran, Ryan o IT. Falta confirmar dónde registra HATR esta alerta.
