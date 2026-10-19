## Same symptom confirmed, details on the linked ticket

https://trebuco.atlassian.net/browse/RCS-28966

Transaction 2609179959263358647 returned 0 rows on 2026-09-18 and is in Prod now. I ran the counts and posted them with my questions on the linked ticket.

| Table | Rows | Distinct content |
|---|---|---|
| ARDM_TENDER | 4 | 1 |
| ARDM_TRANSACTIONDISCOUNT | 32 | 8 |
| ARDM_ITEM | 38 | 37 |

Tender and discount rows repeat. Item rows do not. The cause for this transaction is unconfirmed. I will update here when the linked ticket answers.

Conversation outside the ticket: Teams chat with Viraj Kansara on 2026-10-05.
