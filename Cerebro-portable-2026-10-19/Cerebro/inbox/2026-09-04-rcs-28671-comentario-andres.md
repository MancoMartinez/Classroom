Andres, thanks. That closes the source data question. Confirming for the record: intact in ARDM, gap sits in fti.Transactions during the cutover window, nothing to backfill on the Snowflake side.

The customer beat us to the specific events. Store 7135, register 51, cashier DXM6269, 8/27, transaction IDs 8989, 8990, 8991. Same account across all three per their search, no need to paste the number here. Confirm those are the 3 when you get a chance.

One thing to reconcile before anyone touches Composer. Dan's read was that a search is failing and resaving it might auto fix the binding. Your finding points somewhere else, a platform side job that never wrote these rows during cutover, not a search definition issue. Those are two different fixes. Can you and Dan align on which one applies before we try either?

Real question underneath both: what writes ARDM transactions into fti.Transactions, and can that be triggered manually for the 17 FtiIDs.
