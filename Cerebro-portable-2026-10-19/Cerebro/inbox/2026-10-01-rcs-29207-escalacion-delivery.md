**Escalating to Delivery, Secure 5.** The SFE Star Farming same day high volume definition fails on every run since the 27 Aug SnowTime cutover. No work items generate for fiscal period 24 Aug to 27 Sep.

## 1. Environment and steps to reproduce

Prod. Tenant starbucks-us, c166_sbx, ARDM_PRODUCTION.C166_SBX.

### Starbucks NA (SBX), reported 30 Sep

1. Snowflake, SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY, user SVC_ARP_PRODUCTION_166_USER, error_code 100038, from 30 Sep.
2. Open query ID 01c77251-0109-d5e7-0120-d20111b67fc7, 1 Oct 14:05 PT. Its columns are aliased Topic_-_SFE_-_Star_Farming_same_day_high_volume.
3. Executive Workbench, Workview Monitor set to this definition, date range 1 Jul to 1 Oct.

Expected: runs on 1 Jul, 29 Jul, 26 Aug and 30 Sep.
Actual: no run on 30 Sep. The query fails with:

```
Numeric value '1867074335977200' is not recognized
```

## 2. Findings

| Day | Status | Executions |
|---|---|---|
| 26 Aug | SUCCESS | 35 |
| 28 Aug | FAIL | 4 |
| 9 Sep | FAIL | 4 |
| 30 Sep | FAIL | 276 |
| 1 Oct | FAIL | 180 |

Failing condition:

```
T9.x_MemberID <> 70267962874
```

**x_MemberID is TEXT in ARDM_PRODUCTION.C166_SBX. The definition compares it to an unquoted number.** arpfiles PR 57459 retyped MemberID from Int64 to String, confirmed by Sebastian Rueda on 1 Oct. My reading, unverified: this definition's own condition still declares MemberID as Int64. StarRewardTransactions.search had the same pattern on https://trebuco.atlassian.net/browse/RCS-28873.

## 3. Troubleshooting performed

Snowflake query history for the service user. Executive Workbench for this definition and for control fiscal period definitions, which produced items on 30 Sep. That rules out a data readiness hold and the fiscal year rollover. Teams with Sebastian Rueda on 1 Oct, quoted above. No other conversations. Support cannot read the definition condition.

## 4. Still open

1. Does this definition's condition carry its own Int64 type for MemberID?
2. Once corrected, can the 24 Aug to 27 Sep run be regenerated?

Related: https://trebuco.atlassian.net/browse/RCS-28873, https://trebuco.atlassian.net/browse/RCS-29205, https://trebuco.atlassian.net/browse/RCS-29206
