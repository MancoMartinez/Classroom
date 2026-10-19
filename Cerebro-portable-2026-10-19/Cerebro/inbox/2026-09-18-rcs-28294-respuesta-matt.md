@Matthew Kamminga sample record: `2026-ADUP-45-79`, ShopliftingID `48786`, DateEntered `2026-08-18 23:11`. Same tenant, same Case Type Complaints, satisfies the same filter as the working case below. Zero rows in `incident.SmartAlertProcess` for this ShopliftingID.

Alerts that should have fired, against the working case for comparison:

| ShopliftingID | CaseNo | ConfigID 14, HR Alert 1 | ConfigID 16 | ConfigID 18 |
| --- | --- | --- | --- | --- |
| 48575, working | `2026-ADUP-40-96` | Success | Success | Success |
| 48786, zero rows | `2026-ADUP-45-79` | none | none | none |

Full detail already on this ticket. My August 26 comment has the precondition table and the filter. My August 27 comment has this same side by side comparison with the query used.
