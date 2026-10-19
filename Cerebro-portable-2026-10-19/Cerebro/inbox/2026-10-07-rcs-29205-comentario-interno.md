**Root cause confirmed by SnowTime engineering.** Anushka Chaudhary, SBX engineer, reviewed it on 7 Oct: the c166_sbx SnowTime mappings emit NULL for the five fields in my note of 5 Oct. The values came from pyardm-built rows, which ended in late August.

## Repopulation, per Anushka

| Fields | What pyardm did | Can it be repopulated |
| --- | --- | --- |
| X_PAIDINPAIDOUTREASONCODE, X_PAIDINPAIDOUTREASONENUM | Built header rows, transaction types 50 and 51, from the paidin_paidout feed | Yes. The feed is complete. Needs a new flat model and new header rows with historical transaction IDs |
| X_PARTNEROWNEDTOKEN, X_PARTNERIDONTOKEN | Kept a permanent token table, ref_employee_owntendertoken, not in ARDMPROD | Partly. A rebuild from ardm_customer history reaches 44% at 6 months. Full history not measured |
| X_REFUNDTOOWN | Set when the cashier matches the partner ID on a refund | Only as complete as the token fields |

**This definition filters on X_PARTNEROWNEDTOKEN, so a regenerated 24 Aug to 27 Sep period may be partial.**

## Conversations outside the ticket

| Date | With | Outcome |
| --- | --- | --- |
| 6 Oct | Adarsh Kumar, Teams | Routed to Anushka Chaudhary, SBX engineer |
| 7 Oct | Anushka Chaudhary and Adarsh Kumar, Teams | Confirmed root cause. Anushka is reviewing the mapping |

## Still open

1. Once the mapping is updated, will new transactions carry X_PARTNEROWNEDTOKEN in full?
2. What coverage would a backfill of 24 Aug to 27 Sep reach?
