Hi Enrique, good question, and I am not 100% sure myself, so take this as where I would start.

Before changing anything, I would confirm which setting actually drives that idle timer. On Big Y (RCS-28153) the session timeout came from CPF.Core.LogOnTimeoutMinutes in Control Panel, Engineering, Config Items, and since ENG-7184 the effective value is CustomerEditedValue if it is set, otherwise Value. Kohl's calls this a new idle timer that was not in the release notes, so it might be something else that came with a recent release. Could you check that config item for Kohl's first, read only, and see what value it has?

For the permission part, I have not seen a written rule on who approves config changes. I would ask Vedant Shirude, since he owned ENG-7184 and knows how that timeout works, or Peyman Motlagh on Delivery, since config already in production usually goes to Delivery. The customer already asked for it in writing. I would wait for one of them to confirm before changing it.

If you find out who owns this, let me know so we can write it down for the team.
