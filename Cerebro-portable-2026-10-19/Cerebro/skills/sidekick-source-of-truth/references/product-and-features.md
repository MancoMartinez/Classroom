# Sidekick — Product & Features

## What Sidekick can do today

1. **Build and run searches** across all data areas in natural language — transactions, work items, cashier activity, and more
2. **Look up** transactions by ID or filter, store profiles, and cashier details
3. **Surface, filter, and summarize** work items, investigations, and cases
4. **Run ad-hoc analyses** on any result set, segmented into high/medium/low findings
5. **Take actions** — assign work items, close incidents, add audit action plans, generate AI case synopses, link related cases
6. **Open dashboards, quick links, and saved reports** directly from chat

Result grids are capped at 20 items per query. For larger pulls, searches run in the background and land in the Search menu automatically. On-demand analyses typically complete in ~5 minutes.

## What Sidekick cannot do

- Does not generate content unrelated to LP, AP, or operations workflows
- Does not write external reports or emails
- Does not make autonomous decisions requiring human judgment
- Does not decline returns (that is Decision Intelligence, not Sidekick)
- Does not escalate a case or dispatch to law enforcement without user approval
- Does not act outside a user's existing platform permissions

**Human-in-the-loop is a core design principle.** For irreversible actions, Sidekick prompts for confirmation. Every action requires user approval.

---

## Configuration levels

Retailers decide which level to enable. User-level permissions always also apply.

| Level | Name | What Sidekick can do | Data exposure |
|---|---|---|---|
| 1 | Basic Knowledge | Answer product questions, navigation help | Zero — no retailer data |
| 2 | Search & Navigate | Build/modify searches, find dashboards/quick links/reports | Zero — no sensitive data |
| 3 | View Data | Read work items, cases, audits, store/cashier profiles | Requires approval |
| 4 | Full Workflow | Transaction-level data, attachments, workflow actions (assign, close, etc.) | Requires approval |

**Levels are cumulative** — each level includes all capabilities from the levels below it.

**InfoSec guidance:** Most customers start at Level 1 or 2 while review is in flight. Zero data exposure at those tiers. Graduate to deeper access when compliance team signs off.

---

## Admin-Level Memory (available May 29, 2026)

Lets you teach Sidekick your team's terminology and field preferences once — applies automatically thereafter.

- **Account-wide preferences (admins only):** Use plural phrasing — "We call cashiers associates." Cap: 50 entries.
- **Personal preferences (any user):** Use first-person — "For me, large receipt means over $500." Cap: 15 entries.
- Personal preferences always override account-wide ones for that individual user.
- Sidekick confirms scope after saving; gives one turn to correct.
- View preferences anytime: ask Sidekick "Show me my preferences."

This directly addresses the top beta feedback issue around Composer behavior on complex queries — users can now set preferences for always-on field behavior.

---

## Access & availability

- **GA:** June 9, 2026 (announced at NRF Protect)
- **How to access:** ✨ Sparkle icon, bottom-left corner of any Appriss platform screen
- **Browsers supported:** Chrome, Edge, Safari, Firefox (desktop only)
- **Mobile:** On roadmap based on demand — not yet available
- **Languages:** Optimized for English; works well with other languages; multi-language expansion on roadmap
- **Chat limit:** 50 chats per user per rolling period
- **Chat history:** 30 days, accessible via Navigation menu → Chat History
- **Time zone:** Uses the time zone from the user's Appriss profile

---

## Product by module

**Sidekick in Engage (Omni Returns & Claims)**
Compose plain-language queries about customer return histories, pull decision context instantly, run analyses on any result.

**Sidekick in Secure (Shrink & Exception Analytics)**
Compose multi-condition transaction and cashier searches in plain language; run ad-hoc analyses on demand; surface exception patterns the moment you ask.

**Sidekick in Incident (Case & Audit Management)**
Summarize open work items with timelines, assign cases directly inside the conversation, stitch investigation narratives in seconds.

**Cross-product power:**
Users with all three products get one conversation that spans all three. Ask "is this customer's return pattern showing up in any open cases?" and Sidekick pulls from Engage, Secure, and Incident in one response — no tab switching, no copy-paste.

---

## Demo outline (10-minute version)

Run scenarios in order. Each builds on the last. Use real client data — Sidekick is on in Staging for all clients. Default fallback: US Prod Client ID 15.

### Opening
Show sparkle icon ✨ location. Walk through Sidekick navigation (history, new conversation, feedback).
**Land this line:** "Sidekick doesn't just explain what happened. It helps you do something about it."

### Demo 1 — Find a specific item
**Scene:** LP professionals know something exists in the platform but can't surface it quickly.
- Prompt: "Show me all unassigned work items"
- Prompt: "Summarize work item 184727"
- Prompt: "Close it and add a note that the issue was resolved"
**Line:** "Find it. Act on it. All in the same conversation."

### Demo 2 — Store visit prep
**Scene:** What it used to take to prep for a store visit: 45 minutes of pulling exception reports, checking open cases, reviewing cashier activity.
- Prompt: "I'm visiting store 341. What are the open cases, investigations, and work items I should discuss with the store manager?"
**Line:** "45 minutes of prep work, gone. And now you walk in fully prepared."

### Demo 3 — Build a search in plain language
**Scene:** Pulling the right data used to mean knowing how to build a query.
- Navigate to Search Composer
- Prompt: "Show me all cash transactions from store 104 in the last 6 months over $100"
- Prompt: "Can you remove store no and cashier no and add trading day field on the right"
- Prompt: "Add all the address fields from header on the right"
- Prompt: "Run the search, name it default"
**Line:** "If a user can ask a question, they can pull the data. That's how our customers are training Level 1 analysts faster than they ever have."

### Demo 4 — Analyze the data (run day before — takes up to 5 min)
**Scene:** Sidekick can find the data AND identify what's interesting in it.
- Prompt: "Pull out top trends from this data"
- Review results in Analysis Results menu
- Prompt: "Tell me more about Cashier 1000094 (Store 94) — Extreme Volume Anomaly"
- Export to PDF from Analysis Results
**Line:** "This is what democratizing retail intelligence actually looks like in practice."

### Optional — Engage module
Only if customer has Engage enabled. Shows Sidekick is a platform feature, not a Secure feature.
- Prompt: "Find me the consumer who placed transaction 2604020898800188368"
- Prompt: "Tell me about that consumer's behavior"
**Line:** "Sidekick doesn't care which module the answer lives in. It just goes and gets it."

### Optional — Incident module
Only if customer has Incident enabled.
- Prompt: "What active incidents are there and what should my next steps be?"
- Prompt: "Update case owner to me and update to Store 101 on Incident ITX343-2005-2"
**Line:** "Most tools tell you the queue. Sidekick tells you where to start — and then helps you start."

### Closing
"Five moments from a real LP analyst's day: find the data, find the work, prep for the situation, understand what you found, and close the loop. Each of these used to require a different tool, a different person, or a different hour. Now they're one conversation."

**Proactive ask:** Customers choose the configuration level that matches their compliance posture. Start at Level 1 or 2. Ask what types of prompts caught their attention — the more complex the prompt, the more credits needed, the higher upsell potential.

---

## Roadmap (directional — no timelines)

- Admin-level memory for terminology and field preferences (arrived May 29, 2026 ✓)
- Natural language incident reporting
- Deeper analytics integration
- BOLO alert creation
- Longer-term: fully agentic AI that monitors data streams and creates work items proactively

Never commit to specific timelines. "We're moving toward" language only.

---

## Why not a generic AI tool

"Anyone can bolt AI onto a product. No one can replicate what's underneath ours."

1. **Built on data no one else has:** 20+ years of retail transaction data. 40% of U.S. retail transactions. 250M unique customer IDs. Sidekick answers are grounded in patterns invisible to any single retailer.
2. **Governed, permission-bound, auditable:** Four config levels. Permission-bound to each user. Human-in-the-loop. Full audit trail.
