# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Environment and steps to reproduce

**Environment:** Production, Vallarta tenant, Client ID 432, `apps.apprissretail.com/vallarta/nettrack/`.

### Vallarta Supermarkets (VSA), reported 2026-08-31

1. Sign in at the Secure portal, Vallarta HR account, Chrome.
2. Reach the session handoff at `SystemSelect.aspx`.

Expected: incident session establishes.
Actual: Session Error, "Your Incident session could not be established." Screenshot attached, captured 2026-09-10.

### Same tenant, password reset path, reported 2026-08-31

1. Sign in, forced password reset citing an outdated password.
2. Complete the reset. Reload the page.

Expected: session continues.
Actual: logged out immediately, stuck on Session Error on every reload. Reported by Carolina Ceballos, email attached, 2026-08-31 10:39am.

No calls or Teams messages outside this ticket on this issue.

## 2. Findings

- **Failure is browser dependent, direction not fixed.** Verified. 8/31, three users hit Session Error in Chrome, reached the system in IE. 9/10, a fourth user hit it in IE, reached the system in Chrome.
- **Password reset does not resolve it.** Verified. Carolina Ceballos reset on 8/31, logged out immediately, stuck on Session Error.
- **This surfaced as a side effect of a support request.** Verified, from RCS-28294, https://trebuco.atlassian.net/browse/RCS-28294. I asked for case numbers on August 25, she replied August 31 that she was locked out.

| Precedent | Ticket | Mechanism |
| --- | --- | --- |
| Stater Bros, identical message and URL | RCS-28061, https://trebuco.atlassian.net/browse/RCS-28061 | Null or empty `SecurityLevel` in `incident.LPUser2`, resolved as config update |
| Vallarta, earlier login failure | RCS-28024, https://trebuco.atlassian.net/browse/RCS-28024 | Email never linked in ERMS before cutover |

## 3. Troubleshooting performed, and the limits of support access

Reviewed the RCS-28294 comment thread for origin and timeline. Reviewed RCS-28061 and RCS-28024 for matching mechanisms.

Claude flagged the RCS-28061 SecurityLevel mechanism as the likely match, based on the identical message and URL. I have not queried `incident.LPUser2` for Vallarta yet to confirm. This is a hypothesis from precedent, not from this tenant's data. Could someone evaluate it once I run that check.

Support does not hold Vallarta HR credentials and cannot reproduce this directly. Support cannot read the SSO authentication log.

## 4. Still open

1. Confirm whether `incident.LPUser2.SecurityLevel` is null or empty for the four affected users, the same check that resolved RCS-28061. I can run this once the column is confirmed present.
2. Confirm whether this is the RCS-28061 mechanism, the RCS-28024 mechanism, or a third cause.
3. Explain the inverse browser pattern between 8/31 and 9/10. A pure cache or cookie theory does not cover both directions.

Related: RCS-28294, https://trebuco.atlassian.net/browse/RCS-28294, smart alert engine, tracked separately.
