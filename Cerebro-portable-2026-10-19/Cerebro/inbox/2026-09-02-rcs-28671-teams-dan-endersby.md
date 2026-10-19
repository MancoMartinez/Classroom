Dan, RCS-28671. THD, 17 work items from 28 Aug missing their event rows, right in the SnowTime cutover window Simon confirmed for that day. WISC rerun doesn't fix it, just skips as duplicate.

Does this fall under your team? If so, who rewrites those event rows and can you confirm on the ticket.

---

missed their event rows ?
so is snowtime not making a event row

---

That's what I don't know yet. fti.Transactions has zero rows for these 17. Work item itself generated fine, just no events behind it. Can't tell you if SnowTime skipped writing them or wrote them somewhere that didn't carry over.

Timing is the only lead I have. All 17 hit between 12:05 and 13:07 on the 28th, same window as the cutover.

I reproduced the error myself, not just the customer, so it's not a one-off on their end.

Simon's the one who told me the 28th was your cutover date. He also said dedup on WISC "has been issues in the distant past" and there's now dedup logic, which is what's skipping my rerun instead of fixing it.

One more thing, my role doesn't have access to C085_THD or C085_THD_SNOWTIME in Snowflake. Could you check if the transaction behind work item 248159 exists in one, the other, both, or neither. Store 7135, trading day 2026-08-27. That tells us if the source data is fine and something downstream dropped it, or if it's missing at the source.
