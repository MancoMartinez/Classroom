Read only. Do not modify files, do not run DML or DDL, do not commit.

Context: client AAP (021, C021_AAP) wants to move all their files (STRINVDT inventory, POS TRE_TranHeader/Detail/Tender, tlog zip) to arrive at 9:30 AM EST, not before October 21. Ticket: RCS-29224. PR 58891 (enrich_ardm_item.sql) is merged in main.

Answer with file paths and line numbers as evidence. Mark anything you cannot prove from the code as unverified.

1. Which models build inventory_itemposition, and where do totalsalesquantity, totalsalesvalue, totalreturnedquantity and totalreturnedvalue come from?
2. If POS arrives after inventory_itemposition was built for a day, does any model, incremental window or REBUILD_RANGE recalculate those totals? After how many days?
3. What triggers the hourly load at :30 UTC, and does any model wait for POS or tlog completeness before running?
4. Does PR 58891 change anything about inventory_itemposition, or only ardm_item (department, description, tax, updateddatetime)?
5. If every AAP file shifts 8 hours later, which model windows could miss data (tlog, POS, inventory)? List each window and its lookback.
6. Which scheduled searches or work items for C021 run before 9:30 AM EST?
