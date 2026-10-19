"""
Capitalizable Hours Classifier — Appriss Retail Engineering
============================================================
Reads JSONL files of Jira issues (flat format), classifies each as
Capitalizable or Non-Capitalizable, then computes per-engineer hours
and writes a JSON payload ready for build_report.py.

IMPORTANT — Ancestry model
--------------------------
This script does NOT maintain a hardcoded epic-to-initiative lookup table.
Instead, each issue in the JSONL must already carry its fully-resolved
ancestry chain, populated by walking Jira live during the fetch step
(see SKILL.md § "Fetch and Walk Ancestry"). The expected new fields are:

    "resolved_epic":            "PRODUCT-353"          # direct epic / parent key
    "resolved_epic_summary":    "Search Composer Skill"
    "resolved_epic_desc":       "..."                  # first 500 chars of description
    "resolved_initiative":      "PRODUCT-351"          # top-level PRODUCT-XXX key
    "resolved_initiative_name": "Appriss Sidekick"
    "resolved_initiative_desc": "..."                  # first 500 chars of description

These fields are set by the caller (Claude walking Jira). classify.py
trusts them and never overrides them.

Always-CAP keyword rules
------------------------
Certain terms, when found anywhere in the concatenated text of a work item
(its own summary + type + work_category + its epic name/desc + its initiative
name/desc), guarantee a CAP classification regardless of other rules.
See ALWAYS_CAP_TERMS below. The reasoning column will note which term matched.

AI-assisted fallback
--------------------
When a work item doesn't match any explicit rule AND its initiative has no
hardcoded decision, the script calls the Anthropic API with the full context
of the item + its ancestry and asks Claude to make a CAP/NOT-CAP judgment
under ASC 350-40. These items are flagged "AI-Assisted" in the report
and should be reviewed by the user before the report is finalised.

Usage:
    python classify.py \\
        --month "April 2026" \\
        --working-days 22 \\
        --eng-file eng_issues.jsonl \\
        --datasci-file datasci_issues.jsonl \\
        --retailit-file retailit_issues.jsonl \\
        --ce-file ce_issues.jsonl \\
        --output classified.json \\
        [--anthropic-api-key sk-ant-...]   # optional; falls back to env ANTHROPIC_API_KEY

All --*-file arguments are optional; omit any that have no issues for the month.

Expected JSONL flat format per line (after ancestry walk):
    {
      "key":                    "ENG-1234",
      "summary":                "...",
      "assignee":               "Jane Smith",
      "type":                   "Story",
      "points":                 3,
      "work_category":          "Feature Development",
      "resolutiondate":         "2026-04-15T10:00:00.000+0000",
      "product_and_modules":    "Engage",
      "resolved_epic":          "PRODUCT-353",
      "resolved_epic_summary":  "Search Composer Skill",
      "resolved_epic_desc":     "...",
      "resolved_initiative":    "PRODUCT-351",
      "resolved_initiative_name": "Appriss Sidekick",
      "resolved_initiative_desc": "..."
    }
"""

import argparse
import json
import os
import urllib.request
import urllib.error
from collections import defaultdict, Counter

# ─── Constants ────────────────────────────────────────────────────────────────
NON_CAP          = "Non-Capitalizable"
CAP              = "Capitalizable"
AI_CAP           = "Capitalizable (AI-Assisted)"
AI_NON_CAP       = "Non-Capitalizable (AI-Assisted)"
LOW_POINT_THRESHOLD = 10

# ─── Always-CAP keyword terms ─────────────────────────────────────────────────
# If ANY of these strings appear (case-insensitive) anywhere in the combined
# text context of a work item (its own fields + its epic + its initiative),
# the item is always classified as Capitalizable — regardless of other rules.
#
# These represent initiatives or products that have been explicitly confirmed
# as capitalizable. Add new terms here when a product/initiative is confirmed.
ALWAYS_CAP_TERMS = [
    "engage insights",
    "sidekick",
    "engage models",
    "engage for shopify",
    "action a search",
    "data facteus",
    "dark mode",
    "engage for secure",
    "linking 2.0",
    "engage alerts",
    "securegpt",
]

# ─── Always-NOT-CAP keyword terms ─────────────────────────────────────────────
# Same idea in reverse: these guarantee NOT-CAP when matched in context.
# These are applied AFTER the always-CAP check, so CAP wins if both match.
ALWAYS_NOT_CAP_TERMS = [
    "business as usual",
    "tech debt",
    "tech roadmap",
    "bug backlog",
    "implementation support",
    "customer migration",    # individual customer data migrations
    "gap claims portal",
    "incident migration",
    "platform unification",
    "project calypso",
    "close data centers",
    "snowflake migration",
    "azure migration",
]

# ─── Initiative-level cap decisions (confirmed by Kenny) ──────────────────────
# Maps a top-level initiative key → (cap_decision, human_readable_name).
# These are authoritative: when a work item resolves to one of these initiatives,
# this decision is used and keyword/AI logic is skipped (except ALWAYS_CAP_TERMS
# still fire first above this level).
KNOWN_INITIATIVES = {
    # CAP
    "PRODUCT-376": (CAP,     "Engage Insights"),
    "PRODUCT-375": (CAP,     "Engage Models"),
    "PRODUCT-408": (CAP,     "Dark Mode"),
    "PRODUCT-351": (CAP,     "Appriss Sidekick"),
    "PRODUCT-409": (CAP,     "Action a Search"),
    "PRODUCT-653": (CAP,     "Data Facteus"),
    "PRODUCT-337": (CAP,     "Engage for Shopify"),
    # NOT CAP
    "PRODUCT-394": (NON_CAP, "Business as Usual"),
    "PRODUCT-395": (NON_CAP, "Tech Roadmap"),
    "PRODUCT-476": (NON_CAP, "Close Data Centers (Azure/Snowflake Migration)"),
    "PRODUCT-349": (NON_CAP, "Platform Unification"),
    "PRODUCT-347": (NON_CAP, "Product Adoption"),
    "PRODUCT-296": (NON_CAP, "Gap Claims Portal"),
}

# ─── Product categorization ───────────────────────────────────────────────────
# Maps the raw Jira "Product and Modules" field value → product bucket
PRODUCT_FIELD_MAP = {
    "Engage":    "Engage",
    "Secure":    "Secure",
    "Platform":  "Secure",
    "Incident":  "Secure",
}

# Maps a known initiative key → product bucket (fallback when field is absent)
INITIATIVE_TO_PRODUCT = {
    "PRODUCT-376": "Engage",
    "PRODUCT-375": "Engage",
    "PRODUCT-337": "Engage",
    "PRODUCT-409": "Engage",
    "PRODUCT-351": "Secure",
    "PRODUCT-408": "Secure",
    "PRODUCT-653": "Other",
    "PRODUCT-476": "Other",
    "PRODUCT-349": "Other",
    "PRODUCT-394": "Other",
    "PRODUCT-395": "Other",
    "PRODUCT-347": "Other",
    "PRODUCT-296": "Other",
}

_ENGAGE_KEYWORDS = ("engage", "linking", "retailer", "shopify", "vertex",
                    "search composer", "action a search", "insights", "claims model")
_SECURE_KEYWORDS = ("secure", "sidekick", "ebr", "incident", "dark mode",
                    "loss prevention", "lp ", "case ", "investigation")


# ─── Helpers ──────────────────────────────────────────────────────────────────

def _str(v):
    """Flatten Jira field dicts like {'value': 'Bug', 'id': '...'} to plain strings."""
    if isinstance(v, dict):
        return v.get("value", str(v))
    return v or ""


def _context_text(issue):
    """
    Build the combined text context used for keyword matching and AI prompts.
    Includes: the work item's own fields + its epic + its initiative.
    """
    parts = [
        issue.get("summary", ""),
        _str(issue.get("type", "")),
        _str(issue.get("work_category", "")),
        issue.get("resolved_epic_summary", ""),
        issue.get("resolved_epic_desc", ""),
        issue.get("resolved_initiative_name", ""),
        issue.get("resolved_initiative_desc", ""),
    ]
    return " ".join(p for p in parts if p).lower()


def classify_product(issue):
    """Return one of 'Engage' | 'Secure' | 'Other' for a single issue."""
    raw = issue.get("product_and_modules")
    if raw:
        bucket = PRODUCT_FIELD_MAP.get(raw)
        if bucket:
            return bucket

    init_key = issue.get("resolved_initiative", "")
    if init_key and init_key in INITIATIVE_TO_PRODUCT:
        return INITIATIVE_TO_PRODUCT[init_key]

    text = _context_text(issue)
    if any(k in text for k in _ENGAGE_KEYWORDS):
        return "Engage"
    if any(k in text for k in _SECURE_KEYWORDS):
        return "Secure"

    return "Other"


def _call_claude_for_cap_decision(issue, api_key):
    """
    Call Anthropic API to determine if a work item qualifies for capitalization
    under ASC 350-40. Returns (decision_str, reasoning_str, is_ai_assisted=True).
    """
    work_cat  = _str(issue.get("work_category", ""))
    prompt = f"""You are an accounting assistant helping Appriss Retail classify software
engineering work items as Capitalizable or Non-Capitalizable under ASC 350-40
(internal-use software accounting standard).

Under ASC 350-40, costs are capitalizable during the APPLICATION DEVELOPMENT STAGE
when they are incurred to develop or obtain software for INTERNAL USE that provides
SIGNIFICANT NEW FUNCTIONALITY available to ALL USERS. The following costs are NOT
capitalizable:
- Bug fixes and maintenance
- Individual customer-specific work
- Infrastructure migration (moving existing functionality to new platform)
- Research/pre-feasibility work
- General support, operations, and administration
- Work that improves internal tooling only (not user-facing product)

Here is the work item to classify:

KEY: {issue.get("key")}
SUMMARY: {issue.get("summary")}
TYPE: {_str(issue.get("type"))}
WORK CATEGORY: {work_cat}
STORY POINTS: {issue.get("points")}

PARENT EPIC: {issue.get("resolved_epic", "none")} — {issue.get("resolved_epic_summary", "")}
EPIC DESCRIPTION: {issue.get("resolved_epic_desc", "(none)")}

INITIATIVE: {issue.get("resolved_initiative", "none")} — {issue.get("resolved_initiative_name", "")}
INITIATIVE DESCRIPTION: {issue.get("resolved_initiative_desc", "(none)")}

Respond with ONLY a JSON object (no markdown, no explanation outside the JSON):
{{
  "decision": "Capitalizable" or "Non-Capitalizable",
  "confidence": "high" or "medium" or "low",
  "reasoning": "One or two sentences explaining why, citing the specific ASC 350-40 criteria that apply."
}}"""

    payload = json.dumps({
        "model": "claude-sonnet-4-6",
        "max_tokens": 300,
        "messages": [{"role": "user", "content": prompt}]
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=payload,
        headers={
            "Content-Type":      "application/json",
            "x-api-key":         api_key,
            "anthropic-version": "2023-06-01",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.loads(resp.read().decode("utf-8"))
        text = body["content"][0]["text"].strip()
        # Strip markdown fences if present
        if text.startswith("```"):
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]
        result = json.loads(text.strip())
        raw_decision = result.get("decision", "")
        reasoning    = result.get("reasoning", "No reasoning provided.")
        confidence   = result.get("confidence", "unknown")
        if "Non-Capitalizable" in raw_decision:
            return AI_NON_CAP, f"[AI-Assisted, confidence={confidence}] {reasoning}"
        else:
            return AI_CAP, f"[AI-Assisted, confidence={confidence}] {reasoning}"
    except Exception as e:
        return AI_NON_CAP, f"[AI-Assisted — API error: {e}] Defaulting to Non-Capitalizable."


def classify(issue, api_key=None):
    """
    Return (cap_status, reasoning_string, is_ai_assisted) for one Jira issue.

    Priority order:
      1. Always-CAP keyword match (in combined context text)
      2. Bug / maintenance / research work category rules
      3. Known initiative decision (KNOWN_INITIATIVES table)
      4. Always-NOT-CAP keyword match
      5. Feature Development with no resolved epic → NOT cap
      6. Feature Development with resolved epic → CAP
      7. AI-assisted fallback (calls Anthropic API if api_key provided)
      8. Conservative NOT cap default
    """
    work_cat  = _str(issue.get("work_category", ""))
    issue_type = _str(issue.get("type", ""))
    init_key  = issue.get("resolved_initiative", "")
    epic_key  = issue.get("resolved_epic", "")
    epic_sum  = issue.get("resolved_epic_summary", epic_key)
    init_name = issue.get("resolved_initiative_name", init_key)
    context   = _context_text(issue)

    # ── Rule 1: Always-CAP keyword match ──────────────────────────────────────
    for term in ALWAYS_CAP_TERMS:
        if term in context:
            return CAP, f'Always-CAP term matched: "{term}" found in work item context', False

    # ── Rule 2: Bug / maintenance / research ──────────────────────────────────
    if issue_type == "Bug" or work_cat == "Bug":
        return NON_CAP, "Bug fix — maintenance cost, not capitalizable", False
    if work_cat in ("Maintenance", "Support", "Implementation Support", "Configuration Change"):
        return NON_CAP, f"'{work_cat}' — operational/support work, not capitalizable", False
    if work_cat == "Research":
        return NON_CAP, "Research/R&D — pre-feasibility, not capitalizable", False

    # ── Rule 3: Known initiative decision ─────────────────────────────────────
    if init_key and init_key in KNOWN_INITIATIVES:
        decision, name = KNOWN_INITIATIVES[init_key]
        return decision, f"{name} initiative (confirmed {decision.lower()}); epic: '{epic_sum}'", False

    # ── Rule 4: Always-NOT-CAP keyword match ──────────────────────────────────
    for term in ALWAYS_NOT_CAP_TERMS:
        if term in context:
            return NON_CAP, f'Always-NOT-CAP term matched: "{term}" found in work item context', False

    # ── Rule 5: Feature Development with no parent epic ───────────────────────
    if work_cat == "Feature Development" and not epic_key:
        return NON_CAP, "Feature Development with no resolved parent epic — cannot confirm scope; defaulting not capitalizable", False

    # ── Rule 6: Feature Development with resolved epic ────────────────────────
    if work_cat == "Feature Development" and epic_key:
        return CAP, f"Feature Development under '{epic_sum}' / '{init_name}' — presumed capitalizable", False

    # ── Rule 7: AI-assisted fallback ──────────────────────────────────────────
    if api_key:
        decision, reasoning = _call_claude_for_cap_decision(issue, api_key)
        return decision, reasoning, True

    # ── Rule 8: Conservative default ─────────────────────────────────────────
    return NON_CAP, f"No rule matched; defaulting to not capitalizable (work_category='{work_cat}', epic='{epic_key}')", False


def load_issues(filepath, source_label):
    issues = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line:
                issues.append({**json.loads(line), "_source": source_label})
    return issues


def run(month, working_days, eng_file, datasci_file, retailit_file, ce_file,
        output_file, api_key=None):
    productive_hrs = working_days * 6

    all_issues = []
    sources = [
        (eng_file,      "ENG (sprint)"),
        (datasci_file,  "DATASCI (resolution date)"),
        (retailit_file, "RETAILIT (resolution date)"),
        (ce_file,       "CE (resolution date)"),
    ]
    for fpath, label in sources:
        if not fpath:
            continue
        batch = load_issues(fpath, label)
        print(f"  Loaded {len(batch)} issues from {label}")
        all_issues.extend(batch)

    results          = []
    ai_assisted_keys = []    # items whose classification used the AI fallback
    review_required  = []    # items flagged for human review

    for issue in all_issues:
        status, reasoning, is_ai = classify(issue, api_key=api_key)

        if is_ai:
            ai_assisted_keys.append(issue["key"])

        # AI-assisted items are always flagged for review
        needs_review = is_ai

        product_cat = classify_product(issue)

        results.append({
            **issue,
            "cap_status":   status,
            "reasoning":    reasoning,
            "needs_review": needs_review,
            "product_category": product_cat,
            # Preserve ancestry fields (already in issue from fetch step, re-emit for clarity)
            "resolved_epic":              issue.get("resolved_epic", ""),
            "resolved_epic_summary":      issue.get("resolved_epic_summary", ""),
            "resolved_initiative":        issue.get("resolved_initiative", ""),
            "resolved_initiative_name":   issue.get("resolved_initiative_name", ""),
        })

    # ── Summary output ────────────────────────────────────────────────────────
    if ai_assisted_keys:
        print(f"\n  ⚠  {len(ai_assisted_keys)} item(s) classified by AI — flag for review:")
        for k in sorted(ai_assisted_keys):
            print(f"    {k}")
        print()

    counts = Counter(r["cap_status"] for r in results)
    print(f"\n  Total: {len(results)}")
    for status, n in sorted(counts.items()):
        print(f"    {status}: {n}")

    # Per-engineer summary
    engineer_items = defaultdict(list)
    for r in results:
        engineer_items[r["assignee"]].append(r)

    summary_rows = []
    for eng in sorted(engineer_items.keys()):
        items     = engineer_items[eng]
        total_pts = sum((i.get("points") or 0) for i in items)
        cap_pts   = sum(
            (i.get("points") or 0) for i in items
            if i["cap_status"] in (CAP, AI_CAP)
        )
        if total_pts > 0:
            hrs_per_pt = productive_hrs / total_pts
            cap_hrs    = round(cap_pts * hrs_per_pt, 1)
            cap_pct    = round(cap_pts / total_pts * 100, 1)
        else:
            hrs_per_pt = 0
            cap_hrs    = 0.0
            cap_pct    = 0.0

        def _prod_cap_hrs(prod):
            pts = sum(
                (i.get("points") or 0)
                for i in items
                if i["cap_status"] in (CAP, AI_CAP) and i.get("product_category") == prod
            )
            return round(pts * hrs_per_pt, 1) if total_pts > 0 else 0.0

        summary_rows.append({
            "engineer":       eng,
            "total_pts":      total_pts,
            "cap_pts":        cap_pts,
            "hrs_per_pt":     round(hrs_per_pt, 2),
            "cap_hrs":        cap_hrs,
            "cap_pct":        cap_pct,
            "item_count":     len(items),
            "cap_item_count": sum(1 for i in items if i["cap_status"] in (CAP, AI_CAP)),
            "engage_cap_hrs": _prod_cap_hrs("Engage"),
            "secure_cap_hrs": _prod_cap_hrs("Secure"),
            "other_cap_hrs":  _prod_cap_hrs("Other"),
        })

    with open(output_file, "w") as f:
        json.dump({
            "month":          month,
            "working_days":   working_days,
            "productive_hrs": productive_hrs,
            "results":        results,
            "summary":        summary_rows,
        }, f, indent=2)

    print(f"\n  Saved classified data → {output_file}")
    print(f"  Total capitalizable hours: {sum(r['cap_hrs'] for r in summary_rows):.1f}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--month",           required=True,  help='e.g. "April 2026"')
    p.add_argument("--working-days",    required=True,  type=int)
    p.add_argument("--eng-file",        default=None)
    p.add_argument("--datasci-file",    default=None)
    p.add_argument("--retailit-file",   default=None)
    p.add_argument("--ce-file",         default=None)
    p.add_argument("--output",          default="classified.json")
    p.add_argument("--anthropic-api-key", default=None,
                   help="Anthropic API key for AI-assisted fallback classification. "
                        "Falls back to ANTHROPIC_API_KEY env var if not provided.")
    args = p.parse_args()

    api_key = args.anthropic_api_key or os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("  ℹ  No Anthropic API key found — AI-assisted fallback will use conservative default.")

    run(args.month, args.working_days, args.eng_file, args.datasci_file,
        args.retailit_file, args.ce_file, args.output, api_key=api_key)
