Hi, quick question on RCS-29361, Urban Outfitters client 044. The receipt for Store 124, Pos 2, Trans 1408 (TRANSACTIONID 2609079422895513998, trading day 2026-09-07) prints REFUND WITHOUT RECEIPT while it also shows the Original Transaction Information block.

The viewer call is GET /urbn/platform/viewer/store/api/v1/journal/event/2609079422895513998?connectionName=pos-data, served by GenericEventProvider (ardm_json fetch+resolve). The JSON it returns has no label text. The header has receiptedkeyedreturncount 1, no non receipted returns, and recalledflg true. The returned line has refundwithreceiptflg true. A voided sale line (UO Relaxed Fit Oxford Shirt) has refundwithreceiptflg false.

Which rule in the receipt template prints REFUND WITHOUT RECEIPT, and does it count voided lines?

Thanks.
