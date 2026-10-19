RCS-28223, McDonald's. Mensaje para Teams, Engineering Chat.
Contexto, Kiran Vadday (bvadday) tampoco tiene acceso a App Insights, al ver el detalle del error dijo "Ah.. Thats new" y pidio postearlo en el chat de Engineering.

Correccion de tono, 1 oct
La primera version sonaba a orden, listaba hallazgos y cerraba con "who can pull it", como una tarea asignada. Esto es una consulta de ayuda, Juan y Kiran estan atascados sin acceso. Reescrito para pedir orientacion, no instruir.

Texto para pegar en Teams

Could use some help on RCS-28223, McDonald's. https://trebuco.atlassian.net/browse/RCS-28223

Two store accounts cannot log in with their regular password, and the failure point is different for each one, so we are not sure yet if it is one issue or two.

NSN 14283, Sep 29 around 1:09 PM PST. Host apps.apprissretail.com, path /mcdonalds/signin, landing on systemselect.aspx. Password submitted is the one they always use, response is There has been a system error. Please contact support. No invalid password message, no WAF block page.

NSN 930, same day around 12:03 PM PST. Stops at the email entry step, no error shown, just does not move forward.

On our side, membership.Users and incident.LPUser2 for NSN 14283 both look clean, no lockout, no identity mismatch, so it does not look like a DB issue.

One thing we noticed, maybe unrelated, the 14283 URL lands on systemselect.aspx, same entry point flagged in RCS-28321 before that theory was discarded in RCS-28984. Just flagging the coincidence, not saying it is the cause.

Kiran and I were hoping to check App Insights, appi-prd-wus2-arp, role web-prd-wus2-arp-yarp, around 19:03 and 20:09 UTC on Sep 29, but neither of us has access to that resource. Would appreciate any pointers on who might be able to pull that trace, or another angle we are missing.
