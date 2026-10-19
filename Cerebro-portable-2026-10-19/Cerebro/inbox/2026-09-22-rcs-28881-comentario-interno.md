# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Environment and steps to reproduce

**Environment:** NEXCOM production, on prem, customer hosted. Host `whqapisiis01.nexad.nexweb.us`.
Application path `/apis270/`, so this tenant runs the **270 UI**, not 275. The Confluence page
Modules by Client lists NEXCOM as 275 and is wrong or stale, last modified September 2019.

### NEXCOM (NEX), reported 10 September 2026

1. Sign in to APIS production as Carlo Conty, LP admin, Admin tab visible.
2. Audit Center, Audit admin tab, Templates.
3. Open template `ANNUAL OPS/SERVICES REVIEW`, code `OPS/SERV`. The template editor opens.
4. In the Forms section, click form `2026 Annual Retail & Svcs Review( ID:576 )`.

Expected: the form editor renders.
Actual: the content frame goes blank immediately. The browser holds for 8 to 10 minutes and then
raises Chrome's `This page isn't responding` prompt on `new_docframe.asp`. Screenshots attached by
the customer on 16 September.

Ten of the fourteen forms under that template fail the same way. IDs 577, 578, 575 and 341 open.

## 2. Findings

- verified by customer. The page holds 8 to 10 minutes before Chrome raises the unresponsive
  prompt. That is the browser render thread blocking, not an edge timeout returning an error.
- verified by customer. Template reads `Template deleted.0`, so it is neither deleted nor expired.
- verified by customer. Another large template, 2026 Annual Safety Compliance Audit, opens normally.
- verified by me, 14 September, prep tenant `nexcom-prep`. The Audit module renders normally there.
  The template from this ticket does not exist in prep, so the hang itself cannot be reproduced here.
- verified by me, 22 September, prep tenant. Admin, Labels, Edit, Label Selection lists the tenant's
  full label catalog in sequence. It goes `AUDIT.STATUS.0`, `AUDIT.STATUS.2`, `AUDIT.STATUS.4`.
  `AUDIT.STATUS.1` and `AUDIT.STATUS.3` are not in the table. They were never created for this
  tenant, this is not a cache or display problem.
- unverified, from AI triage, listed so it is not re-explored. Form volume on the combined 2026
  forms may drive the render failure. The forms that still open are the split parts, one is
  literally named Pt2.

## 3. Troubleshooting performed, and the limits of support access

I walked the Audit module end to end in `nexcom-prep` on 14 September with the shared support
account, and captured each screen. The template in this ticket does not exist in prep, and prep
carries a different dashboard and menu configuration from their production, so prep does not model
their live setup or reproduce the hang itself.

Claude flagged the unresolved status label as worth checking directly against the tenant's label
table rather than assuming a cache problem. I checked three things myself on 22 September. I ran
Reset Label Cache in prep, it recompiled all eight configured languages cleanly in 11.03 seconds
with no error, and the unresolved status label on the Home dashboard did not change afterward. I ran
the Troubleshoot Labels control character checker, it returned over 150 defective entries with
invalid characters or unassigned names, none of them `AUDIT.STATUS`, so that check covers a
different defect category. I then opened the label catalog directly and confirmed `AUDIT.STATUS.1`
and `AUDIT.STATUS.3` are absent from it. This is what I think is happening. Could someone evaluate
whether a missing status label can make a synchronous form render hang rather than fail fast, and
give me your thoughts.

**Support cannot go further alone.** NEXCOM is on prem and government. We hold no access to their
production data or servers. A screen rebuild, a label cache reset and any database read are all out
of reach there. Their Lead Applications Administrator is Milan Djordjevic, who worked
https://trebuco.atlassian.net/browse/RCS-28642 with David Beck on 28 August.

Conversations outside the ticket. Support received an informal message from Matt Kamminga with a
screenshot of where Reset Label Cache lives in APIS admin, on a tenant other than NEXCOM, shown as a
navigation reference. The channel is not on record in the ticket.

## 4. Ruled out. Do not repeat

| Hypothesis | Refutation |
|---|---|
| Template deleted or expired | Reads `Template deleted.0` with the filter off |
| Edge timeout at 100s, as in https://trebuco.atlassian.net/browse/RCS-28139 | The page holds 8 to 10 minutes, no 504 or 524 returned |
| User permission gate, as in https://trebuco.atlassian.net/browse/RCS-28852 | Carlo has the Admin tab and other templates open for him |
| Stale label cache | Reset Label Cache recompiled cleanly on 22 September, the missing status label stayed unresolved |

## 5. Still open

1. Confirm whether NEXCOM's production label table has the same gap for `AUDIT.STATUS.1` and
   `AUDIT.STATUS.3` as prep, and whether adding those two entries is safe as a standalone fix.
2. Tell me what to request from Milan on the server side. IIS logs alone may not show this if a
   response is being returned and the browser itself is what stalls.
3. Confirm whether splitting form 576 permanently is the path forward, or whether a fix exists for
   the combined form.

Priority Medium, opened 10 September. The customer has already worked around it by splitting the
annual review into two audits and assigning those to locations, so they are not blocked. Form 576 is
the one they intended to assign.

Routing note. Aimee's L3 procedure, Confluence RTS `478006902856`, sends code and bug work to Under
Engineering Review with Shandana Khan as assignee, and the ENG auto creates on the transition. AALPS
is the engineering queue for Incident, Audit, Aspect legacy and APIS, and Matt Kamminga owns that
area. On https://trebuco.atlassian.net/browse/RCS-28212 Viraj Kansara wrote on 18 August that all
APIS goes direct to Matt Kamminga, so I am naming him here alongside the standard transition.
