Hi Rajith, Shireesh,

Closing this ticket based on the following.

Root cause confirmed on the client side. 70 MAC brand stores stopped transmitting POS data between trading days 9/21 and 9/27. The raw Event Hub capture shows their data present through each store's last active day and absent afterward, so nothing reached the Appriss pipeline to load. L1 reports these stores were migrated to Shopify.

Appriss pipeline verified. GP3 counts in ardm_225.ardm_header match SECURE for stores and transactions. Reference location joins, batch timing and blob ingestion volume were ruled out.

The gap against the customer's own transaction counts already existed before the 9/21 dropout. It reflects a difference in what each side counts and is unrelated to this incident.

The customer has not responded since 10/01 and Camila has notified the CSM.

If Estee Lauder confirms a new feed for the MAC stores through Shopify or another source, or answers the reconciliation questions, please open a new ticket and link it to RCS-29179. Once the migration is confirmed, please review the Grafana store threshold of 293 with the CSM, since the MAC stores will no longer arrive through this feed.
