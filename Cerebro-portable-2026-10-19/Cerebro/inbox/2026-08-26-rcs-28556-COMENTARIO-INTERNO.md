# INTERNAL NOTE. NOT FOR CUSTOMER

## 1. Correction

Support told this customer the blocks were a platform migration side effect, with user session and authentication data reconciling across systems. That statement is wrong. A Cloudflare edge block rejects the request on source IP before it reaches the application, so it never touches the session layer. The customer received that explanation on RCS-28175 on 2026-08-05, then received a second claim on 2026-08-11 that root cause was identified and a hotfix implemented. Joe Austin reopened the same day with "This is not resolved." No change record supports either claim. Do not repeat this explanation on any Vitamin Shoppe ticket.

## 2. Handoff

```
Ticket:   RCS-28556
Client:   Vitamin Shoppe, client 433, Incident LPMS
Ray ID:   a304809aba495425
Client IP: 136.226.130.207
Time:     2026-08-24 16:09 EDT
Host:     apps.apprissretail.com
Type:     Block. Not a timeout.
```

## 3. Evidence read from the attachments

Two full page screenshots landed on this ticket. They carry the data the three earlier Vitamin Shoppe tickets never produced.

| Field | Value |
|---|---|
| Affected user | Michael Holmstrom |
| Request path | `https://apps.apprissretail.com/vitaminshoppe/signin?url=/vitaminshoppe/nettrack/systemselect.aspx` |
| Page title | `Attention Required! \| Cloudflare` |
| Page body | `Sorry, you have been blocked` / `You are unable to access apprissretail.com` |
| Cloudflare Ray ID | `a304809aba495425` |
| Client IP | `136.226.130.207` |
| Tenant slug in path | Present twice. Path segment and `url` parameter. |

## 4. Same case as RCS-28059, on the same Zscaler egress /24

**This is not a similar case. It is the same /24.**

| | RCS-28059 Ahold | RCS-28556 Vitamin Shoppe |
|---|---|---|
| Client IP in text | `136.226.130.120` | `136.226.130.207` |
| Ray ID | `a236838f99b0f80e` | `a304809aba495425` |
| Reported | 2026-07-30 14:54 EDT | 2026-08-24 16:09 EDT |
| Symptom | Intermittent block at sign in | Intermittent block at sign in |
| Country allow list applied | Canada allowed 2026-07-31 | **None. No WAF rule modified for client 433.** |
| Outcome | Customer confirmed sign in. Closed 2026-08-03. | Open, four tickets deep. |

ARIN RDAP on the block that holds both addresses:

```
name           ZSCALER-YTO3
handle         NET-136-226-130-0-1
range          136.226.130.0 to 136.226.130.255
parentHandle   NET-136-226-0-0-1   136.226.0.0/16   org ZSCAL   ZSCALER, INC.
registrant     Zscaler, Inc.
address        151 Front Street West, Toronto, ON M5J 2N1, Canada
```

YTO is Toronto. Both users exit through the same Zscaler node.

**RCS-28059 root cause is already established and documented:** the Cloudflare default block rejecting Zscaler traffic routed through Canada. The fix was a country allow list. Canada was allowed for ADUSA on 2026-07-31, the customer confirmed users could sign in, and the ticket closed 2026-08-03. Per tenant allow lists do not carry across tenants. Confirmed today: no CISS ticket exists for Vitamin Shoppe and no WAF rule has been modified for client 433.

## 5. The block page wording proves nothing. Read Security > Events

The paragraph users see about "a certain word or phrase, a SQL command or malformed data" is Cloudflare's fixed template text. It is not a per rule message. The `apps` perimeter runs default deny:

```
Default action = Block. Access is granted only when a request matches a Skip rule.
Skip rules must appear above the global block rule.
```

Every request that matches no Skip rule falls to the same global block rule and renders the same page with the same paragraph. Country blocks, IP blocks and managed content blocks are indistinguishable from that page. **Only Security > Events resolves which rule fired.** RCS-28059 shows that identical page, and its cause was a decision on request origin.

## 6. Ruled out. Do not repeat

| Hypothesis | Refutation |
|---|---|
| ENG-5664, client slug dropped on URL construction | Slug present twice in the request path. ENG-7176 sets the test itself: "A Ray ID with a valid slug present points at candidate 2. A missing slug in the request path points at candidate 1." |
| Account lockout | Reporter states the same user is blocked at his home office and while visiting stores, then clears with no action on either side. Lockout does not toggle with location. |
| Migration session and token reconciliation | Edge block on source IP. The request never reaches the session layer. |
| Store network or ISP outage | Corporate desk and store visits both affected. Symptom follows the workstation, not the site. |

ENG-5664 status today: Development Complete, assignee Matthew Kamminga, fixVersion `Secure August 2026 Release 2/2`, releaseDate 2026-08-27. It does not apply here.

## 7. What support cannot determine

Support has no Cloudflare console access. Infrastructure owns these four reads.

```
1. Search Ray ID a304809aba495425 in Security > Events.
2. Record the country Cloudflare assigned to 136.226.130.207 at request time.
3. Record the rule ID and rule name that produced the block.
4. Record the country list currently applied to the vitaminshoppe URLs.
```

Item 2 is the one that closes ENG-7176. RDAP places the /24 in Toronto. Zscaler's own registration remark states RDAP data must not be used for geolocation, so RDAP is indicative. The country Cloudflare used is authoritative.

## 8. Remediation. Customer chooses

| | Action | Owner | Note |
|---|---|---|---|
| **A** | Add the countries the customer confirms to `allow-countries` on the vitaminshoppe URLs | Appriss | Route as on RCS-28059. Chris Rippingale, 2026-07-31 14:32 EDT: "Matt raising PR to allow Canada and sending to InfoSec right now." CISS-21846 is the fallback route, closed in 54 minutes. |
| **B** | Pin Zscaler egress for `apps.apprissretail.com` to US nodes, or exclude the hostname from the tunnel | Vitamin Shoppe network team | No change to the Appriss perimeter. Keeps country scope under customer control. |

Scope by country, not by IP. Zscaler egress ranges change and an IP list breaks on the next rotation. The ARIT Cloudflare guide lists "Hardcode IPs in rules" under Do NOT.

Path A carries a prerequisite. Matthew Everett flagged it on RCS-27766 on 2026-08-19: opening a country applies to everyone connecting from there, so the request needs an approver at Vitamin Shoppe with authority for that scope. Ask for the country list first. RCS-28059 never needed an approver because April Valerio's network team supplied the list and the change went through on that.

## 9. Still open

| Item | State |
|---|---|
| Label on this ticket | **Missing. Add `Uni_Jul_26_WAFAccess`.** |
| Links to add | RCS-28059, ENG-7176, RCS-28289 |
| RCS-28289 | Under Customer Review, same mechanism, closes with the same change |
| ENG-7176 | Backlog, unassigned, Medium. The evidence it asked for is on this ticket. |
| RCS-27766 | Work in progress since 2026-07-10. Customer authorised closure 2026-08-24. |
| RCS-28032 | Carries `Uni_Jul_26_WAFAccess` and is the multi district LHUA case. **Remove the label.** |
| Process gap | No documented route to request a WAF or country rule change. Ahold went by arpfiles PR to InfoSec, JCrew went by CISS. Neither is written down. |

Actions taken: none in Cloudflare, none in arpfiles, none in CISS.
