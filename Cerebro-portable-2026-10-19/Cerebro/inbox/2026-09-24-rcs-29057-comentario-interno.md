# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Environment and steps to reproduce

**Environment: Production**, ADUSA tenant.

1. Open case 2026-AHOLD DELHAIZE USA SERVICES, LLC-9999-278. Incident Type Identification Request.
2. Open Report Narrative from the Incident Workbench.
3. Generate the LP External Doc from View / Print Incident.

Expected: the Report Narrative section shows the case narrative.
Actual: the section is empty. Attached LP_EXTERNAL 2.pdf and LP_EXTERNAL 3.pdf.

Same result on test case 2026-AHOLD DELHAIZE USA SERVICES, LLC-9998-11, attached LP_EXTERNAL 4.pdf, and on 2026-AHOLD DELHAIZE USA SERVICES, LLC-9999-223, incident date 2026-07-20, attached LP_EXTERNAL 6.pdf.

## 2. Findings

1. Verified. The eight LP External templates in Document Management, LP_EXTERNALold.docx and LP_EXTERNAL201272023.docx included, fill Report Narrative from the merge field `shoplifting_reportnarrative`. **None of them references Synopsis.**
2. Verified. For Identification Request, Hide / Display Fields had `uco_ReportNarrative` at Visible No. The Report Narrative page showed only the Synopsis box. Shoplifting Incident has it at Visible Yes.
3. Verified. After setting it to Visible Yes, the narrative editor appears above Synopsis. Text in that editor prints on the LP External. Text in Synopsis does not. Attached LP_EXTERNAL 5.pdf from 9998-11.
4. Verified. 9999-278 and 9999-223 have the narrative editor empty and the full text in Synopsis. The 9999-223 text is dated 7/23/26, before the July 29 URL migration.
5. Verified. Search For Incident filtered by Identification Request returns 500 or more cases, the grid limit.
6. Precedent, same customer. https://trebuco.atlassian.net/browse/RCS-22886 had the same symptom on 9999-292 and closed 2025-09-18 as Fixed Configuration, with no technical detail.

My reading: a configuration and data placement issue, not a template change. Users of this incident type had no narrative editor on screen and wrote in Synopsis, which the template does not read.

## 3. Change applied in production

| Incident Type | Form Field Name | Setting | Before | After |
|---|---|---|---|---|
| Identification Request | `uco_ReportNarrative` | Visible | No | Yes |
| Identification Request | `uco_ReportNarrative` | Display on Printout | No | Yes |
| Identification Request | `title_ReportNarrative` | Display on Printout | No | Yes |

Applied by Juan Martinez on 2026-09-24 through the row edit in Hide / Display Fields. Apply Settings was not used. Screenshots before and after attached.

## 4. Troubleshooting performed, and the limits of support access

Order followed: reproduced on 9999-278, reproduced on 9998-11 to rule out location 9999, compared Hide / Display Fields between Identification Request and Shoplifting Incident, applied the change, regenerated 9998-11, opened 9999-223 as a case created before the migration, and read the merge fields of the eight LP External templates.

Claude flagged the hidden `uco_ReportNarrative` as the likely root cause. I checked the field configuration for both incident types, regenerated the LP External on 9998-11 before and after the change, opened 9999-223 without editing it, and pulled the templates from Document Management to read their merge fields. Here is what I found: the template has always read `shoplifting_reportnarrative`, and the case text for this incident type sits in Synopsis. This is what I think is happening: the narrative editor was hidden for Identification Request, so users wrote in the only box available. Could someone else evaluate this and give me your thoughts?

Conversations outside the ticket: none. BJ Probert, who resolved https://trebuco.atlassian.net/browse/RCS-22886, is no longer with the company.

Support cannot move field data across existing cases in bulk.

## 5. Ruled out. Do not repeat

| Hypothesis | Refuted by |
|---|---|
| Specific to location 9999 | 9998-11 reproduced the same result |
| The LP External template changed its narrative source | All eight template versions read `shoplifting_reportnarrative` |
| The RCS-22886 configuration reverted | `Shoplifting_ReportNarrative` row still Visible Yes, Printout Yes |

## 6. Still open

1. For existing Identification Request cases with the narrative editor empty, is copying the Synopsis text into `shoplifting_reportnarrative` the right path, or would adding Synopsis to the LP External template fit better?
2. Which Form Field Name backs Synopsis on this incident type?

Ticket opened 2026-09-22, priority Medium. New cases print as expected since the change.
