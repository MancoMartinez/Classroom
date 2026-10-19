Hi Adarsh, happy Monday! Following the new process for SnowTime escalations, I wanted to reach out about a Starbucks NA High ticket, RCS-29205: https://trebuco.atlassian.net/browse/RCS-29205

A monthly work item for c166_sbx has returned no results since the 27 Aug SnowTime cutover. Ryan DeVries reviewed it and believes some fields were not migrated. I compared one week before the cutover with one week after in ARDM_PRODUCTION.C166_SBX, and these fields had data before and are empty after:

ARDM_TENDER.X_PARTNEROWNEDTOKEN: 631,190 rows before, 0 after
ARDM_TENDER.X_PARTNERIDONTOKEN: 631,190 rows before, 0 after
ARDM_HEADER.X_PAIDINPAIDOUTREASONCODE: 10,253 rows before, 0 after
ARDM_HEADER.X_PAIDINPAIDOUTREASONENUM: 10,253 rows before, 0 after
ARDM_TENDER.X_REFUNDTOOWN: 6 rows before, 0 after

The work item filters on X_PARTNEROWNEDTOKEN. Would you be able to assign someone from your team to take a look? Once the fields are populated again, we would also need them reloaded from 27 Aug so the 24 Aug to 27 Sep period can be regenerated. I am happy to answer any questions. Thank you so much!
