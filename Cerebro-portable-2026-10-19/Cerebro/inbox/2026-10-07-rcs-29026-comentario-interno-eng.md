**Escalating to Engineering.** ADUSA Smart Alerts with the same address in To and CC show Success but never reach SendGrid. Kiran Vadday agreed on 10/7 to review a dedupe.

## 1. Environment and steps to reproduce

Production, ADUSA, client 441. Case `2026-FOOD LION ,LLC-1353-15`, ShopliftingID 1603659, alert `Harassment - Food Lion`, SmartAlertConfigID 209.

1. Grafana, `LPSBO.SmartAlert`, line `13b` for config 209 at 10/7 18:49:34 UTC.
2. SendGrid Email Logs, `jamie.holland@adusa.com`, 10/7.

Expected: Delivered at 18:49:34 UTC.
Actual: no entry. Deliveries at 18:40:41 and 19:02:15 UTC.

## 2. Findings

| Send | To | CC | SendGrid |
| --- | --- | --- | --- |
| 1353-15, 10/4 16:20, row 371425 | `Brian.Tanner@FoodLIon.com` | `Brian.Tanner@FoodLion.com` | **missing** |
| 1353-15 resend, 10/7 18:49, row 371880 | `Brian.Tanner@FoodLIon.com` | `Brian.Tanner@FoodLion.com` | **missing** |
| 1353-15 resend, 10/7 19:26, Brian removed from 209 | none | `Brian.Tanner@FoodLion.com` | Delivered 19:26:21 |
| 0619-27, 9/20 14:12, row 368924 | `kimberly.WILLIAMS@FoodLion.com` | `Kimberly.WILLIAMS@FoodLion.com` | not found 9/25, now past retention |
| 10/4 00:20, row 371350, config 197 | `kimberly.WILLIAMS@FoodLion.com` | `Kimberly.WILLIAMS@FoodLion.com` | **missing** |
| 10/7 02:13, row 371801, config 199 | `Mark.Sens` and `mark.sens` | none | Delivered |

**Verified:** in the 19:26 run, `10c` built 7 CC addresses and `13b` sent 5. Silvana.Baxter and bj.robinson were dropped because they match To exactly. My reading is that the dedupe is case sensitive.

Scope since 9/15: 11 sends. Config 197: 7. Config 209: 3 plus row 371425. Config 361: 1.

## 3. Troubleshooting performed

Claude flagged the duplicate as the likely cause. I checked the 13b lines in Grafana, EmailAddresses in SSMS and each send in SendGrid myself, and removed Brian from alert 209 before the 19:26 resend. Could someone else evaluate this and give me your thoughts?

Outside the ticket: Teams with Kiran Vadday, 10/5 to 10/7. Mike Tasch found nothing on relay pd-lpms-smtp-03 for the 10/4 send.

## 4. Ruled out so far

| Hypothesis | Why |
| --- | --- |
| Semicolon in EmailAddresses | It is the To/CC separator. Sends with it are delivered |
| Attachment size | 0 attachments on 1353-15 |
| Line breaks in addresses | None in config 209 |

## 5. Still open

1. Could the To/CC comparison ignore case?
2. Could SmartAlert.vb check the SendGrid response before writing Success?

Related: https://trebuco.atlassian.net/browse/RCS-29123, https://trebuco.atlassian.net/browse/RETAILIT-20901. Reported 9/21, Medium.
