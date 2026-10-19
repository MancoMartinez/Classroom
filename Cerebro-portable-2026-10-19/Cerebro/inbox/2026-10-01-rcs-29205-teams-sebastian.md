Hi Sebastian Rueda, one more on SBX, https://trebuco.atlassian.net/browse/RCS-29205.

The refunds to partner SVC work item returns 0 because ardm_Tender.x_partnerownedtoken stopped arriving at the 27 Aug cutover. In ARDM_PRODUCTION.C166_SBX it is TRUE on 3,927 refunds before 27 Aug and on none after, while refund volume is normal.

Do you know who owns the SnowTime tender mapping for c166_sbx? I may be looking at the wrong layer, wanted to ask before I route it.
