Hi Sanath, thanks for flagging this. I identified that Claire's ingests via API, endpoint c439_rawdata_postransactions, which is a Gateway file source. Per SLA Rules 9.5 that type routes to Engineering with product type RTIaaS, so I am moving RCS-29037 there instead of answering it from Support.

There is a precedent on file, RCS-28170, TJX, same feed type. The client's API keys expired, the feed stopped, and one trading day landed under the Work Item volume threshold. Once the client resumed sending, that volume recovered on its own with no separate historical file involved. That points to resuming transmission being enough for Claire's too.

One point still needs Engineering to confirm before we can tell the customer for certain. Whether a trading day that fell under the threshold during the outage gets picked up if the missing data arrives late, or stays skipped. I am sending that to Engineering now and will update the ticket once I hear back.
