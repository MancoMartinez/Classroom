# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Environment and steps to reproduce

NEXCOM production, on prem. Host whqapisiis01.nexad.nexweb.us, path /apis270/, APIS 270 UI.

1. Sign in as Carlo Conty, LP admin.
2. Audit Center, Templates, ANNUAL OPS/SERVICES REVIEW, OPS/SERV.
3. Open form 2026 Annual Retail & Svcs Review, ID:576.

Expected: form editor renders.
Actual: content frame blank, Chrome shows This page isn't responding on new_docframe.asp. Ten of fourteen forms fail the same way, IDs 577, 578, 575, 341 open.

## 2. Findings

- verified by customer, fresh attempt, 22 Sep. Hidden frameset exposed via DevTools, technique from Matt Kamminga. spinner_work_area showed Control DB Updated 4:17:05 PM, mymessage Loaded 4:17 pm, 15 minutes.
- verified by me, from the customer's own timestamps. Load time to Control DB Updated is about 34 minutes, longer than the 8 to 10 minutes before Chrome shows unresponsive.
- verified by customer. hidden_work_area stayed empty both attempts. A bar reading 13 Min, No Web Activity appeared near the bottom.
- verified by me, prep, 22 Sep. AUDIT.STATUS.1/.3 missing from the label catalog, secondary unconfirmed lead.

## 3. Troubleshooting performed, and the limits of support access

Claude flagged the 34 minute gap for review. I tested Matt Kamminga's DevTools technique myself in prep first, confirmed it works, then had the customer run it on 576. This is what I think is happening, the gap and the no web activity bar may point to a stuck process, not a render block. Could someone evaluate that?

Support cannot go further alone, NEXCOM is on prem, no server access. Milan Djordjevic is their Applications Administrator.

Conversations outside the ticket. Matt Kamminga shared the DevTools technique informally, I asked him directly for a read on this. Channel not on record.

## 4. Ruled out. Do not repeat

| Hypothesis | Refutation |
|---|---|
| Template deleted or expired | Reads Template deleted.0, filter off |
| Edge timeout at 100s | Holds far longer, no 504 or 524 |
| User permission gate | Carlo has Admin tab, other templates open |
| Stale label cache | Reset Label Cache ran clean, gap unchanged |

## 5. Still open

1. What generates Loaded [time], [N] minutes, and if 34 minutes signals a stuck process.
2. What makes hidden_work_area populate, empty both times.
3. Whether the no web activity bar is routine or tied to this hang.

Priority Medium, opened 10 September. Customer split the review into two audits, not blocked, form 576 still needed.
