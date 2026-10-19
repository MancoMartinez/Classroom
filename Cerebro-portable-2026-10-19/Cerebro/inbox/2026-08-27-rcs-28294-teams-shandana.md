Hi Shandana, RCS-28294 Vallarta Smart Alerts. I posted the reproduction steps you asked for, consolidated into a single escalation note with the environment, the findings and what I ruled out, so you only need to read one comment. Moving it back to Under Engineering Review.

Two cases to diff. 48575 satisfied the filter and generated three SmartAlertProcess rows. 48786 satisfied the same filter seven days later and generated none, so the engine was never invoked for it.

One thing worth checking before anyone picks it up. ENG-7359, Smart Alert not working with Quick Entry, describes users not receiving a CPF cookie and the alert never being created. That matches the zero row case. I have not verified whether 48786 came through Quick Entry, so I have flagged it as a candidate rather than a link. If it is the same defect, tell me and I will close this one against it.

Thanks.
