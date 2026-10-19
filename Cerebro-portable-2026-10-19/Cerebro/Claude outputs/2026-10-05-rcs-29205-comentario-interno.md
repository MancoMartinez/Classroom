**Investigation update.** Ryan DeVries, Delivery, reviewed this on 2 Oct.

## Finding from Delivery

**Ryan's read: some c166_sbx fields were not migrated to SnowTime at the 27 Aug cutover.** This matches my data in the note of 1 Oct: x_partnerownedtoken is TRUE on 3,927 refunds before 27 Aug and on none after.

Ryan noted that missing fields or feeds will likely need the SnowTime team, beyond a mapping correction on the Delivery side.

## Conversations outside the ticket

| Date | With | Outcome |
| --- | --- | --- |
| 2 Oct | Ryan DeVries, Teams | Reviewed the ticket. Proposed a working session with the support team on this ticket |

## Still open

1. Which c166_sbx fields were left out of the SnowTime migration?
2. Who on the SnowTime team owns adding them?
3. Once added, can x_partnerownedtoken be reloaded from 27 Aug and the 24 Aug to 27 Sep run regenerated?

Related: https://trebuco.atlassian.net/browse/RCS-29207
