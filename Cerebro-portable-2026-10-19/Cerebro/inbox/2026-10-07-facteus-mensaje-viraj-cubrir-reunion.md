Facteus, mensaje para Viraj, cubre la reunión de hoy con L1

Fecha 2026-10-07. Juan sin voz, Viraj lleva la llamada con Santhosh en su lugar.

```
Hey Viraj, I lost my voice, can't make today's L1 call with Santhosh. Can you run it in my place?

Quick context so you walk in with everything you need.

Where we are: Chris already closed out the open items on Data Engineering's side. SLA is 1 business
day with a 24 hour turnaround expectation except weekends, escalation routes through Jira Operations
to the whole Data Engineering team, and both dashboards are now linked directly in the triage docs.

Why this call exists: the only thing left before Support accepts the full handover is deciding who
monitors Facteus alerts day to day. From our call on the 25th, the idea was to bring L1 in from the
start since they already run 24/7 rotational monitoring for everything else, rather than loop them
in after the fact.

What needs to come out of today, whether L1 can add Facteus to their existing rotation, which of the
two dashboards they'd use as the source of truth, Grafana (https://apprissretail.grafana.net/goto/svsg2j)
or Saddam's console (https://prd-datacloud-console-app-wus2.azurewebsites.net/), and how they'd
validate it against a real alert before relying on it in production. If that's resolved, we can tell
Chris L1 is ready and pick a date for the full handover.

One flag, Santhosh was looking at the old Facteus Support wiki page, it's from before any of this and
doesn't have the current SLA or escalation info. I already sent him the updated pages too, just in
case it comes up.

Appreciate you covering this, I'll catch up after.

Thanks,
Juan
```
