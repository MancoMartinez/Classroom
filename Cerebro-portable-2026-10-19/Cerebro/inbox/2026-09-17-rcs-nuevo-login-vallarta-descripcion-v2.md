Summary: Vallarta Supermarkets, intermittent login and session errors across Chrome and Internet Explorer

Environment: Production, tenant Vallarta Supermarkets, Client ID 432.

Reporter: Tatiana Barcenas, HR Investigations Lead. Same behavior reported for Paula Lopez and Carolina Ceballos, same team.

How this surfaced. On RCS-28294, support asked Tatiana on August 25 for additional case numbers to continue a smart alert investigation. On August 31 she replied that she could not provide them because she was locked out of the system. Splitting this into its own ticket so it gets tracked as the login defect it is, separate from the smart alert engine issue on RCS-28294.

Symptom timeline.

2026-08-31, approximately 7:15am to 7:35am Pacific. Tatiana Barcenas receives Session Error, Your Incident session could not be established, after logging in.

2026-08-31, 10:39am. Carolina Ceballos reports to Tatiana that the system forced a password reset citing an outdated password, logged her out immediately after the reset, and now returns to the same Session Error screen on every reload.

Tatiana logs in successfully through Internet Explorer during this same window. Chrome is the browser that fails.

Paula Lopez and Carolina Ceballos receive the same Session Error message and are also redirected to Internet Explorer as a workaround. It works for them too.

2026-09-10. Tatiana attempts Chrome again and gets locked out. Attempts Internet Explorer and cannot log in either. Gets assistance resetting her password and logs in successfully.

Same day, a second user receives the Session Error message in Internet Explorer but can access the system through Chrome. The inverse of the pattern above.

Attachments to carry over from RCS-28294: the APPRISS RETAIL login screen showing Invalid user name and/or password, the ERMS Session Error page, and Carolina Ceballos's email of 2026-08-31 with her screenshot attached.
