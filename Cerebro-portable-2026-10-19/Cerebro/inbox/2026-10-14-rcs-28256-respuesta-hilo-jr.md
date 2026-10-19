J.R., Camila and Rae,

I drilled into the four tickets and the user data behind them. Here is the update.

https://trebuco.atlassian.net/browse/RCS-27269 (June 4) built the path that loads the Incident security level from the daily teams file into Secure. https://trebuco.atlassian.net/browse/RCS-27578 (June 26) found that Secure was ignoring those levels at sign in, and the fix went live July 2. https://trebuco.atlassian.net/browse/RCS-27941 (July 22) was a separate configuration matter in Case Type security, resolved September 16. https://trebuco.atlassian.net/browse/RCS-28256 (August 10) started as slow loads, now in https://trebuco.atlassian.net/browse/ENG-9990, and has since collected the blank Incident Security ID reports.

Why cases keep appearing. There are two separate causes, both confirmed in the database today.

First, the level is not being applied at sign in for a group of users. 46 users who signed in since the July 2 fix have Location Manager or District Manager in the daily file, but their account was left without a level, which shows as a blank Incident Security ID. All 46 are users without an Incident user record, while every user who has that record received the level, 79 of 79. One example: Christi Winters has had a manual SSO+ level since April 17, signed in on July 14, and her account still had no level. The level is in the data, but the sign in step is not carrying it over for these users. This needs Engineering to review the sign in logic.

Second, locations that do not exist on our side. 287 Incident users receive an office location in the daily file that is not in our location table. Those users get no hierarchy, so they cannot pick a store when creating an incident. Chris Orth is one of them.

Also, the daily SSO file for October 14 has not loaded yet. The latest load is from October 13.

What we did today: set the level for Paul Bubelnik Jr, Nancy Bolhoff and Rachel Dill, confirmed Chaz Hyman and Vincent Fortner already have it, and asked Colton which store Chris Orth should be assigned to.

Next: I posted these findings in RCS-28256 with a proposal to split it into one ticket per cause, and asked Matthew Kamminga whether the sign in issue should go to Engineering. The location issue would go to Delivery. Once we confirm the manual fix holds after sign in, we can apply it to the other affected accounts while the cause is reviewed.

Rae, for the meeting with Tailored, Friday October 16 at 12:00 PM ET works for me if that is still the slot.

Camila, RCS-28256 is past 60 days, so Jira asks for a review with Support management first. Could we use a few minutes before Friday for that?

Juan Martinez
Appriss Retail Support
