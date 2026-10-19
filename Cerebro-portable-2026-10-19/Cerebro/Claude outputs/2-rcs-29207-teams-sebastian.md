Hi Sebastian Rueda, quick one on SBX, https://trebuco.atlassian.net/browse/RCS-29207.

The SFE Star Farming same day high volume work item fails on every run since the cutover. Snowflake query history shows "Numeric value is not recognized" on the condition T9.x_MemberID <> 70267962874. It ran fine on 26 Aug and has failed 456 times between 30 Sep and today.

You know PR 57459 better than anyone. Did it cover this definition, or is this one still carrying MemberID as Int64 in its own condition? I may be missing something, wanted to check before I route it.
