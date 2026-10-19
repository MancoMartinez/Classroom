**Cause found. The trigger search for this definition fails on every run since the cutover.**

| Check I ran | Result |
|---|---|
| SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY, user SVC_ARP_PRODUCTION_166_USER | Query aliased Topic_-_SFE_-_Star_Farming_same_day_high_volume |
| Status by day | 26 Aug SUCCESS 35. 28 Aug FAIL 4. 9 Sep FAIL 4. 30 Sep FAIL 276. 1 Oct FAIL 180 |
| Last failure | 1 Oct 14:05 PT, query ID 01c77251-0109-d5e7-0120-d20111b67fc7 |

Error, verbatim:

```
Numeric value '1867074335977200' is not recognized
```

The condition that fails:

```
T9.x_MemberID <> 70267962874
```

**Finding.** x_MemberID is TEXT in ARDM_PRODUCTION.C166_SBX. The definition compares it to an unquoted numeric literal, so Snowflake casts every MemberID to a number and stops on the first value it cannot convert. The generator retries every 15 minutes and fails each time.

Same error family as the MemberID retype on https://trebuco.atlassian.net/browse/RCS-28873.

**Open question.** Did arpfiles PR 57459 cover this definition, or does its condition still carry the Int64 type?

Related: https://trebuco.atlassian.net/browse/RCS-29205 and https://trebuco.atlassian.net/browse/RCS-29206
