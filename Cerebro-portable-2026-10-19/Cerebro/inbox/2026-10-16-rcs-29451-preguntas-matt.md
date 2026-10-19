Questions for Matt following the TBI call, October 16

1. Explicit Security ID
J.R. asked whether TBI could send the Incident Security ID explicitly instead of deriving it from the teams file. Would that bypass the failure covered by ENG-10069, or use the same assignment path? If viable, which file, field, values and precedence over team mappings and manual overrides would we support?

2. First sign in and returning users
Rachel had level 5 in SSO+ before account creation, but her first SSO sign in created a NULL SecurityID while assigning groups and a team. Christi has an older persistent level assignment and also had a blank account level. Does ENG-10069 cover both paths, or does the returning user case need separate investigation?

3. Immediate recovery
TBI says some users sign in only once or twice a year. Can we reconcile existing blank Security IDs safely without waiting for another login? Who would own that work, how would we preserve intentional overrides, and what test would approve it?

4. SSU offices and DCs
Chris originally received 90002005; Colton confirmed 40002005 as his correct location. The customer showed SSU in the Brand column. Ryan said it appears we add the 9 but did not recommend replacing it with 4. What is the intended model: a distinct office/DC location or a mapping to an existing brand location? Where can we verify the current SnowTime rule?

5. Which source needs correction?
Which source defines valid locations, and which supplies user assignments? If a DC must be added or mapped, who owns each change and how does it reach both Secure and Incident? Chris's hierarchy was corrected manually; incident creation still needs confirmation.

6. Feed freshness
The October 15 investigation found security assignment timestamps still at October 13, although ReferenceDataBackLoad ran without reported errors. TBI showed a file named for October 14. What batch, receipt and processing evidence can confirm the latest data reached SSO+? Under SnowTime, are unchanged row timestamps expected?

7. Owners and next checkpoint
ENG-10069 is currently Backlog and unassigned. Who takes the security defect, who owns the SnowTime/location investigation, and should the latter have separate technical tracking under RCS-29451? What evidence and next update date can we agree before closing?
