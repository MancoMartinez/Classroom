**Update for Infrastructure.** Smart Alert runs for ADUSA stopped completing on 9/24 around 11:06 UTC. My first note on RCS-29026 went in before RETAILIT-20901 was linked, so the evidence is repeated here.

## 1. Correction

My test case `2026-AHOLD DELHAIZE USA SERVICES, LLC-9998-13` was left Open. The Smart Alert filters require Closed, so its Quit lines prove nothing by themselves. Customer case `2026-FOOD LION ,LLC-2547-32` below is the evidence.

## 2. Environment and steps to reproduce

Production, ADUSA, client 441, Grafana `grafanacloud-apprissretail-logs`.

1. Run this query from 2026-09-20 to 2026-09-25:
```
{service_name=~".+", deployment_environment="usprod"} | clientId="441" |= "End of SmartAlert.ProcessSmartAlert"
```
2. Look at the Logs volume chart.

Expected: End lines every day, as on 9/20 to 9/23.
Actual: the last End is 2026-09-24 11:06:43 UTC, SystemID 1592877. None after that through 9/25.

## 3. Findings

| Finding | Evidence | Status |
|---|---|---|
| **Runs stopped completing** | Last End 9/24 11:06:43 UTC | verified |
| Runs still start and exit | 9/25 20:04 to 20:23 UTC: 89 Begin, 0 End, 76 "still on processing" | verified |
| Queue grows | `ProcessAlertQueue 1. dt.Rows.Count` from 217 to 222 in that window | verified |
| Before the break | 9/20, case 0619-27, ShopliftingID 1596525: 13 Begin, 12 End, alerts inserted into SmartAlertProcess | verified |
| Customer case | 2547-32, ShopliftingID 1598030: first save 20:20:10 UTC ran 11 alerts while Open. Every later save, including the close at 20:27:32 UTC, exits | verified |

```
0. Quit ProcessSmartAlert because the smart alert for the case is still on processing. pSystemType=Case, pSystemID=1598030
```

## 4. Troubleshooting performed

Claude flagged the missing End lines as the likely cause. I ran the Grafana queries above myself, filtered by ShopliftingID 1598030 and 1596525, and compared 9/20 with 9/25. My reading is that runs no longer finish, so the processing state never clears and every later run exits. Could someone else evaluate this and give me your thoughts?

Outside the ticket: Teams and a call with Kiran Vadday and Vedant Shirude on 9/25. Chris Rippingale checked SendGrid.

## 5. Ruled out so far

| Hypothesis | Why |
|---|---|
| Comma separated email group | `SendGridEmail.vb` splits To and CC on commas |

## 6. Still open

1. Did anything change on 9/24 between 11:06 and 14:00 UTC for Nettrack or the Hatr NettrackSmartAlert task?
2. What clears the processing state for a case once a run starts?

Related: https://trebuco.atlassian.net/browse/RCS-29123 reports no alerts on 9/25. Customer reported on 9/21, priority Medium.
