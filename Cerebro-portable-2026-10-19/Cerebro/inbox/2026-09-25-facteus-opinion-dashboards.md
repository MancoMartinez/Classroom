Facteus, opinion on the dashboards for Viraj

Date 2026-09-25. What to say if Viraj asks what I think and what I'd suggest.

My take, neither dashboard means much until it's been checked against a real alert. They exist, Chris linked them in a comment, but nobody has confirmed either one actually reflects what happens when Facteus fires. Two dashboards with no live validation is worse than one, we'd be choosing between them blind.

What I'd suggest, three things.

Pick one as the source of truth for Support, not both. Two dashboards for the same thing means we'll end up checking the wrong one under pressure, or checking both and wasting time reconciling them.

Whichever one we pick, validate it the next time a real alert fires, or ask Data Engineering to walk us through what it looked like the last time one did. We shouldn't put a link in the Confluence pages that nobody's actually opened during an incident.

Once it's picked and validated, get it linked into the internal and external process pages directly. Right now it only lives in a Jira comment from August, that's why Support almost missed it. If it's not in the runbook, it doesn't exist for whoever's on call.
