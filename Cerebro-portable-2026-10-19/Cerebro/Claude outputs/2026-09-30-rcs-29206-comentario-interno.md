**Investigation update.** This definition produced no items for fiscal period 24 Aug to 27 Sep. Its last items came from the 26 Aug run.

| Check I ran | Result |
|---|---|
| Executive Workbench, control fiscal period definitions | Items on 30 Sep |
| Work View, Merch Item discounted and Controllable Discounting Multiple Items | Items on 29 Sep for the same period |
| ARDM_PRODUCTION.C166_SBX.ARDM_HEADER by week, 27 Jul to 27 Sep | StaffDiscountFlg and x_receivingpartnerid stable, no drop at the 27 Aug cutover |
| Snowflake query history, 30 Sep, 50 latest partner queries | All SUCCESS, no error message |

**Ruled out so far:** data readiness hold and fiscal year rollover.

**Still open:** the serveware and controllable discount condition. Its trigger SQL is not among those 50 queries. My reading, unverified: that condition resolves to a column left empty after the cutover.

Related: https://trebuco.atlassian.net/browse/RCS-29205 and https://trebuco.atlassian.net/browse/RCS-29207
