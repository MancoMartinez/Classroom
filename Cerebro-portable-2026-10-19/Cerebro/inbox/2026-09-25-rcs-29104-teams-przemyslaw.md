Hi Przemysław, Ryan DeVries mentioned you mapped GPC 356. Could you help me with RCS-29104? https://trebuco.atlassian.net/browse/RCS-29104

Since trading day 2026-05-04, about 40% of GPC transactions in ardm_356 load with header and items but no tender rows, across roughly 1,650 stores. Example: store CHA266, ticket 533653 on 9/17, a Visa refund with no tender.

The closest change I see in c356gpc is c736cbfa on 5/3, load_raw_pos.py with decrypted_input going from True to False. I may be reading it wrong. Where does the tender come from for GPC, and could that change affect it?
