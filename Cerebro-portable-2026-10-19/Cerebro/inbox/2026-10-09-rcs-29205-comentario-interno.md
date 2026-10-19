**Investigation update. Fix in review: PR 58962, SnowTime repo, by Anushka Chaudhary.** https://dev.azure.com/apprissdevops/Sysrepublic%20Secure/_git/SnowTime/pullrequest/58962

| Part of the PR | Status |
| --- | --- |
| X_PARTNEROWNEDTOKEN and X_PARTNERIDONTOKEN accumulator, built on Ryan DeVries's branch rdevries-rcs29205, with NULL instead of FALSE for unmatched tokens | In review |
| X_PAIDINPAIDOUTREASONCODE and X_PAIDINPAIDOUTREASONENUM | In review |
| X_REFUNDTOOWN approximation | In review |
| Historical seed, rebuild from the cutover and work item regeneration | After deploy. The rebuild needs an admin role, which Anushka is arranging |

## Conversations outside the ticket

| Date | With | Outcome |
| --- | --- | --- |
| 7 and 8 Oct | Ryan DeVries, Teams | Shared his branch. Rows from 27 Aug need a rebuild from the cutover date |
| 8 Oct | Anushka Chaudhary and Adarsh Kumar, Teams | Branch shared. Anushka confirmed it helps and that mapping changes are needed |
| 9 Oct | Anushka Chaudhary, Teams | Asked me to review PR 58962. I sent questions on lab validation, seed and rebuild dates, and who runs the rebuild |

## Still open

1. Has the integrated branch been validated in lab?
2. Who runs the seed, the rebuild from the cutover and the 24 Aug to 27 Sep regeneration?
