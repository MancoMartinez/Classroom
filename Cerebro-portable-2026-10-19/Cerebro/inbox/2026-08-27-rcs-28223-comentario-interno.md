# INTERNAL NOTE. NOT FOR CUSTOMER

@Matthew Kamminga picking this up from David Vargas, who has left the team. Answering both of your questions from 25 Aug, and correcting the analysis this ticket currently carries.

## 1. Direct answers

**Yes, every affected question is a grid question.** The discriminator is `AuditConfigQuestion.GridCols`. Populated at 166 bytes and the question fails. Empty and the question works. No exception across all 82 questions in the audit.

Reproduction steps are in section 4.

## 2. Corrections to what is already in this ticket

**`FieldType` is not a column.** The field is `AuditConfigQuestion.QuestionType`, and in this audit it holds 1, 2, 5 and 9. It never holds 35 or 11. Searching for those values returns nothing.

**Question type is not the common factor.** Q65 is QuestionType 1 and fails. Q116 is QuestionType 1 and works. The Manager questions that fail are type 2, the Crew ones are type 5, and Q65 is type 1. What they share is a populated `GridCols`.

**The defect spans two screens.** David named only `AuditSection_V24_S4.aspx`, ScreenMasterID 83, Manager Week 1. The Crew questions live on `AuditSection_V24_S9.aspx`, ScreenMasterID 88, Crew Week 1. All ten sections of this audit carry grid questions.

**Drop the `Uni_Jul_26_SSOMapping` label and ENG-6198.** Both belong to the customer's login failure, split out to RCS-28486. You and Shandana already unlinked ENG-6198 on 19 Aug.

## 3. What the data establishes

Tenant `mcdonalds`, Client ID 402, `AuditConfigID` 4, Restaurant Cash Audit.

The grid stores its rows in `AuditMasterQuestion.Comments` as nine comma separated fields, rows delimited by a pipe. `GridConfig` declares the shape and matches the rendered table exactly:

```
9,2,Employee Name,1|Coaching,1|1st Verbal,1|2nd Verbal,1|1st Written,1|2nd Written,1|First and Final,1|Termination,1|Comments,1
```

Nine columns, two rows. Identical across all 45 grid questions. The configuration survived the migration intact.

**Columns 2 through 8 stopped accepting input in August 2026.** Those are Coaching, 1st Verbal, 2nd Verbal, 1st Written, 2nd Written, First and Final, and Termination. Counting grid answers that carry data in any of those seven columns, per month:

| Month | Col 2 to 8 populated | Col 1 and 9 only | Col 9 only | Total |
|---|---|---|---|---|
| 2025-06 | 1360 | 2780 | 164 | 4304 |
| 2025-12 | 1128 | 2252 | 197 | 3577 |
| 2026-03 | 1419 | 2396 | 222 | 4037 |
| 2026-06 | 1377 | 2549 | 196 | 4122 |
| 2026-07 | 815 | 1512 | 174 | 2501 |
| 2026-08 | **0** | 57 | 3 | 60 |

Twenty consecutive months between 561 and 1419. August is zero. Total volume collapses from 2501 to 60 in the same step, which is users abandoning a control that does not respond.

What the stored data looks like, before and after:

```
2024, working:   Alfredo ,x,,,,,,,-$36.19|Brandon,x,,,,,,,-12.72
27 Aug 2026:     Channele ,,,,,,,,will coach on documentation for crew |Sylvana,,,,,,,,Will coach on procedures
28 Aug 2026:     ,,,,,,,,Corina$-21.36|,,,,,,,,
```

Nine fields are still written every time. The eight consecutive commas are columns 2 through 8 arriving empty. In the 28 Aug case column 1 did not take the name either, so the user pushed "Corina$-21.36" into the Comments column.

This rules out a dead save path. The control still writes, with the correct field count, and the middle columns arrive empty.

**Timing.** This tenant migrated on 27 July 2026. All 93 screens in the tenant were rebuilt on 29 July 2026 at 05:39, `LastSavedByID` 0, no human edit since. July retains 28 normal days and 815 populated middle columns. August is the first full month after the rebuild and holds zero. The cut falls inside that window. I have not established causation, only the interval.

## 4. Environment and steps to reproduce

Environment: **Production**. Not reproduced in Test. Support has read only database access on this tenant.

### Manager Week 1

1. Sign in to `apps.apprissretail.com/mcdonalds/nettrack/` with Manager rights.
2. Open an audit on Restaurant Cash Audit, section Manager Week 1. Path: `/mcdonalds/nettrack/Audit/screens/incident/402/audit/screens/AuditSection_V24_S4.aspx`
3. Click Expand All.
4. Go to question 2, `AuditConfigQuestionID` 57, "Are there any managers who are at +/- $2 threshold as per Cash Management Policy?"
5. Set Response to Yes. The nine column grid renders below.
6. Click into the `Coaching` cell on row 1 and type an x.

Expected: the cell accepts the character and it persists on save as field 2 of the row.
Actual: no input is accepted in any of columns 2 through 8.

Questions 4 and 6, IDs 60 and 61, behave the same.

### Crew Week 1

1. Same session. Section Crew Week 1. Path: `/mcdonalds/nettrack/Audit/screens/incident/402/audit/screens/AuditSection_V24_S9.aspx`
2. Click Expand All.
3. Go to question 2, `AuditConfigQuestionID` 64, "If so, identify the top two (2) crew members, dollar amount, and what action was taken."
4. Click into the `Coaching` cell on row 1 and type an x.

Expected and actual as above. Questions 4, 5, 7 and 8, IDs 65, 66, 68 and 69, behave the same.

### Live records you can open

| Audit | Date | What it shows |
|---|---|---|
| 4694-30612 | 27 Aug 2026 | Columns 1 and 9 populated, 2 through 8 empty |
| 781-30619 | 28 Aug 2026 | Column 9 only, name and amount merged into it |
| 959-30133 | 6 Aug 2026 | The customer's own audit, store 545, still open, no grid data |

Working control on the same screens: questions with empty `GridCols`, IDs 116, 117, 118, 62 and 63, accept text in their Comments box today.

## 5. Ruled out. Do not repeat

| Hypothesis | Why it fell |
|---|---|
| Grid configuration lost in the migration | `GridCols` at 166 bytes and `GridConfig` at 254 bytes, identical across all 45 grid questions |
| Permission, readonly or hidden flag | `ScreenDetail` for screens 83 and 88 returns 8 rows each with `ReadOnly`, `HiddenField` and `FieldProtected` all 0 |
| Answer storage schema drift | `AuditMasterQuestion` holds one generic `Answer` and `Comments` pair for every question type |
| Incomplete screen rebuild, `BuildStatus` CREATED | 93 of 110 screens in the tenant share that status, 72 Audit and 21 other modules |
| Orphaned Screen Labels, per the RCS-28032 pattern | Every `ScreenDetail` row in the tenant is orphaned, 676 Audit and 594 other modules. `ScreenLabel` holds 407 rows with IDs 100 to 2309 while `ScreenDetail` points at six digit IDs. The join does not apply here and does not single out Audit |
| Platform Cohesion cookie handoff, ENG-6198 | Unlinked on 19 Aug. Belongs to the login failure, now RCS-28486 |

## 6. Troubleshooting performed

Read only queries against the tenant database covering `AuditConfig`, `AuditConfigSection`, `AuditConfigQuestion`, `AuditMaster`, `AuditMasterStore`, `AuditMasterQuestion`, `ScreenMaster`, `ScreenDetail` and `ScreenLabel`. No writes. Client screenshots with URL and timestamp reviewed, both filed on this ticket.

AI assisted: yes. Claude used to review ticket history, extract the Client ID and screen paths from the client screenshots, build the queries and draft this note. Every figure above comes from a query result or from the ticket. None inferred.

Conversations with engineers outside this ticket: none.

## 7. What I need from Engineering

1. Inspect the grid control render for columns 2 through 8 on `AuditSection_V24_S4.aspx` and `AuditSection_V24_S9.aspx`. Column 1 and column 9 respond intermittently, columns 2 through 8 never do. That asymmetry is the lead.
2. Confirm whether the 29 July screen rebuild changed how the grid control is emitted for `GridConfig` values of the form `9,2,...`.
3. Tell me whether other tenants that migrated in the RET20260727 wave show the same drop. Christian Dior, Skechers and Vallarta left on the same server on 27 July.
4. Give me the ADO number once raised.

Customer has been on a Comments field workaround since 24 Aug. One risk worth flagging: for grid questions that field is the grid's own storage, so free text typed there overwrites the nine field structure. Not yet observed in this tenant. The customer has only used it on non grid questions.

Ticket opened 6 Aug, 21 days old, Medium, Escalated. Requesting transition to Under Engineering Review.
