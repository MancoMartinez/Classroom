# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Environment and steps to reproduce

**Environment: Production**, ADUSA tenant, apps.apprissretail.com/adusa.

1. Open case 2026-AHOLD DELHAIZE USA SERVICES, LLC-9999-278. Incident Type Identification Request.
2. Open Report Narrative from the Incident Workbench.
3. Generate the LP External Doc from View / Print Incident.

Expected: the Report Narrative section shows the case narrative.
Actual: the Report Narrative section is empty. Attached LP_EXTERNAL 2.pdf and LP_EXTERNAL 3.pdf, 2026-09-24.

Reproduced on test case 2026-AHOLD DELHAIZE USA SERVICES, LLC-9998-11, location 9998 TEST LOCATION ONLY. Attached LP_EXTERNAL 4.pdf.

## 2. Findings

Hide / Display Fields, read in production on 2026-09-24:

| Form Field Name | Identification Request, before change | Shoplifting Incident |
|---|---|---|
| `uco_ReportNarrative` | Visible **No**, Printout No | Visible **Yes**, Printout Yes |
| `title_ReportNarrative` | Printout No | Printout Yes |
| `Shoplifting_ReportNarrative` | Visible Yes, Printout Yes | Visible Yes, Printout No |

1. Verified. The LP External Doc prints the top editor, `uco_ReportNarrative`. Text entered in Synopsis, `Shoplifting_ReportNarrative`, does not print. After the change, 9998-11 prints the top editor. Attached LP_EXTERNAL 5.pdf.
2. Verified. With `uco_ReportNarrative` hidden, the Report Narrative page showed only Synopsis. Case 9999-278 has its full narrative in Synopsis and the top editor empty.
3. Verified. Display on Printout does not control this print. Case 2026-FOOD LION ,LLC-1080-40, Associate Dishonesty, has `uco_ReportNarrative` Printout No and still prints the narrative. Attached LP_INTERNAL.pdf.
4. Verified. After the change, filtering `uco_ReportNarrative` by Visible No returns no incident types. Identification Request was the only one.
5. Verified. Search For Incident filtered by Incident Type Identification Request returns 500 or more cases, the grid limit. Unverified inference: all of them hold the narrative in Synopsis only, since the top editor was hidden for this type.
6. Precedent, same customer. https://trebuco.atlassian.net/browse/RCS-22886 closed 2025-09-18 as Fixed Configuration. The internal note there shows `Shoplifting_ReportNarrative` set to Printout Yes. That row is unchanged today.

## 3. Change applied in production

| Incident Type | Form Field Name | Setting | Before | After |
|---|---|---|---|---|
| Identification Request | `uco_ReportNarrative` | Visible | No | Yes |
| Identification Request | `uco_ReportNarrative` | Display on Printout | No | Yes |
| Identification Request | `title_ReportNarrative` | Display on Printout | No | Yes |

Applied by Juan Martinez on 2026-09-24 through the row edit in Hide / Display Fields. Apply Settings was not used. Screenshots before and after attached.

## 4. Troubleshooting performed, and the limits of support access

Order followed: reproduced on 9999-278, reproduced on 9998-11 to rule out location 9999, compared Hide / Display Fields between Identification Request and Shoplifting Incident, applied the change to the one row set, regenerated the document on 9998-11, and checked another incident type with Printout No.

Claude flagged the difference in `uco_ReportNarrative` between the two incident types as the likely root cause. I checked the field configuration for both types, regenerated the LP External Doc on 9998-11 before and after the change, and generated the document on an Associate Dishonesty case with Printout No. Here is what I found: the top editor is what prints, and it was hidden for Identification Request. This is what I think is happening: after the September LPMS change the template reads `uco_ReportNarrative`, while ADUSA users kept writing in Synopsis because it was the only box on the page. Could someone else evaluate this and give me your thoughts?

Conversations outside the ticket: none. BJ Probert, who resolved https://trebuco.atlassian.net/browse/RCS-22886, is no longer with the company.

Support cannot see which field the LP External template reads, and cannot update existing case data in bulk.

## 5. Ruled out. Do not repeat

| Hypothesis | Refuted by |
|---|---|
| Specific to location 9999 | 9998-11 reproduced the same result |
| The RCS-22886 configuration reverted | `Shoplifting_ReportNarrative` row still Printout Yes |
| Display on Printout gates the print | 1080-40 prints with Printout No |

## 6. Still open

1. Can the existing Identification Request cases have `Shoplifting_ReportNarrative` copied into `uco_ReportNarrative` where the top editor is empty? The count is 500 or more.
2. Did the September LPMS change move the Report Narrative source of the LP External template to `uco_ReportNarrative`?

Ticket opened 2026-09-22, priority Medium. The customer has the workaround for 9999-278 and knows new cases print.
