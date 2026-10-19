INTERNAL NOTE. NOT FOR CUSTOMER

Smart Alerts are not being processed for any client since 9/24 around 14:00 to 15:00 UTC. Escalating to Infrastructure, per Kiran Vadday. Platform wide.

What the logs show
Grafana, usprod, logger LPSBO.SmartAlert, app web-prd-wus2-arp-nettrack. The Hatr task NettrackSmartAlert runs, then ProcessSmartAlert exits with: "0. Quit ProcessSmartAlert because the smart alert for the case is still on processing. pSystemType=Case, pSystemID=<ShopliftingID>".
In 3.5 hours on 9/25, 20:05 to 23:40 UTC, 1000 of these lines across 19 clients and 443 cases. Client 441 ADUSA 442 lines, 300 202, 432 70, 433 68, 143 65, 423 59, 420 29. Each case is retried and exits again, up to 15 times.
Log volume for this message is low until 9/24 morning and high and constant after that.

Cases
ADUSA 2026-FOOD LION ,LLC-2547-32, saved 9/24 around 20:20 UTC, no alert run. Customer reported it as the first case without an alert.
Test case 2026-AHOLD DELHAIZE USA SERVICES, LLC-9998-13 on store 9998 TEST LOCATION ONLY, ShopliftingID 1598266, 9/25 17:52 UTC. Four Quit lines between 17:52 and 17:55 UTC, Smart Alert History empty. Test alert RCS-29026 test comma is now Inactive.
Related: RCS-29123, no alerts today.

Questions for Infrastructure
1. Was anything deployed to Nettrack or the Hatr NettrackSmartAlert task on 9/24 morning?
2. What sets the "on processing" state for a case, and why is it never cleared?

Separate issue, lower priority
SmartAlert.vb writes RunStatus Success to SmartAlertProcess without checking sendResult from SendEmailAsync, and Warn logs are not kept. A failed send leaves no trace. Example: ADUSA case 2026-FOOD LION ,LLC-0619-27 on 9/20, Defrauded Customer-Food Lion shows Success and was not found in SendGrid.

Impact: customers are not notified of cases that match their Smart Alerts, including high loss cases. Requesting priority High.
