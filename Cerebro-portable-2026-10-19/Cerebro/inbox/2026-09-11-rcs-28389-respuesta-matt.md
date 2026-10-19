Matt, short answer: it is one field, and nobody can flip it from the UI right now, us included.

I signed in as the GUESS tenant and tried it myself today. The Locked checkbox is ticked and
unticking it does nothing, no error, no save. So this is not a customer admin permission gap,
the control is inert for Support too. That matches the title of ENG-7177, "Platform Users:
locked accounts stay locked until Appriss updates the database", which was declined on Aug 24.

The field is membership.Users.Locked in the tenant platform database. The approved remediation
from the Unification bucket review on Aug 13 is UPDATE membership.Users SET Locked = 0 for the
affected users, then purge the client cache rather than clear it. Every prior case closed the
same way, one engineer running the update: Stater Bros on RCS-28166 and RCS-28346, DSW on
RCS-27519, Krispy Kreme on RCS-27886, ADUSA on RCS-28053. Five clients, same defect.

The blocker on my side is access, not knowledge. My production SQL access is read only. I have
the runbook written with the thirteen accounts from Stephanie's Sep 4 table and Sep 11
screenshot, the SELECT to confirm the real state, the scoped UPDATE with a rowcount check, and
the cache purge. I can run the read only steps and hand the rest over. Tell me who owns the
write and it goes out today.

One flag for whoever runs it. We should look at the membership.Users columns before the update.
If the table keeps a failed attempt counter or a lockout date, setting Locked to 0 without
resetting it will re-lock the account on the next failed attempt and we will be back here in a
day.

And one for the ticket itself. 04021@guess.com logged in successfully on 9/9 at 5:12 PM and is
locked again today, same for 03964 on 9/2 and 00156 on 9/3. These are shared store logins
hitting the failed attempt threshold. Unlocking clears today's list and the list rebuilds
itself. Raising the lockout threshold for store accounts, or the admin self service you want
Carly to review, is what actually ends this.

---
Addendum, Sep 11, after running the read only steps.

Nine of the thirteen accounts are Locked = 1 in the database right now. Four more that were
locked on Sep 4 are already back to 0 and nobody on our side reports unlocking them, worth
asking whether the lock expires on its own.

I also found the full procedure in RCS-28166. Kiran unlocked the Stater Bros users on Aug 5 at
JR's request, and JR immediately told the customer to have those users run Forgot password and
set a new one. That ticket closed on exactly that. The unlock alone was never the fix. The
accounts locked because of failed attempts, so handing them back open without a password reset
sends the user straight back to the wrong password and the lock returns. That is what is
happening at GUESS.

One more thing for whoever runs the update. membership.Users has InvalidLogonAttempts and
LastLockDate. We should set Locked to 0 and InvalidLogonAttempts to 0 in the same statement. If
the app recomputes the lock from that counter rather than reading the flag, clearing only the
flag re-locks the account on the next attempt.
