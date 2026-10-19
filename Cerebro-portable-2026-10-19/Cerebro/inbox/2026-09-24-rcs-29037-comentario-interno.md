# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Scope update since my Sep 21 note

**The outage is wider and longer than first reported.** It is no longer a VPN issue only. All of Claire's external integrations have been offline since early Saturday Sep 19, with no restoration ETA.

| Item | Sep 21 | Sep 24 |
|---|---|---|
| Cause on Claire's side | VPN outage | All external integrations offline |
| Start | Saturday morning | Saturday Sep 19, early morning |
| ETA | Expected mid week | None |
| Trading days without data | Sep 19 to 21 | Sep 19 to 24, six days |

## 2. Environment

Production. Client 439, Claire's. Ingestion API, endpoint `c439_rawdata_postransactions`. No reproduction steps apply. The feed is silent because the customer cannot send.

## 3. Troubleshooting performed, and the limits of support access

No new testing on this tenant since my Sep 21 note. The precedent and the open points listed there still stand.

Conversations outside this ticket: one customer email. Chris Angelica sent it to all Claire's data partners on Sep 24 at 10:44 ET, and Shreyas Amai attached it to this ticket the same day. Chris says he will contact each partner individually to agree on three points. Whether transmission simply turns back on, whether historical updates are needed, and any other topic.

Support has no visibility into how the ingestion endpoint validates backdated payloads or how the GNG check treats late data for a trading day already closed.

## 4. Still open

1. Does `c439_rawdata_postransactions` accept payloads dated for a past trading day, and is there a maximum lookback window? The gap is already six trading days and has no end date yet.
2. When late data arrives for a trading day that closed under the GNG minimum, does that day get reprocessed for Work Items, or does it stay skipped?
3. If those days stay skipped, is there a supported way to trigger Work Item generation for them once the data is complete?
4. What should Support ask Claire's to send when Chris reaches out, so the recovery can be validated as complete?
