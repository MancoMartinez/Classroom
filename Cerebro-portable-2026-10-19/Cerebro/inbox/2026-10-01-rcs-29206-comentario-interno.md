**Finding. The 0 for 24 Aug to 27 Sep is the real result of the rule. No partner met all three thresholds in that period.**

| Fiscal period | Trigger search rows, 30 Sep | Partners with controllable discounts on hierarchy 085 | Partners meeting 2 transactions, 2 dates and $30 |
|---|---|---|---|
| 29 Jun to 26 Jul | 4 | 131 | 3 |
| 27 Jul to 23 Aug | 2 | 48 | 2 |
| 24 Aug to 27 Sep | 0 | 103 | 0 |

**How I checked.** I took the discount codes from the transactions behind August work items 156176 and 156175: Partner Discount code 6, controllable codes 3 and 4, ProductHierarchy1 085. I rebuilt the rule on ARDM_PRODUCTION.C166_SBX with those values. P2 matches the live search exactly. P1 is one short because the rebuild leaves out the second product hierarchy list, which I could not read.

**Ruled out so far:** the reference_Employee join, the partner fields on ardm_header, the item and product joins, and a change in discount codes. All complete before and after 27 Aug.

**Conclusion.** No defect found for this definition. The period had partner activity on serveware, and none of it reached the thresholds.

Related: https://trebuco.atlassian.net/browse/RCS-29205 and https://trebuco.atlassian.net/browse/RCS-29207
