**Finding. ardm_Tender.x_partnerownedtoken stops arriving at the 27 Aug cutover. This definition filters on it, so its trigger search returns 0 rows.**

| Check I ran | Result |
|---|---|
| Snowflake query history, 30 Sep 02:08:49 PT | SUCCESS, 0 rows |
| Condition in that query | T1.TransactionType = 2 AND T3.x_partnerownedtoken = :tender_ext_partnerownedtoken |

Refunds in ARDM_PRODUCTION.C166_SBX, 27 Jul to 27 Sep:

| Trading day | x_partnerownedtoken TRUE | x_partnerownedtoken NULL |
|---|---|---|
| Before 27 Aug | 3,927 | 169,878 |
| From 27 Aug | 0 | 204,745 |

Refund volume keeps flowing. Only the token is missing.

**Open questions.**

1. Is x_partnerownedtoken mapped for c166_sbx in the SnowTime tender model?
2. Who owns that mapping for this client?

Related: https://trebuco.atlassian.net/browse/RCS-29206 and https://trebuco.atlassian.net/browse/RCS-29207
