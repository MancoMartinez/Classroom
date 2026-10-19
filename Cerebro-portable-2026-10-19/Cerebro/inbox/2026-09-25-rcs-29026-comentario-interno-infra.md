**Escalating to Infrastructure.** Smart Alerts for ADUSA have not run since 9/24. Kiran Vadday suggested Infrastructure on 9/25 after we reviewed the logs together.

## 1. Environment and steps to reproduce

Production, ADUSA, client 441.

1. In LPMS, create a case on store 9998 TEST LOCATION ONLY, type Miscellaneous Investigation, with an active Smart Alert for that case type.
2. Open Smart Alert History on the case.
3. In Grafana, search the logger `LPSBO.SmartAlert` for the case ShopliftingID.

Expected: one alert run in Smart Alert History.
Actual: "No Matching Alerts Found". Case `2026-AHOLD DELHAIZE USA SERVICES, LLC-9998-13`, ShopliftingID 1598266, 9/25 17:52 UTC.

## 2. Findings

| Finding | Evidence | Status |
|---|---|---|
| The Hatr task runs, then exits for the case | 4 lines between 17:52 and 17:55 UTC for 1598266 | verified |
| Same exit on other ADUSA cases | 263 ShopliftingIDs in one export, 9/25 16:25 to 23:37 UTC | verified |
| Starts on 9/24 | Log volume low until 9/24 morning, high and constant after | verified, read from the chart |
| Customer case | `2026-FOOD LION ,LLC-2547-32`, 9/24 around 20:20 UTC, no alert run | verified |
| Other clients | 19 clients in the unfiltered export, 441 carries 442 of 1000 lines | verified. Normal volume for them is unknown |

```
0. Quit ProcessSmartAlert because the smart alert for the case is still on processing. pSystemType=Case, pSystemID=1598266
```

## 3. Troubleshooting performed

Claude flagged the "still on processing" exit as the likely cause. I checked Smart Alert History, Change History, Incident Logs and the Grafana logs in Control Panel myself. The exit matches my test case and the customer case. My reading is that a case state stays in processing and blocks the run. Could someone else evaluate this and give me your thoughts?

Outside the ticket: Teams and a call with Kiran Vadday and Vedant Shirude on 9/25. Chris Rippingale checked SendGrid.

## 4. Still open

1. Did anything change on 9/24 morning for ADUSA in Nettrack or the NettrackSmartAlert task?
2. What sets the processing state for a case, and what clears it?
3. Is the Quit volume for the other 18 clients normal?

Related: https://trebuco.atlassian.net/browse/RCS-29123. Reported 9/21, priority Medium.
