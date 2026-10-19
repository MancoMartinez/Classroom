Internal note, applies to RCS-29205, RCS-29206 and RCS-29207

Working these three together. Same reporter, same fiscal period 24 Aug to 27 Sep 2026, three different definitions returning 0 after non-zero results in the two prior periods.

c166_sbx cut over from legacy pyardm to SnowTime on 27 Aug 2026, confirmed on RCS-28873. The failing period is the first one that crosses the cutover. All three definitions depend on client _EXT fields: partner discount, partner SVC tender and stars or MemberID.

Working hypothesis, not confirmed: one or more of those fields now resolves to a SnowTime column that is empty or renamed, so the trigger search returns 0 rows without error. Same family as RCS-28873 and RCS-28848. For RCS-29207 a second candidate is the open MemberID numeric binding defect in DeaggregationEngine noted on RCS-28873 on 25 Sep.

Timing and fiscal rollover stay open until checked. A hold on data readiness would affect every monthly definition for the period, not only these three.

Next checks: manual run of each trigger search for the failing and a prior period, run records in workview.WorkItemDefinitionGenerationRequest, and a null count by week on the relevant _EXT columns in ARDM_PRODUCTION.C166_SBX.

Note for anyone reading the RTS triage page for RCS-28873: section 4.2 says SBX has no SnowTime cutover. That was corrected on the ticket on 10 Sep.
