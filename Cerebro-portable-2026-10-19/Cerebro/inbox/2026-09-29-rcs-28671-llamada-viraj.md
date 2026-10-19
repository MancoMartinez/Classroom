Quick update on RCS-28671, THD.

Mohammed deleted the 17 work items and reran them. Only 2 came back. 248159, Ericka's, is not one of them.

The reason: the MD03 search has a date window that follows the day it runs, not the period you rerun. So rerunning 8/27 today returns zero. I confirmed in Snowflake that the data is there, and with the right window both MD03 groups show up.

So this can't be fixed from WISC. It needs Engineering to rerun it anchored to the period. I asked Mohammed yesterday, and today I'm moving the ticket to Under Engineering Review with Shandana so it's tracked.

On the customer side, I told Ericka the replacement isn't available yet. When Engineering confirms the path, I'll send one update to Corey and Ericka covering the full list, not just 248159.

Anything you heard from Mohammed or the customer that I should know?
