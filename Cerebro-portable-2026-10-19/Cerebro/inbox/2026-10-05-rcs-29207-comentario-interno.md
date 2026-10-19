**Handoff to Carl Costelow, Delivery Secure 5.** Ryan DeVries reviewed this on 2 Oct and pointed it to Carl's team, since the search broke when the MemberID field type changed.

## Conversations outside the ticket

| Date | With | Outcome |
| --- | --- | --- |
| 2 Oct | Ryan DeVries, Teams | Removing and re-adding the column in the search did not fix it. Suggested Carl Costelow |
| 2 Oct | Carl Costelow, Teams | Sent the error, the condition and this ticket |
| 5 Oct | Carl Costelow, Teams | Agreed to look into it |

Steps to reproduce, the error and the query ID are in my escalation note of 2 Oct.

## Still open

1. Does this definition's condition still carry MemberID as Int64 after arpfiles PR 57459?
2. Is the fix configuration on your side, or does it need Engineering?
3. Once corrected, can the 24 Aug to 27 Sep run be regenerated?
