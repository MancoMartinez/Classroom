Makes sense. One thing before I try that, heads up from a similar ticket, RCS-28543 on another client. Resaving there re-copied a stale binding instead of fixing it and made the failure count worse, 3 of 30 to 11 of 30. Might be worth trying on one work item first rather than all 17.

Also, GetInstantAnalyticsEvents takes both ftiID and tileID, so I think the search that's failing is tied to a tile, not the work item definition itself (md03-cit-d). Do you know the name or path of that search, or how I'd find it? I don't have visibility into which tile that is from the front end.
