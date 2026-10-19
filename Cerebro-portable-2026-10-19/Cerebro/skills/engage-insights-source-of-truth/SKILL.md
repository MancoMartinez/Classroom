---
name: engage-insights-source-of-truth
description: >
  Appriss Retail's internal source of truth for Engage Insights — the analytics suite covering the Overview, Return Metrics, Claims Metrics, and Incent Metrics dashboards. Use whenever anyone asks ANYTHING about Engage Insights: what a tile, chart, filter, or toggle does, how a metric or rate is calculated (Return Auth Value, Action Rate, Redemption Rate, Denied Rate, PAR Rate), how to build a Metric Series, why a number looks wrong or didn't update, or how to walk a customer through a dashboard in a QBR, demo, or support case. Also triggers on dashboard components (Core Metrics, Action Profiles, PAR Overview, Incent Impact Summary, Data Health, Top 50 tables, Returns & Claims Flow) and glossary terms (BORIS, BORO, PAR, Trackable Returns, Non-Receipted, Override). When in doubt — if Engage Insights is mentioned — use this skill.
---

# Engage Insights — Source of Truth

Engage Insights is the retailer-facing analytics layer that sits on top of Engage's return, claims, and incentive authorization decisioning. It consolidates the metrics, trends, and customer-level detail needed to answer the three questions every loss-prevention and returns team asks daily: **What's happening? Who's driving it? How do I stop it?**

This skill is the extensive, up-to-date reference for everything documented in the Engage Insights user guide at `docs.apprissretail.com`. Treat it as the source of truth — read the relevant reference file(s) below before answering, rather than guessing at dashboard mechanics from memory.

## What Engage Insights is made of

The application combines four things into one experience:

- **Program metrics** for Returns, Claims, and Incent authorization activity, each with its own dedicated dashboard of tiles, summaries, and trend series.
- **Customer intelligence** powered by Appriss's Linking 2.0 identity resolution, surfacing a 360-degree view of each shopper across IDs, transactions, channels, and locations.
- **Near-real-time activity** that surfaces recent return actions shortly after they happen (expect roughly a 12-hour lag depending on POS/portal feeds), so an investigation starts from current reality rather than yesterday's data.
- **Investigation tools** such as customer search, customer profiles, pinned profiles, and alerts that let you move from a top-line number straight to the specific customer, store, SKU, or employee behind it.

It is structured as **four dashboards** plus **two supporting tools** (accessible via Insights but not exclusive to it — Customer Search and Customer Profile):

| Tool | Best used for |
|---|---|
| Overview Dashboard | Understanding the overall financial impact of Engage, spotting trends across stores, customers, & SKUs, and reviewing near-real-time denials & warnings across the business. |
| Return Metrics Dashboard | Taking a deep look at Returns Authorization performance — volume & value, core rates (actions, denials, overrides, calls) and their trends, denial/warning type breakdowns, and day-over-day metric trends. |
| Claims Metrics Dashboard (requires claims data integration) | Taking a deep look at Claims Authorization performance — appeasement request volume, warned & denied amounts, & denial rates across a rolling 30 days and fiscal YTD, plus 12-month trend charts. |
| Incent Metrics Dashboard (requires Incent implementation) | Measuring the financial upside of the Return Incentives program — issuance, redemption, redemption rate, Recovered Returns (additional sales, gross profit, purchases), and program economics (basket size, COGS, gross profit). |
| Customer Search | Searching for a specific customer using a variety of identifiers. **Not yet documented** — the doc site lists this page as "Coming Soon." Don't invent details; tell the user it isn't published yet and to check with their CSM or the doc site directly. |
| Customer Profile | Investigating an individual customer's retail behavior (purchases, returns, claims) and linked identities. **Not yet documented** — same caveat as Customer Search. |

**Need Help?** For anything Engage Insights, access, or program-application questions this skill can't resolve, the standard answer across every page of the guide is: contact your Customer Success Manager.

## Reference files — read before answering

Each dashboard has an extensive reference file with full mechanics, every figure/screenshot from the doc site, common workflows, a troubleshooting table, and a glossary. Read the one(s) relevant to the question — for cross-dashboard questions (e.g. "how does Overview relate to Return Metrics"), read both.

- `references/overview-dashboard.md` — Return Auth Value banner, Date Range filter, Returns & Claims tiles, Actions tile (map + table + export), Returns & Claims Flow diagram, Engage Metrics Summary (donut charts), Top 50 Return Drivers (4 tables), Data Health, three common workflows, troubleshooting, glossary.
- `references/return-metrics-dashboard.md` — the four-part filter bar (Date Range, Channel, Return Type, Location), Engage Returns tile, Actions tile, the eight Core Metrics cards and their Show Rates / Amounts-Counts toggles, trend indicators and drill-in graphs, Action Profiles pie chart, Metric Series builder, three common workflows, troubleshooting, glossary.
- `references/claims-metrics-dashboard.md` — Last 30 Days and Fiscal Year-to-Date bands, the four claims metrics (Total Appeasement Requests, Warned Amount, Denied Amount, Denied Rate), the Amounts/Counts toggle, the Appeasements and Actions 12-month trend charts, glossary.
- `references/incent-metrics-dashboard.md` — how the Incent program mechanically works (receipt-printed offer → redemption → Purchase After Return), the Date Range control, Incent Overview (Total Issued, Total Redeemed, Redemption Rate + chart), PAR Overview (Additional Sales/Gross Profit/Purchases + per-return economics + detail table), Incent Impact Summary (9-column program economics row), glossary.

Screenshots for every numbered figure referenced in the text live under `assets/screenshots/<dashboard-name>/figure-NN.jpg` and are linked inline in each reference file.

## Answering patterns

**"What does X tile/metric/toggle do?"** → find the dashboard, read that reference file, quote the relevant section (including the exact table row if it's a metric definition). Don't paraphrase metric formulas — get them exact (e.g. Denied Rate = Denied Amount ÷ Total Appeasement Requests; Redemption Rate = Total Redeemed ÷ Total Issued; PAR Rate = PAR Count ÷ Trackable Returns).

**"Why does my number look wrong / why didn't it update?"** → check the Troubleshooting table in the relevant reference file first. The single most common cause across all four dashboards is forgetting to click Apply after changing a filter or date range — every dashboard explicitly warns about this. The second most common cause is not stating which toggle view (Show Rates on/off, Amounts $ vs Counts) a figure came from, since the same card shows genuinely different numbers depending on the toggle.

**"How do I investigate/find [a suspicious customer, store, SKU, employee]?"** → use the "common workflows" sections in `overview-dashboard.md` and `return-metrics-dashboard.md`. These are pre-built investigative sequences (daily monitoring, investigating a suspicious shopper, preparing a store/regional review, diagnosing a rise in denials, investigating a flagged store, reviewing a rule change).

**Explaining a dashboard to a customer (QBR/demo context)** → lead with the Return Auth Value banner (Overview) for program-level ROI, since that's explicitly the number built for exec readouts; it is NOT clickable and does NOT respond to the date range filter (fixed trailing-365-day window) — flag that distinction, it trips people up.

**Terminology questions** → each reference file has its own glossary; the terms mostly don't repeat across dashboards except a few shared ones (BORIS, BORO, Amounts/Counts toggle, Non-Receipted). Use the glossary in the dashboard the term appears in.

## Key facts easy to get wrong

- **Return Auth Value** (Overview) is fixed to a trailing 365-day window and never responds to the Date Range filter — this is deliberate, not a bug.
- **Claims Metrics** has no adjustable date range at all — it's fixed to Last 30 Days and Fiscal YTD, plus a rolling-12-months chart. This is a status board, not an investigation surface, by design.
- **Incent Metrics** date range has only three presets (Last Week, Last Month, Last Year) — no custom range in this release.
- A **denial rate** (or any Core Metrics/Claims figure) is meaningless without stating whether it's dollar-weighted (Amounts $) or transaction-weighted (Counts) — the two are "genuinely different figures," not formatting variants.
- **Non-receipted returns** are explicitly called out as "where fraud and abuse concentrate" — this is the fastest filter to reach for when investigating abuse.
- **Trackable Returns** (Incent) will normally be lower than total return count — it's the subset the program could actually attach and follow an incentive on.
- The Claims Metrics and Incent Metrics dashboards only appear if the org has, respectively, a Claims Data integration or an Incent implementation — their absence from a customer's platform is expected, not a defect.
- Actions/near-real-time data has an ~12-hour lag depending on POS/digital-returns-portal/claims-portal feed timing.

## Scope note

This skill covers the four Engage Insights dashboards (Overview, Return Metrics, Claims Metrics, Incent Metrics) as documented at `docs.apprissretail.com/products/product-docs/appriss-engage/user-guides/engage-insights`. The Customer Search & Profiles page under the same Insights section is listed on the doc site as "Coming Soon" with no published content as of this skill's creation — do not fabricate its behavior. If asked about it, say it isn't documented yet and point to the CSM or doc site for the latest.

If the doc site publishes updates to any dashboard (new tiles, changed formulas, new filters), this skill will need a refresh — treat conflicting live-product behavior as a signal to update the reference files, not as something to silently override in an answer.
