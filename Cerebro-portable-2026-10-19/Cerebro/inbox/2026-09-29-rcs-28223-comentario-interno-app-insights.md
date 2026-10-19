New symptom, separate from the grid issue. NSN 930 and NSN 14283 cannot log in with their usual password. Not the same failure point for both, so not treating them as one issue yet.

NSN 930, 29 Sep, approx 12:03 PM PST, stops at the email step, no error shown.
NSN 14283, 29 Sep, approx 1:09 PM PST, apps.apprissretail.com/mcdonalds/signin, systemselect.aspx, system error on password submit.

Checked membership.Users for 14283 and five other mcdonalds store accounts as control, none locked, zero failed attempts. Account looks healthy, likely not a lockout.

I do not have access to appi-prd-wus2-arp, my Azure RBAC only covers a few VMs. Could someone with access pull requests and exceptions for apps.apprissretail.com around 19:03 and 20:09 UTC on 29 Sep?

One unconfirmed note: the 14283 URL lands on systemselect.aspx, same entry point as the GetEncryptionKey theory from RCS-28321, which did not hold up in RCS-28984. Flagging the coincidence only, not the cause.
