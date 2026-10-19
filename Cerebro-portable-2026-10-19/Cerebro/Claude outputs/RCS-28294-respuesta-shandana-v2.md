Hi Shandana, you are right that this ticket picked up an unrelated symptom. Tatiana lost access to the system on August 31 while trying to send me the additional case numbers I asked for on August 25, and the login and session behavior she has reported since then is a separate defect from the smart alert engine.

I have opened RCS-28977 for the login and session behavior.

On the smart alert side, nothing changes from my August 27 comment. The open question is still the one I flagged there. ShopliftingID 48575 produced three SmartAlertProcess rows and 48786 produced zero, so the engine was never invoked for 48786, and that needs the application log around 2026-08-18 23:11 to explain.

I also have an answer now to the timestamp caveat from that same comment, where I asked to confirm which surface renders UTC and which renders local before trusting any timestamp from this tenant. The Change History modal adds a flat 1 hour to the raw UTC value instead of converting to Pacific. Raw incident.CaseChanges.DateChanged for case 2026-ADUP-40-96 reads 2026-08-10 23:23:43 UTC, which converts correctly to 4:23pm Pacific and matches what the customer reported. The modal displayed 8/11/2026 12:23 AM, exactly the raw value plus 1 hour. This confirms the 8 hour gap in my August 27 comment came from the render, not from a batch timing issue, and it is safe to treat the stored timestamps as accurate going forward.

Could you take another look at the 48786 zero row question with that scope narrowed to just the smart alert engine.
