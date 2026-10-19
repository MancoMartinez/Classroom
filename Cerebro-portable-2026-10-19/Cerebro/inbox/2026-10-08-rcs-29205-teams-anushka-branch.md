Hi Anushka, Adarsh, quick update on RCS-29205. Ryan DeVries from Delivery also looked into this and has a branch in the SnowTime repo you may find useful: rdevries-rcs29205

It adds a reference_partnerownedtendertoken accumulator plus an enrich_ardm_tender model for the two token fields, following the c179_kny precedent, and a year-chunked historical seed script that has not been run. A few notes from Ryan:

1. Starbucks only has 1 year of retention, so the seed may not need full history.
2. Both schemas should have full history before the cutover. The rows since 27 Aug are the ones that are wrong.
3. The rows from 27 Aug onward would need a rebuild from the cutover date to fill in correctly.
4. The paid in and paid out reason fields are likely the same problem, but not covered in his branch.

Would this be helpful for your fix? Once the data is rebuilt, the 24 Aug to 27 Sep work items would also need to be regenerated. Would you like me to assign RCS-29205 to you? Thank you so much!
