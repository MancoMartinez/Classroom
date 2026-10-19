**Escalating to Engineering.** Reference text prints on blank audit forms for the new fiscal year templates. The customer asks for Display Reference to default to No.

## 1. Environment and steps to reproduce

Production, SpartanNash netTrack.

1. Admin, Manage Audits, open <template name and version>.
2. Edit Base, Sections/Questions, open a question that has Reference/Help text.
3. Display Reference reads Yes. Screenshot attached.
4. The customer prints the blank form and the reference text appears. Screenshot image001.png, 8 October 2026.

Expected: reference text does not print. Actual: it prints.

## 2. Findings

| Source | Finding | State |
| --- | --- | --- |
| Audit Editor, Production | Display Reference is Yes on the question I opened | verified |
| Config 190 LIMITED Supermarket Store Audit v22 and config 191 MARTIN'S LIMITED Supermarket Audit v22, Production, 8 October | Both are Version FY2027.1, last edited 7 October 2026 by the same user ID, and both use Audit Report SCORED 2026.1.docx and Action Plan Report 2026.1.docx | verified |
| Same configs, question IDs | Live questions of config 190 span IDs 57547 to 57873, above the two V27 test templates, configs 239 and 240, which end at 57353. Live questions of config 191 are one block of 109 consecutive IDs starting right after its highest deleted question, 57762. Deleted sections hold 282 questions in config 190 and 654 in config 191 | verified. Consistent with the customer's account of deleting the old questions and importing new ones |
| Display Reference values | Config 190 live: 66 of 110 questions on, exactly the 66 that carry reference text. Config 191 live: 105 of 109 on, 28 of them without text. Nine other live configs, from FY2025.1 to FY2027.1: 596 of 646 questions on, and every question on in five of them. Config 160, a 2021 template: 200 of 212 on | verified. Reading: Yes looks like the default across the tenant and the import is not proven to be its origin |
| Config 223, the Metcalfes Supermarket Self-Audit, Production | Version FY2027.1, last edited 2 October 2026. Live questions are one block of 82 consecutive IDs, 52516 to 52597, above the 251 questions in its deleted sections, which end at 52391. 68 of the 82 are on. The customer says this one only changed version | verified. Closest name match to Metcalfe's Self in the ticket |
| https://trebuco.atlassian.net/browse/RCS-26171 comment of 3 April 2026 | All questions of config 190 were set to No. Production today shows none off in the live questions and 48 off with text among the 282 deleted ones | ticket statement, current values verified |

Same behavior on this tenant before:

| Ticket | Outcome |
| --- | --- |
| https://trebuco.atlassian.net/browse/RCS-19415 | Code change in the 26 March 2025 release |
| https://trebuco.atlassian.net/browse/RCS-26171 | Display Reference set to No on all questions of one template, April 2026. The comments mention a new method to populate the form, introduced for page breaks |
| https://trebuco.atlassian.net/browse/RCS-27315 | Removed by hand on one template, June 2026 |
| https://trebuco.atlassian.net/browse/RCS-27794 | Closed in July 2026 after the customer reported it no longer printed |

## 3. Troubleshooting performed, and the limits of support access

The Talos triage on this ticket proposed that the bulk import turns Display Reference on. I read the value on one question, ran read only queries on the configuration tables in Production, and read the customer's account of the rollout. The proposal covers imported templates only, and Metcalfe's Self changed version only. Other live configs show Display Reference on for most questions regardless of version, so Yes looks like the tenant default. This is my reading, unverified. Could someone else evaluate it and give me your thoughts?

Conversations outside the ticket: a screen share today with the assigned support engineer. No others.

Support has no recorded method to change Display Reference in bulk. https://trebuco.atlassian.net/browse/RCS-26171 shows it done on 3 April 2026 and does not say how.

## 4. Still open

1. Is Display Reference on by default for new questions, and does the import or a new template version set it to Yes? Could it default to No?
2. Can Display Reference be changed in bulk on the affected templates in Production, and by whom?
3. Does a new template version copy the questions into new rows? Config 223 changed version only, per the customer, and its live questions are a new block of consecutive IDs.
4. Did printing start honoring Display Reference after the change to how the form is populated, as the comments in https://trebuco.atlassian.net/browse/RCS-26171 suggest?
