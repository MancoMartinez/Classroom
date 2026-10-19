@Ryan Barlow I went through the claim records in APIS PROD to add some data points to your timeout finding, in case it helps.

IN-37827-COR-2026-0023, a GL claim entered by the call center on 9/22 at 9:23 PM, shows 26 Sedgwick.Submit entries in its Change History with no user attached. The first one is 9/23 at 12:49 AM and they repeat about every four hours, with a burst on 9/24 between 12:10 PM and 2:07 PM that I assume were your manual runs. The claim stays at Status Pending and Process Status Submitted after every attempt, so each run picks it up again.

For comparison, IN-41257-COR-2026-0002 from the April incident in RCS-26609 has a single Sedgwick.Submit entry on 4/22 at 8:45 PM. If the error handling you added in April is what now keeps a claim in the queue when a run fails, the repeated entries would be that logic working as intended, and every run since 9/22 would be failing before the file is written. Am I reading that correctly?

The last Sedgwick.Submit on this claim is 9/25 at 7:17 PM. There is nothing for the expected runs around 9 PM, 1 AM and 5 AM. Was the job paused or changed after that run?

Two things would help me update 7-Eleven: whether the pending WC and GL claims since 9/21 will go out on the next successful run without a manual step, and whether you have an approximate time for that run. Peta Godzik and John Smithson are waiting on an update for their Risk team.
