**Investigation update.** This definition produced no items for fiscal period 24 Aug to 27 Sep.

| Check I ran | Result |
|---|---|
| Executive Workbench, control fiscal period definitions | Items on 30 Sep |
| Executive Workbench, the three reported definitions combined | Runs on 1 Jul, 29 Jul and 26 Aug. None on 30 Sep |
| ARDM_PRODUCTION.C166_SBX.ARDM_HEADER by week, 27 Jul to 27 Sep | StaffDiscountFlg stable, no drop at the 27 Aug cutover |
| Snowflake query history, 30 Sep, 50 latest partner queries | All SUCCESS, no error message |

**Ruled out so far:** data readiness hold, and the fiscal year rollover. Other fiscal period definitions ran on 30 Sep.

**Still open:** the partner SVC tender side. ardm_Tender.x_partneridontoken is not measured yet. My reading, unverified: a tender column left empty after the cutover.

Related: https://trebuco.atlassian.net/browse/RCS-29206 and https://trebuco.atlassian.net/browse/RCS-29207
