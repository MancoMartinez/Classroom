# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Environment and scenario

Production. Client 439, Claire's. Ingestion API, endpoint c439_rawdata_postransactions.

1. Claire's reports a VPN outage on their side since Saturday morning, per the customer email on RTS-207993, Chris Angelica, Director Data Analytics and Integrations.
2. Gateway file transmission to Appriss has been interrupted since then. No ETA confirmed, customer expects mid week.
3. Customer asks whether resuming regular transmission recovers all data missed during the outage, or whether historical or catch up files are also required.

Expected: a confirmed answer on whether the ingestion pipeline accepts backdated trading day payloads and whether a trading day already skipped by GNG can be picked up later.
Actual: unconfirmed. No Engineering input on file yet for this tenant.

## 2. Findings

Verified. Client is Claire's, client ID 439, feed c439_rawdata_postransactions. Source: this ticket, comment by Sanath Acharya, 2026-09-21.
Verified. Any file whose File Source is Gateway routes to Engineering with product type RTIaaS. Source: internal SLA Rules reference, section 9.5, file monitoring escalation rules.
Precedent, not verified on this tenant. RCS-28170, TJX, https://trebuco.atlassian.net/browse/RCS-28170. Same postransactions feed type. Client API keys expired, the feed stopped, one trading day landed at 200408 transactions against a 1700000 minimum, and 23 Work Item definitions were skipped for that day. Once the client fixed the keys and resumed sending, volume recovered on its own with no separate historical file involved.
Unverified, from AI triage. Whether the c439_rawdata_postransactions endpoint accepts a payload dated for a past trading day with no window restriction.
Unverified, from AI triage. Whether a trading day already closed under the GNG minimum gets reprocessed if a later payload arrives for that same date, or stays permanently skipped for Work Items.

## 3. Troubleshooting performed, and the limits of support access

Claude flagged the RCS-28170 precedent and the GNG mechanism as the likely explanation for what Claire's is asking. I have not run any query or test against this tenant myself yet. This is what the research turned up. Could someone with visibility into the ingestion pipeline evaluate whether it holds for Claire's and share your thoughts?

No conversations held outside this ticket yet.

Support does not have visibility into the ingestion endpoint validation rules or into how the GNG check behaves against late arriving data for an already closed trading day. That is why this is going to Engineering instead of being answered from Support.

## 4. Still open

1. Does the c439_rawdata_postransactions endpoint accept a payload dated for a past trading day with no window restriction?
2. If a trading day already closed under the GNG minimum receives a later payload for that same date, does it get reprocessed for Work Items, or does it stay skipped?
3. Is Engineering the right owner for this ticket, given the file source is Gateway per SLA Rules 9.5?
