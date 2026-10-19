Hi Ryan, thank you again for sharing the branch. I went through it and the accumulator approach makes a lot of sense, following the c179_kny precedent. I had a few questions, and I may be reading some of this wrong:

1. Anushka mentioned that a rebuild from ardm_customer history reached about 44% at 6 months. Your seed goes back to 2020. Would it be worth comparing notes with her so we land on one approach?
2. The seed reads ARDM_PRODUCTION.C166_SBX from 2020 onward, while the notes describe the full history in ARDMPROD.ARDM_166. Does C166_SBX carry that full history, or would the earlier years come from ARDM_166?
3. The ARDM_TENDER rows already loaded since 27 Aug would keep NULL. Would a REBUILD_RANGE from 27 Aug after the seed be the way to fill them, so the 24 Aug to 27 Sep work items can be regenerated?
4. The enrichment returns FALSE for tokens with no match, where pyardm left them NULL. Could that change affect other searches?
5. The branch covers the two token fields. Would the paid in and paid out reason fields be a separate change?

Thanks so much for all the work on this!
