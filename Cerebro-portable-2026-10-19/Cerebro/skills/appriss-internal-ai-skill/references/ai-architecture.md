# AI Architecture Reference

## Core Message
Any vendor can bolt AI onto a product. What they can't replicate is our Data Intelligence foundation — the breadth and depth of retail data we've built over decades. That's what makes our AI's decisions smarter, faster, and more accurate than anything else on the market.

---

## The Three AI Layers

Our AI architecture is built in three layers. Each layer depends on the one before it — this is an engineering dependency, not a metaphor.

### Layer 1 — Data Intelligence (The Foundation)
**What it does:** Connects, structures, and resolves massive amounts of retail data before any model touches it.

Key functions:
- Consumer identity resolution across cards, emails, phone numbers, addresses, and channels
- Cross-retailer consortium signal aggregation (250M unique customer IDs)
- Data normalization across every purchase and return system (in-store, online, contact center)
- Automatic case linking across stores
- Address, email, and ID validation

**Why it matters:** This is the invisible layer most competitors skip — and it's the foundation everything else depends on. Without it, AI models are brittle and decisions are unreliable. Competitors skipping this step are applying weak models to fragmented data.

**The key insight:** You can have the best ML model in the world, but if you can't stitch a consumer's identity across channels or parse the data correctly, your model is guessing on fragments. Our Data Intelligence layer handles that automatically.

---

### Layer 2 — Decision Intelligence (The Action Layer)
**What it does:** Machine learning models making real-time decisions at scale — approve, warn, or decline — in under one second.

Key functions:
- Return authorization at POS, OMS, or customer service center
- Wardrobing detection (buy-use-return patterns)
- Tender laundering detection
- Discount fraud detection
- Peer-based outlier detection for stores and associates
- Online return and claim authorization
- Incentive optimization at point of return

**Why it matters:** This is where data becomes outcomes — not just dashboards. Decisions are made automatically, at scale, trained on more retail loss data than any competitor has access to.

**Decision accuracy:** 99.99% — over 20 years. Built to minimize false positives so good customers aren't punished.

---

### Layer 3 — Workflow Intelligence (The Acceleration Layer)
**What it does:** Large language models and agentic AI that analyze data, generate content, and take workflow actions directly inside the platform.

Key functions (via Sidekick):
- Natural language transaction search and report building
- AI-generated investigation narratives and case synopses
- Work item assignment and case management
- Audit analysis and action plans
- AI case linking across incidents

**Why it matters:** Makes everything faster and accessible to a broader team. What used to take 45 minutes now takes 5. What required a power user now works for any analyst.

**Key distinction:** Sidekick doesn't just explain what happened. It helps you do something about it — inside the workflow, not as a sidecar chatbot.

---

## The 12+ Live AI Systems

### Layer 1 — Data Intelligence Systems

| System | Product | What It Does |
|--------|---------|--------------|
| Consumer Identity Resolution | Engage | Resolves consumer identity across cards, emails, addresses, and channels into one accurate entity using graph algorithms |
| Consortium Model | Engage | Aggregates cross-retailer return behavior signals; flags consumers who've been risky elsewhere |
| Data Normalization | Platform | Normalizes every retailer's purchase/return data into a common model; algorithmic/rule-based |
| Case Linking Model | Incident | Automatically connects related incidents across store locations using supervised learning + LLM |
| Address, Email & ID Validation Signal | Engage | Third-party vendor services integrated by Appriss for identity accuracy and fraud protection |

### Layer 2 — Decision Intelligence Systems

| System | Product | What It Does |
|--------|---------|--------------|
| Store Return Authorization Model | Engage | Real-time approve/warn/decline at POS in <1 second; supervised learning on 20+ years of labeled data |
| Online Return & Claim Authorization Model | Engage | Same ML decisioning as store model, extended to e-commerce, BOPIS, and online claims |
| Wardrobing Detection Model | Engage | Detects buy-use-return behavioral fingerprints; supervised learning |
| Tender Laundering Detection Model | Engage | Identifies payment method manipulation (e.g., cash purchase → gift card return); key ORC indicator |
| Discount Fraud Detection Model | Engage | Flags coupon abuse, employee discount misuse, promotional fraud patterns |
| Exception Detection (Outlier) Model | Secure | Builds peer-group baselines for stores and cashiers; flags statistical deviations; unsupervised learning |
| Incentive Optimization Model | Engage | AI-driven offer selection at point of return (exchange, store credit, partial refund) to reduce cash refunds and improve retention |

### Layer 3 — Workflow Intelligence Systems

| System | Product | What It Does |
|--------|---------|--------------|
| Sidekick | Platform (Engage, Secure, Incident) | Platform-wide AI assistant; writes queries, analyzes cases/investigations/audits, assigns work items, generates synopses |

---

## How to Explain the Dependency

> "Our three layers are not independent — they're stacked. Layer 2's accuracy depends directly on Layer 1's data quality. If a consumer's identity isn't resolved correctly, the return model scores an incomplete picture. Layer 3's usefulness depends on Layers 1 and 2 being reliable — Sidekick can only surface meaningful insights because the data underneath is structured and the decisions it's built on are trustworthy. This is an engineering dependency. It's why competitors who skip Layer 1 end up with AI that looks impressive in a demo but underperforms in production."

---

## Where We're Going (Directional Only — No Timelines)
We are moving from AI that responds to AI that initiates. Today, Sidekick helps analysts when they ask. The vision: a fully agentic AI that monitors data streams, detects anomalies, creates work items, links related incidents, and drafts investigation summaries — proactively, without a human triggering each step. Human-in-the-loop remains a core design principle for sensitive investigations.
