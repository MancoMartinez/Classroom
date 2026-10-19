---
name: appriss-jira-support
description: Lightweight Jira skill for support ticket work at Appriss Retail. Use whenever a support engineer mentions a ticket ID, wants to update or comment on a case, transition a ticket status, log time, or get a quick summary of a Jira issue. Triggers on phrases like "update ticket", "add a comment to", "move to", "log time on", "what's the status of", or any mention of a ticket ID (e.g. RCS-123, RTS-456) in a support context. RCS = Retail Customer Support (L1/L2 customer tickets), RTS = Retail Tenant Support (automation/monitoring). Do NOT use for implementation/coding tasks — use appriss-jira-implement for those.
compatibility: "Atlassian MCP (Jira)"
---

# Appriss Jira Support Skill

Lightweight Jira operations for support engineers. Covers fetching, commenting, transitioning, and time logging on tickets.

## Project Prefix Reference

| Prefix | Project | Used For |
|---|---|---|
| **RCS** | Retail Customer Support | Primary L1/L2 customer-facing support tickets |
| **RTS** | Retail Tenant Support | Automation / monitoring / system-generated alerts |
| **ENG** | Engineering | Dev team stories and bugs |
| **DO** | Product Delivery | New customer onboarding and project management |
| **RDOPS** | Retail Delivery Ops | Delivery operations |
| **ARHELP** | Appriss Retail Help | Internal help desk |

Most support work lives in **RCS**. RTS tickets are typically automation-generated.

---

## Tone Rules (baked in — no external skill required)

All Jira output from this skill follows these rules:

- **Professional and concise** — no filler, no excessive empathy phrases
- **Factual only** — report what is observed in the data/system; never draw LP (loss prevention) conclusions or assign blame to a store/employee
- **No speculation** — if something is unknown, say so and describe next steps
- **Customer-facing comments**: neutral, helpful, solution-focused
- **Internal comments**: direct, technical, terse — written for colleagues not customers

---

## Operations

### Fetch & Summarize

When the user wants to know what's on a ticket:

```
Atlassian:getJiraIssue { cloudId: "{cloudId}", issueIdOrKey: "{TICKET-ID}" }
```

Return a concise summary:
- **Status** and **Priority**
- **Summary** (one line)
- **Description** (2–3 sentence digest — not the full body)
- **Reporter / Assignee**
- **Open questions or blockers** if visible in the description

Do not reproduce the full ticket body verbatim.

---

### Add / Update a Comment

Ask the user: is this a **customer-facing** comment or an **internal** note?

**Customer-facing (visible to reporter):**
```
Atlassian:addCommentToJiraIssue {
  cloudId: "{cloudId}",
  issueIdOrKey: "{TICKET-ID}",
  commentBody: "{markdown content}"
}
```

**Internal / restricted (visible to agents/staff only):**
```
Atlassian:addCommentToJiraIssue {
  cloudId: "{cloudId}",
  issueIdOrKey: "{TICKET-ID}",
  commentBody: "{markdown content}",
  commentVisibility: { type: "role", value: "Service Desk Team" }
}
```

⚠️ `commentVisibility` is the closest equivalent to JSM's Internal Note toggle available through the MCP — it is NOT a true internal note. The `value` must match an exact role or group name in your Jira instance. If it fails, ask the user to confirm the correct role/group name from their Jira admin settings.

Always show the user the drafted comment and confirm before posting. Never post silently.

---

### Transition Status

Fetch available transitions first, then move the ticket:

```
Atlassian:getTransitionsForJiraIssue { cloudId: "{cloudId}", issueIdOrKey: "{TICKET-ID}" }
```

Show the user the available transitions and confirm which one to apply. Then:

```
Atlassian:transitionJiraIssue {
  cloudId: "{cloudId}",
  issueIdOrKey: "{TICKET-ID}",
  transition: { id: "{transition-id}" }
}
```

Never guess a transition ID — always fetch first.

---

### Log Time

```
Atlassian:addWorklogToJiraIssue {
  cloudId: "{cloudId}",
  issueIdOrKey: "{TICKET-ID}",
  timeSpent: "{e.g. 1h 30m}",
  commentBody: "{optional work description}"
}
```

If the user doesn't specify a time format, accepted formats are: `30m`, `2h`, `1h 30m`, `1d`. Confirm the entry before logging.

---

## Error Handling

| Situation | Action |
|---|---|
| Ticket not found | Ask user to confirm the ticket ID and project prefix |
| `commentVisibility` role not found | Report error; ask user to confirm the correct role/group name |
| No transitions returned | Tell the user; they may lack permission to transition this ticket |
| Invalid time format for worklog | Prompt user to re-enter in `30m` / `2h` / `1d` format |
| cloudId unknown | Use `Atlassian:getAccessibleAtlassianResources` to look it up |

---

## Notes

- Always confirm with the user before writing anything to Jira
- Never post a comment or transition a ticket without explicit user approval
- Never make LP determinations or assign fault in comments
- For implementation/coding work on a ticket, use the `appriss-jira-implement` skill instead
