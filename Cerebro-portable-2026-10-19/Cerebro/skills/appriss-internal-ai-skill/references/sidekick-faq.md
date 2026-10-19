# Sidekick & AI Capabilities FAQ

*Added from Rev Org enablement session, March 2026. Keep current.*

---

## What is Sidekick?

Sidekick is Appriss Retail's Agentic Assistant — embedded across Secure, Engage, and Incident. It's not a sidecar chatbot sitting alongside the platform; it operates **inside** your tools and workflows.

**What it does today:**
- Builds queries and reports using natural language (e.g., "Show me cash transactions over $500 with voided items in store 123 this week")
- Analyzes investigations and cases including supporting attachments (PDFs, etc.)
- Analyzes exceptions and audits including audit plans
- Takes actions — assigns work items, generates AI case synopses for investigations and ORC

**Key distinction:** Sidekick doesn't just explain what happened. It helps you do something about it.

---

## Current Beta Capabilities (Free)

The following are currently in beta and **free of charge**:

- **People-centric queries** — ask follow-up questions about a specific store, cashier, or consumer
- **AI case linking** — Incident+ intelligently connects related cases using AI
- **Natural language search and report building** — "How many incidents did I have this week?" or "Who has failed audits in this region?"
- **Actions on incidents** — reassign or close incidents directly through Sidekick
- **Actions on audits** — add action plans, reassign audits, or review historical audits

**Always communicate this clearly:** The beta is free. Say it proactively.

---

## Upcoming Capabilities (Directional — No Timelines)

- **Incident reporting via natural language** — users describe an incident in plain language; Sidekick pre-fills the form, identifies incident type, suspect, and stolen merchandise, and provides a link to review and complete remaining details. Removes friction from the current quick-entry process.
- **BOLO (Be On the Lookout) alert creation** — Sidekick drafts and triggers BOLO alerts on behalf of the user.
- **The vision:** A fully conversational incident reporting process where the system structures data from a natural language description.
- **Longer term:** Fully agentic AI that monitors data streams, detects anomalies, creates work items, links incidents, and drafts investigation summaries — proactively, without a human triggering each step.

---

## Sidekick Configuration Levels

Sidekick supports four levels so organizations can adopt at a pace matching their compliance and governance requirements:

| Level | Capability Tier | Retailer Data Accessed | What It Does |
|-------|-----------------|------------------------|--------------|
| Level 1 | Basic Product Knowledge | None — LLM has no access to retailer data | Understands our products; answers general questions |
| Level 2 | Natural Language Queries & Navigation | None — LLM has no access to sensitive retailer data | Writes queries, finds things in the product, navigates to searches and dashboards |
| Level 3 | Work Item Access | Work items, investigations, cases, audits, consumer profiles | Reads and takes actions on investigations, cases, audits, and consumer profiles |
| Level 4 | Deep Data Access | Transaction-level data, attachments (e.g., PDF reports) | Analyzes transaction data; summarizes documents attached to investigations |

**Key message:** Retailers don't need to grant full data access to start. Start at Level 1 or 2 — zero sensitive data touched — and expand as comfort and compliance framework allows.

---

## Is Sidekick Free?

All capabilities currently in beta are **free of charge** as part of the beta program.

Going forward:
- Some capabilities will be included in a free tier (natural language query building is likely, potentially with usage limits for high-volume users — similar to how ChatGPT handles free vs. paid)
- A formal monetization strategy for heavy/power users is being developed
- Details will be shared when finalized

**For customers:** The beta is free. Communicate this clearly and proactively.

---

## What AI Model Powers Sidekick?

Sidekick is powered by one of the major AI model providers (Anthropic or Azure OpenAI). We don't publicly commit to a specific model because we may switch to a better-performing model at any time — our priority is always accuracy and performance, not loyalty to any single provider.

**If asked externally:** "We use one of the leading AI model providers."  
**Do not publicly commit to Anthropic or Azure OpenAI.**

---

## Is Sidekick Just a Wrapper Around ChatGPT?

No. Here's the distinction:

- **External LLMs** are used by Sidekick to understand what the user is asking — natural language intent parsing only.
- **All decision engines** — return authorization, fraud detection, case linking, etc. — are fully proprietary. Appriss built, trained, optimized, and owns these.
- ChatGPT has no knowledge of what a retail investigator is looking for or how to handle a return fraud pattern.
- Everything on the Engage side (return decisions, fraud scoring) uses purely proprietary models.

**The short answer:** We use the best tools available for each job. For Sidekick's conversational layer, that includes best-in-class external LLMs. For every decision that matters to your business, it's our models — trained on our data — making the call.

---

## How Does Appriss Ensure AI Aligns with Compliance Standards?

1. **Tiered configuration** — Retailers choose their data access level (Levels 1–4)
2. **Permission-bound** — Sidekick never acts outside a user's existing platform permissions
3. **Governance certification** — General Counsel holds AIGP certification through IAPP
4. **Mandatory training** — All Appriss employees complete mandatory AI Ethics and Compliance Training
5. **No PII in training** — Proprietary ML models are trained on historical transaction and return data, not PII
6. **Consortium anonymization** — Cross-retailer signals are anonymized before aggregation; no retailer's customer PII is exposed to another retailer
7. **GenAI data handling** — No customer data is used to retrain base LLM models
8. **Human-in-the-loop** — All consequential outputs support human review; retailers retain final decision authority
9. **Full auditability** — Every return authorization decision is fully auditable

---

## AI Governance Key Contacts

| Name | Title | Contact |
|------|-------|---------|
| Kellie Beckman | General Counsel | kbeckman@apprissretail.com |
| Vishal Patel, Ph.D. | Chief Product Officer | vpatel@apprissretail.com |
| Fin Bauer, Ph.D. | Director of Data Science | bfbauer@apprissretail.com |

---

## How Does Data Normalization Give Appriss a Competitive Advantage?

No competitor today can perform true omnichannel returns authorization for risk modeling. This is a data problem before it's an AI problem.

Getting there requires:
1. Ingesting data from every retailer in formats that vary widely across POS systems, channels, and regions
2. Normalizing that data into a consistent, structured model
3. Building relationships between data points — linking transactions, identities, incidents, and behaviors across systems

This foundational work is what Appriss Retail's implementation and data teams have been doing for over 20 years. Competitors who skip this step are running their AI on incomplete or inconsistent data. The output is only as good as the input.
