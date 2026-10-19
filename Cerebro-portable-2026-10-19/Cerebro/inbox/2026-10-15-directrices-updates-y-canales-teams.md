# Directrices de updates y canales de Teams (15 oct 2026)

Fuente: mensajes de Teams en Retail Ops, canal Data Issues, y el hilo de Viraj Kansara con J.R. Teagle. Origen declarado: instrucciones directas de Ripp. El post de RCS-28966 lo publicó Chris Rippingale.

## Regla 1: pide ayuda en el canal, no en un grupo
Si dependes de otro equipo, publica la petición o la pregunta en el canal que le corresponde. No crees un grupo ni un chat privado. Si ya existe una conversación privada, muévela al canal público. Ripp la considera ocultar problemas en curso.

Canales (equipo Retail Ops):
- SnowTime y problemas de datos: Data Issues
  https://teams.microsoft.com/l/channel/19%3A083fa3a1a2db45d693886b2e844a1d1e%40thread.tacv2/Data%20Issues?groupId=251a274e-8105-4474-9da9-bbacfce8f037&tenantId=00646d1d-3d1b-48b6-bb60-e85055107d85
- Incident Product Line: AALPS Issues
  https://teams.microsoft.com/l/channel/19%3Ad3b0ee0652e64b87a253d54ba3252810%40thread.tacv2/AALPS%20Issues?groupId=251a274e-8105-4474-9da9-bbacfce8f037&tenantId=00646d1d-3d1b-48b6-bb60-e85055107d85
- Secure Product Line: Secure 5 Issues
  https://teams.microsoft.com/l/channel/19%3Acd60b7a0a347493cbd0a67f14d8e26bb%40thread.tacv2/Secure%205%20Issues?groupId=251a274e-8105-4474-9da9-bbacfce8f037&tenantId=00646d1d-3d1b-48b6-bb60-e85055107d85
- Engage Product Line: Engage Issues
  https://teams.microsoft.com/l/channel/19%3A9c9525a8a21f4d7da321f003f2faf3e5%40thread.tacv2/%F0%9F%9A%A8%20Engage%20Issues?groupId=251a274e-8105-4474-9da9-bbacfce8f037&tenantId=00646d1d-3d1b-48b6-bb60-e85055107d85

## Regla 2: cadencia de updates al cliente
- Ticket propio: update cada 2 business days.
- Ticket que pasa a Engineering: update semanal. Se sigue informando aunque el dueño sea otro.
- L2/Data aplica lo mismo. El proceso para el caso Engineering sigue abierto. Implica filtros o grupos nuevos en Jira para tickets donde nuestro equipo es el assignee original y el dueño actual es otro. Ripp pidió un voluntario. Nadie lo había tomado en los mensajes que Juan pegó.

## Caso de referencia: RCS-28966
ICA, duplicate promotion/tender records. Abierto desde el 17 sep 2026. El cliente ya encontró el problema por su cuenta. Ripp exigió discutirlo en Data Issues y preguntó qué hace falta para cerrarlo hoy.
https://teams.microsoft.com/l/message/19:083fa3a1a2db45d693886b2e844a1d1e@thread.tacv2/1792058518084?tenantId=00646d1d-3d1b-48b6-bb60-e85055107d85&groupId=251a274e-8105-4474-9da9-bbacfce8f037&parentMessageId=1792058518084&teamName=Retail%20Ops&channelName=Data%20Issues&createdTime=1792058518084

## Cómo se mide el cumplimiento
Viraj Kansara preguntó si Jira tiene un reporte o fórmula para saber si se envían updates a tiempo.
- J.R. Teagle tiene en su manager dashboard el filtro "no reply 5 business days". Los números son clicables y abren los tickets exactos.
- J.R. puede bajar el umbral a 3 business days. Con la regla de 2 días el umbral actual queda flojo.
- J.R. compartió una versión nueva del scorecard en Support Management (Teams). Viraj lo actualiza a V5.6.

## Uso en tickets futuros
- Antes de abrir un chat o grupo para pedir ayuda, busca el canal de la tabla y publica ahí.
- Pon recordatorio de update cada 2 business days en cada ticket propio. Pasa a semanal cuando el ticket entre a Engineering.
- Verifica en Jira la fecha del último comentario público antes de afirmar que el update está al día. Jira manda sobre cualquier ficha.
- Pendiente sin confirmar: umbral final del dashboard de J.R. y quién toma el filtro de tickets con dueño en Engineering.
