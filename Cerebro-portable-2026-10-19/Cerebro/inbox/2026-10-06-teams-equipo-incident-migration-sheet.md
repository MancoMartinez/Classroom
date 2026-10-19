# Teams al equipo, hoja Incident Migration 2026, ingles. Copiar desde el chat para conservar negritas

Hi team, sharing the **Incident Migration 2026** sheet (attached). Please keep it handy for any Incident or Smart Alert ticket.

**Why it matters**
Not every client is on the new platform yet. Only clients marked **✓ Complete** in the Next Step column run on apps.apprissretail.com (PU mode). Everyone else still runs on legacy NetTrack at apps.lpguys.net, with a different app, database and logs. If you troubleshoot a legacy client in the platform, you get errors or empty screens that have nothing to do with the ticket.

**How to read it (Master Tracker tab)**
- Client Number and Client Slug: the ClientID and the slug used in every URL
- Next Step and Progress: where the migration is. DB Only means the database moves first, the app can still be legacy
- Current URL Incident: the legacy link, apps.lpguys.net/<slug>/nettrack/index.aspx
- New URL: the platform link, apps.apprissretail.com/<slug>/signin
- Server: the legacy node number

**Before you start a ticket**
1. Find the client and check Next Step
2. Complete: work in the platform
3. Anything else: open the Current URL Incident link and check the database in the Customer Server Profile page: https://trebuco.atlassian.net/wiki/spaces/AALPS/pages/474658570288 (an asterisk means the client already uses the platform database)

Example: all Goodwill tenants (379 to 390) are still legacy, so their cases only open from apps.lpguys.net.
