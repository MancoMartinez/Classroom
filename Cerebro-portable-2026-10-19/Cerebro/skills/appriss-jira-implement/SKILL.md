---
name: appriss-jira-implement
description: Implement a Jira work item end-to-end in Claude Code. Use this skill whenever the user says "implement [TICKET-ID]", "work on [ticket]", "start [PROJ-123]", or asks Claude to pick up, build, or code a Jira issue. The skill fetches the ticket from Jira, derives a branch name from git config, creates the branch off `release`, generates a full implementation plan with subtasks, waits for explicit user approval, then implements the plan. Always use this skill when a Jira ticket ID is mentioned alongside any intent to write code or make changes.
compatibility: "bash (git), Atlassian MCP (Jira)"
---

# Appriss Jira Implement Skill

Implements a Jira work item from ticket fetch through approved code changes.

---

## Workflow

### Step 1 — Fetch the Jira ticket

Use the Atlassian MCP to retrieve the ticket. You need:
- Summary (title)
- Description (full body)
- Acceptance criteria (if present, often in description or a custom field)
- Issue type (Story, Bug, Task, Sub-task)
- Priority
- Any linked issues or parent epics that add context

**MCP call pattern:**
```
Atlassian:getJiraIssue { issueIdOrKey: "PROJ-123" }
```

If the user didn't provide the full project key, check git remote or ask. Display a one-paragraph summary of what the ticket is asking for so the user can confirm you've read it correctly before proceeding.

---

### Step 2 — Derive the branch name

**Username derivation (from git config):**
```bash
git config user.name
```
This returns the user's full name (e.g., "Jane Smith"). Derive username as:
- First initial + full last name, lowercased
- "Jane Smith" → `jsmith`
- "Robert De Niro" → `rdeniro` (first initial + last word of name)
- Strip spaces, accents, and special characters

**Short description:**
- Take the ticket summary, lowercase it, replace spaces with hyphens, strip special characters
- Truncate to ~4–5 words max (keep it readable)
- Example: "Add retry logic to payment processor" → `add-retry-payment-processor`

**Final branch name format:**
```
{username}/{ticket-id}/{short-description}
```
Example: `jsmith/PROJ-123/add-retry-payment-processor`

Show the user the derived branch name and confirm before creating it.

---

### Step 3 — Create the branch

**Before creating the branch, ask the user which base branch to fork from:**

> "Which branch should I fork from?"
> - `release`
> - `main`
> - Other (please specify)

Wait for the user's response. Do not assume a default.

Once confirmed, run:

```bash
git fetch origin
git checkout {base-branch}
git pull origin {base-branch}
git checkout -b {branch-name}
```

If the chosen base branch doesn't exist as a remote branch, stop and tell the user before proceeding.

Confirm success by showing the current branch after creation.

---

### Step 4 — Read CLAUDE.md for project conventions

Before planning, locate and read any `CLAUDE.md` file(s) in the repository. These files contain project-specific instructions that must be followed.

```bash
# Find all CLAUDE.md files in the repo
find . -name "CLAUDE.md" -not -path "*/.git/*"
```

Read every `CLAUDE.md` found — there may be one at the root and additional ones in subdirectories for specific packages or services. Extract and note:

- **Build command(s)** — how to compile or build the project
- **Test command(s)** — how to run unit tests, and any flags for running a subset (e.g., a single file or test name)
- **Lint/format commands** — if specified
- **Any conventions** — naming, file structure, patterns the project enforces

If no `CLAUDE.md` exists, fall back to inspecting `package.json`, `Makefile`, `pyproject.toml`, `pom.xml`, or similar to infer build and test commands. Note what you found either way — these commands will be used in the Testing Plan and during implementation.

---

### Step 5 — Generate the implementation plan

Before writing any code, produce a full implementation plan. Structure it as follows:

```
## Implementation Plan: {TICKET-ID} — {Summary}

### Overview
1–2 sentence description of what will be built/changed and why.

### Affected Areas
List of files, modules, services, or systems expected to be touched.

### Subtasks
1. **[Subtask title]**
   - What: description of the change
   - Where: specific file(s) or component(s)
   - How: brief approach (e.g., "add retry wrapper", "update schema", "write unit test")
   - Acceptance: how you'll know this subtask is done

2. **[Subtask title]**
   ...

### Build & Test Commands
Commands sourced from `CLAUDE.md` (or inferred fallback):
- **Build:** `{build command from CLAUDE.md}`
- **Run all tests:** `{test command from CLAUDE.md}`
- **Run single test file:** `{single-file test command if documented}`
- **Lint/format:** `{lint command if documented}`

### Testing Plan

**Unit Tests**
For each logical change, identify:
- Existing test file(s) to modify (path, current coverage gaps)
- New test file(s) to create (path, naming convention matching the codebase)
- Specific test cases to write, listed individually:
  - `test_<scenario>`: what it validates, inputs, expected output/behavior
  - Cover happy path, edge cases, and error/exception paths
- Any mocks, stubs, or fixtures needed

**Integration Tests** (if applicable)
- Which integration test suites are affected
- New integration scenarios to add

**Manual Verification Steps**
- Step-by-step instructions a reviewer could follow to verify the change works end-to-end

### Out of Scope
Anything the ticket does NOT require (to avoid scope creep).

### Open Questions
Any ambiguities that need user input before or during implementation.
```

Be thorough. If the ticket description is sparse, use the codebase context (grep, file reads) to make informed subtasks. State assumptions explicitly.

---

### Step 6 — Wait for plan approval

**STOP HERE.** Do not write any code until the user explicitly approves the plan.

Say:
> "Here's my implementation plan above. Please review and let me know if you'd like any changes, or say **'approved'** / **'go ahead'** to start implementation."

If the user requests changes to the plan, update it and ask again. Do not proceed until you receive clear approval.

---

### Step 6.5 — Offer to update Jira with the QA test plan

After the user approves the plan (Step 6), **before writing any code**, offer to update the Jira ticket with the testing details so the QA team can prepare.

**Ask the user:**
> "Would you like me to update the Jira ticket with the test plan so QA can start preparing?"

If the user says yes, proceed with the steps below. If no, skip to Step 7.

#### Finding the right Jira field

**If the ticket is in the ENG project (ticket ID starts with `ENG-`):** use `customfield_18859` directly — this is the known QA test plan ADF field for that project. Fetch its current value before writing:

```
Atlassian:getJiraIssue {
  cloudId: "{cloudId}",
  issueIdOrKey: "{TICKET-ID}",
  fields: ["customfield_18859"]
}
```

**For all other projects:** scan the issue's field metadata to find a QA-specific test plan field:

```
Atlassian:getJiraIssueTypeMetaWithFields {
  cloudId: "{cloudId}",
  issueTypeId: "{issue_type_id}",
  projectIdOrKey: "{project_key}"
}
```

Scan the returned fields for names matching patterns like:
- `QA Test Plan`, `Test Plan`, `Test Cases`, `QA Scenarios`, `Testing Notes`, `Acceptance Test`, `Manual Test Steps`
- Field keys matching: `customfield_*` with descriptions containing "qa", "test", "scenario"

If a QA-specific field is found, use it. If multiple candidates exist, pick the best match and confirm with the user. If none is found, fall back to adding the test plan as a Jira comment (clearly labelled `## QA Test Plan`).

#### Composing the QA test plan content

Format the test plan from the approved plan's **Testing Plan** section into clear, QA-executable steps:

```
## QA Test Plan — {TICKET-ID}: {Summary}

### Manual Verification Steps
{Numbered list of manual test steps from the approved plan}

### Integration Test Scenarios
{List of integration scenarios, if applicable}

### Edge Cases & Error Paths
{List of edge cases and error conditions to verify}

### Test Environment Notes
{Any setup or environment prerequisites the QA team needs to know}
```

#### Confirm with the user before updating

**STOP.** Show the user:
1. Which field you'll update (field name + key)
2. The exact content you'll write

Say:
> "I'll update the **{Field Name}** field on {TICKET-ID} with the test plan above. Shall I go ahead?"

Wait for explicit approval ("yes", "go ahead", "confirmed", etc.) before making the Jira API call.

#### Updating the field

Once approved, update the issue:

```
Atlassian:editJiraIssue {
  issueIdOrKey: "PROJ-123",
  fields: {
    "{field_key}": "{formatted QA test plan content}"
  }
}
```

If the field is a rich-text (Atlassian Document Format / ADF) field, format the content as ADF. If it's a plain-text or markdown field, use markdown.

**Fallback — add as a comment:** If no writable QA field is found, offer to add the test plan as a Jira comment with a QA-team mention instead:

```
Atlassian:addCommentToJiraIssue {
  issueIdOrKey: "PROJ-123",
  commentBody: "**QA Test Plan**\n\n{formatted content}"
}
```

Always confirm with the user before posting the comment too.

Confirm success by showing the updated field value or a link to the Jira ticket.

---

### Step 7 — Implement the plan

Once approved, work through each subtask in order:

1. Announce which subtask you're starting: `### Implementing: Subtask 1 — [title]`
2. Make the changes
3. Immediately after each functional change, write or update the corresponding unit tests — do not defer tests to the end. Tests are a required deliverable for every subtask that touches logic, not optional cleanup.
   - Look for the existing test file that mirrors the changed file (e.g., `src/payments/retry.ts` → `src/payments/retry.test.ts` or `tests/payments/test_retry.py`)
   - If no test file exists, create one following the naming and structure conventions of nearby test files
   - Cover: happy path, edge cases, and error/exception paths as identified in the Testing Plan
4. Run the test suite after each subtask using the command from `CLAUDE.md` (recorded in the plan's Build & Test Commands section). Use the single-file variant when available to keep feedback fast.
5. Briefly confirm the subtask is complete (including tests passing) before moving to the next

After all subtasks are complete:
- Run the full test suite one final time and confirm all tests pass
- Run any available linter or test suite
- Show a summary of all changed files (`git diff --stat`), highlighting new/modified test files

**STOP HERE — do not commit yet.** Present a handoff summary to the user:

> **Implementation complete on branch `{branch-name}`.**
>
> All changes are staged but not yet committed. Please review the diff in your IDE before we proceed.
>
> When you're ready, let me know and I'll commit and push — or you can do either step yourself.

Only commit and push if the user explicitly asks. Do not commit or push automatically.

**If the user asks Claude to commit**, use the following message format:
```
{TICKET-ID} {Short description of the change}
```
Example: `ENG-123456 Add retry logic to payment processor`

The short description should be sentence-style (capital first letter, no period), imperative tense, and derived from the ticket summary. Ask the user to confirm the message before committing if there's any ambiguity.

---

### Step 8 — Write QA test plan back to Jira

After the implementation plan (including manual verification steps) is approved by the user, offer to publish the test plan to the Jira ticket so the QA team can execute it directly.

**8a — Discover QA field and detect field type**

**If the ticket is in the ENG project (ticket ID starts with `ENG-`):** use `customfield_18859` directly — this is the known QA test plan ADF field for that project.

**For all other projects:** scan the issue's field metadata to find a QA-specific test plan field:

```
Atlassian:getJiraIssueTypeMetaWithFields {
  cloudId: "{cloudId}",
  issueTypeId: "{issue_type_id}",
  projectIdOrKey: "{project_key}"
}
```

Scan the returned fields for names matching patterns like:
- `QA Test Plan`, `Test Plan`, `Test Cases`, `QA Scenarios`, `Testing Notes`, `Acceptance Test`, `Manual Test Steps`
- Field keys matching: `customfield_*` with descriptions containing "qa", "test", "scenario"

If a QA-specific field is found, use it. If multiple candidates exist, pick the best match and note which field you'll use. If none is found, fall back to adding a comment to the ticket instead (clearly labelled `## QA Test Plan`).

**Once the field is identified**, fetch its current value to inspect existing content:

```
Atlassian:getJiraIssue {
  cloudId: "{cloudId}",
  issueIdOrKey: "{TICKET-ID}",
  fields: ["{qa_field_key}"]
}
```

Classify the existing field content using this priority order:

1. **Existing ADF table** — the field value is an ADF document containing a `table` node. Extract column names from the `tableHeader` cells. **This is the highest-priority case — always prefer populating an existing table over creating a new one.**
2. **Existing markdown table** — the field value is a string containing a markdown table (lines starting with `|`). Parse the header row to extract exact column names.
3. **Rich-text / freeform** — an ADF document with no table node, or a long prose string.
4. **Empty / blank** — field exists but has no content. Check the field schema type: if `adf`, create a new ADF table; if `string`/`markdown`, create a new markdown table.

**Parsing an existing markdown table:**

If the field value contains lines like:
```
| Scenario | Expected Result | Actual Result | Notes |
|---|---|---|---|
| | | | |
```

Extract the headers exactly as written (preserve casing and spacing). Map your scenarios to those columns — do not add or remove columns. The separator row (`|---|---`) must be preserved unchanged. Any pre-existing data rows must also be preserved; append new scenario rows after them.

**8b — Compose the test plan content (format depends on field type)**

Derive all test scenarios from the approved Implementation Plan's **Testing Plan** section — manual verification steps, integration scenarios, and edge cases all become individual rows or sections.

**If the field has an existing markdown table (highest priority):**

Preserve the entire existing table structure. Keep the header row and separator row exactly as-is. Keep any existing data rows. Append one new row per scenario from the test plan. Use the exact column names from the existing header to determine what goes in each cell — map your scenario data to the closest matching column using the guide below.

**If the field is a new/empty table field (no existing content):**

Create a new table. The columns to populate are determined by the field type (markdown or ADF). Common columns and how to fill them:

| Column | What to populate |
|---|---|
| `Scenario` / `Test Case` / `Description` | One-line description of what is being tested (e.g., "User submits valid form → success toast shown") |
| `Steps` / `Test Steps` | Numbered steps to reproduce/execute, derived from Manual Verification Steps |
| `Expected Result` | The expected outcome for a passing test (from acceptance criteria or plan) |
| `Actual Result` | Leave **blank** — QA fills this in during execution |
| `Pass / Fail` / `Status` | Leave **blank** — QA fills this in during execution |
| `Notes` | Any prerequisites, environment flags, or edge case context |

Generate one row per distinct scenario. Group related steps into a single row rather than one row per step. A typical ticket should produce 3–10 rows covering: happy path(s), key edge cases, and at least one negative/error path.

Represent the table as ADF if the field uses ADF, or as a markdown table if the field is plain-text/markdown.

**ADF table structure (use when field is ADF):**
```json
{
  "type": "doc",
  "version": 1,
  "content": [
    {
      "type": "table",
      "attrs": { "isNumberColumnEnabled": false, "layout": "default" },
      "content": [
        {
          "type": "tableRow",
          "content": [
            { "type": "tableHeader", "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "Scenario" }] }] },
            { "type": "tableHeader", "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "Steps" }] }] },
            { "type": "tableHeader", "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "Expected Result" }] }] },
            { "type": "tableHeader", "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "Actual Result" }] }] },
            { "type": "tableHeader", "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "Pass/Fail" }] }] },
            { "type": "tableHeader", "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "Notes" }] }] }
          ]
        },
        {
          "type": "tableRow",
          "content": [
            { "type": "tableCell", "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "{scenario description}" }] }] },
            { "type": "tableCell", "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "{numbered steps}" }] }] },
            { "type": "tableCell", "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "{expected outcome}" }] }] },
            { "type": "tableCell", "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "" }] }] },
            { "type": "tableCell", "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "" }] }] },
            { "type": "tableCell", "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "{notes or blank}" }] }] }
          ]
        }
      ]
    }
  ]
}
```
Add one `tableRow` block per scenario. Match the column headers to whatever the existing field actually uses — do not rename them.

**Markdown table (use when field is plain-text/markdown):**
```
| Scenario | Steps | Expected Result | Actual Result | Pass/Fail | Notes |
|---|---|---|---|---|---|
| {description} | 1. … 2. … | {expected outcome} | | | {notes} |
```

**If the field is a freeform rich-text field (no table structure):**

Use this prose format instead:
```
## QA Test Plan — {TICKET-ID}: {Summary}

### Scope
Brief description of what was implemented and what should be verified.

### Prerequisites
Any setup, environment flags, or test data needed before testing.

### Test Scenarios
For each scenario:
**Scenario N — {description}**
Steps:
1. …
Expected Result: …
Notes: …

### Edge Cases & Negative Tests
List edge cases and error paths to verify.

### Out of Scope
What QA should NOT test as part of this ticket.
```

**8c — Confirm with user before writing**

**STOP HERE.** Show the user:
1. The composed test plan content (render the table visually in markdown so it's readable)
2. Which Jira field will be updated (field name + key)
3. The format being used (table rows vs. freeform)
4. Ask for explicit confirmation:

> "I'll update the **{field name}** field on **{TICKET-ID}** with the QA test plan above ({N} scenarios as table rows / freeform text). Should I go ahead?"

Do not write to Jira until the user says yes. The user may also request changes to the scenarios at this point — incorporate feedback and re-confirm before writing.

**8d — Write to Jira**

If a QA field was found:
```
Atlassian:editJiraIssue {
  cloudId: "{cloudId}",
  issueIdOrKey: "{TICKET-ID}",
  fields: {
    "{qa_field_key}": {ADF document object} | "{markdown string}"
  }
}
```

Use the ADF object (not a string) when the field is ADF. Use a plain string when the field is markdown or plain-text.

If no QA field exists, add a comment using the freeform format:
```
Atlassian:addCommentToJiraIssue {
  cloudId: "{cloudId}",
  issueIdOrKey: "{TICKET-ID}",
  commentBody: "{freeform QA test plan markdown}"
}
```

Confirm success to the user and provide the Jira ticket link if available.

---

## Error Handling

| Situation | Action |
|---|---|
| Ticket not found | Ask user to confirm the ticket ID and project |
| Chosen base branch missing from remote | Tell the user and ask them to specify a different branch |
| git config user.name is empty | Ask user to provide their name |
| Ambiguous acceptance criteria | List assumptions in Open Questions, ask before implementing |
| Tests fail after implementation | Report the failure, attempt to fix, ask if stuck |
| No existing test file for changed code | Create one following nearby test file conventions |
| User asks Claude to commit | Use format `{TICKET-ID} {Short description}`, confirm message if ambiguous |
| `CLAUDE.md` exists but no build/test commands | Note the gap in Open Questions; ask the user before implementing |
| `customfield_18859` missing on an ENG ticket | Fall back to scanning for a QA field by name, then comment if none found |
| No QA-specific Jira field found (non-ENG project) | Fall back to adding a clearly-labelled `## QA Test Plan` comment on the ticket |
| Multiple QA field candidates found | Pick the best match, state which field will be used, ask user to confirm before writing |
| User declines Jira update | Skip Step 8; implementation handoff is still complete |
| QA field is table-structured but column names differ from expected | Use the actual column names discovered from the existing field value — never rename columns |
| Existing markdown table found in QA field | Preserve all existing rows; append new scenario rows after them — never overwrite pre-existing data |
| ADF write fails or field rejects structured content | Fall back to markdown string; inform user and show the content for manual paste |

---

## Notes

- Never commit directly to `release`, `main`, or `master`
- Never skip the approval step even if the ticket seems simple
- Never commit or push without explicit user instruction — always wait for the user to review changes in their IDE first
- Commit message format: `{TICKET-ID} {Short imperative description}` — e.g., `ENG-123456 Fix race condition in payment processor`
- If the ticket has sub-tasks in Jira, fetch those too and incorporate them into the plan
- Keep commits focused; one logical change per commit is preferred
- Always confirm with the user before writing anything to Jira (test plan field or comment) — never update silently
- When looking for QA fields, use `expand: "names"` on `getJiraIssue` to get human-readable field labels alongside their keys