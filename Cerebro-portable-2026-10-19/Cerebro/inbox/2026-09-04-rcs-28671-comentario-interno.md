# INTERNAL NOTE. NOT FOR CUSTOMER

## Correction

Recommending this to Dan Endersby's team, from the comment above on 2 September, is superseded. His team ran the cutover, they did not write the query pattern that broke during it. Do not edit Composer fields or resave any search for this defect. See below.

## Answering the question above, resave versus platform gap

NativeCommandParameters on run 2706EDE9 carries the same generated query template on both rows. RowId 0, store 7135. RowId 1, store 7161, no reported issue. Both started at the identical instant, 2026-08-28 12:17:26.4033333. Both Failed 0. Only the bound values differ, store, cashier, account, region.

Representative excerpt, RowId 0:

```
FROM ardm_Header AS T1
LEFT JOIN reference_location AS T2 ON (T1.StoreNo = T2.LocationID)
LEFT JOIN ardm_Tender AS T3 ON (T1.TransactionID = T3.TransactionID AND ...)
```

No database or schema qualifier anywhere in that text. No USE DATABASE or USE SCHEMA statement precedes it. There is no saved search reference in this text to go stale. Dan's resave hypothesis has nothing to bind to here.

An unqualified table reference resolves against whatever schema the session holds active at execution time. Two connections hitting the SnowTime cutover in the same second could each resolve ardm_Header to a different underlying object without the command text ever changing. That is how NativeCommandParameters gets generated and executed for this work item type, a Secure Engineering code path, not a Delivery execution issue and not a stale Composer binding.

## Ruled out, in addition to the table on 2 September

| Hypothesis | Why it falls |
| --- | --- |
| Stale search binding, resave fixes it, per RCS-28543 | NativeCommandParameters on both rows is a runtime generated query, not a reference to any saved search. Nothing to resave. |

## Still open

1. Confirm whether an unqualified table reference in NativeCommandParameters resolves against the session's active schema at execution time, and whether two connections could resolve it differently within the same second during a live cutover.
2. Confirm ownership of the process that writes ARDM transactions into fti.Transactions, per Andres Marciales above. Confirmed outside the SnowTime and dbt pipeline.
3. Confirm whether that write can be triggered again, scoped to the 17 affected FtiIDs, without a full work item regeneration.
4. RCS-28543, Kinney Drugs KNY/179, Under Engineering Review, Shandana Khan. Same SnowTime migration path, different failure mode. Linked for context, not as the fix path here.
5. High priority. Reopened once already, 1 September, for this same defect. Open since 28 August.
