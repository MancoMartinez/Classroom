**Investigation update. Five c166_sbx fields stopped arriving at the 27 Aug SnowTime cutover.** Verified today in ARDM_PRODUCTION.C166_SBX, comparing 17 to 23 Aug with 31 Aug to 6 Sep.

| Field | Rows with data before | Rows with data after |
| --- | --- | --- |
| ARDM_TENDER.X_PARTNEROWNEDTOKEN | 631,190 | 0 |
| ARDM_TENDER.X_PARTNERIDONTOKEN | 631,190 | 0 |
| ARDM_HEADER.X_PAIDINPAIDOUTREASONCODE | 10,253 | 0 |
| ARDM_HEADER.X_PAIDINPAIDOUTREASONENUM | 10,253 | 0 |
| ARDM_TENDER.X_REFUNDTOOWN | 6 | 0 |

The other 32 X_ fields on these four tables kept their volume. This definition filters on X_PARTNEROWNEDTOKEN.

## Conversations outside the ticket

| Date | With | Outcome |
| --- | --- | --- |
| 5 Oct | Adarsh Kumar, Teams | Sent this list and asked for a SnowTime resource, per the new SnowTime escalation process |

## Still open

1. Can these fields be mapped again for c166_sbx?
2. Once mapped, can they be reloaded from 27 Aug so the 24 Aug to 27 Sep run can be regenerated?
