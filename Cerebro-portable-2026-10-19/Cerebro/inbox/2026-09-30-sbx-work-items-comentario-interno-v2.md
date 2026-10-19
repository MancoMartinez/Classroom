Internal note, applies to RCS-29205, RCS-29206 and RCS-29207. Update 30 Sep.

Confirmed in the tenant:
The monthly run for fiscal period 24 Aug to 27 Sep happened on 30 Sep. Control monthly definitions not in these tickets produced items that day. These three definitions have no items for that period. Prior runs on 1 Jul, 29 Jul and 26 Aug produced items for all three.

Ruled out:
Data readiness hold and fiscal year rollover. Both would have held the control definitions too.

Narrowed down:
Discount definitions without partner logic, Merch Item discounted and Controllable Discounting Multiple Items, produced items on 29 Sep for the same period. RCS-29206 groups by ardm_header.x_receivingpartnerid with StaffDiscountFlg = true. Weekly counts in ARDM_PRODUCTION.C166_SBX.ARDM_HEADER from 27 Jul to 27 Sep show no drop at the 27 Aug cutover, so the partner fields are populated.

Working hypothesis, not confirmed:
The serveware or controllable discount condition inside these definitions resolves to a column that is empty or renamed after the SnowTime cutover. For RCS-29207 the open MemberID binding defect on RCS-28873 remains a second candidate.

Next:
Pull the executed trigger SQL and its status for the 30 Sep run from query history, then measure the columns it uses by week.
