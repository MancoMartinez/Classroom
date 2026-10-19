**Investigation update. PR 58962 reviewed and approved. Waiting on the operator-run seed, rebuild and reload.**

Answers from Anushka Chaudhary on my review questions, 14 Oct:

| Question | Answer |
| --- | --- |
| Lab validation | Done |
| Seed and rebuild overlap | Fixed in the last commit. Seed now stops at 21 Aug and tender is rebuilt one day per chunk, as pyardm's daily batch did. About 0.3% of tokens may still differ from pyardm |
| Paid in and paid out reload from 26 Aug | Also covers the 25 Aug events, which arrived on 26 and 27 Aug. Re-bakes ardm_json |
| X_REFUNDTOOWN | Approximation of pyardm's logic, about 6 rows a week. Not used by this work item. Owner sign-off or documented approximation |

The seed, the tender rebuild and the paid in and paid out reload need an admin role and are operator-run.

## Conversations outside the ticket

| Date | With | Outcome |
| --- | --- | --- |
| 14 Oct | Anushka Chaudhary, Teams | Answers above. I approved the PR and will verify the 24 Aug to 27 Sep work items after the rebuild |

## Still open

1. When will the operator run the seed, rebuild and reload?
2. Will the 24 Aug to 27 Sep run regenerate after the rebuild, or does it need a rerun?
