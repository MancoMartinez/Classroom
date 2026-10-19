Hi Bikash,

I picked up RCS-27942 to give you a hand with it. Two things.

First, I could use your help on access. On 6 Aug you queried dbo.Merchandise and got back
ShopliftingID 5333930 with TrackingNo 1ZH4E0790301911717. I have been trying to reach that same data
and I keep landing on empty tables. Which server and database did you run that against? I tried the
074 vss platform database on both sqlmi-prd-wus2-arp-001 and pd-lpms-uswest2-sqldb-001 and
incident.Merchandise came back with zero rows on both.

Second, I want to check something with you in case I am reading it wrong. Looking at the SOW in
ENG-1071, item 4 says the uploads batch call the API to enrich the cartons with Class, Units and
Total Retail. If I am reading that right, CartonClass and CartonContentCode would not come from the
customer import file at all, they would be populated on our side from the API response. That would
explain why Angie sees the retail value but not the other two, and it might mean we do not need her
IT team to confirm anything about the file. Does that match your understanding, or is there
something in the flow I am missing?

There is also ENG-4225, which shipped to production on 25 June. It changed CartonContentCode and
CartonClass on the Merchandise grid from plain text columns to dropdowns that resolve against
ListMaster categories, gated by a CategoryCodeFields config item, and it was set up for VSCoCorpAP
client 123634. Angie reported this on 22 July with June data, so the timing lines up. Worth ruling
out before we take it to engineering.

Happy to jump on a call and go through it together if that is easier.

Thanks,
Juan
