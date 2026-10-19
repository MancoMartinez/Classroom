# RCS-29140 GoodwillSC, Teams a Vedant Shirude, ingles. Pagina con formato: https://claude.ai/artifact (rcs-29140-teams-vedant)

Hi Vedant Shirude, on https://trebuco.atlassian.net/browse/RCS-29140 (GoodwillSC, Property Damage alerts stopped) I think it may be the same pattern we just found on https://trebuco.atlassian.net/browse/RCS-29195 for Goodwill Manasota. There the Property Damage alert filter requires a Report Narrative, and the case had none, so the alert was skipped.

1. Access: GoodwillSC is client 383, not migrated, on lpguys. Customer SSO: https://apps.lpguys.net/goodwillsc/nettrack/index.aspx?nosaml=1 with 1Password GoodwillSC (Upstate Midlands) - Supervisor. Grafana has no logs for legacy tenants.
2. Alert screen: Manage Smart Alerts, Property Damage, Alert Configuration and Build Filters.
3. SQL read only, legacy server, database GoodwillSC, dbo: 3a alert config with LastSent and runQuery, 3b recent Property Damage cases with NarrativeLength and LastAlertRun, 3c runQuery against one case, 3d TOP 20 SmartAlertProcess.
4. Read: narrative NULL with a narrative filter = configuration like 29195. LastSent shows when it stopped. 3c = 1 with no alert row = check how the case was created and saved. 3d rows today = engine works.
