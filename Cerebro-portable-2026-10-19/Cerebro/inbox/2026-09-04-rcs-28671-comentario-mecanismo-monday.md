Compared the two deaggregation requests on run 2706EDE9 directly against the Platform DB.

RowId 0 is Ericka's work item, store 7135. RowId 1 is store 7161, generated in the same run with no
reported issue. Both started at the exact same instant, 2026-08-28 12:17:26.4033333. Both carry
Failed 0, Duplicate 0, Skipped 0. DeaggregationSql is null on both rows, consistent with the 50 run
sample measured earlier on this same period.

NativeCommandParameters carries the generated query text on both rows. The template is identical
between the two. Only the bound values differ, store, cashier, account, region. The generated SQL
selects from ardm_Header, reference_location and ardm_Tender using plain table names. No database or
schema qualifier appears anywhere in the text and no USE DATABASE or USE SCHEMA statement precedes
it.

That rules out a stale search binding as the mechanism here. There is no saved definition reference
in this text to go stale. The same generated command, submitted twice in the same second from the
same template, returned data for one store and nothing for the other. An unqualified table reference
resolves against whatever schema the session has active at execution time. Two connections hitting
the SnowTime cutover in that same minute could each resolve ardm_Header to a different underlying
object without the command text ever changing.

Nobody has confirmed this against the Snowflake connection pool itself. What it does confirm is that
resaving a search definition has nothing to bind to here, and that session or connection context
during the 28 August cutover window fits the data better than a broken definition.

Same question as before, now with a mechanism attached to it. What can trigger deaggregation again
for the 17 affected FtiIDs without a full work item regeneration, and who owns that.
