Hello team, here are the five points in order.

1. Exact stream names. Appriss does not subscribe to a stream on Nike's side. Nike delivers this data by posting it to the Appriss ingestion API, on a separate route per data type. The order feed uses the route provided to your team at onboarding.

2. Consumer client ID. There is no Appriss consumer client ID for this feed. The credential in use is the OAuth client ID Nike authenticates with when posting to us.

3. How the data is being consumed. Not a Kafka consumer and not an S3 sink. Your system posts the payload to our ingestion API over HTTPS with OAuth authentication.

4. Filters being used. None.

5. Examples of missing data. This is a complete absence of order data, not individual missing events. The last order data reached us on 2026-08-27 at 19:02 UTC and nothing has arrived since. Daily volume before that point ran between 195,352 and 234,363 ECOM transactions.

Two things I need from you. Whether anything changed on your side around 2026-08-27 in the credential or the endpoint used for this feed. And the response codes your system received on its posts after that timestamp.
