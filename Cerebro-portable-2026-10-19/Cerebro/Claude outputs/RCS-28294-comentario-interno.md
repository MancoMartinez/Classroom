# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Correction

The Aug 25 internal analysis proposed a fixed Pacific offset without DST as the cause of the 8 hour gap between the client's reported time and the Change History display. Today's query results rule that out. The stored value converts correctly to PDT, UTC minus 7, matching the 4:23pm Pacific time the client reported for the same save. The gap comes from the History modal itself, which adds a flat 1 hour to the raw UTC value instead of converting to Pacific.

## 2. Environment and steps to reproduce

Production. Tenant Vallarta Supermarkets, Client ID 432, database sqldb-prd-wus2-arp-production-432-vsa-platform.

### Vallarta (VSA), case 2026-ADUP-40-96

1. Open case 2026-ADUP-40-96 in nettrack.
2. Open Change History from the case menu.
3. Scroll to the oldest entry, a SAVE.CASE row.
4. Note the displayed timestamp.

Expected: the displayed timestamp reflects the case record's local Pacific time, a UTC minus 7 conversion from the stored value.
Actual: the modal shows 8/11/2026 12:23 AM. The raw incident.CaseChanges.DateChanged value for that row is 2026-08-10 23:23:43.000 UTC. The displayed value equals the raw UTC value plus exactly 1 hour. See attachment image-20260812-181001.png, already on this ticket, uploaded by David Vargas on 2026-08-12, showing the same modal render.

## 3. Findings

Verified. incident.CaseChanges.DateChanged for the first SAVE.CASE on 2026-ADUP-40-96 is 2026-08-10 23:23:43.000 UTC.
Verified. The Change History modal displays this row as 8/11/2026 12:23 AM, exactly raw plus 1 hour.
Verified. 2026-08-10 23:23:43 UTC converts correctly to 2026-08-10 16:23:43 Pacific, PDT, UTC minus 7. This matches the 4:23pm Pacific time the client reported for the same save.
Verified. Vianney Valdez's account, incident.LPUser2 UserID 32665, carries TimeZone America/Los_Angeles in membership.Users. Her account is not misconfigured.
Unverified, from AI triage, listed so it is not re-explored. The modal's plus 1 hour behavior could come from a hardcoded UTC plus 1 fallback in the render path, a common pattern when a server side TimeZoneInfo lookup fails.

## 4. Troubleshooting performed, and the limits of support access

I pulled incident.CaseChanges directly against the production database for tenant 432. incident.ChangeHistory exists in this tenant and holds zero rows, it does not carry this data. I confirmed the real columns with INFORMATION_SCHEMA before writing the query. I compared the raw DateChanged value against the modal's rendered timestamp for the same row, and against the client's independently reported wall clock time.

Claude flagged this as the likely root cause. I checked A, B and C myself, and here is what I found. This is what I think is happening. Could someone else evaluate this and give me your thoughts?

No conversations happened outside this ticket on this finding.

I do not have access to the Change History render code or the server's TimeZoneInfo configuration. Please confirm whether the render path uses a hardcoded offset or a failed TimeZoneInfo lookup.

## 5. Ruled out. Do not repeat

Fixed Pacific offset without DST as the storage mechanism. Ruled out, the stored UTC value converts correctly with DST applied.
Vianney Valdez's account timezone as misconfigured. Ruled out, her account carries the correct IANA zone.

## 6. Still open

1. Confirm whether the Change History render path adds a hardcoded 1 hour offset, or falls back to it when a TimeZoneInfo lookup fails.
2. Confirm whether this render defect affects other tenants or only Vallarta.
3. This finding is separate from the smart alert trigger timing issue already under review on this ticket. Evaluate it independently, do not combine the two into one fix.
