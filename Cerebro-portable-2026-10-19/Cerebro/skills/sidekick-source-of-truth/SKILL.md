---
name: sidekick-source-of-truth
description: >
  Appriss Retail's internal source of truth for Sidekick — the AI workflow intelligence layer built into Engage, Secure, and Incident. Use this skill whenever anyone at Appriss asks ANYTHING about Sidekick: what it is, what it does, how to sell it, pricing, configuration levels, demo guidance, objection handling, governance/InfoSec questions, beta program history, pipeline context, product roadmap, admin-level memory, or how to get a customer started. Also triggers on questions about SecureGPT (Sidekick's predecessor), the sparkle icon, credit tiers, or any AE/CSM/PMM/ELT question that involves the Sidekick product. When in doubt — if Sidekick is mentioned — use this skill.
---

# Sidekick — Source of Truth

Sidekick is Appriss Retail's embedded agentic AI collaborator — the workflow intelligence layer built directly into Engage, Secure, and Incident. **Generally available as of June 9, 2026 (announced at NRF Protect). Beta is over.**

For detailed reference material, see:
- `references/positioning-and-pitch.md` — positioning, pitch versions, talk tracks by persona, vocabulary, old-vs-new framing
- `references/product-and-features.md` — what Sidekick does, configuration levels, admin-level memory, demo guidance
- `references/pricing-and-contracts.md` — tiers, credits, escalator, beta incentives, pipeline
- `references/faq-and-objections.md` — full internal FAQ (47 Qs), objection handlers, governance/InfoSec answers
- `references/beta-program.md` — beta history, usage data, feedback summary, customer context

Read the relevant reference file(s) before answering. For a question that spans multiple topics, read all relevant files.

---

## Quick orientation

**What it is:** The workflow intelligence layer of the Appriss platform. It's the part your team talks to.

**What it does:** Composes searches, pulls profiles, summarizes investigations, runs analyses, takes actions (assign work items, close incidents, add audit action plans) — all in plain language. Doesn't just answer; gets things done.

**Where it lives:** Inside Engage, Secure, and Incident. ✨ Sparkle icon, bottom-left corner of any screen.

**What's different:** One experience across all three products. Acts inside the workflow. Respects existing user permissions. Not a sidecar chatbot.

**Replaced:** SecureGPT (natural-language interface scoped to Secure only). All SecureGPT customers transitioned automatically in March 2026.

**Cost:** Consumption-based credits. Three tiers: Essential $15K/yr (<50 users), Pro $45K/yr (50–499 users), Premier $150K/yr (500+ users). Three-year contracts with 10% annual escalator.

**Governance:** Four configuration levels — Level 1 = zero data access. Customer data never used to train AI models.

---

## How to answer Sidekick questions

**Selling / positioning / pitch questions** → `references/positioning-and-pitch.md`

**Product capability / feature / demo questions** → `references/product-and-features.md`

**Pricing / credits / contract questions** → `references/pricing-and-contracts.md`

**FAQ, objections, InfoSec/Legal questions** → `references/faq-and-objections.md`

**Beta history, customer feedback, pipeline, usage data** → `references/beta-program.md`

---

## Key rules

- **Beta is over.** GA was June 9, 2026. Never describe Sidekick as a beta product.
- **Don't lead with AI.** In pitch contexts, use "embedded collaborator," "workflow intelligence," "the platform you can talk to." Save AI-forward language for InfoSec/Legal conversations.
- **Never commit to roadmap timelines.** Use "we're moving toward" language.
- **Don't disclose AI providers.** Internally: Anthropic + Azure OpenAI. Externally: "one of the leading AI model providers."
- **Human-in-the-loop always applies.** Sidekick proposes; the user decides. Sidekick never acts outside a user's existing permissions.
- **Pricing has no discounting** — only tier combinations (e.g., two Essential tiers = $30K).

---

## External resources

- Product page: https://apprissretail.com/sidekick/
- Press release (GA): https://apprissretail.com/news/appriss-retail-unveils-sidekick/
- Product docs: https://docs.apprissretail.com/products/appriss-sidekick
- Using Sidekick: https://docs.apprissretail.com/products/appriss-sidekick/using-sidekick
- Prompt library: https://docs.apprissretail.com/products/appriss-sidekick/sidekick-prompt-library
- AI governance: https://docs.apprissretail.com/products/appriss-sidekick/ai-governance-and-compliance
- Admin-level memory: https://docs.apprissretail.com/products/appriss-sidekick/admin-level-memory
