Shan, I moved RCS-27991 to Under Engineering Review and it is with you. Engage Analytics SKU detail panels not populating on Harbor Freight and Floor and Decor. High, open since 7/27.

This is the same defect as RCS-28068, which you already accepted into development on 8/18. I linked them. Two questions.

Does the RCS-28068 work cover HFT and FAD, or do those tenants need separate work? And can you give me the ADO bug number so this ticket can track it?

One thing worth checking before anyone opens new work. This defect shipped a fix once already, ADO 66220 against RCS-23643 for Foot Locker in the November 2025 release, titled Engage Analytics dashboard Top 10 lists not populating. Root cause then was the reference data backload failing on a ProductHierarchy4 type conversion, plus the Hierarchy Filter not applying. This may be a regression of that.

Repro steps for all three tenants, the ruled out list and the full history are in the ticket.
