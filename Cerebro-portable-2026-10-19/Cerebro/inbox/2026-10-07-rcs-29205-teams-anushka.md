Hi Anushka, nice to meet you! Adarsh mentioned you are the SBX engineer, so I am starting this chat with him in the loop. Thank you for helping with this one.

The ticket is RCS-29205, a Starbucks NA High: https://trebuco.atlassian.net/browse/RCS-29205

A monthly refunds work item for c166_sbx has returned no results since the 27 Aug SnowTime cutover. I compared one week before the cutover with one week after in ARDM_PRODUCTION.C166_SBX, and these fields had data before and are empty after:

ARDM_TENDER.X_PARTNEROWNEDTOKEN: 631,190 rows before, 0 after
ARDM_TENDER.X_PARTNERIDONTOKEN: 631,190 rows before, 0 after
ARDM_HEADER.X_PAIDINPAIDOUTREASONCODE: 10,253 rows before, 0 after
ARDM_HEADER.X_PAIDINPAIDOUTREASONENUM: 10,253 rows before, 0 after
ARDM_TENDER.X_REFUNDTOOWN: 6 rows before, 0 after

The other 32 X_ fields on those tables kept their volume. The work item filters on X_PARTNEROWNEDTOKEN, so its search returns 0 rows with no error.

Would you be able to take a look at the mapping for these fields? Once they are populated again, we would also need them reloaded from 27 Aug so the 24 Aug to 27 Sep period can be regenerated. Would you like me to assign the ticket to you? The query I used and the full notes are on the ticket, and I am happy to jump on a call anytime. Thank you so much!
