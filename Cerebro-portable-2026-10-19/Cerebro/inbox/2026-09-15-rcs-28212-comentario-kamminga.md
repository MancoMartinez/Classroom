RCS-28212, 7-Eleven, root cause confirmed live today.

Case elevation copies the incident's short type code into the case Case Type field without mapping it to the case-side picklist. Confirmed on CA-44541-COR-2026-0001, the Case Type dropdown lists only Corporate, External, Franchise, Labor/Tips/Subpoena, Vendor/Contractor. The stored value COR does not exist in that list, the UI renders it as a separate checked row with an asterisk.

I tested the report-level workaround from the client's own AdHoc report Corp_Internal_Theft_Fraud, ID 5165, on a test copy, ID 5511. The event_type filter Operand is populated from the same case-side picklist regardless of comparison operator, CONTAIN, IN, or otherwise. COR cannot be selected there under any configuration, by definition it is not a valid picklist member. I also tried filtering on Case ID text directly, no text field in the report exposes the full case number string for a CONTAIN match.

There is no report-side fix available. This needs a data-level correction on the elevation logic, mapping the incident type code to the correct case Case Type value before it gets written. Client is escalated critical, needs a data correction plan and timeline as soon as you can look at it.
