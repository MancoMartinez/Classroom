Addendum para RCS-28556, tras el comentario de Joe Austin del 2026-08-28 08:51 EDT. Pegar como
comentario nuevo, no editar el del 26 de agosto. Formato Jira completo, en ingles, sin corte de
linea dentro de cada bloque.

================================================================================
BLOQUE 1. Comentario interno de escalacion, para pegar en RCS-28556
================================================================================

## 1. Customer confirmation closes the ambiguity

Vitamin Shoppe's own network team reviewed the block page and concluded the block is on the Appriss side, not theirs. Their stated reasoning: "Had this been a block on our side, you'd be seeing either a Zscaler or Defender block page." That statement is technically correct and it resolves the open question from section 5 of the prior comment. Zscaler passed the request through. The Appriss Cloudflare perimeter rejected it on arrival. The fix lives entirely on our side. Path B, the customer pinning Zscaler egress, is no longer a candidate. Move to Path A only.

## 2. On "none of these issues were occurring until the most recent upgrade"

Joe Austin's statement is accurate and it names the real trigger. The new URL scheme moved sign in traffic onto `apps.apprissretail.com`, which sits behind the Cloudflare default deny perimeter described in section 5 of the prior comment. That perimeter did not exist on the legacy URL. This is not a session or authentication reconciliation issue. It is a country rule on a perimeter that is new since the migration. State it in exactly those terms if this reaches the customer. Do not use the word migration alone without naming the mechanism, that phrasing is what produced the false explanation on RCS-28175.

## 3. Escalation, not queue

This ticket qualifies for direct escalation over the standard Infrastructure queue. Three tickets carry the identical mechanism and only one, RCS-28059, has closed. The customer's own IT team has now documented and forwarded the diagnosis. Waiting on a general Infrastructure review cycle repeats the seven week delay already on this tenant.

Contact Matthew Kamminga directly. He filed the arpfiles PR that closed RCS-28059 on 2026-07-31. Reference that PR and this ticket's Ray ID and IP in the same message. Do not route this to Kiran Vadday. Kiran's recent work on this tenant, ENG-6587, is an Incident platform defect under Unification_Jul_26, a case save failure unrelated to Cloudflare or WAF rules. He has no console access to Security Events and no context on country allow lists.

## 4. Message to send Matthew Kamminga, outside Jira

```
Matt, need the same fix you shipped for Ahold on RCS-28059, this time for Vitamin Shoppe.
Client 433, apps.apprissretail.com/vitaminshoppe.
Ray ID a304809aba495425, client IP 136.226.130.207, same /24 as the Ahold case, ZSCALER-YTO3.
Customer's own network team confirmed this is our Cloudflare blocking, not their Zscaler or Defender.
Need allow-countries updated for vitaminshoppe the same way it went for ADUSA on 7/31.
Ticket is RCS-28556. Can you raise the PR today.
```

================================================================================
BLOQUE 2. Transicion recomendada
================================================================================

561 Escalate Ticket, a Escalated.

No 461 Waiting For Infrastructure. Esa transicion asume que la cola normal de Infra la toma. Con
tres tickets del mismo tenant y evidencia entregada por el propio cliente, la cola normal ya fallo
una vez. 561 marca el ticket como fuera del flujo estandar y deja registro de que se escalo por
fuera del canal habitual, que es lo que el mensaje directo a Matthew hace en paralelo.

================================================================================
BLOQUE 3. Nota para Juan, no va en Jira
================================================================================

No hay ticket nuevo ni similar que no conocieramos ya. Lo que cambia es que el propio cliente
certifico el lado del bloqueo, y eso quita la ultima duda que quedaba abierta en la investigacion
del 26 de agosto, seccion 7, item 2.

Sobre Kiran. No es la persona. Verificado en ENG-6587: es ingeniero de aplicacion en defectos de
Incident bajo Unification_Jul_26, no toca Cloudflare ni WAF. Pregunta rapida a Matthew Kamminga,
no a Kiran.
