@Manisha Naik

Could you pull the log for this tracking code from the Work Item Ericka reported.

Tracking code: 774fbb98-fc34-4cd0-8ee8-538f85d2967d
Work Item: 248159
Client: 85, C085_THD
Definition: MD03-APS-D, Consecutive Markdowns for Same Payment Card
Data area: Secure Store, Markdowns
Region 0032-CANADA, District 0157-CHARL, Store 7135, Cashier LDAP DXM6269
Date range on the work item: 08/27/2026

Same format as the log you posted on 31 August at 09:45 would be perfect. I need the failing
identifier and the activity name.

Here is why it matters. The searches Simon repaired are working, and Corey confirmed that with his
users on 31 August. What Ericka is reporting is a different surface. The work item generates, it
reports 3 unique Appriss Secure IDs, and it returns no transactions with a Value Potential of 0.00.
Opening Events throws the system error above.

RCS-28543, Kinney Drugs KNY/179, is the same failure on work items rather than on searches. There
the Step3 deaggregation SQL referenced a physical column that the SnowTime migration had renamed.
That investigation also found the generated SQL persisted per work item, in
workview.WorkItemDefinitionGenerationRequest, columns DeaggregationSql and
DeaggregationNativeCommand. If that holds here, repairing a definition does not repair work items
already generated, which would explain why searches recovered and these work items did not.

I am not stating that as the cause for THD. The log tells us which column fails and whether this is
the same defect or a different one. Everything else waits on that.
