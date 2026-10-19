Workbook: /Users/MancoMenStudio/Downloads/Urban Outfitters - Ticket Review Aug 2026.xlsx. Tickets contains only RCS-28339. Long-term solutions row 5 references all three tickets.

Issue / Theme: Excel export failures: missing field values and zero-result asynchronous exports

Related Tickets: RCS-28339, August 2026. RCS-23141, September 2025. RCS-26238, March to May 2026.

Root Cause Summary: The tickets do not share one confirmed cause. RCS-26238 was caused by two text DisplayFields in Urban Same Tender Card being declared as System.Double instead of System.String. RCS-23141 shows the same search and fields, and repository history preserved those types during the incident, making the same cause highly likely. RCS-28339 is distinct: Email Only Lookup showed eight rows while the asynchronous export reported zero. Its cause remains unconfirmed. Current evidence does not establish a caching or session defect.

Fix Type(s): Delivery and configuration quality control. Engineering and QA for the asynchronous export path.

Recommended Long-Term Action: Add a validation gate for tenant search definitions that rejects incompatible DisplayField types before merge and deployment. Add tests that compare grid and Excel values for text identifiers, leading zeros, customer names, nulls, normal export, and export all. For zero-result exports, make the interactive search and task use the same serialized request. Record the search revision or hash, filters, parameters, tenant and user context, connection, task ID, row counts by stage, and terminal error. Report upstream exceptions as Failed instead of Complete with zero rows. Reproduce RCS-28339 with its saved search and four filter variants before selecting a code change.

Owner: Delivery for Arp Files validation. Search and Export Engineering for request consistency and telemetry. QA for content validation.

Priority & Rationale: Medium-High. The known field-type defect has a deployed correction in PR 51987 and PR 52242. A prevention gap remains. The zero-result pathway lacks sufficient telemetry to diagnose a recurrence from a ticket alone.

Immediate verification: Confirm Urban production uses System.String for both fields. Reproduce RCS-28339 with the same user, search revision, data window, and filter 338553. Collect the task ID and file.

Full evidence: investigaciones/excel-urban-root-cause-2026-09-17.md
