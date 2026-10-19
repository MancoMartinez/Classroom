Target: Long-term solutions, row 5. Replace C5:H5 only.

Completed in the shared workbook on 17 September 2026. Verified by downloading the saved workbook and reading C5:H5 from /Users/MancoMenStudio/Downloads/Urban Outfitters - Ticket Review Aug 2026 (1).xlsx. No comments, links, local paths, PR references, or internal investigation notes were added to the workbook.

C5 Root Cause Summary
Review identified two separate failure modes. The missing customer name and account number fields were caused by an incorrect field type in the search configuration. That configuration was corrected. The zero-row export is a different symptom: the on-screen search returned results while the background export reported zero. The available evidence does not confirm a caching or session issue, and further reproduction is required to isolate that path.

D5 Fix Type(s)
Configuration validation
Engineering / Product
Quality assurance

E5 Recommended Long-Term Action
Add automated validation for search field types before configuration changes are released. Add end-to-end regression tests that compare on-screen results with the exported file, including text identifiers, customer names, blank values, standard export, and export all. For zero-row exports, improve diagnostics so each export records the search version, filters, user context, processing status, and row counts. Reproduce the reported scenario with the same saved search and filters, then use that evidence to determine whether an additional product change is required.

F5 Owner
Engineering / Product / QA

G5 Priority & Rationale
Medium-High. The known missing-field configuration was corrected. Preventive validation and stronger export diagnostics are needed to reduce recurrence and shorten resolution time if the zero-row symptom returns.

H5 Update
Configuration correction completed for the missing fields. Next steps are preventive validation, regression coverage, and targeted reproduction of the zero-row export.
