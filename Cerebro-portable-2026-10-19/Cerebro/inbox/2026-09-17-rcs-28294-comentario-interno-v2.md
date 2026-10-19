# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Correction

**This ticket picked up an unrelated login and session symptom.** Tatiana Barcenas lost system access on August 31 while gathering the case numbers I asked for on August 25. That is now RCS-28977, https://trebuco.atlassian.net/browse/RCS-28977. This ticket returns to the smart alert engine only.

## 2. Environment and steps to reproduce

**Environment:** Production, Vallarta tenant, `/vallarta/nettrack/`. Preconditions and reproduction steps unchanged from my August 27 comment on this ticket.

No calls or Teams messages outside this ticket since then.

## 3. Findings

- **Stored timestamps are accurate.** Verified. `incident.CaseChanges.DateChanged` for case `2026-ADUP-40-96` reads `2026-08-10 23:23:43 UTC`, converts to 4:23pm Pacific, matches the customer's reported time.
- **The Change History modal misrenders that value.** Verified. Modal showed `8/11/2026 12:23 AM`, the raw UTC value plus a flat 1 hour, not a Pacific conversion.
- **This closes the August 27 timestamp caveat.** The 8 hour gap flagged there is the modal render, not a batch timing issue. Stored timestamps are safe to quote.
- **48575 versus 48786 is unchanged**, restated from August 27:

| ShopliftingID | SmartAlertProcess rows |
| --- | --- |
| 48575 | 3, all Success |
| 48786 | 0 |

## 4. Troubleshooting performed, and the limits of support access

Ran `INFORMATION_SCHEMA.COLUMNS` on the Vallarta production DB. `incident.ChangeHistory` is empty for this tenant. `incident.CaseChanges`, 2,580,206 rows, is the real audit table. Compared its raw `DateChanged` against the modal's displayed value for case `2026-ADUP-40-96`.

Claude flagged the modal offset as a display bug rather than a data or timing issue. I ran the schema check and the row comparison myself against production and confirmed it. Could someone confirm this is a display issue only.

Support has read only DB access. Support cannot read application logs or ERMS render code.

## 5. Ruled out. Do not repeat

| Hypothesis | Result |
| --- | --- |
| Batch or queue timing caused the 8 hour gap | Refuted. Flat 1 hour render offset, not execution timing |
| `incident.ChangeHistory` is the audit source here | Refuted. Zero rows for every account and range tested |
| `UPDATE incident.Shoplifting SET InProcess = 0`, Stater Bros pattern, RCS-28465, https://trebuco.atlassian.net/browse/RCS-28465, and RCS-28534, https://trebuco.atlassian.net/browse/RCS-28534 | Refuted. Different case type and table |

## 6. Still open

1. Diff the execution path between 48575 and 48786. Start with the application log around `2026-08-18 23:11` for 48786.
2. Confirm whether `RunStatus = Success` on 48575 means the email was delivered.
3. Confirm whether ENG-7359, https://trebuco.atlassian.net/browse/ENG-7359, covers 48786. Whether it came through Quick Entry is unverified.

Moving to Under Engineering Review, scope narrowed to the smart alert engine.
