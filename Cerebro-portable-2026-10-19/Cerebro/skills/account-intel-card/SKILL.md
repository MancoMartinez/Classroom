---
name: account-intel-card
description: Generate comprehensive Account Intelligence Cards for MQA and Engaged accounts. Creates professional Word documents containing buying committee maps, engagement signals, timeline analysis, account scoring, meeting schedules, and contextual insights. Use when sales/CSM team needs organized account intelligence for strategic planning, customer meetings, or account reviews.
---


# Account Intel Card Generator

## Purpose

Generate professional Account Intelligence Cards that synthesize account data, public information, engagement history, and buying committee intelligence into actionable sales documents.

## When to Use This Skill

Use this skill when:
- Creating intelligence briefs for MQA (Marketing Qualified Account) or Engaged accounts
- Preparing for strategic customer meetings or QBRs
- Analyzing account engagement patterns and signals
- Documenting buying committee structure and gaps
- Consolidating scattered account data into one reference document

## Required User Inputs

The user will provide the following information (via copy/paste or direct input):

1. **Account Name & Basic Info**: Company name, industry, size, location
2. **Account Scores**: Engage and Secure ICP scores from Salesforce (out of 3)
3. **Campaign Trigger**: The campaign name that triggered MQA status (if applicable)
4. **Buying Committee Information**: Known contacts from Sales Navigator or other sources
   - Can be provided as: CSV/Excel export, pasted text, or list of names/roles
   - **Users must label the source of each contact and any associated pain points or insights** (e.g., "from Gong call Jan 10", "from LinkedIn", "from news article [URL]", "from Sales Nav"). Claude will preserve and display these source labels in the document.
5. **Meeting Contact**: The specific person who booked or will attend the meeting
6. **Meeting Schedule**: Date/time of upcoming meetings (if scheduled)
7. **Additional Context**: Any notes, previous closed-lost reasons, special considerations

Note: Salesforce opportunity data is pulled automatically via connector. All other research is done via web search.

## Workflow

### Step 1: Gather and Organize User-Provided Data

Collect all information the user provides. Organize it into clear sections:
- Account basics (name, industry, revenue, size)
- Current scores and status
- Campaign trigger information
- Known contacts and roles
- Meeting contact (person attending the meeting)
- Meeting schedule
- User notes

### Step 2: Pull Salesforce Data

Use the Salesforce connector to query the account. Pull:
- **Past and open opportunities**: Name, stage, close date, amount, and owner for all opportunities associated with this account
- **Account owner**: The current AE assigned to the account

```
Salesforce:soqlQuery
Query: SELECT Name, StageName, CloseDate, Amount, OwnerId, Owner.Name FROM Opportunity WHERE Account.Name = '[Company Name]' ORDER BY CloseDate DESC
```

If the account name lookup fails, try searching by partial name or ask the user to confirm the Salesforce account name. Document all opportunities found, including closed-lost ones — prior loss context is strategically valuable.

### Step 3: Research Public Company Information

**ALWAYS search for recent public information** about the account:

```bash
# Financial and leadership context
web_search: "[Company Name] financial results annual revenue"
web_search: "[Company Name] leadership changes executive team"

# Org context
web_search: "[Company Name] layoffs restructuring reorg"
web_search: "[Company Name] strategic priorities initiatives 2025 2026"

# Technology and AI
web_search: "[Company Name] technology investment IT budget"
web_search: "[Company Name] artificial intelligence AI investment strategy"
```

Gather:
- Recent news (last 3-6 months)
- Financial performance (revenue, growth, public filings if available)
- Leadership changes or strategic initiatives
- **Org context**: Restructuring, reorgs, layoffs, new executive hires, shifts in strategic direction
- **Technology spend**: Publicly available data on IT budget allocation, vendor relationships, or technology priorities
- **AI investment**: How the company is publicly talking about AI — pilots, partnerships, budget commitments, executive statements

If the company is publicly traded, look for:
- Latest 10-K or 10-Q filings (mentions of technology spend, digital transformation, AI)
- Earnings announcements and analyst calls
- Investor presentations

**Source links are required**: Every piece of news or external intelligence included in the document must include the URL or source name it came from. No unsourced claims.

### Step 4: Analyze Buying Committee

Based on the provided contacts, create a comprehensive buying committee map:

**Standard B2B Buying Committee Roles:**
- **Economic Buyer**: Final budget authority (typically C-level, VP Finance, etc.)
- **Champion**: Internal advocate for your solution
- **Technical Evaluator**: Assesses technical fit and integration
- **End User**: Will use the product day-to-day
- **Legal/Procurement**: Contract and vendor management
- **Influencer**: Provides input but not decision authority

**For each known contact, document:**
- Name and title
- Role in buying process
- Engagement level (high/medium/low based on provided data)
- Last interaction date
- Key insights or notes

**Identify gaps:**
- Which critical roles are missing?
- Who needs to be engaged next?
- Are there blockers or concerns based on committee structure?

### Step 5: Build Engagement Timeline

Construct a chronological timeline of key engagements from user-provided data and Salesforce activity:

Format as:
```
[Date] - [Activity Type]: [Description]
Example:
Jan 15, 2026 - Email Response: Opened Q4 Campaign email, clicked demo link
Jan 18, 2026 - Form Submission: Downloaded benchmark report
Jan 22, 2026 - Sales Call: Discovery call with VP Operations (30 min)
Feb 2, 2026 - Event: Attended NRF trade show, visited booth
```

Limit to the 8 most recent or most significant interactions to stay within the 2-page document limit. Highlight campaign responses that triggered MQA status and any executive involvement.

### Step 6: Analyze Signals & Intent

Synthesize engagement signals into actionable intelligence:

**Strong Intent Signals:**
- Demo requests
- Pricing inquiries
- RFP downloads
- Multiple stakeholder engagement
- Executive involvement
- Competitor mentions

**Medium Intent Signals:**
- Content downloads (whitepapers, case studies)
- Webinar attendance
- Email engagement (opens, clicks)
- Website visits to product pages

**Document:**
- What signals indicate buying intent?
- What pain points or needs are evident?
- What competitive threats exist?
- What's the urgency level?

### Step 7: Create the Word Document

Use the docx skill to create a professional Word document. **The document must be 2 pages or fewer.** This is a hard constraint — prioritize the most actionable information and cut anything that is redundant or low-value. Use compact formatting: tighter font sizes (9-10pt for body), condensed tables, and concise prose. Do not pad sections.

**Document Format:**
- US Letter size (12240 x 15840 DXA)
- 0.75-inch margins (to maximize usable space within the 2-page limit)
- Arial font throughout, 9-10pt body text, 11pt section headings
- Professional styling

**Document Sections:**

#### 1. Header: Account Overview
```
[Company Name] - Account Intelligence Card
Generated: [Current Date]  |  Account Owner: [From Salesforce]  |  Status: [MQA/Engaged/etc.]
```

#### 2. Account Snapshot (Compact table, single row per field)
- Company Name | Industry | Annual Revenue | Employee Count | HQ Location
- Account Score (Engage ICP): [X/3] | Account Score (Secure ICP): [Y/3]
- MQA Trigger Campaign: [Campaign Name]

#### 3. Salesforce Opportunities

Compact table of all opportunities found:
| Opportunity Name | Stage | Close Date | Amount | Owner |

Note closed-lost opportunities with a brief loss reason if available.

#### 4. Buying Committee Map

**Meeting Contact**: [Name, Title, Source]

**Other Known Contacts** (compact table):
| Name | Title | Buying Role | Engagement | Source |

**Missing Roles**: [List critical gaps in 1-2 lines]

#### 5. Signals & Intent (concise bullets)
- High-priority signals with source attribution
- Pain points identified (include source for each)
- Urgency assessment
- AI investment notes if relevant

#### 6. Recent News & Company Context

3-5 bullet points maximum. Each bullet must include a hyperlinked source (URL or publication name). Sourced entirely from web search. Focus only on intelligence directly relevant to the sales conversation — shrink, returns, fraud, technology investment, leadership changes, financial pressure.

#### 7. Engagement Timeline

8 entries maximum, most recent first:
```
[Date] | [Type] | [Description]
```

#### 8. Next Actions
- 3-5 prioritized next steps

**2-Page Enforcement**: Before finalizing the document, review total content length. If it exceeds 2 pages, cut in this order: (1) trim Engagement Timeline to 5 entries, (2) condense Company Context to 3 bullets, (3) compress Signals & Intent to 3 bullets, (4) remove any [NOT PROVIDED] placeholder rows from tables.

### Step 8: Finalize and Present

1. Save the document to `/home/claude` first
2. Validate document is 2 pages or fewer
3. Move to `/mnt/user-data/outputs/[CompanyName]-Intel-Card-[YYYY-MM-DD].docx`
4. Present to user with a 2-3 sentence summary

## Output Requirements

**File Naming Convention:**
```
[CompanyName]-Intel-Card-[YYYY-MM-DD].docx
Example: Acme-Corp-Intel-Card-2026-05-05.docx
```

**Document Quality Standards:**
- 2 pages maximum — hard limit, no exceptions
- All external news and intelligence includes source URL or publication name
- Professional formatting throughout
- No spelling or grammatical errors
- Consistent date formats (MMM DD, YYYY)
- Clear section headings
- Tables properly formatted with borders and shading

## Critical Implementation Notes

1. **2-Page Hard Limit**: The document must never exceed 2 pages. Ruthlessly prioritize the most actionable intelligence. If something doesn't help the AE prepare for the meeting, cut it.
2. **Source Links Required**: Every piece of external news or intelligence must include the URL or publication name. Do not include unsourced claims.
3. **Pull Salesforce First**: Run the Salesforce query before drafting the document so opportunity and owner data is available for synthesis.
4. **Cite Sources**: When including public information, note where it came from (e.g., "Reuters, Apr 2026 — [URL]")
5. **Data Privacy**: Remind user that if sharing this document, ensure compliance with data privacy policies
6. **Refresh Guidance**: Suggest updating the Intel Card before major meetings or quarterly
7. **Customization**: If user has specific formatting preferences or additional sections, adapt accordingly — but the 2-page limit still applies

## Error Handling

If missing critical information:
- Note what's missing in the document with "[NOT PROVIDED]" only where strategically important; omit the field entirely if it's low-value
- Continue with available information
- Flag gaps prominently so user can fill them in

If Salesforce returns no results:
- Note explicitly in the Opportunities section that no data was returned
- Ask the user to confirm the account name spelling used in Salesforce

If web search fails or returns no results:
- Document that current public information could not be retrieved
- Suggest user manually add relevant details

## Example User Interaction

**User:** "Create an intel card for Nordstrom. They're an MQA from the NRF Takeback campaign. Here are the contacts from Sales Nav [paste]. Meeting scheduled for Feb 15 with Jane Smith, VP Loss Prevention. Engage ICP: 3/3, Secure ICP: 2/3."

**Claude Response:**
1. Acknowledge receipt of information
2. Query Salesforce for Nordstrom opportunities and account owner
3. Run web searches for financial, leadership, news, and AI context
4. Organize buying committee from Sales Nav data, placing Jane Smith in "Meeting Contact"
5. Create compact 2-page Word document with all source links included
6. Present document with 2-3 sentence summary

**Output:** "I've created your Account Intel Card for Nordstrom — fits within 2 pages. Salesforce shows one prior closed-lost opportunity (Stage: Closed Lost, Q3 2024) owned by Carl. Web search surfaced a Q1 earnings call noting shrink as a top priority and a new VP of Supply Chain hire. Jane Smith is flagged as your meeting contact with two other known committee members identified and one gap (Economic Buyer) called out."

## Skill Maintenance

Update this skill when:
- New account scoring methodologies are introduced
- Additional connectors or data sources become available
- Document format requirements change
- New sections or analysis types are needed

Last updated: May 5, 2026
