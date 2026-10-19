**Escalating to Secure / Incident Engineering.** Matt Kamminga was working this with me and is out until 2026-10-05. The ticket is High and the resolution SLA is breached.

## 1. Environment and steps to reproduce

**Environment: Production.** Tenant `209-tbi`, Tailored Brands. Web role `web-prd-wus2-arp-nettrack`.

1. Sign in to Secure as a Tailored Brands user.
2. Open Incident from Secure. The transition lands on `SystemSelect.aspx`.
3. Time the transition from the click until the page renders.

Expected: not documented. Support holds no target load time for this path.
Actual: 35 to 40 seconds, Colton Neal, 2026-09-16. These are customer timings from the ticket comments. No screenshot of the load time exists.

| Date | Customer timing |
| --- | --- |
| 2026-08-12 | 30 to 45 s, three users |
| 2026-09-02 | 30 to 40 s |
| 2026-09-16 | 35 to 40 s |

## 2. Findings

1. ENG-7168 https://trebuco.atlassian.net/browse/ENG-7168 shipped on 2026-08-27. **The customer timings did not change across that release.**
2. I read the Incident flags in production on 2026-09-08. The two AdHoc flags and `EnableScreenLabelCaching` resolve `True`. `EnableBlobAppendLogging` resolves `False`. Detail and ruled out items are in my internal note of 2026-09-08 on this ticket.
3. Matt, Teams, 2026-09-24: "there is something odd going on for Tailored brands on that. I was in thier site trying to investigate but was not able to get to the bottom of it yet"
4. Precedent, not tested on 209: Chris Rippingale noted on ENG-7168 on 2026-08-14 that tenant 209 had a p50 of 78.8 s on AdHoc requests, higher than other tenants, and left a tenant specific problem as an open branch.

## 3. Troubleshooting and limits of support access

**AI use.** Claude consolidated the ticket history, cross read ENG-7168 and ENG-6680 https://trebuco.atlassian.net/browse/ENG-6680, and flagged a tenant specific problem on 209 as the likely open branch. I checked the flags in production myself, the ENG-7168 release in Jira, and the customer timings against the release date. My reading is that the remaining time sits outside screen label caching and the AdHoc flags on this tenant. Could someone with Profiler access evaluate this and share your thoughts?

**Conversations outside this ticket.** Matt Kamminga on Teams, 2026-09-24, quoted above. No other calls or channels since my note of 2026-09-08.

**What support cannot see.** Application Insights Profiler traces for tenant 209. Support has not timed the transition from a Tailored Brands session. Every timing above comes from the customer.

## 4. Open questions

1. Could someone look at Profiler traces for tenant 209 on the Secure to Incident transition?
2. What is the intended value of `Feature.Incident.EnableBlobAppendLogging` on 209?
3. Who could own this ticket while Matt is out?

Related: ENG-7168 https://trebuco.atlassian.net/browse/ENG-7168, ENG-6680 https://trebuco.atlassian.net/browse/ENG-6680.
