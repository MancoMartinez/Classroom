**Update 10/9. Stuck InProcess flags cleared for Vallarta.**

## 1. What the customer reported

Tatiana Barcenas, 10/9: alerts do not fire when an investigation is closed. Examples `2026-ADUP-65-52` and `2026-ADUP-66-15`.

## 2. Findings

| Check | Result |
| --- | --- |
| `incident.Shoplifting.InProcess` for 43170 and 49371 | **1** on both |
| Grafana, client 432, 43170, 10/8 13:31 | `Begin` then `0. Quit ProcessSmartAlert because the smart alert for the case is still on processing. pSystemType=HR` |
| SmartAlertProcess | Last alerts 9/18 for 43170 and 9/8 for 49371. Nothing for the close |
| All cases with InProcess = 1 | **311**. 198 created in September, 0 in October. Newest 49927, created 9/28 15:33 UTC |

My reading is that these are runs that died during the September Smart Alerts deadlock, fixed in PR 58273 on 9/28, https://trebuco.atlassian.net/browse/RCS-29123. New cases complete normally.

## 3. Action taken

With Matt Kamminga's approval on Teams, I reset `InProcess` to 0 for the 311 cases created before 10/1. IDs saved before the update. Remaining count with InProcess = 1: 0.

## 4. Still open

1. Matt confirmed there is no automatic reset. Any run that fails leaves the case stuck again. Could this be covered in the permanent fix?
2. The two closures above were not alerted. Asking the customer before resending.
