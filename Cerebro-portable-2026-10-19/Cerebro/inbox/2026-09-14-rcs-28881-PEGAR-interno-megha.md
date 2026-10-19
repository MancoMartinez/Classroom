Internal note for Megha. Handoff so you can pick this up at the start of your shift.

I posted a customer update on this ticket and asked Carlo two questions. Carlo had heard nothing from us since the auto acknowledgement on the 10th, so the update was mainly to stop the silence. I did not commit to any cause or any date.

What I asked him. Whether Annual Ops/Services Review still appears in Audit admin, Templates, once the filter that hides expired and deleted templates is turned off, and what the last two columns read next to it. And whether any other template in that same list opens for him.

What I did on my side today. I worked the tenant in the prep environment with the shared account and walked the Audit module end to end. Audit Center, an individual audit, the Audit admin tab, and the template editor for OPS Review Administration, template AT1000000106, all render normally with their tabs, forms and change history. The Audit module itself is not the failure point for this tenant. Annual Ops/Services Review does not exist in prep, so there is no exact reproduction to be had there, and turning off the expired and deleted filter revealed no hidden templates.

Two things worth your attention. The template editor loads a form reference by ID in its Forms section, in the case I opened it read OPS Review - Administration( ID:361 ). If that reference went inconsistent in production while Carlo was mid edit, the editor failing to render is consistent with what he is describing, and it explains why one template fails and the rest do not. Treat that as a working read, not a cause. The second one is that screen label keys come back unresolved across every Audit screen in that tenant, Audit.status.1, Audit.date due, Letter.actions, Form status.0, Template deleted.0, Audit.template code. Same shape as RCS-28032 at Vitamin Shoppe.

Deployment constraint, in case it has not come up. NEXCOM is on prem and government, and we hold no access to their production data or servers. A screen rebuild, a label cache reset or a database check are not things Support can run on this tenant. Their Lead Applications Administrator is Milan Djordjevic, who worked RCS-28642 with David Beck on 28 August, and he is the counterpart for anything that needs server side logs.

Where I would take it next. If Carlo comes back saying the template shows as expired or deleted, the path is for NEXCOM to restore their previous version, since APIS carries no ongoing development. If it shows as normal and other templates open for him, the next ask goes to Milan for IIS and application logs around 10 September, 16:46 Eastern.

The ticket stays with you. Ping me if you want me to take any of it.
