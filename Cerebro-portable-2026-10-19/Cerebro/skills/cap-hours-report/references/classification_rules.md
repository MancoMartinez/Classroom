# Capitalizable Hours — Classification Rules

This document is the authoritative reference for how Jira work items are classified
as Capitalizable or Non-Capitalizable for Appriss Retail's engineering capitalization report.

---

## Core Principle

ASC 350-40 (internal-use software) allows capitalization of costs once **technological
feasibility** is established for a new product or significant new functionality for **all users**.
Costs incurred for maintenance, bug fixes, individual-customer work, or infrastructure
migration do NOT qualify.

---

## Ancestry Model

**Ancestry is always resolved live from Jira at report-run time.** There are no hardcoded
epic-to-initiative lookup tables. Each work item's full ancestry chain (leaf → epic → initiative)
is walked by fetching parent keys from Jira during the data collection step. The resolved
epic and initiative fields are stored in the JSONL and passed through to classify.py.

This means if a ticket is reparented in Jira, the report will automatically reflect the
new ancestry the next time it is run.

---

## Classification Priority Order

Rules are applied top-to-bottom. The first matching rule wins.
"Context" = combined text of the work item's summary, type, work category, plus its
resolved epic name/description and resolved initiative name/description.

| # | Condition | Decision | Rationale |
|---|-----------|----------|-----------|
| 1 | Any Always-CAP term found in context (see table below) | **CAP** | Explicitly confirmed capitalizable product/initiative |
| 2 | Issue type = Bug OR work_category = "Bug" | **NOT cap** | Bug fixes are maintenance |
| 3 | work_category ∈ {Maintenance, Support, Implementation Support, Configuration Change} | **NOT cap** | Operational/support work |
| 4 | work_category = "Research" | **NOT cap** | Pre-feasibility R&D |
| 5 | resolved_initiative in KNOWN_INITIATIVES → CAP entries | **CAP** | Confirmed capitalizable initiative |
| 6 | resolved_initiative in KNOWN_INITIATIVES → NOT cap entries | **NOT cap** | Confirmed non-capitalizable initiative |
| 7 | Any Always-NOT-CAP term found in context (see table below) | **NOT cap** | Confirmed non-capitalizable category |
| 8 | work_category = "Feature Development" AND no resolved epic | **NOT cap** | Can't confirm scope without ancestry |
| 9 | work_category = "Feature Development" AND resolved epic present | **CAP** | Development toward new features |
| 10 | AI-assisted fallback (Anthropic API call with full context) | **CAP or NOT cap (AI)** | Best judgment under ASC 350-40; flagged amber for review |
| 11 | Default / catch-all | **NOT cap** | Conservative default |

---

## Always-CAP Terms

When any of these strings appear (case-insensitive) in the combined context of a work item,
the item is **always Capitalizable** regardless of other rules. These represent products
and initiatives that Kenny has explicitly confirmed as capitalizable.

| Term | Rationale |
|------|-----------|
| `engage insights` | New product capabilities for all users |
| `sidekick` | New AI product |
| `engage models` | New ML product capabilities |
| `engage for shopify` | New Shopify integration |
| `action a search` | New search product feature |
| `data facteus` | New data platform |
| `dark mode` | New feature for all users |
| `engage for secure` | New product feature |
| `linking 2.0` | New product capability |
| `engage alerts` | New product capability |
| `securegpt` | Confirmed capitalizable feature work |

To add a new always-CAP product, add its name (lowercase) to `ALWAYS_CAP_TERMS` in
`scripts/classify.py` and add a row here.

---

## Always-NOT-CAP Terms

When any of these strings appear (case-insensitive) in the combined context of a work item,
and no Always-CAP term was matched first, the item is **always Non-Capitalizable**.

| Term | Rationale |
|------|-----------|
| `business as usual` | Routine maintenance and support |
| `tech debt` | Infrastructure/technical debt work |
| `tech roadmap` | Tech debt, pen tests, performance work |
| `bug backlog` | Bug fix maintenance work |
| `implementation support` | Client onboarding/support |
| `customer migration` | Single-customer data migrations |
| `gap claims portal` | Single-customer engagement |
| `incident migration` | Infrastructure migration |
| `platform unification` | Infrastructure/migration work |
| `project calypso` | Platform unification sub-project |
| `close data centers` | Azure/Snowflake migration infrastructure |
| `snowflake migration` | Infrastructure migration |
| `azure migration` | Infrastructure migration |

---

## Known Initiative Decisions

These top-level initiative keys have explicit cap decisions confirmed by Kenny.
When a work item's ancestry resolves to one of these, the decision is applied directly
(after Always-CAP keyword check).

| Initiative Key | Name | Decision | Notes |
|----------------|------|----------|-------|
| PRODUCT-376 | Engage Insights | **CAP** | New product capabilities for all users |
| PRODUCT-375 | Engage Models | **CAP** | New ML models for all users |
| PRODUCT-408 | Dark Mode | **CAP** | New feature for all users |
| PRODUCT-351 | Appriss Sidekick | **CAP** | New AI product |
| PRODUCT-409 | Action a Search | **CAP** | New search feature |
| PRODUCT-653 | Data Facteus | **CAP** | New data platform |
| PRODUCT-337 | Engage for Shopify | **CAP** | New Shopify integration |
| PRODUCT-394 | Business as Usual | **NOT cap** | Routine maintenance & support |
| PRODUCT-395 | Tech Roadmap | **NOT cap** | Tech debt, pen tests, perf work |
| PRODUCT-476 | Close Data Centers | **NOT cap** | Azure/Snowflake migration |
| PRODUCT-349 | Platform Unification | **NOT cap** | Incident Migration, Calypso |
| PRODUCT-347 | Product Adoption | **NOT cap** | Streamline/impl work |
| PRODUCT-296 | Gap Claims Portal | **NOT cap** | Single customer engagement |

---

## AI-Assisted Classification

When no rule above produces a decision, `classify.py` calls the Anthropic API
(claude-sonnet-4-6) with the full context of the work item — including its own
summary, type, work category, and the name and description of its resolved epic
and initiative. The model is prompted to apply ASC 350-40 criteria and return a
structured JSON decision with confidence and reasoning.

AI-assisted items are:
- Marked `"Capitalizable (AI-Assisted)"` or `"Non-Capitalizable (AI-Assisted)"` in cap_status
- Highlighted **amber** in the Work Item Detail tab
- Listed in the console output when classify.py runs
- Intended for human review before the report is finalised

The confidence field in the reasoning column ("high", "medium", "low") indicates
how certain the model is; low-confidence items warrant closer scrutiny.

---

## Data Quality Flag

Engineers with **fewer than 10 total story points** completed in a sprint where **any
points are capitalizable** are highlighted in red in the Summary tab. A very low total
point count causes the capitalizable-hours figure to be inflated (potentially to the
full monthly cap). These engineers likely have untracked work in Jira.

---

## Working Days by Month (US Federal Holidays)

| Month | Working Days | Available Hrs/Engineer | Holidays Excluded |
|-------|-------------|------------------------|-------------------|
| January 2026 | 20 | 120 | New Year's (Jan 1), MLK Day (Jan 19) |
| February 2026 | 19 | 114 | Presidents' Day (Feb 16) |
| March 2026 | 22 | 132 | (none) |
| April 2026 | 22 | 132 | (none) |
| May 2026 | 21 | 126 | Memorial Day (May 25) |
| June 2026 | 22 | 132 | (none) |
| July 2026 | 23 | 138 | Independence Day (Jul 3 observed) |

Working days = business days in the month minus US federal holidays.
Productive hours = working days × 6 hrs/day.
