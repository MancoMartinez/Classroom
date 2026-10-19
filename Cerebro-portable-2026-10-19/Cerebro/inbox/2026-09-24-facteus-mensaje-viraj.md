Viraj, sharing the full picture on Facteus ahead of tomorrow so we can go straight to your read on it during the call. This covers what Chris sent, what I confirmed directly in Jira and Confluence today, and the open points worth deciding together.

BACKGROUND

Chris Howard sent the support documentation for the Facteus handover and asked for feedback. Camila asked the team to review and reply to that thread, and moved the deadline up twice, the last one being tomorrow. The same day Camila sent that reminder, Chris posted in ENG-6450 that he had chased JR for a response on the access request. Two separate signals landing on the same day, worth keeping in mind for tone tomorrow.

Worth noting for context, not as anything to sort out tonight. Back in the June 4 shadowing meeting, Camila put you and me down as the two owners of Snowflake access follow ups while she was out, and there was already an IT ticket open at that point. That thread never closed. It is the same category of request as the one blocking Facteus now, so it is probably worth deciding together whether we treat this one differently this time.

ACCESS, THE ITEM CURRENTLY BLOCKING THE HANDOVER

RETAILDB-2972, Facteus Access For Support Team, is Open, unassigned, zero comments, created by Chris on September 16. It requests read access to PRODDATACLOUD.FACTEUS_CONFIG, PRODDATACLOUD.FACTEUS, and FACTEUS_DATASHARE, plus ARDM_PRODUCTION and ARDMPROD if not already granted.

Chris also referenced ITHD-9247 in a comment on ENG-6450 from September 16, describing it as the access request already created. I could not open ITHD-9247 from my account, Jira returns no permission or no such issue. I cannot tell if that is the same request as RETAILDB-2972 under a different portal number, or a second, separate request nobody is tracking. If you have visibility into the IT Help Desk portal, checking that is probably the single most useful thing to sort out before we reply to Chris, because it changes who we tell him owns this.

Once that is clear, we should decide whether one of us takes RETAILDB-2972 as the named owner this week, given the June decision put both our names on this category of request.

WHAT'S ALREADY WORKING, NO NEED TO RE-LITIGATE

Two dashboards already exist and answer the request to link a dashboard to every alert. A Grafana dashboard at apprissretail.grafana.net/goto/svsg2j with its alert condition configured, and a console dashboard Saddam built at prd-datacloud-console-app-wus2.azurewebsites.net. Neither shows up from the Confluence pages directly, Chris left both links only as comments on ENG-6450. Worth checking with him whether either one has actually been exercised against a real alert yet.

Chris's own comment on ENG-6450 from September 15 lists the original call notes as a checklist. Marked done on his side, triage information in the ticket, the missing data ticket detail, the decision tree, defining INTERNAL, defining EXTERNAL, the Facteus contact list, and the dashboard link. Still open on his side, the access requirements, and sending the follow up email with feedback, which is the exact thing we are being asked to do now.

PROCESS DESIGN QUESTIONS WORTH RAISING WITH CHRIS

The Missing Clients page sets a 26 hour staleness window on _row_created, and references a drop_ratio value without defining the threshold that should trigger escalation versus one Support can note and move on from. Worth asking Chris to spell out the number.

The internal alert process expects Support to try to resolve smaller issues before escalating. The external process, a direct email from Facteus, routes everything to Data Engineering with no path for Support to close anything on its own. Worth asking Chris directly what, if anything, Support is expected to resolve independently, and what the closure criteria look like when Support ever gets to be the one closing a ticket. A named technical owner and backup on the Data Engineering side would also help, right now the ticket only lists Chris Howard, Nicholas Turner, and Saddam Hussain as a group with no clear escalation order.

SLA AND SCHEDULE

The Requirements Specification, section 5.3, states Facteus gets notified within one hour of an error and either a fix or a detailed update within 24 hours. The operational pages Chris wrote set the internal expectation at one business day, weekdays only, with no stated weekend coverage. ENG-6450 itself has Chris's own note from July that SLAs had not yet been discussed with Facteus specifically and that JR should be looped in if that conversation happens. Worth getting a straight answer from JR on which commitment is the one actually in force, and whether weekend coverage exists for Facteus specifically or only for the general Data Issues category in the OpsGenie guide.

Separately, there is a plain scheduling mismatch. The Requirements Specification, section 5.1, states the process runs at 01:00 UTC. The Process Not Run Within 24 Hours page states it runs at 00:00 UTC. Worth flagging to Chris as a simple factual check, not a bigger issue.

HANDOVER TIMING

ENG-9367, Handover Support Process, was opened today, still in Backlog, targeting the October sprint. Its description covers internal Grafana alerts and direct emails to support@apprissretail.com. That session is probably the right place to actually test the decision tree end to end, run one real internal alert and one real external email through the process, and confirm the out of hours path, rather than signing off on paper before any of it has been exercised live.

WHAT I'D LIKE YOUR READ ON TOMORROW

Whether ITHD-9247 is the same request as RETAILDB-2972, and if you can check that from your access before we reply.

Whether we name one owner for the access ticket this week or keep sharing it.

Whether the process design questions above are the right ones to send back to Chris, or if I am missing context you have that changes the read.

Whether we ask for a dry run inside ENG-9367 before calling the handover complete, or whether that is asking for more than the October timeline allows.

Sources
RETAILDB-2972: trebuco.atlassian.net/browse/RETAILDB-2972
ENG-6450: trebuco.atlassian.net/browse/ENG-6450
ENG-9367: trebuco.atlassian.net/browse/ENG-9367
Requirements Specification: trebuco.atlassian.net/wiki/spaces/DS/pages/477211557894
Process, Internal Alerts: trebuco.atlassian.net/wiki/spaces/DS/pages/478102126595
Process, Issue Reported By Client, External: trebuco.atlassian.net/wiki/spaces/DS/pages/478101897217
Missing Clients: trebuco.atlassian.net/wiki/spaces/DS/pages/478182932484
Process Not Run Within 24 Hours: trebuco.atlassian.net/wiki/spaces/DS/pages/478183063566
Grafana dashboard: apprissretail.grafana.net/goto/svsg2j
