Resolution summary, 9/28.

Issue: Joe Austin reported Smart Alerts stopped around 9/23 for Vitamin Shoppe, client 433. Grafana export of 9/25, 20:05 to 23:40 UTC, shows 68 "still on processing" exits for 433, same pattern as RCS-29123. Start date for 433 not confirmed in Grafana.

Cause, per Kiran Vadday on RCS-29123: deadlock in ProcessSmartAlert when runs process in parallel.

Fix: PR 58273, US prod 9/28.

Verification: Joe ran a test alert on 9/28 and confirmed delivery.

Open: the fix does not reprocess cases stuck with InProcess = 1. Alerts missed 9/23 to 9/28 not resent. Customer offered a resend by case number.

Related: RCS-29123, RCS-29026, RETAILIT-20901.
