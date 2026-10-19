Hi Nichols, Peyman pointed me your way. I am on RCS-28756, the Nike ECOM order feed for client 067.

On prd-datacloud-wus2-ehub-1, entity c67_rawdata_order, both Incoming Messages and Captured Messages went to zero after 2026-08-27 19:02 UTC and have stayed at zero. Incoming sums 64.50M and Captured 64.61M over the last 30 days, so Capture kept up with everything that arrived. Nothing reached the hub after that point, which puts the gap upstream of it.

Peyman mentioned Nike sends this through our ingestion API and that our API is what lands the file into blob. So the question I need answered before I go back to Nike: did the ingestion API log any calls from Nike for the ECOM order feed after 2026-08-27 19:02 UTC? If it did, the data reached us and stopped between the API and the hub. If it did not, it never left their side.

Nike also asked us for four things and I want to send them one complete answer: the exact stream name, the consumer client ID, how the data is consumed, and what filters we apply. Can you give me those, or point me to who has them?
