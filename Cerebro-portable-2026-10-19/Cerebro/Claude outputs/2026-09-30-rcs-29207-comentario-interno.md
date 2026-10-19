**Investigation update.** This definition produced no items for fiscal period 24 Aug to 27 Sep.

| Check I ran | Result |
|---|---|
| Executive Workbench, control fiscal period definitions | Items on 30 Sep |
| Executive Workbench, the three reported definitions combined | Runs on 1 Jul, 29 Jul and 26 Aug. None on 30 Sep |

**Ruled out so far:** data readiness hold and fiscal year rollover.

**Still open, both unverified:**

1. Stars or MemberID columns empty after the 27 Aug cutover.
2. The MemberID numeric binding in DeaggregationEngine, noted on https://trebuco.atlassian.net/browse/RCS-28873 on 25 Sep. That one would leave a "Numeric value is not recognized" error in Snowflake query history.

MemberID query history is not checked yet.

Related: https://trebuco.atlassian.net/browse/RCS-29205 and https://trebuco.atlassian.net/browse/RCS-29206
