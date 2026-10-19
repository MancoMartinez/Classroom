---
name: cap-hours-report
description: >
  Generates Appriss Retail's monthly Engineering Capitalizable Hours report from Jira.
  Use this skill whenever the user asks for a capitalization report, capitalizable hours,
  cap hours, or wants to know how many hours the engineering team can capitalize for a
  given month or sprint. Also triggers on phrases like "run the cap report", "pull
  capitalizable hours for [month]", "generate engineering capitalization for Q[N]",
  or any request to process ENG/DATASCI Jira issues into a capitalizable hours Excel file.
  If the user mentions story points and capitalization in the same breath — use this skill.
---

# Capitalizable Hours Report — Appriss Retail Engineering

This skill pulls completed Jira work items for a given sprint month, resolves each
item's full ancestry chain live from Jira (leaf → epic → initiative), classifies each
as capitalizable or non-capitalizable, converts story points to hours per engineer,
and outputs a formatted two-tab Excel workbook.

---

## Quick Reference

- **Jira Cloud ID:** `7eb600cf-c7e0-43ed-acc4-90b277d43514` (trebuco.atlassian.net)
- **Projects:** `ENG` (sprint filter) + `DATASCI`, `RETAILIT`, `CE` (resolution date filter)
- **Output:** Two-tab Excel — Summary (per-engineer) + Work Item Detail
- **Scripts:** `scripts/classify.py` → `scripts/build_report.py`
- **Rules reference:** `references/classification_rules.md`

---

## Always-CAP Terms

The following terms, when found anywhere in the combined context of a work item
(its own summary/type/category + its epic name/desc + its initiative name/desc),
**always result in a Capitalizable classification**, regardless of other rules.
This list is maintained in `classify.py` under `ALWAYS_CAP_TERMS`:

- `engage insights`
- `sidekick`
- `engage models`
- `engage for shopify`
- `action a search`
- `data facteus`
- `dark mode`
- `engage for secure`
- `linking 2.0`
- `engage alerts`
- `securegpt`

When adding a new product initiative that should always be capitalizable, add its
name (lowercase) to `ALWAYS_CAP_TERMS` in `classify.py`.

---

## Step-by-Step Workflow

### 1. Confirm the Month

If the user hasn't specified a month, ask. You need:
- Month name (e.g., "April 2026")
- The sprint name as it appears in Jira — typically the same string (e.g., "April 2026")

Determine working days and available hours for the month. US federal holidays reduce
working days from the calendar count. See the table in `references/classification_rules.md`
for pre-computed values. For months not listed, count business days minus US federal
holidays, then multiply by 6 productive hrs/day.

### 2. Fetch ENG Issues (Sprint Filter + Pagination)

ENG uses sprint membership, not resolution date, because resolution dates can be
manipulated after a sprint closes.

**Base JQL:**
```
project = ENG AND sprint = "{Month Year}" AND statusCategory = Done ORDER BY key ASC
```

**Pagination pattern** — the Jira MCP caps results at 100 per call:
- Batch 1: run the base JQL, collect all results, note the last key (e.g., `ENG-2500`)
- Batch 2+: append `AND key > "ENG-XXXX"` to fetch the next page
- Stop when a batch returns fewer than 100 results

For each issue, immediately walk its ancestry chain (see § "Walk Ancestry" below).

Flatten each issue into this JSON structure per line (JSONL):
```json
{
  "key": "ENG-1234",
  "summary": "Story summary text",
  "assignee": "Jane Smith",
  "type": "Story",
  "points": 3,
  "work_category": "Feature Development",
  "resolutiondate": "2026-04-15T10:00:00.000+0000",
  "product_and_modules": "Engage",
  "resolved_epic": "PRODUCT-353",
  "resolved_epic_summary": "Search Composer Skill",
  "resolved_epic_desc": "First 500 chars of the epic's description field",
  "resolved_initiative": "PRODUCT-351",
  "resolved_initiative_name": "Appriss Sidekick",
  "resolved_initiative_desc": "First 500 chars of the initiative's description field"
}
```

Jira field mappings (leaf issue):
- `points` ← `customfield_10173`
- `work_category` ← `customfield_20316` (may come back as `{"value": "Feature Development", ...}`)
- `product_and_modules` ← `customfield_22202` (cascading select; capture only the top-level `.value`)
- `parent_key` ← `fields.parent.key` (direct parent; used as starting point for ancestry walk)
- `sprint` ← `customfield_10670`

Save to `{month_slug}_eng_all.jsonl` (e.g., `apr_eng_all.jsonl`).
Merge all batches: `cat apr_eng_b1.jsonl apr_eng_b2.jsonl ... > apr_eng_all.jsonl`

### 3. Fetch DATASCI, RETAILIT, and CE Issues (Resolution Date Filter + Pagination)

DATASCI, RETAILIT, and CE don't use sprints the same way as ENG — use resolution date instead.

**Base JQL (substitute the project key):**
```
project = DATASCI AND resolutiondate >= "{YYYY-MM-01}" AND resolutiondate <= "{YYYY-MM-31}" AND statusCategory = Done ORDER BY key ASC
```

Run the same query for `RETAILIT` and `CE`.

Paginate the same way as ENG. For each issue, walk its ancestry chain (see § "Walk Ancestry").
Save to separate files:
- `{month_slug}_datasci_all.jsonl`
- `{month_slug}_retailit_all.jsonl`
- `{month_slug}_ce_all.jsonl`

If a project returns 0 results, skip its file. Typical counts: DATASCI 70–120 items;
RETAILIT and CE may be smaller.

### 4. Walk Ancestry (for every issue)

**This is the core architectural change**: ancestry is always resolved live from Jira.
No static lookup tables are used. Every issue must carry its resolved epic and initiative
before classify.py is run.

For each issue:

1. Start with `parent_key` from the issue's own fields (this is the direct parent).
2. Fetch that parent from Jira. Capture its `summary` and the first 500 chars of its
   `description`. Note its `issue_type`.
3. If the parent is an **epic** (issue_type = "Epic") that itself has a parent (a
   PRODUCT-XXX initiative key in its own `parent.key` field), you've found both levels —
   set `resolved_epic` = the epic key, `resolved_initiative` = the PRODUCT-XXX key.
4. If the parent's type suggests it's an intermediate level (Story, Task, Sub-task),
   keep walking up: fetch that parent's parent, and so on, until you reach an Epic or
   a PRODUCT-XXX key, or until there's no further parent.
5. The topmost PRODUCT-XXX key you find becomes `resolved_initiative`. The first Epic-type
   key in the chain becomes `resolved_epic`. Also fetch the initiative's summary and
   first 500 chars of description for `resolved_initiative_name` and `resolved_initiative_desc`.
6. If no parent exists (orphan issue), set all resolved fields to `""` / `null`.

**Batch fetching:** Don't fetch each parent one by one if you can avoid it. Collect all
unique parent keys from a batch of issues, then fetch them in one Jira call. Repeat for
the next level up the chain. Most chains are 2–3 levels deep.

**Caching within a run:** Keep a dict of `key → {summary, description, type, parent_key}`
for nodes you've already fetched. Most epics appear many times across a month's issues.

### 5. Run classify.py

```bash
python scripts/classify.py \
  --month "April 2026" \
  --working-days 22 \
  --eng-file apr_eng_all.jsonl \
  --datasci-file apr_datasci_all.jsonl \
  --retailit-file apr_retailit_all.jsonl \
  --ce-file apr_ce_all.jsonl \
  --output apr_classified.json
```

All `--*-file` arguments are optional — omit any project that returned no issues.

The `--anthropic-api-key` flag (or `ANTHROPIC_API_KEY` env var) enables AI-assisted
classification for items that don't match any explicit rule. Without a key, those items
default to Non-Capitalizable.

**Classification logic (applied in order):**

1. **Always-CAP keyword match** — if any term from `ALWAYS_CAP_TERMS` appears in the
   combined text of the item + epic + initiative → CAP. Reasoning states which term matched.
2. **Bug / maintenance / research** — Bug type, Bug category, Maintenance, Support,
   Implementation Support, Configuration Change, Research → NOT cap.
3. **Known initiative decision** — if `resolved_initiative` matches a key in
   `KNOWN_INITIATIVES`, use that decision (CAP or NOT cap).
4. **Always-NOT-CAP keyword match** — terms like "business as usual", "tech debt",
   "customer migration" → NOT cap.
5. **Feature Development with no epic** → NOT cap (can't confirm scope).
6. **Feature Development with resolved epic** → CAP.
7. **AI-assisted fallback** — calls Anthropic API with full context; result flagged amber
   in report for review.
8. **Default** → NOT cap.

**AI-assisted items** are marked `"Capitalizable (AI-Assisted)"` or
`"Non-Capitalizable (AI-Assisted)"` in the Status column, highlighted amber in the
Excel report, and listed in the console output for your review.

### 6. Generate the Excel Report

```bash
python scripts/build_report.py \
  --input apr_classified.json \
  --output "Capitalizable Hours - April 2026.xlsx"
```

Save the output to the user's workspace folder.

### 7. Verify and Present

Do a quick sanity check before presenting:
- Total items = ENG batch total + DATASCI total + RETAILIT total + CE total
- Review all AI-assisted items (amber rows in the Detail tab) — confirm or override
- Scan for engineers with 100% capitalizable rate and very low point totals (data quality flag)
- Check that total capitalizable hours looks reasonable vs. prior months
- Confirm Engage + Secure + Other sum to total capitalizable hours per engineer

Present the file with a brief summary:
- Total items processed
- Capitalizable vs. non-capitalizable count (note how many were AI-assisted)
- Total capitalizable hours broken down by Engage / Secure / Other
- Any engineers flagged for low point count
- Any AI-assisted items that need the user's review

---

## Output Format

**Tab 1 — Summary**
- One row per engineer
- Columns: Engineer, Total Items, Total Story Points, Capitalizable Items,
  Capitalizable Points, Hrs/Point, Available Hours, Capitalizable Hours, Non-Cap Hours,
  % Capitalizable, Engage Cap Hrs, Secure Cap Hrs, Other Cap Hrs, Data Quality Flag
- Navy header, alternating row shading, green highlighting on Capitalizable Hours and %
  columns; teal highlighting on the three product breakdown columns
- Engage + Secure + Other always equals Capitalizable Hours per engineer

**Tab 2 — Work Item Detail**
- One row per Jira issue, sorted by assignee then key
- Columns: Jira Key (hyperlinked), Assignee, Type, Story Points, Work Category, Epic,
  Epic Summary, Initiative, Initiative Name, Product Category, Resolution Date, Status,
  Reasoning, Summary
- **Green** row = rule-based Capitalizable
- **Amber** row = AI-Assisted (requires review)
- **Red** row = Non-Capitalizable
- Auto-filter enabled on all columns
- Legend row below title explains the colour coding

---

## Product Category Logic

Every capitalizable item is assigned to **Engage**, **Secure**, or **Other**. Three-tier priority:

1. **Direct field (ENG only)** — `product_and_modules` (customfield_22202):
   - `"Engage"` → Engage
   - `"Secure"`, `"Platform"`, `"Incident"` → Secure
   - Other values → fall through to tier 2

2. **Initiative mapping** — `INITIATIVE_TO_PRODUCT` in `classify.py` maps each known
   initiative key to a bucket.

3. **Keyword inference** — last resort: scans combined context for terms like "engage",
   "shopify", "sidekick", "ebr" etc.

---

## Data Quality Flag Logic

Engineers flagged = total story points < 10 AND cap points > 0.

The concern: very low total points causes hrs/point ratio to spike, potentially inflating
capitalizable hours to the full monthly cap. Usually means untracked work. Flag for manual review.

---

## Adding New Always-CAP Products

When a new product initiative is confirmed as always-capitalizable:

1. Add its name (lowercase) to `ALWAYS_CAP_TERMS` in `scripts/classify.py`
2. If it also has a known initiative key (PRODUCT-XXX), add it to `KNOWN_INITIATIVES`
   and `INITIATIVE_TO_PRODUCT`
3. Update `references/classification_rules.md` to keep the audit trail current

---

## Common Issues

**"I'm only getting 100 results for ENG"** — pagination needed. Keep fetching with
`AND key > "ENG-LAST-KEY"` until a batch returns < 100.

**DATASCI / RETAILIT / CE sprint filter returns 0** — expected. These projects don't use
sprint tracking; always use resolution date.

**work_category comes back as a dict** — `classify.py` normalizes this via `_str()`.

**Ancestry chain deeper than 2 levels** — walk as far up as needed until you hit a
PRODUCT-XXX key or run out of parents. The fetched description text at each level
enriches the context for both keyword matching and AI classification.

**Engineer at 100% cap with very few points** — the data quality flag highlights them
in red automatically.

**Unknown parent key mid-chain** — if a parent can't be fetched (deleted ticket, permission
error), note the gap in `resolved_epic_desc` / `resolved_initiative_desc` and let the
AI classifier or keyword rules work with what's available. Do not hardcode a mapping.
