# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Correction

None. No previous statement on this ticket needs correction.

## 2. Environment and steps to reproduce

Environment: APIS Production, 7-Eleven tenant, Company ID 7-eleven.

### 7-Eleven, case CA-44541-COR-2026-0001, verified live today

1. Log in to APIS PROD as jbarber.
2. Open the case through All Event Search, Store 44541.
3. Open the Case Type field dropdown on the case form.
4. Look at the list of selectable values.

Expected: COR listed as a selectable Case Type value, matching the value already stored on the case.
Actual: The dropdown lists only Corporate, External, Franchise, Labor/Tips/Subpoena, Vendor/Contractor. COR is not among them. A separate checked row reading star COR renders above the list, outside it, to represent the value already stored on the record. Screenshot attached to this ticket.

### Corp_Internal_Theft_Fraud report, ID 5165, test copy ID 5511

1. Duplicate report 5165 into a test copy, ID 5511, to avoid touching the client's live report.
2. Open Configure filters on the copy.
3. Change the case.event_type filter comparison operator to CONTAIN, then to IN.
4. Open the Operand selector for that filter under each operator.

Expected: COR available as an operand value, or a free text option, so the filter can include it alongside Corporate.
Actual: The Operand control is a fixed picklist under every operator tried. It lists only Corporate, External, Franchise, Labor/Tips/Subpoena, Vendor/Contractor. COR is never offered. Screenshots attached.

## 3. Findings

- Verified: on CA-44541-COR-2026-0001, the stored Case Type value COR does not exist in the case side picklist. Live dropdown, 9/15.
- Verified: the AdHoc report Operand for case.event_type pulls from that same picklist regardless of comparison operator. Tested CONTAIN and IN on report copy 5511.
- Verified: filtering on case.iice_id with CONTAIN and a free text operand returns no additional cases. That field is most likely the internal numeric case ID, not the displayed Case ID string.
- Unverified, from AI triage, listed so it is not re-explored: the root cause is the incident to case elevation step copying the incident's short type code into the case Case Type field without mapping it to a valid case side value.
- Precedent, RCS-1508: in 7-Eleven, the Event Type field on screen maps to event_sub_type in the filter, not event_type. Confirms field naming in this tenant is not literal.

## 4. Troubleshooting performed, and the limits of support access

Claude flagged this as the likely root cause. I checked it myself against the live case and the report builder, and here is what I found. This is what I think is happening. Could someone else evaluate this and give me your thoughts?

I logged into APIS PROD myself and opened the case, the dropdown and the report builder directly, step by step, as described above. I do not have access to the elevation logic itself or to the underlying tables that would confirm where the incident's type code gets written to the case record. That is what Engineering access would confirm.

No conversations happened outside this ticket about this specific finding today.

## 5. Ruled out. Do not repeat

- Report level workaround via CONTAIN or IN on case.event_type. Operand is picklist bound, COR is not a member by definition.
- Free text filter on case.iice_id. Field does not hold the visible Case ID string.
- Self defined SQL style field in the report builder. Not attempted, out of scope for Support without Engineering sign off on a client owned report.

## 6. Still open

1. Confirm whether the elevation logic is copying the incident type code without mapping it, as observed on this one case.
2. If confirmed, provide an estimate for a data level correction and whether it needs a one time backfill for cases already affected.
3. Confirm how many cases across 7-Eleven currently carry an invalid Case Type value like this one, if that is queryable faster on your side than through the report builder.
4. This is currently a Critical client escalation. Please advise on timeline as soon as you have one, even a rough one.
