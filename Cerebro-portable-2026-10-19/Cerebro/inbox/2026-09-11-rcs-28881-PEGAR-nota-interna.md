Internal note, RCS-28881. Context and what we need before anything goes back to the customer.

What the screenshot shows. The APIS navigation frame renders in full for Carlo Conty, including the Admin tab, while the content panel comes back empty. Session, authentication and location hierarchy are resolving. The failure is server side while rendering the audit form. This is not a platform outage and not a permission gate on this user.

Deployment matters here. NEXCOM is an on prem APIS customer, government, and we hold no access to their production data or servers. Only the nexcom-prep site is reachable from our side. Nothing we normally run for this symptom, a screen rebuild, a label cache reset or a database check, can be executed by Support on this tenant. Their Lead Applications Administrator, Milan Djordjevic, is the counterpart who can pull IIS and application logs. He worked RCS-28642 with David Beck on 28 August.

On the Meijer comparison. RCS-28449, Meijer, Secure not loading, was a Secure 5 platform issue restored by Engineering within 47 minutes on 18 August and tracked in the Secure 5 Issues channel. Different product, different hosting, different failure mode. It is not a precedent for this ticket.

Closer precedents, all on Secure rather than APIS, same failure shape. RCS-28139, Sportsman's Warehouse, all audit screens unreachable for all users, caused by BuildAllScreens running synchronously on the HTTP thread and hitting the 100 second edge timeout. RCS-28032, Vitamin Shoppe, NewAudit.aspx and AuditLog.aspx rendering with unresolved screen labels. RCS-28709, Stater Bros, intermittent blank screen, still without a confirmed root cause and without a linked ENG.

Working hypothesis, not confirmed. Carlo reported he was in the middle of updating the Annual Ops/Services Review template when it stopped opening. A form that fails to render only after an edit points at the saved definition of that template rather than at the environment.

What we need from NEXCOM to move this forward.
1. Whether other audit templates open normally for the same users. If they do, the issue is scoped to Annual Ops/Services Review.
2. What changed on that template on or before 10 September, and who saved it.
3. IIS and application event logs from their APIS server for 10 September around 16:46 Eastern, plus the browser console and network trace captured while the blank page loads.
4. Clarification on the second symptom. The email states that users cannot create support cases. We need to know whether that means case entry inside APIS or the Appriss Retail Support portal, since RCS-28881 itself was created through the portal without trouble. If it is case entry inside APIS, the scope is wider than one template and we should treat both symptoms as one incident.

One constraint to set expectations internally. APIS is a legacy product with no ongoing development. If this turns out to be a corrupted template definition and we have no access to their environment, the practical path is for NEXCOM to restore the previous version of the template from their own backup.

Ownership. APIS came back to Support on 8 September. Megha Rathi holds this ticket and already owns RCS-28212 on the same product.
