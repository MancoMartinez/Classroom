# Sidekick — FAQ & Objection Handlers

## What it is

**Q: What is Sidekick?**
Sidekick is Appriss Retail's embedded agentic AI collaborator — built directly into Engage, Secure, and Incident. It's not a bolt-on chatbot; it's workflow intelligence woven into the platform itself. Your team types what they want — build a search, pull a profile, summarize an investigation, assign a work item — and Sidekick goes and does it.

**Q: Is Sidekick just a chatbot?**
No. Unlike a generic chatbot, Sidekick understands Appriss data structures, user permissions, and retail workflows. It doesn't just answer questions — it composes and runs searches, reads investigations, analyzes result sets, and takes actions like assigning cases or adding audit action plans. Think of it as a co-pilot that already knows the system.

**Q: How is this different from typing into a regular search box?**
A search box matches keywords. Sidekick understands intent and retains context. You don't have to know which field to filter by, which menu to open, or which report to run. You describe what you want — "show me high-risk returns from store 104 this week" — and Sidekick goes and does it. It also takes action: composing, running, modifying, assigning. A search box can't.

**Q: What is Sidekick's AI model?**
Sidekick is powered by one of the leading AI model providers. Appriss does not publicly commit to a specific provider because we continuously evaluate performance and may switch to a better-performing model. *(Internal only: we work with Anthropic and Azure OpenAI. Do not disclose externally.)*

**Q: Is Sidekick just a wrapper around ChatGPT?**
No. External large language models are used only to understand what you're asking (natural language intent). Every decision engine — return authorization, fraud scoring, case linking — is a fully proprietary Appriss model trained on 20+ years of retail transaction data.

**Q: What happened to SecureGPT?**
Sidekick is the next-generation replacement for SecureGPT. SecureGPT was a natural-language interface scoped to Secure only. Sidekick is broader — it spans Engage, Secure, and Incident, takes action inside the workflow, and runs on a more capable underlying model. SecureGPT customers were automatically transitioned to Sidekick as part of the March 2026 beta rollout.

---

## Access & availability

**Q: When did Sidekick become generally available?**
GA was June 9, 2026, announced at NRF Protect. The beta program formally closed May 13, 2026.

**Q: Where do I find Sidekick in the platform?**
Look for the ✨ sparkle icon in the bottom-left corner of any Appriss platform screen. No separate login, separate window, or new app to learn.

**Q: Who can access Sidekick?**
All licensed users on supported Appriss platforms can access Sidekick at GA if purchased. Your organization's configuration level (1–4) determines what data Sidekick can read and what actions it can take. Individual user permissions are also respected.

**Q: Does Sidekick work for users who only have access to one Appriss product?**
Yes. Sidekick respects whatever access the user has. If a user only has Engage access, Sidekick only works inside Engage for them.

**Q: Does Sidekick work for users with more than one product?**
Yes — and that's where it shines. Users with all three products get one conversation that spans Engage, Secure, and Incident — no tab switching, no copy-paste.

**Q: Does Sidekick work on mobile?**
Currently supported on desktop browsers (Chrome, Edge, Safari, Firefox) only. Mobile is on the roadmap.

**Q: What languages does Sidekick support?**
Optimized for English, works well with other languages. Broader multi-language support is on the roadmap. Prompting in another language generally returns results in that language.

---

## Using Sidekick

**Q: How many chats can I have?**
50 chats per user per rolling period. Contact your CSM if your team anticipates higher-volume usage.

**Q: How long is chat history saved?**
30 days. Accessible via Navigation menu → Chat History inside the Sidekick panel.

**Q: How do I get the best results?**
Be specific — include store numbers, date ranges, cashier IDs, or transaction IDs. Use action verbs: "find" or "show me" for searches, "summarize" for overviews, "pull up" or "open" for a specific record. Start broad, then refine in follow-ups. Sidekick holds context across the full conversation.

**Q: Does Sidekick know my time zone?**
Yes. Sidekick uses the time zone configured in your Appriss user profile for time-based queries ("yesterday," "this week," "after 6 PM"). Queries spanning multiple regions will surface the time zone explicitly.

**Q: What happens when I navigate away while Sidekick is working?**
Sidekick stays with you. The panel persists across pages. Long-running searches and analyses complete in the background — results appear in the Search menu or Analysis Results menu when ready.

**Q: Can a customer see what their users are asking Sidekick?**
Every prompt and response is logged. Appriss can provide general statistics and benchmarks, but per-user conversation transcripts cannot be shared with clients for compliance reasons.

**Q: How do I give feedback or report issues?**
Two in-app paths: (1) Feedback icon (speech bubble + thumbs-up) in the Sidekick header — bug or feature request. (2) Thumbs-up/thumbs-down on every individual response. Larger ideas: Help User Menu → Roadmap Ideas, or contact your CSM. All feedback goes directly to Product.

---

## Value & use cases

**Q: What are the most impactful use cases?**
- Exception investigation — query suspicious patterns conversationally without manual filter building
- Case synopsis generation — auto-draft ORC investigation summaries in ~5 min
- Store visit prep — "I'm visiting store 56 today — what should I know?" → real-time briefing
- Audit management — add action plans, reassign audits conversationally
- Ad-hoc trend analysis — segment any result set into high/medium/low risk instantly
- On-demand training — L1 agents ask product knowledge questions in real time (Albertsons Level 1 use case)

**Q: How much time can Sidekick save?**
- Search building (5–15 min manually) → seconds conversationally
- Case synopsis drafting (15–30 min per case) → ~5 minutes
- Store visit prep (45 min) → one prompt
Teams running high-volume investigations report the largest compound efficiency gains.

**Q: How does Sidekick help new hires ramp faster?**
New analysts don't need to memorize the platform structure — they just describe what they want and Sidekick takes them there. The 'ready' curve flattens significantly. One beta customer used Sidekick at Level 1 for L1 agent training — employees ask product knowledge questions in real time without a live trainer.

**Q: How many results does Sidekick return in a query grid?**
Result grids are capped at 20 items. For larger pulls, searches run in the background and land in the Search menu automatically.

**Q: How long does an on-demand analysis take?**
~5 minutes for analyses. Simple queries and navigation: near-instant.

---

## AI governance & compliance

*(Use AI-forward language freely in this section — InfoSec and Legal buyers expect it.)*

**Q: Is our data being used to train AI models?**
No — full stop. Customer data is never used to train AI models. Proprietary ML models are trained on Appriss historical transaction data with no PII. The natural language layer uses a major external AI model provider; customer prompts and session data are never used to retrain those base models. Conversations are used for product improvement only.

**Q: Are conversations logged?**
Yes. Every prompt and response is recorded — for product improvement only, never for AI retraining. Admins can access company-level usage statistics; per-user transcripts cannot be shared with clients.

**Q: What about AI hallucinations?**
Sidekick is designed with human-in-the-loop as a core principle. It accelerates workflow — not replaces judgment. Users should always review outputs before acting. Sidekick may occasionally surface incorrect information or misinterpret a prompt. The footer explicitly states this. If users spot a wrong answer, use the in-app thumbs-down — goes directly to Product. Retrying with added context often resolves it.

**Q: What about security threats and prompt injection?**
Defense-in-depth across two layers: (1) Appriss layer — strict role-based access controls on every tool call, scoped to the tenant and capped by config level. Adversarial prompt injection, jailbreak attempts, and data exfiltration attempts are actively detected and logged. (2) AI model layer — built-in safety training refuses harmful/manipulative requests at the model level. Full audit trail: every session, prompt, tool call, and admin action is captured.

**Q: What about EU data residency?**
Sidekick supports EU data residency. AI processing for EU customers is routed through EU-based infrastructure. Appriss works with each customer on GDPR, country-specific frameworks, and sub-processor approvals.

**Q: Will InfoSec and Legal need to review?**
That's exactly the right move and we expect it. Most customers start at Level 1 or 2 while review is in flight — zero sensitive data exposure at those tiers. Appriss is happy to walk through governance posture, data handling, AIGP certification, and other documentation directly with the customer's InfoSec and Legal teams. Contact your CSM to schedule a session with our governance lead.

**Q: Configuration changes — how do they work?**
Configuration level decisions (Levels 1–4) are handled by your CSM in coordination with the customer's internal compliance team. Level changes are submitted via an ENG ticket and typically turned around within the week.

---

## Objection handlers

**"Every vendor has an AI assistant now. What makes this one different?"**
"You're right — the market is loud. Ask three questions: Does it just describe data, or does it take action? Does it work across the full workflow, or only one part? And does it operate inside your existing permission model, or duplicate it? Sidekick passes all three. Most others fail at least two. We can show you all three live in the platform right now."

**"How do we know our data is safe?"**
"Same answer as your existing platform data: it never leaves the security boundary. Sidekick respects role-based permissions, every prompt and response is logged, and customer data is never used to train models. Configuration levels let you start with zero data exposure and graduate to deeper access only when your team is ready. We can run a governance walkthrough with your InfoSec and Legal teams on request."

**"Our team isn't ready for this kind of capability."**
"That's a great signal that this is exactly the time to try it. Sidekick reduces ramp time, not increases it. New analysts get to productivity faster because they don't have to memorize the platform's structure — they just describe what they want. The 'ready' curve flattens."

**"It should just be included in the platform price."**
Acknowledge the sentiment, but reframe: consumption-based pricing means customers who use Sidekick heavily aren't subsidizing those who don't. The model is designed to align cost to value delivered. Lead with the ROI — store visit prep from 45 minutes to 5, case synopsis from 30 minutes to 5. What's an analyst's hourly cost × the number of investigations they run?

**"We have a dedicated person on our team who does this."**
"That person is going to love Sidekick — it amplifies exactly what they do, handles the routine queries so they can focus on the complex judgment calls, and helps the rest of the team operate at their level faster."
