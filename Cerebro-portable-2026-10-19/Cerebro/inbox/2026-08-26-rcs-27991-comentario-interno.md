# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Correction

The `relates to RCS-27586` link on this ticket is wrong. It has been pointing this investigation at the wrong release for four weeks. Remove it as a cause.

RCS-27586 was Kohl's losing the whole Engage dashboard during the Engage Insights migration. The RTS runbook records that symptom as a blank dashboard returning 500 and timeout, not as individual panels failing. That release went to production on 23 July and the customer confirmed it working on 24 July. This ticket was raised on 27 July against a dashboard that renders.

The July 2026 Release 2/2 notes list one Kohl's Insights item, `ENG-6184 KHL | Insights Return Metrics Error`. Return metrics. Not Top 10 panels. Two different defects.

## 2. Environment and steps to reproduce

**Environment: Production.** Reproduced on two tenants by the reporter, and independently reported on a third by an end customer. All three sit on GP3.

### Harbor Freight (HFT), 27 July 2026

1. Sign in to the Harbor Freight production portal.
2. Open the **Engage Analytics** tab from the portal tab bar.
3. Leave the default date range applied.
4. Observe the row of aggregate tiles at the top of the page.
5. Observe the two detail panels directly beneath those tiles.

**Expected:** both detail panels list their top 10 rows.
**Actual:** both panels render an orange warning triangle and no rows. Screenshot attached to this ticket as `Engage Analytics Issue.docx`, captured at report time.

### Floor and Decor (FAD), 14 August 2026

1. Sign in to the Floor and Decor production portal.
2. Open the **Engage Analytics** tab.
3. Set the date range to **08/08/2026 to 08/14/2026**.
4. Observe the two detail panels beneath the aggregate tiles.

**Expected:** both detail panels list their top 10 rows.
**Actual:** panels do not populate. Confirmed by the reporter on 2026-08-14.

### lululemon (LLU), 30 July 2026, reported under RCS-28068

1. Open the Engage Analytics dashboard.
2. Locate the **Top 10 SKUs** and **Top 10 Consumers** tables.
3. Vary the date range across several spans.

**Actual:** tables remain empty at every range. The customer ruled out date range herself before raising the ticket.

### Observed state of the page, HFT

| Component | Result |
|---|---|
| Calls to Appriss | 179, renders |
| Calls Per Action | 5.31%, renders |
| Activity Reports | 126, renders |
| No ID (NR) | View control present |
| Manual ID Entry | View control present |
| Boris Return Amount | $0, renders |
| Lower left detail panel | warning icon, no data |
| Lower right detail panel | warning icon, no data |

**Every aggregate tile on the page returns a value. Only the two SKU level detail panels fail.** Authentication, permissions, session state and the dashboard as a whole are not in play. The failure sits in the data layer feeding those two panels.

Note on tenant state: Harbor Freight has since been migrated to Engage Insights. The Engage Analytics tab was still present on HFT on 27 July when the screenshot was taken. It remains present on FAD.

## 3. Findings

**This defect shipped a fix once already.** The November 2025 Sprint page in R&D records it:

```
66220 | Bug | Engage Analytics dashboard Top 10 lists not populating
RCS-23643 | Foot Locker | Secure EBR | Priority 1
```

Azure DevOps 66220, delivered in the November 2025 first release on branches `release/5.4/5.4136` and `release/5.4/5.4137`.

Root cause recorded on RCS-23643 by Mohammed Mutahhar on 22 October 2025:

```
The Hierarchy Filter is not being applied.
The reference data backload task is failing with:
The given value '44_00001138_NAVY/WHITE/GUM' of type String from the data source
cannot be converted to type nvarchar for Column 7 [ProductHierarchy4].
```

Closed as `Engineer Resolved - Data Corrected`.

Same component, same two panels, near identical title. **Check this as a regression of 66220 before opening new work.** Two checks against HFT and FAD cover it. Reference data backload state, and whether the Hierarchy Filter is applied.

**The same defect is already in development.** RCS-28068 reports the identical symptom on LLU. On 2026-08-05 Carl Costelow wrote, after speaking with Jon Morgan, that this is a code issue and asked for a bug. It moved to `Accepted into Development` under Shandana Khan on 2026-08-18. It carries no Azure DevOps link.

## 4. Troubleshooting performed, and the limits of support access

Steps taken by support:

1. Identified the tenant from the logo in the reporter's attachment.
2. Requested and received the signed in account, the tab visibility and the exact date range from the reporter on 2026-08-14.
3. Compared the symptom against RCS-27586 and rejected it on release timing.
4. Compared the symptom against RCS-23643 and matched it on component and panel.
5. Searched Confluence release notes for July 2026 and August 2026 for a shipped fix to these panels. None exists.
6. Searched Confluence for RCS-27991, RCS-28068 and RCS-28004. No page references any of them.

AI assisted triage was used for the ticket history search, the Confluence search and the cross reference against prior tickets. All findings above were verified against the source record and are cited to it.

Support cannot go further. There is no read access to the Snowflake procedures under `EngageDependent/` that feed `engage_insights__top_skus`, and no visibility into reference data backload job state. Both checks need Engineering.

Conversations outside this ticket: none. Platform was asked twice inside this ticket, on 2026-07-28 and 2026-08-03. Neither request drew a reply in 26 days. That is why this is coming to Engineering through the formal route.

## 5. Ruled out. Do not repeat

| Hypothesis | Why it fell |
|---|---|
| The Kohl's release reached this tenant late | Shipped 23 July, confirmed working 24 July, reported here 27 July |
| Date range too narrow | Reporter varied the range on FAD. LLU customer varied it independently |
| Tenant permissions or SSO | Aggregate tiles render for the same session on the same dashboard |
| Single tenant configuration | Reproduced on HFT, FAD and LLU |

## 6. Still open

Three things I need from Engineering:

1. Confirm whether the RCS-28068 fix covers HFT and FAD, or whether those tenants need separate work.
2. The Azure DevOps bug number for RCS-28068, so this ticket can track it.
3. Confirm or rule out a regression of ADO 66220.

RCS-28004 reports Top Returned SKUs not returning UPC on Harbor Freight and DSW. Same reporter, raised one day after this ticket, assigned to Jon Morgan, no comments since 2026-07-28. Same tenant, same SKU data domain. Confirm whether it shares a root cause.

Priority is High. This ticket has been open 30 days with no engineering comment.
