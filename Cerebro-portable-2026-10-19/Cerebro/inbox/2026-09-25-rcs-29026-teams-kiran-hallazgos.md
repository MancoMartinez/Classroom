Hi Kiran, I went back through Grafana and I think I have a clearer picture, would love your eyes on it:

1. On 9/20 (case 0619-27, when alerts worked) every "Begin of SmartAlert.ProcessSmartAlert" has its "End of SmartAlert.ProcessSmartAlert", and the alerts were inserted into SmartAlertProcess.
2. On 9/25 between 20:04 and 20:23 UTC for 441 there are 89 Begin and 0 End. Runs evaluate the alerts but never log End, and "ProcessAlertQueue 1. dt.Rows.Count" grows from 217 to 222.
3. Case 2547-32 on 9/24: the first save ran at 20:20 UTC while it was still open, and every save after that, including the close at 20:27, exits with "still on processing". So it never got evaluated once it was Closed.
4. "Current ClientID:" shows empty on every run on 9/25.

My read is that the runs don't finish, the processing flag never clears, and the queue keeps growing. My test case was left Open, so I'm not counting it. Does this match what you see in the settings?
